.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBootstrap:

Bootstrap the RTEMS Sources
===========================

You installed the tool suite in your installation prefix and cloned two RTEMS
repositories in the previous sections.  We installed the tool suite in
:file:`$HOME/quick-start/rtems/5` and cloned the repositories in
:file:`$HOME/quick-start/src`.

If you use source archives of a released RTEMS version, then you can skip this
section.

Before you can build a :ref:`Board Support Package (BSP) <BSPs>` for your
target hardware, you have to bootstrap the build system in the RTEMS sources.
This is only necessary, if you use a Git repository clone of the RTEMS sources.
You have to do this after a fresh repository clone and sometimes after build
system file updates (e.g.  after a ``git pull``).  If you are not a build
system expert, then do the bootstrap after each update of build system files.
This is a bit annoying, but improving the build system is a complex and time
consuming undertaking.  Feel free to help the RTEMS Project to improve it.  For
the bootstrap it is important that the right version of Autotools
(:file:`autoconf` and :file:`automake`) are in your ``$PATH``.  The right
version of Autotools is shipped with the RTEMS tool suite you already
installed.

.. code-block:: none

    cd $HOME/quick-start/src/rtems
    export PATH=$HOME/quick-start/rtems/5/bin:"$PATH"
    ./bootstrap -c
    $HOME/quick-start/src/rsb/source-builder/sb-bootstrap

These commands should output something like this (omitted lines are denoted by
...):

.. code-block:: none

    removing automake generated Makefile.in files
    removing configure files
    removing aclocal.m4 files
    $ $HOME/quick-start/src/rsb/source-builder/sb-bootstrap
    RTEMS Source Builder - RTEMS Bootstrap, 5 (f07504d27192)
      1/120: autoreconf: configure.ac
      2/120: autoreconf: c/configure.ac
      3/120: autoreconf: c/src/configure.ac
      4/120: autoreconf: c/src/lib/libbsp/arm/configure.ac
    ...
    120/120: autoreconf: testsuites/tmtests/configure.ac
    Bootstrap time: 0:00:48.744222
