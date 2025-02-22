% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1989, 2007 On-Line Applications Research Corporation (OAR)

# Directory Structure

The RTEMS directory structure is designed to meet the following requirements:

- encourage development of modular components.
- isolate processor and target dependent code, while allowing as much common
  source code as possible to be shared across multiple processors and target
  boards.
- allow multiple RTEMS users to perform simultaneous compilation of RTEMS and
  its support facilities for different processors and targets.

The resulting directory structure has processor and board dependent source
files isolated from generic files. When RTEMS is configured and built, object
directories and an install point will be automatically created based upon the
target CPU family and BSP selected.

The placement of object files based upon the selected BSP name ensures that
object files are not mixed across CPUs or targets. This in combination with
the makefiles allows the specific compilation options to be tailored for a
particular target board. For example, the efficiency of the memory subsystem
for a particular target board may be sensitive to the alignment of data
structures, while on another target board with the same processor memory may be
very limited. For the first target, the options could specify very strict
alignment requirements, while on the second the data structures could be
*packed* to conserve memory. It is impossible to achieve this degree of
flexibility without providing source code.

The RTEMS source tree is organized based on the following variables:

- functionality,
- target processor family,
- target processor model,
- peripherals, and
- target board.

Each of the following sections will describe the contents of the directories in
the RTEMS source tree. The top of the tree will be referenced as
`${RTEMS_ROOT}` in this discussion.

```c
rtems-VERSION
|
+----+----+----+--+-----+---+-------+--------+
|    |    |       |     |   |       |        |
c contrib  cpukit doc make testsuites tools
```

`${RTEMS_ROOT}/c/`
: Historically, this directory was the root of the portions of the
  RTEMS source tree which must be built tailored for a particular CPU
  model or BSP. In the current source, only the build support files for
  the autoconf/automake based build system remain in this subdirectory.

`${RTEMS_ROOT}/cpukit/`
: This directory is the root for all of the "multilib'able" portions of
  RTEMS. This is a GNU way of saying the contents of this directory can be
  compiled like the C Library (`libc.a`) and the functionality is neither
  CPU model nor BSP specific. The source code for most RTEMS services reside
  under this directory. The contents of this directory will be discussed in
  the [CPU Kit Directory] section.

`${RTEMS_ROOT}/bsps`
: This directory is the root for all of the BSP specific source in
  RTEMS. The contents of this directory are discussed in the \[BSPs
  Directory\][bsps directory] section.

`${RTEMS_ROOT}/make/`
: This directory contains files which support RTEMS Makefile's. From a
  user's perspective, the most important part is the BSP specific
  information found in the `config` subdirectory of each BSP.
  Each ".cfg" file is associated with a specific BSP
  and describes the CPU model, and compiler flags used to produce
  an executable for the target board. These files are described in
  detail in the *RTEMS BSP and Driver Guide* and will not be discussed
  further in this document.

`${RTEMS_ROOT}/testsuites/`
: This directory contains the test suites for the various RTEMS APIs and
  support libraries. The contents of this directory are discussed in the
  [testsuites/ Test Suites] section.

## BSPs Directory

The "bsps" directory contains a directory for each CPU family supported by
RTEMS. Beneath each CPU directory is a directory for each BSP for that
processor family.

The "bsps" directory provides all the BSPs provided with this release
of RTEMS. The subdirectories are divided, as discussed previously,
based on specific processor family, then further broken down into specific
target board environments. The "no_cpu" subdirectory provides a starting
point template BSP which can be used to develop a specific BSP for an
unsupported target board. The files in this subdirectory may aid in
preliminary testing of the RTEMS development environment that has been
built for no particular target in mind.

Below each CPU dependent directory is a directory for each target BSP supported
in this release.

Each BSP provides the modules which comprise an RTEMS BSP. The modules are
separated into various subdirectories such as "clock", "console",
"include", "shmsupp", "startup", and "timer" as shown in the following
figure:

```c
Each BSP
|
+-----------+----------+-----+-----+----------+----------+
|           |          |           |          |          |
clock      console    include     shmsupp    startup     timer
```

### CPU Kit Directory

The @code{cpukit/} directory contains many subdirectories with the
most important ones being shown in the structure below:

```c
cpukit
|
+-----------+----------+-----------+
|           |          |           |
posix       rtems       sapi       score
```

The `cpukit/` directory contains a set of subdirectories which contains the
source files comprising the executive portion of the RTEMS development
environment as well as portable support libraries such as support for the C
Library and filesystems. The API specific and "SuperCore" (e.g. `score/`
directory) source code files are separated into distinct directory trees.

The following is a description of each of the subdirectories under `cpukit/`:

`${RTEMS_ROOT}/cpukit/ftpd/`
: This directory contains the RTEMS ftpd server.

`${RTEMS_ROOT}/cpukit/mhttpd/`
: This directory contains the port of the Mongoose web server to RTEMS.

`${RTEMS_ROOT}/cpukit/include/`
: This directory contains header files which are private to RTEMS and not
  considered to be owned by any other component in the CPU Kit.

`${RTEMS_ROOT}/cpukit/libblock/`
: This directory contains support code for using Block Devices such as hard
  drives, floppies, and CD-ROMs. It includes the generic IO primitives for
  block device drivers, disk caching support, and a RAM disk block device
  driver.

`${RTEMS_ROOT}/cpukit/libcsupport/`
: This directory contains the RTEMS specific support routines for the Newlib
  C Library. This includes what are referred to as system calls and found in
  section 2 of the traditional UNIX manual. In addition, it contains a
  thread-safe implementation of the Malloc family of routines as well as BSD
  and POSIX services not found in Newlib.

