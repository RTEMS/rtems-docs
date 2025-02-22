% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2017, 2019 embedded brains GmbH & Co. KG

% Copyright (C) 2017, 2019 Sebastian Huber

# imx (NXP i.MX)

This BSP offers only one variant, the `imx7`. This variant supports the i.MX
7Dual processor and the i.MX 6UL/ULL processor family (with slightly different
clock settings). The basic hardware initialization is not performed by the BSP.
A boot loader with device tree support must be used to start the BSP, e.g.
U-Boot or barebox.

## Build Configuration Options

The following options can be used in the BSP section of the waf
configuration INI file. The waf defaults can be used to inspect the
values.

`BSP_PRESS_KEY_FOR_RESET`
: If defined to a non-zero value, then print a message and wait until pressed
  before resetting board when application terminates.

`BSP_RESET_BOARD_AT_EXIT`
: If defined to a non-zero value, then reset the board when the application
  terminates.

`BSP_PRINT_EXCEPTION_CONTEXT`
: If defined to a non-zero value, then print the exception context when an
  unexpected exception occurs.

`BSP_FDT_BLOB_SIZE_MAX`
: The maximum size of the device tree blob in bytes (default is 262144).

`CONSOLE_USE_INTERRUPTS`
: Use interrupt driven mode for console devices (enabled by default).

`IMX_CCM_IPG_HZ`
: The IPG clock frequency in Hz (default is 67500000).

`IMX_CCM_UART_HZ`
: The UART clock frequency in Hz (default is 24000000).

`IMX_CCM_ECSPI_HZ`
: The ECSPI clock frequency in Hz (default is 67500000).

`IMX_CCM_AHB_HZ`
: The AHB clock frequency in Hz (default is 135000000).

`IMX_CCM_SDHCI_HZ`
: The SDHCI clock frequency in Hz (default is 196363000).

## Clock settings for different boards

The default clock settings are targeted for an i.MX 7Dual evaluation board using
U-Boot. Some other boards with different boot loaders need different settings:

> - Phytec phyCORE-i.MX 6ULL (system on module) with MCIMX6Y2CVM08AB and a
>   barebox bootloader (version `2019.01.0-bsp-yocto-i.mx6ul-pd19.1.0`):
>
>   - IMX_CCM_IPG_HZ=66000000
>   - IMX_CCM_UART_HZ=80000000
>   - IMX_CCM_AHB_HZ=66000000
>   - IMX_CCM_SDHCI_HZ=198000000
>   - IMX_CCM_ECSPI_HZ=60000000

## Boot via U-Boot

The application executable file (ELF file) must be converted to an U-Boot
image. Use the following commands:

```none
arm-rtems@rtems-ver-major@-objcopy -O binary app.exe app.bin
gzip -9 -f -c app.bin > app.bin.gz
mkimage -A arm -O linux -T kernel -a 0x80200000 -e 0x80200000 -n RTEMS -d app.bin.gz app.img
```

Use the following U-Boot commands to boot an application via TFTP download:

```none
tftpboot ${loadaddr} app.img && run loadfdt && bootm ${loadaddr} - ${fdt_addr} ; reset
```

The `loadfdt` command may be not defined in your U-Boot environment. Just
replace it with the appropriate commands to load the device tree at
`${fdt_addr}`.

## Boot via barebox

The same command like for U-Boot can be used to generate an application image.
In a default configuration barebox expects an fdt image called `oftree` and a
kernel image called `zImage` in the root folder of the bootable medium (e.g. an
SD card).

## Clock Driver

The clock driver uses the `ARMv7-AR Generic Timer`.

## Console Driver

The console driver supports up to seven on-chip UARTs. They are initialized
according to the device tree. The console driver does not configure the pins.

## I2C Driver

I2C drivers are registered by the `i2c_bus_register_imx()` function. The I2C
driver does not configure the pins.

```c
#include <assert.h>
#include <bsp.h>

void i2c_init(void)
{
  int rv;

  rv = i2c_bus_register_imx("/dev/i2c-0", "i2c0");
  assert(rv == 0);
}
```

## SPI Driver

SPI drivers are registered by the `spi_bus_register_imx()` function. The SPI
driver configures the pins according to the `pinctrl-0` device tree property.
SPI transfers with a continuous chip select are limited by the FIFO size of 64
bytes. The driver has no DMA support.

```c
#include <assert.h>
#include <bsp.h>

void spi_init(void)
{
  int rv;

  rv =  spi_bus_register_imx("/dev/spi-0", "spi0");
  assert(rv == 0);
}
```

## Network Interface Driver

The network interface driver is provided by the `libbsd`. It is initialized
according to the device tree. It supports checksum offload and interrupt
coalescing. IPv6 transmit checksum offload is not implemented. The interrupt
coalescing uses the MII/GMII clocks and can be controlled by the following
system controls:

> - `dev.ffec.<unit>.int_coal.rx_time`
> - `dev.ffec.<unit>.int_coal.rx_count`
> - `dev.ffec.<unit>.int_coal.tx_time`
> - `dev.ffec.<unit>.int_coal.tx_count`

A value of zero for the time or count disables the interrupt coalescing in the
corresponding direction.

On the Phytec phyCORE-i.MX 6ULL modules the PHY needs an initialization for the
clock. A special PHY driver handles that (`ksz8091rnb`). Add it to your libbsd
config like that:

```c
#define RTEMS_BSD_CONFIG_BSP_CONFIG
#define RTEMS_BSD_CONFIG_INIT
SYSINIT_DRIVER_REFERENCE(ksz8091rnb, miibus);
#include <machine/rtems-bsd-config.h>
```

On chips with two Ethernet controllers, the MDIO lines are shared between the
two controllers for a number of chips variants. This is currently supported with
some restrictions on the initialization order. For this configuration to work,
you have to make sure that the pins are assigned to the Ethernet controller that
is initialized first. The initialization order in `libbsd` depends on the order
of the Ethernet controllers in the device tree. So if (for example) `fec2` is
defined in the device tree sources before `fec1`, make sure that the MDIO lines
are routed to `fec2` and that the Ethernet PHYs are a sub-node of `fec2` in the
device tree.

Note that the clock for the second Ethernet controller is not necessarily
enabled in the `CCM`. On the i.MX6UL/ULL, the clock will be enabled by the
startup code if the node that is compatible with `fsl,imx6ul-anatop` can be
found in the device tree. If you have trouble with the second Ethernet
controller make sure that the `ENET2_125M_EN` bit in the `CCM_ANALOG_PLL_ENET`
register is set as expected.

## MMC/SDCard Driver

The MMC/SDCard driver (uSDHC module) is provided by the `libbsd`. It is
initialized according to the device tree. Pin re-configuration according to
the serial clock frequency is not supported. Data transfers are extremely
slow. This is probably due to the missing DMA support.

## Caveats

The clock and pin configuration support is quite rudimentary and mostly relies
on the boot loader. For a pin group configuration see
`imx_iomux_configure_pins()`. There is no power management support.
