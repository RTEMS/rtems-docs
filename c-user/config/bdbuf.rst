.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Block Device Cache Configuration
================================

This section describes configuration options related to the Block Device Cache
(bdbuf).

.. index:: CONFIGURE_APPLICATION_NEEDS_LIBBLOCK

.. _CONFIGURE_APPLICATION_NEEDS_LIBBLOCK:

CONFIGURE_APPLICATION_NEEDS_LIBBLOCK
------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_LIBBLOCK``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    Provides a Block Device Cache configuration.

NOTES:
    Each option of the Block Device Cache configuration can be explicitly set
    by the user with the configuration options below.  The Block Device Cache
    is used for example by the RFS and DOSFS file systems.

.. index:: CONFIGURE_BDBUF_BUFFER_MAX_SIZE

.. _CONFIGURE_BDBUF_BUFFER_MAX_SIZE:

CONFIGURE_BDBUF_BUFFER_MAX_SIZE
-------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_BUFFER_MAX_SIZE``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    It must be positive and an integral multiple of the buffer minimum size.

DEFAULT VALUE:
    The default value is 4096 bytes.

DESCRIPTION:
    Defines the maximum size of a buffer in bytes.

NOTES:
    None.

.. index:: CONFIGURE_BDBUF_BUFFER_MIN_SIZE

.. _CONFIGURE_BDBUF_BUFFER_MIN_SIZE:

CONFIGURE_BDBUF_BUFFER_MIN_SIZE
-------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_BUFFER_MIN_SIZE``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 512 bytes.

DESCRIPTION:
    Defines the minimum size of a buffer in bytes.

NOTES:
    None.

.. index:: CONFIGURE_BDBUF_CACHE_MEMORY_SIZE

.. _CONFIGURE_BDBUF_CACHE_MEMORY_SIZE:

CONFIGURE_BDBUF_CACHE_MEMORY_SIZE
---------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_CACHE_MEMORY_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 32768 bytes.

DESCRIPTION:
    Size of the cache memory in bytes.

NOTES:
    None.

.. index:: CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS

.. _CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS:

CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS
-------------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    Defines the maximum blocks per read-ahead request.

NOTES:
    A value of 0 disables the read-ahead task (default).  The read-ahead task
    will issue speculative read transfers if a sequential access pattern is
    detected.  This can improve the performance on some systems.

.. index:: CONFIGURE_BDBUF_MAX_WRITE_BLOCKS

.. _CONFIGURE_BDBUF_MAX_WRITE_BLOCKS:

CONFIGURE_BDBUF_MAX_WRITE_BLOCKS
--------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_MAX_WRITE_BLOCKS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 16.

DESCRIPTION:
    Defines the maximum blocks per write request.

NOTES:
    None.

.. index:: CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY

.. _CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY:

CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY
----------------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY``

DATA TYPE:
    Task priority (``rtems_task_priority``).

RANGE:
    Valid task priority.

DEFAULT VALUE:
    The default value is 15.

DESCRIPTION:
    Defines the read-ahead task priority.

NOTES:
    None.

.. index:: CONFIGURE_BDBUF_TASK_STACK_SIZE

.. _CONFIGURE_BDBUF_TASK_STACK_SIZE:

CONFIGURE_BDBUF_TASK_STACK_SIZE
-------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_TASK_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is RTEMS_MINIMUM_STACK_SIZE.

DESCRIPTION:
    Defines the task stack size of the Block Device Cache tasks in bytes.

NOTES:
    None.

.. index:: CONFIGURE_SWAPOUT_BLOCK_HOLD

.. _CONFIGURE_SWAPOUT_BLOCK_HOLD:

CONFIGURE_SWAPOUT_BLOCK_HOLD
----------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_BLOCK_HOLD``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 1000 milliseconds.

DESCRIPTION:
    Defines the swapout task maximum block hold time in milliseconds.

NOTES:
    None.

.. index:: CONFIGURE_SWAPOUT_SWAP_PERIOD

.. _CONFIGURE_SWAPOUT_SWAP_PERIOD:

CONFIGURE_SWAPOUT_SWAP_PERIOD
-----------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_SWAP_PERIOD``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 250 milliseconds.

DESCRIPTION:
    Defines the swapout task swap period in milliseconds.

NOTES:
    None.

.. index:: CONFIGURE_SWAPOUT_TASK_PRIORITY

.. _CONFIGURE_SWAPOUT_TASK_PRIORITY:

CONFIGURE_SWAPOUT_TASK_PRIORITY
-------------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_TASK_PRIORITY``

DATA TYPE:
    Task priority (``rtems_task_priority``).

RANGE:
    Valid task priority.

DEFAULT VALUE:
    The default value is 15.

DESCRIPTION:
    Defines the swapout task priority.

NOTES:
    None.

.. index:: CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY

.. _CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY:

CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY
--------------------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY``

DATA TYPE:
    Task priority (``rtems_task_priority``).

RANGE:
    Valid task priority.

DEFAULT VALUE:
    The default value is 15.

DESCRIPTION:
    Defines the swapout worker task priority.

NOTES:
    None.

.. index:: CONFIGURE_SWAPOUT_WORKER_TASKS

.. _CONFIGURE_SWAPOUT_WORKER_TASKS:

CONFIGURE_SWAPOUT_WORKER_TASKS
------------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_WORKER_TASKS``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    Defines the swapout worker task count.

NOTES:
    None.
