.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

Cross and Canadian Cross Building
---------------------------------

Cross building and Canadian Cross building is the process of building on one
machine an executable that runs on another machine. An example is building a
set of RTEMS tools on Linux to run on Windows. The RSB supports cross building
and Canadian cross building.

This sections details how to the RSB to cross and Canadian cross build.

Cross Building
^^^^^^^^^^^^^^

Cross building is where the _build_ machine and _host_ are different. The
_build_ machine runs the RSB and the _host_ machine is where the output from
the build runs. An example is building a package such as NTP for RTEMS on your
development machine.

To build the NTP package for RTEMS you enter the RSB command:

.. code-block:: shell

    $ ../source-builder/sb-set-builder \
       --log=log_ntp_arm.txt \
       --prefix=$HOME/development/rtems/5 \  <1>
       --host=arm-rtems5 \  <2>
       --with-rtems-bsp=xilinx_zynq_zc706 \  <3>
       5/net/ntp

.. topic:: Items:

  1. The tools and the RTEMS BSP are installed under the same prefix.

  2. The ``--host`` command is the RTEMS architecture and version.

  3. The BSP is built and installed in the prefix. The arhcitecture must match
     the ``--host`` architecture.

.. note: Installing Into Different Directories

  If you install BSPs into a different path to the prefix use the
  ``--with-tools`` option to specify the path to the tools. Do not add the
  'bin' directory at the end of the path.

Canadian Cross Building
^^^^^^^^^^^^^^^^^^^^^^^

A Canadian cross builds are where the **build**, **host** and **target**
machines all differ. For example building an RTEMS compiler for an ARM
processor that runs on Windows is built using a Linux machine. The process is
controlled by setting the build triplet to the host you are building, the host
triplet to the host the tools will run on and the target to the RTEMS
architecture you require. The tools needed by the RSB are:

- Build host C and C++ compiler

- Host C and C++ cross compiler

The RTEMS Source Builder requires you provide the build host C and C++ compiler
and the final host C and C++ cross-compiler. The RSB will build the build host
RTEMS compiler and the final host RTEMS C and C++ compiler, the output of this
process.

The Host C and C++ compiler is a cross-compiler that builds executables for the
host you want the tools for. You need to provide these tools. For Windows a
number of Unix operating systems provide MinGW tool sets as packages.

The RSB will build an RTEMS tool set for the build host. This is needed when
building the final host's RTEMS compiler as it needs to build RTEMS runtime
code such as *libc* on the build host.

TIP: Make sure the host's cross-compiler tools are in your path before run the
RSB build command.

TIP: Canadian Cross built tools will not run on the machine being used to build
them so you should provide the ``--bset-tar-files`` and ``--no-install``
options. The option to not install the files lets you provide a prefix that
does not exist or you cannot access.

To perform a cross build add ``--host=`` to the command line. For example
to build a MinGW tool set on FreeBSD for Windows add ``--host=mingw32``
if the cross compiler is ``mingw32-gcc``:

.. code-block:: shell

    $ ../source-builder/sb-set-builder --host=mingw32 \
       --log=l-mingw32-4.11-sparc.txt \
       --prefix=$HOME/development/rtems/5 \
       5/rtems-sparc

If you are on a Linux Fedora build host with the MinGW packages installed the
command line is:

.. code-block:: shell

    $ ../source-builder/sb-set-builder --host=i686-w64-mingw32 \
       --log=l-mingw32-4.11-sparc.txt \
       --prefix=$HOME/development/rtems/5 \
       5/rtems-sparc
