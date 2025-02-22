% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Input and Output Primitives Manager

## Introduction

The input and output primitives manager is ...

The directives provided by the input and output primitives manager are:

- [pipe] - Create an Inter-Process Channel
- [dup] - Duplicates an open file descriptor
- [dup2] - Duplicates an open file descriptor
- [close] - Closes a file
- [read] - Reads from a file
- [write] - Writes to a file
- [fcntl] - Manipulates an open file descriptor
- [lseek] - Reposition read/write file offset
- [fsync] - Synchronize file complete in-core state with that on disk
- [fdatasync] - Synchronize file in-core data with that on disk
- [sync] - Schedule file system updates
- [mount] - Mount a file system
- [unmount] - Unmount file systems
- [readv] - Vectored read from a file
- [writev] - Vectored write to a file
- [aio_read] - Asynchronous Read
- [aio_write] - Asynchronous Write
- [lio_listio] - List Directed I/O
- [aio_error] - Retrieve Error Status of Asynchronous I/O Operation
- [aio_return] - Retrieve Return Status Asynchronous I/O Operation
- [aio_cancel] - Cancel Asynchronous I/O Request
- [aio_suspend] - Wait for Asynchronous I/O Request
- [aio_fsync] - Asynchronous File Synchronization

## Background

There is currently no text in this section.

## Operations

There is currently no text in this section.

## Directives

This section details the input and output primitives manager's directives. A
subsection is dedicated to each of this manager's directives and describes the
calling sequence, related constants, usage, and status codes.

(pipe)=

### pipe - Create an Inter-Process Channel

```{index} pipe
```

