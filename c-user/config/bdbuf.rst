.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. Generated from spec:/acfg/if/group-bdbuf

Block Device Cache Configuration
================================

This section describes configuration options related to the Block Device Cache
(bdbuf).

.. Generated from spec:/acfg/if/appl-needs-libblock

.. index:: CONFIGURE_APPLICATION_NEEDS_LIBBLOCK

.. _CONFIGURE_APPLICATION_NEEDS_LIBBLOCK:

CONFIGURE_APPLICATION_NEEDS_LIBBLOCK
------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_LIBBLOCK``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the Block Device Cache is
    initialized during system initialization.

NOTES:
    Each option of the Block Device Cache (bdbuf) configuration can be explicitly
    set by the user with the configuration options below.  The Block Device Cache
    is used for example by the RFS and DOSFS filesystems.

.. Generated from spec:/acfg/if/bdbuf-buffer-max-size

.. index:: CONFIGURE_BDBUF_BUFFER_MAX_SIZE

.. _CONFIGURE_BDBUF_BUFFER_MAX_SIZE:

CONFIGURE_BDBUF_BUFFER_MAX_SIZE
-------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_BUFFER_MAX_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 4096.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be an integral multiple of :ref:`CONFIGURE_BDBUF_BUFFER_MIN_SIZE`.

DESCRIPTION:
    The value of this configuration option defines the maximum size of a buffer
    in bytes.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-buffer-min-size

.. index:: CONFIGURE_BDBUF_BUFFER_MIN_SIZE

.. _CONFIGURE_BDBUF_BUFFER_MIN_SIZE:

CONFIGURE_BDBUF_BUFFER_MIN_SIZE
-------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_BUFFER_MIN_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 512.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the minimum size of a buffer
    in bytes.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-cache-memory-size

.. index:: CONFIGURE_BDBUF_CACHE_MEMORY_SIZE

.. _CONFIGURE_BDBUF_CACHE_MEMORY_SIZE:

CONFIGURE_BDBUF_CACHE_MEMORY_SIZE
---------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_CACHE_MEMORY_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 32768.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

DESCRIPTION:
    The value of this configuration option defines the size of the cache memory
    in bytes.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-max-read-ahead-blocks

.. index:: CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS

.. _CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS:

CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS
-------------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the maximum blocks per
    read-ahead request.

NOTES:
    A value of 0 disables the read-ahead task (default).  The read-ahead task
    will issue speculative read transfers if a sequential access pattern is
    detected.  This can improve the performance on some systems.

.. Generated from spec:/acfg/if/bdbuf-max-write-blocks

.. index:: CONFIGURE_BDBUF_MAX_WRITE_BLOCKS

.. _CONFIGURE_BDBUF_MAX_WRITE_BLOCKS:

CONFIGURE_BDBUF_MAX_WRITE_BLOCKS
--------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_MAX_WRITE_BLOCKS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 16.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the maximum blocks per write
    request.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-read-ahead-task-priority

.. index:: CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY

.. _CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY:

CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY
----------------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 15.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid Classic API task
    priority.  The set of valid task priorities is scheduler-specific.

DESCRIPTION:
    The value of this configuration option defines the read-ahead task priority.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-task-stack-size

.. index:: CONFIGURE_BDBUF_TASK_STACK_SIZE

.. _CONFIGURE_BDBUF_TASK_STACK_SIZE:

CONFIGURE_BDBUF_TASK_STACK_SIZE
-------------------------------

CONSTANT:
    ``CONFIGURE_BDBUF_TASK_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is :c:macro:`RTEMS_MINIMUM_STACK_SIZE`.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It shall be small enough so that the task
      stack space calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the task stack size of the
    Block Device Cache tasks in bytes.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-swapout-block-hold

.. index:: CONFIGURE_SWAPOUT_BLOCK_HOLD

.. _CONFIGURE_SWAPOUT_BLOCK_HOLD:

CONFIGURE_SWAPOUT_BLOCK_HOLD
----------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_BLOCK_HOLD``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 1000.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the swapout task maximum block
    hold time in milliseconds.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-swapout-swap-period

.. index:: CONFIGURE_SWAPOUT_SWAP_PERIOD

.. _CONFIGURE_SWAPOUT_SWAP_PERIOD:

CONFIGURE_SWAPOUT_SWAP_PERIOD
-----------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_SWAP_PERIOD``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 250.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the swapout task swap period
    in milliseconds.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-swapout-task-priority

.. index:: CONFIGURE_SWAPOUT_TASK_PRIORITY

.. _CONFIGURE_SWAPOUT_TASK_PRIORITY:

CONFIGURE_SWAPOUT_TASK_PRIORITY
-------------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_TASK_PRIORITY``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 15.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid Classic API task
    priority.  The set of valid task priorities is scheduler-specific.

DESCRIPTION:
    The value of this configuration option defines the swapout task priority.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-swapout-worker-tasks

.. index:: CONFIGURE_SWAPOUT_WORKER_TASKS

.. _CONFIGURE_SWAPOUT_WORKER_TASKS:

CONFIGURE_SWAPOUT_WORKER_TASKS
------------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_WORKER_TASKS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the swapout worker task count.

NOTES:
    None.

.. Generated from spec:/acfg/if/bdbuf-swapout-worker-taskp-riority

.. index:: CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY

.. _CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY:

CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY
--------------------------------------

CONSTANT:
    ``CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 15.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid Classic API task
    priority.  The set of valid task priorities is scheduler-specific.

DESCRIPTION:
    The value of this configuration option defines the swapout worker task
    priority.

NOTES:
    None.
