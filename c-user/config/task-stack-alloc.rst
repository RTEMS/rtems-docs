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

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is ``_Workspace_Allocate``, which indicates that task
    stacks will be allocated from the RTEMS Workspace.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void *( *allocate )( size_t )``.

DESCRIPTION:
    The value of this configuration option initializes the stack allocator
    allocate handler.

NOTES:
    A correctly configured system shall configure the following to be consistent:

    - :ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

    - `CONFIGURE_TASK_STACK_ALLOCATOR`

    - :ref:`CONFIGURE_TASK_STACK_DEALLOCATOR`

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_INIT

.. _CONFIGURE_TASK_STACK_ALLOCATOR_INIT:

CONFIGURE_TASK_STACK_ALLOCATOR_INIT
-----------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is ``NULL``.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void ( *initialize )( size_t )`` or to ``NULL``.

DESCRIPTION:
    The value of this configuration option initializes the stack allocator
    initialization handler.

NOTES:
    A correctly configured system shall configure the following to be consistent:

    - `CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

    - :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`

    - :ref:`CONFIGURE_TASK_STACK_DEALLOCATOR`

.. index:: CONFIGURE_TASK_STACK_DEALLOCATOR
.. index:: task stack deallocator

.. _CONFIGURE_TASK_STACK_DEALLOCATOR:

CONFIGURE_TASK_STACK_DEALLOCATOR
--------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_DEALLOCATOR``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is ``_Workspace_Free``, which indicates that task stacks
    will be allocated from the RTEMS Workspace.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void ( *deallocate )( void * )``.

DESCRIPTION:
    The value of this configuration option initializes the stack allocator
    deallocate handler.

NOTES:
    A correctly configured system shall configure the following to be consistent:

    - :ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

    - :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`

    - `CONFIGURE_TASK_STACK_DEALLOCATOR`
