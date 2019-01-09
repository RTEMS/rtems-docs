.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 embedded brains GmbH <rtems@embedded-brains.de>
.. COMMENT: All rights reserved.

I2C Driver
**********

The Inter-Integrated Circuit (I2C, I²C, IIC) bus drivers should use the
`I2C bus framework <https://git.rtems.org/rtems/tree/cpukit/dev/include/dev/i2c/i2c.h>`_.
For example drivers see the
`Cadence I2C driver <https://git.rtems.org/rtems/tree/bsps/arm/xilinx-zynq/i2c/cadence-i2c.c>`_,
the
`Atmel SAM I2C driver <https://git.rtems.org/rtems/tree/bsps/arm/atsam/i2c/atsam_i2c_bus.c>`_
and the
`I2C framework test <https://git.rtems.org/rtems/tree/testsuites/libtests/i2c01/init.c>`_.

The user API is compatible to the
`Linux I2C user-space API <https://www.kernel.org/doc/Documentation/i2c/dev-interface>`_.
