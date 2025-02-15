.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Chris Johns

.. _BSPs:

Deployment
**********
.. index:: Deployment
.. index:: packages

Deployment is a process companies, organizations or teams use to
control and manage delivery of RTEMS tools, kernels and third party
libraries. Deployed tools, kernels and libraries are packaged and
controlled so the same tools and libraries are used in all phases of a
project.

The Quick Start guide details how tools are built using the RSB. The
tools are installed on your development computer and available for you
to build applications. That build can be viewed as the simplest form
of deployment because it is simple and easy however it does not
scale. Building the tools and kernel on each development machine in a
project or company is time consuming, difficult to get right and
costly to audit.

This section covers the building of tools, kernels and third party
libraries using the RSB for deployment. Custom RSB buildset files are
supported across releases giving you an easy update path. The RSB can
generate a single tarfile for any prefix without needing to install
the pieces built helping ease integration with packaging systems and
continuous integration (CI) for automated workflows.

RSB Deployment
--------------

The RSB provides support for deployment using custom buildset files. A
custom buildset file resides outside the RSB and can build tools for a
number of architectures and kernels for BSPs. Deployment can include
third party libraries if a single BSP is being built.

The RSB ``--no-install`` option builds the tools and kernel without
the final installation phase. A prefix that is not accessible when
running the RSB can be used. This is important if a CI flow is being
used.

The buildset tar file option ``--bset-tar-file`` packages the build's
staging directory tree into a single tar file. The tar file can be
used as the input source to a packaging system.

Buildset configuration files can be tested by adding the ``--dry-run``
option to the ``sb-set-builder`` command line.

The buildset examples that follow assume the prefix path used does not
exist or is not writable and the environment path does not include any
RTEMS tools.

Deployment Repository
^^^^^^^^^^^^^^^^^^^^^

Create a repository to hold a project's buildset configuration
files:

.. code-block:: none

    $ mkdir a-project
    $ cd a-project
    $ git init

Add the RSB as a sub-module:

.. code-block:: none

    $ git submodule add \
      ssh://git@gitlab.rtems.org:2222/rtems/tools/rtems-source-builder.git

Create a configuration directory:

.. code-block:: none

    $ mkdir config
    $ git add config

Tools Configuration
^^^^^^^^^^^^^^^^^^^

This example will build a single tool set with a local configuration
file.

Create a configuration file for the ``project``:

.. code-block:: none

    $ vi config/project-tools.bset

Add the following to the buildset configuration file:

.. code-block:: none

    #
    # Project Tools
    #
    @rtems-ver-major@/rtems-aarch64

Commit the changes to the repository:

.. code-block:: none

   $ git add config/project-tools.bset
   $ git commit -m "Add project aarch64 tools buildset"

Build a tarfile containing the tools using the RSB submodule:

.. code-block:: none

   $ ./rtems-source-builder/source-builder/sb-set-builder \
       --prefix=/opt/project --log=project.txt \
       --bset-tar-file --no-install \
       project-tools

Once the build has finished the ``tar`` directory will contain the
``project`` tools in a tarfile:

.. code-block:: none

   $ ls tar
   project-tools.tar.bz2

Inspect the tarfile to check the path matches the prefix used to build
the tools (sizes may vary):

.. code-block:: none

   $ tar Jtvf tar/project-tools.tar.bz2 | less
   drwxr-xr-x  0 chris  eng        0 Sep  6 14:27 opt/project/bin/
   -rwxr-xr-x  0 chris  eng  1320888 Sep  6 14:20 opt/project/bin/aarch64-rtems@rtems-ver-major@-addr2line
   -rwxr-xr-x  0 chris  eng  1358688 Sep  6 14:20 opt/project/bin/aarch64-rtems@rtems-ver-major@-ar
   -rwxr-xr-x  0 chris  eng  2381976 Sep  6 14:20 opt/project/bin/aarch64-rtems@rtems-ver-major@-as
   -rwxr-xr-x  0 chris  eng  1328440 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-c++
   -rwxr-xr-x  0 chris  eng  1316240 Sep  6 14:20 opt/project/bin/aarch64-rtems@rtems-ver-major@-c++filt
   -rwxr-xr-x  0 chris  eng  1328440 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-cpp
   -rwxr-xr-x  0 chris  eng    60792 Sep  6 14:20 opt/project/bin/aarch64-rtems@rtems-ver-major@-elfedit
   -rwxr-xr-x  0 chris  eng  1328440 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-g++
   -rwxr-xr-x  0 chris  eng  1328440 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-gcc
   -rwxr-xr-x  0 chris  eng  1328440 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-gcc-12.1.1
   -rwxr-xr-x  0 chris  eng    48568 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-gcc-ar
   -rwxr-xr-x  0 chris  eng    48568 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-gcc-nm
   -rwxr-xr-x  0 chris  eng    48576 Sep  6 14:27 opt/project/bin/aarch64-rtems@rtems-ver-major@-gcc-ranlib
   .....

