.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. index:: clock

Clock Manager
*************

Introduction
============

The clock manager provides support for time of day
and other time related capabilities.  The directives provided by
the clock manager are:

- rtems_clock_set_ - Set date and time

- rtems_clock_get_tod_ - Get date and time in TOD format

- rtems_clock_get_tod_timeval_ - Get date and time in timeval format

- rtems_clock_get_seconds_since_epoch_ - Get seconds since epoch

- rtems_clock_get_ticks_per_second_ - Get ticks per second

- rtems_clock_get_ticks_since_boot_ - Get current ticks counter value

- rtems_clock_tick_later_ - Get tick value in the future

- rtems_clock_tick_later_usec_ - Get tick value in the future in microseconds

- rtems_clock_tick_before_ - Is tick value is before a point in time

- rtems_clock_get_uptime_ - Get time since boot

- rtems_clock_get_uptime_timeval_ - Get time since boot in timeval format

- rtems_clock_get_uptime_seconds_ - Get seconds since boot

- rtems_clock_get_uptime_nanoseconds_ - Get nanoseconds since boot

Background
==========

Required Support
----------------

For the features provided by the clock manager to be utilized, periodic timer
interrupts are required.  Therefore, a real-time clock or hardware timer is
necessary to create the timer interrupts.  The clock tick directive
is normally called by the timer ISR to announce to RTEMS that a system clock
tick has occurred.  Elapsed time is measured in ticks.  A tick is defined to be
an integral number of microseconds which is specified by the user in the
Configuration Table.

.. _Time and Date Data Structures:

Time and Date Data Structures
-----------------------------

The clock facilities of the clock manager operate upon calendar time.  These
directives utilize the following date and time structure for the native time
and date format:

.. index:: rtems_time_of_day

.. code-block:: c

    struct rtems_tod_control {
        uint32_t year;   /* greater than 1987 */
        uint32_t month;  /* 1 - 12 */
        uint32_t day;    /* 1 - 31 */
        uint32_t hour;   /* 0 - 23 */
        uint32_t minute; /* 0 - 59 */
        uint32_t second; /* 0 - 59 */
        uint32_t ticks;  /* elapsed between seconds */
    };
    typedef struct rtems_tod_control rtems_time_of_day;

The native date and time format is the only format supported when setting the
system date and time using the ``rtems_clock_set`` directive.  Some
applications expect to operate on a *UNIX-style* date and time data structure.
The ``rtems_clock_get_tod_timeval`` always returns the date and time in
``struct timeval`` format.

The ``struct timeval`` data structure has two fields: ``tv_sec`` and
``tv_usec`` which are seconds and microseconds, respectively.  The ``tv_sec``
field in this data structure is the number of seconds since the POSIX epoch of
*January 1, 1970* but will never be prior to the RTEMS epoch of *January 1,
1988*.

.. index:: timeslicing

Clock Tick and Timeslicing
--------------------------

Timeslicing is a task scheduling discipline in which tasks of equal priority
are executed for a specific period of time before control of the CPU is passed
to another task.  It is also sometimes referred to as the automatic round-robin
scheduling algorithm.  The length of time allocated to each task is known as
the quantum or timeslice.

The system's timeslice is defined as an integral number of ticks, and is
specified in the Configuration Table.  The timeslice is defined for the entire
system of tasks, but timeslicing is enabled and disabled on a per task basis.

The clock tick directives implement timeslicing by decrementing the
running task's time-remaining counter when both timeslicing and preemption are
enabled.  If the task's timeslice has expired, then that task will be preempted
if there exists a ready task of equal priority.

.. index:: delays

Delays
------

A sleep timer allows a task to delay for a given interval or up until a given
time, and then wake and continue execution.  This type of timer is created
automatically by the ``rtems_task_wake_after`` and ``rtems_task_wake_when``
directives and, as a result, does not have an RTEMS ID.  Once activated, a
sleep timer cannot be explicitly deleted.  Each task may activate one and only
one sleep timer at a time.

.. index:: timeouts

Timeouts
--------

Timeouts are a special type of timer automatically created when the timeout
option is used on the ``rtems_message_queue_receive``, ``rtems_event_receive``,
``rtems_semaphore_obtain`` and ``rtems_region_get_segment`` directives.  Each
task may have one and only one timeout active at a time.  When a timeout
expires, it unblocks the task with a timeout status code.

Operations
==========

Announcing a Tick
-----------------

RTEMS provides the several clock tick directives which are called from the
user's real-time clock ISR to inform RTEMS that a tick has elapsed.  Depending
on the timer hardware capabilities the clock driver must choose the most
appropriate clock tick directive.  The tick frequency value, defined in
microseconds, is a configuration parameter found in the Configuration Table.
RTEMS divides one million microseconds (one second) by the number of
microseconds per tick to determine the number of calls to the clock tick
directive per second.  The frequency of clock tick calls determines the
resolution (granularity) for all time dependent RTEMS actions.  For example,
calling the clock tick directive ten times per second yields a higher
resolution than calling the clock tick two times per second.  The clock tick
directives are responsible for maintaining both calendar time and the dynamic
set of timers.

