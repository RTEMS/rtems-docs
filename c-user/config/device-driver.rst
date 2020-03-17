.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Device Driver Configuration
===========================

This section describes configuration options related to the device drivers.
Note that network device drivers are not covered by the following options.

.. index:: CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER

.. _CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER:

CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER
------------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`` is defined when the
    application does *NOT* want the Clock Device Driver and is *NOT* using the
    Timer Driver.  The inclusion or exclusion of the Clock Driver must be
    explicit in user applications.

NOTES:
    This configuration parameter is intended to prevent the common user error
    of using the Hello World example as the baseline for an application and
    leaving out a clock tick source.

.. index:: CONFIGURE_APPLICATION_EXTRA_DRIVERS

.. _CONFIGURE_APPLICATION_EXTRA_DRIVERS:

CONFIGURE_APPLICATION_EXTRA_DRIVERS
-----------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_EXTRA_DRIVERS``

DATA TYPE:
    device driver entry structures

RANGE:
    Undefined or set of device driver entry structures

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_EXTRA_DRIVERS`` is defined if the application has
    device drivers it needs to include in the Device Driver Table.  This should
    be defined to the set of device driver entries that will be placed in the
    table at the *END* of the Device Driver Table.

NOTES:
    None.

.. index:: CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER:

CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
----------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER`` is defined if the application
    wishes to include the Clock Device Driver.

NOTES:
    This device driver is responsible for providing a regular interrupt which
    invokes a clock tick directive.

    If neither the Clock Driver not Benchmark Timer is enabled and the
    configuration parameter
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`` is not defined, then a
    compile time error will occur.

.. index:: CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER
------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`` is defined if the
    application wishes to include the Console Device Driver.

NOTES:
    This device driver is responsible for providing the :file:`/dev/console`
    device file.  This device is used to initialize the standard input, output,
    and error file descriptors.

    BSPs should be constructed in a manner that allows ``printk()`` to work
    properly without the need for the console driver to be configured.

    The

    * ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

    configuration options are mutually exclusive.

.. index:: CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER:

CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER
-----------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER`` is defined if the
    application wishes to include the BSP's Frame Buffer Device Driver.

NOTES:
    Most BSPs do not include support for a Frame Buffer Device Driver. This is
    because many boards do not include the required hardware.

    If this is defined and the BSP does not have this device driver, then the
    user will get a link time error for an undefined symbol.

.. index:: CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER
.. index:: /dev/null

.. _CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER:

CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER
---------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    This configuration variable is specified to enable ``/dev/null`` device driver.

NOTES:
    This device driver is supported by all BSPs.

.. index:: CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER:

CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER
--------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER`` is defined if the application
    wishes to include the Real-Time Clock Driver.

NOTES:
    Most BSPs do not include support for a real-time clock. This is because
    many boards do not include the required hardware.

    If this is defined and the BSP does not have this device driver, then the
    user will get a link time error for an undefined symbol.

.. index:: CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER
-------------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER`` is defined if the
    application wishes to include the Simple Console Device Driver.

NOTES:
    This device driver is responsible for providing the :file:`/dev/console`
    device file.  This device is used to initialize the standard input, output,
    and error file descriptors.

    This device driver reads via ``getchark()``.

    This device driver writes via ``rtems_putc()``.

    The Termios framework is not used.  There is no support to change device
    settings, e.g. baud, stop bits, parity, etc.

    The

    * ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

    configuration options are mutually exclusive.

.. index:: CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER
------------------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER`` is defined if
    the application wishes to include the Simple Task Console Device Driver.

NOTES:
    This device driver is responsible for providing the :file:`/dev/console`
    device file.  This device is used to initialize the standard input, output,
    and error file descriptors.

    This device driver reads via ``getchark()``.

    This device driver writes into a write buffer.  The count of characters
    written into the write buffer is returned.  It might be less than the
    requested count, in case the write buffer is full.  The write is
    non-blocking and may be called from interrupt context.  A dedicated task
    reads from the write buffer and outputs the characters via
    ``rtems_putc()``.  This task runs with the least important priority.  The
    write buffer size is 2047 characters and it is not configurable.

    Use ``fsync(STDOUT_FILENO)`` or ``fdatasync(STDOUT_FILENO)`` to drain the
    write buffer.

    The Termios framework is not used.  There is no support to change device
    settings, e.g.  baud, stop bits, parity, etc.

    The

    * ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

    configuration options are mutually exclusive.

.. index:: CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER:

CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER
---------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER`` is defined if the application
    wishes to include the Stub Device Driver.

NOTES:
    This device driver simply provides entry points that return successful and
    is primarily a test fixture. It is supported by all BSPs.

.. index:: CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER:

CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER
----------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER`` is defined if the application
    wishes to include the Timer Driver.  This device driver is used to
    benchmark execution times by the RTEMS Timing Test Suites.

NOTES:
    If neither the Clock Driver not Benchmark Timer is enabled and the
    configuration parameter
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`` is not defined, then a
    compile time error will occur.

.. index:: CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER:

CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER
-------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER`` is defined if the
    application wishes to include the Watchdog Driver.

NOTES:
    Most BSPs do not include support for a watchdog device driver. This is
    because many boards do not include the required hardware.

    If this is defined and the BSP does not have this device driver, then the
    user will get a link time error for an undefined symbol.

.. index:: CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER
.. index:: /dev/zero

.. _CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER:

CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER
---------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    This configuration variable is specified to enable ``/dev/zero`` device driver.

NOTES:
    This device driver is supported by all BSPs.

.. index:: CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS

.. _CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS:

CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS
------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS``

DATA TYPE:
    device driver entry structures

RANGE:
    Undefined or set of device driver entry structures

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS`` is defined if the
    application has device drivers it needs to include in the Device Driver
    Table.  This should be defined to the set of device driver entries that
    will be placed in the table at the *FRONT* of the Device Driver Table and
    initialized before any other drivers *EXCEPT* any BSP prerequisite drivers.

NOTES:
    In some cases, it is used by System On Chip BSPs to support peripheral
    buses beyond those normally found on the System On Chip. For example, this
    is used by one RTEMS system which has implemented a SPARC/ERC32 based board
    with VMEBus. The VMEBus Controller initialization is performed by a device
    driver configured via this configuration parameter.

.. index:: CONFIGURE_MAXIMUM_DRIVERS

.. _CONFIGURE_MAXIMUM_DRIVERS:

CONFIGURE_MAXIMUM_DRIVERS
-------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_DRIVERS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    This is computed by default, and is set to the number of device drivers
    configured using the ``CONFIGURE_APPLICATIONS_NEEDS_XXX_DRIVER``
    configuration parameters.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_DRIVERS`` is defined as the number of device drivers
    per node.

NOTES:
    If the application will dynamically install device drivers, then this
    configuration parameter must be larger than the number of statically
    configured device drivers. Drivers configured using the
    ``CONFIGURE_APPLICATIONS_NEEDS_XXX_DRIVER`` configuration parameters are
    statically installed.
