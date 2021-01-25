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

.. Generated from spec:/acfg/if/group-bsp

BSP Related Configuration Options
=================================

This section describes configuration options related to the BSP.  Some
configuration options may have a BSP-specific setting which is defined by
``<bsp.h>``.  The BSP-specific settings can be disabled by the
:ref:`CONFIGURE_DISABLE_BSP_SETTINGS` configuration option.

.. Generated from spec:/acfg/if/bsp-idle-task-body

.. index:: BSP_IDLE_TASK_BODY

.. _BSP_IDLE_TASK_BODY:

BSP_IDLE_TASK_BODY
------------------

CONSTANT:
    ``BSP_IDLE_TASK_BODY``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is BSP-specific.

VALUE CONSTRAINTS:
    The value of this configuration option shall be defined to a valid function
    pointer of the type ``void *( *idle_body )( uintptr_t )``.

DESCRIPTION:
    If

    * this configuration option is defined by the BSP

    * and :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` is undefined,

    then the value of this configuration option defines the default value of
    :ref:`CONFIGURE_IDLE_TASK_BODY`.

NOTES:
    As it has knowledge of the specific CPU model, system controller logic, and
    peripheral buses, a BSP-specific IDLE task may be capable of turning
    components off to save power during extended periods of no task activity.

.. Generated from spec:/acfg/if/bsp-idle-task-stack-size

.. index:: BSP_IDLE_TASK_STACK_SIZE

.. _BSP_IDLE_TASK_STACK_SIZE:

BSP_IDLE_TASK_STACK_SIZE
------------------------

CONSTANT:
    ``BSP_IDLE_TASK_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is BSP-specific.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to a
      BSP-specific and application-specific minimum value.

    * It shall be small enough so that the IDLE
      task stack area calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `size_t <https://en.cppreference.com/w/c/types/size_t>`_.

DESCRIPTION:
    If

    * this configuration option is defined by the BSP

    * and :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` is undefined,

    then the value of this configuration option defines the default value of
    :ref:`CONFIGURE_IDLE_TASK_STACK_SIZE`.

NOTES:
    None.

.. Generated from spec:/acfg/if/bsp-initial-extension

.. index:: BSP_INITIAL_EXTENSION

.. _BSP_INITIAL_EXTENSION:

BSP_INITIAL_EXTENSION
---------------------

CONSTANT:
    ``BSP_INITIAL_EXTENSION``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is BSP-specific.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a list of initializers for
    structures of type :c:type:`rtems_extensions_table`.

DESCRIPTION:
    If

    * this configuration option is defined by the BSP

    * and :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` is undefined,

    then the value of this configuration option is used to initialize the table
    of initial user extensions.

NOTES:
    The value of this configuration option is placed after the entries of all
    other initial user extensions.

.. Generated from spec:/acfg/if/bsp-interrupt-stack-size

.. index:: BSP_INTERRUPT_STACK_SIZE

.. _BSP_INTERRUPT_STACK_SIZE:

BSP_INTERRUPT_STACK_SIZE
------------------------

CONSTANT:
    ``BSP_INTERRUPT_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is BSP-specific.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to a
      BSP-specific and application-specific minimum value.

    * It shall be small enough so that the
      interrupt stack area calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `size_t <https://en.cppreference.com/w/c/types/size_t>`_.

    * It shall be aligned according to
      :c:macro:`CPU_INTERRUPT_STACK_ALIGNMENT`.

DESCRIPTION:
    If

    * this configuration option is defined by the BSP

    * and :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` is undefined,

    then the value of this configuration option defines the default value of
    :ref:`CONFIGURE_INTERRUPT_STACK_SIZE`.

NOTES:
    None.

.. Generated from spec:/acfg/if/bsp-prerequisite-drivers

.. index:: CONFIGURE_BSP_PREREQUISITE_DRIVERS

.. _CONFIGURE_BSP_PREREQUISITE_DRIVERS:

CONFIGURE_BSP_PREREQUISITE_DRIVERS
----------------------------------

CONSTANT:
    ``CONFIGURE_BSP_PREREQUISITE_DRIVERS``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is BSP-specific.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a list of initializers for
    structures of type :c:type:`rtems_extensions_table`.

DESCRIPTION:
    If

    * this configuration option is defined by the BSP

    * and :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` is undefined,

    then the value of this configuration option is used to initialize the table
    of initial user extensions.

NOTES:
    The value of this configuration option is placed before the entries of all
    other initial user extensions (including
    :ref:`CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS`).

.. Generated from spec:/acfg/if/disable-bsp-settings

.. index:: CONFIGURE_DISABLE_BSP_SETTINGS

.. _CONFIGURE_DISABLE_BSP_SETTINGS:

CONFIGURE_DISABLE_BSP_SETTINGS
------------------------------

CONSTANT:
    ``CONFIGURE_DISABLE_BSP_SETTINGS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the following BSP related
    configuration options are undefined:

    * :ref:`BSP_IDLE_TASK_BODY`

    * :ref:`BSP_IDLE_TASK_STACK_SIZE`

    * :ref:`BSP_INITIAL_EXTENSION`

    * :ref:`BSP_INTERRUPT_STACK_SIZE`

    * :ref:`CONFIGURE_BSP_PREREQUISITE_DRIVERS`

    * :ref:`CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK`

NOTES:
    None.

.. Generated from spec:/acfg/if/malloc-bsp-supports-sbrk

.. index:: CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK

.. _CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK:

CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK
----------------------------------

CONSTANT:
    ``CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    If

    * this configuration option is defined by the BSP

    * and :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` is undefined,

    then not all memory is made available to the C Program Heap immediately at
    system initialization time.  When :c:func:`malloc` or other standard
    memory allocation functions are unable to allocate memory, they will call the
    BSP supplied :c:func:`sbrk` function to obtain more memory.

NOTES:
    This option should not be defined by the application. Only the BSP knows how
    it allocates memory to the C Program Heap.
