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
