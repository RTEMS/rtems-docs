.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _host-os:

Host Operating Systems
======================

.. sidebar:: *GDB and Python*

   RTEMS uses Python in GDB to aid debugging which means GDB needs to be built
   with Python development libraries. Please check the RSB documentation and
   install the packages specified for your host. Make sure a python development
   package is included.

A wide range of host operating systems and hardware can be used. The host
operating systems supported are:

- Linux
- FreeBSD
- NetBSD
- Apple OS X
- Windows
- Solaris

The functionality on a POSIX operating such as Linux and FreeBSD is similar and
most features on Windows are supported but you are best to ask on the
:r:list:`users` if you have a specific question.

We recommend you maintain your operating system by installing any updates.

We also recommend you keep your environment to the bare minimum,
particularly the PATH variable. Using environment variables has been
proven over the years to be difficult to manage in production systems.

.. warning::

    The RSB assumes your host is set up and the needed packages are installed
    and configured to work. If your host has not been set up please refer to
    :ref:`Hosts` and your host's section for packages you need to install.

.. topic:: Path to use when building applications:

    Do not forget to set the path before you use the tools, for example to
    build the RTEMS kernel.

    The RSB by default will install (copy) the executables to a directory tree
    under the *prefix* you supply. To use the tools once finished just set your
    path to the ``bin`` directory under the *prefix* you use. In the examples
    that follow the *prefix* is ``$HOME/development/rtems/4.11`` and is set
    using the ``--prefix`` option so the path you need to configure to build
    applications can be set with the following in a BASH shell:

    .. code-block:: shell

      $ export PATH=$HOME/development/rtems/4.11/bin:$PATH

    Make sure you place the RTEMS tool path at the front of your path so they
    are searched first. RTEMS can provide newer versions of some tools your
    operating system provides and placing the RTEMS tools path at the front
    means it is searched first and the RTEMS needed versions of the tools are
    used.

.. note::

    RSB and RTEMS have a matching *git branch* for each version of RTEMS. For
    example, if you want to build a toolchain for 4.11, then you should
    checkout the 4.11 branch of the RSB:

    .. code-block:: shell

      $ git checkout -t origin/4.11

    Branches are available for the 4.9, 4.10, and 4.11 versions of RTEMS.

