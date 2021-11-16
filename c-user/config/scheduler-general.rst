.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 2010 Gedare Bloom
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. Generated from spec:/acfg/if/group-schedgeneral

General Scheduler Configuration
===============================

This section describes configuration options related to selecting a
scheduling algorithm for an application.  A scheduler configuration is optional
and only necessary in very specific circumstances.  A normal application
configuration does not need any of the configuration options described in this
section.

By default, the :ref:`SchedulerPriority`
algorithm is used in uniprocessor configurations.  In case SMP is enabled and
the configured maximum processors
(:ref:`CONFIGURE_MAXIMUM_PROCESSORS`) is greater
than one, then the
:ref:`SchedulerSMPEDF`
is selected as the default scheduler algorithm.

For the schedulers provided by RTEMS (see :ref:`RTEMSAPIClassicScheduler`), the
configuration is straightforward.  All that is required is to define the
configuration option which specifies which scheduler you want for in your
application.

The pluggable scheduler interface also enables the user to provide their own
scheduling algorithm.  If you choose to do this, you must define multiple
configuration option.

.. Generated from spec:/acfg/if/cbs-max-servers

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_CBS_MAXIMUM_SERVERS

.. _CONFIGURE_CBS_MAXIMUM_SERVERS:

CONFIGURE_CBS_MAXIMUM_SERVERS
-----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_CBS_MAXIMUM_SERVERS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is :ref:`CONFIGURE_MAXIMUM_TASKS`.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number Constant
Bandwidth Servers that can be concurrently active.

.. rubric:: NOTES:

This configuration option is only evaluated if the configuration option
:ref:`CONFIGURE_SCHEDULER_CBS` is defined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

.. Generated from spec:/acfg/if/max-priority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_PRIORITY
.. index:: maximum priority
.. index:: number of priority levels

.. _CONFIGURE_MAXIMUM_PRIORITY:

CONFIGURE_MAXIMUM_PRIORITY
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 255.

.. rubric:: DESCRIPTION:

For the following schedulers

* :ref:`SchedulerPriority`, which is the default in uniprocessor
  configurations and can be configured through the
  :ref:`CONFIGURE_SCHEDULER_PRIORITY` configuration option,

* :ref:`SchedulerSMPPriority` which can be configured through the
  :ref:`CONFIGURE_SCHEDULER_PRIORITY_SMP` configuration option, and

* :ref:`SchedulerSMPPriorityAffinity` which can be configured through the
  :ref:`CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP` configuration option

this configuration option specifies the maximum numeric priority of any task
for these schedulers and one less that the number of priority levels for
these schedulers.  For all other schedulers provided by RTEMS, this
configuration option has no effect.

.. rubric:: NOTES:

The numerically greatest priority is the logically lowest priority in the
system and will thus be used by the IDLE task.

Priority zero is reserved for internal use by RTEMS and is not available to
applications.

Reducing the number of priorities through this configuration option reduces
the amount of memory allocated by the schedulers listed above.  These
schedulers use a chain control structure per priority and this structure
consists of three pointers.  On a 32-bit architecture, the allocated memory
is 12 bytes * (``CONFIGURE_MAXIMUM_PRIORITY`` + 1), e.g. 3072 bytes for 256
priority levels (default), 48 bytes for 4 priority levels
(``CONFIGURE_MAXIMUM_PRIORITY == 3``).

The default value is 255, because RTEMS shall support 256 priority levels to
be compliant with various standards.  These priorities range from 0 to 255.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be equal to 3, 7, 31, 63, 127, or
255.

.. Generated from spec:/acfg/if/scheduler-assignments

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_ASSIGNMENTS

.. _CONFIGURE_SCHEDULER_ASSIGNMENTS:

CONFIGURE_SCHEDULER_ASSIGNMENTS
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_ASSIGNMENTS``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value of this configuration option is computed so that the
default scheduler is assigned to each configured processor (up to 32).

.. rubric:: DESCRIPTION:

The value of this configuration option is used to initialize the initial
scheduler to processor assignments.

.. rubric:: NOTES:

This configuration option is only evaluated in SMP configurations.

This is an advanced configuration option, see
:ref:`ConfigurationSchedulersClustered`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be a list of the following
  macros:

  * ``RTEMS_SCHEDULER_ASSIGN( processor_index, attributes )``

  * ``RTEMS_SCHEDULER_ASSIGN_NO_SCHEDULER``

* The value of the configuration option shall be a list of exactly
  :ref:`CONFIGURE_MAXIMUM_PROCESSORS` elements.

.. Generated from spec:/acfg/if/scheduler-cbs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_CBS

.. _CONFIGURE_SCHEDULER_CBS:

CONFIGURE_SCHEDULER_CBS
-----------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_CBS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerCBS`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for exactly one processor.

.. Generated from spec:/acfg/if/scheduler-edf

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_EDF

.. _CONFIGURE_SCHEDULER_EDF:

CONFIGURE_SCHEDULER_EDF
-----------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_EDF``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerEDF`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for exactly one processor.

.. Generated from spec:/acfg/if/scheduler-edf-smp

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_EDF_SMP

.. _CONFIGURE_SCHEDULER_EDF_SMP:

