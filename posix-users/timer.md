% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Timer Manager

## Introduction

The timer manager is ...

The services provided by the timer manager are:

- [timer_create] - Create a Per-Process Timer
- [timer_delete] - Delete a Per-Process Timer
- [timer_settime] - Set Next Timer Expiration
- [timer_gettime] - Get Time Remaining on Timer
- [timer_getoverrun] - Get Timer Overrun Count

## Background

## Operations

## System Calls

This section details the timer manager's services. A subsection is dedicated
to each of this manager's services and describes the calling sequence, related
constants, usage, and status codes.

% COMMENT: timer_create

(timer_create)=

### timer_create - Create a Per-Process Timer

**CALLING SEQUENCE:**

```c
#include <time.h>
#include <signal.h>
int timer_create(
    clockid_t        clock_id,
    struct sigevent *evp,
    timer_t         *timerid
);
```

**STATUS CODES:**

`EXXX` -

**DESCRIPTION:**

**NOTES:**

% COMMENT: timer_delete

(timer_delete)=

### timer_delete - Delete a Per-Process Timer

**CALLING SEQUENCE:**

```c
#include <time.h>
int timer_delete(
    timer_t timerid
);
```

**STATUS CODES:**

`EXXX` -

**DESCRIPTION:**

**NOTES:**

% COMMENT: timer_settime

(timer_settime)=

### timer_settime - Set Next Timer Expiration

**CALLING SEQUENCE:**

```c
#include <time.h>
int timer_settime(
    timer_t                  timerid,
    int                      flags,
    const struct itimerspec *value,
    struct itimerspec       *ovalue
);
```

**STATUS CODES:**

`EXXX` -

**DESCRIPTION:**

**NOTES:**

% COMMENT: timer_gettime

(timer_gettime)=

### timer_gettime - Get Time Remaining on Timer

**CALLING SEQUENCE:**

```c
#include <time.h>
int timer_gettime(
    timer_t            timerid,
    struct itimerspec *value
);
```

**STATUS CODES:**

`EXXX` -

**DESCRIPTION:**

**NOTES:**

% COMMENT: timer_getoverrun

(timer_getoverrun)=

### timer_getoverrun - Get Timer Overrun Count

**CALLING SEQUENCE:**

```c
#include <time.h>
int timer_getoverrun(
    timer_t   timerid
);
```

**STATUS CODES:**

`EXXX` -

**DESCRIPTION:**

**NOTES:**
