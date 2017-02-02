.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 2014.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Symmetric Multiprocessing Services
**********************************

Introduction
============

The Symmetric Multiprocessing (SMP) support of the RTEMS 4.11.0 and later is available
on

- ARM,

- PowerPC, and

- SPARC.

It must be explicitly enabled via the ``--enable-smp`` configure command line
option.  To enable SMP in the application configuration see :ref:`Enable SMP
Support for Applications`.  The default scheduler for SMP applications supports
up to 32 processors and is a global fixed priority scheduler, see also
:ref:`Configuring Clustered Schedulers`.  For example applications
see:file:`testsuites/smptests`.

.. warning::

   The SMP support in the release of RTEMS is a work in progress. Before you
   start using this RTEMS version for SMP ask on the RTEMS mailing list.

This chapter describes the services related to Symmetric Multiprocessing
provided by RTEMS.

The application level services currently provided are:

- rtems_get_processor_count_ - Get processor count

- rtems_get_current_processor_ - Get current processor index

Background
==========

Uniprocessor versus SMP Parallelism
-----------------------------------

Uniprocessor systems have long been used in embedded systems. In this hardware
model, there are some system execution characteristics which have long been
taken for granted:

- one task executes at a time

- hardware events result in interrupts

There is no true parallelism. Even when interrupts appear to occur at the same
time, they are processed in largely a serial fashion.  This is true even when
the interupt service routines are allowed to nest.  From a tasking viewpoint,
it is the responsibility of the real-time operatimg system to simulate
parallelism by switching between tasks.  These task switches occur in response
to hardware interrupt events and explicit application events such as blocking
for a resource or delaying.

With symmetric multiprocessing, the presence of multiple processors allows for
true concurrency and provides for cost-effective performance
improvements. Uniprocessors tend to increase performance by increasing clock
speed and complexity. This tends to lead to hot, power hungry microprocessors
which are poorly suited for many embedded applications.

The true concurrency is in sharp contrast to the single task and interrupt
model of uniprocessor systems. This results in a fundamental change to
uniprocessor system characteristics listed above. Developers are faced with a
different set of characteristics which, in turn, break some existing
assumptions and result in new challenges. In an SMP system with N processors,
these are the new execution characteristics.

- N tasks execute in parallel

- hardware events result in interrupts

There is true parallelism with a task executing on each processor and the
possibility of interrupts occurring on each processor. Thus in contrast to
their being one task and one interrupt to consider on a uniprocessor, there are
N tasks and potentially N simultaneous interrupts to consider on an SMP system.

This increase in hardware complexity and presence of true parallelism results
in the application developer needing to be even more cautious about mutual
exclusion and shared data access than in a uniprocessor embedded system. Race
conditions that never or rarely happened when an application executed on a
uniprocessor system, become much more likely due to multiple threads executing
in parallel. On a uniprocessor system, these race conditions would only happen
when a task switch occurred at just the wrong moment. Now there are N-1 tasks
executing in parallel all the time and this results in many more opportunities
for small windows in critical sections to be hit.

Task Affinity
-------------
.. index:: task affinity
.. index:: thread affinity

RTEMS provides services to manipulate the affinity of a task. Affinity is used
to specify the subset of processors in an SMP system on which a particular task
can execute.

By default, tasks have an affinity which allows them to execute on any
available processor.

Task affinity is a possible feature to be supported by SMP-aware
schedulers. However, only a subset of the available schedulers support
affinity. Although the behavior is scheduler specific, if the scheduler does
not support affinity, it is likely to ignore all attempts to set affinity.

The scheduler with support for arbitary processor affinities uses a proof of
concept implementation.  See https://devel.rtems.org/ticket/2510.

Task Migration
--------------
.. index:: task migration
.. index:: thread migration

With more than one processor in the system tasks can migrate from one processor
to another.  There are four reasons why tasks migrate in RTEMS.

