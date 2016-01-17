Timer Manager
#############

.. index:: timers

Introduction
============

The timer manager provides support for timer
facilities.  The directives provided by the timer manager are:

- ``rtems.timer_create`` - Create a timer

- ``rtems.timer_ident`` - Get ID of a timer

- ``rtems.timer_cancel`` - Cancel a timer

- ``rtems.timer_delete`` - Delete a timer

- ``rtems.timer_fire_after`` - Fire timer after interval

- ``rtems.timer_fire_when`` - Fire timer when specified

- ``rtems.timer_initiate_server`` - Initiate server for task-based timers

- ``rtems.timer_server_fire_after`` - Fire task-based timer after interval

- ``rtems.timer_server_fire_when`` - Fire task-based timer when specified

- ``rtems.timer_reset`` - Reset an interval timer

Background
==========

Required Support
----------------

A clock tick is required to support the functionality provided by this manager.

Timers
------

A timer is an RTEMS object which allows the
application to schedule operations to occur at specific times in
the future.  User supplied timer service routines are invoked by
either the ``rtems.clock_tick`` directive or
a special Timer Server task when the timer fires.  Timer service
routines may perform any operations or directives which normally
would be performed by the application code which invoked the``rtems.clock_tick`` directive.

The timer can be used to implement watchdog routines
which only fire to denote that an application error has
occurred.  The timer is reset at specific points in the
application to ensure that the watchdog does not fire.  Thus, if
the application does not reset the watchdog timer, then the
timer service routine will fire to indicate that the application
has failed to reach a reset point.  This use of a timer is
sometimes referred to as a "keep alive" or a "deadman" timer.

Timer Server
------------

The Timer Server task is responsible for executing the timer
service routines associated with all task-based timers.
This task executes at a priority higher than any RTEMS application
task, and is created non-preemptible, and thus can be viewed logically as
the lowest priority interrupt.

By providing a mechanism where timer service routines execute
in task rather than interrupt space, the application is
allowed a bit more flexibility in what operations a timer
service routine can perform.  For example, the Timer Server
can be configured to have a floating point context in which case
it would be safe to perform floating point operations
from a task-based timer.  Most of the time, executing floating
point instructions from an interrupt service routine
is not considered safe. However, since the Timer Server task
is non-preemptible, only directives allowed from an ISR can be
called in the timer service routine.

The Timer Server is designed to remain blocked until a
task-based timer fires.  This reduces the execution overhead
of the Timer Server.

Timer Service Routines
----------------------

The timer service routine should adhere to Ada calling
conventions and have a prototype similar to the following:

.. code:: c

    procedure User_Routine(
    Timer_ID  : in     RTEMS.ID;
    User_Data : in     System.Address
    );

Where the timer_id parameter is the RTEMS object ID
of the timer which is being fired and user_data is a pointer to
user-defined information which may be utilized by the timer
service routine.  The argument user_data may be NULL.

Operations
==========

Creating a Timer
----------------

The ``rtems.timer_create`` directive creates a timer by
allocating a Timer Control Block (TMCB), assigning the timer a
user-specified name, and assigning it a timer ID.  Newly created
timers do not have a timer service routine associated with them
and are not active.

Obtaining Timer IDs
-------------------

When a timer is created, RTEMS generates a unique
timer ID and assigns it to the created timer until it is
deleted.  The timer ID may be obtained by either of two methods.
First, as the result of an invocation of the``rtems.timer_create``
directive, the timer ID is stored in a user provided location.
Second, the timer ID may be obtained later using the``rtems.timer_ident`` directive.  The timer ID
is used by other directives to manipulate this timer.

Initiating an Interval Timer
----------------------------

The ``rtems.timer_fire_after``
and ``rtems.timer_server_fire_after``
directives initiate a timer to fire a user provided
timer service routine after the specified
number of clock ticks have elapsed.  When the interval has
elapsed, the timer service routine will be invoked from the``rtems.clock_tick`` directive if it was initiated
by the ``rtems.timer_fire_after`` directive
and from the Timer Server task if initiated by the``rtems.timer_server_fire_after`` directive.

Initiating a Time of Day Timer
------------------------------

The ``rtems.timer_fire_when``
and ``rtems.timer_server_fire_when``
directive initiate a timer to
fire a user provided timer service routine when the specified
time of day has been reached.  When the interval has elapsed,
the timer service routine will be invoked from the``rtems.clock_tick`` directive
by the ``rtems.timer_fire_when`` directive
and from the Timer Server task if initiated by the``rtems.timer_server_fire_when`` directive.

Canceling a Timer
-----------------

The ``rtems.timer_cancel`` directive is used to halt the
specified timer.  Once canceled, the timer service routine will
not fire unless the timer is reinitiated.  The timer can be
reinitiated using the ``rtems.timer_reset``,``rtems.timer_fire_after``, and``rtems.timer_fire_when`` directives.

Resetting a Timer
-----------------

