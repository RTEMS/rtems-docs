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

.. Generated from spec:/rtems/io/if/group

.. _IOManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/io/if/register-driver
.. spec:/rtems/io/if/unregister-driver
.. spec:/rtems/io/if/initialize
.. spec:/rtems/io/if/register-name
.. spec:/rtems/io/if/open
.. spec:/rtems/io/if/close
.. spec:/rtems/io/if/read
.. spec:/rtems/io/if/write
.. spec:/rtems/io/if/control

The Input/Output (I/O) Manager provides a well-defined mechanism for accessing
device drivers and a structured methodology for organizing device drivers. The
directives provided by the I/O Manager are:

* :ref:`InterfaceRtemsIoRegisterDriver` - Registers and initializes the device
  with the specified device driver address table and device major number in the
  Device Driver Table.

* :ref:`InterfaceRtemsIoUnregisterDriver` - Removes a device driver specified
  by the device major number from the Device Driver Table.

* :ref:`InterfaceRtemsIoInitialize` - Initializes the device specified by the
  device major and minor numbers.

* :ref:`InterfaceRtemsIoRegisterName` - Registers the device specified by the
  device major and minor numbers in the file system under the specified name.

* :ref:`InterfaceRtemsIoOpen` - Opens the device specified by the device major
  and minor numbers.

* :ref:`InterfaceRtemsIoClose` - Closes the device specified by the device
  major and minor numbers.

* :ref:`InterfaceRtemsIoRead` - Reads from the device specified by the device
  major and minor numbers.

* :ref:`InterfaceRtemsIoWrite` - Writes to the device specified by the device
  major and minor numbers.

* :ref:`InterfaceRtemsIoControl` - Controls the device specified by the device
  major and minor numbers.
