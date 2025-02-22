% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 embedded brains GmbH & Co. KG

% Copyright (C) 2020 Christian Mauderer

# imxrt (NXP i.MXRT)

This BSP offers multiple variants. The `imxrt1052` supports the i.MXRT 1052
processor on a IMXRT1050-EVKB (tested with rev A1). Some possibilities to adapt
it to a custom board are described below.

NOTE: The IMXRT1050-EVKB has an backlight controller that must not be enabled
without load. Make sure to either attach a load, disable it by software or
disable it by removing the 0-Ohm resistor on it's input.

The `imxrt1166-cm7-saltshaker` supports an application specific board. Adapting
it to another i.MXRT1166 based board works similar like for the `imxrt1052` BSP.

## Build Configuration Options

Please see the documentation of the `IMXRT_*` and `BSP_*` configuration options
for that. You can generate a default set of options with:

```
./waf bspdefaults --rtems-bsps=arm/imxrt1052 > config.ini
```

## Adapting to a different board

This is only a short overview for the most important steps to adapt the BSP to
another board. Details for most steps follow further below.

1. The device tree has to be adapted to fit the target hardware.
2. A matching clock configuration is necessary (simplest method is to generate
   it with the NXP PinMux tool)
3. The `dcd_data` has to be adapted. That is used for example to initialize
   SDRAM.
4. `imxrt_flexspi_config` has to be adapted to match the Flash connected to
   FlexSPI (if that is used).
5. `BOARD_InitDEBUG_UARTPins` should be adapted to match the used system
   console.

## Boot Process of IMXRT1050-EVKB

There are two possible boot processes supported:

1. The ROM code loads a configuration from HyperFlash (connected to FlexSPI),
   does some initialization (based on device configuration data (DCD)) and then
   starts the application. This is the default case. `linkcmds.flexspi` is used
   for this case.
2. Some custom bootloader does the basic initialization, loads the application
   to SDRAM and starts it from there. Select the `linkcmds.sdram` for this.

For programming the HyperFlash in case 1, you can use the on board debugger
integrated into the IMXRT1050-EVKB. You can generate a flash image out of a
compiled RTEMS application with for example:

```
arm-rtems@rtems-ver-major@-objcopy -O binary build/arm/imxrt1052/testsuites/samples/hello.exe hello.bin
```

Then just copy the generated binary to the mass storage provided by the
debugger. Wait a bit till the mass storage vanishes and re-appears. After that,
reset the board and the newly programmed application will start.

NOTE: It seems that there is a bug on at least some of the on board debuggers.
They can't write more than 1MB to the HyperFlash. If your application is bigger
than that (like quite some of the applications in libbsd), you should use an
external debugger or find some alternative programming method.

For debugging: Create a special application with a `while(true)` loop at end of
`bsp_start_hook_1`. Load that application into flash. Then remove the loop
again, build your BSP for SDRAM and use a debugger to load the application into
SDRAM after the BSP started from flash did the basic initialization.

## Flash Image

For booting from a HyperFlash (or other storage connected to FlexSPI), the ROM
code of the i.MXRT first reads some special flash header information from a
fixed location of the connected flash device. This consists of the Image vector
table (IVT), Boot data and Device configuration data (DCD).

In RTEMS, these flash headers are generated using some C-structures. If you use
a board other than the IMXRT1050-EVKB, those structures have to be adapted. To
do that re-define the following variables in your application (you only need the
ones that need different values):

```c
#include <bsp/flash-headers.h>
const uint8_t imxrt_dcd_data[] =
    { /* Your DCD data here */ };
const ivt imxrt_image_vector_table =
    { /* Your IVT here */ };
const BOOT_DATA_T imxrt_boot_data =
    { /* Your boot data here */ };
const flexspi_nor_config_t imxrt_flexspi_config =
    { /* Your FlexSPI config here */ };
```

You can find the default definitions in `bsps/arm/imxrt/start/flash-*.c`. Take a
look at the `i.MX RT1050 Processor Reference Manual, Rev. 4, 12/2019` chapter
`9.7 Program image` or `i.MX RT1166 Processor Reference Manual, Rev. 0, 05/2021`
chapter `10.7 Program image` for details about the contents.

## FDT

The BSP uses a FDT based initialization. The FDT is linked into the application.
You can find the default FDT used in the BSPs in `bsps/arm/imxrt/dts`. The FDT
is split up into two parts. The controller specific part is put into an `dtsi`
file. The board specific one is in the dts file. Both are installed together
with normal headers into
`${PREFIX}/arm-rtems@rtems-ver-major@/${BSP}/lib/include`. You can use that to
create your own device tree based on that. Basically use something like:

```
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
```

You can then convert your FDT into a C file with (replace `YOUR.dts` and similar
with your FDT source names):

```none
sh> arm-rtems@rtems-ver-major@-cpp -P -x assembler-with-cpp \
           -I ${PREFIX}/arm-rtems@rtems-ver-major@/imxrt1052/lib/include \
           -include "YOUR.dts" /dev/null | \
       dtc -O dtb -o "YOUR.dtb" -b 0 -p 64
sh> rtems-bin2c -A 8 -C -N imxrt_dtb "YOUR.dtb" "YOUR.c"
```

You'll get a C file which defines the `imxrt_dtb` array. Make sure that your new
C file is compiled and linked into the application. It will overwrite the
existing definition of the `imxrt_dtb` in RTEMS.

## Clock Driver

The clock driver uses the generic `ARMv7-M Clock`.

