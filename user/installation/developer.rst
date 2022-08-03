.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _developer:
.. _development-version:
.. _unstable:

Developer (Unstable)
====================
.. index:: Git

RTEMS provides open access to it's development processes. We call this the
developer set up.  The project encourages all users to inspect, review, comment
and contribute to the code base. The processes described here are the same
processes the core development team use when developing and maintaining RTEMS.

.. warning::

   The development version is not for use in production and it can break from
   time to time.

Please read :ref:`development-host` before continuing. The following procedure
assumes you have installed and configured your host operating system. It also
assumes you have installed any dependent packages needed when building the
tools and the kernel.

You need to select a location to build and install the RTEMS Tool chain and
RTEMS. Make sure there is plenty of disk space and a fast disk is
recommended. Our procedure will document building and installing the tools in a
home directory called :file:`development/rtems`. Using a home directory means
you can do this without needing to be root. You can also use
:file:`/opt/rtems/build` if you have access to that path.

The location used to install the tools and kernel is called the `prefix`. It is
best to have a `prefix` for each different version of RTEMS you are using. If
you are using RTEMS 5 in production it is not a good idea to install a
development version of 6 over the top. A separate `prefix` for each version
avoids this.

The RTEMS tool chain changes less often than the RTEMS kernel. One method of
working with development releases is to have a separate `prefix` for the RTEMS
tools and a different one for the RTEMS kernel. You can then update each
without interacting with the other. You can also have a number of RTEMS
versions available to test with.

.. sidebar:: *Downloading the source*

  You need an internet connection to download the source. The downloaded source
  is cached locally and the RSB checksums it. If you run a build again the
  download output will be missing. Using the RSB from git will download the
  source from the upstream project's home site and this could be `http`, `ftp`,
  or `git`.

.. _posix-host-tools-chain:
.. _macos-host-tools-chain:

POSIX and OS X Host Tools Chain
-------------------------------

This procedure will build a SPARC tool chain.

Clone the RTEMS Source Builder (RSB) repository:

.. code-block:: none

  $ cd
  $ mkdir -p development/rtems
  $ cd development/rtems
  $ git clone git://git.rtems.org/rtems-source-builder.git rsb
  Cloning into 'rsb'...
  remote: Counting objects: 5837, done.
  remote: Compressing objects: 100% (2304/2304), done.
  remote: Total 5837 (delta 4014), reused 5056 (delta 3494)
  Receiving objects: 100% (5837/5837), 2.48 MiB | 292.00 KiB/s, done.
  Resolving deltas: 100% (4014/4014), done.
  Checking connectivity... done.

Check all the host packages you need are present. Current libraries are not
checked and this includes checking for the python development libraries GDB
requires:

.. code-block:: none

  $ cd rsb
  $ ./source-builder/sb-check
  RTEMS Source Builder - Check, @rtems-ver-major@ (089327b5dcf9)
  Environment is ok

If you are unsure how to specify the build set for the architecture you wish to
build, just ask the tool:

