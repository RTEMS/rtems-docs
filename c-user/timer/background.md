% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Background

## Required Support

A clock tick is required to support the functionality provided by this manager.

## Timers

A timer is an RTEMS object which allows the application to schedule operations
to occur at specific times in the future. User supplied timer service routines
are invoked by either a clock tick directive or a special Timer
Server task when the timer fires. Timer service routines may perform any
operations or directives which normally would be performed by the application
code which invoked a clock tick directive.

The timer can be used to implement watchdog routines which only fire to denote
that an application error has occurred. The timer is reset at specific points
in the application to ensure that the watchdog does not fire. Thus, if the
application does not reset the watchdog timer, then the timer service routine
will fire to indicate that the application has failed to reach a reset point.
This use of a timer is sometimes referred to as a "keep alive" or a "deadman"
timer.

## Timer Server

The Timer Server task is responsible for executing the timer service routines
associated with all task-based timers. This task executes at a priority
specified by {ref}`rtems_timer_initiate_server() <rtems_timer_initiate_server>`
and it may have a priority of zero (the highest priority). In uniprocessor
configurations, it is created non-preemptible.

By providing a mechanism where timer service routines execute in task rather
than interrupt space, the application is allowed a bit more flexibility in what
operations a timer service routine can perform. For example, the Timer Server
can be configured to have a floating point context in which case it would be
safe to perform floating point operations from a task-based timer. Most of the
time, executing floating point instructions from an interrupt service routine
is not considered safe. The timer service routines invoked by the Timer Server
may block, however, since this blocks the Timer Server itself, other timer
service routines that are already pending do not run until the blocked timer
service routine finished its work.

The Timer Server is designed to remain blocked until a task-based timer fires.
This reduces the execution overhead of the Timer Server.

```{index} rtems_timer_service_routine
```

## Timer Service Routines

The timer service routine should adhere to C calling conventions and have a
prototype similar to the following:

```c
rtems_timer_service_routine user_routine(
    rtems_id   timer_id,
    void      *user_data
);
```

Where the timer_id parameter is the RTEMS object ID of the timer which is being
fired and user_data is a pointer to user-defined information which may be
utilized by the timer service routine. The argument user_data may be NULL.
