.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2015, 2021 embedded brains GmbH & Co. KG
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

.. Generated from spec:/rtems/init/if/group

.. _InitializationManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/init/if/initialize-executive

The Initialization Manager is responsible for initializing the system.

The system initialization includes the initialization of the Board Support
Package, RTEMS, device drivers, the root filesystem, and the application. The
:ref:`RTEMSAPIClassicFatal` is responsible for the system shutdown. The
directives provided by the Initialization Manager are:

* :ref:`InterfaceRtemsInitializeExecutive` - Initializes the system and starts
  multitasking.
