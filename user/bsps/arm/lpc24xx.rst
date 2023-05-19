.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017, 2019 embedded brains GmbH & Co. KG
.. Copyright (C) 2017, 2019 Sebastian Huber

lpc24xx (NXP LPC17XX/LPC24XX/LPC40XX)
=====================================

This BSP offers only several variants.  The following variants support the
`Embedded Artits LPC4088 Developer's Kit <https://www.embeddedartists.com/products/lpc4088-developers-kit/>`_
and earlier board generations:

* lpc17xx_ea_ram

* lpc17xx_ea_rom_int

* lpc24xx_ea

* lpc40xx_ea_ram

* lpc40xx_ea_rom_int

They can be used as a base line for customization.  The basic hardware
initialization is performed by the BSP.  It can be customized via configuration
options and configuration tables.  See also
`<bsp/start-config.h> <https://git.rtems.org/rtems/tree/bsps/arm/lpc24xx/include/bsp/start-config.h>`_.

Clock Driver
------------

The clock driver of the Cortex-M variants uses the `ARMv7-M Systick`.  The
older ARM7TDMI variants use the `TMR0` timer module.

Console Driver
--------------

The console driver supports up to four on-chip UARTs.  Initialization can be
customized via the ``lpc24xx_uart_probe_1()``, ``lpc24xx_uart_probe_2()`` and
``lpc24xx_uart_probe_3()`` functions.

I2C Bus Driver
--------------

I2C bus drivers are registered by the ``lpc24xx_register_i2c_0()``,
``lpc24xx_register_i2c_1()`` and ``lpc24xx_register_i2c_2()`` functions.  The
I2C driver does not configure the pins.  See also
`<bsp/i2c.h> <https://git.rtems.org/rtems/tree/bsps/arm/lpc24xx/include/bsp/i2c.h>`_.

SPI Bus Driver
--------------

SPI bus drivers are registered by the ``lpc24xx_register_ssp_0()``,
``lpc24xx_register_ssp_1()`` and ``lpc24xx_register_ssp_2()`` functions.  The
SSP driver does not configure the pins.  See also
`<bsp/ssp.h> <https://git.rtems.org/rtems/tree/bsps/arm/lpc24xx/include/bsp/ssp.h>`_.

Network Interface Driver
------------------------

Only a legacy network driver is support.  For a `libbsd` base driver the
platform support is missing, see
`if_lpe.c <https://git.rtems.org/rtems-libbsd/tree/rtemsbsd/sys/arm/lpc/if_lpe.c>`_.

USB Driver
----------

The USB host driver (OHCI) is provided by the `libbsd`.

Framebuffer Driver
------------------

For a custom framebuffer driver see
`<bsp/lcd.h> <https://git.rtems.org/rtems/tree/bsps/arm/lpc24xx/include/bsp/lcd.h>`_.

RTC Driver
----------

There is a standard RTC driver available using the on-chip RTC module.
