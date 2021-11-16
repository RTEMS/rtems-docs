.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_LIBBLOCK

.. _CONFIGURE_APPLICATION_NEEDS_LIBBLOCK:

CONFIGURE_APPLICATION_NEEDS_LIBBLOCK
------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_LIBBLOCK``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Block Device Cache is
initialized during system initialization.

.. rubric:: NOTES:

Each option of the Block Device Cache (bdbuf) configuration can be explicitly
set by the user with the configuration options below.  The Block Device Cache
is used for example by the RFS and DOSFS filesystems.

.. Generated from spec:/acfg/if/bdbuf-buffer-max-size

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_BUFFER_MAX_SIZE

.. _CONFIGURE_BDBUF_BUFFER_MAX_SIZE:

CONFIGURE_BDBUF_BUFFER_MAX_SIZE
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_BUFFER_MAX_SIZE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 4096.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum size of a buffer
in bytes.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be an integral multiple of
  :ref:`CONFIGURE_BDBUF_BUFFER_MIN_SIZE`.

.. Generated from spec:/acfg/if/bdbuf-buffer-min-size

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_BUFFER_MIN_SIZE

.. _CONFIGURE_BDBUF_BUFFER_MIN_SIZE:

CONFIGURE_BDBUF_BUFFER_MIN_SIZE
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_BUFFER_MIN_SIZE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 512.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the minimum size of a buffer
in bytes.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-cache-memory-size

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_CACHE_MEMORY_SIZE

.. _CONFIGURE_BDBUF_CACHE_MEMORY_SIZE:

CONFIGURE_BDBUF_CACHE_MEMORY_SIZE
---------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_CACHE_MEMORY_SIZE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 32768.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the size of the cache memory
in bytes.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

.. Generated from spec:/acfg/if/bdbuf-max-read-ahead-blocks

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS

.. _CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS:

CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS
-------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_MAX_READ_AHEAD_BLOCKS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum blocks per
read-ahead request.

.. rubric:: NOTES:

A value of 0 disables the read-ahead task (default).  The read-ahead task
will issue speculative read transfers if a sequential access pattern is
detected.  This can improve the performance on some systems.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-max-write-blocks

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_MAX_WRITE_BLOCKS

.. _CONFIGURE_BDBUF_MAX_WRITE_BLOCKS:

CONFIGURE_BDBUF_MAX_WRITE_BLOCKS
--------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_MAX_WRITE_BLOCKS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 16.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum blocks per write
request.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-read-ahead-task-priority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY

.. _CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY:

CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY
----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_READ_AHEAD_TASK_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 15.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the read-ahead task priority.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid Classic API task
priority.  The set of valid task priorities depends on the scheduler
configuration.

.. Generated from spec:/acfg/if/bdbuf-task-stack-size

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_BDBUF_TASK_STACK_SIZE

.. _CONFIGURE_BDBUF_TASK_STACK_SIZE:

CONFIGURE_BDBUF_TASK_STACK_SIZE
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_BDBUF_TASK_STACK_SIZE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is :c:macro:`RTEMS_MINIMUM_STACK_SIZE`.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the task stack size of the
Block Device Cache tasks in bytes.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to
  :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option shall be small enough so that the task
  stack space calculation carried out by ``<rtems/confdefs.h>`` does not
  overflow an integer of type `uintptr_t
  <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-swapout-block-hold

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SWAPOUT_BLOCK_HOLD

.. _CONFIGURE_SWAPOUT_BLOCK_HOLD:

CONFIGURE_SWAPOUT_BLOCK_HOLD
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SWAPOUT_BLOCK_HOLD``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 1000.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the swapout task maximum block
hold time in milliseconds.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-swapout-swap-period

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SWAPOUT_SWAP_PERIOD

.. _CONFIGURE_SWAPOUT_SWAP_PERIOD:

CONFIGURE_SWAPOUT_SWAP_PERIOD
-----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SWAPOUT_SWAP_PERIOD``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 250.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the swapout task swap period
in milliseconds.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-swapout-task-priority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SWAPOUT_TASK_PRIORITY

.. _CONFIGURE_SWAPOUT_TASK_PRIORITY:

CONFIGURE_SWAPOUT_TASK_PRIORITY
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SWAPOUT_TASK_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 15.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the swapout task priority.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid Classic API task
priority.  The set of valid task priorities depends on the scheduler
configuration.

.. Generated from spec:/acfg/if/bdbuf-swapout-worker-tasks

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SWAPOUT_WORKER_TASKS

.. _CONFIGURE_SWAPOUT_WORKER_TASKS:

CONFIGURE_SWAPOUT_WORKER_TASKS
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SWAPOUT_WORKER_TASKS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the swapout worker task count.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/bdbuf-swapout-worker-taskp-riority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY

.. _CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY:

CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY
--------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_SWAPOUT_WORKER_TASK_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 15.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the swapout worker task
priority.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid Classic API task
priority.  The set of valid task priorities depends on the scheduler
configuration.