`${RTEMS_ROOT}/cpukit/libfs/`
: This directory contains the various non-networked filesystem
  implementations for RTEMS. It includes the In-Memory FileSystem (IMFS),
  the mini-IMFS, and FAT filesystems.

`${RTEMS_ROOT}/cpukit/libi2c/`
: This directory contains the RTEMS I2C framework.

`${RTEMS_ROOT}/cpukit/libmd/`
: This directory contains a port of the standard MD5 checksum code.

`${RTEMS_ROOT}/cpukit/libmisc/`
: This directory contains support facilities which are RTEMS specific but
  otherwise unclassified. In general, they do not adhere to a standard API.
  Among the support facilities in this directory are a `/dev/null` device
  driver, the Stack Overflow Checker, a mini-shell, the CPU and rate
  monotonic period usage monitoring libraries, and a utility to "dump a
  buffer" in a nicely formatted way similar to many ROM monitors.

`${RTEMS_ROOT}/cpukit/libnetworking/`
: This directory contains the port of the FreeBSD TCP/IP stack to RTEMS.

`${RTEMS_ROOT}/cpukit/librpc/`
: This directory contains the port of the FreeBSD RPC/XDR source to RTEMS.

`${RTEMS_ROOT}/cpukit/libpci/`
: This directory contains RTEMS PCI Library.

`${RTEMS_ROOT}/cpukit/posix/`
: This directory contains the RTEMS implementation of the threading portions
  of the POSIX API.

`${RTEMS_ROOT}/cpukit/pppd/`
: This directory contains a port of the free implementation of the PPPD
  network protocol.

`${RTEMS_ROOT}/cpukit/rtems/`
: This directory contains the implementation of the Classic API.

`${RTEMS_ROOT}/cpukit/sapi/`
: This directory contains the implementation of RTEMS services which are
  required but beyond the realm of any standardization efforts. It includes
  initialization, shutdown, and IO services.

`${RTEMS_ROOT}/cpukit/score/`
: This directory contains the "SuperCore" of RTEMS. All APIs are implemented
  in terms of SuperCore services. For example, Classic API tasks and POSIX
  threads are all implemented in terms of SuperCore threads. This provides a
  common infrastructure and a high degree of interoperability between the
  APIs. For example, services from all APIs may be used by any task/thread
  independent of the API used to create it. Within the `score/` directory
  the CPU dependent modules are found. The `score/cpu/` subdirectory
  contains a subdirectory for each target CPU supported by this release of
  the RTEMS executive. Each processor directory contains the CPU dependent
  code necessary to host RTEMS. The `no_cpu` directory provides a starting
  point for developing a new port to an unsupported processor. The files
  contained within the `no_cpu` directory may also be used as a reference
  for the other ports to specific processors.

`${RTEMS_ROOT}/cpukit/telnetd/`
: This directory contains the RTEMS telnetd server.

`${RTEMS_ROOT}/cpukit/wrapup/`
: This directory is responsible for taking the individual libraries and
  objects built in each of the components in the RTEMS CPU Kit source tree
  and bundling them together to form the single RTEMS library
  `librtemscpu.a`. This library contains all BSP and CPU model specific
  software.

`${RTEMS_ROOT}/cpukit/zlib/`
: This directory contains a port of the GNU Zlib compression library to
  RTEMS.

### testsuites/ Test Suites

This directory provides all of the RTEMS Test Suite except those for the
Classic API Ada95 binding This includes the single processor tests,
multiprocessor tests, timing tests, library tests, and sample tests.
Additionally, subdirectories for support functions and test related header
files are provided. The following table lists the test suites currently
included with the RTEMS and the directory in which they may be located:

`${RTEMS_ROOT}/testsuites/libtests/`
: This directory contains the test suite for the various RTEMS support
  components.

`${RTEMS_ROOT}/testsuites/mptests/`
: This directory contains the test suite for the multiprocessor support in
  the Classic API. The tests provided address two node configurations and
  provide coverage for the multiprocessor code found in RTEMS.

`${RTEMS_ROOT}/testsuites/psxtests/`
: This directory contains the test suite for the RTEMS POSIX API.

`${RTEMS_ROOT}/testsuites/samples/`
: This directory provides sample application tests which aid in the testing a
  newly built RTEMS environment, a new BSP, or as starting points for the
  development of an application using the RTEMS executive. They are
  discussed in ::ref::`Sample Applications`.

`${RTEMS_ROOT}/testsuites/sptests/`
: This directory contains the test suite for the RTEMS Classic API when
  executing on a single processor. The tests were originally designed to
  provide near complete test coverage for the entire executive code. With
  the addition of multiple APIs, this is no longer the case as some SuperCore
  functionality is not available through the Classic API. Thus some
  functionality in the SuperCore is only covered by tests in the POSIX API
  Test Suites.

`${RTEMS_ROOT}/testsuites/support/`
: This directory contains support software and header files for the various
  test suites.

`${RTEMS_ROOT}/testsuites/tmtests/`
: This directory contains the timing test suite for the RTEMS Classic API.
  This include tests that benchmark each directive in the Classic API as well
  as a set of critical SuperCore functions. These tests are important for
  helping to verify that RTEMS performs as expected on your target hardware.
  It is not uncommon to discover mistakes in board initialization such as
  caching being disabled as a side-effect of analyzing the results of these
  tests.

`${RTEMS_ROOT}/testsuites/tools/`
: This directory contains tools which execute on the development host and aid
  in executing and evaluating the results of the test suite. The tools
  `difftest` compares the output of one or more tests with the expected
  output. If you place the output of all the `tmtests/` in a single file,
  then the utility `sorttimes` will be able to produce a report organizing
  the execution times by manager.
