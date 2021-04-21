.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
