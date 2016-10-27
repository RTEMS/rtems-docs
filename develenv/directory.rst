.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1989-2007.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Directory Structure
###################

The RTEMS directory structure is designed to meet the following requirements:

- encourage development of modular components.

- isolate processor and target dependent code, while allowing as much common
  source code as possible to be shared across multiple processors and target
  boards.

- allow multiple RTEMS users to perform simultaneous compilation of RTEMS and
  its support facilities for different processors and targets.

The resulting directory structure has processor and board dependent source
files isolated from generic files.  When RTEMS is configured and built, object
directories and an install point will be automatically created based upon the
target CPU family and BSP selected.

The placement of object files based upon the selected BSP name ensures that
object files are not mixed across CPUs or targets.  This in combination with
the makefiles allows the specific compilation options to be tailored for a
particular target board.  For example, the efficiency of the memory subsystem
for a particular target board may be sensitive to the alignment of data
structures, while on another target board with the same processor memory may be
very limited.  For the first target, the options could specify very strict
alignment requirements, while on the second the data structures could be
*packed* to conserve memory.  It is impossible to achieve this degree of
flexibility without providing source code.

The RTEMS source tree is organized based on the following variables:

- functionality,

- target processor family,

- target processor model,

- peripherals, and

- target board.

Each of the following sections will describe the contents of the directories in
the RTEMS source tree.  The top of the tree will be referenced as
``${RTEMS_ROOT}`` in this discussion.

.. code-block:: c

    rtems-VERSION
    |
    +--------+----+----+----+--+-----+---+-------+--------+
    |        |    |    |       |     |   |       |        |
    aclocal automake c contrib  cpukit doc make testsuites tools

``${RTEMS_ROOT}/aclocal/``
    This directory contains the custom M4 macros which are available to the
    various GNU autoconf ``configure.ac`` scripts throughout the RTEMS source
    tree.  GNU autoconf interprets ``configure.ac`` files to produce the
    ``configure`` files used to tailor RTEMS build for a particular host and
    target environment.  The contents of this directory will not be discussed
    further in this document.

``${RTEMS_ROOT}/automake/``
    This directory contains the custom GNU automake fragments which are used to
    support the various ``Makefile.am`` files throughout the RTEMS source tree.
    The contents of this directory will not be discussed further in this
    document.

``${RTEMS_ROOT}/c/``
    This directory is the root of the portions of the RTEMS source tree which
    must be built tailored for a particular CPU model or BSP.  The contents of
    this directory will be discussed in the `c/ Directory`_ section.

``${RTEMS_ROOT}/contrib/``
    This directory contains contributed support software.  Currently this
    directory contains the RPM specifications for cross-compilers hosted on
    GNU/Linux that target various operating systems including MinGW, Cygwin,
    FreeBSD, and Solaris.  The cross-compilers produced using these
    specifications are then used in a Canadian cross build procedure to produce
    the various RTEMS toolsets on a GNU/Linux host.  This directory also
    contains RPM specifications for the prebuilt cross-compilation toolsets
    provided by the RTEMS project.  There are separate subdirectories for each
    of the components in the RTEMS Cross Compilation Environment unde the
    ``contrib/crossrpms/`` directory.  This directory is configured, built, and
    installed separately from the RTEMS executive and tests.  This directory
    will not be discussed further in this document.

``${RTEMS_ROOT}/cpukit/``
    This directory is the root for all of the "multilib'able" portions of
    RTEMS.  This is a GNU way of saying the contents of this directory can be
    compiled like the C Library (``libc.a``) and the functionality is neither
    CPU model nor BSP specific.  The source code for most RTEMS services reside
    under this directory.  The contents of this directory will be discussed in
    the `CPU Kit Directory`_ section.

``${RTEMS_ROOT}/doc/``
    This directory is the root for all RTEMS documentation.  The source for
    RTEMS is written in GNU TeXinfo and used to produce HTML, PDF, and "info"
    files.  The RTEMS documentation is configured, built, and installed
    separately from the RTEMS executive and tests.  The contents of this
    directory will be discussed in the `Documentation Directory`_ section.

``${RTEMS_ROOT}/make/``
    This directory contains files which support the RTEMS Makefile's.  From a
    user's perspective, the most important parts are found in the ``custom/``
    subdirectory.  Each ".cfg" file in this directory is associated with a
    specific BSP and describes the CPU model, compiler flags, and procedure to
    produce an executable for the target board.  These files are described in
    detail in the*RTEMS BSP and Device Driver Development Guide* and will not
    be discussed further in this document.

