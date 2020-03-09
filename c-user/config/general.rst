.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

General System Configuration
============================

This section defines the general system configuration options supported by
``<rtems/confdefs.h>``.

.. index:: CONFIGURE_DIRTY_MEMORY

.. _CONFIGURE_DIRTY_MEMORY:

CONFIGURE_DIRTY_MEMORY
----------------------

CONSTANT:
    ``CONFIGURE_DIRTY_MEMORY``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    By default, the memory used by the RTEMS Workspace and the C Program Heap
    is uninitialized memory.

DESCRIPTION:
    This macro indicates whether RTEMS should dirty the memory used by the
    RTEMS Workspace and the C Program Heap as part of its initialization.  If
    defined, the memory areas are dirtied with a ``0xCF`` byte pattern.
    Otherwise, they are not.

NOTES:
    Dirtying memory can add significantly to system boot time.  It may assist in
    finding code that incorrectly assumes the contents of free memory areas is
    cleared to zero during system initialization.  In case
    :ref:`CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY` is also defined, then the
    memory is first dirtied and then zeroed.

.. index:: CONFIGURE_EXTRA_TASK_STACKS
.. index:: memory for task tasks

.. _CONFIGURE_EXTRA_TASK_STACKS:

CONFIGURE_EXTRA_TASK_STACKS
---------------------------

CONSTANT:
    ``CONFIGURE_EXTRA_TASK_STACKS``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    This configuration parameter is set to the number of bytes the applications
    wishes to add to the task stack requirements calculated by
    ``<rtems/confdefs.h>``.

NOTES:
    This parameter is very important.  If the application creates tasks with
    stacks larger then the minimum, then that memory is NOT accounted for by
    ``<rtems/confdefs.h>``.

.. index:: CONFIGURE_INITIAL_EXTENSIONS

.. _CONFIGURE_INITIAL_EXTENSIONS:

CONFIGURE_INITIAL_EXTENSIONS
----------------------------

CONSTANT:
    ``CONFIGURE_INITIAL_EXTENSIONS``

DATA TYPE:
    List of user extension initializers (``rtems_extensions_table``).

RANGE:
    Undefined or a list of one or more user extensions.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    If ``CONFIGURE_INITIAL_EXTENSIONS`` is defined by the application, then
    this application specific set of initial extensions will be placed in the
    initial extension table.

NOTES:
    None.

.. index:: CONFIGURE_INTERRUPT_STACK_SIZE
.. index:: interrupt stack size

.. _CONFIGURE_INTERRUPT_STACK_SIZE:

CONFIGURE_INTERRUPT_STACK_SIZE
------------------------------

CONSTANT:
    ``CONFIGURE_INTERRUPT_STACK_SIZE``

DATA TYPE:
    Unsigned integer.

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is ``BSP_INTERRUPT_STACK_SIZE`` in case it is defined,
    otherwise the default value is ``CPU_STACK_MINIMUM_SIZE``.

DESCRIPTION:
    The ``CONFIGURE_INTERRUPT_STACK_SIZE`` configuration option defines the
    size of an interrupt stack in bytes.

