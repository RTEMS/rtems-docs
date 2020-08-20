.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. Copyright (C) 2017 Kuan-Hsun Chen.

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
