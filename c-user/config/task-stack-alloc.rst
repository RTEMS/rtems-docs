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

.. Generated from spec:/acfg/if/group-stackalloc

Task Stack Allocator Configuration
==================================

This section describes configuration options related to the task stack
allocator.  RTEMS allows the application or BSP to define its own allocation
and deallocation methods for task stacks. This can be used to place task stacks
in special areas of memory or to utilize a Memory Management Unit so that stack
overflows are detected in hardware.

.. Generated from spec:/acfg/if/task-stack-allocator

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

    * :ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

    * ``CONFIGURE_TASK_STACK_ALLOCATOR``

    * :ref:`CONFIGURE_TASK_STACK_DEALLOCATOR`

.. Generated from spec:/acfg/if/task-stack-no-workspace

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE

.. _CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE:

CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE
------------------------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the system is informed
    that the task stack allocator does not use the RTEMS Workspace.

NOTES:
    This configuration option may be used if a custom task stack allocator is
    configured, see :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`.

.. Generated from spec:/acfg/if/task-stack-allocator-init

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_INIT

.. _CONFIGURE_TASK_STACK_ALLOCATOR_INIT:

CONFIGURE_TASK_STACK_ALLOCATOR_INIT
-----------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is `NULL <https://en.cppreference.com/w/c/types/NULL>`_.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void ( *initialize )( size_t )`` or to
    `NULL <https://en.cppreference.com/w/c/types/NULL>`_.

DESCRIPTION:
    The value of this configuration option initializes the stack allocator
    initialization handler.

NOTES:
    A correctly configured system shall configure the following to be consistent:

    * ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

    * :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`

    * :ref:`CONFIGURE_TASK_STACK_DEALLOCATOR`

.. Generated from spec:/acfg/if/task-stack-deallocator

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

    * :ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

    * :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`

    * ``CONFIGURE_TASK_STACK_DEALLOCATOR``

.. Generated from spec:/acfg/if/task-stack-from-alloc

.. index:: CONFIGURE_TASK_STACK_FROM_ALLOCATOR
.. index:: task stack allocator

.. _CONFIGURE_TASK_STACK_FROM_ALLOCATOR:

CONFIGURE_TASK_STACK_FROM_ALLOCATOR
-----------------------------------

CONSTANT:
    ``CONFIGURE_TASK_STACK_FROM_ALLOCATOR``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is a macro which supports the system heap allocator.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a macro which
    accepts exactly one parameter and returns an unsigned integer.  The
    parameter will be an allocation size and the macro shall return this size
    plus the overhead of the allocator to manage an allocation request for this
    size.

DESCRIPTION:
    The value of this configuration option is used to calculate the task stack
    space size.

NOTES:
    This configuration option may be used if a custom task stack allocator is
    configured, see :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`.
