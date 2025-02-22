% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 TBD

# atsam

Board support package for the Atmel SAM V71/V70/E70/S70 chip platform.

The BSP is customized to a particular board/chip variant by means of BSP config
options.

Use `ATSAM_CHIP = XYZ` to select the chip variant where `XYZ` is one of
`same70j19`, `same70j20`, `same70j21`,
`same70n19`, `same70n20`, `same70n21`,
`same70q19`, `same70q20`, `same70q21`,
`sams70j19`, `sams70j20`, `sams70j21`,
`sams70n19`, `sams70n20`, `sams70n21`,
`sams70q19`, `sams70q20`, `sams70q21`,
`samv71j19`, `samv71j20`, `samv71j21`,
`samv71n19`, `samv71n20`, `samv71n21`,
`samv71q19`, `samv71q20`, `samv71q21`.
By default the BSP uses the ATSAMV71Q21 chip. Not all variants are tested.

Use `ATSAM_SDRAM = XYZ` to select the SDRAM variant where `XYZ` is one of
`is42s16100e-7bli`, `is42s16320f-7bl` and `mt48lc16m16a2p-6a`. Not all
variants are tested with all controller and speed combinations.

Use `BOARD_MAINOSC = XYZ` to set the main oscillator frequency in Hz (default
12MHz).

Use `ATSAM_MCK = XYZ` to set the MCK frequency that should be used. The
default case (123000000) enables operation of an external SDRAM on the SAMv71
Explained evaluation kit. Some other configurations (e.g. 150MHz) would be too
fast on that board.

Your application can also overwrite the clock settings. If you have a
bootloader with one setting in your internal flash and an application with
another setting in your external SDRAM, you should also use the
`ATSAM_CHANGE_CLOCK_FROM_SRAM = 1` option. To overwrite the clock settings,
define the following structures in your application:

```c
const struct atsam_clock_config atsam_clock_config = {
  .pllar_init = my_custom_pllar_value,
  .mckr_init = my_custom_mckr_value,
  .mck_freq = my_resulting_mck_frequency
};

const struct BOARD_Sdram_Config BOARD_Sdram_Config = {
  .sdramc_tr = my_custom_sdramc_tr_value,
  .sdramc_cr = my_custom_sdramc_cr_value,
  .sdramc_mdr = my_custom_sdramc_mdr_value,
  .sdramc_cfr1 = my_custom_sdramc_cfr1_value
};
```

Use `ATSAM_SLOWCLOCK_USE_XTAL = 0` to disable the usage of the external 32 kHz
oscillator for the slow clock. This is useful for example for the SAM E70
Xplained kit.

Use `ATSAM_CONSOLE_BAUD = XYZ` to set the initial baud for console devices
(default 115200).

Use `ATSAM_CONSOLE_DEVICE_TYPE = XYZ` to set the device type for
`/dev/console`, use `0` for USART and `1` for UART (default USART).

Use `ATSAM_CONSOLE_DEVICE_INDEX = XYZ` to set the device index for
`/dev/console` (default `1`, e.g. USART1).

Use `ATSAM_CONSOLE_USE_INTERRUPTS = XYZ` to set the use interrupt driven mode
for console devices (used by default).

Use `ATSAM_MEMORY_NULL_SIZE = XYZ` to set the size of NULL pointer protection
area in bytes (default `0x00000000`).

Use `ATSAM_MEMORY_TCM_SIZE = XYZ` to set the size of tightly coupled memories
(TCM) in bytes (default `0x00000000`). Note: ITCM is reduced by the
`ATSAM_MEMORY_NULL_SIZE`.

Use `ATSAM_MEMORY_QSPIFLASH_SIZE = XYZ` to set the size of QSPI flash in bytes
(default `0x00200000`).

The pins may be configured by the application at link-time. See
`<bsp/pin-config.h>`.

The clock driver uses the ARMv7-M Systick.

The console driver supports the USART and UART devices.

The default linker command file places the code into the internal flash. There
are the alternative linker command files `linkcmds.sdram`,
`linkcmds.qspiflash` and `linkcmds.intsram` that use other memories. To use
them in your application, add the following linker flags: `LDFLAGS += -qnolinkcmds -T linkcmds.XYZ`.

The fast text section uses the ITCM. The fast data section uses the DTCM.

Data and instruction cache are enabled during system start. The RTEMS cache
manager is supported with exception of the freeze functions.
