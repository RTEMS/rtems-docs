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

.. _TimerManagerDirectives:

Directives
==========

This section details the directives of the Timer Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/timer/if/create

.. raw:: latex

    \clearpage

.. index:: rtems_timer_create()
.. index:: create a timer

.. _InterfaceRtemsTimerCreate:

rtems_timer_create()
--------------------

Creates a timer.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_create( rtems_name name, rtems_id *id );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name of the timer.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the identifier of the created timer will be
    stored in this variable.

.. rubric:: DESCRIPTION:

This directive creates a timer which resides on the local node.  The timer has
the user-defined object name specified in ``name``.  The assigned object
identifier is returned in ``id``.  This identifier is used to access the timer
with other timer related directives.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive object available to create a timer.  The number of
    timers available to the application is configured through the
    :ref:`CONFIGURE_MAXIMUM_TIMERS` application configuration option.

.. rubric:: NOTES:

The processor used to maintain the timer is the processor of the calling task
at some point during the timer creation.

For control and maintenance of the timer, RTEMS allocates a :term:`TMCB` from
the local TMCB free pool and initializes it.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The number of timers available to the application is configured through the
  :ref:`CONFIGURE_MAXIMUM_TIMERS` application configuration option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

.. Generated from spec:/rtems/timer/if/ident

.. raw:: latex

    \clearpage

.. index:: rtems_timer_ident()
.. index:: obtain the ID of a timer

.. _InterfaceRtemsTimerIdent:

rtems_timer_ident()
-------------------

Identifies a timer by the object name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_ident( rtems_name name, rtems_id *id );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name to look up.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the object identifier of an object with the
    specified name will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive obtains a timer identifier associated with the timer name
specified in ``name``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was 0.

:c:macro:`RTEMS_INVALID_NAME`
    There was no object with the specified name on the local node.

.. rubric:: NOTES:

If the timer name is not unique, then the timer identifier will match the first
timer with that name in the search order.  However, this timer identifier is
not guaranteed to correspond to the desired timer.

The objects are searched from lowest to the highest index.  Only the local node
is searched.

The timer identifier is used with other timer related directives to access the
timer.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/cancel

.. raw:: latex

    \clearpage

.. index:: rtems_timer_cancel()
.. index:: cancel a timer

.. _InterfaceRtemsTimerCancel:

rtems_timer_cancel()
--------------------

