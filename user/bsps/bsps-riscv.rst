.. comment SPDX-License-Identifier: CC-BY-SA-4.0
.. comment Copyright (c) 2018 embedded brains GmbH

riscv (RISC-V)
**************

RISC-V
======

This BSP offers 13 variants:

* rv32i

* rv32iac

* rv32im

* rv32imac

* rv32imafc

* rv32imafd

* rv32imafdc

* rv64imac

* rv64imac_medany

* rv64imafd

* rv64imafd_medany

* rv64imafdc

* rv64imafdc_medany

Each variant corresponds to a GCC multilib.  A particular variant reflects an
ISA with ABI and code model choice.

The basic hardware initialization is not performed by the BSP.  A boot loader
with device tree support must be used to start the BSP, e.g. BBL.  The BSP must
be started im machine mode.

The reference platform for this BSP is the Qemu `virt` machine.

Build Configuration Options
---------------------------

The following options are available at the configure command line.

``BSP_PRESS_KEY_FOR_RESET``
    If defined to a non-zero value, then print a message and wait until pressed
    before resetting board when application terminates.

``BSP_RESET_BOARD_AT_EXIT``
    If defined to a non-zero value, then reset the board when the application
    terminates.

``BSP_PRINT_EXCEPTION_CONTEXT``
    If defined to a non-zero value, then print the exception context when an
    unexpected exception occurs.

``BSP_FDT_BLOB_SIZE_MAX``
    The maximum size of the device tree blob in bytes (default is 65536).

``BSP_CONSOLE_BAUD``
    The default baud for console driver devices (default 115200).

``RISCV_MAXIMUM_EXTERNAL_INTERRUPTS``
     The maximum number of external interrupts supported by the BSP (default
     64).

``RISCV_ENABLE_HTIF_SUPPORT``
     Enables the HTIF support if defined to a non-zero value, otherwise it is
     disabled (disabled by default).

``RISCV_CONSOLE_MAX_NS16550_DEVICES``
     The maximum number of NS16550 devices supported by the console driver (2
     by default).

``RISCV_RAM_REGION_BEGIN``
     The begin of the RAM region for linker command file (default is 0x70000000
     for 64-bit with -mcmodel=medlow and 0x80000000 for all other).

``RISCV_RAM_REGION_SIZE``
     The size of the RAM region for linker command file (default 64MiB).

Interrupt Controller
--------------------

Exactly one Core Local Interruptor (CLINT) and exactly one Platform-Level
Interrupt Controller (PLIC) are supported.  The maximum number of external
interrupts supported by the BSP is defined by the
``RISCV_MAXIMUM_EXTERNAL_INTERRUPTS`` BSP option.

Clock Driver
------------

The clock driver uses the CLINT timer.

Console Driver
--------------

The console driver supports devices compatible to

* "ucb,htif0" (depending on the ``RISCV_ENABLE_HTIF_SUPPORT`` BSP option),

* "ns16550a" (see ``RISCV_CONSOLE_MAX_NS16550_DEVICES`` BSP option), and

* "ns16750" (see ``RISCV_CONSOLE_MAX_NS16550_DEVICES`` BSP option).

They are initialized according to the device tree.  The console driver does not
configure the pins or peripheral clocks.  The console device is selected
according to the device tree "/chosen/stdout-path" property value.