```{index} create an inter
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int pipe(
    int fildes[2]
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

This routine is not currently supported by RTEMS but could be
in a future version.

(dup)=

### dup - Duplicates an open file descriptor

```{index} dup
```

```{index} duplicates an open file descriptor
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int dup(
    int fildes
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor.
 * - ``EINTR``
   - Function was interrupted by a signal.
 * - ``EMFILE``
   - The process already has the maximum number of file descriptors open and
     tried to open a new one.
```

**DESCRIPTION:**

The `dup` function returns the lowest numbered available file
descriptor. This new desciptor refers to the same open file as the original
descriptor and shares any locks.

**NOTES:**

NONE

(dup2)=

### dup2 - Duplicates an open file descriptor

```{index} dup2
```

```{index} duplicates an open file descriptor
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int dup2(
    int fildes,
    int fildes2
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor.
 * - ``EINTR``
   - Function was interrupted by a signal.
 * - ``EMFILE``
   - The process already has the maximum number of file descriptors open and
     tried to open a new one.
```

**DESCRIPTION:**

`dup2` creates a copy of the file descriptor `oldfd`.

The old and new descriptors may be used interchangeably. They share locks, file
position pointers and flags; for example, if the file position is modified by
using `lseek` on one of the descriptors, the position is also changed for the
other.

**NOTES:**

NONE

(close)=

### close - Closes a file

```{index} close
```

```{index} closes a file.
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int close(
    int fildes
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
 * - ``EINTR``
   - Function was interrupted by a signal.
```

**DESCRIPTION:**

The `close()` function deallocates the file descriptor named by `fildes`
and makes it available for reuse. All outstanding record locks owned by this
process for the file are unlocked.

**NOTES:**

A signal can interrupt the `close()` function. In that case, `close()`
returns -1 with `errno` set to EINTR. The file may or may not be closed.

(read)=

### read - Reads from a file

```{index} read
```

```{index} reads from a file
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
ssize_t read(
    int fildes,
    void *buf,
    size_t nbyte
);
```

**STATUS CODES:**

On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - The O_NONBLOCK flag is set for a file descriptor and the process would be
     delayed in the I/O operation.
 * - ``EBADF``
   - Invalid file descriptor
 * - ``EINTR``
   - Function was interrupted by a signal.
 * - ``EIO``
   - Input or output error
 * - ``EINVAL``
   - Bad buffer pointer
```

**DESCRIPTION:**

The `read()` function reads `nbyte` bytes from the file associated with
`fildes` into the buffer pointed to by `buf`.

The `read()` function returns the number of bytes actually read and placed in
the buffer. This will be less than `nbyte` if:

- The number of bytes left in the file is less than `nbyte`.
- The `read()` request was interrupted by a signal.
- The file is a pipe or FIFO or special file with less than `nbytes`
  immediately available for reading.

When attempting to read from any empty pipe or FIFO:

- If no process has the pipe open for writing, zero is returned to indicate
  end-of-file.
- If some process has the pipe open for writing and O_NONBLOCK is set,
  -1 is returned and `errno` is set to EAGAIN.
- If some process has the pipe open for writing and O_NONBLOCK is clear,
  `read()` waits for some data to be written or the pipe to be closed.

When attempting to read from a file other than a pipe or FIFO and no data is
available.

- If O_NONBLOCK is set, -1 is returned and `errno` is set to EAGAIN.
- If O_NONBLOCK is clear, `read()` waits for some data to become available.
- The O_NONBLOCK flag is ignored if data is available.

**NOTES:**

NONE

(write)=

### write - Writes to a file

```{index} write
```

```{index} writes to a file
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
ssize_t write(
    int fildes,
    const void *buf,
    size_t nbyte
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - The O_NONBLOCK flag is set for a file descriptor and the process would be
     delayed in the I/O operation.
 * - ``EBADF``
   - Invalid file descriptor
 * - ``EFBIG``
   - An attempt was made to write to a file that exceeds the maximum file size
 * - ``EINTR``
   - The function was interrupted by a signal.
 * - ``EIO``
   - Input or output error.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``EPIPE``
   - Attempt to write to a pope or FIFO with no reader.
 * - ``EINVAL``
   - Bad buffer pointer
```

**DESCRIPTION:**

The `write()` function writes `nbyte` from the array pointed to by `buf`
into the file associated with `fildes`.

If `nybte` is zero and the file is a regular file, the `write()` function
returns zero and has no other effect. If `nbyte` is zero and the file is a
special file, te results are not portable.

The `write()` function returns the number of bytes written. This number will
be less than `nbytes` if there is an error. It will never be greater than
`nbytes`.

**NOTES:**

NONE

(fcntl)=

### fcntl - Manipulates an open file descriptor

```{index} fcntl
```

```{index} manipulates an open file descriptor
```

**CALLING SEQUENCE:**

```c
#include <fcntl.h>
int fcntl(
    int fildes,
    int cmd,
    ...
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCESS``
   - Search permission is denied for a direcotry in a file's path prefix.
 * - ``EAGAIN``
   - The O_NONBLOCK flag is set for a file descriptor and the process would be
     delayed in the I/O operation.
 * - ``EBADF``
   - Invalid file descriptor
 * - ``EDEADLK``
   - An ``fcntl`` with function ``F_SETLKW`` would cause a deadlock.
 * - ``EINTR``
   - The functioin was interrupted by a signal.
 * - ``EINVAL``
   - Invalid argument
 * - ``EMFILE``
   - Too many file descriptor or in use by the process.
 * - ``ENOLCK``
   - No locks available
```

**DESCRIPTION:**

`fcntl()` performs one of various miscellaneous operations on\`\`fd\`\`. The
operation in question is determined by `cmd`:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``F_DUPFD``
   - Makes ``arg`` be a copy of ``fd``, closing ``fd`` first if necessary.  The
     same functionality can be more easily achieved by using ``dup2()``.  The
     old and new descriptors may be used interchangeably. They share locks,
     file position pointers and flags; for example, if the file position is
     modified by using ``lseek()`` on one of the descriptors, the position is
     also changed for the other.  The two descriptors do not share the
     close-on-exec flag, however. The close-on-exec flag of the copy is off,
     meaning that it will be closed on exec.  On success, the new descriptor is
     returned.
 * - ``F_GETFD``
   - Read the close-on-exec flag. If the low-order bit is 0, the file will
     remain open across exec, otherwise it will be closed.
 * - ``F_SETFD``
   - Set the close-on-exec flag to the value specified by ``arg`` (only the
     least significant bit is used).
 * - ``F_GETFL``
   - Read the descriptor's flags (all flags (as set by open()) are returned).
 * - ``F_SETFL``
   - Set the descriptor's flags to the value specified by
     ``arg``. Only``O_APPEND`` and ``O_NONBLOCK`` may be set.  The flags are
     shared between copies (made with ``dup()`` etc.) of the same file
     descriptor.  The flags and their semantics are described in ``open()``.
 * - ``F_GETLK``, ``F_SETLK`` and ``F_SETLKW``
   - Manage discretionary file locks. The third argument ``arg`` is a pointer
     to a struct flock (that may be overwritten by this call).
 * - ``F_GETLK``
   - Return the flock structure that prevents us from obtaining the lock, or
     set the``l_type`` field of the lock to ``F_UNLCK`` if there is no
     obstruction.
 * - ``F_SETLK``
   - The lock is set (when ``l_type`` is ``F_RDLCK`` or ``F_WRLCK``) or cleared
     (when it is ``F_UNLCK``. If lock is held by someone else, this call
     returns -1 and sets ``errno`` to EACCES or EAGAIN.
 * - ``F_SETLKW``
   - Like ``F_SETLK``, but instead of returning an error we wait for the lock
     to be released.
 * - ``F_GETOWN``
   - Get the process ID (or process group) of the owner of a socket.  Process
     groups are returned as negative values.
 * - ``F_SETOWN``
   - Set the process or process group that owns a socket.  For these commands,
     ownership means receiving ``SIGIO`` or ``SIGURG`` signals.  Process groups
     are specified using negative values.
```

**NOTES:**

The errors returned by `dup2` are different from those returned by `F_DUPFD`.

(lseek)=

### lseek - Reposition read/write file offset

```{index} lseek
```

```{index} reposition read/write file offset
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
off_t lseek(
    int fildes,
    off_t offset,
    int whence
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - ``fildes`` is not an open file descriptor.
 * - ``ESPIPE``
   - ``fildes`` is associated with a pipe, socket or FIFO.
 * - ``EINVAL``
   - ``whence`` is not a proper value.
```

**DESCRIPTION:**

The `lseek` function repositions the offset of the file descriptor `fildes`
to the argument offset according to the directive whence. The argument
`fildes` must be an open file descriptor. `Lseek` repositions the file
pointer fildes as follows:

- If `whence` is SEEK_SET, the offset is set to `offset` bytes.
- If `whence` is SEEK_CUR, the offset is set to its current location
  plus offset bytes.
- If `whence` is SEEK_END, the offset is set to the size of the
  file plus `offset` bytes.

The `lseek` function allows the file offset to be set beyond the end of the
existing end-of-file of the file. If data is later written at this point,
subsequent reads of the data in the gap return bytes of zeros (until data is
actually written into the gap).

Some devices are incapable of seeking. The value of the pointer associated with
such a device is undefined.

**NOTES:**

NONE

(fsync)=

### fsync - Synchronize file complete in-core state with that on disk

```{index} fsync
```

```{index} synchronize file complete in
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int fsync(
    int fildes
);
```

**STATUS CODES:**

On success, zero is returned. On error, -1 is returned, and `errno` is set
appropriately.

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - ``fd`` is not a valid descriptor open for writing
 * - ``EINVAL``
   - ``fd`` is bound to a special file which does not support support
      synchronization
 * - ``EROFS``
   - ``fd`` is bound to a special file which does not support support
      synchronization
 * - ``EIO``
   - An error occurred during synchronization
```

**DESCRIPTION:**

`fsync` copies all in-core parts of a file to disk.

**NOTES:**

NONE

(fdatasync)=

### fdatasync - Synchronize file in-core data with that on disk

```{index} fdatasync
```

```{index} synchronize file in
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int fdatasync(
    int fildes
);
```

**STATUS CODES:**

On success, zero is returned. On error, -1 is returned, and `errno` is set
appropriately.

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - ``fd`` is not a valid file descriptor open for writing.
 * - ``EINVAL``
   - ``fd`` is bound to a special file which does not support synchronization.
 * - ``EIO``
   - An error occurred during synchronization.
 * - ``EROFS``
   - ``fd`` is bound to a special file which dows not support synchronization.
```

**DESCRIPTION:**

`fdatasync` flushes all data buffers of a file to disk (before the system
call returns). It resembles `fsync` but is not required to update the
metadata such as access time.

Applications that access databases or log files often write a tiny data
fragment (e.g., one line in a log file) and then call `fsync` immediately in
order to ensure that the written data is physically stored on the
harddisk. Unfortunately, fsync will always initiate two write operations: one
for the newly written data and another one in order to update the modification
time stored in the inode. If the modification time is not a part of the
transaction concept `fdatasync` can be used to avoid unnecessary inode disk
write operations.

**NOTES:**

NONE

(sync)=

### sync - Schedule file system updates

```{index} sync
```

```{index} synchronize file systems
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
void sync(
    void
);
```

**STATUS CODES:**

NONE

**DESCRIPTION:**

The `sync` service causes all information in memory that updates file systems
to be scheduled for writing out to all file systems.

**NOTES:**

The writing of data to the file systems is only guaranteed to be scheduled upon
return. It is not necessarily complete upon return from `sync`.

(mount)=

### mount - Mount a file system

```{index} mount
```

```{index} mount a file system
```

**CALLING SEQUENCE:**

```c
#include <libio.h>
int mount(
    rtems_filesystem_mount_table_entry_t **mt_entry,
    rtems_filesystem_operations_table *fs_ops,
    rtems_filesystem_options_t fsoptions,
    char *device,
    char *mount_point
);
```

**STATUS CODES:**

> - - `ENOMEM`
>   - Unable to allocate memory needed.
> - - `EINVAL`
>   - The filesystem does not support being mounted.
> - - `EINVAL`
>   - Attempt to mount a read-only filesystem as writeable.

**DESCRIPTION:**

The `mount` routines mounts the filesystem class which uses the filesystem
operations specified by `fs_ops` and `fsoptions`. The filesystem is
mounted at the directory `mount_point` and the mode of the mounted filesystem
is specified by `fsoptions`. If this filesystem class requires a device,
then the name of the device must be specified by `device`.

If this operation succeeds, the mount table entry for the mounted filesystem is
returned in `mt_entry`.

**NOTES:**

This method is not defined in the POSIX standard.

(unmount)=

### unmount - Unmount file systems

```{index} unmount
```

```{index} unmount file systems
```

**CALLING SEQUENCE:**

```c
#include <libio.h>
int unmount(
    const char *mount_path
);
```

**STATUS CODES:**

> - - `EBUSY`
>   - Filesystem is in use or the root filesystem.
> - - `EACCESS`
>   - Unable to allocate memory needed.

**DESCRIPTION:**

The `unmount` routine removes the attachment of the filesystem specified by
`mount_path`.

**NOTES:**

This method is not defined in the POSIX standard.

(readv)=

### readv - Vectored read from a file

```{index} readv
```

```{index} vectored read from a file
```

**CALLING SEQUENCE:**

```c
#include <sys/uio.h>
ssize_t readv(
    int fildes,
    const struct iovec *iov,
    int iovcnt
);
```

**STATUS CODES:**

In addition to the errors detected by *Input and Output Primitives Manager
read - Reads from a file, read()*, this routine may return -1 and sets
`errno` based upon the following errors:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The sum of the ``iov_len`` values in the iov array overflowed
     an ``ssize_t``.
 * - ``EINVAL``
   - The ``iovcnt`` argument was less than or equal to 0, or greater than
     ``IOV_MAX``.
```

**DESCRIPTION:**

The `readv()` function is equivalent to `read()` except as described
here. The `readv()` function shall place the input data into the `iovcnt`
buffers specified by the members of the `iov` array: `iov[0], iov[1], ..., iov[iovcnt-1]`.

Each `iovec` entry specifies the base address and length of an area in memory
where data should be placed. The `readv()` function always fills an area
completely before proceeding to the next.

**NOTES:**

NONE

(writev)=

### writev - Vectored write to a file

```{index} writev
```

```{index} vectored write to a file
```

**CALLING SEQUENCE:**

```c
#include <sys/uio.h>
ssize_t writev(
    int fildes,
    const struct iovec *iov,
    int iovcnt
);
```

**STATUS CODES:**

In addition to the errors detected by *Input and Output Primitives Manager
write - Write to a file, write()*, this routine may return -1 and sets
`errno` based upon the following errors:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The sum of the ``iov_len`` values in the iov array overflowed
     an ``ssize_t``.
 * - ``EINVAL``
   - The ``iovcnt`` argument was less than or equal to 0, or greater than
     ``IOV_MAX``.
```

**DESCRIPTION:**

The `writev()` function is equivalent to `write()`, except as noted
here. The `writev()` function gathers output data from the `iovcnt` buffers
specified by the members of the `iov array`: `iov[0], iov[1], ..., iov[iovcnt-1]`. The `iovcnt` argument is valid if greater than 0 and less
than or equal to `IOV_MAX`.

Each `iovec` entry specifies the base address and length of an area in memory
from which data should be written. The `writev()` function always writes a
complete area before proceeding to the next.

If `fd` refers to a regular file and all of the `iov_len` members in the
array pointed to by `iov` are 0, `writev()` returns 0 and has no other
effect. For other file types, the behavior is unspecified by POSIX.

**NOTES:**

NONE

(aio-read)=

### aio_read - Asynchronous Read

```{index} aio_read
```

```{index} asynchronous read
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int aio_read(
    struct aiocb *aiocbp
);
```

**STATUS CODES:**

If the request is successfully enqueued, zero is returned.
On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - The file descriptor is not open for reading.
 * - ``EINVAL``
   - Invalid aio_reqprio, aio_offset, or aio_nbytes.
 * - ``EAGAIN``
   - Not enough memory to queue the request.
 * - ``EAGAIN``
   - the addition of a new request to the queue would violate
     the ``RTEMS_AIO_MAX`` limit.
 * - ``EINVAL``
   - The starting position is past the maximum offset for the file.
 * - ``EINVAL``
   - ``aiocbp->aio_sigevent`` does not point to a valid sigevent struct.
 * - ``EINVAL``
   - ``aiocbp`` is a NULL pointer.
```

**DESCRIPTION:**

The `aio_read()` function is the asynchronous equivalent of `read()`.
This function returns immediately, the request is serviced by thread(s)
running in the background.

The parameters for the read are specified in the `aiocbp` structure.

**NOTES:**

NONE

(aio-write)=

### aio_write - Asynchronous Write

```{index} aio_write
```

```{index} asynchronous write
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int aio_write(
    struct aiocb *aiocbp
);
```

**STATUS CODES:**

If the request is successfully enqueued, zero is returned.
On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - The file descriptor is not open for writing.
 * - ``EINVAL``
   - Invalid aio_reqprio, aio_offset, or aio_nbytes.
 * - ``EAGAIN``
   - Not enough memory to queue the request.
 * - ``EAGAIN``
   - the addition of a new request to the queue would violate
     the ``RTEMS_AIO_MAX`` limit.
 * - ``EINVAL``
   - ``aiocbp->aio_sigevent`` does not point to a valid sigevent struct.
 * - ``EINVAL``
   - ``aiocbp`` is a NULL pointer.
```

**DESCRIPTION:**

The `aio_write()` function is the asynchronous equivalent of `write()`.
This function returns immediately, the request is serviced by thread(s)
running in the background.

The parameters for the write are specified in the `aiocbp` structure.

**NOTES:**

NONE

(lio-listio)=

### lio_listio - List Directed I/O

```{index} lio_listio
```

```{index} list directed i/o
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int lio_listio(
    int mode,
    struct aiocb *restrict const list[restrict],
    int nent,
    struct sigevent *restrict sig
);
```

**STATUS CODES:**

If the call to `lio_listio` is successful, zero is returned.
On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - The project has been build with RTEMS_POSIX_API not defined.
 * - ``EAGAIN``
   - The call failed due to resources limitations.
 * - ``EAGAIN``
   - The number of entries indicated by nent value would cause the
     ``RTEMS_AIO_MAX`` limit to be excedeed.
 * - ``EINVAL``
   - list is a ``NULL`` pointer.
 * - ``EINVAL``
   -  ``mode`` is not a valid value.
 * - ``EINVAL``
   - the value of ``nent`` is not valid or higher than ``AIO_LISTIO_MAX``.
 * - ``EINVAL``
   - the ``sigevent`` struct pointed by ``sig`` is not valid.
 * - ``EINTR``
   - The wait for list completion during a ``LIO_WAIT`` operation was
     interrupted by an external event.
 * - ``EIO``
   - One or more of the individual I/O operations failed.
```

**DESCRIPTION:**

The `lio_listio()` function allows for the simultaneous initiation of
multiple asynchronous I/O operations.

Each operation is described by an `aiocb` structure in the array `list`.

The `mode` parameter determines when the function will return.
If `mode` is `LIO_WAIT` the function returns when the I/O operation have
completed, if `mode` is `LIO_NOWAIT` the function returns after enqueueing
the operations.

If `mode` is `LIO_NOWAIT`, the sigevent struct pointed by `sig` is used to
notify list completion.

**NOTES:**

When the `mode` is `LIO_NOWAIT` and the `sigev_notify` field of `sig`
is set to `SIGEV_SIGNAL`, a signal is sent to the process to notify the
completion of the list. Since each RTEMS application is logically a single POSIX
process, if the user wants to wait for the signal (using, for example,
`sigwait()`), it is necessary to ensure that the signal is blocked by every
thread.

This function is only available when `RTEMS_POSIX_API` is defined. To do so,
it's necessary to add `RTEMS_POSIX_API = True` to the `config.ini` file.

(aio-error)=

### aio_error - Retrieve Error Status of Asynchronous I/O Operation

```{index} aio_error
```

```{index} retrieve error status of asynchronous i/o operation
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int aio_error(
    const struct aiocb *aiocbp
);
```

**STATUS CODES:**

The function return the error status of the request, if 0 is returned the
operation completed without errors.

If the request is still in progress, the function returns `EINPROGRESS`.

On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The return status for the request has already been retrieved.
 * - ``EINVAL``
   - ``aiocbp`` is a NULL pointer.
```

**DESCRIPTION:**

The `aio_error()` function retrieves the error status of the request.

`aiocbp` is a pointer to the request control block.

**NOTES:**

NONE
.. \_aio_return:

### aio_return - Retrieve Return Status of Asynchronous I/O Operation

```{index} aio_return
```

```{index} retrieve return status asynchronous i/o operation
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
ssize_t aio_return(
    struct aiocb *aiocbp
);
```

**STATUS CODES:**

If the result can be returned, it is returned as defined by the various
operations.

On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The return status for the request has already been retrieved.
 * - ``EINVAL``
   - ``aiocbp`` is a NULL pointer.
```

**DESCRIPTION:**

The `aio_return()` function retrieves the return status of the
asynchronous I/O operation.
`aiocbp` is a pointer to the request control block.

**NOTES:**

NONE

(aio-cancel)=

### aio_cancel - Cancel Asynchronous I/O Request

```{index} aio_cancel
```

```{index} cancel asynchronous i/o request
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int aio_cancel(
    int fildes,
    struct aiocb *aiocbp
);
```

**STATUS CODES:**

If the function terminated without errors, the return value has one
of the following values:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``AIO_CANCELED``
   - The requested operation(s) were canceled.
 * - ``AIO_NOTCANCELED``
   - Some operations could not be canceled because they are in progress.
 * - ``AIO_ALLDONE``
   - None of the operations could be canceled because they are already complete.
```

If the file descriptor is invalid, -1 is returned and `errno` is set to `EBADF`

**DESCRIPTION:**

The `aio_cancel()` function attempts to cancel asynchronous I/O operations.

`filedes` is the file descriptor associated with the operations to be canceled.
`aiocbp` is a pointer to an asynchronous I/O control block.

If `aiocbp` is NULL, the function will attempt to eliminate all the operations
enqueued for the specified `filedes`.

If `aiocbp` points to a control block, then only the referenced operation
shall be eliminated.
The `aio_filedef` value of `aiocbp` must be equal to `filedes`, otherwise
the function will return with an error.

**NOTES:**

NONE

(aio-suspend)=

### aio_suspend - Wait for Asynchronous I/O Request

```{index} aio_suspend
```

```{index} wait for asynchronous i/o request
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int aio_suspend(
    const struct aiocb *const list[],
    int nent,
    const struct timespec *timeout
);
```

**STATUS CODES:**

On success, zero is returned.
On error, -1 is returned, and `errno` is set appropriately.

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``E``
   - The
```

**DESCRIPTION:**

The `aio_suspend()` function suspends the calling process until one or more
operations have completed or until the specified `timeout` has expired.
`list` contains the requests that must complete.

**NOTES:**

This routine is not currently supported by RTEMS.

(aio-fsync)=

### aio_fsync - Asynchronous File Synchronization

```{index} aio_fsync
```

```{index} asynchronous file synchronization
```

**CALLING SEQUENCE:**

```c
#include <aio.h>
int aio_fsync(
    int op,
    struct aiocb *aiocbp
);
```

**STATUS CODES:**

If the requests are succesfully enqueued, zero is returned.
On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EAGAIN``
   - The operation could not be queued due to temporary resource limitations.
 * - ``EAGAIN``
   - the addition of a new request to the queue would violate
     the ``RTEMS_AIO_MAX`` limit.
 * - ``EBADF``
   - The aio_fildes member of aiocbp is not a valid file descriptor.
 * - ``EINVAL``
   - A value of op other than O_SYNC or O_DSYNC was specified.
 * - ``EINVAL``
   - ``aiocbp->aio_sigevent`` does not point to a valid sigevent struct.
 * - ``EINVAL``
   - ``aiocbp`` is a NULL pointer.
```

**DESCRIPTION:**

The `aio_fsync()` function initiates an asynchronous file sync operation.
`op` specifies what kind of synchronization should be performed.
If `op` is `O_SYNC`, all currently queued I/O operations shall be
synchronized as if by a call to `fsync()`.
If `op` is `O_DSYNC`, all currently queued I/O operations shall be
synchronized as if by a call to `fdatasync()`.

**NOTES:**

Currently, `O_DSYNC` and `O_SYNC` are mapped to the same value.
As a result, every file will be synced as if by a call to `fsync()`.
