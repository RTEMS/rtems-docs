.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 DornerWorks
.. Copyright (C) 2019 Jeff Kubascik <jeff.kubascik@dornerworks.com>

xen (Xen on ARM)
================

This BSP enables RTEMS to run as a guest virtual machine in AArch32 mode on the
Xen hypervisor for ARMv8 platforms.

Drivers:

* Clock: ARMv7-AR Generic Timer

* Console: Virtual PL011 device

* Interrupt: GICv2

BSP variants:

* xen_virtual: completely virtualized guest with no dependence on underlying
  hardware

The xen_virtual BSP variant relies on standard Xen features, so it should be
able to run on any ARMv8 platform.

Xen allows for the passthrough of hardware peripherals to guest virtual
machines. BSPs could be added in the future targeting specific hardware
platforms and include the appropriate drivers.

This BSP was tested with Xen running on the Xilinx Zynq UltraScale+ MPSoC using
the Virtuosity distribution maintained by DornerWorks.

Execution
---------

This procedure describes how to run the ticker sample application that should
already be built with the BSP.

The ``ticker.exe`` file can be found in the BSP build tree at:

.. code-block:: none

    arm-rtems5/c/xen_virtual/testsuites/samples/ticker.exe

The ``ticker.exe`` elf file must be translated to a binary format.

.. code-block:: none

    arm-rtems5-objcopy -O binary ticker.exe ticker.bin

Then place the ``ticker.bin`` file on the dom0 filesystem.

From the dom0 console, create a configuration file ``ticker.cfg`` with the
following contents.

.. code-block:: none

    name = "ticker"1G
    kernel = "ticker.bin"
    memory = 8
    vcpus = 1
    gic_version = "v2"
    vuart = "sbsa_uart"

Create the virtual machine and attach to the virtual vpl011 console.

.. code-block:: none

    xl create ticker.cfg && xl console -t vuart ticker

To return back to the dom0 console, press both ``Ctrl`` and ``]`` on your
keyboard.

Additional Information
----------------------

* `Virtuosity distribution <https://dornerworks.com/xen/virtuosity>`_