NOTES:
    The interrupt stack size must be aligned according to
    ``CPU_INTERRUPT_STACK_ALIGNMENT``.

    There is one interrupt stack available for each configured processor
    (:ref:`CONFIGURE_MAXIMUM_PROCESSORS <CONFIGURE_MAXIMUM_PROCESSORS>`).  The
    interrupt stack areas are statically allocated in a special linker section
    (``.rtemsstack.interrupt``).  The placement of this linker section is
    BSP-specific.

    Some BSPs use the interrupt stack as the initialization stack which is used
    to perform the sequential system initialization before the multithreading
    is started.

    The interrupt stacks are covered by the :ref:`stack checker
    <CONFIGURE_STACK_CHECKER_ENABLED>`.  However, using a too small interrupt
    stack size may still result in undefined behaviour.

    In releases before RTEMS 5.1 the default value was
    :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE
    <CONFIGURE_MINIMUM_TASK_STACK_SIZE>` instead of ``CPU_STACK_MINIMUM_SIZE``.

.. index:: CONFIGURE_MAXIMUM_FILE_DESCRIPTORS
.. index:: maximum file descriptors

.. _CONFIGURE_MAXIMUM_FILE_DESCRIPTORS:

CONFIGURE_MAXIMUM_FILE_DESCRIPTORS
----------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_FILE_DESCRIPTORS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    If ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`` is defined, then the
    default value is 3, otherwise the default value is 0.  Three file
    descriptors allows RTEMS to support standard input, output, and error I/O
    streams on ``/dev/console``.

DESCRIPTION:
    This configuration parameter is set to the maximum number of file like
    objects that can be concurrently open.

NOTES:
    None.

.. index:: CONFIGURE_MAXIMUM_PRIORITY
.. index:: maximum priority
.. index:: number of priority levels

.. _CONFIGURE_MAXIMUM_PRIORITY:

CONFIGURE_MAXIMUM_PRIORITY
--------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PRIORITY``

DATA TYPE:
    Unsigned integer (``uint8_t``).

RANGE:
    Valid values for this configuration parameter must be one (1) less than
    than a power of two (2) between 4 and 256 inclusively.  In other words,
    valid values are 3, 7, 31, 63, 127, and 255.

DEFAULT VALUE:
    The default value is 255, because RTEMS must support 256 priority levels to
    be compliant with various standards. These priorities range from zero (0)
    to 255.

DESCRIPTION:
   For the schedulers

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

NOTES:
   The numerically greatest priority is the logically lowest priority in the
   system and will thus be used by the IDLE task.

   Priority zero (0) is reserved for internal use by RTEMS and is not available
   to applications.

   Reducing the number of priorities through this configuration option reduces
   the amount of memory allocated by the schedulers listed above.  These
   schedulers use a chain control structure per priority and this structure
   consists of three pointers.  On a 32-bit architecture, the allocated memory
   is 12 bytes * (``CONFIGURE_MAXIMUM_PRIORITY`` + 1), e.g. 3072 bytes for 256
   priority levels (default), 48 bytes for 4 priority levels
   (``CONFIGURE_MAXIMUM_PRIORITY == 3``).

.. index:: CONFIGURE_MAXIMUM_PROCESSORS

.. _CONFIGURE_MAXIMUM_PROCESSORS:

CONFIGURE_MAXIMUM_PROCESSORS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PROCESSORS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 1.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_PROCESSORS`` must be set to the maximum number of
    processors an application intends to use.  The number of actually available
    processors depends on the hardware and may be less.  It is recommended to
    use the smallest value suitable for the application in order to save
    memory.  Each processor needs an idle thread and interrupt stack for
    example.

NOTES:
    If there are more processors available than configured, the rest will be
    ignored.  This configuration define is ignored in uniprocessor
    configurations.

.. index:: CONFIGURE_MAXIMUM_THREAD_NAME_SIZE
.. index:: maximum thread name size

.. _CONFIGURE_MAXIMUM_THREAD_NAME_SIZE:

CONFIGURE_MAXIMUM_THREAD_NAME_SIZE
----------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_THREAD_NAME_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    No restrictions.

DEFAULT VALUE:
    The default value is 16.  This value was chosen for Linux compatibility,
    see
    `PTHREAD_SETNAME_NP(3) <http://man7.org/linux/man-pages/man3/pthread_setname_np.3.html>`_.

DESCRIPTION:
   This configuration parameter specifies the maximum thread name size
   including the terminating `NUL` character.

NOTE:
   The size of the thread control block is increased by the maximum thread name
   size.  This configuration option is available since RTEMS 5.1.

.. index:: CONFIGURE_MEMORY_OVERHEAD

.. _CONFIGURE_MEMORY_OVERHEAD:

CONFIGURE_MEMORY_OVERHEAD
-------------------------

CONSTANT:
    ``CONFIGURE_MEMORY_OVERHEAD``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    This parameter is set to the number of kilobytes the application wishes to
    add to the requirements calculated by ``<rtems/confdefs.h>``.

