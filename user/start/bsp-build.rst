.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH & Co. KG
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBSPBuild:

Build a Board Support Package (BSP)
===================================

You installed the tool suite in your installation prefix, made ready the source
for two RTEMS source packages and if you are using a Git clone bootstrapped the
RTEMS sources in the previous sections.  We installed the tool suite in
:file:`$HOME/quick-start/rtems/6` and unpacked the source in
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

.. _QuickStartBSPBuild_RSB:

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
        --target=sparc-rtems@rtems-ver-major@ --with-rtems-bsp=erc32 --with-rtems-tests=yes @rtems-ver-major@/rtems-kernel

This command should output something like:

.. code-block:: none

    RTEMS Source Builder - Set Builder, @rtems-ver-majminver@
    Build Set: @rtems-ver-major@/rtems-kernel
    config: tools/rtems-kernel-@rtems-ver-major@.cfg
    package: sparc-rtems@rtems-ver-major@-kernel-erc32-1
    building: sparc-rtems@rtems-ver-major@-kernel-erc32-1
    sizes: sparc-rtems@rtems-ver-major@-kernel-erc32-1: 2.279GB (installed: 44.612MB)
    cleaning: sparc-rtems@rtems-ver-major@-kernel-erc32-1
    reporting: tools/rtems-kernel-@rtems-ver-major@.cfg -> sparc-rtems@rtems-ver-major@-kernel-erc32-1.txt
    reporting: tools/rtems-kernel-@rtems-ver-major@.cfg -> sparc-rtems@rtems-ver-major@-kernel-erc32-1.xml
    installing: sparc-rtems@rtems-ver-major@-kernel-erc32-1 -> $BASE/
    cleaning: sparc-rtems@rtems-ver-major@-kernel-erc32-1
    Build Set: Time 0:03:09.896961

The RSB BSP build can be customised with following RSB command line options:

``--with-rtems-tests``:
    Build the test suite. If ``yes`` is provided all tests in the testsuite are
    build. If ``no`` is provided no tests are built and if ``samples`` is
    provided only the sample executables are built, e.g.
    ``--with-rtems-tests=yes``. The test executables are install under the BSP
    in the :file:`tests` directory and you can execute them with the
    :ref:`tester and run command <rtems-tester-command>`.

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

.. _QuickStartBSPBuild_Manual:

Manual BSP Build
----------------

We manually build the BSP in four steps. The first step is to set your path.
Prepend the RTEMS tool suite binary directory to your ``$PATH`` throughout the
remaining steps. Run the command:

.. code-block:: none

    export PATH=$HOME/quick-start/rtems/@rtems-ver-major@/bin:"$PATH"

Check your installed tools can be found by running:

.. code-block:: none

    command -v sparc-rtems@rtems-ver-major@-gcc && echo "found" || echo "not found"

The output should be:

.. code-block:: none

    found

If ``not found`` is printed the tools are not correctly installed or the path
has not been correctly set. Check the contents of the path
:file:`$HOME/quick-start/rtems/@rtems-ver-major@/bin` manually and if
:file:`sparc-rtems@rtems-ver-major@-gcc` is present the path is wrong. If the
file cannot be found return to :ref:`QuickStartTools` and install the tools
again.

The second step is to configure the BSP.  There are various BSP build
configuration options available.  Some options are BSP-specific.  Each section
in the INI-style configuration file ``config.ini`` instructs the build system to
build a particular BSP variant (`sparc/erc32` in our case).  We enable the build
of the tests with the ``BUILD_TESTS = True`` option and use default values for
everything else.  For detailed information about the BSP build system, see
:ref:`BSPBuildSystem`.

.. code-block:: none

    cd $HOME/quick-start/src/rtems
    echo "[sparc/erc32]" > config.ini
    echo "BUILD_TESTS = True" >> config.ini
    ./waf configure --prefix=$HOME/quick-start/rtems/@rtems-ver-major@

The first invocation of ``./waf`` needs a bit of time (e.g. 10 seconds) since an
internal cache file is populated.  This command should output something like
this.  In this output the base directory :file:`$HOME/quick-start` was replaced
by ``$BASE``.

