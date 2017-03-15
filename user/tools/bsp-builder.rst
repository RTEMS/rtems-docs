.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2017 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

RTEMS BSP Builder
=================

.. index:: Tools, rtems-bsp-builder

The RTEMS BSP Builder is an RTEMS developer tool to build RTEMS in ways users
do not to test changes to RTEMS. RTEMS has large number of architectures, board
support packages and configuration options. This tool provides a standard way
to test a change.

Developer Workflows
-------------------

There are a number of RTEMS developers each with a different view or expertise
in RTEMS. Developer can work in the generic areas such as scheduling, file
systems or the shell, then there are users turned developers adding a new BSP,
or even a new port to a new architecture. A common approach for all these
developers is to select a BSP and to work with that BSP. Developers working in
a generic areas of RTEMS tend to select a BSP that has good simulator support
with good debugging such as QEMU, while developers of a new BSP or a new port
tend to work on target hardware. This type of development does not check the
other architectures, BSP, and build options and a change may change the number
of warnings or introduce build errors. It is important for the RTEMS project to
have developers fix these issues before pushing the changes to master
repository to avoid breaking the code for other developers. It is best for a
developer to resolve as many issues as they work on changes because comming
back to a problem often proves difficult.

The RTEMS BSP Builder forms part of a developers workflow where patches are
tested before being pushed to the repository.

Build Characteristics
---------------------

Build characteristic are the various parts of a build that can varied changing
what is built. RTEMS can vary builds based on:

#. Architecture

#. Board Support Package (BSP)

#. Build Configuration options

#. BSP Options

The BSP Builder provides a template of build variation to try and reduce the
possble combinations to something manageable. It is not realistic to build all
possible combinations on a single machine in reasonible time.

The RTEMS BSP Builder specifies it builds in terms of:

#. Profiles

#. Builds

The RTEMS BSP Builder will build a list of builds for a profile of board
support packages.

Profiles
^^^^^^^^

A profile is named collection of architectures and board support packages. When
the RTEMS BSP Builder is asked to build a specific profile it builds the BSPs
in the specified architectures.

The default configuration provides standard profiles based on
:ref:`Tiers`. They are:

#. ``tier-1`` (default)

#. ``tier-2``

#. ``tier-3``

#. ``tier-4``

Builds
^^^^^^

A build is a list of builds and each BSP in a profiles is built using each
build in the builds list.

The default configuration provides standard builds based around the commonly
varied configure options.

The builds are:

#. ``all`` (default)

#. ``basic``

A ``basic`` build is the ``standard`` or default set configure options.

The ``all`` build is:

 +-----------------------+-----------------------------------------------------+
 | Label                 | Configure Options                                   |
 +-----------------------+-----------------------------------------------------+
 | ``debug``             | ``--enable-debug``                                  |
 +-----------------------+-----------------------------------------------------+
 | ``profiling``         | ``--enable-profiling``                              |
 +-----------------------+-----------------------------------------------------+
 | ``smp``               | ``--enable-sm``                                     |
 +-----------------------+-----------------------------------------------------+
 | ``smp-debug``         | ``--enable-smp --enable-debug``                     |
 +-----------------------+-----------------------------------------------------+
 | ``posix``             | ``--enable-posix``                                  |
 +-----------------------+-----------------------------------------------------+
 | ``no-posix``          | ``--disable-posix``                                 |
 +-----------------------+-----------------------------------------------------+
 | ``posix-debug``       | ``--enable-posix --enable-debug``                   |
 +-----------------------+-----------------------------------------------------+
 | ``posix-profiling``   | ``--enable-posix --enable-profiling``               |
 +-----------------------+-----------------------------------------------------+
 | ``posix-smp``         | ``--enable-posix --enable-smp``                     |
 +-----------------------+-----------------------------------------------------+
 | ``network``           | ``--enable-networking``                             |
 +-----------------------+-----------------------------------------------------+
 | ``no-network``        | ``--disable-networking``                            |
 +-----------------------+-----------------------------------------------------+
 | ``network-debug``     | ``--disable-networking``                            |
 +-----------------------+-----------------------------------------------------+
 | ``network-debug``     | ``--enable-debug --enable-networking``              |
 +-----------------------+-----------------------------------------------------+
 | ``smp-network``       | ``--enable-smp --enable-networking``                |
 +-----------------------+-----------------------------------------------------+
 | ``smp-network-debug`` | ``--enable-smp --enable-debug --enable-networking`` |
 +-----------------------+-----------------------------------------------------+

Command
-------

:program:`rtems-bsp-builder` [options]

.. option:: -?

   Display a compact help.

.. option:: -h, --help

   Display the full help.

.. option:: --prefix

   Prefix to pass to configure then building a BSP.

.. option:: --rtems-tools

   The path the RTEMS tools such as the C compiler. This option avoid polluting
   your path.

.. option:: --rtems

   The path the RTEMS source tree to build.

.. option:: --build-path

   The path to build the BSP and place the build output. This can be any path
   and away from your current directory or the RTEMS source code. The storage
   does not need to be fast like an SSD.

.. option:: --log

   The log file.

.. option:: --stop-on-error

   Stop the build on an error. The default is to build all the builds for a
   profile.

.. option:: --no-clean

   Do not remove the build once finished. This option lets you inspect the
   built output. The output of output can be large and disks can fill with this
   option.

.. option:: --profiles

   Build the list of profiles. The default is ``tier-1``.

.. option:: --build

   The build to be used. The default is ``all``.

.. option:: --arch

   Specify an architecure for a BSP to build instead of using a profile.

.. option:: --bsp

   The a specific BSP to build instead of using a profile.

.. option:: --dry-run

   Do not do the actual builds just show what would be built.
