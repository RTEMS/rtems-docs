.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2014, 2017.
.. COMMENT: embedded brains GmbH & Co. KG

Self-Contained Objects
**********************

Introduction
============

One of the original design goals of RTEMS was the support for heterogeneous
computing based on message passing.  This was realized by synchronization
objects with an architecture-independent identifier provided by the system
during object creation (a 32-bit unsigned integer used as a bitfield) and a
user-defined four character name.  This approach in the so called Classic API
has some weaknesses:

* Dynamic memory (the workspace) is used to allocate object pools.  This
  requires a complex configuration with heavy use of the C pre-processor.
  The unlimited objects support optionally expands and shrinks the object pool.
  Dynamic memory is strongly discouraged by some coding standards, e.g.  MISRA
  C:2012 :cite:`MISRA:2012:C`.

* Objects are created via function calls which return an object identifier.
  The object operations use this identifier and map it internally to an object
  representation.

* The object identifier is only known at run-time.  This hinders compiler
  optimizations and static analysis.

* The objects reside in a table, e.g. they are subject to false sharing of
  cache lines :cite:`Drepper:2007:Memory`.

* The object operations use a rich set of options and attributes.  For each
  object operation these parameters must be evaluated and validated at run-time
  to figure out what to do exactly for this operation.

For applications that use fine grained locking the mapping of the identifier to
the object representation and the parameter evaluation are a significant
overhead that may degrade the performance dramatically.  An example is the `new
network stack (libbsd) <https://git.rtems.org/rtems-libbsd>`_ which uses
hundreds of locks in a basic setup.  Another example is the OpenMP support
(libgomp).

To overcome these issues new self-contained synchronization objects are
available since RTEMS 4.11.  Self-contained synchronization objects encapsulate
all their state in exactly one data structure.  The user must provide the
storage space for this structure and nothing more.  The user is responsible for
the object life-cycle.  Initialization and destruction of self-contained
synchronization objects cannot fail provided all function parameters are valid.
In particular, a not enough memory error cannot happen.  It is possible to
statically initialize self-contained synchronization objects.  This allows an
efficient use of static analysis tools.

Several header files define self-contained synchronization objects.  The Newlib
:file:`<sys/lock.h>` header file provides

* mutexes,

* recursive mutexes,

* condition variables,

* counting semaphores,

* binary semaphores, and

* Futex synchronization :cite:`Franke:2002:Futex`.

They are used internally in Newlib (e.g. for FILE objects), for the C++11
threads and the OpenMP support (libgomp).  The Newlib provided self-contained
synchronization objects focus on performance.  There are no error checks to
catch software errors, e.g. invalid parameters.  The application configuration
is significantly simplified, since it is no longer necessary to account for
lock objects used by Newlib and GCC.  The Newlib defined self-contained
synchronization objects can be a statically initialized and reside in the
``.bss`` section.  Destruction is a no-operation.

The header file :file:`<pthread.h>` provides

* POSIX barriers (:c:type:`pthread_barrier_t`),

* POSIX condition variables (:c:type:`pthread_cond_t`),

* POSIX mutexes (:c:type:`pthread_mutex_t`),

* POSIX reader/writer locks (:c:type:`pthread_rwlock_t`), and

* POSIX spinlocks (:c:type:`pthread_spinlock_t`)

as self-contained synchronization objects.  The POSIX synchronization objects are
used for example by the Ada run-time support.  The header file
:file:`<semaphore.h>` provides self-contained

* POSIX unnamed semaphores (:c:type:`sem_t` initialized via :c:func:`sem_init`).

RTEMS Thread API
================

