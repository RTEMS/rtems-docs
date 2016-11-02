.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment COPYRIGHT (c) 2012 - 2016.
.. comment Chris Johns <chrisj@rtems.org>

.. _Hosts:

Hosts
#####

The known supported hosts are listed in the following sections. If a host or a
new version of a host is known to work and it not listed please lets us know.

Linux
~~~~~

A number of different Linux distrubutions are known to work. The following have
been tested and report as working.

.. _ArchLinux:

ArchLinux
^^^^^^^^^

The following packages are required on a fresh Archlinux 64bit installation::

    # pacman -S base-devel gdb xz unzip ncurses git zlib

Archlinux, by default installs ``texinfo-5`` which is incompatible for building
GCC 4.7 tree. You will have to obtain ``texinfo-legacy`` from ``AUR`` and
provide a manual override::

    # pacman -R texinfo
    $ yaourt -S texinfo-legacy
    # ln -s /usr/bin/makeinfo-4.13a /usr/bin/makeinfo

.. _CentOS:

CentOS
^^^^^^

The following packages are required on a minimal CentOS 6.3 64bit installation::

    # yum install autoconf automake binutils gcc gcc-c++ gdb make patch \
    bison flex xz unzip ncurses-devel texinfo zlib-devel python-devel git

The minimal CentOS distribution is a specific DVD that installs a minimal
system. If you use a full system some of these packages may have been
installed.

.. _Fedora:

Fedora
^^^^^^

The RTEMS Source Builder has been tested on Fedora 19 64bit with the following
packages::

    # yum install ncurses-devel python-devel git bison gcc cvs gcc-c++ \
         flex texinfo patch perl-Text-ParseWords zlib-devel

.. _Raspbian:

Raspbian
^^^^^^^^

The is the Debian distribution for the Raspberry Pi. The following packages are
required::

    $ sudo apt-get install autoconf automake bison flex binutils gcc g++ gdb \
    texinfo unzip ncurses-dev python-dev git

It is recommended you get Model B of the Pi with 512M of memory and to mount a
remote disk over the network. The tools can be built on the network disk with a
prefix under your home directory as recommended and end up on the SD card.

.. _Ubuntu:
.. _Xubuntu:

Ubuntu
^^^^^^

The latest version is Ubuntu 16.04.1 LTS 64bit. This section also includes
Xubuntu. A minimal installation was used and the following packages installed::

    $ sudo apt-get build-dep binutils gcc g++ gdb unzip git
    $ sudo apt-get install python2.7-dev

.. _Linux Mint:

Linux Mint
^^^^^^^^^^

zlib package is required on Linux Mint. It has a different name (other
than the usual zlib-dev)::

    # sudo apt-get install zlib1g-dev

.. _openSUSE:

openSUSE
^^^^^^^^

This has been reported to work but no instructions were provided. This is an
opportunity to contribute. Please submit any guidance you can provide.

.. _FreeBSD:

FreeBSD
~~~~~~~

The RTEMS Source Builder has been tested on FreeBSD 9.1, 10.3 and 11 64bit
version. You need to install some ports. They are::

    # cd /usr/ports
    # portinstall --batch lang/python27

If you wish to build Windows (mingw32) tools please install the following
ports::

    # cd /usr/ports
    # portinstall --batch devel/mingw32-binutils devel/mingw32-gcc
    # portinstall --batch devel/mingw32-zlib devel/mingw32-pthreads

The +zlip+ and +pthreads+ ports for MinGW32 are used for builiding a Windows
QEMU.

If you are on FreeBSD 10.0 and you have pkgng installed you can use 'pkg
install' rather than 'portinstall'.

.. _NetBSD:

NetBSD
~~~~~~

The RTEMS Source Builder has been tested on NetBSD 6.1 i386. Packages to add
are::

    # pkg_add ftp://ftp.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/6.1/devel/gmake-3.82nb7.tgz
    # pkg_add ftp://ftp.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/6.1/devel/bison-2.7.1.tgz
    # pkg_add ftp://ftp.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/6.1/archivers/xz-5.0.4.tgz