- The scheduler changes explicitly via
  :ref:`rtems_task_set_scheduler() <rtems_task_set_scheduler>` or similar
  directives.

- The task processor affinity changes explicitly via
  :ref:`rtems_task_set_affinity() <rtems_task_set_affinity>` or similar
  directives.

- The task resumes execution after a blocking operation.  On a priority based
  scheduler it will evict the lowest priority task currently assigned to a
  processor in the processor set managed by the scheduler instance.

- The task moves temporarily to another scheduler instance due to locking
  protocols like the :ref:`MrsP` or the :ref:`OMIP`.

Task migration should be avoided so that the working set of a task can stay on
the most local cache level.

Clustered Scheduling
--------------------

The scheduler is responsible to assign processors to some of the threads which
are ready to execute.  Trouble starts if more ready threads than processors
exist at the same time.  There are various rules how the processor assignment
can be performed attempting to fulfill additional constraints or yield some
overall system properties.  As a matter of fact it is impossible to meet all
requirements at the same time.  The way a scheduler works distinguishes
real-time operating systems from general purpose operating systems.

We have clustered scheduling in case the set of processors of a system is
partitioned into non-empty pairwise-disjoint subsets of processors.  These
subsets are called clusters.  Clusters with a cardinality of one are
partitions.  Each cluster is owned by exactly one scheduler instance.  In case
the cluster size equals the processor count, it is called global scheduling.

Modern SMP systems have multi-layer caches.  An operating system which neglects
cache constraints in the scheduler will not yield good performance.  Real-time
operating systems usually provide priority (fixed or job-level) based
schedulers so that each of the highest priority threads is assigned to a
processor.  Priority based schedulers have difficulties in providing cache
locality for threads and may suffer from excessive thread migrations
:cite:`Brandenburg:2011:SL` :cite:`Compagnin:2014:RUN`.  Schedulers that use local run
queues and some sort of load-balancing to improve the cache utilization may not
fulfill global constraints :cite:`Gujarati:2013:LPP` and are more difficult to
implement than one would normally expect :cite:`Lozi:2016:LSDWC`.

Clustered scheduling was implemented for RTEMS SMP to best use the cache
topology of a system and to keep the worst-case latencies under control.  The
low-level SMP locks use FIFO ordering.  So, the worst-case run-time of
operations increases with each processor involved.  The scheduler configuration
is quite flexible and done at link-time, see :ref:`Configuring Clustered
Schedulers`.  It is possible to re-assign processors to schedulers during
run-time via :ref:`rtems_scheduler_add_processor()
<rtems_scheduler_add_processor>` and :ref:`rtems_scheduler_remove_processor()
<rtems_scheduler_remove_processor>`.  The schedulers are implemented in an
object-oriented fashion.

The problem is to provide synchronization
primitives for inter-cluster synchronization (more than one cluster is involved
in the synchronization process). In RTEMS there are currently some means
available

- events,

- message queues,

- mutexes using the :ref:`OMIP`,

- mutexes using the :ref:`MrsP`, and

- binary and counting semaphores.

The clustered scheduling approach enables separation of functions with
real-time requirements and functions that profit from fairness and high
throughput provided the scheduler instances are fully decoupled and adequate
inter-cluster synchronization primitives are used.

To set the scheduler of a task see :ref:`rtems_scheduler_ident()
<rtems_scheduler_ident>` and :ref:`rtems_task_set_scheduler()
<rtems_task_set_scheduler>`.

Scheduler Helping Protocol
--------------------------

The scheduler provides a helping protocol to support locking protocols like
*Migratory Priority Inheritance* or the *Multiprocessor Resource Sharing
Protocol*.  Each ready task can use at least one scheduler node at a time to
gain access to a processor.  Each scheduler node has an owner, a user and an
optional idle task.  The owner of a scheduler node is determined a task
creation and never changes during the life time of a scheduler node.  The user
of a scheduler node may change due to the scheduler helping protocol.  A
scheduler node is in one of the four scheduler help states:

