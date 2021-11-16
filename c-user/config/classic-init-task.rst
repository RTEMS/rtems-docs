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

.. Generated from spec:/acfg/if/group-classicinit

Classic API Initialization Task Configuration
=============================================

This section describes configuration options related to the Classic API
initialization task.

.. Generated from spec:/acfg/if/init-task-arguments

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_ARGUMENTS

.. _CONFIGURE_INIT_TASK_ARGUMENTS:

CONFIGURE_INIT_TASK_ARGUMENTS
-----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_ARGUMENTS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines task argument of the Classic
API initialization task.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be convertible to an integer of
type :c:type:`rtems_task_argument`.

.. Generated from spec:/acfg/if/init-task-attributes

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_ATTRIBUTES

.. _CONFIGURE_INIT_TASK_ATTRIBUTES:

CONFIGURE_INIT_TASK_ATTRIBUTES
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_ATTRIBUTES``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is :c:macro:`RTEMS_DEFAULT_ATTRIBUTES`.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the task attributes of the
Classic API initialization task.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid task attribute set.

.. Generated from spec:/acfg/if/init-task-construct-storage-size

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_CONSTRUCT_STORAGE_SIZE

.. _CONFIGURE_INIT_TASK_CONSTRUCT_STORAGE_SIZE:

CONFIGURE_INIT_TASK_CONSTRUCT_STORAGE_SIZE
------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_CONSTRUCT_STORAGE_SIZE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

This configuration option has no default value.  If it is not specified, then
the Classic API initialization task will be created with the stack size
defined by the :ref:`CONFIGURE_INIT_TASK_STACK_SIZE` configuration option.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the task storage size of the
Classic API initialization task.

.. rubric:: NOTES:

If this configuration option is specified, then

* a task storage area of the specified size is statically allocated by
  ``<rtems/confdefs.h>`` for the Classic API initialization task,

* the Classic API initialization task is constructed by
  :c:func:`rtems_task_construct` instead of using
  :c:func:`rtems_task_create`,

* the maximum thread-local storage size defined by
  :ref:`CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE` is used for the Classic API
  initialization task,

* the Classic API initialization task should be accounted for in
  :ref:`CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE`, and

* the task storage area used for the Classic API initialization task is not
  reclaimed by the system if the task is deleted.

The

* :ref:`CONFIGURE_INIT_TASK_STACK_SIZE` and

* ``CONFIGURE_INIT_TASK_CONSTRUCT_STORAGE_SIZE``

configuration options are mutually exclusive.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to
  :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

* The value of the configuration option shall be defined using
  :c:func:`RTEMS_TASK_STORAGE_SIZE`.

.. Generated from spec:/acfg/if/init-task-entrypoint

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_ENTRY_POINT

.. _CONFIGURE_INIT_TASK_ENTRY_POINT:

CONFIGURE_INIT_TASK_ENTRY_POINT
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_ENTRY_POINT``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is ``Init``.

.. rubric:: DESCRIPTION:

The value of this configuration option initializes the entry point of the
Classic API initialization task.

.. rubric:: NOTES:

The application shall provide the function referenced by this configuration
option.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be defined to a valid function
pointer of the type ``void ( *entry_point )( rtems_task_argument )``.

.. Generated from spec:/acfg/if/init-task-initial-modes

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_INITIAL_MODES

.. _CONFIGURE_INIT_TASK_INITIAL_MODES:

CONFIGURE_INIT_TASK_INITIAL_MODES
---------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_INITIAL_MODES``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

In SMP  configurations, the default value is :c:macro:`RTEMS_DEFAULT_MODES`
otherwise the default value is :c:macro:`RTEMS_NO_PREEMPT`.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the initial execution mode of
the Classic API initialization task.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid task mode set.

.. Generated from spec:/acfg/if/init-task-name

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_NAME

.. _CONFIGURE_INIT_TASK_NAME:

CONFIGURE_INIT_TASK_NAME
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_NAME``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is ``rtems_build_name( 'U', 'I', '1', ' ' )``.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the name of the Classic API
initialization task.

.. rubric:: NOTES:

Use :c:func:`rtems_build_name` to define the task name.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be convertible to an integer of
type :c:type:`rtems_name`.

.. Generated from spec:/acfg/if/init-task-priority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_PRIORITY

.. _CONFIGURE_INIT_TASK_PRIORITY:

CONFIGURE_INIT_TASK_PRIORITY
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 1.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the initial priority of the
Classic API initialization task.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid Classic API task
priority.  The set of valid task priorities depends on the scheduler
configuration.

.. Generated from spec:/acfg/if/init-task-stack-size

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_INIT_TASK_STACK_SIZE

.. _CONFIGURE_INIT_TASK_STACK_SIZE:

CONFIGURE_INIT_TASK_STACK_SIZE
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_INIT_TASK_STACK_SIZE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the task stack size of the
Classic API initialization task.

.. rubric:: NOTES:

The

* ``CONFIGURE_INIT_TASK_STACK_SIZE`` and

* :ref:`CONFIGURE_INIT_TASK_CONSTRUCT_STORAGE_SIZE`

configuration options are mutually exclusive.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to
  :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

* The value of the configuration option shall be small enough so that the task
  stack space calculation carried out by ``<rtems/confdefs.h>`` does not
  overflow an integer of type `uintptr_t
  <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/rtems-init-tasks-table

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_RTEMS_INIT_TASKS_TABLE

.. _CONFIGURE_RTEMS_INIT_TASKS_TABLE:

CONFIGURE_RTEMS_INIT_TASKS_TABLE
--------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_RTEMS_INIT_TASKS_TABLE``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then exactly one Classic API
initialization task is configured.

.. rubric:: NOTES:

The application shall define exactly one of the following configuration
options

* ``CONFIGURE_RTEMS_INIT_TASKS_TABLE``,

* :ref:`CONFIGURE_POSIX_INIT_THREAD_TABLE`, or

* :ref:`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`

otherwise a compile time error in the configuration file will occur.
