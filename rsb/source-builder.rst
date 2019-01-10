.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

RTEMS Source Builder
====================

The RTEMS Source Builder or RSB is a tool to build packages from source. It is
used by the RTEMS project to build it's compilers and OS. The RSB helps
consolidate the details you need to build a package from source in a controlled
and verifiable way. The tool is aimed at developers of software who use tool
sets for embedded development. The RSB is not limited to building tools just
for RTEMS, you can build bare metal development environments.

Embedded development typically uses cross-compiling tool chains, debuggers, and
debugging aids. Together we call these a **tool set**. The RTEMS Source Builder
is designed to fit this specific niche but is not limited to it. The RSB can be
used outside of the RTEMS project and we welcome this.

The RTEMS Source Builder is typically used to build a set of tools or a **build
set**. A **build set** is a collection of packages and a package is a specific
tool, for example gcc or gdb, or library. The RTEMS Source Builder attempts to
support any host environment that runs Python and you can build the package
on. The RSB is not some sort of magic that can take any piece of source code
and make it build. Someone at some point in time has figured out how to build
that package from source and taught this tool.

The RTEMS Source Builder has been tested on:

- ArchLinux
- CentOS
- Fedora
- Raspbian
- Ubuntu (includes XUbuntu)
- Linux Mint
- openSUSE
- FreeBSD
- NetBSD
- MacOS
- Windows

.. topic:: Setting up your Host

   :ref:`Hosts` details setting up hosts.

The RTEMS Source Builder has two types of configuration data. The first is the
*build set*. A *build set* describes a collection of packages that define a set
of tools you would use when developing software for RTEMS. For example the
basic GNU tool set is binutils, gcc, and gdb and is the typical base suite of
tools you need for an embedded cross-development type project. The second type
of configuration data is the configuration files and they define how a package
is built. Configuration files are scripts loosely based on the RPM spec file
format and they detail the steps needed to build a package. The steps are
*preparation*, *building*, and *installing*. Scripts support macros, shell
expansion, logic, includes plus many more features useful when build packages.

The RTEMS Source Builder does not interact with any host package management
systems. There is no automatic dependence checking between various packages you
build or packages and software your host system you may have installed. We
assume the build sets and configuration files you are using have been created
by developers who do. Support is provided for package config or ``pkgconfg``
type files so you can check and use standard libraries if present. If you have
a problem please ask on our :r:list:`devel`.

.. comment: TBD: The section "Installing and Tar Files" does not exist.

This documentation caters for a range of users from new to experienced RTEMS
developers who want to understand the RTEMS Source Builder. New users
who just want to build tools should follow the Quick Start section in
the User's Guide.  Users building a binary tool set for release can
read the "Installing and Tar Files". Users wanting to run and test
bleeding edge tools or packages, or wanting update or extend the RSB's
configuration can read the remaining sections.

.. topic:: Bug Reporting

   If you think you have found a problem please see :ref:`Bugs, Crashes, and
   Build Failures`.

Controlling the Tools Build
---------------------------

Build sets can be controlled via the command line to enable and disable various
features. There is no definitive list of build options that can be listed
because they are implemented with the configuration scripts. The best way to
find what is available is to grep the configuration files. for ``with`` and
``without``.

Following are currently available:

``--without-rtems``
  Do not build RTEMS when building an RTEMS build set.

``--without-cxx``
  Do not build a C++ compiler.

``--with-ada``
  Attempt to build an Ada compiler.  You need a native GNAT installed.

``--with-fortran``
  Attempt to build a Fortran compiler.

``--with-objc``
  Attempt to build a C++ compiler.