CONFIGURE_SCHEDULER_EDF_SMP
---------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_EDF_SMP``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerSMPEDF`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

This scheduler algorithm is only available when RTEMS is built with SMP
support enabled.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for up to 32 processors.

This scheduler algorithm is the default in SMP configurations if
:ref:`CONFIGURE_MAXIMUM_PROCESSORS` is
greater than one.

.. Generated from spec:/acfg/if/scheduler-name

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_NAME

.. _CONFIGURE_SCHEDULER_NAME:

CONFIGURE_SCHEDULER_NAME
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_NAME``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is

* ``"MEDF"`` for the :ref:`SchedulerSMPEDF`,

* ``"MPA "`` for the :ref:`SchedulerSMPPriorityAffinity`,

* ``"MPD "`` for the :ref:`SchedulerSMPPriority`,

* ``"MPS "`` for the :ref:`SchedulerSMPPrioritySimple`,

* ``"UCBS"`` for the :ref:`SchedulerCBS`,

* ``"UEDF"`` for the :ref:`SchedulerEDF`,

* ``"UPD "`` for the :ref:`SchedulerPriority`, and

* ``"UPS "`` for the :ref:`SchedulerPrioritySimple`.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the name of the default
scheduler.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

Schedulers can be identified via :c:func:`rtems_scheduler_ident`.

Use :c:func:`rtems_build_name` to define the scheduler name.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be convertible to an integer of
type :c:type:`rtems_name`.

.. Generated from spec:/acfg/if/scheduler-priority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_PRIORITY

.. _CONFIGURE_SCHEDULER_PRIORITY:

CONFIGURE_SCHEDULER_PRIORITY
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerPriority`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for exactly one processor.

This scheduler algorithm is the default when
:ref:`CONFIGURE_MAXIMUM_PROCESSORS` is
exactly one.

The memory allocated for this scheduler depends on the
:ref:`CONFIGURE_MAXIMUM_PRIORITY` configuration option.

.. Generated from spec:/acfg/if/scheduler-priority-affinity-smp

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP

.. _CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP:

CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP
-----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerSMPPriorityAffinity`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

This scheduler algorithm is only available when RTEMS is built with SMP
support enabled.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for up to 32 processors.

The memory allocated for this scheduler depends on the
:ref:`CONFIGURE_MAXIMUM_PRIORITY` configuration option.

.. Generated from spec:/acfg/if/scheduler-priority-smp

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_PRIORITY_SMP

.. _CONFIGURE_SCHEDULER_PRIORITY_SMP:

CONFIGURE_SCHEDULER_PRIORITY_SMP
--------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_PRIORITY_SMP``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerSMPPriority`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

This scheduler algorithm is only available when RTEMS is built with SMP
support enabled.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for up to 32 processors.

The memory allocated for this scheduler depends on the
:ref:`CONFIGURE_MAXIMUM_PRIORITY` configuration option.

.. Generated from spec:/acfg/if/scheduler-simple

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_SIMPLE

.. _CONFIGURE_SCHEDULER_SIMPLE:

CONFIGURE_SCHEDULER_SIMPLE
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_SIMPLE``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerPrioritySimple`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for exactly one processor.

.. Generated from spec:/acfg/if/scheduler-simple-smp

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_SIMPLE_SMP

.. _CONFIGURE_SCHEDULER_SIMPLE_SMP:

CONFIGURE_SCHEDULER_SIMPLE_SMP
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_SIMPLE_SMP``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the
:ref:`SchedulerSMPPrioritySimple`
algorithm is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

This scheduler algorithm is only available when RTEMS is built with SMP
support enabled.

In case no explicit :ref:`ConfigurationSchedulersClustered`
is present, then it is used as the scheduler for up to 32 processors.

.. Generated from spec:/acfg/if/scheduler-strong-apa

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_STRONG_APA

.. _CONFIGURE_SCHEDULER_STRONG_APA:

CONFIGURE_SCHEDULER_STRONG_APA
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_STRONG_APA``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Strong APA algorithm
is made available to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

This scheduler algorithm is only available when RTEMS is built with SMP
support enabled.

This scheduler algorithm is not correctly implemented.  Do not use it.

.. Generated from spec:/acfg/if/scheduler-user

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SCHEDULER_USER

.. _CONFIGURE_SCHEDULER_USER:

CONFIGURE_SCHEDULER_USER
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SCHEDULER_USER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the user shall provide a
scheduler algorithm to the application.

.. rubric:: NOTES:

This scheduler configuration option is an advanced configuration option.
Think twice before you use it.

RTEMS allows the application to provide its own task/thread scheduling
algorithm. In order to do this, one shall define
``CONFIGURE_SCHEDULER_USER`` to indicate the application provides its own
scheduling algorithm. If ``CONFIGURE_SCHEDULER_USER`` is defined then the
following additional macros shall be defined:

* ``CONFIGURE_SCHEDULER`` shall be defined to a static definition of
  the scheduler data structures of the user scheduler.

* ``CONFIGURE_SCHEDULER_TABLE_ENTRIES`` shall be defined to a scheduler
  table entry initializer for the user scheduler.

* ``CONFIGURE_SCHEDULER_USER_PER_THREAD`` shall be defined to the type of
  the per-thread information of the user scheduler.

At this time, the mechanics and requirements for writing a new scheduler
are evolving and not fully documented.  It is recommended that you look at
the existing Deterministic Priority Scheduler in
``cpukit/score/src/schedulerpriority*.c`` for guidance.  For guidance on
the configuration macros, please examine ``cpukit/sapi/include/confdefs.h``
for how these are defined for the Deterministic Priority Scheduler.
