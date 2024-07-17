.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2009 On-Line Applications Research Corporation (OAR)

ARM Specific Information
************************

This chapter discusses the *ARM architecture*
(http://en.wikipedia.org/wiki/ARM_architecture) dependencies in this port of
RTEMS.  The ARMv4T (and compatible), ARMv7-A, ARMv7-R and ARMv7-M architecture
versions are supported by RTEMS.  Processors with a MMU use a static
configuration which is set up during system start.  SMP is supported.

**Architecture Documents**

For information on the ARM architecture refer to the *ARM Infocenter*
(http://infocenter.arm.com/).

CPU Model Dependent Features
============================

This section presents the set of features which vary across ARM implementations
and are of importance to RTEMS.  The set of CPU model feature macros are
defined in the file :file:`cpukit/score/cpu/arm/rtems/score/arm.h` based upon
the particular CPU model flags specified on the compilation command line.

CPU Model Name
--------------

The macro ``CPU_MODEL_NAME`` is a string which designates the architectural
level of this CPU model.  See in :file:`cpukit/score/cpu/arm/rtems/score/arm.h`
for the values.

Count Leading Zeroes Instruction
--------------------------------

The ARMv5 and later instruction sets have the count leading zeroes ``clz``
instruction which could be used to speed up the find first bit operation. The
use of this instruction should significantly speed up the scheduling associated
with a thread blocking.  This is currently not used.

Floating Point Unit
-------------------

The following floating point units are supported:

- VFPv2 (for example available on ARM926EJ-S processors)

- VFPv3-D32/NEON (for example available on Cortex-A processors)

- VFPv3-D16 (for example available on Cortex-R processors)

- FPv4-SP-D16 (for example available on Cortex-M processors)

- FPv5-D16 (for example available on Cortex-M7 processors)

Multilibs
=========

The following multilibs are available:

#. ``.``: ARMv4T, ARM instruction set

#. ``vfp/hard``: ARMv4T, ARM instruction set with hard-float ABI and VFPv2 support

#. ``thumb``: ARMv4T, Thumb-1 instruction set

#. ``thumb/armv6-m``: ARMv6M, subset of Thumb-2 instruction set

#. ``thumb/armv7-a``: ARMv7-A, Thumb-2 instruction set

#. ``thumb/armv7-a/neon/hard``: ARMv7-A, Thumb-2 instruction set with
   hard-float ABI Neon and VFP-D32 support

#. ``thumb/armv7-r``: ARMv7-R, Thumb-2 instruction set

#. ``thumb/armv7-r/vfpv3-d16/hard``: ARMv7-R, Thumb-2 instruction set with
   hard-float ABI VFP-D16 support

#. ``thumb/cortex-m3``: Cortex-M3, Thumb-2 instruction set with hardware
   integer division (SDIV/UDIV) and a fix for Cortex-M3 Errata 602117.

#. ``thumb/cortex-m4``: Cortex-M4, Thumb-2 instruction set with hardware
   integer division (SDIV/UDIV) and DSP instructions

#. ``thumb/cortex-m4/fpv4-sp-d16``: Cortex-M4, Thumb-2 instruction set with
   hardware integer division (SDIV/UDIV), DSP instructions and hard-float ABI
   FPv4-SP support

#. ``thumb/cortex-m7/fpv5-d16``: Cortex-M7, Thumb-2 instruction set with
   hard-float ABI and FPv5-D16 support

#. ``eb/thumb/armv7-r``: ARMv7-R, Big-endian Thumb-2 instruction set

#. ``eb/thumb/armv7-r/vfpv3-d16/hard``: ARMv7-R, Big-endian Thumb-2 instruction
   set with hard-float ABI VFP-D16 support

Multilib 1., 2. and 3. support the legacy ARM7TDMI and ARM926EJ-S processors.

Multilib 4. supports the Cortex-M0 and Cortex-M1 cores.

Multilib 5. and 6. support the Cortex-A processors.

Multilib 7., 8., 13. and 14. support the Cortex-R processors.  Here also
big-endian variants are available.

Use for example the following GCC options:

.. code-block:: shell

    -mthumb -march=armv7-a -mfpu=neon -mfloat-abi=hard -mtune=cortex-a9

to build an application or BSP for the ARMv7-A architecture and tune the code
for a Cortex-A9 processor.  It is important to select the options used for the
multilibs. For example:

.. code-block:: shell

    -mthumb -mcpu=cortex-a9

alone will not select the ARMv7-A multilib.

Calling Conventions
===================

Please refer to the *Procedure Call Standard for the ARM Architecture*
(http://infocenter.arm.com/help/topic/com.arm.doc.ihi0042c/IHI0042C_aapcs.pdf).

Memory Model
============

A flat 32-bit memory model is supported.  The board support package must take
care of initializing the MMU if necessary.

Note that architecture variants which support unaligned accesses must not use
memcpy() or memset() on device memory as those functions are hand-optimized and
will take advantage of unaligned accesses where available. *As per ARM*
(https://developer.arm.com/documentation/ddi0406/c/Application-Level-Architecture/Application-Level-Memory-Model/Alignment-support/Unaligned-data-access-restrictions-in-ARMv7-and-ARMv6),
unaligned accesses are not permitted for device memory.

Interrupt Processing
====================

The ARMv4T (and compatible) architecture has seven exception types:

- Reset

- Undefined

- Software Interrupt (SWI)

- Prefetch Abort

- Data Abort

- Interrupt (IRQ)

- Fast Interrupt (FIQ)

Of these types only the IRQ has explicit operating system support.  It is
intentional that the FIQ is not supported by the operating system.  Without
operating system support for the FIQ it is not necessary to disable them during
critical sections of the system.

The ARMv7-M architecture has a completely different exception model.  Here
interrupts are disabled with a write of 0x80 to the ``basepri_max`` register.
This means that all exceptions and interrupts with a priority value of greater
than or equal to 0x80 are disabled.  Thus exceptions and interrupts with a
priority value of less than 0x80 are non-maskable with respect to the operating
system and therefore must not use operating system services.  Several support
libraries of chip vendors implicitly shift the priority value somehow before
the value is written to the NVIC IPR register.  This can easily lead to
confusion.

Interrupt Levels
----------------

There are exactly two interrupt levels on ARM with respect to RTEMS.  Level
zero corresponds to interrupts enabled.  Level one corresponds to interrupts
disabled.

Interrupt Stack
---------------

The board support package must initialize the interrupt stack. The memory for
the stacks is usually reserved in the linker script.

Symmetric Multiprocessing
=========================

SMP is supported on ARMv7-A.  Available platforms are:

- Altera Cyclone V

- NXP i.MX 7

- Xilinx Zynq

Thread-Local Storage
====================

Thread-local storage is supported.
