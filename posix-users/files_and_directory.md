% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Files and Directories Manager

## Introduction

The files and directories manager is ...

The directives provided by the files and directories manager are:

- [opendir] - Open a Directory
- [readdir] - Reads a directory
- [rewinddir] - Resets the `readdir()` pointer
- [scandir] - Scan a directory for matching entries
- [telldir] - Return current location in directory stream
- [closedir] - Ends directory read operation
- [getdents] - Get directory entries
- [chdir] - Changes the current working directory
- [fchdir] - Changes the current working directory
- [getcwd] - Gets current working directory
- [open] - Opens a file
- [creat] - Create a new file or rewrite an existing one
- [umask] - Sets a file creation mask
- [link] - Creates a link to a file
- [symlink] - Creates a symbolic link to a file
- [readlink] - Obtain the name of the link destination
- [mkdir] - Makes a directory
- [mkfifo] - Makes a FIFO special file
- [unlink] - Removes a directory entry
- [rmdir] - Delete a directory
- [rename] - Renames a file
- [stat] - Gets information about a file.
- [fstat] - Gets file status
- [lstat] - Gets file status
- [access] - Check permissions for a file.
- [chmod] - Changes file mode
- [fchmod] - Changes permissions of a file
- [chown] - Changes the owner and/ or group of a file
- [utime] - Change access and/or modification times of an inode
- [ftruncate] - Truncate a file to a specified length
- [truncate] - Truncate a file to a specified length
- [pathconf] - Gets configuration values for files
- [fpathconf] - Get configuration values for files
- [mknod] - Create a directory

## Background

### Path Name Evaluation

A pathname is a string that consists of no more than `PATH_MAX` bytes,
including the terminating null character. A pathname has an optional beginning
slash, followed by zero or more filenames separated by slashes. If the
pathname refers to a directory, it may also have one or more trailing
slashes. Multiple successive slahes are considered to be the same as one slash.

POSIX allows a pathname that begins with precisely two successive slashes to be
interpreted in an implementation-defined manner. RTEMS does not currently
recognize this as a special condition. Any number of successive slashes is
treated the same as a single slash. POSIX requires that an implementation treat
more than two leading slashes as a single slash.

## Operations

There is currently no text in this section.

## Directives

This section details the files and directories manager's directives. A
subsection is dedicated to each of this manager's directives and describes the
calling sequence, related constants, usage, and status codes.

(opendir)=

### opendir - Open a Directory

```{index} opendir
```

```{index} open a directory
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <dirent.h>
int opendir(
    const char *dirname
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission was denied on a component of the path prefix of
     ``dirname``, or read permission is denied
 * - ``EMFILE``
   - Too many file descriptors in use by process
 * - ``ENFILE``
   - Too many files are currently open in the system.
 * - ``ENOENT``
   - Directory does not exist, or ``name`` is an empty string.
 * - ``ENOMEM``
   - Insufficient memory to complete the operation.
 * - ``ENOTDIR``
   - ``name`` is not a directory.
```

**DESCRIPTION:**

This routine opens a directory stream corresponding to the
directory specified by the `dirname` argument. The
directory stream is positioned at the first entry.

**NOTES:**

The routine is implemented in Cygnus newlib.

(readdir)=

### readdir - Reads a directory

```{index} readdir
```

```{index} reads a directory
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <dirent.h>
    int readdir(
    DIR *dirp
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
```

**DESCRIPTION:**

The `readdir()` function returns a pointer to a structure `dirent`
representing the next directory entry from the directory stream pointed to by
`dirp`. On end-of-file, `NULL` is returned.

The `readdir()` function may (or may not) return entries for `.` or `..`
Your program should tolerate reading dot and dot-dot but not require them.

The data pointed to be `readdir()` may be overwritten by another call to
`readdir()` for the same directory stream. It will not be overwritten by a
call for another directory.

**NOTES:**

If `ptr` is not a pointer returned by `malloc()`, `calloc()`, or
`realloc()` or has been deallocated with `free()` or `realloc()`, the
results are not portable and are probably disastrous.

The routine is implemented in Cygnus newlib.

(rewinddir)=

### rewinddir - Resets the readdir() pointer

```{index} rewinddir
```

```{index} resets the readdir() pointer
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <dirent.h>
void rewinddir(
    DIR *dirp
);
```

**STATUS CODES:**

No value is returned.

**DESCRIPTION:**

The `rewinddir()` function resets the position associated with the directory
stream pointed to by `dirp`. It also causes the directory stream to refer to
the current state of the directory.

**NOTES:**

NONE

If `dirp` is not a pointer by `opendir()`, the results are undefined.

