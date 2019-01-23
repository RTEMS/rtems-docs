.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _released-version:

Releases
========
.. index:: tarball
.. index:: release

RTEMS releases provide a stable version of the kernel for the supported
architectures. RTEMS maintaines the current and previous releases. Support for
older releases is provided using the RTEMS support channels.

Please read :ref:`development-host` before continuing. The following procedure
assumes you have installed and configured your host operating. It also assumes
you have installed any dependent packages needed when building the tools and
the kernel.

You need to select a location to build and install the RTEMS Tool chain and
RTEMS. Make sure there is plenty of disk space and a fast disk is
recommended. Our procedure will document building and installing the tools in a
base directory called :file:`/opt/rtems`. This path will require root
access. If you are working on a machine you do not have root access to you can
use a home directory, If building on Windows use :file:`/c/opt/rtems` to keep
the top level paths as short as possible. :ref:`windows-path-length` provides
more detail about path lengths on Windows.

The location used to install the tools and kernel is called the `prefix`.
:ref:`QuickStartPrefixes` explains prefixes and how to use them. It is best to
have a `prefix` for each different version of RTEMS you are using. If you are
using RTEMS 4.11 in production it is **not** a good idea to install a
development version of 5 over the top by using the same `prefix` as the 4.11
build. A separate `prefix` for each version avoids this.

Released versions of the RTEMS Source Builder (RSB) downloads all source code
for all packages from the :r:url:`ftp` rather than from the package's home
site. Hosting all the source on the :r:url:`ftp` ensures the source is present
for the life of the release on the :r:url:`ftp`. If there is a problem
accessing the RTEMS FTP the RSB will fall back to the packages home site.

