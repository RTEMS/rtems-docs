.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Signal Manager
##############

Introduction
============

The signal manager provides the functionality associated with the generation,
delivery, and management of process-oriented signals.

The directives provided by the signal manager are:

- sigaddset_ - Add a Signal to a Signal Set

- sigdelset_ - Delete a Signal from a Signal Set

- sigfillset_ - Fill a Signal Set

- sigismember_ - Is Signal a Member of a Signal Set

- sigemptyset_ - Empty a Signal Set

- sigaction_ - Examine and Change Signal Action

- pthread_kill_ - Send a Signal to a Thread

- sigprocmask_ - Examine and Change Process Blocked Signals

- pthread_sigmask_ - Examine and Change Thread Blocked Signals

- kill_ - Send a Signal to a Process

- sigpending_ - Examine Pending Signals

- sigsuspend_ - Wait for a Signal

- pause_ - Suspend Process Execution

- sigwait_ - Synchronously Accept a Signal

- sigwaitinfo_ - Synchronously Accept a Signal

- sigtimedwait_ - Synchronously Accept a Signal with Timeout

- sigqueue_ - Queue a Signal to a Process

- alarm_ - Schedule Alarm

- ualarm_ - Schedule Alarm in Microseconds

Background
==========

Signals
-------

POSIX signals are an asynchronous event mechanism.  Each process and thread has
a set of signals associated with it.  Individual signals may be enabled
(e.g. unmasked) or blocked (e.g. ignored) on both a per-thread and process
level.  Signals which are enabled have a signal handler associated with them.
When the signal is generated and conditions are met, then the signal handler is
invoked in the proper process or thread context asynchronous relative to the
logical thread of execution.

If a signal has been blocked when it is generated, then it is queued and kept
pending until the thread or process unblocks the signal or explicitly checks
for it.  Traditional, non-real-time POSIX signals do not queue.  Thus if a
process or thread has blocked a particular signal, then multiple occurrences of
that signal are recorded as a single occurrence of that signal.

.. COMMENT: TODO: SIGRTMIN and SIGRTMAX ?

One can check for the set of outstanding signals that have been blocked.
Services are provided to check for outstanding process or thread directed
signals.

Signal Delivery
---------------

Signals which are directed at a thread are delivered to the specified thread.

Signals which are directed at a process are delivered to a thread which is
selected based on the following algorithm:

#. If the action for this signal is currently ``SIG_IGN``, then the signal is
   simply ignored.

#. If the currently executing thread has the signal unblocked, then the signal
   is delivered to it.

#. If any threads are currently blocked waiting for this signal
   (``sigwait()``), then the signal is delivered to the highest priority thread
   waiting for this signal.

#. If any other threads are willing to accept delivery of the signal, then the
   signal is delivered to the highest priority thread of this set. In the
   event, multiple threads of the same priority are willing to accept this
   signal, then priority is given first to ready threads, then to threads
   blocked on calls which may be interrupted, and finally to threads blocked on
   non-interruptible calls.

#. In the event the signal still can not be delivered, then it is left
   pending. The first thread to unblock the signal (``sigprocmask()`` or
   ``pthread_sigprocmask()``) or to wait for this signal (``sigwait()``) will
   be the recipient of the signal.

Operations
==========

Signal Set Management
---------------------

Each process and each thread within that process has a set of individual
signals and handlers associated with it.  Services are provided to construct
signal sets for the purposes of building signal sets - type ``sigset_t`` - that
are used to provide arguments to the services that mask, unmask, and check on
pending signals.

Blocking Until Signal Generation
--------------------------------

A thread may block until receipt of a signal.  The "sigwait" and "pause"
families of functions block until the requested signal is received or if using
``sigtimedwait()`` until the specified timeout period has elapsed.

Sending a Signal
----------------

This is accomplished via one of a number of services that sends a signal to
either a process or thread.  Signals may be directed at a process by the
service ``kill()`` or at a thread by the service ``pthread_kill()``

Directives
==========

This section details the signal manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. _sigaddset:

sigaddset - Add a Signal to a Signal Set
----------------------------------------
.. index:: sigaddset
.. index:: add a signal to a signal set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigaddset(
        sigset_t *set,
        int       signo
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This function adds the signal ``signo`` to the specified signal ``set``.

**NOTES:**

The set must be initialized using either ``sigemptyset`` or ``sigfillset``
before using this function.

.. _sigdelset:

sigdelset - Delete a Signal from a Signal Set
---------------------------------------------
.. index:: sigdelset
.. index:: delete a signal from a signal set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigdelset(
        sigset_t *set,
        int       signo
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This function deletes the signal specified by ``signo`` from the specified
signal ``set``.

**NOTES:**

The set must be initialized using either ``sigemptyset`` or ``sigfillset``
before using this function.

.. _sigfillset:

sigfillset - Fill a Signal Set
------------------------------
.. index:: sigfillset
.. index:: fill a signal set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigfillset(
        sigset_t *set
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This function fills the specified signal ``set`` such that all signals are set.

.. _sigismember:

sigismember - Is Signal a Member of a Signal Set
------------------------------------------------
.. index:: sigismember
.. index:: is signal a member of a signal set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigismember(
        const sigset_t *set,
        int             signo
    );

**STATUS CODES:**

The function returns either 1 or 0 if completed successfully, otherwise it
returns -1 and sets ``errno`` to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This function returns returns 1 if ``signo`` is a member of ``set`` and 0
otherwise.

**NOTES:**

The set must be initialized using either ``sigemptyset`` or ``sigfillset``
before using this function.

.. _sigemptyset:

sigemptyset - Empty a Signal Set
--------------------------------
.. index:: sigemptyset
.. index:: empty a signal set

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigemptyset(
        sigset_t *set
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This function initializes an empty signal set pointed to by ``set``.

.. _sigaction:

sigaction - Examine and Change Signal Action
--------------------------------------------
.. index:: sigaction
.. index:: examine and change signal action

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigaction(
        int                     sig,
        const struct sigaction *act,
        struct sigaction       *oact
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.
 * - ``ENOTSUP``
   - Realtime Signals Extension option not supported.

**DESCRIPTION:**

If the argument act is not a null pointer, it points to a structure specifying
the action to be associated with the specified signal. If the argument oact is
not a null pointer, the action previously associated with the signal is stored
in the location pointed to by the argument oact. If the argument act is a null
pointer, signal handling is unchanged; thus, the call can be used to enquire
about the current handling of a given signal.

The structure ``sigaction`` has the following members:

.. list-table::
 :class: rtems-table

 * - ``void(*)(int) sa_handler``
   - Pointer to a signal-catching function or one of the macros SIG_IGN or
     SIG_DFL.
 * - ``sigset_t sa_mask``
   - Additional set of signals to be blocked during execution of
     signal-catching function.
 * - ``int sa_flags``
   - Special flags to affect behavior of signal.
 * - ``void(*)(int, siginfo_t*, void*) sa_sigaction``
   - Alternative pointer to a signal-catching function.

``sa_handler`` and ``sa_sigaction`` should never be used at the same time as
their storage may overlap.

If the ``SA_SIGINFO`` flag (see below) is set in ``sa_flags``, the
``sa_sigaction`` field specifies a signal-catching function,
otherwise``sa_handler`` specifies the action to be associated with the signal,
which may be a signal-catching function or one of the macros ``SIG_IGN`` or
``SIG_DFN``.

The following flags can be set in the ``sa_flags`` field:

.. list-table::
 :class: rtems-table

 * - ``SA_SIGINFO``
   - If not set, the signal-catching function should be declared as ``void
     func(int signo)`` and the address of the function should be set
     in``sa_handler``.  If set, the signal-catching function should be declared
     as ``void func(int signo, siginfo_t* info, void* context)`` and the
     address of the function should be set in ``sa_sigaction``.

The prototype of the ``siginfo_t`` structure is the following:

.. code-block:: c

    typedef struct
    {
        int si_signo;        /* Signal number */
        int si_code;         /* Cause of the signal */
        pid_t si_pid;        /* Sending process ID */
        uid_t si_uid;        /* Real user ID of sending process */
        void* si_addr;       /* Address of faulting instruction */
        int si_status;       /* Exit value or signal */
        union sigval
        {
            int sival_int;   /* Integer signal value */
            void* sival_ptr; /* Pointer signal value */
        } si_value;          /* Signal value */
    }

**NOTES:**

The signal number cannot be SIGKILL.

.. _pthread_kill:

pthread_kill - Send a Signal to a Thread
----------------------------------------
.. index:: pthread_kill
.. index:: send a signal to a thread

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int pthread_kill(
        pthread_t thread,
        int       sig
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno`` to
indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``ESRCH``
   - The thread indicated by the parameter thread is invalid.
 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This functions sends the specified signal ``sig`` to a thread referenced to by
``thread``.

If the signal code is ``0``, arguments are validated and no signal is sent.

.. _sigprocmask:

sigprocmask - Examine and Change Process Blocked Signals
--------------------------------------------------------
.. index:: sigprocmask
.. index:: examine and change process blocked signals

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigprocmask(
        int             how,
        const sigset_t *set,
        sigset_t       *oset
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.

**DESCRIPTION:**

This function is used to alter the set of currently blocked signals on a
process wide basis. A blocked signal will not be received by the process. The
behavior of this function is dependent on the value of ``how`` which may be one
of the following:

.. list-table::
 :class: rtems-table

 * - ``SIG_BLOCK``
   - The set of blocked signals is set to the union of ``set`` and those
     signals currently blocked.
 * - ``SIG_UNBLOCK``
   - The signals specific in ``set`` are removed from the currently blocked
     set.
 * - ``SIG_SETMASK``
   - The set of currently blocked signals is set to ``set``.

If ``oset`` is not ``NULL``, then the set of blocked signals prior to this call
is returned in ``oset``. If ``set`` is ``NULL``, no change is done, allowing to
examine the set of currently blocked signals.

**NOTES:**

It is not an error to unblock a signal which is not blocked.

In the current implementation of RTEMS POSIX API ``sigprocmask()`` is
technically mapped to ``pthread_sigmask()``.

.. _pthread_sigmask:

pthread_sigmask - Examine and Change Thread Blocked Signals
-----------------------------------------------------------
.. index:: pthread_sigmask
.. index:: examine and change thread blocked signals

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int pthread_sigmask(
    int             how,
    const sigset_t *set,
    sigset_t       *oset
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function is used to alter the set of currently blocked signals for the
calling thread. A blocked signal will not be received by the process. The
behavior of this function is dependent on the value of ``how`` which may be one
of the following:

.. list-table::
 :class: rtems-table

 * - ``SIG_BLOCK``
   - The set of blocked signals is set to the union of ``set`` and those
     signals currently blocked.
 * - ``SIG_UNBLOCK``
   - The signals specific in ``set`` are removed from the currently blocked
     set.
 * - ``SIG_SETMASK``
   - The set of currently blocked signals is set to ``set``.

If ``oset`` is not ``NULL``, then the set of blocked signals prior to this call
is returned in ``oset``. If ``set`` is ``NULL``, no change is done, allowing to
examine the set of currently blocked signals.

**NOTES:**

It is not an error to unblock a signal which is not blocked.

.. _kill:

kill - Send a Signal to a Process
---------------------------------
.. index:: kill
.. index:: send a signal to a process

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sys/types.h>
    #include <signal.h>
    int kill(
        pid_t pid,
        int   sig
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno`` to
indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.
 * - ``EPERM``
   - Process does not have permission to send the signal to any receiving
     process.
 * - ``ESRCH``
   - The process indicated by the parameter pid is invalid.

**DESCRIPTION:**

This function sends the signal ``sig`` to the process ``pid``.

**NOTES:**

Since RTEMS is a single-process system, a signal can only be sent to the
calling process (i.e. the current node).

.. _sigpending:

sigpending - Examine Pending Signals
------------------------------------
.. index:: sigpending
.. index:: examine pending signals

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
        int sigpending(
        const sigset_t *set
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EFAULT``
   - Invalid address for set.

**DESCRIPTION:**

This function allows the caller to examine the set of currently pending
signals. A pending signal is one which has been raised but is currently
blocked. The set of pending signals is returned in ``set``.

.. _sigsuspend:

sigsuspend - Wait for a Signal
------------------------------
.. index:: sigsuspend
.. index:: wait for a signal

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
       int sigsuspend(
       const sigset_t *sigmask
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINTR``
   - Signal interrupted this function.

**DESCRIPTION:**

This function temporarily replaces the signal mask for the process with that
specified by ``sigmask`` and blocks the calling thread until a signal is
raised.

.. _pause:

pause - Suspend Process Execution
---------------------------------
.. index:: pause
.. index:: suspend process execution

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int pause( void );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINTR``
   - Signal interrupted this function.

**DESCRIPTION:**

This function causes the calling thread to be blocked until an unblocked signal
is received.

.. _sigwait:

sigwait - Synchronously Accept a Signal
---------------------------------------
.. index:: sigwait
.. index:: synchronously accept a signal

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigwait(
        const sigset_t *set,
        int            *sig
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.
 * - ``EINTR``
   - Signal interrupted this function.

**DESCRIPTION:**

This function selects a pending signal based on the set specified in ``set``,
atomically clears it from the set of pending signals, and returns the signal
number for that signal in ``sig``.

.. _sigwaitinfo:

sigwaitinfo - Synchronously Accept a Signal
-------------------------------------------
.. index:: sigwaitinfo
.. index:: synchronously accept a signal

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigwaitinfo(
        const sigset_t *set,
        siginfo_t      *info
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

*EINTR*
    Signal interrupted this function.

**DESCRIPTION:**

This function selects a pending signal based on the set specified in ``set``,
atomically clears it from the set of pending signals, and returns information
about that signal in ``info``.

The prototype of the ``siginfo_t`` structure is the following:

.. code-block:: c

    typedef struct
    {
        int si_signo;        /* Signal number */
        int si_code;         /* Cause of the signal */
        pid_t si_pid;        /* Sending process ID */
        uid_t si_uid;        /* Real user ID of sending process */
        void* si_addr;       /* Address of faulting instruction */
        int si_status;       /* Exit value or signal */
        union sigval
        {
            int sival_int;   /* Integer signal value */
            void* sival_ptr; /* Pointer signal value */
        } si_value;          /* Signal value */
    }

.. _sigtimedwait:

sigtimedwait - Synchronously Accept a Signal with Timeout
---------------------------------------------------------
.. index:: sigtimedwait
.. index:: synchronously accept a signal with timeout

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigtimedwait(
        const sigset_t        *set,
        siginfo_t             *info,
        const struct timespec *timeout
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - Timed out while waiting for the specified signal set.
 * - ``EINVAL``
   - Nanoseconds field of the timeout argument is invalid.
 * - ``EINTR``
   - Signal interrupted this function.

**DESCRIPTION:**

This function selects a pending signal based on the set specified in ``set``,
atomically clears it from the set of pending signals, and returns information
about that signal in ``info``. The calling thread will block up to ``timeout``
waiting for the signal to arrive.

The ``timespec`` structure is defined as follows:

.. code-block:: c

    struct timespec
    {
        time_t tv_sec; /* Seconds */
        long tv_nsec;  /* Nanoseconds */
    }

**NOTES:**

If ``timeout`` is NULL, then the calling thread will wait forever for the
specified signal set.

.. _sigqueue:

sigqueue - Queue a Signal to a Process
--------------------------------------
.. index:: sigqueue
.. index:: queue a signal to a process

**CALLING SEQUENCE:**

.. code-block:: c

    #include <signal.h>
    int sigqueue(
        pid_t              pid,
        int                signo,
        const union sigval value
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets ``errno``
to indicate the error. ``errno`` may be set to:

.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - No resources available to queue the signal. The process has already queued
     ``SIGQUEUE_MAX`` signals that are still pending at the receiver or the
     systemwide resource limit has been exceeded.
 * - ``EINVAL``
   - The value of the signo argument is an invalid or unsupported signal
     number.
 * - ``EPERM``
   - The process does not have the appropriate privilege to send the signal to
     the receiving process.
 * - ``ESRCH``
   - The process pid does not exist.

**DESCRIPTION:**

This function sends the signal specified by ``signo`` to the process ``pid``

The ``sigval`` union is specified as:

.. code-block:: c

    union sigval
    {
        int sival_int; /* Integer signal value */
        void* sival_ptr; /* Pointer signal value */
    }

**NOTES:**

Since RTEMS is a single-process system, a signal can only be sent to the
calling process (i.e. the current node).

.. _alarm:

alarm - Schedule Alarm
----------------------
.. index:: alarm
.. index:: schedule alarm

**CALLING SEQUENCE:**

.. code-block:: c

    #include <unistd.h>
    unsigned int alarm(
        unsigned int seconds
    );

**STATUS CODES:**

This call always succeeds.

If there was a previous ``alarm()`` request with time remaining, then this
routine returns the number of seconds until that outstanding alarm would have
fired. If no previous ``alarm()`` request was outstanding, then zero is
returned.

**DESCRIPTION:**

The ``alarm()`` service causes the ``SIGALRM`` signal to be generated after the
number of seconds specified by ``seconds`` has elapsed.

**NOTES:**

Alarm requests do not queue.  If ``alarm`` is called while a previous request
is outstanding, the call will result in rescheduling the time at which the
``SIGALRM`` signal will be generated.

If the notification signal, ``SIGALRM``, is not caught or ignored, the calling
process is terminated.

.. _ualarm:

ualarm - Schedule Alarm in Microseconds
---------------------------------------
.. index:: alarm
.. index:: microseonds alarm
.. index:: usecs alarm
.. index:: schedule alarm in microseonds

**CALLING SEQUENCE:**

.. code-block:: c

    #include <unistd.h>
    useconds_t ualarm(
        useconds_t useconds,
        useconds_t interval
    );

**STATUS CODES:**

This call always succeeds.

If there was a previous ``ualarm()`` request with time remaining, then this
routine returns the number of seconds until that outstanding alarm would have
fired. If no previous ``alarm()`` request was outstanding, then zero is
returned.

**DESCRIPTION:**

The ``ualarm()`` service causes the ``SIGALRM`` signal to be generated after
the number of microseconds specified by ``useconds`` has elapsed.

When ``interval`` is non-zero, repeated timeout notification occurs with a
period in microseconds specified by ``interval``.

**NOTES:**

Alarm requests do not queue.  If ``alarm`` is called while a previous request
is outstanding, the call will result in rescheduling the time at which the
``SIGALRM`` signal will be generated.

If the notification signal, ``SIGALRM``, is not caught or ignored, the calling
process is terminated.
