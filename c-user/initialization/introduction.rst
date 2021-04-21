.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Introduction
============

The Initialization Manager is responsible for initializing the Board Support
Package, RTEMS, device drivers, the root filesystem and the application.  The
:ref:`Fatal Error Manager <fatal_error_manager>` is responsible for the system
shutdown.

The Initialization Manager provides only one directive:

- :ref:`rtems_initialize_executive`
