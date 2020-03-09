.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Classic API Configuration
=========================

This section defines the Classic API related system configuration parameters
supported by ``<rtems/confdefs.h>``.

.. index:: CONFIGURE_MAXIMUM_BARRIERS

.. _CONFIGURE_MAXIMUM_BARRIERS:

CONFIGURE_MAXIMUM_BARRIERS
--------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_BARRIERS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_BARRIERS`` is the maximum number of Classic API
    Barriers that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

.. index:: CONFIGURE_MAXIMUM_MESSAGE_QUEUES

.. _CONFIGURE_MAXIMUM_MESSAGE_QUEUES:

CONFIGURE_MAXIMUM_MESSAGE_QUEUES
--------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_MESSAGE_QUEUES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_MESSAGE_QUEUES`` is the maximum number of Classic API
    Message Queues that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.  You have
    to account for the memory used to store the messages of each message queue,
    see :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.

.. index:: CONFIGURE_MAXIMUM_PARTITIONS

.. _CONFIGURE_MAXIMUM_PARTITIONS:

CONFIGURE_MAXIMUM_PARTITIONS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PARTITIONS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_PARTITIONS`` is the maximum number of Classic API
    Partitions that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

.. index:: CONFIGURE_MAXIMUM_PERIODS

.. _CONFIGURE_MAXIMUM_PERIODS:

CONFIGURE_MAXIMUM_PERIODS
-------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PERIODS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_PERIODS`` is the maximum number of Classic API Periods
    that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

.. index:: CONFIGURE_MAXIMUM_PORTS

.. _CONFIGURE_MAXIMUM_PORTS:

CONFIGURE_MAXIMUM_PORTS
-----------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PORTS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_PORTS`` is the maximum number of Classic API Ports that
    can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

.. index:: CONFIGURE_MAXIMUM_REGIONS

.. _CONFIGURE_MAXIMUM_REGIONS:

CONFIGURE_MAXIMUM_REGIONS
-------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_REGIONS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_REGIONS`` is the maximum number of Classic API Regions
    that can be concurrently active.

NOTES:
    None.

.. index:: CONFIGURE_MAXIMUM_SEMAPHORES

.. _CONFIGURE_MAXIMUM_SEMAPHORES:

CONFIGURE_MAXIMUM_SEMAPHORES
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_SEMAPHORES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_SEMAPHORES`` is the maximum number of Classic API
    Semaphores that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

    In SMP configurations, the size of a Semaphore Control Block depends on the
    scheduler count (see :ref:`ConfigurationSchedulerTable`).  The semaphores
    using the :ref:`MrsP` need a ceiling priority per scheduler.

.. index:: CONFIGURE_MAXIMUM_TASKS

.. _CONFIGURE_MAXIMUM_TASKS:

CONFIGURE_MAXIMUM_TASKS
-----------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_TASKS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is ``0``.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_TASKS`` is the maximum number of Classic API Tasks that
    can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

    The calculations for the required memory in the RTEMS Workspace for tasks
    assume that each task has a minimum stack size and has floating point
    support enabled.  The configuration parameter
    ``CONFIGURE_EXTRA_TASK_STACKS`` is used to specify task stack requirements
    *ABOVE* the minimum size required.  See :ref:`Reserve Task/Thread Stack
    Memory Above Minimum` for more information about
    ``CONFIGURE_EXTRA_TASK_STACKS``.

    The maximum number of POSIX threads is specified by
    :ref:`CONFIGURE_MAXIMUM_POSIX_THREADS <CONFIGURE_MAXIMUM_POSIX_THREADS>`.

    A future enhancement to ``<rtems/confdefs.h>`` could be to eliminate the
    assumption that all tasks have floating point enabled. This would require
    the addition of a new configuration parameter to specify the number of
    tasks which enable floating point support.

.. index:: CONFIGURE_MAXIMUM_TIMERS

.. _CONFIGURE_MAXIMUM_TIMERS:

CONFIGURE_MAXIMUM_TIMERS
------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_TIMERS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_TIMERS`` is the maximum number of Classic API Timers
    that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

.. index:: CONFIGURE_MAXIMUM_USER_EXTENSIONS

.. _CONFIGURE_MAXIMUM_USER_EXTENSIONS:

CONFIGURE_MAXIMUM_USER_EXTENSIONS
---------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_USER_EXTENSIONS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_USER_EXTENSIONS`` is the maximum number of Classic API
    User Extensions that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.
