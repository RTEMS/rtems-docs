.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

.. index:: fatal error detection
.. index:: fatal error processing
.. index:: fatal error user extension

Overview
--------

The fatal error manager is called upon detection of an irrecoverable error
condition by either RTEMS or the application software.  Fatal errors are also
used in case it is difficult or impossible to return an error condition by
other means, e.g. a return value of a directive call.  Fatal errors can be
detected from various sources, for example

- the executive (RTEMS),
- support libraries,
- user system code, and
- user application code.

RTEMS automatically invokes the fatal error manager upon detection of an error
it considers to be fatal.  Similarly, the user should invoke the fatal error
manager upon detection of a fatal error.

Each static or dynamic user extension set may include a fatal error handler.
The fatal error handler in the static extension set can be used to provide
access to debuggers and monitors which may be present on the target hardware.
If any user-supplied fatal error handlers are installed, the fatal error
manager will invoke them.  Usually, the board support package provides a fatal
error extension which resets the board.  If no user handlers are configured or
if all the user handler return control to the fatal error manager, then the
RTEMS default fatal error handler is invoked.  If the default fatal error
handler is invoked, then the system state is marked as failed.

Although the precise behavior of the default fatal error handler is processor
specific, in general, it will disable all maskable interrupts, place the error
code in a known processor dependent place (generally either on the stack or in
a register), and halt the processor.  The precise actions of the RTEMS fatal
error are discussed in the Default Fatal Error Processing chapter of the
Applications Supplement document for a specific target processor.

Fatal Sources
-------------

The following fatal sources are defined for RTEMS via the
:c:type:`rtems_fatal_source` enumeration.  Each symbolic name has the
corresponding numeric fatal source in parenthesis.

INTERNAL_ERROR_CORE (0)
    Errors of the core operating system.  See :ref:`internal_errors`.

INTERNAL_ERROR_RTEMS_API (1)
    Errors of the Classic API.

INTERNAL_ERROR_POSIX_API (2)
    Errors of the POSIX API.

RTEMS_FATAL_SOURCE_BDBUF (3)
    Fatal source for the block device cache.  See
    :c:type:`rtems_bdbuf_fatal_code`.

RTEMS_FATAL_SOURCE_APPLICATION (4)
    Fatal source for application-specific errors.  The fatal code is
    application-specific.

RTEMS_FATAL_SOURCE_EXIT (5)
    Fatal source of :c:func:`exit()`.  The fatal code is the :c:func:`exit()`
    status code.

RTEMS_FATAL_SOURCE_BSP (6)
    Fatal source for BSP errors.  The fatal codes are defined in
    :file:`<bsp/fatal.h>`.  Examples are interrupt and exception
    initialization.  See :c:type:`bsp_fatal_code` and :c:func:`bsp_fatal()`.

RTEMS_FATAL_SOURCE_ASSERT (7)
    Fatal source of :c:macro:`assert()`.  The fatal code is the pointer value
    of the assert context.  See :c:type:`rtems_assert_context`.

RTEMS_FATAL_SOURCE_STACK_CHECKER (8)
    Fatal source of the stack checker.  The fatal code is the object name of
    the executing task.

RTEMS_FATAL_SOURCE_EXCEPTION (9)
    Fatal source of the exceptions.  The fatal code is the pointer value of the
    exception frame pointer.  See :c:type:`rtems_exception_frame` and
    :ref:`rtems_exception_frame_print`.

RTEMS_FATAL_SOURCE_SMP (10)
    Fatal source of SMP domain.  See :c:type:`SMP_Fatal_code`.

RTEMS_FATAL_SOURCE_PANIC (11)
    Fatal source of :c:func:`rtems_panic`, see :ref:`rtems_panic`.

RTEMS_FATAL_SOURCE_INVALID_HEAP_FREE (12)
    Fatal source for invalid C program heap frees via :c:func:`free`.  The
    fatal code is the bad pointer.

RTEMS_FATAL_SOURCE_HEAP (13)
    Fatal source for heap errors.  The fatal code is the address to a heap error
    context.  See :c:type:`Heap_Error_context`.

.. _internal_errors:

Internal Error Codes
--------------------

The following error codes are defined for the :c:data:`INTERNAL_ERROR_CORE`
fatal source.  Each symbolic name has the corresponding numeric error code in
parenthesis.

