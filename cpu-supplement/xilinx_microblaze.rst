.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 On-Line Applications Research Corporation (OAR)

Xilinx MicroBlaze Specific Information
**************************************

This chapter discusses the dependencies of the *MicroBlaze architecture*
(https://en.wikipedia.org/wiki/MicroBlaze).

**Architecture Documents**

For information on the MicroBlaze architecture, refer to
*UG984 MicroBlaze Processor Reference Guide*
(https://www.xilinx.com/support/documentation/sw_manuals/xilinx2021_2/ug984-vivado-microblaze-ref.pdf).

CPU Model Dependent Features
============================

There are no CPU model dependent features in this port.

Calling Conventions
===================

Please refer to "Chapter 4: MicroBlaze Application Binary Interface" of
*UG984 MicroBlaze Processor Reference Guide*
(https://www.xilinx.com/support/documentation/sw_manuals/xilinx2021_2/ug984-vivado-microblaze-ref.pdf).

Interrupt Processing
====================

Hardware exceptions, interrupts, and user exceptions are all supported. When a
hardware exception or user exception occurs, a fatal error will be generated.
When an interrupt occurs, the interrupt source is determined by reading the
AXI Interrupt Controller's Interrupt Status Register and masking it with the
Interrupt Enable Register.

Interrupt Levels
----------------

There are exactly two interrupt levels on MicroBlaze with respect to RTEMS.
Level zero corresponds to interrupts disabled. Level one corresponds to
interrupts enabled. This is the inverse of how most other architectures handle
interrupt enable status.

Interrupt Stack
---------------

The memory region for the interrupt stack is defined by the BSP.

Default Fatal Error Processing
==============================

The default fatal error is BSP-specific.

Symmetric Multiprocessing
=========================

SMP is not supported.

Thread-Local Storage
====================

Thread-local storage is supported.
