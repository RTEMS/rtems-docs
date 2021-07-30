.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 2015 On-Line Applications Research Corporation (OAR)

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

.. Generated from spec:/rtems/io/if/group-3

.. _KernelCharacterIOSupportIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/io/if/putc
.. spec:/rtems/io/if/put-char
.. spec:/rtems/io/if/putk
.. spec:/rtems/io/if/printk
.. spec:/rtems/io/if/vprintk
.. spec:/rtems/io/if/printk-printer
.. spec:/rtems/io/if/getchark

The kernel character input/output support is an extension of the
:ref:`RTEMSAPIClassicIO` to output characters to the kernel character output
device and receive characters from the kernel character input device using a
polled and non-blocking implementation.

The directives may be used to print debug and test information.  The kernel
character input/output support should work even if no Console Driver is
configured, see :ref:`CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`.  The kernel
character input and output device is provided by the :term:`BSP`. Applications
may change the device. The directives provided by the Kernel Character I/O
Support are:

* :ref:`InterfaceRtemsPutc` - Outputs the character to the kernel character
  output device.

* :ref:`InterfaceRtemsPutChar` - Puts the character using
  :ref:`InterfaceRtemsPutc`

* :ref:`InterfacePutk` - Outputs the characters of the string and a newline
  character to the kernel character output device.

* :ref:`InterfacePrintk` - Outputs the characters defined by the format string
  and the arguments to the kernel character output device.

* :ref:`InterfaceVprintk` - Outputs the characters defined by the format string
  and the variable argument list to the kernel character output device.

* :ref:`InterfaceRtemsPrintkPrinter` - Outputs the characters defined by the
  format string and the variable argument list to the kernel character output
  device.

* :ref:`InterfaceGetchark` - Tries to dequeue a character from the kernel
  character input device.
