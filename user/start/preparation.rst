.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 Shashvat Jain
.. Copyright (C) 2019 embedded brains GmbH & Co. KG
.. Copyright (C) 2019 Sebastian Huber
.. Copyright (C) 2020 Chris Johns
.. Copyright (C) 2020 Gedare Bloom

.. _QuickStartPreparation:

Preparation
===========

You need to perform some basic preparation to get started with RTEMS
development.  You need tools from your host's operating system to build the
RTEMS tool suite from source.  The RTEMS tools you build are used to build the
Board Support Package (BSP) libraries for your target hardware from source. The
BSP libraries contain the RTEMS operating system. All RTEMS tools
and runtime libraries are built from source on your host machine. The RTEMS
Project does not maintain binary builds of the tools. This may appear to be the
opposite to what you normally experience with host operating systems, and it
is, however this approach works well. RTEMS is not a host operating system and
it is not a distrbution. Providing binary packages for every possible host
operating system is too big a task for the RTEMS Project and it is not a good
use of core developer time. Their time is better spent making RTEMS better and
faster. This is not a one-click
installation process, but there are :ref:`good reasons <WhyBuildFromSource>` to
build everything from source.
The RTEMS Project base installation sets up the tools and the RTEMS kernel for
the selected BSPs. The tools run on your host computer are used to compile,
link, and format executables so they can run on your target hardware.


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
Python development environment. The following procedure assumes you have
installed and configured your host operating system. It also assumes
you have installed any dependent packages needed when building the tools and
the kernel. Please make sure you can build native C/C++
applications on your host computer.  You must be able to build native Python C
modules as some RTEMS tools contain these modules.  Usually, you have to
install a Python development package for this.  The Python scripts of the RTEMS
Project expect on POSIX systems that a ``python`` command is available [1]_.
Please have a look at the :ref:`Host Computer <host-computer>` chapter for the
gory details.  In particular :ref:`Microsoft Windows <microsoft-windows>` users
should do this.

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

.. _QuickStartPreparation_Version:

Selecting a Version of RTEMS
----------------------------

In the examples of this manual we will often refer to a specific version of
RTEMS, which will usually be the version that accompanied the publication of
this documentation manual. That may not be the appropriate version for you to
use, for example, it may be too old (or too new) depending on what you are
trying to do.  If you're not sure what version to use, we generally recommend
using the most recent release or the development head (master), and you may
want to consult with the same version of the documentation. We hope that newer
is better.

An RTEMS *release* involves the creation of a single downloadable file,
normally a compressed tarball, that packages the source of all the repositories
in a state consistent with the time the release is created.
A release branch is a git branch pushed to the repositories named with the
numeric identifier of the branch.
A release branch release is a git tag on a release branch with
the tags pushed to the repositories.

Numbering for RTEMS versions beginning with RTEMS 5 uses a format as follows.
The master branch has the version **N.0.0** with N being the next major release
number. The first release of this series has the version number **N.1.0.** and
there is exactly one commit with this version number in the corresponding
repository. The first bugfix release (minor release) of this series will have
the version number **N.2.0**. The release branch will have the version
number **N.M.1** with **M** being the last minor release of this series.

For example:

* 5.0.0 is the version number of the development master for the 5 series.
* 5.1.0 is the first release of the 5 series.
* 5.1.1 is the version number of the 5 series release branch right after
  the 5.1.0 release until 5.2.0 is released.
* 5.2.0 is the first bugfix release of the 5 series
* 5.2.1 is the version number of the 5 series release branch right after
  the 5.2.0 release until 5.3.0 is released.
* 6.0.0 is the version number of the development master for the 6 series.

RTEMS development tools use **N** as the version number and are expected to
work with all releases and the release branch of the N series.
So to build tools for compiling RTEMS version number 5.1.0 for SPARC use
``sparc-rtems5``. Despite the number not increasing, the tools may change
within a release branch, for example the tools packaged with 5.1.1 still use
the ``sparc-rtems5`` moniker, but are likely not the same as the tools used
in version 5.1.0. This tool mismatch can be a source of confusion. Be sure to
use the toolchain that matches your release.

.. [1] The Python scripts use a shebang of ``#!/usr/bin/env python``.
