.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _rtems-kernel:

RTEMS Kernel
============

RTEMS is an open source real-time operating system. As a user you have access
to all the source code. The ``RTEMS Kernel`` section will show you how you
build the RTEMS kernel on your host.

Development Sources
-------------------

Create a new location to build the RTEMS kernel:

.. code-block:: none

  $ cd $HOME/development/rtems
  $ mkdir src
  $ cd src

Clone the RTEMS respository:

.. code-block:: none

  $ git clone https://gitlab.rtems.org/rtems/rtos/rtems.git rtems
  Cloning into 'rtems'...
  remote: Counting objects: 483342, done.
  remote: Compressing objects: 100% (88974/88974), done.
  remote: Total 483342 (delta 390053), reused 475669 (delta 383809)
  Receiving objects: 100% (483342/483342), 69.88 MiB | 1.37 MiB/s, done.
  Resolving deltas: 100% (390053/390053), done.
  Checking connectivity... done.

Building a BSP
--------------

We build RTEMS in a directory within the source tree we have just cloned.  For
the details, see the :ref:`BSPBuildSystem`.  We will build for the ``erc32``
BSP with POSIX enabled.  Firstly, create the file :file:`config.ini` in the
source tree root directory with the BSP build configuration, for example:

.. code-block:: ini

  [sparc/erc32]
  RTEMS_POSIX_API = True

Configure RTEMS using the ``waf configure`` command:

.. code-block:: none

  $ cd $HOME/development/rtems/src/rtems
  $ ./waf configure --prefix=$HOME/development/rtems/6
  Setting top to                           : $HOME/development/rtems/src/rtems
  Setting out to                           : $HOME/development/rtems/src/rtems/build
  Regenerate build specification cache (needs a couple of seconds)...
  Configure board support package (BSP)    : sparc/erc32
  Checking for program 'sparc-rtems6-gcc'  : $HOME/development/rtems/6/bin/sparc-rtems6-gcc
  Checking for program 'sparc-rtems6-g++'  : $HOME/development/rtems/6/bin/sparc-rtems6-g++
  Checking for program 'sparc-rtems6-ar'   : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'sparc-rtems6-ld'   : $HOME/development/rtems/6/bin/sparc-rtems6-ld
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'g++, c++'          : $HOME/development/rtems/6/bin/sparc-rtems6-g++
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'gas, gcc'          : $HOME/development/rtems/6/bin/sparc-rtems6-gcc
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'gcc, cc'           : $HOME/development/rtems/6/bin/sparc-rtems6-gcc
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for asm flags '-MMD'            : yes
  Checking for c flags '-MMD'              : yes
  Checking for cxx flags '-MMD'            : yes
  Checking for program 'rtems-bin2c'       : $HOME/development/rtems/6/bin/rtems-bin2c
  Checking for program 'gzip'              : /usr/bin/gzip
  Checking for program 'xz'                : /usr/bin/xz
  Checking for program 'rtems-ld'          : $HOME/development/rtems/6/bin/rtems-ld
  Checking for program 'rtems-syms'        : $HOME/development/rtems/6/bin/rtems-syms
  Checking for program 'rtems-bin2c'       : $HOME/development/rtems/6/bin/rtems-bin2c
  Checking for program 'gzip'              : /usr/bin/gzip
  Checking for program 'xz'                : /usr/bin/xz
  'configure' finished successfully (7.996s)

Build RTEMS:

.. code-block:: none

  $ ./waf
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build'
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build'
  'build' finished successfully (0.051s)
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  [   1/1524] Compiling bsps/shared/dev/serial/mc68681_reg2.c
  [   2/1524] Compiling bsps/shared/dev/rtc/mc146818a_ioreg.c
  [   3/1524] Compiling bsps/shared/dev/flash/am29lv160.c
  ...
  [1521/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/libz.a
  [1522/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/librtemscxx.a
  [1523/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/testsuites/samples/paranoia.exe
  [1524/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/libmghttpd.a
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  'build_sparc/erc32' finished successfully (4.894s)

Installing A BSP
----------------

All that remains to be done is to install the kernel. Installing RTEMS copies
the API headers and architecture specific libraries to a locaiton under the
`prefix` you provide. You can install any number of BSPs under the same
`prefix`. We recommend you have a separate `prefix` for different versions of
RTEMS. Do not mix versions of RTEMS under the same `prefix`. Make installs
RTEMS with the following command:

.. code-block:: none

  $ ./waf install
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build'
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build'
  'install' finished successfully (0.074s)
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/libchip/am29lv160.h (from bsps/include/libchip/am29lv160.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/libchip/mc146818a.h (from bsps/include/libchip/mc146818a.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/libchip/mc68681.h (from bsps/include/libchip/mc68681.h)
  ...
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/rtems/version.h (from cpukit/include/rtems/version.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/rtems/vmeintr.h (from cpukit/include/rtems/vmeintr.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/rtems/watchdogdrv.h (from cpukit/include/rtems/watchdogdrv.h)
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  'install_sparc/erc32' finished successfully (0.637s)

Contributing Patches
--------------------

RTEMS welcomes fixes to bugs and new features. For more details, please see
:ref:`Contributing`.

