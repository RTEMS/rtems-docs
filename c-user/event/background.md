% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Background

```{index} event flag, definition
```

```{index} event set, definition
```

```{index} rtems_event_set
```

## Event Sets

An event flag is used by a task (or ISR) to inform another task of the
occurrence of a significant situation. Thirty-two event flags are associated
with each task. A collection of one or more event flags is referred to as an
event set. The data type `rtems_event_set` is used to manage event sets.

The application developer should remember the following key characteristics of
event operations when utilizing the event manager:

- Events provide a simple synchronization facility.
- Events are aimed at tasks.
- Tasks can wait on more than one event simultaneously.
- Events are independent of one another.
- Events do not hold or transport data.
- Events are not queued. In other words, if an event is sent more than once to
  a task before being received, the second and subsequent send operations to
  that same task have no effect.

An event set is posted when it is directed (or sent) to a task. A pending
event is an event that has been posted but not received. An event condition is
used to specify the event set which the task desires to receive and the
algorithm which will be used to determine when the request is satisfied. An
event condition is satisfied based upon one of two algorithms which are
selected by the user. The `RTEMS_EVENT_ANY` algorithm states that an event
condition is satisfied when at least a single requested event is posted. The
`RTEMS_EVENT_ALL` algorithm states that an event condition is satisfied when
every requested event is posted.

```{index} event condition, building
```

```{index} event set, building
```

## Building an Event Set or Condition

An event set or condition is built by a bitwise OR of the desired events. The
set of valid events is `RTEMS_EVENT_0` through `RTEMS_EVENT_31`. If an
event is not explicitly specified in the set or condition, then it is not
present. Events are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each event appears
exactly once in the event set list.

For example, when sending the event set consisting of `RTEMS_EVENT_6`,
`RTEMS_EVENT_15`, and `RTEMS_EVENT_31`, the event parameter to the
`rtems_event_send` directive should be `RTEMS_EVENT_6 | RTEMS_EVENT_15 | RTEMS_EVENT_31`.

## Building an EVENT_RECEIVE Option Set

In general, an option is built by a bitwise OR of the desired option
components. The set of valid options for the `rtems_event_receive` directive
are listed in the following table:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``RTEMS_WAIT``
   - task will wait for event (default)
 * - ``RTEMS_NO_WAIT``
   - task should not wait
 * - ``RTEMS_EVENT_ALL``
   - return after all events (default)
 * - ``RTEMS_EVENT_ANY``
   - return after any events
```

Option values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each option
appears exactly once in the component list. An option listed as a default is
not required to appear in the option list, although it is a good programming
practice to specify default options. If all defaults are desired, the option
`RTEMS_DEFAULT_OPTIONS` should be specified on this call.

This example demonstrates the option parameter needed to poll for all events in
a particular event condition to arrive. The option parameter passed to the
`rtems_event_receive` directive should be either `RTEMS_EVENT_ALL | RTEMS_NO_WAIT` or `RTEMS_NO_WAIT`. The option parameter can be set to
`RTEMS_NO_WAIT` because `RTEMS_EVENT_ALL` is the default condition for
`rtems_event_receive`.
