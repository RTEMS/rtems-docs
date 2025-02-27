% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1989, 2008 On-Line Applications Research Corporation (OAR)

# Semaphore Manager

## Introduction

The semaphore manager provides functions to allocate, delete, and control
semaphores. This manager is based on the POSIX 1003.1 standard.

The directives provided by the semaphore manager are:

- [sem_init] - Initialize an unnamed semaphore
- [sem_destroy] - Destroy an unnamed semaphore
- [sem_open] - Open a named semaphore
- [sem_close] - Close a named semaphore
- [sem_unlink] - Remove a named semaphore
- [sem_wait] - Lock a semaphore
- [sem_trywait] - Lock a semaphore
- [sem_timedwait] - Wait on a Semaphore for a Specified Time
- [sem_post] - Unlock a semaphore
- [sem_getvalue] - Get the value of a semeaphore

## Background

### Theory

Semaphores are used for synchronization and mutual exclusion by indicating the
availability and number of resources. The task (the task which is returning
resources) notifying other tasks of an event increases the number of resources
held by the semaphore by one. The task (the task which will obtain resources)
waiting for the event decreases the number of resources held by the semaphore
by one. If the number of resources held by a semaphore is insufficient (namely
0), the task requiring resources will wait until the next time resources are
returned to the semaphore. If there is more than one task waiting for a
semaphore, the tasks will be placed in the queue.

### "sem_t" Structure

```{index} sem_t
```

The `sem_t` structure is used to represent semaphores. It is passed as an
argument to the semaphore directives and is defined as follows:

```c
typedef int sem_t;
```

### Building a Semaphore Attribute Set

## Operations

### Using as a Binary Semaphore

Although POSIX supports mutexes, they are only visible between threads. To work
between processes, a binary semaphore must be used.

Creating a semaphore with a limit on the count of 1 effectively restricts the
semaphore to being a binary semaphore. When the binary semaphore is available,
the count is 1. When the binary semaphore is unavailable, the count is 0.

Since this does not result in a true binary semaphore, advanced binary features
like the Priority Inheritance and Priority Ceiling Protocols are not available.

There is currently no text in this section.

## Directives

This section details the semaphore manager's directives. A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

(sem_init)=

### sem_init - Initialize an unnamed semaphore

```{index} sem_init
```

```{index} initialize an unnamed semaphore
```

**CALLING SEQUENCE:**

```c
int sem_init(
    sem_t        *sem,
    int           pshared,
    unsigned int  value
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The value argument exceeds ``SEM_VALUE_MAX``
 * - ``ENOSPC``
   - A resource required to initialize the semaphore has been exhausted The
     limit on semaphores (``SEM_VALUE_MAX``) has been reached
 * - ``ENOSYS``
   - The function sem_init is not supported by this implementation
 * - ``EPERM``
   - The process lacks appropriate privileges to initialize the semaphore
```

**DESCRIPTION:**

The `sem_init` function is used to initialize the unnamed semaphore referred
to by `sem`. The value of the initialized semaphore is the parameter
`value`. The semaphore remains valid until it is destroyed.

% COMMENT: ADD MORE HERE XXX

**NOTES:**

If the functions completes successfully, it shall return a value of zero.
otherwise, it shall return a value of -1 and set `errno` to specify the error
that occurred.

Multiprocessing is currently not supported in this implementation.

(sem_destroy)=

### sem_destroy - Destroy an unnamed semaphore

```{index} sem_destroy
```

```{index} destroy an unnamed semaphore
```

**CALLING SEQUENCE:**

```c
int sem_destroy(
    sem_t *sem
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The value argument exceeds ``SEM_VALUE_MAX``
 * - ``ENOSYS``
   - The function ``sem_init`` is not supported by this implementation
 * - ``EBUSY``
   - There are currently processes blocked on the semaphore
```

**DESCRIPTION:**

The `sem_destroy` function is used to destroy an unnamed semaphore refered to
by `sem`. `sem_destroy` can only be used on a semaphore that was created
using sem_init.

**NOTES:**

If the functions completes successfully, it shall return a value of zero.
Otherwise, it shall return a value of -1 and set `errno` to specify the error
that occurred.

Multiprocessing is currently not supported in this implementation.

(sem_open)=

### sem_open - Open a named semaphore

```{index} sem_open
```

```{index} open a named semaphore
```

**CALLING SEQUENCE:**

