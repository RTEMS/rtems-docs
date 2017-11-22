.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Initialization Manager
**********************

Introduction
============

The Initialization Manager is responsible for initializing the Board Support
Package, RTEMS, device drivers, the root filesystem and the application.  The
:ref:`Fatal Error Manager <fatal_error_manager>` is responsible for the system
shutdown.

The Initialization Manager provides only one directive:

- rtems_initialize_executive_ - Initialize RTEMS

Background
==========

.. index:: initialization tasks

Initialization Tasks
--------------------

Initialization task(s) are the mechanism by which RTEMS transfers initial
control to the user's application.  Initialization tasks differ from other
application tasks in that they are defined in the User Initialization Tasks
Table and automatically created and started by RTEMS as part of its
initialization sequence.  Since the initialization tasks are scheduled using
the same algorithm as all other RTEMS tasks, they must be configured at a
priority and mode which will ensure that they will complete execution before
other application tasks execute.  Although there is no upper limit on the
number of initialization tasks, an application is required to define at least
one.

A typical initialization task will create and start the static set of
application tasks.  It may also create any other objects used by the
application.  Initialization tasks which only perform initialization should
delete themselves upon completion to free resources for other tasks.
Initialization tasks may transform themselves into a "normal" application task.
This transformation typically involves changing priority and execution mode.
RTEMS does not automatically delete the initialization tasks.

The Idle Task
-------------

The Idle Task is the lowest priority task in a system and executes only when no
other task is ready to execute.  The default implementation of this task
consists of an infinite loop. RTEMS allows the Idle Task body to be replaced by
a CPU specific implementation, a BSP specific implementation or an application
specific implementation.

The Idle Task is preemptible and *WILL* be preempted when any other task is
made ready to execute.  This characteristic is critical to the overall behavior
of any application.

Initialization Manager Failure
------------------------------

System initialization errors are fatal.  See :ref:`internal_errors`.

Operations
==========

Initializing RTEMS
------------------

The Initialization Manager :c:func:`rtems_initialize_executive()` directives is
called by the :c:func:`boot_card()` routine which is invoked by the Board
Support Package once a basic C run-time environment is set up.  This consists
of

- a valid and accessible text section, read-only data, read-write data and
  zero-initialized data,

- an initialization stack large enough to initialize the rest of the Board
  Support Package, RTEMS and the device drivers,

- all registers and components mandated by Application Binary Interface, and

- disabled interrupts.

The :c:func:`rtems_initialize_executive()` directive uses a system
initialization :ref:`linker set <linker_sets>` to initialize only those parts
of the overall RTEMS feature set that is necessary for a particular
application.  Each RTEMS feature used the application may optionally register
an initialization handler.  The system initialization API is available via
:samp:`#included <rtems/sysinit.h>`.

A list of all initialization steps follows.  Some steps are optional depending
on the requested feature set of the application.  The initialization steps are
execute in the order presented here.

RTEMS_SYSINIT_BSP_WORK_AREAS
    The work areas consisting of C Program Heap and the RTEMS Workspace are
    initialized by the Board Support Package.  This step is mandatory.

RTEMS_SYSINIT_BSP_START
    Basic initialization step provided by the Board Support Package.  This step
    is mandatory.

RTEMS_SYSINIT_INITIAL_EXTENSIONS
    Registers the initial extensions.  This step is optional and depends on the
    application configuration.

RTEMS_SYSINIT_MP_EARLY
    Early MPCI initialization.  This step is mandatory on MPCI configurations.

RTEMS_SYSINIT_DATA_STRUCTURES
    This directive is called when the Board Support Package has completed its
    basic initialization and allows RTEMS to initialize the application
    environment based upon the information in the Configuration Table, User
    Initialization Tasks Table, Device Driver Table, User Extension Table,
    Multiprocessor Configuration Table, and the Multiprocessor Communications
    Interface (MPCI) Table.

RTEMS_SYSINIT_CPU_SET
    Initialization of system CPU set.  This step is optional and depends on the
    application configuration.

RTEMS_SYSINIT_MP
    MPCI initialization.  This step is mandatory on MPCI configurations.

RTEMS_SYSINIT_USER_EXTENSIONS
    Initialization of the User Extensions object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_TASKS
    Initialization of the Classic Tasks object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_TIMER
    Initialization of the Classic Timer object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_SIGNAL
    Initialization of the Classic Signal support.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_EVENT
    Initialization of the Classic Event support.  This step is optional and
    depends on the application configuration.  This step is only used on MPCI
    configurations.

