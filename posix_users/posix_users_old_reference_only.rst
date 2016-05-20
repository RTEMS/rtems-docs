.. comment SPDX-License-Identifier: CC-BY-SA-4.0

:orphan:



.. COMMENT: %**end of header

.. COMMENT: COPYRIGHT (c) 1989-2013.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: Master file for the POSIX API User's Guide

.. COMMENT: Joel's Questions

.. COMMENT: 1.  Why does paragraphindent only impact makeinfo?

.. COMMENT: 2.  Why does paragraphindent show up in HTML?

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: The following determines which set of the tables and figures we will use.

.. COMMENT: We default to ASCII but if available TeX or HTML versions will

.. COMMENT: be used instead.

.. COMMENT: @clear use-html

.. COMMENT: @clear use-tex

.. COMMENT: The following variable says to use texinfo or html for the two column

.. COMMENT: texinfo tables.  For somethings the format does not look good in html.

.. COMMENT: With our adjustment to the left column in TeX, it nearly always looks

.. COMMENT: good printed.

.. COMMENT: Custom whitespace adjustments.  We could fiddle a bit more.

.. COMMENT: variable substitution info:

.. COMMENT: Note: At the moment we do not document the Ada interface but by building

.. COMMENT: in the infrastructure Florist support should be simple to add.

.. COMMENT: the language is @value{LANGUAGE}

.. COMMENT: NOTE:  don't use underscore in the name

.. COMMENT: Title Page Stuff

.. COMMENT: I don't really like having a short title page.  -joel

.. COMMENT: @shorttitlepage RTEMS POSIX API User's Guide

============================
RTEMS POSIX API User’s Guide
============================

.. COMMENT: COPYRIGHT (c) 1988-2015.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: The following puts a space somewhere on an otherwise empty page so we

.. COMMENT: can force the copyright description onto a left hand page.

COPYRIGHT © 1988 - 2015.

On-Line Applications Research Corporation (OAR).

The authors have used their best efforts in preparing
this material.  These efforts include the development, research,
and testing of the theories and programs to determine their
effectiveness.  No warranty of any kind, expressed or implied,
with regard to the software or the material contained in this
document is provided.  No liability arising out of the
application or use of any product described in this document is
assumed.  The authors reserve the right to revise this material
and to make changes from time to time in the content hereof
without obligation to notify anyone of such revision or changes.

The RTEMS Project is hosted at http://www.rtems.org.  Any
inquiries concerning RTEMS, its related support components, or its
documentation should be directed to the Community Project hosted athttp://www.rtems.org.

Any inquiries for commercial services including training, support, custom
development, application development assistance should be directed tohttp://www.rtems.com.

.. COMMENT: This prevents a black box from being printed on "overflow" lines.

.. COMMENT: The alternative is to rework a sentence to avoid this problem.

RTEMS POSIX API User’s Guide
############################

.. COMMENT: COPYRIGHT (c) 1989-2011.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Preface
#######

This is the User’s Guide for the POSIX API support
provided in RTEMS.

The functionality described in this document is based
on the following standards:

- POSIX 1003.1b-1993.

- POSIX 1003.1h/D3.

- Open Group Single UNIX Specification.

Much of the POSIX API standard is actually implemented in the
Cygnus Newlib ANSI C Library.  Please refer to documentation on
Newlib for more information on the functionality it supplies.

This manual is still under construction and improvements
are welcomed from users.

Acknowledgements
================

.. COMMENT: COPYRIGHT (c) 1988-2009.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: The RTEMS Project has been granted permission from The Open Group

.. COMMENT: IEEE to excerpt and use portions of the POSIX standards documents

.. COMMENT: in the RTEMS POSIX API User's Guide and RTEMS Shell User's Guide.

.. COMMENT: We have to include a specific acknowledgement paragraph in these

.. COMMENT: documents (e.g. preface or copyright page) and another slightly

.. COMMENT: different paragraph for each manual page that excerpts and uses

.. COMMENT: text from the standards.

.. COMMENT: This file should help ensure that the paragraphs are consistent

.. COMMENT: and not duplicated

    The Institute of Electrical and Electronics Engineers, Inc and The
    Open Group, have given us permission to reprint portions of their
    documentation.
    Portions of this text are reprinted and reproduced in electronic
    form from IEEE Std 1003.1, 2004 Edition, Standard for Information
    Technology â Operating System Interface (POSIX), The Open
    Group Base Specifications Issue 6, Copyright Â© 2001-2004 by the
    Institute of Electrical and Electronics Engineers, Inc and The
    Open Group. In the event of any discrepancy between this version
    and the original IEEE and The Open Group Standard, the original
    IEEE and The Open Group Standard is the referee document. The
    original Standard can be obtained online athttp://www.opengroup.org/unix/online.html.
    This notice shall appear on any product containing this material.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Process Creation and Execution Manager
######################################

Introduction
============

The process creation and execution manager provides the
functionality associated with the creation and termination
of processes.

The directives provided by the process creation and execution manager are:

- ``fork`` - Create a Process

- ``execl`` - Execute a File

- ``execv`` - Execute a File

- ``execle`` - Execute a File

- ``execve`` - Execute a File

- ``execlp`` - Execute a File

- ``execvp`` - Execute a File

- ``pthread_atfork`` - Register Fork Handlers

- ``wait`` - Wait for Process Termination

- ``waitpid`` - Wait for Process Termination

- ``_exit`` - Terminate a Process

Background
==========

POSIX process functionality can not be completely
supported by RTEMS.  This is because RTEMS provides no memory
protection and implements a *single process, multi-threaded
execution model*.  In this light, RTEMS provides none of the
routines that are associated with the creation of new processes.
However, since the entire RTEMS application (e.g. executable)
is logically a single POSIX process, RTEMS is able to provide
implementations of many operations on processes.  The rule of
thumb is that those routines provide a meaningful result.
For example, ``getpid()`` returns the node number.

Operations
==========

The only functionality method defined by this manager which is
supported by RTEMS is the ``_exit`` service.  The
implementation of ``_exit`` shuts the application down and
is equivalent to invoking either ``exit`` or``rtems_shutdown_executive``.

Directives
==========

This section details the process creation and execution manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

fork - Create a Process
-----------------------
.. index:: fork
.. index:: create a process

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    int fork( void );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

execl - Execute a File
----------------------
.. index:: execl
.. index:: execute a file

**CALLING SEQUENCE:**

