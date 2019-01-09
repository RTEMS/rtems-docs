.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. COMMENT: All rights reserved.

.. index:: timers

Timer Manager
*************

Introduction
============

The timer manager provides support for timer
facilities.  The directives provided by the timer manager are:

- rtems_timer_create_ - Create a timer

- rtems_timer_ident_ - Get ID of a timer

- rtems_timer_cancel_ - Cancel a timer

- rtems_timer_delete_ - Delete a timer

- rtems_timer_fire_after_ - Fire timer after interval

- rtems_timer_fire_when_ - Fire timer when specified

- rtems_timer_initiate_server_ - Initiate server for task-based timers

- rtems_timer_server_fire_after_ - Fire task-based timer after interval

- rtems_timer_server_fire_when_ - Fire task-based timer when specified

- rtems_timer_reset_ - Reset an interval timer

Background
==========

Required Support
----------------

A clock tick is required to support the functionality provided by this manager.

Timers
------

A timer is an RTEMS object which allows the application to schedule operations
to occur at specific times in the future.  User supplied timer service routines
are invoked by either a clock tick directive or a special Timer
Server task when the timer fires.  Timer service routines may perform any
operations or directives which normally would be performed by the application
code which invoked a clock tick directive.

The timer can be used to implement watchdog routines which only fire to denote
that an application error has occurred.  The timer is reset at specific points
in the application to ensure that the watchdog does not fire.  Thus, if the
application does not reset the watchdog timer, then the timer service routine
will fire to indicate that the application has failed to reach a reset point.
This use of a timer is sometimes referred to as a "keep alive" or a "deadman"
timer.

Timer Server
------------

The Timer Server task is responsible for executing the timer service routines
associated with all task-based timers.  This task executes at a priority
specified by :ref:`rtems_timer_initiate_server() <rtems_timer_initiate_server>`
and it may have a priority of zero (the highest priority).  In uniprocessor
configurations, it is created non-preemptible.

By providing a mechanism where timer service routines execute in task rather
than interrupt space, the application is allowed a bit more flexibility in what
operations a timer service routine can perform.  For example, the Timer Server
can be configured to have a floating point context in which case it would be
safe to perform floating point operations from a task-based timer.  Most of the
time, executing floating point instructions from an interrupt service routine
is not considered safe. The timer service routines invoked by the Timer Server
may block, however, since this blocks the Timer Server itself, other timer
service routines that are already pending do not run until the blocked timer
service routine finished its work.

The Timer Server is designed to remain blocked until a task-based timer fires.
This reduces the execution overhead of the Timer Server.

.. index:: rtems_timer_service_routine

Timer Service Routines
----------------------

The timer service routine should adhere to C calling conventions and have a
prototype similar to the following:

.. code-block:: c

    rtems_timer_service_routine user_routine(
        rtems_id   timer_id,
        void      *user_data
    );

Where the timer_id parameter is the RTEMS object ID of the timer which is being
fired and user_data is a pointer to user-defined information which may be
utilized by the timer service routine.  The argument user_data may be NULL.

Operations
==========

Creating a Timer
----------------

The ``rtems_timer_create`` directive creates a timer by allocating a Timer
Control Block (TMCB), assigning the timer a user-specified name, and assigning
it a timer ID.  Newly created timers do not have a timer service routine
associated with them and are not active.

Obtaining Timer IDs
-------------------

When a timer is created, RTEMS generates a unique timer ID and assigns it to
the created timer until it is deleted.  The timer ID may be obtained by either
of two methods.  First, as the result of an invocation of the
``rtems_timer_create`` directive, the timer ID is stored in a user provided
location.  Second, the timer ID may be obtained later using the
``rtems_timer_ident`` directive.  The timer ID is used by other directives to
manipulate this timer.

Initiating an Interval Timer
----------------------------

The ``rtems_timer_fire_after`` and ``rtems_timer_server_fire_after`` directives
initiate a timer to fire a user provided timer service routine after the
specified number of clock ticks have elapsed.  When the interval has elapsed,
the timer service routine will be invoked from a clock tick
directive if it was initiated by the ``rtems_timer_fire_after`` directive and
from the Timer Server task if initiated by the
``rtems_timer_server_fire_after`` directive.

Initiating a Time of Day Timer
------------------------------

The ``rtems_timer_fire_when`` and ``rtems_timer_server_fire_when`` directive
initiate a timer to fire a user provided timer service routine when the
specified time of day has been reached.  When the interval has elapsed, the
timer service routine will be invoked from a clock tick directive
by the ``rtems_timer_fire_when`` directive and from the Timer Server task if
initiated by the ``rtems_timer_server_fire_when`` directive.

Canceling a Timer
-----------------

