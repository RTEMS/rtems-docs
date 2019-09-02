.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. Copyright (C) 2017 Kuan-Hsun Chen.

.. index:: rate mononitonic tasks
.. index:: periodic tasks

Rate Monotonic Manager
**********************

Introduction
============

The rate monotonic manager provides facilities to implement tasks which execute
in a periodic fashion.  Critically, it also gathers information about the
execution of those periods and can provide important statistics to the user
which can be used to analyze and tune the application.  The directives provided
by the rate monotonic manager are:

- rtems_rate_monotonic_create_ - Create a rate monotonic period

- rtems_rate_monotonic_ident_ - Get ID of a period

- rtems_rate_monotonic_cancel_ - Cancel a period

- rtems_rate_monotonic_delete_ - Delete a rate monotonic period

- rtems_rate_monotonic_period_ - Conclude current/Start next period

- rtems_rate_monotonic_get_status_ - Obtain status from a period

- rtems_rate_monotonic_get_statistics_ - Obtain statistics from a period

- rtems_rate_monotonic_reset_statistics_ - Reset statistics for a period

- rtems_rate_monotonic_reset_all_statistics_ - Reset statistics for all periods

- rtems_rate_monotonic_report_statistics_ - Print period statistics report

Background
==========

The rate monotonic manager provides facilities to manage the execution of
periodic tasks.  This manager was designed to support application designers who
utilize the Rate Monotonic Scheduling Algorithm (RMS) to ensure that their
periodic tasks will meet their deadlines, even under transient overload
conditions.  Although designed for hard real-time systems, the services
provided by the rate monotonic manager may be used by any application which
requires periodic tasks.

Rate Monotonic Manager Required Support
---------------------------------------

A clock tick is required to support the functionality provided by this manager.

Period Statistics
-----------------

This manager maintains a set of statistics on each period object.  These
statistics are reset implictly at period creation time and may be reset or
obtained at any time by the application.  The following is a list of the
information kept:

``owner``
  is the id of the thread that owns this period.

``count``
  is the total number of periods executed.

``missed_count``
  is the number of periods that were missed.

``min_cpu_time``
  is the minimum amount of CPU execution time consumed on any execution of the
  periodic loop.

``max_cpu_time``
  is the maximum amount of CPU execution time consumed on any execution of the
  periodic loop.

``total_cpu_time``
  is the total amount of CPU execution time consumed by executions of the
  periodic loop.

``min_wall_time``
  is the minimum amount of wall time that passed on any execution of the
  periodic loop.

``max_wall_time``
  is the maximum amount of wall time that passed on any execution of the
  periodic loop.

``total_wall_time``
  is the total amount of wall time that passed during executions of the
  periodic loop.

Each period is divided into two consecutive phases.  The period starts with the
active phase of the task and is followed by the inactive phase of the task.  In
the inactive phase the task is blocked and waits for the start of the next
period.  The inactive phase is skipped in case of a period miss.  The wall time
includes the time during the active phase of the task on which the task is not
executing on a processor.  The task is either blocked (for example it waits for
a resource) or a higher priority tasks executes, thus preventing it from
executing.  In case the wall time exceeds the period time, then this is a
period miss.  The gap between the wall time and the period time is the margin
between a period miss or success.

The period statistics information is inexpensive to maintain and can provide
very useful insights into the execution characteristics of a periodic task
loop.  But it is just information.  The period statistics reported must be
analyzed by the user in terms of what the applications is.  For example, in an
application where priorities are assigned by the Rate Monotonic Algorithm, it
would be very undesirable for high priority (i.e. frequency) tasks to miss
their period.  Similarly, in nearly any application, if a task were supposed to
execute its periodic loop every 10 milliseconds and it averaged 11
milliseconds, then application requirements are not being met.

The information reported can be used to determine the "hot spots" in the
application.  Given a period's id, the user can determine the length of that
period.  From that information and the CPU usage, the user can calculate the
percentage of CPU time consumed by that periodic task.  For example, a task
executing for 20 milliseconds every 200 milliseconds is consuming 10 percent of
the processor's execution time.  This is usually enough to make it a good
candidate for optimization.