## IOMUX

The i.MXRT IOMUXC is initialized based on the FDT. For that, the `pinctrl-0`
fields of all devices with a status of `ok` or `okay` will be parsed.

## Console Driver

LPUART drivers are registered based on the FDT. The special `rtems,path`
attribute defines where the device file for the console is created.

The `stdout-path` in the `chosen` node determines which LPUART is used for the
console.

## I2C Driver

I2C drivers are registered based on the FDT. The special `rtems,path` attribute
defines where the device file for the I2C bus is created.

Limitations:

- Only basic I2C is implemented. This is mostly a driver limitation and not a
  hardware one.

## SPI Driver

SPI drivers are registered based on the FDT. The special `rtems,path` attribute
defines where the device file for the SPI bus is created.

Note that the SPI-pins on the evaluation board are shared with the SD card.
Populate R278, R279, R280, R281 on the IMXRT1050-EVKB (Rev A) to use the SPI
pins on the Arduino connector.

By default, the native chip selects are used. If you want to use GPIOs as chip
select instead, you can use the `cs-gpios` and `num-cs` attributes just like on
a Linux SPI controller. A maximum of `IMXRT_LPSPI_MAX_CS` pins can be used.

The hardware doesn't support selecting no native chip select during a transfer.
Therefore one native chip select has to be reserved as a dummy if you want to be
able to use GPIOs. The pin function for this chip select must not be configured
on any pin. Dummy will be the first of the first four chip selects that is not a
native one. Example configuration:

```
&lpspi4 {
  status = "okay";
  pinctrl-0 = <&my_pinctrl_lpspi4>;
  cs-gpios = <0>, <0>, <&gpio1 1 0>, <0>, <&gpio11 5 1>;
  num-cs = <5>;
}
```

In this case, CS2 will be the dummy chip select and no pin must be configured
with that function. CS0, CS1 and CS3 are just native chip selects and should be
used via pin functions. GPIO1.1 is used as a high active CS and GPIO11.5 a low
active one.

Limitations:

- Only a basic SPI driver is implemented. This is mostly a driver limitation and
  not a hardware one.
- GPIO CS pins on i.MXRT10xx are not tested. The chip has a lot of errate so
  they might not work.
- Switching from one mode (CPOL/CPHA) to another one can lead to single wrong
  edges on the CLK line if GPIO CS pins are involved. Make sure to stuff a dummy
  transfer with `SPI_NO_CS` set if you use multiple modes together with a GPIO
  CS.

## Network Interface Driver

The network interface driver is provided by the `libbsd`. It is initialized
according to the device tree.

Note on the hardware: The i.MXRT1050 EVKB maybe has a wrong termination of the
RXP, RXN, TXP and TXN lines. The resistors R126 through R129 maybe shouldn't be
populated because the used KSZ8081RNB already has an internal termination.
Ethernet does work on short distance anyway. But keep it in mind in case you
have problems. Source:
<https://community.nxp.com/t5/i-MX-RT/Error-in-IMXRT1050-EVKB-and-1060-schematic-ethernet/m-p/835540#M1587>

## NXP SDK files

A lot of peripherals are currently not yet supported by RTEMS drivers. The NXP
SDK offers drivers for these. For convenience, the BSP compiles the drivers from
the SDK. But please note that they are not tested and maybe won't work out of
the box. Everything that works with interrupts most likely needs some special
treatment.

The SDK files are imported to RTEMS from the NXP mcux-sdk git repository that
you can find here: <https://github.com/nxp-mcuxpresso/mcux-sdk/>

The directory structure has been preserved and all files are in a
`bsps/arm/imxrt/mcux-sdk` directory. All patches to the files are marked with
`#ifdef __rtems__` markers.

The suggested method to import new or updated files is to apply all RTEMS
patches to the mcux-sdk repository, rebase them to the latest mcux-sdk release
and re-import the files. The new base revision should be mentioned in the commit
description to make future updates simpler.

A import helper script (that might or might not work on newer releases of the
mcux-sdk) can be found here:
<https://raw.githubusercontent.com/c-mauderer/nxp-mcux-sdk/d21c3e61eb8602b2cf8f45fed0afa50c6aee932f/export_to_RTEMS.py>

## Clocks and SDRAM

The clock configuration support is quite rudimentary. The same is true for
SDRAM. It mostly relies on the DCD and on a static clock configuration that is
taken from the NXP SDK example projects.

If you need to adapt the DCD or clock config to support a different hardware,
you should generate these files using the NXP MCUXpresso Configuration Tools.
You can add the generated files to your application to overwrite the default
RTEMS ones or you can add them to RTEMS in a new BSP variant.

As a special case, the imxrt1052 BSP will adapt it's PLL setting based on the
chip variant. The commercial variant of the i.MXRT1052 will use a core clock of
600MHz for the ARM core. The industrial variants only uses 528MHz. For other
chip or BSP variants, you should adapt the files generated with the MCUXpresso
Configuration Tools.

## Caveats

- The MPU settings are currently quite permissive.

- There is no power management support.

- On the i.MXRT1166, sleeping of the Cortex M7 can't be disabled even for
  debugging purposes. That makes it hard for a debugger to access the
  controller. To make debugging a bit easier, it's possible to overwrite the
  idle thread with the following one in the application:

  > ```c
  > void * _CPU_Thread_Idle_body(uintptr_t ignored)
  > {
  >   (void)ignored;
  >   while (true) {
  >     /* void */
  >   }
  > }
  > ```
