.. SPDX-License-Identifier: CC-BY-SA-4.0


Glossary
********

.. glossary::

  Architecture
    Family or class of processor based around a common instruction set. RTEMS
    architectures follow the GCC architecture model as RTEMS needs an GCC
    architecture compiler for each support RTEMS architecture.

  APA
    Arbitrary Processor Affinity

  API
    Application Programming Interface

  Binutils
    GNU Binary Utilities such as the assembler ``as``, linker ``ld`` and a
    range of other tools used in the development of software.

  BSP
    Board Support Package is a specific configuration RTEMS can be built
    for. An RTEMS install process installs specific library and headers files
    for a single BSP. A BSP optimises RTEMS to a specific target hardware.

  Buildbot
    A continuous inteagration build server.

  C11
    ISO/IEC 9899:2011

  C++11
    ISO/IEC 14882:2011

  Crosscompiler

    A compiler built to run on a Host that generate code for another
    architecture.

  DLL
    Dynamically Linker Library used on Windows.

  EDF
    Earliest Deadline First

  EMB²
    `Embedded Multicore Building Blocks <https://embb.io>`_

  FAT
    File Allocation Table

  Futex
    Fast User-Space Locking

  IMFS
    In-Memory File System

  JFFS2
    Journalling Flash File System version 2

  GCC
    GNU Compiler Collection

  GDB
    GNU Debugger

  GNU
    GNU's Not Unix

  Host
    The computer and operating system that hosts the RTEMS development tools
    such as the compiler, linker and debugger.

  MinGW
    Minimal GNU system for Windows that lets GCC built programs use the
    standard Windows operating system DLLs. It lets you build native Windows
    programs with the GNU GCC compiler.

  MinGW64
    Minimal GNU system for 64bit Windows. MinGW64 is not the MinGW project.

  MrsP
    Multiprocessor Resource-Sharing Protocol

  MSYS2
    Minimal System 2 is a fork of the MinGW project's MSYS tool and the MinGW
    MSYS tool is a fork of Cygwin project. The Cygwin project provides a POSIX
    emulation layer for Windows so POSIX software can run on Windows. MSYS is a
    minimal version that is just enough to let ``configure`` scripts run. MSYS
    has a simplified path structure to make it easier to building native Windows
    programs.

  NFSv2
    Network File System version 2

  OMIP
    :math:`O(m)` Independence-Preserving Protocol

  OpenMP
    Open Multi-Processing

  POSIX
    Portable Operating System Interface is a standard that lets software be
    portable between compliant operating systems.

  prefix
    A path used when building a package so all parts of the package reside
    under that path.

  RFS
    RTEMS File System

  RSB
    RTEMS Source Builder is part of the RTEMS Tools Project. It builds packages
    such as the tools for the RTEMS operating system.

  RTEMS
    The Real-Time Executive for Multiprocessor Systems or RTEMS is an open
    source fully featured Real Time Operating System or RTOS that supports a
    variety of open standard application programming interfaces (API) and
    interface standards such as POSIX and BSD sockets.

  SMP
    Symmetric Multiprocessing

  Target
    A target is the hardware or simulator a BSP built executable runs on.

  Test Suite
   See Testsuite

  Testsuite
    RTEMS test suite located in the ``testsuites/`` directory.

  TLS
    Thread-Local Storage

  Waf
    Waf build system.  For more information see http://www.waf.io/

  YAFFS2
    `Yet Another Flash File System version 2 <https://git.rtems.org/sebh/rtems-yaffs2.git>`_
