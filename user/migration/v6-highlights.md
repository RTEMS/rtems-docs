.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 Gedare Bloom

.. _6_highlights:

RTEMS 6 Highlights
==================

This section describes some of the major improvements and changes in RTEMS 6.
Please refer to the release notes for more detailed updates as this is not an
exhaustive list of changes.


Chat with RTEMS Community on Discord
------------------------------------

We have established an active community on our :r:url:`discord` that has pretty
much replaced our mailing lists, although you're still more than welcome to use
those too. Hop on by and say Hi!

Contribute to RTEMS through GitLab
----------------------------------

We have upgraded our development infrastructure to use a self-hosted GitLab
instance. This has replaced both our Trac ticket system and also our use of the
:r:list:`devel` for patch submissions. Check it out at our :r:url:`devel` and
maybe review some MRs, open an Issue, or send us some code! Hit us up on the
:r:url:`discord` if you need any help. We have really seen a lot of engagement
and faster pace of development with GitLab, and we are hopeful that it allows
us to improve the pace and quality of delivering RTEMS.

Flight Readiness and Pre-Qualification
--------------------------------------

One of the major efforts during the version 6 development is what we call the
pre-qualification of RTEMS. This effort was sponsored primarily by the European
Space Agency (ESA) and included several contributors. From the RTEMS community,
the primary contributors were from embedded brains GmbH & Co. KG. The outcome
of this effort can be seen in both the high quality of the RTEMS 6 code and in
the improved documentation. Most notably is the creation of a new RTEMS Manual
for RTEMS Software Engineering to help guide RTEMS contributors and document
our community processes in a way that supports flight readiness and similar
rigorous safety-critical systems engineering efforts.

Revamping the Network Stacks
----------------------------

A major undertaking in this release cycle is the refactoring and improving of
our various network stacks. The Legacy Network stack has been pulled out of
RTEMS (cpukit/libnetworking) and now resides in the rtems-net-legacy.git
repository. This effort was led by Vijay Banerjee, and allows us to gracefully
maintain this stack without having to carry it in rtems.git. We have also
started to adopt an lwIP stack in the rtems-lwip.git repository for use with
RTEMS on lightweight targets with several contributions from community members
including Vijay, Pavel Pisa, and Kinsey Moore. Meanwhile, the rtems-libbsd.git
repository holds the high-performance networking stack we borrow from FreeBSD.
The rtems-libbsd has also undergone some major changes during this release
cycle, and we are pleased to offer networking stack versions based on FreeBSD
12 and FreeBSD 14 for use with RTEMS 6. This stack has especially been improved
by the work of embedded brains GmbH & Co. KG., OAR Corporation, and by a newer
face in our community, Aaron Nyholm. Thank you to all who are contributing to
make our networking stacks modern, performant, and secure while continuing to
support users with backwards-compatibility needs.

New Build System
----------------

Another big contribution early in the 6 development cycle was the introduction
of a `modern build system using waf <BSPBuildSystem>`. This build system has a
lot of advantages over our previous system that used configure and make. Chief
among them is the build speed! In addition to being much faster, the new system
encapsulates configuration in a more flexible and programmatic way.
Accomplishing all this resulted in many changes to the internal layout of the
source code and header files in RTEMS.

Debugging with GDB
------------------

As part of a Google Summer of Code project completed by Suraj Kumar under the
guidance of Chris Johns, we now have pretty printing integrated with gdb for
RTEMS. This capability is documented in
:ref:`Pretty Printing and GDB <PrettyPrinting>`.

