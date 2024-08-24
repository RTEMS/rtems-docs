.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

SuperH Specific Information
***************************

This chapter discusses the SuperH architecture dependencies in this port of
RTEMS.  The SuperH family has a wide variety of implementations by a wide range
of vendors.  Consequently, there are many, many CPU models within it.

**Architecture Documents**

For information on the SuperH architecture, refer to the following documents
available from VENDOR (http://www.XXX.com/):

- *SuperH Family Reference, VENDOR, PART NUMBER*.

CPU Model Dependent Features
============================

This chapter presents the set of features which vary across SuperH
implementations and are of importance to RTEMS.  The set of CPU model feature
macros are defined in the file ``cpukit/score/cpu/sh/sh.h`` based upon the
particular CPU model specified on the compilation command line.

Another Optional Feature
------------------------

The macro XXX

Calling Conventions
===================

Calling Mechanism
-----------------

All RTEMS directives are invoked using a ``XXX`` instruction and return to the
user application via the ``XXX`` instruction.

Register Usage
--------------

The SH1 has 16 general registers (r0..r15).

- r0..r3 used as general volatile registers

- r4..r7 used to pass up to 4 arguments to functions, arguments above 4 are
  passed via the stack)

- r8..13 caller saved registers (i.e. push them to the stack if you need them
  inside of a function)

- r14 frame pointer

- r15 stack pointer

Parameter Passing
-----------------

XXX

Memory Model
============

Flat Memory Model
-----------------

The SuperH family supports a flat 32-bit address space with addresses ranging
from 0x00000000 to 0xFFFFFFFF (4 gigabytes).  Each address is represented by a
32-bit value and is byte addressable.  The address may be used to reference a
single byte, word (2-bytes), or long word (4 bytes).  Memory accesses within
this address space are performed in big endian fashion by the processors in
this family.

Some of the SuperH family members support virtual memory and segmentation.
RTEMS does not support virtual memory or segmentation on any of the SuperH
family members.  It is the responsibility of the BSP to initialize the mapping
for a flat memory model.

Interrupt Processing
====================

Although RTEMS hides many of the processor dependent details of interrupt
processing, it is important to understand how the RTEMS interrupt manager is
mapped onto the processor's unique architecture. Discussed in this chapter are
the MIPS's interrupt response and control mechanisms as they pertain to RTEMS.

Vectoring of an Interrupt Handler
---------------------------------

Upon receipt of an interrupt the XXX family members with separate interrupt
stacks automatically perform the following actions:

- TBD

A nested interrupt is processed similarly by these CPU models with the
exception that only a single ISF is placed on the interrupt stack and the
current stack need not be switched.

Interrupt Levels
----------------

TBD

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