Setting the Time
----------------

The ``rtems_clock_set`` directive allows a task or an ISR to set the date and
time maintained by RTEMS.  If setting the date and time causes any outstanding
timers to pass their deadline, then the expired timers will be fired during the
invocation of the ``rtems_clock_set`` directive.

Obtaining the Time
------------------

RTEMS provides multiple directives which can be used by an application to obtain the current date and time or date and time related information.  These directives allow a task or an ISR to obtain the current date and time or date and time related information.  The current date and time can be returned in either native or *UNIX-style* format.  Additionally, the application can obtain date and time related information such as the number of seconds since the RTEMS epoch, the number of ticks since the executive was initialized, and the number of ticks per second.  The following directives are available:

``rtems_clock_get_tod``
  obtain native style date and time

``rtems_clock_get_time_value``
  obtain *UNIX-style* date and time

``rtems_clock_get_ticks_since_boot``
  obtain number of ticks since RTEMS was initialized

``rtems_clock_get_seconds_since_epoch``
  obtain number of seconds since RTEMS epoch

``rtems_clock_get_ticks_per_second``
  obtain number of clock ticks per second

Calendar time operations will return an error code if invoked before the date
and time have been set.

.. index:: rtems_clock_get

Transition Advice for the Obsolete rtems_clock_get
--------------------------------------------------

The method ``rtems_clock_get`` took an untyped pointer with an
options argument to indicate the time information desired. This has
been replaced with a set of typed directives whose name is of the form
``rtems_clock_get_INFORMATION`` where INFORMATION indicates the type of
information and possibly the format.  These methods directly correspond to
what were previously referred to ask "clock options." These strongly typed
were available for multiple releases in parallel with ``rtems_clock_get``
until that method was removed.


Directives
==========

This section details the clock manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_clock_set:

.. index:: set the time of day
.. index:: rtems_clock_set

