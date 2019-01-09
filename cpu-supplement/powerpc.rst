.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

PowerPC Specific Information
****************************

Multilibs
=========

The following multilibs are available:

#. ``.``: 32-bit PowerPC with FPU

#. ``nof``: 32-bit PowerPC with software floating point support

#. ``m403``: Instruction set for PPC403 with FPU

#. ``m505``: Instruction set for MPC505 with FPU

#. ``m603e``: Instruction set for MPC603e with FPU

#. ``m603e/nof``: Instruction set for MPC603e with software floating
   point support

#. ``m604``: Instruction set for MPC604 with FPU

#. ``m604/nof``: Instruction set for MPC604 with software floating point
   support

#. ``m860``: Instruction set for MPC860 with FPU

#. ``m7400``: Instruction set for MPC7500 with FPU

#. ``m7400/nof``: Instruction set for MPC7500 with software floating
   point support

#. ``m8540``: Instruction set for e200, e500 and e500v2 cores with
   single-precision FPU and SPE

#. ``m8540/gprsdouble``: Instruction set for e200, e500 and e500v2 cores
   with double-precision FPU and SPE

#. ``m8540/nof/nospe``: Instruction set for e200, e500 and e500v2 cores
   with software floating point support and no SPE

#. ``me6500/m32``: 32-bit instruction set for e6500 core with FPU and
   AltiVec

#. ``me6500/m32/nof/noaltivec``: 32-bit instruction set for e6500 core
   with software floating point support and no AltiVec

#. ``me6500/m64``: 64-bit instruction set for e6500 core with FPU and
   AltiVec

#. ``me6500/m64/nof/noaltivec``: 64-bit instruction set for e6500 core
   with software floating point support and no AltiVec

Application Binary Interface
============================

In 32-bit PowerPC configurations the ABI defined by
`Power Architecture 32-bit Application Binary Interface Supplement 1.0 - Embedded <https://ftp.rtems.org/pub/rtems/people/sebh/Power-Arch-32-bit-ABI-supp-1.0-Embedded.pdf>`_
is used.

In 64-bit PowerPC configurations the ABI defined by
`Power Architecture 64-Bit ELF V2 ABI Specification, Version 1.1 <https://ftp.rtems.org/pub/rtems/people/sebh/ABI64BitOpenPOWERv1.1_16July2015_pub.pdf>`_
is used.

Special Registers
=================

The following special-purpose registers are used by RTEMS:

*Special-Purpose Register General 0 (SPRG0)*
    In SMP configurations, this register contains the address of the per-CPU
    control of the processor.

*Special-Purpose Register General 1 (SPRG1)*
    This register contains the interrupt stack pointer for the outer-most
    interrupt service routine.

*Special-Purpose Register General 2 (SPRG2)*
    This register contains the address of interrupt stack area begin.

Memory Model
============

The memory model is flat.

Interrupt Processing
====================

Interrupt Levels
----------------

There are exactly two interrupt levels on PowerPC with respect to RTEMS.  Level
zero corresponds to interrupts enabled.  Level one corresponds to interrupts
disabled.

Interrupt Stack
---------------

The interrupt stack size can be configured via the
``CONFIGURE_INTERRUPT_STACK_SIZE`` application configuration option.

Default Fatal Error Processing
==============================

The default fatal error handler is BSP-specific.

Symmetric Multiprocessing
=========================

SMP is supported.  Available platforms are the Freescale QorIQ P series (e.g.
P1020) and T series (e.g. T2080, T4240).

Thread-Local Storage
====================

Thread-local storage is supported.

64-bit Caveats
==============

* The thread pointer is ``r13`` in contrast to ``r2`` used in the 32-bit ABI.

* The TOC pointer is ``r2``.  It must be initialized as part of the C run-time
  setup.  A valid stack pointer is not enough to call C functions.  They may
  use the TOC to get addresses and constants.

* The TOC must be within the first 2GiB of the address space.  This simplifies
  the interrupt prologue, since the ``r2`` can be set to ``.TOC.`` via the
  usual ``lis`` followed by ``ori`` combination.  The ``lis`` is subject to
  sign-extension.

* The ``PPC_REG_LOAD``, ``PPC_REG_STORE``, ``PPC_REG_STORE_UPDATE``, and
  ``PPC_REG_CMP`` macros are available for assembly code to provide register
  size operations selected by the GCC ``-m32`` and ``-m64`` options.

* The ``MSR[CM]`` bit must be set all the time, otherwise the MMU translation
  my yield unexpected results.  The ``EPCR[ICM]`` or ``EPCR[GICM]`` bits may be
  used to enable the 64-bit compute mode for exceptions.
