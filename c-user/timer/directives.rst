.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