``${RTEMS_ROOT}/testsuites/``
    This directory contains the test suites for the various RTEMS APIs and
    support libraries.  The contents of this directory are discussed in the
    `testsuites/ Test Suites`_ section.

``${RTEMS_ROOT}/tools/``
    This directory contains RTEMS specific support utilities which execute on
    the development host.  These utilities are divided into subdirectories
    based upon whether they are used in the process of building RTEMS and
    applications, are CPU specific, or are used to assist in updating the RTEMS
    source tree and applications.  The support utilities used in the process of
    building RTEMS are described in :ref:`RTEMS Specific Utilities`.
    These are the only components of this subtree that will be discussed
    in this document.

c/ Directory
============

The ``${RTEMS_ROOT}/c/`` directory was formerly the root directory of all RTEMS
source code.  At this time, it contains the root directory for only those RTEMS
components which must be compiled or linked in a way that is specific to a
particular CPU model or board.  This directory contains the following
subdirectories:

``${RTEMS_ROOT}/c/src/``
    This directory is logically the root for the RTEMS components which are CPU
    model or board dependent.  Thus this directory is the root for the BSPs and
    the Ada Test Suites as well as CPU model and BSP dependent libraries.  The
    contents of this directory are discussed in the `c/src/ Directory`_
    section.

c/src/ Directory
----------------

As mentioned previously, this directory is logically the root for the RTEMS
components which are CPU model or board dependent.  The following is a list of
the subdirectories in this directory and a description of each.

``${RTEMS_ROOT}/c/src/aclocal/``
    This directory contains the custom M4 macros which are available to the
    various GNU autoconf ``configure.ac`` scripts throughout this portion of
    the RTEMS source tree.  GNU autoconf interprets``configure.ac`` files to
    produce the ``configure`` files used to tailor RTEMS build for a particular
    host and target environment.  The contents of this directory will not be
    discussed further in this document.

``${RTEMS_ROOT}/c/src/ada/``
    This directory contains the Ada95 language bindings to the RTEMS Classic
    API.

``${RTEMS_ROOT}/c/src/ada-tests/``
    This directory contains the test suite for the Ada language bindings to the
    Classic API.

``${RTEMS_ROOT}/c/src/automake/``
    This directory contains files which are "Makefile fragments."  They are
    included as required by the various ``Makefile.am`` files throughout this
    portion of the RTEMS source tree.

``${RTEMS_ROOT}/c/src/lib/``
    This directory contains the directories ``libbsp/`` and ``libcpu/`` which
    contain the source code for the Board Support Packages (BSPs) and CPU Model
    specific source code for RTEMS.  The ``libbsp/`` is organized based upon
    the CPU family and boards BSPs.  The contents of ``libbsp/`` are discussed
    briefly in `c/src/lib/libbsp BSP Directory`_ and presented in detail in
    the*RTEMS BSP and Device Driver Development Guide*.  The ``libcpu/``
    directory is also organized by CPU family with further divisions based upon
    CPU model and features that are shared across CPU models such as caching
    and DMA.

``${RTEMS_ROOT}/c/src/libchip/``
    This directory contains device drivers for various peripheral chips which
    are designed to be CPU and board dependent.  This directory contains a
    variety of drivers for serial devices, network interface controllers,
    shared memory and real-time clocks.

``${RTEMS_ROOT}/c/src/librtems++/``
    This directory contains C++ classes which map to the RTEMS Classic API.

``${RTEMS_ROOT}/c/src/make/``
    This directory is used to generate the bulk of the supporting rules files
    which are installed as part of the Application Makefiles.  This file
    contains settings for various Makefile variables to tailor them to the
    particular CPU model and BSP configured.

``${RTEMS_ROOT}/c/src/nfsclient/``
    This directory contains a Network File System (NFS) client for RTEMS.  With
    this file system, a user's application can access files on a remote
    computer.

``${RTEMS_ROOT}/c/src/optman/``
    This directory contains stubs for the RTEMS Classic API Managers which are
    considered optional and whose use may be explicitly forbidden by an
    application.  All of the directive implementations in this Optional
    Managers return ``E_NOTCONFIGURED``.

