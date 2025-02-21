.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

=======
Preface
=======

The purpose of this manual is to provide a roadmap to those people porting
RTEMS to a new CPU family. This process includes a variety of activities
including the following:

- targeting the GNU development tools

- porting the RTEMS executive code

- developing a Board Support Package

- writing an RTEMS CPU Supplement manual for the completed port.

This document focuses on the process of actually porting the RTEMS
executive code proper.  Each of the data structures, routines, and macro
definitions required of a port of RTEMS is described in this document.

Porting any operating system, including RTEMS, requires knowledge of the
operating system, target CPU architecture, and debug environment.  It is
very desirable to have a CPU simulator or hardware emulator when debugging
the port.  This manual assumes that the user is familiar with building and
using RTEMS, the C programming language, and the target CPU architecture.
It is desirable to be familiar with the assembly language for the target
CPU family but since only a limited amount of assembly is required to port
RTEMS.
