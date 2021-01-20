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

.. _EventManagerDirectives:

Directives
==========

This section details the directives of the Event Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/event/if/send

.. raw:: latex

    \clearpage

.. index:: rtems_event_send()

.. _InterfaceRtemsEventSend:

rtems_event_send()
------------------

Sends the event set to the task.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_event_send( rtems_id id, rtems_event_set event_in );

.. rubric:: PARAMETERS:

``id``
    This parameter is the identifier of the target task to receive the event
    set.

``event_in``
    This parameter is the event set to send.

.. rubric:: DESCRIPTION:

This directive sends the event set, ``event_in``, to the target task identified
by ``id``.  Based upon the state of the target task, one of the following
situations applies:

* The target task is blocked waiting for events, then

  * if the waiting task's input event condition is satisfied, then the task is
    made ready for execution, or

  * otherwise, the event set is posted but left pending and the task remains
    blocked.

* The target task is not waiting for events, then the event set is posted and
  left pending.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no task associated with the identifier specified by ``id``.

.. rubric:: NOTES:

Events can be sent by tasks or an :term:`ISR`.

Specifying :c:macro:`RTEMS_SELF` for ``id`` results in the event set being sent
to the calling task.

The event set to send shall be built by a *bitwise or* of the desired events.
The set of valid events is :c:macro:`RTEMS_EVENT_0` through
:c:macro:`RTEMS_EVENT_31`.  If an event is not explicitly specified in the set,
then it is not present.

Identical events sent to a task are not queued.  In other words, the second,
and subsequent, posting of an event to a task before it can perform an
:ref:`InterfaceRtemsEventReceive` has no effect.

The calling task will be preempted if it has preemption enabled and a higher
priority task is unblocked as the result of this directive.

Sending an event set to a global task which does not reside on the local node
will generate a request telling the remote node to send the event set to the
appropriate task.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may unblock another task which may preempt the calling task.

.. Generated from spec:/rtems/event/if/receive

.. raw:: latex

    \clearpage

.. index:: rtems_event_receive()

.. _InterfaceRtemsEventReceive:

rtems_event_receive()
---------------------

Receives or gets an event set from the calling task.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_event_receive(
      rtems_event_set  event_in,
      rtems_option     option_set,
      rtems_interval   ticks,
      rtems_event_set *event_out
    );

.. rubric:: PARAMETERS:

``event_in``
    This parameter is the event set of interest.  Use
    :c:macro:`RTEMS_PENDING_EVENTS` to get the pending events.

``option_set``
    This parameter is the option set.

``ticks``
    This parameter is the timeout in clock ticks if the :c:macro:`RTEMS_WAIT`
    option is set.  Use :c:macro:`RTEMS_NO_TIMEOUT` to wait potentially
    forever.

``event_out``
    This parameter is the pointer to an event set.  The received or pending
    events are stored in the referenced event set if the operation was
    successful.

.. rubric:: DESCRIPTION:

This directive can be used to

* get the pending events of the calling task, or

* receive events.

To **get the pending events** use the constant :c:macro:`RTEMS_PENDING_EVENTS`
for the ``event_in`` parameter.  The pending events are returned to the calling
task but the event set of the calling task is left unaltered.  The
``option_set`` and ``ticks`` parameters are ignored in this case.  The
directive returns immediately and does not block.

To **receive events** you have to define an input event condition and some
options.

The **option set** specified in ``option_set`` is built through a *bitwise or*
of the option constants described below.  Not all combinations of options are
allowed.  Some options are mutually exclusive.  If mutually exclusive options
are combined, the behaviour is undefined.  Options not mentioned below are not
evaluated by this directive and have no effect. Default options can be selected
by using the :c:macro:`RTEMS_DEFAULT_OPTIONS` constant.  The option set defines

* if the calling task will wait or poll for the events, and

* if the calling task wants to receive all or any of the input events.

The calling task can **wait** or **poll** for the events.

* **Waiting** for events is the default and can be emphasized through the use
  of the :c:macro:`RTEMS_WAIT` option.  The ``ticks`` parameter defines how
  long the calling task is willing to wait.  Use :c:macro:`RTEMS_NO_TIMEOUT` to
  wait potentially forever, otherwise set a timeout interval in clock ticks.

* Not waiting for events (**polling**) is selected by the
  :c:macro:`RTEMS_NO_WAIT` option.  If this option is defined, then the
  ``ticks`` parameter is ignored.

The calling task can receive **all** or **any** of the input events specified
in ``event_in``.

* Receiving **all** input events is the default and can be emphasized through
  the use of the :c:macro:`RTEMS_EVENT_ALL` option.

* Receiving **any** of the input events is selected by the
  :c:macro:`RTEMS_EVENT_ANY` option.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``event_out`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_UNSATISFIED`
    The events of interest were not immediately available.

:c:macro:`RTEMS_TIMEOUT`
    The events of interest were not available within the specified timeout
    interval.

.. rubric:: NOTES:

This directive only affects the events specified in ``event_in``. Any pending
events that do not correspond to any of the events specified in ``event_in``
will be left pending.

To receive all events use the event set constant :c:macro:`RTEMS_ALL_EVENTS`
for the ``event_in`` parameter.  Do not confuse this event set constant with
the directive option :c:macro:`RTEMS_EVENT_ALL`.

A task can **receive all of the pending events** by calling the directive with
a value of :c:macro:`RTEMS_ALL_EVENTS` for the ``event_in`` parameter and the
bitwise or of the :c:macro:`RTEMS_NO_WAIT` and :c:macro:`RTEMS_EVENT_ANY`
options for the ``option_set`` parameter.  The pending events are returned and
the event set of the task is cleared.  If no events are pending then the
:c:macro:`RTEMS_UNSATISFIED` status code will be returned.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The timeout functionality of the directive requires a :term:`clock tick`.
