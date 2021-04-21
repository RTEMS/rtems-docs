.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

RTEMS_SYSINIT_RECORD
    Initialization of the event recording is the first initialization step.
    This allows to record the further system initialization.  This step is
    optional and depends on the :ref:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS`
    configuration option.

RTEMS_SYSINIT_BSP_EARLY
    The Board Support Package may perform an early platform initialization in
    this step.  This step is optional.

RTEMS_SYSINIT_MEMORY
    The Board Support Package should initialize everything so that calls to
    :c:func:`_Memory_Get()` can be made after this step.  This step is optional.

RTEMS_SYSINIT_DIRTY_MEMORY
    The free memory is dirtied in this step.  This step is optional and depends
    on the :c:macro:`BSP_DIRTY_MEMORY` BSP option.

RTEMS_SYSINIT_ISR_STACK
    The stack checker initializes the ISR stacks in this step.  This step is
    optional and depends on the :ref:`CONFIGURE_STACK_CHECKER_ENABLED`
    configuration option.

RTEMS_SYSINIT_PER_CPU_DATA
    The per-CPU data is initialized in this step.  This step is mandatory.

RTEMS_SYSINIT_SBRK
    The Board Support Package may initialize the :c:func:`sbrk()` support in
    this step.  This step is optional.

RTEMS_SYSINIT_WORKSPACE
    The workspace is initialized in this step.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_MALLOC
    The C program heap is initialized in this step.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_BSP_START
    The Board Support Package should perform a general platform initialization
    in this step (e.g. interrupt controller initialization).  This step is
    mandatory.

RTEMS_SYSINIT_CPU_COUNTER
    Initialization of the CPU counter hardware and support functions.  The CPU
    counter is initialized early to allow its use in the tracing and profiling
    of the system initialization sequence.  This step is optional and depends
    on the application configuration.

RTEMS_SYSINIT_INITIAL_EXTENSIONS
    Registers the initial extensions.  This step is optional and depends on the
    application configuration.

RTEMS_SYSINIT_MP_EARLY
    In MPCI configurations, an early MPCI initialization is performed in this
    step.  This step is mandatory in MPCI configurations.

RTEMS_SYSINIT_DATA_STRUCTURES
    This directive is called when the Board Support Package has completed its
    basic initialization and allows RTEMS to initialize the application
    environment based upon the information in the Configuration Table, User
    Initialization Tasks Table, Device Driver Table, User Extension Table,
    Multiprocessor Configuration Table, and the Multiprocessor Communications
    Interface (MPCI) Table.

RTEMS_SYSINIT_MP
    In MPCI configurations, a general MPCI initialization is performed in this
    step.  This step is mandatory in MPCI configurations.

RTEMS_SYSINIT_USER_EXTENSIONS
    Initialization of the User Extensions object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_TASKS
    Initialization of the Classic Tasks object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_TASKS_MP
    In MPCI configurations, the Classic Tasks MPCI support is initialized in
    this step.  This step is optional and depends on the application
    configuration.

RTEMS_SYSINIT_CLASSIC_TIMER
    Initialization of the Classic Timer object class.  This step is optional
    and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_SIGNAL
    Initialization of the Classic Signal support.  This step is optional and
    depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_SIGNAL_MP
    In MPCI configurations, the Classic Signal MPCI support is initialized in
    this step.  This step is optional and depends on the application
    configuration.

RTEMS_SYSINIT_CLASSIC_EVENT
    Initialization of the Classic Event support.  This step is optional and
    depends on the application configuration.  This step is only used on MPCI
    configurations.

RTEMS_SYSINIT_CLASSIC_EVENT_MP
    In MPCI configurations, the Classic Event MPCI support is initialized in
    this step.  This step is optional and depends on the application
    configuration.

RTEMS_SYSINIT_CLASSIC_MESSAGE_QUEUE
    Initialization of the Classic Message Queue object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_SEMAPHORE
    Initialization of the Classic Semaphore object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_SEMAPHORE_MP
    In MPCI configurations, the Classic Semaphore MPCI support is initialized
    in this step.  This step is optional and depends on the application
    configuration.

RTEMS_SYSINIT_CLASSIC_PARTITION
    Initialization of the Classic Partition object class.  This step is
    optional and depends on the application configuration.

RTEMS_SYSINIT_CLASSIC_PARTITION_MP
    In MPCI configurations, the Classic Partition MPCI support is initialized
    in this step.  This step is optional and depends on the application
    configuration.

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

RTEMS_SYSINIT_POSIX_SHM
    Initialization of the POSIX Shared Memory object class.  This step is
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
    In MPCI configurations, the MPCI server is initialized in this step.  This
    step is mandatory in MPCI configurations.

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

Global Construction
-------------------

The global construction is carried out by the first Classic API initialization
task (first is defined by index zero in the Classic API initialization task
configuration table).  If no Classic API initialization task exists, then it is
carried out by the first POSIX API initialization thread.  If no initialization
task or thread exists, then no global construction is performed, see for
example :ref:`Specify Idle Task Performs Application Initialization`.  The
Classic API task or POSIX API thread which carries out global construction is
called the main thread.

Global construction runs before the entry function of the main thread.  The
configuration of the main thread must take the global construction into
account.  In particular, the main thread stack size, priority, attributes and
initial modes must be set accordingly.  Thread-local objects and POSIX key
values created during global construction are accessible by the main thread.
If other initialization tasks are configured, and one of them has a higher
priority than the main thread and the main thread is preemptible, this task
executes before the global construction.  In case the main thread blocks during
global construction, then other tasks may run.  In SMP configurations, other
initialization tasks may run in parallel with global construction.  Tasks
created during global construction may preempt the main thread or run in
parallel in SMP configurations.  All RTEMS services allowed in task context are
allowed during global construction.

Global constructors are C++ global object constructors or functions with the
constructor attribute.  For example, the following test program

.. code-block:: c

    #include <stdio.h>
    #include <assert.h>

    class A {
      public:
        A()
        {
          puts( "A:A()" );
        }
    };

    static A a;

    static thread_local int i;

    static thread_local int j;

    static __attribute__(( __constructor__ )) void b( void )
    {
      i = 1;
      puts( "b()" );
    }

    static __attribute__(( __constructor__( 1000 ) )) void c( void )
    {
      puts( "c()" );
    }

    int main( void )
    {
      assert( i == 1 );
      assert( j == 0 );
      return 0;
    }

should output:

.. code-block:: shell

    c()
    b()
    A:A()
