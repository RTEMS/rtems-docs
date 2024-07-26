.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH & Co. KG
.. Copyright (C) 2020 Sebastian Huber
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

System Initialization
*********************

Introduction
============

The system initialization consists of a low-level initialization performed by
the start code in the start file (:file:`start.o`) and a high-level
initialization carried out by :c:func:`boot_card()`.  The final step of a
successful high-level initialization is to switch to the initialization task
and change into the normal system mode with multi-threading enabled.  Errors
during system initialization are fatal and end up in a call to
:c:func:`_Terminate()`.

Low-Level Initialization via Start Code in the Start File (start.o)
===================================================================

The start code in the start file (:file:`start.o`) must be provided by the BSP.
It is the first file presented to the linker and starts the process to link an
executable (application image).  It should contain the entry symbol of the
executable.  It is the responsibility of the linker script in conjunction with
the compiler specifications file or compiler options to put the start code in
the correct location in the executable.  The start code is typically written in
assembly language since it will tinker with the stack pointer.  The general
rule of thumb is that the start code in assembly language should do the minimum
necessary to allow C code to execute to complete the initialization sequence.

The low-level system initialization may depend on a platform initialization
carried out by a boot loader.  The low-level system initialization may perform
the following steps:

* Initialize the initialization stack.  The initialization stack should use the
  ISR stack area.  The symbols :c:macro:`_ISR_Stack_area_begin`,
  :c:macro:`_ISR_Stack_area_end`, and :c:macro:`_ISR_Stack_size` should be used
  to do this.

* Initialize processor registers and modes.

* Initialize pins.

* Initialize clocks (PLLs).

* Initialize memory controllers.

* Initialize instruction, data, and unified caches.

* Initialize memory management or protection units (MMU).

* Initialize processor exceptions.

* Copy the data sections from a read-only section to the runtime location.

* Set the BSS (``.bss``) section to zero.

* Initialize the C runtime environment.

* Call :c:func:`boot_card()` to hand over to the high-level initialization.

For examples of start file codes see:

* `bsps/arm/shared/start/start.S <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/shared/start/start.S>`_

* `bsps/riscv/shared/start/start.S <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/riscv/shared/start/start.S>`_

High-Level Initialization via boot_card()
=========================================

The high-level initialization is carried out by :c:func:`boot_card()`.  For the
high-level initialization steps see the `Initialization Manager` chapter in the
RTEMS Classic API Guide.  There are several system initialization steps which
must be implemented by the BSP.

Early BSP Initialization
------------------------

The BSP may provide a system initialization handler (order
:c:macro:`RTEMS_SYSINIT_BSP_EARLY`) to perform an early BSP initialization.
This handler is invoked before the memory information and high-level dynamic
memory services (workspace and C program heap) are initialized.

Memory Information
------------------

The BSP must provide the memory information to the system with an
implementation of the :c:func:`_Memory_Get()` function.  The BSP should use the
default implementation in
`bsps/shared/shared/start/bspgetworkarea-default.c <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/shared/start/bspgetworkarea-default.c>`_.
The memory information is used by low-level memory consumers such as the
per-CPU data, the workspace, and the C program heap.  The BSP may use a system
initialization handler (order :c:macro:`RTEMS_SYSINIT_MEMORY`) to set up the
infrastructure used by :c:func:`_Memory_Get()`.

BSP Initialization
------------------

The BSP must provide an implementation of the :c:func:`bsp_start()` function.
This function is registered as a system initialization handler (order
:c:macro:`RTEMS_SYSINIT_BSP_START`) in the module implementing
:c:func:`boot_card()`.  The :c:func:`bsp_start()` function should perform a
general platform initialization.  The interrupt controllers are usually
initialized here.  The C program heap may be used in this handler.  It is not
allowed to create any operating system objects, e.g. RTEMS semaphores or tasks.
The BSP may register additional system initialization handlers in the module
implementing :c:func:`bsp_start()`.

Error Handling
==============

Errors during system initialization are fatal and end up in a call to
:c:func:`_Terminate()`.  See also the `Fatal Error Manager` chapter in the
RTEMS Classic API Guide.

The BSP may use BSP-specific fatal error codes, see
`<bsp/fatal.h> <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/include/bsp/fatal.h>`_.

The BSP should provide an initial extension which implements a fatal error
handler.  It should use the default implementation provided by
`<bsp/default-initial-extension.h> <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/include/bsp/default-initial-extension.h>`_ and
`bspfatal-default.c <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/shared/start/bspfatal-default.c>`_.
If the default implementation is used, the BSP must implement a
:c:func:`bsp_reset()` function which should reset the platform.
