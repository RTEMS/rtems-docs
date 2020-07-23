.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the event manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: send event set to a task
.. index:: rtems_event_send

.. _rtems_event_send:

EVENT_SEND - Send event set to a task
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_event_send (
            rtems_id         id,
            rtems_event_set  event_in
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - event set sent successfully
     * - ``RTEMS_INVALID_ID``
       - invalid task id

DESCRIPTION:
    This directive sends an event set, event_in, to the task specified by id.
    If a blocked task's input event condition is satisfied by this directive,
    then it will be made ready.  If its input event condition is not satisfied,
    then the events satisfied are updated and the events not satisfied are left
    pending.  If the task specified by id is not blocked waiting for events,
    then the events sent are left pending.

NOTES:
    Specifying ``RTEMS_SELF`` for id results in the event set being sent to the
    calling task.

    Identical events sent to a task are not queued.  In other words, the
    second, and subsequent, posting of an event to a task before it can perform
    an ``rtems_event_receive`` has no effect.

    The calling task will be preempted if it has preemption enabled and a
    higher priority task is unblocked as the result of this directive.

    Sending an event set to a global task which does not reside on the local
    node will generate a request telling the remote node to send the event set
    to the appropriate task.

.. raw:: latex

   \clearpage

.. index:: receive event condition
.. index:: rtems_event_receive

.. _rtems_event_receive:

EVENT_RECEIVE - Receive event condition
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_event_receive (
            rtems_event_set  event_in,
            rtems_option     option_set,
            rtems_interval   ticks,
            rtems_event_set *event_out
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - event received successfully
     * - ``RTEMS_UNSATISFIED``
       - input event not satisfied (``RTEMS_NO_WAIT``)
     * - ``RTEMS_INVALID_ADDRESS``
       - ``event_out`` is NULL
     * - ``RTEMS_TIMEOUT``
       - timed out waiting for event

DESCRIPTION:

    This directive attempts to receive the event condition specified in
    event_in.  If event_in is set to ``RTEMS_PENDING_EVENTS``, then the current
    pending events are returned in event_out and left pending.  The
    ``RTEMS_WAIT`` and ``RTEMS_NO_WAIT`` options in the option_set parameter
    are used to specify whether or not the task is willing to wait for the
    event condition to be satisfied. ``RTEMS_EVENT_ANY`` and
    ``RTEMS_EVENT_ALL`` are used in the option_set parameter are used to
    specify whether a single event or the complete event set is necessary to
    satisfy the event condition.  The event_out parameter is returned to the
    calling task with the value that corresponds to the events in event_in that
    were satisfied.

    If pending events satisfy the event condition, then event_out is set to the
    satisfied events and the pending events in the event condition are cleared.
    If the event condition is not satisfied and ``RTEMS_NO_WAIT`` is specified,
    then event_out is set to the currently satisfied events.  If the calling
    task chooses to wait, then it will block waiting for the event condition.

    If the calling task must wait for the event condition to be satisfied, then
    the timeout parameter is used to specify the maximum interval to wait.  If
    it is set to ``RTEMS_NO_TIMEOUT``, then the calling task will wait forever.

NOTES:
    This directive only affects the events specified in event_in.  Any pending
    events that do not correspond to any of the events specified in event_in
    will be left pending.

    The following event receive option constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_WAIT``
       - task will wait for event (default)
     * - ``RTEMS_NO_WAIT``
       - task should not wait
     * - ``RTEMS_EVENT_ALL``
       - return after all events (default)
     * - ``RTEMS_EVENT_ANY``
       - return after any events

    A clock tick is required to support the functionality of this directive.
