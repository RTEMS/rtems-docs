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

.. Generated from spec:/acfg/if/group-devdrv

Device Driver Configuration
===========================

This section describes configuration options related to the device drivers.
Note that network device drivers are not covered by the following options.

.. Generated from spec:/acfg/if/appl-does-not-need-clock-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER

.. _CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER:

CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER
------------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then a Clock Driver may be
initialized during system initialization.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then **no** Clock Driver is
initialized during system initialization.

.. rubric:: NOTES:

This configuration parameter is intended to prevent the common user error
of using the Hello World example as the baseline for an application and
leaving out a clock tick source.

The application shall define exactly one of the following configuration options

* :ref:`CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER`,

* ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER``, or

* :ref:`CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER`,

otherwise a compile time error in the configuration file will occur.

.. Generated from spec:/acfg/if/appl-extra-drivers

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_EXTRA_DRIVERS

.. _CONFIGURE_APPLICATION_EXTRA_DRIVERS:

CONFIGURE_APPLICATION_EXTRA_DRIVERS
-----------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_EXTRA_DRIVERS``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is the empty list.

.. rubric:: DESCRIPTION:

The value of this configuration option is used to initialize the Device
Driver Table.

.. rubric:: NOTES:

The value of this configuration option is placed after the entries of other
device driver configuration options.

See :ref:`CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS` for an alternative
placement of application device driver initializers.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a list of initializers for
structures of type :c:type:`rtems_driver_address_table`.

.. Generated from spec:/acfg/if/appl-needs-ata-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_ATA_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_ATA_DRIVER:

CONFIGURE_APPLICATION_NEEDS_ATA_DRIVER
--------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_ATA_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the ATA Driver is
initialized during system initialization.

.. rubric:: NOTES:

Most BSPs do not include support for an ATA Driver.

If this option is defined and the BSP does not have this device driver, then
the user will get a link time error for an undefined symbol.

.. Generated from spec:/acfg/if/appl-needs-clock-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER:

CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Clock Driver is
initialized during system initialization.

.. rubric:: NOTES:

The Clock Driver is responsible for providing a regular interrupt
which invokes a clock tick directive.

The application shall define exactly one of the following configuration options

* ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``,

* :ref:`CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`, or

* :ref:`CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER`,

otherwise a compile time error in the configuration file will occur.

.. Generated from spec:/acfg/if/appl-needs-console-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER
------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Console Driver is
initialized during system initialization.

.. rubric:: NOTES:

The Console Driver is responsible for providing the :file:`/dev/console`
device file.  This device is used to initialize the standard input, output,
and error file descriptors.

BSPs should be constructed in a manner that allows :ref:`InterfacePrintk` to work
properly without the need for the Console Driver to be configured.

The

* ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

* :ref:`CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER`, and

* :ref:`CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER`

configuration options are mutually exclusive.

.. Generated from spec:/acfg/if/appl-needs-framebuffer-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER:

CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER
-----------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Frame Buffer Driver is
initialized during system initialization.

.. rubric:: NOTES:

Most BSPs do not include support for a Frame Buffer Driver. This is
because many boards do not include the required hardware.

If this option is defined and the BSP does not have this device driver, then
the user will get a link time error for an undefined symbol.

.. Generated from spec:/acfg/if/appl-needs-ide-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_IDE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_IDE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_IDE_DRIVER
--------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_IDE_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the IDE Driver is
initialized during system initialization.

.. rubric:: NOTES:

Most BSPs do not include support for an IDE Driver.

If this option is defined and the BSP does not have this device driver, then
the user will get a link time error for an undefined symbol.

.. Generated from spec:/acfg/if/appl-needs-null-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER
.. index:: /dev/null

.. _CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER:

CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER
---------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the :file:`/dev/null`
Driver is initialized during system initialization.

.. rubric:: NOTES:

This device driver is supported by all BSPs.

.. Generated from spec:/acfg/if/appl-needs-rtc-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER:

CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER
--------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Real-Time Clock Driver
is initialized during system initialization.

.. rubric:: NOTES:

Most BSPs do not include support for a real-time clock (RTC). This is because
many boards do not include the required hardware.

If this is defined and the BSP does not have this device driver, then the
user will get a link time error for an undefined symbol.

.. Generated from spec:/acfg/if/appl-needs-simple-console-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER
-------------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Simple Console Driver
is initialized during system initialization.

.. rubric:: NOTES:

This device driver is responsible for providing the :file:`/dev/console`
device file.  This device is used to initialize the standard input, output,
and error file descriptors.

This device driver reads via :ref:`InterfaceGetchark`.

This device driver writes via :ref:`InterfaceRtemsPutc`.

The Termios framework is not used.  There is no support to change device
settings, e.g. baud, stop bits, parity, etc.

The

* :ref:`CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`,

* ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

* :ref:`CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER`

configuration options are mutually exclusive.

.. Generated from spec:/acfg/if/appl-needs-simple-task-console-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER
------------------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Simple Task Console
Driver is initialized during system initialization.

.. rubric:: NOTES:

This device driver is responsible for providing the :file:`/dev/console`
device file.  This device is used to initialize the standard input, output,
and error file descriptors.

This device driver reads via :ref:`InterfaceGetchark`.

