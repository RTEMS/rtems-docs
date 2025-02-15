.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016, 2019 embedded brains GmbH & Co. KG

SPI Driver
**********

The Serial Peripheral Interface (SPI) bus drivers should use the
`SPI bus framework
<https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/spi/spi.h>`_.
The user API is compatible to the
`Linux SPI user-space API <https://www.kernel.org/doc/Documentation/spi/spidev>`_.

For example SPI bus drivers see:

* `Atmel SAM SPI driver <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/atsam/spi/atsam_spi_bus.c>`_
* `NXP i.MX SPI driver <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/imx/spi/imx-ecspi.c>`_
* `NXP LPC17XX/LPC24XX/LPC40XX SSP driver <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/lpc24xx/spi/ssp.c>`_
* `SPI framework test <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/testsuites/libtests/spi01/init.c>`_
