.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Process Environment
###################

Process Identification
======================

Get Process and Parent Process IDs
----------------------------------

.. code:: c

    getpid(), Function, Implemented, SUSP Functionality
    getppid(), Function, Implemented, SUSP Functionality

User Identification
===================

Get Real User Effective User Real Group and Effective Group IDs
---------------------------------------------------------------

.. code:: c

    getuid(), Function, Implemented, SUSP Functionality
    geteuid(), Function, Implemented, SUSP Functionality
    getgid(), Function, Implemented, SUSP Functionality
    getegid(), Function, Implemented, SUSP Functionality

Set User and Group IDs
----------------------

.. code:: c

    setuid(), Function, Implemented, SUSP Functionality
    setgid(), Function, Implemented, SUSP Functionality

Get Supplementary Group IDs
---------------------------

.. code:: c

    getgroups(), Function, Implemented, SUSP Functionality

Get User Name
-------------

.. code:: c

    getlogin(), Function, Implemented, SUSP Functionality
    getlogin_r(), Function, Implemented, SUSP Functionality

Process Groups
==============

Get Process Group ID
--------------------

.. code:: c

    getpgrp(), Function, Implemented, SUSP Functionality

Create Session and Set Process Group ID
---------------------------------------

.. code:: c

    setsid(), Function, Implemented, SUSP Functionality

Set Process Group ID for Job Control
------------------------------------

.. code:: c

    setpgid(), Function, Dummy Implementation

System Identification
=====================

Get System Name
---------------

.. code:: c

    struct utsname, Type, Implemented
    uname(), Function, Implemented

Time
====

Get System Time
---------------

.. code:: c

    time(), Function, Implemented

Get Process Times
-----------------

.. code:: c

    struct tms, Type, Implemented
    times(), Function, Implemented

NOTE: ``times`` always returns 0 for tms_stime, tms_cutime, and
tms_cstime fields of the ``struct tms`` returned.

Environment Variables
=====================

Environment Access
------------------

.. code:: c

    getenv(), Function, Implemented

Terminal Identification
=======================

Generate Terminal Pathname
--------------------------

.. code:: c

    ctermid(), Function, Implemented

Determine Terminal Device Name
------------------------------

.. code:: c

    ttyname(), Function, Implemented, untested
    ttyname_r(), Function, Implemented, untested
    isatty(), Function, Implemented

Configurable System Variables
=============================

Get Configurable System Variables
---------------------------------

.. code:: c

    sysconf(), Function, Dummy Implementation
    _SC_AIO_LISTIO_MAX, Constant, Implemented
    _SC_AIO_MAX, Constant, Implemented
    _SC_AIO_PRIO_DELTA_MAX, Constant, Implemented
    _SC_ARG_MAX, Constant, Implemented
    _SC_CHILD_MAX, Constant, Implemented
    _SC_CLK_TCK, Constant, Implemented
    CLK_TCK, Constant, Implemented
    _SC_DELAYTIMER_MAX, Constant, Implemented
    _SC_GETGR_R_SIZE_MAX, Constant, Implemented
    _SC_GETPW_R_SIZE_MAX, Constant, Implemented
    _SC_LOGIN_NAME_MAX, Constant, Implemented
    _SC_MQ_OPEN_MAX, Constant, Implemented
    _SC_MQ_PRIO_MAX, Constant, Implemented
    _SC_NGROUPS_MAX, Constant, Implemented
    _SC_OPEN_MAX, Constant, Implemented
    _SC_PAGESIZE, Constant, Implemented
    _SC_RTSIG_MAX, Constant, Implemented
    _SC_SEM_NSEMS_MAX, Constant, Implemented
    _SC_SEM_VALUE_MAX, Constant, Implemented
    _SC_SIGQUEUE_MAX, Constant, Implemented
    _SC_STREAM_MAX, Constant, Implemented
    _SC_THREAD_DESTRUCTOR_ITERATIONS, Constant, Implemented
    _SC_THREAD_KEYS_MAX, Constant, Implemented
    _SC_THREAD_STACK_MIN, Constant, Implemented
    _SC_THREAD_THREADS_MAX, Constant, Implemented
    _SC_TIMER_MAX, Constant, Implemented
    _SC_TTY_NAME_MAX, Constant, Implemented
    _SC_TZNAME_MAX, Constant, Implemented
    _SC_ASYNCHRONOUS_IO, Constant, Implemented
    _SC_FSYNC, Constant, Implemented
    _SC_JOB_CONROL, Constant, Implemented
    _SC_MAPPED_FILES, Constant, Implemented
    _SC_MEMLOCK, Constant, Implemented
    _SC_MEMLOCK_RANGE, Constant, Implemented
    _SC_MEMORY_PROTECTION, Constant, Implemented
    _SC_MESSAGE_PASSING, Constant, Implemented
    _SC_PRIORITIZED_IO, Constant, Implemented
    _SC_PRIORITY_SCHEDULING, Constant, Unimplemented
    _SC_REALTIME_SIGNALS, Constant, Implemented
    _SC_SAVED_IDS, Constant, Implemented
    _SC_SEMAPHORES, Constant, Implemented
    _SC_SHARED_MEMORY_OBJECTS, Constant, Implemented
    _SC_SYNCHRONIZED_IO, Constant, Implemented
    _SC_TIMERS, Constant, Implemented
    _SC_THREADS, Constant, Implemented
    _SC_THREAD_ATTR_STACKADDR, Constant, Implemented
    _SC_THREAD_ATTR_STACKSIZE, Constant, Implemented
    _SC_THREAD_PRIORITY_SCHEDULING, Constant, Implemented
    _SC_THREAD_PRIO_INHERIT, Constant, Implemented
    _SC_THREAD_PRIO_PROTECT, Constant, Unimplemented
    _SC_THREAD_PROCESS_SHARED, Constant, Implemented
    _SC_THREAD_SAFE_FUNCTIONS, Constant, Implemented
    _SC_VERSION, Constant, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

