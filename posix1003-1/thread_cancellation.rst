.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Thread Cancellation
###################

Thread Cancellation Overview
============================

Cancelability States
--------------------

.. code:: c

    PTHREAD_CANCEL_DISABLE, Constant, Implemented
    PTHREAD_CANCEL_ENABLE, Constant, Implemented
    PTHREAD_CANCEL_ASYNCHRONOUS, Constant, Implemented
    PTHREAD_CANCEL_DEFERRED, Constant, Implemented

Cancellation Points
-------------------

Thread Cancellation Cleanup Handlers
------------------------------------

.. code:: c

    PTHREAD_CANCELED, Constant, Unimplemented

Async-Cancel Safety
-------------------

Thread Cancellation Functions
=============================

Canceling Execution of a Thread
-------------------------------

.. code:: c

    pthread_cancel(), Function, Implemented

Setting Cancelability State
---------------------------

.. code:: c

    pthread_setcancelstate(), Function, Implemented
    pthread_setcanceltype(), Function, Implemented
    pthread_testcancel(), Function, Implemented

Establishing Cancellation Handlers
----------------------------------

.. code:: c

    pthread_cleanup_push(), Function, Implemented
    pthread_cleanup_pop(), Function, Implemented

Language-Independent Cancellation Functionality
===============================================

Requesting Cancellation
-----------------------

Associating Cleanup Code With Scopes
------------------------------------

Controlling Cancellation Within Scopes
--------------------------------------

Defined Cancellation Sequence
-----------------------------

List of Cancellation Points
---------------------------

.. COMMENT: DO NOT EDIT - AUTOMATICALLY GENERATED!!!

