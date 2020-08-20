.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. Copyright (C) 2017 Kuan-Hsun Chen.

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

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
       - period status retrieved successfully
     * - ``RTEMS_INVALID_ID``
       - invalid rate monotonic period id
     * - ``RTEMS_INVALID_ADDRESS``
       - invalid address of status
     * - ``RTEMS_NOT_DEFINED``
       - no status is available due to the cpu usage of the task having been
         reset since the period initiated

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
       - period statistics retrieved successfully
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