NOTES:
    This configuration parameter should only be used when it is suspected that
    a bug in ``<rtems/confdefs.h>`` has resulted in an underestimation.
    Typically the memory allocation will be too low when an application does
    not account for all message queue buffers or task stacks.

.. index:: CONFIGURE_MICROSECONDS_PER_TICK
.. index:: tick quantum

.. _CONFIGURE_MICROSECONDS_PER_TICK:

CONFIGURE_MICROSECONDS_PER_TICK
-------------------------------

CONSTANT:
    ``CONFIGURE_MICROSECONDS_PER_TICK``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    This is not defined by default. When not defined, the clock tick quantum is
    configured to be 10,000 microseconds which is ten (10) milliseconds.

DESCRIPTION:
    This constant is  used to specify the length of time between clock ticks.

    When the clock tick quantum value is too low, the system will spend so much
    time processing clock ticks that it does not have processing time available
    to perform application work. In this case, the system will become
    unresponsive.

    The lowest practical time quantum varies widely based upon the speed of the
    target hardware and the architectural overhead associated with
    interrupts. In general terms, you do not want to configure it lower than is
    needed for the application.

    The clock tick quantum should be selected such that it all blocking and
    delay times in the application are evenly divisible by it. Otherwise,
    rounding errors will be introduced which may negatively impact the
    application.

NOTES:
    This configuration parameter has no impact if the Clock Tick Device driver
    is not configured.

    There may be BSP specific limits on the resolution or maximum value of a
    clock tick quantum.

.. index:: CONFIGURE_MINIMUM_TASK_STACK_SIZE
.. index:: minimum task stack size

.. _CONFIGURE_MINIMUM_TASK_STACK_SIZE:

CONFIGURE_MINIMUM_TASK_STACK_SIZE
---------------------------------

CONSTANT:
    ``CONFIGURE_MINIMUM_TASK_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is architecture-specific.

DESCRIPTION:
    This configuration parameter defines the minimum stack size in bytes for
    every user task or thread in the system.

NOTES:
    Adjusting this parameter should be done with caution.  Examining the actual
    stack usage using the stack checker usage reporting facility is recommended
    (see also :ref:`CONFIGURE_STACK_CHECKER_ENABLED <CONFIGURE_STACK_CHECKER_ENABLED>`).

    This parameter can be used to lower the minimum from that recommended. This
    can be used in low memory systems to reduce memory consumption for
    stacks. However, this must be done with caution as it could increase the
    possibility of a blown task stack.

    This parameter can be used to increase the minimum from that
    recommended. This can be used in higher memory systems to reduce the risk
    of stack overflow without performing analysis on actual consumption.

    By default, this configuration parameter defines also the minimum stack
    size of POSIX threads.  This can be changed with the
    :ref:`CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE <CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE>`
    configuration option.

    In releases before RTEMS 5.1 the ``CONFIGURE_MINIMUM_TASK_STACK_SIZE`` was
    used to define the default value of :ref:`CONFIGURE_INTERRUPT_STACK_SIZE
    <CONFIGURE_INTERRUPT_STACK_SIZE>`.

.. index:: CONFIGURE_STACK_CHECKER_ENABLED

.. _CONFIGURE_STACK_CHECKER_ENABLED:

CONFIGURE_STACK_CHECKER_ENABLED
-------------------------------

CONSTANT:
    ``CONFIGURE_STACK_CHECKER_ENABLED``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default, and thus stack checking is disabled.

DESCRIPTION:
    This configuration parameter is defined when the application wishes to
    enable run-time stack bounds checking.

NOTES:
    In 4.9 and older, this configuration parameter was named ``STACK_CHECKER_ON``.

    This increases the time required to create tasks as well as adding overhead
    to each context switch.

.. index:: CONFIGURE_TICKS_PER_TIMESLICE
.. index:: ticks per timeslice

.. _CONFIGURE_TICKS_PER_TIMESLICE:

CONFIGURE_TICKS_PER_TIMESLICE
-----------------------------

CONSTANT:
    ``CONFIGURE_TICKS_PER_TIMESLICE``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 50.

DESCRIPTION:
    This configuration parameter specifies the length of the timeslice quantum
    in ticks for each task.

