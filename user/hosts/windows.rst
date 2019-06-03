.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _microsoft-windows:

Microsoft Windows
=================

RTEMS supports Windows as a development host and the tools for most
architectures are available. The RTEMS Project relies on the GNU tools for
compilers and debuggers and we use the simulators that come with GDB and
QEMU. The Windows support for these tools varies and the RTEMS Project is
committed to helping the open source community improve the Windows
experience. If something is not working or supported please email the
:r:list:`users`.

The RTEMS Project's Windows tools can be native Windows executables
which give the user the best possible experience on Windows. Native
Windows programs use the standard Windows DLLs and paths. Integration
with standard Windows integrated development tools such as editors is
straight forward. POSIX emulation environments such as Cygwin and the
MSYS2 shell have special executables that require a POSIX emulation DLL
and these emulation DLLs add an extra layer of complexity as well as a
performance over-head. The RTEMS Project uses these POSIX emulation shells
to run configure scripts that come with various open source packages such
as `gcc` so they form an important and valued part of the environment we
describe here. The output of this procedure forms the tools you use during
your application development and they do not depend on the emulation DLLs.

The performance of a native Windows compiler is as good as you can have
on Windows and the performance compiling a single file will be similar to
that on a host like Linux or FreeBSD given the same hardware. Building
the tools from source is much slower on Windows because POSIX shells
and related tools are used and the POSIX emulation overhead it much much
slower than a native POSIX operating system like Linux and FreeBSD. This
overhead is only during the building of the tools and the RTEMS kernel
and if you use a suitable build system that is native to Windows your
application development should be similar to other operating systems.

Building is known to work on `Windows 7 64bit Professional` and
`Windows 10 64bit`.

.. _windows-path-length:

Windows Path Length
-------------------

Windows path length is limited and can cause problems when building the
tools. The standard Windows API has a ``MAX_PATH`` length of 260
characters. This can effect some of the tools used by RTEMS. It is recommended
you keep the top level directories as short as possible when building the RTEMS
tools and you should also keep an eye on the path length when developing your
application. The RTEMS built tools can handle much longer path lengths however
some of the GNU tools such as those in the ``binutils`` package cannot.

The release packages of the RSB when unpacked have top level file names that
are too big to build RTEMS. You need to change or rename that path to something
smaller to build. This is indicated in :ref:`released-version`.

.. _windows-spaces-in-paths:

Windows Spaces In Paths
-----------------------

Occasionally, a program will fail on Windows with errors that
appear as if a directory or file name was partially parsed by
some utility or program. This can be caused by having directories
of file names with spaces. Programs written in scripting languages
sometimes fail to properly quote file names and the space is
incorrectly interpreted. 

Parts of the PATH inherited from the native Windows environment often
include directory names with spaces. Sometimes it is necessary to set
the PATH explicitly to avoid these.

.. _msys2_parallel_builds:

Parallel Builds with Make
-------------------------

The MSYS2 GNU ``make`` has problems when using the `jobs` option. The RSB
defaults to automatically using as many cores as the host machine has. To get a
successful build on Windows it is recommended you add the ``--jobs=none``
option to all RSB build set commands.

POSIX Support
-------------

Building the RTEMS compilers, debugger, the RTEMS kernel and a number of other
third-party packages requires a POSIX environment. On Windows you can use Cygwin
or MSYS2. This document focuses on MSYS2. It is smaller than Cygwin and comes
with the Arch Linux package manager ``pacman``.

MSYS2 provides MinGW64 support as well as a POSIX shell called MSYS2. The
MinGW64 compiler and related tools produce 64bit native Windows
executables. The shell is a standard Bourne shell and the MSYS2 environment is
a stripped Cygwin shell with enough support to run the various ``configure``
scripts needed to build the RTEMS tools and the RTEMS kernel.

MSYS2 is built around the ``pacman`` packaging tool. This makes MSYS2 a
distribution and that is a welcome feature on Windows. You get a powerful tool
to manage your development environment on Windows.

Python
------

We need Python to build the tools as the RSB is written in Python and we need
suitable Python libraries to link to GDB as RTEMS makes use of GDB's Python
support. This places specific demands on the Python we need installed and
available and MSYS2 provides suitable Python versions we can use. You need to
make sure you have the correct type and version of Python installed.

