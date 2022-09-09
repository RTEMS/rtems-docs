.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012 Gedare Bloom
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Default Value Selection Philosophy
==================================

The user should be aware that the defaults are intentionally set as low as
possible.  By default, no application resources are configured.  The
``<rtems/confdefs.h>`` file ensures that at least one application task or
thread is configured and that at least one of the initialization task/thread
tables is configured.

.. _Sizing the RTEMS Workspace:

Sizing the RTEMS Workspace
==========================

The RTEMS Workspace is a user-specified block of memory reserved for use by
RTEMS.  The application should NOT modify this memory.  This area consists
primarily of the RTEMS data structures whose exact size depends upon the values
specified in the Configuration Table.  In addition, task stacks and floating
point context areas are dynamically allocated from the RTEMS Workspace.

The ``<rtems/confdefs.h>`` mechanism calculates the size of the RTEMS Workspace
automatically.  It assumes that all tasks are floating point and that all will
be allocated the minimum stack space.  This calculation includes the amount of
memory that will be allocated for internal use by RTEMS. The automatic
calculation may underestimate the workspace size truly needed by the
application, in which case one can use the ``CONFIGURE_MEMORY_OVERHEAD`` macro
to add a value to the estimate. See :ref:`Specify Memory Overhead` for more
details.

The memory area for the RTEMS Workspace is determined by the BSP.  In case the
RTEMS Workspace is too large for the available memory, then a fatal run-time
error occurs and the system terminates.

The file ``<rtems/confdefs.h>`` will calculate the value of the
``work_space_size`` parameter of the Configuration Table. There are many
parameters the application developer can specify to help ``<rtems/confdefs.h>``
in its calculations.  Correctly specifying the application requirements via
parameters such as ``CONFIGURE_EXTRA_TASK_STACKS`` and
``CONFIGURE_MAXIMUM_TASKS`` is critical for production software.

For each class of objects, the allocation can operate in one of two ways.  The
default way has an ceiling on the maximum number of object instances which can
concurrently exist in the system. Memory for all instances of that object class
is reserved at system initialization.  The second way allocates memory for an
initial number of objects and increases the current allocation by a fixed
increment when required. Both ways allocate space from inside the RTEMS
Workspace.

See :ref:`ConfigUnlimitedObjects` for more details about the second way, which
allows for dynamic allocation of objects and therefore does not provide
determinism.  This mode is useful mostly for when the number of objects cannot
be determined ahead of time or when porting software for which you do not know
the object requirements.

The space needed for stacks and for RTEMS objects will vary from one version of
RTEMS and from one target processor to another.  Therefore it is safest to use
``<rtems/confdefs.h>`` and specify your application's requirements in terms of
the numbers of objects and multiples of ``RTEMS_MINIMUM_STACK_SIZE``, as far as
is possible. The automatic estimates of space required will in general change
when:

- a configuration parameter is changed,

- task or interrupt stack sizes change,

- the floating point attribute of a task changes,

- task floating point attribute is altered,

- RTEMS is upgraded, or

- the target processor is changed.

Failure to provide enough space in the RTEMS Workspace may result in fatal
run-time errors terminating the system.

Potential Issues with RTEMS Workspace Size Estimation
=====================================================

The ``<rtems/confdefs.h>`` file estimates the amount of memory required for the
RTEMS Workspace.  This estimate is only as accurate as the information given to
``<rtems/confdefs.h>`` and may be either too high or too low for a variety of
reasons.  Some of the reasons that ``<rtems/confdefs.h>`` may reserve too much
memory for RTEMS are:

- All tasks/threads are assumed to be floating point.

Conversely, there are many more reasons that the resource estimate could be too
low:

- Task/thread stacks greater than minimum size must be accounted for explicitly
  by developer.

- Memory for messages is not included.

- Device driver requirements are not included.

- Network stack requirements are not included.

- Requirements for add-on libraries are not included.

