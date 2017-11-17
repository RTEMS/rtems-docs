.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

.. index:: fatal errors

.. _fatal_error_manager:

Fatal Error Manager
*******************

Introduction
============

The fatal error manager processes all fatal or irrecoverable errors and other
sources of system termination (for example after :c:func:`exit()`).  Fatal
errors are identified by the (fatal source, error code) pair.  The directives
provided by the fatal error manager are:

- rtems_fatal_ - Invoke the fatal error handler

- rtems_shutdown_executive_ - Shutdown RTEMS

- rtems_exception_frame_print_ - Print the CPU exception frame

- rtems_fatal_source_text_ - Return the fatal source text

- rtems_internal_error_text_ - Return the error code text

- rtems_fatal_error_occurred_ - Invoke the fatal error handler (deprecated)

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
error extesion which resets the board.  If no user handlers are configured or
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

.. _internal_errors:

Internal Error Codes
--------------------

The following error codes are defined for the :c:data:`INTERNAL_ERROR_CORE`
fatal source.  Each symbolic name has the corresponding numeric error code in
parenthesis.

INTERNAL_ERROR_TOO_LITTLE_WORKSPACE (2)
    There is not enough memory for the workspace.  This fatal error may occur
    during system initialization.  It is an application configuration error.

INTERNAL_ERROR_WORKSPACE_ALLOCATION (3)
    An allocation from the workspace failed.  This fatal error may occur during
    system initialization.  It is an application configuration error.

INTERNAL_ERROR_INTERRUPT_STACK_TOO_SMALL (4)
    The configured interrupt stack size is too small.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

INTERNAL_ERROR_THREAD_EXITTED (5)
    A non-POSIX thread entry function returned.  This is an API usage error.

    An example code to provoke this fatal error is:

    .. code-block:: c

        void task( rtems_arg arg )
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

INTERNAL_ERROR_BAD_STACK_HOOK (14)
    The stack allocator hook or stack free hook is NULL.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

INTERNAL_ERROR_UNLIMITED_AND_MAXIMUM_IS_0 (19)
    An object class is configured to use the unlimited objects option, however,
    the count of objects for each extension is zero.  This fatal error may
    occur during system initialization.  It is an application configuration
    error.

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

INTERNAL_ERROR_POSIX_INIT_THREAD_ENTRY_IS_NULL (27)
    A POSIX initialization thread entry function is NULL.  This fatal error may
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

        void bad( rtems_id timer_id, void *arg )
        {
          rtems_id *sem_id;

          sem_id = arg;

          rtems_semaphore_obtain( *sem_id, RTEMS_WAIT, RTEMS_NO_TIMEOUT );
          assert( 0 );
        }

        void fire_bad_timer( rtems_task_argument arg )
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

INTERNAL_ERROR_LIBIO_USER_ENV_KEY_CREATE_FAILED (34)
    Creation of the IO library user environment POSIX key failed.  This fatal
    error may occur during system initialization.  It is an application
    configuration error.

INTERNAL_ERROR_LIBIO_SEM_CREATE_FAILED (35)
    Creation of the IO library semaphore failed.  This fatal error may occur
    during system initialization.  It is an application configuration error.

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
    <https://man.openbsd.org/arc4random.3>`_ functions.

Operations
==========

.. index:: _Terminate

.. _Terminate:

Announcing a Fatal Error
------------------------

The :c:func:`_Terminate()` internal error handler is invoked when the
application or the executive itself determines that a fatal error has occurred
or a final system state is reached (for example after :c:func:`rtems_fatal()`
or :c:func:`exit()`).

The first action of the internal error handler is to call the fatal extension of
the user extensions.  For the initial extensions the following conditions are
required

- a valid stack pointer and enough stack space,

- a valid code memory, and

- valid read-only data.

For the initial extensions the read-write data (including .bss segment) is not
required on single processor configurations.  In SMP configurations, however,
the read-write data must be initialized since this function must determine the
state of the other processors and request them to shut-down if necessary.

