.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

BSP Related Configuration Options
=================================

This section describes configuration options related to the BSP.  Some
configuration options may have a BSP-specific setting which is defined by
``<bsp.h>``.  The BSP-specific settings can be disabled by the
:ref:`CONFIGURE_DISABLE_BSP_SETTINGS` configuration option.

.. index:: BSP_IDLE_TASK_BODY

.. _BSP_IDLE_TASK_BODY:

BSP_IDLE_TASK_BODY
------------------

CONSTANT:
    ``BSP_IDLE_TASK_BODY``

DATA TYPE:
    Function pointer.

RANGE:
    Undefined or valid function pointer.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    If ``BSP_IDLE_TASK_BODY`` is defined by the BSP and
    ``CONFIGURE_IDLE_TASK_BODY`` is not defined by the application, then this
    BSP specific idle task body will be used.

NOTES:
    As it has knowledge of the specific CPU model, system controller logic, and
    peripheral buses, a BSP specific IDLE task may be capable of turning
    components off to save power during extended periods of no task activity

.. index:: BSP_IDLE_TASK_STACK_SIZE

.. _BSP_IDLE_TASK_STACK_SIZE:

BSP_IDLE_TASK_STACK_SIZE
------------------------

CONSTANT:
    ``BSP_IDLE_TASK_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    If ``BSP_IDLE_TASK_STACK_SIZE`` is defined by the BSP and
    ``CONFIGURE_IDLE_TASK_STACK_SIZE`` is not defined by the application, then
    this BSP suggested idle task stack size will be used.

NOTES:
    The order of precedence for configuring the IDLE task stack size is:

    - RTEMS default minimum stack size.

    - If defined, then ``CONFIGURE_MINIMUM_TASK_STACK_SIZE``.

    - If defined, then the BSP specific ``BSP_IDLE_TASK_SIZE``.

    - If defined, then the application specified ``CONFIGURE_IDLE_TASK_SIZE``.

.. index:: BSP_INITIAL_EXTENSION

.. _BSP_INITIAL_EXTENSION:

BSP_INITIAL_EXTENSION
---------------------

CONSTANT:
    ``BSP_INITIAL_EXTENSION``

DATA TYPE:
    List of user extension initializers (``rtems_extensions_table``).

RANGE:
    Undefined or a list of user extension initializers.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    If ``BSP_INITIAL_EXTENSION`` is defined by the BSP, then this BSP specific
    initial extension will be placed as the last entry in the initial extension
    table.

NOTES:
    None.

.. index:: BSP_INTERRUPT_STACK_SIZE

.. _BSP_INTERRUPT_STACK_SIZE:

BSP_INTERRUPT_STACK_SIZE
------------------------

CONSTANT:
    ``BSP_INTERRUPT_STACK_SIZE``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    If ``BSP_INTERRUPT_STACK_SIZE`` is defined by the BSP and
    ``CONFIGURE_INTERRUPT_STACK_SIZE`` is not defined by the application, then
    this BSP specific interrupt stack size will be used.

NOTES:
    None.

.. index:: BSP_MAXIMUM_DEVICES

.. _BSP_MAXIMUM_DEVICES:

BSP_MAXIMUM_DEVICES
-------------------

CONSTANT:
    ``BSP_MAXIMUM_DEVICES``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    If ``BSP_MAXIMUM_DEVICES`` is defined by the BSP and
    ``CONFIGURE_MAXIMUM_DEVICES`` is not defined by the application, then this
    BSP specific maximum device count will be used.

NOTES:
    This option is specific to the device file system (devFS) and should not be
    confused with the ``CONFIGURE_MAXIMUM_DRIVERS`` option.  This parameter
    only impacts the devFS and thus is only used by ``<rtems/confdefs.h>`` when
    ``CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM`` is specified.

.. index:: CONFIGURE_BSP_PREREQUISITE_DRIVERS

.. _CONFIGURE_BSP_PREREQUISITE_DRIVERS:

CONFIGURE_BSP_PREREQUISITE_DRIVERS
----------------------------------

CONSTANT:
    ``CONFIGURE_BSP_PREREQUISITE_DRIVERS``

DATA TYPE:
    List of device driver initializers (``rtems_driver_address_table``).

RANGE:
    Undefined or array of device drivers.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    ``CONFIGURE_BSP_PREREQUISITE_DRIVERS`` is defined if the BSP has device
    drivers it needs to include in the Device Driver Table.  This should be
    defined to the set of device driver entries that will be placed in the
    table at the *FRONT* of the Device Driver Table and initialized before any
    other drivers *INCLUDING* any application prerequisite drivers.

NOTES:
    ``CONFIGURE_BSP_PREREQUISITE_DRIVERS`` is typically used by BSPs to
    configure common infrastructure such as bus controllers or probe for
    devices.

.. index:: CONFIGURE_DISABLE_BSP_SETTINGS

.. _CONFIGURE_DISABLE_BSP_SETTINGS:

CONFIGURE_DISABLE_BSP_SETTINGS
------------------------------

CONSTANT:
    ``CONFIGURE_DISABLE_BSP_SETTINGS``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    All BSP specific configuration settings can be disabled by the application
    with the ``CONFIGURE_DISABLE_BSP_SETTINGS`` option.

NOTES:
    None.

.. index:: CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK

.. _CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK:

CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK
----------------------------------

CONSTANT:
    ``CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This option is BSP specific.

DESCRIPTION:
    This configuration parameter is defined by a BSP to indicate that it does
    not allocate all available memory to the C Program Heap used by the Malloc
    Family of routines.

    If defined, when ``malloc()`` is unable to allocate memory, it will call
    the BSP supplied ``sbrk()`` to obtain more memory.

NOTES:
    This parameter should not be defined by the application. Only the BSP knows
    how it allocates memory to the C Program Heap.
