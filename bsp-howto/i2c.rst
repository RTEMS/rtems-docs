.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016, 2019 embedded brains GmbH & Co. KG

I2C Driver
**********

The Inter-Integrated Circuit (I2C, I²C, IIC) bus drivers should use the
`I2C bus framework <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/i2c.h>`_.
The user API is compatible to the
`Linux I2C user-space API <https://www.kernel.org/doc/Documentation/i2c/dev-interface>`_.

For example I2C bus drivers see:

* `Atmel SAM I2C driver <https://git.rtems.org/rtems/tree/bsps/arm/atsam/i2c/atsam_i2c_bus.c>`_
* `Cadence I2C driver <https://git.rtems.org/rtems/tree/bsps/arm/xilinx-zynq/i2c/cadence-i2c.c>`_
* `I2C framework test <https://git.rtems.org/rtems/tree/testsuites/libtests/i2c01/init.c>`_
* `NXP i.MX I2C driver <https://git.rtems.org/rtems/tree/bsps/arm/imx/i2c/imx-i2c.c>`_
* `NXP LPC17XX/LPC24XX/LPC40XX I2C driver <https://git.rtems.org/rtems/tree/bsps/arm/lpc24xx/i2c/i2c.c>`_

For example I2C device drivers see:

* ADC

   * `TI ADS 16-Bit <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/ti-ads-16bit-adc.h>`_

* `EEPROM <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/eeprom.h>`_

* GPIO

   * `NXP PCA9535 <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/gpio-nxp-pca9535.h>`_

* Power Management

   * `NXP PCA9548A <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/switch-nxp-pca9548a.h>`_

   * `TI LM25066A <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/ti-lm25066a.h>`_

* Sensors

   * `NXP LM75A <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/sensor-lm75a.h>`_

   * `TI TMP112 <https://git.rtems.org/rtems/tree/cpukit/include/dev/i2c/ti-tmp112.h>`_
