.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBSPBuild:

Build a Board Support Package (BSP)
===================================

You installed the tool suite in your installation prefix, cloned two RTEMS
repositories and bootstrapped the RTEMS sources in the previous sections.  We
installed the tool suite in :file:`$HOME/quick-start/rtems/5` and cloned the
repositories in :file:`$HOME/quick-start/src`.  We also bootstrapped the RTEMS
sources.

You are now able to build :ref:`Board Support Packages (BSPs) <BSPs>` for all
architectures where you have an RTEMS tool suite installed.  To build
applications on top of RTEMS, you have to configure, build and install a BSP
for your target hardware.  To select a proper BSP for your target hardware
consult the :ref:`BSPs <BSPs>` chapter.  We select the `erc32` BSP.

We configure, build and install the BSP in four steps.  The first step is to
create a build directory.  It must be separate from the RTEMS source directory.
We use :file:`$HOME/quick-start/build/b-erc32`.

.. code-block:: none

    mkdir -p $HOME/quick-start/build/b-erc32

The second step is to configure the BSP.  There are various configuration
options available.  Some configuration options are BSP-specific.  Prepend the
RTEMS tool suite binary directory to your ``$PATH`` throughout the remaining
steps.

.. code-block:: none

    cd $HOME/quick-start/build/b-erc32
    export PATH=$HOME/quick-start/rtems/5/bin:"$PATH"
    $HOME/quick-start/src/rtems/configure \
        --prefix=$HOME/quick-start/rtems/5 \
        --enable-maintainer-mode \
        --target=sparc-rtems5 \
        --enable-rtemsbsp=erc32 \
        --enable-tests

This command should output something like this (omitted lines are denoted by
...):

.. code-block:: none

    checking for gmake... gmake
    checking for RTEMS Version... 5.0.0
    checking build system type... x86_64-unknown-freebsd12.0
    checking host system type... x86_64-unknown-freebsd12.0
    checking target system type... sparc-unknown-rtems5
    ...
    config.status: creating Makefile

    target architecture: sparc.
    available BSPs: erc32.
    'gmake all' will build the following BSPs: erc32.
    other BSPs can be built with 'gmake RTEMS_BSP="bsp1 bsp2 ..."'

    config.status: creating Makefile

Building the BSP is the third step.

.. code-block:: none

    cd $HOME/quick-start/build/b-erc32
    make

This command should output something like this (omitted lines are denoted by
...).  In this output the base directory :file:`$HOME/quick-start` was replaced
by ``$BASE``.

.. code-block:: none

    Configuring RTEMS_BSP=erc32
    checking for gmake... gmake
    checking build system type... x86_64-unknown-freebsd12.0
    checking host system type... sparc-unknown-rtems5
    checking rtems target cpu... sparc
    checking for a BSD-compatible install... /usr/bin/install -c
    checking whether build environment is sane... yes
    checking for sparc-rtems5-strip... sparc-rtems5-strip
    checking for a thread-safe mkdir -p... $BASE/src/rtems/c/src/../../install-sh -c -d
    checking for gawk... no
    checking for mawk... no
    checking for nawk... nawk
    checking whether gmake sets $(MAKE)... yes
    checking whether to enable maintainer-specific portions of Makefiles... yes
    checking for RTEMS_BSP... erc32
    checking whether CPU supports libposix... yes
    configure: setting up make/custom
    configure: creating make/erc32.cache
    gmake[3]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32'
    ...
    sparc-rtems5-gcc  -mcpu=cypress -O2 -g -ffunction-sections -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -B./../../lib/libbsp/sparc/erc32 -B$BASE/src/rtems/bsps/sparc/erc32/start -specs bsp_specs -qrtems -L./../../cpukit -L$BASE/src/rtems/bsps/sparc/shared/start -Wl,--wrap=printf -Wl,--wrap=puts -Wl,--wrap=putchar -Wl,--gc-sections -o spwkspace.exe spwkspace/spwkspace-init.o ./../../lib/libbsp/sparc/erc32/librtemsbsp.a ./../../cpukit/librtemscpu.a 
    gmake[5]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32/testsuites/sptests'
    gmake[4]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32/testsuites'
    gmake[3]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32'
    gmake[2]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32'
    gmake[1]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c'
    gmake[1]: Entering directory '$BASE/build/b-erc32'
    gmake[1]: Nothing to be done for 'all-am'.
    gmake[1]: Leaving directory '$BASE/build/b-erc32'

The last step is to install the BSP.

.. code-block:: none

    cd $HOME/quick-start/build/b-erc32
    make install

This command should output something like this (omitted lines are denoted by
...).  In this output the base directory :file:`$HOME/quick-start` was replaced
by ``$BASE``.

.. code-block:: none

    Making install in sparc-rtems5/c
    gmake[1]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c'
    Making install in .
    gmake[2]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c'
    gmake[3]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c'
    gmake[3]: Nothing to be done for 'install-exec-am'.
    gmake[3]: Nothing to be done for 'install-data-am'.
    gmake[3]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c'
    gmake[2]: Leaving directory '$BASE/build/b-erc32/sparc-rtems5/c'
    Making install in erc32
    gmake[2]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32'
    gmake[3]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32'
    Making install-am in .
    Making install-am in cpukit
    gmake[4]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32/cpukit'
    gmake[5]: Entering directory '$BASE/build/b-erc32/sparc-rtems5/c/erc32/cpukit'
    gmake[5]: Nothing to be done for 'install-exec-am'.
     $BASE/src/rtems/c/src/../../cpukit/../install-sh -c -d '$BASE/rtems/5/sparc-rtems5/erc32/lib/include'
    ...
    $BASE/src/rtems/make/Templates/Makefile.lib '$BASE/rtems/5/share/rtems5/make/Templates'
     $BASE/src/rtems/./install-sh -c -d '$BASE/rtems/5/make/custom'
     /usr/bin/install -c -m 644 $BASE/src/rtems/make/custom/default.cfg '$BASE/rtems/5/make/custom'
    gmake[2]: Leaving directory '$BASE/build/b-erc32'
    gmake[1]: Leaving directory '$BASE/build/b-erc32'