However, execution time alone is not enough to gauge the value of optimizing a
particular task.  It is more important to optimize a task executing 2
millisecond every 10 milliseconds (20 percent of the CPU) than one executing 10
milliseconds every 100 (10 percent of the CPU).  As a general rule of thumb,
the higher frequency at which a task executes, the more important it is to
optimize that task.

.. index:: periodic task, definition

Periodicity Definitions
----------------------------------

A periodic task is one which must be executed at a regular interval.  The
interval between successive iterations of the task is referred to as its
period.  Periodic tasks can be characterized by the length of their period and
execution time.  The period and execution time of a task can be used to
determine the processor utilization for that task.  Processor utilization is
the percentage of processor time used and can be calculated on a per-task or
system-wide basis.  Typically, the task's worst-case execution time will be
less than its period.  For example, a periodic task's requirements may state
that it should execute for 10 milliseconds every 100 milliseconds.  Although
the execution time may be the average, worst, or best case, the worst-case
execution time is more appropriate for use when analyzing system behavior under
transient overload conditions... index:: aperiodic task, definition

In contrast, an aperiodic task executes at irregular intervals and has only a
soft deadline.  In other words, the deadlines for aperiodic tasks are not
rigid, but adequate response times are desirable.  For example, an aperiodic
task may process user input from a terminal.

.. index:: sporadic task, definition

Finally, a sporadic task is an aperiodic task with a hard deadline and minimum
interarrival time.  The minimum interarrival time is the minimum period of time
which exists between successive iterations of the task.  For example, a
sporadic task could be used to process the pressing of a fire button on a
joystick.  The mechanical action of the fire button ensures a minimum time
period between successive activations, but the missile must be launched by a
hard deadline.

.. index:: Rate Monotonic Scheduling Algorithm, definition
.. index:: RMS Algorithm, definition

Rate Monotonic Scheduling Algorithm
-----------------------------------

The Rate Monotonic Scheduling Algorithm (RMS) is important to real-time systems
designers because it allows one to sufficiently guarantee that a set of tasks
is schedulable (see :cite:`Liu:1973:Scheduling`, :cite:`Lehoczky:1989:RM`,
:cite:`Sha:1990:Ada`, :cite:`Burns:1991:Review`).

A set of tasks is said to be schedulable if all of the tasks can meet their
deadlines.  RMS provides a set of rules which can be used to perform
a guaranteed schedulability analysis for a task set.  This analysis determines
whether a task set is schedulable under worst-case conditions and emphasizes
the predictability of the system's behavior.  It has been proven that:

.. sidebar:: *RMS*

  RMS is an optimal fixed-priority algorithm for scheduling independent,
  preemptible, periodic tasks on a single processor.

RMS is optimal in the sense that if a set of tasks can be scheduled by any
fixed-priority algorithm, then RMS will be able to schedule that task set.
RMS bases it schedulability analysis on the processor utilization level below
which all deadlines can be met.

RMS calls for the static assignment of task priorities based upon their period.
The shorter a task's period, the higher its priority.  For example, a task with
a 1 millisecond period has higher priority than a task with a 100 millisecond
period.  If two tasks have the same period, then RMS does not distinguish
between the tasks.  However, RTEMS specifies that when given tasks of equal
priority, the task which has been ready longest will execute first.  RMS's
priority assignment scheme does not provide one with exact numeric values for
task priorities.  For example, consider the following task set and priority
assignments:

+--------------------+---------------------+---------------------+
| Task               | Period              | Priority            |
|                    | (in milliseconds)   |                     |
+====================+=====================+=====================+
|         1          |         100         |         Low         |
+--------------------+---------------------+---------------------+
|         2          |          50         |       Medium        |
+--------------------+---------------------+---------------------+
|         3          |          50         |       Medium        |
+--------------------+---------------------+---------------------+
|         4          |          25         |        High         |
+--------------------+---------------------+---------------------+

RMS only calls for task 1 to have the lowest priority, task 4 to have the
highest priority, and tasks 2 and 3 to have an equal priority between that of
tasks 1 and 4.  The actual RTEMS priorities assigned to the tasks must only
adhere to those guidelines.