Tools and Kernel
^^^^^^^^^^^^^^^^

This example builds a single tool set and an RTEMS kernel for a BSP
using a buildset defined BSP settings.

We use the same ``a-project`` repository from the previous example and
add a new configuration. Add a configuration file to build the tools
and a BSP:

.. code-block:: none

   $ vi config/project-tools-bsp.bset

Add the following to the buildset configuration file and save:

.. code-block:: none

   #
   # Project Tools and BSP
   #
   %define with_rtems_bsp     aarch64/versal_aiedge
   %define with_rtems_bspopts BSP_XILINX_VERSAL_NOCACHE_LENGTH=0x4000000 \
                              BSP_XILINX_VERSAL_RAM_LENGTH=0x200000000
   @rtems-ver-major@/rtems-aarch64
   @rtems-ver-major@/rtems-kernel

The configuration provides BSP options. Commit the changes to the
repository:

.. code-block:: none

   $ git add config/project-tools-bsp.bset
   $ git commit -m "Add project tools and BSP buildset"

Build a tarfile of the tools and BSP using the RSB submodule:

.. code-block:: none

   $ ./rtems-source-builder/source-builder/sb-set-builder \
       --prefix=/opt/project --log=project.txt \
       --bset-tar-file --no-install \
       project-tools-bsp

A buildset configuration file that uses buildset BSP defines is
limited to a single architecture and the tools built need to match the
architecture of the BSP.

You can specify more than one BSP to be built. An updated
configuration could be:

.. code-block:: none

   %define with_rtems_bsp     aarch64/versal_aiedge \
                              aarch64/zynqmp_apu

This is useful when deploying more than one BSP. If you need multiple
architectures and BSPs consider the Tools and Kernel With Config
example.

Buildset BSP options are applied to all BSPs in the BSP list. If they
are specific to a BSP only specify a single BSP in the BSP define.

RTEMS 5 supports this type of buildset file.

Tools and Kernel with Config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example builds tool sets for different architectures and multiple
BSPs for the architectures using a kernel configuration INI file.

Tools for the ``arch64`` and ``arm`` architectures are built and three
BSPs each with different options.

We use the same ``a-project`` repository from the previous example and
add the new configurations. Add a configuration file to build the
tools and BSPs:

.. code-block:: none

   $ vi config/project-tools-bsp-config.bset

Add the following to the buildset configuration file and save:

.. code-block:: none

   #
   # Project Tools and BSPs
   #
   %define with_rtems_bsp_config config/project-bsps.ini
   @rtems-ver-major@/rtems-aarch64
   @rtems-ver-major@/rtems-arm
   @rtems-ver-major@/rtems-kernel

Add a kernel configuration INI file:

.. code-block:: none

   $ vi config/project-bsps.bset

Add the following to the kernel configuration INI file and save:

.. code-block:: none

   #
   # Project BSPs
   #
   [DEFAULT]
   RTEMS_POSIX_API = True
   BUILD_SAMPLES = True
   BUILD_TESTS = False

   [aarch64/versal_aiedge]
   BSP_XILINX_VERSAL_NOCACHE_LENGTH = 0x4000000
   BSP_XILINX_VERSAL_RAM_LENGTH = 0x200000000

   [aarch64/zynqmp_apu]
   RTEMS_SMP = True

   [arm/xilinx_zynq_zc706]
   RTEMS_SMP = True
   BSP_XILINX_VERSAL_NOCACHE_LENGTH = 0x4000000
   BSP_XILINX_VERSAL_RAM_LENGTH = 0x200000000

Commit the changes to the repository:

.. code-block:: none

   $ git add config/project-tools-bsp-config.bset
   $ git add config/project-bsps.ini
   $ git commit -m "Add project tools and BSPs buildset and kernel config"

Build a tarfile of the tools and BSPs using the RSB submodule:

.. code-block:: none

   $ ./rtems-source-builder/source-builder/sb-set-builder \
       --prefix=/opt/project --log=project.txt \
       --bset-tar-file --no-install \
       project-tools-bsp-config

Tools, Kernel and Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^

Third party libraries can be built as part of a single RSB
configuration if only one BSP is built at a time. The RSB support for
building packages does not support building for multiple BSPs.

We use the same ``a-project`` repository from the previous example and
add a new configuration. Add a configuration file to build the tools,
BSPs and LibBSD:

.. code-block:: none

   $ vi config/project-aarch64-tools-bsp-libbsd.bset

Add the following to the buildset configuration file and save:

.. code-block:: none

   #
   # Project Tools, BSP and LibBSD
   #
   %define with_rtems_bsp     aarch64/versal_aiedge
   %define with_rtems_bspopts BSP_XILINX_VERSAL_NOCACHE_LENGTH=0x4000000 \
                              BSP_XILINX_VERSAL_RAM_LENGTH=0x200000000
   6/rtems-aarch64
   6/rtems-kernel
   6/rtems-libbsd

Commit the changes to the repository:

.. code-block:: none

   $ git add config/project-aarch64-tools-bsp-libbsd.bset
   $ git commit -m "Add project aarch64 tools, BSP and libbsd"

Build a tarfile of the tools, BSP and LibBSD using the RSB
submodule:

.. code-block:: none

   $ ./rtems-source-builder/source-builder/sb-set-builder \
       --prefix=/opt/project --log=project.txt \
       --bset-tar-file --no-install \
       project-aarch64-tools-bsp-libbsd

The tarfile can be reviewed to see the BSP libraries built (sizes may vary):

.. code-block:: none

   $ tar jtvf tar/project-aarch64-tools-bsp-libbsd.tar.bz2 | \
              grep -e '\.a$' | grep -e 'versal_aiedge'
   -rw-r--r--  0 chris  eng 138936312 Sep  7 14:58 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libbsd.a
   -rw-r--r--  0 chris  eng    686190 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libdebugger.a
   -rw-r--r--  0 chris  eng    164086 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libftpd.a
   -rw-r--r--  0 chris  eng    107560 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libftpfs.a
   -rw-r--r--  0 chris  eng    978812 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libjffs2.a
   -rw-r--r--  0 chris  eng    412354 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libmghttpd.a
   -rw-r--r--  0 chris  eng   2099962 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/librtemsbsp.a
   -rw-r--r--  0 chris  eng  29693496 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/librtemscpu.a
   -rw-r--r--  0 chris  eng    435236 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/librtemscxx.a
   -rw-r--r--  0 chris  eng    141234 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/librtemsdefaultconfig.a
   -rw-r--r--  0 chris  eng    856514 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/librtemstest.a
   -rw-r--r--  0 chris  eng    159004 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libtelnetd.a
   -rw-r--r--  0 chris  eng    137386 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libtftpfs.a
   -rw-r--r--  0 chris  eng    476692 Sep  7 14:56 opt/project/aarch64-rtems@rtems-ver-major@/versal_aiedge/lib/libz.a

Tools, Kernel with Config and Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example builds the tools, kernel and LibBSD using an RSB
configuration file and a kernel configuration file. The kernel
configuration provides easier kernel and BSP option management.

Third party libraries can be built as part of a single RSB
configuration if only one BSP is built at a time. The RSB support for
building packages does not support building for multiple BSPs.

We use the same ``a-project`` repository from the previous example and
add a new configuration. Add a configuration file to build the tools,
BSPs and LibBSD:

.. code-block:: none

   $ vi config/project-aarch-tools-bsp-libbsd-config.bset

Add the following to the buildset configuration file and save:

.. code-block:: none

   #
   # Project Tools, BSP and LibBSD
   #
   %define with_rtems_bsp_config config/project-aarch64-bsp.ini
   6/rtems-aarch64
   6/rtems-kernel
   6/rtems-libbsd

Add a kernel configuration INI file:

.. code-block:: none

   $ vi config/project-aarch64-bsp.bset

Add the following kernel configuration INI file and save:

.. code-block:: none

   #
   # Project Versal AI Edge BSP
   #
   [DEFAULT]
   RTEMS_POSIX_API = True
   BUILD_SAMPLES = True
   BUILD_TESTS = False

   [aarch64/versal_aiedge]
   BSP_XILINX_VERSAL_NOCACHE_LENGTH = 0x4000000
   BSP_XILINX_VERSAL_RAM_LENGTH = 0x200000000

Commit the changes to the repository:

.. code-block:: none

   $ git add config/project-aarch64-tools-bsp-libbsd-config.bset
   $ git add config/project-aarch64-bsp.ini
   $ git commit -m "Add project aarch64 tools, BSP (with config) and libbsd"

Build the tarfile of the tools, BSP and LibBSD using the RSB
submodule:

.. code-block:: none

   $ ./rtems-source-builder/source-builder/sb-set-builder \
       --prefix=/opt/project --log=project.txt \
       --bset-tar-file --no-install \
       project-aarch64-tools-bsp-libbsd-config