```c
int sem_open(
    const char *name,
    int         oflag
);
```

**ARGUMENTS:**

The following flag bit may be set in oflag:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``O_CREAT``
   - Creates the semaphore if it does not already exist. If ``O_CREAT`` is set
     and the semaphore already exists then ``O_CREAT`` has no
     effect. Otherwise, ``sem_open()`` creates a semaphore. The ``O_CREAT``
     flag requires the third and fourth argument: mode and value of type
     ``mode_t`` and ``unsigned int``, respectively.
 * - ``O_EXCL``
   - If ``O_EXCL`` and ``O_CREAT`` are set, all call to ``sem_open()`` shall
     fail if the semaphore name exists
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Valid name specified but oflag permissions are denied, or the semaphore
     name specified does not exist and permission to create the named semaphore
     is denied.
 * - ``EEXIST``
   - ``O_CREAT`` and ``O_EXCL`` are set and the named semaphore already exists.
 * - ``EINTR``
   - The ``sem_open()`` operation was interrupted by a signal.
 * - ``EINVAL``
   - The ``sem_open()`` operation is not supported for the given name.
 * - ``EMFILE``
   - Too many semaphore descriptors or file descriptors in use by this process.
 * - ``ENAMETOOLONG``
   - The length of the name exceed ``PATH_MAX`` or name component is longer
     than ``NAME_MAX`` while ``POSIX_NO_TRUNC`` is in effect.
 * - ``ENOENT``
   - ``O_CREAT`` is not set and the named semaphore does not exist.
 * - ``ENOSPC``
   - There is insufficient space for the creation of a new named semaphore.
 * - ``ENOSYS``
   - The function ``sem_open()`` is not supported by this implementation.
