.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _prefixs:

Prefixes
========

You will see the term **prefix** referred to though out this documentation and
in a wide number of software packages you can download from the internet. A
**prefix** is a path on your computer a software package is built and installed
under. Packages that have a **prefix** will place all parts under the *prefix
path*. On a host computer like Linux the packages you install from your
distribution typically use a platform specific standard *prefix*. For example
on Linux it is :file:`/usr` and on FreeBSD it is :file:`/usr/local`.

We recommend you **do not** use the standard *prefix* when installing RTEMS
Tools. If you are building the tools as a normal user and not as ``root`` the
RTEMS Source Builder (RSB) will fail if the *prefix* is not writable. We
recommend you leave the standand *prefix* for the packages your operating
system installs.

A further reason not use the standard *prefix* is to allow more than one
version of RTEMS to exist on your host machine at a time. The ``autoconf`` and
``automake`` tools required by RTEMS are not versioned and vary between RTEMS
versions. If you use a single *prefix* then there is a chance things from
different versions may interact. This should not happen but it could.

For POSIX or Unix hosts the RTEMS Project uses :file:`/opt/rtems` as a standard
*prefix*. We view this *prefix* as a production level path and we place
development versions under a different *prefix* away from the production
versions. Under this top level *prefix* we place the various versions, for
example for version 4.11.0 the *prefix* would be :file:`/opt/rtems/4.11.0`. If
an update called 4.11.1 is released the *prefix* would be
:file:`/opt/rtems/4.11.1`. This choice is entirly yours. You may decide to have
a single path for all RTEMS 4.11 releases of :file:`/opt/rtems/4.11`.

For Windows a typical prefix is :file:`C:\\opt` and as an MSYS2 path that is
:file:`/c/opt`.

.. _project_sandboxing:

Project Sandboxing
==================

Project specific sandboxes let you have a number of projects running in
parallel with each project in its own sandbox. You simlpy have a prefix per
project and under that prefix you create a simple yet repeatable structure.

As an exapmle lets say I have a large disk under :file:`/bd` for *Big Disk*. As
``root`` create a directory called ``project`` and give the directory suitable
permissions to be writable by you as a user.

Lets create project sandbox for my *Box Sorter* project. First create a project
directory called :file:`/bd/projects/box-sorter`. Under this create
:file:`rtems` and under that create :file:`rtems-4.11.0`. Under this path you
can follow the :ref:`released-version` procedure to build a tool set using the
prefix of :file:`/bd/projects/box-sorter/rtems/4.11.0`. You are free to create
your project specific directories under :file:`/bd/projects/box-sorter`.

A variation of this is to have a single set of *production* tools and RTEMS
BSPs on the disk under :file:`/bd/rtems` you can share between your projects.

:file:`/bd/rtems`
  The top path to production tools and kernels.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0 compiler, debuggers, tools and Board
  Support Packages (BSPs).

:file:`/bd/projects`
  Project specific development trees.

A further variation is to use the ``--without-rtems`` option with the RTEMS to
not build the BSPs when building the tools and to buld RTEMS specifically for
each project. This lets you have a production tools installed at a top level
on your disk and each project can have a specific and possibly customised
version of RTEMS.

:file:`/bd/rtems`
  The top path to production tools and kernels.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0 compiler, debuggers and tools.

:file:`/bd/projects`
  Project specific development trees.

If there is an RTEMS kernel you to share between projects you can move this to
a top level and share. In this case you will end up with:

:file:`/bd/rtems`
  The top path to production tools and kernels.

:file:`/bd/rtems/4.11.0`
  Production prefix for RTEMS 4.11.0.

:file:`/bd/rtems/4.11.0/tools`
  Production prefix for RTEMS 4.11.0 compiler, debuggers and tools.

:file:`/bd/rtems/4.11.0/bsps`
  Production prefix for RTEMS 4.11.0 Board Support Packages (BSPs).

:file:`/bd/projects`
  Project specific development trees.

The project sandoxing approach allows you move a specific production part into
the project's sandbox to allow you to customise it. This is useful if you are
testing new relesaes. The typical dependency is the order listed above. You can
test new RTEMS kernels with production tools but new tools will require you
build the kernel with them. Release notes with each release will let know
what you need to update.