:dfn:`help yourself`
    This scheduler node is solely used by the owner task.  This task owns no
    resources using a helping protocol and thus does not take part in the
    scheduler helping protocol.  No help will be provided for other tasks.

:dfn:`help active owner`
    This scheduler node is owned by a task actively owning a resource and can
    be used to help out tasks.  In case this scheduler node changes its state
    from ready to scheduled and the task executes using another node, then an
    idle task will be provided as a user of this node to temporarily execute on
    behalf of the owner task.  Thus lower priority tasks are denied access to
    the processors of this scheduler instance.  In case a task actively owning
    a resource performs a blocking operation, then an idle task will be used
    also in case this node is in the scheduled state.

:dfn:`help active rival`
    This scheduler node is owned by a task actively obtaining a resource
    currently owned by another task and can be used to help out tasks.  The
    task owning this node is ready and will give away its processor in case the
    task owning the resource asks for help.

:dfn:`help passive`
    This scheduler node is owned by a task obtaining a resource currently owned
    by another task and can be used to help out tasks.  The task owning this
    node is blocked.

The following scheduler operations return a task in need for help

- unblock,

- change priority,

- yield, and

- ask for help.

A task in need for help is a task that encounters a scheduler state change from
scheduled to ready (this is a pre-emption by a higher priority task) or a task
that cannot be scheduled in an unblock operation.  Such a task can ask tasks
which depend on resources owned by this task for help.

In case it is not possible to schedule a task in need for help, then the
scheduler nodes available for the task will be placed into the set of ready
scheduler nodes of the corresponding scheduler instances.  Once a state change
from ready to scheduled happens for one of scheduler nodes it will be used to
schedule the task in need for help.

The ask for help scheduler operation is used to help tasks in need for help
returned by the operations mentioned above.  This operation is also used in
case the root of a resource sub-tree owned by a task changes.

The run-time of the ask for help procedures depend on the size of the resource
tree of the task needing help and other resource trees in case tasks in need
for help are produced during this operation.  Thus the worst-case latency in
the system depends on the maximum resource tree size of the application.

OpenMP
------

OpenMP support for RTEMS is available via the GCC provided libgomp.  There is
libgomp support for RTEMS in the POSIX configuration of libgomp since GCC 4.9
(requires a Newlib snapshot after 2015-03-12). In GCC 6.1 or later (requires a
Newlib snapshot after 2015-07-30 for <sys/lock.h> provided self-contained
synchronization objects) there is a specialized libgomp configuration for RTEMS
which offers a significantly better performance compared to the POSIX
configuration of libgomp.  In addition application configurable thread pools
for each scheduler instance are available in GCC 6.1 or later.

The run-time configuration of libgomp is done via environment variables
documented in the `libgomp manual <https://gcc.gnu.org/onlinedocs/libgomp/>`_.
The environment variables are evaluated in a constructor function which
executes in the context of the first initialization task before the actual
initialization task function is called (just like a global C++ constructor).
To set application specific values, a higher priority constructor function must
be used to set up the environment variables.

.. code-block:: c

    #include <stdlib.h>
    void __attribute__((constructor(1000))) config_libgomp( void )
    {
        setenv( "OMP_DISPLAY_ENV", "VERBOSE", 1 );
        setenv( "GOMP_SPINCOUNT", "30000", 1 );
        setenv( "GOMP_RTEMS_THREAD_POOLS", "1$2@SCHD", 1 );
    }

The environment variable ``GOMP_RTEMS_THREAD_POOLS`` is RTEMS-specific.  It
determines the thread pools for each scheduler instance.  The format for
``GOMP_RTEMS_THREAD_POOLS`` is a list of optional
``<thread-pool-count>[$<priority>]@<scheduler-name>`` configurations separated
by ``:`` where:

- ``<thread-pool-count>`` is the thread pool count for this scheduler instance.

- ``$<priority>`` is an optional priority for the worker threads of a thread
  pool according to ``pthread_setschedparam``.  In case a priority value is
  omitted, then a worker thread will inherit the priority of the OpenMP master
  thread that created it.  The priority of the worker thread is not changed by
  libgomp after creation, even if a new OpenMP master thread using the worker
  has a different priority.

- ``@<scheduler-name>`` is the scheduler instance name according to the RTEMS
  application configuration.

In case no thread pool configuration is specified for a scheduler instance,
then each OpenMP master thread of this scheduler instance will use its own
dynamically allocated thread pool.  To limit the worker thread count of the
thread pools, each OpenMP master thread must call ``omp_set_num_threads``.

Lets suppose we have three scheduler instances ``IO``, ``WRK0``, and ``WRK1``
with ``GOMP_RTEMS_THREAD_POOLS`` set to ``"1@WRK0:3$4@WRK1"``.  Then there are
no thread pool restrictions for scheduler instance ``IO``.  In the scheduler
instance ``WRK0`` there is one thread pool available.  Since no priority is
specified for this scheduler instance, the worker thread inherits the priority
of the OpenMP master thread that created it.  In the scheduler instance
``WRK1`` there are three thread pools available and their worker threads run at
priority four.

Application Issues
==================

Most operating system services provided by the uni-processor RTEMS are
available in SMP configurations as well.  However, applications designed for an
uni-processor environment may need some changes to correctly run in an SMP
configuration.

As discussed earlier, SMP systems have opportunities for true parallelism which
was not possible on uni-processor systems. Consequently, multiple techniques
that provided adequate critical sections on uni-processor systems are unsafe on
SMP systems. In this section, some of these unsafe techniques will be
discussed.

In general, applications must use proper operating system provided mutual
exclusion mechanisms to ensure correct behavior.

Task variables
--------------

Task variables are ordinary global variables with a dedicated value for each
thread.  During a context switch from the executing thread to the heir thread,
the value of each task variable is saved to the thread control block of the
executing thread and restored from the thread control block of the heir thread.
This is inherently broken if more than one executing thread exists.
Alternatives to task variables are POSIX keys and :ref:`TLS <TLS>`.  All use
cases of task variables in the RTEMS code base were replaced with alternatives.
The task variable API has been removed in RTEMS 4.12.

Highest Priority Thread Never Walks Alone
-----------------------------------------

On a uni-processor system, it is safe to assume that when the highest priority
task in an application executes, it will execute without being preempted until
it voluntarily blocks. Interrupts may occur while it is executing, but there
will be no context switch to another task unless the highest priority task
voluntarily initiates it.

Given the assumption that no other tasks will have their execution interleaved
with the highest priority task, it is possible for this task to be constructed
such that it does not need to acquire a mutex for protected access to shared
data.

In an SMP system, it cannot be assumed there will never be a single task
executing. It should be assumed that every processor is executing another
application task. Further, those tasks will be ones which would not have been
executed in a uni-processor configuration and should be assumed to have data
synchronization conflicts with what was formerly the highest priority task
which executed without conflict.

Disabling of Thread Pre-Emption
-------------------------------

A thread which disables pre-emption prevents that a higher priority thread gets
hold of its processor involuntarily.  In uni-processor configurations, this can
be used to ensure mutual exclusion at thread level.  In SMP configurations,
however, more than one executing thread may exist.  Thus, it is impossible to
ensure mutual exclusion using this mechanism.  In order to prevent that
applications using pre-emption for this purpose, would show inappropriate
behaviour, this feature is disabled in SMP configurations and its use would
case run-time errors.

Disabling of Interrupts
-----------------------

