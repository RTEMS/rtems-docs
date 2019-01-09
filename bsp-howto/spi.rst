.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 embedded brains GmbH <rtems@embedded-brains.de>

SPI Driver
**********

The Serial Peripheral Interface (SPI) bus drivers should use the
`SPI bus framework
<https://git.rtems.org/rtems/tree/cpukit/dev/include/dev/spi/spi.h>`_.
For
example drivers see the
`Atmel SAM SPI driver <https://git.rtems.org/rtems/tree/bsps/arm/atsam/spi/atsam_spi_bus.c>`_
and the
`SPI framework test <https://git.rtems.org/rtems/tree/testsuites/libtests/spi01/init.c>`_.

The user API is compatible to the
`Linux SPI user-space API <https://www.kernel.org/doc/Documentation/spi/spidev>`_.