The ``rtems_timer_cancel`` directive is used to halt the specified timer.  Once
canceled, the timer service routine will not fire unless the timer is
reinitiated.  The timer can be reinitiated using the ``rtems_timer_reset``,
``rtems_timer_fire_after``, and ``rtems_timer_fire_when`` directives.

Resetting a Timer
-----------------

The ``rtems_timer_reset`` directive is used to restore an interval timer
initiated by a previous invocation of ``rtems_timer_fire_after`` or
``rtems_timer_server_fire_after`` to its original interval length.  If the
timer has not been used or the last usage of this timer was by the
``rtems_timer_fire_when`` or ``rtems_timer_server_fire_when`` directive, then
an error is returned.  The timer service routine is not changed or fired by
this directive.

Initiating the Timer Server
---------------------------

The ``rtems_timer_initiate_server`` directive is used to allocate and start the
execution of the Timer Server task.  The application can specify both the stack
size and attributes of the Timer Server.  The Timer Server executes at a
priority higher than any application task and thus the user can expect to be
preempted as the result of executing the ``rtems_timer_initiate_server``
directive.

Deleting a Timer
----------------

The ``rtems_timer_delete`` directive is used to delete a timer.  If the timer
is running and has not expired, the timer is automatically canceled.  The
timer's control block is returned to the TMCB free list when it is deleted.  A
timer can be deleted by a task other than the task which created the timer.
Any subsequent references to the timer's name and ID are invalid.

Directives
==========

This section details the timer manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage
.. index:: create a timer
.. index:: rtems_timer_create

.. _rtems_timer_create:

