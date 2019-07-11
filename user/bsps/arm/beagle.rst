.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 Vijay Kumar Banerjee

beagle
======

This BSP supports four variants, `beagleboardorig`, `beagleboardxm`, `beaglebonewhite`
and `beagleboneblack`. The basic hardware initialization is not performed by
the BSP.  A boot loader with device tree support must be used to start the BSP,
e.g. U-Boot.

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

    arm-rtems5-objcopy hello.exe -O app.bin
    gzip 9 app.bin
    mkimage -A arm -O linux -T kernel -a 0x80000000 -e 0x80000000 -n RTEMS -d app.bin.gz rtems-app.img

Getting the Device Tree Blob
----------------------------

The Device Tree Blob(dtb) is needed to load the device tree while starting up
the kernel. We build the dtb from the FreeBSD source matching the commit hash
from the libbsd HEAD of freebsd-org. For example if the HEAD is at
"19a6ceb89dbacf74697d493e48c388767126d418"
Then the right dts file is:
https://github.com/freebsd/freebsd/blob/19a6ceb89dbacf74697d493e48c388767126d418/sys/gnu/dts/arm/am335x-boneblack.dts

.. code-block:: none

     #building the dtb
     #We will use the script from https://github.com/freebsd/freebsd/blob/19a6ceb89dbacf74697d493e48c388767126d418/sys/tools/fdt/make_dtb.sh

     export MACHINE='arm' #The make_dtb.sh script uses environment variable MACHINE
     SCRIPT_DIR=$HOME/freebsd/sys/tools/fdt
     #The arguments to the script are
     # $1 -> Build Tree
     # $2 -> DTS source file
     # $3 -> output path of the DTB file
     ${SCRIPT_DIR}/make_dtb.sh ${SCRIPT_DIR}/../../ \
     ${SCRIPT_DIR}/../../gnu/dts/arm/am335x-boneblack.dts \
     $(pwd)
Writing the uEnv.txt file
-------------------------

The uEnv.txt file is needed to set any environment variable before the kernel is
loaded. Each line is a u-boot command that the uboot will execute during
starting up.

Add the following to a file named uEnv.txt:

.. code-block:: none

     setenv bootdelay 5
     uenvcmd=run boot
     boot=fatload mmc 0 0x80800000 rtems-app.img ; fatload mmc 0 0x88000000 am335x-boneblack.dtb ; bootm 0x80800000 - 0x88000000

I2C Driver
----------

This BSP uses the I2C framework and is registered using
``am335x_i2c_bus_register()`` the function prototype is given below:

.. code-block:: C

   int am335x_i2c_bus_register(
   const char         *bus_path,
   uintptr_t           register_base,
   uint32_t            input_clock,
   rtems_vector_number irq
   );

This function is needed only while registering with custom path with custom
values. For registering the `/dev/i2c-0` device, a wrapper function is provided,
``bbb_register_i2c_0()`` similarly ``bbb_register_i2c_1()`` and
``bbb_register_i2c_2()`` are respectively used to register `i2c-1` and `i2c-2`.

SPI Driver
----------

The SPI device `/dev/spi-0` can be registered with ``bbb_register_spi_0()```