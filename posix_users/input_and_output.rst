Input and Output Primitives Manager
###################################

Introduction
============

The input and output primitives manager is ...

The directives provided by the input and output primitives manager are:

- ``pipe`` - Create an Inter-Process Channel

- ``dup`` - Duplicates an open file descriptor

- ``dup2`` - Duplicates an open file descriptor

- ``close`` - Closes a file

- ``read`` - Reads from a file

- ``write`` - Writes to a file

- ``fcntl`` - Manipulates an open file descriptor

- ``lseek`` - Reposition read/write file offset

- ``fsync`` - Synchronize file complete in-core state with that on disk

- ``fdatasync`` - Synchronize file in-core data with that on disk

- ``sync`` - Schedule file system updates

- ``mount`` - Mount a file system

- ``unmount`` - Unmount file systems

- ``readv`` - Vectored read from a file

- ``writev`` - Vectored write to a file

- ``aio_read`` - Asynchronous Read

- ``aio_write`` - Asynchronous Write

- ``lio_listio`` - List Directed I/O

- ``aio_error`` - Retrieve Error Status of Asynchronous I/O Operation

- ``aio_return`` - Retrieve Return Status Asynchronous I/O Operation

- ``aio_cancel`` - Cancel Asynchronous I/O Request

- ``aio_suspend`` - Wait for Asynchronous I/O Request

- ``aio_fsync`` - Asynchronous File Synchronization

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the input and output primitives manager's directives.
A subsection is dedicated to each of this manager's directives
and describes the calling sequence, related constants, usage,
and status codes.

pipe - Create an Inter-Process Channel
--------------------------------------
.. index:: pipe
.. index:: create an inter

**CALLING SEQUENCE:**

