.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Preface
*******

The Real Time Executive for Multiprocessor Systems (RTEMS) is designed to be
portable across multiple processor architectures.  However, the nature of
real-time systems makes it essential that the application designer understand
certain processor dependent implementation details.  These processor
dependencies include calling convention, board support package issues,
interrupt processing, exact RTEMS memory requirements, performance data, header
files, and the assembly language interface to the executive.

Each architecture represents a CPU family and usually there are a wide variety
of CPU models within it.  These models share a common Instruction Set
Architecture (ISA) which often varies based upon some well-defined rules.
There are often multiple implementations of the ISA and these may be from one
or multiple vendors.

On top of variations in the ISA, there may also be variations which occur when
a CPU core implementation is combined with a set of peripherals to form a
system on chip.  For example, there are many ARM CPU models from numerous
semiconductor vendors and a wide variety of peripherals.  But at the ISA level,
they share a common compatibility.

RTEMS depends upon this core similarity across the CPU models and leverages
that to minimize the source code that is specific to any particular CPU core
implementation or CPU model.

This manual is separate and distinct from the RTEMS Porting Guide.  That manual
is a guide on porting RTEMS to a new architecture.  This manual is focused on
the more mundane CPU architecture specific issues that may impact application
development.  For example, if you need to write a subroutine in assembly
language, it is critical to understand the calling conventions for the target
architecture.

The first chapter in this manual describes these issues in general terms.  In a
sense, it is posing the questions one should be aware may need to be answered
and understood when porting an RTEMS application to a new architecture.  Each
subsequent chapter gives the answers to those questions for a particular CPU
architecture.
