.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

.. index:: asynchronous signal routine
.. index:: ASR

Signal Manager Definitions
--------------------------

The signal manager allows a task to optionally define an asynchronous signal
routine (ASR).  An ASR is to a task what an ISR is to an application's set of
tasks.  When the processor is interrupted, the execution of an application is
also interrupted and an ISR is given control.  Similarly, when a signal is sent
to a task, that task's execution path will be "interrupted" by the ASR.
Sending a signal to a task has no effect on the receiving task's current
execution state.

.. index:: rtems_signal_set

A signal flag is used by a task (or ISR) to inform another task of the
occurrence of a significant situation.  Thirty-two signal flags are associated
with each task.  A collection of one or more signals is referred to as a signal
set.  The data type ``rtems_signal_set`` is used to manipulate signal sets.

A signal set is posted when it is directed (or sent) to a task. A pending
signal is a signal that has been sent to a task with a valid ASR, but has not
been processed by that task's ASR.

.. index:: ASR vs. ISR
.. index:: ISR vs. ASR

A Comparison of ASRs and ISRs
-----------------------------

The format of an ASR is similar to that of an ISR with the following
exceptions:

- ISRs are scheduled by the processor hardware.  ASRs are scheduled by RTEMS.

- ISRs do not execute in the context of a task and may invoke only a subset of
  directives.  ASRs execute in the context of a task and may execute any
  directive.

- When an ISR is invoked, it is passed the vector number as its argument.  When
  an ASR is invoked, it is passed the signal set as its argument.

- An ASR has a task mode which can be different from that of the task.  An ISR
  does not execute as a task and, as a result, does not have a task mode.

.. index:: signal set, building

Building a Signal Set
---------------------

A signal set is built by a bitwise OR of the desired signals.  The set of valid
signals is ``RTEMS_SIGNAL_0`` through ``RTEMS_SIGNAL_31``.  If a signal is not
explicitly specified in the signal set, then it is not present.  Signal values
are specifically designed to be mutually exclusive, therefore bitwise OR and
addition operations are equivalent as long as each signal appears exactly once
in the component list.

This example demonstrates the signal parameter used when sending the signal set
consisting of ``RTEMS_SIGNAL_6``, ``RTEMS_SIGNAL_15``, and ``RTEMS_SIGNAL_31``.
The signal parameter provided to the ``rtems_signal_send`` directive should be
``RTEMS_SIGNAL_6 | RTEMS_SIGNAL_15 | RTEMS_SIGNAL_31``.

.. index:: ASR mode, building

Building an ASR Mode
--------------------

In general, an ASR's mode is built by a bitwise OR of the desired mode
components.  The set of valid mode components is the same as those allowed with
the task_create and task_mode directives.  A complete list of mode options is
provided in the following table:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_PREEMPT``
   - is masked by ``RTEMS_PREEMPT_MASK`` and enables preemption
 * - ``RTEMS_NO_PREEMPT``
   - is masked by ``RTEMS_PREEMPT_MASK`` and disables preemption
 * - ``RTEMS_NO_TIMESLICE``
   - is masked by ``RTEMS_TIMESLICE_MASK`` and disables timeslicing
 * - ``RTEMS_TIMESLICE``
   - is masked by ``RTEMS_TIMESLICE_MASK`` and enables timeslicing
 * - ``RTEMS_ASR``
   - is masked by ``RTEMS_ASR_MASK`` and enables ASR processing
 * - ``RTEMS_NO_ASR``
   - is masked by ``RTEMS_ASR_MASK`` and disables ASR processing
 * - ``RTEMS_INTERRUPT_LEVEL(0)``
   - is masked by ``RTEMS_INTERRUPT_MASK`` and enables all interrupts
 * - ``RTEMS_INTERRUPT_LEVEL(n)``
   - is masked by ``RTEMS_INTERRUPT_MASK`` and sets interrupts level n

Mode values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each mode appears
exactly once in the component list.  A mode component listed as a default is
not required to appear in the mode list, although it is a good programming
practice to specify default components.  If all defaults are desired, the mode
``DEFAULT_MODES`` should be specified on this call.

This example demonstrates the mode parameter used with the
``rtems_signal_catch`` to establish an ASR which executes at interrupt level
three and is non-preemptible.  The mode should be set to
``RTEMS_INTERRUPT_LEVEL(3) | RTEMS_NO_PREEMPT`` to indicate the desired
processor mode and interrupt level.
