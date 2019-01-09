.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017 Chris Johns <chrisj@rtems.org>

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
in RTEMS. Developers can work in the generic areas such as scheduling, file
systems or the shell, or users can become developers adding a new BSP, or even
a new port to a new architecture. A common approach for all these developers is
to select a BSP and to work with that BSP. Developers working in a generic
areas of RTEMS tend to select a BSP that has good simulator support with good
debugging such as QEMU, while developers of a new BSP or a new port tend to
work on target hardware. This type of development does not check the other
architectures, BSP, and build options and a change may change the number of
warnings or introduce build errors. It is important for the RTEMS project to
have developers fix these issues before pushing the changes to the master
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

#. Build options

#. BSP Options

The BSP Builder provides a template of builds to try and reduce the possble
combinations to something manageable. It is not realistic to build all possible
combinations on a single machine in reasonible time.

The RTEMS BSP Builder specifies it builds in terms of:

#. Profiles

#. Architectures

#. BSPs

#. Builds

The RTEMS BSP Builder builds are created by user options that vary these parameters.

Profiles
^^^^^^^^

A profile is named collection of architectures and board support packages. When
the RTEMS BSP Builder is asked to build a specific profile it builds the BSPs
in the specified architectures.

The default configuration provides standard profiles for :ref:`Tiers`. They are:

#. ``tier-1`` (default)

#. ``tier-2``

#. ``tier-3``

#. ``tier-4``

The ``everythings`` profile allows all BSPs to be built.

Builds
^^^^^^

A build is a list of builds or a build set and each BSP in a profile,
architecture of BSP is built with.

The default configuration provides standard builds based around the commonly
varied configure options.

The builds are:

#. ``all`` (default)

#. ``tests``

#. ``standard``, also ``no-tests``

#. ``debug``

#. ``profiling``

#. ``smp``

#. ``smp-debug``

#. ``posix``

#. ``no-posix``

#. ``posix-debug``

#. ``posix-profiling``

#. ``network``

#. ``no-network``

#. ``network-debug``

#. ``smp-network``

#. ``smp-network-debug``

All Build
~~~~~~~~~

The ``all`` build is:

- ``debug``
- ``profiling``
- ``smp``
- ``smp-debug``
- ``posix``
- ``no-posix``
- ``posix-debug``
- ``posix-profiling``
- ``network``
- ``no-network``
- ``network-debug``
- ``smp-network``
- ``smp-network-debug``

A build maps to specific configuration options. The mappings are:

 +-----------------------+-----------------------------------------------------+
 | ``debug``             | ``config:base``, ``config:debug``                   |
 +-----------------------+-----------------------------------------------------+
 | ``profiling``         | ``config:base``, ``config:profiling``               |
 +-----------------------+-----------------------------------------------------+
 | ``smp``               | ``config:base``, ``config:smp``                     |
 +-----------------------+-----------------------------------------------------+
 | ``smp-debug``         | ``config:base``, ``config:smp``, ``config:debug``   |
 +-----------------------+-----------------------------------------------------+
 | ``posix``             | ``config:base``, ``config:posix``                   |
 +-----------------------+-----------------------------------------------------+
 | ``no-posix``          | ``config:base``, ``config:no-posix``                |
 +-----------------------+-----------------------------------------------------+
 | ``posix-debug``       | ``config:base``, ``config:posix``, ``config:debug`` |
 +-----------------------+-----------------------------------------------------+
 | ``posix-profiling``   | ``config:base``, ``config:posix``,                  |
 |                       | ``config:profiling``                                |
 +-----------------------+-----------------------------------------------------+
 | ``network``           | ``config:base``, ``config:network``                 |
 +-----------------------+-----------------------------------------------------+
 | ``no-network``        | ``config:base``, ``config:no-network``              |
 +-----------------------+-----------------------------------------------------+
 | ``network-debug``     | ``config:base``, ``config:network``,                |
 |                       | ``config:debug``                                    |
 +-----------------------+-----------------------------------------------------+
 | ``smp-network``       | ``config:base``, ``config:smp``, ``config:network`` |
 +-----------------------+-----------------------------------------------------+
 | ``smp-network-debug`` | ``config:base``, ``config:smp``,                    |
 |                       | ``config:network``, ``config:debug``                |
 +-----------------------+-----------------------------------------------------+

