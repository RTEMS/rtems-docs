.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Thread Manager
##############

Introduction
============

The thread manager implements the functionality required of the thread manager
as defined by POSIX 1003.1b. This standard requires that a compliant operating
system provide the facilties to manage multiple threads of control and defines
the API that must be provided.

The services provided by the thread manager are:

- pthread_attr_init_ - Initialize a Thread Attribute Set

- pthread_attr_destroy_ - Destroy a Thread Attribute Set

- pthread_attr_setdetachstate_ - Set Detach State

- pthread_attr_getdetachstate_ - Get Detach State

- pthread_attr_setstacksize_ - Set Thread Stack Size

- pthread_attr_getstacksize_ - Get Thread Stack Size

- pthread_attr_setstackaddr_ - Set Thread Stack Address

- pthread_attr_getstackaddr_ - Get Thread Stack Address

- pthread_attr_setscope_ - Set Thread Scheduling Scope

- pthread_attr_getscope_ - Get Thread Scheduling Scope

- pthread_attr_setinheritsched_ - Set Inherit Scheduler Flag

- pthread_attr_getinheritsched_ - Get Inherit Scheduler Flag

- pthread_attr_setschedpolicy_ - Set Scheduling Policy

- pthread_attr_getschedpolicy_ - Get Scheduling Policy

- pthread_attr_setschedparam_ - Set Scheduling Parameters

- pthread_attr_getschedparam_ - Get Scheduling Parameters

- pthread_attr_getaffinity_np_ - Get Thread Affinity Attribute

- pthread_attr_setaffinity_np_ - Set Thread Affinity Attribute

- pthread_create_ - Create a Thread

- pthread_exit_ - Terminate the Current Thread

- pthread_detach_ - Detach a Thread

- pthread_getconcurrency_ - Get Thread Level of Concurrency

- pthread_setconcurrency_ - Set Thread Level of Concurrency

- pthread_getattr_np_ - Get Thread Attributes

- pthread_join_ - Wait for Thread Termination

- pthread_self_ - Get Thread ID

- pthread_equal_ - Compare Thread IDs

- pthread_once_ - Dynamic Package Initialization

- pthread_setschedparam_ - Set Thread Scheduling Parameters

- pthread_getschedparam_ - Get Thread Scheduling Parameters

- pthread_getaffinity_np_ - Get Thread Affinity

- pthread_setaffinity_np_ - Set Thread Affinity

Background
==========

Thread Attributes
-----------------

Thread attributes are utilized only at thread creation time. A thread attribute
structure may be initialized and passed as an argument to the
``pthread_create`` routine.

*stack address*
    is the address of the optionally user specified stack area for this thread.
    If this value is NULL, then RTEMS allocates the memory for the thread stack
    from the RTEMS Workspace Area. Otherwise, this is the user specified
    address for the memory to be used for the thread's stack. Each thread must
    have a distinct stack area. Each processor family has different alignment
    rules which should be followed.

*stack size*
    is the minimum desired size for this thread's stack area.  If the size of
    this area as specified by the stack size attribute is smaller than the
    minimum for this processor family and the stack is not user specified, then
    RTEMS will automatically allocate a stack of the minimum size for this
    processor family.

*contention scope*
    specifies the scheduling contention scope. RTEMS only supports the
    PTHREAD_SCOPE_PROCESS scheduling contention scope.

*scheduling inheritance*
    specifies whether a user specified or the scheduling policy and parameters
    of the currently executing thread are to be used. When this is
    PTHREAD_INHERIT_SCHED, then the scheduling policy and parameters of the
    currently executing thread are inherited by the newly created thread.

*scheduling policy and parameters*
    specify the manner in which the thread will contend for the processor.  The
    scheduling parameters are interpreted based on the specified policy.  All
    policies utilize the thread priority parameter.

Operations
==========

There is currently no text in this section.

Services
========

This section details the thread manager's services.  A subsection is dedicated
to each of this manager's services and describes the calling sequence, related
constants, usage, and status codes.