In general, ``<rtems/confdefs.h>`` is very accurate when given enough
information.  However, it is quite easy to use a library and forget to account
for its resources.

Configuration Example
=====================

In the following example, the configuration information for a system with a
single message queue, four (4) tasks, and a timeslice of fifty (50)
milliseconds is as follows:

.. code-block:: c

    #include <bsp.h>
    #define CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER
    #define CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
    #define CONFIGURE_MICROSECONDS_PER_TICK   1000 /* 1 millisecond */
    #define CONFIGURE_TICKS_PER_TIMESLICE       50 /* 50 milliseconds */
    #define CONFIGURE_RTEMS_INIT_TASKS_TABLE
    #define CONFIGURE_MAXIMUM_TASKS 4
    #define CONFIGURE_MAXIMUM_MESSAGE_QUEUES 1
    #define CONFIGURE_MESSAGE_BUFFER_MEMORY \
               CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE(20, sizeof(struct USER_MESSAGE))
    #define CONFIGURE_INIT
    #include <rtems/confdefs.h>

In this example, only a few configuration parameters are specified. The impact
of these are as follows:

- The example specified ``CONFIGURE_RTEMS_INIT_TASK_TABLE`` but did not specify
  any additional parameters. This results in a configuration of an application
  which will begin execution of a single initialization task named ``Init``
  which is non-preemptible and at priority one (1).

- By specifying ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``, this application
  is configured to have a clock tick device driver. Without a clock tick device
  driver, RTEMS has no way to know that time is passing and will be unable to
  support delays and wall time. Further configuration details about time are
  provided. Per ``CONFIGURE_MICROSECONDS_PER_TICK`` and
  ``CONFIGURE_TICKS_PER_TIMESLICE``, the user specified they wanted a clock
  tick to occur each millisecond, and that the length of a timeslice would be
  fifty (50) milliseconds.

- By specifying ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``, the application
  will include a console device driver. Although the console device driver may
  support a combination of multiple serial ports and display and keyboard
  combinations, it is only required to provide a single device named
  ``/dev/console``. This device will be used for Standard Input, Output and
  Error I/O Streams. Thus when ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``
  is specified, implicitly three (3) file descriptors are reserved for the
  Standard I/O Streams and those file descriptors are associated with
  ``/dev/console`` during initialization. All console devices are expected to
  support the POSIX*termios* interface.

- The example above specifies via ``CONFIGURE_MAXIMUM_TASKS`` that the
  application requires a maximum of four (4) simultaneously existing Classic
  API tasks. Similarly, by specifying ``CONFIGURE_MAXIMUM_MESSAGE_QUEUES``,
  there may be a maximum of only one (1) concurrently existent Classic API
  message queues.

- The most surprising configuration parameter in this example is the use of
  ``CONFIGURE_MESSAGE_BUFFER_MEMORY``. Message buffer memory is allocated from
  the RTEMS Workspace and must be accounted for. In this example, the single
  message queue will have up to twenty (20) messages of type ``struct
  USER_MESSAGE``.

- The ``CONFIGURE_INIT`` constant must be defined in order to make
  ``<rtems/confdefs.h>`` instantiate the configuration data structures.  This
  can only be defined in one source file per application that includes
  ``<rtems/confdefs.h>`` or the symbol table will be instantiated multiple
  times and linking errors produced.

This example illustrates that parameters have default values. Among other
things, the application implicitly used the following defaults:

- All unspecified types of communications and synchronization objects in the
  Classic and POSIX Threads API have maximums of zero (0).

- The filesystem will be the default filesystem which is the In-Memory File
  System (IMFS).

- The application will have the default number of priority levels.

- The minimum task stack size will be that recommended by RTEMS for the target
  architecture.

.. _ConfigUnlimitedObjects:

Unlimited Objects
=================