Non-initial extensions require in addition valid read-write data.  The board
support package (BSP) may install an initial extension that performs a system
reset.  In this case the non-initial extensions will be not called.

The fatal extensions are called with three parameters:

- the fatal source,

- a legacy parameter which is always false, and

- an error code with a fatal source dependent content.

Once all fatal extensions executed, the error information will be stored to
:c:data:`_Internal_errors_What_happened` and the system state is set to
:c:macro:`SYSTEM_STATE_TERMINATED`.

The final step is to call the CPU port specific :c:func:`_CPU_Fatal_halt()`.

Directives
==========

This section details the fatal error manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: announce fatal error
.. index:: fatal error, announce
.. index:: rtems_fatal

.. _rtems_fatal:

FATAL - Invoke the fatal error
------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_fatal(
           rtems_fatal_source fatal_source,
           rtems_fatal_code   error_code
        ) RTEMS_NO_RETURN;

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    This directive terminates the system.

NOTE:
    Registered :c:func:`atexit()` or :c:func:`on_exit()` handlers are not
    called.  Use :c:func:`exit()` in case these handlers should be invoked.

.. raw:: latex

   \clearpage

.. index:: shutdown RTEMS
.. index:: rtems_shutdown_executive

.. _rtems_shutdown_executive:

SHUTDOWN_EXECUTIVE - Shutdown RTEMS
-----------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_shutdown_executive(
            uint32_t result
        );

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    This directive is called when the application wishes to shutdown RTEMS.
    The system is terminated with a fatal source of ``RTEMS_FATAL_SOURCE_EXIT``
    and the specified ``result`` code.

NOTES:
    This directive *must* be the last RTEMS directive invoked by an application
    and it *does not return* to the caller.

    This directive may be called any time.

.. raw:: latex

   \clearpage

.. index:: exception frame
.. index:: rtems_exception_frame_print

.. _rtems_exception_frame_print:

EXCEPTION_FRAME_PRINT - Prints the exception frame
--------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_exception_frame_print(
            const rtems_exception_frame *frame
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    Prints the exception frame via ``printk()``.

.. raw:: latex

   \clearpage

.. index:: fatal error
.. index:: rtems_fatal_source_text

.. _rtems_fatal_source_text:

FATAL_SOURCE_TEXT - Returns a text for a fatal source
-----------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_fatal_source_text(
            rtems_fatal_source source
        );

DIRECTIVE STATUS CODES:
    The fatal source text or "?" in case the passed fatal source is invalid.

DESCRIPTION:
    Returns a text for a fatal source.  The text for fatal source is the
    enumerator constant.

.. raw:: latex

   \clearpage

.. index:: fatal error
.. index:: rtems_internal_error_text

.. _rtems_internal_error_text:

INTERNAL_ERROR_TEXT - Returns a text for an internal error code
---------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_internal_error_text(
            rtems_fatal_code error
        );

DIRECTIVE STATUS CODES:
    The error code text or "?" in case the passed error code is invalid.

DESCRIPTION:
    Returns a text for an internal error code.  The text for each internal
    error code is the enumerator constant.

.. raw:: latex

   \clearpage

.. index:: announce fatal error
.. index:: fatal error, announce
.. index:: rtems_fatal_error_occurred

.. _rtems_fatal_error_occurred:

FATAL_ERROR_OCCURRED - Invoke the fatal error handler (deprecated)
------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_fatal_error_occurred(
            uint32_t  the_error
        ) RTEMS_NO_RETURN;

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    This directive processes fatal errors.  If the FATAL error extension is
    defined in the configuration table, then the user-defined error extension
    is called.  If configured and the provided FATAL error extension returns,
    then the RTEMS default error handler is invoked.  This directive can be
    invoked by RTEMS or by the user's application code including initialization
    tasks, other tasks, and ISRs.

NOTES:
    This directive is deprecated and should not be used in new code.

    This directive supports local operations only.

    Unless the user-defined error extension takes special actions such as
    restarting the calling task, this directive WILL NOT RETURN to the caller.

    The user-defined extension for this directive may wish to initiate a global
    shutdown.