Build Configurations
--------------------

Build configurations are ``configure`` options. These are mapped to the various
builds. The configurations are:

 +------------------+----------------------------------------------------------+
 | ``base``         | ``--target=@ARCH@-rtems@RTEMS_VERSION@``                 |
 |                  | ``--enable-rtemsbsp=@BSP@``                              |
 |                  | ``--prefix=@PREFIX@``                                    |
 +------------------+----------------------------------------------------------+
 | ``tests``        | ``--enable-tests``                                       |
 +------------------+----------------------------------------------------------+
 | ``debug``        | ``--enable-debug``                                       |
 +------------------+----------------------------------------------------------+
 | ``no-debug``     | ``--disable-debug``                                      |
 +------------------+----------------------------------------------------------+
 | ``profiling``    | ``--enable-profiling``                                   |
 +------------------+----------------------------------------------------------+
 | ``no-profiling`` | ``--disable-profiling``                                  |
 +------------------+----------------------------------------------------------+
 | ``smp``          | ``--enable-smp``                                         |
 +------------------+----------------------------------------------------------+
 | ``no-smp``       | ``--disable-smp``                                        |
 +------------------+----------------------------------------------------------+
 | ``posix``        | ``--enable-posix``                                       |
 +------------------+----------------------------------------------------------+
 | ``no-posix``     | ``--disable-posix``                                      |
 +------------------+----------------------------------------------------------+
 | ``network``      | ``--enable-networking``                                  |
 +------------------+----------------------------------------------------------+
 | ``no-network``   | ``--disable-networking``                                 |
 +------------------+----------------------------------------------------------+

Performance
-----------

The RTEMS BSP Builder is designed to extract the maximum performance from your
hardware when building RTEMS. The RTEMS build system is based on ``autoconf``,
``automake`` and GNU ``make``. Building consists of two phases:

#. Configuring

#. Building

The Configuring phase and the start of the Build phase runs autoconf's
``configure`` scripts. These execute as a single linear process and are not run
in parallel even if you specify more than one job to ``make``. The configure
part of a build is approximately 30% of the total time and higher if building
the tests. Performing a single build at a time will not fully utilized a
multi-core machine because of the large amount of time the system is idle.

The RTEMS BSP Builder can run more than one build in parallel. A build can also
request ``make`` run its build with more than one job. The ``--jobs`` option
lets a user specify the number of build jobs to run at once and the number of
``make`` jobs each build runs with. Together these options can fully load a
system and can overload a machine.

Tuning the best ratio of buld jobs to make jobs requires running some builds
and observing the system's performance. If the build job count is too low the
system will show idle periods and if you have too many build jobs with too many
make jobs the system will have too many processing running and the operating
system's overheads in administting too processes at once lowers the overall
performance.

A fast eight core machine where the operating system shows sixteen cores can
support a build option of ``--jobs=5/10``. The machine will be fully loaded the
average build time is around 18 seconds.

The type of build selected effects the optimum jobs option. For example
building the tests changes the percentage of time spent configuring copmared to
bulding so the make jobs parameter becomes a dominant factor. Lowering the make
jobs value avoids having too many active processes running at once.

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

   The path to build the BSP and place the build output. This can be any path
   and away from your current directory or the RTEMS source code. The storage
   does not need to be fast like an SSD.

.. option:: --log

   The log file.

.. option:: --config-report

   Print a configuration report and exit.

.. option:: --warnings-report

   Create a warnings report once all builds have finished.

.. option:: --stop-on-error

   Stop the build on an error. The default is to build all the builds for a
   profile.

.. option:: --no-clean

   Do not remove the build once finished. This option lets you inspect the
   built output. The amount of output can be large and disks can fill with this
   option.

