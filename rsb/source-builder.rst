.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment COPYRIGHT (c) 2012 - 2016.
.. comment Chris Johns <chrisj@rtems.org>

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

Why Build from Source?
----------------------

The RTEMS Source Builder is not a replacement for the binary install systems
you have with commercial operating systems or open source operating system
distributions. Those products and distributions are critically important and
are the base that allows the RSB to work. The RTEMS Source Builder sits
somewhere between you manually entering the commands to build a tool set and a
tool such as ``yum`` or ``apt-get`` to install binary packages made
specifically for your host operating system. Building manually or installing a
binary package from a remote repository are valid and real alternatives. The
RSB provides the specific service of repeatably being able to build tool sets
from source code. The process leaves you with the source code used to build
the tools and the ability to rebuilt it.

If you are developing a system or product that has a long shelf life or is used
in a critical piece of infrastructure that has a long life cycle being able to
build from source is important. It insulates the project from the fast ever
changing world of the host development machines. If your tool set is binary and
you have lost the ability to build it you have lost a degree of control and
flexibility open source gives you. Fast moving host environments are
fantastic. We have powerful multi-core computers with huge amounts of memory
and state of the art operating systems to run on them however the product or
project you are part of may need to be maintained well past the life time of
these host. Being able to build from source an important and critical part of
this process because you can move to a newer host and create an equivalent tool
set.

Building from source provides you with control over the configuration of the
package you are building. If all or the most important dependent parts are
built from source you limit the exposure to host variations. For example the
GNU C compiler (gcc) currently uses a number of 3rd party libraries internally
(gmp, mpfr, etc). If your validated compiler generating code for your target
processor is dynamically linked against the host's version of these libraries
any change in the host's configuration may effect you. The changes the host's
package management system makes may be perfectly reasonable in relation to the
distribution being managed however this may not extend to you and your
tools. Building your tools from source and controlling the specific version of
these dependent parts means you are not exposing yourself to unexpected and
often difficult to resolve problems. On the other side you need to make sure
your tools build and work with newer versions of the host operating
system. Given the stability of standards based libraries like ``libc`` and ever
improving support for standard header file locations this task is becoming
easier.

The RTEMS Source Builder is designed to be audited and incorporated into a
project's verification and validation process. If your project is developing
critical applications that needs to be traced from source to executable code in
the target, you need to also consider the tools and how to track them.

If your IT department maintains all your computers and you do not have suitable
rights to install binary packages, building from source lets you create your
own tool set that you install under your home directory. Avoiding installing
any extra packages as a super user is always helpful in maintaining a secure
computing environment.

History
-------

The RTEMS Source Builder is a stand alone tool based on another tool called the
*SpecBuilder* written by Chris Johns. The *SpecBuilder* was written around 2010
for the RTEMS project to provide Chris with a way to build tools on hosts that
did not support RPMs. At the time the RTEMS tools maintainer only supported
*spec* files and these files held all the vital configuration data needed to
create suitable tool sets. The available SRPM and *spec* files by themselves
where of little use because a suitable ``rpm`` tool was needed to use them. At
the time the available versions of ``rpm`` for a number of non-RPM hosts were
broken and randomly maintained. The solution Chris settled on was to use the
*spec* files and to write a Python based tool that parsed the *spec* file
format creating a shell script that could be run to build the package. The
approach proved successful and Chris was able to track the RPM version of the
RTEMS tools on a non-RPM host for a number of years.

The *SpecBuilder* tool did not build tools or packages unrelated to the RTEMS
Project where no suitable *spec* file was available so another tool was
needed. Rather than start again Chris decided to take the parsing code for the
*spec* file format and build a new tool called the RTEMS Source Builder.

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


