.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