Many applications have tasks with both hard and soft deadlines.  The tasks with
hard deadlines are typically referred to as the critical task set, with the
soft deadline tasks being the non-critical task set.  The critical task set can
be scheduled using RMS, with the non-critical tasks not executing under
transient overload, by simply assigning priorities such that the lowest
priority critical task (i.e. longest period) has a higher priority than the
highest priority non-critical task.  Although RMS may be used to assign
priorities to the non-critical tasks, it is not necessary.  In this instance,
schedulability is only guaranteed for the critical task set.

.. index:: RMS schedulability analysis

Schedulability Analysis
-----------------------

RMS allows application designers to ensure that tasks can meet all deadlines under fixed-priority assignment,
even under transient overload, without knowing exactly when any given task will
execute by applying proven schedulability analysis rules.

Assumptions
^^^^^^^^^^^

The schedulability analysis rules for RMS were developed based on the following
assumptions:

- The requests for all tasks for which hard deadlines exist are periodic, with
  a constant interval between requests.

- Each task must complete before the next request for it occurs.

- The tasks are independent in that a task does not depend on the initiation or
  completion of requests for other tasks.

- The execution time for each task without preemption or interruption is
  constant and does not vary.

- Any non-periodic tasks in the system are special.  These tasks displace
  periodic tasks while executing and do not have hard, critical deadlines.

Once the basic schedulability analysis is understood, some of the above
assumptions can be relaxed and the side-effects accounted for.

.. index:: RMS Processor Utilization Rule

Processor Utilization Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Processor Utilization Rule requires that processor utilization be
calculated based upon the period and execution time of each task.
The fraction of processor time spent executing task index is ``Time(i)
/ Period(i)``.  The processor utilization can be calculated as follows
where n is the number of tasks in the set being analyzed:

.. math::

    Utilization = \sum_{i=1}^{n} Time_i/Period_i

To ensure schedulability even under transient overload, the processor
utilization must adhere to the following rule:

.. math::

    maximumUtilization = n * (2^{\frac{1}{n}} - 1)

As the number of tasks increases, the above formula approaches ln(2) for a
worst-case utilization factor of approximately 0.693.  Many tasks sets can be
scheduled with a greater utilization factor.  In fact, the average processor
utilization threshold for a randomly generated task set is approximately 0.88.
See more detail in :cite:`Liu:1973:Scheduling`.

Processor Utilization Rule Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example illustrates the application of the Processor Utilization Rule to
an application with three critical periodic tasks.  The following table details
the RMS priority, period, execution time, and processor utilization for each
task:

+------------+----------+--------+-----------+-------------+
| Task       | RMS      | Period | Execution | Processor   |
|            | Priority |        | Time      | Utilization |
+============+==========+========+===========+=============+
|     1      |   High   |  100   |    15     |    0.15     |
+------------+----------+--------+-----------+-------------+
|     2      |  Medium  |  200   |    50     |    0.25     |
+------------+----------+--------+-----------+-------------+
|     3      |   Low    |  300   |   100     |    0.33     |
+------------+----------+--------+-----------+-------------+

The total processor utilization for this task set is 0.73 which is below the
upper bound of 3 * (2**(1/3) - 1), or 0.779, imposed by the Processor
Utilization Rule.  Therefore, this task set is guaranteed to be schedulable
using RMS.

.. index:: RMS First Deadline Rule

First Deadline Rule
^^^^^^^^^^^^^^^^^^^

If a given set of tasks do exceed the processor utilization upper limit imposed
by the Processor Utilization Rule, they can still be guaranteed to meet all
their deadlines by application of the First Deadline Rule.  This rule can be
stated as follows:

For a given set of independent periodic tasks, if each task meets its first
deadline when all tasks are started at the same time, then the deadlines will
always be met for any combination of start times.

A key point with this rule is that ALL periodic tasks are assumed to start at
the exact same instant in time.  Although this assumption may seem to be
invalid, RTEMS makes it quite easy to ensure.  By having a non-preemptible user
initialization task, all application tasks, regardless of priority, can be
created and started before the initialization deletes itself.  This technique
ensures that all tasks begin to compete for execution time at the same instant
- when the user initialization task deletes itself.
See more detail in :cite:`Lehoczky:1989:RM`.

First Deadline Rule Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The First Deadline Rule can ensure schedulability even when the Processor
Utilization Rule fails.  The example below is a modification of the Processor
Utilization Rule example where task execution time has been increased from 15
to 25 units.  The following table details the RMS priority, period, execution
time, and processor utilization for each task:

+------------+----------+--------+-----------+-------------+
| Task       | RMS      | Period | Execution | Processor   |
|            | Priority |        | Time      | Utilization |
+============+==========+========+===========+=============+
|     1      |   High   |  100   |    25     |    0.25     |
+------------+----------+--------+-----------+-------------+
|     2      |  Medium  |  200   |    50     |    0.25     |
+------------+----------+--------+-----------+-------------+
|     3      |   Low    |  300   |   100     |    0.33     |
+------------+----------+--------+-----------+-------------+

The total processor utilization for the modified task set is 0.83 which is
above the upper bound of 3 * (2**(1/3) - 1), or 0.779, imposed by the Processor
Utilization Rule.  Therefore, this task set is not guaranteed to be schedulable
using RMS.  However, the First Deadline Rule can guarantee the schedulability
of this task set.  This rule calls for one to examine each occurrence of
deadline until either all tasks have met their deadline or one task failed to
meet its first deadline.  The following table details the time of each deadline
occurrence, the maximum number of times each task may have run, the total
execution time, and whether all the deadlines have been met:

+----------+------+------+------+----------------------+---------------+
| Deadline | Task | Task | Task | Total                | All Deadlines |
| Time     | 1    | 2    | 3    | Execution Time       | Met?          |
+==========+======+======+======+======================+===============+
|   100    |  1   |  1   |  1   |  25 + 50 + 100 = 175 |      NO       |
+----------+------+------+------+----------------------+---------------+
|   200    |  2   |  1   |  1   |  50 + 50 + 100 = 200 |     YES       |
+----------+------+------+------+----------------------+---------------+

The key to this analysis is to recognize when each task will execute.  For
example at time 100, task 1 must have met its first deadline, but tasks 2 and 3
may also have begun execution.  In this example, at time 100 tasks 1 and 2 have
completed execution and thus have met their first deadline.  Tasks 1 and 2 have
used (25 + 50) = 75 time units, leaving (100 - 75) = 25 time units for task 3
to begin.  Because task 3 takes 100 ticks to execute, it will not have
completed execution at time 100.  Thus at time 100, all of the tasks except
task 3 have met their first deadline.

At time 200, task 1 must have met its second deadline and task 2 its first
deadline.  As a result, of the first 200 time units, task 1 uses (2 * 25) = 50
and task 2 uses 50, leaving (200 - 100) time units for task 3.  Task 3 requires
100 time units to execute, thus it will have completed execution at time 200.
Thus, all of the tasks have met their first deadlines at time 200, and the task
set is schedulable using the First Deadline Rule.

Relaxation of Assumptions
^^^^^^^^^^^^^^^^^^^^^^^^^

The assumptions used to develop the RMS schedulability rules are uncommon in
most real-time systems.  For example, it was assumed that tasks have constant
unvarying execution time.  It is possible to relax this assumption, simply by
using the worst-case execution time of each task.

Another assumption is that the tasks are independent.  This means that the
tasks do not wait for one another or contend for resources.  This assumption
can be relaxed by accounting for the amount of time a task spends waiting to
acquire resources.  Similarly, each task's execution time must account for any
I/O performed and any RTEMS directive calls.

In addition, the assumptions did not account for the time spent executing
interrupt service routines.  This can be accounted for by including all the
processor utilization by interrupt service routines in the utilization
calculation.  Similarly, one should also account for the impact of delays in
accessing local memory caused by direct memory access and other processors
accessing local dual-ported memory.

The assumption that nonperiodic tasks are used only for initialization or
failure-recovery can be relaxed by placing all periodic tasks in the critical
task set.  This task set can be scheduled and analyzed using RMS.  All
nonperiodic tasks are placed in the non-critical task set.  Although the
critical task set can be guaranteed to execute even under transient overload,
the non-critical task set is not guaranteed to execute.

In conclusion, the application designer must be fully cognizant of the system
and its run-time behavior when performing schedulability analysis for a system
using RMS.  Every hardware and software factor which impacts the execution time
of each task must be accounted for in the schedulability analysis.

Operations
==========

Creating a Rate Monotonic Period
--------------------------------

