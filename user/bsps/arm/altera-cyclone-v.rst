.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017, 2019 embedded brains GmbH
.. Copyright (C) 2017, 2019 Sebastian Huber

altera-cyclone-v (Intel Cyclone V)
==================================

This BSP offers only one variant, the `altcycv_devkit`.  This variant supports
the Intel Cyclone V system on chip.  The basic hardware initialization is not
performed by the BSP.  A boot loader with device tree support must be used to
start the BSP, e.g. U-Boot.

The BSP is known to run on these boards:

* `Cyclone V SoC Development Kit <https://www.intel.com/content/www/us/en/programmable/products/boards_and_kits/dev-kits/altera/kit-cyclone-v-soc.html>`_

* `Enclustra Mars MA3 SoC Module <https://www.enclustra.com/en/products/system-on-chip-modules/mars-ma3/>`_

* `Terasic DE10-Standard Development Kit <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=165&No=1081>`_

Boot via U-Boot
---------------

The application executable file (ELF file) must be converted to an U-Boot
image.  Use the following commands:

.. code-block:: none

    arm-rtems@rtems-ver-major@-objcopy -O binary app.exe app.bin
    gzip -9 -f -c app.bin > app.bin.gz
    mkimage -A arm -O linux -T kernel -a 0x00300000 -e 0x00300000 -n RTEMS -d app.bin.gz app.img

Use the following U-Boot commands to boot an application via TFTP download:

.. code-block:: none

    tftpboot ${loadaddr} app.img && run loadfdt && bootm ${loadaddr} - ${fdt_addr} ; reset

The ``loadfdt`` command may be not defined in your U-Boot environment.  Just
replace it with the appropriate commands to load the device tree at
``${fdt_addr}``.

Clock Driver
------------

The clock driver uses the `Cortex-A9 MPCore Global Timer`.

Console Driver
--------------

The console driver supports up to two on-chip NS16550 UARTs.  The console
driver does not configure the pins.

I2C Driver
----------

There is a legacy I2C driver.  It should be converted to the I2C driver framework.

Network Interface Driver
------------------------

The network interface driver is provided by the `libbsd`.  It is initialized
according to the device tree.  It supports checksum offload.

MMC/SDCard Driver
-----------------

The MMC/SDCard driver is provided by the `libbsd`.  It is
initialized according to the device tree.  Pin re-configuration according to
the serial clock frequency is not supported.  DMA transfers are supported.

USB Host Driver
---------------

The USB host driver is provided by the `libbsd`.  It is initialized according
to the device tree.  The driver works in polled mode.

Caveats
-------

The clock and pin configuration support is quite rudimentary and mostly relies
on the boot loader.
