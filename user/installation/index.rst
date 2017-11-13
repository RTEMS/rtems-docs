.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. index:: Installation
.. _installation:

Installation
************

This section details how to set up and install the RTEMS Ecosystem. You will
create a set of tools and an RTEMS kernel for your selected Board Support
Package (BSP).

You will be asked to follow a few simple steps and when you have finished you
will have a development environment set up you can use to build applications
for RTEMS. You will have also created a development environment you and a team
can adapt for a project of any size and complexity.

.. index:: Tools

RTEMS applications are developed using cross-development tools running on a
development computer, more commonlly referred to as the host computer. These
are typically your desktop machine or a special build server. All RTEMS tools
and runtime libraries are built from source on your host machine. The RTEMS
Project does not maintain binary builds of the tools. This may appear to be the
opposite to what you normally experience with host operating systems, and it
is, however this approach works well. RTEMS is not a host operating system and
it is not a distrbution. Providing binary packages for every possible host
operating system is too big a task for the RTEMS Project and it is not a good
use of core developer time. Their time is better spent making RTEMS better and
faster.

The RTEMS Project base installation set ups the tools and the RTEMS kernel for
the selected BSPs. The tools run on your host computer are used to compile,
link, and format executables so they can run on your target hardware.

The RTEMS Project supports two set ups, release and developer
environments. Release installations create the tools and kernel in a single
pass ready for you to use. The tools and kernel are stable and only bug fixes
are added creating new dot point releases. The developer set up tracks the Git
repositories for the tools and kernel.

.. comment: code block warning is in kernel.rst

.. toctree::

   prefixes-sandboxing
   releases
   developer
   kernel