``${RTEMS_ROOT}/c/src/support/``
    This directory exists solely to generate the RTEMS version string which
    includes the RTEMS version, CPU architecture, CPU model, and BSP name.

``${RTEMS_ROOT}/c/src/wrapup/``
    This directory is responsible for taking the individual libraries and
    objects built in each of the components in the RTEMS source tree and
    bundling them together to form the single RTEMS library ``librtemsbsp.a``.
    This library contains all BSP and CPU model specific software.

c/src/lib/libbsp BSP Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "libbsp" directory contains a directory for each CPU family supported by
RTEMS.  Beneath each CPU directory is a directory for each BSP for that
processor family.

The "libbsp" directory provides all the BSPs provided with this release of the
RTEMS executive.  The subdirectories are divided, as discussed previously,
based on specific processor family, then further broken down into specific
target board environments.  The "no_cpu" subdirectory provides a starting point
template BSP which can be used to develop a specific BSP for an unsupported
target board.  The files in this subdirectory may aid in preliminary testing of
the RTEMS development environment that has been built for no particular target
in mind.

Below each CPU dependent directory is a directory for each target BSP supported
in this release.

Each BSP provides the modules which comprise an RTEMS BSP.  The modules are
separated into the subdirectories "clock", "console", "include", "shmsupp",
"startup", and "timer" as shown in the following figure:

.. code-block:: c

    Each BSP
    |
    +-----------+----------+-----+-----+----------+----------+
    |           |          |           |          |          |
    clock      console    include     shmsupp    startup     timer

CPU Kit Directory
=================

The @code{cpukit/} directory structure is as follows:

.. code-block:: c

    cpukit
    |
    +-----------+----------+-----------+----------+
    |           |          |           |          |
    posix       rtems       sapi       score     wrapup

The ``cpukit/`` directory contains a set of subdirectories which contains the
source files comprising the executive portion of the RTEMS development
environment as well as portable support libraries such as support for the C
Library and filesystems.  The API specific and "SuperCore" (e.g. ``score/``
directory) source code files are separated into distinct directory trees.

The following is a description of each of the subdirectories under ``cpukit/``:

``${RTEMS_ROOT}/cpukit/aclocal/``
    This directory contains the custom M4 macros which are available to the
    various GNU autoconf ``configure.ac`` scripts throughout the CPU Kit
    portion of the RTEMS source tree.  GNU autoconf interprets ``configure.ac``
    files to produce the ``configure`` files used to tailor RTEMS build for a
    particular host and target environment.  The contents of this directory
    will not be discussed further in this document.

``${RTEMS_ROOT}/cpukit/automake/``
    This directory contains files which are "Makefile fragments."  They are
    included as required by the various ``Makefile.am`` files throughout the
    CPU Kit portion of the RTEMS source tree.

``${RTEMS_ROOT}/cpukit/ftpd/``
    This directory contains the RTEMS ftpd server.

``${RTEMS_ROOT}/cpukit/httpd/``
    This directory contains the port of the GoAhead web server to RTEMS.

``${RTEMS_ROOT}/cpukit/include/``
    This directory contains header files which are private to RTEMS and not
    considered to be owned by any other component in the CPU Kit.

``${RTEMS_ROOT}/cpukit/libblock/``
    This directory contains support code for using Block Devices such as hard
    drives, floppies, and CD-ROMs.  It includes the generic IO primitives for
    block device drivers, disk caching support, and a RAM disk block device
    driver.

``${RTEMS_ROOT}/cpukit/libcsupport/``
    This directory contains the RTEMS specific support routines for the Newlib
    C Library.  This includes what are referred to as system calls and found in
    section 2 of the traditional UNIX manual.  In addition, it contains a
    thread-safe implementation of the Malloc family of routines as well as BSD
    and POSIX services not found in Newlib.

``${RTEMS_ROOT}/cpukit/libfs/``
    This directory contains the various non-networked filesystem
    implementations for RTEMS.  It includes the In-Memory FileSystem (IMFS),
    the mini-IMFS, and FAT filesystems.

``${RTEMS_ROOT}/cpukit/libi2c/``
    This directory contains the RTEMS I2C framework.

``${RTEMS_ROOT}/cpukit/libmd/``
    This directory contains a port of the standard MD5 checksum code.