To give RTEMS users access to self-contained synchronization objects an API is
necessary.  One option would be to simply use the POSIX threads API (pthreads),
C11 threads or C++11 threads.  However, these standard APIs lack for example
binary semaphores which are important for task/interrupt synchronization.  The
timed operations use in general time values specified by seconds and
nanoseconds.  Setting up the time values in seconds (time_t has 64 bits) and
nanoseconds is burdened with a high overhead compared to time values in clock
ticks for relative timeouts.  The POSIX API mutexes can be configured for
various protocols and options, this adds a run-time overhead.  There are a
variety of error conditions.  This is a problem in combination with some coding
standards, e.g.  MISRA C:2012.  APIs used by Linux (e.g. `<linux/mutex.h>
<http://lxr.free-electrons.com/source/include/linux/mutex.h>`_) or the FreeBSD
kernel (e.g. `MUTEX(9)
<https://www.freebsd.org/cgi/man.cgi?query=mutex&sektion=9>`_) are better
suited as a template for high-performance synchronization objects.  The goal of
the `RTEMS Thread API` is to offer the highest performance with the lowest
space-overhead on RTEMS.  It should be suitable for device drivers.

Mutual Exclusion
================

The :c:type:`rtems_mutex` and :c:type:`rtems_recursive_mutex` objects provide
mutual-exclusion synchronization using the :ref:`PriorityInheritance` in
uniprocessor configurations or the :ref:`OMIP` in SMP configurations.
Recursive locking should be used with care :cite:`Williams:2012:CA`.  The
storage space for these object must be provided by the user.  There are no
defined comparison or assignment operators for these type.  Only the object
itself may be used for performing synchronization.  The result of referring to
copies of the object in calls to

* :c:func:`rtems_mutex_lock`,

* :c:func:`rtems_recursive_mutex_lock`,

* :c:func:`rtems_mutex_try_lock`,

* :c:func:`rtems_recursive_mutex_try_lock`,

* :c:func:`rtems_mutex_unlock`,

* :c:func:`rtems_recursive_mutex_unlock`,

* :c:func:`rtems_mutex_set_name`,

* :c:func:`rtems_recursive_mutex_set_name`,

* :c:func:`rtems_mutex_get_name`,

* :c:func:`rtems_recursive_mutex_get_name`,

* :c:func:`rtems_mutex_destroy`, and

* :c:func:`rtems_recursive_mutex_destroy`

is undefined.  Objects of the type :c:type:`rtems_mutex` must be initialized
via

* :c:func:`RTEMS_MUTEX_INITIALIZER`, or

* :c:func:`rtems_mutex_init`.

They must be destroyed via

* :c:func:`rtems_mutex_destroy`.

Objects of the type :c:type:`rtems_recursive_mutex` must be initialized via

* :c:func:`RTEMS_RECURSIVE_MUTEX_INITIALIZER`, or

* :c:func:`rtems_recursive_mutex_init`.

They must be destroyed via

* :c:func:`rtems_recursive_mutex_destroy`.

.. raw:: latex

    \clearpage

Static mutex initialization
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_mutex mutex = RTEMS_MUTEX_INITIALIZER(
          name
        );

        rtems_recursive_mutex mutex = RTEMS_RECURSIVE_MUTEX_INITIALIZER(
          name
        );

DESCRIPTION:
    An initializer for static initialization.  It is equivalent to a call to
    :c:func:`rtems_mutex_init` or :c:func:`rtems_recursive_mutex_init`
    respectively.

NOTES:
    Global mutexes with a ``name`` of ``NULL`` may reside in the ``.bss``
    section.

.. raw:: latex

    \clearpage

Run-time mutex initialization
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_mutex_init(
          rtems_mutex *mutex,
          const char  *name
        );

        void rtems_recursive_mutex_init(
          rtems_recursive_mutex *mutex,
          const char            *name
        );

DESCRIPTION:
    Initializes the ``mutex`` with the specified ``name``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the mutex.  A
    ``name`` of ``NULL`` is valid.  The mutex is unlocked after initialization.

.. raw:: latex

    \clearpage

Lock the mutex
--------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_mutex_lock(
          rtems_mutex *mutex
        );

        void rtems_recursive_mutex_lock(
          rtems_recursive_mutex *mutex
        );

DESCRIPTION:
    Locks the ``mutex``.

