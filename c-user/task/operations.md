% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Operations

## Creating Tasks

The `rtems_task_create` directive creates a task by allocating a task control
block, assigning the task a user-specified name, allocating it a stack and
floating point context area, setting a user-specified initial priority, setting
a user-specified initial mode, and assigning it a task ID. Newly created tasks
are initially placed in the dormant state. All RTEMS tasks execute in the most
privileged mode of the processor.

## Obtaining Task IDs

When a task is created, RTEMS generates a unique task ID and assigns it to the
created task until it is deleted. The task ID may be obtained by either of two
methods. First, as the result of an invocation of the `rtems_task_create`
directive, the task ID is stored in a user provided location. Second, the task
ID may be obtained later using the `rtems_task_ident` directive. The task ID
is used by other directives to manipulate this task.

## Starting and Restarting Tasks

The `rtems_task_start` directive is used to place a dormant task in the ready
state. This enables the task to compete, based on its current priority, for
the processor and other system resources. Any actions, such as suspension or
change of priority, performed on a task prior to starting it are nullified when
the task is started.

With the `rtems_task_start` directive the user specifies the task's starting
address and argument. The argument is used to communicate some startup
information to the task. As part of this directive, RTEMS initializes the
task's stack based upon the task's initial execution mode and start address.
The starting argument is passed to the task in accordance with the target
processor's calling convention.

The `rtems_task_restart` directive restarts a task at its initial starting
address with its original priority and execution mode, but with a possibly
different argument. The new argument may be used to distinguish between the
original invocation of the task and subsequent invocations. The task's stack
and control block are modified to reflect their original creation values.
Although references to resources that have been requested are cleared,
resources allocated by the task are NOT automatically returned to RTEMS. A
task cannot be restarted unless it has previously been started (i.e. dormant
tasks cannot be restarted). All restarted tasks are placed in the ready state.

## Suspending and Resuming Tasks

The `rtems_task_suspend` directive is used to place either the caller or
another task into a suspended state. The task remains suspended until a
`rtems_task_resume` directive is issued. This implies that a task may be
suspended as well as blocked waiting either to acquire a resource or for the
expiration of a timer.

The `rtems_task_resume` directive is used to remove another task from the
suspended state. If the task is not also blocked, resuming it will place it in
the ready state, allowing it to once again compete for the processor and
resources. If the task was blocked as well as suspended, this directive clears
the suspension and leaves the task in the blocked state.

Suspending a task which is already suspended or resuming a task which is not
suspended is considered an error. The `rtems_task_is_suspended` can be used
to determine if a task is currently suspended.

## Delaying the Currently Executing Task

The `rtems_task_wake_after` directive creates a sleep timer which allows a
task to go to sleep for a specified count of clock ticks. The task is blocked
until the count of clock ticks has elapsed, at which time the task is unblocked.
A task calling the `rtems_task_wake_after` directive with a delay of
`RTEMS_YIELD_PROCESSOR` ticks will yield the processor to any other ready
task of equal or greater priority and remain ready to execute.

The `rtems_task_wake_when` directive creates a sleep timer which allows a
task to go to sleep until a specified date and time. The calling task is
blocked until the specified date and time has occurred, at which time the task
is unblocked.

## Changing Task Priority

The `rtems_task_set_priority` directive is used to obtain or change the
current priority of either the calling task or another task. If the new
priority requested is `RTEMS_CURRENT_PRIORITY` or the task's actual priority,
then the current priority will be returned and the task's priority will remain
unchanged. If the task's priority is altered, then the task will be scheduled
according to its new priority.

The `rtems_task_restart` directive resets the priority of a task to its
original value.

## Changing Task Mode

The `rtems_task_mode` directive is used to obtain or change the current
execution mode of the calling task. A task's execution mode is used to enable
preemption, timeslicing, ASR processing, and to set the task's interrupt level.

The `rtems_task_restart` directive resets the mode of a task to its original
value.

## Task Deletion

RTEMS provides the `rtems_task_delete` directive to allow a task to delete
itself or any other task. This directive removes all RTEMS references to the
task, frees the task's control block, removes it from resource wait queues, and
deallocates its stack as well as the optional floating point context. The
task's name and ID become inactive at this time, and any subsequent references
to either of them is invalid. In fact, RTEMS may reuse the task ID for another
task which is created later in the application. A specialization of
`rtems_task_delete` is `rtems_task_exit` which deletes the calling task.

Unexpired delay timers (i.e. those used by `rtems_task_wake_after` and
`rtems_task_wake_when`) and timeout timers associated with the task are
automatically deleted, however, other resources dynamically allocated by the
task are NOT automatically returned to RTEMS. Therefore, before a task is
deleted, all of its dynamically allocated resources should be deallocated by
the user. This may be accomplished by instructing the task to delete itself
rather than directly deleting the task. Other tasks may instruct a task to
delete itself by sending a "delete self" message, event, or signal, or by
restarting the task with special arguments which instruct the task to delete
itself.

## Setting Affinity to a Single Processor

On some embedded applications targeting SMP systems, it may be beneficial to
lock individual tasks to specific processors. In this way, one can designate a
processor for I/O tasks, another for computation, etc.. The following
illustrates the code sequence necessary to assign a task an affinity for
processor with index `processor_index`.

```c
#include <rtems.h>
#include <assert.h>

void pin_to_processor(rtems_id task_id, int processor_index)
{
    rtems_status_code sc;
    cpu_set_t         cpuset;
    CPU_ZERO(&cpuset);
    CPU_SET(processor_index, &cpuset);
    sc = rtems_task_set_affinity(task_id, sizeof(cpuset), &cpuset);
    assert(sc == RTEMS_SUCCESSFUL);
}
```

It is important to note that the `cpuset` is not validated until the
`rtems_task_set_affinity` call is made. At that point, it is validated
against the current system configuration.

```{index} rtems_task_get_note()
```

```{index} rtems_task_set_note()
```

## Transition Advice for Removed Notepads

Task notepads and the associated directives {ref}`rtems_task_get_note` and
{ref}`rtems_task_set_note` were removed in RTEMS 5.1. These were never
thread-safe to access and subject to conflicting use of the notepad index by
libraries which were designed independently.

It is recommended that applications be modified to use services which are
thread safe and not subject to issues with multiple applications conflicting
over the key (e.g. notepad index) selection. For most applications, POSIX Keys
should be used. These are available in all RTEMS build configurations. It is
also possible that thread-local storage (TLS) is an option for some use cases.

```{index} rtems_task_variable_add()
```

```{index} rtems_task_variable_get()
```

```{index} rtems_task_variable_delete()
```

## Transition Advice for Removed Task Variables

Task notepads and the associated directives {ref}`rtems_task_variable_add`,
{ref}`rtems_task_variable_get` and {ref}`rtems_task_variable_delete` were
removed in RTEMS 5.1. Task variables must be replaced by POSIX Keys or
thread-local storage (TLS). POSIX Keys are available in all configurations and
support value destructors. For the TLS support consult the {title}`RTEMS CPU Architecture Supplement`.
