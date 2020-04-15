.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. _ConfigurationSchedulersClustered:

Clustered Scheduler Configuration
=================================

This section describes configuration options related to clustered scheduling.
A clustered scheduler configuration is optional.  It is an advanced
configuration area and only necessary in specific circumstances.

Clustered scheduling helps to control the worst-case latencies in a
multiprocessor system (SMP).  The goal is to reduce the amount of shared state
in the system and thus prevention of lock contention.  Modern multiprocessor
systems tend to have several layers of data and instruction caches.  With
clustered scheduling it is possible to honour the cache topology of a system
and thus avoid expensive cache synchronization traffic.

We have clustered scheduling in case the set of processors of a system is
partitioned into non-empty pairwise-disjoint subsets.  These subsets are called
clusters.  Clusters with a cardinality of one are partitions.  Each cluster is
owned by exactly one scheduler.

In order to use clustered scheduling the application designer has to answer two
questions.

#. How is the set of processors partitioned into clusters?

#. Which scheduler algorithm is used for which cluster?

The schedulers are statically configured.

Configuration Step 1 - Scheduler Algorithms
-------------------------------------------

Firstly, the application must select which scheduling algorithms are available
with the following defines

- :ref:`CONFIGURE_SCHEDULER_EDF_SMP <CONFIGURE_SCHEDULER_EDF_SMP>`,

- :ref:`CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP <CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP>`,

- :ref:`CONFIGURE_SCHEDULER_PRIORITY_SMP <CONFIGURE_SCHEDULER_PRIORITY_SMP>`, and

- :ref:`CONFIGURE_SCHEDULER_SIMPLE_SMP <CONFIGURE_SCHEDULER_SIMPLE_SMP>`.

This is necessary to calculate the per-thread overhead introduced by the
scheduler algorithms.  After these definitions the configuration file must
``#include <rtems/scheduler.h>`` to have access to scheduler-specific
configuration macros.

It is possible to make more than one scheduler algorithm available to the
application.  For example a :ref:`Simple Priority SMP Scheduler
<SchedulerSMPPrioritySimple>` could be used in a partition for low latency
tasks in addition to an :ref:`EDF SMP Scheduler <SchedulerSMPEDF>` for a
general-purpose cluster.  Since the per-thread overhead depends on the
scheduler algorithm only the scheduler algorithms used by the application
should be configured.

Configuration Step 2 - Schedulers
---------------------------------

Each scheduler needs some data structures.  Use the following macros to create
the scheduler data structures for a particular scheduler identified in the
configuration by ``name``.

- ``RTEMS_SCHEDULER_EDF_SMP(name)``,

- ``RTEMS_SCHEDULER_PRIORITY_AFFINITY_SMP(name, prio_count)``,

- ``RTEMS_SCHEDULER_PRIORITY_SMP(name, prio_count)``, and

- ``RTEMS_SCHEDULER_SIMPLE_SMP(name)``.

The ``name`` parameter is used as part of a designator for scheduler-specific
data structures, so the usual C/C++ designator rules apply.  This ``name`` is
not the scheduler object name.  Additional parameters are scheduler-specific.

.. _ConfigurationSchedulerTable:

Configuration Step 3 - Scheduler Table
--------------------------------------

The schedulers are registered in the system via the scheduler table.  To
populate the scheduler table define ``CONFIGURE_SCHEDULER_TABLE_ENTRIES`` to a
list of the following scheduler table entry initializers

- ``RTEMS_SCHEDULER_TABLE_EDF_SMP(name, obj_name)``,

- ``RTEMS_SCHEDULER_TABLE_PRIORITY_AFFINITY_SMP(name, obj_name)``,

- ``RTEMS_SCHEDULER_TABLE_PRIORITY_SMP(name, obj_name)``, and

- ``RTEMS_SCHEDULER_TABLE_SIMPLE_SMP(name, obj_name)``.

The ``name`` parameter must correspond to the parameter defining the scheduler
data structures of configuration step 2.  The ``obj_name`` determines the
scheduler object name and can be used in :ref:`rtems_scheduler_ident()
<rtems_scheduler_ident>` to get the scheduler object identifier.  The scheduler
index is defined by the index of the scheduler table.  It is a configuration
error to add a scheduler multiple times to the scheduler table.

Configuration Step 4 - Processor to Scheduler Assignment
--------------------------------------------------------

The last step is to define which processor uses which scheduler.  For this
purpose a scheduler assignment table must be defined.  The entry count of this
table must be equal to the configured maximum processors
(:ref:`CONFIGURE_MAXIMUM_PROCESSORS <CONFIGURE_MAXIMUM_PROCESSORS>`).  A
processor assignment to a scheduler can be optional or mandatory.  The boot
processor must have a scheduler assigned.  In case the system needs more
mandatory processors than available then a fatal run-time error will occur.  To
specify the scheduler assignments define
``CONFIGURE_SCHEDULER_ASSIGNMENTS`` to a list of

- ``RTEMS_SCHEDULER_ASSIGN(scheduler_index, attr)`` and

- ``RTEMS_SCHEDULER_ASSIGN_NO_SCHEDULER``