We cannot use the Python executables created by the Python project (python.org)
as they are built by Microsoft's C (MSC) compiler. Linking the MSC Python
libraries with the MinGW64 executables is not easy and MSYS provides us with a
simple solution so we do not support linking MSC libraries.

MSYS2 provides two types and two versions of Python executables, MinGW and MSYS
and Python version 2 and 3. For Windows we need the MinGW executable so we have
suitables libraries and we have to have Python version 2 because on Windows GDB
only builds with Python2.

You also need to install the MSYS version of Python along with the MinGW64
Python2 package. The MSYS Python is version 3 and the RSB can support version 2
and 3 of Python and it helps handle some of the long paths building GCC can
generate.

.. _microsoft-windows-installation:

MSYS2
-----

MSYS2 is installed on a new machine using the MSYS2 installer found on
https://msys2.github.io/. Please select the ``x86_64`` variant for 64bit
support. Run the installer following the 7 steps listed on the page.

MSYS2 uses the ``pacman`` package manager. The Arch Linux project has detailed
documentation on how to use ``pacman``. What is shown here is a just few
examples of what you can do.

.. sidebar:: **Pin MSYS2 Shell to Taskbar**

  Pin the MSYS2 64bit Shell to the Taskbar so you always use it rather than the
  32bit Shell.

Open a 64bit MSYS shell from the Start Menu:

.. figure:: ../../images/msys2-minw64-start-menu.png
  :width: 50%
  :align: center
  :alt: MSYS2 64bit Shell Start Menu

The packages we require are:

* python
* mingw-w64-x86_64-python2
* mingw-w64-x86_64-gcc
* git
* bison
* cvs
* diffutils
* make
* patch
* tar
* texinfo
* unzip

.. note::

  The actual output provided may vary due to changes in the dependent packages
  or newer package versions.

Install the packages using ``pacman``:

.. code-block:: none

  $ pacman -S python mingw-w64-x86_64-python2 mingw-w64-x86_64-gcc \
  bison cvs diffutils git make patch tar texinfo unzip
  resolving dependencies...
  looking for conflicting packages...
      .... output shortened for brevity ....

.. _Cygwin:

Cygwin
------

Building on Windows is a little more complicated because the Cygwin shell is
used rather than the MSYS2 shell. The MSYS2 shell is simpler because the
detected host triple is MinGW so the build is a standard cross-compiler build.
A Canadian cross-build using Cygwin is supported if you would like native
tools or you can use a Cygwin built set of tools.

Install a recent Cygwin version using the Cygwin setup tool. Select and install
the groups and packages listed:

.. table:: Cygwin Packages

  ======= =========================
  Group   Package
  Archive bsdtar
  Archive unzip
  Archive xz
  Devel   autoconf
  Devel   autoconf2.1
  Devel   autoconf2.5
  Devel   automake
  Devel   binutils
  Devel   bison
  Devel   flex
  Devel   gcc4-core
  Devel   gcc4-g++
  Devel   git
  Devel   make
  Devel   mingw64-x86_64-binutils
  Devel   mingw64-x86_64-gcc-core
  Devel   mingw64-x86_64-g++
  Devel   mingw64-x86_64-runtime
  Devel   mingw64-x86_64-zlib
  Devel   patch
  Devel   zlib-devel
  MinGW   mingw-zlib-devel
  Python  python
  ======= =========================

The setup tool will add a number of dependent package and it is ok to accept
them.

Disabling Windows Defender improves performance if you have another up to date
virus detection tool installed and enabled. The excellent ``Process Hacker 2``
tool can monitor the performance and the Windows Defender service contributed a
high load. In this case a third-party virus tool was installed so the Windows
Defender service was not needed.

To build a MinGW tool chain a Canadian cross-compile (Cxc) is required on
Cygwin because the host is Cygwin therefore a traditional cross-compile will
result in Cygiwn binaries. With a Canadian cross-compile a Cygwin
cross-compiler is built as well as the MinGW RTEMS cross-compiler. The Cygwin
cross-compiler is required to build the C runtime for the RTEMS target because
we are building under Cygiwn. The build output for an RTEMS 4.10 ARM tool set
is:

