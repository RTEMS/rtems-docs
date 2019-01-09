.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

Architectures
=============
.. index:: Architectures

An RTEMS architecture is a class or family of a processor that RTEMS
supports. The RTEMS architecture model follows the architecture model of
GCC. An architecture in GCC results in a specific RTEMS GCC compiler. This
compiler may support a range of processors in the family that may have
differences in instructions sets or floating point support. RTEMS configures
GCC to create separate runtime libraries for each supported instruction set and
floating point unit in the architecture. This is termed **multlib**. Multlibs
are manage automatically by GCC by selecting a specific instruction set or
specific device in a family.

RTEMS executables are statically linked for a specific target therefore a
precise and exact match can be made for the hardware that extracts the best
possible performance. The compiler supports the variants to the instruction set
and RTEMS extends the specialization to specific processors in an
architecture. This specialization gives RTEMS a finer resolution of features
and capabilites a specific device may offer allowing the kernel, drivers and
application to make the most of those resources. The trade off is portability
however this is not important because the executable are statically linked for
a single target.

.. note::

   RTEMS support dynamically load code through the ``dlopen``
   interface. Loading code via this interface results in an executable image
   that is equivalent to statically linked executable of the same code. Dynamic
   loading is a system level tool for system architects.

RTEMS supports 18 architectures:

- arm
- bfin
- epiphany
- i386
- lm32
- m68k
- mips
- moxie
- nios2
- no_cpu
- or1k
- riscv
- powerpc
- sh
- sparc
- sparc64
- v850
- x86_64
