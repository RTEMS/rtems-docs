.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

Quick Start
============

The following is a quick start guide that provides a basic set of commands to
build the RTEMS Tools and Kernel. The quick start guide provides links to the
detailed sections if any problems are encoutnered.

The detailed procedure for installing RTEMS can be found in
:ref:`installation`.

The development host computer needs to be set up for this quick start procedure
to complete successfully. :ref:`host-computer` details what is needed for the
supported host operating systems. If Windows is being used it is recommended
following the procedure in :ref:`microsoft-windows` first.

Their are many ways and locations a suitable environment can be set up. A
common factor that defines the final location of tools and projects is the
place you have suitable storage. :ref:`prefixes` and :ref:`project-sandboxing`
provide detailed examples of possible locations and set ups .

This procedure installs a developer set up using the RTEMS Git repositories on
a Unix (POSIX) or MacOS host. The output from the commands has been removed and
replaced with ``...``.

Create a workspace, download the RTEMS Source Builder (RSB) and build a tool
chain (:ref:`posix-host-tools-chain`):

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

Build the RTEMS Kernel (:ref:`rtems-kernel-install`) by cloning the repository,
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
                     --target=sparc-rtems4.12 --enable-rtemsbsp=erc32 --enable-posix
    ...
  $ make -j 8
    ...
  $ make install

You can now build a 3rd party library or an application.