``${RTEMS_ROOT}/c/src/libmisc/``
    This directory contains support facilities which are RTEMS specific but
    otherwise unclassified.  In general, they do not adhere to a standard API.
    Among the support facilities in this directory are a ``/dev/null`` device
    driver, the Stack Overflow Checker, a mini-shell, the CPU and rate
    monotonic period usage monitoring libraries, and a utility to "dump a
    buffer" in a nicely formatted way similar to many ROM monitors.

``${RTEMS_ROOT}/cpukit/libnetworking/``
    This directory contains the port of the FreeBSD TCP/IP stack to RTEMS.

``${RTEMS_ROOT}/cpukit/librpc/``
    This directory contains the port of the FreeBSD RPC/XDR source to RTEMS.

``${RTEMS_ROOT}/cpukit/libpci/``
    This directory contains RTEMS PCI Library.

``${RTEMS_ROOT}/cpukit/posix/``
    This directory contains the RTEMS implementation of the threading portions
    of the POSIX API.

``${RTEMS_ROOT}/cpukit/pppd/``
    This directory contains a port of the free implementation of the PPPD
    network protocol.

``${RTEMS_ROOT}/cpukit/rtems/``
    This directory contains the implementation of the Classic API.

``${RTEMS_ROOT}/cpukit/sapi/``
    This directory contains the implementation of RTEMS services which are
    required but beyond the realm of any standardization efforts.  It includes
    initialization, shutdown, and IO services.

``${RTEMS_ROOT}/cpukit/score/``
    This directory contains the "SuperCore" of RTEMS.  All APIs are implemented
    in terms of SuperCore services.  For example, Classic API tasks and POSIX
    threads are all implemented in terms of SuperCore threads.  This provides a
    common infrastructure and a high degree of interoperability between the
    APIs.  For example, services from all APIs may be used by any task/thread
    independent of the API used to create it.  Within the ``score/`` directory
    the CPU dependent modules are found.  The ``score/cpu/`` subdirectory
    contains a subdirectory for each target CPU supported by this release of
    the RTEMS executive.  Each processor directory contains the CPU dependent
    code necessary to host RTEMS.  The ``no_cpu`` directory provides a starting
    point for developing a new port to an unsupported processor.  The files
    contained within the ``no_cpu`` directory may also be used as a reference
    for the other ports to specific processors.

``${RTEMS_ROOT}/cpukit/shttpd/``
    This directory contains the port of the Simple HTTPD web server to RTEMS.

``${RTEMS_ROOT}/cpukit/telnetd/``
    This directory contains the RTEMS telnetd server.

``${RTEMS_ROOT}/cpukit/wrapup/``
    This directory is responsible for taking the individual libraries and
    objects built in each of the components in the RTEMS CPU Kit source tree
    and bundling them together to form the single RTEMS library
    ``librtemscpu.a``.  This library contains all BSP and CPU model specific
    software.

``${RTEMS_ROOT}/cpukit/zlib/``
    This directory contains a port of the GNU Zlib compression library to
    RTEMS.

testsuites/ Test Suites
=======================

This directory provides all of the RTEMS Test Suite except those for the
Classic API Ada95 binding This includes the single processor tests,
multiprocessor tests, timing tests, library tests, and sample tests.
Additionally, subdirectories for support functions and test related header
files are provided.  The following table lists the test suites currently
included with the RTEMS and the directory in which they may be located:

``${RTEMS_ROOT}/testsuites/libtests/``
    This directory contains the test suite for the various RTEMS support
    components.

``${RTEMS_ROOT}/testsuites/mptests/``
    This directory contains the test suite for the multiprocessor support in
    the Classic API.  The tests provided address two node configurations and
    provide coverage for the multiprocessor code found in RTEMS.

``${RTEMS_ROOT}/testsuites/psxtests/``
    This directory contains the test suite for the RTEMS POSIX API.

``${RTEMS_ROOT}/testsuites/samples/``
    This directory provides sample application tests which aid in the testing a
    newly built RTEMS environment, a new BSP, or as starting points for the
    development of an application using the RTEMS executive.  They are
    discussed in `Sample Applications`_.

``${RTEMS_ROOT}/testsuites/sptests/``
    This directory contains the test suite for the RTEMS Classic API when
    executing on a single processor.  The tests were originally designed to
    provide near complete test coverage for the entire executive code.  With
    the addition of multiple APIs, this is no longer the case as some SuperCore
    functionality is not available through the Classic API.  Thus some
    functionality in the SuperCore is only covered by tests in the POSIX API
    Test Suites.

