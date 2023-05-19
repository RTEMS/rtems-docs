.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 embedded brains GmbH & Co. KG

RISC-V Specific Information
***************************

Calling Conventions
===================

Please refer to the
`RISC-V ELF psABI specification <https://github.com/riscv/riscv-elf-psabi-doc/blob/master/riscv-elf.md>`_.

Multilibs
=========

The GCC for RISC-V can generate code for several 32-bit and 64-bit ISA/ABI
variants.  The following multilibs are available:

* ``.``: The default multilib ISA is RV32IMAFDC with ABI ILP32D.

* ``rv32i/ilp32``: ISA RV32I with ABI ILP32.

* ``rv32im/ilp32``: ISA RV32IM with ABI ILP32.

* ``rv32imafd/ilp32d``: ISA RV32IMAFD with ABI ILP32D.

* ``rv32iac/ilp32``: ISA RV32IAC with ABI ILP32.

* ``rv32imac/ilp32``: ISA RV32IMAC with ABI ILP32.

* ``rv32imafc/ilp32f``: ISA RV32IMAFC with ABI ILP32F.

* ``rv64imafd/lp64d``: ISA RV64IMAFD with ABI LP64D and code model medlow.

* ``rv64imafd/lp64d/medany``: ISA RV64IMAFD with ABI LP64D and code model medany.

* ``rv64imac/lp64``: ISA RV64IMAC with ABI LP64 and code model medlow.

* ``rv64imac/lp64/medany``: ISA RV64IMAC with ABI LP64 and code model medany.

* ``rv64imafdc/lp64d``: ISA RV64IMAFDC with ABI LP64D and code model medlow.

* ``rv64imafdc/lp64d/medany``: ISA RV64IMAFDC with ABI LP64D and code model medany.

Interrupt Processing
====================

Interrupt exceptions are handled via the interrupt extensions API.  All other
exceptions end up in a fatal error (RTEMS_FATAL_SOURCE_EXCEPTION).

Interrupt Levels
----------------

There are exactly two interrupt levels on RISC-V with respect to RTEMS.  Level
zero corresponds to machine interrupts enabled.  Level one corresponds to
machine interrupts disabled.

Interrupt Stack
---------------

The memory region for the interrupt stack is defined by the BSP.

Default Fatal Error Processing
==============================

The default fatal error is BSP-specific.

Symmetric Multiprocessing
=========================

SMP is supported.

Thread-Local Storage
====================

Thread-local storage is supported.
