.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

Quick Start Guide
=================

.. index:: Quick Start

The following is a quick start guide that provides you with the basic commands
you need to build the RTEMS Tools and Kernel.

You need to have your development host set up and ready, the
:ref:`development-host` covers what you need.

This procedure does a development (unstable) build from Git for a POSIX
host. You can refer to the specific section that cover the specific part of the
process in detail if you have an issue. The output from the commands has been
removed and replaced with ``...``.

Create a workspace, download the RTEMS Source Builder (RSB) and build a tool
chain (See :ref:`rtems-tools-chain`):

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
      --prefix=/usr/home/chris/development/rtems/4.12 4.12/rtems-sparc
    ...

Build the RTEMS Kernel (See :ref:`rtems-kernel`) by cloning the repository,
running the ``bootstrap`` procecure, building and finally installing the
kernel:

.. code-block:: shell

  $ export PATH=$HOME/development/rtems/4.12/bin:$PATH
  $ cd
  $ cd development/rtems
  $ mkdir kernel
  $ cd kernel
  $ git clone git://git.rtems.org/rtems.git rtems
    ...
  $ cd rtems
  $ ./bootstrap -c && ./bootstrap -p && \
              $HOME/development/rtems/rsb/source-builder/sb-bootstrap
    ...
  $ cd ..
  $ mkdir erc32
  $ cd erc32
  $ $HOME/development/rtems/kernel/rtems/configure --prefix=$HOME/development/rtems/4.12 \
                     --target=sparc-rtems4.12 --enable-rtemsbsp=erc32 --enable-posix \
		     --disable-networking
    ...
  $ make -j 8
    ...
  $ make install

You can now build a 3rd party library like LibBSD or an application.
