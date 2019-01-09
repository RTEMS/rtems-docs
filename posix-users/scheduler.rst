.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Scheduler Manager
#################

Introduction
============

The scheduler manager ...

The directives provided by the scheduler manager are:

- sched_get_priority_min_ - Get Minimum Priority Value

- sched_get_priority_max_ - Get Maximum Priority Value

- sched_rr_get_interval_ - Get Timeslicing Quantum

- sched_yield_ - Yield the Processor

Background
==========

Priority
--------

In the RTEMS implementation of the POSIX API, the priorities range from the low
priority of ``sched_get_priority_min()`` to the highest priority of
``sched_get_priority_max()``. Numerically higher values represent higher
priorities.

Scheduling Policies
-------------------

The following scheduling policies are available:

*SCHED_FIFO*
    Priority-based, preemptive scheduling with no timeslicing. This is
    equivalent to what is called "manual round-robin" scheduling.

*SCHED_RR*
    Priority-based, preemptive scheduling with timeslicing. Time quantums are
    maintained on a per-thread basis and are not reset at each context switch.
    Thus, a thread which is preempted and subsequently resumes execution will
    attempt to complete the unused portion of its time quantum.

*SCHED_OTHER*
    Priority-based, preemptive scheduling with timeslicing. Time quantums are
    maintained on a per-thread basis and are reset at each context switch.

*SCHED_SPORADIC*
    Priority-based, preemptive scheduling utilizing three additional
    parameters: budget, replenishment period, and low priority. Under this
    policy, the thread is allowed to execute for "budget" amount of time before
    its priority is lowered to "low priority". At the end of each replenishment
    period, the thread resumes its initial priority and has its budget
    replenished.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the scheduler manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. _sched_get_priority_min:

sched_get_priority_min - Get Minimum Priority Value
---------------------------------------------------
.. index:: sched_get_priority_min
.. index:: get minimum priority value

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sched.h>
    int sched_get_priority_min(
        int policy
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of the following:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The indicated policy is invalid.

**DESCRIPTION:**

This routine return the minimum (numerically and logically lowest) priority for
the specified ``policy``.

**NOTES:**

NONE

.. _sched_get_priority_max:

sched_get_priority_max - Get Maximum Priority Value
---------------------------------------------------
.. index:: sched_get_priority_max
.. index:: get maximum priority value

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sched.h>
    int sched_get_priority_max(
        int policy
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of the following:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The indicated policy is invalid.

**DESCRIPTION:**

This routine return the maximum (numerically and logically highest) priority
for the specified ``policy``.

**NOTES:**

NONE

.. _sched_rr_get_interval:

sched_rr_get_interval - Get Timeslicing Quantum
-----------------------------------------------
.. index:: sched_rr_get_interval
.. index:: get timeslicing quantum

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sched.h>
    int sched_rr_get_interval(
        pid_t            pid,
        struct timespec *interval
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of the following:

.. list-table::
 :class: rtems-table

 * - ``ESRCH``
   - The indicated process id is invalid.
 * - ``EINVAL``
   - The specified interval pointer parameter is invalid.

**DESCRIPTION:**

This routine returns the length of the timeslice quantum in the ``interval``
parameter for the specified ``pid``.

**NOTES:**

The ``pid`` argument should be 0 to indicate the calling process.

.. _sched_yield:

sched_yield - Yield the Processor
---------------------------------
.. index:: sched_yield
.. index:: yield the processor

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sched.h>
    int sched_yield( void );

**STATUS CODES:**

This routine always returns zero to indicate success.

**DESCRIPTION:**

This call forces the calling thread to yield the processor to another
thread. Normally this is used to implement voluntary round-robin task
scheduling.

**NOTES:**

NONE
