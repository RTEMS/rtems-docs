% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Thread Cancellation Manager

## Introduction

The
thread cancellation manager is ...

The directives provided by the thread cancellation manager are:

- [pthread_cancel] - Cancel Execution of a Thread
- [pthread_setcancelstate] - Set Cancelability State
- [pthread_setcanceltype] - Set Cancelability Type
- [pthread_testcancel] - Create Cancellation Point
- [pthread_cleanup_push] - Establish Cancellation Handler
- [pthread_cleanup_pop] - Remove Cancellation Handler

## Background

There is currently no text in this section.

## Operations

There is currently no text in this section.

## Directives

This section details the thread cancellation manager's directives. A
subsection is dedicated to each of this manager's directives and describes the
calling sequence, related constants, usage, and status codes.

(pthread_cancel)=

### pthread_cancel - Cancel Execution of a Thread

```{index} pthread_cancel
```

```{index} cancel execution of a thread
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_cancel(
    pthread_t thread
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

**NOTES:**

(pthread_setcancelstate)=

### pthread_setcancelstate - Set Cancelability State

```{index} pthread_setcancelstate
```

```{index} set cancelability state
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_setcancelstate(
    int state,
    int *oldstate
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

**NOTES:**

(pthread_setcanceltype)=

### pthread_setcanceltype - Set Cancelability Type

```{index} pthread_setcanceltype
```

```{index} set cancelability type
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
int pthread_setcanceltype(
    int type,
    int *oldtype
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

**NOTES:**

(pthread_testcancel)=

### pthread_testcancel - Create Cancellation Point

```{index} pthread_testcancel
```

```{index} create cancellation point
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
void pthread_testcancel(
    void
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

**NOTES:**

(pthread_cleanup_push)=

### pthread_cleanup_push - Establish Cancellation Handler

```{index} pthread_cleanup_push
```

```{index} establish cancellation handler
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
void pthread_cleanup_push(
    void (*routine)(void*),
    void *arg
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

**NOTES:**

(pthread_cleanup_pop)=

### pthread_cleanup_pop - Remove Cancellation Handler

```{index} pthread_cleanup_pop
```

```{index} remove cancellation handler
```

**CALLING SEQUENCE:**

```c
#include <pthread.h>
void pthread_cleanup_pop(
    int execute
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

**NOTES:**
