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

.. Generated from spec:/acfg/if/group-idle

Idle Task Configuration
=======================

This section describes configuration options related to the idle tasks.

.. Generated from spec:/acfg/if/idle-task-body

.. index:: CONFIGURE_IDLE_TASK_BODY

.. _CONFIGURE_IDLE_TASK_BODY:

CONFIGURE_IDLE_TASK_BODY
------------------------

CONSTANT:
    ``CONFIGURE_IDLE_TASK_BODY``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    If :ref:`BSP_IDLE_TASK_BODY` is defined, then this will be the default value,
    otherwise the default value is ``_CPU_Thread_Idle_body``.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void *( *idle_body )( uintptr_t )``.

DESCRIPTION:
    The value of this configuration option initializes the IDLE thread body.

NOTES:
    IDLE threads shall not block.  A blocking IDLE thread results in undefined
    system behaviour because the scheduler assume that at least one ready thread
    exists.

    IDLE threads can be used to initialize the application, see configuration
    option :ref:`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`.

.. Generated from spec:/acfg/if/idle-task-init-appl

.. index:: CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION

.. _CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION:

CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION
-------------------------------------------

CONSTANT:
    ``CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the user is assumed to
    provide one or more initialization tasks.

DESCRIPTION:
    This configuration option is defined to indicate that the user has configured
    **no** user initialization tasks or threads and that the user provided IDLE
    task will perform application initialization and then transform itself into
    an IDLE task.

NOTES:
    If you use this option be careful, the user IDLE task **cannot** block at all
    during the initialization sequence.  Further, once application
    initialization is complete, it shall make itself preemptible and enter an idle
    body loop.

    The IDLE task shall run at the lowest priority of all tasks in the system.

    If this configuration option is defined, then it is mandatory to configure a
    user IDLE task with the :ref:`CONFIGURE_IDLE_TASK_BODY` configuration option,
    otherwise a compile time error in the configuration file will occur.

    The application shall define exactly one of the following configuration
    options

    * :ref:`CONFIGURE_RTEMS_INIT_TASKS_TABLE`,

    * :ref:`CONFIGURE_POSIX_INIT_THREAD_TABLE`, or

    * ``CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION``

    otherwise a compile time error in the configuration file will occur.

.. Generated from spec:/acfg/if/idle-task-stack-size

.. index:: CONFIGURE_IDLE_TASK_STACK_SIZE

.. _CONFIGURE_IDLE_TASK_STACK_SIZE:

CONFIGURE_IDLE_TASK_STACK_SIZE
------------------------------

CONSTANT:
    ``CONFIGURE_IDLE_TASK_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to a
      BSP-specific and application-specific minimum value.

    * It shall be small enough so that the IDLE
      task stack area calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `size_t <https://en.cppreference.com/w/c/types/size_t>`_.

DESCRIPTION:
    The value of this configuration option defines the task stack size for an
    IDLE task.

NOTES:
    In SMP configurations, there is one IDLE task per configured processor, see
    :ref:`CONFIGURE_MAXIMUM_PROCESSORS`.