.. code:: c

    int pipe(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

dup - Duplicates an open file descriptor
----------------------------------------
.. index:: dup
.. index:: duplicates an open file descriptor

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int dup(
    int fildes
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor.

*EINTR*
    Function was interrupted by a signal.

*EMFILE*
    The process already has the maximum number of file descriptors open
    and tried to open a new one.

**DESCRIPTION:**

The ``dup`` function returns the lowest numbered available file
descriptor. This new desciptor refers to the same open file as the
original descriptor and shares any locks.

**NOTES:**

NONE

dup2 - Duplicates an open file descriptor
-----------------------------------------
.. index:: dup2
.. index:: duplicates an open file descriptor

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int dup2(
    int fildes,
    int fildes2
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor.

*EINTR*
    Function was interrupted by a signal.

*EMFILE*
    The process already has the maximum number of file descriptors open
    and tried to open a new one.

**DESCRIPTION:**

``dup2`` creates a copy of the file descriptor ``oldfd``.

The old and new descriptors may be used interchangeably. They share locks, file
position pointers and flags; for example, if the file position is modified by using``lseek`` on one of the descriptors, the position is also changed for the other.

**NOTES:**

NONE

close - Closes a file
---------------------
.. index:: close
.. index:: closes a file.

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int close(
    int fildes
    );

**STATUS CODES:**

*EBADF*
    Invalid file descriptor

*EINTR*
    Function was interrupted by a signal.

**DESCRIPTION:**

The ``close()`` function deallocates the file descriptor named by``fildes`` and makes it available for reuse. All outstanding
record locks owned by this process for the file are unlocked.

**NOTES:**

A signal can interrupt the ``close()`` function. In that case,``close()`` returns -1 with ``errno`` set to EINTR. The file
may or may not be closed.

read - Reads from a file
------------------------
.. index:: read
.. index:: reads from a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int read(
    int           fildes,
    void         \*buf,
    unsigned int  nbyte
    );

**STATUS CODES:**

On error, this routine returns -1 and sets ``errno`` to one of
the following:

*EAGAIN*
    The O_NONBLOCK flag is set for a file descriptor and the process
    would be delayed in the I/O operation.

*EBADF*
    Invalid file descriptor

*EINTR*
    Function was interrupted by a signal.

*EIO*
    Input or output error

*EINVAL*
    Bad buffer pointer

**DESCRIPTION:**

The ``read()`` function reads ``nbyte`` bytes from the file
associated with ``fildes`` into the buffer pointed to by ``buf``.

The ``read()`` function returns the number of bytes actually read
and placed in the buffer. This will be less than ``nbyte`` if:

- The number of bytes left in the file is less than ``nbyte``.

- The ``read()`` request was interrupted by a signal.

- The file is a pipe or FIFO or special file with less than ``nbytes``
  immediately available for reading.

When attempting to read from any empty pipe or FIFO:

- If no process has the pipe open for writing, zero is returned to
  indicate end-of-file.

- If some process has the pipe open for writing and O_NONBLOCK is set,
  -1 is returned and ``errno`` is set to EAGAIN.

- If some process has the pipe open for writing and O_NONBLOCK is clear,``read()`` waits for some data to be written or the pipe to be closed.

When attempting to read from a file other than a pipe or FIFO and no data
is available.

- If O_NONBLOCK is set, -1 is returned and ``errno`` is set to EAGAIN.

- If O_NONBLOCK is clear, ``read()`` waits for some data to become
  available.

- The O_NONBLOCK flag is ignored if data is available.

**NOTES:**

NONE

write - Writes to a file
------------------------
.. index:: write
.. index:: writes to a file

**CALLING SEQUENCE:**

.. code:: c

    #include <unistd.h>
    int write(
    int           fildes,
    const void   \*buf,
    unsigned int  nbytes
    );

**STATUS CODES:**

*EAGAIN*
    The O_NONBLOCK flag is set for a file descriptor and the process
    would be delayed in the I/O operation.

*EBADF*
    Invalid file descriptor

*EFBIG*
    An attempt was made to write to a file that exceeds the maximum file
    size

*EINTR*
    The function was interrupted by a signal.

*EIO*
    Input or output error.

*ENOSPC*
    No space left on disk.

*EPIPE*
    Attempt to write to a pope or FIFO with no reader.

*EINVAL*
    Bad buffer pointer

**DESCRIPTION:**

The ``write()`` function writes ``nbyte`` from the array pointed
to by ``buf`` into the file associated with ``fildes``.

If ``nybte`` is zero and the file is a regular file, the ``write()``
function returns zero and has no other effect. If ``nbyte`` is zero
and the file is a special file, te results are not portable.

The ``write()`` function returns the number of bytes written. This
number will be less than ``nbytes`` if there is an error. It will never
be greater than ``nbytes``.

**NOTES:**

NONE

fcntl - Manipulates an open file descriptor
-------------------------------------------
.. index:: fcntl
.. index:: manipulates an open file descriptor

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <fcntl.h>
    #include <unistd.h>
    int fcntl(
    int fildes,
    int cmd
    );

**STATUS CODES:**

*EACCESS*
    Search permission is denied for a direcotry in a file's path
    prefix.

*EAGAIN*
    The O_NONBLOCK flag is set for a file descriptor and the process
    would be delayed in the I/O operation.

*EBADF*
    Invalid file descriptor

*EDEADLK*
    An ``fcntl`` with function F_SETLKW would cause a deadlock.

*EINTR*
    The functioin was interrupted by a signal.

*EINVAL*
    Invalid argument

*EMFILE*
    Too many file descriptor or in use by the process.

*ENOLCK*
    No locks available

**DESCRIPTION:**

``fcntl()`` performs one of various miscellaneous operations on``fd``. The operation in question is determined by ``cmd``:

*F_DUPFD*
    Makes ``arg`` be a copy of ``fd``, closing ``fd`` first if necessary.
    The same functionality can be more easily achieved by using ``dup2()``.
    The old and new descriptors may be used interchangeably. They share locks,
    file position pointers and flags; for example, if the file position is
    modified by using ``lseek()`` on one of the descriptors, the position is
    also changed for the other.
    The two descriptors do not share the close-on-exec flag, however. The
    close-on-exec flag of the copy is off, meaning that it will be closed on
    exec.
    On success, the new descriptor is returned.

*F_GETFD*
    Read the close-on-exec flag. If the low-order bit is 0, the file will
    remain open across exec, otherwise it will be closed.

*F_SETFD*
    Set the close-on-exec flag to the value specified by ``arg`` (only the least
    significant bit is used).

*F_GETFL*
    Read the descriptor's flags (all flags (as set by open()) are returned).

*F_SETFL*
    Set the descriptor's flags to the value specified by ``arg``. Only``O_APPEND`` and ``O_NONBLOCK`` may be set.
    The flags are shared between copies (made with ``dup()`` etc.) of the same
    file descriptor.
    The flags and their semantics are described in ``open()``.

*F_GETLK, F_SETLK and F_SETLKW*
    Manage discretionary file locks. The third argument ``arg`` is a pointer to a
    struct flock (that may be overwritten by this call).

*F_GETLK*
    Return the flock structure that prevents us from obtaining the lock, or set the``l_type`` field of the lock to ``F_UNLCK`` if there is no obstruction.

*F_SETLK*
    The lock is set (when ``l_type`` is ``F_RDLCK`` or ``F_WRLCK``) or
    cleared (when it is ``F_UNLCK``. If lock is held by someone else, this
    call returns -1 and sets ``errno`` to EACCES or EAGAIN.

*F_SETLKW*
    Like ``F_SETLK``, but instead of returning an error we wait for the lock to
    be released.

*F_GETOWN*
    Get the process ID (or process group) of the owner of a socket.
    Process groups are returned as negative values.

*F_SETOWN*
    Set the process or process group that owns a socket.
    For these commands, ownership means receiving ``SIGIO`` or ``SIGURG``
    signals.
    Process groups are specified using negative values.

**NOTES:**

The errors returned by ``dup2`` are different from those returned by``F_DUPFD``.

lseek - Reposition read/write file offset
-----------------------------------------
.. index:: lseek
.. index:: reposition read/write file offset

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/types.h>
    #include <unistd.h>
    int lseek(
    int    fildes,
    off_t  offset,
    int    whence
    );

**STATUS CODES:**

*EBADF*
    ``fildes`` is not an open file descriptor.

*ESPIPE*
    ``fildes`` is associated with a pipe, socket or FIFO.

*EINVAL*
    ``whence`` is not a proper value.

**DESCRIPTION:**

The ``lseek`` function repositions the offset of the file descriptor``fildes`` to the argument offset according to the directive whence.
The argument ``fildes`` must be an open file descriptor. ``Lseek``
repositions the file pointer fildes as follows:

- If ``whence`` is SEEK_SET, the offset is set to ``offset`` bytes.

- If ``whence`` is SEEK_CUR, the offset is set to its current location
  plus offset bytes.

- If ``whence`` is SEEK_END, the offset is set to the size of the
  file plus ``offset`` bytes.

The ``lseek`` function allows the file offset to be set beyond the end
of the existing end-of-file of the file. If data is later written at this
point, subsequent reads of the data in the gap return bytes of zeros
(until data is actually written into the gap).

Some devices are incapable of seeking. The value of the pointer associated
with such a device is undefined.

**NOTES:**

NONE

fsync - Synchronize file complete in-core state with that on disk
-----------------------------------------------------------------
.. index:: fsync
.. index:: synchronize file complete in

**CALLING SEQUENCE:**

.. code:: c

    int fsync(
    int fd
    );

**STATUS CODES:**

On success, zero is returned. On error, -1 is returned, and ``errno``
is set appropriately.

*EBADF*
    ``fd`` is not a valid descriptor open for writing

*EINVAL*
    ``fd`` is bound to a special file which does not support support synchronization

*EROFS*
    ``fd`` is bound to a special file which does not support support synchronization

*EIO*
    An error occurred during synchronization

**DESCRIPTION:**

``fsync`` copies all in-core parts of a file to disk.

**NOTES:**

NONE

fdatasync - Synchronize file in-core data with that on disk
-----------------------------------------------------------
.. index:: fdatasync
.. index:: synchronize file in

**CALLING SEQUENCE:**

.. code:: c

    int fdatasync(
    int fd
    );

**STATUS CODES:**

On success, zero is returned. On error, -1 is returned, and ``errno`` is
set appropriately.

*EBADF*
    ``fd`` is not a valid file descriptor open for writing.

*EINVAL*
    ``fd`` is bound to a special file which does not support synchronization.

*EIO*
    An error occurred during synchronization.

*EROFS*
    ``fd`` is bound to a special file which dows not support synchronization.

**DESCRIPTION:**

``fdatasync`` flushes all data buffers of a file to disk (before the system call
returns). It resembles ``fsync`` but is not required to update the metadata such
as access time.

Applications that access databases or log files often write a tiny data fragment
(e.g., one line in a log file) and then call ``fsync`` immediately in order to
ensure that the written data is physically stored on the harddisk. Unfortunately,
fsync will always initiate two write operations: one for the newly written data and
another one in order to update the modification time stored in the inode. If the
modification time is not a part of the transaction concept ``fdatasync`` can be
used to avoid unnecessary inode disk write operations.

**NOTES:**

NONE

sync - Schedule file system updates
-----------------------------------
.. index:: sync
.. index:: synchronize file systems

**CALLING SEQUENCE:**

.. code:: c

    void sync(void);

**STATUS CODES:**

NONE

**DESCRIPTION:**

The ``sync`` service causes all information in memory that updates
file systems to be scheduled for writing out to all file systems.

**NOTES:**

The writing of data to the file systems is only guaranteed to be
scheduled upon return.  It is not necessarily complete upon return
from ``sync``.

mount - Mount a file system
---------------------------
.. index:: mount
.. index:: mount a file system

**CALLING SEQUENCE:**

.. code:: c

    #include <libio.h>
    int mount(
    rtems_filesystem_mount_table_entry_t \**mt_entry,
    rtems_filesystem_operations_table    \*fs_ops,
    rtems_filesystem_options_t            fsoptions,
    char                                 \*device,
    char                                 \*mount_point
    );

**STATUS CODES:**

*EXXX*

**DESCRIPTION:**

The ``mount`` routines mounts the filesystem class
which uses the filesystem operations specified by ``fs_ops``
and ``fsoptions``.  The filesystem is mounted at the directory``mount_point`` and the mode of the mounted filesystem is
specified by ``fsoptions``.  If this filesystem class requires
a device, then the name of the device must be specified by ``device``.

If this operation succeeds, the mount table entry for the mounted
filesystem is returned in ``mt_entry``.

**NOTES:**

NONE

unmount - Unmount file systems
------------------------------
.. index:: unmount
.. index:: unmount file systems

**CALLING SEQUENCE:**

.. code:: c

    #include <libio.h>
    int unmount(
    const char \*mount_path
    );

**STATUS CODES:**

*EXXX*

**DESCRIPTION:**

The ``unmount`` routine removes the attachment of the filesystem specified
by ``mount_path``.

**NOTES:**

NONE

readv - Vectored read from a file
---------------------------------
.. index:: readv
.. index:: vectored read from a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/uio.h>
    ssize_t readv(
    int                 fd,
    const struct iovec \*iov,
    int                 iovcnt
    );

**STATUS CODES:**

In addition to the errors detected by``Input and Output Primitives Manager read - Reads from a file, read()``,
this routine may return -1 and sets ``errno`` based upon the following
errors:

*EINVAL*
    The sum of the ``iov_len`` values in the iov array overflowed an``ssize_t``.

*EINVAL*
    The ``iovcnt`` argument was less than or equal to 0, or greater
    than ``IOV_MAX``.

**DESCRIPTION:**

The ``readv()`` function is equivalent to ``read()``
except as described here. The ``readv()`` function shall place
the input data into the ``iovcnt`` buffers specified by the
members of the ``iov`` array: ``iov[0], iov[1], ..., iov[iovcnt-1]``.

Each ``iovec`` entry specifies the base address and length of an area
in memory where data should be placed. The ``readv()`` function
always fills an area completely before proceeding to the next.

**NOTES:**

NONE

writev - Vectored write to a file
---------------------------------
.. index:: writev
.. index:: vectored write to a file

**CALLING SEQUENCE:**

.. code:: c

    #include <sys/uio.h>
    ssize_t writev(
    int                 fd,
    const struct iovec \*iov,
    int                 iovcnt
    );

**STATUS CODES:**

In addition to the errors detected by``Input and Output Primitives Manager write - Write to a file, write()``,
this routine may return -1 and sets ``errno`` based upon the following
errors:

*EINVAL*
    The sum of the ``iov_len`` values in the iov array overflowed an``ssize_t``.

*EINVAL*
    The ``iovcnt`` argument was less than or equal to 0, or greater
    than ``IOV_MAX``.

**DESCRIPTION:**

The ``writev()`` function is equivalent to ``write()``,
except as noted here. The ``writev()`` function gathers output
data from the ``iovcnt`` buffers specified by the members of
the ``iov array``: ``iov[0], iov[1], ..., iov[iovcnt-1]``.
The ``iovcnt`` argument is valid if greater than 0 and less
than or equal to ``IOV_MAX``.

Each ``iovec`` entry specifies the base address and length of
an area in memory from which data should be written. The ``writev()``
function always writes a complete area before proceeding to the next.

If ``fd`` refers to a regular file and all of the ``iov_len``
members in the array pointed to by ``iov`` are 0, ``writev()``
returns 0 and has no other effect. For other file types, the behavior
is unspecified by POSIX.

**NOTES:**

NONE

aio_read - Asynchronous Read
----------------------------
.. index:: aio_read
.. index:: asynchronous read

**CALLING SEQUENCE:**

.. code:: c

    int aio_read(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_write - Asynchronous Write
------------------------------
.. index:: aio_write
.. index:: asynchronous write

**CALLING SEQUENCE:**

.. code:: c

    int aio_write(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

lio_listio - List Directed I/O
------------------------------
.. index:: lio_listio
.. index:: list directed i/o

**CALLING SEQUENCE:**

.. code:: c

    int lio_listio(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_error - Retrieve Error Status of Asynchronous I/O Operation
---------------------------------------------------------------
.. index:: aio_error
.. index:: retrieve error status of asynchronous i/o operation

**CALLING SEQUENCE:**

.. code:: c

    int aio_error(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_return - Retrieve Return Status Asynchronous I/O Operation
--------------------------------------------------------------
.. index:: aio_return
.. index:: retrieve return status asynchronous i/o operation

**CALLING SEQUENCE:**

.. code:: c

    int aio_return(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_cancel - Cancel Asynchronous I/O Request
--------------------------------------------
.. index:: aio_cancel
.. index:: cancel asynchronous i/o request

**CALLING SEQUENCE:**

.. code:: c

    int aio_cancel(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_suspend - Wait for Asynchronous I/O Request
-----------------------------------------------
.. index:: aio_suspend
.. index:: wait for asynchronous i/o request

**CALLING SEQUENCE:**

.. code:: c

    int aio_suspend(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

aio_fsync - Asynchronous File Synchronization
---------------------------------------------
.. index:: aio_fsync
.. index:: asynchronous file synchronization

**CALLING SEQUENCE:**

.. code:: c

    int aio_fsync(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

