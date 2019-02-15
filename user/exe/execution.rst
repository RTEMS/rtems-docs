.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

.. _TargetExecution:

Target Execution
================
.. index::  Target Execution

Fixed position statically linked executables have a fixed address in a target's
address space. The location in the address space for code, data and read-only
data is fixed. The BSP defines the memory map and it is set by the BSP
developer based on the target's hardware requirements and it's bootloader.

Targets typically contains a bootloader that is executed after the target's
processor exits reset. A bootloader is specific to a target's processor and
hardware configuration and is responsible for the low level initialization of
the hardware resources needed to load and execute an operating system's
kernel. In the case of RTEMS this is the RTEMS executable.

Bootloaders vary in size, complexity and functionality. Some architectures have
a number of bootloader stages and others have only minimal support. An example
of a high end system is Xilinx's Zynq processor with three stages. First a mask
ROM in the System On Chip (SOC) executes after reset loading a first stage
bootloader (FSBL) from an SD card, QSPI flash or NAND flash depending on
signals connected to the device. The FSBL loads a second stage bootloader
(SSBL) such as U-Boot and this loads the kernel. U-Boot can be configured to
load a kernel from a range of media and file system formats as well as over a
network using a number of protocols. This structure provides flexibility at the
system level to support development environments such as a workshop or
laboratory through to tightly control production configurations.

Bootloaders often have custom formats for the executable image they load. The
formats can be simple to keep the bootloader simple or complex to support
check-sums, encryption or redundancy in case an image becomes corrupted. A
bootloader often provides a host tool that creates the required file from the
RTEMS executable's ELF file.

If RTEMS is to run from RAM the bootloader reads the image and loads the code,
initialized data and read-only data into the RAM and then jumps to a known
entry point. If the code is executed from non-volatile storage the process to
write the image into that storage will have extracted the various binary parts
and written those to the correct location.

The important point to note is the binary parts of the executable are somehow
loaded into the target's address space ready to execute. The way this done may
vary but the out come is always the same, the binary code, data and read-only
data is resident in the processor's address space at the BSP defined
addresses.
