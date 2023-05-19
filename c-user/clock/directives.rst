.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2014, 2021 embedded brains GmbH & Co. KG
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. _ClockManagerDirectives:

Directives
==========

This section details the directives of the Clock Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/clock/if/set

.. raw:: latex

    \clearpage

.. index:: rtems_clock_set()

.. _InterfaceRtemsClockSet:

rtems_clock_set()
-----------------

Sets the :term:`CLOCK_REALTIME` to the time of day.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_clock_set( const rtems_time_of_day *time_of_day );

.. rubric:: PARAMETERS:

``time_of_day``
    This parameter is the time of day to set the clock.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``time_of_day`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_CLOCK`
    The time of day specified by ``time_of_day`` was invalid.

.. rubric:: NOTES:

The date, time, and ticks specified by ``time_of_day`` are all range-checked,
and an error is returned if any one is out of its valid range.

RTEMS can represent time points of the :term:`CLOCK_REALTIME` clock in
nanoseconds ranging from 1988-01-01T00:00:00.000000000Z to
2514-05-31T01:53:03.999999999Z.  The future uptime of the system shall be in
this range, otherwise the system behaviour is undefined.  Due to implementation
constraints, the time of day set by the directive shall be before
2100-01-01:00:00.000000000Z.  The latest valid time of day accepted by the
POSIX `clock_settime()
<https://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_settime.html>`_
is 2400-01-01T00:00:00.999999999Z.

The specified time is based on the configured :term:`clock tick` rate, see the
:ref:`CONFIGURE_MICROSECONDS_PER_TICK` application configuration option.

Setting the time forward will fire all :term:`CLOCK_REALTIME` timers which are
scheduled at a time point before or at the time set by the directive.  This may
unblock tasks, which may preempt the calling task. User-provided timer routines
will execute in the context of the caller.

It is allowed to call this directive from within interrupt context, however,
this is not recommended since an arbitrary number of timers may fire.

The directive shall be called at least once to enable the service of
:term:`CLOCK_REALTIME` related directives.  If the clock is not set at least
once, they may return an error status.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive may change the priority of a task.  This may cause the calling
  task to be preempted.

* The directive may unblock a task.  This may cause the calling task to be
  preempted.

* The time of day set by the directive shall be 1988-01-01T00:00:00.000000000Z
  or later.

* The time of day set by the directive shall be before
  2100-01-01T00:00:00.000000000Z.

.. Generated from spec:/rtems/clock/if/get-tod

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_tod()

.. _InterfaceRtemsClockGetTod:

rtems_clock_get_tod()
---------------------

Gets the time of day associated with the current :term:`CLOCK_REALTIME`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_clock_get_tod( rtems_time_of_day *time_of_day );

.. rubric:: PARAMETERS:

``time_of_day``
    This parameter is the pointer to an :ref:`InterfaceRtemsTimeOfDay` object.
    When the directive call is successful, the time of day associated with the
    :term:`CLOCK_REALTIME` at some point during the directive call will be
    stored in this object.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``time_of_day`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_NOT_DEFINED`
    The :term:`CLOCK_REALTIME` was not set.  It can be set with
    :ref:`InterfaceRtemsClockSet`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-tod-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_tod_timeval()

.. _InterfaceRtemsClockGetTodTimeval:

rtems_clock_get_tod_timeval()
-----------------------------

Gets the seconds and microseconds elapsed since the :term:`Unix epoch` and the
current :term:`CLOCK_REALTIME`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_clock_get_tod_timeval( struct timeval *time_of_day );

.. rubric:: PARAMETERS:

``time_of_day``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  When the directive call is successful, the seconds and
    microseconds elapsed since the :term:`Unix epoch` and the
    :term:`CLOCK_REALTIME` at some point during the directive call will be
    stored in this object.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``time_of_day`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_NOT_DEFINED`
    The :term:`CLOCK_REALTIME` was not set.  It can be set with
    :ref:`InterfaceRtemsClockSet`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-realtime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_realtime()

.. _InterfaceRtemsClockGetRealtime:

rtems_clock_get_realtime()
--------------------------

