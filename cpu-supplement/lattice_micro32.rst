.. SPDX-License-Identifier: CC-BY-SA-4.0


Lattice Mico32 Specific Information
***********************************

This chaper discusses the Lattice Mico32 architecture dependencies in this port
of RTEMS. The Lattice Mico32 is a 32-bit Harvard, RISC architecture "soft"
microprocessor, available for free with an open IP core licensing
agreement. Although mainly targeted for Lattice FPGA devices the microprocessor
can be implemented on other vendors' FPGAs, too.

**Architecture Documents**

For information on the Lattice Mico32 architecture, refer to the following
documents available from Lattice Semiconductor http://www.latticesemi.com/.

- *"LatticeMico32 Processor Reference Manual"*
  http://www.latticesemi.com/dynamic/view_document.cfm?document_id=20890

CPU Model Dependent Features
============================

The Lattice Mico32 architecture allows for different configurations of the
processor. This port is based on the assumption that the following options are
implemented:

- hardware multiplier

- hardware divider

- hardware barrel shifter

- sign extension instructions

- instruction cache

- data cache

- debug

Register Architecture
=====================

This section gives a brief introduction to the register architecture of the
Lattice Mico32 processor.

The Lattice Mico32 is a RISC archictecture processor with a 32-register file of
32-bit registers.

Register Name

Function

r0

holds value zero

r1-r25

general purpose

r26/gp

general pupose / global pointer

r27/fp

general pupose / frame pointer

r28/sp

stack pointer

r29/ra

return address

r30/ea

exception address

r31/ba

breakpoint address

Note that on processor startup all register values are undefined including r0,
thus r0 has to be initialized to zero.

Calling Conventions
===================

Calling Mechanism
-----------------

A call instruction places the return address to register r29 and a return from
subroutine (ret) is actually a branch to r29/ra.

Register Usage
--------------

A subroutine may freely use registers r1 to r10 which are *not* preserved
across subroutine invocations.

Parameter Passing
-----------------

When calling a C function the first eight arguments are stored in registers r1
to r8. Registers r1 and r2 hold the return value.

Memory Model
============

The Lattice Mico32 processor supports a flat memory model with a 4 Gbyte
address space with 32-bit addresses.

The following data types are supported:

================== ==== ======================
Type               Bits C Compiler Type
================== ==== ======================
unsigned byte      8    unsigned char
signed byte        8    char
unsigned half-word 16   unsigned short
signed half-word   16   short
unsigned word      32   unsigned int / unsigned long
signed word        32   int / long
================== ==== ======================

Data accesses need to be aligned, with unaligned accesses result are undefined.

Interrupt Processing
====================

The Lattice Mico32 has 32 interrupt lines which are however served by only one
exception vector. When an interrupt occurs following happens:

- address of next instruction placed in r30/ea

- IE field of IE CSR saved to EIE field and IE field cleared preventing further
  exceptions from occuring.

- branch to interrupt exception address EBA CSR + 0xC0

The interrupt exception handler determines from the state of the interrupt
pending registers (IP CSR) and interrupt enable register (IE CSR) which
interrupt to serve and jumps to the interrupt routine pointed to by the
corresponding interrupt vector.

For now there is no dedicated interrupt stack so every task in the system MUST
have enough stack space to accommodate the worst case stack usage of that
particular task and the interrupt service routines COMBINED.

Nested interrupts are not supported.

Symmetric Multiprocessing
=========================

SMP is not supported.

Thread-Local Storage
====================

Thread-local storage is not implemented.

Board Support Packages
======================

There are no Lattice Micro32 specific notes on BSPs.

System Reset
------------

An RTEMS based application is initiated or re-initiated when the processor is
reset.