macros.  The ``scheduler_index`` parameter must be a valid index into the
scheduler table defined by configuration step 3.  The ``attr`` parameter
defines the scheduler assignment attributes.  By default, a scheduler
assignment to a processor is optional.  For the scheduler assignment attribute
use one of the mutually exclusive variants

- ``RTEMS_SCHEDULER_ASSIGN_DEFAULT``,

- ``RTEMS_SCHEDULER_ASSIGN_PROCESSOR_MANDATORY``, and

- ``RTEMS_SCHEDULER_ASSIGN_PROCESSOR_OPTIONAL``.

It is possible to add/remove processors to/from schedulers at run-time, see
:ref:`rtems_scheduler_add_processor() <rtems_scheduler_add_processor>` and
:ref:`rtems_scheduler_remove_processor() <rtems_scheduler_remove_processor>`.

Configuration Example
---------------------

The following example shows a scheduler configuration for a hypothetical
product using two chip variants.  One variant has four processors which is used
for the normal product line and another provides eight processors for the
high-performance product line.  The first processor performs hard-real time
control of actuators and sensors.  The second processor is not used by RTEMS at
all and runs a Linux instance to provide a graphical user interface.  The
additional processors are used for a worker thread pool to perform data
processing operations.

The processors managed by RTEMS use two Deterministic Priority SMP schedulers
capable of dealing with 256 priority levels.  The scheduler with index zero has
the name ``"IO "``.  The scheduler with index one has the name ``"WORK"``.  The
scheduler assignments of the first, third and fourth processor are mandatory,
so the system must have at least four processors, otherwise a fatal run-time
error will occur during system startup.  The processor assignments for the
fifth up to the eighth processor are optional so that the same application can
be used for the normal and high-performance product lines.  The second
processor has no scheduler assigned and runs Linux.  A hypervisor will ensure
that the two systems cannot interfere in an undesirable way.

.. code-block:: c

    #define CONFIGURE_MAXIMUM_PROCESSORS 8
    #define CONFIGURE_MAXIMUM_PRIORITY 255

    /* Configuration Step 1 - Scheduler Algorithms */
    #define CONFIGURE_SCHEDULER_PRIORITY_SMP
    #include <rtems/scheduler.h>

    /* Configuration Step 2 - Schedulers */
    RTEMS_SCHEDULER_PRIORITY_SMP(io, CONFIGURE_MAXIMUM_PRIORITY + 1);
    RTEMS_SCHEDULER_PRIORITY_SMP(work, CONFIGURE_MAXIMUM_PRIORITY + 1);

    /* Configuration Step 3 - Scheduler Table */
    #define CONFIGURE_SCHEDULER_TABLE_ENTRIES \
      RTEMS_SCHEDULER_TABLE_PRIORITY_SMP( \
        io, \
         rtems_build_name('I', 'O', ' ', ' ') \
      ), \
      RTEMS_SCHEDULER_TABLE_PRIORITY_SMP( \
        work, \
        rtems_build_name('W', 'O', 'R', 'K') \
      )

    /* Configuration Step 4 - Processor to Scheduler Assignment */
    #define CONFIGURE_SCHEDULER_ASSIGNMENTS \
      RTEMS_SCHEDULER_ASSIGN(0, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_MANDATORY), \
      RTEMS_SCHEDULER_ASSIGN_NO_SCHEDULER, \
      RTEMS_SCHEDULER_ASSIGN(1, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_MANDATORY), \
      RTEMS_SCHEDULER_ASSIGN(1, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_MANDATORY), \
      RTEMS_SCHEDULER_ASSIGN(1, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_OPTIONAL), \
      RTEMS_SCHEDULER_ASSIGN(1, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_OPTIONAL), \
      RTEMS_SCHEDULER_ASSIGN(1, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_OPTIONAL), \
      RTEMS_SCHEDULER_ASSIGN(1, RTEMS_SCHEDULER_ASSIGN_PROCESSOR_OPTIONAL)

Configuration Errors
--------------------

In case one of the scheduler indices in ``CONFIGURE_SCHEDULER_ASSIGNMENTS``
is invalid a link-time error will occur with an undefined reference to
``RTEMS_SCHEDULER_INVALID_INDEX``.

Some fatal errors may occur in case of scheduler configuration inconsistencies
or a lack of processors on the system.  The fatal source is
``RTEMS_FATAL_SOURCE_SMP``.

- ``SMP_FATAL_BOOT_PROCESSOR_NOT_ASSIGNED_TO_SCHEDULER`` - the boot processor
  must have a scheduler assigned.

- ``SMP_FATAL_MANDATORY_PROCESSOR_NOT_PRESENT`` - there exists a mandatory
  processor beyond the range of physically or virtually available processors.
  The processor demand must be reduced for this system.

- ``SMP_FATAL_START_OF_MANDATORY_PROCESSOR_FAILED`` - the start of a mandatory
  processor failed during system initialization.  The system may not have this
  processor at all or it could be a problem with a boot loader for example.
  Check the ``CONFIGURE_SCHEDULER_ASSIGNMENTS`` definition.

- ``SMP_FATAL_MULTITASKING_START_ON_UNASSIGNED_PROCESSOR`` - it is not allowed
  to start multitasking on a processor with no scheduler assigned.
