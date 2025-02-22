% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2011 Petr Benes

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Uniprocessor Schedulers

All uniprocessor schedulers included in RTEMS are priority based. The
processor is allocated to the highest priority task allowed to run.

(schedulerpriority)=

## Deterministic Priority Scheduler

This is the scheduler implementation which has always been in RTEMS. After the
4.10 release series, it was factored into a pluggable scheduler selection. It
schedules tasks using a priority based algorithm which takes into account
preemption. It is implemented using an array of FIFOs with a FIFO per
priority. It maintains a bitmap which is used to track which priorities have
ready tasks.

This algorithm is deterministic (e.g., predictable and fixed) in execution time.
This comes at the cost of using slightly over three (3) kilobytes of RAM on a
system configured to support 256 priority levels.

This scheduler is only aware of a single core.

(schedulerprioritysimple)=

## Simple Priority Scheduler

This scheduler implementation has the same behaviour as the Deterministic
Priority Scheduler but uses only one linked list to manage all ready tasks.
When a task is readied, a linear search of that linked list is performed to
determine where to insert the newly readied task.

This algorithm uses much less RAM than the Deterministic Priority Scheduler but
is *O(n)* where *n* is the number of ready tasks. In a small system with a
small number of tasks, this will not be a performance issue. Reducing RAM
consumption is often critical in small systems that are incapable of
supporting a large number of tasks.

This scheduler is only aware of a single core.

```{index} earliest deadline first scheduling
```

(scheduleredf)=

## Earliest Deadline First Scheduler

This is an alternative scheduler in RTEMS for single-core applications. The
primary EDF advantage is high total CPU utilization (theoretically up to
100%). It assumes that tasks have priorities equal to deadlines.

This EDF is initially preemptive, however, individual tasks may be declared
not-preemptive. Deadlines are declared using only Rate Monotonic manager whose
goal is to handle periodic behavior. Period is always equal to the deadline. All
ready tasks reside in a single ready queue implemented using a red-black tree.

This implementation of EDF schedules two different types of task priority types
while each task may switch between the two types within its execution. If a
task does have a deadline declared using the Rate Monotonic manager, the task
is deadline-driven and its priority is equal to deadline. On the contrary, if a
task does not have any deadline or the deadline is cancelled using the Rate
Monotonic manager, the task is considered a background task with priority equal
to that assigned upon initialization in the same manner as for priority
scheduler. Each background task is of lower importance than each
deadline-driven one and is scheduled when no deadline-driven task and no higher
priority background task is ready to run.

Every deadline-driven scheduling algorithm requires means for tasks to claim a
deadline. The Rate Monotonic Manager is responsible for handling periodic
execution. In RTEMS periods are equal to deadlines, thus if a task announces a
period, it has to be finished until the end of this period. The call of
`rtems_rate_monotonic_period` passes the scheduler the length of an oncoming
deadline. Moreover, the `rtems_rate_monotonic_cancel` and
`rtems_rate_monotonic_delete` calls clear the deadlines assigned to the task.

```{index} constant bandwidth server scheduling
```

(schedulercbs)=

## Constant Bandwidth Server Scheduling (CBS)

This is an alternative scheduler in RTEMS for single-core applications. The
CBS is a budget aware extension of EDF scheduler. The main goal of this
scheduler is to ensure temporal isolation of tasks meaning that a task's
execution in terms of meeting deadlines must not be influenced by other tasks
as if they were run on multiple independent processors.

Each task can be assigned a server (current implementation supports only one
task per server). The server is characterized by period (deadline) and
computation time (budget). The ratio budget/period yields bandwidth, which is
the fraction of CPU to be reserved by the scheduler for each subsequent period.

The CBS is equipped with a set of rules applied to tasks attached to servers
ensuring that deadline miss because of another task cannot occur. In case a
task breaks one of the rules, its priority is pulled to background until the
end of its period and then restored again. The rules are:

- Task cannot exceed its registered budget,
- Task cannot be unblocked when a ratio between remaining budget and remaining
  deadline is higher than declared bandwidth.

The CBS provides an extensive API. Unlike EDF, the
`rtems_rate_monotonic_period` does not declare a deadline because it is
carried out using CBS API. This call only announces next period.