NOTES:
    This function must be called from thread context with interrupts enabled.
    In case the mutex is currently locked by another thread, then the thread is
    blocked until it becomes the mutex owner.  Threads wait in priority order.

    A recursive lock happens in case the mutex owner tries to lock the mutex
    again.  The result of recursively locking a mutex depends on the mutex
    variant.  For a normal (non-recursive) mutex (:c:type:`rtems_mutex`) the
    result is unpredictable.  It could block the owner indefinetly or lead to a
    fatal deadlock error.  A recursive mutex (:c:type:`rtems_recursive_mutex`)
    can be locked recursively by the mutex owner.

    Each mutex lock operation must have a corresponding unlock operation.

.. raw:: latex

    \clearpage

Try to lock the mutex
---------------------

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_mutex_try_lock(
          rtems_mutex *mutex
        );

        int rtems_recursive_mutex_try_lock(
          rtems_recursive_mutex *mutex
        );

DESCRIPTION:
    Tries to lock the ``mutex``. In case the mutex is not locked, it will be
    locked and the function returns with a return value of ``0``. If the mutex
    is already locked, the function will return with a value of ``EBUSY``.

NOTES:
    This function must be called from thread context with interrupts enabled.

    For recursively locking a mutex, please also see the notes for
    :c:func:`rtems_mutex_lock` and :c:func:`rtems_recursive_mutex_lock`.

    Each mutex lock operation must have a corresponding unlock operation.

.. raw:: latex

    \clearpage

Unlock the mutex
----------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_mutex_unlock(
          rtems_mutex *mutex
        );

        void rtems_recursive_mutex_unlock(
          rtems_recursive_mutex *mutex
        );

DESCRIPTION:
    Unlocks the ``mutex``.

NOTES:
    This function must be called from thread context with interrupts enabled.
    In case the currently executing thread is not the owner of the ``mutex``,
    then the result is unpredictable.

    Exactly the outer-most unlock will make a recursive mutex available to
    other threads.

.. raw:: latex

    \clearpage

.. raw:: latex

    \clearpage

Set mutex name
--------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_mutex_set_name(
          rtems_mutex *mutex,
          const char  *name
        );

        void rtems_recursive_mutex_set_name(
          rtems_recursive_mutex *mutex,
          const char            *name
        );

DESCRIPTION:
    Sets the ``mutex`` name to ``name``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the mutex.  A
    ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Get mutex name
--------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_mutex_get_name(
          const rtems_mutex *mutex
        );

        const char *rtems_recursive_mutex_get_name(
          const rtems_recursive_mutex *mutex
        );

DESCRIPTION:
    Returns the ``mutex`` name.

NOTES:
    The name may be ``NULL``.

Mutex destruction
-----------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_mutex_destroy(
          rtems_mutex *mutex
        );

        void rtems_recursive_mutex_destroy(
          rtems_recursive_mutex *mutex
        );

DESCRIPTION:
    Destroys the ``mutex``.

NOTES:
    In case the mutex is locked or still in use, then the result is
    unpredictable.

Condition Variables
===================

The :c:type:`rtems_condition_variable` object provides a condition variable
synchronization object.  The storage space for this object must be provided by
the user.  There are no defined comparison or assignment operators for this
type.  Only the object itself may be used for performing synchronization.  The
result of referring to copies of the object in calls to

* :c:func:`rtems_condition_variable_wait`,

* :c:func:`rtems_condition_variable_signal`,

* :c:func:`rtems_condition_variable_broadcast`,

* :c:func:`rtems_condition_variable_set_name`,

* :c:func:`rtems_condition_variable_get_name`, and

* :c:func:`rtems_condition_variable_destroy`

is undefined.  Objects of this type must be initialized via

* :c:func:`RTEMS_CONDITION_VARIABLE_INITIALIZER`, or

* :c:func:`rtems_condition_variable_init`.

They must be destroyed via

* :c:func:`rtems_condition_variable_destroy`.

.. raw:: latex

    \clearpage

Static condition variable initialization
----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_condition_variable condition_variable = RTEMS_CONDITION_VARIABLE_INITIALIZER(
          name
        );

DESCRIPTION:
    An initializer for static initialization.  It is equivalent to a call to
    :c:func:`rtems_condition_variable_init`.

NOTES:
    Global condition variables with a ``name`` of ``NULL`` may reside in the
    ``.bss`` section.

