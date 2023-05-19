.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH & Co. KG

realview-pbx-a9
===============

The ``arm/realview_pbx_a9_qemu`` BSP is intended to be used with Qemu.  The
Qemu ``realview-pbx-a9`` machine can be used to run SMP tests using for example
the Qemu ``-smp 4`` command line option.

The command line to execute an ELF file :file:`app.exe` on this Qemu machine
is:

.. code-block:: none

    export QEMU_AUDIO_DRV="none"
    qemu-system-arm -net none -nographic -M realview-pbx-a9 -m 256M -kernel app.exe

You do not need to specify a device tree blob.
