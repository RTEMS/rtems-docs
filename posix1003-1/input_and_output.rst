.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Input and Output Primitives
###########################

Pipes
=====

Create an Inter-Process Channel
-------------------------------

.. code:: c

    pipe(), Function, Dummy Implementation

NOTE: pipe() returns ENOSYS.

File Descriptor Manipulation
============================

Duplicate an Open File Descriptor
---------------------------------

.. code:: c

    dup(), Function, Implemented
    dup2(), Function, Implemented

File Descriptor Deassignment
============================

Close a File
------------

.. code:: c

    close(), Function, Implemented

Input and Output
================

Read from a File
----------------

.. code:: c

    read(), Function, Implemented

Write to a File
---------------

.. code:: c

    write(), Function, Implemented

Control Operations on Files
===========================

Data Definitions for File Control Operations
--------------------------------------------

File Control
------------

.. code:: c

    struct flock, Type, Implemented
    fcntl(), Function, Implemented
    F_DUPFD, Constant, Implemented
    F_GETFD, Constant, Implemented
    F_GETLK, Constant, Implemented
    F_SETFD, Constant, Implemented
    F_GETFL, Constant, Implemented
    F_SETFL, Constant, Implemented
    F_SETLK, Constant, Implemented
    F_SETLKW, Constant, Implemented
    FD_CLOEXEC, Constant, Implemented
    F_RDLCK, Constant, Implemented
    F_UNLCK, Constant, Implemented
    F_WRLCK, Constant, Implemented
    O_ACCMODE, Constant, Implemented

NOTE: A number of constants are used by both ``open`` and ``fcntl``.``O_CREAT``, ``O_EXCL``, ``O_NOCTTY``, ``O_TRUNC``,``O_APPEND``, ``O_DSYNC``, ``O_NONBLOCK``, ``O_RSYNC``,``O_SYNC``, ``O_RDONLY``, ``O_RDWR``, and ``O_WRONLY``
are also included in another section.  See `Open a File`_.

Reposition Read/Write File Offset
---------------------------------

.. code:: c

    lseek(), Function, Implemented
    SEEK_SET, Constant, Implemented
    SEEK_CUR, Constant, Implemented
    SEEK_END, Constant, Implemented

File Synchronization
====================

Synchronize the State of a File
-------------------------------

.. code:: c

    fsync(), Function, Implemented

Synchronize the Data of a File
------------------------------

.. code:: c

    fdatasync(), Function, Implemented

Asynchronous Input and Output
=============================

Data Definitions for Asynchronous Input and Output
--------------------------------------------------

Asynchronous I/O Control Block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    struct aiocb, Type, Untested Implementation

Asynchronous I/O Manifest Constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    AIO_CANCELED, Constant, Implemented
    AIO_NOTCANCELED, Constant, Implemented
    AIO_ALLDONE, Constant, Implemented
    LIO_WAIT, Constant, Implemented
    LIO_NOWAIT, Constant, Implemented
    LIO_READ, Constant, Implemented
    LIO_WRITE, Constant, Implemented
    LIO_NOP, Constant, Implemented

Asynchronous Read
-----------------

.. code:: c

    aio_read(), Function, Dummy Implementation

Asynchronous Write
------------------

.. code:: c

    aio_write(), Function, Dummy Implementation

List Directed I/O
-----------------

.. code:: c

    lio_listio(), Function, Dummy Implementation

Retrieve Error Status of Asynchronous I/O Operation
---------------------------------------------------

.. code:: c

    aio_error(), Function, Dummy Implementation

Retrieve Return Status of Asynchronous I/O Operation
----------------------------------------------------

.. code:: c

    aio_return(), Function, Dummy Implementation

Cancel Asynchronous I/O Request
-------------------------------

.. code:: c

    aio_cancel(), Function, Dummy Implementation

Wait for Asynchronous I/O Request
---------------------------------

.. code:: c

    aio_suspend(), Function, Dummy Implementation

Asynchronous File Synchronization
---------------------------------

.. code:: c

    aio_fsync(), Function, Dummy Implementation

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

