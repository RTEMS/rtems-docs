.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
