% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Condition Variable Manager

## Introduction

The condition variable manager ...

The directives provided by the condition variable manager are:

- [pthread_condattr_init] - Initialize a Condition Variable Attribute Set
- [pthread_condattr_destroy] - Destroy a Condition Variable Attribute Set
- [pthread_condattr_setpshared] - Set Process Shared Attribute
- [pthread_condattr_getpshared] - Get Process Shared Attribute
- [pthread_cond_init] - Initialize a Condition Variable
- [pthread_cond_destroy] - Destroy a Condition Variable
- [pthread_cond_signal] - Signal a Condition Variable
- [pthread_cond_broadcast] - Broadcast a Condition Variable
- [pthread_cond_wait] - Wait on a Condition Variable
- [pthread_cond_timedwait] - With with Timeout a Condition Variable

## Background

There is currently no text in this section.

## Operations

There is currently no text in this section.

## Directives

This section details the condition variable manager's directives. A subsection
is dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

(pthread-condattr-init)=

### pthread_condattr_init - Initialize a Condition Variable Attribute Set

```{index} pthread_condattr_init
```

```{index} initialize a condition variable attribute set
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_condattr_init(
    pthread_condattr_t *attr
);
```

**STATUS CODES:**

> - - `ENOMEM`
>   - Insufficient memory is available to initialize the condition variable
>     attributes object.

**DESCRIPTION:**

**NOTES:**

(pthread-condattr-destroy)=

### pthread_condattr_destroy - Destroy a Condition Variable Attribute Set

```{index} pthread_condattr_destroy
```

```{index} destroy a condition variable attribute set
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_condattr_destroy(
    pthread_condattr_t *attr
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The attribute object specified is invalid.
```

**DESCRIPTION:**

**NOTES:**

(pthread-condattr-setpshared)=

### pthread_condattr_setpshared - Set Process Shared Attribute

```{index} pthread_condattr_setpshared
```

```{index} set process shared attribute
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_condattr_setpshared(
    pthread_condattr_t *attr,
    int                 pshared
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.
```

**DESCRIPTION:**

**NOTES:**

(pthread-condattr-getpshared)=

### pthread_condattr_getpshared - Get Process Shared Attribute

```{index} pthread_condattr_getpshared
```

```{index} get process shared attribute
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_condattr_getpshared(
    const pthread_condattr_t *attr,
    int                      *pshared
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument passed.
```

**DESCRIPTION:**

**NOTES:**

(pthread-cond-init)=

### pthread_cond_init - Initialize a Condition Variable

```{index} pthread_cond_init
```

```{index} initialize a condition variable
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cond_init(
    pthread_cond_t           *cond,
    const pthread_condattr_t *attr
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - The system lacked a resource other than memory necessary to create the
     initialize the condition variable object.
 * - ``ENOMEM``
   - Insufficient memory is available to initialize the condition variable
     object.
 * - ``EBUSY``
   - The specified condition variable has already been initialized.
 * - ``EINVAL``
   - The specified attribute value is invalid.
```

**DESCRIPTION:**

**NOTES:**

(pthread-cond-destroy)=

### pthread_cond_destroy - Destroy a Condition Variable

```{index} pthread_cond_destroy
```

```{index} destroy a condition variable
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cond_destroy(
    pthread_cond_t *cond
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified condition variable is invalid.
 * - ``EBUSY``
   - The specified condition variable is currently in use.
```

**DESCRIPTION:**

**NOTES:**

(pthread-cond-signal)=

### pthread_cond_signal - Signal a Condition Variable

```{index} pthread_cond_signal
```

```{index} signal a condition variable
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cond_signal(
    pthread_cond_t *cond
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified condition variable is not valid.
```

**DESCRIPTION:**

**NOTES:**

This routine should not be invoked from a handler from an asynchronous signal
handler or an interrupt service routine.

(pthread-cond-broadcast)=

### pthread_cond_broadcast - Broadcast a Condition Variable

```{index} pthread_cond_broadcast
```

```{index} broadcast a condition variable
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cond_broadcast(
    pthread_cond_t *cond
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified condition variable is not valid.
```

**DESCRIPTION:**

**NOTES:**

This routine should not be invoked from a handler from an asynchronous signal
handler or an interrupt service routine.

(pthread-cond-wait)=

### pthread_cond_wait - Wait on a Condition Variable

```{index} pthread_cond_wait
```

```{index} wait on a condition variable
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cond_wait(
    pthread_cond_t *cond,
    pthread_mutex_t *mutex
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The specified condition variable or mutex is not initialized OR different
     mutexes were specified for concurrent ``pthread_cond_wait()`` and
     ``pthread_cond_timedwait()`` operations on the same condition variable OR
     the mutex was not owned by the current thread at the time of the call.
```

**DESCRIPTION:**

**NOTES:**

(pthread-cond-timedwait)=

### pthread_cond_timedwait - Wait with Timeout a Condition Variable

```{index} pthread_cond_timedwait
```

```{index} wait with timeout a condition variable
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cond_timedwait(
    pthread_cond_t        *cond,
    pthread_mutex_t       *mutex,
    const struct timespec *abstime
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The nanoseconds field of timeout is invalid.
 * - ``EINVAL``
   - The specified condition variable or mutex is not initialized OR different
     mutexes were specified for concurrent ``pthread_cond_wait()`` and
     ``pthread_cond_timedwait()`` operations on the same condition variable OR
     the mutex was not owned by the current thread at the time of the call.
 * - ``ETIMEDOUT``
   - The specified time has elapsed without the condition variable being
     satisfied.
```

**DESCRIPTION:**

**NOTES:**