.. raw:: latex

    \clearpage

Run-time condition variable initialization
------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_condition_variable_init(
          rtems_condition_variable *condition_variable,
          const char               *name
        );

DESCRIPTION:
    Initializes the ``condition_variable`` with the specified ``name``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the condition
    variable.  A ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Wait for condition signal
-------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_condition_variable_wait(
          rtems_condition_variable *condition_variable,
          rtems_mutex              *mutex
        );

DESCRIPTION:
    Atomically waits for a condition signal and unlocks the mutex.  Once the
    condition is signalled to the thread it wakes up and locks the mutex again.

NOTES:
    This function must be called from thread context with interrupts enabled.
    Threads wait in priority order.

.. raw:: latex

    \clearpage

Signals a condition change
--------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_condition_variable_signal(
          rtems_condition_variable *condition_variable
        );

DESCRIPTION:
    Signals a condition change to the highest priority waiting thread.  If no
    threads wait currently on this condition variable, then nothing happens.

.. raw:: latex

    \clearpage

Broadcasts a condition change
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_condition_variable_broadcast(
          rtems_condition_variable *condition_variable
        );

DESCRIPTION:
    Signals a condition change to all waiting thread.  If no threads wait
    currently on this condition variable, then nothing happens.

.. raw:: latex

    \clearpage

.. raw:: latex

    \clearpage

Set condition variable name
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_condition_variable_set_name(
          rtems_condition_variable *condition_variable,
          const char               *name
        );

DESCRIPTION:
    Sets the ``condition_variable`` name to ``name``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the condition
    variable.  A ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Get condition variable name
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_condition_variable_get_name(
          const rtems_condition_variable *condition_variable
        );

DESCRIPTION:
    Returns the ``condition_variable`` name.

NOTES:
    The name may be ``NULL``.

Condition variable destruction
------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_condition_variable_destroy(
          rtems_condition_variable *condition_variable
        );

DESCRIPTION:
    Destroys the ``condition_variable``.

NOTES:
    In case the condition variable still in use, then the result is
    unpredictable.

Counting Semaphores
===================

The :c:type:`rtems_counting_semaphore` object provides a counting semaphore
synchronization object.  The storage space for this object must be provided by
the user.  There are no defined comparison or assignment operators for this
type.  Only the object itself may be used for performing synchronization.  The
result of referring to copies of the object in calls to

* :c:func:`rtems_counting_semaphore_wait`,

* :c:func:`rtems_counting_semaphore_post`,

* :c:func:`rtems_counting_semaphore_set_name`,

* :c:func:`rtems_counting_semaphore_get_name`, and

* :c:func:`rtems_counting_semaphore_destroy`

is undefined.  Objects of this type must be initialized via

* :c:func:`RTEMS_COUNTING_SEMAPHORE_INITIALIZER`, or

* :c:func:`rtems_counting_semaphore_init`.

They must be destroyed via

* :c:func:`rtems_counting_semaphore_destroy`.

.. raw:: latex

    \clearpage

Static counting semaphore initialization
----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_counting_semaphore counting_semaphore = RTEMS_COUNTING_SEMAPHORE_INITIALIZER(
          name,
          value
        );

DESCRIPTION:
    An initializer for static initialization.  It is equivalent to a call to
    :c:func:`rtems_counting_semaphore_init`.

NOTES:
    Global counting semaphores with a ``name`` of ``NULL`` may reside in the
    ``.bss`` section.

.. raw:: latex

    \clearpage

Run-time counting semaphore initialization
------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_counting_semaphore_init(
          rtems_counting_semaphore *counting_semaphore,
          const char               *name,
          unsigned int              value
        );

DESCRIPTION:
    Initializes the ``counting_semaphore`` with the specified ``name`` and
    ``value``.  The initial value is set to ``value``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the counting
    semaphore.  A ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Wait for a counting semaphore
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_counting_semaphore_wait(
          rtems_counting_semaphore *counting_semaphore
        );

DESCRIPTION:
    Waits for the ``counting_semaphore``.  In case the current semaphore value
    is positive, then the value is decremented and the function returns
    immediately, otherwise the thread is blocked waiting for a semaphore post.