.. _pthread_attr_init:

pthread_attr_init - Initialize a Thread Attribute Set
-----------------------------------------------------
.. index:: pthread_attr_init
.. index:: initialize a thread attribute set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_init(
        pthread_attr_t *attr
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_init`` routine initializes the thread attributes object
specified by ``attr`` with the default value for all of the individual
attributes.

**NOTES:**

The settings in the default attributes are implementation defined. For RTEMS,
the default attributes are as follows:

.. list-table::
 :class: rtems-table

 * - *stackadr*
   - is not set to indicate that RTEMS is to allocate the stack memory.
 * - *stacksize*
   - is set to ``PTHREAD_MINIMUM_STACK_SIZE``.
 * - *contentionscope*
   - is set to ``PTHREAD_SCOPE_PROCESS``.
 * - *inheritsched*
   - is set to ``PTHREAD_INHERIT_SCHED`` to indicate that the created thread
     inherits its scheduling attributes from its parent.
 * - detachstate
   - is set to ``PTHREAD_CREATE_JOINABLE``.

.. _pthread_attr_destroy:

pthread_attr_destroy - Destroy a Thread Attribute Set
-----------------------------------------------------
.. index:: pthread_attr_destroy
.. index:: destroy a thread attribute set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_destroy(
        pthread_attr_t *attr
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_attr_destroy`` routine is used to destroy a thread attributes
object. The behavior of using an attributes object after it is destroyed is
implementation dependent.

**NOTES:**

NONE

.. _pthread_attr_setdetachstate:

pthread_attr_setdetachstate - Set Detach State
----------------------------------------------
.. index:: pthread_attr_setdetachstate
.. index:: set detach state

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setdetachstate(
        pthread_attr_t *attr,
        int             detachstate
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The detachstate argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setdetachstate`` routine is used to value of the
``detachstate`` attribute. This attribute controls whether the thread is
created in a detached state.

The ``detachstate`` can be either ``PTHREAD_CREATE_DETACHED`` or
``PTHREAD_CREATE_JOINABLE``. The default value for all threads is
``PTHREAD_CREATE_JOINABLE``.

**NOTES:**

If a thread is in a detached state, then the use of the ID with the
``pthread_detach`` or ``pthread_join`` routines is an error.

.. _pthread_attr_getdetachstate:

pthread_attr_getdetachstate - Get Detach State
----------------------------------------------
.. index:: pthread_attr_getdetachstate
.. index:: get detach state

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getdetachstate(
        const pthread_attr_t *attr,
        int                  *detachstate
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The detatchstate pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getdetachstate`` routine is used to obtain the current value
of the ``detachstate`` attribute as specified by the ``attr`` thread attribute
object.

**NOTES:**

NONE

.. _pthread_attr_setstacksize:

pthread_attr_setstacksize - Set Thread Stack Size
-------------------------------------------------
.. index:: pthread_attr_setstacksize
.. index:: set thread stack size

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setstacksize(
        pthread_attr_t *attr,
        size_t          stacksize
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_attr_setstacksize`` routine is used to set the ``stacksize``
attribute in the ``attr`` thread attribute object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_ATTR_STACKSIZE`` to indicate that this routine is supported.

If the specified stacksize is below the minimum required for this CPU
(``PTHREAD_STACK_MIN``, then the stacksize will be set to the minimum for this
CPU.

.. _pthread_attr_getstacksize:

pthread_attr_getstacksize - Get Thread Stack Size
-------------------------------------------------
.. index:: pthread_attr_getstacksize
.. index:: get thread stack size

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getstacksize(
        const pthread_attr_t *attr,
        size_t               *stacksize
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The stacksize pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getstacksize`` routine is used to obtain the ``stacksize``
attribute in the ``attr`` thread attribute object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_ATTR_STACKSIZE`` to indicate that this routine is supported.

.. _pthread_attr_setstackaddr:

pthread_attr_setstackaddr - Set Thread Stack Address
----------------------------------------------------
.. index:: pthread_attr_setstackaddr
.. index:: set thread stack address

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setstackaddr(
        pthread_attr_t *attr,
        void           *stackaddr
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_attr_setstackaddr`` routine is used to set the ``stackaddr``
attribute in the ``attr`` thread attribute object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_ATTR_STACKADDR`` to indicate that this routine is supported.

It is imperative to the proper operation of the system that each thread have
sufficient stack space.

.. _pthread_attr_getstackaddr:

pthread_attr_getstackaddr - Get Thread Stack Address
----------------------------------------------------
.. index:: pthread_attr_getstackaddr
.. index:: get thread stack address

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getstackaddr(
        const pthread_attr_t  *attr,
        void                 **stackaddr
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The stackaddr pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getstackaddr`` routine is used to obtain the ``stackaddr``
attribute in the ``attr`` thread attribute object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_ATTR_STACKADDR`` to indicate that this routine is supported.

.. _pthread_attr_setscope:

pthread_attr_setscope - Set Thread Scheduling Scope
---------------------------------------------------
.. index:: pthread_attr_setscope
.. index:: set thread scheduling scope

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setscope(
        pthread_attr_t *attr,
        int             contentionscope
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The contention scope specified is not valid.
 * - ``ENOTSUP``
   - The contention scope specified (``PTHREAD_SCOPE_SYSTEM``) is not supported.

**DESCRIPTION:**

The ``pthread_attr_setscope`` routine is used to set the contention scope field
in the thread attribute object ``attr`` to the value specified by
``contentionscope``.

The ``contentionscope`` must be either ``PTHREAD_SCOPE_SYSTEM`` to indicate
that the thread is to be within system scheduling contention or
``PTHREAD_SCOPE_PROCESS`` indicating that the thread is to be within the
process scheduling contention scope.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_getscope:

pthread_attr_getscope - Get Thread Scheduling Scope
---------------------------------------------------
.. index:: pthread_attr_getscope
.. index:: get thread scheduling scope

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getscope(
        const pthread_attr_t *attr,
        int                  *contentionscope
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The contentionscope pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getscope`` routine is used to obtain the value of the
contention scope field in the thread attributes object ``attr``. The current
value is returned in ``contentionscope``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_setinheritsched:

pthread_attr_setinheritsched - Set Inherit Scheduler Flag
---------------------------------------------------------
.. index:: pthread_attr_setinheritsched
.. index:: set inherit scheduler flag

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setinheritsched(
        pthread_attr_t *attr,
        int             inheritsched
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The specified scheduler inheritance argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setinheritsched`` routine is used to set the inherit
scheduler field in the thread attribute object ``attr`` to the value specified
by ``inheritsched``.

The ``contentionscope`` must be either ``PTHREAD_INHERIT_SCHED`` to indicate
that the thread is to inherit the scheduling policy and parameters fromthe
creating thread, or ``PTHREAD_EXPLICIT_SCHED`` to indicate that the scheduling
policy and parameters for this thread are to be set from the corresponding
values in the attributes object.  If ``contentionscope`` is
``PTHREAD_INHERIT_SCHED``, then the scheduling attributes in the ``attr``
structure will be ignored at thread creation time.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_getinheritsched:

pthread_attr_getinheritsched - Get Inherit Scheduler Flag
---------------------------------------------------------
.. index:: pthread_attr_getinheritsched
.. index:: get inherit scheduler flag

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getinheritsched(
        const pthread_attr_t *attr,
        int                  *inheritsched
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The inheritsched pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getinheritsched`` routine is used to object the current
value of the inherit scheduler field in the thread attribute object ``attr``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_setschedpolicy:

pthread_attr_setschedpolicy - Set Scheduling Policy
---------------------------------------------------
.. index:: pthread_attr_setschedpolicy
.. index:: set scheduling policy

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setschedpolicy(
        pthread_attr_t *attr,
        int             policy
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``ENOTSUP``
   - The specified scheduler policy argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setschedpolicy`` routine is used to set the scheduler policy
field in the thread attribute object ``attr`` to the value specified by
``policy``.

Scheduling policies may be one of the following:

- ``SCHED_DEFAULT``

- ``SCHED_FIFO``

- ``SCHED_RR``

- ``SCHED_SPORADIC``

- ``SCHED_OTHER``

The precise meaning of each of these is discussed elsewhere in this manual.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_getschedpolicy:

pthread_attr_getschedpolicy - Get Scheduling Policy
---------------------------------------------------
.. index:: pthread_attr_getschedpolicy
.. index:: get scheduling policy

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getschedpolicy(
        const pthread_attr_t *attr,
        int                  *policy
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The specified scheduler policy argument pointer is invalid.

**DESCRIPTION:**

The ``pthread_attr_getschedpolicy`` routine is used to obtain the scheduler
policy field from the thread attribute object ``attr``.  The value of this
field is returned in ``policy``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_setschedparam:

pthread_attr_setschedparam - Set Scheduling Parameters
------------------------------------------------------
.. index:: pthread_attr_setschedparam
.. index:: set scheduling parameters

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_setschedparam(
        pthread_attr_t           *attr,
        const struct sched_param  param
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The specified scheduler parameter argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setschedparam`` routine is used to set the scheduler
parameters field in the thread attribute object ``attr`` to the value specified
by ``param``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_getschedparam:

pthread_attr_getschedparam - Get Scheduling Parameters
------------------------------------------------------
.. index:: pthread_attr_getschedparam
.. index:: get scheduling parameters

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_attr_getschedparam(
        const pthread_attr_t *attr,
        struct sched_param   *param
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The specified scheduler parameter argument pointer is invalid.

**DESCRIPTION:**

The ``pthread_attr_getschedparam`` routine is used to obtain the scheduler
parameters field from the thread attribute object ``attr``.  The value of this
field is returned in ``param``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_attr_getaffinity_np:

pthread_attr_getaffinity_np - Get Thread Affinity Attribute
-----------------------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_attr_getaffinity_np(
        const pthread_attr_t *attr,
        size_t                cpusetsize,
        cpu_set_t            *cpuset
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EFAULT``
   - The attribute pointer argument is invalid.
 * - ``EFAULT``
   - The cpuset pointer argument is invalid.
 * - ``EINVAL``
   - The ``cpusetsize`` does not match the value of ``affinitysetsize`` field
     in the thread attribute object.

**DESCRIPTION:**

The ``pthread_attr_getaffinity_np`` routine is used to obtain the
``affinityset`` field from the thread attribute object ``attr``.  The value of
this field is returned in ``cpuset``.

**NOTES:**

NONE

.. _pthread_attr_setaffinity_np:

pthread_attr_setaffinity_np - Set Thread Affinity Attribute
-----------------------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_attr_setaffinity_np(
        pthread_attr_t    *attr,
        size_t             cpusetsize,
        const cpu_set_t   *cpuset
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EFAULT``
   - The attribute pointer argument is invalid.
 * - ``EFAULT``
   - The cpuset pointer argument is invalid.
 * - ``EINVAL``
   - The ``cpusetsize`` does not match the value of ``affinitysetsize`` field
     in the thread attribute object.
 * - ``EINVAL``
   - The ``cpuset`` did not select a valid cpu.
 * - ``EINVAL``
   - The ``cpuset`` selected a cpu that was invalid.

**DESCRIPTION:**

The ``pthread_attr_setaffinity_np`` routine is used to set the ``affinityset``
field in the thread attribute object ``attr``.  The value of this field is
returned in ``cpuset``.

**NOTES:**

NONE

.. _pthread_create:

pthread_create - Create a Thread
--------------------------------
.. index:: pthread_create
.. index:: create a thread

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_create(
        pthread_t             *thread,
        const pthread_attr_t  *attr,
        void                 (*start_routine)( void *),
        void                  *arg
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The user specified a stack address and the size of the area was not large
     enough to meet this processor's minimum stack requirements.
 * - ``EINVAL``
   - The specified scheduler inheritance policy was invalid.
 * - ``ENOTSUP``
   - The specified contention scope was ``PTHREAD_SCOPE_PROCESS``.
 * - ``EINVAL``
   - The specified thread priority was invalid.
 * - ``EINVAL``
   - The specified scheduling policy was invalid.
 * - ``EINVAL``
   - The scheduling policy was ``SCHED_SPORADIC`` and the specified
     replenishment period is less than the initial budget.
 * - ``EINVAL``
   - The scheduling policy was ``SCHED_SPORADIC`` and the specified low
     priority is invalid.
 * - ``EAGAIN``
   - The system lacked the necessary resources to create another thread, or the
     self imposed limit on the total number of threads in a process
     ``PTHREAD_THREAD_MAX`` would be exceeded.
 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

The ``pthread_create`` routine is used to create a new thread with the
attributes specified by ``attr``. If the ``attr`` argument is ``NULL``, then
the default attribute set will be used. Modification of the contents of
``attr`` after this thread is created does not have an impact on this thread.

The thread begins execution at the address specified by ``start_routine`` with
``arg`` as its only argument. If ``start_routine`` returns, then it is
functionally equivalent to the thread executing the ``pthread_exit`` service.

Upon successful completion, the ID of the created thread is returned in the
``thread`` argument.

**NOTES:**

There is no concept of a single main thread in RTEMS as there is in a tradition
UNIX system. POSIX requires that the implicit return of the main thread results
in the same effects as if there were a call to ``exit``. This does not occur in
RTEMS.

The signal mask of the newly created thread is inherited from its creator and
the set of pending signals for this thread is empty.

.. _pthread_exit:

pthread_exit - Terminate the Current Thread
-------------------------------------------
.. index:: pthread_exit
.. index:: terminate the current thread

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    void pthread_exit(
        void *status
    );

**STATUS CODES:**

*NONE*

**DESCRIPTION:**

The ``pthread_exit`` routine is used to terminate the calling thread.  The
``status`` is made available to any successful join with the terminating
thread.

When a thread returns from its start routine, it results in an implicit call to
the ``pthread_exit`` routine with the return value of the function serving as
the argument to ``pthread_exit``.

**NOTES:**

Any cancellation cleanup handlers that hace been pushed and not yet popped
shall be popped in reverse of the order that they were pushed. After all
cancellation cleanup handlers have been executed, if the thread has any
thread-specific data, destructors for that data will be invoked.

Thread termination does not release or free any application visible resources
including byt not limited to mutexes, file descriptors, allocated memory,
etc.. Similarly, exitting a thread does not result in any process-oriented
cleanup activity.

There is no concept of a single main thread in RTEMS as there is in a tradition
UNIX system. POSIX requires that the implicit return of the main thread results
in the same effects as if there were a call to ``exit``. This does not occur in
RTEMS.

All access to any automatic variables allocated by the threads is lost when the
thread exits. Thus references (i.e. pointers) to local variables of a thread
should not be used in a global manner without care. As a specific example, a
pointer to a local variable should NOT be used as the return value.

.. _pthread_detach:

pthread_detach - Detach a Thread
--------------------------------
.. index:: pthread_detach
.. index:: detach a thread

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_detach(
        pthread_t thread
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ESRCH``
   - The thread specified is invalid.
 * - ``EINVAL``
   - The thread specified is not a joinable thread.

**DESCRIPTION:**

The ``pthread_detach`` routine is used to to indicate that storage for
``thread`` can be reclaimed when the thread terminates without another thread
joinging with it.

**NOTES:**

If any threads have previously joined with the specified thread, then they will
remain joined with that thread. Any subsequent calls to ``pthread_join`` on the
specified thread will fail.

.. COMMENT: pthread_getconcurrency

.. _pthread_getconcurrency:

pthread_getconcurrency - Obtain Thread Concurrency
--------------------------------------------------
.. index:: pthread_getconcurrency
.. index:: obtain thread concurrency

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_getconcurrency(void);

**STATUS CODES:**

This method returns the current concurrency mapping value.

**DESCRIPTION:**

The ``pthread_getconcurrency`` method returns the number of user threads
mapped onto kernel threads. For RTEMS, user and kernel threads are mapped
1:1 and per the POSIX standard this method returns 1 initially and 
the value last set by ``pthread_setconcurrency`` otherwise.

**NOTES:**

NONE

.. COMMENT: pthread_setconcurrency

.. _pthread_setconcurrency:

pthread_setconcurrency - Set Thread Concurrency
-----------------------------------------------
.. index:: pthread_setconcurrency
.. index:: obtain thread concurrency

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_setconcurrency(void);

**STATUS CODES:**

This method returns 0 on success.

**DESCRIPTION:**

The ``pthread_setconcurrency`` method requests the number of user threads
mapped onto kernel threads. Per the POSIX standard, this is considered
a request and may have no impact.

For RTEMS, user and kernel threads are always mapped 1:1 and thus this
method has no change on the mapping. However, ``pthread_getconcurrency``
will return the value set.

**NOTES:**

NONE

.. COMMENT: pthread_getattr_np

.. _pthread_getattr_np:

pthread_getattr_np - Get Thread Attributes
------------------------------------------
.. index:: pthread_getattr_np
.. index:: get thread attributes

**CALLING SEQUENCE:**

.. code-block:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_getattr_np(
        pthread_t       thread,
        pthread_attr_t *attr
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ESRCH``
   - The thread specified is invalid.
 * - ``EINVAL``
   - The attribute pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_getattr_np`` routine is used to obtain the attributes associated
with ``thread``.

**NOTES:**

Modification of the execution modes and priority through the Classic API may
result in a combination that is not representable in the POSIX API.

.. _pthread_join:

pthread_join - Wait for Thread Termination
------------------------------------------
.. index:: pthread_join
.. index:: wait for thread termination

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_join(
        pthread_t    thread,
        void       **value_ptr
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ESRCH``
   - The thread specified is invalid.
 * - ``EINVAL``
   - The thread specified is not a joinable thread.
 * - ``EDEADLK``
   - A deadlock was detected or thread is the calling thread.

**DESCRIPTION:**

The ``pthread_join`` routine suspends execution of the calling thread until
``thread`` terminates. If ``thread`` has already terminated, then this routine
returns immediately. The value returned by ``thread`` (i.e. passed to
``pthread_exit`` is returned in ``value_ptr``.

When this routine returns, then ``thread`` has been terminated.

**NOTES:**

The results of multiple simultaneous joins on the same thread is undefined.

If any threads have previously joined with the specified thread, then they will
remain joined with that thread. Any subsequent calls to ``pthread_join`` on the
specified thread will fail.

If value_ptr is NULL, then no value is returned.

.. _pthread_self:

pthread_self - Get Thread ID
----------------------------
.. index:: pthread_self
.. index:: get thread id

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    pthread_t pthread_self( void );

**STATUS CODES:**

The value returned is the ID of the calling thread.

**DESCRIPTION:**

This routine returns the ID of the calling thread.

**NOTES:**

NONE

.. _pthread_equal:

pthread_equal - Compare Thread IDs
----------------------------------
.. index:: pthread_equal
.. index:: compare thread ids

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_equal(
        pthread_t t1,
        pthread_t t2
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``zero``
   - The thread ids are not equal.
 * - ``non-zero``
   - The thread ids are equal.

**DESCRIPTION:**

The ``pthread_equal`` routine is used to compare two thread IDs and determine
if they are equal.

**NOTES:**

The behavior is undefined if the thread IDs are not valid.

.. _pthread_once:

pthread_once - Dynamic Package Initialization
---------------------------------------------
.. index:: pthread_once
.. index:: dynamic package initialization

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    pthread_once_t once_control = PTHREAD_ONCE_INIT;
    int pthread_once(
        pthread_once_t   *once_control,
        void            (*init_routine)(void)
    );

**STATUS CODES:**

NONE

**DESCRIPTION:**

The ``pthread_once`` routine is used to provide controlled initialization of
variables. The first call to ``pthread_once`` by any thread with the same
``once_control`` will result in the ``init_routine`` being invoked with no
arguments. Subsequent calls to ``pthread_once`` with the same ``once_control``
will have no effect.

The ``init_routine`` is guaranteed to have run to completion when this routine
returns to the caller.

**NOTES:**

The behavior of ``pthread_once`` is undefined if ``once_control`` is automatic
storage (i.e. on a task stack) or is not initialized using
``PTHREAD_ONCE_INIT``.

.. _pthread_setschedparam:

pthread_setschedparam - Set Thread Scheduling Parameters
--------------------------------------------------------
.. index:: pthread_setschedparam
.. index:: set thread scheduling parameters

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_setschedparam(
        pthread_t           thread,
        int                 policy,
        struct sched_param *param
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The scheduling parameters indicated by the parameter param is invalid.
 * - ``EINVAL``
   - The value specified by policy is invalid.
 * - ``EINVAL``
   - The scheduling policy was ``SCHED_SPORADIC`` and the specified
     replenishment period is less than the initial budget.
 * - ``EINVAL``
   - The scheduling policy was ``SCHED_SPORADIC`` and the specified low
     priority is invalid.
 * - ``ESRCH``
   - The thread indicated was invalid.

**DESCRIPTION:**

The ``pthread_setschedparam`` routine is used to set the scheduler parameters
currently associated with the thread specified by ``thread`` to the policy
specified by ``policy``. The contents of ``param`` are interpreted based upon
the ``policy`` argument.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. _pthread_getschedparam:

pthread_getschedparam - Get Thread Scheduling Parameters
--------------------------------------------------------
.. index:: pthread_getschedparam
.. index:: get thread scheduling parameters

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pthread.h>
    int pthread_getschedparam(
        pthread_t           thread,
        int                *policy,
        struct sched_param *param
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The policy pointer argument is invalid.
 * - ``EINVAL``
   - The scheduling parameters pointer argument is invalid.
 * - ``ESRCH``
   - The thread indicated by the parameter thread is invalid.

**DESCRIPTION:**

The ``pthread_getschedparam`` routine is used to obtain the scheduler policy
and parameters associated with ``thread``.  The current policy and associated
parameters values returned in``policy`` and ``param``, respectively.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol
``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the family of routines
to which this routine belongs is supported.

.. COMMENT: pthread_getaffinity_np

.. _pthread_getaffinity_np:

pthread_getaffinity_np - Get Thread Affinity
--------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_getaffinity_np(
        const pthread_t       id,
        size_t                cpusetsize,
        cpu_set_t            *cpuset
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EFAULT``
   - The cpuset pointer argument is invalid.
 * - ``EINVAL``
   - The ``cpusetsize`` does not match the value of ``affinitysetsize`` field
     in the thread attribute object.

**DESCRIPTION:**

The ``pthread_getaffinity_np`` routine is used to obtain the ``affinity.set``
field from the thread control object associated with the ``id``.  The value of
this field is returned in ``cpuset``.

**NOTES:**

NONE

.. COMMENT: pthread_setaffinity_np

.. _pthread_setaffinity_np:

pthread_setaffinity_np - Set Thread Affinity
--------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_setaffinity_np(
        pthread_t          id,
        size_t             cpusetsize,
        const cpu_set_t   *cpuset
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EFAULT``
   - The cpuset pointer argument is invalid.
 * - ``EINVAL``
   - The ``cpusetsize`` does not match the value of ``affinitysetsize`` field
     in the thread attribute object.
 * - ``EINVAL``
   - The ``cpuset`` did not select a valid cpu.
 * - ``EINVAL``
   - The ``cpuset`` selected a cpu that was invalid.

**DESCRIPTION:**

The ``pthread_setaffinity_np`` routine is used to set the ``affinityset`` field
of the thread object ``id``.  The value of this field is returned in ``cpuset``

**NOTES:**

NONE
