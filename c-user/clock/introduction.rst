.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2014, 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/rtems/clock/if/group

.. _ClockManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/clock/if/set
.. spec:/rtems/clock/if/get-tod
.. spec:/rtems/clock/if/get-tod-timeval
.. spec:/rtems/clock/if/get-realtime
.. spec:/rtems/clock/if/get-realtime-bintime
.. spec:/rtems/clock/if/get-realtime-timeval
.. spec:/rtems/clock/if/get-realtime-coarse
.. spec:/rtems/clock/if/get-realtime-coarse-bintime
.. spec:/rtems/clock/if/get-realtime-coarse-timeval
.. spec:/rtems/clock/if/get-monotonic
.. spec:/rtems/clock/if/get-monotonic-bintime
.. spec:/rtems/clock/if/get-monotonic-sbintime
.. spec:/rtems/clock/if/get-monotonic-timeval
.. spec:/rtems/clock/if/get-monotonic-coarse
.. spec:/rtems/clock/if/get-monotonic-coarse-bintime
.. spec:/rtems/clock/if/get-monotonic-coarse-timeval
.. spec:/rtems/clock/if/get-boot-time
.. spec:/rtems/clock/if/get-boot-time-bintime
.. spec:/rtems/clock/if/get-boot-time-timeval
.. spec:/rtems/clock/if/get-seconds-since-epoch
.. spec:/rtems/clock/if/get-ticks-per-second
.. spec:/rtems/clock/if/get-ticks-since-boot
.. spec:/rtems/clock/if/get-uptime
.. spec:/rtems/clock/if/get-uptime-timeval
.. spec:/rtems/clock/if/get-uptime-seconds
.. spec:/rtems/clock/if/get-uptime-nanoseconds
.. spec:/rtems/clock/if/tick-later
.. spec:/rtems/clock/if/tick-later-usec
.. spec:/rtems/clock/if/tick-before

The Clock Manager provides support for time of day and other time related
capabilities. The directives provided by the Clock Manager are:

* :ref:`InterfaceRtemsClockSet` - Sets the :term:`CLOCK_REALTIME` to the time
  of day.

* :ref:`InterfaceRtemsClockGetTod` - Gets the time of day associated with the
  current :term:`CLOCK_REALTIME`.

* :ref:`InterfaceRtemsClockGetTodTimeval` - Gets the seconds and microseconds
  elapsed since the :term:`Unix epoch` and the current :term:`CLOCK_REALTIME`.

* :ref:`InterfaceRtemsClockGetRealtime` - Gets the time elapsed since the
  :term:`Unix epoch` measured using :term:`CLOCK_REALTIME` in seconds and
  nanoseconds format.

* :ref:`InterfaceRtemsClockGetRealtimeBintime` - Gets the time elapsed since
  the :term:`Unix epoch` measured using :term:`CLOCK_REALTIME` in binary time
  format.

* :ref:`InterfaceRtemsClockGetRealtimeTimeval` - Gets the time elapsed since
  the :term:`Unix epoch` measured using :term:`CLOCK_REALTIME` in seconds and
  microseconds format.

* :ref:`InterfaceRtemsClockGetRealtimeCoarse` - Gets the time elapsed since the
  :term:`Unix epoch` measured using :term:`CLOCK_REALTIME` in coarse resolution
  in seconds and nanoseconds format.

* :ref:`InterfaceRtemsClockGetRealtimeCoarseBintime` - Gets the time elapsed
  since the :term:`Unix epoch` measured using :term:`CLOCK_REALTIME` in coarse
  resolution in binary time format.

* :ref:`InterfaceRtemsClockGetRealtimeCoarseTimeval` - Gets the time elapsed
  since the :term:`Unix epoch` measured using :term:`CLOCK_REALTIME` in coarse
  resolution in seconds and microseconds format.

* :ref:`InterfaceRtemsClockGetMonotonic` - Gets the time elapsed since some
  fixed time point in the past measured using the :term:`CLOCK_MONOTONIC` in
  seconds and nanoseconds format.

* :ref:`InterfaceRtemsClockGetMonotonicBintime` - Gets the time elapsed since
  some fixed time point in the past measured using the :term:`CLOCK_MONOTONIC`
  in binary time format.

* :ref:`InterfaceRtemsClockGetMonotonicSbintime` - Gets the time elapsed since
  some fixed time point in the past measured using the :term:`CLOCK_MONOTONIC`
  in signed binary time format.

* :ref:`InterfaceRtemsClockGetMonotonicTimeval` - Gets the time elapsed since
  some fixed time point in the past measured using the :term:`CLOCK_MONOTONIC`
  in seconds and microseconds format.

* :ref:`InterfaceRtemsClockGetMonotonicCoarse` - Gets the time elapsed since
  some fixed time point in the past measured using the :term:`CLOCK_MONOTONIC`
  in coarse resolution in seconds and nanoseconds format.

* :ref:`InterfaceRtemsClockGetMonotonicCoarseBintime` - Gets the time elapsed
  since some fixed time point in the past measured using the
  :term:`CLOCK_MONOTONIC` in coarse resolution in binary time format.

* :ref:`InterfaceRtemsClockGetMonotonicCoarseTimeval` - Gets the time elapsed
  since some fixed time point in the past measured using the
  :term:`CLOCK_MONOTONIC` in coarse resolution in seconds and microseconds
  format.

* :ref:`InterfaceRtemsClockGetBootTime` - Gets the time elapsed since the
  :term:`Unix epoch` at some time point during system initialization in seconds
  and nanoseconds format.

* :ref:`InterfaceRtemsClockGetBootTimeBintime` - Gets the time elapsed since
  the :term:`Unix epoch` at some time point during system initialization in
  binary time format.

* :ref:`InterfaceRtemsClockGetBootTimeTimeval` - Gets the time elapsed since
  the :term:`Unix epoch` at some time point during system initialization in
  seconds and microseconds format.

* :ref:`InterfaceRtemsClockGetSecondsSinceEpoch` - Gets the seconds elapsed
  since the :term:`RTEMS epoch` and the current :term:`CLOCK_REALTIME`.

* :ref:`InterfaceRtemsClockGetTicksPerSecond` - Gets the number of :term:`clock
  ticks <clock tick>` per second configured for the application.

* :ref:`InterfaceRtemsClockGetTicksSinceBoot` - Gets the number of :term:`clock
  ticks <clock tick>` since some time point during the system initialization or
  the last overflow of the clock tick counter.

* :ref:`InterfaceRtemsClockGetUptime` - Gets the seconds and nanoseconds
  elapsed since some time point during the system initialization using
  :term:`CLOCK_MONOTONIC`.

* :ref:`InterfaceRtemsClockGetUptimeTimeval` - Gets the seconds and
  microseconds elapsed since some time point during the system initialization
  using :term:`CLOCK_MONOTONIC`.

* :ref:`InterfaceRtemsClockGetUptimeSeconds` - Gets the seconds elapsed since
  some time point during the system initialization using
  :term:`CLOCK_MONOTONIC`.

* :ref:`InterfaceRtemsClockGetUptimeNanoseconds` - Gets the nanoseconds elapsed
  since some time point during the system initialization using
  :term:`CLOCK_MONOTONIC`.

* :ref:`InterfaceRtemsClockTickLater` - Gets a :term:`clock tick` value which
  is at least delta clock ticks in the future.

* :ref:`InterfaceRtemsClockTickLaterUsec` - Gets a :term:`clock tick` value
  which is at least delta microseconds in the future.

* :ref:`InterfaceRtemsClockTickBefore` - Indicates if the current :term:`clock
  tick` counter is before the ticks.
