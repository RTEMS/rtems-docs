.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. index:: Quick Start

.. _QuickStart:

Quick Start
***********

Follow the sections of this chapter step by step to get started developing
applications on top of RTEMS.

.. toctree::
    :maxdepth: 5
    :numbered:

    host
    prefixes
    sources
    tools
    bootstrap

The following is a quick start guide that provides a basic set of commands to
build the RTEMS Tools and Kernel. The quick start guide provides links to the
detailed sections if any problems are encountered.

The detailed procedure for installing an RTEMS Workspace and installing
all tools can be found in :ref:`installation`. This includes information
on installation points, developer versions, and the RTEMS kernel.

The short version of this procedure is as follows
(:ref:`posix-host-tools-chain`):

#. Create a workspace (:ref:`installation`),

#. Download the RTEMS Source Builder (RSB),

#. Build an RTEMS tool chain for a specific target architecture,

#. Download RTEMS, and then

#. Build RTEMS for a specific Board Support Package (BSP).

Each of these steps is described in a section in this guide.

Creating a Workspace
====================

Before beginning, the development host computer needs to be set up for
this quick start procedure to complete successfully. :ref:`host-computer`
details what is needed for the supported host operating systems. If
Windows is being used it is recommended following the procedure in
:ref:`microsoft-windows` first.

There are many ways and locations a suitable environment can be set up. A
common factor that defines the final location of tools and projects is the
place you have suitable storage. Another is permissions.  There is no
need to become root or the administrator and we recommend you avoid
doing this. You can build and install the tools anywhere on the host's
file system you, as a standard user, have read and write access too.
:ref:`Prefixes` and :ref:`ProjectSandboxing` provide detailed examples
of possible locations and set ups.

Simple Example
==============

.. code-block:: shell

  $ cd
  $ mkdir -p development/rtems
  $ cd development/rtems
  $ git clone git://git.rtems.org/rtems-source-builder.git rsb
    ...
  $ cd rsb
  $ ./source-builder/sb-check
    ...
  $ cd rtems
  $ ../source-builder/sb-set-builder \
      --prefix=/usr/home/chris/development/rtems/5 5/rtems-sparc
    ...

Build the RTEMS Kernel (:ref:`rtems-kernel-install`) by cloning the repository,
running the ``bootstrap`` procecure, building and finally installing the
kernel:

.. code-block:: shell

  $ export PATH=$HOME/development/rtems/5/bin:$PATH
  $ cd
  $ cd development/rtems
  $ mkdir kernel
  $ cd kernel
  $ git clone git://git.rtems.org/rtems.git rtems
    ...
  $ cd rtems
  $ ./bootstrap -c && $HOME/development/rtems/rsb/source-builder/sb-bootstrap
    ...
  $ cd ..
  $ mkdir erc32
  $ cd erc32
  $ $HOME/development/rtems/kernel/rtems/configure --prefix=$HOME/development/rtems/5 \
                     --target=sparc-rtems5 --enable-rtemsbsp=erc32 --enable-posix
    ...
  $ make -j 8
    ...
  $ make install

You can now build a third-party library or an application.
