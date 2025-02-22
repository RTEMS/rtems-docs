% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Operations

## Announcing a Tick

RTEMS provides the several clock tick directives which are called from the
user's real-time clock ISR to inform RTEMS that a tick has elapsed. Depending
on the timer hardware capabilities the clock driver must choose the most
appropriate clock tick directive. The tick frequency value, defined in
microseconds, is a configuration parameter found in the Configuration Table.
RTEMS divides one million microseconds (one second) by the number of
microseconds per tick to determine the number of calls to the clock tick
directive per second. The frequency of clock tick calls determines the
resolution (granularity) for all time dependent RTEMS actions. For example,
calling the clock tick directive ten times per second yields a higher
resolution than calling the clock tick two times per second. The clock tick
directives are responsible for maintaining both calendar time and the dynamic
set of timers.

## Setting the Time

The `rtems_clock_set` directive allows a task or an ISR to set the date and
time maintained by RTEMS. If setting the date and time causes any outstanding
timers to pass their deadline, then the expired timers will be fired during the
invocation of the `rtems_clock_set` directive.

## Obtaining the Time

RTEMS provides multiple directives which can be used by an application to obtain the current date and time or date and time related information. These directives allow a task or an ISR to obtain the current date and time or date and time related information. The current date and time can be returned in either native or *UNIX-style* format. Additionally, the application can obtain date and time related information such as the number of seconds since the RTEMS epoch, the number of ticks since the executive was initialized, and the number of ticks per second. The following directives are available:

`rtems_clock_get_tod`

: obtain native style date and time

`rtems_clock_get_time_value`

: obtain *UNIX-style* date and time

`rtems_clock_get_ticks_since_boot`

: obtain number of ticks since RTEMS was initialized

`rtems_clock_get_seconds_since_epoch`

: obtain number of seconds since RTEMS epoch

`rtems_clock_get_ticks_per_second`

: obtain number of clock ticks per second

Calendar time operations will return an error code if invoked before the date
and time have been set.

(clockmanageradviceclockget)=

## Transition Advice for the Removed rtems_clock_get()

The directive {ref}`rtems_clock_get` took an untyped pointer with an options
argument to indicate the time information desired. This has been replaced with
a set of typed directives:

- {ref}`rtems_clock_get_seconds_since_epoch`
- {ref}`rtems_clock_get_ticks_per_second`
- {ref}`rtems_clock_get_ticks_since_boot`
- {ref}`rtems_clock_get_tod`
- {ref}`rtems_clock_get_tod_timeval`

These directives directly correspond to what were previously referred to as
*clock options*. These strongly typed directives were available for multiple
releases in parallel with {c:func}`rtems_clock_get` until that directive was
removed.