``${RTEMS_ROOT}/testsuites/support/``
    This directory contains support software and header files for the various
    test suites.

``${RTEMS_ROOT}/testsuites/tmtests/``
    This directory contains the timing test suite for the RTEMS Classic API.
    This include tests that benchmark each directive in the Classic API as well
    as a set of critical SuperCore functions.  These tests are important for
    helping to verify that RTEMS performs as expected on your target hardware.
    It is not uncommon to discover mistakes in board initialization such as
    caching being disabled as a side-effect of analyzing the results of these
    tests.

``${RTEMS_ROOT}/testsuites/tools/``
    This directory contains tools which execute on the development host and aid
    in executing and evaluating the results of the test suite.  The tools
    ``difftest`` compares the output of one or more tests with the expected
    output.  If you place the output of all the ``tmtests/`` in a single file,
    then the utility ``sorttimes`` will be able to produce a report organizing
    the execution times by manager.

Documentation Directory
=======================

This directory contains the source code for all RTEMS documentation in
``TexInfo`` format as well as utilities used in the generation of the RTEMS
documentation set.  This source code is used to produce the RTEMS documentation
in various formats including PDF, HTML, and PostScript.

``${RTEMS_ROOT}/doc/ada_user/``
    This directory contains the source code for the *RTEMS Applications Ada
    User's Guide* which documents the Ada95 binding to the Classic API.  This
    manual is produced from from the same source base as the *RTEMS Application
    C User's Guide*.

``${RTEMS_ROOT}/doc/bsp_howto/``
    This directory contains the source code for the*RTEMS BSP and Device Driver
    Development Guide*.

``${RTEMS_ROOT}/doc/common/``
    This directory contains the source code for the files which are shared
    across multiple manuals in the RTEMS Documentation Set.  This includes the
    copyright page as well as the timing tables which can be filled in on a per
    BSP basis in the CPU supplements.

``${RTEMS_ROOT}/doc/cpu_supplement/``
    This directory contains the source code for the RTEMS CPU Supplement.

``${RTEMS_ROOT}/doc/develenv/``
    This directory contains the source code for the*RTEMS Development
    Environment Guide*.  This is the document you are currently reading.

``${RTEMS_ROOT}/doc/filesystem/``
    This directory contains the source code for the*RTEMS Filesystem Design
    Guide*.  This manual is a continuous work in process as it attempts to
    capture the design of the interface between system calls and filesystem
    implementations as well as the information required by those implementing
    filesystems.

``${RTEMS_ROOT}/doc/images/``
    This directory contains the source code for the graphics used in the HTML
    version of the RTEMS Documentation.

``${RTEMS_ROOT}/doc/networking/``
    This directory contains the source code for the*RTEMS Network Supplement*.

``${RTEMS_ROOT}/doc/new_chapters/``
    This directory contains the source code for the new documentation
    components which have not yet been collected into a new manual or merged
    into an existing document.  Currently, this primarily contains draft
    documentation for some portions of the facilities implemented in
    ``${RTEMS_ROOT}/c/src/libmisc/``.

``${RTEMS_ROOT}/doc/porting/``
    This directory contains the source code for the*RTEMS Porting Guide*.

``${RTEMS_ROOT}/doc/posix1003.1/``
    This directory contains the source code for the*RTEMS POSIX 1003.1
    Compliance Guide*.

``${RTEMS_ROOT}/doc/posix_users/``
    This directory contains the source code for the*RTEMS POSIX API User's
    Guide*.  It is important to note that RTEMS' support for POSIX is a
    combination of functionality provided by RTEMS and the Newlib C Library so
    some functionality is documented by Newlib.

``${RTEMS_ROOT}/doc/relnotes/``
    This directory contains the source code for a formally release notes
    document.  This has not been used for recent RTEMS releases.

``${RTEMS_ROOT}/doc/started/``
    This directory contains the source code for the*Getting Started with RTEMS
    for C/C++ Users* manual.

``${RTEMS_ROOT}/doc/tools/``
    This directory contains the source code for the tools used on the
    development host to assist in producing the RTEMS Documentation.  The most
    important of these tools is ``bmenu`` which generates the hierarchical node
    linking commands based upon chapter, section, and subsection organization.

``${RTEMS_ROOT}/doc/user/``
    This directory contains the source code for the *RTEMS Applications C
    User's Guide* which documents the Classic API.
