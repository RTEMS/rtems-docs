.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/acfg/if/group-general

General System Configuration
============================

This section describes general system configuration options.

.. Generated from spec:/acfg/if/dirty-memory

.. index:: CONFIGURE_DIRTY_MEMORY

.. _CONFIGURE_DIRTY_MEMORY:

CONFIGURE_DIRTY_MEMORY
----------------------

CONSTANT:
    ``CONFIGURE_DIRTY_MEMORY``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the memory areas used for
    the RTEMS Workspace and the C Program Heap are dirtied with a ``0xCF`` byte
    pattern during system initialization.

NOTES:
    Dirtying memory can add significantly to system initialization time.  It may
    assist in finding code that incorrectly assumes the contents of free memory
    areas is cleared to zero during system initialization.  In case
    :ref:`CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY` is also defined, then the
    memory is first dirtied and then zeroed.

    See also :ref:`CONFIGURE_MALLOC_DIRTY`.

.. Generated from spec:/acfg/if/disable-newlib-reentrancy

.. index:: CONFIGURE_DISABLE_NEWLIB_REENTRANCY

.. _CONFIGURE_DISABLE_NEWLIB_REENTRANCY:

CONFIGURE_DISABLE_NEWLIB_REENTRANCY
-----------------------------------

CONSTANT:
    ``CONFIGURE_DISABLE_NEWLIB_REENTRANCY``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the Newlib reentrancy
    support per thread is disabled and a global reentrancy structure is used.

NOTES:
    You can enable this option to reduce the size of the :term:`TCB`.  Use this
    option with care, since it can lead to race conditions and undefined system
    behaviour.  For example, :c:macro:`errno` is no longer a thread-local
    variable if this option is enabled.

.. Generated from spec:/acfg/if/executive-ram-size

.. index:: CONFIGURE_EXECUTIVE_RAM_SIZE

.. _CONFIGURE_EXECUTIVE_RAM_SIZE:

CONFIGURE_EXECUTIVE_RAM_SIZE
----------------------------

CONSTANT:
    ``CONFIGURE_EXECUTIVE_RAM_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    If this configuration option is undefined, then the RTEMS Workspace and task
    stack space size is calculated by ``<rtems/confdefs.h>`` based on the values
    configuration options.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to `UINTPTR_MAX <https://en.cppreference.com/w/c/types/integer>`_.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

DESCRIPTION:
    The value of this configuration option defines the RTEMS Workspace size in
    bytes.

NOTES:
    This is an advanced configuration option.  Use it only if you know exactly
    what you are doing.

.. Generated from spec:/acfg/if/extra-task-stacks

.. index:: CONFIGURE_EXTRA_TASK_STACKS
.. index:: memory for task tasks

.. _CONFIGURE_EXTRA_TASK_STACKS:

CONFIGURE_EXTRA_TASK_STACKS
---------------------------

CONSTANT:
    ``CONFIGURE_EXTRA_TASK_STACKS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be small enough so that the task
      stack space calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the number of bytes the
    applications wishes to add to the task stack requirements calculated by
    ``<rtems/confdefs.h>``.

NOTES:
    This parameter is very important.  If the application creates tasks with
    stacks larger then the minimum, then that memory is **not** accounted for by
    ``<rtems/confdefs.h>``.

.. Generated from spec:/acfg/if/initial-extensions

.. index:: CONFIGURE_INITIAL_EXTENSIONS

.. _CONFIGURE_INITIAL_EXTENSIONS:

CONFIGURE_INITIAL_EXTENSIONS
----------------------------

CONSTANT:
    ``CONFIGURE_INITIAL_EXTENSIONS``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is the empty list.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a list of initializers for
    structures of type :c:type:`rtems_extensions_table`.

DESCRIPTION:
    The value of this configuration option is used to initialize the table of
    initial user extensions.

NOTES:
    The value of this configuration option is placed before the entries of
    :ref:`BSP_INITIAL_EXTENSION` and after the entries of all other initial
    user extensions.

.. Generated from spec:/acfg/if/interrupt-stack-size

.. index:: CONFIGURE_INTERRUPT_STACK_SIZE
.. index:: interrupt stack size

.. _CONFIGURE_INTERRUPT_STACK_SIZE:

CONFIGURE_INTERRUPT_STACK_SIZE
------------------------------

CONSTANT:
    ``CONFIGURE_INTERRUPT_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is :ref:`BSP_INTERRUPT_STACK_SIZE` in case it is defined,
    otherwise the default value is :c:macro:`CPU_STACK_MINIMUM_SIZE`.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to a
      BSP-specific and application-specific minimum value.

    * It shall be small enough so that the
      interrupt stack area calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `size_t <https://en.cppreference.com/w/c/types/size_t>`_.

    * It shall be aligned according to
      :c:macro:`CPU_INTERRUPT_STACK_ALIGNMENT`.

