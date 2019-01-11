.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. index:: prefix
.. _prefixes:

Prefixes
========

You will see the term :ref:term:`prefix` referred to thoughout this
documentation and in a wide number of software packages you can download from
the internet. A **prefix** is the path on your computer a software package is
built and installed under. Packages that have a **prefix** will place all parts
under the **prefix** path. On a host computer like Linux the packages you
install from your distribution typically use a platform specific standard
**prefix**. For example on Linux it is :file:`/usr` and on FreeBSD it is
:file:`/usr/local`.

We recommend you *DO NOT* use the standard **prefix** when installing the RTEMS
Tools. The standard **prefix** is the default **prefix** each package built by
the RSB contains. If you are building the tools when logged in as a *Standard
User* and not as the *Super User* (``root``) or *Administrator* the RTEMS
Source Builder (RSB) *will* fail and report an error if the default **prefix**
is not writable. We recommend you leave the standand **prefix** for the
packages your operating system installs or software you manually install such
as applications.

A further reason not to use the standard **prefix** is to allow more than one
version of RTEMS to exist on your host machine at a time. The ``autoconf`` and
``automake`` tools required by RTEMS are not versioned and vary between the
various versions of RTEMS. If you use a single **prefix** such as the standard
**prefix** there is a chance parts from a package of different versions may
interact. This should not happen but it can.

For POSIX or Unix hosts, the RTEMS Project uses :file:`/opt/rtems` as it's
standard **prefix**. We view this **prefix** as a production level path, and we
prefer to place development versions under a different **prefix** away from the
production versions. Under this top level **prefix** we place the various
versions we need for development. For example the version 4.11.0 **prefix**
would be :file:`/opt/rtems/4.11.0`. If an update called 4.11.1 is released the
**prefix** would be :file:`/opt/rtems/4.11.1`. These are recommendations and
the choice of what you use is entirely yours. You may decide to have a single
path for all RTEMS 4.11 releases of :file:`/opt/rtems/4.11`.

For Windows a typical **prefix** is :file:`C:\\opt\\rtems` and as an MSYS2 path
this is :file:`/c/opt/rtems`.
