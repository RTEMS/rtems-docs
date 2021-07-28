.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

- a legacy parameter which is always set to :c:macro:`false`, and

- an error code with a fatal source dependent content.

Once all fatal extensions executed, the system state is set to
:c:macro:`SYSTEM_STATE_TERMINATED`.

The final step is to call the CPU port specific :c:func:`_CPU_Fatal_halt()`.