.. code-block:: none

    $ ../source-builder/sb-set-builder --list-bsets   <1>
    RTEMS Source Builder - Set Builder, 6 (7d80719f7472)
    Examining: config
    Examining: ../source-builder/config     <2>
    Examining: ../bare/config
        6/rtems-aarch64.bset
        6/rtems-all.bset                    <3>
        6/rtems-arm.bset                    <4>
        6/rtems-base.bset
        6/rtems-bfin.bset
        6/rtems-default.bset
        6/rtems-i386.bset
        6/rtems-kernel.bset
        6/rtems-libbsd.bset
        6/rtems-llvm.bset
        6/rtems-lm32.bset
        6/rtems-m68k.bset
        6/rtems-microblaze.bset
        6/rtems-mips.bset
        6/rtems-moxie.bset
        6/rtems-net-legacy.bset
        6/rtems-nios2.bset
        6/rtems-or1k.bset
        6/rtems-packages.bset
        6/rtems-powerpc.bset
        6/rtems-riscv.bset
        6/rtems-sh.bset
        6/rtems-sparc.bset
        6/rtems-sparc64.bset
        6/rtems-tools.bset
        6/rtems-v850.bset
        6/rtems-x86_64.bset
        7/rtems-aarch64.bset
        7/rtems-all.bset
        7/rtems-arm.bset
        7/rtems-base.bset
        7/rtems-bfin.bset
        7/rtems-default.bset
        7/rtems-i386.bset
        7/rtems-lm32.bset
        7/rtems-m68k.bset
        7/rtems-microblaze.bset
        7/rtems-mips.bset
        7/rtems-moxie.bset
        7/rtems-nios2.bset
        7/rtems-or1k.bset
        7/rtems-powerpc.bset
        7/rtems-riscv.bset
        7/rtems-sh.bset
        7/rtems-sparc.bset
        7/rtems-sparc64.bset
        7/rtems-v850.bset
        7/rtems-x86_64.bset
        bsps/atsamv.bset
        bsps/beagleboneblack.bset
        bsps/erc32.bset
        bsps/gr712rc.bset
        bsps/gr740.bset
        bsps/imx7.bset
        bsps/pc.bset
        bsps/qoriq_e500.bset
        bsps/qoriq_e6500_32.bset
        bsps/qoriq_e6500_64.bset
        bsps/raspberrypi2.bset
        bsps/xilinx_zynq_zc702.bset
        bsps/xilinx_zynq_zc706.bset
        bsps/xilinx_zynq_zedboard.bset
        databases/sqlite.bset
        devel/autotools-base.bset
        devel/autotools-internal.bset
        devel/autotools.bset
        devel/capstone.bset
        devel/dtc.bset
        devel/libtool.bset
        devel/libusb.bset
        devel/or1ksim.bset
        devel/qemu-couverture.bset
        devel/qemu-xilinx.bset
        devel/qemu.bset
        devel/sis.bset
        devel/spike.bset
        devel/swig.bset
        ftp/curl.bset
        gnu-tools-4.6.bset
        gnu-tools-4.8.2.bset
        graphics/freetype2.bset
        graphics/graphics-all.bset
        graphics/libjpeg.bset
        graphics/libpng.bset
        graphics/libtiff.bset
        graphics/microwindows.bset
        graphics/nxlib.bset
        graphics/t1lib.bset
        lang/gcc491.bset
        net-mgmt/net-snmp.bset
        net/lwip.bset
        net/ntp.bset

.. topic:: Items:

  1. Only option required is ``--list-bsets``

  2. The paths inspected. See :ref:`Configuration`.

  3. A build set to build all RTEMS @rtems-ver-major@ supported architectures.

  4. The build set for the ARM architecture on RTEMS @rtems-ver-major@.