The routine is implemented in Cygnus newlib.

(scandir)=

### scandir - Scan a directory for matching entries

```{index} scandir
```

```{index} scan a directory for matching entries
```

**CALLING SEQUENCE:**

```c
#include <dirent.h>
int scandir(
    const char       *dir,
    struct dirent ***namelist,
    int  (*select)(const struct dirent *),
    int  (*compar)(const struct dirent **, const struct dirent **)
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOMEM``
   - Insufficient memory to complete the operation.
```

**DESCRIPTION:**

The `scandir()` function scans the directory `dir`, calling `select()` on
each directory entry. Entries for which `select()` returns non-zero are
stored in strings allocated via `malloc()`, sorted using `qsort()` with the
comparison function `compar()`, and collected in array `namelist` which is
allocated via `malloc()`. If `select` is `NULL`, all entries are
selected.

**NOTES:**

The routine is implemented in Cygnus newlib.

(telldir)=

### telldir - Return current location in directory stream

```{index} telldir
```

```{index} return current location in directory stream
```

**CALLING SEQUENCE:**

```c
#include <dirent.h>
off_t telldir(
    DIR *dir
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid directory stream descriptor ``dir``.
```

**DESCRIPTION:**

The `telldir()` function returns the current location associated with the
directory stream `dir`.

**NOTES:**

The routine is implemented in Cygnus newlib.

(closedir)=

### closedir - Ends directory read operation

```{index} closedir
```

```{index} ends directory read operation
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <dirent.h>
int closedir(
    DIR *dirp
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
```

**DESCRIPTION:**

The directory stream associated with `dirp` is closed. The value in `dirp`
may not be usable after a call to `closedir()`.

**NOTES:**

NONE

The argument to `closedir()` must be a pointer returned by `opendir()`. If
it is not, the results are not portable and most likely unpleasant.

The routine is implemented in Cygnus newlib.

(chdir)=

### chdir - Changes the current working directory

```{index} chdir
```

```{index} changes the current working directory
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int chdir(
    const char *path
);
```

**STATUS CODES:**

On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when directory
     was expected.
```

**DESCRIPTION:**

The `chdir()` function causes the directory named by `path` to become the
current working directory; that is, the starting point for searches of
pathnames not beginning with a slash.

If `chdir()` detects an error, the current working directory is not changed.

**NOTES:**

NONE

(fchdir)=

### fchdir - Changes the current working directory

```{index} fchdir
```

```{index} changes the current working directory
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int fchdir(
    int fd
);
```

**STATUS CODES:**

On error, this routine returns -1 and sets `errno` to one of the following:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when directory
     was expected.
```

**DESCRIPTION:**

The `fchdir()` function causes the directory named by `fd` to become the
current working directory; that is, the starting point for searches of
pathnames not beginning with a slash.

If `fchdir()` detects an error, the current working directory is not changed.

**NOTES:**

NONE

(getcwd)=

### getcwd - Gets current working directory

```{index} getcwd
```

```{index} gets current working directory
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int getcwd( void );
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument
 * - ``ERANGE``
   - Result is too large
 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
```

**DESCRIPTION:**

The `getcwd()` function copies the absolute pathname of the current working
directory to the character array pointed to by `buf`. The `size` argument
is the number of bytes available in `buf`

**NOTES:**

There is no way to determine the maximum string length that `fetcwd()` may
need to return. Applications should tolerate getting `ERANGE` and allocate a
larger buffer.

It is possible for `getcwd()` to return EACCES if, say, `login` puts the
process into a directory without read access.

The 1988 standard uses `int` instead of `size_t` for the second parameter.

(open)=

### open - Opens a file

```{index} open
```

```{index} opens a file
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int open(
    const char *path,
    int         oflag,
    mode_t      mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
 * - ``EEXIST``
   - The named file already exists.
 * - ``EINTR``
   - Function was interrupted by a signal.
 * - ``EISDIR``
   - Attempt to open a directory for writing or to rename a file to be a
     directory.
 * - ``EMFILE``
   - Too many file descriptors are in use by this process.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENFILE``
   - Too many files are currently open in the system.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``ENXIO``
   - No such device. This error may also occur when a device is not ready, for
     example, a tape drive is off-line.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

The `open` function establishes a connection between a file and a file
descriptor. The file descriptor is a small integer that is used by I/O
functions to reference the file. The `path` argument points to the pathname
for the file.

The `oflag` argument is the bitwise inclusive OR of the values of symbolic
constants. The programmer must specify exactly one of the following three
symbols:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``O_RDONLY``
   - Open for reading only.
 * - ``O_WRONLY``
   - Open for writing only.
 * - ``O_RDWR``
   - Open for reading and writing.
```

