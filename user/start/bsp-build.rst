.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBSPBuild:

Build a Board Support Package (BSP)
===================================

You installed the tool suite in your installation prefix, made ready the source
for two RTEMS source packages and if you are using a Git clone bootstrapped the
RTEMS sources in the previous sections.  We installed the tool suite in
:file:`$HOME/quick-start/rtems/5` and unpacked the source in
:file:`$HOME/quick-start/src`.

You are now able to build :ref:`Board Support Packages (BSPs) <BSPs>` for all
architectures you have an installed RTEMS tool suite.  To build applications on
top of RTEMS, you have to build and install a BSP for your target hardware.  To
select a proper BSP for your target hardware consult the :ref:`BSPs <BSPs>`
chapter.  We select the `erc32` BSP. The ``erc32`` BSP uses approximately 2.3G
bytes of disk space when the testsuite is built and 44M bytes of space when
installed.

We will first show how to build the BSP using the RSB and then we will show how
to build the same BSP `manually <QuickStartBSPBuild_Manual>`_. You only need to
use one of the listed methods to build the BSP.

In the output in this section the base directory :file:`$HOME/quick-start` was
replaced by ``$BASE``.

.. QuickStartBSPBuild_RSB:

RSB BSP Build
-------------

The RSB build of RTEMS does not use the RTEMS source we made ready. It uses the
RSB source you downloaded in a previous section. If you are using a release RSB
source archive the BSP built is the released kernel image. If you are using a
Git clone of the RSB the BSP will be version referenced in the RSB clone.

To build the BSP with all the tests run this command:

.. code-block:: none

    cd $HOME/quick-start/src/rsb/rtems
    ../source-builder/sb-set-builder --prefix=$HOME/quick-start/rtems/5 \
        --target=sparc-rtems5 --with-rtems-bsp=erc32 --with-rtems-tests=yes 5/rtems-kernel

This command should output something like this:

.. code-block:: none

    RTEMS Source Builder - Set Builder, 5.1.0
    Build Set: 5/rtems-kernel
    config: tools/rtems-kernel-5.cfg
    package: sparc-rtems5-kernel-erc32-1
    building: sparc-rtems5-kernel-erc32-1
    sizes: sparc-rtems5-kernel-erc32-1: 2.279GB (installed: 44.612MB)
    cleaning: sparc-rtems5-kernel-erc32-1
    reporting: tools/rtems-kernel-5.cfg -> sparc-rtems5-kernel-erc32-1.txt
    reporting: tools/rtems-kernel-5.cfg -> sparc-rtems5-kernel-erc32-1.xml
    installing: sparc-rtems5-kernel-erc32-1 -> $BASE/
    cleaning: sparc-rtems5-kernel-erc32-1
    Build Set: Time 0:03:09.896961

The RSB BSP build can be customised with following RSB command line options:

``--with-rtems-tests``:
    Build the test suite. If ``yes`` is provided all tests in the testsuite are
    build. If ``no`` is provided no tests are built and if ``samples`` is
    provided only the sample executables are built, e.g.
    ``--with-rtems-tests=yes``.

``--with-rtems-smp``:
    Build with SMP support. The BSP has to have SMP support or this option will
    fail with an error.

``--with-rtems-legacy-network``:
    Build the legacy network software. We recommend you use the current network
    support in the RTEMS BSP Library (libbsd) unless you need to maintain a
    legacy product. Do not use the legacy networking software for new
    developments.

``--with-rtems-bspopts``:
    Build the BSP with BSP specific options. This is an advanced option. Please
    refer to the BSP specific details in the :ref:`Board Support Packages
    (BSPs)` of this manual or the BSP source code in the RTEMS source
    directory. To supply a list of options quote then list with ``"``, e.g.
    ``--with-rtems-bspopts="BSP_POWER_DOWN_AT_FATAL_HALT=1"``

If you have built a BSP with the RSB, you can move on to
:ref:`QuickStartBSPTest`.

.. QuickStartBSPBuild_Manual:

Manual BSP Build
----------------

We manually build the BSP in four steps.  The first step is to create a build
directory.  It must be separate from the RTEMS source directory.  We use
:file:`$HOME/quick-start/build/b-erc32`.

.. code-block:: none

    mkdir -p $HOME/quick-start/build/b-erc32

The second step is to set your path. Prepend the RTEMS tool suite binary
directory to your ``$PATH`` throughout the remaining steps. Run the command:

.. code-block:: none

    export PATH=$HOME/quick-start/rtems/5/bin:"$PATH"

Check your installed tools can be found by running:

.. code-block:: none

    command -v sparc-rtems5-gcc && echo "found" || echo "not found"

The output should be:

.. code-block:: none

    found

If ``not found`` is printed the tools are not correctly installed or the path
has not been correctly set. Check the contents of the path
:file:`$HOME/quick-start/rtems/5/bin` manually and if :file:`sparc-rtems5-gcc`
is present the path is wrong. If the file cannot be found return to
:ref:`QuickStartTools` and install the tools again.

The third step is to configure the BSP.  There are various configuration
options available.  Some configuration options are BSP-specific.

.. code-block:: none

    cd $HOME/quick-start/build/b-erc32
    $HOME/quick-start/src/rtems/configure \
        --prefix=$HOME/quick-start/rtems/5 \
        --enable-maintainer-mode \
        --target=sparc-rtems5 \
        --enable-rtemsbsp=erc32 \
        --enable-tests

This command should output something like this (omitted lines are denoted by
``...``):

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

Building the BSP is the forth step.

.. code-block:: none

    cd $HOME/quick-start/build/b-erc32
    make

This command should output something like this (omitted lines are denoted by
...).

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
