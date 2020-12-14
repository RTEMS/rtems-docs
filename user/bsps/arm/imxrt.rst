.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH
.. Copyright (C) 2020 Christian Mauderer

imxrt (NXP i.MXRT)
==================

This BSP offers only one variant, the `imxrt1052`. This variant supports the
i.MXRT 1052 processor on a IMXRT1050-EVKB (tested with rev A1). You can also
configure it to work with custom boards.

Build Configuration Options
---------------------------

Please see the documentation of the `IMXRT_*` and `BSP_*` configuration options
for that. You can generate a default set of options with::

  ./waf bsp_defaults --rtems-bsps=arm/imxrt1052 > config.ini

Boot Process
------------

There are two possible boot processes supported:

1) The ROM code loads a configuration from HyperFlash (connected to FlexSPI),
   does some initialization (based on device configuration data (DCD)) and then
   starts the application. This is the default case. `linkcmds.flexspi` is used
   for this case.

2) Some custom bootloader does the basic initialization, loads the application
   to SDRAM and starts it from there. Select the `linkcmds.sdram` for this.

For programming the HyperFlash in case 1, you can use the on board debugger
integrated into the IMXRT1050-EVKB. You can generate a flash image out of a
compiled RTEMS application with for example::

  arm-rtems6-objcopy -O binary build/arm/imxrt1052/testsuites/samples/hello.exe hello.bin

Then just copy the generated binary to the mass storage provided by the
debugger. Wait a bit till the mass storage vanishes and re-appears. After that,
reset the board and the newly programmed application will start.

For debugging: Create a special application with a `while(true)` loop at end of
`bsp_start_hook_1`. Load that application into flash. Then remove the loop
again, build your BSP for SDRAM and use a debugger to load the application into
SDRAM after the BSP started from flash did the basic initialization.

Flash Image
-----------

For booting from a HyperFlash (or other storage connected to FlexSPI), the ROM
code of the i.MXRT first reads some special flash header information from a
fixed location of the connected flash device. This consists of the Image vector
table (IVT), Boot data and Device configuration data (DCD).

In RTEMS, these flash headers are generated using some C-structures. If you use
a board other than the IMXRT1050-EVKB, those structures have to be adapted. To
do that re-define the following variables in your application (you only need the
ones that need different values):

.. code-block:: c

  #include <bsp/flash-headers.h>
  const uint8_t imxrt_dcd_data[] =
      { /* Your DCD data here */ };
  const ivt imxrt_image_vector_table =
      { /* Your IVT here */ };
  const BOOT_DATA_T imxrt_boot_data =
      { /* Your boot data here */ };
  const flexspi_nor_config_t imxrt_flexspi_config =
      { /* Your FlexSPI config here */ };

You can find the default definitions in `bsps/arm/imxrt/start/flash-*.c`. Take a
look at the `i.MX RT1050 Processor Reference Manual, Rev. 4, 12/2019` chapter
`9.7 Program image` for details about the contents.

FDT
---

The BSP uses a FDT based initialization. The FDT is linked into the application.
You can find the default FDT used in the BSP in
`bsps/arm/imxrt/dts/imxrt1050-evkb.dts`. The FDT is split up into two parts. The
core part is put into an `dtsi` file and is installed together with normal
headers into `${PREFIX}/arm-rtems6/imxrt1052/lib/include`. You can use that to
create your own device tree based on that. Basically use something like::

  /dts-v1/;
  
  #include <imxrt/imxrt1050-pinfunc.h>
  #include <imxrt/imxrt1050.dtsi>
  
  &lpuart1 {
          pinctrl-0 = <&pinctrl_lpuart1>;
          status = "okay";
  };
  
  &chosen {
          stdout-path = &lpuart1;
  };
  
  /* put your further devices here */
  
  &iomuxc {
          pinctrl_lpuart1: lpuart1grp {
                  fsl,pins = <
                          IMXRT_PAD_GPIO_AD_B0_12__LPUART1_TX     0x8
                          IMXRT_PAD_GPIO_AD_B0_13__LPUART1_RX     0x13000
                  >;
          };
  
          /* put your further pinctrl groups here */
  };

You can then convert your FDT into a C file with (replace `YOUR.dts` and similar
with your FDT source names)::

  sh> arm-rtems6-cpp -P -x assembler-with-cpp \
                     -I ${PREFIX}/arm-rtems6/imxrt1052/lib/include \
                     -include "YOUR.dts" /dev/null | \
            dtc -@ -O dtb -o "YOUR.dtb" -b 0 -p 1024
  sh> rtems-bin2c -C -N imxrt_dtb "YOUR.dtb" "YOUR.c"

Make sure that your new c file is compiled and linked into the application.

Clock Driver
------------

The clock driver uses the generic `ARMv7-M Clock`.

IOMUX
-----

The i.MXRT IOMUXC is initialized based on the FDT. For that, the `pinctrl-0`
fields of all devices with a status of `ok` or `okay` will be parsed.

Console Driver
--------------

LPUART drivers are registered based on the FDT. The special `rtems,path`
attribute defines where the device file for the console is created.

The `stdout-path` in the `chosen` node determines which LPUART is used for the
console.

I2C Driver
----------

I2C drivers are registered based on the FDT. The special `rtems,path` attribute
defines where the device file for the I2C bus is created.

Limitations:

* Only basic I2C is implemented. This is mostly a driver limitation and not a
  hardware one.

SPI Driver
----------

SPI drivers are registered based on the FDT. The special `rtems,path` attribute
defines where the device file for the SPI bus is created.

Note that the SPI-pins on the evaluation board are shared with the SD card.
Populate R278, R279, R280, R281 on the IMXRT1050-EVKB (Rev A) to use the SPI
pins on the Arduino connector.

Limitations:

* Only a basic SPI driver is implemented. This is mostly a driver limitation and
  not a hardware one.

Network Interface Driver
------------------------

The network interface driver is provided by the `libbsd`. It is initialized
according to the device tree.

Note on the hardware: The i.MXRT1050 EVKB maybe has a wrong termination of the
RXP, RXN, TXP and TXN lines. The resistors R126 through R129 maybe shouldn't be
populated because the used KSZ8081RNB already has an internal termination.
Ethernet does work on short distance anyway. But keep it in mind in case you
have problems. Source:
https://community.nxp.com/t5/i-MX-RT/Error-in-IMXRT1050-EVKB-and-1060-schematic-ethernet/m-p/835540#M1587

NXP SDK files
-------------

A lot of peripherals are currently not yet supported by RTEMS drivers. The NXP
SDK offers drivers for these. For convenience, the BSP compiles the drivers from
the SDK. But please note that they are not tested and maybe won't work out of
the box. Everything that works with interrupts most likely needs some special
treatment.

Caveats
-------

The clock configuration support is quite rudimentary. The same is true for
SDRAM. It mostly relies on the DCD and on a static clock configuration that is
taken from the NXP SDK example projects.

The MPU settings are currently quite permissive.

There is no power management support.
