Terminology and General Requirements
####################################

Conventions
===========

Definitions
===========

General Concepts
================

Error Numbers
=============

.. code:: c

    E2BIG, Constant, Implemented
    EACCES, Constant, Implemented
    EAGAIN, Constant, Implemented
    EBADF, Constant, Implemented
    EBADMSG, Constant, Implemented
    EBUSY, Constant, Implemented
    ECANCELED, Constant, Unimplemented
    ECHILD, Constant, Implemented
    EDEADLK, Constant, Implemented
    EDOM, Constant, Implemented
    EEXIST, Constant, Implemented
    EFAULT, Constant, Implemented
    EFBIG, Constant, Implemented
    EINPROGRESS, Constant, Implemented
    EINTR, Constant, Implemented
    EINVAL, Constant, Implemented
    EIO, Constant, Implemented
    EISDIR, Constant, Implemented
    EMFILE, Constant, Implemented
    EMLINK, Constant, Implemented
    EMSGSIZE, Constant, Implemented
    ENAMETOOLONG, Constant, Implemented
    ENFILE, Constant, Implemented
    ENODEV, Constant, Implemented
    ENOENT, Constant, Implemented
    ENOEXEC, Constant, Implemented
    ENOLCK, Constant, Implemented
    ENOMEM, Constant, Implemented
    ENOSPC, Constant, Implemented
    ENOSYS, Constant, Implemented
    ENOTDIR, Constant, Implemented
    ENOTEMPTY, Constant, Implemented
    ENOTSUP, Constant, Implemented
    ENOTTY, Constant, Implemented
    ENXIO, Constant, Implemented
    EPERM, Constant, Implemented
    EPIPE, Constant, Implemented
    ERANGE, Constant, Implemented
    EROFS, Constant, Implemented
    ESPIPE, Constant, Implemented
    ESRCH, Constant, Implemented
    ETIMEDOUT, Constant, Implemented
    EXDEV, Constant, Implemented

Primitive System Types
======================

.. code:: c

    dev_t, Type, Implemented
    gid_t, Type, Implemented
    ino_t, Type, Implemented
    mode_t, Type, Implemented
    nlink_t, Type, Implemented
    off_t, Type, Implemented
    pid_t, Type, Implemented
    pthread_t, Type, Implemented
    pthread_attr_t, Type, Implemented
    pthread_mutex_t, Type, Implemented
    pthread_mutex_attr_t, Type, Implemented
    pthread_cond_t, Type, Implemented
    pthread_cond_attr_t, Type, Implemented
    pthread_key_t, Type, Implemented
    pthread_once_t, Type, Implemented
    size_t, Type, Implemented
    ssize_t, Type, Implemented
    time_t, Type, Implemented
    uid_t, Type, Implemented

NOTE: time_t is not listed in this section but is used by many functions.

Environment Description
=======================

C Language Definitions
======================

Symbols From the C Standard
---------------------------

.. code:: c

    NULL, Constant, Implemented

POSIX.1 Symbols
---------------

.. code:: c

    _POSIX_C_SOURCE, Feature Flag,

Numerical Limits
================

C Language Limits
=================

.. code:: c

    CHAR_BIT, Constant, Implemented
    CHAR_MAX, Constant, Implemented
    CHAR_MIN, Constant, Implemented
    INT_MAX, Constant, Implemented
    INT_MIN, Constant, Implemented
    LONG_MAX, Constant, Implemented
    LONG_MIN, Constant, Implemented
    MB_LEN_MAX, Constant, Implemented
    SCHAR_MAX, Constant, Implemented
    SCHAR_MIN, Constant, Implemented
    SHRT_MAX, Constant, Implemented
    SHRT_MIN, Constant, Implemented
    UCHAR_MAX, Constant, Implemented
    UINT_MAX, Constant, Implemented
    ULONG_MAX, Constant, Implemented
    USHRT_MAX, Constant, Implemented

NOTE: These are implemented in GCC’s limits.h file.

Minimum Values
--------------

.. code:: c

    _POSIX_AIO_LISTIO_MAX, Constant, Implemented
    _POSIX_AIO_MAX, Constant, Implemented
    _POSIX_ARG_MAX, Constant, Implemented
    _POSIX_CHILD_MAX, Constant, Implemented
    _POSIX_DELAYTIMER_MAX, Constant, Implemented
    _POSIX_LINK_MAX, Constant, Implemented
    _POSIX_LOGIN_NAME_MAX, Constant, Implemented
    _POSIX_MAX_CANON, Constant, Implemented
    _POSIX_MAX_INPUT, Constant, Implemented
    _POSIX_MQ_OPEN_MAX, Constant, Implemented
    _POSIX_MQ_PRIO_MAX, Constant, Implemented
    _POSIX_NAME_MAX, Constant, Implemented
    _POSIX_NGROUPS_MAX, Constant, Implemented
    _POSIX_OPEN_MAX, Constant, Implemented
    _POSIX_PATH_MAX, Constant, Implemented
    _POSIX_PIPE_BUF, Constant, Implemented
    _POSIX_RTSIG_MAX, Constant, Implemented
    _POSIX_SEM_NSEMS_MAX, Constant, Implemented
    _POSIX_SEM_VALUE_MAX, Constant, Implemented
    _POSIX_SIGQUEUE_MAX, Constant, Implemented
    _POSIX_SSIZE_MAX, Constant, Implemented
    _POSIX_STREAM_MAX, Constant, Implemented
    _POSIX_THREAD_DESTRUCTOR_ITERATIONS, Constant, Implemented
    _POSIX_THREAD_KEYS_MAX, Constant, Implemented
    _POSIX_THREAD_THREADS_MAX, Constant, Implemented
    _POSIX_TTY_NAME_MAX, Constant, Implemented
    _POSIX_TIME_MAX, Constant, Unimplemented
    _POSIX_TZNAME_MAX, Constant, Implemented

