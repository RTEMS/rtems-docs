.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Synchronization
###############

Semaphore Characteristics
=========================

NOTE: Semaphores are implemented but only unnamed semaphores
are currently tested.
.. code:: c

    sem_t, Type, Implemented

Semaphore Functions
===================

Initialize an Unnamed Semaphore
-------------------------------

.. code:: c

    sem_init(), Function, Implemented
    SEM_FAILED, Constant, Implemented

Destroy an Unnamed Semaphore
----------------------------

.. code:: c

    sem_destroy(), Function, Implemented

Initialize/Open a Named Semaphore
---------------------------------

.. code:: c

    sem_open(), Function, Implemented

Close a Named Semaphore
-----------------------

.. code:: c

    sem_close(), Function, Implemented

Remove a Named Semaphore
------------------------

.. code:: c

    sem_unlink(), Function, Implemented

Lock a Semaphore
----------------

.. code:: c

    sem_wait(), Function, Implemented
    sem_trywait(), Function, Implemented

Unlock a Semaphore
------------------

.. code:: c

    sem_post(), Function, Implemented

Get the Value of a Semaphore
----------------------------

.. code:: c

    sem_getvalue(), Function, Implemented

Mutexes
=======

Mutex Initialization Attributes
-------------------------------

.. code:: c

    pthread_mutexattr_init(), Function, Implemented
    pthread_mutexattr_destroy(), Function, Implemented
    pthread_mutexattr_getpshared(), Function, Implemented
    pthread_mutexattr_setpshared(), Function, Implemented
    PTHREAD_PROCESS_SHARED, Constant, Implemented
    PTHREAD_PROCESS_PRIVATE, Constant, Implemented

Initializing and Destroying a Mutex
-----------------------------------

.. code:: c

    pthread_mutex_init(), Function, Implemented
    pthread_mutex_destroy(), Function, Implemented
    PTHREAD_MUTEX_INITIALIZER, Constant, Implemented

Locking and Unlocking a Mutex
-----------------------------

.. code:: c

    pthread_mutex_lock(), Function, Implemented
    pthread_mutex_trylock(), Function, Implemented
    pthread_mutex_unlock(), Function, Implemented

Condition Variables
===================

Condition Variable Initialization Attributes
--------------------------------------------

.. code:: c

    pthread_condattr_init(), Function, Implemented
    pthread_condattr_destroy(), Function, Implemented
    pthread_condattr_getpshared(), Function, Implemented
    pthread_condattr_setpshared(), Function, Implemented

Initialization and Destroying Condition Variables
-------------------------------------------------

.. code:: c

    pthread_cond_init(), Function, Implemented
    pthread_cond_destroy(), Function, Implemented
    PTHREAD_COND_INITIALIZER, Constant, Implemented

Broadcasting and Signaling a Condition
--------------------------------------

.. code:: c

    pthread_cond_signal(), Function, Implemented
    pthread_cond_broadcast(), Function, Implemented

Waiting on a Condition
----------------------

.. code:: c

    pthread_cond_wait(), Function, Implemented
    pthread_cond_timedwait(), Function, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

