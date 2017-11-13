.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _host-computer:

.. _development-host:

Host Computer
*************
.. index:: Host Computer

RTEMS applications are developed using cross-development tools running on a
development computer, more often called the host computer. These are typically
your desktop machine or a special build server. All RTEMS tools and runtime
libraries are built from source on your host machine. The RTEMS Project does
not maintain binary builds of the tools. This differs to what you normally
experience with host operating systems, and it is, however this approach works
well. RTEMS is not a host operating system and it is not a
distrbution. Deploying binary packages for every possible host operating system
is too big a task for the RTEMS Project and it is not a good use of core
developer time. Their time is better spent making RTEMS better and faster.

The RTEMS Project's aim is to give you complete freedom to decide on the
languages used in your project, which version control system, and the build
system for your application.

The rule for selecting a computer for a developer is `more is better` but we do
understand there are limits. Projects set up different configurations, some
have a development machine per developer while others set up a tightly
controlled central build server. RTEMS Ecosystem is flexible and lets you
engineer a development environment that suites you. The basic specs are:

- Multicore processor
- 8G bytes RAM
- 256G harddisk

RTEMS makes no demands on graphics.

If you are using a VM or your host computer is not a fast modern machine do not
be concerned. The tools may take longer to build than faster hardware however
building tools is something you do once. Once the tools and RTEMS is built all
your time can be spent writing and developing your application. Over an hour
can happen and for the ARM architecture and with all BSPs it can be many hours.

.. toctree::

   os
   posix
   macos
   windows
