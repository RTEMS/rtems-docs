.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _development-version:

Development Version
===================
.. index:: Git

RTEMS provides open access to it's development processes. The project encouages
all users to inspect, review, comment and contribute to the code base. The
processes described here are the same processes the core development team use
when developing and maintaining RTEMS.

Please read :ref:`development-hosts` before continuing.

.. warning::

   The development version is not for use in production and it can break from
   time to time.

The following procedure assumes you have installed and configured your host
operating. It also assumes you have installed any dependent packages needed
when building the tools and the kernel.

You need to select a location to build and install the RTEMS Tool chain and
RTEMS. Make sure there is plenty of disk space and a fast disk is
recommended. Our procedure will document building and installing the tools in a
home directory called :file:`development/rtems`. Using a home directory means
you can do this without needing to be root. You can also use
:file:`/opt/rtems/build` if you have access to that path.

The location used to install the tools and kernel is called the `prefix`. It is
best to have a `prefix` for each different version of RTEMS you are using. If
you are using RTEMS 4.11 in production it is not a good to install a
development version of 4.12 over the top. A separate `prefix` for each version
avoids this.

The RTEMS tool chain changes less often than the RTEMS kernel. One method of
working with development releases is to have a separate `prefix` for the RTEMS
tools and a different one for the RTEMS kernel. You can then update each
without interacting with the other. You can also have a number of RTEMS
versions available to test with.

This procedure will build a SPARC tool chain.

RTEMS Tools Chain
-----------------

Clone the RTEMS Source Builder (RSB) repository:

.. code-block:: shell

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

.. sidebar:: *Downloading the source*

  You need an internet connection to download the source. The downloaded source
  is cached locally and the RSB checksums it. If you run a build again the
  download output will be missing. Using the RSB from git will download the
  source from the upstream project's home site and this could be `http`, `ftp`,
  or `git`.

Check all the host packages you need are present. Current libraries are not
checked and this includes checking for the python development libraries GDB
requires:

.. code-block:: shell

  $ cd rsb
  $ ./source-builder/sb-check
  RTEMS Source Builder - Check, 4.12 (e645642255cc)
  Environment is ok

Build a tool chain for the SPARC architecure. We are using the SPARC
architecture because GDB has a good simulator that lets us run and test the
samples RTEMS builds by default. The current development version
is `4.12` and is on master:

