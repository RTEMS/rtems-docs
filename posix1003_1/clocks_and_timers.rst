.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Clocks and Timers
#################

Data Definitions for Clocks and Timers
======================================

Time Value Specification Structures
-----------------------------------

.. code:: c

    struct timespec, Type, Implemented
    struct itimerspec, Type, Implemented

Timer Event Notification Control Block
--------------------------------------

Type Definitions
----------------

.. code:: c

    clockid_t, Type, Implemented
    timerid_t, Type, Implemented

Timer Event Notification Manifest Constants
-------------------------------------------

.. code:: c

    CLOCK_REALTIME, Constant, Implemented
    TIMER_ABSTIME, Constant, Implemented

Clock and Timer Functions
=========================

Clocks
------

.. code:: c

    clock_settime(), Function, Partial Implementation
    clock_gettime(), Function, Partial Implementation
    clock_getres(), Function, Implemented

Create a Per-Process Timer
--------------------------

.. code:: c

    timer_create(), Function, Implemented

Delete a Per-Process Timer
--------------------------

.. code:: c

    timer_delete(), Function, Implemented

Per-Process Timers
------------------

.. code:: c

    timer_settime(), Function, Implemented
    timer_gettime(), Function, Implemented
    timer_getoverrun(), Function, Implemented

High Resolution Sleep
---------------------

.. code:: c

    nanosleep(), Function, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

