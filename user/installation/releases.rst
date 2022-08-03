.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _released-version:

Releases
========
.. index:: tarball
.. index:: release

RTEMS releases provide a stable version of the kernel for the supported
architectures. RTEMS maintaines the current and previous releases. Support for
older releases is provided using the RTEMS support channels.

Please read :ref:`development-host` before continuing. The following procedure
assumes you have installed and configured your host operating. It also assumes
you have installed any dependent packages needed when building the tools and
the kernel.

You need to select a location to build and install the RTEMS Tool chain and
RTEMS. Make sure there is plenty of disk space and a fast disk is
recommended. Our procedure will document building and installing the tools in a
base directory called :file:`/opt/rtems`. This path will require root
access. If you are working on a machine you do not have root access to you can
use a home directory, If building on Windows use :file:`/c/opt/rtems` to keep
the top level paths as short as possible. :ref:`windows-path-length` provides
more detail about path lengths on Windows.

The location used to install the tools and kernel is called the `prefix`.
:ref:`QuickStartPrefixes` explains prefixes and how to use them. It is best to
have a `prefix` for each different version of RTEMS you are using. If you are
using RTEMS in production it is **not** a good idea to install a development
version of over the top by using the same `prefix`. A separate `prefix` for each
version avoids this.

Released versions of the RTEMS Source Builder (RSB) download all source code
for all packages from the :r:url:`ftp` rather than from the package's home
site. Hosting all the source on the :r:url:`ftp` ensures the source is present
for the life of the release on the :r:url:`ftp`. If there is a problem
accessing the RTEMS FTP the RSB will fall back to the packages home site.

The :r:url:`ftp` is hosted at the Oregon State University's The Open Source Lab
(http://osuosl.org/). This is a nonprofit organization working for the
advancement of open source technologies and RTEMS is very fortunate to be
shosted here. It has excellent internet access and performance.

.. note:: **Controlling the RTEMS Kernel Build**

   Building RSB releases by default does not build the RTEMS kernel. To build
   the RTEMS kernel add the ``--with-rtems`` option to the RSB command line.

   By default all the BSPs for an architecture are built. If you only wish to
   have a specific BSP built you can specify the BSP list by providing to the
   RSB the option ``--with-rtemsbsp``. For example to build two BSPs for the
   SPARC architecture you can supply ``--with-rtemsbsp="erc32 leon3"``. This can
   speed the build time up for some architectures that have a lot of BSPs.

Once you have built the tools and kernel you can move to the Packages section
of the manual.

RTEMS Tools and Kernel
----------------------

This procedure will build a SPARC tool chain. Set up a suitable workspace to
build the release in. On Unix:

.. code-block:: none

 $ cd
 $ mkdir -p development/rtems/releases
 $ cd development/rtems/releases

If building on Windows:

.. code-block:: none

 $ cd /c
 $ mkdir -p opt/rtems
 $ cd opt/rtems

**Note** the paths on Windows will be different to those shown.

Download the RTEMS Source Builder (RSB) from the RTEMS FTP server:

.. code-block:: none

 $ wget https://ftp.rtems.org/pub/rtems/releases/@rtems-ver-major@/@rtems-ver-majminrev@/rtems-source-builder-@rtems-ver-majminrev@.tar.xz
 --2016-03-21 10:50:04-- https://ftp.rtems.org/pub/rtems/releases/@rtems-ver-major/@rtems-ver-majminrev@/rtems-source-builder-@rtems-ver-majminrev@.tar.xz
 Resolving ftp.rtems.org (ftp.rtems.org)... 140.211.10.151
 Connecting to ftp.rtems.org (ftp.rtems.org)|140.211.10.151|:443... connected.
 HTTP request sent, awaiting response... 200 OK
 Length: 967056 (944K) [application/x-xz]
 Saving to: 'rtems-source-builder-@rtems-ver-majminrev@.tar.xz'

 rtems-source-builder-@rtems-ver-majminrev@ 100%[====================================>] 944.39K 206KB/s   in 5.5s

 2016-03-21 10:50:11 (173 KB/s) - 'rtems-source-builder-@rtems-ver-majminrev@.tar.xz' saved [967056/967056]

On Unix unpack the RSB release tar file using:

.. code-block:: none

 $ tar Jxf rtems-source-builder-@rtems-ver-majminrev@.tar.xz
 $ cd rtems-source-builder-@rtems-ver-majminrev@/rtems/

On Windows you need to shorten the path (See :ref:`windows-path-length`) after
you have unpacked the tar file:

.. code-block:: none

 $ tar Jxf rtems-source-builder-@rtems-ver-majminrev@.tar.xz
 $ mv rtems-source-builder-@rtems-ver-majminrev@ @rtems-ver-majminrev@
 $ cd @rtems-ver-majminrev@

Build a tool chain for the SPARC architecure. We are using the SPARC
architecture in our example because GDB has a good simulator that lets us run
and test the samples RTEMS builds by default

If building on Windows add ``--jobs=none`` to avoid GNU make issues on Windows
discussed in :ref:`msys2_parallel_builds`.

.. code-block:: none

 $ ../source-builder/sb-set-builder \
     --prefix=/opt/rtems/@rtems-ver-major@ @rtems-ver-major@/rtems-sparc

You can now build a third-party library or an application as defaulted in TBD.
