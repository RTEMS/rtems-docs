.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.


Target Dependent Files
######################

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
distribution are located in the directory ``c/src/lib/libbsp``.  The BSP source
directory is further subdivided based on the CPU family and BSP.

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
directory ``c/src/lib/libchip``.  The source code is further divided based upon
the class of hardware.  Example classes include serial communications
controllers, real-time clocks, non-volatile memory, and network controllers.

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
"rtems support". The RTEMS Project encourages users to use support services
however we do not endorse any providers.

CPU Dependent Executive Files
=============================

The CPU dependent files in the RTEMS executive source code are found in the
following directory:

.. code-block:: c

    cpukit/score/cpu/<CPU>

where <CPU> is replaced with the CPU family name.

Within each CPU dependent directory inside the executive proper is a file named
``<CPU>.h`` which contains information about each of the supported CPU models
within that family.

CPU Dependent Support Files
===========================

The CPU dependent support files contain routines which aid in the development
of applications using that CPU family.  For example, the support routines
may contain standard trap handlers for alignment or floating point exceptions
or device drivers for peripheral controllers found on the CPU itself.
This class of code may be found in the following directory:

.. code-block:: c

    c/src/lib/libcpu/<CPU>

CPU model dependent support code is found in the following directory:

.. code-block:: c

    c/src/lib/libcpu/<CPU>/<CPU_MODEL>

<CPU_MODEL> may be a specific CPU model name or a name indicating a CPU core or
a set of related CPU models.  The file ``configure.ac`` in each
``c/src/lib/libcpu/<CPU>`` directory contains the logic which enables the
appropriate subdirectories for the specific CPU model your BSP has.

Board Support Package Structure
===============================

The BSPs are all under the ``c/src/lib/libbsp`` directory.  Below this
directory, there is a subdirectory for each CPU family.  Each BSP is found
under the subdirectory for the appropriate processor family (arm, powerpc,
sparc, etc.).  In addition, there is source code available which may be shared
across all BSPs regardless of the CPU family or just across BSPs within a
single CPU family.  This results in a BSP using the following directories:

.. code-block:: c

    c/src/lib/libbsp/shared
    c/src/lib/libbsp/<CPU>/shared
    c/src/lib/libbsp/<CPU>/<BSP>

Under each BSP specific directory, there is a collection of subdirectories.
For commonly provided functionality, the BSPs follow a convention on
subdirectory naming.  The following list describes the commonly found
subdirectories under each BSP.

- ``console``:
  is technically the serial driver for the BSP rather than just a console
  driver, it deals with the board UARTs (i.e. serial devices).

- ``clock``:
  support for the clock tick - a regular time basis to the kernel.

- ``timer``:
  support of timer devices.

- ``rtc`` or ``tod``:
  support for the hardware real-time clock.

- ``nvmem``:
  support for non-volatile memory such as EEPROM or Flash.

- ``network``:
  the Ethernet driver.

- ``shmsupp``:
  support of shared memory driver MPCI layer in a multiprocessor system,

- ``include``:
  include files for this BSP.

- ``gnatsupp``:
  BSP specific support for the GNU Ada run-time.  Each BSP that wishes to have
  the possibility to map faults or exceptions into Ada language exceptions or
  hardware interrupts into Ada interrupt tasks must provide this support.

There may be other directories in the BSP tree and the name should be
indicative of the functionality of the code within that directory.

The build order of the BSP is determined by the Makefile structure.  This
structure is discussed in more detail in the :ref:`Makefiles` chapter.

.. sidebar:

This manual refers to the gen68340 BSP for numerous concrete examples.  You
should have a copy of the gen68340 BSP available while reading this piece of
documentation.  This BSP is located in the following directory:

.. code-block:: c

    c/src/lib/libbsp/m68k/gen68340

Later in this document, the $BSP340_ROOT label will be used to refer to this
directory.