.. option:: --profiles

   Build the comma separated list of profiles. The default is ``tier-1``.

.. option:: --arch

   A comma separated list of architecures to build using the selected build.

.. option:: --bsp

   A comma separated list of BSPs to build where a BSP is of the format
   ``arch/bsp`` using the selected build.

.. option:: --build

   The build to be used. The default is ``all``. See ``--config-report`` for a
   list of vlaid builds.

.. option:: --jobs

   The jobs options where the format is ``build-jobs/make-jobs``. The default
   is ``1/num-cores`` where ``num-cores`` is the operating system reported
   number of cores.

.. option:: --dry-run

   Do not do the actual builds just show what would be built.

Examples
^^^^^^^^

The following is a *tier-1* profile build of *all* on a machine where all the
source and tools are located on fast SSD disks and the build happens on a
spinning disk mounted under `build`. The build uses a development source tree
that is bootstrapped and ready to build. The source can have local patches that
need to be regression tested:

.. code-block:: shell

  $ /opt/rtems/5/bin/rtems-bsp-builder --build-path=/build/rtems \
            --rtems-tools=/opt/work/rtems/5 \
            --rtems=/opt/work/chris/rtems/kernel/rtems.git \
            --profiles=tier-1 \
            --jobs=5/10
  RTEMS Tools Project - RTEMS Kernel BSP Builder, 5.not_released
  Profile(s): tier-1
  Cleaning: bsp-builds
  [  1/655] arm/altcycv_devkit (debug)                         Start
  [  1/655] arm/altcycv_devkit (debug)                         Creating: bsp-builds/arm/altcycv_devkit.debug
  [  2/655] arm/altcycv_devkit (no-posix)                      Start
  [  2/655] arm/altcycv_devkit (no-posix)                      Creating: bsp-builds/arm/altcycv_devkit.no-posix
  [  3/655] arm/altcycv_devkit (posix)                         Start
  [  1/655] arm/altcycv_devkit (debug)                         Configuring
  [  3/655] arm/altcycv_devkit (posix)                         Creating: bsp-builds/arm/altcycv_devkit.posix
  [  2/655] arm/altcycv_devkit (no-posix)                      Configuring
  [  4/655] arm/altcycv_devkit (posix-debug)                   Start
  [  1/655] arm/altcycv_devkit (debug)                         Building
  [  3/655] arm/altcycv_devkit (posix)                         Configuring
  [  4/655] arm/altcycv_devkit (posix-debug)                   Creating: bsp-builds/arm/altcycv_devkit.posix-debug
  [  2/655] arm/altcycv_devkit (no-posix)                      Building
  [  5/655] arm/altcycv_devkit (posix-profiling)               Start
  [  4/655] arm/altcycv_devkit (posix-debug)                   Configuring
  [  3/655] arm/altcycv_devkit (posix)                         Building
   ....
  [654/655] sparc/ngmp (posix-profiling)                       PASS
  [654/655] sparc/ngmp (posix-profiling)                       Warnings:0  exes:0  objs:0  libs:0
  [654/655] sparc/ngmp (posix-profiling)                       Finished (duration:0:01:49.002189)
  [654/655] sparc/ngmp (posix-profiling)                       Status: Pass:  655  Fail:    0 (configure:0 build:0)
  [655/655] sparc/ngmp (profiling)                             PASS
  [655/655] sparc/ngmp (profiling)                             Warnings:0  exes:0  objs:0  libs:0
  [655/655] sparc/ngmp (profiling)                             Finished (duration:0:01:260.002098)
  [655/655] sparc/ngmp (profiling)                             Status: Pass:  655  Fail:    0 (configure:0 build:0)
  [651/655] sparc/ngmp (no-posix)                              Cleaning: bsp-builds/sparc/ngmp.no-posix
  [652/655] sparc/ngmp (posix)                                 Cleaning: bsp-builds/sparc/ngmp.posix
  [653/655] sparc/ngmp (posix-debug)                           Cleaning: bsp-builds/sparc/ngmp.posix-debug
  [654/655] sparc/ngmp (posix-profiling)                       Cleaning: bsp-builds/sparc/ngmp.posix-profiling
  [655/655] sparc/ngmp (profiling)                             Cleaning: bsp-builds/sparc/ngmp.profiling
  Total: Warnings:31689  exes:6291  objs:793839  libs:37897
  Failures:
   No failure(s)
  Average BSP Build Time: 0:00:18.165000
  Total Time 3:41:48.075006
  Passes: 655   Failures: 0