.. _MacOS:

MacOS
~~~~~

The RTEMS Source Builder has been tested on Mountain Lion. You will need to
install the Xcode app using the *App Store* tool, run Xcode and install the
Developers Tools package within Xcode.

.. _Mavericks:

Mavericks
^^^^^^^^^

The RSB works on Mavericks and the GNU tools can be built for RTEMS using the
Mavericks clang LLVM tool chain. You will need to build and install a couple of
packages to make the RSB pass the +sb-check+. These are CVS and XZ. You can get
these tools from a packaging tool for MacOS such as *MacPorts* or *HomeBrew*.

I do not use 3rd party packaging on MacOS and prefer to build the packages from
source using a prefix of ``/usr/local``. There are good 3rd party packages around
however they sometimes bring in extra dependence and that complicates my build
environment and I want to know the minimal requirements when building
tools. The following are required:

. The XZ package's home page is http://tukaani.org/xz/ and I use version
  5.0.5. XZ builds and installs cleanly.

Serria
^^^^^^

The RSB works on Serria with the latest Xcode.

.. _Windows:

Windows
~~~~~~~

Windows tool sets are supported. The tools are native Windows executable which
means they do not need an emulation layer to run once built. The tools
understand and use standard Windows paths and integrate easily into Windows IDE
environments because they understand and use standard Windows paths. Native
Windows tools have proven over time to be stable and reliable with good
performance. If you are a Windows user or you are required to use Windows you
can still develop RTEMS application as easily as a Unix operating system. Some
debugging experiences may vary and if this is an issue please raised the topic
on the RTEMS Users mailing list.

Building the tools or some other packages may require a Unix or POSIX type
shell. There are a few options, Cygwin and MSYS2. I recommend MSYS2.

.. _MSYS2:

MSYS2
^^^^^

This is a new version of the MinGW project's original MSYS. MSYS2 is based
around the Arch Linux pacman packager. MSYS and MSYS2 are a specific fork of
the Cygwin project with some fundamental changes in the handling of paths and
mounts that allow easy interaction between the emulated POSIX environment and
the native Windows environment.

Install MSYS2 using the installer you can download from
https://msys2.github.io/. Follow the instructions on the install page and make
sure you remove any global path entries to any other Cygwin, MinGW, MSYS or
packages that may uses a Cygwin DLL, for example some ports of Git.

To build the tools you need install the following packages using pacman::

 $ pacman -S git cvs bison make texinfo patch unzip diffutils tar \
          mingw64/mingw-w64-x86_64-gcc mingw64/mingw-w64-x86_64-binutils

To build make sure you add '--without-python --jobs=none' to the standard RSB
command line. MSYS2 has a temp file name issue and so the GNU AR steps on
itself when running in parallel on SMP hardware which means we have to set the
jobs option to none.

Install a suitable version of Python from http://www.python.org/ and add it to
the start of your path. The MSYS2 python does not work with waf.

.. _Cygwin:

Cygwin

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
high load. In this case a 3rd party virus tool was installed so the Windows
Defender service was not needed.

To build a MinGW tool chain a Canadian cross-compile (Cxc) is required on
Cygwin because the host is Cygwin therefore a traditional cross-compile will
result in Cygiwn binaries. With a Canadian cross-compile a Cygwin
cross-compiler is built as well as the MinGW RTEMS cross-compiler. The Cygwin
cross-compiler is required to build the C runtime for the RTEMS target because
we are building under Cygiwn. The build output for an RTEMS 4.10 ARM tool set
is::

    chris@cygthing ~/development/rtems/src/rtems-source-builder/rtems
    $ ../source-builder/sb-set-builder --log=l-arm.txt --prefix=$HOME/development/rtems/4.10 4.10/rtems-arm
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
