.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.


Target Dependent Files
**********************

.. warning::

   This chapter contains outdated and confusing information.

RTEMS has a multi-layered approach to portability. This is done to maximize the
amount of software that can be reused. Much of the RTEMS source code can be
reused on all RTEMS platforms. Other parts of the executive are specific to
hardware in some sense.  RTEMS classifies target dependent code based upon its
dependencies into one of the following categories.

- CPU dependent

- Board dependent

- Peripheral dependent

CPU Dependent
=============

This class of code includes the foundation routines for the executive proper
such as the context switch and the interrupt subroutine implementations.
Sources for the supported processor families can be found in
``cpukit/score/cpu``.  A good starting point for a new family of processors is
the ``no_cpu`` directory, which holds both prototypes and descriptions of each
needed CPU dependent function.

CPU dependent code is further subcategorized if the implementation is dependent
on a particular CPU model.  For example, the MC68000 and MC68020 processors are
both members of the m68k CPU family but there are significant differences
between these CPU models which RTEMS must take into account.

The source code found in the ``cpukit/score/cpu`` is required to only depend
upon the CPU model variations that GCC distinguishes for the purposes of
multilib'ing.  Multilib is the term the GNU community uses to refer to building
a single library source multiple times with different compiler options so the
binary code generated is compatible.  As an example, from GCC's perspective,
many PowerPC CPU models are just a PPC603e.  Remember that GCC only cares about
the CPU code itself and need not be aware of any peripherals.  In the embedded
community, we are exposed to thousands of CPU models which are all based upon
only a relative small number of CPU cores.

Similarly for the SPARC/ERC32 BSP, the ``RTEMS_CPU`` is specified as ``erc32``
which is the name of the CPU model and BSP for this SPARC V7 system on chip.
But the multilib variant used is actually ``v7`` which indicates the ERC32 CPU
core is a SPARC V7.

Board Dependent
===============

This class of code provides the most specific glue between RTEMS and a
particular board.  This code is represented by the Board Support Packages and
associated Device Drivers.  Sources for the BSPs included in the RTEMS
distribution are located in the directory
`bsps <https://git.rtems.org/rtems/tree/bsps>`_.  The BSP source directory is
further subdivided based on the CPU family and BSP.

Some BSPs may support multiple board models within a single board family.  This
is necessary when the board supports multiple variants on a single base board.
For example, the Motorola MVME162 board family has a fairly large number of
variations based upon the particular CPU model and the peripherals actually
placed on the board.

Peripheral Dependent
====================

This class of code provides a reusable library of peripheral device drivers
which can be tailored easily to a particular board.  The libchip library is a
collection of reusable software objects that correspond to standard
controllers.  Just as the hardware engineer chooses a standard controller when
designing a board, the goal of this library is to let the software engineer do
the same thing.

The source code for the reusable peripheral driver library may be found in the
directory
`cpukit/dev <https://git.rtems.org/rtems/tree/cpukit/dev>`_ or
`bsps/shared/dev <https://git.rtems.org/rtems/tree/bsps/shared/dev>`_.  The
source code is further divided based upon the class of hardware.  Example
classes include serial communications controllers, real-time clocks,
non-volatile memory, and network controllers.

Questions to Ask
================

When evaluating what is required to support RTEMS applications on a particular
target board, the following questions should be asked:

- Does a BSP for this board exist?

- Does a BSP for a similar board exists?

- Is the board's CPU supported?

If there is already a BSP for the board, then things may already be ready to
start developing application software.  All that remains is to verify that the
existing BSP provides device drivers for all the peripherals on the board that
the application will be using.  For example, the application in question may
require that the board's Ethernet controller be used and the existing BSP may
not support this.

If the BSP does not exist and the board's CPU model is supported, then examine
the reusable chip library and existing BSPs for a close match.  Other BSPs and
libchip provide starting points for the development of a new BSP.  It is often
possible to copy existing components in the reusable chip library or device
drivers from BSPs from different CPU families as the starting point for a new
device driver.  This will help reduce the development effort required.

If the board's CPU family is supported but the particular CPU model on that
board is not, then the RTEMS port to that CPU family will have to be augmented.
After this is done, development of the new BSP can proceed.

Otherwise both CPU dependent code and the BSP will have to be written.

This type of development often requires specialized skills and there are people
in the community who provide those services.  If you need help in making these
modifications to RTEMS try a search in a search engine with something like
"RTEMS support". The RTEMS Project encourages users to use support services
however we do not endorse any providers.

CPU Dependent Executive Files
=============================

The CPU dependent files in the RTEMS executive source code are found in the
``cpukit/score/cpu/${RTEMS_CPU}`` directories.  The ``${RTEMS_CPU}`` is a
particular architecture, e.g. arm, powerpc, riscv, sparc, etc.

Within each CPU dependent directory inside the executive proper is a file named
:file:`cpu.h` which contains information about each of the supported CPU models
within that family.

Board Support Package Structure
===============================

The BSPs are all under the `bsps <https://git.rtems.org/rtems/tree/bsps>`_
directory.  The structure in this source subtree is:

* ``bsps/shared``
* ``bsps/${RTEMS_CPU}/shared``
* ``bsps/${RTEMS_CPU}/${RTEMS_BSP_FAMILY}``

The ``${RTEMS_CPU}`` is a particular architecture, e.g. arm, powerpc, riscv,
sparc, etc.  The ``shared`` directories contain code shared by all BSPs or BSPs
of a particular architecture.  The ``${RTEMS_BSP_FAMILY}`` directories contain
BSPs for a particular system on chip (SoC) or processor family.

Use the following structure under the
``bsps/${RTEMS_CPU}/${RTEMS_BSP_FAMILY}``:

* :file:`ata` - the legacy ATA/IDE driver
* :file:`btimer` - the legacy benchmark timer driver
* :file:`cache` - cache controller support
* :file:`clock` - the clock driver
* :file:`config` - build system configuration files
* :file:`console` - the console driver
* :file:`contrib` - imports of external sources

  * the layout of external sources should be used as is if possible

* :file:`i2c` - the I2C driver
* :file:`include` - public header files
* :file:`irq` - the interrupt controller support
* :file:`mpci` - support for heterogeneous multiprocessing
  (``RTEMS_MULTIPROCESSING``)
* :file:`net` - legacy network stack drivers
* :file:`rtc` - the RTC driver
* :file:`spi` - the SPI driver
* :file:`start` - everything required to run a minimal application without
  devices

  * :file:`start.S` - lowest level startup code
  * :file:`bspstart.c` - low level startup code
  * :file:`bspsmp.c` - SMP support
  * :file:`linkcmds` - a linker command file
