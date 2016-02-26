.. COMMENT: COPYRIGHT(c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation(OAR).
.. COMMENT: All rights reserved.

Timer Manager
#############

Introduction
============

The timer manager is ...

The services provided by the timer manager are:

- timer_create_ - Create a Per-Process Timer

- timer_delete_ - Delete a Per-Process Timer

- timer_settime_ - Set Next Timer Expiration

- timer_gettime_ - Get Time Remaining on Timer

- timer_getoverrun_ - Get Timer Overrun Count

Background
==========

Operations
==========

System Calls
============

This section details the timer manager's services.  A subsection is dedicated
to each of this manager's services and describes the calling sequence, related
constants, usage, and status codes.

.. COMMENT: timer_create

.. _timer_create:

timer_create - Create a Per-Process Timer
-----------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <time.h>
    #include <signal.h>
    int timer_create(
        clockid_t        clock_id,
        struct sigevent *evp,
        timer_t         *timerid
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_delete

.. _timer_delete:

timer_delete - Delete a Per-Process Timer
-----------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <time.h>
    int timer_delete(
        timer_t timerid
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_settime

.. _timer_settime:

timer_settime - Set Next Timer Expiration
-----------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <time.h>
    int timer_settime(
        timer_t                  timerid,
        int                      flags,
        const struct itimerspec *value,
        struct itimerspec       *ovalue
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_gettime

.. _timer_gettime:

timer_gettime - Get Time Remaining on Timer
-------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <time.h>
    int timer_gettime(
        timer_t            timerid,
        struct itimerspec *value
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**

.. COMMENT: timer_getoverrun

.. _timer_getoverrun:

timer_getoverrun - Get Timer Overrun Count
------------------------------------------

**CALLING SEQUENCE:**

.. code-block:: c

    #include <time.h>
    int timer_getoverrun(
        timer_t   timerid
    );

**STATUS CODES:**

``EXXX`` -

**DESCRIPTION:**

**NOTES:**
