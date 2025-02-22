% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Operations

## Creating a Timer

The `rtems_timer_create` directive creates a timer by allocating a Timer
Control Block (TMCB), assigning the timer a user-specified name, and assigning
it a timer ID. Newly created timers do not have a timer service routine
associated with them and are not active.

## Obtaining Timer IDs

When a timer is created, RTEMS generates a unique timer ID and assigns it to
the created timer until it is deleted. The timer ID may be obtained by either
of two methods. First, as the result of an invocation of the
`rtems_timer_create` directive, the timer ID is stored in a user provided
location. Second, the timer ID may be obtained later using the
`rtems_timer_ident` directive. The timer ID is used by other directives to
manipulate this timer.

## Initiating an Interval Timer

The `rtems_timer_fire_after` and `rtems_timer_server_fire_after` directives
initiate a timer to fire a user provided timer service routine after the
specified number of clock ticks have elapsed. When the interval has elapsed,
the timer service routine will be invoked from a clock tick
directive if it was initiated by the `rtems_timer_fire_after` directive and
from the Timer Server task if initiated by the
`rtems_timer_server_fire_after` directive.

## Initiating a Time of Day Timer

The `rtems_timer_fire_when` and `rtems_timer_server_fire_when` directive
initiate a timer to fire a user provided timer service routine when the
specified time of day has been reached. When the interval has elapsed, the
timer service routine will be invoked from a clock tick directive
by the `rtems_timer_fire_when` directive and from the Timer Server task if
initiated by the `rtems_timer_server_fire_when` directive.

## Canceling a Timer

The `rtems_timer_cancel` directive is used to halt the specified timer. Once
canceled, the timer service routine will not fire unless the timer is
reinitiated. The timer can be reinitiated using the `rtems_timer_reset`,
`rtems_timer_fire_after`, and `rtems_timer_fire_when` directives.

## Resetting a Timer

The `rtems_timer_reset` directive is used to restore an interval timer
initiated by a previous invocation of `rtems_timer_fire_after` or
`rtems_timer_server_fire_after` to its original interval length. If the
timer has not been used or the last usage of this timer was by the
`rtems_timer_fire_when` or `rtems_timer_server_fire_when` directive, then
an error is returned. The timer service routine is not changed or fired by
this directive.

## Initiating the Timer Server

The `rtems_timer_initiate_server` directive is used to allocate and start the
execution of the Timer Server task. The application can specify both the stack
size and attributes of the Timer Server. The Timer Server executes at a
priority higher than any application task and thus the user can expect to be
preempted as the result of executing the `rtems_timer_initiate_server`
directive.

## Deleting a Timer

The `rtems_timer_delete` directive is used to delete a timer. If the timer
is running and has not expired, the timer is automatically canceled. The
timer's control block is returned to the TMCB free list when it is deleted. A
timer can be deleted by a task other than the task which created the timer.
Any subsequent references to the timer's name and ID are invalid.
