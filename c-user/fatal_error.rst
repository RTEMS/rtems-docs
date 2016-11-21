.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Fatal Error Manager
*******************

.. index:: fatal errors

Introduction
============

The fatal error manager processes all fatal or irrecoverable errors and other
sources of system termination (for example after :c:func:`exit()`).  Fatal
errors are identified by the (fatal source, error code) pair.  The directives
provided by the fatal error manager are:

- rtems_fatal_ - Invoke the fatal error handler

- rtems_exception_frame_print_ - Print the CPU exception frame

- rtems_fatal_source_text_ - Return the fatal source text

- rtems_internal_error_text_ - Return the error code text

- rtems_fatal_error_occurred_ - Invoke the fatal error handler (deprecated)

Background
==========

Overview
--------

.. index:: fatal error detection
.. index:: fatal error processing
.. index:: fatal error user extension

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
:c:type:`rtems_fatal_source` enumeration.

INTERNAL_ERROR_CORE
    Errors of the core operating system.  See :ref:`internal_errors`.

INTERNAL_ERROR_RTEMS_API
    Errors of the Classic API.

INTERNAL_ERROR_POSIX_API
    Errors of the POSIX API.

RTEMS_FATAL_SOURCE_BDBUF
    Fatal source for the block device cache.  See
    :c:type:`rtems_bdbuf_fatal_code`.

RTEMS_FATAL_SOURCE_APPLICATION
    Fatal source for application-specific errors.  The fatal code is
    application-specific.

RTEMS_FATAL_SOURCE_EXIT
    Fatal source of :c:func:`exit()`.  The fatal code is the :c:func:`exit()`
    status code.

RTEMS_FATAL_SOURCE_BSP
    Fatal source for BSP errors.  The fatal codes are defined in
    :file:`<bsp/fatal.h>`.  Examples are interrupt and exception
    initialization.  See :c:type:`bsp_fatal_code` and :c:func:`bsp_fatal()`.

RTEMS_FATAL_SOURCE_ASSERT
    Fatal source of :c:macro:`assert()`.  The fatal code is the pointer value
    of the assert context.  See :c:type:`rtems_assert_context`.

RTEMS_FATAL_SOURCE_STACK_CHECKER
    Fatal source of the stack checker.  The fatal code is the object name of
    the executing task.

RTEMS_FATAL_SOURCE_EXCEPTION
    Fatal source of the exceptions.  The fatal code is the pointer value of the
    exception frame pointer.  See :c:type:`rtems_exception_frame` and
    :ref:`rtems_exception_frame_print`.

RTEMS_FATAL_SOURCE_SMP
    Fatal source of SMP domain.  See :c:type:`SMP_Fatal_code`.

.. _internal_errors:

Internal Error Codes
--------------------

The following error codes are defined for the :c:data:`INTERNAL_ERROR_CORE`
fatal source.

INTERNAL_ERROR_NO_CONFIGURATION_TABLE
  Document me.

INTERNAL_ERROR_NO_CPU_TABLE
  Document me.

INTERNAL_ERROR_TOO_LITTLE_WORKSPACE
    Document me.

INTERNAL_ERROR_WORKSPACE_ALLOCATION
    Document me.

INTERNAL_ERROR_INTERRUPT_STACK_TOO_SMALL
    Document me.

INTERNAL_ERROR_THREAD_EXITTED
    Document me.

INTERNAL_ERROR_INCONSISTENT_MP_INFORMATION
    Document me.

INTERNAL_ERROR_INVALID_NODE
    Document me.

INTERNAL_ERROR_NO_MPCI
    Document me.

INTERNAL_ERROR_BAD_PACKET
    Document me.

INTERNAL_ERROR_OUT_OF_PACKETS
    Document me.

INTERNAL_ERROR_OUT_OF_GLOBAL_OBJECTS
    Document me.

INTERNAL_ERROR_OUT_OF_PROXIES
    Document me.

INTERNAL_ERROR_INVALID_GLOBAL_ID
    Document me.

INTERNAL_ERROR_BAD_STACK_HOOK
    Document me.

INTERNAL_ERROR_BAD_ATTRIBUTES
    Document me.

INTERNAL_ERROR_IMPLEMENTATION_KEY_CREATE_INCONSISTENCY
    Document me.

INTERNAL_ERROR_THREAD_QUEUE_ENQUEUE_FROM_BAD_STATE
    Document me.

