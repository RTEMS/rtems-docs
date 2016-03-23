.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _microsoft-windows-installation:

Microsoft Windows
-----------------
.. index:: Microsoft Windows Installation

This section details how you create an RTEMS development environment on
Windows. The installation documented here is on `Windows 7 64bit
Professional`. Building on `Windows 10` has been reported as working.

Please see :ref:`microsoft-windows` before continuing.

.. note::

   If the RSB reports ``error: no hosts defaults found; please add`` you have
   probably opened an MSYS2 32bit Shell. Close all 32bit Shell windows and open
   the MSYS2 64bit Shell.

RTEMS Tools
~~~~~~~~~~~

Create a workspace for RTEMS using the following shell command:

.. sidebar:: *Creating Tool Archives*

  Add ``--bset-tar-file`` to the ``sb-set-builder`` command line to create
  tar files of the built package set.

.. code-block:: shell

   ~
  $ mkdir -p /c/opt/rtems

The ``/c`` path is an internal MSYS2 mount point of the ``C:`` drive. The
command creates the RTEMS work space on the ``C:`` drive. If you wish to use
another drive please subsitute ``/c`` with your drive letter.

We build and install all RTEMS packages under the `prefix` we just
created. Change to that directory and get a copy of the RSB:

.. code-block:: shell

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

.. code-block:: shell

   /c/opt/rtems/rsb
  $ git checkout 4.11
  Branch 4.11 set up to track remote branch 4.11 from origin.
  Switched to a new branch '4.11'
   /c/opt/rtems/rsb
  $

Check the RSB has a valid environment:

.. code-block:: shell

   /c/opt/rtems/rsb
  $ cd rtems
   /c/opt/rtems/rsb/rtems
  $ ../source-builder/sb-check
  RTEMS Source Builder - Check, 4.11 (01ac76f2f90f)
  Environment is ok
   /c/opt/rtems/rsb/rtems
  $

To build a set of RTEMS tools for the Intel ``i386`` architecture. The build
runs a single job rather a job per CPU in your machine and will take a long
time so please be patient. The RSB creates a log file containing all the build
output and it will be changing size. The RSB command to build ``i386`` tools
is:

.. code-block:: shell

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

Building the Kernel
~~~~~~~~~~~~~~~~~~~

We can now build the RTEMS kernel using the RTEMS tools we have just
built. First we need to set the path to the tools:

.. code-block:: shell

   /c
  $ cd /c/opt/rtems
   /c/opt/rtems
  $ export PATH=/c/opt/rtems/4.11/bin:$PATH
   /c/opt/rtems
  $

We currently build RTEMS from the git release branch for 4.11:

.. code-block:: shell

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

.. code-block:: shell

   /c/opt/rtems/kernel/rtems
  $ ./bootstrap -c
  removing automake generated Makefile.in files
  removing configure files
  removing aclocal.m4 files

Then we generate the pre-install header file automake make files:

.. code-block:: shell

   /c/opt/rtems/kernel/rtems
  $ ./bootstrap -p
  Generating ./c/src/ada/preinstall.am
  Generating ./c/src/lib/libbsp/arm/altera-cyclone-v/preinstall.am
  Generating ./c/src/lib/libbsp/arm/atsam/preinstall.am
  Generating ./c/src/lib/libbsp/arm/beagle/preinstall.am
  Generating ./c/src/lib/libbsp/arm/csb336/preinstall.am
  Generating ./c/src/lib/libbsp/arm/csb337/preinstall.am
  Generating ./c/src/lib/libbsp/arm/edb7312/preinstall.am
  Generating ./c/src/lib/libbsp/arm/gdbarmsim/preinstall.am
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

Finally we run the RSB's parallel ``bootstrap`` command:

.. code-block:: shell

  $ /c/opt/rtems/rsb/source-builder/sb-bootstrap
  RTEMS Source Builder - RTEMS Bootstrap, 4.11 (76188ee494dd)
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
found in the to directory of the RTEMS kernel source. We build the Board
Support Package (BSP) outside the kernel source tree:

.. code-block:: shell

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

.. code-block:: shell

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

.. code-block:: shell

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

.. code-block:: shell

   /c/opt/rtems/kernel/pc686
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

Building the LibBSD
~~~~~~~~~~~~~~~~~~~

The RTEMS BSD Library or libBSD as it is also know is a package of FreeBSD code
ported to RTEMS. It provides a number of advantanced services including a
networking stack