INTERNAL_ERROR_TOO_LITTLE_WORKSPACE (2)
    There is not enough memory for the workspace.  This fatal error may occur
    during system initialization.  It is an application configuration error.

INTERNAL_ERROR_THREAD_EXITTED (5)
    A non-POSIX thread entry function returned.  This is an API usage error.

    An example code to provoke this fatal error is:

    .. code-block:: c

        rtems_task task( rtems_task_argument arg )
        {
          /* Classic API tasks must not return */
        }

        void create_bad_task( void )
        {
          rtems_status_code sc;
          rtems_id          task_id;

          sc = rtems_task_create(
            rtems_build_name('T', 'A', 'S', 'K'),
            1,
            RTEMS_MINIMUM_STACK_SIZE,
            RTEMS_DEFAULT_MODES,
            RTEMS_DEFAULT_ATTRIBUTES,
            &task_id
          );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_task_start( task_id, task, 0 );
          assert( sc == RTEMS_SUCCESSFUL );
        }

INTERNAL_ERROR_INCONSISTENT_MP_INFORMATION (6)
    This fatal error can only occur on MPCI configurations.  The MPCI nodes or
    global objects configuration is inconsistent.  This fatal error may occur
    during system initialization.  It is an application configuration error.

INTERNAL_ERROR_INVALID_NODE (7)
    This fatal error can only occur on MPCI configurations.  The own MPCI node
    number is invalid.  This fatal error may occur during system
    initialization.  It is an application configuration error.

INTERNAL_ERROR_NO_MPCI (8)
    This fatal error can only occur on MPCI configurations.  There is no MPCI
    configuration table.  This fatal error may occur during system
    initialization.  It is an application configuration error.

INTERNAL_ERROR_BAD_PACKET (9)
    This fatal error can only occur on MPCI configurations.  The MPCI server
    thread received a bad packet.

INTERNAL_ERROR_OUT_OF_PACKETS (10)
    This fatal error can only occur on MPCI configurations.  The MPCI packet
    pool is empty.  It is an application configuration error.

INTERNAL_ERROR_OUT_OF_GLOBAL_OBJECTS (11)
    This fatal error can only occur on MPCI configurations.  The MPCI global
    objects pool is empty.  It is an application configuration error.

INTERNAL_ERROR_OUT_OF_PROXIES (12)
    This fatal error can only occur on MPCI configurations.  The MPCI thread
    proxy pool is empty.  It is an application configuration error.

INTERNAL_ERROR_INVALID_GLOBAL_ID (13)
    This fatal error can only occur on MPCI configurations.  The system cannot
    find the global object for a specific object identifier.  In case this
    happens, then this is probably an operating system bug.

INTERNAL_ERROR_NO_MEMORY_FOR_HEAP (23)
    There is not enough memory for the C program heap.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

INTERNAL_ERROR_CPU_ISR_INSTALL_VECTOR (24)
    The use of :c:func:`_CPU_ISR_install_vector()` is illegal on this system.

INTERNAL_ERROR_RESOURCE_IN_USE (25)
    This fatal error can only occur on debug configurations.  It happens in
    case a thread which owns mutexes is deleted.  Mutexes owned by a deleted
    thread are in an inconsistent state.

INTERNAL_ERROR_RTEMS_INIT_TASK_ENTRY_IS_NULL (26)
    An RTEMS initialization task entry function is NULL.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

INTERNAL_ERROR_THREAD_QUEUE_DEADLOCK (28)
    A deadlock was detected during a thread queue enqueue operation.

INTERNAL_ERROR_THREAD_QUEUE_ENQUEUE_STICKY_FROM_BAD_STATE (29)
    This fatal error can only happen in SMP configurations.  It is not allowed
    to obtain MrsP semaphores in a context with thread dispatching disabled,
    for example interrupt context.

    An example code to provoke this fatal error is:

    .. code-block:: c

        rtems_timer_service_routine bad( rtems_id timer_id, void *arg )
        {
          rtems_id *sem_id;

          sem_id = arg;

          rtems_semaphore_obtain( *sem_id, RTEMS_WAIT, RTEMS_NO_TIMEOUT );
          assert( 0 );
        }

        rtems_task fire_bad_timer( rtems_task_argument arg )
        {
          rtems_status_code sc;
          rtems_id          sem_id;
          rtems_id          timer_id;

          sc = rtems_semaphore_create(
            rtems_build_name('M', 'R', 'S', 'P'),
            1,
            RTEMS_MULTIPROCESSOR_RESOURCE_SHARING
              | RTEMS_BINARY_SEMAPHORE,
            1,
            &sem_id
          );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_timer_create(
            rtems_build_name( 'E', 'V', 'I', 'L' ),
            &timer_id
          );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_semaphore_obtain( sem_id, RTEMS_WAIT, RTEMS_NO_TIMEOUT );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_timer_fire_after( timer_id, 1, bad, &sem_id );
          assert( sc == RTEMS_SUCCESSFUL );

          rtems_task_wake_after( 2 );
          assert( 0 );
        }

INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL (30)
    It is illegal to call blocking operating system services with thread
    dispatching disabled, for example in interrupt context.

    An example code to provoke this fatal error is:

    .. code-block:: c

        void bad( rtems_id id, void *arg )
        {
          rtems_task_wake_after( RTEMS_YIELD_PROCESSOR );
          assert( 0 );
        }

        void fire_bad_timer( void )
        {
          rtems_status_code sc;
          rtems_id          id;

          sc = rtems_timer_create(
            rtems_build_name( 'E', 'V', 'I', 'L' ),
            &id
          );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_timer_fire_after( id, 1, bad, NULL );
          assert( sc == RTEMS_SUCCESSFUL );

          rtems_task_wake_after( 2 );
          assert( 0 );
        }

INTERNAL_ERROR_BAD_THREAD_DISPATCH_ENVIRONMENT (31)
    In SMP configurations, it is a fatal error to call blocking operating
    system with interrupts disabled, since this prevents delivery of
    inter-processor interrupts.  This could lead to executing threads which are
    not allowed to execute resulting in undefined system behaviour.

    Some CPU ports, for example the ARM Cortex-M port, have a similar problem,
    since the interrupt state is not a part of the thread context.

    This fatal error is detected in the operating system core function
    :c:func:`_Thread_Do_dispatch()` responsible to carry out a thread dispatch.

    An example code to provoke this fatal error is:

    .. code-block:: c

        void bad( void )
        {
          rtems_interrupt_level level;

          rtems_interrupt_local_disable( level );
          rtems_task_suspend( RTEMS_SELF );
          rtems_interrupt_local_enable( level  );
        }

INTERNAL_ERROR_RTEMS_INIT_TASK_CREATE_FAILED (32)
    Creation of an RTEMS initialization task failed.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

INTERNAL_ERROR_POSIX_INIT_THREAD_CREATE_FAILED (33)
    Creation of a POSIX initialization thread failed.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

INTERNAL_ERROR_LIBIO_STDOUT_FD_OPEN_FAILED (36)
    Open of the standard output file descriptor failed or resulted in an
    unexpected file descriptor number.  This fatal error may occur during
    system initialization.  It is an application configuration error.

INTERNAL_ERROR_LIBIO_STDERR_FD_OPEN_FAILED (37)
    Open of the standard error file descriptor failed or resulted in an
    unexpected file descriptor number.  This fatal error may occur during
    system initialization.  It is an application configuration error.

INTERNAL_ERROR_ILLEGAL_USE_OF_FLOATING_POINT_UNIT (38)
    The floating point unit was used illegally, for example in interrupt
    context on some architectures.

INTERNAL_ERROR_ARC4RANDOM_GETENTROPY_FAIL (39)
    A :c:func:`getentropy` system call failed in one of the `ARC4RANDOM(3)
    <https://man.openbsd.org/arc4random.3>`_ functions.  This fatal error can
    only be fixed with a different implementation of :c:func:`getentropy`.

INTERNAL_ERROR_NO_MEMORY_FOR_PER_CPU_DATA (40)
    This fatal error may happen during workspace initialization.  There is not
    enough memory available to populate the per-CPU data areas, see
    `<rtems/score/percpudata.h> <https://git.rtems.org/rtems/tree/cpukit/include/rtems/score/percpudata.h>`_.

INTERNAL_ERROR_TOO_LARGE_TLS_SIZE (41)
    This fatal error may happen during system initialization.  The actual
    thread-local storage (TLS) size of the application exceeds the configured
    maximum, see
    :ref:`CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE <CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE>`.
    You can get the thread-local storage size of an application using the RTEMS
    tool ``rtems-execinfo``.