The :r:url:`ftp` is hosted at the Oregon State University's The Open Source Lab
(http://osuosl.org/). This is a nonprofit organization working for the
advancement of open source technologies and RTEMS is very fortunate to be
shosted here. It has excellent internet access and performance.

.. note:: **Controlling the RTEMS Kernel Build**

   Building releases by default does not build the RTEMS kernel. To
   build the RTEMS kernel add the ``--with-rtems`` option to the RSB
   command line.

   By default all the BSPs for an architecture are built. If you only wish to
   have a specific BSP built you can specify the BSP list by providing to the
   RSB the option ``--with-rtemsbsp``. For example to build two BSPs for the
   SPARC architecture you can supply ``--with-rtemsbsp="erc32 leon3"``. This can
   speed the build time up for some architectures that have a lot of BSPs.

Once you have built the tools and kernel you can move to the Packages section
of the manual.

RTEMS Tools and Kernel
----------------------

This procedure will build a SPARC tool chain. Set up a suitable workspace to
build the release in. On Unix:

.. code-block:: shell

 $ cd
 $ mkdir -p development/rtems/releases
 $ cd development/rtems/releases

If building on Windows:

.. code-block:: shell

 $ cd /c
 $ mkdir -p opt/rtems
 $ cd opt/rtems

**Note** the paths on Windows will be different to those shown.

Download the RTEMS Source Builder (RSB) from the RTEMS FTP server:

.. code-block:: shell

 $ wget https://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/rtems-source-builder-4.11.0.tar.xz
 --2016-03-21 10:50:04-- https://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/rtems-source-builder-4.11.0.tar.xz
 Resolving ftp.rtems.org (ftp.rtems.org)... 140.211.10.151
 Connecting to ftp.rtems.org (ftp.rtems.org)|140.211.10.151|:443... connected.
 HTTP request sent, awaiting response... 200 OK
 Length: 967056 (944K) [application/x-xz]
 Saving to: 'rtems-source-builder-4.11.0.tar.xz'

 rtems-source-builder-4.1 100%[====================================>] 944.39K 206KB/s   in 5.5s

 2016-03-21 10:50:11 (173 KB/s) - 'rtems-source-builder-4.11.0.tar.xz' saved [967056/967056]

On Unix unpack the RSB release tar file using:

.. code-block:: shell

 $ tar Jxf rtems-source-builder-4.11.0.tar.xz
 $ cd rtems-source-builder-4.11.0/rtems/

On Windows you need to shorten the path (See :ref:`windows-path-length`) after
you have unpacked the tar file:

.. code-block:: shell

 $ tar Jxf rtems-source-builder-4.11.0.tar.xz
 $ mv rtems-source-builder-4.11.0 4.110
 $ cd 4.11.0

Build a tool chain for the SPARC architecure. We are using the SPARC
architecture in our example because GDB has a good simulator that lets us run
and test the samples RTEMS builds by default

If building on Windows add ``--jobs=none`` to avoid GNU make issues on Windows
discussed in :ref:`msys2_parallel_builds`.

.. code-block:: shell

 $ ../source-builder/sb-set-builder \
     --prefix=/opt/rtems/4.11 4.11/rtems-sparc
 Build Set: 4.11/rtems-sparc
 Build Set: 4.11/rtems-autotools.bset
 Build Set: 4.11/rtems-autotools-internal.bset
 config: tools/rtems-autoconf-2.69-1.cfg
 package: autoconf-2.69-x86_64-freebsd10.1-1
 Creating source directory: sources
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/autoconf-2.69.tar.gz -> sources/autoconf-2.69.tar.gz
 downloading: sources/autoconf-2.69.tar.gz - 1.8MB of 1.8MB (100%)
 building: autoconf-2.69-x86_64-freebsd10.1-1
 config: tools/rtems-automake-1.12.6-1.cfg
 package: automake-1.12.6-x86_64-freebsd10.1-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/automake-1.12.6.tar.gz -> sources/automake-1.12.6.tar.gz
 downloading: sources/automake-1.12.6.tar.gz - 2.0MB of 2.0MB (100%)
 Creating source directory: patches
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/automake-1.12.6-bugzilla.redhat.com-1239379.diff -> patches/automake-1.12.6-bugzilla.redhat.com-1239379.diff
 downloading: patches/automake-1.12.6-bugzilla.redhat.com-1239379.diff - 408.0 bytes of 408.0 bytes (100%)
 building: automake-1.12.6-x86_64-freebsd10.1-1
 cleaning: autoconf-2.69-x86_64-freebsd10.1-1
 cleaning: automake-1.12.6-x86_64-freebsd10.1-1
 Build Set: Time 0:00:32.749337
 Build Set: 4.11/rtems-autotools-base.bset
 config: tools/rtems-autoconf-2.69-1.cfg
 package: autoconf-2.69-x86_64-freebsd10.1-1
 building: autoconf-2.69-x86_64-freebsd10.1-1
 reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-freebsd10.1-1.txt
 reporting: tools/rtems-autoconf-2.69-1.cfg -> autoconf-2.69-x86_64-freebsd10.1-1.xml
 config: tools/rtems-automake-1.12.6-1.cfg
 package: automake-1.12.6-x86_64-freebsd10.1-1
 building: automake-1.12.6-x86_64-freebsd10.1-1
 reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-freebsd10.1-1.txt
 reporting: tools/rtems-automake-1.12.6-1.cfg -> automake-1.12.6-x86_64-freebsd10.1-1.xml
 installing: autoconf-2.69-x86_64-freebsd10.1-1 -> /opt/work/rtems/4.11.0
 installing: automake-1.12.6-x86_64-freebsd10.1-1 -> /opt/work/rtems/4.11.0
 cleaning: autoconf-2.69-x86_64-freebsd10.1-1
 cleaning: automake-1.12.6-x86_64-freebsd10.1-1
 Build Set: Time 0:00:15.619219
 Build Set: Time 0:00:48.371085
 config: devel/expat-2.1.0-1.cfg
 package: expat-2.1.0-x86_64-freebsd10.1-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/expat-2.1.0.tar.gz -> sources/expat-2.1.0.tar.gz
 downloading: sources/expat-2.1.0.tar.gz - 549.4kB of 549.4kB (100%)
 building: expat-2.1.0-x86_64-freebsd10.1-1
 reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-freebsd10.1-1.txt
 reporting: devel/expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-freebsd10.1-1.xml
 config: tools/rtems-binutils-2.26-1.cfg
 package: sparc-rtems4.11-binutils-2.26-x86_64-freebsd10.1-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/binutils-2.26.tar.bz2 -> sources/binutils-2.26.tar.bz2
 downloading: sources/binutils-2.26.tar.bz2 - 24.4MB of 24.4MB (100%)
 building: sparc-rtems4.11-binutils-2.26-x86_64-freebsd10.1-1
 reporting: tools/rtems-binutils-2.26-1.cfg ->
 sparc-rtems4.11-binutils-2.26-x86_64-freebsd10.1-1.txt
 reporting: tools/rtems-binutils-2.26-1.cfg ->
 sparc-rtems4.11-binutils-2.26-x86_64-freebsd10.1-1.xml
 config: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg
 package: sparc-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd10.1-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/gcc-4.9.3.tar.bz2 -> sources/gcc-4.9.3.tar.bz2
 downloading: sources/gcc-4.9.3.tar.bz2 - 85.8MB of 85.8MB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/newlib-2.2.0.20150423.tar.gz -> sources/newlib-2.2.0.20150423.tar.gz
 downloading: sources/newlib-2.2.0.20150423.tar.gz - 16.7MB of 16.7MB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/mpfr-3.0.1.tar.bz2 -> sources/mpfr-3.0.1.tar.bz2
 downloading: sources/mpfr-3.0.1.tar.bz2 - 1.1MB of 1.1MB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/mpc-0.8.2.tar.gz -> sources/mpc-0.8.2.tar.gz
 downloading: sources/mpc-0.8.2.tar.gz - 535.5kB of 535.5kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/gmp-5.0.5.tar.bz2 -> sources/gmp-5.0.5.tar.bz2
 downloading: sources/gmp-5.0.5.tar.bz2 - 2.0MB of 2.0MB (100%)
 building: sparc-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd10.1-1
 reporting: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg ->
 sparc-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd10.1-1.txt
 reporting: tools/rtems-gcc-4.9.3-newlib-2.2.0-20150423-1.cfg ->
 sparc-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd10.1-1.xml
 config: tools/rtems-gdb-7.9-1.cfg
 package: sparc-rtems4.11-gdb-7.9-x86_64-freebsd10.1-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/gdb-7.9.tar.xz -> sources/gdb-7.9.tar.xz
 downloading: sources/gdb-7.9.tar.xz - 17.0MB of 17.0MB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0001-sim-erc32-Disassembly-in-stand-alone-mode-did-not-wo.patch -> patches/0001-sim-erc32-Disassembly-in-stand-alone-mode-did-not-wo.patch
 downloading: patches/0001-sim-erc32-Disassembly-in-stand-alone-mode-did-not-wo.patch - 1.9kB of 1.9kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0002-sim-erc32-Corrected-wrong-CPU-implementation-and-ver.patch -> patches/0002-sim-erc32-Corrected-wrong-CPU-implementation-and-ver.patch
 downloading: patches/0002-sim-erc32-Corrected-wrong-CPU-implementation-and-ver.patch - 827.0 bytes of 827.0 bytes (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0003-sim-erc32-Perform-pseudo-init-if-binary-linked-to-no.patch -> patches/0003-sim-erc32-Perform-pseudo-init-if-binary-linked-to-no.patch
 downloading: patches/0003-sim-erc32-Perform-pseudo-init-if-binary-linked-to-no.patch - 2.6kB of 2.6kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0004-sim-erc32-Use-fenv.h-for-host-FPU-access.patch -> patches/0004-sim-erc32-Use-fenv.h-for-host-FPU-access.patch
 downloading: patches/0004-sim-erc32-Use-fenv.h-for-host-FPU-access.patch - 4.9kB of 4.9kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0005-sim-erc32-Remove-unused-defines-in-Makefile-and-swit.patch -> patches/0005-sim-erc32-Remove-unused-defines-in-Makefile-and-swit.patch
 downloading: patches/0005-sim-erc32-Remove-unused-defines-in-Makefile-and-swit.patch - 871.0 bytes of 871.0 bytes (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0006-sim-erc32-Fix-incorrect-simulator-performance-report.patch -> patches/0006-sim-erc32-Fix-incorrect-simulator-performance-report.patch
 downloading: patches/0006-sim-erc32-Fix-incorrect-simulator-performance-report.patch - 5.6kB of 5.6kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0007-sim-erc32-File-loading-via-command-line-did-not-work.patch -> patches/0007-sim-erc32-File-loading-via-command-line-did-not-work.patch
 downloading: patches/0007-sim-erc32-File-loading-via-command-line-did-not-work.patch - 1.0kB of 1.0kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0008-sim-erc32-Added-v-command-line-switch-for-verbose-ou.patch -> patches/0008-sim-erc32-Added-v-command-line-switch-for-verbose-ou.patch
 downloading: patches/0008-sim-erc32-Added-v-command-line-switch-for-verbose-ou.patch - 3.6kB of 3.6kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0009-sim-erc32-Removed-type-mismatch-compiler-warnings.patch -> patches/0009-sim-erc32-Removed-type-mismatch-compiler-warnings.patch
 downloading: patches/0009-sim-erc32-Removed-type-mismatch-compiler-warnings.patch - 1.9kB of 1.9kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0010-sim-erc32-Switched-emulated-memory-to-host-endian-or.patch -> patches/0010-sim-erc32-Switched-emulated-memory-to-host-endian-or.patch
 downloading: patches/0010-sim-erc32-Switched-emulated-memory-to-host-endian-or.patch - 16.0kB of 16.0kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0011-sim-erc32-use-SIM_AC_OPTION_HOSTENDIAN-to-probe-for-.patch -> patches/0011-sim-erc32-use-SIM_AC_OPTION_HOSTENDIAN-to-probe-for-.patch
 downloading: patches/0011-sim-erc32-use-SIM_AC_OPTION_HOSTENDIAN-to-probe-for-.patch - 14.8kB of 14.8kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0012-sim-erc32-Use-memory_iread-function-for-instruction-.patch -> patches/0012-sim-erc32-Use-memory_iread-function-for-instruction-.patch
 downloading: patches/0012-sim-erc32-Use-memory_iread-function-for-instruction-.patch - 3.8kB of 3.8kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0013-sim-erc32-Fix-a-few-compiler-warnings.patch-> patches/0013-sim-erc32-Fix-a-few-compiler-warnings.patch
 downloading: patches/0013-sim-erc32-Fix-a-few-compiler-warnings.patch - 2.2kB of 2.2kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0014-sim-erc32-Use-gdb-callback-for-UART-I-O-when-linked-.patch -> patches/0014-sim-erc32-Use-gdb-callback-for-UART-I-O-when-linked-.patch
 downloading: patches/0014-sim-erc32-Use-gdb-callback-for-UART-I-O-when-linked-.patch - 9.2kB of 9.2kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0015-sim-erc32-Access-memory-subsystem-through-struct-mem.patch -> patches/0015-sim-erc32-Access-memory-subsystem-through-struct-mem.patch
 downloading: patches/0015-sim-erc32-Access-memory-subsystem-through-struct-mem.patch - 22.9kB of 22.9kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0016-sim-erc32-Use-readline.h-for-readline-types-and-func.patch -> patches/0016-sim-erc32-Use-readline.h-for-readline-types-and-func.patch
 downloading: patches/0016-sim-erc32-Use-readline.h-for-readline-types-and-func.patch - 1.5kB of 1.5kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0017-sim-erc32-Move-local-extern-declarations-into-sis.h.patch -> patches/0017-sim-erc32-Move-local-extern-declarations-into-sis.h.patch
 downloading: patches/0017-sim-erc32-Move-local-extern-declarations-into-sis.h.patch - 5.8kB of 5.8kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0018-sim-erc32-Add-support-for-LEON3-processor-emulation.patch -> patches/0018-sim-erc32-Add-support-for-LEON3-processor-emulation.patch
 downloading: patches/0018-sim-erc32-Add-support-for-LEON3-processor-emulation.patch - 66.7kB of 66.7kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0019-sim-erc32-Add-support-for-LEON2-processor-emulation.patch -> patches/0019-sim-erc32-Add-support-for-LEON2-processor-emulation.patch
 downloading: patches/0019-sim-erc32-Add-support-for-LEON2-processor-emulation.patch - 26.1kB of 26.1kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0020-sim-erc32-Updated-documentation.patch -> patches/0020-sim-erc32-Updated-documentation.patch
 downloading: patches/0020-sim-erc32-Updated-documentation.patch - 16.1kB of 16.1kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0021-sim-erc32-Add-data-watchpoint-support.patch -> patches/0021-sim-erc32-Add-data-watchpoint-support.patch
 downloading: patches/0021-sim-erc32-Add-data-watchpoint-support.patch - 10.1kB of 10.1kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0022-Add-watchpoint-support-to-gdb-simulator-interface.patch -> patches/0022-Add-watchpoint-support-to-gdb-simulator-interface.patch
 downloading: patches/0022-Add-watchpoint-support-to-gdb-simulator-interface.patch - 25.5kB of 25.5kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/0023-sim-erc32-ELF-loading-could-fail-on-unaligned-sectio.patch -> patches/0023-sim-erc32-ELF-loading-could-fail-on-unaligned-sectio.patch
 downloading: patches/0023-sim-erc32-ELF-loading-could-fail-on-unaligned-sectio.patch - 1.3kB of 1.3kB (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/gdb-sim-arange-inline.diff -> patches/gdb-sim-arange-inline.diff
 downloading: patches/gdb-sim-arange-inline.diff - 761.0 bytes of 761.0 bytes (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/gdb-sim-cgen-inline.diff -> patches/gdb-sim-cgen-inline.diff
 downloading: patches/gdb-sim-cgen-inline.diff - 706.0 bytes of 706.0 bytes (100%)
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/sources/patch-gdb-python-python-config.py -> patches/patch-gdb-python-python-config.py
 downloading: patches/patch-gdb-python-python-config.py - 449.0 bytes of 449.0 bytes (100%)
 building: sparc-rtems4.11-gdb-7.9-x86_64-freebsd10.1-1
 reporting: tools/rtems-gdb-7.9-1.cfg ->
 sparc-rtems4.11-gdb-7.9-x86_64-freebsd10.1-1.txt
 reporting: tools/rtems-gdb-7.9-1.cfg ->
 sparc-rtems4.11-gdb-7.9-x86_64-freebsd10.1-1.xml
 config: tools/rtems-tools-4.11-1.cfg
 package: rtems-tools-4.11.0-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/rtems-tools-4.11.0.tar.xz -> sources/rtems-tools-4.11.0.tar.xz
 downloading: sources/rtems-tools-4.11.0.tar.xz - 1.6MB of 1.6MB (100%)
 building: rtems-tools-4.11.0-1
 reporting: tools/rtems-tools-4.11-1.cfg -> rtems-tools-4.11.0-1.txt
 reporting: tools/rtems-tools-4.11-1.cfg -> rtems-tools-4.11.0-1.xml
 config: tools/rtems-kernel-4.11.cfg
 package: sparc-rtems4.11-kernel-4.11.0-1
 download: ftp://ftp.rtems.org/pub/rtems/releases/4.11/4.11.0/rtems-4.11.0.tar.xz -> sources/rtems-4.11.0.tar.xz
 downloading: sources/rtems-4.11.0.tar.xz - 9.3MB of 9.3MB (100%)
 building: sparc-rtems4.11-kernel-4.11.0-1
 reporting: tools/rtems-kernel-4.11.cfg -> sparc-rtems4.11-kernel-4.11.0-1.txt
 reporting: tools/rtems-kernel-4.11.cfg -> sparc-rtems4.11-kernel-4.11.0-1.xml
 installing: expat-2.1.0-x86_64-freebsd10.1-1 -> /opt/work/rtems/4.11.0
 installing: sparc-rtems4.11-binutils-2.26-x86_64-freebsd10.1-1 -> /opt/work/rtems/4.11.0
 installing: sparc-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd10.1-1 -> /opt/work/rtems/4.11.0
 installing: sparc-rtems4.11-gdb-7.9-x86_64-freebsd10.1-1 -> /opt/work/rtems/4.11.0
 installing: rtems-tools-4.11.0-1 -> /opt/work/rtems/4.11.0
 installing: sparc-rtems4.11-kernel-4.11.0-1 -> /opt/work/rtems/4.11.0
 cleaning: expat-2.1.0-x86_64-freebsd10.1-1
 cleaning: sparc-rtems4.11-binutils-2.26-x86_64-freebsd10.1-1
 cleaning: sparc-rtems4.11-gcc-4.9.3-newlib-2.2.0.20150423-x86_64-freebsd10.1-1
 cleaning: sparc-rtems4.11-gdb-7.9-x86_64-freebsd10.1-1
 cleaning: rtems-tools-4.11.0-1
 cleaning: sparc-rtems4.11-kernel-4.11.0-1
 Build Set: Time 0:19:15.713662

You can now build a third-party library or an application as defaulted in TBD.