This device driver writes into a write buffer.  The count of characters
written into the write buffer is returned.  It might be less than the
requested count, in case the write buffer is full.  The write is
non-blocking and may be called from interrupt context.  A dedicated task
reads from the write buffer and outputs the characters via
:ref:`InterfaceRtemsPutc`.  This task runs with the least important priority.
The write buffer size is 2047 characters and it is not configurable.

Use ``fsync( STDOUT_FILENO )`` or ``fdatasync( STDOUT_FILENO )`` to drain the
write buffer.

The Termios framework is not used.  There is no support to change device
settings, e.g.  baud, stop bits, parity, etc.

The

* :ref:`CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`,

* :ref:`CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER`, and

* ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

configuration options are mutually exclusive.

.. Generated from spec:/acfg/if/appl-needs-stub-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER:

CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER
---------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Stub Driver is
initialized during system initialization.

.. rubric:: NOTES:

This device driver simply provides entry points that return successful and
is primarily a test fixture. It is supported by all BSPs.

.. Generated from spec:/acfg/if/appl-needs-timer-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER:

CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER
----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Benchmark Timer Driver is
initialized during system initialization.

.. rubric:: NOTES:

The Benchmark Timer Driver is intended for the benchmark tests of the RTEMS
Testsuite.  Applications should not use this driver.

The application shall define exactly one of the following configuration options

* :ref:`CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER`,

* :ref:`CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`, or

* ``CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER``,

otherwise a compile time error will occur.

.. Generated from spec:/acfg/if/appl-needs-watchdog-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER:

CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER
-------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Watchdog Driver is
initialized during system initialization.

.. rubric:: NOTES:

Most BSPs do not include support for a watchdog device driver. This is
because many boards do not include the required hardware.

If this is defined and the BSP does not have this device driver, then the
user will get a link time error for an undefined symbol.

.. Generated from spec:/acfg/if/appl-needs-zero-driver

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER
.. index:: /dev/zero

.. _CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER:

CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER
---------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the :file:`/dev/zero`
Driver is initialized during system initialization.

.. rubric:: NOTES:

This device driver is supported by all BSPs.

.. Generated from spec:/acfg/if/appl-prerequisite-drivers

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS

.. _CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS:

CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS
------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is the empty list.

.. rubric:: DESCRIPTION:

The value of this configuration option is used to initialize the Device
Driver Table.

.. rubric:: NOTES:

The value of this configuration option is placed after the entries defined by
:c:macro:`CONFIGURE_BSP_PREREQUISITE_DRIVERS` and before all other device driver
configuration options.

See :ref:`CONFIGURE_APPLICATION_EXTRA_DRIVERS` for an alternative placement
of application device driver initializers.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a list of initializers for
structures of type :c:type:`rtems_driver_address_table`.

.. Generated from spec:/acfg/if/ata-driver-task-priority

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_ATA_DRIVER_TASK_PRIORITY

.. _CONFIGURE_ATA_DRIVER_TASK_PRIORITY:

CONFIGURE_ATA_DRIVER_TASK_PRIORITY
----------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_ATA_DRIVER_TASK_PRIORITY``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 140.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the ATA task priority.

.. rubric:: NOTES:

This configuration option is only evaluated if the configuration option
:ref:`CONFIGURE_APPLICATION_NEEDS_ATA_DRIVER` is defined.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a valid Classic API task
priority.  The set of valid task priorities depends on the scheduler
configuration.

.. Generated from spec:/acfg/if/exception-to-signal-mapping

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_EXCEPTION_TO_SIGNAL_MAPPING

.. _CONFIGURE_EXCEPTION_TO_SIGNAL_MAPPING:

CONFIGURE_EXCEPTION_TO_SIGNAL_MAPPING
-------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_EXCEPTION_TO_SIGNAL_MAPPING``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the machine exception to
POSIX signal mapping is configured during system initialization.

.. rubric:: NOTES:

This device driver is responsible for setting up a mapping from machine
exceptions to POSIX signals so that applications may consume them and alter
task execution as necessary.

This is especially useful for applications written in Ada or C++.

.. Generated from spec:/acfg/if/max-drivers

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_DRIVERS

.. _CONFIGURE_MAXIMUM_DRIVERS:

CONFIGURE_MAXIMUM_DRIVERS
-------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_DRIVERS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

This is computed by default, and is set to the number of statically
configured device drivers configured using the following configuration
options:

* :ref:`CONFIGURE_APPLICATION_EXTRA_DRIVERS`

* :ref:`CONFIGURE_APPLICATION_NEEDS_ATA_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_IDE_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_LIBBLOCK`

* :ref:`CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER`

* :ref:`CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER`

* :ref:`CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS`

If the :ref:`CONFIGURE_DISABLE_BSP_SETTINGS` configuration option is not defined and
the :term:`BSP` provides
:c:macro:`CONFIGURE_BSP_PREREQUISITE_DRIVERS`, then the BSP-provided
prerequisite device drivers are also taken into account.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the number of device drivers.

.. rubric:: NOTES:

If the application will dynamically install device drivers, then the
configuration option value shall be larger than the number of statically
configured device drivers.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be less than or equal to
  `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

* The value of the configuration option shall be greater than or equal than the
  number of statically configured device drivers.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.
