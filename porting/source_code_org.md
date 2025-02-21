.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Source Code Organization
########################

This section describes the organization of the source code within RTEMS
that is CPU family and CPU model dependent.

Introduction
============

The CPU family dependent files associated with a port of the RTEMS
executive code proper to a particular processor family are found in
cpukit/score/cpu.  Support code for this port as well as processor
dependent code which may be reused across multiple Board Support Packages
is found in c/src/lib/libcpu.

XXX list the files and directories here