DESCRIPTION:
    The value of this configuration option defines the size of an interrupt stack
    in bytes.

NOTES:
    There is one interrupt stack available for each configured processor
    (:ref:`CONFIGURE_MAXIMUM_PROCESSORS`).  The interrupt stack areas are
    statically allocated in a special linker section (``.rtemsstack.interrupt``).
    The placement of this linker section is BSP-specific.

    Some BSPs use the interrupt stack as the initialization stack which is used
    to perform the sequential system initialization before the multithreading
    is started.

    The interrupt stacks are covered by the stack checker, see
    :ref:`CONFIGURE_STACK_CHECKER_ENABLED`.  However, using a too small interrupt stack
    size may still result in undefined behaviour.

    In releases before RTEMS 5.1 the default value was
    :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE` instead of
    :c:macro:`CPU_STACK_MINIMUM_SIZE`.

.. Generated from spec:/acfg/if/malloc-dirty

.. index:: CONFIGURE_MALLOC_DIRTY

.. _CONFIGURE_MALLOC_DIRTY:

CONFIGURE_MALLOC_DIRTY
----------------------

CONSTANT:
    ``CONFIGURE_MALLOC_DIRTY``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then each memory area returned
    by C Program Heap allocator functions such as :c:func:`malloc` is dirtied
    with a ``0xCF`` byte pattern before it is handed over to the application.

NOTES:
    The dirtying performed by this option is carried out for each successful
    memory allocation from the C Program Heap in contrast to
    :ref:`CONFIGURE_DIRTY_MEMORY` which dirties the memory only once during the
    system initialization.

.. Generated from spec:/acfg/if/max-file-descriptors

.. index:: CONFIGURE_MAXIMUM_FILE_DESCRIPTORS
.. index:: maximum file descriptors

.. _CONFIGURE_MAXIMUM_FILE_DESCRIPTORS:

CONFIGURE_MAXIMUM_FILE_DESCRIPTORS
----------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_FILE_DESCRIPTORS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 3.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

DESCRIPTION:
    The value of this configuration option defines the maximum number of file
    like objects that can be concurrently open.

NOTES:
    The default value of three file descriptors allows RTEMS to support standard
    input, output, and error I/O streams on :file:`/dev/console`.

.. Generated from spec:/acfg/if/max-processors

.. index:: CONFIGURE_MAXIMUM_PROCESSORS

.. _CONFIGURE_MAXIMUM_PROCESSORS:

CONFIGURE_MAXIMUM_PROCESSORS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PROCESSORS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 1.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 1
    and less than or equal to :c:macro:`CPU_MAXIMUM_PROCESSORS`.

DESCRIPTION:
    The value of this configuration option defines the maximum number of
    processors an application intends to use.  The number of actually available
    processors depends on the hardware and may be less.  It is recommended to use
    the smallest value suitable for the application in order to save memory.
    Each processor needs an IDLE task stack and interrupt stack for example.

NOTES:
    If there are more processors available than configured, the rest will be
    ignored.

    This configuration option is only evaluated in SMP configurations (e.g. RTEMS
    was built with the ``--enable-smp`` build configuration option).  In all
    other configurations it has no effect.

.. Generated from spec:/acfg/if/max-thread-name-size

.. index:: CONFIGURE_MAXIMUM_THREAD_NAME_SIZE
.. index:: maximum thread name size

.. _CONFIGURE_MAXIMUM_THREAD_NAME_SIZE:

CONFIGURE_MAXIMUM_THREAD_NAME_SIZE
----------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_THREAD_NAME_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 16.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

DESCRIPTION:
    The value of this configuration option defines the maximum thread name size
    including the terminating ``NUL`` character.

NOTES:
    The default value was chosen for Linux compatibility, see
    `PTHREAD_SETNAME_NP(3) <http://man7.org/linux/man-pages/man3/pthread_setname_np.3.html>`_.

    The size of the thread control block is increased by the maximum thread name
    size.

    This configuration option is available since RTEMS 5.1.

.. Generated from spec:/acfg/if/memory-overhead

.. index:: CONFIGURE_MEMORY_OVERHEAD

.. _CONFIGURE_MEMORY_OVERHEAD:

CONFIGURE_MEMORY_OVERHEAD
-------------------------

CONSTANT:
    ``CONFIGURE_MEMORY_OVERHEAD``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It shall be small enough so that the
      RTEMS Workspace size calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the number of kilobytes the
    application wishes to add to the RTEMS Workspace size calculated by
    ``<rtems/confdefs.h>``.

NOTES:
    This configuration option should only be used when it is suspected that a bug
    in ``<rtems/confdefs.h>`` has resulted in an underestimation.  Typically the
    memory allocation will be too low when an application does not account for
    all message queue buffers or task stacks, see
    :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.