NOTES:
    This function must be called from thread context with interrupts enabled.
    Threads wait in priority order.

.. raw:: latex

    \clearpage

Post a counting semaphore
-------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_counting_semaphore_post(
          rtems_counting_semaphore *counting_semaphore
        );

DESCRIPTION:
    Posts the ``counting_semaphore``.  In case at least one thread is waiting
    on the counting semaphore, then the highest priority thread is woken up,
    otherwise the current value is incremented.

NOTES:
    This function may be called from interrupt context.  In case it is called
    from thread context, then interrupts must be enabled.

.. raw:: latex

    \clearpage

.. raw:: latex

    \clearpage

Set counting semaphore name
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_counting_semaphore_set_name(
          rtems_counting_semaphore *counting_semaphore,
          const char               *name
        );

DESCRIPTION:
    Sets the ``counting_semaphore`` name to ``name``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the counting
    semaphore.  A ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Get counting semaphore name
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_counting_semaphore_get_name(
          const rtems_counting_semaphore *counting_semaphore
        );

DESCRIPTION:
    Returns the ``counting_semaphore`` name.

NOTES:
    The name may be ``NULL``.

Counting semaphore destruction
------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_counting_semaphore_destroy(
          rtems_counting_semaphore *counting_semaphore
        );

DESCRIPTION:
    Destroys the ``counting_semaphore``.

NOTES:
    In case the counting semaphore still in use, then the result is
    unpredictable.

Binary Semaphores
=================

The :c:type:`rtems_binary_semaphore` object provides a binary semaphore
synchronization object.  The storage space for this object must be provided by
the user.  There are no defined comparison or assignment operators for this
type.  Only the object itself may be used for performing synchronization.  The
result of referring to copies of the object in calls to

* :c:func:`rtems_binary_semaphore_wait`,

* :c:func:`rtems_binary_semaphore_wait_timed_ticks`,

* :c:func:`rtems_binary_semaphore_try_wait`,

* :c:func:`rtems_binary_semaphore_post`,

* :c:func:`rtems_binary_semaphore_set_name`,

* :c:func:`rtems_binary_semaphore_get_name`, and

* :c:func:`rtems_binary_semaphore_destroy`

is undefined.  Objects of this type must be initialized via

* :c:func:`RTEMS_BINARY_SEMAPHORE_INITIALIZER`, or

* :c:func:`rtems_binary_semaphore_init`.

They must be destroyed via

* :c:func:`rtems_binary_semaphore_destroy`.

.. raw:: latex

    \clearpage

Static binary semaphore initialization
--------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_binary_semaphore binary_semaphore = RTEMS_BINARY_SEMAPHORE_INITIALIZER(
          name
        );

DESCRIPTION:
    An initializer for static initialization.  It is equivalent to a call to
    :c:func:`rtems_binary_semaphore_init`.

NOTES:
    Global binary semaphores with a ``name`` of ``NULL`` may reside in the
    ``.bss`` section.

.. raw:: latex

    \clearpage

Run-time binary semaphore initialization
----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_binary_semaphore_init(
          rtems_binary_semaphore *binary_semaphore,
          const char             *name
        );

DESCRIPTION:
    Initializes the ``binary_semaphore`` with the specified ``name``.  The
    initial value is set to zero.

NOTES:
    The ``name`` must be persistent throughout the life-time of the binary
    semaphore.  A ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Wait for a binary semaphore
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_binary_semaphore_wait(
          rtems_binary_semaphore *binary_semaphore
        );

DESCRIPTION:
    Waits for the ``binary_semaphore``.  In case the current semaphore value is
    one, then the value is set to zero and the function returns immediately,
    otherwise the thread is blocked waiting for a semaphore post.

NOTES:
    This function must be called from thread context with interrupts enabled.
    Threads wait in priority order.

.. raw:: latex

    \clearpage