INTERNAL_ERROR_UNLIMITED_AND_MAXIMUM_IS_0
    Document me.

INTERNAL_ERROR_GXX_KEY_ADD_FAILED
    Document me.

INTERNAL_ERROR_GXX_MUTEX_INIT_FAILED
    Document me.

INTERNAL_ERROR_NO_MEMORY_FOR_HEAP
    Document me.

INTERNAL_ERROR_CPU_ISR_INSTALL_VECTOR
    Document me.

INTERNAL_ERROR_RESOURCE_IN_USE
    Document me.

INTERNAL_ERROR_RTEMS_INIT_TASK_ENTRY_IS_NULL
    Document me.

INTERNAL_ERROR_POSIX_INIT_THREAD_ENTRY_IS_NULL
    Document me.

INTERNAL_ERROR_THREAD_QUEUE_DEADLOCK
    Document me.

INTERNAL_ERROR_THREAD_QUEUE_ENQUEUE_STICKY_FROM_BAD_STATE
    Document me.

INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL
    Document me.

INTERNAL_ERROR_BAD_THREAD_DISPATCH_ENVIRONMENT
    On SMP configurations, it is a fatal error to call blocking operating
    system with interrupts disabled, since this prevents delivery of
    inter-processor interrupts.  This could lead to executing threads which are
    not allowed to execute resulting in undefined system behaviour.

    Some CPU ports, for example the ARM Cortex-M port, have a similar problem,
    since the interrupt state is not a part of the thread context.

    This fatal error is detected in the operating system core function
    :c:func:`_Thread_Do_dispatch()` responsible to carry out a thread dispatch.

    An example code to provoke this fatal error is:

    .. code-block:: c

        void bad(void)
        {
          rtems_interrupt_level level;

          rtems_interrupt_local_disable(level);
          rtems_task_suspend(RTEMS_SELF);
          rtems_interrupt_local_enable(level);
        }

Operations
==========

.. _Announcing a Fatal Error:

Announcing a Fatal Error
------------------------
.. index:: _Terminate

The :c:func:`_Terminate()` internal error handler is invoked when the
application or the executive itself determines that a fatal error has occurred
or a final system state is reached (for example after :c:func:`rtems_fatal()`
or :c:func:`exit()`).

The first action of the internal error handler is to call the fatal handler of
the user extensions.  For the initial extensions the following conditions are
required

- a valid stack pointer and enough stack space,

- a valid code memory, and

- valid read-only data.

For the initial extensions the read-write data (including .bss segment) is not
required on single processor configurations.  On SMP configurations, however,
the read-write data must be initialized since this function must determine the
state of the other processors and request them to shut-down if necessary.

Non-initial extensions require in addition valid read-write data.  The board
support package (BSP) may install an initial extension that performs a system
reset.  In this case the non-initial extensions will be not called.

The fatal handler are called with three parameters:

- the fatal source,

- a legacy parameter, the internal error indicator, and

- an error code with a fatal source dependent content.

Once all fatal handler executed, the error information will be stored to
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

.. _rtems_fatal:

FATAL - Invoke the fatal error
------------------------------
.. index:: announce fatal error
.. index:: fatal error, announce
.. index:: rtems_fatal

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_fatal(
           rtems_fatal_source source,
           rtems_fatal_code   error
        ) RTEMS_NO_RETURN;

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    This directive invokes the internal error handler with is internal set to
    false.

.. raw:: latex

   \clearpage

.. _rtems_exception_frame_print:

EXCEPTION_FRAME_PRINT - Prints the exception frame
--------------------------------------------------
.. index:: exception frame
.. index:: rtems_exception_frame_print

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

.. _rtems_fatal_source_text:

FATAL_SOURCE_TEXT - Returns a text for a fatal source
-----------------------------------------------------
.. index:: fatal error
.. index:: rtems_fatal_source_text

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

.. _rtems_internal_error_text:

INTERNAL_ERROR_TEXT - Returns a text for an internal error code
---------------------------------------------------------------
.. index:: fatal error
.. index:: rtems_internal_error_text

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

.. _rtems_fatal_error_occurred:

FATAL_ERROR_OCCURRED - Invoke the fatal error handler (deprecated)
------------------------------------------------------------------
.. index:: announce fatal error
.. index:: fatal error, announce
.. index:: rtems_fatal_error_occurred

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