A low overhead means that ensures mutual exclusion in uni-processor
configurations is the disabling of interrupts around a critical section.  This
is commonly used in device driver code.  In SMP configurations, however,
disabling the interrupts on one processor has no effect on other processors.
So, this is insufficient to ensure system-wide mutual exclusion.  The macros

* :ref:`rtems_interrupt_disable() <rtems_interrupt_disable>`,

* :ref:`rtems_interrupt_enable() <rtems_interrupt_enable>`, and

* :ref:`rtems_interrupt_flash() <rtems_interrupt_flash>`.

are disabled in SMP configurations and its use will cause compile-time warnings
and link-time errors.  In the unlikely case that interrupts must be disabled on
the current processor, the

* :ref:`rtems_interrupt_local_disable() <rtems_interrupt_local_disable>`, and

* :ref:`rtems_interrupt_local_enable() <rtems_interrupt_local_enable>`.

macros are now available in all configurations.

Since disabling of interrupts is insufficient to ensure system-wide mutual
exclusion on SMP a new low-level synchronization primitive was added --
interrupt locks.  The interrupt locks are a simple API layer on top of the SMP
locks used for low-level synchronization in the operating system core.
Currently, they are implemented as a ticket lock.  In uni-processor
configurations, they degenerate to simple interrupt disable/enable sequences by
means of the C pre-processor.  It is disallowed to acquire a single interrupt
lock in a nested way.  This will result in an infinite loop with interrupts
disabled.  While converting legacy code to interrupt locks, care must be taken
to avoid this situation to happen.

.. code-block:: c
    :linenos:

    #include <rtems.h>

    void legacy_code_with_interrupt_disable_enable( void )
    {
      rtems_interrupt_level level;

      rtems_interrupt_disable( level );
      /* Critical section */
      rtems_interrupt_enable( level );
    }

    RTEMS_INTERRUPT_LOCK_DEFINE( static, lock, "Name" )

    void smp_ready_code_with_interrupt_lock( void )
    {
      rtems_interrupt_lock_context lock_context;

      rtems_interrupt_lock_acquire( &lock, &lock_context );
      /* Critical section */
      rtems_interrupt_lock_release( &lock, &lock_context );
    }

An alternative to the RTEMS-specific interrupt locks are POSIX spinlocks.  The
:c:type:`pthread_spinlock_t` is defined as a self-contained object, e.g. the
user must provide the storage for this synchronization object.

.. code-block:: c
    :linenos:

    #include <assert.h>
    #include <pthread.h>

    pthread_spinlock_t lock;

    void smp_ready_code_with_posix_spinlock( void )
    {
      int error;

      error = pthread_spin_lock( &lock );
      assert( error == 0 );
      /* Critical section */
      error = pthread_spin_unlock( &lock );
      assert( error == 0 );
    }

In contrast to POSIX spinlock implementation on Linux or FreeBSD, it is not
allowed to call blocking operating system services inside the critical section.
A recursive lock attempt is a severe usage error resulting in an infinite loop
with interrupts disabled.  Nesting of different locks is allowed.  The user
must ensure that no deadlock can occur.  As a non-portable feature the locks
are zero-initialized, e.g. statically initialized global locks reside in the
``.bss`` section and there is no need to call :c:func:`pthread_spin_init`.

Interrupt Service Routines Execute in Parallel With Threads
-----------------------------------------------------------

On a machine with more than one processor, interrupt service routines (this
includes timer service routines installed via :ref:`rtems_timer_fire_after()
<rtems_timer_fire_after>`) and threads can execute in parallel.  Interrupt
service routines must take this into account and use proper locking mechanisms
to protect critical sections from interference by threads (interrupt locks or
POSIX spinlocks).  This likely requires code modifications in legacy device
drivers.

Timers Do Not Stop Immediately
------------------------------

