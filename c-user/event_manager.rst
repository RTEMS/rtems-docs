.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Event Manager
*************

.. index:: events

Introduction
============

The event manager provides a high performance method of intertask communication
and synchronization.  The directives provided by the event manager are:

- rtems_event_send_ - Send event set to a task
- rtems_event_receive_ - Receive event condition

Background
==========

Event Sets
----------
.. index:: event flag, definition
.. index:: event set, definition
.. index:: rtems_event_set

An event flag is used by a task (or ISR) to inform another task of the
occurrence of a significant situation.  Thirty-two event flags are associated
with each task.  A collection of one or more event flags is referred to as an
event set.  The data type ``rtems_event_set`` is used to manage event sets.

The application developer should remember the following key characteristics of
event operations when utilizing the event manager:

- Events provide a simple synchronization facility.

- Events are aimed at tasks.

- Tasks can wait on more than one event simultaneously.

- Events are independent of one another.

- Events do not hold or transport data.

- Events are not queued.  In other words, if an event is sent more than once to
  a task before being received, the second and subsequent send operations to
  that same task have no effect.

An event set is posted when it is directed (or sent) to a task.  A pending
event is an event that has been posted but not received.  An event condition is
used to specify the event set which the task desires to receive and the
algorithm which will be used to determine when the request is satisfied. An
event condition is satisfied based upon one of two algorithms which are
selected by the user.  The ``RTEMS_EVENT_ANY`` algorithm states that an event
condition is satisfied when at least a single requested event is posted.  The
``RTEMS_EVENT_ALL`` algorithm states that an event condition is satisfied when
every requested event is posted.

Building an Event Set or Condition
----------------------------------
.. index:: event condition, building
.. index:: event set, building

An event set or condition is built by a bitwise OR of the desired events.  The
set of valid events is ``RTEMS_EVENT_0`` through ``RTEMS_EVENT_31``.  If an
event is not explicitly specified in the set or condition, then it is not
present.  Events are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each event appears
exactly once in the event set list.

For example, when sending the event set consisting of ``RTEMS_EVENT_6``,
``RTEMS_EVENT_15``, and ``RTEMS_EVENT_31``, the event parameter to the
``rtems_event_send`` directive should be ``RTEMS_EVENT_6 | RTEMS_EVENT_15 |
RTEMS_EVENT_31``.

Building an EVENT_RECEIVE Option Set
------------------------------------

In general, an option is built by a bitwise OR of the desired option
components.  The set of valid options for the ``rtems_event_receive`` directive
are listed in the following table:

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

Option values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each option
appears exactly once in the component list.  An option listed as a default is
not required to appear in the option list, although it is a good programming
practice to specify default options.  If all defaults are desired, the option
``RTEMS_DEFAULT_OPTIONS`` should be specified on this call.

This example demonstrates the option parameter needed to poll for all events in
a particular event condition to arrive.  The option parameter passed to the
``rtems_event_receive`` directive should be either ``RTEMS_EVENT_ALL |
RTEMS_NO_WAIT`` or ``RTEMS_NO_WAIT``.  The option parameter can be set to
``RTEMS_NO_WAIT`` because ``RTEMS_EVENT_ALL`` is the default condition for
``rtems_event_receive``.

Operations
==========

Sending an Event Set
--------------------

The ``rtems_event_send`` directive allows a task (or an ISR) to direct an event
set to a target task.  Based upon the state of the target task, one of the
following situations applies:

- Target Task is Blocked Waiting for Events

  - If the waiting task's input event condition is satisfied, then the task is
    made ready for execution.

  - If the waiting task's input event condition is not satisfied, then the
    event set is posted but left pending and the task remains blocked.

- Target Task is Not Waiting for Events

  - The event set is posted and left pending.

Receiving an Event Set
----------------------

The ``rtems_event_receive`` directive is used by tasks to accept a specific
input event condition.  The task also specifies whether the request is
satisfied when all requested events are available or any single requested event
is available.  If the requested event condition is satisfied by pending events,
then a successful return code and the satisfying event set are returned
immediately.  If the condition is not satisfied, then one of the following
situations applies:

- By default, the calling task will wait forever for the event condition to be
  satisfied.

- Specifying the ``RTEMS_NO_WAIT`` option forces an immediate return with an
  error status code.

- Specifying a timeout limits the period the task will wait before returning
  with an error status code.

Determining the Pending Event Set
---------------------------------

A task can determine the pending event set by calling the
``rtems_event_receive`` directive with a value of ``RTEMS_PENDING_EVENTS`` for
the input event condition.  The pending events are returned to the calling task
but the event set is left unaltered.

Receiving all Pending Events
----------------------------

A task can receive all of the currently pending events by calling the
``rtems_event_receive`` directive with a value of ``RTEMS_ALL_EVENTS`` for the
input event condition and ``RTEMS_NO_WAIT | RTEMS_EVENT_ANY`` for the option
set.  The pending events are returned to the calling task and the event set is
cleared.  If no events are pending then the ``RTEMS_UNSATISFIED`` status code
will be returned.

Directives
==========

This section details the event manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_event_send:

EVENT_SEND - Send event set to a task
-------------------------------------
.. index:: send event set to a task
.. index:: rtems_event_send

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

.. _rtems_event_receive:

EVENT_RECEIVE - Receive event condition
---------------------------------------
.. index:: receive event condition
.. index:: rtems_event_receive

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