Build a tool chain for the SPARC architecture. We are using the SPARC
architecture because GDB has a good simulator that lets us run and
test the samples RTEMS builds by default. The development version is
one more than ``@rtems-ver-major@` and is on the ``master`` branch:

.. _windows-tool-chain:

Windows Host Tool Chain
-----------------------
.. index:: Microsoft Windows Installation

This section details how you create an RTEMS development environment on
Windows. The installation documented here is on `Windows 7 64bit
Professional`. Building on `Windows 10` has been reported as working.

Please see :ref:`microsoft-windows` before continuing.

.. note::

   If the RSB reports ``error: no hosts defaults found; please add`` you have
   probably opened an MSYS2 32bit Shell. Close all 32bit Shell windows and open
   the MSYS2 64bit Shell.

RTEMS Windows Tools
^^^^^^^^^^^^^^^^^^^

Create a workspace for RTEMS using the following shell command:

.. sidebar:: *Creating Tool Archives*

  Add ``--bset-tar-file`` to the ``sb-set-builder`` command line to create
  tar files of the built package set.

.. code-block:: none

   ~
  $ mkdir -p /c/opt/rtems

The ``/c`` path is an internal MSYS2 mount point of the ``C:`` drive. The
command creates the RTEMS work space on the ``C:`` drive. If you wish to use
another drive please subsitute ``/c`` with your drive letter.

We build and install all RTEMS packages under the `prefix` we just
created. Change to that directory and get a copy of the RSB:

.. code-block:: none

   ~
  $ cd /c/opt/rtems
   /c/opt/rtems
  $ git clone git://git.rtems.org/rtems-source-builder.git rsb
  Cloning into 'rsb'...
  remote: Counting objects: 5716, done.
  remote: Compressing objects: 100% (2183/2183), done.
  remote: Total 5716 (delta 3919), reused 5071 (delta 3494)
  Receiving objects: 100% (5716/5716), 2.46 MiB | 656.00 KiB/s, done.
  Resolving deltas: 100% (3919/3919), done.
  Checking connectivity... done.
  Checking out files: 100% (630/630), done.
   /c/opt/rtems
  $ cd rsb

We are building RTEMS 4.11 tools so select the *4.11* branch:

.. code-block:: none

   /c/opt/rtems/rsb
  $ git checkout 4.11
  Branch 4.11 set up to track remote branch 4.11 from origin.
  Switched to a new branch '4.11'
   /c/opt/rtems/rsb
  $

Check the RSB has a valid environment:

.. code-block:: none

   /c/opt/rtems/rsb
  $ cd rtems
   /c/opt/rtems/rsb/rtems
  $ ../source-builder/sb-check
  RTEMS Source Builder - Check, 4.11 (01ac76f2f90f)
  Environment is ok
   /c/opt/rtems/rsb/rtems
  $

To build a set of RTEMS tools for the Intel ``i386`` architecture. The build
runs a single job rather than a job per CPU in your machine and will take a
long time so please be patient. The RSB creates a log file containing all the
build output and it will be changing size. The RSB command to build ``i386``
tools is:

.. code-block:: none

   /c/opt/rtems/rsb/rtems
  $ ../source-builder/sb-set-builder --prefix=/c/opt/rtems/4.11 \
                                     --jobs=none 4.11/rtems-i386
  RTEMS Source Builder - Set Builder, 4.11 (01ac76f2f90f)
  Build Set: 4.11/rtems-i386
  Build Set: 4.11/rtems-autotools.bset
  Build Set: 4.11/rtems-autotools-internal.bset
  config: tools/rtems-autoconf-2.69-1.cfg
  package: autoconf-2.69-x86_64-w64-mingw32-1
  Creating source directory: sources
  download: ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz -> sources/autoconf-2.69.tar.gz
  downloading: sources/autoconf-2.69.tar.gz - 1.8MB of 1.8MB (100%)
   building: autoconf-2.69-x86_64-w64-mingw32-1
  config: tools/rtems-automake-1.12.6-1.cfg
  package: automake-1.12.6-x86_64-w64-mingw32-1
  download: ftp://ftp.gnu.org/gnu/automake/automake-1.12.6.tar.gz -> sources/automake-1.12.6.tar.gz
  downloading: sources/automake-1.12.6.tar.gz - 2.0MB of 2.0MB (100%)
   building: automake-1.12.6-x86_64-w64-mingw32-1
  cleaning: autoconf-2.69-x86_64-w64-mingw32-1
  cleaning: automake-1.12.6-x86_64-w64-mingw32-1
  Build Set: Time 0:00:42.515625
  Build Set: 4.11/rtems-autotools-base.bset
  config: tools/rtems-autoconf-2.69-1.cfg
  package: autoconf-2.69-x86_64-w64-mingw32-1
  building: autoconf-2.69-x86_64-w64-mingw32-1
  reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-w64-mingw32-1.xml
  config: tools/rtems-automake-1.12.6-1.cfg
  package: automake-1.12.6-x86_64-w64-mingw32-1
  building: automake-1.12.6-x86_64-w64-mingw32-1
  reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-w64-mingw32-1.xml
  tarball: tar/rtems-4.11-autotools-x86_64-w64-mingw32-1.tar.bz2
  installing: autoconf-2.69-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: automake-1.12.6-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  cleaning: autoconf-2.69-x86_64-w64-mingw32-1
  cleaning: automake-1.12.6-x86_64-w64-mingw32-1
  Build Set: Time 0:00:37.718750
  Build Set: Time 0:01:20.234375
  config: devel/expat-2.1.0-1.cfg
  package: expat-2.1.0-x86_64-w64-mingw32-1
  download: http://downloads.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz -> sources/expat-2.1.0.tar.gz
   redirect: http://iweb.dl.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz
  downloading: sources/expat-2.1.0.tar.gz - 549.4kB of 549.4kB (100%)
  building: expat-2.1.0-x86_64-w64-mingw32-1
  reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-w64-mingw32-1.txt
  reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-w64-mingw32-1.xml
  config: tools/rtems-binutils-2.24-1.cfg
  package: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1
  download: ftp://ftp.gnu.org/gnu/binutils/binutils-2.24.tar.bz2 -> sources/binutils-2.24.tar.bz2
  downloading: sources/binutils-2.24.tar.bz2 - 21.7MB of 21.7MB (100%)
  building: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1
  reporting: tools/rtems-binutils-2.24-1.cfg -> i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-binutils-2.24-1.cfg -> i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1.xml
  config: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg
  package: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1
  download: ftp://ftp.gnu.org/gnu/gcc/gcc-4.9.3/gcc-4.9.3.tar.bz2 -> sources/gcc-4.9.3.tar.bz2
  downloading: sources/gcc-4.9.3.tar.bz2 - 85.8MB of 85.8MB (100%)
  download: ftp://sourceware.org/pub/newlib/newlib-2.2.0.20150423.tar.gz -> sources/newlib-2.2.0.20150423.tar.gz
  downloading: sources/newlib-2.2.0.20150423.tar.gz - 16.7MB of 16.7MB (100%)
  download: http://www.mpfr.org/mpfr-3.0.1/mpfr-3.0.1.tar.bz2 -> sources/mpfr-3.0.1.tar.bz2
  downloading: sources/mpfr-3.0.1.tar.bz2 - 1.1MB of 1.1MB (100%)
  download: http://www.multiprecision.org/mpc/download/mpc-0.8.2.tar.gz -> sources/mpc-0.8.2.tar.gz
  downloading: sources/mpc-0.8.2.tar.gz - 535.5kB of 535.5kB (100%)
  download: ftp://ftp.gnu.org/gnu/gmp/gmp-5.0.5.tar.bz2 -> sources/gmp-5.0.5.tar.bz2
  downloading: sources/gmp-5.0.5.tar.bz2 - 2.0MB of 2.0MB (100%)
  building: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1
  reporting: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg ->
  i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg ->
  i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1.xml
  config: tools/rtems-gdb-7.9-1.cfg
  package: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1
  download: http://ftp.gnu.org/gnu/gdb/gdb-7.9.tar.xz -> sources/gdb-7.9.tar.xz
  downloading: sources/gdb-7.9.tar.xz - 17.0MB of 17.0MB (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.11/gdb/gdb-sim-arange-inline.diff -> patches/gdb-sim-arange-inline.diff
  downloading: patches/gdb-sim-arange-inline.diff - 761.0 bytes of 761.0 bytes (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.11/gdb/gdb-sim-cgen-inline.diff -> patches/gdb-sim-cgen-inline.diff
  downloading: patches/gdb-sim-cgen-inline.diff - 706.0 bytes of 706.0 bytes (100%)
  building: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1
  reporting: tools/rtems-gdb-7.9-1.cfg ->
  i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1.txt
  reporting: tools/rtems-gdb-7.9-1.cfg ->
  i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1.xml
  config: tools/rtems-tools-4.11-1.cfg
  package: rtems-tools-4.11-1
  Creating source directory: sources/git
  git: clone: git://git.rtems.org/rtems-tools.git -> sources/git/rtems-tools.git
  git: reset: git://git.rtems.org/rtems-tools.git
  git: fetch: git://git.rtems.org/rtems-tools.git -> sources/git/rtems-tools.git
  git: checkout: git://git.rtems.org/rtems-tools.git => 4.11
  git: pull: git://git.rtems.org/rtems-tools.git
  building: rtems-tools-4.11-1
  reporting: tools/rtems-tools-4.11-1.cfg -> rtems-tools-4.11-1.txt
  reporting: tools/rtems-tools-4.11-1.cfg -> rtems-tools-4.11-1.xml
  config: tools/rtems-kernel-4.11.cfg
  installing: expat-2.1.0-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1 -> C:\opt\rtems\4.11
  installing: rtems-tools-4.11-1 -> C:\opt\rtems\4.11
  cleaning: expat-2.1.0-x86_64-w64-mingw32-1
  cleaning: i386-rtems4.11-binutils-2.24-x86_64-w64-mingw32-1
  cleaning: i386-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-w64-mingw32-1
  cleaning: i386-rtems4.11-gdb-7.9-x86_64-w64-mingw32-1
  cleaning: rtems-tools-4.11-1
  Build Set: Time 1:32:58.972919
   /c/opt/rtems/rsb/rtems
  $

.. _rtems-kernel-install:

Building the Kernel
^^^^^^^^^^^^^^^^^^^

We can now build the RTEMS kernel using the RTEMS tools we have just
built. First we need to set the path to the tools:

.. code-block:: none

   /c
  $ cd /c/opt/rtems
   /c/opt/rtems
  $ export PATH=/c/opt/rtems/4.11/bin:$PATH
   /c/opt/rtems
  $

We currently build RTEMS from the git release branch for 4.11:

.. code-block:: none

   /c/opt/rtems
  $ mkdir kernel
   /c/opt/rtems
  $ cd kernel
   /c/opt/rtems/kernel
  $ git clone git://git.rtems.org/rtems.git rtems
  Cloning into 'rtems'...
  remote: Counting objects: 482766, done.
  remote: Compressing objects: 100% (88781/88781), done.
  remote: Total 482766 (delta 389610), reused 475155 (delta 383437)
  Receiving objects: 100% (482766/482766), 69.77 MiB | 697.00 KiB/s, done.
  Resolving deltas: 100% (389610/389610), done.
  Checking connectivity... done.
  Checking out files: 100% (10626/10626), done.
   /c/opt/rtems/kernel
  $ cd rtems
   /c/opt/rtems/kernel/rtems
  $ git checkout 4.11
  Checking out files: 100% (2553/2553), done.
  Branch 4.11 set up to track remote branch 4.11 from origin.
  Switched to a new branch '4.11'
   /c/opt/rtems/kernel
  $

The kernel code cloned from git needs to be `bootstrapped`. Bootstrapping
creates ``autoconf`` and ``automake`` generated files. To bootstrap we first
clean away any files, then generate the pre-install header file lists and
finally we generate the ``autoconf`` and ``automake`` files using the RSB's
bootstrap tool. First we clean any generated files that exist:

.. code-block:: none

   /c/opt/rtems/kernel/rtems
  $ ./bootstrap -c
  removing automake generated Makefile.in files
  removing configure files
  removing aclocal.m4 files

Then we generate the pre-install header file automake make files:

.. code-block:: none

   /c/opt/rtems/kernel/rtems
  $ ./bootstrap -p
  Generating ./c/src/ada/preinstall.am
  Generating ./c/src/lib/libbsp/arm/altera-cyclone-v/preinstall.am
  Generating ./c/src/lib/libbsp/arm/atsam/preinstall.am
  Generating ./c/src/lib/libbsp/arm/beagle/preinstall.am
  Generating ./c/src/lib/libbsp/arm/csb336/preinstall.am
  Generating ./c/src/lib/libbsp/arm/csb337/preinstall.am
  Generating ./c/src/lib/libbsp/arm/edb7312/preinstall.am
    .......
  Generating ./cpukit/score/cpu/mips/preinstall.am
  Generating ./cpukit/score/cpu/moxie/preinstall.am
  Generating ./cpukit/score/cpu/nios2/preinstall.am
  Generating ./cpukit/score/cpu/no_cpu/preinstall.am
  Generating ./cpukit/score/cpu/or1k/preinstall.am
  Generating ./cpukit/score/cpu/powerpc/preinstall.am
  Generating ./cpukit/score/cpu/sh/preinstall.am
  Generating ./cpukit/score/cpu/sparc/preinstall.am
  Generating ./cpukit/score/cpu/sparc64/preinstall.am
  Generating ./cpukit/score/cpu/v850/preinstall.am
  Generating ./cpukit/score/preinstall.am
  Generating ./cpukit/telnetd/preinstall.am
  Generating ./cpukit/wrapup/preinstall.am
  Generating ./cpukit/zlib/preinstall.am
   /c/opt/rtems/kernel/rtems

Finally we run the parallel ``bootstrap`` command:

.. code-block:: none

  $ ./rtems-bootstrap
  RTEMS Bootstrap, 4.11 (76188ee494dd)
    1/139: autoreconf: configure.ac
    2/139: autoreconf: c/configure.ac
    3/139: autoreconf: c/src/configure.ac
    4/139: autoreconf: c/src/ada-tests/configure.ac
    5/139: autoreconf: c/src/lib/libbsp/arm/configure.ac
    6/139: autoreconf: c/src/lib/libbsp/arm/altera-cyclone-v/configure.ac
    7/139: autoreconf: c/src/lib/libbsp/arm/atsam/configure.ac
    8/139: autoreconf: c/src/lib/libbsp/arm/beagle/configure.ac
    9/139: autoreconf: c/src/lib/libbsp/arm/csb336/configure.ac
   10/139: autoreconf: c/src/lib/libbsp/arm/csb337/configure.ac
   11/139: autoreconf: c/src/lib/libbsp/arm/edb7312/configure.ac
    .......
  129/139: autoreconf: testsuites/samples/configure.ac
  130/139: autoreconf: testsuites/smptests/configure.ac
  131/139: autoreconf: testsuites/sptests/configure.ac
  132/139: autoreconf: testsuites/tmtests/configure.ac
  133/139: autoreconf: testsuites/tools/configure.ac
  134/139: autoreconf: testsuites/tools/generic/configure.ac
  135/139: autoreconf: tools/build/configure.ac
  136/139: autoreconf: tools/cpu/configure.ac
  137/139: autoreconf: tools/cpu/generic/configure.ac
  138/139: autoreconf: tools/cpu/nios2/configure.ac
  139/139: autoreconf: tools/cpu/sh/configure.ac
  Bootstrap time: 0:20:38.759766
   /c/opt/rtems/kernel/rtems
  $

We will build the RTEMS kernel for the ``i386`` target and the ``pc686``
BSP. You can check the available BSPs by running the ``rtems-bsps`` command
found in the top directory of the RTEMS kernel source. We build the Board
Support Package (BSP) outside the kernel source tree:

.. code-block:: none

   /c/opt/rtems/kernel/rtems
  $ cd ..
   /c/opt/rtems/kernel
  $ mkdir pc686
   /c/opt/rtems/kernel
  $ cd pc686
   /c/opt/rtems/kernel/pc686
  $

Configure the RTEMS kernel to build ``pc686`` BSP for the ``i386`` target with
networking disabled, We will build the external libBSD stack later:

.. code-block:: none

   /c/opt/rtems/kernel/pc686
  $ /c/opt/rtems/kernel/rtems/configure --prefix=/c/opt/rtems/4.11 \
         --target=i386-rtems4.11 --disable-networking --enable-rtemsbsp=pc686
  checking for gmake... no
  checking for make... make
  checking for RTEMS Version... 4.11.99.0
  checking build system type... x86_64-pc-mingw64
  checking host system type... x86_64-pc-mingw64
  checking target system type... i386-pc-rtems4.11
  checking for a BSD-compatible install... /usr/bin/install -c
  checking whether build environment is sane... yes
  checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
  checking for gawk... gawk
  checking whether make sets $(MAKE)... yes
  checking whether to enable maintainer-specific portions of Makefiles... no
  checking that generated files are newer than configure... done
  configure: creating ./config.status
  configure: configuring in ./tools/build
    .......
  checking whether make sets $(MAKE)... yes
  checking whether to enable maintainer-specific portions of Makefiles... no
  checking that generated files are newer than configure... done
  configure: creating ./config.status
  config.status: creating Makefile

  target architecture: i386.
  available BSPs: pc686.
  'make all' will build the following BSPs: pc686.
  other BSPs can be built with 'make RTEMS_BSP="bsp1 bsp2 ..."'

  config.status: creating Makefile
   /c/opt/rtems/kernel/pc686
  $

Build the kernel:

.. code-block:: none

   /c/opt/rtems/kernel/pc686
  $ make
  Making all in tools/build
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
  make  all-am
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
  gcc -DHAVE_CONFIG_H -I. -I/c/opt/rtems/kernel/rtems/tools/build     -g -O2 -MT
  cklength.o -MD -MP -MF .deps/cklength.Tpo -c -o cklength.o
  /c/opt/rtems/kernel/rtems/tools/build/cklength.c
  gcc -DHAVE_CONFIG_H -I. -I/c/opt/rtems/kernel/rtems/tools/build     -g -O2 -MT
  eolstrip.o -MD -MP -MF .deps/eolstrip.Tpo -c -o eolstrip.o
  /c/opt/rtems/kernel/rtems/tools/build/eolstrip.c
    ..........
  i386-rtems4.11-objcopy -O binary nsecs.nxe nsecs.bin
  ../../../../../pc686/build-tools/bin2boot -v nsecs.ralf 0x00097E00
  ../../../../../pc686/lib/start16.bin 0x00097C00 0 nsecs.bin 0x00100000 0
  header address       0x00097e00, its memory size 0xzx
  first  image address 0x00097c00, its memory size 0x00000200
  second image address 0x00100000, its memory size 0x0003d800
  rm -f nsecs.nxe
  make[6]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites/samples/nsecs'
  make[5]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites/samples'
  make[4]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites/samples'
  make[4]: Entering directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites'
  make[4]: Nothing to be done for 'all-am'.
  make[4]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites'
  make[3]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686/testsuites'
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c/pc686'
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686/i386-rtems4.11/c'
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686'
  make[1]: Nothing to be done for 'all-am'.
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686'
   /c/opt/rtems/kernel/pc696
  $

Install the kernel to our prefix:

.. code-block:: none

  $ make install
  Making install in tools/build
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/build'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/bin'
    /usr/bin/install -c cklength.exe eolstrip.exe packhex.exe unhex.exe
    rtems-bin2c.exe '/c/opt/rtems/4.11/bin'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/bin'
   /usr/bin/install -c install-if-change '/c/opt/rtems/4.11/bin'
  make[2]: Nothing to be done for 'install-data-am'.
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/build'
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/build'
  Making install in tools/cpu
  make[1]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu'
  Making install in generic
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[3]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[3]: Nothing to be done for 'install-exec-am'.
  make[3]: Nothing to be done for 'install-data-am'.
  make[3]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686/tools/cpu/generic'
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu'
  make[3]: Entering directory '/c/opt/rtems/kernel/pc686/tools/cpu'
  make[3]: Nothing to be done for 'install-exec-am'.
  make[3]: Nothing to be done for 'install-data-am'.
    ..........
  make[2]: Entering directory '/c/opt/rtems/kernel/pc686'
  make[2]: Nothing to be done for 'install-exec-am'.
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/make'
   /usr/bin/install -c -m 644 /c/opt/rtems/kernel/rtems/make/main.cfg
   /c/opt/rtems/kernel/rtems/make/leaf.cfg '/c/opt/rtems/4.11/make'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/share/rtems4.11/make/Templates'
   /usr/bin/install -c -m 644
   /c/opt/rtems/kernel/rtems/make/Templates/Makefile.dir
   /c/opt/rtems/kernel/rtems/make/Templates/Makefile.leaf
   /c/opt/rtems/kernel/rtems/make/Templates/Makefile.lib
   '/c/opt/rtems/4.11/share/rtems4.11/make/Templates'
   /usr/bin/mkdir -p '/c/opt/rtems/4.11/make/custom'
   /usr/bin/install -c -m 644 /c/opt/rtems/kernel/rtems/make/custom/default.cfg
   '/c/opt/rtems/4.11/make/custom'
  make[2]: Leaving directory '/c/opt/rtems/kernel/pc686'
  make[1]: Leaving directory '/c/opt/rtems/kernel/pc686'
   /c/opt/rtems/kernel/pc686
  $