The ``rtems_rate_monotonic_create`` directive creates a rate monotonic period
which is to be used by the calling task to delineate a period.  RTEMS allocates
a Period Control Block (PCB) from the PCB free list.  This data structure is
used by RTEMS to manage the newly created rate monotonic period.  RTEMS returns
a unique period ID to the application which is used by other rate monotonic
manager directives to access this rate monotonic period.

Manipulating a Period
---------------------

The ``rtems_rate_monotonic_period`` directive is used to establish and maintain
periodic execution utilizing a previously created rate monotonic period.  Once
initiated by the ``rtems_rate_monotonic_period`` directive, the period is said
to run until it either expires or is reinitiated.  The state of the rate
monotonic period results in one of the following scenarios:

- If the rate monotonic period is running, the calling task will be blocked for
  the remainder of the outstanding period and, upon completion of that period,
  the period will be reinitiated with the specified period.

- If the rate monotonic period is not currently running and has not expired, it
  is initiated with a length of period ticks and the calling task returns
  immediately.

- If the rate monotonic period has expired before the task invokes the
  ``rtems_rate_monotonic_period`` directive, the postponed job will be released
  until there is no more postponed jobs. The calling task returns immediately
  with a timeout error status. In the watchdog routine, the period will still
  be updated periodically and track the count of the postponed jobs :cite:`Chen:2016:Overrun`.
  Please note, the count of the postponed jobs is only saturated until 0xffffffff.

Obtaining the Status of a Period
--------------------------------

If the ``rtems_rate_monotonic_period`` directive is invoked with a period of
``RTEMS_PERIOD_STATUS`` ticks, the current state of the specified rate
monotonic period will be returned.  The following table details the
relationship between the period's status and the directive status code returned
by the ``rtems_rate_monotonic_period`` directive:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_SUCCESSFUL``
   - period is running
 * - ``RTEMS_TIMEOUT``
   - period has expired
 * - ``RTEMS_NOT_DEFINED``
   - period has never been initiated

Obtaining the status of a rate monotonic period does not alter the state or
length of that period.

Canceling a Period
------------------

The ``rtems_rate_monotonic_cancel`` directive is used to stop the period
maintained by the specified rate monotonic period.  The period is stopped and
the rate monotonic period can be reinitiated using the
``rtems_rate_monotonic_period`` directive.

Deleting a Rate Monotonic Period
--------------------------------

The ``rtems_rate_monotonic_delete`` directive is used to delete a rate
monotonic period.  If the period is running and has not expired, the period is
automatically canceled.  The rate monotonic period's control block is returned
to the PCB free list when it is deleted.  A rate monotonic period can be
deleted by a task other than the task which created the period.

Examples
--------

The following sections illustrate common uses of rate monotonic periods to
construct periodic tasks.

Simple Periodic Task
--------------------

This example consists of a single periodic task which, after initialization,
executes every 100 clock ticks.

.. code-block:: c
    :linenos:

    rtems_task Periodic_task(rtems_task_argument arg)
    {
        rtems_name        name;
        rtems_id          period;
        rtems_status_code status;
        name = rtems_build_name( 'P', 'E', 'R', 'D' );
        status = rtems_rate_monotonic_create( name, &period );
        if ( status != RTEMS_SUCCESSFUL ) {
            printf( "rtems_monotonic_create failed with status of %d.\n", status );
            exit( 1 );
        }
        while ( 1 ) {
            if ( rtems_rate_monotonic_period( period, 100 ) == RTEMS_TIMEOUT )
                break;
            /* Perform some periodic actions */
        }
        /* missed period so delete period and SELF */
        status = rtems_rate_monotonic_delete( period );
        if ( status != RTEMS_SUCCESSFUL ) {
            printf( "rtems_rate_monotonic_delete failed with status of %d.\n", status );
            exit( 1 );
        }
        status = rtems_task_delete( RTEMS_SELF );    /* should not return */
        printf( "rtems_task_delete returned with status of %d.\n", status );
        exit( 1 );
    }