.. code-block:: shell

  $ cd rtems
  $ ../source-builder/sb-set-builder \
      --prefix=/usr/home/chris/development/rtems/4.12 4.12/rtems-sparc
  RTEMS Source Builder - Set Builder, 4.12 (e645642255cc)
  Build Set: 4.12/rtems-sparc
  Build Set: 4.12/rtems-autotools.bset
  Build Set: 4.12/rtems-autotools-internal.bset
  config: tools/rtems-autoconf-2.69-1.cfg
  package: autoconf-2.69-x86_64-linux-gnu-1
  Creating source directory: sources
  download: ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz -> sources/autoconf-2.69.tar.gz
  downloading: sources/autoconf-2.69.tar.gz - 1.8MB of 1.8MB (100%)
  building: autoconf-2.69-x86_64-linux-gnu-1
  config: tools/rtems-automake-1.12.6-1.cfg
  package: automake-1.12.6-x86_64-linux-gnu-1
  download: ftp://ftp.gnu.org/gnu/automake/automake-1.12.6.tar.gz -> sources/automake-1.12.6.tar.gz
  downloading: sources/automake-1.12.6.tar.gz - 2.0MB of 2.0MB (100%)
  Creating source directory: patches
  download: https://git.rtems.org/rtems-tools/plain/tools/4.12/automake/automake-1.12.6-bugzilla.redhat.com-1239379.diff -> patches/automake-1.12.6-bugzilla.redhat.com-1239379.diff
  downloading: patches/automake-1.12.6-bugzilla.redhat.com-1239379.diff - 408.0 bytes of 408.0 bytes (100%)
  building: automake-1.12.6-x86_64-linux-gnu-1
  cleaning: autoconf-2.69-x86_64-linux-gnu-1
  cleaning: automake-1.12.6-x86_64-linux-gnu-1
  Build Set: Time 0:00:17.465024
  Build Set: 4.12/rtems-autotools-base.bset
  config: tools/rtems-autoconf-2.69-1.cfg
  package: autoconf-2.69-x86_64-linux-gnu-1
  building: autoconf-2.69-x86_64-linux-gnu-1
  reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-linux-gnu-1.txt
  reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-linux-gnu-1.xml
  config: tools/rtems-automake-1.12.6-1.cfg
  package: automake-1.12.6-x86_64-linux-gnu-1
  building: automake-1.12.6-x86_64-linux-gnu-1
  reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-linux-gnu-1.txt
  reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-linux-gnu-1.xml
  installing: autoconf-2.69-x86_64-linux-gnu-1 -> /usr/home/chris/development/rtems/4.12
  installing: automake-1.12.6-x86_64-linux-gnu-1 -> /usr/home/chris/development/rtems/4.12
  cleaning: autoconf-2.69-x86_64-linux-gnu-1
  cleaning: automake-1.12.6-x86_64-linux-gnu-1
  Build Set: Time 0:00:05.358624
  Build Set: Time 0:00:22.824422
  config: devel/expat-2.1.0-1.cfg
  package: expat-2.1.0-x86_64-linux-gnu-1
  download: http://downloads.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz -> sources/expat-2.1.0.tar.gz
    redirect: http://internode.dl.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz
  downloading: sources/expat-2.1.0.tar.gz - 549.4kB of 549.4kB (100%)
  building: expat-2.1.0-x86_64-linux-gnu-1
  reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-linux-gnu-1.txt
  reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-linux-gnu-1.xml
  config: tools/rtems-binutils-2.26-1.cfg
  package: sparc-rtems4.12-binutils-2.26-x86_64-linux-gnu-1
  download: ftp://ftp.gnu.org/gnu/binutils/binutils-2.26.tar.bz2 -> sources/binutils-2.26.tar.bz2
  downloading: sources/binutils-2.26.tar.bz2 - 24.4MB of 24.4MB (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.12/binutils/binutils-2.26-rtems-aarch64-x86_64.patch -> patches/binutils-2.26-rtems-aarch64-x86_64.patch
  downloading: patches/binutils-2.26-rtems-aarch64-x86_64.patch - 3.2kB	of 3.2kB (100%)
  building: sparc-rtems4.12-binutils-2.26-x86_64-linux-gnu-1
  reporting: tools/rtems-binutils-2.26-1.cfg -> sparc-rtems4.12-binutils-2.26-x86_64-linux-gnu-1.txt
  reporting: tools/rtems-binutils-2.26-1.cfg -> sparc-rtems4.12-binutils-2.26-x86_64-linux-gnu-1.xml
  config: tools/rtems-gcc-6-20160228-newlib-2.3.0.20160226-1.cfg
  package: sparc-rtems4.12-gcc-6-20160228-newlib-2.3.0.20160226-x86_64-linux-gnu-1
  download: ftp://gcc.gnu.org/pub/gcc/snapshots/6-20160228/gcc-6-20160228.tar.bz2 -> sources/gcc-6-20160228.tar.bz2
  downloading: sources/gcc-6-20160228.tar.bz2 - 90.8MB of 90.8MB (100%)
  download: ftp://sourceware.org/pub/newlib/newlib-2.3.0.20160226.tar.gz -> sources/newlib-2.3.0.20160226.tar.gz
  downloading: sources/newlib-2.3.0.20160226.tar.gz - 16.9MB of 16.9MB (100%)
  download: http://www.mpfr.org/mpfr-2.4.2/mpfr-2.4.2.tar.bz2 ->
  sources/mpfr-2.4.2.tar.bz2
  downloading: sources/mpfr-2.4.2.tar.bz2 - 1.0MB of 1.0MB (100%)
  download: http://www.multiprecision.org/mpc/download/mpc-0.8.1.tar.gz -> sources/mpc-0.8.1.tar.gz
  downloading: sources/mpc-0.8.1.tar.gz - 532.2kB of 532.2kB (100%)
  download: ftp://ftp.gnu.org/gnu/gmp/gmp-4.3.2.tar.bz2 -> sources/gmp-4.3.2.tar.bz2
  downloading: sources/gmp-4.3.2.tar.bz2 - 1.8MB of 1.8MB (100%)
  building: sparc-rtems4.12-gcc-6-20160228-newlib-2.3.0.20160226-x86_64-linux-gnu-1
  reporting: tools/rtems-gcc-6-20160228-newlib-2.3.0.20160226-1.cfg -> sparc-rtems4.12-gcc-6-20160228-newlib-2.3.0.20160226-x86_64-linux-gnu-1.txt
  reporting: tools/rtems-gcc-6-20160228-newlib-2.3.0.20160226-1.cfg -> sparc-rtems4.12-gcc-6-20160228-newlib-2.3.0.20160226-x86_64-linux-gnu-1.xml
  config: tools/rtems-gdb-7.9-1.cfg
  package: sparc-rtems4.12-gdb-7.9-x86_64-linux-gnu-1
  download: http://ftp.gnu.org/gnu/gdb/gdb-7.9.tar.xz -> sources/gdb-7.9.tar.xz
  downloading: sources/gdb-7.9.tar.xz - 17.0MB of 17.0MB (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.12/gdb/gdb-sim-arange-inline.diff -> patches/gdb-sim-arange-inline.diff
  downloading: patches/gdb-sim-arange-inline.diff - 761.0 bytes of 761.0 bytes (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.12/gdb/gdb-sim-cgen-inline.diff -> patches/gdb-sim-cgen-inline.diff
  downloading: patches/gdb-sim-cgen-inline.diff - 706.0 bytes of 706.0 bytes (100%)
  download: https://git.rtems.org/rtems-tools/plain/tools/4.12/gdb/gdb-7.9-aarch64-x86_64.patch -> patches/gdb-7.9-aarch64-x86_64.patch
  downloading: patches/gdb-7.9-aarch64-x86_64.patch - 1.7kB of 1.7kB (100%)
  building: sparc-rtems4.12-gdb-7.9-x86_64-linux-gnu-1
  reporting: tools/rtems-gdb-7.9-1.cfg -> sparc-rtems4.12-gdb-7.9-x86_64-linux-gnu-1.txt
  reporting: tools/rtems-gdb-7.9-1.cfg -> sparc-rtems4.12-gdb-7.9-x86_64-linux-gnu-1.xml
  config: tools/rtems-tools-4.12-1.cfg
  package: rtems-tools-HEAD-1
  Creating source directory: sources/git
  git: clone: git://git.rtems.org/rtems-tools.git -> sources/git/rtems-tools.git
  git: reset: git://git.rtems.org/rtems-tools.git
  git: fetch: git://git.rtems.org/rtems-tools.git -> sources/git/rtems-tools.git
  git: checkout: git://git.rtems.org/rtems-tools.git => HEAD
  git: pull: git://git.rtems.org/rtems-tools.git
  building: rtems-tools-HEAD-1
  reporting: tools/rtems-tools-4.12-1.cfg -> rtems-tools-HEAD-1.txt
  reporting: tools/rtems-tools-4.12-1.cfg -> rtems-tools-HEAD-1.xml
  installing: expat-2.1.0-x86_64-linux-gnu-1 -> /usr/home/chris/development/rtems/4.12
  installing: sparc-rtems4.12-binutils-2.26-x86_64-linux-gnu-1 -> /usr/home/chris/development/rtems/4.12
  installing: sparc-rtems4.12-gcc-6-20160228-newlib-2.3.0.20160226-x86_64-linux-gnu-1 -> /usr/home/chris/development/rtems/4.12
  installing: sparc-rtems4.12-gdb-7.9-x86_64-linux-gnu-1 -> /usr/home/chris/development/rtems/4.12
  installing: rtems-tools-HEAD-1 -> /usr/home/chris/development/rtems/4.12
  cleaning: expat-2.1.0-x86_64-linux-gnu-1
  cleaning: sparc-rtems4.12-binutils-2.26-x86_64-linux-gnu-1
  cleaning: sparc-rtems4.12-gcc-6-20160228-newlib-2.3.0.20160226-x86_64-linux-gnu-1
  cleaning: sparc-rtems4.12-gdb-7.9-x86_64-linux-gnu-1
  cleaning: rtems-tools-HEAD-1
  Build Set: Time 0:31:09.754219

RTEMS Kernel
------------

We need to set our path to include the RTEMS tools we built in the previous
section. The RTEMS tools needs to be first in your path because RTEMS provides
specific versions of the ``autoconf`` and ``automake`` tools. We want to use
the RTEMS version and not your host's versions:


.. code-block:: shell

  $ export PATH=$HOME/development/rtems/4.12/bin:$PATH

Create a new location to build the RTEMS kernel:

.. code-block:: shell

  $ cd
  $ cd development/rtems
  $ mkdir kernel
  $ cd kernel

Clone the RTEMS respository:

.. code-block:: shell

  $ git clone git://git.rtems.org/rtems.git rtems
  Cloning into 'rtems'...
  remote: Counting objects: 483342, done.
  remote: Compressing objects: 100% (88974/88974), done.
  remote: Total 483342 (delta 390053), reused 475669 (delta 383809)
  Receiving objects: 100% (483342/483342), 69.88 MiB | 1.37 MiB/s, done.
  Resolving deltas: 100% (390053/390053), done.
  Checking connectivity... done.

The developers version of the code from git requires we ``bootstrap`` the
source code. This is an ``autoconf`` and ``automake`` bootstrap to create the
various files generated by ``autoconf`` and ``automake``. RTEMS does not keep
these generated files under version control. The bootstrap process is slow so
to speed it up the RSB provides a command that can perform the bootstrap in
parallel using your available cores. We need to enter the cloned source
directory then run the bootsrap commands:

.. code-block:: shell

  $ cd rtems
  $ ./bootstrap -c && ./bootstrap -p && \
              $HOME/development/rtems/rsb/source-builder/sb-bootstrap
  removing automake generated Makefile.in files
  removing configure files
  removing aclocal.m4 files
  Generating ./cpukit/dtc/libfdt/preinstall.am
  Generating ./cpukit/zlib/preinstall.am
  Generating ./cpukit/libdl/preinstall.am
  Generating ./cpukit/posix/preinstall.am
  Generating ./cpukit/pppd/preinstall.am
  Generating ./cpukit/librpc/preinstall.am
  Generating ./cpukit/preinstall.am
  Generating ./cpukit/sapi/preinstall.am
  Generating ./cpukit/score/preinstall.am
  Generating ./cpukit/score/cpu/mips/preinstall.am
  Generating ./cpukit/score/cpu/sh/preinstall.am
  Generating ./cpukit/score/cpu/sparc/preinstall.am
  Generating ./cpukit/score/cpu/no_cpu/preinstall.am
  Generating ./cpukit/score/cpu/arm/preinstall.am
  Generating ./cpukit/score/cpu/m32c/preinstall.am
  Generating ./cpukit/score/cpu/moxie/preinstall.am
  Generating ./cpukit/score/cpu/v850/preinstall.am
  Generating ./cpukit/score/cpu/sparc64/preinstall.am
  Generating ./cpukit/score/cpu/or1k/preinstall.am
  Generating ./cpukit/score/cpu/i386/preinstall.am
  Generating ./cpukit/score/cpu/nios2/preinstall.am
  Generating ./cpukit/score/cpu/epiphany/preinstall.am
  Generating ./cpukit/score/cpu/m68k/preinstall.am
  Generating ./cpukit/score/cpu/lm32/preinstall.am
  Generating ./cpukit/score/cpu/powerpc/preinstall.am
  Generating ./cpukit/score/cpu/bfin/preinstall.am
  Generating ./cpukit/libpci/preinstall.am
  Generating ./cpukit/libcrypt/preinstall.am
  Generating ./cpukit/rtems/preinstall.am
  Generating ./cpukit/telnetd/preinstall.am
  Generating ./cpukit/libnetworking/preinstall.a
   ......
  Generating ./c/src/lib/libbsp/powerpc/gen5200/preinstall.am
  Generating ./c/src/lib/libbsp/powerpc/mpc55xxevb/preinstall.am
  Generating ./c/src/lib/libbsp/bfin/TLL6527M/preinstall.am
  Generating ./c/src/lib/libbsp/bfin/bf537Stamp/preinstall.am
  Generating ./c/src/lib/libbsp/bfin/eZKit533/preinstall.am
  Generating ./c/src/librtems++/preinstall.am
  Generating ./c/src/libchip/preinstall.am
  Generating ./c/src/wrapup/preinstall.am
  Generating ./c/src/ada/preinstall.am
  RTEMS Source Builder - RTEMS Bootstrap, 4.12 (e645642255cc modified)
    1/139: autoreconf: configure.ac
    2/139: autoreconf: cpukit/configure.ac
    3/139: autoreconf: tools/cpu/configure.ac
    4/139: autoreconf: tools/cpu/generic/configure.ac
    5/139: autoreconf: tools/cpu/sh/configure.ac
    6/139: autoreconf: tools/cpu/nios2/configure.ac
    7/139: autoreconf: tools/build/configure.ac
    8/139: autoreconf: doc/configure.ac
   ......
  124/139: autoreconf: c/src/make/configure.ac
  125/139: autoreconf: c/src/librtems++/configure.ac
  126/139: autoreconf: c/src/ada-tests/configure.ac
  127/139: autoreconf: testsuites/configure.ac
  128/139: autoreconf: testsuites/libtests/configure.ac
  129/139: autoreconf: testsuites/mptests/configure.ac
  130/139: autoreconf: testsuites/fstests/configure.ac
  131/139: autoreconf: testsuites/sptests/configure.ac
  132/139: autoreconf: testsuites/tmtests/configure.ac
  133/139: autoreconf: testsuites/smptests/configure.ac
  134/139: autoreconf: testsuites/tools/configure.ac
  135/139: autoreconf: testsuites/tools/generic/configure.ac
  136/139: autoreconf: testsuites/psxtests/configure.ac
  137/139: autoreconf: testsuites/psxtmtests/configure.ac
  138/139: autoreconf: testsuites/rhealstone/configure.ac
  139/139: autoreconf: testsuites/samples/configure.ac
  Bootstrap time: 0:02:47.398824

We build RTEMS in a directory outside of the source tree we have just cloned
and ``bootstrapped``. You cannot build RTEMS while in the source tree. Lets
create a suitable directory using the name of the BSP we are going to build:

.. code-block:: shell

  $ cd ..
  $ mkdir erc32
  $ cd erc32

Configure RTEMS using the ``configure`` command. We use a full path to
``configure`` so the object files built contain the absolute path of the source
files. If you are source level debugging you will be able to access the source
code to RTEMS from the debugger. We will build for the ``erc32`` BSP with POSIX
enabled and the networking stack disabled:

.. code-block:: shell

  $ $HOME/development/rtems/kernel/rtems/configure --prefix=$HOME/development/rtems/4.12 \
                     --target=sparc-rtems4.12 --enable-rtemsbsp=erc32 --enable-posix \
		     --disable-networking
  checking for gmake... no
  checking for make... make
  checking for RTEMS Version... 4.11.99.0
  checking build system type... x86_64-pc-linux-gnu
  checking host system type... x86_64-pc-linux-gnu
  checking target system type... sparc-unknown-rtems4.12
  checking for a BSD-compatible install... /usr/bin/install -c
  checking whether build environment is sane... yes
  checking for a thread-safe mkdir -p... /bin/mkdir -p
  checking for gawk... no
  checking for mawk... mawk
  checking whether make sets $(MAKE)... yes
  checking whether to enable maintainer-specific portions of Makefiles... no
  checking that generated files are newer than configure... done
   ......
  checking target system type... sparc-unknown-rtems4.12
  checking rtems target cpu... sparc
  checking for a BSD-compatible install... /usr/bin/install -c
  checking whether build environment is sane... yes
  checking for sparc-rtems4.12-strip... sparc-rtems4.12-strip
  checking for a thread-safe mkdir -p... /bin/mkdir -p
  checking for gawk... no
  checking for mawk... mawk
  checking whether make sets $(MAKE)... yes
  checking whether to enable maintainer-specific portions of Makefiles... no
  checking that generated files are newer than configure... done
  configure: creating ./config.status
  config.status: creating Makefile

  target architecture: sparc.
  available BSPs: erc32.
  'make all' will build the following BSPs: erc32.
  other BSPs can be built with 'make RTEMS_BSP="bsp1 bsp2 ..."'

  config.status: creating Makefile

Build RTEMS using two cores:

.. code-block:: shell

  $ make -j 2
  Making all in tools/build
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  make  all-am
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT cklength.o -MD -MP -MF .deps/cklength.Tpo -c -o cklength.o /home/chris/development/rtems/kernel/rtems/tools/build/cklength.c
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT eolstrip.o -MD -MP -MF .deps/eolstrip.Tpo -c -o eolstrip.o /home/chris/development/rtems/kernel/rtems/tools/build/eolstrip.c
  mv -f .deps/cklength.Tpo .deps/cklength.Po
  mv -f .deps/eolstrip.Tpo .deps/eolstrip.Po
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT compat.o -MD -MP -MF .deps/compat.Tpo -c -o compat.o /home/chris/development/rtems/kernel/rtems/tools/build/compat.c
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT packhex.o -MD -MP -MF .deps/packhex.Tpo -c -o packhex.o /home/chris/development/rtems/kernel/rtems/tools/build/packhex.c
  mv -f .deps/compat.Tpo .deps/compat.Po
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT unhex.o -MD -MP -MF .deps/unhex.Tpo -c -o unhex.o /home/chris/development/rtems/kernel/rtems/tools/build/unhex.c
  mv -f .deps/packhex.Tpo .deps/packhex.Po
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT rtems-bin2c.o -MD -MP -MF .deps/rtems-bin2c.Tpo -c -o rtems-bin2c.o /home/chris/development/rtems/kernel/rtems/tools/build/rtems-bin2c.c
  mv -f .deps/unhex.Tpo .deps/unhex.Po
  gcc -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/tools/build     -g -O2 -MT binpatch.o -MD -MP -MF .deps/binpatch.Tpo -c -o binpatch.o /home/chris/development/rtems/kernel/rtems/tools/build/binpatch.c
  mv -f .deps/rtems-bin2c.Tpo .deps/rtems-bin2c.Po
  gcc  -g -O2   -o cklength cklength.o
  mv -f .deps/binpatch.Tpo .deps/binpatch.Po
  gcc  -g -O2   -o eolstrip eolstrip.o compat.o
  gcc  -g -O2   -o packhex packhex.o
  gcc  -g -O2   -o rtems-bin2c rtems-bin2c.o compat.o
  gcc  -g -O2   -o unhex unhex.o compat.o
  gcc  -g -O2   -o binpatch binpatch.o
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  Making all in tools/cpu
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  Making all in generic
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu/generic'
  make[2]: Nothing to be done for 'all'.
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu/generic'
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  make[2]: Nothing to be done for 'all-am'.
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  Making all in testsuites/tools
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32/testsuites/tools'
  Making all in generic
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/testsuites/tools/generic'
  make[2]: Nothing to be done for 'all'.
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/testsuites/tools/generic'
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/testsuites/tools'
  make[2]: Nothing to be done for 'all-am'.
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/testsuites/tools'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/testsuites/tools'
  Making all in sparc-rtems4.12/c
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/c'
  Making all in .
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/c'
  Configuring RTEMS_BSP=erc32
  checking for gmake... no
  checking for make... make
  checking build system type... x86_64-pc-linux-gnu
  checking host system type... sparc-unknown-rtems4.12
   ......
  sparc-rtems4.12-gcc -B../../../../../erc32/lib/ -specs bsp_specs -qrtems -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/c/src/../../testsuites/samples/nsecs -I.. -I/home/chris/development/rtems/kernel/rtems/c/src/../../testsuites/samples/../support/include   -mcpu=cypress -O2 -g -ffunction-sections -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -MT init.o -MD -MP -MF .deps/init.Tpo -c -o init.o /home/chris/development/rtems/kernel/rtems/c/src/../../testsuites/samples/nsecs/init.c
  sparc-rtems4.12-gcc -B../../../../../erc32/lib/ -specs bsp_specs -qrtems -DHAVE_CONFIG_H -I. -I/home/chris/development/rtems/kernel/rtems/c/src/../../testsuites/samples/nsecs -I.. -I/home/chris/development/rtems/kernel/rtems/c/src/../../testsuites/samples/../support/include   -mcpu=cypress -O2 -g -ffunction-sections -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -MT empty.o -MD -MP -MF .deps/empty.Tpo -c -o empty.o /home/chris/development/rtems/kernel/rtems/c/src/../../testsuites/samples/nsecs/empty.c
  mv -f .deps/empty.Tpo .deps/empty.Po
  mv -f .deps/init.Tpo .deps/init.Po
  sparc-rtems4.12-gcc -B../../../../../erc32/lib/ -specs bsp_specs -qrtems -mcpu=cypress -O2 -g -ffunction-sections -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs -Wl,--gc-sections  -mcpu=cypress   -o nsecs.exe init.o empty.o
  sparc-rtems4.12-nm -g -n nsecs.exe > nsecs.num
  sparc-rtems4.12-size nsecs.exe
     text    data     bss     dec     hex filename
   121392    1888    6624  129904   1fb70 nsecs.exe
  cp nsecs.exe nsecs.ralf
  make[6]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32/testsuites/samples/nsecs'
  make[5]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32/testsuites/samples'
  make[4]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32/testsuites/samples'
  make[4]: Entering directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32/testsuites'
  make[4]: Nothing to be done for 'all-am'.
  make[4]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32/testsuites'
  make[3]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32/testsuites'
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/ c/erc32'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/c'
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32'
  make[1]: Nothing to be done for 'all-am'.
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32'

All that remains to be done is to install the kernel. Installing RTEMS copies
the API headers and architecture specific libraries to a locaiton under the
`prefix` you provide. You can install any number of BSPs under the same
`prefix`. We recommend you have a separate `prefix` for different versions of
RTEMS. Do not mix versions of RTEMS under the same `prefix`. Make installs
RTEMS with the following command:

.. code-block:: shell

  $ make install
  Making install in tools/build
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  /bin/mkdir -p '/home/chris/development/rtems/4.12/bin'
  /usr/bin/install -c cklength eolstrip packhex unhex rtems-bin2c '/home/chris/development/rtems/4.12/bin'
  /bin/mkdir -p '/home/chris/development/rtems/4.12/bin'
  /usr/bin/install -c install-if-change '/home/chris/development/rtems/4.12/bin'
  make[2]: Nothing to be done for 'install-data-am'.
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/build'
  Making install in tools/cpu
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  Making install in generic
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu/generic'
  make[3]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu/generic'
  make[3]: Nothing to be done for 'install-exec-am'.
  make[3]: Nothing to be done for 'install-data-am'.
  make[3]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu/generic'
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu/generic'
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  make[3]: Entering directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  make[3]: Nothing to be done for 'install-exec-am'.
  make[3]: Nothing to be done for 'install-data-am'.
  make[3]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/tools/cpu
   ......
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32/sparc-rtems4.12/c'
  make[1]: Entering directory '/home/chris/development/rtems/kernel/erc32'
  make[2]: Entering directory '/home/chris/development/rtems/kernel/erc32'
  make[2]: Nothing to be done for 'install-exec-am'.
  /bin/mkdir -p '/home/chris/development/rtems/4.12/make'
  /usr/bin/install -c -m 644 /home/chris/development/rtems/kernel/rtems/make/main.cfg /home/chris/development/rtems/kernel/rtems/make/leaf.cfg '/home/chris/development/rtems/4.12/make'
  /bin/mkdir -p '/home/chris/development/rtems/4.12/share/rtems4.12/make/Templates'
  /usr/bin/install -c -m 644 /home/chris/development/rtems/kernel/rtems/make/Templates/Makefile.dir /home/chris/development/rtems/kernel/rtems/make/Templates/Makefile.leaf /home/chris/development/rtems/kernel/rtems/make/Templates/Makefile.lib '/home/chris/development/rtems/4.12/share/rtems4.12/make/Templates'
  /bin/mkdir -p '/home/chris/development/rtems/4.12/make/custom'
  /usr/bin/install -c -m 644 /home/chris/development/rtems/kernel/rtems/make/custom/default.cfg '/home/chris/development/rtems/4.12/make/custom'
  make[2]: Leaving directory '/home/chris/development/rtems/kernel/erc32'
  make[1]: Leaving directory '/home/chris/development/rtems/kernel/erc32'

Contributing Patches
--------------------

RTEMS welcomes fixes to bugs and new features. The RTEMS Project likes to have
bugs fixed against a ticket created on our :r:url:`devel`. Please raise a
ticket if you have a bug. Any changes that are made can be tracked against the
ticket. If you want to add a new a feature please post a message to
:r:list:`devel` describing what you would like to implement. The RTEMS
maintainer will help decide if the feature is in the best interest of the
project. Not everything is and the maintainers need to evalulate how much
effort it is to maintain the feature. Once accepted into the source tree it
becomes the responsibility of the maintainers to keep the feature updated and
working.

Changes to the source tree are tracked using git. If you have not made changes
and enter the source tree and enter a git status command you will see nothing
has changed:

.. code-block:: shell

  $ cd ../rtems
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  nothing to commit, working directory clean

We will make a change to the source code. In this example I change the help
message to the RTEMS shell's ``halt`` command. Running the same git status
command reports:

.. code-block:: shell

  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

          modified:   cpukit/libmisc/shell/main_halt.c

  no changes added to commit (use "git add" and/or "git commit -a")

As an example I have a ticket open and the ticket number is 9876. I commit the
change with the follow git command:

.. code-block:: shell

  $ git commit cpukit/libmisc/shell/main_halt.c

An editor is opened and I enter my commit message. The first line is a title
and the following lines form a body. My message is:

.. code-block:: shell

  shell: Add more help detail to the halt command.

  Closes #9876.

  # Please enter the commit message for your changes. Lines starting
  # with '#' will be ignored, and an empty message aborts the commit.
  # Explicit paths specified without -i or -o; assuming --only paths...
  #
  # Committer: Chris Johns <chrisj@rtems.org>
  #
  # On branch master
  # Your branch is up-to-date with 'origin/master'.
  #
  # Changes to be committed:
  #       modified:   cpukit/libmisc/shell/main_halt.c

When you save and exit the editor git will report the commit's status:

.. code-block:: shell

  $ git commit cpukit/libmisc/shell/main_halt.c
  [master 9f44dc9] shell: Add more help detail to the halt command.
   1 file changed, 1 insertion(+), 1 deletion(-)

You can either email the patch to :r:list:`devel` with the following git
command:

.. code-block:: shell

  $ git send-email --to=devel@rtems.org -1
   <add output here>

Or you can ask git to create a patch file using:

.. code-block:: shell

  $ git format-patch -1
  0001-shell-Add-more-help-detail-to-the-halt-command.patch

This patch can be attached to a ticket.
