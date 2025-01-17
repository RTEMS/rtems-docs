.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

.. highlight:: shell

.. _RSB:

Source Builder
**************

The RTEMS Source Builder or RSB is a tool to build packages from source. The
RTEMS project uses it to build it's compilers, tools, kernel and 3rd party
packages. The tool is aimed at developers of software for RTEMS who use tool
sets for embedded development.

The RSB consolidates the details you need to build a package from source in a
controlled and verifiable way. The RSB is not limited to building tools for
RTEMS, you can build bare metal development environments.

.. comment: TBD: The section "Installing and Tar Files" does not exist.

The RSB section of this manual caters for a range of users from new to
experienced RTEMS developers who want to understand the RTEMS Source
Builder. New users who just want to build tools should follow :ref:`QuickStart`
in this manual. Users building a binary tool set for release can read the
"Installing and Tar Files". Users wanting to run and test bleeding edge tools
or packages, or wanting update or extend the RSB's configuration can read the
remaining sections.

Embedded development typically uses cross-compiling tool chains, debuggers, and
debugging aids. Together we call these a **tool set**. The RTEMS Source Builder
is designed to fit this specific niche but is not limited to it. The RSB can be
used outside of the RTEMS project and we welcome this.

The RTEMS Source Builder is typically used to build a set of packages or a
**build set**. A **build set** is a collection of packages and a package is a
specific tool, for example GCC, GDB, or library of code and a single **build
set** can build them all in a single command. The RTEMS Source Builder
attempts to support any host environment that runs Python and you can build
the package on. The RSB is not some sort of magic that can take any piece of
source code and make it build. Someone at some point in time has figured out
how to build that package from source and taught this tool.

.. sidebar:: Setting up your Host

   See :ref:`QuickStartPreparation` for details on setting up hosts.

The RTEMS Source Builder is known to work on:

- ArchLinux
- CentOS
- Fedora
- Raspbian
- Ubuntu (includes XUbuntu)
- Linux Mint
- openSUSE
- FreeBSD
- NetBSD
- Solaris
- MacOS
- Windows

The RTEMS Source Builder has two types of configuration data. The first is the
*build set*. A *build set* describes a collection of packages that define a set
of tools you would use when developing software for RTEMS. For example the
basic GNU tool set is Binutils, GCC, and GDB and is the typical base suite of
tools you need for an embedded cross-development type project. The second type
of configuration data are the configuration files and they define how a package
is built. Configuration files are scripts loosely based on the RPM spec file
format and they detail the steps needed to build a package. The steps are
*preparation*, *building*, and *installing*. Scripts support macros, shell
expansion, logic, includes plus many more features useful when build packages.

The RTEMS Source Builder does not interact with any host package management
systems. There is no automatic dependence checking between various packages you
build or packages and software your host system you may have installed. We
assume the build sets and configuration files you are using have been created
by developers who do. Support is provided for package config or ``pkgconfig``
type files so you can check and use standard libraries if present.

The RSB is not intended to be run with administrator privileges, and it is
known to break in certain builds if run as the *root* or *superuser* account.
If you need to install with elevated privileges, you should stage your build
into a tar file using `--bset-tar-file --no-install` and then unpack it to the
destination, as described in :ref:`RSBDeployment`.

If you have a problem please ask on our :r:list:`devel`.

.. topic:: Bug Reporting

   If you think you have found a problem please see :ref:`Bugs, Crashes, and
   Build Failures`.

.. toctree::

   why-build-from-source.rst
   project-sets
   cross-canadian-cross
   third-party-packages
   configuration
   commands
   deployment
   bug-reporting
   history