Gets the time elapsed since the :term:`Unix epoch` measured using
:term:`CLOCK_REALTIME` in seconds and nanoseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_realtime( struct timespec *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timespec
    <https://en.cppreference.com/w/c/chrono/timespec>`_ object.  The time
    elapsed since the :term:`Unix epoch` measured using the
    :term:`CLOCK_REALTIME` at some time point during the directive call will be
    stored in this object.  Calling the directive with a pointer equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_ is undefined behaviour.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.  Alternatively, the
:ref:`InterfaceRtemsClockGetRealtimeCoarse` directive may be used to get the
time in a lower resolution and with less runtime overhead.

See :ref:`InterfaceRtemsClockGetRealtimeBintime` and
:ref:`InterfaceRtemsClockGetRealtimeTimeval` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-realtime-bintime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_realtime_bintime()

.. _InterfaceRtemsClockGetRealtimeBintime:

rtems_clock_get_realtime_bintime()
----------------------------------

Gets the time elapsed since the :term:`Unix epoch` measured using
:term:`CLOCK_REALTIME` in binary time format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_realtime_bintime( struct bintime *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a ``struct bintime`` object.  The time
    elapsed since the :term:`Unix epoch` measured using the
    :term:`CLOCK_REALTIME` at some time point during the directive call will be
    stored in this object.  Calling the directive with a pointer equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_ is undefined behaviour.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.  Alternatively, the
:ref:`InterfaceRtemsClockGetRealtimeCoarseBintime` directive may be used to get
the time in a lower resolution and with less runtime overhead.

See :ref:`InterfaceRtemsClockGetRealtime` and
:ref:`InterfaceRtemsClockGetRealtimeTimeval` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-realtime-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_realtime_timeval()

.. _InterfaceRtemsClockGetRealtimeTimeval:

rtems_clock_get_realtime_timeval()
----------------------------------

Gets the time elapsed since the :term:`Unix epoch` measured using
:term:`CLOCK_REALTIME` in seconds and microseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_realtime_timeval( struct timeval *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  The time elapsed since the :term:`Unix epoch` measured using the
    :term:`CLOCK_REALTIME` at some time point during the directive call will be
    stored in this object.  Calling the directive with a pointer equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_ is undefined behaviour.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.  Alternatively, the
:ref:`InterfaceRtemsClockGetRealtimeCoarseTimeval` directive may be used to get
the time in a lower resolution and with less runtime overhead.

See :ref:`InterfaceRtemsClockGetRealtime` and
:ref:`InterfaceRtemsClockGetRealtimeBintime` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-realtime-coarse

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_realtime_coarse()

.. _InterfaceRtemsClockGetRealtimeCoarse:

rtems_clock_get_realtime_coarse()
---------------------------------

Gets the time elapsed since the :term:`Unix epoch` measured using
:term:`CLOCK_REALTIME` in coarse resolution in seconds and nanoseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_realtime_coarse( struct timespec *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timespec
    <https://en.cppreference.com/w/c/chrono/timespec>`_ object.  The time
    elapsed since the :term:`Unix epoch` measured using the
    :term:`CLOCK_REALTIME` at some time point close to the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive does not access a device to get the time.  It uses a recent
snapshot provided by the :term:`Clock Driver`.  Alternatively, the
:ref:`InterfaceRtemsClockGetRealtime` directive may be used to get the time in
a higher resolution and with a higher runtime overhead.

See :ref:`InterfaceRtemsClockGetRealtimeCoarseBintime` and
:ref:`InterfaceRtemsClockGetRealtimeCoarseTimeval` to get the time in
alternative formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-realtime-coarse-bintime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_realtime_coarse_bintime()

.. _InterfaceRtemsClockGetRealtimeCoarseBintime:

rtems_clock_get_realtime_coarse_bintime()
-----------------------------------------

Gets the time elapsed since the :term:`Unix epoch` measured using
:term:`CLOCK_REALTIME` in coarse resolution in binary time format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_realtime_coarse_bintime( struct bintime *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a ``struct bintime`` object.  The time
    elapsed since the :term:`Unix epoch` measured using the
    :term:`CLOCK_REALTIME` at some time point close to the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive does not access a device to get the time.  It uses a recent
snapshot provided by the :term:`Clock Driver`.  Alternatively, the
:ref:`InterfaceRtemsClockGetRealtimeBintime` directive may be used to get the
time in a higher resolution and with a higher runtime overhead.

See :ref:`InterfaceRtemsClockGetRealtimeCoarse` and
:ref:`InterfaceRtemsClockGetRealtimeCoarseTimeval` to get the time in
alternative formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-realtime-coarse-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_realtime_coarse_timeval()

.. _InterfaceRtemsClockGetRealtimeCoarseTimeval:

rtems_clock_get_realtime_coarse_timeval()
-----------------------------------------

Gets the time elapsed since the :term:`Unix epoch` measured using
:term:`CLOCK_REALTIME` in coarse resolution in seconds and microseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_realtime_coarse_timeval( struct timeval *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  The time elapsed since the :term:`Unix epoch` measured using the
    :term:`CLOCK_REALTIME` at some time point close to the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive does not access a device to get the time.  It uses a recent
snapshot provided by the :term:`Clock Driver`.  Alternatively, the
:ref:`InterfaceRtemsClockGetRealtimeTimeval` directive may be used to get the
time in a higher resolution and with a higher runtime overhead.

See :ref:`InterfaceRtemsClockGetRealtimeCoarse` and
:ref:`InterfaceRtemsClockGetRealtimeCoarseTimeval` to get the time in
alternative formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic()

.. _InterfaceRtemsClockGetMonotonic:

rtems_clock_get_monotonic()
---------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in seconds and nanoseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_monotonic( struct timespec *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timespec
    <https://en.cppreference.com/w/c/chrono/timespec>`_ object.  The time
    elapsed since some fixed time point in the past measured using the
    :term:`CLOCK_MONOTONIC` at some time point during the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.  Alternatively, the
:ref:`InterfaceRtemsClockGetMonotonicCoarse` directive may be used to get the
time with in a lower resolution and with less runtime overhead.

See :ref:`InterfaceRtemsClockGetMonotonicBintime`,
:ref:`InterfaceRtemsClockGetMonotonicSbintime`, and
:ref:`InterfaceRtemsClockGetMonotonicTimeval` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic-bintime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic_bintime()

.. _InterfaceRtemsClockGetMonotonicBintime:

rtems_clock_get_monotonic_bintime()
-----------------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in binary time format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_monotonic_bintime( struct bintime *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a ``struct bintime`` object.  The time
    elapsed since some fixed time point in the past measured using the
    :term:`CLOCK_MONOTONIC` at some time point during the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.  Alternatively, the
:ref:`InterfaceRtemsClockGetMonotonicCoarseBintime` directive may be used to
get the time in a lower resolution and with less runtime overhead.

See :ref:`InterfaceRtemsClockGetMonotonic`,
:ref:`InterfaceRtemsClockGetMonotonicSbintime`, and
:ref:`InterfaceRtemsClockGetMonotonicTimeval` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic-sbintime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic_sbintime()

.. _InterfaceRtemsClockGetMonotonicSbintime:

rtems_clock_get_monotonic_sbintime()
------------------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in signed binary time format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    int64_t rtems_clock_get_monotonic_sbintime( void );

.. rubric:: RETURN VALUES:

Returns the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` at some time point during the directive call.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.

See :ref:`InterfaceRtemsClockGetMonotonic`,
:ref:`InterfaceRtemsClockGetMonotonicBintime`, and
:ref:`InterfaceRtemsClockGetMonotonicTimeval` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic_timeval()

.. _InterfaceRtemsClockGetMonotonicTimeval:

rtems_clock_get_monotonic_timeval()
-----------------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in seconds and microseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_monotonic_timeval( struct timeval *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  The time elapsed since some fixed time point in the past measured
    using the :term:`CLOCK_MONOTONIC` at some time point during the directive
    call will be stored in this object.  Calling the directive with a pointer
    equal to `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive accesses a device provided by the :term:`Clock Driver` to get the
time in the highest resolution available to the system.  Alternatively, the
:ref:`InterfaceRtemsClockGetMonotonicCoarseTimeval` directive may be used to
get the time in a lower resolution and with less runtime overhead.

See :ref:`InterfaceRtemsClockGetMonotonic`,
:ref:`InterfaceRtemsClockGetMonotonicBintime`, and
:ref:`InterfaceRtemsClockGetMonotonicSbintime` to get the time in alternative
formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic-coarse

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic_coarse()

.. _InterfaceRtemsClockGetMonotonicCoarse:

rtems_clock_get_monotonic_coarse()
----------------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in coarse resolution in seconds and nanoseconds
format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_monotonic_coarse( struct timespec *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timespec
    <https://en.cppreference.com/w/c/chrono/timespec>`_ object.  The time
    elapsed since some fixed time point in the past measured using the
    :term:`CLOCK_MONOTONIC` at some time point close to the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive does not access a device to get the time.  It uses a recent
snapshot provided by the :term:`Clock Driver`.  Alternatively, the
:ref:`InterfaceRtemsClockGetMonotonic` directive may be used to get the time in
a higher resolution and with a higher runtime overhead.

See :ref:`InterfaceRtemsClockGetMonotonicCoarseBintime` and
:ref:`InterfaceRtemsClockGetMonotonicCoarseTimeval` to get the time in
alternative formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic-coarse-bintime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic_coarse_bintime()

.. _InterfaceRtemsClockGetMonotonicCoarseBintime:

rtems_clock_get_monotonic_coarse_bintime()
------------------------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in coarse resolution in binary time format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_monotonic_coarse_bintime( struct bintime *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a ``struct bintime`` object.  The time
    elapsed since some fixed time point in the past measured using the
    :term:`CLOCK_MONOTONIC` at some time point close to the directive call will
    be stored in this object.  Calling the directive with a pointer equal to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive does not access a device to get the time.  It uses a recent
snapshot provided by the :term:`Clock Driver`.  Alternatively, the
:ref:`InterfaceRtemsClockGetMonotonicBintime` directive may be used to get the
time in a higher resolution and with a higher runtime overhead.

See :ref:`InterfaceRtemsClockGetMonotonicCoarse` and
:ref:`InterfaceRtemsClockGetMonotonicCoarseTimeval` to get the time in
alternative formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-monotonic-coarse-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_monotonic_coarse_timeval()

.. _InterfaceRtemsClockGetMonotonicCoarseTimeval:

rtems_clock_get_monotonic_coarse_timeval()
------------------------------------------

Gets the time elapsed since some fixed time point in the past measured using
the :term:`CLOCK_MONOTONIC` in coarse resolution in seconds and microseconds
format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_monotonic_coarse_timeval( struct timeval *time_snapshot );

.. rubric:: PARAMETERS:

``time_snapshot``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  The time elapsed since some fixed time point in the past measured
    using the :term:`CLOCK_MONOTONIC` at some time point close to the directive
    call will be stored in this object.  Calling the directive with a pointer
    equal to `NULL <https://en.cppreference.com/w/c/types/NULL>`_ is undefined
    behaviour.

.. rubric:: NOTES:

The directive does not access a device to get the time.  It uses a recent
snapshot provided by the :term:`Clock Driver`.  Alternatively, the
:ref:`InterfaceRtemsClockGetMonotonicTimeval` directive may be used to get the
time in a higher resolution and with a higher runtime overhead.

See :ref:`InterfaceRtemsClockGetMonotonicCoarse` and
:ref:`InterfaceRtemsClockGetMonotonicCoarseBintime` to get the time in
alternative formats.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-boot-time

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_boot_time()

.. _InterfaceRtemsClockGetBootTime:

rtems_clock_get_boot_time()
---------------------------

Gets the time elapsed since the :term:`Unix epoch` at some time point during
system initialization in seconds and nanoseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_boot_time( struct timespec *boot_time );

.. rubric:: PARAMETERS:

``boot_time``
    This parameter is the pointer to a `struct timespec
    <https://en.cppreference.com/w/c/chrono/timespec>`_ object.  The time
    elapsed since the :term:`Unix epoch` at some time point during system
    initialization call will be stored in this object.  Calling the directive
    with a pointer equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_ is undefined behaviour.

.. rubric:: NOTES:

See :ref:`InterfaceRtemsClockGetBootTimeBintime` and
:ref:`InterfaceRtemsClockGetBootTimeTimeval` to get the boot time in
alternative formats.  Setting the :term:`CLOCK_REALTIME` will also set the boot
time.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-boot-time-bintime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_boot_time_bintime()

.. _InterfaceRtemsClockGetBootTimeBintime:

rtems_clock_get_boot_time_bintime()
-----------------------------------

Gets the time elapsed since the :term:`Unix epoch` at some time point during
system initialization in binary time format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_boot_time_bintime( struct bintime *boot_time );

.. rubric:: PARAMETERS:

``boot_time``
    This parameter is the pointer to a ``struct bintime`` object.  The time
    elapsed since the :term:`Unix epoch` at some time point during system
    initialization call will be stored in this object.  Calling the directive
    with a pointer equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_ is undefined behaviour.

.. rubric:: NOTES:

See :ref:`InterfaceRtemsClockGetBootTime` and
:ref:`InterfaceRtemsClockGetBootTimeTimeval` to get the boot time in
alternative formats.  Setting the :term:`CLOCK_REALTIME` will also set the boot
time.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-boot-time-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_boot_time_timeval()

.. _InterfaceRtemsClockGetBootTimeTimeval:

rtems_clock_get_boot_time_timeval()
-----------------------------------

Gets the time elapsed since the :term:`Unix epoch` at some time point during
system initialization in seconds and microseconds format.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_boot_time_timeval( struct timeval *boot_time );

.. rubric:: PARAMETERS:

``boot_time``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  The time elapsed since the :term:`Unix epoch` at some time point
    during system initialization call will be stored in this object.  Calling
    the directive with a pointer equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_ is undefined behaviour.

.. rubric:: NOTES:

See :ref:`InterfaceRtemsClockGetBootTime` and
:ref:`InterfaceRtemsClockGetBootTimeBintime` to get the boot time in
alternative formats.  Setting the :term:`CLOCK_REALTIME` will also set the boot
time.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-seconds-since-epoch

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_seconds_since_epoch()

.. _InterfaceRtemsClockGetSecondsSinceEpoch:

rtems_clock_get_seconds_since_epoch()
-------------------------------------

Gets the seconds elapsed since the :term:`RTEMS epoch` and the current
:term:`CLOCK_REALTIME`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_clock_get_seconds_since_epoch(
      rtems_interval *seconds_since_rtems_epoch
    );

.. rubric:: PARAMETERS:

``seconds_since_rtems_epoch``
    This parameter is the pointer to an :ref:`InterfaceRtemsInterval` object.
    When the directive call is successful, the seconds elapsed since the
    :term:`RTEMS epoch` and the :term:`CLOCK_REALTIME` at some point during the
    directive call will be stored in this object.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``seconds_since_rtems_epoch`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_NOT_DEFINED`
    The :term:`CLOCK_REALTIME` was not set.  It can be set with
    :ref:`InterfaceRtemsClockSet`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-ticks-per-second

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_ticks_per_second()

.. _InterfaceRtemsClockGetTicksPerSecond:

rtems_clock_get_ticks_per_second()
----------------------------------

Gets the number of :term:`clock ticks <clock tick>` per second configured for
the application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_interval rtems_clock_get_ticks_per_second( void );

.. rubric:: RETURN VALUES:

Returns the number of clock ticks per second configured for this application.

.. rubric:: NOTES:

The number of clock ticks per second is defined indirectly by the
:ref:`CONFIGURE_MICROSECONDS_PER_TICK` configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/clock/if/get-ticks-since-boot

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_ticks_since_boot()

.. _InterfaceRtemsClockGetTicksSinceBoot:

rtems_clock_get_ticks_since_boot()
----------------------------------

Gets the number of :term:`clock ticks <clock tick>` since some time point
during the system initialization or the last overflow of the clock tick
counter.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_interval rtems_clock_get_ticks_since_boot( void );

.. rubric:: RETURN VALUES:

Returns the number of :term:`clock ticks <clock tick>` since some time point
during the system initialization or the last overflow of the clock tick
counter.

.. rubric:: NOTES:

With a 1ms clock tick, this counter overflows after 50 days since boot.  This
is the historical measure of uptime in an RTEMS system.  The newer service
:ref:`InterfaceRtemsClockGetUptime` is another and potentially more accurate
way of obtaining similar information.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/clock/if/get-uptime

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_uptime()

.. _InterfaceRtemsClockGetUptime:

rtems_clock_get_uptime()
------------------------

Gets the seconds and nanoseconds elapsed since some time point during the
system initialization using :term:`CLOCK_MONOTONIC`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_clock_get_uptime( struct timespec *uptime );

.. rubric:: PARAMETERS:

``uptime``
    This parameter is the pointer to a `struct timespec
    <https://en.cppreference.com/w/c/chrono/timespec>`_ object.  When the
    directive call is successful, the seconds and nanoseconds elapsed since
    some time point during the system initialization and some point during the
    directive call using :term:`CLOCK_MONOTONIC` will be stored in this object.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``uptime`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-uptime-timeval

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_uptime_timeval()

.. _InterfaceRtemsClockGetUptimeTimeval:

rtems_clock_get_uptime_timeval()
--------------------------------

Gets the seconds and microseconds elapsed since some time point during the
system initialization using :term:`CLOCK_MONOTONIC`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_clock_get_uptime_timeval( struct timeval *uptime );

.. rubric:: PARAMETERS:

``uptime``
    This parameter is the pointer to a `struct timeval
    <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/sys/time.h.html>`_
    object.  The seconds and microseconds elapsed since some time point during
    the system initialization and some point during the directive call using
    :term:`CLOCK_MONOTONIC` will be stored in this object.  The pointer shall
    be valid, otherwise the behaviour is undefined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-uptime-seconds

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_uptime_seconds()

.. _InterfaceRtemsClockGetUptimeSeconds:

rtems_clock_get_uptime_seconds()
--------------------------------

Gets the seconds elapsed since some time point during the system initialization
using :term:`CLOCK_MONOTONIC`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    time_t rtems_clock_get_uptime_seconds( void );

.. rubric:: RETURN VALUES:

Returns the seconds elapsed since some time point during the system
initialization and some point during the directive call using
:term:`CLOCK_MONOTONIC`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/get-uptime-nanoseconds

.. raw:: latex

    \clearpage

.. index:: rtems_clock_get_uptime_nanoseconds()

.. _InterfaceRtemsClockGetUptimeNanoseconds:

rtems_clock_get_uptime_nanoseconds()
------------------------------------

Gets the nanoseconds elapsed since some time point during the system
initialization using :term:`CLOCK_MONOTONIC`.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint64_t rtems_clock_get_uptime_nanoseconds( void );

.. rubric:: RETURN VALUES:

Returns the nanoseconds elapsed since some time point during the system
initialization and some point during the directive call using
:term:`CLOCK_MONOTONIC`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/tick-later

.. raw:: latex

    \clearpage

.. index:: rtems_clock_tick_later()

.. _InterfaceRtemsClockTickLater:

rtems_clock_tick_later()
------------------------

Gets a :term:`clock tick` value which is at least delta clock ticks in the
future.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_interval rtems_clock_tick_later( rtems_interval delta );

.. rubric:: PARAMETERS:

``delta``
    This parameter is the delta value in clock ticks.

.. rubric:: RETURN VALUES:

Returns a :term:`clock tick` counter value which is at least ``delta`` clock
ticks in the future.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/tick-later-usec

.. raw:: latex

    \clearpage

.. index:: rtems_clock_tick_later_usec()

.. _InterfaceRtemsClockTickLaterUsec:

rtems_clock_tick_later_usec()
-----------------------------

Gets a :term:`clock tick` value which is at least delta microseconds in the
future.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_interval rtems_clock_tick_later_usec( rtems_interval delta_in_usec );

.. rubric:: PARAMETERS:

``delta_in_usec``
    This parameter is the delta value in microseconds.

.. rubric:: RETURN VALUES:

Returns a :term:`clock tick` counter value which is at least ``delta_in_usec``
microseconds in the future.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.

.. Generated from spec:/rtems/clock/if/tick-before

.. raw:: latex

    \clearpage

.. index:: rtems_clock_tick_before()

.. _InterfaceRtemsClockTickBefore:

rtems_clock_tick_before()
-------------------------

Indicates if the current :term:`clock tick` counter is before the ticks.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    bool rtems_clock_tick_before( rtems_interval ticks );

.. rubric:: PARAMETERS:

``ticks``
    This parameter is the ticks value to check.

.. rubric:: RETURN VALUES:

Returns true, if current :term:`clock tick` counter indicates a time before the
time in ticks, otherwise returns false.

.. rubric:: NOTES:

This directive can be used to write busy loops with a timeout.

.. code-block:: c
    :linenos:

    status busy( void )
    {
      rtems_interval timeout;

      timeout = rtems_clock_tick_later_usec( 10000 );

      do {
        if ( ok() ) {
          return success;
        }
      } while ( rtems_clock_tick_before( timeout ) );

      return timeout;
    }

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* The directive requires a :term:`Clock Driver`.