.. code:: c

    int execl(
    const char \*path,
    const char \*arg,
    ...
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

execv - Execute a File
----------------------
.. index:: execv
.. index:: execute a file

**CALLING SEQUENCE:**

.. code:: c

    int execv(
    const char \*path,
    char const \*argv[],
    ...
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

execle - Execute a File
-----------------------
.. index:: execle
.. index:: execute a file

**CALLING SEQUENCE:**

.. code:: c

    int execle(
    const char \*path,
    const char \*arg,
    ...
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

execve - Execute a File
-----------------------
.. index:: execve
.. index:: execute a file

**CALLING SEQUENCE:**

.. code:: c

    int execve(
    const char \*path,
    char \*const argv[],
    char \*const envp[]
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

execlp - Execute a File
-----------------------
.. index:: execlp
.. index:: execute a file

**CALLING SEQUENCE:**

.. code:: c

    int execlp(
    const char \*file,
    const char \*arg,
    ...
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

execvp - Execute a File
-----------------------
.. index:: execvp
.. index:: execute a file

**CALLING SEQUENCE:**

.. code:: c

    int execvp(
    const char \*file,
    char \*const argv[]
    ...
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

pthread_atfork - Register Fork Handlers
---------------------------------------
.. index:: pthread_atfork
.. index:: register fork handlers

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    int pthread_atfork(
    void (\*prepare)(void),
    void (\*parent)(void),
    void (\*child)(void)
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

wait - Wait for Process Termination
-----------------------------------
.. index:: wait
.. index:: wait for process termination

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/wait.h>
    int wait(
    int \*stat_loc
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

waitpid - Wait for Process Termination
--------------------------------------
.. index:: waitpid
.. index:: wait for process termination

**CALLING SEQUENCE:**

.. code:: c

    int wait(
    pid_t  pid,
    int   \*stat_loc,
    int    options
    );

**STATUS CODES:**

*ENOSYS*
    This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

_exit - Terminate a Process
---------------------------
.. index:: _exit
.. index:: terminate a process

**CALLING SEQUENCE:**

.. code:: c

    void _exit(
    int status
    );

**STATUS CODES:**

NONE

**DESCRIPTION:**

The ``_exit()`` function terminates the calling process.

**NOTES:**

In RTEMS, a process is equivalent to the entire application on a single
processor. Invoking this service terminates the application.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Signal Manager
##############

Introduction
============

The signal manager provides the functionality associated with
the generation, delivery, and management of process-oriented
signals.

The directives provided by the signal manager are:

- ``sigaddset`` - Add a Signal to a Signal Set

- ``sigdelset`` - Delete a Signal from a Signal Set

- ``sigfillset`` - Fill a Signal Set

- ``sigismember`` - Is Signal a Member of a Signal Set

- ``sigemptyset`` - Empty a Signal Set

- ``sigaction`` - Examine and Change Signal Action

- ``pthread_kill`` - Send a Signal to a Thread

- ``sigprocmask`` - Examine and Change Process Blocked Signals

- ``pthread_sigmask`` - Examine and Change Thread Blocked Signals

- ``kill`` - Send a Signal to a Process

- ``sigpending`` - Examine Pending Signals

- ``sigsuspend`` - Wait for a Signal

- ``pause`` - Suspend Process Execution

- ``sigwait`` - Synchronously Accept a Signal

- ``sigwaitinfo`` - Synchronously Accept a Signal

- ``sigtimedwait`` - Synchronously Accept a Signal with Timeout

- ``sigqueue`` - Queue a Signal to a Process

- ``alarm`` - Schedule Alarm

- ``ualarm`` - Schedule Alarm in Microseconds

Background
==========

Signals
-------

POSIX signals are an asynchronous event mechanism.  Each process
and thread has a set of signals associated with it.  Individual
signals may be enabled (e.g. unmasked) or blocked (e.g. ignored)
on both a per-thread and process level.  Signals which are
enabled have a signal handler associated with them.  When the
signal is generated and conditions are met, then the signal
handler is invoked in the proper process or thread context
asynchronous relative to the logical thread of execution.

If a signal has been blocked when it is generated, then it
is queued and kept pending until the thread or process unblocks
the signal or explicitly checks for it.
Traditional, non-real-time POSIX signals do not queue.  Thus
if a process or thread has blocked a particular signal, then
multiple occurrences of that signal are recorded as a
single occurrence of that signal.

.. COMMENT: TODO: SIGRTMIN and SIGRTMAX ?

One can check for the set of outstanding signals that have been
blocked.   Services are provided to check for outstanding process
or thread directed signals.

Signal Delivery
---------------

Signals which are directed at a thread are delivered to the specified thread.

Signals which are directed at a process are delivered to a thread which
is selected based on the following algorithm:

# If the action for this signal is currently ``SIG_IGN``,
  then the signal is simply ignored.

# If the currently executing thread has the signal unblocked, then
  the signal is delivered to it.

# If any threads are currently blocked waiting for this signal
  (``sigwait()``), then the signal is delivered to the highest priority
  thread waiting for this signal.

# If any other threads are willing to accept delivery of the signal, then
  the signal is delivered to the highest priority thread of this set. In the
  event, multiple threads of the same priority are willing to accept this
  signal, then priority is given first to ready threads, then to threads
  blocked on calls which may be interrupted, and finally to threads blocked
  on non-interruptible calls.

# In the event the signal still can not be delivered, then it is left
  pending. The first thread to unblock the signal (``sigprocmask()`` or``pthread_sigprocmask()``) or to wait for this signal
  (``sigwait()``) will be the recipient of the signal.

Operations
==========

Signal Set Management
---------------------

Each process and each thread within that process has a set of
individual signals and handlers associated with it.   Services
are provided to construct signal sets for the purposes of building
signal sets – type ``sigset_t`` – that are used to
provide arguments to the services that mask, unmask, and
check on pending signals.

Blocking Until Signal Generation
--------------------------------

A thread may block until receipt of a signal.  The "sigwait"
and "pause" families of functions block until the requested
signal is received or if using ``sigtimedwait()`` until the specified
timeout period has elapsed.

Sending a Signal
----------------

This is accomplished
via one of a number of services that sends a signal to either a
process or thread.  Signals may be directed at a process by
the service ``kill()`` or at a thread by the service``pthread_kill()``

Directives
==========

This section details the signal manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

sigaddset - Add a Signal to a Signal Set
----------------------------------------
.. index:: sigaddset
.. index:: add a signal to a signal set

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigaddset(
    sigset_t \*set,
    int       signo
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function adds the signal ``signo`` to the specified signal ``set``.

**NOTES:**

The set must be initialized using either ``sigemptyset`` or ``sigfillset``
before using this function.

sigdelset - Delete a Signal from a Signal Set
---------------------------------------------
.. index:: sigdelset
.. index:: delete a signal from a signal set

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigdelset(
    sigset_t \*set,
    int       signo
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function deletes the signal specified by ``signo`` from the specified
signal ``set``.

**NOTES:**

The set must be initialized using either ``sigemptyset`` or ``sigfillset``
before using this function.

sigfillset - Fill a Signal Set
------------------------------
.. index:: sigfillset
.. index:: fill a signal set

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigfillset(
    sigset_t \*set
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function fills the specified signal ``set`` such that all
signals are set.

sigismember - Is Signal a Member of a Signal Set
------------------------------------------------
.. index:: sigismember
.. index:: is signal a member of a signal set

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigismember(
    const sigset_t \*set,
    int             signo
    );

**STATUS CODES:**

The function returns either 1 or 0 if completed successfully, otherwise it
returns -1 and sets ``errno`` to indicate the error. ``errno`` may be set
to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function returns returns 1 if ``signo`` is a member of ``set``
and 0 otherwise.

**NOTES:**

The set must be initialized using either ``sigemptyset`` or ``sigfillset``
before using this function.

sigemptyset - Empty a Signal Set
--------------------------------
.. index:: sigemptyset
.. index:: empty a signal set

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigemptyset(
    sigset_t \*set
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function initializes an empty signal set pointed to by ``set``.

sigaction - Examine and Change Signal Action
--------------------------------------------
.. index:: sigaction
.. index:: examine and change signal action

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigaction(
    int                     sig,
    const struct sigaction \*act,
    struct sigaction       \*oact
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

*ENOTSUP*
    Realtime Signals Extension option not supported.

**DESCRIPTION:**

If the argument act is not a null pointer, it points to a structure specifying
the action to be associated with the specified signal. If the argument oact is
not a null pointer, the action previously associated with the signal is stored
in the location pointed to by the argument oact. If the argument act is a null
pointer, signal handling is unchanged; thus, the call can be used to enquire
about the current handling of a given signal.

The structure ``sigaction`` has the following members:

``void(\*)(int) sa_handler``
    Pointer to a signal-catching function or one of the macros SIG_IGN or SIG_DFL.

``sigset_t sa_mask``
    Additional set of signals to be blocked during execution of signal-catching function.

``int sa_flags``
    Special flags to affect behavior of signal.

``void(\*)(int, siginfo_t*, void*) sa_sigaction``
    Alternative pointer to a signal-catching function.

``sa_handler`` and ``sa_sigaction`` should never be used at the same time as their storage may overlap.

If the ``SA_SIGINFO`` flag (see below) is set in ``sa_flags``, the``sa_sigaction`` field specifies a signal-catching function, otherwise``sa_handler`` specifies the action to be associated with the signal, which
may be a signal-catching function or one of the macros ``SIG_IGN`` or``SIG_DFN``.

The following flags can be set in the ``sa_flags`` field:

``SA_SIGINFO``
    If not set, the signal-catching function should be declared as ``void
    func(int signo)`` and the address of the function should be set in``sa_handler``.  If set, the signal-catching function should be declared as``void func(int signo, siginfo_t* info, void* context)`` and the address of
    the function should be set in ``sa_sigaction``.

The prototype of the ``siginfo_t`` structure is the following:
.. code:: c

    typedef struct
    {
    int si_signo; /* Signal number \*/
    int si_code; /* Cause of the signal \*/
    pid_t si_pid; /* Sending process ID \*/
    uid_t si_uid; /* Real user ID of sending process \*/
    void* si_addr; /* Address of faulting instruction \*/
    int si_status; /* Exit value or signal \*/
    union sigval
    {
    int sival_int; /* Integer signal value \*/
    void* sival_ptr; /* Pointer signal value \*/
    } si_value; /* Signal value \*/
    }

**NOTES:**

The signal number cannot be SIGKILL.

pthread_kill - Send a Signal to a Thread
----------------------------------------
.. index:: pthread_kill
.. index:: send a signal to a thread

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int pthread_kill(
    pthread_t thread,
    int       sig
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*ESRCH*
    The thread indicated by the parameter thread is invalid.

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This functions sends the specified signal ``sig`` to a thread referenced
to by ``thread``.

If the signal code is ``0``, arguments are validated and no signal is sent.

sigprocmask - Examine and Change Process Blocked Signals
--------------------------------------------------------
.. index:: sigprocmask
.. index:: examine and change process blocked signals

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigprocmask(
    int             how,
    const sigset_t \*set,
    sigset_t       \*oset
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function is used to alter the set of currently blocked signals
on a process wide basis. A blocked signal will not be received by the
process. The behavior of this function is dependent on the value of``how`` which may be one of the following:

``SIG_BLOCK``
    The set of blocked signals is set to the union of ``set`` and
    those signals currently blocked.

``SIG_UNBLOCK``
    The signals specific in ``set`` are removed from the currently
    blocked set.

``SIG_SETMASK``
    The set of currently blocked signals is set to ``set``.

If ``oset`` is not ``NULL``, then the set of blocked signals prior to
this call is returned in ``oset``. If ``set`` is *NULL*, no change is
done, allowing to examine the set of currently blocked signals.

**NOTES:**

It is not an error to unblock a signal which is not blocked.

In the current implementation of RTEMS POSIX API sigprocmask() is technically
mapped to pthread_sigmask().

pthread_sigmask - Examine and Change Thread Blocked Signals
-----------------------------------------------------------
.. index:: pthread_sigmask
.. index:: examine and change thread blocked signals

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int pthread_sigmask(
    int             how,
    const sigset_t \*set,
    sigset_t       \*oset
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

This function is used to alter the set of currently blocked signals
for the calling thread. A blocked signal will not be received by the
process. The behavior of this function is dependent on the value of``how`` which may be one of the following:

``SIG_BLOCK``
    The set of blocked signals is set to the union of ``set`` and
    those signals currently blocked.

``SIG_UNBLOCK``
    The signals specific in ``set`` are removed from the currently
    blocked set.

``SIG_SETMASK``
    The set of currently blocked signals is set to ``set``.

If ``oset`` is not ``NULL``, then the set of blocked signals prior to
this call is returned in ``oset``. If ``set`` is *NULL*, no change is
done, allowing to examine the set of currently blocked signals.

**NOTES:**

It is not an error to unblock a signal which is not blocked.

kill - Send a Signal to a Process
---------------------------------
.. index:: kill
.. index:: send a signal to a process

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <signal.h>
    int kill(
    pid_t pid,
    int   sig
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

*EPERM*
    Process does not have permission to send the signal to any receiving process.

*ESRCH*
    The process indicated by the parameter pid is invalid.

**DESCRIPTION:**

This function sends the signal ``sig`` to the process ``pid``.

**NOTES:**

Since RTEMS is a single-process system, a signal can only be sent to the calling
process (i.e. the current node).

sigpending - Examine Pending Signals
------------------------------------
.. index:: sigpending
.. index:: examine pending signals

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigpending(
    const sigset_t \*set
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EFAULT*
    Invalid address for set.

**DESCRIPTION:**

This function allows the caller to examine the set of currently pending
signals. A pending signal is one which has been raised but is currently
blocked. The set of pending signals is returned in ``set``.

sigsuspend - Wait for a Signal
------------------------------
.. index:: sigsuspend
.. index:: wait for a signal

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigsuspend(
    const sigset_t \*sigmask
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINTR*
    Signal interrupted this function.

**DESCRIPTION:**

This function temporarily replaces the signal mask for the process
with that specified by ``sigmask`` and blocks the calling thread
until a signal is raised.

pause - Suspend Process Execution
---------------------------------
.. index:: pause
.. index:: suspend process execution

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int pause( void );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINTR*
    Signal interrupted this function.

**DESCRIPTION:**

This function causes the calling thread to be blocked until an
unblocked signal is received.

sigwait - Synchronously Accept a Signal
---------------------------------------
.. index:: sigwait
.. index:: synchronously accept a signal

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigwait(
    const sigset_t \*set,
    int            \*sig
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINVAL*
    Invalid argument passed.

*EINTR*
    Signal interrupted this function.

**DESCRIPTION:**

This function selects a pending signal based on the set specified in``set``, atomically clears it from the set of pending signals, and
returns the signal number for that signal in ``sig``.

sigwaitinfo - Synchronously Accept a Signal
-------------------------------------------
.. index:: sigwaitinfo
.. index:: synchronously accept a signal

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigwaitinfo(
    const sigset_t \*set,
    siginfo_t      \*info
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EINTR*
    Signal interrupted this function.

**DESCRIPTION:**

This function selects a pending signal based on the set specified in``set``, atomically clears it from the set of pending signals, and
returns information about that signal in ``info``.

The prototype of the ``siginfo_t`` structure is the following:
.. code:: c

    typedef struct
    {
    int si_signo; /* Signal number \*/
    int si_code; /* Cause of the signal \*/
    pid_t si_pid; /* Sending process ID \*/
    uid_t si_uid; /* Real user ID of sending process \*/
    void* si_addr; /* Address of faulting instruction \*/
    int si_status; /* Exit value or signal \*/
    union sigval
    {
    int sival_int; /* Integer signal value \*/
    void* sival_ptr; /* Pointer signal value \*/
    } si_value; /* Signal value \*/
    }

sigtimedwait - Synchronously Accept a Signal with Timeout
---------------------------------------------------------
.. index:: sigtimedwait
.. index:: synchronously accept a signal with timeout

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigtimedwait(
    const sigset_t        \*set,
    siginfo_t             \*info,
    const struct timespec \*timeout
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EAGAIN*
    Timed out while waiting for the specified signal set.

*EINVAL*
    Nanoseconds field of the timeout argument is invalid.

*EINTR*
    Signal interrupted this function.

**DESCRIPTION:**

This function selects a pending signal based on the set specified in``set``, atomically clears it from the set of pending signals, and
returns information about that signal in ``info``. The calling thread
will block up to ``timeout`` waiting for the signal to arrive.

The ``timespec`` structure is defined as follows:
.. code:: c

    struct timespec
    {
    time_t tv_sec; /* Seconds \*/
    long tv_nsec; /* Nanoseconds \*/
    }

**NOTES:**

If ``timeout`` is NULL, then the calling thread will wait forever for
the specified signal set.

sigqueue - Queue a Signal to a Process
--------------------------------------
.. index:: sigqueue
.. index:: queue a signal to a process

**CALLING SEQUENCE:**

.. code:: c

    #include <signal.h>
    int sigqueue(
    pid_t              pid,
    int                signo,
    const union sigval value
    );

**STATUS CODES:**

The function returns 0 on success, otherwise it returns -1 and sets``errno`` to indicate the error. ``errno`` may be set to:

*EAGAIN*
    No resources available to queue the signal. The process has already
    queued SIGQUEUE_MAX signals that are still pending at the receiver
    or the systemwide resource limit has been exceeded.

*EINVAL*
    The value of the signo argument is an invalid or unsupported signal
    number.

*EPERM*
    The process does not have the appropriate privilege to send the signal
    to the receiving process.

*ESRCH*
    The process pid does not exist.

**DESCRIPTION:**

This function sends the signal specified by ``signo`` to the
process ``pid``

The ``sigval`` union is specified as:
.. code:: c

    union sigval
    {
    int sival_int; /* Integer signal value \*/
    void* sival_ptr; /* Pointer signal value \*/
    }

**NOTES:**

Since RTEMS is a single-process system, a signal can only be sent to the calling
process (i.e. the current node).

alarm - Schedule Alarm
----------------------
.. index:: alarm
.. index:: schedule alarm

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    unsigned int alarm(
    unsigned int seconds
    );

**STATUS CODES:**

This call always succeeds.

If there was a previous ``alarm()`` request with time remaining,
then this routine returns the number of seconds until that outstanding
alarm would have fired. If no previous ``alarm()`` request was
outstanding, then zero is returned.

**DESCRIPTION:**

The ``alarm()`` service causes the ``SIGALRM`` signal to
be generated after the number of seconds specified by``seconds`` has elapsed.

**NOTES:**

Alarm requests do not queue.  If ``alarm`` is called while
a previous request is outstanding, the call will result in
rescheduling the time at which the ``SIGALRM`` signal
will be generated.

If the notification signal, ``SIGALRM``, is not caught or ignored, the
calling process is terminated.

ualarm - Schedule Alarm in Microseconds
---------------------------------------
.. index:: alarm
.. index:: microseonds alarm
.. index:: usecs alarm
.. index:: schedule alarm in microseonds

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    useconds_t ualarm(
    useconds_t useconds,
    useconds_t interval
    );

**STATUS CODES:**

This call always succeeds.

If there was a previous ``ualarm()`` request with time remaining,
then this routine returns the number of seconds until that outstanding
alarm would have fired. If no previous ``alarm()`` request was
outstanding, then zero is returned.

**DESCRIPTION:**

The ``ualarm()`` service causes the ``SIGALRM`` signal to
be generated after the number of microseconds specified by``useconds`` has elapsed.

When ``interval`` is non-zero, repeated timeout notification occurs
with a period in microseconds specified by ``interval``.

**NOTES:**

Alarm requests do not queue.  If ``alarm`` is called while
a previous request is outstanding, the call will result in
rescheduling the time at which the ``SIGALRM`` signal
will be generated.

If the notification signal, ``SIGALRM``, is not caught or ignored, the
calling process is terminated.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Process Environment Manager
###########################

Introduction
============

The process environment manager is responsible for providing the
functions related to user and group Id management.

The directives provided by the process environment manager are:

- ``getpid`` - Get Process ID

- ``getppid`` - Get Parent Process ID

- ``getuid`` - Get User ID

- ``geteuid`` - Get Effective User ID

- ``getgid`` - Get Real Group ID

- ``getegid`` - Get Effective Group ID

- ``setuid`` - Set User ID

- ``setgid`` - Set Group ID

- ``getgroups`` - Get Supplementary Group IDs

- ``getlogin`` - Get User Name

- ``getlogin_r`` - Reentrant Get User Name

- ``getpgrp`` - Get Process Group ID

- ``setsid`` - Create Session and Set Process Group ID

- ``setpgid`` - Set Process Group ID for Job Control

- ``uname`` - Get System Name

- ``times`` - Get Process Times

- ``getenv`` - Get Environment Variables

- ``setenv`` - Set Environment Variables

- ``ctermid`` - Generate Terminal Pathname

- ``ttyname`` - Determine Terminal Device Name

- ``ttyname_r`` - Reentrant Determine Terminal Device Name

- ``isatty`` - Determine if File Descriptor is Terminal

- ``sysconf`` - Get Configurable System Variables

Background
==========

Users and Groups
----------------

RTEMS provides a single process, multi-threaded execution environment.
In this light, the notion of user and group is somewhat without meaning.
But RTEMS does provide services to provide a synthetic version of
user and group.  By default, a single user and group is associated
with the application.  Thus unless special actions are taken,
every thread in the application shares the same user and group Id.
The initial rationale for providing user and group Id functionality
in RTEMS was for the filesystem infrastructure to implement
file permission checks.  The effective user/group Id capability
has since been used to implement permissions checking by
the ``ftpd`` server.

In addition to the "real" user and group Ids, a process may
have an effective user/group Id.  This allows a process to
function using a more limited permission set for certain operations.

User and Group Names
--------------------

POSIX considers user and group Ids to be a unique integer that
may be associated with a name.  This is usually accomplished
via a file named ``/etc/passwd`` for user Id mapping and``/etc/groups`` for group Id mapping.  Again, although
RTEMS is effectively a single process and thus single user
system, it provides limited support for user and group
names.  When configured with an appropriate filesystem, RTEMS
will access the appropriate files to map user and group Ids
to names.

If these files do not exist, then RTEMS will synthesize
a minimal version so this family of services return without
error.  It is important to remember that a design goal of
the RTEMS POSIX services is to provide useable and
meaningful results even though a full process model
is not available.

Environment Variables
---------------------

POSIX allows for variables in the run-time environment.  These are
name/value pairs that make be dynamically set and obtained by
programs.  In a full POSIX environment with command line shell
and multiple processes,  environment variables may be set in
one process – such as the shell – and inherited by child
processes.  In RTEMS, there is only one process and thus
only one set of environment variables across all processes.

Operations
==========

Accessing User and Group Ids
----------------------------

The user Id associated with the current thread may be obtain
using the ``getuid()`` service.  Similarly, the group Id
may be obtained using the ``getgid()`` service.

Accessing Environment Variables
-------------------------------

The value associated with an environment variable may be
obtained using the ``getenv()`` service and set using
the ``putenv()`` service.

Directives
==========

This section details the process environment manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

getpid - Get Process ID
-----------------------
.. index:: getpid
.. index:: get process id

**CALLING SEQUENCE:**

.. code:: c

    int getpid( void );

**STATUS CODES:**

The process Id is returned.

**DESCRIPTION:**

This service returns the process Id.

**NOTES:**

NONE

getppid - Get Parent Process ID
-------------------------------
.. index:: getppid
.. index:: get parent process id

**CALLING SEQUENCE:**

.. code:: c

    int getppid( void );

**STATUS CODES:**

The parent process Id is returned.

**DESCRIPTION:**

This service returns the parent process Id.

**NOTES:**

NONE

getuid - Get User ID
--------------------
.. index:: getuid
.. index:: get user id

**CALLING SEQUENCE:**

.. code:: c

    int getuid( void );

**STATUS CODES:**

The effective user Id is returned.

**DESCRIPTION:**

This service returns the effective user Id.

**NOTES:**

NONE

geteuid - Get Effective User ID
-------------------------------
.. index:: geteuid
.. index:: get effective user id

**CALLING SEQUENCE:**

.. code:: c

    int geteuid( void );

**STATUS CODES:**

The effective group Id is returned.

**DESCRIPTION:**

This service returns the effective group Id.

**NOTES:**

NONE

getgid - Get Real Group ID
--------------------------
.. index:: getgid
.. index:: get real group id

**CALLING SEQUENCE:**

.. code:: c

    int getgid( void );

**STATUS CODES:**

The group Id is returned.

**DESCRIPTION:**

This service returns the group Id.

**NOTES:**

NONE

getegid - Get Effective Group ID
--------------------------------
.. index:: getegid
.. index:: get effective group id

**CALLING SEQUENCE:**

.. code:: c

    int getegid( void );

**STATUS CODES:**

The effective group Id is returned.

**DESCRIPTION:**

This service returns the effective group Id.

**NOTES:**

NONE

setuid - Set User ID
--------------------
.. index:: setuid
.. index:: set user id

**CALLING SEQUENCE:**

.. code:: c

    int setuid(
    uid_t uid
    );

**STATUS CODES:**

This service returns 0.

**DESCRIPTION:**

This service sets the user Id to ``uid``.

**NOTES:**

NONE

setgid - Set Group ID
---------------------
.. index:: setgid
.. index:: set group id

**CALLING SEQUENCE:**

.. code:: c

    int setgid(
    gid_t  gid
    );

**STATUS CODES:**

This service returns 0.

**DESCRIPTION:**

This service sets the group Id to ``gid``.

**NOTES:**

NONE

getgroups - Get Supplementary Group IDs
---------------------------------------
.. index:: getgroups
.. index:: get supplementary group ids

**CALLING SEQUENCE:**

.. code:: c

    int getgroups(
    int    gidsetsize,
    gid_t  grouplist[]
    );

**STATUS CODES:**

NA

**DESCRIPTION:**

This service is not implemented as RTEMS has no notion of
supplemental groups.

**NOTES:**

If supported, this routine would only be allowed for
the super-user.

getlogin - Get User Name
------------------------
.. index:: getlogin
.. index:: get user name

**CALLING SEQUENCE:**

.. code:: c

    char \*getlogin( void );

**STATUS CODES:**

Returns a pointer to a string containing the name of the
current user.

**DESCRIPTION:**

This routine returns the name of the current user.

**NOTES:**

This routine is not reentrant and subsequent calls to``getlogin()`` will overwrite the same buffer.

getlogin_r - Reentrant Get User Name
------------------------------------
.. index:: getlogin_r
.. index:: reentrant get user name
.. index:: get user name, reentrant

**CALLING SEQUENCE:**

.. code:: c

    int getlogin_r(
    char   \*name,
    size_t  namesize
    );

**STATUS CODES:**

*EINVAL*
    The arguments were invalid.

**DESCRIPTION:**

This is a reentrant version of the ``getlogin()`` service.  The
caller specified their own buffer, ``name``, as well as the
length of this buffer, ``namesize``.

**NOTES:**

NONE

getpgrp - Get Process Group ID
------------------------------
.. index:: getpgrp
.. index:: get process group id

**CALLING SEQUENCE:**

.. code:: c

    pid_t getpgrp( void );

**STATUS CODES:**

The procress group Id is returned.

**DESCRIPTION:**

This service returns the current progress group Id.

**NOTES:**

This routine is implemented in a somewhat meaningful
way for RTEMS but is truly not functional.

setsid - Create Session and Set Process Group ID
------------------------------------------------
.. index:: setsid
.. index:: create session and set process group id

**CALLING SEQUENCE:**

.. code:: c

    pid_t setsid( void );

**STATUS CODES:**

*EPERM*
    The application does not have permission to create a process group.

**DESCRIPTION:**

This routine always returns ``EPERM`` as RTEMS has no way
to create new processes and thus no way to create a new process
group.

**NOTES:**

NONE

setpgid - Set Process Group ID for Job Control
----------------------------------------------
.. index:: setpgid
.. index:: set process group id for job control

**CALLING SEQUENCE:**

.. code:: c

    int setpgid(
    pid_t pid,
    pid_t pgid
    );

**STATUS CODES:**

*ENOSYS*
    The routine is not implemented.

**DESCRIPTION:**

This service is not implemented for RTEMS as process groups are not
supported.

**NOTES:**

NONE

uname - Get System Name
-----------------------
.. index:: uname
.. index:: get system name

**CALLING SEQUENCE:**

.. code:: c

    int uname(
    struct utsname \*name
    );

**STATUS CODES:**

*EPERM*
    The provided structure pointer is invalid.

**DESCRIPTION:**

This service returns system information to the caller.  It does this
by filling in the ``struct utsname`` format structure for the
caller.

**NOTES:**

The information provided includes the operating system (RTEMS in
all configurations), the node number, the release as the RTEMS
version, and the CPU family and model.  The CPU model name
will indicate the multilib executive variant being used.

times - Get process times
-------------------------
.. index:: times
.. index:: get process times

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/time.h>
    clock_t times(
    struct tms \*ptms
    );

**STATUS CODES:**

This routine returns the number of clock ticks that have elapsed
since the system was initialized (e.g. the application was
started).

**DESCRIPTION:**

``times`` stores the current process times in ``ptms``.  The
format of ``struct tms`` is as defined in``<sys/times.h>``.  RTEMS fills in the field ``tms_utime``
with the number of ticks that the calling thread has executed
and the field ``tms_stime`` with the number of clock ticks
since system boot (also returned).  All other fields in the``ptms`` are left zero.

**NOTES:**

RTEMS has no way to distinguish between user and system time
so this routine returns the most meaningful information
possible.

getenv - Get Environment Variables
----------------------------------
.. index:: getenv
.. index:: get environment variables

**CALLING SEQUENCE:**

.. code:: c

    char \*getenv(
    const char \*name
    );

**STATUS CODES:**

*NULL*
    when no match

*pointer to value*
    when successful

**DESCRIPTION:**

This service searches the set of environment variables for
a string that matches the specified ``name``.  If found,
it returns the associated value.

**NOTES:**

The environment list consists of name value pairs that
are of the form *name = value*.

setenv - Set Environment Variables
----------------------------------
.. index:: setenv
.. index:: set environment variables

**CALLING SEQUENCE:**

.. code:: c

    int setenv(
    const char \*name,
    const char \*value,
    int overwrite
    );

**STATUS CODES:**

Returns 0 if successful and -1 otherwise.

**DESCRIPTION:**

This service adds the variable ``name`` to the environment with``value``.  If ``name`` is not already exist, then it is
created.  If ``name`` exists and ``overwrite`` is zero, then
the previous value is not overwritten.

**NOTES:**

NONE

ctermid - Generate Terminal Pathname
------------------------------------
.. index:: ctermid
.. index:: generate terminal pathname

**CALLING SEQUENCE:**

.. code:: c

    char \*ctermid(
    char \*s
    );

**STATUS CODES:**

Returns a pointer to a string indicating the pathname for the controlling
terminal.

**DESCRIPTION:**

This service returns the name of the terminal device associated with
this process.  If ``s`` is NULL, then a pointer to a static buffer
is returned.  Otherwise, ``s`` is assumed to have a buffer of
sufficient size to contain the name of the controlling terminal.

**NOTES:**

By default on RTEMS systems, the controlling terminal is ``/dev/console``.
Again this implementation is of limited meaning, but it provides
true and useful results which should be sufficient to ease porting
applications from a full POSIX implementation to the reduced
profile supported by RTEMS.

ttyname - Determine Terminal Device Name
----------------------------------------
.. index:: ttyname
.. index:: determine terminal device name

**CALLING SEQUENCE:**

.. code:: c

    char \*ttyname(
    int fd
    );

**STATUS CODES:**

Pointer to a string containing the terminal device name or
NULL is returned on any error.

**DESCRIPTION:**

This service returns a pointer to the pathname of the terminal
device that is open on the file descriptor ``fd``.  If``fd`` is not a valid descriptor for a terminal device,
then NULL is returned.

**NOTES:**

This routine uses a static buffer.

ttyname_r - Reentrant Determine Terminal Device Name
----------------------------------------------------
.. index:: ttyname_r
.. index:: reentrant determine terminal device name

**CALLING SEQUENCE:**

.. code:: c

    int ttyname_r(
    int   fd,
    char \*name,
    int   namesize
    );

**STATUS CODES:**

This routine returns -1 and sets ``errno`` as follows:

*EBADF*
    If not a valid descriptor for a terminal device.

*EINVAL*
    If ``name`` is NULL or ``namesize`` are insufficient.

**DESCRIPTION:**

This service the pathname of the terminal device that is open
on the file descriptor ``fd``.

**NOTES:**

NONE

isatty - Determine if File Descriptor is Terminal
-------------------------------------------------
.. index:: isatty
.. index:: determine if file descriptor is terminal

**CALLING SEQUENCE:**

.. code:: c

    int isatty(
    int fd
    );

**STATUS CODES:**

Returns 1 if ``fd`` is a terminal device and 0 otherwise.

**DESCRIPTION:**

This service returns 1 if ``fd`` is an open file descriptor
connected to a terminal and 0 otherwise.

**NOTES:**

sysconf - Get Configurable System Variables
-------------------------------------------
.. index:: sysconf
.. index:: get configurable system variables

**CALLING SEQUENCE:**

.. code:: c

    long sysconf(
    int name
    );

**STATUS CODES:**

The value returned is the actual value of the system resource.
If the requested configuration name is a feature flag, then
1 is returned if the available and 0 if it is not.  On any
other error condition, -1 is returned.

**DESCRIPTION:**

This service is the mechanism by which an application determines
values for system limits or options at runtime.

**NOTES:**

Much of the information that may be obtained via ``sysconf``
has equivalent macros in ``<unistd.h``.  However, those
macros reflect conservative limits which may have been altered
by application configuration.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Files and Directories Manager
#############################

Introduction
============

The files and directories manager is ...

The directives provided by the files and directories manager are:

- ``opendir`` - Open a Directory

- ``readdir`` - Reads a directory

- ``rewinddir`` - Resets the ``readdir()`` pointer

- ``scandir`` - Scan a directory for matching entries

- ``telldir`` - Return current location in directory stream

- ``closedir`` - Ends directory read operation

- ``getdents`` - Get directory entries

- ``chdir`` - Changes the current working directory

- ``fchdir`` - Changes the current working directory

- ``getcwd`` - Gets current working directory

- ``open`` - Opens a file

- ``creat`` - Create a new file or rewrite an existing one

- ``umask`` - Sets a file creation mask

- ``link`` - Creates a link to a file

- ``symlink`` - Creates a symbolic link to a file

- ``readlink`` - Obtain the name of the link destination

- ``mkdir`` - Makes a directory

- ``mkfifo`` - Makes a FIFO special file

- ``unlink`` - Removes a directory entry

- ``rmdir`` - Delete a directory

- ``rename`` - Renames a file

- ``stat`` - Gets information about a file.

- ``fstat`` - Gets file status

- ``lstat`` - Gets file status

- ``access`` - Check permissions for a file.

- ``chmod`` - Changes file mode

- ``fchmod`` - Changes permissions of a file

- ``chown`` - Changes the owner and/ or group of a file

- ``utime`` - Change access and/or modification times of an inode

- ``ftruncate`` - Truncate a file to a specified length

- ``truncate`` - Truncate a file to a specified length

- ``pathconf`` - Gets configuration values for files

- ``fpathconf`` - Get configuration values for files

- ``mknod`` - Create a directory

Background
==========

Path Name Evaluation
--------------------

A pathname is a string that consists of no more than ``PATH_MAX``
bytes, including the terminating null character. A pathname has an optional
beginning slash, followed by zero or more filenames separated by slashes.
If the pathname refers to a directory, it may also have one or more trailing
slashes. Multiple successive slahes are considered to be the same as
one slash.

POSIX allows a pathname that begins with precisely two successive slashes to be
interpreted in an implementation-defined manner. RTEMS does not currently
recognize this as a special condition. Any number of successive
slashes is treated the same as a single slash. POSIX requires that
an implementation treat more than two leading slashes as a single slash.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the files and directories manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

opendir - Open a Directory
--------------------------
.. index:: opendir
.. index:: open a directory

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <dirent.h>
    int opendir(
    const char \*dirname
    );

**STATUS CODES:**

*EACCES*
    Search permission was denied on a component of the path
    prefix of ``dirname``, or read permission is denied

*EMFILE*
    Too many file descriptors in use by process

*ENFILE*
    Too many files are currently open in the system.

*ENOENT*
    Directory does not exist, or ``name`` is an empty string.

*ENOMEM*
    Insufficient memory to complete the operation.

*ENOTDIR*
    ``name`` is not a directory.

**DESCRIPTION:**

This routine opens a directory stream corresponding to the
directory specified by the ``dirname`` argument. The
directory stream is positioned at the first entry.

**NOTES:**

The routine is implemented in Cygnus newlib.

readdir - Reads a directory
---------------------------
.. index:: readdir
.. index:: reads a directory

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <dirent.h>
    int readdir(
    DIR \*dirp
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

**DESCRIPTION:**

The ``readdir()`` function returns a pointer to a structure ``dirent``
representing the next directory entry from the directory stream pointed to
by ``dirp``. On end-of-file, NULL is returned.

The ``readdir()`` function may (or may not) return entries for . or .. Your
program should tolerate reading dot and dot-dot but not require them.

The data pointed to be ``readdir()`` may be overwritten by another call to``readdir()`` for the same directory stream. It will not be overwritten by
a call for another directory.

**NOTES:**

If ``ptr`` is not a pointer returned by ``malloc()``, ``calloc()``, or``realloc()`` or has been deallocated with ``free()`` or``realloc()``, the results are not portable and are probably disastrous.

The routine is implemented in Cygnus newlib.

rewinddir - Resets the readdir() pointer
----------------------------------------
.. index:: rewinddir
.. index:: resets the readdir() pointer

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <dirent.h>
    void rewinddir(
    DIR \*dirp
    );

**STATUS CODES:**

No value is returned.

**DESCRIPTION:**

The ``rewinddir()`` function resets the position associated with
the directory stream pointed to by ``dirp``. It also causes the
directory stream to refer to the current state of the directory.

**NOTES:**

NONE

If ``dirp`` is not a pointer by ``opendir()``, the results are
undefined.

The routine is implemented in Cygnus newlib.

scandir - Scan a directory for matching entries
-----------------------------------------------
.. index:: scandir
.. index:: scan a directory for matching entries

**CALLING SEQUENCE:**

.. code:: c

    #include <dirent.h>
    int scandir(
    const char       \*dir,
    struct dirent \***namelist,
    int  (\*select)(const struct dirent \*),
    int  (\*compar)(const struct dirent \**, const struct dirent \**)
    );

**STATUS CODES:**

*ENOMEM*
    Insufficient memory to complete the operation.

**DESCRIPTION:**

The ``scandir()`` function scans the directory ``dir``, calling``select()`` on each directory entry. Entries for which ``select()``
returns non-zero are stored in strings allocated via ``malloc()``,
sorted using ``qsort()`` with the comparison function ``compar()``,
and collected in array ``namelist`` which is allocated via ``malloc()``.
If ``select`` is NULL, all entries are selected.

**NOTES:**

The routine is implemented in Cygnus newlib.

telldir - Return current location in directory stream
-----------------------------------------------------
.. index:: telldir
.. index:: return current location in directory stream

**CALLING SEQUENCE:**

.. code:: c

    #include <dirent.h>
    off_t telldir(
    DIR \*dir
    );

**STATUS CODES:**

*EBADF*
    Invalid directory stream descriptor ``dir``.

**DESCRIPTION:**

The ``telldir()`` function returns the current location associated with the
directory stream ``dir``.

**NOTES:**

The routine is implemented in Cygnus newlib.

closedir - Ends directory read operation
----------------------------------------
.. index:: closedir
.. index:: ends directory read operation

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <dirent.h>
    int closedir(
    DIR \*dirp
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

**DESCRIPTION:**

The directory stream associated with ``dirp`` is closed.
The value in ``dirp`` may not be usable after a call to``closedir()``.

**NOTES:**

NONE

The argument to ``closedir()`` must be a pointer returned by``opendir()``. If it is not, the results are not portable and
most likely unpleasant.

The routine is implemented in Cygnus newlib.

chdir - Changes the current working directory
---------------------------------------------
.. index:: chdir
.. index:: changes the current working directory

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int chdir(
    const char \*path
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of
the following:

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is
    in effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the specified pathname was not a directory when directory
    was expected.

**DESCRIPTION:**

The ``chdir()`` function causes the directory named by ``path`` to
become the current working directory; that is, the starting point for
searches of pathnames not beginning with a slash.

If ``chdir()`` detects an error, the current working directory is not
changed.

**NOTES:**

NONE

fchdir - Changes the current working directory
----------------------------------------------
.. index:: fchdir
.. index:: changes the current working directory

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int fchdir(
    int fd
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of
the following:

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is
    in effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the specified pathname was not a directory when directory
    was expected.

**DESCRIPTION:**

The ``fchdir()`` function causes the directory named by ``fd`` to
become the current working directory; that is, the starting point for
searches of pathnames not beginning with a slash.

If ``fchdir()`` detects an error, the current working directory is not
changed.

**NOTES:**

NONE

getcwd - Gets current working directory
---------------------------------------
.. index:: getcwd
.. index:: gets current working directory

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int getcwd( void );

**STATUS CODES:**

*EINVAL*
    Invalid argument

*ERANGE*
    Result is too large

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

**DESCRIPTION:**

The ``getcwd()`` function copies the absolute pathname of the current
working directory to the character array pointed to by ``buf``. The``size`` argument is the number of bytes available in ``buf``

**NOTES:**

There is no way to determine the maximum string length that ``fetcwd()``
may need to return. Applications should tolerate getting ``ERANGE``
and allocate a larger buffer.

It is possible for ``getcwd()`` to return EACCES if, say, ``login``
puts the process into a directory without read access.

The 1988 standard uses ``int`` instead of ``size_t`` for the second
parameter.

open - Opens a file
-------------------
.. index:: open
.. index:: opens a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>
    int open(
    const char \*path,
    int         oflag,
    mode_t      mode
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

*EEXIST*
    The named file already exists.

*EINTR*
    Function was interrupted by a signal.

*EISDIR*
    Attempt to open a directory for writing or to rename a file to be a
    directory.

*EMFILE*
    Too many file descriptors are in use by this process.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENFILE*
    Too many files are currently open in the system.

*ENOENT*
    A file or directory does not exist.

*ENOSPC*
    No space left on disk.

*ENOTDIR*
    A component of the specified pathname was not a directory when a directory
    was expected.

*ENXIO*
    No such device. This error may also occur when a device is not ready, for
    example, a tape drive is off-line.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

The ``open`` function establishes a connection between a file and a file
descriptor. The file descriptor is a small integer that is used by I/O
functions to reference the file. The ``path`` argument points to the
pathname for the file.

The ``oflag`` argument is the bitwise inclusive OR of the values of
symbolic constants. The programmer must specify exactly one of the following
three symbols:

*O_RDONLY*
    Open for reading only.

*O_WRONLY*
    Open for writing only.

*O_RDWR*
    Open for reading and writing.

Any combination of the following symbols may also be used.

*O_APPEND*
    Set the file offset to the end-of-file prior to each write.

*O_CREAT*
    If the file does not exist, allow it to be created. This flag indicates
    that the ``mode`` argument is present in the call to ``open``.

*O_EXCL*
    This flag may be used only if O_CREAT is also set. It causes the call
    to ``open`` to fail if the file already exists.

*O_NOCTTY*
    If ``path`` identifies a terminal, this flag prevents that teminal from
    becoming the controlling terminal for thi9s process. See Chapter 8 for a
    description of terminal I/O.

*O_NONBLOCK*
    Do no wait for the device or file to be ready or available. After the file
    is open, the ``read`` and ``write`` calls return immediately. If the
    process would be delayed in the read or write opermation, -1 is returned and``errno`` is set to ``EAGAIN`` instead of blocking the caller.

*O_TRUNC*
    This flag should be used only on ordinary files opened for writing. It
    causes the file to be tuncated to zero length..

Upon successful completion, ``open`` returns a non-negative file
descriptor.

**NOTES:**

NONE

creat - Create a new file or rewrite an existing one
----------------------------------------------------
.. index:: creat
.. index:: create a new file or rewrite an existing one

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>
    int creat(
    const char \*path,
    mode_t      mode
    );

**STATUS CODES:**

*EEXIST*
    ``path`` already exists and O_CREAT and O_EXCL were used.

*EISDIR*
    ``path`` refers to a directory and the access requested involved
    writing

*ETXTBSY*
    ``path`` refers to an executable image which is currently being
    executed and write access was requested

*EFAULT*
    ``path`` points outside your accessible address space

*EACCES*
    The requested access to the file is not allowed, or one of the
    directories in ``path`` did not allow search (execute) permission.

*ENAMETOOLONG*
    ``path`` was too long.

*ENOENT*
    A directory component in ``path`` does not exist or is a dangling
    symbolic link.

*ENOTDIR*
    A component used as a directory in ``path`` is not, in fact, a
    directory.

*EMFILE*
    The process alreadyh has the maximum number of files open.

*ENFILE*
    The limit on the total number of files open on the system has been
    reached.

*ENOMEM*
    Insufficient kernel memory was available.

*EROFS*
    ``path`` refers to a file on a read-only filesystem and write access
    was requested

**DESCRIPTION:**

``creat`` attempts to create a file and return a file descriptor for
use in read, write, etc.

**NOTES:**

NONE

The routine is implemented in Cygnus newlib.

umask - Sets a file creation mask.
----------------------------------
.. index:: umask
.. index:: sets a file creation mask.

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    mode_t umask(
    mode_t cmask
    );

**STATUS CODES:**

**DESCRIPTION:**

The ``umask()`` function sets the process file creation mask to ``cmask``.
The file creation mask is used during ``open()``, ``creat()``, ``mkdir()``,``mkfifo()`` calls to turn off permission bits in the ``mode`` argument.
Bit positions that are set in ``cmask`` are cleared in the mode of the
created file.

**NOTES:**

NONE

The ``cmask`` argument should have only permission bits set. All other
bits should be zero.

In a system which supports multiple processes, the file creation mask is inherited
across ``fork()`` and ``exec()`` calls. This makes it possible to alter the
default permission bits of created files. RTEMS does not support multiple processes
so this behavior is not possible.

link - Creates a link to a file
-------------------------------
.. index:: link
.. index:: creates a link to a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int link(
    const char \*existing,
    const char \*new
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*EEXIST*
    The named file already exists.

*EMLINK*
    The number of links would exceed ``LINK_MAX``.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOSPC*
    No space left on disk.

*ENOTDIR*
    A component of the specified pathname was not a directory when a directory
    was expected.

*EPERM*
    Operation is not permitted. Process does not have the appropriate priviledges
    or permissions to perform the requested operations.

*EROFS*
    Read-only file system.

*EXDEV*
    Attempt to link a file to another file system.

**DESCRIPTION:**

The ``link()`` function atomically creates a new link for an existing file
and increments the link count for the file.

If the ``link()`` function fails, no directories are modified.

The ``existing`` argument should not be a directory.

The caller may (or may not) need permission to access the existing file.

**NOTES:**

NONE

symlink - Creates a symbolic link to a file
-------------------------------------------
.. index:: symlink
.. index:: creates a symbolic link to a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int symlink(
    const char \*topath,
    const char \*frompath
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*EEXIST*
    The named file already exists.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOSPC*
    No space left on disk.

*ENOTDIR*
    A component of the specified pathname was not a directory when a directory
    was expected.

*EPERM*
    Operation is not permitted. Process does not have the appropriate priviledges
    or permissions to perform the requested operations.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

The ``symlink()`` function creates a symbolic link from the frombath to the
topath. The symbolic link will be interpreted at run-time.

If the ``symlink()`` function fails, no directories are modified.

The caller may (or may not) need permission to access the existing file.

**NOTES:**

NONE

readlink - Obtain the name of a symbolic link destination
---------------------------------------------------------
.. index:: readlink
.. index:: obtain the name of a symbolic link destination

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int readlink(
    const char \*path,
    char       \*buf,
    size_t      bufsize
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the prefix pathname was not a directory when a directory
    was expected.

*ELOOP*
    Too many symbolic links were encountered in the pathname.

*EINVAL*
    The pathname does not refer to a symbolic link

*EFAULT*
    An invalid pointer was passed into the ``readlink()`` routine.

**DESCRIPTION:**

The ``readlink()`` function places the symbolic link destination into``buf`` argument and returns the number of characters copied.

If the symbolic link destination is longer than bufsize characters the
name will be truncated.

**NOTES:**

NONE

mkdir - Makes a directory
-------------------------
.. index:: mkdir
.. index:: makes a directory

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int mkdir(
    const char \*path,
    mode_t      mode
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*EEXIST*
    The name file already exist.

*EMLINK*
    The number of links would exceed LINK_MAX

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOSPC*
    No space left on disk.

*ENOTDIR*
    A component of the specified pathname was not a directory when a directory
    was expected.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

The ``mkdir()`` function creates a new diectory named ``path``. The
permission bits (modified by the file creation mask) are set from ``mode``.
The owner and group IDs for the directory are set from the effective user ID
and group ID.

The new directory may (or may not) contain entries for.. and .. but is otherwise
empty.

**NOTES:**

NONE

mkfifo - Makes a FIFO special file
----------------------------------
.. index:: mkfifo
.. index:: makes a fifo special file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int mkfifo(
    const char \*path,
    mode_t      mode
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*EEXIST*
    The named file already exists.

*ENOENT*
    A file or directory does not exist.

*ENOSPC*
    No space left on disk.

*ENOTDIR*
    A component of the specified ``path`` was not a directory when a directory
    was expected.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

The ``mkfifo()`` function creates a new FIFO special file named ``path``.
The permission bits (modified by the file creation mask) are set from``mode``. The owner and group IDs for the FIFO are set from the efective
user ID and group ID.

**NOTES:**

NONE

unlink - Removes a directory entry
----------------------------------
.. index:: unlink
.. index:: removes a directory entry

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int unlink(
    const char path
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*EBUSY*
    The directory is in use.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the specified ``path`` was not a directory when a directory
    was expected.

*EPERM*
    Operation is not permitted. Process does not have the appropriate priviledges
    or permissions to perform the requested operations.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

The ``unlink`` function removes the link named by ``path`` and decrements the
link count of the file referenced by the link. When the link count goes to zero
and no process has the file open, the space occupied by the file is freed and the
file is no longer accessible.

**NOTES:**

NONE

rmdir - Delete a directory
--------------------------
.. index:: rmdir
.. index:: delete a directory

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int rmdir(
    const char \*pathname
    );

**STATUS CODES:**

*EPERM*
    The filesystem containing ``pathname`` does not support the removal
    of directories.

*EFAULT*
    ``pathname`` points ouside your accessible address space.

*EACCES*
    Write access to the directory containing ``pathname`` was not
    allowed for the process’s effective uid, or one of the directories in``pathname`` did not allow search (execute) permission.

*EPERM*
    The directory containing ``pathname`` has the stickybit (S_ISVTX)
    set and the process’s effective uid is neither the uid of the file to
    be delected nor that of the director containing it.

*ENAMETOOLONG*
    ``pathname`` was too long.

*ENOENT*
    A dirctory component in ``pathname`` does not exist or is a
    dangling symbolic link.

*ENOTDIR*
    ``pathname``, or a component used as a directory in ``pathname``,
    is not, in fact, a directory.

*ENOTEMPTY*
    ``pathname`` contains entries other than . and .. .

*EBUSY*
    ``pathname`` is the current working directory or root directory of
    some process

*EBUSY*
    ``pathname`` is the current directory or root directory of some
    process.

*ENOMEM*
    Insufficient kernel memory was available

*EROGS*
    ``pathname`` refers to a file on a read-only filesystem.

*ELOOP*
    ``pathname`` contains a reference to a circular symbolic link

**DESCRIPTION:**

``rmdir`` deletes a directory, which must be empty

**NOTES:**

NONE

rename - Renames a file
-----------------------
.. index:: rename
.. index:: renames a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int rename(
    const char \*old,
    const char \*new
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

*EBUSY*
    The directory is in use.

*EEXIST*
    The named file already exists.

*EINVAL*
    Invalid argument.

*EISDIR*
    Attempt to open a directory for writing or to rename a file to be a
    directory.

*EMLINK*
    The number of links would exceed LINK_MAX.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is
    in effect.

*ENOENT*
    A file or directory does no exist.

*ENOSPC*
    No space left on disk.

*ENOTDIR*
    A component of the specified pathname was not a directory when a
    directory was expected.

*ENOTEMPTY*
    Attempt to delete or rename a non-empty directory.

*EROFS*
    Read-only file system

*EXDEV*
    Attempt to link a file to another file system.

**DESCRIPTION:**

The ``rename()`` function causes the file known bo ``old`` to
now be known as ``new``.

Ordinary files may be renamed to ordinary files, and directories may be
renamed to directories; however, files cannot be converted using``rename()``. The ``new`` pathname may not contain a path prefix
of ``old``.

**NOTES:**

If a file already exists by the name ``new``, it is removed. The``rename()`` function is atomic. If the ``rename()`` detects an
error, no files are removed. This guarantees that the``rename("x", "x")`` does not remove ``x``.

You may not rename dot or dot-dot.

The routine is implemented in Cygnus newlib using ``link()`` and``unlink()``.

stat - Gets information about a file
------------------------------------
.. index:: stat
.. index:: gets information about a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int stat(
    const char  \*path,
    struct stat \*buf
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

*EBADF*
    Invalid file descriptor.

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is
    in effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the specified pathname was not a directory when a
    directory was expected.

**DESCRIPTION:**

The ``path`` argument points to a pathname for a file. Read, write, or
execute permission for the file is not required, but all directories listed
in ``path`` must be searchable. The ``stat()`` function obtains
information about the named file and writes it to the area pointed to by``buf``.

**NOTES:**

NONE

fstat - Gets file status
------------------------
.. index:: fstat
.. index:: gets file status

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int fstat(
    int          fildes,
    struct stat \*buf
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

**DESCRIPTION:**

The ``fstat()`` function obtains information about the file
associated with ``fildes`` and writes it to the area pointed
to by the ``buf`` argument.

**NOTES:**

If the filesystem object referred to by ``fildes`` is a
link, then the information returned in ``buf`` refers
to the destination of that link.  This is in contrast to``lstat()`` which does not follow the link.

lstat - Gets file status
------------------------
.. index:: lstat
.. index:: gets file status

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int lstat(
    int          fildes,
    struct stat \*buf
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

**DESCRIPTION:**

The ``lstat()`` function obtains information about the file
associated with ``fildes`` and writes it to the area pointed
to by the ``buf`` argument.

**NOTES:**

If the filesystem object referred to by ``fildes`` is a
link, then the information returned in ``buf`` refers
to the link itself.  This is in contrast to ``fstat()``
which follows the link.

The ``lstat()`` routine is defined by BSD 4.3 and SVR4
and not included in POSIX 1003.1b-1996.

access - Check permissions for a file
-------------------------------------
.. index:: access
.. index:: check permissions for a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int access(
    const char \*pathname,
    int         mode
    );

**STATUS CODES:**

*EACCES*
    The requested access would be denied, either to the file itself or
    one of the directories in ``pathname``.

*EFAULT*
    ``pathname`` points outside your accessible address space.

*EINVAL*
    ``Mode`` was incorrectly specified.

*ENAMETOOLONG*
    ``pathname`` is too long.

*ENOENT*
    A directory component in ``pathname`` would have been accessible but
    does not exist or was a dangling symbolic link.

*ENOTDIR*
    A component used as a directory in ``pathname`` is not, in fact,
    a directory.

*ENOMEM*
    Insufficient kernel memory was available.

**DESCRIPTION:**

``Access`` checks whether the process would be allowed to read, write or
test for existence of the file (or other file system object) whose name is``pathname``. If ``pathname`` is a symbolic link permissions of the
file referred by this symbolic link are tested.

``Mode`` is a mask consisting of one or more of R_OK, W_OK, X_OK and F_OK.

**NOTES:**

NONE

chmod - Changes file mode.
--------------------------
.. index:: chmod
.. index:: changes file mode.

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int chmod(
    const char \*path,
    mode_t      mode
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the specified pathname was not a directory when a directory
    was expected.

*EPERM*
    Operation is not permitted. Process does not have the appropriate priviledges
    or permissions to perform the requested operations.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

Set the file permission bits, the set user ID bit, and the set group ID bit
for the file named by ``path`` to ``mode``. If the effective user ID
does not match the owner of the file and the calling process does not have
the appropriate privileges, ``chmod()`` returns -1 and sets ``errno`` to``EPERM``.

**NOTES:**

NONE

fchmod - Changes permissions of a file
--------------------------------------
.. index:: fchmod
.. index:: changes permissions of a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <sys/stat.h>
    int fchmod(
    int    fildes,
    mode_t mode
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix.

*EBADF*
    The descriptor is not valid.

*EFAULT*
    ``path`` points outside your accessible address space.

*EIO*
    A low-level I/o error occurred while modifying the inode.

*ELOOP*
    ``path`` contains a circular reference

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is
    in effect.

*ENOENT*
    A file or directory does no exist.

*ENOMEM*
    Insufficient kernel memory was avaliable.

*ENOTDIR*
    A component of the specified pathname was not a directory when a
    directory was expected.

*EPERM*
    The effective UID does not match the owner of the file, and is not
    zero

*EROFS*
    Read-only file system

**DESCRIPTION:**

The mode of the file given by ``path`` or referenced by``filedes`` is changed.

**NOTES:**

NONE

getdents - Get directory entries
--------------------------------
.. index:: getdents
.. index:: get directory entries

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    #include <linux/dirent.h>
    #include <linux/unistd.h>
    long getdents(
    int   dd_fd,
    char \*dd_buf,
    int   dd_len
    );

**STATUS CODES:**

A successful call to ``getdents`` returns th the number of bytes read.
On end of directory, 0 is returned. When an error occurs, -1 is returned,
and ``errno`` is set appropriately.

*EBADF*
    Invalid file descriptor ``fd``.

*EFAULT*
    Argument points outside the calling process’s address space.

*EINVAL*
    Result buffer is too small.

*ENOENT*
    No such directory.

*ENOTDIR*
    File descriptor does not refer to a directory.

**DESCRIPTION:**

``getdents`` reads several ``dirent`` structures from the directory
pointed by ``fd`` into the memory area pointed to by ``dirp``. The
parameter ``count`` is the size of the memory area.

**NOTES:**

NONE

chown - Changes the owner and/or group of a file.
-------------------------------------------------
.. index:: chown
.. index:: changes the owner and/or group of a file.

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <unistd.h>
    int chown(
    const char \*path,
    uid_t       owner,
    gid_t       group
    );

**STATUS CODES:**

*EACCES*
    Search permission is denied for a directory in a file’s path prefix

*EINVAL*
    Invalid argument

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC is in
    effect.

*ENOENT*
    A file or directory does not exist.

*ENOTDIR*
    A component of the specified pathname was not a directory when a directory
    was expected.

*EPERM*
    Operation is not permitted. Process does not have the appropriate priviledges
    or permissions to perform the requested operations.

*EROFS*
    Read-only file system.

**DESCRIPTION:**

The user ID and group ID of the file named by ``path`` are set to``owner`` and ``path``, respectively.

For regular files, the set group ID (S_ISGID) and set user ID (S_ISUID)
bits are cleared.

Some systems consider it a security violation to allow the owner of a file to
be changed, If users are billed for disk space usage, loaning a file to
another user could result in incorrect billing. The ``chown()`` function
may be restricted to privileged users for some or all files. The group ID can
still be changed to one of the supplementary group IDs.

**NOTES:**

This function may be restricted for some file. The ``pathconf`` function
can be used to test the ``_PC_CHOWN_RESTRICTED`` flag.

utime - Change access and/or modification times of an inode
-----------------------------------------------------------
.. index:: utime
.. index:: change access and/or modification times of an inode

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    int utime(
    const char     \*filename,
    struct utimbuf \*buf
    );

**STATUS CODES:**

*EACCES*
    Permission to write the file is denied

*ENOENT*
    ``Filename`` does not exist

**DESCRIPTION:**

``Utime`` changes the access and modification times of the inode
specified by ``filename`` to the ``actime`` and ``modtime``
fields of ``buf`` respectively. If ``buf`` is NULL, then the
access and modification times of the file are set to the current time.

**NOTES:**

NONE

ftruncate - truncate a file to a specified length
-------------------------------------------------
.. index:: ftruncate
.. index:: truncate a file to a specified length

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int ftrunctate(
    int    fd,
    size_t length
    );

**STATUS CODES:**

*ENOTDIR*
    A component of the path prefix is not a directory.

*EINVAL*
    The pathname contains a character with the high-order bit set.

*ENAMETOOLONG*
    A component of a pathname exceeded 255 characters, or an entire
    path name exceeded 1023 characters.

*ENOENT*
    The named file does not exist.

*EACCES*
    The named file is not writable by the user.

*EACCES*
    Search permission is denied for a component of the path prefix.

*ELOOP*
    Too many symbolic links were encountered in translating the
    pathname

*EISDIR*
    The named file is a directory.

*EROFS*
    The named file resides on a read-only file system

*ETXTBSY*
    The file is a pure procedure (shared text) file that is being
    executed

*EIO*
    An I/O error occurred updating the inode.

*EFAULT*
    ``Path`` points outside the process’s allocated address space.

*EBADF*
    The ``fd`` is not a valid descriptor.

**DESCRIPTION:**

``truncate()`` causes the file named by ``path`` or referenced by``fd`` to be truncated to at most ``length`` bytes in size. If the
file previously was larger than this size, the extra data is lost. With``ftruncate()``, the file must be open for writing.

**NOTES:**

NONE

truncate - truncate a file to a specified length
------------------------------------------------
.. index:: truncate
.. index:: truncate a file to a specified length

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int trunctate(
    const char \*path,
    size_t      length
    );

**STATUS CODES:**

*ENOTDIR*
    A component of the path prefix is not a directory.

*EINVAL*
    The pathname contains a character with the high-order bit set.

*ENAMETOOLONG*
    A component of a pathname exceeded 255 characters, or an entire
    path name exceeded 1023 characters.

*ENOENT*
    The named file does not exist.

*EACCES*
    The named file is not writable by the user.

*EACCES*
    Search permission is denied for a component of the path prefix.

*ELOOP*
    Too many symbolic links were encountered in translating the
    pathname

*EISDIR*
    The named file is a directory.

*EROFS*
    The named file resides on a read-only file system

*ETXTBSY*
    The file is a pure procedure (shared text) file that is being
    executed

*EIO*
    An I/O error occurred updating the inode.

*EFAULT*
    ``Path`` points outside the process’s allocated address space.

*EBADF*
    The ``fd`` is not a valid descriptor.

**DESCRIPTION:**

``truncate()`` causes the file named by ``path`` or referenced by``fd`` to be truncated to at most ``length`` bytes in size. If the
file previously was larger than this size, the extra data is lost. With``ftruncate()``, the file must be open for writing.

**NOTES:**

NONE

pathconf - Gets configuration values for files
----------------------------------------------
.. index:: pathconf
.. index:: gets configuration values for files

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int pathconf(
    const char \*path,
    int         name
    );

**STATUS CODES:**

*EINVAL*
    Invalid argument

*EACCES*
    Permission to write the file is denied

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC
    is in effect.

*ENOENT*
    A file or directory does not exist

*ENOTDIR*
    A component of the specified ``path`` was not a directory whan a
    directory was expected.

**DESCRIPTION:**

``pathconf()`` gets a value for the configuration option ``name``
for the open file descriptor ``filedes``.

The possible values for ``name`` are:

*_PC_LINK_MAX*
    returns the maximum number of links to the file. If ``filedes`` or``path`` refer to a directory, then the value applies to the whole
    directory. The corresponding macro is ``_POSIX_LINK_MAX``.

*_PC_MAX_CANON*
    returns the maximum length of a formatted input line, where ``filedes``
    or ``path`` must refer to a terminal. The corresponding macro is``_POSIX_MAX_CANON``.

*_PC_MAX_INPUT*
    returns the maximum length of an input line, where ``filedes`` or``path`` must refer to a terminal. The corresponding macro is``_POSIX_MAX_INPUT``.

*_PC_NAME_MAX*
    returns the maximum length of a filename in the directory ``path`` or``filedes``. The process is allowed to create. The corresponding macro
    is ``_POSIX_NAME_MAX``.

*_PC_PATH_MAX*
    returns the maximum length of a relative pathname when ``path`` or``filedes`` is the current working directory. The corresponding macro
    is ``_POSIX_PATH_MAX``.

*_PC_PIPE_BUF*
    returns the size of the pipe buffer, where ``filedes`` must refer to a
    pipe or FIFO and ``path`` must refer to a FIFO. The corresponding macro
    is ``_POSIX_PIPE_BUF``.

*_PC_CHOWN_RESTRICTED*
    returns nonzero if the chown(2) call may not be used on this file. If``filedes`` or ``path`` refer to a directory, then this applies to all
    files in that directory. The corresponding macro is``_POSIX_CHOWN_RESTRICTED``.

**NOTES:**

Files with name lengths longer than the value returned for ``name`` equal``_PC_NAME_MAX`` may exist in the given directory.

fpathconf - Gets configuration values for files
-----------------------------------------------
.. index:: fpathconf
.. index:: gets configuration values for files

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int fpathconf(
    int filedes,
    int name
    );

**STATUS CODES:**

*EINVAL*
    Invalid argument

*EACCES*
    Permission to write the file is denied

*ENAMETOOLONG*
    Length of a filename string exceeds PATH_MAX and _POSIX_NO_TRUNC
    is in effect.

*ENOENT*
    A file or directory does not exist

*ENOTDIR*
    A component of the specified ``path`` was not a directory whan a
    directory was expected.

**DESCRIPTION:**

``pathconf()`` gets a value for the configuration option ``name``
for the open file descriptor ``filedes``.

The possible values for name are:

*_PC_LINK_MAX*
    returns the maximum number of links to the file. If ``filedes`` or``path`` refer to a directory, then the value applies to the whole
    directory. The corresponding macro is _POSIX_LINK_MAX.

*_PC_MAX_CANON*
    returns the maximum length of a formatted input line, where ``filedes``
    or ``path`` must refer to a terminal. The corresponding macro is``_POSIX_MAX_CANON``.

*_PC_MAX_INPUT*
    returns the maximum length of an input line, where ``filedes`` or``path`` must refer to a terminal. The corresponding macro is``_POSIX_MAX_INPUT``.

*_PC_NAME_MAX*
    returns the maximum length of a filename in the directory ``path`` or``filedes``. The process is allowed to create. The corresponding macro
    is ``_POSIX_NAME_MAX``.

*_PC_PATH_MAX*
    returns the maximum length of a relative pathname when ``path`` or``filedes`` is the current working directory. The corresponding macro
    is ``_POSIX_PATH_MAX``.

*_PC_PIPE_BUF*
    returns the size of the pipe buffer, where ``filedes`` must refer to a
    pipe or FIFO and ``path`` must refer to a FIFO. The corresponding macro
    is ``_POSIX_PIPE_BUF``.

*_PC_CHOWN_RESTRICTED*
    returns nonzero if the ``chown()`` call may not be used on this file. If``filedes`` or ``path`` refer to a directory, then this applies to all
    files in that directory. The corresponding macro is``_POSIX_CHOWN_RESTRICTED``.

**NOTES:**

NONE

mknod - create a directory
--------------------------
.. index:: mknod
.. index:: create a directory

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    #include <fcntl.h>
    #include <sys/types.h>
    #include <sys/stat.h>
    long mknod(
    const char \*pathname,
    mode_t      mode,
    dev_t       dev
    );

**STATUS CODES:**

``mknod`` returns zero on success, or -1 if an error occurred (in which case,
errno is set appropriately).

*ENAMETOOLONG*
    ``pathname`` was too long.

*ENOENT*
    A directory component in ``pathname`` does not exist or is a dangling symbolic
    link.

*ENOTDIR*
    A component used in the directory ``pathname`` is not, in fact, a directory.

*ENOMEM*
    Insufficient kernel memory was available

*EROFS*
    ``pathname`` refers to a file on a read-only filesystem.

*ELOOP*
    ``pathname`` contains a reference to a circular symbolic link, ie a symbolic
    link whose expansion contains a reference to itself.

*ENOSPC*
    The device containing ``pathname`` has no room for the new node.

**DESCRIPTION:**

``mknod`` attempts to create a filesystem node (file, device special file or
named pipe) named ``pathname``, specified by ``mode`` and ``dev``.

``mode`` specifies both the permissions to use and the type of node to be created.

It should be a combination (using bitwise OR) of one of the file types listed
below and the permissions for the new node.

The permissions are modified by the process’s ``umask`` in the usual way: the
permissions of the created node are ``(mode & ~umask)``.

The file type should be one of ``S_IFREG``, ``S_IFCHR``, ``S_IFBLK`` and``S_IFIFO`` to specify a normal file (which will be created empty), character
special file, block special file or FIFO (named pipe), respectively, or zero, which
will create a normal file.

If the file type is ``S_IFCHR`` or ``S_IFBLK`` then ``dev`` specifies the major
and minor numbers of the newly created device special file; otherwise it is ignored.

The newly created node will be owned by the effective uid of the process. If the
directory containing the node has the set group id bit set, or if the filesystem
is mounted with BSD group semantics, the new node will inherit the group ownership
from its parent directory; otherwise it will be owned by the effective gid of the
process.

**NOTES:**

NONE

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Input and Output Primitives Manager
###################################

Introduction
============

The input and output primitives manager is ...

The directives provided by the input and output primitives manager are:

- ``pipe`` - Create an Inter-Process Channel

- ``dup`` - Duplicates an open file descriptor

- ``dup2`` - Duplicates an open file descriptor

- ``close`` - Closes a file

- ``read`` - Reads from a file

- ``write`` - Writes to a file

- ``fcntl`` - Manipulates an open file descriptor

- ``lseek`` - Reposition read/write file offset

- ``fsync`` - Synchronize file complete in-core state with that on disk

- ``fdatasync`` - Synchronize file in-core data with that on disk

- ``sync`` - Schedule file system updates

- ``mount`` - Mount a file system

- ``unmount`` - Unmount file systems

- ``readv`` - Vectored read from a file

- ``writev`` - Vectored write to a file

- ``aio_read`` - Asynchronous Read

- ``aio_write`` - Asynchronous Write

- ``lio_listio`` - List Directed I/O

- ``aio_error`` - Retrieve Error Status of Asynchronous I/O Operation

- ``aio_return`` - Retrieve Return Status Asynchronous I/O Operation

- ``aio_cancel`` - Cancel Asynchronous I/O Request

- ``aio_suspend`` - Wait for Asynchronous I/O Request

- ``aio_fsync`` - Asynchronous File Synchronization

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the input and output primitives manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

pipe - Create an Inter-Process Channel
--------------------------------------
.. index:: pipe
.. index:: create an inter

**CALLING SEQUENCE:**

.. code:: c

    int pipe(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

dup - Duplicates an open file descriptor
----------------------------------------
.. index:: dup
.. index:: duplicates an open file descriptor

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int dup(
    int fildes
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor.

*EINTR*
    Function was interrupted by a signal.

*EMFILE*
    The process already has the maximum number of file descriptors open
    and tried to open a new one.

**DESCRIPTION:**

The ``dup`` function returns the lowest numbered available file
descriptor. This new desciptor refers to the same open file as the
original descriptor and shares any locks.

**NOTES:**

NONE

dup2 - Duplicates an open file descriptor
-----------------------------------------
.. index:: dup2
.. index:: duplicates an open file descriptor

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int dup2(
    int fildes,
    int fildes2
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor.

*EINTR*
    Function was interrupted by a signal.

*EMFILE*
    The process already has the maximum number of file descriptors open
    and tried to open a new one.

**DESCRIPTION:**

``dup2`` creates a copy of the file descriptor ``oldfd``.

The old and new descriptors may be used interchangeably. They share locks, file
position pointers and flags; for example, if the file position is modified by using``lseek`` on one of the descriptors, the position is also changed for the other.

**NOTES:**

NONE

close - Closes a file
---------------------
.. index:: close
.. index:: closes a file.

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int close(
    int fildes
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

*EINTR*
    Function was interrupted by a signal.

**DESCRIPTION:**

The ``close()`` function deallocates the file descriptor named by``fildes`` and makes it available for reuse. All outstanding
record locks owned by this process for the file are unlocked.

**NOTES:**

A signal can interrupt the ``close()`` function. In that case,``close()`` returns -1 with ``errno`` set to EINTR. The file
may or may not be closed.

read - Reads from a file
------------------------
.. index:: read
.. index:: reads from a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int read(
    int           fildes,
    void         \*buf,
    unsigned int  nbyte
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of
the following:

*EAGAIN*
    The O_NONBLOCK flag is set for a file descriptor and the process
    would be delayed in the I/O operation.

*EBADF*
    Invalid file descriptor

*EINTR*
    Function was interrupted by a signal.

*EIO*
    Input or output error

*EINVAL*
    Bad buffer pointer

**DESCRIPTION:**

The ``read()`` function reads ``nbyte`` bytes from the file
associated with ``fildes`` into the buffer pointed to by ``buf``.

The ``read()`` function returns the number of bytes actually read
and placed in the buffer. This will be less than ``nbyte`` if:

- The number of bytes left in the file is less than ``nbyte``.

- The ``read()`` request was interrupted by a signal.

- The file is a pipe or FIFO or special file with less than ``nbytes``
  immediately available for reading.

When attempting to read from any empty pipe or FIFO:

- If no process has the pipe open for writing, zero is returned to
  indicate end-of-file.

- If some process has the pipe open for writing and O_NONBLOCK is set,
  -1 is returned and ``errno`` is set to EAGAIN.

- If some process has the pipe open for writing and O_NONBLOCK is clear,``read()`` waits for some data to be written or the pipe to be closed.

When attempting to read from a file other than a pipe or FIFO and no data
is available.

- If O_NONBLOCK is set, -1 is returned and ``errno`` is set to EAGAIN.

- If O_NONBLOCK is clear, ``read()`` waits for some data to become
  available.

- The O_NONBLOCK flag is ignored if data is available.

**NOTES:**

NONE

write - Writes to a file
------------------------
.. index:: write
.. index:: writes to a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int write(
    int           fildes,
    const void   \*buf,
    unsigned int  nbytes
    );

**STATUS CODES:**

*EAGAIN*
    The O_NONBLOCK flag is set for a file descriptor and the process
    would be delayed in the I/O operation.

*EBADF*
    Invalid file descriptor

*EFBIG*
    An attempt was made to write to a file that exceeds the maximum file
    size

*EINTR*
    The function was interrupted by a signal.

*EIO*
    Input or output error.

*ENOSPC*
    No space left on disk.

*EPIPE*
    Attempt to write to a pope or FIFO with no reader.

*EINVAL*
    Bad buffer pointer

**DESCRIPTION:**

The ``write()`` function writes ``nbyte`` from the array pointed
to by ``buf`` into the file associated with ``fildes``.

If ``nybte`` is zero and the file is a regular file, the ``write()``
function returns zero and has no other effect. If ``nbyte`` is zero
and the file is a special file, te results are not portable.

The ``write()`` function returns the number of bytes written. This
number will be less than ``nbytes`` if there is an error. It will never
be greater than ``nbytes``.

**NOTES:**

NONE

fcntl - Manipulates an open file descriptor
-------------------------------------------
.. index:: fcntl
.. index:: manipulates an open file descriptor

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <fcntl.h>
    #include <unistd.h>
    int fcntl(
    int fildes,
    int cmd
    );

**STATUS CODES:**

*EACCESS*
    Search permission is denied for a direcotry in a file’s path
    prefix.

*EAGAIN*
    The O_NONBLOCK flag is set for a file descriptor and the process
    would be delayed in the I/O operation.

*EBADF*
    Invalid file descriptor

*EDEADLK*
    An ``fcntl`` with function F_SETLKW would cause a deadlock.

*EINTR*
    The functioin was interrupted by a signal.

*EINVAL*
    Invalid argument

*EMFILE*
    Too many file descriptor or in use by the process.

*ENOLCK*
    No locks available

**DESCRIPTION:**

``fcntl()`` performs one of various miscellaneous operations on``fd``. The operation in question is determined by ``cmd``:

*F_DUPFD*
    Makes ``arg`` be a copy of ``fd``, closing ``fd`` first if necessary.
    The same functionality can be more easily achieved by using ``dup2()``.
    The old and new descriptors may be used interchangeably. They share locks,
    file position pointers and flags; for example, if the file position is
    modified by using ``lseek()`` on one of the descriptors, the position is
    also changed for the other.
    The two descriptors do not share the close-on-exec flag, however. The
    close-on-exec flag of the copy is off, meaning that it will be closed on
    exec.
    On success, the new descriptor is returned.

*F_GETFD*
    Read the close-on-exec flag. If the low-order bit is 0, the file will
    remain open across exec, otherwise it will be closed.

*F_SETFD*
    Set the close-on-exec flag to the value specified by ``arg`` (only the least
    significant bit is used).

*F_GETFL*
    Read the descriptor’s flags (all flags (as set by open()) are returned).

*F_SETFL*
    Set the descriptor’s flags to the value specified by ``arg``. Only``O_APPEND`` and ``O_NONBLOCK`` may be set.
    The flags are shared between copies (made with ``dup()`` etc.) of the same
    file descriptor.
    The flags and their semantics are described in ``open()``.

*F_GETLK, F_SETLK and F_SETLKW*
    Manage discretionary file locks. The third argument ``arg`` is a pointer to a
    struct flock (that may be overwritten by this call).

*F_GETLK*
    Return the flock structure that prevents us from obtaining the lock, or set the``l_type`` field of the lock to ``F_UNLCK`` if there is no obstruction.

*F_SETLK*
    The lock is set (when ``l_type`` is ``F_RDLCK`` or ``F_WRLCK``) or
    cleared (when it is ``F_UNLCK``. If lock is held by someone else, this
    call returns -1 and sets ``errno`` to EACCES or EAGAIN.

*F_SETLKW*
    Like ``F_SETLK``, but instead of returning an error we wait for the lock to
    be released.

*F_GETOWN*
    Get the process ID (or process group) of the owner of a socket.
    Process groups are returned as negative values.

*F_SETOWN*
    Set the process or process group that owns a socket.
    For these commands, ownership means receiving ``SIGIO`` or ``SIGURG``
    signals.
    Process groups are specified using negative values.

**NOTES:**

The errors returned by ``dup2`` are different from those returned by``F_DUPFD``.

lseek - Reposition read/write file offset
-----------------------------------------
.. index:: lseek
.. index:: reposition read/write file offset

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <unistd.h>
    int lseek(
    int    fildes,
    off_t  offset,
    int    whence
    );

**STATUS CODES:**

*EBADF*
    ``fildes`` is not an open file descriptor.

*ESPIPE*
    ``fildes`` is associated with a pipe, socket or FIFO.

*EINVAL*
    ``whence`` is not a proper value.

**DESCRIPTION:**

The ``lseek`` function repositions the offset of the file descriptor``fildes`` to the argument offset according to the directive whence.
The argument ``fildes`` must be an open file descriptor. ``Lseek``
repositions the file pointer fildes as follows:

- If ``whence`` is SEEK_SET, the offset is set to ``offset`` bytes.

- If ``whence`` is SEEK_CUR, the offset is set to its current location
  plus offset bytes.

- If ``whence`` is SEEK_END, the offset is set to the size of the
  file plus ``offset`` bytes.

The ``lseek`` function allows the file offset to be set beyond the end
of the existing end-of-file of the file. If data is later written at this
point, subsequent reads of the data in the gap return bytes of zeros
(until data is actually written into the gap).

Some devices are incapable of seeking. The value of the pointer associated
with such a device is undefined.

**NOTES:**

NONE

fsync - Synchronize file complete in-core state with that on disk
-----------------------------------------------------------------
.. index:: fsync
.. index:: synchronize file complete in

**CALLING SEQUENCE:**

.. code:: c

    int fsync(
    int fd
    );

**STATUS CODES:**

On success, zero is returned. On error, -1 is returned, and ``errno``
is set appropriately.

*EBADF*
    ``fd`` is not a valid descriptor open for writing

*EINVAL*
    ``fd`` is bound to a special file which does not support support synchronization

*EROFS*
    ``fd`` is bound to a special file which does not support support synchronization

*EIO*
    An error occurred during synchronization

**DESCRIPTION:**

``fsync`` copies all in-core parts of a file to disk.

**NOTES:**

NONE

fdatasync - Synchronize file in-core data with that on disk
-----------------------------------------------------------
.. index:: fdatasync
.. index:: synchronize file in

**CALLING SEQUENCE:**

.. code:: c

    int fdatasync(
    int fd
    );

**STATUS CODES:**

On success, zero is returned. On error, -1 is returned, and ``errno`` is
set appropriately.

*EBADF*
    ``fd`` is not a valid file descriptor open for writing.

*EINVAL*
    ``fd`` is bound to a special file which does not support synchronization.

*EIO*
    An error occurred during synchronization.

*EROFS*
    ``fd`` is bound to a special file which dows not support synchronization.

**DESCRIPTION:**

``fdatasync`` flushes all data buffers of a file to disk (before the system call
returns). It resembles ``fsync`` but is not required to update the metadata such
as access time.

Applications that access databases or log files often write a tiny data fragment
(e.g., one line in a log file) and then call ``fsync`` immediately in order to
ensure that the written data is physically stored on the harddisk. Unfortunately,
fsync will always initiate two write operations: one for the newly written data and
another one in order to update the modification time stored in the inode. If the
modification time is not a part of the transaction concept ``fdatasync`` can be
used to avoid unnecessary inode disk write operations.

**NOTES:**

NONE

sync - Schedule file system updates
-----------------------------------
.. index:: sync
.. index:: synchronize file systems

**CALLING SEQUENCE:**

.. code:: c

    void sync(void);

**STATUS CODES:**

NONE

**DESCRIPTION:**

The ``sync`` service causes all information in memory that updates
file systems to be scheduled for writing out to all file systems.

**NOTES:**

The writing of data to the file systems is only guaranteed to be
scheduled upon return.  It is not necessarily complete upon return
from ``sync``.

mount - Mount a file system
---------------------------
.. index:: mount
.. index:: mount a file system

**CALLING SEQUENCE:**

.. code:: c

    #include <libio.h>
    int mount(
    rtems_filesystem_mount_table_entry_t \**mt_entry,
    rtems_filesystem_operations_table    \*fs_ops,
    rtems_filesystem_options_t            fsoptions,
    char                                 \*device,
    char                                 \*mount_point
    );

**STATUS CODES:**

*EXXX*

**DESCRIPTION:**

The ``mount`` routines mounts the filesystem class
which uses the filesystem operations specified by ``fs_ops``
and ``fsoptions``.  The filesystem is mounted at the directory``mount_point`` and the mode of the mounted filesystem is
specified by ``fsoptions``.  If this filesystem class requires
a device, then the name of the device must be specified by ``device``.

If this operation succeeds, the mount table entry for the mounted
filesystem is returned in ``mt_entry``.

**NOTES:**

NONE

unmount - Unmount file systems
------------------------------
.. index:: unmount
.. index:: unmount file systems

**CALLING SEQUENCE:**

.. code:: c

    #include <libio.h>
    int unmount(
    const char \*mount_path
    );

**STATUS CODES:**

*EXXX*

**DESCRIPTION:**

The ``unmount`` routine removes the attachment of the filesystem specified
by ``mount_path``.

**NOTES:**

NONE

readv - Vectored read from a file
---------------------------------
.. index:: readv
.. index:: vectored read from a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/uio.h>
    ssize_t readv(
    int                 fd,
    const struct iovec \*iov,
    int                 iovcnt
    );

**STATUS CODES:**

In addition to the errors detected by``Input and Output Primitives Manager read - Reads from a file, read()``,
this routine may return -1 and sets ``errno`` based upon the following
errors:

*EINVAL*
    The sum of the ``iov_len`` values in the iov array overflowed an``ssize_t``.

*EINVAL*
    The ``iovcnt`` argument was less than or equal to 0, or greater
    than ``IOV_MAX``.

**DESCRIPTION:**

The ``readv()`` function is equivalent to ``read()``
except as described here. The ``readv()`` function shall place
the input data into the ``iovcnt`` buffers specified by the
members of the ``iov`` array: ``iov[0], iov[1], ..., iov[iovcnt-1]``.

Each ``iovec`` entry specifies the base address and length of an area
in memory where data should be placed. The ``readv()`` function
always fills an area completely before proceeding to the next.

**NOTES:**

NONE

writev - Vectored write to a file
---------------------------------
.. index:: writev
.. index:: vectored write to a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/uio.h>
    ssize_t writev(
    int                 fd,
    const struct iovec \*iov,
    int                 iovcnt
    );

**STATUS CODES:**

In addition to the errors detected by``Input and Output Primitives Manager write - Write to a file, write()``,
this routine may return -1 and sets ``errno`` based upon the following
errors:

*EINVAL*
    The sum of the ``iov_len`` values in the iov array overflowed an``ssize_t``.

*EINVAL*
    The ``iovcnt`` argument was less than or equal to 0, or greater
    than ``IOV_MAX``.

**DESCRIPTION:**

The ``writev()`` function is equivalent to ``write()``,
except as noted here. The ``writev()`` function gathers output
data from the ``iovcnt`` buffers specified by the members of
the ``iov array``: ``iov[0], iov[1], ..., iov[iovcnt-1]``.
The ``iovcnt`` argument is valid if greater than 0 and less
than or equal to ``IOV_MAX``.

Each ``iovec`` entry specifies the base address and length of
an area in memory from which data should be written. The ``writev()``
function always writes a complete area before proceeding to the next.

If ``fd`` refers to a regular file and all of the ``iov_len``
members in the array pointed to by ``iov`` are 0, ``writev()``
returns 0 and has no other effect. For other file types, the behavior
is unspecified by POSIX.

**NOTES:**

NONE

aio_read - Asynchronous Read
----------------------------
.. index:: aio_read
.. index:: asynchronous read

**CALLING SEQUENCE:**

.. code:: c

    int aio_read(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_write - Asynchronous Write
------------------------------
.. index:: aio_write
.. index:: asynchronous write

**CALLING SEQUENCE:**

.. code:: c

    int aio_write(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

lio_listio - List Directed I/O
------------------------------
.. index:: lio_listio
.. index:: list directed i/o

**CALLING SEQUENCE:**

.. code:: c

    int lio_listio(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_error - Retrieve Error Status of Asynchronous I/O Operation
---------------------------------------------------------------
.. index:: aio_error
.. index:: retrieve error status of asynchronous i/o operation

**CALLING SEQUENCE:**

.. code:: c

    int aio_error(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_return - Retrieve Return Status Asynchronous I/O Operation
--------------------------------------------------------------
.. index:: aio_return
.. index:: retrieve return status asynchronous i/o operation

**CALLING SEQUENCE:**

.. code:: c

    int aio_return(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_cancel - Cancel Asynchronous I/O Request
--------------------------------------------
.. index:: aio_cancel
.. index:: cancel asynchronous i/o request

**CALLING SEQUENCE:**

.. code:: c

    int aio_cancel(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_suspend - Wait for Asynchronous I/O Request
-----------------------------------------------
.. index:: aio_suspend
.. index:: wait for asynchronous i/o request

**CALLING SEQUENCE:**

.. code:: c

    int aio_suspend(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_fsync - Asynchronous File Synchronization
---------------------------------------------
.. index:: aio_fsync
.. index:: asynchronous file synchronization

**CALLING SEQUENCE:**

.. code:: c

    int aio_fsync(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Device- and Class- Specific Functions Manager
#############################################

Introduction
============

The device- and class- specific functions manager is ...

The directives provided by the device- and class- specific functions
manager are:

- ``cfgetispeed`` - Reads terminal input baud rate

- ``cfgetospeed`` - Reads terminal output baud rate

- ``cfsetispeed`` - Sets terminal input baud rate

- ``cfsetospeed`` - Set terminal output baud rate

- ``tcgetattr`` - Gets terminal attributes

- ``tcsetattr`` - Set terminal attributes

- ``tcsendbreak`` - Sends a break to a terminal

- ``tcdrain`` - Waits for all output to be transmitted to the terminal

- ``tcflush`` - Discards terminal data

- ``tcflow`` - Suspends/restarts terminal output

- ``tcgetpgrp`` - Gets foreground process group ID

- ``tcsetpgrp`` - Sets foreground process group ID

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the device- and class- specific functions manager’s
directives. A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

cfgetispeed - Reads terminal input baud rate
--------------------------------------------
.. index:: cfgetispeed
.. index:: reads terminal input baud rate

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    int cfgetispeed(
    const struct termios \*p
    );

**STATUS CODES:**

The ``cfgetispeed()`` function returns a code for baud rate.

**DESCRIPTION:**

The ``cfsetispeed()`` function stores a code for the terminal speed
stored in a struct termios. The codes are defined in ``<termios.h>``
by the macros BO, B50, B75, B110, B134, B150, B200, B300, B600, B1200,
B1800, B2400, B4800, B9600, B19200, and B38400.

The ``cfsetispeed()`` function does not do anything to the hardware.
It merely stores a value for use by ``tcsetattr()``.

**NOTES:**

Baud rates are defined by symbols, such as B110, B1200, B2400. The actual
number returned for any given speed may change from system to system.

cfgetospeed - Reads terminal output baud rate
---------------------------------------------
.. index:: cfgetospeed
.. index:: reads terminal output baud rate

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    int cfgetospeed(
    const struct termios \*p
    );

**STATUS CODES:**

The ``cfgetospeed()`` function returns the termios code for the baud rate.

**DESCRIPTION:**

The ``cfgetospeed()`` function returns a code for the terminal speed
stored in a ``struct termios``. The codes are defined in ``<termios.h>``
by the macros BO, B50, B75, B110, B134, B150, B200, B300, B600, B1200, B1800,
B2400, B4800, B9600, B19200, and B38400.

The ``cfgetospeed()`` function does not do anything to the hardware.
It merely returns the value stored by a previous call to ``tcgetattr()``.

**NOTES:**

Baud rates are defined by symbols, such as B110, B1200, B2400. The actual
number returned for any given speed may change from system to system.

cfsetispeed - Sets terminal input baud rate
-------------------------------------------
.. index:: cfsetispeed
.. index:: sets terminal input baud rate

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    int cfsetispeed(
    struct termios \*p,
    speed_t         speed
    );

**STATUS CODES:**

The ``cfsetispeed()`` function returns a zero when successful and
returns -1 when an error occurs.

**DESCRIPTION:**

The ``cfsetispeed()`` function stores a code for the terminal speed
stored in a struct termios. The codes are defined in ``<termios.h>``
by the macros B0, B50, B75, B110, B134, B150, B200, B300, B600, B1200,
B1800, B2400, B4800, B9600, B19200, and B38400.

**NOTES:**

This function merely stores a value in the ``termios`` structure. It
does not change the terminal speed until a ``tcsetattr()`` is done.
It does not detect impossible terminal speeds.

cfsetospeed - Sets terminal output baud rate
--------------------------------------------
.. index:: cfsetospeed
.. index:: sets terminal output baud rate

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    int cfsetospeed(
    struct termios \*p,
    speed_t         speed
    );

**STATUS CODES:**

The ``cfsetospeed()`` function returns a zero when successful and
returns -1 when an error occurs.

**DESCRIPTION:**

The ``cfsetospeed()`` function stores a code for the terminal speed stored
in a struct ``termios``. The codes are defiined in ``<termios.h>`` by the
macros B0, B50, B75, B110, B134, B150, B200, B300, B600, B1200, B1800, B2400,
B4800, B9600, B19200, and B38400.

The ``cfsetospeed()`` function does not do anything to the hardware. It
merely stores a value for use by ``tcsetattr()``.

**NOTES:**

This function merely stores a value in the ``termios`` structure.
It does not change the terminal speed until a ``tcsetattr()`` is done.
It does not detect impossible terminal speeds.

tcgetattr - Gets terminal attributes
------------------------------------
.. index:: tcgetattr
.. index:: gets terminal attributes

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    #include <unistd.h>
    int tcgetattr(
    int             fildes,
    struct termios \*p
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

*ENOOTY*
    Terminal control function attempted for a file that is not a terminal.

**DESCRIPTION:**

The ``tcgetattr()`` gets the parameters associated with the terminal
referred to by ``fildes`` and stores them into the ``termios()``
structure pointed to by ``termios_p``.

**NOTES:**

NONE

tcsetattr - Set terminal attributes
-----------------------------------
.. index:: tcsetattr
.. index:: set terminal attributes

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    #include <unistd.h>
    int tcsetattr(
    int                   fildes,
    int                   options,
    const struct termios \*tp
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

tcsendbreak - Sends a break to a terminal
-----------------------------------------
.. index:: tcsendbreak
.. index:: sends a break to a terminal

**CALLING SEQUENCE:**

.. code:: c

    int tcsendbreak(
    int fd
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

tcdrain - Waits for all output to be transmitted to the terminal.
-----------------------------------------------------------------
.. index:: tcdrain
.. index:: waits for all output to be transmitted to the terminal.

**CALLING SEQUENCE:**

.. code:: c

    #include <termios.h>
    #include <unistd.h>
    int tcdrain(
    int fildes
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

*EINTR*
    Function was interrupted by a signal

*ENOTTY*
    Terminal control function attempted for a file that is not a terminal.

**DESCRIPTION:**

The ``tcdrain()`` function waits until all output written to``fildes`` has been transmitted.

**NOTES:**

NONE

tcflush - Discards terminal data
--------------------------------
.. index:: tcflush
.. index:: discards terminal data

**CALLING SEQUENCE:**

.. code:: c

    int tcflush(
    int fd
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

tcflow - Suspends/restarts terminal output.
-------------------------------------------
.. index:: tcflow
.. index:: suspends/restarts terminal output.

**CALLING SEQUENCE:**

.. code:: c

    int tcflow(
    int fd
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

tcgetpgrp - Gets foreground process group ID
--------------------------------------------
.. index:: tcgetpgrp
.. index:: gets foreground process group id

**CALLING SEQUENCE:**

.. code:: c

    int tcgetpgrp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

tcsetpgrp - Sets foreground process group ID
--------------------------------------------
.. index:: tcsetpgrp
.. index:: sets foreground process group id

**CALLING SEQUENCE:**

.. code:: c

    int tcsetpgrp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Language-Specific Services for the C Programming Language Manager
#################################################################

Introduction
============

The
language-specific services for the C programming language manager is ...

The directives provided by the language-specific services for the C programming language manager are:

- ``setlocale`` - Set the Current Locale

- ``fileno`` - Obtain File Descriptor Number for this File

- ``fdopen`` - Associate Stream with File Descriptor

- ``flockfile`` - Acquire Ownership of File Stream

- ``ftrylockfile`` - Poll to Acquire Ownership of File Stream

- ``funlockfile`` - Release Ownership of File Stream

- ``getc_unlocked`` - Get Character without Locking

- ``getchar_unlocked`` - Get Character from stdin without Locking

- ``putc_unlocked`` - Put Character without Locking

- ``putchar_unlocked`` - Put Character to stdin without Locking

- ``setjmp`` - Save Context for Non-Local Goto

- ``longjmp`` - Non-Local Jump to a Saved Context

- ``sigsetjmp`` - Save Context with Signal Status for Non-Local Goto

- ``siglongjmp`` - Non-Local Jump with Signal Status to a Saved Context

- ``tzset`` - Initialize Time Conversion Information

- ``strtok_r`` - Reentrant Extract Token from String

- ``asctime_r`` - Reentrant struct tm to ASCII Time Conversion

- ``ctime_r`` - Reentrant time_t to ASCII Time Conversion

- ``gmtime_r`` - Reentrant UTC Time Conversion

- ``localtime_r`` - Reentrant Local Time Conversion

- ``rand_r`` - Reentrant Random Number Generation

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the language-specific services for the C programming language manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

setlocale - Set the Current Locale
----------------------------------
.. index:: setlocale
.. index:: set the current locale

**CALLING SEQUENCE:**

.. code:: c

    int setlocale(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

fileno - Obtain File Descriptor Number for this File
----------------------------------------------------
.. index:: fileno
.. index:: obtain file descriptor number for this file

**CALLING SEQUENCE:**

.. code:: c

    int fileno(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

fdopen - Associate Stream with File Descriptor
----------------------------------------------
.. index:: fdopen
.. index:: associate stream with file descriptor

**CALLING SEQUENCE:**

.. code:: c

    int fdopen(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

flockfile - Acquire Ownership of File Stream
--------------------------------------------
.. index:: flockfile
.. index:: acquire ownership of file stream

**CALLING SEQUENCE:**

.. code:: c

    int flockfile(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

ftrylockfile - Poll to Acquire Ownership of File Stream
-------------------------------------------------------
.. index:: ftrylockfile
.. index:: poll to acquire ownership of file stream

**CALLING SEQUENCE:**

.. code:: c

    int ftrylockfile(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

funlockfile - Release Ownership of File Stream
----------------------------------------------
.. index:: funlockfile
.. index:: release ownership of file stream

**CALLING SEQUENCE:**

.. code:: c

    int funlockfile(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getc_unlocked - Get Character without Locking
---------------------------------------------
.. index:: getc_unlocked
.. index:: get character without locking

**CALLING SEQUENCE:**

.. code:: c

    int getc_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getchar_unlocked - Get Character from stdin without Locking
-----------------------------------------------------------
.. index:: getchar_unlocked
.. index:: get character from stdin without locking

**CALLING SEQUENCE:**

.. code:: c

    int getchar_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

putc_unlocked - Put Character without Locking
---------------------------------------------
.. index:: putc_unlocked
.. index:: put character without locking

**CALLING SEQUENCE:**

.. code:: c

    int putc_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

putchar_unlocked - Put Character to stdin without Locking
---------------------------------------------------------
.. index:: putchar_unlocked
.. index:: put character to stdin without locking

**CALLING SEQUENCE:**

.. code:: c

    int putchar_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

setjmp - Save Context for Non-Local Goto
----------------------------------------
.. index:: setjmp
.. index:: save context for non

**CALLING SEQUENCE:**

.. code:: c

    int setjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

longjmp - Non-Local Jump to a Saved Context
-------------------------------------------
.. index:: longjmp
.. index:: non

**CALLING SEQUENCE:**

.. code:: c

    int longjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

sigsetjmp - Save Context with Signal Status for Non-Local Goto
--------------------------------------------------------------
.. index:: sigsetjmp
.. index:: save context with signal status for non

**CALLING SEQUENCE:**

.. code:: c

    int sigsetjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

siglongjmp - Non-Local Jump with Signal Status to a Saved Context
-----------------------------------------------------------------
.. index:: siglongjmp
.. index:: non

**CALLING SEQUENCE:**

.. code:: c

    int siglongjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

tzset - Initialize Time Conversion Information
----------------------------------------------
.. index:: tzset
.. index:: initialize time conversion information

**CALLING SEQUENCE:**

.. code:: c

    int tzset(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

strtok_r - Reentrant Extract Token from String
----------------------------------------------
.. index:: strtok_r
.. index:: reentrant extract token from string

**CALLING SEQUENCE:**

.. code:: c

    int strtok_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

asctime_r - Reentrant struct tm to ASCII Time Conversion
--------------------------------------------------------
.. index:: asctime_r
.. index:: reentrant struct tm to ascii time conversion

**CALLING SEQUENCE:**

.. code:: c

    int asctime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

ctime_r - Reentrant time_t to ASCII Time Conversion
---------------------------------------------------
.. index:: ctime_r
.. index:: reentrant time_t to ascii time conversion

**CALLING SEQUENCE:**

.. code:: c

    int ctime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

gmtime_r - Reentrant UTC Time Conversion
----------------------------------------
.. index:: gmtime_r
.. index:: reentrant utc time conversion

**CALLING SEQUENCE:**

.. code:: c

    int gmtime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

localtime_r - Reentrant Local Time Conversion
---------------------------------------------
.. index:: localtime_r
.. index:: reentrant local time conversion

**CALLING SEQUENCE:**

.. code:: c

    int localtime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

rand_r - Reentrant Random Number Generation
-------------------------------------------
.. index:: rand_r
.. index:: reentrant random number generation

**CALLING SEQUENCE:**

.. code:: c

    int rand_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

System Databases Manager
########################

Introduction
============

The
system databases manager is ...

The directives provided by the system databases manager are:

- ``getgrgid`` - Get Group File Entry for ID

- ``getgrgid_r`` - Reentrant Get Group File Entry

- ``getgrnam`` - Get Group File Entry for Name

- ``getgrnam_r`` - Reentrant Get Group File Entry for Name

- ``getpwuid`` - Get Password File Entry for UID

- ``getpwuid_r`` - Reentrant Get Password File Entry for UID

- ``getpwnam`` - Get Password File Entry for Name

- ``getpwnam_r`` - Reentrant Get Password File Entry for Name

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the system databases manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

getgrgid - Get Group File Entry for ID
--------------------------------------
.. index:: getgrgid
.. index:: get group file entry for id

**CALLING SEQUENCE:**

.. code:: c

    int getgrgid(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getgrgid_r - Reentrant Get Group File Entry
-------------------------------------------
.. index:: getgrgid_r
.. index:: reentrant get group file entry

**CALLING SEQUENCE:**

.. code:: c

    int getgrgid_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getgrnam - Get Group File Entry for Name
----------------------------------------
.. index:: getgrnam
.. index:: get group file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getgrnam(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getgrnam_r - Reentrant Get Group File Entry for Name
----------------------------------------------------
.. index:: getgrnam_r
.. index:: reentrant get group file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getgrnam_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwuid - Get Password File Entry for UID
------------------------------------------
.. index:: getpwuid
.. index:: get password file entry for uid

**CALLING SEQUENCE:**

.. code:: c

    int getpwuid(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwuid_r - Reentrant Get Password File Entry for UID
------------------------------------------------------
.. index:: getpwuid_r
.. index:: reentrant get password file entry for uid

**CALLING SEQUENCE:**

.. code:: c

    int getpwuid_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwnam - Password File Entry for Name
---------------------------------------
.. index:: getpwnam
.. index:: password file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getpwnam(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwnam_r - Reentrant Get Password File Entry for Name
-------------------------------------------------------
.. index:: getpwnam_r
.. index:: reentrant get password file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getpwnam_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT(c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation(OAR).

.. COMMENT: All rights reserved.

Semaphore Manager
#################

Introduction
============

The semaphore manager provides functions to allocate, delete, and control
semaphores. This manager is based on the POSIX 1003.1 standard.

The directives provided by the semaphore manager are:

- ``sem_init`` - Initialize an unnamed semaphore

- ``sem_destroy`` - Destroy an unnamed semaphore

- ``sem_open`` - Open a named semaphore

- ``sem_close`` - Close a named semaphore

- ``sem_unlink`` - Remove a named semaphore

- ``sem_wait`` - Lock a semaphore

- ``sem_trywait`` - Lock a semaphore

- ``sem_timedwait`` - Wait on a Semaphore for a Specified Time

- ``sem_post`` - Unlock a semaphore

- ``sem_getvalue`` - Get the value of a semeaphore

Background
==========

Theory
------

Semaphores are used for synchronization and mutual exclusion by indicating the
availability and number of resources. The task (the task which is returning
resources) notifying other tasks of an event increases the number of resources
held by the semaphore by one. The task (the task which will obtain resources)
waiting for the event decreases the number of resources held by the semaphore
by one. If the number of resources held by a semaphore is insufficient (namely
0), the task requiring resources will wait until the next time resources are
returned to the semaphore. If there is more than one task waiting for a
semaphore, the tasks will be placed in the queue.

"sem_t" Structure
-----------------
.. index:: sem_t

The ``sem_t`` structure is used to represent semaphores. It is passed as an
argument to the semaphore directives and is defined as follows:
.. code:: c

    typedef int sem_t;

Building a Semaphore Attribute Set
----------------------------------

Operations
==========

Using as a Binary Semaphore
---------------------------

Although POSIX supports mutexes, they are only visible between threads. To work
between processes, a binary semaphore must be used.

Creating a semaphore with a limit on the count of 1 effectively restricts the
semaphore to being a binary semaphore. When the binary semaphore is available,
the count is 1. When the binary semaphore is unavailable, the count is 0.

Since this does not result in a true binary semaphore, advanced binary features like the Priority Inheritance and Priority Ceiling Protocols are not available.

There is currently no text in this section.

Directives
==========

This section details the semaphore manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

sem_init - Initialize an unnamed semaphore
------------------------------------------
.. index:: sem_init
.. index:: initialize an unnamed semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_init(
    sem_t        \*sem,
    int           pshared,
    unsigned int  value
    );

**STATUS CODES:**

*EINVAL*
    The value argument exceeds SEM_VALUE_MAX

*ENOSPC*
    A resource required to initialize the semaphore has been exhausted
    The limit on semaphores (SEM_VALUE_MAX) has been reached

*ENOSYS*
    The function sem_init is not supported by this implementation

*EPERM*
    The process lacks appropriate privileges to initialize the semaphore

**DESCRIPTION:**

The sem_init function is used to initialize the unnamed semaphore referred to
by "sem". The value of the initialized semaphore is the parameter "value". The
semaphore remains valid until it is destroyed.

ADD MORE HERE XXX

**NOTES:**

If the functions completes successfully, it shall return a value of zero.
Otherwise, it shall return a value of -1 and set "errno" to specify the error
that occurred.

Multiprocessing is currently not supported in this implementation.

sem_destroy - Destroy an unnamed semaphore
------------------------------------------
.. index:: sem_destroy
.. index:: destroy an unnamed semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_destroy(
    sem_t \*sem
    );

**STATUS CODES:**

*EINVAL*
    The value argument exceeds SEM_VALUE_MAX

*ENOSYS*
    The function sem_init is not supported by this implementation

*EBUSY*
    There are currently processes blocked on the semaphore

**DESCRIPTION:**

The sem_destroy function is used to destroy an unnamed semaphore refered to by
"sem". sem_destroy can only be used on a semaphore that was created using
sem_init.

**NOTES:**

If the functions completes successfully, it shall return a value of zero.
Otherwise, it shall return a value of -1 and set "errno" to specify the error
that occurred.

Multiprocessing is currently not supported in this implementation.

sem_open - Open a named semaphore
---------------------------------
.. index:: sem_open
.. index:: open a named semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_open(
    const char \*name,
    int         oflag
    );

**ARGUMENTS:**

The following flag bit may be set in oflag:

``O_CREAT`` - Creates the semaphore if it does not already exist. If O_CREAT
is set and the semaphore already exists then O_CREAT has no effect. Otherwise,
sem_open() creates a semaphore. The O_CREAT flag requires the third and fourth
argument: mode and value of type mode_t and unsigned int, respectively.

``O_EXCL`` - If O_EXCL and O_CREAT are set, all call to sem_open() shall fail
if the semaphore name exists

**STATUS CODES:**

*EACCES*
    Valid name specified but oflag permissions are denied, or the semaphore name
    specified does not exist and permission to create the named semaphore is denied.

*EEXIST*
    O_CREAT and O_EXCL are set and the named semaphore already exists.

*EINTR*
    The sem_open() operation was interrupted by a signal.

*EINVAL*
    The sem_open() operation is not supported for the given name.

*EMFILE*
    Too many semaphore descriptors or file descriptors in use by this process.

*ENAMETOOLONG*
    The length of the name exceed PATH_MAX or name component is longer than NAME_MAX
    while POSIX_NO_TRUNC is in effect.

*ENOENT*
    O_CREAT is not set and the named semaphore does not exist.

*ENOSPC*
    There is insufficient space for the creation of a new named semaphore.

*ENOSYS*
    The function sem_open() is not supported by this implementation.

**DESCRIPTION:**

The sem_open() function establishes a connection between a specified semaphore and
a process. After a call to sem_open with a specified semaphore name, a process
can reference to semaphore by the associated name using the address returned by
the call. The oflag arguments listed above control the state of the semaphore by
determining if the semaphore is created or accessed by a call to sem_open().

**NOTES:**

sem_close - Close a named semaphore
-----------------------------------
.. index:: sem_close
.. index:: close a named semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_close(
    sem_t \*sem_close
    );

**STATUS CODES:**

*EACCES*
    The semaphore argument is not a valid semaphore descriptor.

*ENOSYS*
    The function sem_close is not supported by this implementation.

**DESCRIPTION:**

The sem_close() function is used to indicate that the calling process is finished
using the named semaphore indicated by sem. The function sem_close deallocates
any system resources that were previously allocated by a sem_open system call. If
sem_close() completes successfully it returns a 1, otherwise a value of -1 is
return and errno is set.

**NOTES:**

sem_unlink - Unlink a semaphore
-------------------------------
.. index:: sem_unlink
.. index:: unlink a semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_unlink(
    const char \*name
    );

**STATUS CODES:**

*EACCESS*
    Permission is denied to unlink a semaphore.

*ENAMETOOLONG*
    The length of the strong name exceed NAME_MAX while POSIX_NO_TRUNC is in effect.

*ENOENT*
    The name of the semaphore does not exist.

*ENOSPC*
    There is insufficient space for the creation of a new named semaphore.

*ENOSYS*
    The function sem_unlink is not supported by this implementation.

**DESCRIPTION:**

The sem_unlink() function shall remove the semaphore name by the string name. If
a process is currently accessing the name semaphore, the sem_unlink command has
no effect. If one or more processes have the semaphore open when the sem_unlink
function is called, the destruction of semaphores shall be postponed until all
reference to semaphore are destroyed by calls to sem_close, _exit(), or exec.
After all references have been destroyed, it returns immediately.

If the termination is successful, the function shall return 0. Otherwise, a -1
is returned and the errno is set.

**NOTES:**

sem_wait - Wait on a Semaphore
------------------------------
.. index:: sem_wait
.. index:: wait on a semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_wait(
    sem_t \*sem
    );

**STATUS CODES:**

*EINVAL*
    The "sem" argument does not refer to a valid semaphore

**DESCRIPTION:**

This function attempts to lock a semaphore specified by ``sem``. If the
semaphore is available, then the semaphore is locked (i.e., the semaphore
value is decremented). If the semaphore is unavailable (i.e., the semaphore
value is zero), then the function will block until the semaphore becomes
available. It will then successfully lock the semaphore. The semaphore
remains locked until released by a ``sem_post()`` call.

If the call is unsuccessful, then the function returns -1 and sets errno to the
appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

sem_trywait - Non-blocking Wait on a Semaphore
----------------------------------------------
.. index:: sem_trywait
.. index:: non

**CALLING SEQUENCE:**

.. code:: c

    int sem_trywait(
    sem_t \*sem
    );

**STATUS CODES:**

*EAGAIN*
    The semaphore is not available (i.e., the semaphore value is zero), so the
    semaphore could not be locked.

*EINVAL*
    The ``sem`` argument does not refewr to a valid semaphore

**DESCRIPTION:**

This function attempts to lock a semaphore specified by ``sem``. If the
semaphore is available, then the semaphore is locked (i.e., the semaphore
value is decremented) and the function returns a value of 0. The semaphore
remains locked until released by a ``sem_post()`` call. If the semaphore
is unavailable (i.e., the semaphore value is zero), then the function will
return a value of -1 immediately and set ``errno`` to EAGAIN.

If the call is unsuccessful, then the function returns -1 and sets``errno`` to the appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

sem_timedwait - Wait on a Semaphore for a Specified Time
--------------------------------------------------------
.. index:: sem_timedwait
.. index:: wait on a semaphore for a specified time

**CALLING SEQUENCE:**

.. code:: c

    int sem_timedwait(
    sem_t                 \*sem,
    const struct timespec \*abstime
    );

**STATUS CODES:**

*EAGAIN*
    The semaphore is not available (i.e., the semaphore value is zero), so the
    semaphore could not be locked.

*EINVAL*
    The ``sem`` argument does not refewr to a valid semaphore

**DESCRIPTION:**

This function attemtps to lock a semaphore specified by ``sem``,
and will wait for the semaphore until the absolute time specified by``abstime``. If the semaphore is available, then the semaphore is
locked (i.e., the semaphore value is decremented) and the function
returns a value of 0. The semaphore remains locked until released by
a ``sem_post()`` call. If the semaphore is unavailable, then the
function will wait for the semaphore to become available for the amount
of time specified by ``timeout``.

If the semaphore does not become available within the interval specified by``timeout``, then the function returns -1 and sets ``errno`` to EAGAIN.
If any other error occurs, the function returns -1 and sets ``errno`` to
the appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

sem_post - Unlock a Semaphore
-----------------------------
.. index:: sem_post
.. index:: unlock a semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_post(
    sem_t \*sem
    );

**STATUS CODES:**

*EINVAL*
    The ``sem`` argument does not refer to a valid semaphore

**DESCRIPTION:**

This function attempts to release the semaphore specified by ``sem``. If
other tasks are waiting on the semaphore, then one of those tasks (which one
depends on the scheduler being used) is allowed to lock the semaphore and
return from its ``sem_wait()``, ``sem_trywait()``, or``sem_timedwait()`` call. If there are no other tasks waiting on the
semaphore, then the semaphore value is simply incremented. ``sem_post()``
returns 0 upon successful completion.

If an error occurs, the function returns -1 and sets ``errno`` to the
appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

sem_getvalue - Get the value of a semaphore
-------------------------------------------
.. index:: sem_getvalue
.. index:: get the value of a semaphore

**CALLING SEQUENCE:**

.. code:: c

    int sem_getvalue(
    sem_t \*sem,
    int   \*sval
    );

**STATUS CODES:**

*EINVAL*
    The "sem" argument does not refer to a valid semaphore

*ENOSYS*
    The function sem_getvalue is not supported by this implementation

**DESCRIPTION:**

The sem_getvalue functions sets the location referenced by the "sval" argument
to the value of the semaphore without affecting the state of the semaphore. The
updated value represents a semaphore value that occurred at some point during
the call, but is not necessarily the actual value of the semaphore when it
returns to the calling process.

If "sem" is locked, the value returned by sem_getvalue will be zero or a
negative number whose absolute value is the number of processes waiting for the
semaphore at some point during the call.

**NOTES:**

If the functions completes successfully, it shall return a value of zero.
Otherwise, it shall return a value of -1 and set "errno" to specify the error
that occurred.

.. COMMENT: COPYRIGHT (c) 1989-2008.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Mutex Manager
#############

Introduction
============

The mutex manager implements the functionality required of the mutex
manager as defined by POSIX 1003.1b-1996. This standard requires that
a compliant operating system provide the facilties to ensure that
threads can operate with mutual exclusion from one another and
defines the API that must be provided.

The services provided by the mutex manager are:

- ``pthread_mutexattr_init`` - Initialize a Mutex Attribute Set

- ``pthread_mutexattr_destroy`` - Destroy a Mutex Attribute Set

- ``pthread_mutexattr_setprotocol`` - Set the Blocking Protocol

- ``pthread_mutexattr_getprotocol`` - Get the Blocking Protocol

- ``pthread_mutexattr_setprioceiling`` - Set the Priority Ceiling

- ``pthread_mutexattr_getprioceiling`` - Get the Priority Ceiling

- ``pthread_mutexattr_setpshared`` - Set the Visibility

- ``pthread_mutexattr_getpshared`` - Get the Visibility

- ``pthread_mutex_init`` - Initialize a Mutex

- ``pthread_mutex_destroy`` - Destroy a Mutex

- ``pthread_mutex_lock`` - Lock a Mutex

- ``pthread_mutex_trylock`` - Poll to Lock a Mutex

- ``pthread_mutex_timedlock`` - Lock a Mutex with Timeout

- ``pthread_mutex_unlock`` - Unlock a Mutex

- ``pthread_mutex_setprioceiling`` - Dynamically Set the Priority Ceiling

- ``pthread_mutex_getprioceiling`` - Dynamically Get the Priority Ceiling

Background
==========

Mutex Attributes
----------------

Mutex attributes are utilized only at mutex creation time. A mutex
attribute structure may be initialized and passed as an argument to
the ``mutex_init`` routine. Note that the priority ceiling of
a mutex may be set at run-time.

*blocking protcol*
    is the XXX

*priority ceiling*
    is the XXX

*pshared*
    is the XXX

PTHREAD_MUTEX_INITIALIZER
-------------------------

This is a special value that a variable of type ``pthread_mutex_t``
may be statically initialized to as shown below:
.. code:: c

    pthread_mutex_t my_mutex = PTHREAD_MUTEX_INITIALIZER;

This indicates that ``my_mutex`` will be automatically initialized
by an implicit call to ``pthread_mutex_init`` the first time
the mutex is used.

Note that the mutex will be initialized with default attributes.

Operations
==========

There is currently no text in this section.

Services
========

This section details the mutex manager’s services.
A subsection is dedicated to each of this manager’s services
and describes the calling sequence, related constants, usage,
and status codes.

pthread_mutexattr_init - Initialize a Mutex Attribute Set
---------------------------------------------------------
.. index:: pthread_mutexattr_init
.. index:: initialize a mutex attribute set

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_init(
    pthread_mutexattr_t \*attr
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_mutexattr_init`` routine initializes the mutex attributes
object specified by ``attr`` with the default value for all of the
individual attributes.

**NOTES:**

XXX insert list of default attributes here.

pthread_mutexattr_destroy - Destroy a Mutex Attribute Set
---------------------------------------------------------
.. index:: pthread_mutexattr_destroy
.. index:: destroy a mutex attribute set

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_destroy(
    pthread_mutexattr_t \*attr
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_mutex_attr_destroy`` routine is used to destroy a mutex
attributes object. The behavior of using an attributes object after
it is destroyed is implementation dependent.

**NOTES:**

NONE

pthread_mutexattr_setprotocol - Set the Blocking Protocol
---------------------------------------------------------
.. index:: pthread_mutexattr_setprotocol
.. index:: set the blocking protocol

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_setprotocol(
    pthread_mutexattr_t \*attr,
    int                  protocol
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The protocol argument is invalid.

**DESCRIPTION:**

The ``pthread_mutexattr_setprotocol`` routine is used to set value of the``protocol`` attribute. This attribute controls the order in which
threads waiting on this mutex will receive it.

The ``protocol`` can be one of the following:

*``PTHREAD_PRIO_NONE``*
    in which case blocking order is FIFO.

*``PTHREAD_PRIO_INHERIT``*
    in which case blocking order is priority with the priority inheritance
    protocol in effect.

*``PTHREAD_PRIO_PROTECT``*
    in which case blocking order is priority with the priority ceiling
    protocol in effect.

**NOTES:**

There is currently no way to get simple priority blocking ordering
with POSIX mutexes even though this could easily by supported by RTEMS.

pthread_mutexattr_getprotocol - Get the Blocking Protocol
---------------------------------------------------------
.. index:: pthread_mutexattr_getprotocol
.. index:: get the blocking protocol

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_getprotocol(
    pthread_mutexattr_t \*attr,
    int                 \*protocol
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The protocol pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_mutexattr_getprotocol`` routine is used to obtain
the value of the ``protocol`` attribute. This attribute controls
the order in which threads waiting on this mutex will receive it.

**NOTES:**

NONE

pthread_mutexattr_setprioceiling - Set the Priority Ceiling
-----------------------------------------------------------
.. index:: pthread_mutexattr_setprioceiling
.. index:: set the priority ceiling

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_setprioceiling(
    pthread_mutexattr_t \*attr,
    int                  prioceiling
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The prioceiling argument is invalid.

**DESCRIPTION:**

The ``pthread_mutexattr_setprioceiling`` routine is used to set value of the``prioceiling`` attribute. This attribute specifies the priority that
is the ceiling for threads obtaining this mutex. Any task obtaining this
mutex may not be of greater priority that the ceiling. If it is of lower
priority, then its priority will be elevated to ``prioceiling``.

**NOTES:**

NONE

pthread_mutexattr_getprioceiling - Get the Priority Ceiling
-----------------------------------------------------------
.. index:: pthread_mutexattr_getprioceiling
.. index:: get the priority ceiling

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_getprioceiling(
    const pthread_mutexattr_t \*attr,
    int                       \*prioceiling
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The prioceiling pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_mutexattr_getprioceiling`` routine is used to obtain the
value of the ``prioceiling`` attribute. This attribute specifies the
priority ceiling for this mutex.

**NOTES:**

NONE

pthread_mutexattr_setpshared - Set the Visibility
-------------------------------------------------
.. index:: pthread_mutexattr_setpshared
.. index:: set the visibility

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_setpshared(
    pthread_mutexattr_t \*attr,
    int                  pshared
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The pshared argument is invalid.

**DESCRIPTION:**

**NOTES:**

pthread_mutexattr_getpshared - Get the Visibility
-------------------------------------------------
.. index:: pthread_mutexattr_getpshared
.. index:: get the visibility

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutexattr_getpshared(
    const pthread_mutexattr_t \*attr,
    int                       \*pshared
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The pshared pointer argument is invalid.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_init - Initialize a Mutex
---------------------------------------
.. index:: pthread_mutex_init
.. index:: initialize a mutex

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_init(
    pthread_mutex_t           \*mutex,
    const pthread_mutexattr_t \*attr
    );

**STATUS CODES:**

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The specified protocol is invalid.

*EAGAIN*
    The system lacked the necessary resources to initialize another mutex.

*ENOMEM*
    Insufficient memory exists to initialize the mutex.

*EBUSY*
    Attempted to reinialize the object reference by mutex, a previously
    initialized, but not yet destroyed.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_destroy - Destroy a Mutex
---------------------------------------
.. index:: pthread_mutex_destroy
.. index:: destroy a mutex

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_destroy(
    pthread_mutex_t \*mutex
    );

**STATUS CODES:**

*EINVAL*
    The specified mutex is invalid.

*EBUSY*
    Attempted to destroy the object reference by mutex, while it is locked or
    referenced by another thread.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_lock - Lock a Mutex
---------------------------------
.. index:: pthread_mutex_lock
.. index:: lock a mutex

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_lock(
    pthread_mutex_t \*mutex
    );

**STATUS CODES:**

*EINVAL*
    The specified mutex is invalid.

*EINVAL*
    The mutex has the protocol attribute of PTHREAD_PRIO_PROTECT and the
    priority of the calling thread is higher than the current priority
    ceiling.

*EDEADLK*
    The current thread already owns the mutex.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_trylock - Poll to Lock a Mutex
--------------------------------------------
.. index:: pthread_mutex_trylock
.. index:: poll to lock a mutex

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_trylock(
    pthread_mutex_t \*mutex
    );

**STATUS CODES:**

*EINVAL*
    The specified mutex is invalid.

*EINVAL*
    The mutex has the protocol attribute of PTHREAD_PRIO_PROTECT and the
    priority of the calling thread is higher than the current priority
    ceiling.

*EBUSY*
    The mutex is already locked.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_timedlock - Lock a Mutex with Timeout
---------------------------------------------------
.. index:: pthread_mutex_timedlock
.. index:: lock a mutex with timeout

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    #include <time.h>
    int pthread_mutex_timedlock(
    pthread_mutex_t       \*mutex,
    const struct timespec \*timeout
    );

**STATUS CODES:**

*EINVAL*
    The specified mutex is invalid.

*EINVAL*
    The nanoseconds field of timeout is invalid.

*EINVAL*
    The mutex has the protocol attribute of PTHREAD_PRIO_PROTECT and the
    priority of the calling thread is higher than the current priority
    ceiling.

*EDEADLK*
    The current thread already owns the mutex.

*ETIMEDOUT*
    The calling thread was unable to obtain the mutex within the specified
    timeout period.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_unlock - Unlock a Mutex
-------------------------------------
.. index:: pthread_mutex_unlock
.. index:: unlock a mutex

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_unlock(
    pthread_mutex_t \*mutex
    );

**STATUS CODES:**

*EINVAL*
    The specified mutex is invalid.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_setprioceiling - Dynamically Set the Priority Ceiling
-------------------------------------------------------------------
.. index:: pthread_mutex_setprioceiling
.. index:: dynamically set the priority ceiling

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_setprioceiling(
    pthread_mutex_t \*mutex,
    int              prioceiling,
    int             \*oldceiling
    );

**STATUS CODES:**

*EINVAL*
    The oldceiling pointer parameter is invalid.

*EINVAL*
    The prioceiling parameter is an invalid priority.

*EINVAL*
    The specified mutex is invalid.

**DESCRIPTION:**

**NOTES:**

pthread_mutex_getprioceiling - Get the Current Priority Ceiling
---------------------------------------------------------------
.. index:: pthread_mutex_getprioceiling
.. index:: get the current priority ceiling

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_mutex_getprioceiling(
    pthread_mutex_t \*mutex,
    int             \*prioceiling
    );

**STATUS CODES:**

*EINVAL*
    The prioceiling pointer parameter is invalid.

*EINVAL*
    The specified mutex is invalid.

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Condition Variable Manager
##########################

Introduction
============

The condition variable manager ...

The directives provided by the condition variable manager are:

- ``pthread_condattr_init`` - Initialize a Condition Variable Attribute Set

- ``pthread_condattr_destroy`` - Destroy a Condition Variable Attribute Set

- ``pthread_condattr_setpshared`` - Set Process Shared Attribute

- ``pthread_condattr_getpshared`` - Get Process Shared Attribute

- ``pthread_cond_init`` - Initialize a Condition Variable

- ``pthread_cond_destroy`` - Destroy a Condition Variable

- ``pthread_cond_signal`` - Signal a Condition Variable

- ``pthread_cond_broadcast`` - Broadcast a Condition Variable

- ``pthread_cond_wait`` - Wait on a Condition Variable

- ``pthread_cond_timedwait`` - With with Timeout a Condition Variable

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the condition variable manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

pthread_condattr_init - Initialize a Condition Variable Attribute Set
---------------------------------------------------------------------
.. index:: pthread_condattr_init
.. index:: initialize a condition variable attribute set

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_condattr_init(
    pthread_condattr_t \*attr
    );

**STATUS CODES:**

*ENOMEM*
    Insufficient memory is available to initialize the condition variable
    attributes object.

**DESCRIPTION:**

**NOTES:**

pthread_condattr_destroy - Destroy a Condition Variable Attribute Set
---------------------------------------------------------------------
.. index:: pthread_condattr_destroy
.. index:: destroy a condition variable attribute set

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_condattr_destroy(
    pthread_condattr_t \*attr
    );

**STATUS CODES:**

*EINVAL*
    The attribute object specified is invalid.

**DESCRIPTION:**

**NOTES:**

pthread_condattr_setpshared - Set Process Shared Attribute
----------------------------------------------------------
.. index:: pthread_condattr_setpshared
.. index:: set process shared attribute

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_condattr_setpshared(
    pthread_condattr_t \*attr,
    int                 pshared
    );

**STATUS CODES:**

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

**NOTES:**

pthread_condattr_getpshared - Get Process Shared Attribute
----------------------------------------------------------
.. index:: pthread_condattr_getpshared
.. index:: get process shared attribute

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_condattr_getpshared(
    const pthread_condattr_t \*attr,
    int                      \*pshared
    );

**STATUS CODES:**

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

**NOTES:**

pthread_cond_init - Initialize a Condition Variable
---------------------------------------------------
.. index:: pthread_cond_init
.. index:: initialize a condition variable

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_cond_init(
    pthread_cond_t           \*cond,
    const pthread_condattr_t \*attr
    );

**STATUS CODES:**

*EAGAIN*
    The system lacked a resource other than memory necessary to create the
    initialize the condition variable object.

*ENOMEM*
    Insufficient memory is available to initialize the condition variable object.

*EBUSY*
    The specified condition variable has already been initialized.

*EINVAL*
    The specified attribute value is invalid.

**DESCRIPTION:**

**NOTES:**

pthread_cond_destroy - Destroy a Condition Variable
---------------------------------------------------
.. index:: pthread_cond_destroy
.. index:: destroy a condition variable

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_cond_destroy(
    pthread_cond_t \*cond
    );

**STATUS CODES:**

*EINVAL*
    The specified condition variable is invalid.

*EBUSY*
    The specified condition variable is currently in use.

**DESCRIPTION:**

**NOTES:**

pthread_cond_signal - Signal a Condition Variable
-------------------------------------------------
.. index:: pthread_cond_signal
.. index:: signal a condition variable

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_cond_signal(
    pthread_cond_t \*cond
    );

**STATUS CODES:**

*EINVAL*
    The specified condition variable is not valid.

**DESCRIPTION:**

**NOTES:**

This routine should not be invoked from a handler from an asynchronous signal
handler or an interrupt service routine.

pthread_cond_broadcast - Broadcast a Condition Variable
-------------------------------------------------------
.. index:: pthread_cond_broadcast
.. index:: broadcast a condition variable

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_cond_broadcast(
    pthread_cond_t \*cond
    );

**STATUS CODES:**

*EINVAL*
    The specified condition variable is not valid.

**DESCRIPTION:**

**NOTES:**

This routine should not be invoked from a handler from an asynchronous signal
handler or an interrupt service routine.

pthread_cond_wait - Wait on a Condition Variable
------------------------------------------------
.. index:: pthread_cond_wait
.. index:: wait on a condition variable

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_cond_wait(
    pthread_cond_t \*cond,
    pthread_mutex_t \*mutex
    );

**STATUS CODES:**

*EINVAL*
    The specified condition variable or mutex is not initialized OR different
    mutexes were specified for concurrent pthread_cond_wait() and
    pthread_cond_timedwait() operations on the same condition variable OR
    the mutex was not owned by the current thread at the time of the call.

**DESCRIPTION:**

**NOTES:**

pthread_cond_timedwait - Wait with Timeout a Condition Variable
---------------------------------------------------------------
.. index:: pthread_cond_timedwait
.. index:: wait with timeout a condition variable

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_cond_timedwait(
    pthread_cond_t        \*cond,
    pthread_mutex_t       \*mutex,
    const struct timespec \*abstime
    );

**STATUS CODES:**

*EINVAL*
    The specified condition variable or mutex is not initialized OR different
    mutexes were specified for concurrent pthread_cond_wait() and
    pthread_cond_timedwait() operations on the same condition variable OR
    the mutex was not owned by the current thread at the time of the call.

*ETIMEDOUT*
    The specified time has elapsed without the condition variable being
    satisfied.

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Memory Management Manager
#########################

Introduction
============

The
memory management manager is ...

The directives provided by the memory management manager are:

- ``mlockall`` - Lock the Address Space of a Process

- ``munlockall`` - Unlock the Address Space of a Process

- ``mlock`` - Lock a Range of the Process Address Space

- ``munlock`` - Unlock a Range of the Process Address Space

- ``mmap`` - Map Process Addresses to a Memory Object

- ``munmap`` - Unmap Previously Mapped Addresses

- ``mprotect`` - Change Memory Protection

- ``msync`` - Memory Object Synchronization

- ``shm_open`` - Open a Shared Memory Object

- ``shm_unlink`` - Remove a Shared Memory Object

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the memory management manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

mlockall - Lock the Address Space of a Process
----------------------------------------------
.. index:: mlockall
.. index:: lock the address space of a process

**CALLING SEQUENCE:**

.. code:: c

    int mlockall(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

munlockall - Unlock the Address Space of a Process
--------------------------------------------------
.. index:: munlockall
.. index:: unlock the address space of a process

**CALLING SEQUENCE:**

.. code:: c

    int munlockall(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

mlock - Lock a Range of the Process Address Space
-------------------------------------------------
.. index:: mlock
.. index:: lock a range of the process address space

**CALLING SEQUENCE:**

.. code:: c

    int mlock(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

munlock - Unlock a Range of the Process Address Space
-----------------------------------------------------
.. index:: munlock
.. index:: unlock a range of the process address space

**CALLING SEQUENCE:**

.. code:: c

    int munlock(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

mmap - Map Process Addresses to a Memory Object
-----------------------------------------------
.. index:: mmap
.. index:: map process addresses to a memory object

**CALLING SEQUENCE:**

.. code:: c

    int mmap(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

munmap - Unmap Previously Mapped Addresses
------------------------------------------
.. index:: munmap
.. index:: unmap previously mapped addresses

**CALLING SEQUENCE:**

.. code:: c

    int munmap(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

mprotect - Change Memory Protection
-----------------------------------
.. index:: mprotect
.. index:: change memory protection

**CALLING SEQUENCE:**

.. code:: c

    int mprotect(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

msync - Memory Object Synchronization
-------------------------------------
.. index:: msync
.. index:: memory object synchronization

**CALLING SEQUENCE:**

.. code:: c

    int msync(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

shm_open - Open a Shared Memory Object
--------------------------------------
.. index:: shm_open
.. index:: open a shared memory object

**CALLING SEQUENCE:**

.. code:: c

    int shm_open(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

shm_unlink - Remove a Shared Memory Object
------------------------------------------
.. index:: shm_unlink
.. index:: remove a shared memory object

**CALLING SEQUENCE:**

.. code:: c

    int shm_unlink(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Scheduler Manager
#################

Introduction
============

The scheduler manager ...

The directives provided by the scheduler manager are:

- ``sched_get_priority_min`` - Get Minimum Priority Value

- ``sched_get_priority_max`` - Get Maximum Priority Value

- ``sched_rr_get_interval`` - Get Timeslicing Quantum

- ``sched_yield`` - Yield the Processor

Background
==========

Priority
--------

In the RTEMS implementation of the POSIX API, the priorities range from
the low priority of ``sched_get_priority_min()`` to the highest priority of``sched_get_priority_max()``. Numerically higher values represent higher
priorities.

Scheduling Policies
-------------------

The following scheduling policies are available:

*SCHED_FIFO*
    Priority-based, preemptive scheduling with no timeslicing. This is equivalent
    to what is called "manual round-robin" scheduling.

*SCHED_RR*
    Priority-based, preemptive scheduling with timeslicing. Time quantums are
    maintained on a per-thread basis and are not reset at each context switch.
    Thus, a thread which is preempted and subsequently resumes execution will
    attempt to complete the unused portion of its time quantum.

*SCHED_OTHER*
    Priority-based, preemptive scheduling with timeslicing. Time quantums are
    maintained on a per-thread basis and are reset at each context switch.

*SCHED_SPORADIC*
    Priority-based, preemptive scheduling utilizing three additional parameters:
    budget, replenishment period, and low priority. Under this policy, the
    thread is allowed to execute for "budget" amount of time before its priority
    is lowered to "low priority". At the end of each replenishment period,
    the thread resumes its initial priority and has its budget replenished.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the scheduler manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

sched_get_priority_min - Get Minimum Priority Value
---------------------------------------------------
.. index:: sched_get_priority_min
.. index:: get minimum priority value

**CALLING SEQUENCE:**

.. code:: c

    #include <sched.h>
    int sched_get_priority_min(
    int policy
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*EINVAL*
    The indicated policy is invalid.

**DESCRIPTION:**

This routine return the minimum (numerically and logically lowest) priority
for the specified ``policy``.

**NOTES:**

NONE

sched_get_priority_max - Get Maximum Priority Value
---------------------------------------------------
.. index:: sched_get_priority_max
.. index:: get maximum priority value

**CALLING SEQUENCE:**

.. code:: c

    #include <sched.h>
    int sched_get_priority_max(
    int policy
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*EINVAL*
    The indicated policy is invalid.

**DESCRIPTION:**

This routine return the maximum (numerically and logically highest) priority
for the specified ``policy``.

**NOTES:**

NONE

sched_rr_get_interval - Get Timeslicing Quantum
-----------------------------------------------
.. index:: sched_rr_get_interval
.. index:: get timeslicing quantum

**CALLING SEQUENCE:**

.. code:: c

    #include <sched.h>
    int sched_rr_get_interval(
    pid_t            pid,
    struct timespec \*interval
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*ESRCH*
    The indicated process id is invalid.

*EINVAL*
    The specified interval pointer parameter is invalid.

**DESCRIPTION:**

This routine returns the length of the timeslice quantum in the``interval`` parameter for the specified ``pid``.

**NOTES:**

The ``pid`` argument should be 0 to indicate the calling process.

sched_yield - Yield the Processor
---------------------------------
.. index:: sched_yield
.. index:: yield the processor

**CALLING SEQUENCE:**

.. code:: c

    #include <sched.h>
    int sched_yield( void );

**STATUS CODES:**

This routine always returns zero to indicate success.

**DESCRIPTION:**

This call forces the calling thread to yield the processor to another
thread. Normally this is used to implement voluntary round-robin
task scheduling.

**NOTES:**

NONE

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Clock Manager
#############

Introduction
============

The clock manager provides services two primary classes
of services.  The first focuses on obtaining and setting
the current date and time.  The other category of services
focus on allowing a thread to delay for a specific length
of time.

The directives provided by the clock manager are:

- ``clock_gettime`` - Obtain Time of Day

- ``clock_settime`` - Set Time of Day

- ``clock_getres`` - Get Clock Resolution

- ``sleep`` - Delay Process Execution

- ``usleep`` - Delay Process Execution in Microseconds

- ``nanosleep`` - Delay with High Resolution

- ``gettimeofday`` - Get the Time of Day

- ``time`` - Get time in seconds

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the clock manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

clock_gettime - Obtain Time of Day
----------------------------------
.. index:: clock_gettime
.. index:: obtain time of day

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int clock_gettime(
    clockid_t        clock_id,
    struct timespec \*tp
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*EINVAL*
    The tp pointer parameter is invalid.

*EINVAL*
    The clock_id specified is invalid.

**DESCRIPTION:**

**NOTES:**

NONE

clock_settime - Set Time of Day
-------------------------------
.. index:: clock_settime
.. index:: set time of day

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int clock_settime(
    clockid_t              clock_id,
    const struct timespec \*tp
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*EINVAL*
    The tp pointer parameter is invalid.

*EINVAL*
    The clock_id specified is invalid.

*EINVAL*
    The contents of the tp structure are invalid.

**DESCRIPTION:**

**NOTES:**

NONE

clock_getres - Get Clock Resolution
-----------------------------------
.. index:: clock_getres
.. index:: get clock resolution

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int clock_getres(
    clockid_t        clock_id,
    struct timespec \*res
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*EINVAL*
    The res pointer parameter is invalid.

*EINVAL*
    The clock_id specified is invalid.

**DESCRIPTION:**

**NOTES:**

If res is NULL, then the resolution is not returned.

sleep - Delay Process Execution
-------------------------------
.. index:: sleep
.. index:: delay process execution

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    unsigned int sleep(
    unsigned int seconds
    );

**STATUS CODES:**

This routine returns the number of unslept seconds.

**DESCRIPTION:**

The ``sleep()`` function delays the calling thread by the specified
number of ``seconds``.

**NOTES:**

This call is interruptible by a signal.

usleep - Delay Process Execution in Microseconds
------------------------------------------------
.. index:: usleep
.. index:: delay process execution
.. index:: delay process execution
.. index:: usecs delay process execution
.. index:: microsecond delay process execution

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    useconds_t usleep(
    useconds_t useconds
    );

**STATUS CODES:**

This routine returns the number of unslept seconds.

**DESCRIPTION:**

The ``sleep()`` function delays the calling thread by the specified
number of ``seconds``.

The ``usleep()`` function suspends the calling thread from execution
until either the number of microseconds specified by the``useconds`` argument has elapsed or a signal is delivered to the
calling thread and its action is to invoke a signal-catching function
or to terminate the process.

Because of other activity, or because of the time spent in
processing the call, the actual length of time the thread is
blocked may be longer than
the amount of time specified.

**NOTES:**

This call is interruptible by a signal.

The Single UNIX Specification allows this service to be implemented using
the same timer as that used by the ``alarm()`` service.  This is*NOT* the case for *RTEMS* and this call has no interaction with
the ``SIGALRM`` signal.

nanosleep - Delay with High Resolution
--------------------------------------
.. index:: nanosleep
.. index:: delay with high resolution

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int nanosleep(
    const struct timespec \*rqtp,
    struct timespec       \*rmtp
    );

**STATUS CODES:**

On error, this routine returns -1 and sets errno to one of the following:

*EINTR*
    The routine was interrupted by a signal.

*EAGAIN*
    The requested sleep period specified negative seconds or nanoseconds.

*EINVAL*
    The requested sleep period specified an invalid number for the nanoseconds
    field.

**DESCRIPTION:**

**NOTES:**

This call is interruptible by a signal.

gettimeofday - Get the Time of Day
----------------------------------
.. index:: gettimeofday
.. index:: get the time of day

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/time.h>
    #include <unistd.h>
    int gettimeofday(
    struct timeval  \*tp,
    struct timezone \*tzp
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` as appropriate.

*EPERM*
    ``settimeofdat`` is called by someone other than the superuser.

*EINVAL*
    Timezone (or something else) is invalid.

*EFAULT*
    One of ``tv`` or ``tz`` pointed outside your accessible address
    space

**DESCRIPTION:**

This routine returns the current time of day in the ``tp`` structure.

**NOTES:**

Currently, the timezone information is not supported. The ``tzp``
argument is ignored.

time - Get time in seconds
--------------------------
.. index:: time
.. index:: get time in seconds

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int time(
    time_t \*tloc
    );

**STATUS CODES:**

This routine returns the number of seconds since the Epoch.

**DESCRIPTION:**

``time`` returns the time since 00:00:00 GMT, January 1, 1970,
measured in seconds

If ``tloc`` in non null, the return value is also stored in the
memory pointed to by ``t``.

**NOTES:**

NONE

.. COMMENT: This is the chapter from the RTEMS POSIX 1003.1b API User's Guide that

.. COMMENT: documents the services provided by the timer @c  manager.

Timer Manager
#############

Introduction
============

The timer manager is ...

The services provided by the timer manager are:

- ``timer_create`` - Create a Per-Process Timer

- ``timer_delete`` - Delete a Per-Process Timer

- ``timer_settime`` - Set Next Timer Expiration

- ``timer_gettime`` - Get Time Remaining on Timer

- ``timer_getoverrun`` - Get Timer Overrun Count

Background
==========

Operations
==========

System Calls
============

This section details the timer manager’s services.
A subsection is dedicated to each of this manager’s services
and describes the calling sequence, related constants, usage,
and status codes.

.. COMMENT: timer_create

timer_create - Create a Per-Process Timer
-----------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    #include <signal.h>
    int timer_create(
    clockid_t        clock_id,
    struct sigevent \*evp,
    timer_t         \*timerid
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_delete

timer_delete - Delete a Per-Process Timer
-----------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int timer_delete(
    timer_t timerid
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_settime

timer_settime - Set Next Timer Expiration
-----------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int timer_settime(
    timer_t                  timerid,
    int                      flags,
    const struct itimerspec \*value,
    struct itimerspec       \*ovalue
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_gettime

timer_gettime - Get Time Remaining on Timer
-------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int timer_gettime(
    timer_t            timerid,
    struct itimerspec \*value
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_getoverrun

timer_getoverrun - Get Timer Overrun Count
------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <time.h>
    int timer_getoverrun(
    timer_t   timerid
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT(c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation(OAR).

.. COMMENT: All rights reserved.

Message Passing Manager
#######################

Introduction
============

The message passing manager is the means to provide communication and
synchronization capabilities using POSIX message queues.

The directives provided by the message passing manager are:

- ``mq_open`` - Open a Message Queue

- ``mq_close`` - Close a Message Queue

- ``mq_unlink`` - Remove a Message Queue

- ``mq_send`` - Send a Message to a Message Queue

- ``mq_receive`` - Receive a Message from a Message Queue

- ``mq_notify`` - Notify Process that a Message is Available

- ``mq_setattr`` - Set Message Queue Attributes

- ``mq_getattr`` - Get Message Queue Attributes

Background
==========

Theory
------

Message queues are named objects that operate with readers and writers.
In addition, a message queue is a priority queue of discrete messages.
POSIX message queues offer a certain, basic amount of application access
to, and control over, the message queue geometry that can be changed.

Messages
--------

A message is a variable length buffer where information can be stored to
support communication. The length of the message and the information
stored in that message are user-defined and can be actual data,
pointer(s), or empty. There is a maximum acceptable length for a message
that is associated with each message queue.

Message Queues
--------------

Message queues are named objects similar to the pipes of POSIX. They are
a means of communicating data between multiple processes and for passing
messages among tasks and ISRs. Message queues can contain a variable
number of messages from 0 to an upper limit that is user defined. The
maximum length of the message can be set on a per message queue basis.
Normally messages are sent and received from the message queue in FIFO
order. However, messages can also be prioritized and a priority queue
established for the passing of messages. Synchronization is needed when a
task waits for a message to arrive at a queue. Also, a task may poll a
queue for the arrival of a message... index:: mqd_t

The message queue descriptor ``mqd_t`` represents the message queue. It is
passed as an argument to all of the message queue functions.

Building a Message Queue Attribute Set
--------------------------------------

The mq_attr structure is used to define the characteristics of the message
queue... index:: mq_attr

.. code:: c

    typedef struct mq_attr{
    long mq_flags;
    long mq_maxmsg;
    long mq_msgsize;
    long mq_curmsgs;
    };

All of these attributes are set when the message queue is created using
mq_open. The mq_flags field is not used in the creation of a message
queue, it is only used by mq_setattr and mq_getattr. The structure
mq_attr is passed as an argument to mq_setattr and mq_getattr.

The mq_flags contain information affecting the behavior of the message
queue. The O_NONBLOCK mq_flag is the only flag that is defined. In
mq_setattr, the mq_flag can be set to dynamically change the blocking and
non-blocking behavior of the message queue. If the non-block flag is set
then the message queue is non-blocking, and requests to send and receive
messages do not block waiting for resources. For a blocking message
queue, a request to send might have to wait for an empty message queue,
and a request to receive might have to wait for a message to arrive on the
queue. Both mq_maxmsg and mq_msgsize affect the sizing of the message
queue. mq_maxmsg specifies how many messages the queue can hold at any
one time. mq_msgsize specifies the size of any one message on the queue.
If either of these limits is exceeded, an error message results.

Upon return from mq_getattr, the mq_curmsgs is set according to the
current state of the message queue. This specifies the number of messages
currently on the queue.

Notification of a Message on the Queue
--------------------------------------

Every message queue has the ability to notify one (and only one) process
whenever the queue’s state changes from empty (0 messages) to nonempty.
This means that the process does not have to block or constantly poll
while it waits for a message. By calling mq_notify, you can attach a
notification request to a message queue. When a message is received by an
empty queue, if there are no processes blocked and waiting for the
message, then the queue notifies the requesting process of a message
arrival. There is only one signal sent by the message queue, after that
the notification request is de-registered and another process can attach
its notification request. After receipt of a notification, a process must
re-register if it wishes to be notified again.

If there is a process blocked and waiting for the message, that process
gets the message, and notification is not sent. It is also possible for
another process to receive the message after the notification is sent but
before the notified process has sent its receive request.

Only one process can have a notification request attached to a message
queue at any one time. If another process attempts to register a
notification request, it fails. You can de-register for a message queue
by passing a NULL to mq_notify, this removes any notification request
attached to the queue. Whenever the message queue is closed, all
notification attachments are removed.

POSIX Interpretation Issues
---------------------------

There is one significant point of interpretation related to
the RTEMS implementation of POSIX message queues:

*What happens to threads already blocked on a message queue when the
mode of that same message queue is changed from blocking to non-blocking?*

The RTEMS POSIX implementation decided to unblock all waiting tasks
with an ``EAGAIN`` status just as if a non-blocking version of
the same operation had returned unsatisfied.  This case is not
discussed in the POSIX standard and other implementations may have
chosen alternative behaviors.

Operations
==========

Opening or Creating a Message Queue
-----------------------------------

If the message queue already exists, mq_open() opens it, if the message
queue does not exist, mq_open() creates it. When a message queue is
created, the geometry of the message queue is contained in the attribute
structure that is passed in as an argument. This includes mq_msgsize that
dictates the maximum size of a single message, and the mq_maxmsg that
dictates the maximum number of messages the queue can hold at one time.
The blocking or non-blocking behavior of the queue can also specified.

Closing a Message Queue
-----------------------

The mq_close() function is used to close the connection made to a message
queue that was made during mq_open. The message queue itself and the
messages on the queue are persistent and remain after the queue is closed.

Removing a Message Queue
------------------------

The mq_unlink() function removes the named message queue. If the message
queue is not open when mq_unlink is called, then the queue is immediately
eliminated. Any messages that were on the queue are lost, and the queue
can not be opened again. If processes have the queue open when mq_unlink
is called, the removal of the queue is delayed until the last process
using the queue has finished. However, the name of the message queue is
removed so that no other process can open it.

Sending a Message to a Message Queue
------------------------------------

The mq_send() function adds the message in priority order to the message
queue. Each message has an assigned a priority. The highest priority
message is be at the front of the queue.

The maximum number of messages that a message queue may accept is
specified at creation by the mq_maxmsg field of the attribute structure.
If this amount is exceeded, the behavior of the process is determined
according to what oflag was used when the message queue was opened. If
the queue was opened with O_NONBLOCK flag set, the process does not block,
and an error is returned. If the O_NONBLOCK flag was not set, the process
does block and wait for space on the queue.

Receiving a Message from a Message Queue
----------------------------------------

The mq_receive() function is used to receive the oldest of the highest
priority message(s) from the message queue specified by mqdes. The
messages are received in FIFO order within the priorities. The received
message’s priority is stored in the location referenced by the msg_prio.
If the msg_prio is a NULL, the priority is discarded. The message is
removed and stored in an area pointed to by msg_ptr whose length is of
msg_len. The msg_len must be at least equal to the mq_msgsize attribute
of the message queue.

The blocking behavior of the message queue is set by O_NONBLOCK at mq_open
or by setting O_NONBLOCK in mq_flags in a call to mq_setattr. If this is
a blocking queue, the process does block and wait on an empty queue. If
this a non-blocking queue, the process does not block. Upon successful
completion, mq_receive returns the length of the selected message in bytes
and the message is removed from the queue.

Notification of Receipt of a Message on an Empty Queue
------------------------------------------------------

The mq_notify() function registers the calling process to be notified of
message arrival at an empty message queue. Every message queue has the
ability to notify one (and only one) process whenever the queue’s state
changes from empty (0 messages) to nonempty. This means that the process
does not have to block or constantly poll while it waits for a message.
By calling mq_notify, a notification request is attached to a message
queue. When a message is received by an empty queue, if there are no
processes blocked and waiting for the message, then the queue notifies the
requesting process of a message arrival. There is only one signal sent by
the message queue, after that the notification request is de-registered
and another process can attach its notification request. After receipt of
a notification, a process must re-register if it wishes to be notified
again.

If there is a process blocked and waiting for the message, that process
gets the message, and notification is not sent. Only one process can have
a notification request attached to a message queue at any one time. If
another process attempts to register a notification request, it fails.
You can de-register for a message queue by passing a NULL to mq_notify,
this removes any notification request attached to the queue. Whenever the
message queue is closed, all notification attachments are removed.

Setting the Attributes of a Message Queue
-----------------------------------------

The mq_setattr() function is used to set attributes associated with the
open message queue description referenced by the message queue descriptor
specified by mqdes. The \*omqstat represents the old or previous
attributes. If omqstat is non-NULL, the function mq_setattr() stores, in
the location referenced by omqstat, the previous message queue attributes
and the current queue status. These values are the same as would be
returned by a call to mq_getattr() at that point.

There is only one mq_attr.mq_flag that can be altered by this call. This
is the flag that deals with the blocking and non-blocking behavior of the
message queue. If the flag is set then the message queue is non-blocking,
and requests to send or receive do not block while waiting for resources.
If the flag is not set, then message send and receive may involve waiting
for an empty queue or waiting for a message to arrive.

Getting the Attributes of a Message Queue
-----------------------------------------

The mq_getattr() function is used to get status information and attributes
of the message queue associated with the message queue descriptor. The
results are returned in the mq_attr structure referenced by the mqstat
argument. All of these attributes are set at create time, except the
blocking/non-blocking behavior of the message queue which can be
dynamically set by using mq_setattr. The attribute mq_curmsg is set to
reflect the number of messages on the queue at the time that mq_getattr
was called.

Directives
==========

This section details the message passing manager’s directives. A
subsection is dedicated to each of this manager’s directives and describes
the calling sequence, related constants, usage, and status codes.

mq_open - Open a Message Queue
------------------------------
.. index:: mq_open
.. index:: open a message queue

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    mqd_t mq_open(
    const char     \*name,
    int             oflag,
    mode_t          mode,
    struct mq_attr \*attr
    );

**STATUS CODES:**

``EACCES`` - Either the message queue exists and the permissions
requested in oflags were denied, or the message does not exist and
permission to create one is denied.

``EEXIST`` - You tried to create a message queue that already exists.

``EINVAL`` - An inappropriate name was given for the message queue, or
the values of mq-maxmsg or mq_msgsize were less than 0.

``ENOENT`` - The message queue does not exist, and you did not specify
to create it.

``EINTR`` - The call to mq_open was interrupted by a signal.

``EMFILE`` - The process has too many files or message queues open.
This is a process limit error.

``ENFILE`` - The system has run out of resources to support more open
message queues. This is a system error.

``ENAMETOOLONG`` - mq_name is too long.

**DESCRIPTION:**

The mq_open () function establishes the connection between a process and a
message queue with a message queue descriptor. If the message queue
already exists, mq_open opens it, if the message queue does not exist,
mq_open creates it. Message queues can have multiple senders and
receivers. If mq_open is successful, the function returns a message queue
descriptor. Otherwise, the function returns a -1 and sets ’errno’ to
indicate the error.

The name of the message queue is used as an argument. For the best of
portability, the name of the message queue should begin with a "/" and no
other "/" should be in the name. Different systems interpret the name in
different ways.

The oflags contain information on how the message is opened if the queue
already exists. This may be O_RDONLY for read only, O_WRONLY for write
only, of O_RDWR, for read and write.

In addition, the oflags contain information needed in the creation of a
message queue. ``O_NONBLOCK`` - If the non-block flag is set then the
message queue is non-blocking, and requests to send and receive messages
do not block waiting for resources. If the flag is not set then the
message queue is blocking, and a request to send might have to wait for an
empty message queue. Similarly, a request to receive might have to wait
for a message to arrive on the queue. ``O_CREAT`` - This call specifies
that the call the mq_open is to create a new message queue. In this case
the mode and attribute arguments of the function call are utilized. The
message queue is created with a mode similar to the creation of a file,
read and write permission creator, group, and others.

The geometry of the message queue is contained in the attribute structure.
This includes mq_msgsize that dictates the maximum size of a single
message, and the mq_maxmsg that dictates the maximum number of messages
the queue can hold at one time. If a NULL is used in the mq_attr
argument, then the message queue is created with implementation defined
defaults. ``O_EXCL`` - is always set if O_CREAT flag is set. If the
message queue already exists, O_EXCL causes an error message to be
returned, otherwise, the new message queue fails and appends to the
existing one.

**NOTES:**

The mq_open () function does not add or remove messages from the queue.
When a new message queue is being created, the mq_flag field of the
attribute structure is not used.

mq_close - Close a Message Queue
--------------------------------
.. index:: mq_close
.. index:: close a message queue

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    int mq_close(
    mqd_t mqdes
    );

**STATUS CODES:**

``EINVAL`` - The descriptor does not represent a valid open message
queue

**DESCRIPTION:**

The mq_close function removes the association between the message queue
descriptor, mqdes, and its message queue. If mq_close() is successfully
completed, the function returns a value of zero; otherwise, the function
returns a value of -1 and sets errno to indicate the error.

**NOTES:**

If the process had successfully attached a notification request to the
message queue via mq_notify, this attachment is removed, and the message
queue is available for another process to attach for notification.
mq_close has no effect on the contents of the message queue, all the
messages that were in the queue remain in the queue.

mq_unlink - Remove a Message Queue
----------------------------------
.. index:: mq_unlink
.. index:: remove a message queue

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    int mq_unlink(
    const char \*name
    );

**STATUS CODES:**

``EINVAL`` - The descriptor does not represent a valid message queue

**DESCRIPTION:**

The mq_unlink() function removes the named message queue. If the message
queue is not open when mq_unlink is called, then the queue is immediately
eliminated. Any messages that were on the queue are lost, and the queue
can not be opened again. If processes have the queue open when mq_unlink
is called, the removal of the queue is delayed until the last process
using the queue has finished. However, the name of the message queue is
removed so that no other process can open it. Upon successful completion,
the function returns a value of zero. Otherwise, the named message queue
is not changed by this function call, and the function returns a value of
-1 and sets errno to indicate the error.

**NOTES:**

Calls to mq_open() to re-create the message queue may fail until the
message queue is actually removed. However, the mq_unlink() call need not
block until all references have been closed; it may return immediately.

mq_send - Send a Message to a Message Queue
-------------------------------------------
.. index:: mq_send
.. index:: send a message to a message queue

**CALLING SEQUENCE:**

.. code:: c

    #include<mqueue.h>
    int mq_send(
    mqd_t        mqdes,
    const char  \*msg_ptr,
    size_t       msg_len,
    unsigned int msg_prio
    );

**STATUS CODES:**

``EBADF`` - The descriptor does not represent a valid message queue, or the queue was opened for read only O_RDONLY``EINVAL`` - The value of msg_prio was greater than the MQ_PRIO_MAX.``EMSGSIZE`` - The msg_len is greater than the mq_msgsize attribute of the message queue``EAGAIN`` - The message queue is non-blocking, and there is no room on the queue for another message as specified by the mq_maxmsg.``EINTR`` - The message queue is blocking. While the process was waiting for free space on the queue, a signal arrived that interrupted the wait.

**DESCRIPTION:**

The mq_send() function adds the message pointed to by the argument msg_ptr
to the message queue specified by mqdes. Each message is assigned a
priority , from 0 to MQ_PRIO_MAX. MQ_PRIO_MAX is defined in <limits.h> and
must be at least 32. Messages are added to the queue in order of their
priority. The highest priority message is at the front of the queue.

The maximum number of messages that a message queue may accept is
specified at creation by the mq_maxmsg field of the attribute structure.
If this amount is exceeded, the behavior of the process is determined
according to what oflag was used when the message queue was opened. If
the queue was opened with O_NONBLOCK flag set, then the EAGAIN error is
returned. If the O_NONBLOCK flag was not set, the process blocks and
waits for space on the queue, unless it is interrupted by a signal.

Upon successful completion, the mq_send () function returns a value of
zero. Otherwise, no message is enqueued, the function returns -1, and
errno is set to indicate the error.

**NOTES:**

If the specified message queue is not full, mq_send inserts the message at
the position indicated by the msg_prio argument.

mq_receive - Receive a Message from a Message Queue
---------------------------------------------------
.. index:: mq_receive
.. index:: receive a message from a message queue

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    size_t mq_receive(
    mqd_t         mqdes,
    char         \*msg_ptr,
    size_t        msg_len,
    unsigned int \*msg_prio
    );

**STATUS CODES:**

``EBADF`` - The descriptor does not represent a valid message queue, or the queue was opened for write only O_WRONLY``EMSGSIZE`` - The msg_len is less than the mq_msgsize attribute of the message queue``EAGAIN`` - The message queue is non-blocking, and the queue is empty``EINTR`` - The message queue is blocking. While the process was waiting for a message to arrive on the queue, a signal arrived that interrupted the wait.

**DESCRIPTION:**

The mq_receive function is used to receive the oldest of the highest
priority message(s) from the message queue specified by mqdes. The
messages are received in FIFO order within the priorities. The received
message’s priority is stored in the location referenced by the msg_prio.
If the msg_prio is a NULL, the priority is discarded. The message is
removed and stored in an area pointed to by msg_ptr whose length is of
msg_len. The msg_len must be at least equal to the mq_msgsize attribute
of the message queue.

The blocking behavior of the message queue is set by O_NONBLOCK at mq_open
or by setting O_NONBLOCK in mq_flags in a call to mq_setattr. If this is
a blocking queue, the process blocks and waits on an empty queue. If this
a non-blocking queue, the process does not block.

Upon successful completion, mq_receive returns the length of the selected
message in bytes and the message is removed from the queue. Otherwise, no
message is removed from the queue, the function returns a value of -1, and
sets errno to indicate the error.

**NOTES:**

If the size of the buffer in bytes, specified by the msg_len argument, is
less than the mq_msgsize attribute of the message queue, the function
fails and returns an error

mq_notify - Notify Process that a Message is Available
------------------------------------------------------
.. index:: mq_notify
.. index:: notify process that a message is available

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    int mq_notify(
    mqd_t                  mqdes,
    const struct sigevent \*notification
    );

**STATUS CODES:**

``EBADF`` - The descriptor does not refer to a valid message queue``EBUSY`` - A notification request is already attached to the queue

**DESCRIPTION:**

If the argument notification is not NULL, this function registers the
calling process to be notified of message arrival at an empty message
queue associated with the specified message queue descriptor, mqdes.

Every message queue has the ability to notify one (and only one) process
whenever the queue’s state changes from empty (0 messages) to nonempty.
This means that the process does not have to block or constantly poll
while it waits for a message. By calling mq_notify, a notification
request is attached to a message queue. When a message is received by an
empty queue, if there are no processes blocked and waiting for the
message, then the queue notifies the requesting process of a message
arrival. There is only one signal sent by the message queue, after that
the notification request is de-registered and another process can attach
its notification request. After receipt of a notification, a process must
re-register if it wishes to be notified again.

If there is a process blocked and waiting for the message, that process
gets the message, and notification is not be sent. Only one process can
have a notification request attached to a message queue at any one time.
If another process attempts to register a notification request, it fails.
You can de-register for a message queue by passing a NULL to mq_notify;
this removes any notification request attached to the queue. Whenever the
message queue is closed, all notification attachments are removed.

Upon successful completion, mq_notify returns a value of zero; otherwise,
the function returns a value of -1 and sets errno to indicate the error.

**NOTES:**

It is possible for another process to receive the message after the notification is sent but before the notified process has sent its receive request.

mq_setattr - Set Message Queue Attributes
-----------------------------------------
.. index:: mq_setattr
.. index:: set message queue attributes

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    int mq_setattr(
    mqd_t                 mqdes,
    const struct mq_attr \*mqstat,
    struct mq_attr       \*omqstat
    );

**STATUS CODES:**

``EBADF`` - The message queue descriptor does not refer to a valid, open queue.``EINVAL`` - The mq_flag value is invalid.

**DESCRIPTION:**

The mq_setattr function is used to set attributes associated with the open
message queue description referenced by the message queue descriptor
specified by mqdes. The \*omqstat represents the old or previous
attributes. If omqstat is non-NULL, the function mq_setattr() stores, in
the location referenced by omqstat, the previous message queue attributes
and the current queue status. These values are the same as would be
returned by a call to mq_getattr() at that point.

There is only one mq_attr.mq_flag which can be altered by this call.
This is the flag that deals with the blocking and non-blocking behavior of
the message queue. If the flag is set then the message queue is
non-blocking, and requests to send or receive do not block while waiting
for resources. If the flag is not set, then message send and receive may
involve waiting for an empty queue or waiting for a message to arrive.

Upon successful completion, the function returns a value of zero and the
attributes of the message queue have been changed as specified.
Otherwise, the message queue attributes is unchanged, and the function
returns a value of -1 and sets errno to indicate the error.

**NOTES:**

All other fields in the mq_attr are ignored by this call.

mq_getattr - Get Message Queue Attributes
-----------------------------------------
.. index:: mq_getattr
.. index:: get message queue attributes

**CALLING SEQUENCE:**

.. code:: c

    #include <mqueue.h>
    int mq_getattr(
    mqd_t mqdes,
    struct mq_attr \*mqstat
    );

**STATUS CODES:**

``EBADF`` - The message queue descriptor does not refer to a valid,
open message queue.

**DESCRIPTION:**

The mqdes argument specifies a message queue descriptor. The mq_getattr
function is used to get status information and attributes of the message
queue associated with the message queue descriptor. The results are
returned in the mq_attr structure referenced by the mqstat argument. All
of these attributes are set at create time, except the
blocking/non-blocking behavior of the message queue which can be
dynamically set by using mq_setattr. The attribute mq_curmsg is set to
reflect the number of messages on the queue at the time that mq_getattr
was called.

Upon successful completion, the mq_getattr function returns zero.
Otherwise, the function returns -1 and sets errno to indicate the error.

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2014.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Thread Manager
##############

Introduction
============

The thread manager implements the functionality required of the thread
manager as defined by POSIX 1003.1b. This standard requires that
a compliant operating system provide the facilties to manage multiple
threads of control and defines the API that must be provided.

The services provided by the thread manager are:

- ``pthread_attr_init`` - Initialize a Thread Attribute Set

- ``pthread_attr_destroy`` - Destroy a Thread Attribute Set

- ``pthread_attr_setdetachstate`` - Set Detach State

- ``pthread_attr_getdetachstate`` - Get Detach State

- ``pthread_attr_setstacksize`` - Set Thread Stack Size

- ``pthread_attr_getstacksize`` - Get Thread Stack Size

- ``pthread_attr_setstackaddr`` - Set Thread Stack Address

- ``pthread_attr_getstackaddr`` - Get Thread Stack Address

- ``pthread_attr_setscope`` - Set Thread Scheduling Scope

- ``pthread_attr_getscope`` - Get Thread Scheduling Scope

- ``pthread_attr_setinheritsched`` - Set Inherit Scheduler Flag

- ``pthread_attr_getinheritsched`` - Get Inherit Scheduler Flag

- ``pthread_attr_setschedpolicy`` - Set Scheduling Policy

- ``pthread_attr_getschedpolicy`` - Get Scheduling Policy

- ``pthread_attr_setschedparam`` - Set Scheduling Parameters

- ``pthread_attr_getschedparam`` - Get Scheduling Parameters

- ``pthread_attr_getaffinity_np`` - Get Thread Affinity Attribute

- ``pthread_attr_setaffinity_np`` - Set Thread Affinity Attribute

- ``pthread_create`` - Create a Thread

- ``pthread_exit`` - Terminate the Current Thread

- ``pthread_detach`` - Detach a Thread

- ``pthread_getattr_np`` - Get Thread Attributes

- ``pthread_join`` - Wait for Thread Termination

- ``pthread_self`` - Get Thread ID

- ``pthread_equal`` - Compare Thread IDs

- ``pthread_once`` - Dynamic Package Initialization

- ``pthread_setschedparam`` - Set Thread Scheduling Parameters

- ``pthread_getschedparam`` - Get Thread Scheduling Parameters

- ``pthread_getaffinity_np`` - Get Thread Affinity

- ``pthread_setaffinity_np`` - Set Thread Affinity

Background
==========

Thread Attributes
-----------------

Thread attributes are utilized only at thread creation time. A thread
attribute structure may be initialized and passed as an argument to
the ``pthread_create`` routine.

*stack address*
    is the address of the optionally user specified stack area for this thread.
    If this value is NULL, then RTEMS allocates the memory for the thread stack
    from the RTEMS Workspace Area. Otherwise, this is the user specified
    address for the memory to be used for the thread’s stack. Each thread must
    have a distinct stack area. Each processor family has different alignment
    rules which should be followed.

*stack size*
    is the minimum desired size for this thread’s stack area.
    If the size of this area as specified by the stack size attribute
    is smaller than the minimum for this processor family and the stack
    is not user specified, then RTEMS will automatically allocate a
    stack of the minimum size for this processor family.

*contention scope*
    specifies the scheduling contention scope. RTEMS only supports the
    PTHREAD_SCOPE_PROCESS scheduling contention scope.

*scheduling inheritance*
    specifies whether a user specified or the scheduling policy and
    parameters of the currently executing thread are to be used. When
    this is PTHREAD_INHERIT_SCHED, then the scheduling policy and
    parameters of the currently executing thread are inherited by
    the newly created thread.

*scheduling policy and parameters*
    specify the manner in which the thread will contend for the processor.
    The scheduling parameters are interpreted based on the specified policy.
    All policies utilize the thread priority parameter.

Operations
==========

There is currently no text in this section.

Services
========

This section details the thread manager’s services.
A subsection is dedicated to each of this manager’s services
and describes the calling sequence, related constants, usage,
and status codes.

pthread_attr_init - Initialize a Thread Attribute Set
-----------------------------------------------------
.. index:: pthread_attr_init
.. index:: initialize a thread attribute set

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_init(
    pthread_attr_t \*attr
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_init`` routine initializes the thread attributes
object specified by ``attr`` with the default value for all of the
individual attributes.

**NOTES:**

The settings in the default attributes are implementation defined. For
RTEMS, the default attributes are as follows:

- stackadr
  is not set to indicate that RTEMS is to allocate the stack memory.

- stacksize
  is set to ``PTHREAD_MINIMUM_STACK_SIZE``.

- contentionscope
  is set to ``PTHREAD_SCOPE_PROCESS``.

- inheritsched
  is set to ``PTHREAD_INHERIT_SCHED`` to indicate that the created
  thread inherits its scheduling attributes from its parent.

- detachstate
  is set to ``PTHREAD_CREATE_JOINABLE``.

pthread_attr_destroy - Destroy a Thread Attribute Set
-----------------------------------------------------
.. index:: pthread_attr_destroy
.. index:: destroy a thread attribute set

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_destroy(
    pthread_attr_t \*attr
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_attr_destroy`` routine is used to destroy a thread
attributes object. The behavior of using an attributes object after
it is destroyed is implementation dependent.

**NOTES:**

NONE

pthread_attr_setdetachstate - Set Detach State
----------------------------------------------
.. index:: pthread_attr_setdetachstate
.. index:: set detach state

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setdetachstate(
    pthread_attr_t \*attr,
    int             detachstate
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The detachstate argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setdetachstate`` routine is used to value of the``detachstate`` attribute. This attribute controls whether the
thread is created in a detached state.

The ``detachstate`` can be either ``PTHREAD_CREATE_DETACHED`` or``PTHREAD_CREATE_JOINABLE``. The default value for all threads is``PTHREAD_CREATE_JOINABLE``.

**NOTES:**

If a thread is in a detached state,
then the use of the ID with the ``pthread_detach`` or``pthread_join`` routines is an error.

pthread_attr_getdetachstate - Get Detach State
----------------------------------------------
.. index:: pthread_attr_getdetachstate
.. index:: get detach state

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getdetachstate(
    const pthread_attr_t \*attr,
    int                  \*detachstate
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The detatchstate pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getdetachstate`` routine is used to obtain the
current value of the ``detachstate`` attribute as specified
by the ``attr`` thread attribute object.

**NOTES:**

NONE

pthread_attr_setstacksize - Set Thread Stack Size
-------------------------------------------------
.. index:: pthread_attr_setstacksize
.. index:: set thread stack size

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setstacksize(
    pthread_attr_t \*attr,
    size_t          stacksize
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_attr_setstacksize`` routine is used to set the``stacksize`` attribute in the ``attr`` thread attribute
object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_ATTR_STACKSIZE`` to indicate that this
routine is supported.

If the specified stacksize is below the minimum required for this CPU
(``PTHREAD_STACK_MIN``, then the stacksize will be set to the minimum
for this CPU.

pthread_attr_getstacksize - Get Thread Stack Size
-------------------------------------------------
.. index:: pthread_attr_getstacksize
.. index:: get thread stack size

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getstacksize(
    const pthread_attr_t \*attr,
    size_t               \*stacksize
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The stacksize pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getstacksize`` routine is used to obtain the``stacksize`` attribute in the ``attr`` thread attribute
object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_ATTR_STACKSIZE`` to indicate that this
routine is supported.

pthread_attr_setstackaddr - Set Thread Stack Address
----------------------------------------------------
.. index:: pthread_attr_setstackaddr
.. index:: set thread stack address

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setstackaddr(
    pthread_attr_t \*attr,
    void           \*stackaddr
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

**DESCRIPTION:**

The ``pthread_attr_setstackaddr`` routine is used to set the``stackaddr`` attribute in the ``attr`` thread attribute
object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_ATTR_STACKADDR`` to indicate that this
routine is supported.

It is imperative to the proper operation of the system that
each thread have sufficient stack space.

pthread_attr_getstackaddr - Get Thread Stack Address
----------------------------------------------------
.. index:: pthread_attr_getstackaddr
.. index:: get thread stack address

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getstackaddr(
    const pthread_attr_t  \*attr,
    void                 \**stackaddr
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The stackaddr pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getstackaddr`` routine is used to obtain the``stackaddr`` attribute in the ``attr`` thread attribute
object.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_ATTR_STACKADDR`` to indicate that this
routine is supported.

pthread_attr_setscope - Set Thread Scheduling Scope
---------------------------------------------------
.. index:: pthread_attr_setscope
.. index:: set thread scheduling scope

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setscope(
    pthread_attr_t \*attr,
    int             contentionscope
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The contention scope specified is not valid.

*ENOTSUP*
    The contention scope specified (PTHREAD_SCOPE_SYSTEM) is not supported.

**DESCRIPTION:**

The ``pthread_attr_setscope`` routine is used to set the contention
scope field in the thread attribute object ``attr`` to the value
specified by ``contentionscope``.

The ``contentionscope`` must be either ``PTHREAD_SCOPE_SYSTEM``
to indicate that the thread is to be within system scheduling contention
or ``PTHREAD_SCOPE_PROCESS`` indicating that the thread is to be
within the process scheduling contention scope.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_getscope - Get Thread Scheduling Scope
---------------------------------------------------
.. index:: pthread_attr_getscope
.. index:: get thread scheduling scope

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getscope(
    const pthread_attr_t \*attr,
    int                  \*contentionscope
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The contentionscope pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getscope`` routine is used to obtain the
value of the contention scope field in the thread attributes
object ``attr``. The current value is returned in``contentionscope``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_setinheritsched - Set Inherit Scheduler Flag
---------------------------------------------------------
.. index:: pthread_attr_setinheritsched
.. index:: set inherit scheduler flag

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setinheritsched(
    pthread_attr_t \*attr,
    int             inheritsched
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The specified scheduler inheritance argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setinheritsched`` routine is used to set the
inherit scheduler field in the thread attribute object ``attr`` to
the value specified by ``inheritsched``.

The ``contentionscope`` must be either ``PTHREAD_INHERIT_SCHED``
to indicate that the thread is to inherit the scheduling policy
and parameters fromthe creating thread, or ``PTHREAD_EXPLICIT_SCHED``
to indicate that the scheduling policy and parameters for this thread
are to be set from the corresponding values in the attributes object.
If ``contentionscope`` is ``PTHREAD_INHERIT_SCHED``, then the
scheduling attributes in the ``attr`` structure will be ignored
at thread creation time.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_getinheritsched - Get Inherit Scheduler Flag
---------------------------------------------------------
.. index:: pthread_attr_getinheritsched
.. index:: get inherit scheduler flag

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getinheritsched(
    const pthread_attr_t \*attr,
    int                  \*inheritsched
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The inheritsched pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_getinheritsched`` routine is used to
object the current value of the inherit scheduler field in
the thread attribute object ``attr``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_setschedpolicy - Set Scheduling Policy
---------------------------------------------------
.. index:: pthread_attr_setschedpolicy
.. index:: set scheduling policy

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setschedpolicy(
    pthread_attr_t \*attr,
    int             policy
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*ENOTSUP*
    The specified scheduler policy argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setschedpolicy`` routine is used to set the
scheduler policy field in the thread attribute object ``attr`` to
the value specified by ``policy``.

Scheduling policies may be one of the following:

- ``SCHED_DEFAULT``

- ``SCHED_FIFO``

- ``SCHED_RR``

- ``SCHED_SPORADIC``

- ``SCHED_OTHER``

The precise meaning of each of these is discussed elsewhere in this
manual.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_getschedpolicy - Get Scheduling Policy
---------------------------------------------------
.. index:: pthread_attr_getschedpolicy
.. index:: get scheduling policy

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getschedpolicy(
    const pthread_attr_t \*attr,
    int                  \*policy
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The specified scheduler policy argument pointer is invalid.

**DESCRIPTION:**

The ``pthread_attr_getschedpolicy`` routine is used to obtain the
scheduler policy field from the thread attribute object ``attr``.
The value of this field is returned in ``policy``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_setschedparam - Set Scheduling Parameters
------------------------------------------------------
.. index:: pthread_attr_setschedparam
.. index:: set scheduling parameters

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_setschedparam(
    pthread_attr_t           \*attr,
    const struct sched_param  param
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The specified scheduler parameter argument is invalid.

**DESCRIPTION:**

The ``pthread_attr_setschedparam`` routine is used to set the
scheduler parameters field in the thread attribute object ``attr`` to
the value specified by ``param``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_getschedparam - Get Scheduling Parameters
------------------------------------------------------
.. index:: pthread_attr_getschedparam
.. index:: get scheduling parameters

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_attr_getschedparam(
    const pthread_attr_t \*attr,
    struct sched_param   \*param
    );

**STATUS CODES:**

*EINVAL*
    The attribute pointer argument is invalid.

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The specified scheduler parameter argument pointer is invalid.

**DESCRIPTION:**

The ``pthread_attr_getschedparam`` routine is used to obtain the
scheduler parameters field from the thread attribute object ``attr``.
The value of this field is returned in ``param``.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_attr_getaffinity_np - Get Thread Affinity Attribute
-----------------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_attr_getaffinity_np(
    const pthread_attr_t \*attr,
    size_t                cpusetsize,
    cpu_set_t            \*cpuset
    );

**STATUS CODES:**

*EFAULT*
    The attribute pointer argument is invalid.

*EFAULT*
    The cpuset pointer argument is invalid.

*EINVAL*
    The ``cpusetsize`` does not match the value of ``affinitysetsize``
    field in the thread attribute object.

**DESCRIPTION:**

The ``pthread_attr_getaffinity_np`` routine is used to obtain the``affinityset`` field from the thread attribute object ``attr``.
The value of this field is returned in ``cpuset``.

**NOTES:**

NONE

pthread_attr_setaffinity_np - Set Thread Affinity Attribute
-----------------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_attr_setaffinity_np(
    pthread_attr_t    \*attr,
    size_t             cpusetsize,
    const cpu_set_t   \*cpuset
    );

**STATUS CODES:**

*EFAULT*
    The attribute pointer argument is invalid.

*EFAULT*
    The cpuset pointer argument is invalid.

*EINVAL*
    The ``cpusetsize`` does not match the value of ``affinitysetsize``
    field in the thread attribute object.

*EINVAL*
    The ``cpuset`` did not select a valid cpu.

*EINVAL*
    The ``cpuset`` selected a cpu that was invalid.

**DESCRIPTION:**

The ``pthread_attr_setaffinity_np`` routine is used to set the``affinityset`` field in the thread attribute object ``attr``.
The value of this field is returned in ``cpuset``.

**NOTES:**

NONE

pthread_create - Create a Thread
--------------------------------
.. index:: pthread_create
.. index:: create a thread

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_create(
    pthread_t             \*thread,
    const pthread_attr_t  \*attr,
    void                 (\*start_routine)( void \*),
    void                  \*arg
    );

**STATUS CODES:**

*EINVAL*
    The attribute set is not initialized.

*EINVAL*
    The user specified a stack address and the size of the area was not
    large enough to meet this processor’s minimum stack requirements.

*EINVAL*
    The specified scheduler inheritance policy was invalid.

*ENOTSUP*
    The specified contention scope was PTHREAD_SCOPE_PROCESS.

*EINVAL*
    The specified thread priority was invalid.

*EINVAL*
    The specified scheduling policy was invalid.

*EINVAL*
    The scheduling policy was SCHED_SPORADIC and the specified replenishment
    period is less than the initial budget.

*EINVAL*
    The scheduling policy was SCHED_SPORADIC and the specified low priority
    is invalid.

*EAGAIN*
    The system lacked the necessary resources to create another thread, or the
    self imposed limit on the total number of threads in a process
    PTHREAD_THREAD_MAX would be exceeded.

*EINVAL*
    Invalid argument passed.

**DESCRIPTION:**

The ``pthread_create`` routine is used to create a new thread with
the attributes specified by ``attr``. If the ``attr`` argument
is ``NULL``, then the default attribute set will be used. Modification
of the contents of ``attr`` after this thread is created does not
have an impact on this thread.

The thread begins execution at the address specified by ``start_routine``
with ``arg`` as its only argument. If ``start_routine`` returns,
then it is functionally equivalent to the thread executing the``pthread_exit`` service.

Upon successful completion, the ID of the created thread is returned in the``thread`` argument.

**NOTES:**

There is no concept of a single main thread in RTEMS as there is in
a tradition UNIX system. POSIX requires that the implicit return of
the main thread results in the same effects as if there were a call
to ``exit``. This does not occur in RTEMS.

The signal mask of the newly created thread is inherited from its
creator and the set of pending signals for this thread is empty.

pthread_exit - Terminate the Current Thread
-------------------------------------------
.. index:: pthread_exit
.. index:: terminate the current thread

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    void pthread_exit(
    void \*status
    );

**STATUS CODES:**

*NONE*

**DESCRIPTION:**

The ``pthread_exit`` routine is used to terminate the calling thread.
The ``status`` is made available to any successful join with the
terminating thread.

When a thread returns from its start routine, it results in an
implicit call to the ``pthread_exit`` routine with the return
value of the function serving as the argument to ``pthread_exit``.

**NOTES:**

Any cancellation cleanup handlers that hace been pushed and not yet popped
shall be popped in reverse of the order that they were pushed. After
all cancellation cleanup handlers have been executed, if the
thread has any thread-specific data, destructors for that data will
be invoked.

Thread termination does not release or free any application visible
resources including byt not limited to mutexes, file descriptors, allocated
memory, etc.. Similarly, exitting a thread does not result in any
process-oriented cleanup activity.

There is no concept of a single main thread in RTEMS as there is in
a tradition UNIX system. POSIX requires that the implicit return of
the main thread results in the same effects as if there were a call
to ``exit``. This does not occur in RTEMS.

All access to any automatic variables allocated by the threads is lost
when the thread exits. Thus references (i.e. pointers) to local variables
of a thread should not be used in a global manner without care. As
a specific example, a pointer to a local variable should NOT be used
as the return value.

pthread_detach - Detach a Thread
--------------------------------
.. index:: pthread_detach
.. index:: detach a thread

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_detach(
    pthread_t thread
    );

**STATUS CODES:**

*ESRCH*
    The thread specified is invalid.

*EINVAL*
    The thread specified is not a joinable thread.

**DESCRIPTION:**

The ``pthread_detach`` routine is used to to indicate that storage
for ``thread`` can be reclaimed when the thread terminates without
another thread joinging with it.

**NOTES:**

If any threads have previously joined with the specified thread, then they
will remain joined with that thread. Any subsequent calls to``pthread_join`` on the specified thread will fail.

.. COMMENT: pthread_getattr_np

pthread_getattr_np - Get Thread Attributes
------------------------------------------
.. index:: pthread_getattr_np
.. index:: get thread attributes

**CALLING SEQUENCE:**

.. code:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_getattr_np(
    pthread_t       thread,
    pthread_attr_t \*attr
    );

**STATUS CODES:**

*ESRCH*
    The thread specified is invalid.

*EINVAL*
    The attribute pointer argument is invalid.

**DESCRIPTION:**

The ``pthread_getattr_np`` routine is used to obtain the
attributes associated with ``thread``.

**NOTES:**

Modification of the execution modes and priority through the Classic API
may result in a combination that is not representable in the POSIX API.

pthread_join - Wait for Thread Termination
------------------------------------------
.. index:: pthread_join
.. index:: wait for thread termination

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_join(
    pthread_t    thread,
    void       \**value_ptr
    );

**STATUS CODES:**

*ESRCH*
    The thread specified is invalid.

*EINVAL*
    The thread specified is not a joinable thread.

*EDEADLK*
    A deadlock was detected or thread is the calling thread.

**DESCRIPTION:**

The ``pthread_join`` routine suspends execution of the calling thread
until ``thread`` terminates. If ``thread`` has already terminated,
then this routine returns immediately. The value returned by ``thread``
(i.e. passed to ``pthread_exit`` is returned in ``value_ptr``.

When this routine returns, then ``thread`` has been terminated.

**NOTES:**

The results of multiple simultaneous joins on the same thread is undefined.

If any threads have previously joined with the specified thread, then they
will remain joined with that thread. Any subsequent calls to``pthread_join`` on the specified thread will fail.

If value_ptr is NULL, then no value is returned.

pthread_self - Get Thread ID
----------------------------
.. index:: pthread_self
.. index:: get thread id

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    pthread_t pthread_self( void );

**STATUS CODES:**

The value returned is the ID of the calling thread.

**DESCRIPTION:**

This routine returns the ID of the calling thread.

**NOTES:**

NONE

pthread_equal - Compare Thread IDs
----------------------------------
.. index:: pthread_equal
.. index:: compare thread ids

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_equal(
    pthread_t t1,
    pthread_t t2
    );

**STATUS CODES:**

*zero*
    The thread ids are not equal.

*non-zero*
    The thread ids are equal.

**DESCRIPTION:**

The ``pthread_equal`` routine is used to compare two thread
IDs and determine if they are equal.

**NOTES:**

The behavior is undefined if the thread IDs are not valid.

pthread_once - Dynamic Package Initialization
---------------------------------------------
.. index:: pthread_once
.. index:: dynamic package initialization

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    pthread_once_t once_control = PTHREAD_ONCE_INIT;
    int pthread_once(
    pthread_once_t   \*once_control,
    void            (\*init_routine)(void)
    );

**STATUS CODES:**

NONE

**DESCRIPTION:**

The ``pthread_once`` routine is used to provide controlled initialization
of variables. The first call to ``pthread_once`` by any thread with the
same ``once_control`` will result in the ``init_routine`` being
invoked with no arguments. Subsequent calls to ``pthread_once`` with
the same ``once_control`` will have no effect.

The ``init_routine`` is guaranteed to have run to completion when
this routine returns to the caller.

**NOTES:**

The behavior of ``pthread_once`` is undefined if ``once_control``
is automatic storage (i.e. on a task stack) or is not initialized using``PTHREAD_ONCE_INIT``.

pthread_setschedparam - Set Thread Scheduling Parameters
--------------------------------------------------------
.. index:: pthread_setschedparam
.. index:: set thread scheduling parameters

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_setschedparam(
    pthread_t           thread,
    int                 policy,
    struct sched_param \*param
    );

**STATUS CODES:**

*EINVAL*
    The scheduling parameters indicated by the parameter param is invalid.

*EINVAL*
    The value specified by policy is invalid.

*EINVAL*
    The scheduling policy was SCHED_SPORADIC and the specified replenishment
    period is less than the initial budget.

*EINVAL*
    The scheduling policy was SCHED_SPORADIC and the specified low priority
    is invalid.

*ESRCH*
    The thread indicated was invalid.

**DESCRIPTION:**

The ``pthread_setschedparam`` routine is used to set the
scheduler parameters currently associated with the thread specified
by ``thread`` to the policy specified by ``policy``. The
contents of ``param`` are interpreted based upon the ``policy``
argument.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

pthread_getschedparam - Get Thread Scheduling Parameters
--------------------------------------------------------
.. index:: pthread_getschedparam
.. index:: get thread scheduling parameters

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_getschedparam(
    pthread_t           thread,
    int                \*policy,
    struct sched_param \*param
    );

**STATUS CODES:**

*EINVAL*
    The policy pointer argument is invalid.

*EINVAL*
    The scheduling parameters pointer argument is invalid.

*ESRCH*
    The thread indicated by the parameter thread is invalid.

**DESCRIPTION:**

The ``pthread_getschedparam`` routine is used to obtain the
scheduler policy and parameters associated with ``thread``.
The current policy and associated parameters values returned in``policy`` and ``param``, respectively.

**NOTES:**

As required by POSIX, RTEMS defines the feature symbol``_POSIX_THREAD_PRIORITY_SCHEDULING`` to indicate that the
family of routines to which this routine belongs is supported.

.. COMMENT: pthread_getaffinity_np

pthread_getaffinity_np - Get Thread Affinity
--------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_getaffinity_np(
    const pthread_t       id,
    size_t                cpusetsize,
    cpu_set_t            \*cpuset
    );

**STATUS CODES:**

*EFAULT*
    The cpuset pointer argument is invalid.

*EINVAL*
    The ``cpusetsize`` does not match the value of ``affinitysetsize``
    field in the thread attribute object.

**DESCRIPTION:**

The ``pthread_getaffinity_np`` routine is used to obtain the``affinity.set`` field from the thread control object associated
with the ``id``.  The value of this field is returned in ``cpuset``.

**NOTES:**

NONE

.. COMMENT: pthread_setaffinity_np

pthread_setaffinity_np - Set Thread Affinity
--------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #define _GNU_SOURCE
    #include <pthread.h>
    int pthread_setaffinity_np(
    pthread_t          id,
    size_t             cpusetsize,
    const cpu_set_t   \*cpuset
    );

**STATUS CODES:**

*EFAULT*
    The cpuset pointer argument is invalid.

*EINVAL*
    The ``cpusetsize`` does not match the value of ``affinitysetsize``
    field in the thread attribute object.

*EINVAL*
    The ``cpuset`` did not select a valid cpu.

*EINVAL*
    The ``cpuset`` selected a cpu that was invalid.

**DESCRIPTION:**

The ``pthread_setaffinity_np`` routine is used to set the``affinityset`` field of the thread object ``id``.
The value of this field is returned in ``cpuset``

**NOTES:**

NONE

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Key Manager
###########

Introduction
============

The key manager allows for the creation and deletion of Data keys
specific to threads.

The directives provided by the key manager are:

- ``pthread_key_create`` - Create Thread Specific Data Key

- ``pthread_key_delete`` - Delete Thread Specific Data Key

- ``pthread_setspecific`` - Set Thread Specific Key Value

- ``pthread_getspecific`` - Get Thread Specific Key Value

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the key manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

pthread_key_create - Create Thread Specific Data Key
----------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_key_create(
    pthread_key_t \*key,
    void (\*destructor)( void )
    );

**STATUS CODES:**

*EAGAIN*
    There were not enough resources available to create another key.

*ENOMEM*
    Insufficient memory exists to create the key.

**DESCRIPTION**

The pthread_key_create() function shall create a thread-specific data
key visible to all threads in the process. Key values provided by
pthread_key_create() are opaque objects used to locate thread-specific
data. Although the same key value may be used by different threads, the
values bound to the key by pthread_setspecific() are maintained on a
per-thread basis and persist for the life of the calling thread.

Upon key creation, the value NULL shall be associated with the new key
in all active threads. Upon thread creation, the value NULL shall be
associated with all defined keys in the new thread.

**NOTES**

An optional destructor function may be associated with each key value.
At thread exit, if a key value has a non-NULL destructor pointer, and
the thread has a non-NULL value associated with that key, the value of
the key is set to NULL, and then the function pointed to is called with
the previously associated value as its sole argument. The order of
destructor calls is unspecified if more than one destructor exists for
a thread when it exits.

pthread_key_delete - Delete Thread Specific Data Key
----------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_key_delete(
    pthread_key_t key);

**STATUS CODES:**

*EINVAL*
    The key was invalid

**DESCRIPTION:**

The pthread_key_delete() function shall delete a thread-specific data key
previously returned by pthread_key_create(). The thread-specific data
values associated with key need not be NULL at the time pthread_key_delete()
is called. It is the responsibility of the application to free any
application storage or perform any cleanup actions for data structures related
to the deleted key or associated thread-specific data in any
threads; this cleanup can be done either before or after
pthread_key_delete() is called. Any attempt to use key following the call to
pthread_key_delete() results in undefined behavior.

**NOTES:**

The pthread_key_delete() function shall be callable from within
destructor functions. No destructor functions shall be invoked by
pthread_key_delete(). Any destructor function that may have been
associated with key shall no longer be called upon thread exit.

pthread_setspecific - Set Thread Specific Key Value
---------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    int pthread_setspecific(
    pthread_key_t key,
    const void \*value
    );

**STATUS CODES:**

*EINVAL*
    The specified key is invalid.

**DESCRIPTION:**

The pthread_setspecific() function shall associate a thread-specific value
with a key obtained via a previous call to pthread_key_create().
Different threads may bind different values to the same key. These values
are typically pointers to blocks of dynamically allocated memory that
have been reserved for use by the calling thread.

**NOTES:**

The effect of calling pthread_setspecific() with a key value not obtained
from pthread_key_create() or after key has
been deleted with pthread_key_delete() is undefined.

pthread_setspecific() may be called from a thread-specific data
destructor function. Calling pthread_setspecific() from a thread-specific
data destructor routine may result either in lost storage (after at least
PTHREAD_DESTRUCTOR_ITERATIONS attempts at destruction) or in an infinite loop.

pthread_getspecific - Get Thread Specific Key Value
---------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    #include <pthread.h>
    void \*pthread_getspecific(
    pthread_key_t key
    );

**STATUS CODES:**

*NULL*
    There is no thread-specific data associated with the specified key.

*non-NULL*
    The data associated with the specified key.

**DESCRIPTION:**

The pthread_getspecific() function shall return the value currently bound to
the specified key on behalf of the calling thread.

**NOTES:**

The effect of calling pthread_getspecific() with a key value not obtained from
pthread_key_create() or after key has
been deleted with pthread_key_delete() is undefined.

pthread_getspecific() may be called from a thread-specific data destructor
function. A call to pthread_getspecific() for the thread-specific data key
being destroyed shall return the value NULL, unless the value is changed
(after the destructor starts) by a call to pthread_setspecific().

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Thread Cancellation Manager
###########################

Introduction
============

The
thread cancellation manager is ...

The directives provided by the thread cancellation manager are:

- ``pthread_cancel`` - Cancel Execution of a Thread

- ``pthread_setcancelstate`` - Set Cancelability State

- ``pthread_setcanceltype`` - Set Cancelability Type

- ``pthread_testcancel`` - Create Cancellation Point

- ``pthread_cleanup_push`` - Establish Cancellation Handler

- ``pthread_cleanup_pop`` - Remove Cancellation Handler

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the thread cancellation manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

pthread_cancel - Cancel Execution of a Thread
---------------------------------------------
.. index:: pthread_cancel
.. index:: cancel execution of a thread

**CALLING SEQUENCE:**

.. code:: c

    int pthread_cancel(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

pthread_setcancelstate - Set Cancelability State
------------------------------------------------
.. index:: pthread_setcancelstate
.. index:: set cancelability state

**CALLING SEQUENCE:**

.. code:: c

    int pthread_setcancelstate(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

pthread_setcanceltype - Set Cancelability Type
----------------------------------------------
.. index:: pthread_setcanceltype
.. index:: set cancelability type

**CALLING SEQUENCE:**

.. code:: c

    int pthread_setcanceltype(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

pthread_testcancel - Create Cancellation Point
----------------------------------------------
.. index:: pthread_testcancel
.. index:: create cancellation point

**CALLING SEQUENCE:**

.. code:: c

    int pthread_testcancel(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

pthread_cleanup_push - Establish Cancellation Handler
-----------------------------------------------------
.. index:: pthread_cleanup_push
.. index:: establish cancellation handler

**CALLING SEQUENCE:**

.. code:: c

    int pthread_cleanup_push(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

pthread_cleanup_pop - Remove Cancellation Handler
-------------------------------------------------
.. index:: pthread_cleanup_pop
.. index:: remove cancellation handler

**CALLING SEQUENCE:**

.. code:: c

    int pthread_cleanup_push(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Services Provided by C Library (libc)
#####################################

Introduction
============

This section lists the routines that provided by the Newlib C Library.

Standard Utility Functions (stdlib.h)
=====================================

- ``abort`` - Abnormal termination of a program

- ``abs`` - Integer absolute value (magnitude)

- ``assert`` - Macro for Debugging Diagnostics

- ``atexit`` - Request execution of functions at program exit

- ``atof`` - String to double or float

- ``atoi`` - String to integer

- ``bsearch`` - Binary search

- ``calloc`` - Allocate space for arrays

- ``div`` - Divide two integers

- ``ecvtbuf`` - Double or float to string of digits

- ``ecvt`` - Double or float to string of digits (malloc result)

- ``__env_lock`` - Lock environment list for getenv and setenv

- ``gvcvt`` - Format double or float as string

- ``exit`` - End program execution

- ``getenv`` - Look up environment variable

- ``labs`` - Long integer absolute value (magnitude)

- ``ldiv`` - Divide two long integers

- ``malloc`` - Allocate memory

- ``realloc`` - Reallocate memory

- ``free`` - Free previously allocated memory

- ``mallinfo`` - Get information about allocated memory

- ``__malloc_lock`` - Lock memory pool for malloc and free

- ``mbstowcs`` - Minimal multibyte string to wide string converter

- ``mblen`` - Minimal multibyte length

- ``mbtowc`` - Minimal multibyte to wide character converter

- ``qsort`` - Sort an array

- ``rand`` - Pseudo-random numbers

- ``strtod`` - String to double or float

- ``strtol`` - String to long

- ``strtoul`` - String to unsigned long

- ``system`` - Execute command string

- ``wcstombs`` - Minimal wide string to multibyte string converter

- ``wctomb`` - Minimal wide character to multibyte converter

Character Type Macros and Functions (ctype.h)
=============================================

- ``isalnum`` - Alphanumeric character predicate

- ``isalpha`` - Alphabetic character predicate

- ``isascii`` - ASCII character predicate

- ``iscntrl`` - Control character predicate

- ``isdigit`` - Decimal digit predicate

- ``islower`` - Lower-case character predicate

- ``isprint`` - Printable character predicates (isprint, isgraph)

- ``ispunct`` - Punctuation character predicate

- ``isspace`` - Whitespace character predicate

- ``isupper`` - Uppercase character predicate

- ``isxdigit`` - Hexadecimal digit predicate

- ``toascii`` - Force integers to ASCII range

- ``tolower`` - Translate characters to lower case

- ``toupper`` - Translate characters to upper case

Input and Output (stdio.h)
==========================

- ``clearerr`` - Clear file or stream error indicator

- ``fclose`` - Close a file

- ``feof`` - Test for end of file

- ``ferror`` - Test whether read/write error has occurred

- ``fflush`` - Flush buffered file output

- ``fgetc`` - Get a character from a file or stream

- ``fgetpos`` - Record position in a stream or file

- ``fgets`` - Get character string from a file or stream

- ``fiprintf`` - Write formatted output to file (integer only)

- ``fopen`` - Open a file

- ``fdopen`` - Turn an open file into a stream

- ``fputc`` - Write a character on a stream or file

- ``fputs`` - Write a character string in a file or stream

- ``fread`` - Read array elements from a file

- ``freopen`` - Open a file using an existing file descriptor

- ``fseek`` - Set file position

- ``fsetpos`` - Restore position of a stream or file

- ``ftell`` - Return position in a stream or file

- ``fwrite`` - Write array elements from memory to a file or stream

- ``getc`` - Get a character from a file or stream (macro)

- ``getchar`` - Get a character from standard input (macro)

- ``gets`` - Get character string from standard input (obsolete)

- ``iprintf`` - Write formatted output (integer only)

- ``mktemp`` - Generate unused file name

- ``perror`` - Print an error message on standard error

- ``putc`` - Write a character on a stream or file (macro)

- ``putchar`` - Write a character on standard output (macro)

- ``puts`` - Write a character string on standard output

- ``remove`` - Delete a file’s name

- ``rename`` - Rename a file

- ``rewind`` - Reinitialize a file or stream

- ``setbuf`` - Specify full buffering for a file or stream

- ``setvbuf`` - Specify buffering for a file or stream

- ``siprintf`` - Write formatted output (integer only)

- ``printf`` - Write formatted output

- ``scanf`` - Scan and format input

- ``tmpfile`` - Create a temporary file

- ``tmpnam`` - Generate name for a temporary file

- ``vprintf`` - Format variable argument list

Strings and Memory (string.h)
=============================

- ``bcmp`` - Compare two memory areas

- ``bcopy`` - Copy memory regions

- ``bzero`` - Initialize memory to zero

- ``index`` - Search for character in string

- ``memchr`` - Find character in memory

- ``memcmp`` - Compare two memory areas

- ``memcpy`` - Copy memory regions

- ``memmove`` - Move possibly overlapping memory

- ``memset`` - Set an area of memory

- ``rindex`` - Reverse search for character in string

- ``strcasecmp`` - Compare strings ignoring case

- ``strcat`` - Concatenate strings

- ``strchr`` - Search for character in string

- ``strcmp`` - Character string compare

- ``strcoll`` - Locale specific character string compare

- ``strcpy`` - Copy string

- ``strcspn`` - Count chars not in string

- ``strerror`` - Convert error number to string

- ``strlen`` - Character string length

- ``strlwr`` - Convert string to lower case

- ``strncasecmp`` - Compare strings ignoring case

- ``strncat`` - Concatenate strings

- ``strncmp`` - Character string compare

- ``strncpy`` - Counted copy string

- ``strpbrk`` - Find chars in string

- ``strrchr`` - Reverse search for character in string

- ``strspn`` - Find initial match

- ``strstr`` - Find string segment

- ``strtok`` - Get next token from a string

- ``strupr`` - Convert string to upper case

- ``strxfrm`` - Transform string

Signal Handling (signal.h)
==========================

- ``raise`` - Send a signal

- ``signal`` - Specify handler subroutine for a signal

Time Functions (time.h)
=======================

- ``asctime`` - Format time as string

- ``clock`` - Cumulative processor time

- ``ctime`` - Convert time to local and format as string

- ``difftime`` - Subtract two times

- ``gmtime`` - Convert time to UTC (GMT) traditional representation

- ``localtime`` - Convert time to local representation

- ``mktime`` - Convert time to arithmetic representation

- ``strftime`` - Flexible calendar time formatter

- ``time`` - Get current calendar time (as single number)

Locale (locale.h)
=================

- ``setlocale`` - Select or query locale

Reentrant Versions of Functions
===============================

- Equivalent for errno variable:
  - ``errno_r`` - XXX

- Locale functions:
  - ``localeconv_r`` - XXX
  - ``setlocale_r`` - XXX

- Equivalents for stdio variables:
  - ``stdin_r`` - XXX
  - ``stdout_r`` - XXX
  - ``stderr_r`` - XXX

- Stdio functions:
  - ``fdopen_r`` - XXX
  - ``perror_r`` - XXX
  - ``tempnam_r`` - XXX
  - ``fopen_r`` - XXX
  - ``putchar_r`` - XXX
  - ``tmpnam_r`` - XXX
  - ``getchar_r`` - XXX
  - ``puts_r`` - XXX
  - ``tmpfile_r`` - XXX
  - ``gets_r`` - XXX
  - ``remove_r`` - XXX
  - ``vfprintf_r`` - XXX
  - ``iprintf_r`` - XXX
  - ``rename_r`` - XXX
  - ``vsnprintf_r`` - XXX
  - ``mkstemp_r`` - XXX
  - ``snprintf_r`` - XXX
  - ``vsprintf_r`` - XXX
  - ``mktemp_t`` - XXX
  - ``sprintf_r`` - XXX

- Signal functions:
  - ``init_signal_r`` - XXX
  - ``signal_r`` - XXX
  - ``kill_r`` - XXX
  - ``_sigtramp_r`` - XXX
  - ``raise_r`` - XXX

- Stdlib functions:
  - ``calloc_r`` - XXX
  - ``mblen_r`` - XXX
  - ``srand_r`` - XXX
  - ``dtoa_r`` - XXX
  - ``mbstowcs_r`` - XXX
  - ``strtod_r`` - XXX
  - ``free_r`` - XXX
  - ``mbtowc_r`` - XXX
  - ``strtol_r`` - XXX
  - ``getenv_r`` - XXX
  - ``memalign_r`` - XXX
  - ``strtoul_r`` - XXX
  - ``mallinfo_r`` - XXX
  - ``mstats_r`` - XXX
  - ``system_r`` - XXX
  - ``malloc_r`` - XXX
  - ``rand_r`` - XXX
  - ``wcstombs_r`` - XXX
  - ``malloc_r`` - XXX
  - ``realloc_r`` - XXX
  - ``wctomb_r`` - XXX
  - ``malloc_stats_r`` - XXX
  - ``setenv_r`` - XXX

- String functions:
  - ``strtok_r`` - XXX

- System functions:
  - ``close_r`` - XXX
  - ``link_r`` - XXX
  - ``unlink_r`` - XXX
  - ``execve_r`` - XXX
  - ``lseek_r`` - XXX
  - ``wait_r`` - XXX
  - ``fcntl_r`` - XXX
  - ``open_r`` - XXX
  - ``write_r`` - XXX
  - ``fork_r`` - XXX
  - ``read_r`` - XXX
  - ``fstat_r`` - XXX
  - ``sbrk_r`` - XXX
  - ``gettimeofday_r`` - XXX
  - ``stat_r`` - XXX
  - ``getpid_r`` - XXX
  - ``times_r`` - XXX

- Time function:
  - ``asctime_r`` - XXX

Miscellaneous Macros and Functions
==================================

- ``unctrl`` - Return printable representation of a character

Variable Argument Lists
=======================

- Stdarg (stdarg.h):
  - ``va_start`` - XXX
  - ``va_arg`` - XXX
  - ``va_end`` - XXX

- Vararg (varargs.h):
  - ``va_alist`` - XXX
  - ``va_start-trad`` - XXX
  - ``va_arg-trad`` - XXX
  - ``va_end-trad`` - XXX

Reentrant System Calls
======================

- ``open_r`` - XXX

- ``close_r`` - XXX

- ``lseek_r`` - XXX

- ``read_r`` - XXX

- ``write_r`` - XXX

- ``fork_r`` - XXX

- ``wait_r`` - XXX

- ``stat_r`` - XXX

- ``fstat_r`` - XXX

- ``link_r`` - XXX

- ``unlink_r`` - XXX

- ``sbrk_r`` - XXX

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Services Provided by the Math Library (libm)
############################################

Introduction
============

This section lists the routines that provided by the Newlib Math Library
(libm).

Standard Math Functions (math.h)
================================

- ``acos`` - Arccosine

- ``acosh`` - Inverse hyperbolic cosine

- ``asin`` - Arcsine

- ``asinh`` - Inverse hyperbolic sine

- ``atan`` - Arctangent

- ``atan2`` - Arctangent of y/x

- ``atanh`` - Inverse hyperbolic tangent

- ``jN`` - Bessel functions (jN and yN)

- ``cbrt`` - Cube root

- ``copysign`` - Sign of Y and magnitude of X

- ``cosh`` - Hyperbolic cosine

- ``erf`` - Error function (erf and erfc)

- ``exp`` - Exponential

- ``expm1`` - Exponential of x and - 1

- ``fabs`` - Absolute value (magnitude)

- ``floor`` - Floor and ceiling (floor and ceil)

- ``fmod`` - Floating-point remainder (modulo)

- ``frexp`` - Split floating-point number

- ``gamma`` - Logarithmic gamma function

- ``hypot`` - Distance from origin

- ``ilogb`` - Get exponent

- ``infinity`` - Floating infinity

- ``isnan`` - Check type of number

- ``ldexp`` - Load exponent

- ``log`` - Natural logarithms

- ``log10`` - Base 10 logarithms

- ``log1p`` - Log of 1 + X

- ``matherr`` - Modifiable math error handler

- ``modf`` - Split fractional and integer parts

- ``nan`` - Floating Not a Number

- ``nextafter`` - Get next representable number

- ``pow`` - X to the power Y

- ``remainder`` - remainder of X divided by Y

- ``scalbn`` - scalbn

- ``sin`` - Sine or cosine (sin and cos)

- ``sinh`` - Hyperbolic sine

- ``sqrt`` - Positive square root

- ``tan`` - Tangent

- ``tanh`` - Hyperbolic tangent

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Status of Implementation
########################

This chapter provides an overview of the status of the implementation
of the POSIX API for RTEMS.  The *POSIX 1003.1b Compliance Guide*
provides more detailed information regarding the implementation of
each of the numerous functions, constants, and macros specified by
the POSIX 1003.1b standard.

RTEMS supports many of the process and user/group oriented services
in a "single user/single process" manner.  This means that although
these services may be of limited usefulness or functionality, they
are provided and do work in a coherent manner.  This is significant
when porting existing code from UNIX to RTEMS.

- Implementation
  - The current implementation of ``dup()`` is insufficient.
  - FIFOs ``mkfifo()`` are not currently implemented.
  - Asynchronous IO is not implemented.
  - The ``flockfile()`` family is not implemented
  - getc/putc unlocked family is not implemented
  - Shared Memory is not implemented
  - Mapped Memory is not implemented

  - NOTES:

    - For Shared Memory and Mapped Memory services, it is unclear what
      level of support is appropriate and possible for RTEMS.

- Functional Testing
  - Tests for unimplemented services

- Performance Testing
  - There are no POSIX Performance Tests.

- Documentation

  - Many of the service description pages are not complete in this
    manual.  These need to be completed and information added to the
    background and operations sections.

  - Example programs (not just tests) would be very nice.

Command and Variable Index
##########################

.. COMMENT: There are currently no Command and Variable Index entries.

Concept Index
#############

.. COMMENT: There are currently no Concept Index entries.

