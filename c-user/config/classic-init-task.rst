.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Classic API Initialization Task Configuration
=============================================

This section describes configuration options related to the Classic API
initialization task.

.. index:: CONFIGURE_INIT_TASK_ARGUMENTS

.. _CONFIGURE_INIT_TASK_ARGUMENTS:

CONFIGURE_INIT_TASK_ARGUMENTS
-----------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_ARGUMENTS``

DATA TYPE:
    RTEMS Task Argument (``rtems_task_argument``).

RANGE:
    Complete range of the type.

DEFAULT VALUE:
    The default value is 0.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_ARGUMENTS`` is the task argument of the single
    initialization task defined by the Classic API Initialization Tasks Table.

NOTES:
    None.

.. index:: CONFIGURE_INIT_TASK_ATTRIBUTES

.. _CONFIGURE_INIT_TASK_ATTRIBUTES:

CONFIGURE_INIT_TASK_ATTRIBUTES
------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_ATTRIBUTES``

DATA TYPE:
    RTEMS Attributes (``rtems_attribute``).

RANGE:
    Valid task attribute sets.

DEFAULT VALUE:
    The default value is ``RTEMS_DEFAULT_ATTRIBUTES``.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_ATTRIBUTES`` is the task attributes of the single
    initialization task defined by the Classic API Initialization Tasks Table.

NOTES:
    None.

.. index:: CONFIGURE_INIT_TASK_ENTRY_POINT

.. _CONFIGURE_INIT_TASK_ENTRY_POINT:

CONFIGURE_INIT_TASK_ENTRY_POINT
-------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_ENTRY_POINT``

DATA TYPE:
    Task entry function pointer (``rtems_task_entry``).

RANGE:
    Valid task entry function pointer.

DEFAULT VALUE:
    The default value is ``Init``.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_ENTRY_POINT`` is the entry point (a.k.a. function
    name) of the single initialization task defined by the Classic API
    Initialization Tasks Table.

NOTES:
    The user must implement the function ``Init`` or the function name provided
    in this configuration parameter.

.. index:: CONFIGURE_INIT_TASK_INITIAL_MODES

.. _CONFIGURE_INIT_TASK_INITIAL_MODES:

CONFIGURE_INIT_TASK_INITIAL_MODES
---------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_INITIAL_MODES``

DATA TYPE:
    RTEMS Mode (``rtems_mode``).

RANGE:
    Valid task mode sets.

DEFAULT VALUE:
    The default value is ``RTEMS_NO_PREEMPT``.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_INITIAL_MODES`` is the initial execution mode of the
    single initialization task defined by the Classic API Initialization Tasks
    Table.

NOTES:
    None.

.. index:: CONFIGURE_INIT_TASK_NAME

.. _CONFIGURE_INIT_TASK_NAME:

CONFIGURE_INIT_TASK_NAME
------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_NAME``

DATA TYPE:
    RTEMS Name (``rtems_name``).

RANGE:
    Any value.

DEFAULT VALUE:
    The default value is ``rtems_build_name( 'U', 'I', '1', ' ' )``.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_NAME`` is the name of the single initialization task
    defined by the Classic API Initialization Tasks Table.

NOTES:
    None.

.. index:: CONFIGURE_INIT_TASK_PRIORITY

.. _CONFIGURE_INIT_TASK_PRIORITY:

CONFIGURE_INIT_TASK_PRIORITY
----------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_PRIORITY``

DATA TYPE:
    RTEMS Task Priority (``rtems_task_priority``).

RANGE:
    One (1) to the maximum user priority value of the scheduler.

DEFAULT VALUE:
    The default value is 1, which is the highest priority in the Classic API.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_PRIORITY`` is the initial priority of the single
    initialization task defined by the Classic API Initialization Tasks Table.

NOTES:
    None.

.. index:: CONFIGURE_INIT_TASK_STACK_SIZE

.. _CONFIGURE_INIT_TASK_STACK_SIZE:

CONFIGURE_INIT_TASK_STACK_SIZE
------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    The default value is RTEMS_MINIMUM_STACK_SIZE.

DESCRIPTION:
    ``CONFIGURE_INIT_TASK_STACK_SIZE`` is the stack size of the single
    initialization task defined by the Classic API Initialization Tasks Table.

NOTES:
    If the stack size specified is greater than the configured minimum, it must
    be accounted for in ``CONFIGURE_EXTRA_TASK_STACKS``.  See :ref:`Reserve
    Task/Thread Stack Memory Above Minimum` for more information about
    ``CONFIGURE_EXTRA_TASK_STACKS``.

.. index:: CONFIGURE_RTEMS_INIT_TASKS_TABLE

.. _CONFIGURE_RTEMS_INIT_TASKS_TABLE:

CONFIGURE_RTEMS_INIT_TASKS_TABLE
--------------------------------

CONSTANT:
    ``CONFIGURE_RTEMS_INIT_TASKS_TABLE``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_RTEMS_INIT_TASKS_TABLE`` is defined if the user wishes to use a
    Classic RTEMS API Initialization Task Table. The table built by
    ``<rtems/confdefs.h>`` specifies the parameters for a single task. This is
    sufficient for applications which initialization the system from a single
    task.

    By default, this field is not defined as the user MUST select their own API
    for initialization tasks.

NOTES:
    The application may choose to use the initialization tasks or threads table
    from another API.

    A compile time error will be generated if the user does not configure any
    initialization tasks or threads.
