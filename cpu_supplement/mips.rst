.. comment SPDX-License-Identifier: CC-BY-SA-4.0

MIPS Specific Information
#########################

This chapter discusses the MIPS architecture dependencies
in this port of RTEMS.  The MIPS family has a wide variety
of implementations by a wide range of vendors.  Consequently,
there are many, many CPU models within it.

**Architecture Documents**

IDT docs are online at http://www.idt.com/products/risc/Welcome.html

For information on the XXX architecture, refer to the following documents
available from VENDOR (:file:`http//www.XXX.com/`):

- *XXX Family Reference, VENDOR, PART NUMBER*.

CPU Model Dependent Features
============================

This section presents the set of features which vary
across MIPS implementations and are of importance to RTEMS.
The set of CPU model feature macros are defined in the file``cpukit/score/cpu/mips/mips.h`` based upon the particular CPU
model specified on the compilation command line.

Another Optional Feature
------------------------

The macro XXX

Calling Conventions
===================

Processor Background
--------------------

TBD

Calling Mechanism
-----------------

TBD

Register Usage
--------------

TBD

Parameter Passing
-----------------

TBD

Memory Model
============

Flat Memory Model
-----------------

The MIPS family supports a flat 32-bit address
space with addresses ranging from 0x00000000 to 0xFFFFFFFF (4
gigabytes).  Each address is represented by a 32-bit value and
is byte addressable.  The address may be used to reference a
single byte, word (2-bytes), or long word (4 bytes).  Memory
accesses within this address space are performed in big endian
fashion by the processors in this family.

Some of the MIPS family members such as the support virtual memory and
segmentation.  RTEMS does not support virtual memory or
segmentation on any of these family members.

Interrupt Processing
====================

Although RTEMS hides many of the processor dependent
details of interrupt processing, it is important to understand
how the RTEMS interrupt manager is mapped onto the processor's
unique architecture. Discussed in this chapter are the MIPS's
interrupt response and control mechanisms as they pertain to
RTEMS.

Vectoring of an Interrupt Handler
---------------------------------

Upon receipt of an interrupt the XXX family
members with separate interrupt stacks automatically perform the
following actions:

- TBD

A nested interrupt is processed similarly by these
CPU models with the exception that only a single ISF is placed
on the interrupt stack and the current stack need not be
switched.

Interrupt Levels
----------------

TBD

Default Fatal Error Processing
==============================

The default fatal error handler for this target architecture disables
processor interrupts, places the error code in *XXX*, and executes a``XXX`` instruction to simulate a halt processor instruction.

Symmetric Multiprocessing
=========================

SMP is not supported.

Thread-Local Storage
====================

Thread-local storage is not implemented.

Board Support Packages
======================

System Reset
------------

An RTEMS based application is initiated or
re-initiated when the processor is reset.  When the
processor is reset, it performs the following actions:

- TBD

Processor Initialization
------------------------

TBD

.. COMMENT: Copyright (c) 2014 embedded brains GmbH.  All rights reserved.

