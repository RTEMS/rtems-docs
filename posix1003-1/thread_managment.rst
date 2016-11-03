.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Thread Management
#################

Threads
=======

Thread Functions
================

Thread Creation Attributes
--------------------------

.. code:: c

    pthread_attr_init(), Function, Implemented
    pthread_attr_destroy(), Function, Implemented
    pthread_attr_setstacksize(), Function, Implemented
    pthread_attr_getstacksize(), Function, Implemented
    pthread_attr_setstackaddr(), Function, Implemented
    pthread_attr_getstackaddr(), Function, Implemented
    pthread_attr_setdetachstate(), Function, Implemented
    pthread_attr_getdetachstate(), Function, Implemented
    PTHREAD_CREATE_JOINABLE, Constant, Implemented
    PTHREAD_CREATE_DETACHED, Constant, Implemented

Thread Creation
---------------

.. code:: c

    pthread_create(), Function, Implemented

Wait for Thread Termination
---------------------------

.. code:: c

    pthread_join(), Function, Implemented

Detaching a Thread
------------------

.. code:: c

    pthread_detach(), Function, Implemented

Thread Termination
------------------

.. code:: c

    pthread_exit(), Function, Implemented

Get Thread ID
-------------

.. code:: c

    pthread_self(), Function, Implemented

Compare Thread IDs
------------------

.. code:: c

    pthread_equal(), Function, Implemented

Dynamic Package Initialization
------------------------------

.. code:: c

    pthread_once(), Function, Implemented
    PTHREAD_ONCE_INIT, Constant, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

