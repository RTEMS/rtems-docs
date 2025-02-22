% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2016, 2019 embedded brains GmbH & Co. KG

# I2C Driver

The Inter-Integrated Circuit (I2C, I²C, IIC) bus drivers should use the
[I2C bus framework](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/i2c.h).
The user API is compatible to the
[Linux I2C user-space API](https://www.kernel.org/doc/Documentation/i2c/dev-interface).

For example I2C bus drivers see:

- [Atmel SAM I2C driver](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/atsam/i2c/atsam_i2c_bus.c)
- [Cadence I2C driver](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/xilinx-zynq/i2c/cadence-i2c.c)
- [I2C framework test](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/testsuites/libtests/i2c01/init.c)
- [NXP i.MX I2C driver](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/imx/i2c/imx-i2c.c)
- [NXP LPC17XX/LPC24XX/LPC40XX I2C driver](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/arm/lpc24xx/i2c/i2c.c)

For example I2C device drivers see:

- ADC

  > - [TI ADS 16-Bit](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/ti-ads-16bit-adc.h)

- [EEPROM](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/eeprom.h)

- GPIO

  > - [NXP PCA9535](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/gpio-nxp-pca9535.h)

- Power Management

  > - [NXP PCA9548A](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/switch-nxp-pca9548a.h)
  > - [TI LM25066A](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/ti-lm25066a.h)

- Sensors

  > - [NXP LM75A](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/sensor-lm75a.h)
  > - [TI TMP112](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/dev/i2c/ti-tmp112.h)
