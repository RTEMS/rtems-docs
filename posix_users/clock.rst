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