Run-Time Increasable Values
---------------------------

.. code:: c

    _POSIX_NGROUPS_MAX, Constant, Implemented

Run-Time Invariant Values (Possible Indeterminate)
--------------------------------------------------

.. code:: c

    AIO_LISTIO_MAX, Constant, Implemented
    AIO_MAX, Constant, Implemented
    AIO_PRIO_DELTA_MAX, Constant, Implemented
    ARG_MAX, Constant, Implemented
    CHILD_MAX, Constant, Implemented
    DELAYTIMER_MAX, Constant, Implemented
    LOGIN_NAME_MAX, Constant, Implemented
    MQ_OPEN_MAX, Constant, Implemented
    OPEN_MAX, Constant, Implemented
    PAGESIZE, Constant, Implemented
    PTHREAD_DESTRUCTOR_ITERATIONS, Constant, Implemented
    PTHREAD_KEYS_MAX, Constant, Implemented
    PTHREAD_STACK_MIN, Constant, Implemented
    PTHJREAD_THREADS_MAX, Constant, Implemented
    RTSIG_MAX, Constant, Implemented
    SEM_NSEMS_MAX, Constant, Implemented
    SEM_VALUE_MAX, Constant, Implemented
    SIGQUEUE_MAX, Constant, Implemented
    STREAM_MAX, Constant, Implemented
    TIMER_MAX, Constant, Implemented
    TTY_NAME_MAX, Constant, Implemented
    TZNAME_MAX, Constant, Implemented

Pathname Variable Values
------------------------

.. code:: c

    LINK_MAX, Constant, Implemented
    MAX_CANON, Constant, Implemented
    MAX_INPUT, Constant, Implemented
    NAME_MAX, Constant, Implemented
    PATH_MAX, Constant, Implemented
    PIPE_BUF, Constant, Implemented

Invariant Values
----------------

.. code:: c

    SSIZE_MAX, Constant, Implemented

Maximum Values
--------------

.. code:: c

    _POSIX_CLOCKRES_MIN, Constant, Implemented

Symbolic Constants
==================

Symbolic Constants for the access Function
------------------------------------------

.. code:: c

    R_OK, Constant, Implemented
    W_OK, Constant, Implemented
    X_OK, Constant, Implemented
    F_OK, Constant, Implemented

Symbolic Constants for the lseek Function
-----------------------------------------

.. code:: c

    SEEK_SET, Constant, Implemented
    SEEK_CUR, Constant, Implemented
    SEEK_END, Constant, Implemented

Compile-Time Symbolic Constants for Portability Specifications
--------------------------------------------------------------

.. code:: c

    _POSIX_ASYNCHRONOUS_IO, Feature Flag,
    _POSIX_FSYNC, Feature Flag,
    _POSIX_JOB_CONTROL, Feature Flag,
    _POSIX_MAPPED_FILES, Feature Flag,
    _POSIX_MEMLOCK, Feature Flag,
    _POSIX_MEMLOCK_RANGE, Feature Flag,
    _POSIX_MEMORY_PROTECTION, Feature Flag,
    _POSIX_MESSAGE_PASSING, Feature Flag,
    _POSIX_PRIORITIZED_IO, Feature Flag,
    _POSIX_PRIORITY_SCHEDULING, Feature Flag,
    _POSIX_REALTIME_SIGNALS, Feature Flag,
    _POSIX_SAVED_IDS, Feature Flag,
    _POSIX_SEMAPHORES, Feature Flag,
    _POSIX_SHARED_MEMORY_OBJECTS, Feature Flag,
    _POSIX_SYNCHRONIZED_IO, Feature Flag,
    _POSIX_THREADS, Feature Flag,
    _POSIX_THREAD_ATTR_STACKADDR, Feature Flag,
    _POSIX_THREAD_ATTR_STACKSIZE, Feature Flag,
    _POSIX_THREAD_PRIORITY_SCHEDULING, Feature Flag,
    _POSIX_THREAD_PRIO_INHERIT, Feature Flag,
    _POSIX_THREAD_PRIO_CEILING, Feature Flag,
    _POSIX_THREAD_PROCESS_SHARED, Feature Flag,
    _POSIX_THREAD_SAFE_FUNCTIONS, Feature Flag,
    _POSIX_TIMERS, Feature Flag,
    _POSIX_VERSION, Feature Flag,

Execution-Time Symbolic Constants for Portability Specifications
----------------------------------------------------------------

.. code:: c

    _POSIX_ASYNC_IO, Feature Flag,
    _POSIX_CHOWN_RESTRICTED, Feature Flag,
    _POSIX_NO_TRUNC, Feature Flag,
    _POSIX_PRIO_IO, Feature Flag,
    _POSIX_SYNC_IO, Feature Flag,
    _POSIX_VDISABLE, Feature Flag,

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

