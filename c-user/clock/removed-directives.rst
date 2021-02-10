.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Removed Directives
==================

.. raw:: latex

   \clearpage

.. _rtems_clock_get:

CLOCK_GET - Get date and time information
-----------------------------------------
.. index:: obtain the time of day
.. index:: rtems_clock_get

.. warning::

    This directive was removed in RTEMS 5.1.  See also
    :ref:`ClockManagerAdviceClockGet`.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_clock_get(
           rtems_clock_get_options  option,
           void                    *time_buffer
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
    This directive obtains the system date and time.  If the caller is
    attempting to obtain the date and time (i.e.  option is set to either
    ``RTEMS_CLOCK_GET_SECONDS_SINCE_EPOCH``, ``RTEMS_CLOCK_GET_TOD``, or
    ``RTEMS_CLOCK_GET_TIME_VALUE``) and the date and time has not been set with
    a previous call to ``rtems_clock_set``, then the ``RTEMS_NOT_DEFINED``
    status code is returned.  The caller can always obtain the number of ticks
    per second (option is ``RTEMS_CLOCK_GET_TICKS_PER_SECOND``) and the number
    of ticks since the executive was initialized option is
    ``RTEMS_CLOCK_GET_TICKS_SINCE_BOOT``).

    The ``option`` argument may taken on any value of the enumerated type
    ``rtems_clock_get_options``.  The data type expected for ``time_buffer`` is
    based on the value of ``option`` as indicated below:

    .. index:: rtems_clock_get_options

    +-----------------------------------------+---------------------------+
    | Option                                  | Return type               |
    +=========================================+===========================+
    | ``RTEMS_CLOCK_GET_TOD``                 | ``(rtems_time_of_day *)`` |
    +-----------------------------------------+---------------------------+
    | ``RTEMS_CLOCK_GET_SECONDS_SINCE_EPOCH`` | ``(rtems_interval *)``    |
    +-----------------------------------------+---------------------------+
    | ``RTEMS_CLOCK_GET_TICKS_SINCE_BOOT``    | ``(rtems_interval *)``    |
    +-----------------------------------------+---------------------------+
    |``RTEMS_CLOCK_GET_TICKS_PER_SECOND``     | ``(rtems_interval *)``    |
    +-----------------------------------------+---------------------------+
    | ``RTEMS_CLOCK_GET_TIME_VALUE``          | ``(struct timeval *)``    |
    +-----------------------------------------+---------------------------+

NOTES:
    This directive is callable from an ISR.

    This directive will not cause the running task to be preempted.
    Re-initializing RTEMS causes the system date and time to be reset to an
    uninitialized state.  Another call to ``rtems_clock_set`` is required to
    re-initialize the system date and time to application specific
    specifications.