The ``rtems.timer_reset`` directive is used to restore an
interval timer initiated by a previous invocation of``rtems.timer_fire_after`` or``rtems.timer_server_fire_after`` to
its original interval length.  If the
timer has not been used or the last usage of this timer
was by the ``rtems.timer_fire_when``
or ``rtems.timer_server_fire_when``
directive, then an error is returned.  The timer service routine
is not changed or fired by this directive.

Initiating the Timer Server
---------------------------

The ``rtems.timer_initiate_server`` directive is used to
allocate and start the execution of the Timer Server task.  The
application can specify both the stack size and attributes of the
Timer Server.  The Timer Server executes at a priority higher than
any application task and thus the user can expect to be preempted
as the result of executing the ``rtems.timer_initiate_server``
directive.

Deleting a Timer
----------------

The ``rtems.timer_delete`` directive is used to delete a timer.
If the timer is running and has not expired, the timer is
automatically canceled.  The timer’s control block is returned
to the TMCB free list when it is deleted.  A timer can be
deleted by a task other than the task which created the timer.
Any subsequent references to the timer’s name and ID are invalid.

Directives
==========

This section details the timer manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

TIMER_CREATE - Create a timer
-----------------------------
.. index:: create a timer

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Create (
    Name   : in     RTEMS.Name;
    ID     :    out RTEMS.ID;
    Result :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer created successfully
``RTEMS.INVALID_ADDRESS`` - ``id`` is NULL
``RTEMS.INVALID_NAME`` - invalid timer name
``RTEMS.TOO_MANY`` - too many timers created

**DESCRIPTION:**

This directive creates a timer.  The assigned timer
id is returned in id.  This id is used to access the timer with
other timer manager directives.  For control and maintenance of
the timer, RTEMS allocates a TMCB from the local TMCB free pool
and initializes it.

**NOTES:**

This directive will not cause the calling task to be
preempted.

TIMER_IDENT - Get ID of a timer
-------------------------------
.. index:: obtain the ID of a timer

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Ident (
    Name   : in     RTEMS.Name;
    ID     :    out RTEMS.ID;
    Result :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer identified successfully
``RTEMS.INVALID_ADDRESS`` - ``id`` is NULL
``RTEMS.INVALID_NAME`` - timer name not found

**DESCRIPTION:**

This directive obtains the timer id associated with
the timer name to be acquired.  If the timer name is not unique,
then the timer id will match one of the timers with that name.
However, this timer id is not guaranteed to correspond to the
desired timer.  The timer id is used to access this timer in
other timer related directives.

**NOTES:**

This directive will not cause the running task to be
preempted.

TIMER_CANCEL - Cancel a timer
-----------------------------
.. index:: cancel a timer

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Cancel (
    ID     : in     RTEMS.ID;
    Result :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer canceled successfully
``RTEMS.INVALID_ID`` - invalid timer id

**DESCRIPTION:**

This directive cancels the timer id.  This timer will
be reinitiated by the next invocation of ``rtems.timer_reset``,``rtems.timer_fire_after``, or``rtems.timer_fire_when`` with this id.

**NOTES:**

This directive will not cause the running task to be preempted.

TIMER_DELETE - Delete a timer
-----------------------------
.. index:: delete a timer

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Delete (
    ID     : in     RTEMS.ID;
    Result :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer deleted successfully
``RTEMS.INVALID_ID`` - invalid timer id

**DESCRIPTION:**

This directive deletes the timer specified by id.  If
the timer is running, it is automatically canceled.  The TMCB
for the deleted timer is reclaimed by RTEMS.

**NOTES:**

This directive will not cause the running task to be
preempted.

A timer can be deleted by a task other than the task
which created the timer.

TIMER_FIRE_AFTER - Fire timer after interval
--------------------------------------------
.. index:: fire a timer after an interval

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Fire_After (
    ID        : in     RTEMS.ID;
    Ticks     : in     RTEMS.Interval;
    Routine   : in     RTEMS.Timer_Service_Routine;
    User_Data : in     RTEMS.Address;
    Result    :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer initiated successfully
``RTEMS.INVALID_ADDRESS`` - ``routine`` is NULL
``RTEMS.INVALID_ID`` - invalid timer id
``RTEMS.INVALID_NUMBER`` - invalid interval

**DESCRIPTION:**

This directive initiates the timer specified by id.
If the timer is running, it is automatically canceled before
being initiated.  The timer is scheduled to fire after an
interval ticks clock ticks has passed.  When the timer fires,
the timer service routine routine will be invoked with the
argument user_data.

**NOTES:**

This directive will not cause the running task to be
preempted.

TIMER_FIRE_WHEN - Fire timer when specified
-------------------------------------------
.. index:: fire a timer at wall time

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Fire_When (
    ID        : in     RTEMS.ID;
    Wall_Time : in     RTEMS.Time_Of_Day;
    Routine   : in     RTEMS.Timer_Service_Routine;
    User_Data : in     RTEMS.Address;
    Result    :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer initiated successfully
``RTEMS.INVALID_ADDRESS`` - ``routine`` is NULL
``RTEMS.INVALID_ADDRESS`` - ``wall_time`` is NULL
``RTEMS.INVALID_ID`` - invalid timer id
``RTEMS.NOT_DEFINED`` - system date and time is not set
``RTEMS.INVALID_CLOCK`` - invalid time of day

**DESCRIPTION:**

This directive initiates the timer specified by id.
If the timer is running, it is automatically canceled before
being initiated.  The timer is scheduled to fire at the time of
day specified by wall_time.  When the timer fires, the timer
service routine routine will be invoked with the argument
user_data.

**NOTES:**

This directive will not cause the running task to be
preempted.

TIMER_INITIATE_SERVER - Initiate server for task-based timers
-------------------------------------------------------------
.. index:: initiate the Timer Server

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Initiate_Server (
    Server_Priority : in     RTEMS.Task_Priority;
    Stack_Size      : in     RTEMS.Unsigned32;
    Attribute_Set   : in     RTEMS.Attribute;
    Result          :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - Timer Server initiated successfully
``RTEMS.TOO_MANY`` - too many tasks created

**DESCRIPTION:**

This directive initiates the Timer Server task.  This task
is responsible for executing all timers initiated via the``rtems.timer_server_fire_after`` or``rtems.timer_server_fire_when`` directives.

**NOTES:**

This directive could cause the calling task to be preempted.

The Timer Server task is created using the``rtems.task_create`` service and must be accounted
for when configuring the system.

Even through this directive invokes the ``rtems.task_create``
and ``rtems.task_start`` directives, it should only fail
due to resource allocation problems.

TIMER_SERVER_FIRE_AFTER - Fire task-based timer after interval
--------------------------------------------------------------
.. index:: fire task-based a timer after an interval

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Fire_Server_After (
    ID        : in     RTEMS.ID;
    Ticks     : in     RTEMS.Interval;
    Routine   : in     RTEMS.Timer_Service_Routine;
    User_Data : in     RTEMS.Address;
    Result    :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer initiated successfully
``RTEMS.INVALID_ADDRESS`` - ``routine`` is NULL
``RTEMS.INVALID_ID`` - invalid timer id
``RTEMS.INVALID_NUMBER`` - invalid interval
``RTEMS.INCORRECT_STATE`` - Timer Server not initiated

**DESCRIPTION:**

This directive initiates the timer specified by id and specifies
that when it fires it will be executed by the Timer Server.

If the timer is running, it is automatically canceled before
being initiated.  The timer is scheduled to fire after an
interval ticks clock ticks has passed.  When the timer fires,
the timer service routine routine will be invoked with the
argument user_data.

**NOTES:**

This directive will not cause the running task to be
preempted.

TIMER_SERVER_FIRE_WHEN - Fire task-based timer when specified
-------------------------------------------------------------
.. index:: fire a task-based timer at wall time

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Fire_Server_When (
    ID        : in     RTEMS.ID;
    Wall_Time : in     RTEMS.Time_Of_Day;
    Routine   : in     RTEMS.Timer_Service_Routine;
    User_Data : in     RTEMS.Address;
    Result    :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer initiated successfully
``RTEMS.INVALID_ADDRESS`` - ``routine`` is NULL
``RTEMS.INVALID_ADDRESS`` - ``wall_time`` is NULL
``RTEMS.INVALID_ID`` - invalid timer id
``RTEMS.NOT_DEFINED`` - system date and time is not set
``RTEMS.INVALID_CLOCK`` - invalid time of day
``RTEMS.INCORRECT_STATE`` - Timer Server not initiated

**DESCRIPTION:**

This directive initiates the timer specified by id and specifies
that when it fires it will be executed by the Timer Server.

If the timer is running, it is automatically canceled before
being initiated.  The timer is scheduled to fire at the time of
day specified by wall_time.  When the timer fires, the timer
service routine routine will be invoked with the argument
user_data.

**NOTES:**

This directive will not cause the running task to be
preempted.

TIMER_RESET - Reset an interval timer
-------------------------------------
.. index:: reset a timer

**CALLING SEQUENCE:**

.. code:: c

    procedure Timer_Reset (
    ID     : in     RTEMS.ID;
    Result :    out RTEMS.Status_Codes
    );

**DIRECTIVE STATUS CODES:**

``RTEMS.SUCCESSFUL`` - timer reset successfully
``RTEMS.INVALID_ID`` - invalid timer id
``RTEMS.NOT_DEFINED`` - attempted to reset a when or newly created timer

**DESCRIPTION:**

This directive resets the timer associated with id.
This timer must have been previously initiated with either the``rtems.timer_fire_after`` or``rtems.timer_server_fire_after``
directive.  If active the timer is canceled,
after which the timer is reinitiated using the same interval and
timer service routine which the original``rtems.timer_fire_after````rtems.timer_server_fire_after``
directive used.

**NOTES:**

If the timer has not been used or the last usage of this timer
was by a ``rtems.timer_fire_when`` or``rtems.timer_server_fire_when``
directive, then the ``RTEMS.NOT_DEFINED`` error is
returned.

Restarting a cancelled after timer results in the timer being
reinitiated with its previous timer service routine and interval.

This directive will not cause the running task to be preempted.

.. COMMENT: COPYRIGHT (c) 1988-2007.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

