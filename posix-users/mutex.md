% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Mutex Manager

## Introduction

The mutex manager implements the functionality required of the mutex manager as
defined by POSIX 1003.1b-1996. This standard requires that a compliant
operating system provide the facilties to ensure that threads can operate with
mutual exclusion from one another and defines the API that must be provided.

The services provided by the mutex manager are:

- [pthread_mutexattr_init] - Initialize a Mutex Attribute Set
- [pthread_mutexattr_destroy] - Destroy a Mutex Attribute Set
- [pthread_mutexattr_setprotocol] - Set the Blocking Protocol
- [pthread_mutexattr_getprotocol] - Get the Blocking Protocol
- [pthread_mutexattr_setprioceiling] - Set the Priority Ceiling
- [pthread_mutexattr_getprioceiling] - Get the Priority Ceiling
- [pthread_mutexattr_setpshared] - Set the Visibility
- [pthread_mutexattr_getpshared] - Get the Visibility
- [pthread_mutex_init] - Initialize a Mutex
- [pthread_mutex_destroy] - Destroy a Mutex
- [pthread_mutex_lock] - Lock a Mutex
- [pthread_mutex_trylock] - Poll to Lock a Mutex
- [pthread_mutex_timedlock] - Lock a Mutex with Timeout
- [pthread_mutex_clocklock] - Lock a Mutex with Timeout against the chosen clock (monotonic or realtime)
- [pthread_mutex_unlock] - Unlock a Mutex
- [pthread_mutex_setprioceiling] - Dynamically Set the Priority Ceiling
- [pthread_mutex_getprioceiling] - Dynamically Get the Priority Ceiling

## Background

### Mutex Attributes

Mutex attributes are utilized only at mutex creation time. A mutex attribute
structure may be initialized and passed as an argument to the `mutex_init`
routine. Note that the priority ceiling of a mutex may be set at run-time.

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - *blocking protcol*
   - is the XXX
 * - *priority ceiling*
   - is the XXX
 * - *pshared*
   - is the XXX
