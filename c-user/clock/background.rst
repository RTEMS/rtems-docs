.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2021 embedded brains GmbH & Co. KG
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

Required Support
----------------

For the features provided by the Clock Manager to be utilized, a :term:`Clock
Driver` is required.  The Clock Driver usually provides a clock interrupt which
is serviced on each configured processor at each :term:`clock tick`.  In
addition, the Clock Driver provides three clock sources:

* clock tick

* :term:`CLOCK_REALTIME`

* :term:`CLOCK_MONOTONIC`

The time of these clock sources advances at each clock tick.  This yields the
time of the clock sources in a coarse resolution.  To get the time of the
``CLOCK_REALTIME`` or ``CLOCK_MONOTONIC`` clock sources in a higher resolution,
the Clock Driver may use a clock device to get the time between clock ticks.

.. _Time and Date Data Structures:

Time and Date Data Structures
-----------------------------

The clock facilities of the Clock Manager operate upon calendar time.  These
directives utilize the following date and time structure for the native time
and date format:

.. index:: rtems_time_of_day

.. code-block:: c

    typedef struct {
        uint32_t year;   /* greater than 1987 */
        uint32_t month;  /* 1 - 12 */
        uint32_t day;    /* 1 - 31 */
        uint32_t hour;   /* 0 - 23 */
        uint32_t minute; /* 0 - 59 */
        uint32_t second; /* 0 - 59 */
        uint32_t ticks;  /* elapsed between seconds */
    } rtems_time_of_day;

The native date and time format is the only format supported when setting the
system date and time using the :ref:`InterfaceRtemsClockSet` directive.  Some
applications expect to operate on a *UNIX-style* date and time data structure.
For example, the :ref:`InterfaceRtemsClockGetTodTimeval` returns the date and
time in ``struct timeval`` format.

.. index:: struct timeval
.. index:: struct timespec

Some directives use data structures defined by :term:`POSIX`.  The ``struct
timeval`` data structure has two members: ``tv_sec`` and ``tv_usec`` which are
seconds and microseconds, respectively.  The ``struct timespec`` data structure
has two members: ``tv_sec`` and ``tv_nsec`` which are seconds and nanoseconds,
respectively.  For :term:`CLOCK_REALTIME` time points, the ``tv_sec`` member in
these data structures is the number of seconds since the :term:`Unix epoch` but
will never be prior to the :term:`RTEMS epoch`.

.. index:: struct bintime
.. index:: sbintime_t

The ``struct bintime`` and ``sbintime_t`` time formats used by some directives
originate in FreeBSD.  The ``struct bintime`` data structure which represents
time in a binary time format has two members: ``sec`` and ``frac`` which are
seconds and fractions of a second in units of :math:`1 / 2^{64}` seconds,
respectively.  The ``sbintime_t`` type is a signed 64-bit integer type used to
represent time in units of :math:`1 / 2^{32}` seconds.

.. index:: timeslicing

Clock Tick and Timeslicing
--------------------------

Timeslicing is a task scheduling discipline in which tasks of equal priority
are executed for a specific period of time before control of the CPU is passed
to another task.  It is also sometimes referred to as the automatic round-robin
scheduling algorithm.  The length of time allocated to each task is known as
the quantum or timeslice.

The system's timeslice is defined as an integral number of ticks, and is
specified by the :ref:`CONFIGURE_TICKS_PER_TIMESLICE` application configuration
option.  The timeslice is defined for the entire system of tasks, but
timeslicing is enabled and disabled on a per task basis.

The clock tick directives implement timeslicing by decrementing the
running task's time-remaining counter when both timeslicing and preemption are
enabled.  If the task's timeslice has expired, then that task will be preempted
if there exists a ready task of equal priority.

.. index:: delays

Delays
------

A sleep timer allows a task to delay for a given interval or up until a given
time, and then wake and continue execution.  This type of timer is created
automatically by the :ref:`InterfaceRtemsTaskWakeAfter` and
:ref:`InterfaceRtemsTaskWakeWhen` directives and, as a result, does not have an
object identifier.  Once activated, a sleep timer cannot be explicitly deleted.
Each task may activate one and only one sleep timer at a time.

.. index:: timeouts

Timeouts
--------

Timeouts are a special type of timer automatically created when the timeout
option is used on the :ref:`InterfaceRtemsBarrierWait`,
:ref:`InterfaceRtemsEventReceive`, :ref:`InterfaceRtemsMessageQueueReceive`,
:ref:`InterfaceRtemsRegionGetSegment`, and :ref:`InterfaceRtemsSemaphoreObtain`
directives.  Each task may have one and only one timeout active at a time.
When a timeout expires, it unblocks the task with a timeout status code.
