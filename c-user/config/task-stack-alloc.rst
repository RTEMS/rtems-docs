.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Task Stack Allocator Configuration
==================================

This section describes configuration options related to the task stack
allocator.  RTEMS allows the application or BSP to define its own allocation
and deallocation methods for task stacks. This can be used to place task stacks
in special areas of memory or to utilize a Memory Management Unit so that stack
overflows are detected in hardware.

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR
.. index:: task stack allocator

.. _CONFIGURE_TASK_STACK_ALLOCATOR:

CONFIGURE_TASK_STACK_ALLOCATOR
------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_ALLOCATOR``

DATA TYPE:
    Function pointer.

RANGE:
    Undefined or valid function pointer.

DEFAULT VALUE:
    The default value is ``_Workspace_Allocate``, which indicates that task
    stacks will be allocated from the RTEMS Workspace.

DESCRIPTION:
    ``CONFIGURE_TASK_STACK_ALLOCATOR`` may point to a user provided routine to
    allocate task stacks.

NOTES:
    A correctly configured system must configure the following to be consistent:

    - ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

    - ``CONFIGURE_TASK_STACK_ALLOCATOR``

    - ``CONFIGURE_TASK_STACK_DEALLOCATOR``

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_INIT

.. _CONFIGURE_TASK_STACK_ALLOCATOR_INIT:

CONFIGURE_TASK_STACK_ALLOCATOR_INIT
-----------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

DATA TYPE:
    Function pointer.

RANGE:
    Undefined, NULL or valid function pointer.

DEFAULT VALUE:
    The default value is NULL, which indicates that task stacks will be
    allocated from the RTEMS Workspace.

DESCRIPTION:
    ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT`` configures the initialization
    method for an application or BSP specific task stack allocation
    implementation.

NOTES:
    A correctly configured system must configure the following to be consistent:

    - ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

    - ``CONFIGURE_TASK_STACK_ALLOCATOR``

    - ``CONFIGURE_TASK_STACK_DEALLOCATOR``

.. index:: CONFIGURE_TASK_STACK_DEALLOCATOR
.. index:: task stack deallocator

.. _CONFIGURE_TASK_STACK_DEALLOCATOR:

CONFIGURE_TASK_STACK_DEALLOCATOR
--------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_DEALLOCATOR``

DATA TYPE:
    Function pointer.

RANGE:
    Undefined or valid function pointer.

DEFAULT VALUE:
    The default value is ``_Workspace_Free``, which indicates that task stacks
    will be allocated from the RTEMS Workspace.

DESCRIPTION:
    ``CONFIGURE_TASK_STACK_DEALLOCATOR`` may point to a user provided routine
    to free task stacks.

NOTES:
    A correctly configured system must configure the following to be consistent:

    - ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

    - ``CONFIGURE_TASK_STACK_ALLOCATOR``

    - ``CONFIGURE_TASK_STACK_DEALLOCATOR``
