.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartTools:

Install the Tool Suite
======================

You chose an installation prefix and cloned two RTEMS repositories in the
previous sections.  We chose :file:`$HOME/quick-start/rtems/5` as the
installation prefix and cloned the repositories in
:file:`$HOME/quick-start/src`.

You must select the
:ref:`target architecture <TargetArchitectures>` for which you need a tool
suite.  In this quick start chapter we choose `sparc-rtems5`.  The
`sparc-rtems5` is the tool suite name for the SPARC architecture and RTEMS
version 5.  The tool suite for RTEMS and the RTEMS sources are tightly coupled.
For example, do not use a RTEMS version 5 tool suite with RTEMS version 4.11
sources and vice versa.  We use the RSB in two steps.  The first step is to
download additional sources and patches.  Afterwards, you could disconnect your
host computer from the internet.  It is no longer required to work with RTEMS.

.. code-block:: none

    cd $HOME/quick-start/src/rsb/rtems
    ../source-builder/sb-set-builder --source-only-download 5/rtems-sparc

This command should output something like this (omitted lines are denoted by
...):

.. code-block:: none

    RTEMS Source Builder - Set Builder, 5 (98588a55961a)
    warning: exe: absolute exe found in path: (__unzip) /usr/local/bin/unzip
    Build Set: 5/rtems-sparc
    ...
    download: https://ftp.gnu.org/gnu/gcc/gcc-7.4.0/gcc-7.4.0.tar.xz -> sources/gcc-7.4.0.tar.xz
    ...
    Build Sizes: usage: 0.000B total: 141.738MB (sources: 141.559MB, patches: 183.888KB, installed 0.000B)
    Build Set: Time 0:01:17.613061

If you encounter errors in the first step, check your internet connection,
firewall settings, virus scanners and the availability of the download servers.
The seconds step is to build and install the tool suite.

.. code-block:: none

    cd $HOME/quick-start/src/rsb/rtems
    ../source-builder/sb-set-builder --prefix=$HOME/quick-start/rtems/5 5/rtems-sparc

This command should output something like this (omitted lines are denoted by
...):

.. code-block:: none

    RTEMS Source Builder - Set Builder, 5 (98588a55961a)
    warning: exe: absolute exe found in path: (__unzip) /usr/local/bin/unzip
    Build Set: 5/rtems-sparc
    ...
    config: tools/rtems-gcc-7.4.0-newlib-3e24fbf6f.cfg
    package: sparc-rtems5-gcc-7.4.0-newlib-3e24fbf6f-x86_64-freebsd12.0-1
    building: sparc-rtems5-gcc-7.4.0-newlib-3e24fbf6f-x86_64-freebsd12.0-1
    sizes: sparc-rtems5-gcc-7.4.0-newlib-3e24fbf6f-x86_64-freebsd12.0-1: 4.651GB (installed: 879.191MB)
    cleaning: sparc-rtems5-gcc-7.4.0-newlib-3e24fbf6f-x86_64-freebsd12.0-1
    ....
    Build Sizes: usage: 5.618GB total: 1.105GB (sources: 141.559MB, patches: 185.823KB, installed 989.908MB)
    Build Set: Time 0:22:02.262039

In case the seconds step was successful, you can check if for example the cross
C compiler works with the following command:

.. code-block:: none

    $HOME/quick-start/rtems/5/bin/sparc-rtems5-gcc --version --verbose

This command should output something like below.  In this output the actual
prefix path was replaced by ``$PREFIX``.  The ``compiled by`` line depends on
the native C++ compiler of your host computer.  In the output you see the Git
hash of the RSB.  This helps you to identify the exact sources which were used
to build the cross compiler of your RTEMS tool suite.

