.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the signal manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: establish an ASR
.. index:: install an ASR
.. index:: rtems_signal_catch

.. _rtems_signal_catch:

SIGNAL_CATCH - Establish an ASR
-------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_signal_catch(
            rtems_asr_entry  asr_handler,
            rtems_mode       mode
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - always successful

DESCRIPTION:
    This directive establishes an asynchronous signal routine (ASR) for the
    calling task.  The asr_handler parameter specifies the entry point of the
    ASR.  If asr_handler is NULL, the ASR for the calling task is invalidated
    and all pending signals are cleared.  Any signals sent to a task with an
    invalid ASR are discarded.  The mode parameter specifies the execution mode
    for the ASR.  This execution mode supersedes the task's execution mode
    while the ASR is executing.

NOTES:
    This directive will not cause the calling task to be preempted.

    The following task mode constants are defined by RTEMS:

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

.. raw:: latex

   \clearpage

.. index:: send signal set
.. index:: rtems_signal_send

.. _rtems_signal_send:

SIGNAL_SEND - Send signal set to a task
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_signal_send(
            rtems_id         id,
            rtems_signal_set signal_set
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - signal sent successfully
     * - ``RTEMS_INVALID_ID``
       - task id invalid
     * - ``RTEMS_INVALID_NUMBER``
       - empty signal set
     * - ``RTEMS_NOT_DEFINED``
       - ASR invalid

DESCRIPTION:
    This directive sends a signal set to the task specified in id.  The
    signal_set parameter contains the signal set to be sent to the task.

    If a caller sends a signal set to a task with an invalid ASR, then an error
    code is returned to the caller.  If a caller sends a signal set to a task
    whose ASR is valid but disabled, then the signal set will be caught and
    left pending for the ASR to process when it is enabled. If a caller sends a
    signal set to a task with an ASR that is both valid and enabled, then the
    signal set is caught and the ASR will execute the next time the task is
    dispatched to run.

NOTES:
    Sending a signal set to a task has no effect on that task's state.  If a
    signal set is sent to a blocked task, then the task will remain blocked and
    the signals will be processed when the task becomes the running task.

    Sending a signal set to a global task which does not reside on the local
    node will generate a request telling the remote node to send the signal set
    to the specified task.