Wait for a binary semaphore with timeout in ticks
-------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_binary_semaphore_wait_timed_ticks(
          rtems_binary_semaphore *binary_semaphore,
          uint32_t                ticks
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``0``
        - The semaphore wait was successful.
      * - ``ETIMEDOUT``
        - The semaphore wait timed out.

DESCRIPTION:
    Waits for the ``binary_semaphore`` with a timeout in ``ticks``.  In case
    the current semaphore value is one, then the value is set to zero and the
    function returns immediately with a return value of ``0``, otherwise the
    thread is blocked waiting for a semaphore post.  The time waiting for a
    semaphore post is limited by ``ticks``.  A ``ticks`` value of zero
    specifies an infinite timeout.

NOTES:
    This function must be called from thread context with interrupts enabled.
    Threads wait in priority order.

.. raw:: latex

    \clearpage

Tries to wait for a binary semaphore
------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_binary_semaphore_try_wait(
          rtems_binary_semaphore *binary_semaphore
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``0``
        - The semaphore wait was successful.
      * - ``EAGAIN``
        - The semaphore wait failed.

DESCRIPTION:
    Tries to wait for the ``binary_semaphore``.  In case the current semaphore
    value is one, then the value is set to zero and the function returns
    immediately with a return value of ``0``, otherwise it returns immediately
    with a return value of ``EAGAIN``.

NOTES:
    This function may be called from interrupt context.  In case it is called
    from thread context, then interrupts must be enabled.

.. raw:: latex

    \clearpage

Post a binary semaphore
-----------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_binary_semaphore_post(
          rtems_binary_semaphore *binary_semaphore
        );

DESCRIPTION:
    Posts the ``binary_semaphore``.  In case at least one thread is waiting
    on the binary semaphore, then the highest priority thread is woken up,
    otherwise the current value is set to one.

NOTES:
    This function may be called from interrupt context.  In case it is called
    from thread context, then interrupts must be enabled.

.. raw:: latex

    \clearpage

.. raw:: latex

    \clearpage

Set binary semaphore name
-------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_binary_semaphore_set_name(
          rtems_binary_semaphore *binary_semaphore,
          const char             *name
        );

DESCRIPTION:
    Sets the ``binary_semaphore`` name to ``name``.

NOTES:
    The ``name`` must be persistent throughout the life-time of the binary
    semaphore.  A ``name`` of ``NULL`` is valid.

.. raw:: latex

    \clearpage

Get binary semaphore name
-------------------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_binary_semaphore_get_name(
          const rtems_binary_semaphore *binary_semaphore
        );

DESCRIPTION:
    Returns the ``binary_semaphore`` name.

NOTES:
    The name may be ``NULL``.

Binary semaphore destruction
----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_binary_semaphore_destroy(
          rtems_binary_semaphore *binary_semaphore
        );

DESCRIPTION:
    Destroys the ``binary_semaphore``.

NOTES:
    In case the binary semaphore still in use, then the result is
    unpredictable.

Threads
=======

.. warning::

   The self-contained threads support is work in progress.  In contrast to the
   synchronization objects the self-contained thread support is not just an API
   glue layer to already existing implementations.

The :c:type:`rtems_thread` object provides a thread of execution.

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_THREAD_INITIALIZER(
          name,
          thread_size,
          priority,
          flags,
          entry,
          arg
        );

        void rtems_thread_start(
          rtems_thread *thread,
          const char   *name,
          size_t        thread_size,
          uint32_t      priority,
          uint32_t      flags,
          void       ( *entry )( void * ),
          void         *arg
        );

        void rtems_thread_restart(
          rtems_thread *thread,
          void         *arg
        ) RTEMS_NO_RETURN;

        void rtems_thread_event_send(
          rtems_thread *thread,
          uint32_t      events
        );

        uint32_t rtems_thread_event_poll(
          rtems_thread *thread,
          uint32_t      events_of_interest
        );

        uint32_t rtems_thread_event_wait_all(
          rtems_thread *thread,
          uint32_t      events_of_interest
        );

        uint32_t rtems_thread_event_wait_any(
          rtems_thread *thread,
          uint32_t      events_of_interest
        );

        void rtems_thread_destroy(
          rtems_thread *thread
        );

        void rtems_thread_destroy_self(
          void
        ) RTEMS_NO_RETURN;