.. code-block:: none

  chris@cygwin ~/development/rtems/src/rtems-source-builder/rtems
  $ ../source-builder/sb-set-builder --log=l-arm.txt \
                --prefix=$HOME/development/rtems/4.10 4.10/rtems-arm
  RTEMS Source Builder - Set Builder, v0.2
  Build Set: 4.10/rtems-arm
  config: expat-2.1.0-1.cfg
  package: expat-2.1.0-x86_64-w64-mingw32-1
  building: expat-2.1.0-x86_64-w64-mingw32-1
  reporting: expat-2.1.0-1.cfg -> expat-2.1.0-x86_64-w64-mingw32-1.html
  config: tools/rtems-binutils-2.20.1-1.cfg
  package: arm-rtems4.10-binutils-2.20.1-1   <1>
  building: arm-rtems4.10-binutils-2.20.1-1
  package: (Cxc) arm-rtems4.10-binutils-2.20.1-1   <2>
  building: (Cxc) arm-rtems4.10-binutils-2.20.1-1
  reporting: tools/rtems-binutils-2.20.1-1.cfg ->
  arm-rtems4.10-binutils-2.20.1-1.html
  config: tools/rtems-gcc-4.4.7-newlib-1.18.0-1.cfg
  package: arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1
  building: arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1
  package: (Cxc) arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1
  building: (Cxc) arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1
  reporting: tools/rtems-gcc-4.4.7-newlib-1.18.0-1.cfg ->
  arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1.html
  config: tools/rtems-gdb-7.3.1-1.cfg
  package: arm-rtems4.10-gdb-7.3.1-1
  building: arm-rtems4.10-gdb-7.3.1-1
  reporting: tools/rtems-gdb-7.3.1-1.cfg -> arm-rtems4.10-gdb-7.3.1-1.html
  config: tools/rtems-kernel-4.10.2.cfg
  package: arm-rtems4.10-kernel-4.10.2-1
  building: arm-rtems4.10-kernel-4.10.2-1
  reporting: tools/rtems-kernel-4.10.2.cfg -> arm-rtems4.10-kernel-4.10.2-1.html
  installing: expat-2.1.0-x86_64-w64-mingw32-1 -> /cygdrive/c/Users/chris/development/rtems/4.10
  installing: arm-rtems4.10-binutils-2.20.1-1 -> /cygdrive/c/Users/chris/development/rtems/4.10 <3>
  installing: arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1 -> /cygdrive/c/Users/chris/development/rtems/4.10
  installing: arm-rtems4.10-gdb-7.3.1-1 -> /cygdrive/c/Users/chris/development/rtems/4.10
  installing: arm-rtems4.10-kernel-4.10.2-1 -> /cygdrive/c/Users/chris/development/rtems/4.10
  cleaning: expat-2.1.0-x86_64-w64-mingw32-1
  cleaning: arm-rtems4.10-binutils-2.20.1-1
  cleaning: arm-rtems4.10-gcc-4.4.7-newlib-1.18.0-1
  cleaning: arm-rtems4.10-gdb-7.3.1-1
  cleaning: arm-rtems4.10-kernel-4.10.2-1
  Build Set: Time 10:09:42.810547   <4>

.. topic:: Items:

  1. The Cygwin version of the ARM cross-binutils.

  2. The +(Cxc)+ indicates this is the MinGW build of the package.

  3. Only the MinGW version is installed.

  4. Cygwin is slow so please be patient. This time was on an AMD Athlon 64bit
     Dual Core 6000+ running at 3GHz with 4G RAM running Windows 7 64bit.

.. warning::

  Cygwin documents the 'Big List Of Dodgy Apps' or 'BLODA'. The link is
  http://cygwin.com/faq/faq.html#faq.using.bloda and it is worth a look. You
  will see a large number of common pieces of software found on Windows systems
  that can cause problems. My testing has been performed with NOD32 running and
  I have seen some failures. The list is for all of Cygwin so I am not sure
  which of the listed programs effect the RTEMS Source Biulder. The following
  FAQ item talks about *fork* failures and presents some technical reasons they
  cannot be avoided in all cases. Cygwin and it's fork MSYS are fantastic
  pieces of software in a difficult environment. I have found building a single
  tool tends to work, building all at once is harder.