RTEMS_SYSINIT_CLASSIC_MESSAGE_QUEUE
    Initialization of the Classic Message Queue object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_SEMAPHORE
    Initialization of the Classic Semaphore object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_PARTITION
    Initialization of the Classic Partition object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_REGION
    Initialization of the Classic Region object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_DUAL_PORTED_MEMORY
    Initialization of the Classic Dual-Ported Memory object class.  This step
    is optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_RATE_MONOTONIC
    Initialization of the Classic Rate-Monotonic object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_BARRIER
    Initialization of the Classic Barrier object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_POSIX_SIGNALS
    Initialization of the POSIX Signals support.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_POSIX_THREADS
    Initialization of the POSIX Threads object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_POSIX_MESSAGE_QUEUE
    Initialization of the POSIX Message Queue object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_POSIX_SEMAPHORE
    Initialization of the POSIX Semaphore object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_POSIX_TIMER
    Initialization of the POSIX Timer object class.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_POSIX_RWLOCK
    Initialization of the POSIX Read-Write Locks object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_POSIX_KEYS
    Initialization of the POSIX Keys object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_POSIX_CLEANUP
    Initialization of the POSIX Cleanup support.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_IDLE_THREADS
    Initialization of idle threads.  This step is mandatory.

RTEMS_SYSINIT_LIBIO
    Initialization of IO library.  This step is optional and depends on the
    application configuration.

RTEMS_SYSINIT_ROOT_FILESYSTEM
    Initialization of the root filesystem.  This step is optional and depends
    on the application configuration.

RTEMS_SYSINIT_DRVMGR
    Driver manager initialization.  This step is optional and depends on the
    application configuration.  Only available if the driver manager is
    enabled.

RTEMS_SYSINIT_MP_SERVER
    MPCI server initialization.  This step is mandatory on MPCI configurations.

RTEMS_SYSINIT_BSP_PRE_DRIVERS
    Initialization step performed right before device drivers are initialized.
    This step is mandatory.

RTEMS_SYSINIT_DRVMGR_LEVEL_1
    Driver manager level 1 initialization.  This step is optional and depends
    on the application configuration.  Only available if the driver manager is
    enabled.

RTEMS_SYSINIT_DEVICE_DRIVERS
    This step initializes all statically configured device drivers and performs
    all RTEMS initialization which requires device drivers to be initialized.
    This step is mandatory.  In a multiprocessor configuration, this service
    will initialize the Multiprocessor Communications Interface (MPCI) and
    synchronize with the other nodes in the system.

RTEMS_SYSINIT_DRVMGR_LEVEL_2
    Driver manager level 2 initialization.  This step is optional and depends
    on the application configuration.  Only available if the driver manager is
    enabled.

RTEMS_SYSINIT_DRVMGR_LEVEL_3
    Driver manager level 3 initialization.  This step is optional and depends
    on the application configuration.  Only available if the driver manager is
    enabled.

RTEMS_SYSINIT_DRVMGR_LEVEL_4
    Driver manager level 4 initialization.  This step is optional and depends
    on the application configuration.  Only available if the driver manager is
    enabled.

RTEMS_SYSINIT_MP_FINALIZE
    Finalize MPCI initialization.  This step is mandatory on MPCI
    configurations.

RTEMS_SYSINIT_CLASSIC_USER_TASKS
    Creates and starts the Classic initialization tasks.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_POSIX_USER_THREADS
    Creates POSIX initialization threads.  This step is optional and depends on
    the application configuration.

RTEMS_SYSINIT_STD_FILE_DESCRIPTORS
    Open the standard input, output and error file descriptors.  This step is
    optional and depends on the application configuration.

The final action of the :c:func:`rtems_initialize_executive()` directive is to
start multitasking and switch to the highest priority ready thread.  RTEMS does
not return to the initialization context and the initialization stack may be
re-used for interrupt processing.

Many of RTEMS actions during initialization are based upon the contents of the
Configuration Table.  For more information regarding the format and contents of
this table, please refer to the chapter :ref:`Configuring a System`.

Directives
==========

This section details the Initialization Manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: initialize RTEMS
.. index:: start multitasking
.. index:: rtems_initialize_executive

.. _rtems_initialize_executive:

INITIALIZE_EXECUTIVE - Initialize RTEMS
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_initialize_executive(void);

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    Iterates through the system initialization linker set and invokes the
    registered handlers.  The final step is to start multitasking.

NOTES:
    This directive should be called by :c:func:`boot_card()` only.

    This directive *does not return* to the caller.  Errors in the
    initialization sequence are usually fatal and lead to a system termination.
