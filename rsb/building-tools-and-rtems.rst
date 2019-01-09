.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2018 Chris Johns <chrisj@rtems.org>

Building Tools and RTEMS
========================

The Quick Start section of the RTEMS Users Guide covers the typical
information and process needed to build both an RTEMS toolset and
RTEMS itself. This section has information on specific configuration
options that may be needed.

Controlling the Build
---------------------

Build sets can be controlled via the command line to enable and disable various
features. There is no definitive list of build options that can be listed
because they are implemented with the configuration scripts. The best way to
find what is available is to grep the configuration files. for ``with`` and
``without``.

Following are currently available:

``--without-rtems``
  Do not build RTEMS when building an RTEMS build set.

``--without-cxx``
  Do not build a C++ compiler.

``--with-ada``
  Attempt to build an Ada compiler.  You need a native GNAT installed.

``--with-fortran``
  Attempt to build a Fortran compiler.

``--with-objc``
  Attempt to build a C++ compiler.
