.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Process Primitives
##################

Process Creation and Execution
==============================

Process Creation
----------------

.. code:: c

    fork(), Function, Unimplementable, Requires Processes

Execute a File
--------------

.. code:: c

    execl(), Function, Unimplementable, Requires Processes
    execv(), Function, Unimplementable, Requires Processes
    execle(), Function, Unimplementable, Requires Processes
    execve(), Function, Unimplementable, Requires Processes
    execlp(), Function, Unimplementable, Requires Processes
    execvp(), Function, Unimplementable, Requires Processes

Register Fork Handlers
----------------------

.. code:: c

    pthread_atfork(), Function, Unimplementable, Requires Processes

Process Termination
===================

Wait for Process Termination
----------------------------

.. code:: c

    wait(), Function, Unimplementable, Requires Processes
    waitpid(), Function, Unimplementable, Requires Processes
    WNOHANG, Constant, Unimplementable, Requires Processes
    WUNTRACED, Constant, Unimplementable, Requires Processes
    WIFEXITED(), Function, Unimplementable, Requires Processes
    WEXITSTATUS(), Function, Unimplementable, Requires Processes
    WIFSIGNALED(), Function, Unimplementable, Requires Processes
    WTERMSIG(), Function, Unimplementable, Requires Processes
    WIFSTOPPED(), Function, Unimplementable, Requires Processes
    WSTOPSIG(), Function, Unimplementable, Requires Processes

Terminate a Process
-------------------

.. code:: c

    _exit(), Function, Implemented

Signals
=======

Signal Concepts
---------------

Signal Names
~~~~~~~~~~~~

.. code:: c

    sigset_t, Type, Implemented
    SIG_DFL, Constant, Implemented
    SIG_IGN, Constant, Implemented
    SIG_ERR, Constant, Implemented
    SIGABRT, Constant, Implemented
    SIGALRM, Constant, Implemented
    SIGFPE, Constant, Implemented
    SIGHUP, Constant, Implemented
    SIGILL, Constant, Implemented
    SIGINT, Constant, Implemented
    SIGKILL, Constant, Implemented
    SIGPIPE, Constant, Implemented
    SIGQUIT, Constant, Implemented
    SIGSEGV, Constant, Implemented
    SIGTERM, Constant, Implemented
    SIGUSR1, Constant, Implemented
    SIGUSR2, Constant, Implemented
    SIGCHLD, Constant, Unimplemented
    SIGCONT, Constant, Unimplemented
    SIGSTOP, Constant, Unimplemented
    SIGTSTP, Constant, Unimplemented
    SIGTTIN, Constant, Unimplemented
    SIGTTOU, Constant, Unimplemented
    SIGBUS, Constant, Implemented
    SIGRTMIN, Constant, Implemented
    SIGRTMAX, Constant, Implemented

NOTE: SIG_ERR is technically an extension to the C Library which is
not documented anywhere else according to the index.

Signal Generation and Delivery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    struct sigevent, Type, Implemented
    union sigval, Type, Implemented
    SIGEV_NONE, Constant, Implemented
    SIGEV_SIGNAL, Constant, Implemented
    SIGEV_THREAD, Constant, Implemented

Signal Actions
~~~~~~~~~~~~~~

.. code:: c

    siginfo_t, Type, Implemented
    SI_USER, Constant, Implemented
    SI_QUEUE, Constant, Implemented
    SI_TIMER, Constant, Implemented
    SI_ASYNCIO, Constant, Implemented
    SI_MESGQ, Constant, Implemented

Send a Signal to a Process
--------------------------

.. code:: c

    kill(), Function, Implemented

Manipulate Signal Sets
----------------------

.. code:: c

    sigemptyset(), Function, Implemented
    sigfillset(), Function, Implemented
    sigaddset(), Function, Implemented
    sigdelset(), Function, Implemented
    sigismember(), Function, Implemented

Examine and Change Signal Action
--------------------------------

.. code:: c

    sigaction(), Function, Implemented
    sigaction, Type, Implemented
    SA_NOCLDSTOP, Constant, Implemented
    SA_SIGINFO, Constant, Implemented

Examine and Change Blocked Signals
----------------------------------

.. code:: c

    pthread_sigmask(), Function, Implemented
    sigprocmask(), Function, Implemented
    SIG_BLOCK, Constant, Implemented
    SIG_UNBLOCK, Constant, Implemented
    SIG_SETMASK, Constant, Implemented

Examine Pending Signals
-----------------------

.. code:: c

    sigpending(), Function, Implemented

Wait for a Signal
-----------------

.. code:: c

    sigsuspend(), Function, Implemented

Synchronously Accept a Signal
-----------------------------

.. code:: c

    sigwait(), Function, Implemented
    sigwaitinfo(), Function, Implemented
    sigtimedwait(), Function, Implemented

Queue a Signal to a Process
---------------------------

.. code:: c

    sigqueue(), Function, Implemented

Send a Signal to a Thread
-------------------------

.. code:: c

    pthread_kill(), Function, Implemented

Timer Operations
================

Schedule Alarm
--------------

.. code:: c

    alarm(), Function, Implemented

Suspend Process Execution
-------------------------

.. code:: c

    pause(), Function, Implemented

Delay Process Execution
-----------------------

.. code:: c

    sleep(), Function, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