The above task creates a rate monotonic period as part of its initialization.
The first time the loop is executed, the ``rtems_rate_monotonic_period``
directive will initiate the period for 100 ticks and return immediately.
Subsequent invocations of the ``rtems_rate_monotonic_period`` directive will
result in the task blocking for the remainder of the 100 tick period.  If, for
any reason, the body of the loop takes more than 100 ticks to execute, the
``rtems_rate_monotonic_period`` directive will return the ``RTEMS_TIMEOUT``
status. If the above task misses its deadline, it will delete the rate
monotonic period and itself.

Task with Multiple Periods
--------------------------

This example consists of a single periodic task which, after initialization,
performs two sets of actions every 100 clock ticks.  The first set of actions
is performed in the first forty clock ticks of every 100 clock ticks, while the
second set of actions is performed between the fortieth and seventieth clock
ticks.  The last thirty clock ticks are not used by this task.

.. code-block:: c
    :linenos:

    rtems_task Periodic_task(rtems_task_argument arg)
    {
        rtems_name        name_1, name_2;
        rtems_id          period_1, period_2;
        name_1 = rtems_build_name( 'P', 'E', 'R', '1' );
        name_2 = rtems_build_name( 'P', 'E', 'R', '2' );
        (void ) rtems_rate_monotonic_create( name_1, &period_1 );
        (void ) rtems_rate_monotonic_create( name_2, &period_2 );
        while ( 1 ) {
            if ( rtems_rate_monotonic_period( period_1, 100 ) == RTEMS_TIMEOUT )
                break;
            if ( rtems_rate_monotonic_period( period_2, 40 ) == RTEMS_TIMEOUT )
            break;
            /*
             *  Perform first set of actions between clock
             *  ticks 0 and 39 of every 100 ticks.
             */
            if ( rtems_rate_monotonic_period( period_2, 30 ) == RTEMS_TIMEOUT )
                break;
            /*
             *  Perform second set of actions between clock 40 and 69
             *  of every 100 ticks.  THEN ...
             *
             *  Check to make sure we didn't miss the period_2 period.
             */
            if ( rtems_rate_monotonic_period( period_2, RTEMS_PERIOD_STATUS ) == RTEMS_TIMEOUT )
                break;
            (void) rtems_rate_monotonic_cancel( period_2 );
        }
        /* missed period so delete period and SELF */
        (void ) rtems_rate_monotonic_delete( period_1 );
        (void ) rtems_rate_monotonic_delete( period_2 );
        (void ) rtems_task_delete( RTEMS_SELF );
    }

The above task creates two rate monotonic periods as part of its
initialization.  The first time the loop is executed, the
``rtems_rate_monotonic_period`` directive will initiate the period_1 period for
100 ticks and return immediately.  Subsequent invocations of the
``rtems_rate_monotonic_period`` directive for period_1 will result in the task
blocking for the remainder of the 100 tick period.  The period_2 period is used
to control the execution time of the two sets of actions within each 100 tick
period established by period_1.  The ``rtems_rate_monotonic_cancel( period_2
)`` call is performed to ensure that the period_2 period does not expire while
the task is blocked on the period_1 period.  If this cancel operation were not
performed, every time the ``rtems_rate_monotonic_period( period_2, 40 )`` call
is executed, except for the initial one, a directive status of
``RTEMS_TIMEOUT`` is returned.  It is important to note that every time this
call is made, the period_2 period will be initiated immediately and the task
will not block.

If, for any reason, the task misses any deadline, the
``rtems_rate_monotonic_period`` directive will return the ``RTEMS_TIMEOUT``
directive status. If the above task misses its deadline, it will delete the
rate monotonic periods and itself.

Directives
==========

This section details the rate monotonic manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create a period
.. index:: rtems_rate_monotonic_create

.. _rtems_rate_monotonic_create:

RATE_MONOTONIC_CREATE - Create a rate monotonic period
------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_create(
            rtems_name  name,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - rate monotonic period created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid period name
     * - ``RTEMS_TOO_MANY``
       - too many periods created

DESCRIPTION:
    This directive creates a rate monotonic period.  The assigned rate
    monotonic id is returned in id.  This id is used to access the period with
    other rate monotonic manager directives.  For control and maintenance of
    the rate monotonic period, RTEMS allocates a PCB from the local PCB free
    pool and initializes it.

NOTES:
    This directive will not cause the calling task to be preempted.

.. raw:: latex

   \clearpage

.. index:: get ID of a period
.. index:: obtain ID of a period
.. index:: rtems_rate_monotonic_ident

.. _rtems_rate_monotonic_ident:

RATE_MONOTONIC_IDENT - Get ID of a period
-----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_ident(
            rtems_name  name,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period identified successfully
     * - ``RTEMS_INVALID_NAME``
       - period name not found

DESCRIPTION:
    This directive obtains the period id associated with the period name to be
    acquired.  If the period name is not unique, then the period id will match
    one of the periods with that name.  However, this period id is not
    guaranteed to correspond to the desired period.  The period id is used to
    access this period in other rate monotonic manager directives.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: cancel a period
.. index:: rtems_rate_monotonic_cancel

.. _rtems_rate_monotonic_cancel:

RATE_MONOTONIC_CANCEL - Cancel a period
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_cancel(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period canceled successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id
     * - ``RTEMS_NOT_OWNER_OF_RESOURCE``
       - rate monotonic period not created by calling task

DESCRIPTION:

    This directive cancels the rate monotonic period id.  This period will be
    reinitiated by the next invocation of ``rtems_rate_monotonic_period``
    with id.

NOTES:
    This directive will not cause the running task to be preempted.

    The rate monotonic period specified by id must have been created by the
    calling task.

.. raw:: latex

   \clearpage

.. index:: rtems_rate_monotonic_delete
.. index:: delete a period

.. _rtems_rate_monotonic_delete:

RATE_MONOTONIC_DELETE - Delete a rate monotonic period
------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id

DESCRIPTION:

    This directive deletes the rate monotonic period specified by id.  If the
    period is running, it is automatically canceled.  The PCB for the deleted
    period is reclaimed by RTEMS.

NOTES:
    This directive will not cause the running task to be preempted.

    A rate monotonic period can be deleted by a task other than the task which
    created the period.

.. raw:: latex

   \clearpage

.. index:: conclude current period
.. index:: start current period
.. index:: period initiation
.. index:: rtems_rate_monotonic_period

.. _rtems_rate_monotonic_period:

RATE_MONOTONIC_PERIOD - Conclude current/Start next period
----------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_period(
            rtems_id       id,
            rtems_interval length
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period initiated successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id
     * - ``RTEMS_NOT_OWNER_OF_RESOURCE``
       - period not created by calling task
     * - ``RTEMS_NOT_DEFINED``
       - period has never been initiated (only possible when period is set to PERIOD_STATUS)
     * - ``RTEMS_TIMEOUT``
       - period has expired

DESCRIPTION:
    This directive initiates the rate monotonic period id with a length of
    period ticks.  If id is running, then the calling task will block for the
    remainder of the period before reinitiating the period with the specified
    period.  If id was not running (either expired or never initiated), the
    period is immediately initiated and the directive returns immediately.
    If id has expired its period, the postponed job will be released immediately
    and the following calls of this directive will release postponed
    jobs until there is no more deadline miss.

    If invoked with a period of ``RTEMS_PERIOD_STATUS`` ticks, the current
    state of id will be returned.  The directive status indicates the current
    state of the period.  This does not alter the state or period of the
    period.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: get status of period
.. index:: obtain status of period
.. index:: rtems_rate_monotonic_get_status

.. _rtems_rate_monotonic_get_status:

RATE_MONOTONIC_GET_STATUS - Obtain status from a period
-------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_get_status(
            rtems_id                            id,
            rtems_rate_monotonic_period_status *status
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period initiated successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id
     * - ``RTEMS_INVALID_ADDRESS``
       - invalid address of status

*DESCRIPTION:
    This directive returns status information associated with the rate
    monotonic period id in the following data structure:

    .. index:: rtems_rate_monotonic_period_status

    .. code-block:: c

        typedef struct {
            rtems_id                              owner;
            rtems_rate_monotonic_period_states    state;
            rtems_rate_monotonic_period_time_t    since_last_period;
            rtems_thread_cpu_usage_t              executed_since_last_period;
            uint32_t                              postponed_jobs_count;
        }  rtems_rate_monotonic_period_status;

    .. COMMENT: RATE_MONOTONIC_INACTIVE does not have RTEMS in front of it.

    A configure time option can be used to select whether the time information
    is given in ticks or seconds and nanoseconds.  The default is seconds and
    nanoseconds.  If the period's state is ``RATE_MONOTONIC_INACTIVE``, both
    time values will be set to 0.  Otherwise, both time values will contain
    time information since the last invocation of the
    ``rtems_rate_monotonic_period`` directive.  More specifically, the
    since_last_period value contains the elapsed time which has occurred since
    the last invocation of the ``rtems_rate_monotonic_period`` directive and
    the ``executed_since_last_period`` contains how much processor time the
    owning task has consumed since the invocation of the
    ``rtems_rate_monotonic_period`` directive. In addition, the
    ``postponed_jobs_count value`` contains the count of jobs which are not
    released yet.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: get statistics of period
.. index:: obtain statistics of period
.. index:: rtems_rate_monotonic_get_statistics

.. _rtems_rate_monotonic_get_statistics:

RATE_MONOTONIC_GET_STATISTICS - Obtain statistics from a period
---------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_get_statistics(
            rtems_id                                id,
            rtems_rate_monotonic_period_statistics *statistics
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period initiated successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id
     * - ``RTEMS_INVALID_ADDRESS``
       - invalid address of statistics

DESCRIPTION:
    This directive returns statistics information associated with the rate
    monotonic period id in the following data structure:

    .. index:: rtems_rate_monotonic_period_statistics

    .. code-block:: c

        typedef struct {
            uint32_t     count;
            uint32_t     missed_count;
            #ifdef RTEMS_ENABLE_NANOSECOND_CPU_USAGE_STATISTICS
              struct timespec min_cpu_time;
              struct timespec max_cpu_time;
              struct timespec total_cpu_time;
            #else
              uint32_t  min_cpu_time;
              uint32_t  max_cpu_time;
              uint32_t  total_cpu_time;
            #endif
            #ifdef RTEMS_ENABLE_NANOSECOND_RATE_MONOTONIC_STATISTICS
              struct timespec min_wall_time;
              struct timespec max_wall_time;
              struct timespec total_wall_time;
            #else
             uint32_t  min_wall_time;
             uint32_t  max_wall_time;
             uint32_t  total_wall_time;
            #endif
        }  rtems_rate_monotonic_period_statistics;

    This directive returns the current statistics information for the period
    instance assocaited with ``id``.  The information returned is indicated by
    the structure above.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: reset statistics of period
.. index:: rtems_rate_monotonic_reset_statistics

.. _rtems_rate_monotonic_reset_statistics:

RATE_MONOTONIC_RESET_STATISTICS - Reset statistics for a period
---------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_rate_monotonic_reset_statistics(
            rtems_id  id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - period initiated successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id

DESCRIPTION:
    This directive resets the statistics information associated with this rate
    monotonic period instance.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: reset statistics of all periods
.. index:: rtems_rate_monotonic_reset_all_statistics

.. _rtems_rate_monotonic_reset_all_statistics:

RATE_MONOTONIC_RESET_ALL_STATISTICS - Reset statistics for all periods
----------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_rate_monotonic_reset_all_statistics(void);

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive resets the statistics information associated with all rate
    monotonic period instances.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: print period statistics report
.. index:: period statistics report
.. index:: rtems_rate_monotonic_report_statistics

.. _rtems_rate_monotonic_report_statistics:

RATE_MONOTONIC_REPORT_STATISTICS - Print period statistics report
-----------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_rate_monotonic_report_statistics(void);

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive prints a report on all active periods which have executed at
    least one period. The following is an example of the output generated by
    this directive.

    .. index:: rtems_rate_monotonic_period_statistics

    .. code-block:: c

        ID      OWNER   PERIODS  MISSED    CPU TIME    WALL TIME
        MIN/MAX/AVG  MIN/MAX/AVG
        0x42010001  TA1       502     0       0/1/0.99    0/0/0.00
        0x42010002  TA2       502     0       0/1/0.99    0/0/0.00
        0x42010003  TA3       501     0       0/1/0.99    0/0/0.00
        0x42010004  TA4       501     0       0/1/0.99    0/0/0.00
        0x42010005  TA5        10     0       0/1/0.90    0/0/0.00

NOTES:
    This directive will not cause the running task to be preempted.
