.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

Dependencies
============
.. index:: Dependencies

RTEMS applications are developed using cross-development tools running on a
host computer, typically your desktop or a special build server. All RTEMS
tools and runtime libraries are built from source on your host machine. The
RTEMS Project does not maintain binary builds of the tools. This may appear be
the opposite to what you normally experience with host operating systems, and
it is, however this approach works well. RTEMS is not a host operating system
and it is not a distrbution. Providing binary packages for every possible host
operating system is to big a task for the RTEMS Project and it is not a good
use of the core developers time. Their time is better spent making RTEMS better
and faster.

Developer Computer
------------------

The rule for selecting a computer for a developer is `more is better` but we do
understand there are limits. Projects set up different configurations and what
is described here is not an approved set up, rather it is a guide. Some
projects have a suitable development machine per developer while others set up
a tightly controlled central build server. RTEMS is flexible and lets you
engineering a development environment that suites you. The basic specs are:

- Multicore processor
- 8G bytes RAM
- 256G harddisk

RTEMS makes no demands on graphics.

Host Software
-------------

A wide range of host operating systems and hardware can be used. The host
operating systems supported are:

- Linux
- FreeBSD
- NetBSD
- Apple OS X
- Windows
- Solaris

The functionality on POSIX operating such as Linux and FreeBSD is similar and
most features on Windows are supported but you are best to ask on
:r:list:`users` if you have a specific question.

Install and set up your host operating system. We recommend you maintain your
operating system by installing any updates.
