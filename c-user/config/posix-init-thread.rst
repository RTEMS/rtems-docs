.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

POSIX Initialization Thread Configuration
=========================================

This section describes configuration options related to the POSIX
initialization thread.

.. index:: CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT

.. _CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT:

CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT
---------------------------------------

CONSTANT:
    ``CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT``

DATA TYPE:
    POSIX thread function pointer (``void *(*entry_point)(void *)``).

RANGE:
    Undefined or a valid POSIX thread function pointer.

DEFAULT VALUE:
    The default value is ``POSIX_Init``.

DESCRIPTION:
    ``CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT`` is the entry point
    (a.k.a. function name) of the single initialization thread defined by the
    POSIX API Initialization Threads Table.

NOTES:
    The user must implement the function ``POSIX_Init`` or the function name
    provided in this configuration parameter.

.. index:: CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE

.. _CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE:

CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE
--------------------------------------

CONSTANT:
    ``CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is 2 \* RTEMS_MINIMUM_STACK_SIZE.

DESCRIPTION:
    ``CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE`` is the stack size of the single
    initialization thread defined by the POSIX API Initialization Threads
    Table.

NOTES:
    If the stack size specified is greater than the configured minimum, it must
    be accounted for in ``CONFIGURE_EXTRA_TASK_STACKS``.  See :ref:`Reserve
    Task/Thread Stack Memory Above Minimum` for more information about
    ``CONFIGURE_EXTRA_TASK_STACKS``.

.. index:: CONFIGURE_POSIX_INIT_THREAD_TABLE

.. _CONFIGURE_POSIX_INIT_THREAD_TABLE:

CONFIGURE_POSIX_INIT_THREAD_TABLE
---------------------------------

CONSTANT:
    ``CONFIGURE_POSIX_INIT_THREAD_TABLE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then exactly one POSIX
    initialization thread is configured.

NOTES:
    The application must define exactly one of the following configuration
    options

    * :ref:`CONFIGURE_RTEMS_INIT_TASKS_TABLE`,

    * :ref:`CONFIGURE_POSIX_INIT_THREAD_TABLE`, or

    * :ref:`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`

    otherwise a compile time error in the configuration file will occur.
