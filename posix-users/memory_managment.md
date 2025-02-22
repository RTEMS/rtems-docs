% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Memory Management Manager

## Introduction

The
memory management manager is ...

The directives provided by the memory management manager are:

- [mlockall] - Lock the Address Space of a Process
- [munlockall] - Unlock the Address Space of a Process
- [mlock] - Lock a Range of the Process Address Space
- [munlock] - Unlock a Range of the Process Address Space
- [mmap] - Map Process Addresses to a Memory Object
- [munmap] - Unmap Previously Mapped Addresses
- [mprotect] - Change Memory Protection
- [msync] - Memory Object Synchronization
- [shm_open] - Open a Shared Memory Object
- [shm_unlink] - Remove a Shared Memory Object

## Background

There is currently no text in this section.

## Operations

There is currently no text in this section.

## Directives

This section details the memory management manager's directives. A subsection
is dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

(mlockall)=

### mlockall - Lock the Address Space of a Process

```{index} mlockall
```

```{index} lock the address space of a process
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int mlockall(
    int flags
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

(munlockall)=

### munlockall - Unlock the Address Space of a Process

```{index} munlockall
```

```{index} unlock the address space of a process
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int munlockall(
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

(mlock)=

### mlock - Lock a Range of the Process Address Space

```{index} mlock
```

```{index} lock a range of the process address space
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int mlock(
    const void *addr,
    size_t len
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

(munlock)=

### munlock - Unlock a Range of the Process Address Space

```{index} munlock
```

```{index} unlock a range of the process address space
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int munlock(
    const void *addr,
    size_t len
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

(mmap)=

### mmap - Map Process Addresses to a Memory Object

```{index} mmap
```

```{index} map process addresses to a memory object
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
void *mmap(
    void *addr,
    size_t len,
    int prot,
    int flags,
    int fildes,
    off_t off
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - The fildes argument is not a valid open file descriptor.
 * - ``EINVAL``
   - The value of len is zero.
 * - ``EINVAL``
   - The value of flags is invalid (neither MAP_PRIVATE nor MAP_SHARED is set).
 * - ``EINVAL``
   - The addr argument (if MAP_FIXED was specified) or off is not a multiple of
     the page size as returned by sysconf(), or is considered invalid by the
     implementation.
 * - ``ENODEV``
   - The fildes argument refers to a file whose type is not supported by mmap.
 * - ``ENOMEM``
   - MAP_FIXED was specified, and the range [addr,addr+len) exceeds that
     allowed for the address space of a process; or, if MAP_FIXED was not
     specified and there is insufficient room in the address space to effect
     the mapping.
 * - ``ENOTSUP``
   - MAP_FIXED or MAP_PRIVATE was specified in the flags argument and the
     implementation does not support this functionality.
 * - ``ENOTSUP``
   - The implementation does not support the combination of accesses requested
     in the prot argument.
 * - ``ENXIO``
   - Addresses in the range [off,off+len) are invalid for the object specified
     by fildes.
 * - ``ENXIO``
   - MAP_FIXED was specified in flags and the combination of addr, len, and off
     is invalid for the object specified by fildes.
 * - ``EOVERFLOW``
   - The file is a regular file and the value of off plus len exceeds the
     offset maximum established in the open file description associated with
     fildes.
```

**DESCRIPTION:**

`mmap` establishes a mapping between an address `pa` for `len` bytes to
the memory object represented by the file descriptor `fildes` at offset
`off` for `len` bytes. The value of `pa` is an implementation-defined
function of the parameter addr and the values of `flags`. A successful
`mmap()` call shall return `pa` as its result. An unsuccessful call returns
`MAP_FAILED` and sets `errno` accordingly.

**NOTES:**

RTEMS is a single address space operating system without privilege separation
between the kernel and user space. Therefore, the implementation of `mmap`
has a number of implementation-specific issues to be aware of:

> - Read, write and execute permissions are allowed because the memory in RTEMS
>   does not normally have protections but we cannot hide access to memory.
>   Thus, the use of `PROT_NONE` for the `prot` argument is not supported.
>   Similarly, there is no restriction of write access, so `PROT_WRITE` must
>   be in the `prot` argument.
> - Anonymous mappings must have `fildes` set to -1 and `off` set to 0.
>   Shared mappings are not supported with Anonymous mappings.
> - `MAP_FIXED` is not supported for shared memory objects with `MAP_SHARED`.
> - Support for shared mappings is dependent on the underlying object's
>   filesystem implementation of an `mmap_h` file operation handler.

(munmap)=

### munmap - Unmap Previously Mapped Addresses

```{index} munmap
```

```{index} unmap previously mapped addresses
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int munmap(
    void *addr,
    size_t len
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Addresses in the range [addr,addr+len) are outside the valid range for the
     address space.
 * - ``EINVAL``
   - The len argument is 0.
```

**DESCRIPTION:**

The `munmap()` function shall remove any mappings for those entire pages
containing any part of the address space of the process starting at `addr`
and continuing for `len` bytes. If there are no mappings in the specified
address range, then `munmap()` has no effect.

Upon successful completion, `munmap()` shall return 0; otherwise, it shall
return -1 and set `errno` to indicate the error.

**NOTES:**

(mprotect)=

### mprotect - Change Memory Protection

```{index} mprotect
```

```{index} change memory protection
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int mprotect(
    void *addr,
    size_t len,
    int prot
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

(msync)=

### msync - Memory Object Synchronization

```{index} msync
```

```{index} memory object synchronization
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int msync(
    void *addr,
    size_t len,
    int flags
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

(shm-open)=

### shm_open - Open a Shared Memory Object

```{index} shm_open
```

```{index} open a shared memory object
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int shm_open(
    const char *name,
    int oflag,
    mode_t mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - The shared memory object exists and the permissions specified by oflag are
     denied, or the shared memory object does not exist and permission to
     create the shared memory object is denied, or O_TRUNC is specified and
     write permission is denied.
 * - ``EEXIST``
   - O_CREAT and O_EXCL are set and the named shared memory object already
     exists.
 * - ``EINVAL``
   - The ``shm_open()`` operation is not supported for the given name.
 * - ``EMFILE``
   - All file descriptors available to the process are currently open.
 * - ``ENFILE``
   - Too many shared memory objects are currently open in the system.
 * - ``ENOENT``
   - O_CREAT is not set and the named shared memory object does not exist.
 * - ``ENOSPC``
   - There is insufficient space for the creation of the new shared memory
     object.
 * - ``ENAMETOOLONG``
   - The length of the name argument exceeds ``_POSIX_PATH_MAX``.

```

**DESCRIPTION:**

The `shm_open()` function shall establish a connection between a shared
memory object and a file descriptor. It shall create an open file description
that refers to the shared memory object and a file descriptor that refers to
that open file description. The `name` argument points to a string naming a
shared memory object.

If successful, `shm_open()` shall return a file descriptor for the shared
memory object. Upon successful completion, the `shm_open()` function shall
return a non-negative integer representing the file descriptor. Otherwise, it
shall return -1 and set `errno` to indicate the error.

**NOTES:**

An application can set the `_POSIX_Shm_Object_operations` to control the
behavior of shared memory objects when accessed via the file descriptor.

The `name` must be valid for an RTEMS SuperCore Object.

(shm-unlink)=

### shm_unlink - Remove a Shared Memory Object

```{index} shm_unlink
```

```{index} remove a shared memory object
```

**CALLING SEQUENCE:**

```c
#include <sys/mman.h>
int shm_unlink(
    const char *name
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOENT``
   - The named shared memory object does not exist.
 * - ``ENAMETOOLONG``
   - The length of the name argument exceeds ``_POSIX_PATH_MAX``.
```

**DESCRIPTION:**

The `shm_unlink()` function shall remove the name of the shared memory object
named by the string pointed to by `name`.

If one or more references to the shared memory object exist when the object is
unlinked, the name shall be removed before `shm_unlink()` returns, but the
removal of the memory object contents shall be postponed until all open and map
references to the shared memory object have been removed.

Even if the object continues to exist after the last `shm_unlink()`, reuse of
the name shall subsequently cause `shm_open()` to behave as if no shared
memory object of this name exists.

Upon successful completion, a value of zero shall be returned. Otherwise, a
value of -1 shall be returned and errno set to indicate the error. If -1 is
returned, the named shared memory object shall not be changed by this function
call.

**NOTES:**
