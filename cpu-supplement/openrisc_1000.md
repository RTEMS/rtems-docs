.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2014 Hesham Almatary
.. Copyright (C) 1989, 2007 On-Line Applications Research Corporation (OAR)

OpenRISC 1000 Specific Information
**********************************

This chapter discusses the`OpenRISC 1000 architecture
http://opencores.org/or1k/Main_Page dependencies in this port of RTEMS. There
are many implementations for OpenRISC like or1200 and mor1kx. Currently RTEMS
supports basic features that all implementations should have.

**Architecture Documents**

For information on the OpenRISC 1000 architecture refer to the`OpenRISC 1000
architecture manual http://openrisc.github.io/or1k.html.

Calling Conventions
===================

Please refer to the`Function Calling Sequence
http://openrisc.github.io/or1k.html#__RefHeading__504887_595890882.

Floating Point Unit
-------------------

A floating point unit is currently not supported.

Memory Model
============

A flat 32-bit memory model is supported.

Interrupt Processing
====================

OpenRISC 1000 architecture has 13 exception types:

- Reset

- Bus Error

- Data Page Fault

- Instruction Page Fault

- Tick Timer

- Alignment

- Illegal Instruction

- External Interrupt

- D-TLB Miss

- I-TLB Miss

- Range

- System Call

- Floating Point

- Trap

Interrupt Levels
----------------

There are only two levels: interrupts enabled and interrupts disabled.

Interrupt Stack
---------------

The OpenRISC RTEMS port uses a dedicated software interrupt stack.  The stack
for interrupts is allocated during interrupt driver initialization.  When an
interrupt is entered, the _ISR_Handler routine is responsible for switching
from the interrupted task stack to RTEMS software interrupt stack.

Symmetric Multiprocessing
=========================

SMP is not supported.