Timer service routines run in the context of the clock interrupt.  On
uni-processor configurations, it is sufficient to disable interrupts and remove
a timer from the set of active timers to stop it.  In SMP configurations,
however, the timer service routine may already run and wait on an SMP lock
owned by the thread which is about to stop the timer.  This opens the door to
subtle synchronization issues.  During destruction of objects, special care
must be taken to ensure that timer service routines cannot access (partly or
fully) destroyed objects.

False Sharing of Cache Lines Due to Objects Table
-------------------------------------------------

The Classic API and most POSIX API objects are indirectly accessed via an
object identifier.  The user-level functions validate the object identifier and
map it to the actual object structure which resides in a global objects table
for each object class.  So, unrelated objects are packed together in a table.
This may result in false sharing of cache lines.  The effect of false sharing
of cache lines can be observed with the `TMFINE 1
<https://git.rtems.org/rtems/tree/testsuites/tmtests/tmfine01>`_ test program
on a suitable platform, e.g. QorIQ T4240.  High-performance SMP applications
need full control of the object storage :cite:`Drepper:2007:Memory`.
Therefore, self-contained synchronization objects are now available for RTEMS.

Implementation Details
======================

Thread Dispatch Details
-----------------------

This section gives background information to developers interested in the
interrupt latencies introduced by thread dispatching.  A thread dispatch
consists of all work which must be done to stop the currently executing thread
on a processor and hand over this processor to an heir thread.

In SMP systems, scheduling decisions on one processor must be propagated
to other processors through inter-processor interrupts.  A thread dispatch
which must be carried out on another processor does not happen instantaneously.
Thus, several thread dispatch requests might be in the air and it is possible
that some of them may be out of date before the corresponding processor has
time to deal with them.  The thread dispatch mechanism uses three per-processor
variables,

- the executing thread,

- the heir thread, and

- a boolean flag indicating if a thread dispatch is necessary or not.

Updates of the heir thread are done via a normal store operation.  The thread
dispatch necessary indicator of another processor is set as a side-effect of an
inter-processor interrupt.  So, this change notification works without the use
of locks.  The thread context is protected by a TTAS lock embedded in the
context to ensure that it is used on at most one processor at a time.
Normally, only thread-specific or per-processor locks are used during a thread
dispatch.  This implementation turned out to be quite efficient and no lock
contention was observed in the testsuite.  The heavy-weight thread dispatch
sequence is only entered in case the thread dispatch indicator is set.

The context-switch is performed with interrupts enabled.  During the transition
from the executing to the heir thread neither the stack of the executing nor
the heir thread must be used during interrupt processing.  For this purpose a
temporary per-processor stack is set up which may be used by the interrupt
prologue before the stack is switched to the interrupt stack.

Directives
==========

This section details the symmetric multiprocessing services.  A subsection is
dedicated to each of these services and describes the calling sequence, related
constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_get_processor_count:

GET_PROCESSOR_COUNT - Get processor count
-----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        uint32_t rtems_get_processor_count(void);

DIRECTIVE STATUS CODES:
    The count of processors in the system.

DESCRIPTION:
    In uni-processor configurations, a value of one will be returned.

    In SMP configurations, this returns the value of a global variable set
    during system initialization to indicate the count of utilized processors.
    The processor count depends on the physically or virtually available
    processors and application configuration.  The value will always be less
    than or equal to the maximum count of application configured processors.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_get_current_processor:

GET_CURRENT_PROCESSOR - Get current processor index
---------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        uint32_t rtems_get_current_processor(void);

DIRECTIVE STATUS CODES:
    The index of the current processor.

DESCRIPTION:
    In uni-processor configurations, a value of zero will be returned.

    In SMP configurations, an architecture specific method is used to obtain the
    index of the current processor in the system.  The set of processor indices
    is the range of integers starting with zero up to the processor count minus
    one.

    Outside of sections with disabled thread dispatching the current processor
    index may change after every instruction since the thread may migrate from
    one processor to another.  Sections with disabled interrupts are sections
    with thread dispatching disabled.

NOTES:
    None.
