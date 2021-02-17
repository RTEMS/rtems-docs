.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. _SignalManagerDirectives:

Directives
==========

This section details the directives of the Signal Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/signal/if/catch

.. raw:: latex

    \clearpage

.. index:: rtems_signal_catch()
.. index:: establish an ASR
.. index:: install an ASR

.. _InterfaceRtemsSignalCatch:

rtems_signal_catch()
--------------------

Establishes an asynchronous signal routine (ASR) for the calling task.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_signal_catch(
      rtems_asr_entry asr_handler,
      rtems_mode      mode_set
    );

.. rubric:: PARAMETERS:

``asr_handler``
    This parameter is the handler to process an asynchronous signal set.

``mode_set``
    This parameter is the task mode while an asynchronous signal set is
    processed by the handler.  See :ref:`InterfaceRtemsTaskMode`.

.. rubric:: DESCRIPTION:

This directive establishes an asynchronous signal routine (ASR) for the calling
task.  The ``asr_handler`` parameter specifies the entry point of the ASR.  A
task may have at most one handler installed at a time.  The most recently
installed handler is used.  When ``asr_handler`` is `NULL
<https://en.cppreference.com/w/c/types/NULL>`_, the ASR for the calling task is
invalidated and all pending signals are cleared.  Any signals sent to a task
with an invalid ASR are discarded.  The ``mode_set`` parameter specifies the
execution mode for the ASR.  This execution mode supersedes the task's
execution mode while the ASR is executing.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_NOT_IMPLEMENTED`
    The :c:macro:`RTEMS_NO_PREEMPT` was set in ``mode_set`` and the system
    configuration had no implementation for this mode.

:c:macro:`RTEMS_NOT_IMPLEMENTED`
    The :c:func:`RTEMS_INTERRUPT_LEVEL` was set to a positive level in
    ``mode_set`` and the system configuration had no implementation for this
    mode.

.. rubric:: NOTES:

It is strongly recommended to disable ASR processing during ASR processing by
setting :c:macro:`RTEMS_NO_ASR` in ``mode_set``, otherwise a recursion may
happen during ASR processing.  Uncontrolled recursion may lead to stack
overflows.

Using the same mutex (in particular a recursive mutex) in normal task context
and during ASR processing may result in undefined behaviour.

Asynchronous signal handlers can access thread-local storage (:term:`TLS`).
When thread-local storage is shared between normal task context and ASR
processing, it may be protected by disabled interrupts.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/signal/if/send

.. raw:: latex

    \clearpage

.. index:: rtems_signal_send()
.. index:: send signal set

.. _InterfaceRtemsSignalSend:

rtems_signal_send()
-------------------

Sends the signal set to the task.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_signal_send(
      rtems_id         id,
      rtems_signal_set signal_set
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the identifier of the target task to receive the signal
    set.

``signal_set``
    This parameter is the signal set to send.

.. rubric:: DESCRIPTION:

This directive sends the signal set, ``signal_set``, to the target task
identified by ``id``.

If a caller sends a signal set to a task with an invalid :term:`ASR`, then an
error code is returned to the caller.  If a caller sends a signal set to a task
whose ASR is valid but disabled, then the signal set will be caught and left
pending for the ASR to process when it is enabled.  If a caller sends a signal
set to a task with an ASR that is both valid and enabled, then the signal set
is caught and the ASR will execute the next time the task is dispatched to run.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The ``signal_set`` parameter was 0.

:c:macro:`RTEMS_INVALID_ID`
    There was no task associated with the identifier specified by ``id``.

:c:macro:`RTEMS_NOT_DEFINED`
    The target task had no valid ASR installed.

.. rubric:: NOTES:

Sending a signal set to a task has no effect on that task's state.  If a signal
set is sent to a blocked task, then the task will remain blocked and the
signals will be processed when the task becomes the running task.

Sending a signal set to a global task which does not reside on the local node
will generate a request telling the remote node to send the signal set to the
specified task.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* When the directive operates on a local object, the directive will not cause
  the calling task to be preempted.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.
