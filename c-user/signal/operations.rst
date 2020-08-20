.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Establishing an ASR
-------------------

The ``rtems_signal_catch`` directive establishes an ASR for the calling task.
The address of the ASR and its execution mode are specified to this directive.
The ASR's mode is distinct from the task's mode.  For example, the task may
allow preemption, while that task's ASR may have preemption disabled.  Until a
task calls ``rtems_signal_catch`` the first time, its ASR is invalid, and no
signal sets can be sent to the task.

A task may invalidate its ASR and discard all pending signals by calling
``rtems_signal_catch`` with a value of NULL for the ASR's address.  When a
task's ASR is invalid, new signal sets sent to this task are discarded.

A task may disable ASR processing (``RTEMS_NO_ASR``) via the task_mode
directive.  When a task's ASR is disabled, the signals sent to it are left
pending to be processed later when the ASR is enabled.

Any directive that can be called from a task can also be called from an ASR.  A
task is only allowed one active ASR.  Thus, each call to ``rtems_signal_catch``
replaces the previous one.

Normally, signal processing is disabled for the ASR's execution mode, but if
signal processing is enabled for the ASR, the ASR must be reentrant.

Sending a Signal Set
--------------------

The ``rtems_signal_send`` directive allows both tasks and ISRs to send signals
to a target task.  The target task and a set of signals are specified to the
``rtems_signal_send`` directive.  The sending of a signal to a task has no
effect on the execution state of that task.  If the task is not the currently
running task, then the signals are left pending and processed by the task's ASR
the next time the task is dispatched to run.  The ASR is executed immediately
before the task is dispatched.  If the currently running task sends a signal to
itself or is sent a signal from an ISR, its ASR is immediately dispatched to
run provided signal processing is enabled.

If an ASR with signals enabled is preempted by another task or an ISR and a new
signal set is sent, then a new copy of the ASR will be invoked, nesting the
preempted ASR.  Upon completion of processing the new signal set, control will
return to the preempted ASR.  In this situation, the ASR must be reentrant.

Like events, identical signals sent to a task are not queued.  In other words,
sending the same signal multiple times to a task (without any intermediate
signal processing occurring for the task), has the same result as sending that
signal to that task once.

.. index:: rtems_asr

Processing an ASR
-----------------

Asynchronous signals were designed to provide the capability to generate
software interrupts.  The processing of software interrupts parallels that of
hardware interrupts.  As a result, the differences between the formats of ASRs
and ISRs is limited to the meaning of the single argument passed to an ASR.
The ASR should have the following calling sequence and adhere to C calling
conventions:

.. code-block:: c

    rtems_asr user_routine(
        rtems_signal_set signals
    );

When the ASR returns to RTEMS the mode and execution path of the interrupted
task (or ASR) is restored to the context prior to entering the ASR.