In real-time embedded systems the RAM is normally a limited, critical resource
and dynamic allocation is avoided as much as possible to ensure predictable,
deterministic execution times. For such cases, see :ref:`Sizing the RTEMS
Workspace` for an overview of how to tune the size of the workspace.
Frequently when users are porting software to RTEMS the precise resource
requirements of the software is unknown. In these situations users do not need
to control the size of the workspace very tightly because they just want to get
the new software to run; later they can tune the workspace size as needed.

The following object classes in the Classic API can be configured in unlimited
mode:

- Barriers

- Message Queues

- Partitions

- Periods

- Ports

- Regions

- Semaphores

- Tasks

- Timers

Additionally, the following object classes from the POSIX API can be configured
in unlimited mode:

- Keys -- :c:func:`pthread_key_create`

- Key Value Pairs -- :c:func:`pthread_setspecific`

- Message Queues -- :c:func:`mq_open`

- Named Semaphores -- :c:func:`sem_open`

- Shared Memory -- :c:func:`shm_open`

- Threads -- :c:func:`pthread_create`

- Timers -- :c:func:`timer_create`

.. warning::

    The following object classes can *not* be configured in unlimited mode:

    - Drivers

    - File Descriptors

    - POSIX Queued Signals

    - User Extensions

Due to the memory requirements of unlimited objects it is strongly recommended
to use them only in combination with the unified work areas. See :ref:`Separate
or Unified Work Areas` for more information on unified work areas.

The following example demonstrates how the two simple configuration defines for
unlimited objects and unified works areas can replace many seperate
configuration defines for supported object classes:

.. code-block:: c

    #define CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
    #define CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER
    #define CONFIGURE_UNIFIED_WORK_AREAS
    #define CONFIGURE_UNLIMITED_OBJECTS
    #define CONFIGURE_RTEMS_INIT_TASKS_TABLE
    #define CONFIGURE_INIT
    #include <rtems/confdefs.h>

Users are cautioned that using unlimited objects is not recommended for
production software unless the dynamic growth is absolutely required. It is
generally considered a safer embedded systems programming practice to know the
system limits rather than experience an out of memory error at an arbitrary and
largely unpredictable time in the field.

.. index:: rtems_resource_unlimited

.. _ConfigUnlimitedObjectsClass:

Unlimited Objects by Class
--------------------------

When the number of objects is not known ahead of time, RTEMS provides an
auto-extending mode that can be enabled individually for each object type by
using the macro ``rtems_resource_unlimited``. This takes a value as a
parameter, and is used to set the object maximum number field in an API
Configuration table. The value is an allocation unit size. When RTEMS is
required to grow the object table it is grown by this size. The kernel will
return the object memory back to the RTEMS Workspace when an object is
destroyed. The kernel will only return an allocated block of objects to the
RTEMS Workspace if at least half the allocation size of free objects remain
allocated. RTEMS always keeps one allocation block of objects allocated. Here
is an example of using ``rtems_resource_unlimited``:

.. code-block:: c

    #define CONFIGURE_MAXIMUM_TASKS rtems_resource_unlimited(5)

.. index:: rtems_resource_is_unlimited
.. index:: rtems_resource_maximum_per_allocation

Object maximum specifications can be evaluated with the
``rtems_resource_is_unlimited`` and``rtems_resource_maximum_per_allocation``
macros.

.. _ConfigUnlimitedObjectsDefault:

Unlimited Objects by Default
----------------------------

To ease the burden of developers who are porting new software RTEMS also
provides the capability to make all object classes listed above operate in
unlimited mode in a simple manner. The application developer is only
responsible for enabling unlimited objects
(:ref:`CONFIGURE_UNLIMITED_OBJECTS`) and specifying the allocation size
(:ref:`CONFIGURE_UNLIMITED_ALLOCATION_SIZE`).

.. code-block:: c

    #define CONFIGURE_UNLIMITED_OBJECTS
    #define CONFIGURE_UNLIMITED_ALLOCATION_SIZE 5
