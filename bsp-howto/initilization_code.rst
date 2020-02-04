.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Initialization Code
*******************

.. warning::

   This chapter contains outdated and confusing information.

Introduction
============

The initialization code is the first piece of code executed when there's a
reset/reboot. Its purpose is to initialize the board for the application.  This
chapter contains a narrative description of the initialization process followed
by a description of each of the files and routines commonly found in the BSP
related to initialization.  The remainder of this chapter covers special issues
which require attention such as interrupt vector table and chip select
initialization.

Most of the examples in this chapter will be based on the SPARC/ERC32 and
m68k/gen68340 BSP initialization code.  Like most BSPs, the initialization for
these BSP is contained under the :file:`start` directory in the BSP source
directory.  The BSP source code for these BSPs is in the following directories:

.. code-block:: shell

    bsps/m68k/gen68340
    bsps/sparc/erc32

Both BSPs contain startup code written in assembly language and C.  The
gen68340 BSP has its early initialization start code in the ``start340``
subdirectory and its C startup code in the ``startup`` directory.  In the
``start340`` directory are two source files.  The file ``startfor340only.s`` is
the simpler of these files as it only has initialization code for a MC68340
board.  The file ``start340.s`` contains initialization for a 68349 based board
as well.

Similarly, the ERC32 BSP has startup code written in assembly language and C.
However, this BSP shares this code with other SPARC BSPs.  Thus the
``Makefile.am`` explicitly references the following files for this
functionality.

.. code-block:: shell

    ../../sparc/shared/start.S

.. note::

   In most BSPs, the directory named ``start340`` in the gen68340 BSP would be
   simply named ``start`` or start followed by a BSP designation.

Board Initialization
====================

This section describes the steps an application goes through from the time the
first BSP code is executed until the first application task executes.

The initialization flows from assembly language start code to the shared
``bootcard.c`` framework then through the C Library, RTEMS, device driver
initialization phases, and the context switch to the first application task.
After this, the application executes until it calls ``exit``,
``rtems_shutdown_executive``, or some other normal termination initiating
routine and a fatal system state is reached.  The optional
``bsp_fatal_extension`` initial extension can perform BSP specific system
termination.

The routines invoked during this will be discussed and their location in the
RTEMS source tree pointed out as we discuss each.

Start Code - Assembly Language Initialization
---------------------------------------------

The assembly language code in the directory ``start`` is the first part of the
application to execute.  It is responsible for initializing the processor and
board enough to execute the rest of the BSP.  This includes:

- initializing the stack

- zeroing out the uninitialized data section ``.bss``

- disabling external interrupts

- copy the initialized data from ROM to RAM

The general rule of thumb is that the start code in assembly should do the
minimum necessary to allow C code to execute to complete the initialization
sequence.

The initial assembly language start code completes its execution by invoking
the shared routine ``boot_card()``.

The label (symbolic name) associated with the starting address of the program
is typically called ``start``.  The start object file is the first object file
linked into the program image so it is ensured that the start code is at offset
0 in the ``.text`` section.  It is the responsibility of the linker script in
conjunction with the compiler specifications file to put the start code in the
correct location in the application image.

boot_card() - Boot the Card
---------------------------

The ``boot_card()`` is the first C code invoked.  This file is the core
component in the RTEMS BSP Initialization Framework and provides the proper
sequencing of initialization steps for the BSP, RTEMS and device drivers. All
BSPs use the same shared version of ``boot_card()`` which is located in the
`bsps/shared/start/bootcard.c <https://git.rtems.org/rtems/tree/bsps/shared/start/bootcard.c>`_
file.

The ``boot_card()`` routine performs the following functions:

- It disables processor interrupts.

- It sets the command line argument variables
  for later use by the application.

- It invokes the routine ``rtems_initialize_executive()`` which never returns.
  This routine will perform the system initialization through a linker set.
  The important BSP-specific steps are outlined below.

- Initialization of the RTEMS Workspace and the C Program Heap.  Usually the
  default implementation in
  `bsps/shared/start/bspgetworkarea-default.c <https://git.rtems.org/rtems/tree/bsps/shared/start/bspgetworkarea-default.c>`_
  should be sufficient.  Custom implementations can use
  ``bsp_work_area_initialize_default()`` or
  ``bsp_work_area_initialize_with_table()`` available as inline functions from
  ``#include <bsp/bootcard.h>``.

- Invocation of the BSP-specific routine ``bsp_start()`` which is written in C and
  thus able to perform more advanced initialization.  Often MMU, bus and
  interrupt controller initialization occurs here.  Since the RTEMS Workspace
  and the C Program Heap was already initialized by
  ``bsp_work_area_initialize()``, this routine may use ``malloc()``, etc.

- Specific initialization steps can be registered via the
  ``RTEMS_SYSINIT_ITEM()`` provided by ``#include <rtems/sysinit.h>``.

bsp_work_area_initialize() - BSP Specific Work Area Initialization
------------------------------------------------------------------

This is the first BSP specific C routine to execute during system
initialization.  It must initialize the support for allocating memory from the
C Program Heap and RTEMS Workspace commonly referred to as the work areas.
Many BSPs place the work areas at the end of RAM although this is certainly not
a requirement.  Usually the default implementation in
`bsps/shared/start/bspgetworkarea-default.c <https://git.rtems.org/rtems/tree/bsps/shared/start/bspgetworkarea-default.c>`_
should be sufficient.  Custom implementations can use
``bsp_work_area_initialize_default()`` or
``bsp_work_area_initialize_with_table()`` available as inline functions from
``#include <bsp/bootcard.h>``.

bsp_start() - BSP Specific Initialization
-----------------------------------------

This is the second BSP specific C routine to execute during system
initialization.  It is called right after ``bsp_work_area_initialize()``.  The
``bsp_start()`` routine often performs required fundamental hardware
initialization such as setting bus controller registers that do not have a
direct impact on whether or not C code can execute.  The interrupt controllers
are usually initialized here.  The source code for this routine is usually
found in the file ``bsps/${RTEMS_CPU}/${RTEMS_BSP}/start.c``.
It is not allowed to create any operating system objects, e.g. RTEMS
semaphores.

After completing execution, this routine returns to the ``boot_card()``
routine.  In case of errors, the initialization should be terminated via
``bsp_fatal()``.
