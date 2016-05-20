.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Files and Directories
#####################

Directories
===========

Format of Directory Entries
---------------------------

Directory Operations
--------------------

.. code:: c

    struct dirent, Type, Implemented
    opendir(), Function, Implemented
    readdir(), Function, Implemented
    readdir_r(), Function, Implemented
    rewinddir(), Function, Implemented
    closedir(), Function, Implemented

Working Directory
=================

Change Current Working Directory
--------------------------------

.. code:: c

    chdir(), Function, Implemented

Get Working Directory Pathname
------------------------------

.. code:: c

    getcwd(), Function, Implemented

General File Creation
=====================

Open a File
-----------

.. code:: c

    open(), Function, Implemented
    O_RDONLY, Constant, Implemented
    O_WRONLY, Constant, Implemented
    O_RDWR, Constant, Implemented
    O_APPEND, Constant, Implemented
    O_CREAT, Constant, Implemented
    O_DSYNC, Constant, Unimplemented
    O_EXCL, Constant, Implemented
    O_NOCTTY, Constant, Implemented
    O_NONBLOCK, Constant, Implemented
    O_RSYNC, Constant, Unimplemented
    O_SYNC, Constant, Implemented
    O_TRUNC, Constant, Implemented

NOTE: In the newlib fcntl.h, O_SYNC is defined only if _POSIX_SOURCE is
not defined.  This seems wrong.

Create a New File or Rewrite an Existing One
--------------------------------------------

.. code:: c

    creat(), Function, Implemented

Set File Creation Mask
----------------------

.. code:: c

    umask(), Function, Implemented

Link to a File
--------------

.. code:: c

    link(), Function, Implemented

Special File Creation
=====================

Make a Directory
----------------

.. code:: c

    mkdir(), Function, Implemented

Make a FIFO Special File
------------------------

.. code:: c

    mkfifo(), Function, Untested Implementation

NOTE: mkfifo() is implemented but no filesystem supports FIFOs.

File Removal
============

Remove Directory Entries
------------------------

.. code:: c

    unlink(), Function, Implemented

Remove a Directory
------------------

.. code:: c

    rmdir(), Function, Implemented

Rename a File
-------------

.. code:: c

    rename(), Function, Partial Implementation

File Characteristics
====================

File Characteristics Header and Data Structure
----------------------------------------------

.. code:: c

    struct stat, Type, Implemented

<sys/stat.h> File Types
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    S_ISBLK(), Function, Implemented
    S_ISCHR(), Function, Implemented
    S_ISDIR(), Function, Implemented
    S_ISFIFO(), Function, Implemented
    S_ISREG(), Function, Implemented
    S_TYPEISMQ(), Function, Unimplemented
    S_TYPEISSEM(), Function, Unimplemented
    S_TYPEISSHM(), Function, Unimplemented

<sys/stat.h> File Modes
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    S_IRWXU, Constant, Implemented
    S_IRUSR, Constant, Implemented
    S_IWUSR, Constant, Implemented
    S_IXUSR, Constant, Implemented
    S_IRWXG, Constant, Implemented
    S_IRGRP, Constant, Implemented
    S_IWGRP, Constant, Implemented
    S_IXGRP, Constant, Implemented
    S_IRWXO, Constant, Implemented
    S_IROTH, Constant, Implemented
    S_IWOTH, Constant, Implemented
    S_IXOTH, Constant, Implemented
    S_ISUID, Constant, Implemented
    S_ISGID, Constant, Implemented

<sys/stat.h> Time Entries
~~~~~~~~~~~~~~~~~~~~~~~~~

Get File Status
---------------

.. code:: c

    stat(), Function, Implemented
    fstat(), Function, Implemented

Check File Accessibility
------------------------

.. code:: c

    access(), Function, Implemented

Change File Modes
-----------------

.. code:: c

    chmod(), Function, Implemented
    fchmod(), Function, Implemented

Change Owner and Group of a File
--------------------------------

.. code:: c

    chown(), Function, Implemented

Set File Access and Modification Times
--------------------------------------

.. code:: c

    struct utimbuf, Type, Implemented
    utime(), Function, Implemented

Truncate a File to a Specified Length
-------------------------------------

.. code:: c

    ftruncate(), Function, Implemented

Configurable Pathname Variable
==============================

Get Configurable Pathname Variables
-----------------------------------

.. code:: c

    pathconf(), Function, Implemented
    fpathconf(), Function, Implemented
    _PC_LINK_MAX, Constant, Implemented
    _PC_MAX_CANON, Constant, Implemented
    _PC_MAX_INPUT, Constant, Implemented
    _PC_MAX_INPUT, Constant, Implemented
    _PC_NAME_MAX, Constant, Implemented
    _PC_PATH_MAX, Constant, Implemented
    _PC_PIPE_BUF, Constant, Implemented
    _PC_ASYNC_IO, Constant, Implemented
    _PC_CHOWN_RESTRICTED, Constant, Implemented
    _PC_NO_TRUNC, Constant, Implemented
    _PC_PRIO_IO, Constant, Implemented
    _PC_SYNC_IO, Constant, Implemented
    _PC_VDISABLE, Constant, Implemented

NOTE: The newlib unistd.h and sys/unistd.h are installed and the
include search patch is used to get the right one.  There are
conflicts between the newlib unistd.h and RTEMS' version.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

