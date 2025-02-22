% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2011 Petr Benes

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# SMP Schedulers

All SMP schedulers included in RTEMS are priority based. The processors
managed by a scheduler instance are allocated to the highest priority tasks
allowed to run.

(schedulersmpedf)=

## Earliest Deadline First SMP Scheduler

This is a job-level fixed-priority scheduler using the Earliest Deadline First
(EDF) method. By convention, the maximum priority level is
$min(INT\_MAX, 2^{62} - 1)$ for background tasks. Tasks without an
active deadline are background tasks. In case deadlines are not used, then the
EDF scheduler behaves exactly like a fixed-priority scheduler. The tasks with
an active deadline have a higher priority than the background tasks. This
scheduler supports {ref}`task processor affinities <rtems_task_set_affinity>`
of one-to-one and one-to-all, e.g., a task can execute on exactly one processor
or all processors managed by the scheduler instance. The processor affinity
set of a task must contain all online processors to select the one-to-all
affinity. This is to avoid pathological cases if processors are added/removed
to/from the scheduler instance at run-time. In case the processor affinity set
contains not all online processors, then a one-to-one affinity will be used
selecting the processor with the largest index within the set of processors
currently owned by the scheduler instance. This scheduler algorithm supports
{ref}`thread pinning <ThreadPinning>`. The ready queues use a red-black tree
with the task priority as the key.

This scheduler algorithm is the default scheduler in SMP configurations if more
than one processor is configured ({ref}`CONFIGURE_MAXIMUM_PROCESSORS
<CONFIGURE_MAXIMUM_PROCESSORS>`).

(schedulersmppriority)=

## Deterministic Priority SMP Scheduler

A fixed-priority scheduler which uses a table of chains with one chain per
priority level for the ready tasks. The maximum priority level is
configurable. By default, the maximum priority level is 255 (256 priority
levels), see {ref}`CONFIGURE_MAXIMUM_PRIORITY`.

(schedulersmpprioritysimple)=

## Simple Priority SMP Scheduler

A fixed-priority scheduler which uses a sorted chain for the ready tasks. By
convention, the maximum priority level is 255. The implementation limit is
actually $2^{63} - 1$.

(schedulersmppriorityaffinity)=

## Arbitrary Processor Affinity Priority SMP Scheduler

A fixed-priority scheduler which uses a table of chains with one chain per
priority level for the ready tasks. The maximum priority level is
configurable. By default, the maximum priority level is 255 (256 priority
levels), see {ref}`CONFIGURE_MAXIMUM_PRIORITY`. This scheduler supports
arbitrary task processor affinities. The worst-case run-time complexity of
some scheduler operations exceeds $O(n)$ while $n$ is the count of
ready tasks.
