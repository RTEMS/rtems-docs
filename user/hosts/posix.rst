.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _posix-hosts:

POSIX Hosts
===========

POSIX hosts are most Unix operating systems such as Linux, FreeBSD and
NetBSD. RTEMS development works well on Unix and can scale from a single user
and a desktop machine to a team with decentralised or centralised development
infrastructure.

Root Access
-----------

You either have ``root`` access to your host development machine or you do
not. Some users are given hardware that is centrally managed. If you do not
have ``root`` access you can create your work environment in your home
directory. You could use a prefix of :file:`$HOME/development/rtems` or
:file:`$HOME/rtems`. Note, the ``$HOME`` environment variable can be
substituted with ``~``.

:ref:`QuickStartPrefixes` details using Prefixes to manage the installation.

RTEMS Tools and packages do not require ``root`` access
to be built and we encourage you to not build the tools as ``root``. If you
need to control write access then it is best to manage this with groups
assigned to users.

If you have ``root`` access you can decide to install the tools under any
suitable prefix. This may depend on the hardware in your host development
machine. If the machine is a centralised build server the prefix may be used to
separate production versions from the test versions and the prefix paths may
have restricted access rights to only those who manage and have configuration
control of the machine. We call this project sandboxing and
:ref:`ProjectSandboxing` explains this in more detail.

Linux
-----

BSP Build will require ``pax`` package if RTEMS is configured with the
``--enable-tests`` option, see :ref:`BuildingRTEMSTests`. This package is not
installed , by default, on many Linux distributions, you can check for it
using your package manager. Install it, if it is not present on your system.

A number of different Linux distrubutions are known to work. The following have
been tested and report as working.

.. _ArchLinux:

ArchLinux
~~~~~~~~~

The following packages are required on a fresh Archlinux 64bit installation:

.. code-block:: none

  # pacman -S base-devel gdb xz unzip ncurses git zlib

Archlinux, by default installs ``texinfo-5`` which is incompatible for building
GCC 4.7 tree. You will have to obtain ``texinfo-legacy`` from ``AUR`` and
provide a manual override:

.. code-block:: none

  # pacman -R texinfo
  $ yaourt -S texinfo-legacy
  # ln -s /usr/bin/makeinfo-4.13a /usr/bin/makeinfo

.. _CentOS:

CentOS
~~~~~~

The following packages are required on a minimal CentOS 6.3 or Cent)S 7
64-bit installation:

.. code-block:: none

  # yum install autoconf automake binutils gcc gcc-c++ gdb make patch pax \
  bison flex xz unzip ncurses-devel texinfo zlib-devel python-devel git

On CentOS 8, the ``pax`` command is now provided by the ``spax`` package,
you need to enable the PowerTools repository. and use Python3.  On a
fresh install, the following commands should install everything you
need for RTEMS development:

.. code-block:: none

  # dnf install yum-utils
  # dnf config-manager --set-enabled PowerTools
  # dnf update
  # dnf groupinstall "Development Tools"
  # dnf install python3 python3-pip python3-setuptools python3-devel
  # dnf install texinfo spax
  # alternatives --set python /usr/bin/python3

The minimal CentOS distribution is a specific DVD that installs a minimal
system. If you use a full system some of these packages may have been
installed.

.. _Fedora:

Fedora
~~~~~~

The RTEMS Source Builder has been tested on Fedora 19 64bit with the following
packages:

.. code-block:: none

  # yum install ncurses-devel python-devel git bison gcc cvs gcc-c++ \
       flex texinfo patch perl-Text-ParseWords zlib-devel

.. _Raspbian:

Raspbian
~~~~~~~~

The is the Debian distribution for the Raspberry Pi. The following packages are
required:

.. code-block:: none

  $ sudo apt-get install autoconf automake bison flex binutils gcc g++ gdb \
  texinfo unzip ncurses-dev python-dev git

It is recommended you get Model B of the Pi with 512M of memory and to mount a
remote disk over the network. The tools can be built on the network disk with a
prefix under your home directory as recommended and end up on the SD card.

.. _Ubuntu:
.. _Xubuntu:

Ubuntu
~~~~~~

The latest version is Ubuntu 18.04.1 LTS 64-bit. This section also includes
Xubuntu. A minimal installation was used and the following packages installed:

.. code-block:: none

  $ sudo apt-get build-dep build-essential gcc-defaults g++ gdb git \
  unzip pax bison flex texinfo unzip python3-dev libpython-dev \
  libncurses5-dev zlib1g-dev

Note that in previous versions of Ubuntu, the package libpython-dev was
python2.7-dev. The name of packages changes over time. You need the
package with Python development libraries for C/C++ programs. The following
is needed for recent versions:

.. code-block:: none

  $ sudo apt-get install python-dev

It is likely necessary that you will have to enable the Ubuntu Source
Repositories.  Users have suggested the following web pages which have
instructions:

* https://askubuntu.com/questions/158871/how-do-i-enable-the-source-code-repositories/158872
* https://askubuntu.com/questions/496549/error-you-must-put-some-source-uris-in-your-sources-list

.. _Linux Mint:

Linux Mint
~~~~~~~~~~

zlib package is required on Linux Mint. It has a different name (other
than the usual zlib-dev):

.. code-block:: none

  # sudo apt-get install zlib1g-dev

.. _openSUSE:

openSUSE
~~~~~~~~

This has been reported to work but no instructions were provided. This is an
opportunity to contribute. Please submit any guidance you can provide.

.. _FreeBSD:

FreeBSD
-------

The RTEMS Source Builder has been tested on FreeBSD 9.1, 10.3, 11 and
12 64bit version. You need to install some ports. They are:

.. code-block:: none

  # cd /usr/ports
  # portinstall --batch lang/python27

If you wish to build Windows (mingw32) tools please install the following
ports:

.. code-block:: none

  # cd /usr/ports
  # portinstall --batch devel/mingw32-binutils devel/mingw32-gcc
  # portinstall --batch devel/mingw32-zlib devel/mingw32-pthreads

The +zlip+ and +pthreads+ ports for MinGW32 are used for builiding a Windows
QEMU.

If you are on FreeBSD 10.0 and you have pkgng installed you can use 'pkg
install' rather than 'portinstall'.

We recommend you run as root the following command to speed up Python
3's subprocess support:

.. code-block:: none

  # mount -t fdescfs none /dev/fd

This speeds up closing file descriptors when creating subprocesses.

.. _NetBSD:

NetBSD
------

The RTEMS Source Builder has been tested on NetBSD 6.1 i386. Packages to add
are:

.. code-block:: none

  # pkg_add ftp://ftp.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/6.1/devel/gmake-3.82nb7.tgz
  # pkg_add ftp://ftp.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/6.1/devel/bison-2.7.1.tgz
  # pkg_add ftp://ftp.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/6.1/archivers/xz-5.0.4.tgz