Cancels the timer.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_cancel( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

.. rubric:: DESCRIPTION:

This directive cancels the timer specified by ``id``.  This timer will be
reinitiated by the next invocation of :ref:`InterfaceRtemsTimerReset`,
:ref:`InterfaceRtemsTimerFireAfter`, or :ref:`InterfaceRtemsTimerFireWhen` with
the same timer identifier.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/delete

.. raw:: latex

    \clearpage

.. index:: rtems_timer_delete()
.. index:: delete a timer

.. _InterfaceRtemsTimerDelete:

rtems_timer_delete()
--------------------

Deletes the timer.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_delete( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

.. rubric:: DESCRIPTION:

This directive deletes the timer specified by ``id``.  If the timer is running,
it is automatically canceled.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: NOTES:

The :term:`TMCB` for the deleted timer is reclaimed by RTEMS.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The calling task does not have to be the task that created the object.  Any
  local task that knows the object identifier can delete the object.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

.. Generated from spec:/rtems/timer/if/fire-after

.. raw:: latex

    \clearpage

.. index:: rtems_timer_fire_after()
.. index:: fire a timer after an interval

.. _InterfaceRtemsTimerFireAfter:

rtems_timer_fire_after()
------------------------

Fires the timer after the interval.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_fire_after(
      rtems_id                          id,
      rtems_interval                    ticks,
      rtems_timer_service_routine_entry routine,
      void                             *user_data
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

``ticks``
    This parameter is the interval until the routine is fired in clock ticks.

``routine``
    This parameter is the routine to schedule.

``user_data``
    This parameter is the argument passed to the routine when it is fired.

.. rubric:: DESCRIPTION:

This directive initiates the timer specified by ``id``.  If the timer is
running, it is automatically canceled before being initiated.  The timer is
scheduled to fire after an interval of clock ticks has passed specified by
``ticks``.  When the timer fires, the timer service routine ``routine`` will be
invoked with the argument ``user_data`` in the context of the clock tick
:term:`ISR`.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The ``ticks`` parameter was 0.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``routine`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/fire-when

.. raw:: latex

    \clearpage

.. index:: rtems_timer_fire_when()
.. index:: fire a timer at time of day

.. _InterfaceRtemsTimerFireWhen:

rtems_timer_fire_when()
-----------------------

Fires the timer at the time of day.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_fire_when(
      rtems_id                          id,
      rtems_time_of_day                *wall_time,
      rtems_timer_service_routine_entry routine,
      void                             *user_data
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

``wall_time``
    This parameter is the time of day when the routine is fired.

``routine``
    This parameter is the routine to schedule.

``user_data``
    This parameter is the argument passed to the routine when it is fired.

.. rubric:: DESCRIPTION:

This directive initiates the timer specified by ``id``.  If the timer is
running, it is automatically canceled before being initiated.  The timer is
scheduled to fire at the time of day specified by ``wall_time``.  When the
timer fires, the timer service routine ``routine`` will be invoked with the
argument ``user_data`` in the context of the clock tick :term:`ISR`.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_NOT_DEFINED`
    The system date and time was not set.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``routine`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``wall_time`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_CLOCK`
    The time of day was invalid.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/initiate-server

.. raw:: latex

    \clearpage

.. index:: rtems_timer_initiate_server()
.. index:: initiate the Timer Server

.. _InterfaceRtemsTimerInitiateServer:

rtems_timer_initiate_server()
-----------------------------

Initiates the Timer Server.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_initiate_server(
      rtems_task_priority priority,
      size_t              stack_size,
      rtems_attribute     attribute_set
    );

.. rubric:: PARAMETERS:

``priority``
    This parameter is the task priority.

``stack_size``
    This parameter is the task stack size in bytes.

``attribute_set``
    This parameter is the task attribute set.

.. rubric:: DESCRIPTION:

This directive initiates the Timer Server task.  This task is responsible for
executing all timers initiated via the
:ref:`InterfaceRtemsTimerServerFireAfter` or
:ref:`InterfaceRtemsTimerServerFireWhen` directives.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INCORRECT_STATE`
    The Timer Server was already initiated.

:c:macro:`RTEMS_INVALID_PRIORITY`
    The task priority was invalid.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive task object available to create the Timer Server
    task.

:c:macro:`RTEMS_UNSATISFIED`
    There was not enough memory to allocate the task storage area.  The task
    storage area contains the task stack, the thread-local storage, and the
    floating point context.

:c:macro:`RTEMS_UNSATISFIED`
    One of the task create extensions failed to create the Timer Server task.

.. rubric:: NOTES:

The Timer Server task is created using the :ref:`InterfaceRtemsTaskCreate`
directive and must be accounted for when configuring the system.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The number of timers available to the application is configured through the
  :ref:`CONFIGURE_MAXIMUM_TIMERS` application configuration option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

.. Generated from spec:/rtems/timer/if/server-fire-after

.. raw:: latex

    \clearpage

.. index:: rtems_timer_server_fire_after()
.. index:: fire task-based a timer after an interval

.. _InterfaceRtemsTimerServerFireAfter:

rtems_timer_server_fire_after()
-------------------------------

Fires the timer after the interval using the Timer Server.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_server_fire_after(
      rtems_id                          id,
      rtems_interval                    ticks,
      rtems_timer_service_routine_entry routine,
      void                             *user_data
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

``ticks``
    This parameter is the interval until the routine is fired in clock ticks.

``routine``
    This parameter is the routine to schedule.

``user_data``
    This parameter is the argument passed to the routine when it is fired.

.. rubric:: DESCRIPTION:

This directive initiates the timer specified by ``id``.  If the timer is
running, it is automatically canceled before being initiated.  The timer is
scheduled to fire after an interval of clock ticks has passed specified by
``ticks``.  When the timer fires, the timer service routine ``routine`` will be
invoked with the argument ``user_data`` in the context of the Timer Server
task.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INCORRECT_STATE`
    The Timer Server was not initiated.

:c:macro:`RTEMS_INVALID_NUMBER`
    The ``ticks`` parameter was 0.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``routine`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/server-fire-when

.. raw:: latex

    \clearpage

.. index:: rtems_timer_server_fire_when()
.. index:: fire a task-based timer at time of day

.. _InterfaceRtemsTimerServerFireWhen:

rtems_timer_server_fire_when()
------------------------------

Fires the timer at the time of day using the Timer Server.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_server_fire_when(
      rtems_id                          id,
      rtems_time_of_day                *wall_time,
      rtems_timer_service_routine_entry routine,
      void                             *user_data
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

``wall_time``
    This parameter is the time of day when the routine is fired.

``routine``
    This parameter is the routine to schedule.

``user_data``
    This parameter is the argument passed to the routine when it is fired.

.. rubric:: DESCRIPTION:

This directive initiates the timer specified by ``id``.  If the timer is
running, it is automatically canceled before being initiated.  The timer is
scheduled to fire at the time of day specified by ``wall_time``.  When the
timer fires, the timer service routine ``routine`` will be invoked with the
argument ``user_data`` in the context of the Timer Server task.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INCORRECT_STATE`
    The Timer Server was not initiated.

:c:macro:`RTEMS_NOT_DEFINED`
    The system date and time was not set.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``routine`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``wall_time`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_CLOCK`
    The time of day was invalid.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/reset

.. raw:: latex

    \clearpage

.. index:: rtems_timer_reset()
.. index:: reset a timer

.. _InterfaceRtemsTimerReset:

rtems_timer_reset()
-------------------

Resets the timer.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_reset( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

.. rubric:: DESCRIPTION:

This directive resets the timer specified by ``id``.  This timer must have been
previously initiated with either the :ref:`InterfaceRtemsTimerFireAfter` or
:ref:`InterfaceRtemsTimerServerFireAfter` directive.  If active the timer is
canceled, after which the timer is reinitiated using the same interval and
timer service routine which the original :ref:`InterfaceRtemsTimerFireAfter` or
:ref:`InterfaceRtemsTimerServerFireAfter` directive used.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

:c:macro:`RTEMS_NOT_DEFINED`
    The timer was not of the interval class.

.. rubric:: NOTES:

If the timer has not been used or the last usage of this timer was by a
:ref:`InterfaceRtemsTimerFireWhen` or :ref:`InterfaceRtemsTimerServerFireWhen`
directive, then the :c:macro:`RTEMS_NOT_DEFINED` error is returned.

Restarting a cancelled after timer results in the timer being reinitiated with
its previous timer service routine and interval.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/timer/if/get-information

.. raw:: latex

    \clearpage

.. index:: rtems_timer_get_information()

.. _InterfaceRtemsTimerGetInformation:

rtems_timer_get_information()
-----------------------------

Gets information about the timer.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_timer_get_information(
      rtems_id                 id,
      rtems_timer_information *the_info
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the timer identifier.

``the_info``
    This parameter is the pointer to a timer information variable.  When the
    directive call is successful, the information about the timer will be
    stored in this variable.

.. rubric:: DESCRIPTION:

This directive returns information about the timer.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``the_info`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ID`
    There was no timer associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.
