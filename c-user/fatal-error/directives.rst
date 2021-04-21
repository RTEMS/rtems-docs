.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

FATAL - Invoke the fatal error handler
--------------------------------------

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

.. index:: panic
.. index:: rtems_panic

.. _rtems_panic:

PANIC - Print a message and invoke the fatal error handler
----------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_panic(
          const char *fmt,
          ...
        ) RTEMS_NO_RETURN RTEMS_PRINTFLIKE( 1, 2 );

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    This directive prints a message via :c:func:`printk` specified by the
    format and optional parameters and then terminates the system with the
    :c:macro:`RTEMS_FATAL_SOURCE_PANIC` fatal source.  The fatal code is set to
    the format string address.

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
