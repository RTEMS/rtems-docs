% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2018 On-Line Applications Research Corporation (OAR)

# Background

A barrier can be viewed as a gate at which tasks wait until the gate is opened.
This has many analogies in the real world. Horses and other farm animals may
approach a closed gate and gather in front of it, waiting for someone to open
the gate so they may proceed. Similarly, ticket holders gather at the gates of
arenas before concerts or sporting events waiting for the arena personnel to
open the gates so they may enter.

Barriers are useful during application initialization. Each application task
can perform its local initialization before waiting for the application as a
whole to be initialized. Once all tasks have completed their independent
initializations, the "application ready" barrier can be released.

## Automatic Versus Manual Barriers

Just as with a real-world gate, barriers may be configured to be manually
opened or automatically opened. All tasks calling the `rtems_barrier_wait`
directive will block until a controlling task invokes
the `rtems_barrier_release` directive.

Automatic barriers are created with a limit to the number of tasks which may
simultaneously block at the barrier. Once this limit is reached, all of the
tasks are released. For example, if the automatic limit is ten tasks, then the
first nine tasks calling the `rtems_barrier_wait` directive will block. When
the tenth task calls the `rtems_barrier_wait` directive, the nine blocked
tasks will be released and the tenth task returns to the caller without
blocking.

## Building a Barrier Attribute Set

In general, an attribute set is built by a bitwise OR of the desired attribute
components. The following table lists the set of valid barrier attributes:

`RTEMS_BARRIER_AUTOMATIC_RELEASE`
: automatically release the barrier when the configured number of tasks are
  blocked

`RTEMS_BARRIER_MANUAL_RELEASE`
: only release the barrier when the application invokes the
  `rtems_barrier_release` directive. (default)

```{note}
Barriers only support FIFO blocking order because all waiting tasks are
released as a set. Thus the released tasks will all become ready to execute
at the same time and compete for the processor based upon their priority.
```

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list. An attribute listed as a default
is not required to appear in the attribute list, although it is a good
programming practice to specify default attributes. If all defaults are
desired, the attribute `RTEMS_DEFAULT_ATTRIBUTES` should be specified on this
call.

This example demonstrates the attribute_set parameter needed to create a
barrier with the automatic release policy. The `attribute_set` parameter
passed to the `rtems_barrier_create` directive will be
`RTEMS_BARRIER_AUTOMATIC_RELEASE`. In this case, the user must also specify
the `maximum_waiters` parameter.
