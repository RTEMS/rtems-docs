.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2020 On-Line Applications Research Corporation (OAR)

AArch64 Specific Information
************************

This chapter discusses the dependencies of the
*ARM AArch64 architecture*
(https://en.wikipedia.org/wiki/ARM_architecture#AArch64_features) in this port
of RTEMS.  The ARMv8-A versions are supported by RTEMS.  Processors with a MMU
use a static configuration which is set up during system start.  SMP is not
supported.

**Architecture Documents**

For information on the ARM AArch64 architecture refer to the *ARM Infocenter*
(http://infocenter.arm.com/).

CPU Model Dependent Features
============================

This section presents the set of features which vary across ARM AArch64
implementations and are of importance to RTEMS.  The set of CPU model feature
macros are defined in the file :file:`cpukit/score/cpu/aarch64/rtems/score/aarch64.h`
based upon the particular CPU model flags specified on the compilation command
line.

CPU Model Name
--------------

The macro ``CPU_MODEL_NAME`` is a string which designates the architectural
level of this CPU model.  See in :file:`cpukit/score/cpu/aarch64/rtems/score/aarch64.h`
for the values.

Floating Point Unit and SIMD
----------------------------

The Advanced SIMD (NEON) and Floating-point instruction set extension is
supported and expected to be present since all ARMv8-A CPUs are expected to
support it as per the *ARMv8-A Programmer's Guide Chapter 7 introduction*
(https://developer.arm.com/docs/den0024/a/aarch64-floating-point-and-neon). As
such, ``CPU_HARDWARE_FP`` will always be set to ``TRUE``.

Multilibs
=========

The following multilib variants are available:

#. ``ILP32``: AArch64 instruction set and registers using 32bit long int and pointers

#. ``LP64``: AArch64 instruction set and registers using 64bit long int and pointers

Use for example the following GCC options:

.. code-block:: shell

    -mcpu=cortex-a53 -mabi=ilp32

to build an application or BSP for the ARMv8-A architecture and tune the code
for a Cortex-A53 processor.  It is important to select the correct ABI.

Calling Conventions
===================

Please refer to the *Procedure Call Standard for the ARM 64-bit Architecture*
(https://github.com/ARM-software/abi-aa/releases/download/2019Q4/aapcs64.pdf).

Memory Model
============

A flat 64-bit or 32-bit memory model is supported depending on the selected multilib
variant.  All AArch64 CPU variants support a built-in MMU for which basic initialization
for a flat memory model is handled.

Interrupt Processing
====================

The Reset Vector is determined using RVBAR and is Read-Only. RVBAR is set using
configuration signals only sampled at reset.  The ARMv8 architecture has four
exception types:

- Synchronous Exception

- Interrupt (IRQ)

- Fast Interrupt (FIQ)

- System Error Exception

Of these types only the synchronous and IRQ exceptions have explicit operating
system support.  It is intentional that the FIQ is not supported by the operating
system.  Without operating system support for the FIQ it is not necessary to
disable them during critical sections of the system.

Interrupt Levels
----------------

There are exactly two interrupt levels on ARMv8 with respect to RTEMS.  Level
zero corresponds to interrupts enabled.  Level one corresponds to interrupts
disabled.

Interrupt Stack
---------------

The board support package must initialize the interrupt stack. The memory for
the stacks is usually reserved in the linker script. The interrupt stack pointer
is stored in the EL0 stack pointer and is accessed by switching to SP0 mode
at the beginning of interrupt calls and back to SPx mode after completion of
interrupt calls using the `spsel` instruction.

Default Fatal Error Processing
==============================

The default fatal error handler for this architecture performs the following
actions:

- disables operating system supported interrupts (IRQ),

- places the error code in ``x0``, and

- executes an infinite loop to simulate a halt processor instruction.

Symmetric Multiprocessing
=========================

SMP is not currently supported on ARMv8-A.

Thread-Local Storage
====================

Thread-local storage (TLS) is supported. AArch64 uses unmodified TLS variant I
which is not explcitly stated, but can be inferred from the behavior of GCC and
*Addenda to, and Errata in, the ABI for the Arm® Architecture*
(https://developer.arm.com/documentation/ihi0045/g). This alters expectations
for the size of the TLS Thread Control Block (TCB) such that, under the LP64
multilib variant, the TCB is 16 bytes in size instead of 8 bytes.
