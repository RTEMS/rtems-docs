.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017, 2018 embedded brains GmbH

arm (ARM)
*********

altera-cyclone-v
================

TODO.

atsam
=====

TODO.

beagle
======

TODO.

csb336
======

TODO.

csb337
======

TODO.

edb7312
=======

TODO.

gdbarmsim
=========

TODO.

gumstix
=======

TODO.

imx (NXP i.MX)
==============

This BSP offers only one variant, the `imx7`.  This variant supports the i.MX
7Dual processor.  The basic hardware initialization is not performed by the
BSP.  A boot loader with device tree support must be used to start the BSP,
e.g. U-Boot.

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
    The maximum size of the device tree blob in bytes (default is 262144).

``CONSOLE_USE_INTERRUPTS``
    Use interrupt driven mode for console devices (enabled by default).

``IMX_CCM_IPG_HZ``
   The IPG clock frequency in Hz (default is 67500000).

``IMX_CCM_UART_HZ``
   The UART clock frequency in Hz (default is 24000000).

``IMX_CCM_AHB_HZ``
   The AHB clock frequency in Hz (default is 135000000).

Boot via U-Boot
---------------

The application executable file (ELF file) must be converted to an U-Boot
image.  Use the following commands:

::

    arm-rtems5-objcopy -O binary app.exe app.bin
    gzip -9 -f -c app.bin > app.bin.gz
    mkimage -A arm -O linux -T kernel -a 0x80200000 -e 0x80200000 -n RTEMS -d app.bin.gz app.img

Use the following U-Boot commands to boot an application via TFTP download:

::

    tftpboot ${loadaddr} app.img && run loadfdt && bootm ${loadaddr} - ${fdt_addr} ; reset

Clock Driver
------------

The clock driver uses the `ARMv7-AR Generic Timer`.

Console Driver
--------------

The console driver supports up to seven on-chip UARTs.  They are initialized
according to the device tree.  The console driver does not configure the pins.

I2C Driver
----------

I2C drivers are registered by the ``i2c_bus_register_imx()`` function.  The I2C
driver does not configure the pins.

.. code-block:: c

    #include <assert.h>
    #include <bsp.h>

    void i2c_init(void)
    {
      int rv;

      rv = i2c_bus_register_imx("/dev/i2c-0", "i2c0");
      assert(rv == 0);
    }

SPI Driver
----------

SPI drivers are registered by the ``spi_bus_register_imx()`` function.  The SPI
driver configures the pins according to the ``pinctrl-0`` device tree property.
SPI transfers with a continuous chip select are limited by the FIFO size of 64
bytes.  The driver has no DMA support.

.. code-block:: c

    #include <assert.h>
    #include <bsp.h>

    void spi_init(void)
    {
      int rv;

      rv =  spi_bus_register_imx("/dev/spi-0", "spi0");
      assert(rv == 0);
    }

Network Interface Driver
------------------------

The network interface driver is provided by the `libbsd`.  It is initialized
according to the device tree.  It supports checksum offload and interrupt
coalescing.  IPv6 transmit checksum offload is not implemented.  The interrupt
coalescing uses the MII/GMII clocks and can be controlled by the following
system controls:

 * ``dev.ffec.<unit>.int_coal.rx_time``
 * ``dev.ffec.<unit>.int_coal.rx_count``
 * ``dev.ffec.<unit>.int_coal.tx_time``
 * ``dev.ffec.<unit>.int_coal.tx_count``

A value of zero for the time or count disables the interrupt coalescing in the
corresponding direction.

MMC/SDCard Driver
-----------------

The MMC/SDCard driver (uSDHC module) is provided by the `libbsd`.  It is
initialized according to the device tree.  Pin re-configuration according to
the serial clock frequency is not supported.  Data transfers are extremely
slow.  This is probably due to the missing DMA support.

Caveats
-------

The clock and pin configuration support is quite rudimentary and mostly relies
on the boot loader.  For a pin group configuration see
``imx_iomux_configure_pins()``.  There is no power management support.

lm3s69xx
========

TODO.

lpc176x
=======

TODO.

lpc24xx
=======

TODO.

lpc32xx
=======

TODO.

raspberrypi
===========

TODO.

realview-pbx-a9
===============

TODO.

rtl22xx
=======

TODO.

smdk2410
========

TODO.

stm32f4
=======

TODO.

tms570
======

TODO.

xilinx-zynq
===========

TODO.
