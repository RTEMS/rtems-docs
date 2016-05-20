.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Epiphany Specific Information
#############################

This chapter discusses the`Epiphany Architecture <http://adapteva.com/docs/epiphany_sdk_ref.pdf>`_
dependencies in this port of RTEMS. Epiphany is a chip that can come with 16 and
64 cores, each of which can run RTEMS separately or they can work together to
run a SMP RTEMS application.

**Architecture Documents**

For information on the Epiphany architecture refer to the`Epiphany Architecture Reference <http://adapteva.com/docs/epiphany_arch_ref.pdf>`_.

Calling Conventions
===================

Please refer to the`Epiphany SDK <http://adapteva.com/docs/epiphany_sdk_ref.pdf>`_
Appendix A: Application Binary Interface

Floating Point Unit
-------------------

A floating point unit is currently not supported.

Memory Model
============

A flat 32-bit memory model is supported, no caches. Each core has its own 32 KiB
strictly ordered local memory along with an access to a shared 32 MiB external
DRAM.

Interrupt Processing
====================

Every Epiphany core has 10 exception types:

- Reset

- Software Exception

- Data Page Fault

- Timer 0

- Timer 1

- Message Interrupt

- DMA0 Interrupt

- DMA1 Interrupt

- WANT Interrupt

- User Interrupt

Interrupt Levels
----------------

There are only two levels: interrupts enabled and interrupts disabled.

Interrupt Stack
---------------

The Epiphany RTEMS port uses a dedicated software interrupt stack.
The stack for interrupts is allocated during interrupt driver initialization.
When an  interrupt is entered, the _ISR_Handler routine is responsible for
switching from the interrupted task stack to RTEMS software interrupt stack.

Default Fatal Error Processing
==============================

The default fatal error handler for this architecture performs the
following actions:

- disables operating system supported interrupts (IRQ),

- places the error code in ``r0``, and

- executes an infinite loop to simulate a halt processor instruction.

Symmetric Multiprocessing
=========================

SMP is not supported.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

