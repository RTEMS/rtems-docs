Execution Scheduling
####################

Scheduling Parameters
=====================

.. code:: c

    struct sched_param, Type, Implemented

Scheduling Policies
===================

.. code:: c

    SCHED_FIFO, Constant, Implemented
    SCHED_RR, Constant, Implemented
    SCHED_OTHER, Constant, Implemented

NOTE: RTEMS adds SCHED_SPORADIC.

SCHED_FIFO
----------

SCHED_RR
--------

SCHED_OTHER
-----------

Process Scheduling Functions
============================

Set Scheduling Parameters
-------------------------

.. code:: c

    sched_setparam(), Function, Dummy Implementation

Get Scheduling Parameters
-------------------------

.. code:: c

    sched_getparam(), Function, Dummy Implementation

Set Scheduling Policy and Scheduling Parameters
-----------------------------------------------

.. code:: c

    sched_setscheduler(), Function, Dummy Implementation

Get Scheduling Policy
---------------------

.. code:: c

    sched_getscheduler(), Function, Dummy Implementation

Yield Processor
---------------

.. code:: c

    sched_yield(), Function, Implemented

Get Scheduling Parameter Limits
-------------------------------

.. code:: c

    sched_get_priority_max(), Function, Implemented
    sched_get_priority_min(), Function, Implemented
    sched_get_priority_rr_get_interval(), Function, Implemented

Thread Scheduling
=================

Thread Scheduling Attributes
----------------------------

.. code:: c

    PTHREAD_SCOPE_PROCESS, Constant, Implemented
    PTHREAD_SCOPE_SYSTEM, Constant, Implemented

Scheduling Contention Scope
---------------------------

Scheduling Allocation Domain
----------------------------

Scheduling Documentation
------------------------

Thread Scheduling Functions
===========================

Thread Creation Scheduling Attributes
-------------------------------------

.. code:: c

    pthread_attr_setscope(), Function, Implemented
    pthread_attr_getscope(), Function, Implemented
    pthread_attr_setinheritsched(), Function, Implemented
    pthread_attr_getinheritsched(), Function, Implemented
    pthread_attr_setschedpolicy(), Function, Implemented
    pthread_attr_getschedpolicy(), Function, Implemented
    pthread_attr_setschedparam(), Function, Implemented
    pthread_attr_getschedparam(), Function, Implemented
    PTHREAD_INHERIT_SCHED, Constant, Implemented
    PTHREAD_EXPLICIT_SCHED, Constant, Implemented

Dynamic Thread Scheduling Parameters Access
-------------------------------------------

.. code:: c

    pthread_setschedparam(), Function, Implemented
    pthread_getschedparam(), Function, Implemented

Synchronization Scheduling
==========================

Mutex Initialization Scheduling Attributes
------------------------------------------

.. code:: c

    pthread_mutexattr_setprotocol(), Function, Implemented
    pthread_mutexattr_getprotocol(), Function, Implemented
    pthread_mutexattr_setprioceiling(), Function, Implemented
    pthread_mutexattr_getprioceiling(), Function, Implemented
    PTHREAD_PRIO_NONE, Constant, Implemented
    PTHREAD_PRIO_INHERIT, Constant, Implemented
    PTHREAD_PRIO_PROTECT, Constant, Implemented

Change the Priority Ceiling of a Mutex
--------------------------------------

.. code:: c

    pthread_mutex_setprioceiling(), Function, Implemented
    pthread_mutex_getprioceiling(), Function, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

