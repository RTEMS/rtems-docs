.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

POSIX API Configuration
=======================

This section describes configuration options related to the POSIX API.  Most
POSIX API objects are available by default since RTEMS 5.1.  The queued signals
and timers are only available if RTEMS was built with the ``--enable-posix``
build configuration option.

.. index:: CONFIGURE_MAXIMUM_POSIX_KEYS

.. _CONFIGURE_MAXIMUM_POSIX_KEYS:

CONFIGURE_MAXIMUM_POSIX_KEYS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_KEYS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_KEYS`` is the maximum number of POSIX API Keys
    that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

.. index:: CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS

.. _CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS:

CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS
---------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is
    :ref:`CONFIGURE_MAXIMUM_POSIX_KEYS <CONFIGURE_MAXIMUM_POSIX_KEYS>` *
    :ref:`CONFIGURE_MAXIMUM_TASKS <CONFIGURE_MAXIMUM_TASKS>` +
    :ref:`CONFIGURE_MAXIMUM_POSIX_THREADS <CONFIGURE_MAXIMUM_POSIX_THREADS>`.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS`` is the maximum number of key
    value pairs used by POSIX API Keys that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

    A key value pair is created by :c:func:`pthread_setspecific` if the value
    is not :c:macro:`NULL`, otherwise it is deleted.

.. index:: CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES

.. _CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES:

CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES
--------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES`` is the maximum number of POSIX
    API Message Queues that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.  You have
    to account for the memory used to store the messages of each message queue,
    see :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.

.. index:: CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS

.. _CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS:

CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS
--------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS`` is the maximum number of POSIX
    API Queued Signals that can be concurrently active.

NOTES:
    Unlimited objects are not available for queued signals.

    Queued signals are only available if RTEMS was built with the
    ``--enable-posix`` build configuration option.

.. index:: CONFIGURE_MAXIMUM_POSIX_SEMAPHORES

.. _CONFIGURE_MAXIMUM_POSIX_SEMAPHORES:

CONFIGURE_MAXIMUM_POSIX_SEMAPHORES
----------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_SEMAPHORES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_SEMAPHORES`` is the maximum number of POSIX API
    Named Semaphores that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

    Named semaphores are created with ``sem_open()``.  Semaphores initialized
    with ``sem_init()`` are not affected by this configuration option since the
    storage space for these semaphores is user-provided.

.. index:: CONFIGURE_MAXIMUM_POSIX_THREADS

.. _CONFIGURE_MAXIMUM_POSIX_THREADS:

CONFIGURE_MAXIMUM_POSIX_THREADS
-------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_THREADS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_THREADS`` is the maximum number of POSIX API
    Threads that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

    This calculations for the required memory in the RTEMS Workspace for
    threads assume that each thread has a minimum stack size and has floating
    point support enabled.  The configuration parameter
    ``CONFIGURE_EXTRA_TASK_STACKS`` is used to specify thread stack
    requirements *ABOVE* the minimum size required.  See :ref:`Reserve
    Task/Thread Stack Memory Above Minimum` for more information about
    ``CONFIGURE_EXTRA_TASK_STACKS``.

    The maximum number of Classic API Tasks is specified by
    :ref:`CONFIGURE_MAXIMUM_TASKS <CONFIGURE_MAXIMUM_TASKS>`.

    All POSIX threads have floating point enabled.

.. index:: CONFIGURE_MAXIMUM_POSIX_TIMERS

.. _CONFIGURE_MAXIMUM_POSIX_TIMERS:

CONFIGURE_MAXIMUM_POSIX_TIMERS
------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_TIMERS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_POSIX_TIMERS`` is the maximum number of POSIX API
    Timers that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode.

    Timers are only available if RTEMS was built with the
    ``--enable-posix`` build configuration option.

.. index:: CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE
.. index:: minimum POSIX thread stack size

.. _CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE:

CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE
-----------------------------------------

CONSTANT:
    ``CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is two times the value of
    :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE <CONFIGURE_MINIMUM_TASK_STACK_SIZE>`.

DESCRIPTION:
    This configuration parameter defines the minimum stack size in bytes for
    every POSIX thread in the system.

NOTES:
    None.
