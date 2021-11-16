.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2021 On-Line Applications Research Corporation (OAR)

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

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR
.. index:: task stack allocator

.. _CONFIGURE_TASK_STACK_ALLOCATOR:

CONFIGURE_TASK_STACK_ALLOCATOR
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_TASK_STACK_ALLOCATOR``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is ``_Workspace_Allocate``, which indicates that task
stacks will be allocated from the RTEMS Workspace.

.. rubric:: DESCRIPTION:

The value of this configuration option initializes the stack allocator
allocate handler.

.. rubric:: NOTES:

A correctly configured system shall configure the following to be consistent:

* :ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

* ``CONFIGURE_TASK_STACK_ALLOCATOR``

* :ref:`CONFIGURE_TASK_STACK_DEALLOCATOR`

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be defined to a valid function
pointer of the type ``void *( *allocate )( size_t )``.

.. Generated from spec:/acfg/if/task-stack-no-workspace

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE

.. _CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE:

CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE
------------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the system is informed
that the task stack allocator does not use the RTEMS Workspace.

.. rubric:: NOTES:

This configuration option may be used if a custom task stack allocator is
configured, see :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`.

.. Generated from spec:/acfg/if/task-stack-allocator-for-idle

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_FOR_IDLE
.. index:: task stack allocator for IDLE tasks

.. _CONFIGURE_TASK_STACK_ALLOCATOR_FOR_IDLE:

CONFIGURE_TASK_STACK_ALLOCATOR_FOR_IDLE
---------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_TASK_STACK_ALLOCATOR_FOR_IDLE``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is ``_Stack_Allocator_allocate_for_idle_default``, which
indicates that IDLE task stacks will be allocated from an area statically
allocated by ``<rtems/confdefs.h>``.

.. rubric:: DESCRIPTION:

The value of this configuration option is the address for the stack allocator
allocate handler used to allocate the task stack of each
:term:`IDLE task`.

.. rubric:: NOTES:

This configuration option is independent of the other thread stack allocator
configuration options.  It is assumed that any memory allocated for the stack
of an :term:`IDLE task` will not be from the RTEMS Workspace or the
memory statically allocated by default.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be defined to a valid function
pointer of the type ``void *( *allocate )( uint32_t, size_t )``.

.. Generated from spec:/acfg/if/task-stack-allocator-init

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_TASK_STACK_ALLOCATOR_INIT

.. _CONFIGURE_TASK_STACK_ALLOCATOR_INIT:

CONFIGURE_TASK_STACK_ALLOCATOR_INIT
-----------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is `NULL <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: DESCRIPTION:

The value of this configuration option initializes the stack allocator
initialization handler.

.. rubric:: NOTES:

A correctly configured system shall configure the following to be consistent:

* ``CONFIGURE_TASK_STACK_ALLOCATOR_INIT``

* :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`

* :ref:`CONFIGURE_TASK_STACK_DEALLOCATOR`

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be defined to a valid function
pointer of the type ``void ( *initialize )( size_t )`` or to `NULL
<https://en.cppreference.com/w/c/types/NULL>`_.

.. Generated from spec:/acfg/if/task-stack-deallocator

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_TASK_STACK_DEALLOCATOR
.. index:: task stack deallocator

.. _CONFIGURE_TASK_STACK_DEALLOCATOR:

CONFIGURE_TASK_STACK_DEALLOCATOR
--------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_TASK_STACK_DEALLOCATOR``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is ``_Workspace_Free``, which indicates that task stacks
will be allocated from the RTEMS Workspace.

.. rubric:: DESCRIPTION:

The value of this configuration option initializes the stack allocator
deallocate handler.

.. rubric:: NOTES:

A correctly configured system shall configure the following to be consistent:

* :ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT`

* :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`

* ``CONFIGURE_TASK_STACK_DEALLOCATOR``

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be defined to a valid function
pointer of the type ``void ( *deallocate )( void * )``.

.. Generated from spec:/acfg/if/task-stack-from-alloc

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_TASK_STACK_FROM_ALLOCATOR
.. index:: task stack allocator

.. _CONFIGURE_TASK_STACK_FROM_ALLOCATOR:

CONFIGURE_TASK_STACK_FROM_ALLOCATOR
-----------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_TASK_STACK_FROM_ALLOCATOR``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is a macro which supports the system heap allocator.

.. rubric:: DESCRIPTION:

The value of this configuration option is used to calculate the task stack
space size.

.. rubric:: NOTES:

This configuration option may be used if a custom task stack allocator is
configured, see :ref:`CONFIGURE_TASK_STACK_ALLOCATOR`.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be defined to a macro which accepts
exactly one parameter and returns an unsigned integer.  The parameter will be
an allocation size and the macro shall return this size plus the overhead of
the allocator to manage an allocation request for this size.
