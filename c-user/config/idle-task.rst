.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Idle Task Configuration
=======================

This section describes configuration options related to the idle tasks.

.. index:: CONFIGURE_IDLE_TASK_BODY

.. _CONFIGURE_IDLE_TASK_BODY:

CONFIGURE_IDLE_TASK_BODY
------------------------

CONSTANT:
    ``CONFIGURE_IDLE_TASK_BODY``

DATA TYPE:
    Function pointer.

RANGE:
    Undefined or valid function pointer.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_IDLE_TASK_BODY`` is set to the function name corresponding to
    the application specific IDLE thread body.  If not specified, the BSP or
    RTEMS default IDLE thread body will be used.

NOTES:
    None.

.. index:: CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION

.. _CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION:

CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION
-------------------------------------------

CONSTANT:
    ``CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default, the user is assumed to provide one or more
    initialization tasks.

DESCRIPTION:
    ``CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`` is set to indicate that the
    user has configured *NO* user initialization tasks or threads and that the
    user provided IDLE task will perform application initialization and then
    transform itself into an IDLE task.

NOTES:
    If you use this option be careful, the user IDLE task *CANNOT* block at all
    during the initialization sequence.  Further, once application
    initialization is complete, it must make itself preemptible and enter an
    IDLE body loop.

    The IDLE task must run at the lowest priority of all tasks in the system.

.. index:: CONFIGURE_IDLE_TASK_STACK_SIZE

.. _CONFIGURE_IDLE_TASK_STACK_SIZE:

CONFIGURE_IDLE_TASK_STACK_SIZE
------------------------------

CONSTANT:
    ``CONFIGURE_IDLE_TASK_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    The default value is RTEMS_MINIMUM_STACK_SIZE.

DESCRIPTION:
    ``CONFIGURE_IDLE_TASK_STACK_SIZE`` is set to the desired stack size for the
    IDLE task.

NOTES:
    None.