NOTES:
    This configuration parameter has no impact if the Clock Tick Device driver
    is not configured.

.. index:: CONFIGURE_UNIFIED_WORK_AREAS
.. index:: unified work areas
.. index:: separate work areas
.. index:: RTEMS Workspace
.. index:: C Program Heap

.. _CONFIGURE_UNIFIED_WORK_AREAS:

CONFIGURE_UNIFIED_WORK_AREAS
----------------------------

CONSTANT:
    ``CONFIGURE_UNIFIED_WORK_AREAS``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default, which specifies that the C Program Heap and
    the RTEMS Workspace will be separate.

DESCRIPTION:
    When defined, the C Program Heap and the RTEMS Workspace will be one pool
    of memory.

    When not defined, there will be separate memory pools for the RTEMS
    Workspace and C Program Heap.

NOTES:
    Having separate pools does have some advantages in the event a task blows a
    stack or writes outside its memory area. However, in low memory systems the
    overhead of the two pools plus the potential for unused memory in either
    pool is very undesirable.

    In high memory environments, this is desirable when you want to use the
    RTEMS "unlimited" objects option.  You will be able to create objects until
    you run out of all available memory rather then just until you run out of
    RTEMS Workspace.

.. _CONFIGURE_UNLIMITED_ALLOCATION_SIZE:

CONFIGURE_UNLIMITED_ALLOCATION_SIZE
-----------------------------------

CONSTANT:
    ``CONFIGURE_UNLIMITED_ALLOCATION_SIZE``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    If not defined and ``CONFIGURE_UNLIMITED_OBJECTS`` is defined, the default
    value is eight (8).

DESCRIPTION:
    ``CONFIGURE_UNLIMITED_ALLOCATION_SIZE`` provides an allocation size to use
    for ``rtems_resource_unlimited`` when using
    ``CONFIGURE_UNLIMITED_OBJECTS``.

NOTES:
    By allowing users to declare all resources as being unlimited the user can
    avoid identifying and limiting the resources
    used. ``CONFIGURE_UNLIMITED_OBJECTS`` does not support varying the
    allocation sizes for different objects; users who want that much control
    can define the ``rtems_resource_unlimited`` macros themselves.

.. index:: CONFIGURE_UNLIMITED_OBJECTS

.. _CONFIGURE_UNLIMITED_OBJECTS:

CONFIGURE_UNLIMITED_OBJECTS
---------------------------

CONSTANT:
    ``CONFIGURE_UNLIMITED_OBJECTS``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_UNLIMITED_OBJECTS`` enables ``rtems_resource_unlimited`` mode
    for Classic API and POSIX API objects that do not already have a specific
    maximum limit defined.

NOTES:
    When using unlimited objects, it is common practice to also specify
    ``CONFIGURE_UNIFIED_WORK_AREAS`` so the system operates with a single pool
    of memory for both RTEMS and application memory allocations.

.. index:: CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION

.. _CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION:

CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION
---------------------------------------

CONSTANT:
    ``CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default, and thus the system initialization is
    quiet.

DESCRIPTION:
    This configuration option enables to print some information during system
    initialization.

NOTES:
    You may use this feature to debug system initialization issues.  The
    printk() function is used to print the information.

.. index:: CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY
.. index:: clear C Program Heap
.. index:: clear RTEMS Workspace
.. index:: zero C Program Heap
.. index:: zero RTEMS Workspace

.. _CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY:

CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY
--------------------------------------

CONSTANT:
    ``CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.  The default is *NOT* to zero out the RTEMS
    Workspace or C Program Heap.

DESCRIPTION:
    This macro indicates whether RTEMS should zero the RTEMS Workspace and C
    Program Heap as part of its initialization.  If defined, the memory regions
    are zeroed.  Otherwise, they are not.

NOTES:
    Zeroing memory can add significantly to system boot time. It is not
    necessary for RTEMS but is often assumed by support libraries.  In case
    :ref:`CONFIGURE_DIRTY_MEMORY` is also defined, then the memory is first
    dirtied and then zeroed.