.. Generated from spec:/acfg/if/message-buffer-memory

.. index:: CONFIGURE_MESSAGE_BUFFER_MEMORY
.. index:: configure message queue buffer memory
.. index:: CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE
.. index:: memory for a single message queue's buffers

.. _CONFIGURE_MESSAGE_BUFFER_MEMORY:

CONFIGURE_MESSAGE_BUFFER_MEMORY
-------------------------------

CONSTANT:
    ``CONFIGURE_MESSAGE_BUFFER_MEMORY``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It shall be small enough so that the
      RTEMS Workspace size calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the number of bytes reserved
    for message queue buffers in the RTEMS Workspace.

NOTES:
    The configuration options :ref:`CONFIGURE_MAXIMUM_MESSAGE_QUEUES` and
    :ref:`CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES` define only how many message
    queues can be created by the application.  The memory for the message
    buffers is configured by this option.  For each message queue you have to
    reserve some memory for the message buffers.  The size depends on the
    maximum number of pending messages and the maximum size of the messages of
    a message queue.  Use the ``CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE()`` macro
    to specify the message buffer memory for each message queue and sum them up
    to define the value for ``CONFIGURE_MAXIMUM_MESSAGE_QUEUES``.

    The interface for the ``CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE()`` help
    macro is as follows:

    .. code-block:: c

        CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE( max_messages, max_msg_size )

    Where ``max_messages`` is the maximum number of pending messages and
    ``max_msg_size`` is the maximum size in bytes of the messages of the
    corresponding message queue.  Both parameters shall be compile time
    constants.  Not using this help macro (e.g. just using
    ``max_messages * max_msg_size``) may result in an underestimate of the
    RTEMS Workspace size.

    The following example illustrates how the
    ``CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE()`` help macro can be used to assist in
    calculating the message buffer memory required.  In this example, there are
    two message queues used in this application.  The first message queue has a
    maximum of 24 pending messages with the message structure defined by the
    type ``one_message_type``.  The other message queue has a maximum of 500
    pending messages with the message structure defined by the type
    ``other_message_type``.

    .. code-block:: c

        #define CONFIGURE_MESSAGE_BUFFER_MEMORY ( \
            CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE( \
              24, \
              sizeof( one_message_type ) \
            ) \
            + CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE( \
              500, \
              sizeof( other_message_type ) \
            ) \
          )

.. Generated from spec:/acfg/if/microseconds-per-tick

.. index:: CONFIGURE_MICROSECONDS_PER_TICK
.. index:: clock tick quantum
.. index:: tick quantum

.. _CONFIGURE_MICROSECONDS_PER_TICK:

CONFIGURE_MICROSECONDS_PER_TICK
-------------------------------

CONSTANT:
    ``CONFIGURE_MICROSECONDS_PER_TICK``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 10000.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to a Clock Driver specific value.

    * It shall be less than or equal to a Clock Driver specific value.

    * The resulting clock ticks per second should be an integer.

DESCRIPTION:
    The value of this configuration option defines the length of time in
    microseconds between clock ticks (clock tick quantum).

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
    This configuration option has no impact if the Clock Driver is not
    configured, see :ref:`CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`.

    There may be Clock Driver specific limits on the resolution or maximum value
    of a clock tick quantum.

.. Generated from spec:/acfg/if/min-task-stack-size

.. index:: CONFIGURE_MINIMUM_TASK_STACK_SIZE
.. index:: minimum task stack size

.. _CONFIGURE_MINIMUM_TASK_STACK_SIZE:

CONFIGURE_MINIMUM_TASK_STACK_SIZE
---------------------------------

CONSTANT:
    ``CONFIGURE_MINIMUM_TASK_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is :c:macro:`CPU_STACK_MINIMUM_SIZE`.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be small enough so that the task
      stack space calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

    * It shall be greater than or equal to a
      BSP-specific and application-specific minimum value.

DESCRIPTION:
    The value of this configuration option defines the minimum stack size in
    bytes for every user task or thread in the system.

NOTES:
    Adjusting this parameter should be done with caution.  Examining the actual
    stack usage using the stack checker usage reporting facility is recommended
    (see also :ref:`CONFIGURE_STACK_CHECKER_ENABLED`).

    This parameter can be used to lower the minimum from that recommended. This
    can be used in low memory systems to reduce memory consumption for
    stacks. However, this shall be done with caution as it could increase the
    possibility of a blown task stack.

    This parameter can be used to increase the minimum from that
    recommended. This can be used in higher memory systems to reduce the risk
    of stack overflow without performing analysis on actual consumption.

    By default, this configuration parameter defines also the minimum stack
    size of POSIX threads.  This can be changed with the
    :ref:`CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE`
    configuration option.

    In releases before RTEMS 5.1 the ``CONFIGURE_MINIMUM_TASK_STACK_SIZE`` was
    used to define the default value of :ref:`CONFIGURE_INTERRUPT_STACK_SIZE`.