To build a couple of BSPs you are interested in with tests:

.. code-block:: shell

  $ /opt/rtems/5/bin/rtems-bsp-builder --build-path=/build/rtems \
            --rtems-tools=/opt/work/rtems/5 \
            --rtems=/opt/work/chris/rtems/kernel/rtems.git \
            ----log=lpc-log \
            --bsp=arm/lpc2362,arm/lpc23xx_tli800 \
            --build=tests \
            --jobs=5/12
  RTEMS Tools Project - RTEMS Kernel BSP Builder, 5.not_released
  BSPS(s): arm/lpc2362, arm/lpc23xx_tli800
  Cleaning: bsp-builds
  [1/2] arm/lpc2362 (tests)        Start
  [1/2] arm/lpc2362 (tests)        Creating: bsp-builds/arm/lpc2362.tests
  [2/2] arm/lpc23xx_tli800 (tests) Start
  [2/2] arm/lpc23xx_tli800 (tests) Creating: bsp-builds/arm/lpc23xx_tli800.tests
  [1/2] arm/lpc2362 (tests)        Configuring
  [2/2] arm/lpc23xx_tli800 (tests) Configuring
  [1/2] arm/lpc2362 (tests)        Building
  [2/2] arm/lpc23xx_tli800 (tests) Building
  [1/2] arm/lpc2362 (tests)        FAIL
  [1/2] arm/lpc2362 (tests)        Warnings:74  exes:58  objs:1645  libs:74
  [1/2] arm/lpc2362 (tests)        Finished (duration:0:01:31.708252)
  [1/2] arm/lpc2362 (tests)        Status: Pass:    0  Fail:    2 (configure:0 build:2)
  [2/2] arm/lpc23xx_tli800 (tests) FAIL
  [2/2] arm/lpc23xx_tli800 (tests) Warnings:74  exes:51  objs:1632  libs:74
  [2/2] arm/lpc23xx_tli800 (tests) Finished (duration:0:01:31.747582)
  [2/2] arm/lpc23xx_tli800 (tests) Status: Pass:    0  Fail:    2 (configure:0 build:2)
  [1/2] arm/lpc2362 (tests)        Cleaning: bsp-builds/arm/lpc2362.tests
  [2/2] arm/lpc23xx_tli800 (tests) Cleaning: bsp-builds/arm/lpc23xx_tli800.tests
  Total: Warnings:74  exes:109  objs:3277  libs:148
  Failures:
     1 tests arm/lpc2362 build:
        configure: /opt/work/chris/rtems/kernel/rtems.git/configure --target\
        =arm-rtems5 --enable-rtemsbsp=lpc2362 --prefix=/opt/rtems/5\
        --enable-tests
       error: ld/collect2:0 error: math.exe section '.rodata' will not fit
              in region 'ROM_INT'; region 'ROM_INT' overflowed by 7284 bytes

     2 tests arm/lpc23xx_tli800 build:
        configure: /opt/work/chris/rtems/kernel/rtems.git/configure --target\
        =arm-rtems5 --enable-rtemsbsp=lpc23xx_tli800\
        --prefix=/opt/rtems/5 --enable-tests
       error: ld/collect2:0 error: math.exe section '.text' will not fit in
              region 'ROM_INT'; region 'ROM_INT' overflowed by 13972 bytes

  Average BSP Build Time: 0:00:46.658257
  Total Time 0:01:33.316514
  Passes: 0   Failures: 2

The summary report printed shows both BSP builds failed with the error detail
shown. In this case both are linker related errors where the test do not fit
into the target's available resources.
