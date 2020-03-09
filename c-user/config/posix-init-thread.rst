.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

POSIX Initialization Thread Configuration
=========================================

The ``<rtems/confdefs.h>`` configuration system can automatically generate a
POSIX Initialization Threads Table named ``POSIX_Initialization_threads`` with
a single entry.  The following parameters control the generation of that table.

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

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This field is not defined by default, as the user MUST select their own API
    for initialization tasks.

DESCRIPTION:
    ``CONFIGURE_POSIX_INIT_THREAD_TABLE`` is defined if the user wishes to use
    a POSIX API Initialization Threads Table.  The table built by
    ``<rtems/confdefs.h>`` specifies the parameters for a single thread. This
    is sufficient for applications which initialization the system from a
    single task.

    By default, this field is not defined as the user MUST select their own API
    for initialization tasks.

NOTES:
    The application may choose to use the initialization tasks or threads table
    from another API.

    A compile time error will be generated if the user does not configure any
    initialization tasks or threads.