.. code-block:: none

    Setting top to                           : $BASE/quick-start/src/rtems
    Setting out to                           : $BASE/quick-start/src/rtems/build
    Configure board support package (BSP)    : sparc/erc32
    Checking for program 'sparc-rtems@rtems-ver-major@-gcc'  : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-gcc
    Checking for program 'sparc-rtems@rtems-ver-major@-g++'  : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-g++
    Checking for program 'sparc-rtems@rtems-ver-major@-ar'   : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-ar
    Checking for program 'sparc-rtems@rtems-ver-major@-ld'   : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-ld
    Checking for program 'ar'                : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-ar
    Checking for program 'g++, c++'          : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-g++
    Checking for program 'ar'                : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-ar
    Checking for program 'gas, gcc'          : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-gcc
    Checking for program 'ar'                : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-ar
    Checking for program 'gcc, cc'           : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-gcc
    Checking for program 'ar'                : $BASE/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-ar
    Checking for asm flags '-MMD'            : yes
    Checking for c flags '-MMD'              : yes
    Checking for cxx flags '-MMD'            : yes
    Checking for program 'rtems-bin2c'       : $BASE/quick-start/rtems/@rtems-ver-major@/bin/rtems-bin2c
    Checking for program 'gzip'              : /usr/bin/gzip
    Checking for program 'rtems-ld'          : $BASE/quick-start/rtems/@rtems-ver-major@/bin/rtems-ld
    Checking for program 'rtems-syms'        : $BASE/quick-start/rtems/@rtems-ver-major@/bin/rtems-syms
    Checking for program 'xz'                : $BASE/anaconda3/bin/xz
    'configure' finished successfully (0.414s)

Building the BSP is the third step.

.. code-block:: none

    cd $HOME/quick-start/src/rtems
    ./waf

This command should output something like this (omitted lines are denoted by
...).

.. code-block:: none

    Waf: Entering directory `$BASE/quick-start/src/rtems/build'
    Waf: Leaving directory `$BASE/quick-start/src/rtems/build'
    'build' finished successfully (0.085s)
    Waf: Entering directory `$BASE/quick-start/src/rtems/build/sparc/erc32'
    [   1/4093] Compiling bsps/shared/dev/serial/mc68681_reg2.c
    [   2/4093] Compiling bsps/shared/dev/rtc/mc146818a_ioreg.c
    [   3/4093] Compiling bsps/shared/dev/flash/am29lv160.c
        ...
    [4093/4093] Processing link: build/sparc/erc32/testsuites/libtests/dl01/dl01-tar.o build/sparc/erc32/testsuites/libtests/dl01/init.o build/sparc/erc32/testsuites/libtests/dl01/dl-load.o build/sparc/erc32/testsuites/libtests/dl01/dl01-sym.o -> build/sparc/erc32/testsuites/libtests/dl01.exe
    Waf: Leaving directory `$BASE/quick-start/src/rtems/build/sparc/erc32'
    'build_sparc/erc32' finished successfully (2m14.111s)

The last step is to install the BSP.

.. code-block:: none

    cd $HOME/quick-start/src/rtems
    ./waf install

This command should output something like this (omitted lines are denoted by
...).  In this output the base directory :file:`$HOME/quick-start` was replaced
by ``$BASE``.

.. code-block:: none

    Waf: Entering directory `$BASE/quick-start/src/rtems/build'
    Waf: Leaving directory `$BASE/quick-start/src/rtems/build'
    'install' finished successfully (0.081s)
    Waf: Entering directory `$BASE/quick-start/src/rtems/build/sparc/erc32'
    + install $BASE/quick-start/rtems/@rtems-ver-major@/sparc-rtems@rtems-ver-major@/erc32/lib/include/libchip/am29lv16.h (from bsps/include/libchip/am29lv1.h)
    + install $BASE/quick-start/rtems/@rtems-ver-major@/sparc-rtems@rtems-ver-major@/erc32/lib/include/libchip/mc146818a.h (from bsps/include/libchip/mc146818a.h)
    + install $BASE/quick-start/rtems/@rtems-ver-major@/sparc-rtems@rtems-ver-major@/erc32/lib/include/libchip/mc68681.h (from bsps/include/libchip/mc68681.h))
    ...
    + install $BASE/quick-start/rtems/@rtems-ver-major@/sparc-rtems@rtems-ver-major@/erc32/lib/include/rtems/score/watchdogticks.h (from cpukit/include/rtems/score/watchdogticks.h)
    + install $BASE/quick-start/rtems/@rtems-ver-major@/sparc-rtems@rtems-ver-major@/erc32/lib/include/rtems/score/wkspace.h (from cpukit/include/rtems/score/wkspace.h)
    + install $BASE/quick-start/rtems/@rtems-ver-major@/sparc-rtems@rtems-ver-major@/erc32/lib/include/rtems/score/wkspacedata.h (from cpukit/include/rtems/score/wkspacedata.h)
    Waf: Leaving directory `$BASE/quick-start/src/rtems/build/sparc/erc32'
    'install_sparc/erc32' finished successfully (1.834s))
