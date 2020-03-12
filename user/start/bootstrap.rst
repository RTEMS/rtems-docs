.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBootstrap:

Bootstrap the RTEMS Sources
===========================

You installed the tool suite in your installation prefix and made ready the
source for two RTEMS source packages in the previous sections.  We installed
the tool suite in :file:`$HOME/quick-start/rtems/5` and unpacked the RSB source
in :file:`$HOME/quick-start/src`.

You only need to *bootstrap* the RTEMS sources if you have used
:ref:`QuickStartSources_Git` to get the sources. If you use source archives of
a released RTEMS version you can skip this section and move to
:ref:`QuickStartBSPBuild`.

Before you can build a :ref:`Board Support Package (BSP) <BSPs>` for your
target hardware from Git cloned RTEMS sources, you have to bootstrap the build
system in the RTEMS sources.  This is only necessary if you use a Git
repository clone of the RTEMS sources.  You have to do this after a fresh
repository clone and sometimes after build system file updates (e.g.  after a
``git pull``).  If you are not a build system expert, then do the bootstrap
after each update of build system files.  This is a bit annoying, but improving
the build system is a complex and time consuming undertaking.  Feel free to
help the RTEMS Project to improve it.  For the bootstrap it is important that
the right version of Autotools (:file:`autoconf` and :file:`automake`) are in
your ``$PATH``.  The right version of Autotools is shipped with the RTEMS tool
suite you already installed. Set the path to the tool suite installed under
your selected *prefix*:

.. code-block:: none

    export PATH=$HOME/quick-start/rtems/5/bin:"$PATH"

Change into the RTEMS source tree to *bootstrap* the build system:

.. code-block:: none

    cd $HOME/quick-start/src/rtems
    ./rtems-bootstrap

This command should output something like this (omitted lines are denoted by
``...``):

.. code-block:: none

    RTEMS Bootstrap, 1.0
      1/122: autoreconf: configure.ac
      2/122: autoreconf: testsuites/configure.ac
      3/122: autoreconf: testsuites/fstests/configure.ac
      4/122: autoreconf: testsuites/smptests/configure.ac
      5/122: autoreconf: testsuites/psxtests/configure.ac
      6/122: autoreconf: testsuites/mptests/configure.ac
    ...
    121/122: autoreconf: c/src/lib/libbsp/lm32/milkymist/configure.ac
    122/122: autoreconf: c/src/make/configure.ac
    Bootstrap time: 0:00:46.404643
