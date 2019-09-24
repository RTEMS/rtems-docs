.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 Vijay Kumar Banerjee

beagle
======

This BSP supports four variants, `beagleboardorig`, `beagleboardxm`,
`beaglebonewhite` and `beagleboneblack`. The basic hardware initialization is
not performed by the BSP.  A boot loader with device tree support must be used
to start the BSP, e.g., U-Boot.

TODO(These drivers are present but not documented yet):

 *  Clock driver.
 *  Network Interface Driver.
 *  SDcard driver.
 *  GPIO Driver.
 *  Console driver.
 *  PWM Driver.
 *  RTC driver.

Boot via U-Boot
---------------
To boot via uboot, the ELF must be converted to a U-Boot image like below:

.. code-block:: none

    arm-rtems5-objcopy hello.exe -O binary app.bin
    gzip -9 app.bin
    mkimage -A arm -O linux -T kernel -a 0x80000000 -e 0x80000000 -n RTEMS -d app.bin.gz rtems-app.img

Getting the Device Tree Blob
----------------------------

The Device Tree Blob (DTB) is needed to load the device tree while starting up
the kernel. We build the dtb from the FreeBSD source matching the commit hash
from the libbsd HEAD of freebsd-org. For example if the HEAD is at
"19a6ceb89dbacf74697d493e48c388767126d418"
Then the right Device Tree Source (DTS) file is:
https://github.com/freebsd/freebsd/blob/19a6ceb89dbacf74697d493e48c388767126d418/sys/gnu/dts/arm/am335x-boneblack.dts

Please refer to the :ref:`DeviceTree` to know more about building and applying
the Device Trees.

Writing the uEnv.txt file
-------------------------

The uEnv.txt file is needed to set any environment variable before the kernel is
loaded. Each line is a u-boot command that the uboot will execute during start
up.

Add the following to a file named uEnv.txt:

.. code-block:: none

     setenv bootdelay 5
     uenvcmd=run boot
     boot=fatload mmc 0 0x80800000 rtems-app.img ; fatload mmc 0 0x88000000 am335x-boneblack.dtb ; bootm 0x80800000 - 0x88000000

I2C Driver
----------

The Beagle has the `i2c-0` device registered at initialization. For registering
`i2c-1` and `i2c-2` ``bbb_register_i2c_1()`` and
``bbb_register_i2c_2()`` wrapper functions are respectively used.

For registering an I2C device with a custom path (say `/dev/i2c-3`) the
function ``am335x_i2c_bus_register()`` has to be used.

The function prototype is given below:

.. code-block:: C

   int am335x_i2c_bus_register(
   const char         *bus_path,
   uintptr_t           register_base,
   uint32_t            input_clock,
   rtems_vector_number irq
   );

SPI Driver
----------

The SPI device `/dev/spi-0` can be registered with ``bbb_register_spi_0()``

For registering with a custom path, the ``bsp_register_spi()`` can be used.

The function prototype is given below:

.. code-block:: C

    rtems_status_code bsp_register_spi(
       const char         *bus_path,
       uintptr_t           register_base,
       rtems_vector_number irq
    );