.. Generated from spec:/acfg/if/stack-checker-enabled

.. index:: CONFIGURE_STACK_CHECKER_ENABLED

.. _CONFIGURE_STACK_CHECKER_ENABLED:

CONFIGURE_STACK_CHECKER_ENABLED
-------------------------------

CONSTANT:
    ``CONFIGURE_STACK_CHECKER_ENABLED``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the stack checker is
    enabled.

NOTES:
    The stack checker performs run-time stack bounds checking.  This increases
    the time required to create tasks as well as adding overhead to each context
    switch.

    In 4.9 and older, this configuration option was named ``STACK_CHECKER_ON``.

.. Generated from spec:/acfg/if/ticks-per-time-slice

.. index:: CONFIGURE_TICKS_PER_TIMESLICE
.. index:: ticks per timeslice

.. _CONFIGURE_TICKS_PER_TIMESLICE:

CONFIGURE_TICKS_PER_TIMESLICE
-----------------------------

CONSTANT:
    ``CONFIGURE_TICKS_PER_TIMESLICE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 50.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the length of the timeslice
    quantum in ticks for each task.

NOTES:
    This configuration option has no impact if the Clock Driver is not
    configured, see :ref:`CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`.

.. Generated from spec:/acfg/if/unified-work-areas

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

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then there will be separate memory
    pools for the RTEMS Workspace and C Program Heap.

DESCRIPTION:
    In case this configuration option is defined, then the RTEMS Workspace and
    the C Program Heap will be one pool of memory.

NOTES:
    Having separate pools does have some advantages in the event a task blows a
    stack or writes outside its memory area. However, in low memory systems the
    overhead of the two pools plus the potential for unused memory in either
    pool is very undesirable.

    In high memory environments, this is desirable when you want to use the
    :ref:`ConfigUnlimitedObjects` option.  You will be able to create objects
    until you run out of all available memory rather then just until you run out
    of RTEMS Workspace.

.. Generated from spec:/acfg/if/unlimited-allocation-size

.. index:: CONFIGURE_UNLIMITED_ALLOCATION_SIZE

.. _CONFIGURE_UNLIMITED_ALLOCATION_SIZE:

CONFIGURE_UNLIMITED_ALLOCATION_SIZE
-----------------------------------

CONSTANT:
    ``CONFIGURE_UNLIMITED_ALLOCATION_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 8.

VALUE CONSTRAINTS:
    The value of this configuration option shall meet the constraints of all
    object classes to which it is applied.

DESCRIPTION:
    If :ref:`CONFIGURE_UNLIMITED_OBJECTS` is defined, then the value of this
    configuration option defines the default objects maximum of all object
    classes supporting :ref:`ConfigUnlimitedObjects` to
    ``rtems_resource_unlimited( CONFIGURE_UNLIMITED_ALLOCATION_SIZE )``.

NOTES:
    By allowing users to declare all resources as being unlimited the user can
    avoid identifying and limiting the resources used.

    The object maximum of each class can be configured also individually using
    the :c:func:`rtems_resource_unlimited` macro.

.. Generated from spec:/acfg/if/unlimited-objects

.. index:: CONFIGURE_UNLIMITED_OBJECTS

.. _CONFIGURE_UNLIMITED_OBJECTS:

CONFIGURE_UNLIMITED_OBJECTS
---------------------------

CONSTANT:
    ``CONFIGURE_UNLIMITED_OBJECTS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then unlimited objects are used
    by default.

NOTES:
    When using unlimited objects, it is common practice to also specify
    :ref:`CONFIGURE_UNIFIED_WORK_AREAS` so the system operates with a single pool
    of memory for both RTEMS Workspace and C Program Heap.

    This option does not override an explicit configuration for a particular
    object class by the user.

    See also :ref:`CONFIGURE_UNLIMITED_ALLOCATION_SIZE`.

.. Generated from spec:/acfg/if/verbose-system-init

.. index:: CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION

.. _CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION:

CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION
---------------------------------------

CONSTANT:
    ``CONFIGURE_VERBOSE_SYSTEM_INITIALIZATION``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the system initialization
    is verbose.

NOTES:
    You may use this feature to debug system initialization issues.  The
    :c:func:`printk` function is used to print the information.

.. Generated from spec:/acfg/if/zero-workspace-automatically

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

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the memory areas used for
    the RTEMS Workspace and the C Program Heap are zeroed with a ``0x00`` byte
    pattern during system initialization.

NOTES:
    Zeroing memory can add significantly to the system initialization time. It is
    not necessary for RTEMS but is often assumed by support libraries.  In case
    :ref:`CONFIGURE_DIRTY_MEMORY` is also defined, then the memory is first
    dirtied and then zeroed.