CLOCK_SET - Set date and time
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_clock_set(
            rtems_time_of_day *time_buffer
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - date and time set successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``time_buffer`` is NULL
      * - ``RTEMS_INVALID_CLOCK``
        - invalid time of day

DESCRIPTION:
    This directive sets the system date and time.  The date, time, and ticks in
    the time_buffer structure are all range-checked, and an error is returned
    if any one is out of its valid range.

NOTES:
    Years before 1988 are invalid.

    The system date and time are based on the configured tick rate (number of
    microseconds in a tick).

    Setting the time forward may cause a higher priority task, blocked waiting
    on a specific time, to be made ready.  In this case, the calling task will
    be preempted after the next clock tick.

    Re-initializing RTEMS causes the system date and time to be reset to an
    uninitialized state.  Another call to ``rtems_clock_set`` is required to
    re-initialize the system date and time to application specific
    specifications.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_tod:

.. index:: obtain the time of day
.. index:: rtems_clock_get_tod

CLOCK_GET_TOD - Get date and time in TOD format
-----------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_clock_get_tod(
            rtems_time_of_day *time_buffer
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
	- current time obtained successfully
      * - ``RTEMS_NOT_DEFINED``
	- system date and time is not set
      * - ``RTEMS_INVALID_ADDRESS``
	- ``time_buffer`` is NULL

DESCRIPTION:
    This directive obtains the system date and time.  If the date and time has
    not been set with a previous call to ``rtems_clock_set``, then the
    ``RTEMS_NOT_DEFINED`` status code is returned.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.
    Re-initializing RTEMS causes the system date and time to be reset to an
    uninitialized state.  Another call to ``rtems_clock_set`` is required to
    re-initialize the system date and time to application specific
    specifications.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_tod_timeval:

.. index:: obtain the time of day
.. index:: rtems_clock_get_tod_timeval

CLOCK_GET_TOD_TIMEVAL - Get date and time in timeval format
-----------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_clock_get_tod_interval(
            struct timeval  *time
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table
      * - ``RTEMS_SUCCESSFUL``
	- current time obtained successfully
      * - ``RTEMS_NOT_DEFINED``
	- system date and time is not set
      * - ``RTEMS_INVALID_ADDRESS``
	- ``time`` is NULL

DESCRIPTION:
    This directive obtains the system date and time in POSIX ``struct timeval``
    format.  If the date and time has not been set with a previous call to
    ``rtems_clock_set``, then the ``RTEMS_NOT_DEFINED`` status code is
    returned.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.
    Re-initializing RTEMS causes the system date and time to be reset to an
    uninitialized state.  Another call to ``rtems_clock_set`` is required to
    re-initialize the system date and time to application specific
    specifications.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_seconds_since_epoch:

.. index:: obtain seconds since epoch
.. index:: rtems_clock_get_seconds_since_epoch

CLOCK_GET_SECONDS_SINCE_EPOCH - Get seconds since epoch
-------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_clock_get_seconds_since_epoch(
            rtems_interval *the_interval
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table
      * - ``RTEMS_SUCCESSFUL``
	- current time obtained successfully
      * - ``RTEMS_NOT_DEFINED``
	- system date and time is not set
      * - ``RTEMS_INVALID_ADDRESS``
	- ``the_interval`` is NULL

DESCRIPTION:
    This directive returns the number of seconds since the RTEMS epoch and the
    current system date and time.  If the date and time has not been set with a
    previous call to ``rtems_clock_set``, then the ``RTEMS_NOT_DEFINED`` status
    code is returned.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.
    Re-initializing RTEMS causes the system date and time to be reset to an
    uninitialized state.  Another call to ``rtems_clock_set`` is required to
    re-initialize the system date and time to application specific
    specifications.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_ticks_per_second:

.. index:: obtain seconds since epoch
.. index:: rtems_clock_get_ticks_per_second

CLOCK_GET_TICKS_PER_SECOND - Get ticks per second
-------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_interval rtems_clock_get_ticks_per_second(void);

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive returns the number of clock ticks per second.  This is
    strictly based upon the microseconds per clock tick that the application
    has configured.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_ticks_since_boot:

.. index:: obtain ticks since boot
.. index:: get current ticks counter value
.. index:: rtems_clock_get_ticks_since_boot

CLOCK_GET_TICKS_SINCE_BOOT - Get current ticks counter value
------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_interval rtems_clock_get_ticks_since_boot(void);

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:

    This directive returns the current tick counter value.  With a 1ms clock
    tick, this counter overflows after 50 days since boot.  This is the
    historical measure of uptime in an RTEMS system.  The newer service
    ``rtems_clock_get_uptime`` is another and potentially more accurate way of
    obtaining similar information.

NOTES:

    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_clock_tick_later:

.. index:: rtems_clock_tick_later

CLOCK_TICK_LATER - Get tick value in the future
-----------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_interval rtems_clock_tick_later(
            rtems_interval delta
        );

DESCRIPTION:
    Returns the ticks counter value delta ticks in the future.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_clock_tick_later_usec:

.. index:: rtems_clock_tick_later_usec

CLOCK_TICK_LATER_USEC - Get tick value in the future in microseconds
--------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_interval rtems_clock_tick_later_usec(
            rtems_interval delta_in_usec
        );

DESCRIPTION:
    Returns the ticks counter value at least delta microseconds in the future.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_clock_tick_before:

.. index:: rtems_clock_tick_before

CLOCK_TICK_BEFORE - Is tick value is before a point in time
-----------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_interval rtems_clock_tick_before(
            rtems_interval tick
        );

DESCRIPTION:
    Returns true if the current ticks counter value indicates a time before the
    time specified by the tick value and false otherwise.

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.

EXAMPLE:
    .. code-block:: c

        status busy( void )
        {
            rtems_interval timeout = rtems_clock_tick_later_usec( 10000 );
            do {
                if ( ok() ) {
                    return success;
                }
            } while ( rtems_clock_tick_before( timeout ) );
            return timeout;
        }

.. raw:: latex

   \clearpage

.. _rtems_clock_get_uptime:

.. index:: clock get uptime
.. index:: uptime
.. index:: rtems_clock_get_uptime

CLOCK_GET_UPTIME - Get the time since boot
------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_clock_get_uptime(
            struct timespec *uptime
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table
      * - ``RTEMS_SUCCESSFUL``
	- clock tick processed successfully
      * - ``RTEMS_INVALID_ADDRESS``
	- ``time_buffer`` is ``NULL``

DESCRIPTION:
    This directive returns the seconds and nanoseconds since the system was
    booted.  If the BSP supports nanosecond clock accuracy, the time reported
    will probably be different on every call.

NOTES:
    This directive may be called from an ISR.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_uptime_timeval:

.. index:: clock get uptime interval
.. index:: uptime
.. index:: rtems_clock_get_uptime_timeval

CLOCK_GET_UPTIME_TIMEVAL - Get the time since boot in timeval format
--------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_clock_get_uptime_timeval(
            struct timeval *uptime
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive returns the seconds and microseconds since the system was
    booted.  If the BSP supports nanosecond clock accuracy, the time reported
    will probably be different on every call.

NOTES:
    This directive may be called from an ISR.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_uptime_seconds:

.. index:: clock get uptime seconds
.. index:: uptime
.. index:: rtems_clock_get_uptime_seconds

CLOCK_GET_UPTIME_SECONDS - Get the seconds since boot
-----------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        time_t rtems_clock_get_uptime_seconds(void);

DIRECTIVE STATUS CODES:
    The system uptime in seconds.

DESCRIPTION:
    This directive returns the seconds since the system was booted.

NOTES:
    This directive may be called from an ISR.

.. raw:: latex

   \clearpage

.. _rtems_clock_get_uptime_nanoseconds:

.. index:: clock get nanoseconds uptime
.. index:: uptime
.. index:: rtems_clock_get_uptime_nanoseconds

CLOCK_GET_UPTIME_NANOSECONDS - Get the nanoseconds since boot
-------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        uint64_t rtems_clock_get_uptime_nanoseconds(void);

DIRECTIVE STATUS CODES:
    The system uptime in nanoseconds.

DESCRIPTION:
    This directive returns the nanoseconds since the system was booted.

NOTES:
    This directive may be called from an ISR.
