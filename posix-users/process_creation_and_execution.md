% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Process Creation and Execution Manager

## Introduction

The process creation and execution manager provides the functionality
associated with the creation and termination of processes.

The directives provided by the process creation and execution manager are:

- [fork] - Create a Process
- [execl] - Execute a File
- [execv] - Execute a File
- [execle] - Execute a File
- [execve] - Execute a File
- [execlp] - Execute a File
- [execvp] - Execute a File
- [pthread_atfork] - Register Fork Handlers
- [wait] - Wait for Process Termination
- [waitpid] - Wait for Process Termination
- [\_exit][\_exit] - Terminate a Process

## Background

POSIX process functionality can not be completely supported by RTEMS. This is
because RTEMS provides no memory protection and implements a *single process,
multi-threaded execution model*. In this light, RTEMS provides none of the
routines that are associated with the creation of new processes. However,
since the entire RTEMS application (e.g. executable) is logically a single
POSIX process, RTEMS is able to provide implementations of many operations on
processes. The rule of thumb is that those routines provide a meaningful
result. For example, `getpid()` returns the node number.

## Operations

The only functionality method defined by this manager which is supported by
RTEMS is the `_exit` service. The implementation of `_exit` shuts the
application down and is equivalent to invoking either `exit` or
`rtems_shutdown_executive`.

## Directives

This section details the process creation and execution manager's directives.
A subsection is dedicated to each of this manager's directives and describes
the calling sequence, related constants, usage, and status codes.

(fork)=

### fork - Create a Process

```{index} fork
```

```{index} create a process
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
int fork( void );
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(execl)=

### execl - Execute a File

```{index} execl
```

```{index} execute a file
```

**CALLING SEQUENCE:**

```c
int execl(
    const char *path,
    const char *arg,
    ...
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(execv)=

### execv - Execute a File

```{index} execv
```

```{index} execute a file
```

**CALLING SEQUENCE:**

```c
int execv(
    const char *path,
    char const *argv[],
    ...
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(execle)=

### execle - Execute a File

```{index} execle
```

```{index} execute a file
```

**CALLING SEQUENCE:**

```c
int execle(
    const char *path,
    const char *arg,
    ...
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(execve)=

### execve - Execute a File

```{index} execve
```

```{index} execute a file
```

**CALLING SEQUENCE:**

```c
int execve(
    const char *path,
    char *const argv[],
    char *const envp[]
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(execlp)=

### execlp - Execute a File

```{index} execlp
```

```{index} execute a file
```

**CALLING SEQUENCE:**

```c
int execlp(
    const char *file,
    const char *arg,
    ...
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(execvp)=

### execvp - Execute a File

```{index} execvp
```

```{index} execute a file
```

**CALLING SEQUENCE:**

```c
int execvp(
    const char *file,
    char *const argv[],
    ...
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(pthread-atfork)=

### pthread_atfork - Register Fork Handlers

```{index} pthread_atfork
```

```{index} register fork handlers
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
int pthread_atfork(
    void (*prepare)(void),
    void (*parent)(void),
    void (*child)(void)
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``0``
   - This routine is a non-functional stub.
```

**DESCRIPTION:**

This routine is non-functional stub.

**NOTES:**

The POSIX specification for `pthread_atfork()` does not address the behavior
when in a single process environment. Originally, the RTEMS implementation
returned -1 and set errno to `ENOSYS`. This was an arbitrary decision
part with no basis from the wider POSIX community. The FACE Technical
Standard includes profiles without multiple process support and defined
the behavior in a single process environment to return 0. Logically, the
application can register atfork handlers but they will never be invoked.

(wait)=

### wait - Wait for Process Termination

```{index} wait
```

```{index} wait for process termination
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/wait.h>
int wait(
    int *stat_loc
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::


 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(waitpid)=

### waitpid - Wait for Process Termination

```{index} waitpid
```

```{index} wait for process termination
```

**CALLING SEQUENCE:**

```c
int wait(
    pid_t  pid,
    int   *stat_loc,
    int    options
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.
```

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

(exit)=

### \_exit - Terminate a Process

```{index} _exit
```

```{index} terminate a process
```

**CALLING SEQUENCE:**

```c
void _exit(
    int status
);
```

**STATUS CODES:**

NONE

**DESCRIPTION:**

The `_exit()` function terminates the calling process.

**NOTES:**

In RTEMS, a process is equivalent to the entire application on a single
processor. Invoking this service terminates the application.