```

### PTHREAD_MUTEX_INITIALIZER

This is a special value that a variable of type `pthread_mutex_t` may be
statically initialized to as shown below:

```c
pthread_mutex_t my_mutex = PTHREAD_MUTEX_INITIALIZER;
```

This indicates that `my_mutex` will be automatically initialized by an
implicit call to `pthread_mutex_init` the first time the mutex is used.

Note that the mutex will be initialized with default attributes.

## Operations

There is currently no text in this section.

## Services

This section details the mutex manager's services. A subsection is dedicated
to each of this manager's services and describes the calling sequence, related
constants, usage, and status codes.

(pthread_mutexattr_init)=

### pthread_mutexattr_init - Initialize a Mutex Attribute Set

```{index} pthread_mutexattr_init
```

```{index} initialize a mutex attribute set
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_init(
    pthread_mutexattr_t *attr
);
```

**STATUS CODES:**

*EINVAL*
: The attribute pointer argument is invalid.

**DESCRIPTION:**

The `pthread_mutexattr_init` routine initializes the mutex attributes object
specified by `attr` with the default value for all of the individual
attributes.

**NOTES:**

XXX insert list of default attributes here.

(pthread_mutexattr_destroy)=

### pthread_mutexattr_destroy - Destroy a Mutex Attribute Set

```{index} pthread_mutexattr_destroy
```

```{index} destroy a mutex attribute set
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
    int pthread_mutexattr_destroy(
    pthread_mutexattr_t *attr
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
```

**DESCRIPTION:**

The `pthread_mutex_attr_destroy` routine is used to destroy a mutex
attributes object. The behavior of using an attributes object after it is
destroyed is implementation dependent.

**NOTES:**

NONE

(pthread_mutexattr_setprotocol)=

### pthread_mutexattr_setprotocol - Set the Blocking Protocol

```{index} pthread_mutexattr_setprotocol
```

```{index} set the blocking protocol
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_setprotocol(
    pthread_mutexattr_t *attr,
    int                  protocol
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The protocol argument is invalid.
```

**DESCRIPTION:**

The `pthread_mutexattr_setprotocol` routine is used to set value of the
`protocol` attribute. This attribute controls the order in which threads
waiting on this mutex will receive it.

The `protocol` can be one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``PTHREAD_PRIO_NONE``
   - in which case blocking order is FIFO.
 * - ``PTHREAD_PRIO_INHERIT``
   - in which case blocking order is priority with the priority inheritance
     protocol in effect.
 * - ``PTHREAD_PRIO_PROTECT``
   - in which case blocking order is priority with the priority ceiling
     protocol in effect.
```

**NOTES:**

There is currently no way to get simple priority blocking ordering with POSIX
mutexes even though this could easily by supported by RTEMS.

(pthread_mutexattr_getprotocol)=

### pthread_mutexattr_getprotocol - Get the Blocking Protocol

```{index} pthread_mutexattr_getprotocol
```

```{index} get the blocking protocol
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_getprotocol(
    pthread_mutexattr_t *attr,
    int                 *protocol
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The protocol pointer argument is invalid.
```

**DESCRIPTION:**

The `pthread_mutexattr_getprotocol` routine is used to obtain the value of
the `protocol` attribute. This attribute controls the order in which threads
waiting on this mutex will receive it.

**NOTES:**

NONE

(pthread_mutexattr_setprioceiling)=

### pthread_mutexattr_setprioceiling - Set the Priority Ceiling

```{index} pthread_mutexattr_setprioceiling
```

```{index} set the priority ceiling
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_setprioceiling(
    pthread_mutexattr_t *attr,
    int                  prioceiling
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The prioceiling argument is invalid.
```

**DESCRIPTION:**

The `pthread_mutexattr_setprioceiling` routine is used to set value of the
`prioceiling` attribute. This attribute specifies the priority that is the
ceiling for threads obtaining this mutex. Any task obtaining this mutex may not
be of greater priority that the ceiling. If it is of lower priority, then its
priority will be elevated to `prioceiling`.

**NOTES:**

NONE

(pthread_mutexattr_getprioceiling)=

### pthread_mutexattr_getprioceiling - Get the Priority Ceiling

```{index} pthread_mutexattr_getprioceiling
```

```{index} get the priority ceiling
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_getprioceiling(
    const pthread_mutexattr_t *attr,
    int                       *prioceiling
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The prioceiling pointer argument is invalid.
```

**DESCRIPTION:**

The `pthread_mutexattr_getprioceiling` routine is used to obtain the value of
the `prioceiling` attribute. This attribute specifies the priority ceiling
for this mutex.

**NOTES:**

NONE

(pthread_mutexattr_setpshared)=

### pthread_mutexattr_setpshared - Set the Visibility

```{index} pthread_mutexattr_setpshared
```

```{index} set the visibility
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_setpshared(
    pthread_mutexattr_t *attr,
    int                  pshared
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The pshared argument is invalid.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutexattr_getpshared)=

### pthread_mutexattr_getpshared - Get the Visibility

```{index} pthread_mutexattr_getpshared
```

```{index} get the visibility
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutexattr_getpshared(
    const pthread_mutexattr_t *attr,
    int                       *pshared
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute pointer argument is invalid.
 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The pshared pointer argument is invalid.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_init)=

### pthread_mutex_init - Initialize a Mutex

```{index} pthread_mutex_init
```

```{index} initialize a mutex
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutex_init(
    pthread_mutex_t           *mutex,
    const pthread_mutexattr_t *attr
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute set is not initialized.
 * - ``EINVAL``
   - The specified protocol is invalid.
 * - ``EAGAIN``
   - The system lacked the necessary resources to initialize another mutex.
 * - ``ENOMEM``
   - Insufficient memory exists to initialize the mutex.
 * - ``EBUSY``
   - Attempted to reinialize the object reference by mutex, a previously
     initialized, but not yet destroyed.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_destroy)=

### pthread_mutex_destroy - Destroy a Mutex

```{index} pthread_mutex_destroy
```

```{index} destroy a mutex
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
    int pthread_mutex_destroy(
    pthread_mutex_t *mutex
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified mutex is invalid.
 * - ``EBUSY``
   - Attempted to destroy the object reference by mutex, while it is locked or
     referenced by another thread.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_lock)=

### pthread_mutex_lock - Lock a Mutex

```{index} pthread_mutex_lock
```

```{index} lock a mutex
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutex_lock(
    pthread_mutex_t *mutex
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified mutex is invalid.
 * - ``EINVAL``
   - The mutex has the protocol attribute of ``PTHREAD_PRIO_PROTECT`` and the
     priority of the calling thread is higher than the current priority
     ceiling.
 * - ``EDEADLK``
   - The current thread already owns the mutex.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_trylock)=

### pthread_mutex_trylock - Poll to Lock a Mutex

```{index} pthread_mutex_trylock
```

```{index} poll to lock a mutex
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutex_trylock(
    pthread_mutex_t *mutex
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified mutex is invalid.
 * - ``EINVAL``
   - The mutex has the protocol attribute of ``PTHREAD_PRIO_PROTECT`` and the
     priority of the calling thread is higher than the current priority ceiling.
 * - ``EBUSY``
   - The mutex is already locked.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_timedlock)=

### pthread_mutex_timedlock - Lock a Mutex with Timeout

```{index} pthread_mutex_timedlock
```

```{index} lock a mutex with timeout
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
#include <time.h>
int pthread_mutex_timedlock(
    pthread_mutex_t       *mutex,
    const struct timespec *timeout
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified mutex is invalid.
 * - ``EINVAL``
   - The nanoseconds field of timeout is invalid.
 * - ``EINVAL``
   - The mutex has the protocol attribute of ``PTHREAD_PRIO_PROTECT`` and the
     priority of the calling thread is higher than the current priority
     ceiling.
 * - ``EDEADLK``
   - The current thread already owns the mutex.
 * - ``ETIMEDOUT``
   - The calling thread was unable to obtain the mutex within the specified
     timeout period.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_clocklock)=

### pthread_mutex_clocklock - Lock a Mutex with Timeout against the chosen clock

```{index} pthread_mutex_clocklock
```

```{index} lock a mutex with timeout against chosen clock
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
#include <time.h>
int pthread_mutex_clocklock(
    pthread_mutex_t       *mutex,
    clockid_t              clockid,
    const struct timespec *abstime
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified mutex is invalid.
 * - ``EINVAL``
   - The nanoseconds field of timeout is invalid.
 * - ``EINVAL``
   - The mutex has the protocol attribute of ``PTHREAD_PRIO_PROTECT`` and the
     priority of the calling thread is higher than the current priority
     ceiling.
 * - ``EINVAL``
   - The clock specified by clockid is not supported.
 * - ``EDEADLK``
   - The current thread already owns the mutex.
 * - ``ETIMEDOUT``
   - The calling thread was unable to obtain the mutex within the specified
     timeout period.
```

**DESCRIPTION:**

The `pthread_mutex_clocklock()` function locks the mutex specified by `mutex`. If the mutex is already locked, the calling thread blocks until the mutex becomes available or until the absolute timeout specified by `abstime` is reached. The timeout is measured against the clock specified by `clockid`.

The only supported clocks are `CLOCK_MONOTONIC` and `CLOCK_REALTIME`.

**NOTES:**

(pthread_mutex_unlock)=

### pthread_mutex_unlock - Unlock a Mutex

```{index} pthread_mutex_unlock
```

```{index} unlock a mutex
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutex_unlock(
    pthread_mutex_t *mutex
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified mutex is invalid.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_setprioceiling)=

### pthread_mutex_setprioceiling - Dynamically Set the Priority Ceiling

```{index} pthread_mutex_setprioceiling
```

```{index} dynamically set the priority ceiling
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutex_setprioceiling(
    pthread_mutex_t *mutex,
    int              prioceiling,
    int             *oldceiling
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The oldceiling pointer parameter is invalid.
 * - ``EINVAL``
   - The prioceiling parameter is an invalid priority.
 * - ``EINVAL``
   - The specified mutex is invalid.
```

**DESCRIPTION:**

**NOTES:**

(pthread_mutex_getprioceiling)=

### pthread_mutex_getprioceiling - Get the Current Priority Ceiling

```{index} pthread_mutex_getprioceiling
```

```{index} get the current priority ceiling
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_mutex_getprioceiling(
    pthread_mutex_t *mutex,
    int             *prioceiling
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The prioceiling pointer parameter is invalid.
 * - ``EINVAL``
   - The specified mutex is invalid.
```

**DESCRIPTION:**

**NOTES:**
