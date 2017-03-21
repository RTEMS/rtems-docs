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

   Prefix to pass to configure when building a BSP.

.. option:: --rtems-tools

   The path the RTEMS tools such as the C compiler. This option avoid polluting
   your path. This path is to the tool's prefix used to build and install the
   tools and not exact path to an executable.

.. option:: --rtems

   The path the RTEMS source tree to build.

.. option:: --build-path
0
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
   built output. The amount of output can be large and disks can fill with this
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

Examples
^^^^^^^^

The following is a *tier-1* profile build of *all* on a machine where all the
source and tools are located on fast SSD disks and the build happens on a
spinning disk mounted under `build`. The build uses a development source tree
that is configured and ready to build. The source can have local patches that
need to be regression tested:

.. code-block:: shell

  $ /opt/rtems/4.12/bin/rtems-bsp-builder --build-path=/build/rtems \
            --rtems-tools=/opt/work/rtems/4.12 \
	    --rtems=/opt/work/chris/rtems/kernel/rtems.git \
	    --profiles=tier-1
  RTEMS Tools Project - RTEMS Kernel BSP Builder, 4.12 (31e22e337cf3 modified)
  ]] Profile: tier-1
  ] BSP: arm/altcycv_devkit
  . Creating: build/arm/altcycv_devkit
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/debug
  ^ Time 0:03:45.450099
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/no-posix
  ^ Time 0:03:39.598817
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/posix
  ^ Time 0:03:40.242016
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/posix-debug
  ^ Time 0:03:40.325694
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/posix-profiling
  ^ Time 0:03:39.999044
  . Configuring: posix-smp
  . Building: posix-smp
  + Pass: posix-smp: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/posix-smp
  ^ Time 0:03:39.462674
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/profiling
  ^ Time 0:03:39.860434
  . Configuring: smp
  . Building: smp
  + Pass: smp: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/smp
  ^ Time 0:03:39.928132
  . Configuring: smp-debug
  . Building: smp-debug
  + Pass: smp-debug: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit/smp-debug
  ^ Time 0:03:40.414716
  ^ BSP Time 0:33:09.399355
  ] BSP: arm/altcycv_devkit_smp
  . Creating: build/arm/altcycv_devkit_smp
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/debug
  ^ Time 0:03:39.891703
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/no-posix
  ^ Time 0:03:40.730781
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/posix
  ^ Time 0:03:39.966778
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/posix-debug
  ^ Time 0:03:39.871038
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/posix-profiling
  ^ Time 0:03:39.626562
  . Configuring: posix-smp
  . Building: posix-smp
  + Pass: posix-smp: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/posix-smp
  ^ Time 0:04:00.433920
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/profiling
  ^ Time 0:04:07.316248
  . Configuring: smp
  . Building: smp
  + Pass: smp: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/smp
  ^ Time 0:04:02.147503
  . Configuring: smp-debug
  . Building: smp-debug
  + Pass: smp-debug: warnings:99  exes:560  objs:2760  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/altcycv_devkit_smp/smp-debug
  ^ Time 0:03:46.626848
  ^ BSP Time 0:34:20.797975
  ] BSP: arm/xilinx_zynq_zc702
  . Creating: build/arm/xilinx_zynq_zc702
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/debug
  ^ Time 0:04:48.221615
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/no-posix
  ^ Time 0:03:38.480575
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/posix
  ^ Time 0:03:39.993491
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/posix-debug
  ^ Time 0:03:42.712069
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/posix-profiling
  ^ Time 0:03:40.859795
  . Configuring: posix-smp
  . Building: posix-smp
  + Pass: posix-smp: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/posix-smp
  ^ Time 0:03:37.047568
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/profiling
  ^ Time 0:03:37.822230
  . Configuring: smp
  . Building: smp
  + Pass: smp: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/smp
  ^ Time 0:03:36.921624
  . Configuring: smp-debug
  . Building: smp-debug
  + Pass: smp-debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc702/smp-debug
  ^ Time 0:03:37.072002
  ^ BSP Time 0:34:03.305717
  ] BSP: arm/xilinx_zynq_zc706
  . Creating: build/arm/xilinx_zynq_zc706
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/debug
  ^ Time 0:03:41.005831
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/no-posix
  ^ Time 0:03:36.625042
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/posix
  ^ Time 0:03:36.811815
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/posix-debug
  ^ Time 0:03:36.997970
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/posix-profiling
  ^ Time 0:03:37.051871
  . Configuring: posix-smp
  . Building: posix-smp
  + Pass: posix-smp: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/posix-smp
  ^ Time 0:03:37.525090
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/profiling
  ^ Time 0:03:37.398436
  . Configuring: smp
  . Building: smp
  + Pass: smp: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/smp
  ^ Time 0:03:36.341299
  . Configuring: smp-debug
  . Building: smp-debug
  + Pass: smp-debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zc706/smp-debug
  ^ Time 0:03:37.991431
  ^ BSP Time 0:32:41.878632
  ] BSP: arm/xilinx_zynq_zedboard
  . Creating: build/arm/xilinx_zynq_zedboard
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/debug
  ^ Time 0:03:36.807900
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/no-posix
  ^ Time 0:03:37.808461
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/posix
  ^ Time 0:03:36.583274
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/posix-debug
  ^ Time 0:03:37.305808
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/posix-profiling
  ^ Time 0:03:38.172598
  . Configuring: posix-smp
  . Building: posix-smp
  + Pass: posix-smp: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/posix-smp
  ^ Time 0:03:36.840879
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/profiling
  ^ Time 0:03:37.557138
  . Configuring: smp
  . Building: smp
  + Pass: smp: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/smp
  ^ Time 0:03:37.215842
  . Configuring: smp-debug
  . Building: smp-debug
  + Pass: smp-debug: warnings:99  exes:560  objs:2749  libs:76
    Status: configure:0 build:0
  . Cleaning: build/arm/xilinx_zynq_zedboard/smp-debug
  ^ Time 0:03:36.580128
  ^ BSP Time 0:32:38.996825
  ] BSP: i386/pc686
  . Creating: build/i386/pc686
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  . Cleaning: build/i386/pc686/debug
  ^ Time 0:03:30.095820
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  . Cleaning: build/i386/pc686/no-posix
  ^ Time 0:03:29.235921
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  . Cleaning: build/i386/pc686/posix
  ^ Time 0:03:30.413376
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  . Cleaning: build/i386/pc686/posix-debug
  ^ Time 0:03:29.512518
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  + Pass: posix-profiling: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  . Cleaning: build/i386/pc686/posix-profiling
  ^ Time 0:03:30.870472
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:118  exes:560  objs:2770  libs:76
    Status: configure:0 build:0
  . Cleaning: build/i386/pc686/profiling
  ^ Time 0:03:30.768413
  ^ BSP Time 0:21:03.174394
  ] BSP: sparc/erc32
  . Creating: build/sparc/erc32
  . Configuring: debug
  . Building: debug
  + Pass: debug: warnings:96  exes:559  objs:2769  libs:77
    Status: configure:0 build:0
  . Cleaning: build/sparc/erc32/debug
  ^ Time 0:03:10.233967
  . Configuring: no-posix
  . Building: no-posix
  + Pass: no-posix: warnings:96  exes:559  objs:2769  libs:77
    Status: configure:0 build:0
  . Cleaning: build/sparc/erc32/no-posix
  ^ Time 0:03:11.151673
  . Configuring: posix
  . Building: posix
  + Pass: posix: warnings:96  exes:559  objs:2769  libs:77
    Status: configure:0 build:0
  . Cleaning: build/sparc/erc32/posix
  ^ Time 0:03:10.069584
  . Configuring: posix-debug
  . Building: posix-debug
  + Pass: posix-debug: warnings:96  exes:559  objs:2769  libs:77
    Status: configure:0 build:0
  . Cleaning: build/sparc/erc32/posix-debug
  ^ Time 0:03:10.661856
  . Configuring: posix-profiling
  . Building: posix-profiling
  + Pass: posix-profiling: warnings:96  exes:559  objs:2769  libs:77
    Status: configure:0 build:0
  . Cleaning: build/sparc/erc32/posix-profiling
  ^ Time 0:03:11.079471
  . Configuring: profiling
  . Building: profiling
  + Pass: profiling: warnings:96  exes:559  objs:2769  libs:77
    Status: configure:0 build:0
  . Cleaning: build/sparc/erc32/profiling
  ^ Time 0:03:10.630353
  ^ BSP Time 0:19:06.556621
  ^ Profile Time 3:27:04.111801
    warnings:5739  exes:559  objs:2769  libs:77
  * Passes: 57   Failures: 0
