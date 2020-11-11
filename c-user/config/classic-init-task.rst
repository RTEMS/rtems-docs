.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://docs.rtems.org/branches/master/user/support/bugs.html
..
.. For information on updating and regenerating please refer to:
..
.. https://docs.rtems.org/branches/master/eng/req/howto.html

.. Generated from spec:/acfg/if/group-classicinit

Classic API Initialization Task Configuration
=============================================

This section describes configuration options related to the Classic API
initialization task.

.. Generated from spec:/acfg/if/init-task-arguments

.. index:: CONFIGURE_INIT_TASK_ARGUMENTS

.. _CONFIGURE_INIT_TASK_ARGUMENTS:

CONFIGURE_INIT_TASK_ARGUMENTS
-----------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_ARGUMENTS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid integer of type
    :c:type:`rtems_task_argument`.

DESCRIPTION:
    The value of this configuration option defines task argument of the Classic
    API initialization task.

NOTES:
    None.

.. Generated from spec:/acfg/if/init-task-attributes

.. index:: CONFIGURE_INIT_TASK_ATTRIBUTES

.. _CONFIGURE_INIT_TASK_ATTRIBUTES:

CONFIGURE_INIT_TASK_ATTRIBUTES
------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_ATTRIBUTES``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is :c:macro:`RTEMS_DEFAULT_ATTRIBUTES`.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid task attribute set.

DESCRIPTION:
    The value of this configuration option defines the task attributes of the
    Classic API initialization task.

NOTES:
    None.

.. Generated from spec:/acfg/if/init-task-entrypoint

.. index:: CONFIGURE_INIT_TASK_ENTRY_POINT

.. _CONFIGURE_INIT_TASK_ENTRY_POINT:

CONFIGURE_INIT_TASK_ENTRY_POINT
-------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_ENTRY_POINT``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is ``Init``.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void ( *entry_point )( rtems_task_argument )``.

DESCRIPTION:
    The value of this configuration option initializes the entry point of the
    Classic API initialization task.

NOTES:
    The application shall provide the function referenced by this configuration
    option.

.. Generated from spec:/acfg/if/init-task-initial-modes

.. index:: CONFIGURE_INIT_TASK_INITIAL_MODES

.. _CONFIGURE_INIT_TASK_INITIAL_MODES:

CONFIGURE_INIT_TASK_INITIAL_MODES
---------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_INITIAL_MODES``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    In SMP  configurations, the default value is :c:macro:`RTEMS_DEFAULT_MODES`
    otherwise the default value is :c:macro:`RTEMS_NO_PREEMPT`.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid task mode set.

DESCRIPTION:
    The value of this configuration option defines the initial execution mode of
    the Classic API initialization task.

NOTES:
    None.

.. Generated from spec:/acfg/if/init-task-name

.. index:: CONFIGURE_INIT_TASK_NAME

.. _CONFIGURE_INIT_TASK_NAME:

CONFIGURE_INIT_TASK_NAME
------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_NAME``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is ``rtems_build_name( 'U', 'I', '1', ' ' )``.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid integer of type
    :c:type:`rtems_name`.

DESCRIPTION:
    The value of this configuration option defines the name of the Classic API
    initialization task.

NOTES:
    Use :c:func:`rtems_build_name` to define the task name.

.. Generated from spec:/acfg/if/init-task-priority

.. index:: CONFIGURE_INIT_TASK_PRIORITY

.. _CONFIGURE_INIT_TASK_PRIORITY:

CONFIGURE_INIT_TASK_PRIORITY
----------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_PRIORITY``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 1.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a valid Classic API task
    priority.  The set of valid task priorities is scheduler-specific.

DESCRIPTION:
    The value of this configuration option defines the initial priority of the
    Classic API initialization task.

NOTES:
    None.

.. Generated from spec:/acfg/if/init-task-stack-size

.. index:: CONFIGURE_INIT_TASK_STACK_SIZE

.. _CONFIGURE_INIT_TASK_STACK_SIZE:

CONFIGURE_INIT_TASK_STACK_SIZE
------------------------------

CONSTANT:
    ``CONFIGURE_INIT_TASK_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

    * It shall be small enough so that the task
      stack space calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the task stack size of the
    Classic API initialization task.

NOTES:
    None.

.. Generated from spec:/acfg/if/rtems-init-tasks-table

.. index:: CONFIGURE_RTEMS_INIT_TASKS_TABLE

.. _CONFIGURE_RTEMS_INIT_TASKS_TABLE:

CONFIGURE_RTEMS_INIT_TASKS_TABLE
--------------------------------

CONSTANT:
    ``CONFIGURE_RTEMS_INIT_TASKS_TABLE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then exactly one Classic API
    initialization task is configured.

NOTES:
    The application shall define exactly one of the following configuration
    options

    * ``CONFIGURE_RTEMS_INIT_TASKS_TABLE``,

    * :ref:`CONFIGURE_POSIX_INIT_THREAD_TABLE`, or

    * :ref:`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`

    otherwise a compile time error in the configuration file will occur.