```

**DESCRIPTION:**

The `sem_open()` function establishes a connection between a specified
semaphore and a process. After a call to sem_open with a specified semaphore
name, a process can reference to semaphore by the associated name using the
address returned by the call. The oflag arguments listed above control the
state of the semaphore by determining if the semaphore is created or accessed
by a call to `sem_open()`.

**NOTES:**

(sem_close)=

### sem_close - Close a named semaphore

```{index} sem_close
```

```{index} close a named semaphore
```

**CALLING SEQUENCE:**

```c
int sem_close(
    sem_t *sem_close
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - The semaphore argument is not a valid semaphore descriptor.
 * - ``ENOSYS``
   - The function ``sem_close`` is not supported by this implementation.
```

**DESCRIPTION:**

The `sem_close()` function is used to indicate that the calling process is
finished using the named semaphore indicated by `sem`. The function
`sem_close` deallocates any system resources that were previously allocated
by a `sem_open` system call. If `sem_close()` completes successfully it
returns a 1, otherwise a value of -1 is return and `errno` is set.

**NOTES:**

(sem_unlink)=

### sem_unlink - Unlink a semaphore

```{index} sem_unlink
```

```{index} unlink a semaphore
```

**CALLING SEQUENCE:**

```c
int sem_unlink(
    const char *name
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCESS``
   - Permission is denied to unlink a semaphore.
 * - ``ENAMETOOLONG``
   - The length of the strong name exceed ``NAME_MAX`` while ``POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - The name of the semaphore does not exist.
 * - ``ENOSPC``
   - There is insufficient space for the creation of a new named semaphore.
 * - ``ENOSYS``
   - The function ``sem_unlink`` is not supported by this implementation.
```

**DESCRIPTION:**

The `sem_unlink()` function shall remove the semaphore name by the string
name. If a process is currently accessing the name semaphore, the
`sem_unlink` command has no effect. If one or more processes have the
semaphore open when the `sem_unlink` function is called, the destruction of
semaphores shall be postponed until all reference to semaphore are destroyed by
calls to `sem_close`, `_exit()`, or `exec`. After all references have
been destroyed, it returns immediately.

If the termination is successful, the function shall return 0. Otherwise, a -1
is returned and the `errno` is set.

**NOTES:**

(sem_wait)=

### sem_wait - Wait on a Semaphore

```{index} sem_wait
```

```{index} wait on a semaphore
```

**CALLING SEQUENCE:**

```c
int sem_wait(
    sem_t *sem
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The ``sem`` argument does not refer to a valid semaphore
```

**DESCRIPTION:**

This function attempts to lock a semaphore specified by `sem`. If the
semaphore is available, then the semaphore is locked (i.e., the semaphore
value is decremented). If the semaphore is unavailable (i.e., the semaphore
value is zero), then the function will block until the semaphore becomes
available. It will then successfully lock the semaphore. The semaphore
remains locked until released by a `sem_post()` call.

If the call is unsuccessful, then the function returns -1 and sets `errno` to
the appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

(sem_trywait)=

### sem_trywait - Non-blocking Wait on a Semaphore

```{index} sem_trywait
```

```{index} non
```

**CALLING SEQUENCE:**

```c
int sem_trywait(
    sem_t *sem
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - The semaphore is not available (i.e., the semaphore value is zero), so the
     semaphore could not be locked.
 * - ``EINVAL``
   - The ``sem`` argument does not refewr to a valid semaphore
```

**DESCRIPTION:**

This function attempts to lock a semaphore specified by `sem`. If the
semaphore is available, then the semaphore is locked (i.e., the semaphore value
is decremented) and the function returns a value of 0. The semaphore remains
locked until released by a `sem_post()` call. If the semaphore is unavailable
(i.e., the semaphore value is zero), then the function will return a value
of -1 immediately and set `errno` to `EAGAIN`.

If the call is unsuccessful, then the function returns -1 and sets `errno` to
the appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

(sem_timedwait)=

### sem_timedwait - Wait on a Semaphore for a Specified Time

```{index} sem_timedwait
```

```{index} wait on a semaphore for a specified time
```

**CALLING SEQUENCE:**

```c
int sem_timedwait(
    sem_t                 *sem,
    const struct timespec *abstime
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The ``sem`` argument does not refewr to a valid semaphore
 * - ``EINVAL``
   - The nanoseconds field of timeout is invalid.
 * - ``ETIMEDOUT``
   - The calling thread was unable to get the semaphore within the specified
     timeout period.
```

**DESCRIPTION:**

This function attemtps to lock a semaphore specified by `sem`, and will wait
for the semaphore until the absolute time specified by `abstime`. If the
semaphore is available, then the semaphore is locked (i.e., the semaphore value
is decremented) and the function returns a value of 0. The semaphore remains
locked until released by a `sem_post()` call. If the semaphore is
unavailable, then the function will wait for the semaphore to become available
for the amount of time specified by `timeout`.

If the semaphore does not become available within the interval specified by
`timeout`, then the function returns -1 and sets `errno` to `EAGAIN`. If
any other error occurs, the function returns -1 and sets `errno` to the
appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

(sem_post)=

### sem_post - Unlock a Semaphore

```{index} sem_post
```

```{index} unlock a semaphore
```

**CALLING SEQUENCE:**

```c
int sem_post(
    sem_t *sem
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The ``sem`` argument does not refer to a valid semaphore
```

**DESCRIPTION:**

This function attempts to release the semaphore specified by `sem`. If other
tasks are waiting on the semaphore, then one of those tasks (which one depends
on the scheduler being used) is allowed to lock the semaphore and return from
its `sem_wait()`, `sem_trywait()`, or `sem_timedwait()` call. If there
are no other tasks waiting on the semaphore, then the semaphore value is simply
incremented. `sem_post()` returns 0 upon successful completion.

If an error occurs, the function returns -1 and sets `errno` to the
appropriate error code.

**NOTES:**

Multiprocessing is not supported in this implementation.

(sem_getvalue)=

### sem_getvalue - Get the value of a semaphore

```{index} sem_getvalue
```

```{index} get the value of a semaphore
```

**CALLING SEQUENCE:**

```c
int sem_getvalue(
    sem_t *sem,
    int   *sval
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The ``sem`` argument does not refer to a valid semaphore
 * - ``ENOSYS``
   - The function ``sem_getvalue`` is not supported by this implementation
```

**DESCRIPTION:**

The `sem_getvalue` functions sets the location referenced by the `sval`
argument to the value of the semaphore without affecting the state of the
semaphore. The updated value represents a semaphore value that occurred at some
point during the call, but is not necessarily the actual value of the semaphore
when it returns to the calling process.

If `sem` is locked, the value returned by `sem_getvalue` will be zero or a
negative number whose absolute value is the number of processes waiting for the
semaphore at some point during the call.

**NOTES:**

If the functions completes successfully, it shall return a value of zero.
Otherwise, it shall return a value of -1 and set `errno` to specify the error
that occurred.