Any combination of the following symbols may also be used.

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``O_APPEND``
   - Set the file offset to the end-of-file prior to each write.
 * - ``O_CREAT``
   - If the file does not exist, allow it to be created. This flag indicates
     that the ``mode`` argument is present in the call to ``open``.
 * - ``O_EXCL``
   - This flag may be used only if ``O_CREAT`` is also set. It causes the call
     to ``open`` to fail if the file already exists.
 * - ``O_NOCTTY``
   - Do not assign controlling terminal.
 * - ``O_NONBLOCK``
   - Do no wait for the device or file to be ready or available. After the file
     is open, the ``read`` and ``write`` calls return immediately. If the
     process would be delayed in the read or write opermation, -1 is returned
     and``errno`` is set to ``EAGAIN`` instead of blocking the caller.
 * - ``O_TRUNC``
   - This flag should be used only on ordinary files opened for writing. It
     causes the file to be tuncated to zero length..
```

Upon successful completion, `open` returns a non-negative file descriptor.

**NOTES:**

NONE

(creat)=

### creat - Create a new file or rewrite an existing one

```{index} creat
```

```{index} create a new file or rewrite an existing one
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int creat(
    const char *path,
    mode_t      mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EEXIST``
   - ``path`` already exists and ``O_CREAT`` and ``O_EXCL`` were used.
 * - ``EISDIR``
   - ``path`` refers to a directory and the access requested involved writing
 * - ``ETXTBSY``
   - ``path`` refers to an executable image which is currently being executed
     and write access was requested
 * - ``EFAULT``
   - ``path`` points outside your accessible address space
 * - ``EACCES``
   - The requested access to the file is not allowed, or one of the directories
     in ``path`` did not allow search (execute) permission.
 * - ``ENAMETOOLONG``
   - ``path`` was too long.
 * - ``ENOENT``
   - A directory component in ``path`` does not exist or is a dangling symbolic
     link.
 * - ``ENOTDIR``
   - A component used as a directory in ``path`` is not, in fact, a directory.
 * - ``EMFILE``
   - The process alreadyh has the maximum number of files open.
 * - ``ENFILE``
   - The limit on the total number of files open on the system has been
     reached.
 * - ``ENOMEM``
   - Insufficient kernel memory was available.
 * - ``EROFS``
   - ``path`` refers to a file on a read-only filesystem and write access was
     requested
```

**DESCRIPTION:**

`creat` attempts to create a file and return a file descriptor for use in
read, write, etc.

**NOTES:**

NONE

The routine is implemented in Cygnus newlib.

(umask)=

### umask - Sets a file creation mask.

```{index} umask
```

```{index} sets a file creation mask.
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
mode_t umask(
    mode_t cmask
);
```

**STATUS CODES:**

**DESCRIPTION:**

The `umask()` function sets the process file creation mask to `cmask`. The
file creation mask is used during `open()`, `creat()`, `mkdir()`,
`mkfifo()` calls to turn off permission bits in the `mode` argument. Bit
positions that are set in `cmask` are cleared in the mode of the created
file.

**NOTES:**

NONE

The `cmask` argument should have only permission bits set. All other bits
should be zero.

In a system which supports multiple processes, the file creation mask is
inherited across `fork()` and `exec()` calls. This makes it possible to
alter the default permission bits of created files. RTEMS does not support
multiple processes so this behavior is not possible.

(link)=

### link - Creates a link to a file

```{index} link
```

```{index} creates a link to a file
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int link(
    const char *existing,
    const char *new
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``EEXIST``
   - The named file already exists.
 * - ``EMLINK``
   - The number of links would exceed ``LINK_MAX``.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``EPERM``
   - Operation is not permitted. Process does not have the appropriate
     priviledges or permissions to perform the requested operations.
 * - ``EROFS``
   - Read-only file system.
 * - ``EXDEV``
   - Attempt to link a file to another file system.
```

**DESCRIPTION:**

The `link()` function atomically creates a new link for an existing file and
increments the link count for the file.

If the `link()` function fails, no directories are modified.

The `existing` argument should not be a directory.

The caller may (or may not) need permission to access the existing file.

**NOTES:**

NONE

(symlink)=

### symlink - Creates a symbolic link to a file

```{index} symlink
```

```{index} creates a symbolic link to a file
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int symlink(
    const char *topath,
    const char *frompath
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``EEXIST``
   - The named file already exists.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``EPERM``
   - Operation is not permitted. Process does not have the appropriate
     priviledges or permissions to perform the requested operations.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

The `symlink()` function creates a symbolic link from the frombath to the
topath. The symbolic link will be interpreted at run-time.

If the `symlink()` function fails, no directories are modified.

The caller may (or may not) need permission to access the existing file.

**NOTES:**

NONE

(readlink)=

### readlink - Obtain the name of a symbolic link destination

```{index} readlink
```

```{index} obtain the name of a symbolic link destination
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int readlink(
    const char *path,
    char       *buf,
    size_t      bufsize
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the prefix pathname was not a directory when a directory
     was expected.
 * - ``ELOOP``
   - Too many symbolic links were encountered in the pathname.
 * - ``EINVAL``
   - The pathname does not refer to a symbolic link
 * - ``EFAULT``
   - An invalid pointer was passed into the ``readlink()`` routine.
```

**DESCRIPTION:**

The `readlink()` function places the symbolic link destination into `buf`
argument and returns the number of characters copied.

If the symbolic link destination is longer than bufsize characters the name
will be truncated.

**NOTES:**

NONE

(mkdir)=

### mkdir - Makes a directory

```{index} mkdir
```

```{index} makes a directory
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int mkdir(
    const char *path,
    mode_t      mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``EEXIST``
   - The name file already exist.
 * - ``EMLINK``
   - The number of links would exceed ``LINK_MAX``
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

The `mkdir()` function creates a new diectory named `path`. The permission
bits (modified by the file creation mask) are set from `mode`. The owner and
group IDs for the directory are set from the effective user ID and group ID.

The new directory may (or may not) contain entries for `.` and `..` but is
otherwise empty.

**NOTES:**

NONE

(mkfifo)=

### mkfifo - Makes a FIFO special file

```{index} mkfifo
```

```{index} makes a fifo special file
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int mkfifo(
    const char *path,
    mode_t      mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``EEXIST``
   - The named file already exists.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``ENOTDIR``
   - A component of the specified ``path`` was not a directory when a directory
     was expected.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

The `mkfifo()` function creates a new FIFO special file named `path`. The
permission bits (modified by the file creation mask) are set from `mode`. The
owner and group IDs for the FIFO are set from the efective user ID and
group ID.

**NOTES:**

NONE

(unlink)=

### unlink - Removes a directory entry

```{index} unlink
```

```{index} removes a directory entry
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int unlink(
    const char path
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``EBUSY``
   - The directory is in use.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the specified ``path`` was not a directory when a directory
     was expected.
 * - ``EPERM``
   - Operation is not permitted. Process does not have the appropriate
     priviledges or permissions to perform the requested operations.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

The `unlink` function removes the link named by `path` and decrements the
link count of the file referenced by the link. When the link count goes to zero
and no process has the file open, the space occupied by the file is freed and
the file is no longer accessible.

**NOTES:**

NONE

(rmdir)=

### rmdir - Delete a directory

```{index} rmdir
```

```{index} delete a directory
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int rmdir(
    const char *pathname
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EPERM``
   - The filesystem containing ``pathname`` does not support the removal of
     directories.
 * - ``EFAULT``
   - ``pathname`` points ouside your accessible address space.
 * - ``EACCES``
   - Write access to the directory containing ``pathname`` was not allowed for
     the process's effective uid, or one of the directories in``pathname`` did
     not allow search (execute) permission.
 * - ``EPERM``
   - The directory containing ``pathname`` has the stickybit (S_ISVTX) set and
     the process's effective uid is neither the uid of the file to be delected
     nor that of the director containing it.
 * - ``ENAMETOOLONG``
   - ``pathname`` was too long.
 * - ``ENOENT``
   - A dirctory component in ``pathname`` does not exist or is a dangling
     symbolic link.
 * - ``ENOTDIR``
   - ``pathname``, or a component used as a directory in ``pathname``, is not,
     in fact, a directory.
 * - ``ENOTEMPTY``
   - ``pathname`` contains entries other than . and .. .
 * - ``EBUSY``
   - ``pathname`` is the current working directory or root directory of some
     process
 * - ``EBUSY``
   - ``pathname`` is the current directory or root directory of some process.
 * - ``ENOMEM``
   - Insufficient kernel memory was available
 * - ``EROGS``
   - ``pathname`` refers to a file on a read-only filesystem.
 * - ``ELOOP``
   - ``pathname`` contains a reference to a circular symbolic link
```

**DESCRIPTION:**

`rmdir` deletes a directory, which must be empty

**NOTES:**

NONE

(rename)=

### rename - Renames a file

```{index} rename
```

```{index} renames a file
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int rename(
    const char *old,
    const char *new
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
 * - ``EBUSY``
   - The directory is in use.
 * - ``EEXIST``
   - The named file already exists.
 * - ``EINVAL``
   - Invalid argument.
 * - ``EISDIR``
   - Attempt to open a directory for writing or to rename a file to be a
     directory.
 * - ``EMLINK``
   - The number of links would exceed ``LINK_MAX``.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does no exist.
 * - ``ENOSPC``
   - No space left on disk.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``ENOTEMPTY``
   - Attempt to delete or rename a non-empty directory.
 * - ``EROFS``
   - Read-only file system
 * - ``EXDEV``
   - Attempt to link a file to another file system.
```

**DESCRIPTION:**

The `rename()` function causes the file known bo `old` to now be known as
`new`.

Ordinary files may be renamed to ordinary files, and directories may be renamed
to directories; however, files cannot be converted using `rename()`. The
`new` pathname may not contain a path prefix of `old`.

**NOTES:**

If a file already exists by the name `new`, it is removed. The `rename()`
function is atomic. If the `rename()` detects an error, no files are
removed. This guarantees that the `rename("x", "x")` does not remove `x`.

You may not rename dot or dot-dot.

The routine is implemented in Cygnus newlib using `link()` and `unlink()`.

(stat)=

### stat - Gets information about a file

```{index} stat
```

```{index} gets information about a file
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int stat(
    const char  *path,
    struct stat *buf
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
 * - ``EBADF``
   - Invalid file descriptor.
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
```

**DESCRIPTION:**

The `path` argument points to a pathname for a file. Read, write, or execute
permission for the file is not required, but all directories listed in `path`
must be searchable. The `stat()` function obtains information about the named
file and writes it to the area pointed to by `buf`.

**NOTES:**

NONE

(fstat)=

### fstat - Gets file status

```{index} fstat
```

```{index} gets file status
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int fstat(
    int          fildes,
    struct stat *buf
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
```

**DESCRIPTION:**

The `fstat()` function obtains information about the file associated with
`fildes` and writes it to the area pointed to by the `buf` argument.

**NOTES:**

If the filesystem object referred to by `fildes` is a link, then the
information returned in `buf` refers to the destination of that link. This
is in contrast to `lstat()` which does not follow the link.

(lstat)=

### lstat - Gets file status

```{index} lstat
```

```{index} gets file status
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int lstat(
    int          fildes,
    struct stat *buf
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
```

**DESCRIPTION:**

The `lstat()` function obtains information about the file associated with
`fildes` and writes it to the area pointed to by the `buf` argument.

**NOTES:**

If the filesystem object referred to by `fildes` is a link, then the
information returned in `buf` refers to the link itself. This is in contrast
to `fstat()` which follows the link.

The `lstat()` routine is defined by BSD 4.3 and SVR4 and not included in
POSIX 1003.1b-1996.

(access)=

### access - Check permissions for a file

```{index} access
```

```{index} check permissions for a file
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int access(
    const char *pathname,
    int         mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - The requested access would be denied, either to the file itself or one of
     the directories in ``pathname``.
 * - ``EFAULT``
   - ``pathname`` points outside your accessible address space.
 * - ``EINVAL``
   - ``Mode`` was incorrectly specified.
 * - ``ENAMETOOLONG``
   - ``pathname`` is too long.
 * - ``ENOENT``
   - A directory component in ``pathname`` would have been accessible but does
     not exist or was a dangling symbolic link.
 * - ``ENOTDIR``
   - A component used as a directory in ``pathname`` is not, in fact, a
     directory.
 * - ``ENOMEM``
   - Insufficient kernel memory was available.
```

**DESCRIPTION:**

`Access` checks whether the process would be allowed to read, write or test
for existence of the file (or other file system object) whose name is
`pathname`. If `pathname` is a symbolic link permissions of the file
referred by this symbolic link are tested.

`Mode` is a mask consisting of one or more of `R_OK`, `W_OK`, `X_OK`
and `F_OK`.

**NOTES:**

NONE

(chmod)=

### chmod - Changes file mode.

```{index} chmod
```

```{index} changes file mode.
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int chmod(
    const char *path,
    mode_t      mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``EPERM``
   - Operation is not permitted. Process does not have the appropriate
     priviledges or permissions to perform the requested operations.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

Set the file permission bits, the set user ID bit, and the set group ID bit for
the file named by `path` to `mode`. If the effective user ID does not match
the owner of the file and the calling process does not have the appropriate
privileges, `chmod()` returns -1 and sets `errno` to `EPERM`.

**NOTES:**

NONE

(fchmod)=

### fchmod - Changes permissions of a file

```{index} fchmod
```

```{index} changes permissions of a file
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <sys/stat.h>
int fchmod(
    int    fildes,
    mode_t mode
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix.
 * - ``EBADF``
   - The descriptor is not valid.
 * - ``EFAULT``
   - ``path`` points outside your accessible address space.
 * - ``EIO``
   - A low-level I/o error occurred while modifying the inode.
 * - ``ELOOP``
   - ``path`` contains a circular reference
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does no exist.
 * - ``ENOMEM``
   - Insufficient kernel memory was avaliable.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``EPERM``
   - The effective UID does not match the owner of the file, and is not zero
 * - ``EROFS``
   - Read-only file system
```

**DESCRIPTION:**

The mode of the file given by `path` or referenced by `filedes` is changed.

**NOTES:**

NONE

(getdents)=

### getdents - Get directory entries

```{index} getdents
```

```{index} get directory entries
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
#include <linux/dirent.h>
#include <linux/unistd.h>
long getdents(
    int   dd_fd,
    char *dd_buf,
    int   dd_len
);
```

**STATUS CODES:**

A successful call to `getdents` returns th the number of bytes read. On end
of directory, 0 is returned. When an error occurs, -1 is returned, and
`errno` is set appropriately.

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor ``fd``.
 * - ``EFAULT``
   - Argument points outside the calling process's address space.
 * - ``EINVAL``
   - Result buffer is too small.
 * - ``ENOENT``
   - No such directory.
 * - ``ENOTDIR``
   - File descriptor does not refer to a directory.
```

**DESCRIPTION:**

`getdents` reads several `dirent` structures from the directory pointed by
`fd` into the memory area pointed to by `dirp`. The parameter `count` is
the size of the memory area.

**NOTES:**

NONE

(chown)=

### chown - Changes the owner and/or group of a file.

```{index} chown
```

```{index} changes the owner and/or group of a file.
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
#include <unistd.h>
int chown(
    const char *path,
    uid_t       owner,
    gid_t       group
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Search permission is denied for a directory in a file's path prefix
 * - ``EINVAL``
   - Invalid argument
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist.
 * - ``ENOTDIR``
   - A component of the specified pathname was not a directory when a directory
     was expected.
 * - ``EPERM``
   - Operation is not permitted. Process does not have the appropriate
     priviledges or permissions to perform the requested operations.
 * - ``EROFS``
   - Read-only file system.
```

**DESCRIPTION:**

The user ID and group ID of the file named by `path` are set to `owner` and
`path`, respectively.

For regular files, the set group ID (`S_ISGID`) and set user ID (`S_ISUID`)
bits are cleared.

Some systems consider it a security violation to allow the owner of a file to
be changed, If users are billed for disk space usage, loaning a file to another
user could result in incorrect billing. The `chown()` function may be
restricted to privileged users for some or all files. The group ID can still be
changed to one of the supplementary group IDs.

**NOTES:**

This function may be restricted for some file. The `pathconf` function can be
used to test the `_PC_CHOWN_RESTRICTED` flag.

(utime)=

### utime - Change access and/or modification times of an inode

```{index} utime
```

```{index} change access and/or modification times of an inode
```

**CALLING SEQUENCE:**

```c
#include <sys/types.h>
int utime(
    const char     *filename,
    struct utimbuf *buf
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EACCES``
   - Permission to write the file is denied
 * - ``ENOENT``
   - ``Filename`` does not exist
```

**DESCRIPTION:**

`Utime` changes the access and modification times of the inode specified by
`filename` to the `actime` and `modtime` fields of `buf`
respectively. If `buf` is `NULL`, then the access and modification times of the
file are set to the current time.

**NOTES:**

NONE

(ftruncate)=

### ftruncate - truncate a file to a specified length

```{index} ftruncate
```

```{index} truncate a file to a specified length
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int ftrunctate(
    int    fd,
    size_t length
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOTDIR``
   - A component of the path prefix is not a directory.
 * - ``EINVAL``
   - The pathname contains a character with the high-order bit set.
 * - ``ENAMETOOLONG``
   - The length of the specified pathname exceeds ``PATH_MAX`` bytes, or the length
     of a component of the pathname exceeds ``NAME_MAX`` bytes.
 * - ``ENOENT``
   - The named file does not exist.
 * - ``EACCES``
   - The named file is not writable by the user.
 * - ``EACCES``
   - Search permission is denied for a component of the path prefix.
 * - ``ELOOP``
   - Too many symbolic links were encountered in translating the pathname
 * - ``EISDIR``
   - The named file is a directory.
 * - ``EROFS``
   - The named file resides on a read-only file system
 * - ``ETXTBSY``
   - The file is a pure procedure (shared text) file that is being executed
 * - ``EIO``
   - An I/O error occurred updating the inode.
 * - ``EFAULT``
   - ``Path`` points outside the process's allocated address space.
 * - ``EBADF``
   - The ``fd`` is not a valid descriptor.
```

**DESCRIPTION:**

`truncate()` causes the file named by `path` or referenced by `fd` to be
truncated to at most `length` bytes in size. If the file previously was
larger than this size, the extra data is lost. With `ftruncate()`, the file
must be open for writing.

**NOTES:**

NONE

(truncate)=

### truncate - truncate a file to a specified length

```{index} truncate
```

```{index} truncate a file to a specified length
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int trunctate(
    const char *path,
    size_t      length
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENOTDIR``
   - A component of the path prefix is not a directory.
 * - ``EINVAL``
   - The pathname contains a character with the high-order bit set.
 * - ``ENAMETOOLONG``
   - The length of the specified pathname exceeds ``PATH_MAX`` bytes, or the length
     of a component of the pathname exceeds ``NAME_MAX`` bytes.
 * - ``ENOENT``
   - The named file does not exist.
 * - ``EACCES``
   - The named file is not writable by the user.
 * - ``EACCES``
   - Search permission is denied for a component of the path prefix.
 * - ``ELOOP``
   - Too many symbolic links were encountered in translating the pathname
 * - ``EISDIR``
   - The named file is a directory.
 * - ``EROFS``
   - The named file resides on a read-only file system
 * - ``ETXTBSY``
   - The file is a pure procedure (shared text) file that is being executed
 * - ``EIO``
   - An I/O error occurred updating the inode.
 * - ``EFAULT``
   - ``Path`` points outside the process's allocated address space.
 * - ``EBADF``
   - The ``fd`` is not a valid descriptor.
```

**DESCRIPTION:**

`truncate()` causes the file named by `path` or referenced by\`\`fd\`\` to be
truncated to at most `length` bytes in size. If the file previously was
larger than this size, the extra data is lost. With `ftruncate()`, the file
must be open for writing.

**NOTES:**

NONE

(pathconf)=

### pathconf - Gets configuration values for files

```{index} pathconf
```

```{index} gets configuration values for files
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int pathconf(
    const char *path,
    int         name
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument
 * - ``EACCES``
   - Permission to write the file is denied
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist
 * - ``ENOTDIR``
   - A component of the specified ``path`` was not a directory whan a directory
     was expected.
```

**DESCRIPTION:**

`pathconf()` gets a value for the configuration option `name` for the open
file descriptor `filedes`.

The possible values for `name` are:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``_PC_LINK_MAX``
   - Returns the maximum number of links to the file. If ``filedes`` or``path``
     refer to a directory, then the value applies to the whole directory. The
     corresponding macro is ``_POSIX_LINK_MAX``.
 * - ``_PC_MAX_CANON``
   - Returns the maximum length of a formatted input line, where ``filedes`` or
     ``path`` must refer to a terminal. The corresponding macro is
     ``_POSIX_MAX_CANON``.
 * - ``_PC_MAX_INPUT``
   - Returns the maximum length of an input line, where ``filedes`` or ``path``
     must refer to a terminal. The corresponding macro is``_POSIX_MAX_INPUT``.
 * - ``_PC_NAME_MAX``
   - Returns the maximum length of a filename in the directory ``path`` or
     ``filedes``. The process is allowed to create. The corresponding macro is
     ``_POSIX_NAME_MAX``.
 * - ``_PC_PATH_MAX``
   - returns the maximum length of a relative pathname when ``path``
     or``filedes`` is the current working directory. The corresponding macro is
     ``_POSIX_PATH_MAX``.
 * - ``_PC_PIPE_BUF``
   - returns the size of the pipe buffer, where ``filedes`` must refer to a
     pipe or FIFO and ``path`` must refer to a FIFO. The corresponding macro is
     ``_POSIX_PIPE_BUF``.
 * - ``_PC_CHOWN_RESTRICTED``
   - Returns nonzero if the ``chown(2)`` call may not be used on this
     file. If``filedes`` or ``path`` refer to a directory, then this applies to
     all files in that directory. The corresponding macro is
     ``_POSIX_CHOWN_RESTRICTED``.
```

**NOTES:**

Files with name lengths longer than the value returned for `name` equal
`_PC_NAME_MAX` may exist in the given directory.

(fpathconf)=

### fpathconf - Gets configuration values for files

```{index} fpathconf
```

```{index} gets configuration values for files
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
int fpathconf(
    int filedes,
    int name
);
```

**STATUS CODES:**

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - Invalid argument
 * - ``EACCES``
   - Permission to write the file is denied
 * - ``ENAMETOOLONG``
   - Length of a filename string exceeds ``PATH_MAX`` and ``_POSIX_NO_TRUNC``
     is in effect.
 * - ``ENOENT``
   - A file or directory does not exist
 * - ``ENOTDIR``
   - A component of the specified ``path`` was not a directory whan a directory
     was expected.
```

**DESCRIPTION:**

`pathconf()` gets a value for the configuration option `name` for the open
file descriptor `filedes`.

The possible values for name are:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``_PC_LINK_MAX``
   - Returns the maximum number of links to the file. If ``filedes`` or
     ``path`` refer to a directory, then the value applies to the whole
     directory. The corresponding macro is ``_POSIX_LINK_MAX``.
 * - ``_PC_MAX_CANON``
   - returns the maximum length of a formatted input line, where ``filedes`` or
     ``path`` must refer to a terminal. The corresponding macro is
     ``_POSIX_MAX_CANON``.
 * - ``_PC_MAX_INPUT``
   - Returns the maximum length of an input line, where ``filedes`` or ``path``
     must refer to a terminal. The corresponding macro is ``_POSIX_MAX_INPUT``.
 * - ``_PC_NAME_MAX``
   - Returns the maximum length of a filename in the directory ``path`` or
     ``filedes``. The process is allowed to create. The corresponding macro is
     ``_POSIX_NAME_MAX``.
 * - ``_PC_PATH_MAX``
   - Returns the maximum length of a relative pathname when ``path`` or
     ``filedes`` is the current working directory. The corresponding macro is
     ``_POSIX_PATH_MAX``.
 * - ``_PC_PIPE_BUF``
   - Returns the size of the pipe buffer, where ``filedes`` must refer to a
     pipe or FIFO and ``path`` must refer to a FIFO. The corresponding macro is
     ``_POSIX_PIPE_BUF``.
 * - ``_PC_CHOWN_RESTRICTED``
   - Returns nonzero if the ``chown()`` call may not be used on this file. If
     ``filedes`` or ``path`` refer to a directory, then this applies to all
     files in that directory. The corresponding macro is
     ``_POSIX_CHOWN_RESTRICTED``.
```

**NOTES:**

NONE

(mknod)=

### mknod - create a directory

```{index} mknod
```

```{index} create a directory
```

**CALLING SEQUENCE:**

```c
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
long mknod(
    const char *pathname,
    mode_t      mode,
    dev_t       dev
);
```

**STATUS CODES:**

`mknod` returns zero on success, or -1 if an error occurred (in which case,
errno is set appropriately).

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``ENAMETOOLONG``
   - ``pathname`` was too long.
 * - ``ENOENT``
   - A directory component in ``pathname`` does not exist or is a dangling
     symbolic link.
 * - ``ENOTDIR``
   - A component used in the directory ``pathname`` is not, in fact, a
     directory.
 * - ``ENOMEM``
   - Insufficient kernel memory was available
 * - ``EROFS``
   - ``pathname`` refers to a file on a read-only filesystem.
 * - ``ELOOP``
   - ``pathname`` contains a reference to a circular symbolic link, ie a
     symbolic link whose expansion contains a reference to itself.
 * - ``ENOSPC``
   - The device containing ``pathname`` has no room for the new node.
```

**DESCRIPTION:**

`mknod` attempts to create a filesystem node (file, device special file or
named pipe) named `pathname`, specified by `mode` and `dev`.

`mode` specifies both the permissions to use and the type of node to be created.

It should be a combination (using bitwise OR) of one of the file types listed
below and the permissions for the new node.

The permissions are modified by the process's `umask` in the usual way: the
permissions of the created node are `(mode & ~umask)`.

The file type should be one of `S_IFREG`, `S_IFCHR`, `S_IFBLK` and
`S_IFIFO` to specify a normal file (which will be created empty), character
special file, block special file or FIFO (named pipe), respectively, or zero,
which will create a normal file.

If the file type is `S_IFCHR` or `S_IFBLK` then `dev` specifies the major
and minor numbers of the newly created device special file; otherwise it is
ignored.

The newly created node will be owned by the effective uid of the process. If
the directory containing the node has the set group id bit set, or if the
filesystem is mounted with BSD group semantics, the new node will inherit the
group ownership from its parent directory; otherwise it will be owned by the
effective gid of the process.

**NOTES:**

NONE