.. code-block:: none

    Using built-in specs.
    COLLECT_GCC=$PREFIX/bin/sparc-rtems5-gcc
    COLLECT_LTO_WRAPPER=$PREFIX/bin/../libexec/gcc/sparc-rtems5/7.4.0/lto-wrapper
    sparc-rtems5-gcc (GCC) 7.4.0 20181206 (RTEMS 5, RSB 98588a55961a92f5d27bfd756dfc9e31b2b1bf98, Newlib 3e24fbf6f)
    Copyright (C) 2017 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


    Target: sparc-rtems5
    Configured with: ../gcc-7.4.0/configure --prefix=$PREFIX --bindir=$PREFIX/bin --exec_prefix=$PREFIX --includedir=$PREFIX/include --libdir=$PREFIX/lib --libexecdir=$PREFIX/libexec --mandir=$PREFIX/share/man --infodir=$PREFIX/share/info --datadir=$PREFIX/share --build=x86_64-freebsd12.0 --host=x86_64-freebsd12.0 --target=sparc-rtems5 --disable-libstdcxx-pch --with-gnu-as --with-gnu-ld --verbose --with-newlib --disable-nls --without-included-gettext --disable-win32-registry --enable-version-specific-runtime-libs --disable-lto --enable-newlib-io-c99-formats --enable-newlib-iconv --enable-newlib-iconv-encodings=big5,cp775,cp850,cp852,cp855,cp866,euc_jp,euc_kr,euc_tw,iso_8859_1,iso_8859_10,iso_8859_11,iso_8859_13,iso_8859_14,iso_8859_15,iso_8859_2,iso_8859_3,iso_8859_4,iso_8859_5,iso_8859_6,iso_8859_7,iso_8859_8,iso_8859_9,iso_ir_111,koi8_r,koi8_ru,koi8_u,koi8_uni,ucs_2,ucs_2_internal,ucs_2be,ucs_2le,ucs_4,ucs_4_internal,ucs_4be,ucs_4le,us_ascii,utf_16,utf_16be,utf_16le,utf_8,win_1250,win_1251,win_1252,win_1253,win_1254,win_1255,win_1256,win_1257,win_1258 --enable-threads --disable-plugin --enable-libgomp --enable-languages=c,c++
    Thread model: rtems
    gcc version 7.4.0 20181206 (RTEMS 5, RSB 98588a55961a92f5d27bfd756dfc9e31b2b1bf98, Newlib 3e24fbf6f) (GCC) 
    COLLECT_GCC_OPTIONS='--version' '-v' '-mcpu=v7'
     $PREFIX/bin/../libexec/gcc/sparc-rtems5/7.4.0/cc1 -quiet -v -iprefix $PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/ help-dummy -quiet -dumpbase help-dummy -mcpu=v7 -auxbase help-dummy -version --version -o /tmp//ccuAN1wc.s
    GNU C11 (GCC) version 7.4.0 20181206 (RTEMS 5, RSB 98588a55961a92f5d27bfd756dfc9e31b2b1bf98, Newlib 3e24fbf6f) (sparc-rtems5)
            compiled by GNU C version 4.2.1 Compatible FreeBSD Clang 6.0.1 (tags/RELEASE_601/final 335540), GMP version 6.1.0, MPFR version 3.1.4, MPC version 1.0.3, isl version isl-0.16.1-GMP

    GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
    COLLECT_GCC_OPTIONS='--version' '-v' '-mcpu=v7'
     $PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/bin/as -v -s --version -o /tmp//ccFVgRAa.o /tmp//ccuAN1wc.s
    GNU assembler version 2.32 (sparc-rtems5) using BFD version (GNU Binutils) 2.32
    GNU assembler (GNU Binutils) 2.32
    Copyright (C) 2019 Free Software Foundation, Inc.
    This program is free software; you may redistribute it under the terms of
    the GNU General Public License version 3 or later.
    This program has absolutely no warranty.
    This assembler was configured for a target of `sparc-rtems5'.
    COMPILER_PATH=$PREFIX/bin/../libexec/gcc/sparc-rtems5/7.4.0/:$PREFIX/bin/../libexec/gcc/:$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/bin/
    LIBRARY_PATH=$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/:$PREFIX/bin/../lib/gcc/:$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/lib/
    COLLECT_GCC_OPTIONS='--version' '-v' '-mcpu=v7'
     $PREFIX/bin/../libexec/gcc/sparc-rtems5/7.4.0/collect2 --version $PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/lib/crt0.o -L$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0 -L$PREFIX/bin/../lib/gcc -L$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/lib /tmp//ccFVgRAa.o -lgcc -lc -lgcc
    collect2 version 7.4.0 20181206 (RTEMS 5, RSB 98588a55961a92f5d27bfd756dfc9e31b2b1bf98, Newlib 3e24fbf6f)
    $PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/bin/ld --version $PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/lib/crt0.o -L$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0 -L$PREFIX/bin/../lib/gcc -L$PREFIX/bin/../lib/gcc/sparc-rtems5/7.4.0/../../../../sparc-rtems5/lib /tmp//ccFVgRAa.o -lgcc -lc -lgcc
    GNU ld (GNU Binutils) 2.32
    Copyright (C) 2019 Free Software Foundation, Inc.
    This program is free software; you may redistribute it under the terms of
    the GNU General Public License version 3 or (at your option) a later version.
    This program has absolutely no warranty.
    COLLECT_GCC_OPTIONS='--version' '-v' '-mcpu=v7'
