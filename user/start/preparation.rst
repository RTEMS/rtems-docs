.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber
.. Copyright (C) 2020 Chris Johns

.. _QuickStartPreparation:

Preparation
===========

You need to perform some basic preparation to get started with RTEMS
development.  You need tools from your host's operating system to build the
RTEMS tool suite from source.  The RTEMS tools you build are used to build the
Board Support Package (BSP) libraries for your target hardware from source. The
BSP libraries contain the RTEMS operating system.  This is not a one-click
installation process, but there are :ref:`good reasons <WhyBuildFromSource>` to
build everything from source.

During this Quick Start guide you will:

* Select a suitable place to install RTEMS.

* Select if you download all the source code before you start building RTEMS or
  the source is downloaded on demand as it is needed.  If you do not have a
  reliable internet connection we recommend you download all the source before
  starting a build.

* Build a tool suite.

* Build and test a BSP.

* Optionally  build additional packages.

Alternatively you can build a BSP as a package using the RSB. This is
covered in :ref:`QuickStartBSPPackages`

Host Computer
-------------

The *host computer* is a computer you use to develop applications.  It runs all
your tools, editors, documentation viewers, etc.  You need a native C, C++, and
Python development environment.  Please make sure you can build native C/C++
applications on your host computer.  You must be able to build native Python C
modules as some RTEMS tools contain these modules.  Usually, you have to
install a Python development package for this.  Please have a look at the
:ref:`Host Computer <host-computer>` chapter for the gory details.  In
particular :ref:`Microsoft Windows <microsoft-windows>` users should do this.

Selecting a BSP
---------------

If you are new to RTEMS and you are looking to try RTEMS then the best suited
Board Support Package (BSP) is the :ref:`SPARC ERC32 <BSP_sparc_erc32>`
(``erc32``). The SPARC ERC32 BSP has a robust simulator that runs the example
and test executables on your host computer. This Quick Start guide will build
the ``erc32`` BSP and run RTEMS tests executables in the simulator. The ERC32
BSP is a SPARC architecture BSP so the tool suite name is ``sparc-rtems5``.

If you are looking for a hardware target to run RTEMS on we recommend the
:ref:`BeagleBone Black <BSP_arm_beagleboneblack>` (``beagleboneblack``)
BSP. The BeagleBone Black support includes the RTEMS BSD Library (``libbsd``)
and networking. The BeagleBone Black BSP is an ARM architecture BSP so the tool
suite name is ``arm-rtems5``.
