.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartSources:

Obtain the Sources
==================

You chose an installation prefix previous section.  We chose
:file:`$HOME/quick-start/rtems/5` as the installation prefix.

You need at least two source archives or Git repositories to work with RTEMS.
You can download the source archives for a released RTEMS version or you can
clone Git repositories to get all versions of RTEMS including the development
head.

We will clone the Git repositories into :file:`$HOME/quick-start/src`.

.. code-block:: none

    mkdir -p $HOME/quick-start/src
    cd $HOME/quick-start/src
    git clone git://git.rtems.org/rtems-source-builder.git rsb
    git clone git://git.rtems.org/rtems.git

The :file:`rsb` repository clone contains the
:ref:`RTEMS Source Builder (RSB) <RSB>`.  We clone it into
:file:`rsb` to get shorter paths during the tool suite build.  The
:file:`rtems` repository clone contains the RTEMS sources.  These two
repositories are enough to get started.  There are
`more repositories <https://git.rtems.org>`_ available.

Alternatively, you can download the source archives of a released RTEMS
version.

.. code-block:: none

    mkdir -p $HOME/quick-start/src
    cd $HOME/quick-start/src
    curl https://ftp.rtems.org/pub/rtems/releases/4.11/4.11.3/rtems-4.11.3.tar.xz | tar xJf -
    curl https://ftp.rtems.org/pub/rtems/releases/4.11/4.11.3/rtems-source-builder-4.11.3.tar.xz | tar xJf -

This quick start chapter focuses on working with the Git repository clones
since this gives you some flexibility.  You can switch between branches to try
out different RTEMS versions.  You have access to the RTEMS source history.
The RTEMS Project welcomes contributions.  The Git repositories enable you to
easily create patches and track local changes.  If you prefer to work with
archives of a released RTEMS version, then simply replace the version number 5
used throughout this chapter with the version number you selected, e.g. 4.11.
