.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2015, 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/rtems/fatal/if/group

.. _FatalErrorManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/fatal/if/fatal
.. spec:/rtems/fatal/if/panic
.. spec:/rtems/fatal/if/shutdown-executive
.. spec:/rtems/fatal/if/exception-frame-print
.. spec:/rtems/fatal/if/source-text
.. spec:/rtems/fatal/if/internal-error-text
.. spec:/rtems/fatal/if/error-occurred

The Fatal Error Manager processes all fatal or irrecoverable errors and other
sources of system termination (for example after :c:func:`exit`).  Fatal errors
are identified by the fatal source and code pair. The directives provided by
the Fatal Error Manager are:

* :ref:`InterfaceRtemsFatal` - Invokes the fatal error handler.

* :ref:`InterfaceRtemsPanic` - Prints the message and invokes the fatal error
  handler.

* :ref:`InterfaceRtemsShutdownExecutive` - Invokes the fatal error handler.

* :ref:`InterfaceRtemsExceptionFramePrint` - Prints the exception frame.

* :ref:`InterfaceRtemsFatalSourceText` - Returns a descriptive text for the
  fatal source.

* :ref:`InterfaceRtemsInternalErrorText` - Returns a descriptive text for the
  internal error code.

* :ref:`InterfaceRtemsFatalErrorOccurred` - Invokes the fatal error handler.