TIMER_CREATE - Create a timer
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_create(
            rtems_name  name,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer created successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_NAME``
       - invalid timer name
     * - ``RTEMS_TOO_MANY``
       - too many timers created

DESCRIPTION:
    This directive creates a timer.  The assigned timer id is returned in id.
    This id is used to access the timer with other timer manager directives.
    For control and maintenance of the timer, RTEMS allocates a TMCB from the
    local TMCB free pool and initializes it.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    In SMP configurations, the processor of the currently executing thread
    determines the processor used for the created timer.  During the life-time
    of the timer this processor is used to manage the timer internally.

.. raw:: latex

   \clearpage

.. index:: obtain the ID of a timer
.. index:: rtems_timer_ident

.. _rtems_timer_ident:

TIMER_IDENT - Get ID of a timer
-------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_ident(
            rtems_name  name,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer identified successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_NAME``
       - timer name not found

DESCRIPTION:
    This directive obtains the timer id associated with the timer name to be
    acquired.  If the timer name is not unique, then the timer id will match
    one of the timers with that name.  However, this timer id is not guaranteed
    to correspond to the desired timer.  The timer id is used to access this
    timer in other timer related directives.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: cancel a timer
.. index:: rtems_timer_cancel

.. _rtems_timer_cancel:

TIMER_CANCEL - Cancel a timer
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_cancel(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer canceled successfully
     * - ``RTEMS_INVALID_ID``
       - invalid timer id

DESCRIPTION:
    This directive cancels the timer id.  This timer will be reinitiated by the
    next invocation of ``rtems_timer_reset``, ``rtems_timer_fire_after``, or
    ``rtems_timer_fire_when`` with this id.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: delete a timer
.. index:: rtems_timer_delete

.. _rtems_timer_delete:

TIMER_DELETE - Delete a timer
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid timer id

DESCRIPTION:
    This directive deletes the timer specified by id.  If the timer is running,
    it is automatically canceled.  The TMCB for the deleted timer is reclaimed
    by RTEMS.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    A timer can be deleted by a task other than the task which created the
    timer.

.. raw:: latex

   \clearpage

.. index:: fire a timer after an interval
.. index:: rtems_timer_fire_after

.. _rtems_timer_fire_after:

TIMER_FIRE_AFTER - Fire timer after interval
--------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_fire_after(
            rtems_id                           id,
            rtems_interval                     ticks,
            rtems_timer_service_routine_entry  routine,
            void                              *user_data
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer initiated successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``routine`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid timer id
     * - ``RTEMS_INVALID_NUMBER``
       - invalid interval

DESCRIPTION:
    This directive initiates the timer specified by id.  If the timer is
    running, it is automatically canceled before being initiated.  The timer is
    scheduled to fire after an interval ticks clock ticks has passed.  When the
    timer fires, the timer service routine routine will be invoked with the
    argument user_data.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: fire a timer at wall time
.. index:: rtems_timer_fire_when

.. _rtems_timer_fire_when:

TIMER_FIRE_WHEN - Fire timer when specified
-------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_fire_when(
            rtems_id                           id,
            rtems_time_of_day                 *wall_time,
            rtems_timer_service_routine_entry  routine,
            void                              *user_data
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer initiated successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``routine`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``wall_time`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid timer id
     * - ``RTEMS_NOT_DEFINED``
       - system date and time is not set
     * - ``RTEMS_INVALID_CLOCK``
       - invalid time of day

DESCRIPTION:
    This directive initiates the timer specified by id.  If the timer is
    running, it is automatically canceled before being initiated.  The timer is
    scheduled to fire at the time of day specified by wall_time.  When the
    timer fires, the timer service routine routine will be invoked with the
    argument user_data.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: initiate the Timer Server
.. index:: rtems_timer_initiate_server

.. _rtems_timer_initiate_server:

TIMER_INITIATE_SERVER - Initiate server for task-based timers
-------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_initiate_server(
            uint32_t         priority,
            uint32_t         stack_size,
            rtems_attribute  attribute_set
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Timer Server initiated successfully
     * - ``RTEMS_TOO_MANY``
       - too many tasks created

DESCRIPTION:
    This directive initiates the Timer Server task.  This task is responsible
    for executing all timers initiated via the
    ``rtems_timer_server_fire_after`` or ``rtems_timer_server_fire_when``
    directives.

NOTES:
    This directive could cause the calling task to be preempted.

    The Timer Server task is created using the ``rtems_task_create`` service
    and must be accounted for when configuring the system.

    Even through this directive invokes the ``rtems_task_create`` and
    ``rtems_task_start`` directives, it should only fail due to resource
    allocation problems.

.. raw:: latex

   \clearpage

.. index:: fire task-based a timer after an interval
.. index:: rtems_timer_server_fire_after

.. _rtems_timer_server_fire_after:

TIMER_SERVER_FIRE_AFTER - Fire task-based timer after interval
--------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_server_fire_after(
            rtems_id                           id,
            rtems_interval                     ticks,
            rtems_timer_service_routine_entry  routine,
            void                              *user_data
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer initiated successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``routine`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid timer id
     * - ``RTEMS_INVALID_NUMBER``
       - invalid interval
     * - ``RTEMS_INCORRECT_STATE``
       - Timer Server not initiated

DESCRIPTION:
    This directive initiates the timer specified by id and specifies that when
    it fires it will be executed by the Timer Server.

    If the timer is running, it is automatically canceled before being
    initiated.  The timer is scheduled to fire after an interval ticks clock
    ticks has passed.  When the timer fires, the timer service routine routine
    will be invoked with the argument user_data.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: fire a task-based timer at wall time
.. index:: rtems_timer_server_fire_when

.. _rtems_timer_server_fire_when:

TIMER_SERVER_FIRE_WHEN - Fire task-based timer when specified
-------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_server_fire_when(
            rtems_id                           id,
            rtems_time_of_day                 *wall_time,
            rtems_timer_service_routine_entry  routine,
            void                              *user_data
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer initiated successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``routine`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``wall_time`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid timer id
     * - ``RTEMS_NOT_DEFINED``
       - system date and time is not set
     * - ``RTEMS_INVALID_CLOCK``
       - invalid time of day
     * - ``RTEMS_INCORRECT_STATE``
       - Timer Server not initiated

DESCRIPTION:
    This directive initiates the timer specified by id and specifies that when
    it fires it will be executed by the Timer Server.

    If the timer is running, it is automatically canceled before being
    initiated.  The timer is scheduled to fire at the time of day specified by
    wall_time.  When the timer fires, the timer service routine routine will be
    invoked with the argument user_data.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: reset a timer
.. index:: rtems_timer_reset

.. _rtems_timer_reset:

TIMER_RESET - Reset an interval timer
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_timer_reset(
            rtems_id   id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - timer reset successfully
     * - ``RTEMS_INVALID_ID``
       - invalid timer id
     * - ``RTEMS_NOT_DEFINED``
       - attempted to reset a when or newly created timer

DESCRIPTION:
    This directive resets the timer associated with id.  This timer must have
    been previously initiated with either the ``rtems_timer_fire_after`` or
    ``rtems_timer_server_fire_after`` directive.  If active the timer is
    canceled, after which the timer is reinitiated using the same interval and
    timer service routine which the original ``rtems_timer_fire_after`` or
    ``rtems_timer_server_fire_after`` directive used.

NOTES:
    If the timer has not been used or the last usage of this timer was by a
    ``rtems_timer_fire_when`` or ``rtems_timer_server_fire_when`` directive,
    then the ``RTEMS_NOT_DEFINED`` error is returned.

    Restarting a cancelled after timer results in the timer being reinitiated
    with its previous timer service routine and interval.

    This directive will not cause the running task to be preempted.
