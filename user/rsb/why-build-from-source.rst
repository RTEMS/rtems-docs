.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

Why Build from Source?
======================

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
the tools and the ability to rebuild it.

If you are developing a system or product that has a long shelf life or is used
in a critical piece of infrastructure that has a long life cycle being able to
build from source is important. It insulates the project from the fast ever
changing world of the host development machines. If your tool set is binary and
you have lost the ability to build it you have lost a degree of control and
flexibility open source gives you. Fast moving host environments are
fantastic. We have powerful multi-core computers with huge amounts of memory
and state of the art operating systems your development uses however the
product or project you are part of may need to be maintained well past the life
time of these host. Being able to build from source is an important and
critical part of this process because you can move to a newer host and create
an equivalent tool set.

Building from source provides you with control over the configuration of the
package you are building. If all or the most important dependent parts are
built from source you limit the exposure to host variations. For example the
GNU Compiler Collection (GCC) currently uses a number of third-party libraries
internally (GMP, ISL, MPC, MPFR, etc.). If your validated compiler generating
code for your target
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
