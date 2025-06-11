% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2022 Mohd Noor Aman

% Copyright (C) 2024 Ning Yang

(BSP_aarch64_Raspberrypi_4)=

# Raspberry Pi 4B

The 'raspberrypi4b' BSP currently supports only the LP64 ABI. ILP32 is not
supported. Raspberry pi 4B all variants and Raspberry Pi 400 are supported.
The default bootloader which is used by the Raspbian OS or other OS can be used
to boot RTEMS. SMP is supported.

Raspberry Pi 4B has 2 types of interrupt controller, GIC-400 (GICv2) and ARM
legacy generic controller. Both are supported.

The documentation says that `enable_gic=1` is the default but that seems to
be true only if device tree is present otherwise it reverts to the legacy
interrupt controller. So set `enable_gic=1` in the `config.txt` file
to make sure gic is enable.

## Build Configuration Options

The following options can be used in the BSP section of the waf
configuration INI file. The waf defaults can be used to inspect the
values.

`CONSOLE_USE_INTERRUPTS`
: Use interrupt driven mode for console devices (enabled by default).

`GPU_CORE_CLOCK_RATE`
: The GPU processor core frequency in Hz (default is 500000000), The value of
  this option should be the same as the value of option `core_freq` in
  `config.txt`. [See the Raspberry Pi documentation for details](https://www.raspberrypi.com/documentation/computers/config_txt.html#overclocking).

`BSP_SPI_USE_INTERRUPTS`
: Use interrupt mode in the SPI driver (enabled by default).

`BSP_CLOCK_USE_SYSTEMTIMER`
: Use the `System Timer` in the clock driver (disable by default).

`BSP_CONSOLE_PORT`
: Default UART port for the console device (default is UART0). The optional
  ports are `UART0`, `UART2`, `UART3`, `UART4`, `UART5`.

`BSP_PL011_CLOCK_FREQ`
: PL011 UART clock frequency in Hz (default is 48000000). The value of
  this option should be the same as the value of option `init_uart_clock`
  in `config.txt`. [See the Raspberry Pi documentation for details](https://www.raspberrypi.com/documentation/computers/legacy_config_txt.html#init_uart_clock).

## Clock Driver

Raspberry pi 4B has two timers.

The `System Timer` and The `ARM Generic Timer`.

The clock from the ARM timer is derived from the system clock. This clock can
change dynamically e.g. if the system goes into reduced power or in low power
mode. Thus the clock speed adapts to the overall system performance
capabilities. For accurate timing it is recommended to use the system timers.

The clock driver uses the `ARM Generic Timer` by default.
Set `BSP_CLOCK_USE_SYSTEMTIMER = True` in the `Build Configuration Options`
to enable the `System Timer`.

## Console Driver

Raspberry pi 4B has 2 types of UARTs, ARM PL011 and Mini-uart. The PL011 is a
capable, broadly 16550-compatible UART, while the mini UART has a reduced
feature set. The console driver supports the default Qemu emulated ARM PL011
PrimeCell UART as well as the physical ARM PL011 PrimeCell UART in the
raspberrypi hardware. Mini-uart is not supported.

Set `BSP_CONSOLE_PORT` in the `Build Configuration Options` to set the
default UART port for the console device.

Initialize gpio of UART and install UART to the dev directory by
`raspberrypi_uart_init()` function.

```c
#include <assert.h>
#include <bsp/console.h>

void uart_init(void)
{
  int rv;

  /* The optional devices are UART0, UART2, UART3, UART4, UART5. */
  rv =  raspberrypi_uart_init(UART0);
  assert(rv == 0);
}
```

## GPIO Driver

The GPIO of Raspberry pi 4B can be controlled by the following functions:
`raspberrypi_gpio_set_function()`
`raspberrypi_gpio_set_pin()`
`raspberrypi_gpio_clear_pin()`
`raspberrypi_gpio_set_pull()`

```c #include <bsp/rpi-gpio.h>
void gpio(void)
{
  /* Define the operation of the general-purpose I/O pins. Each of the 58
   * GPIO pins has at least two alternative functions as defined.
   * The optional functions are GPIO_INPUT, GPIO_OUTPUT, GPIO_AF5, GPIO_AF4,
   * GPIO_AF0, GPIO_AF1, GPIO_AF2, GPIO_AF3
   */
  raspberrypi_gpio_set_function(8, GPIO_AF0);

  /* Control the actuation of the internal pull-up/down resistors.
   * The optional value are GPIO_PULL_NONE, GPIO_PULL_UP, GPIO_PULL_DOWN
   */
  raspberrypi_gpio_set_pull(8, GPIO_PULL_NONE);

  /* Clear a GPIO pin. */
  raspberrypi_gpio_clear_pin(8);

  /* Set a GPIO pin. */
  raspberrypi_gpio_set_pin(8);
}
```

## SPI Driver

The BCM2711 device has five SPI interfaces of this type: SPI0, SPI3, SPI4,
SPI5 & SPI6. It has two additional mini SPI interfaces (SPI1 and SPI2).
The SPI driver supports SPI0, SPI3, SPI4, SPI5 & SPI6. The mini SPI is not
supported.

SPI drivers are registered by the `raspberrypi_spi_init()` function.
The driver has no DMA support, but has interrupt support.

```c
#include <assert.h>
#include <bsp/raspberrypi-spi.h>

void spi_init(void)
{
  int rv;

  /*
   * The optional devices are raspberrypi_SPI0, raspberrypi_SPI3,
   * raspberrypi_SPI4, raspberrypi_SPI5, raspberrypi_SPI6.
   */
  rv =  raspberrypi_spi_init(raspberrypi_SPI0);
  assert(rv == 0);
}
```

## Watchdog Driver

```c
void raspberrypi_watchdog_example()
{
  raspberrypi_watchdog_init();
  raspberrypi_watchdog_start(15000);

  raspberrypi_watchdog_reload();
  /* ... */
  raspberrypi_watchdog_reload();

  raspberrypi_watchdog_stop();
}
```

The watchdog driver is used to implement BSP/system reset.

## Preparing to boot

Raspberry Pi uses a different mechanism to boot when compared with any ARM SoC.
First the GPU initializes, loads the bootloader (Raspberry pi firmware) and then
looks for the kernel img. This whole process is done by the GPU (VideoCore IV)
till the kernel is loaded. More information can be found on the [Raspberry pi
documentation page](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#boot-sequence).
By default the arm64 mode looks for the `kernel8.img`. Any other kernel can be
loaded by adding `kernel=<img_name>` to the `config.txt` file.

The Firmware files are required in order to boot RTEMS. The latest firmware can
be downloaded from the [Raspberry Pi Firmware Repository](https://github.com/raspberrypi/firmware/). USB boot is supported. All the
files (Firmwares and kernel) must be place in the FAT32 partition only. Add
`arm_64bit=1` in the `config.txt` file in order to boot the BSP in 64bit
kernel mode (it is default).

### UART Setup

Connect your serial device to the GPIO15 and GPIO14. Add the following to the
`config.txt` file in order to use the PL011 UART0 and thus disabling the
default Mini-uart.

A Minimal version of `config.txt` using UART0:
```ini
dtoverlay=disable-bt
arm_64bit=1
kernel=kernel8.img
enable_uart=1
```

### Generating kernel image

The following steps show how to run `hello.exe` on the BSP. Other executables
can be processed in a similar way.

To create the kernel image:

```shell
$ aarch64-rtems@rtems-ver-major@-objcopy -Obinary hello.exe kernel8.img
```

Copy the kernel image to the SD card.

## JTAG Setup

The Raspberry Pi 4 doesn't have dedicated JTAG pins. Instead, you must configure
the GPIO pins (GPIO22-GPIO27) to activate the JTAG functionality. The RPi 4
documentation refers to this as Alt4 functions of those pins. Alt5 does exist
too, which goes from GPIO4, 5, 6, 12 and 13. you can check this out from
[pinout.xyz](https://pinout.xyz/pinout/jtag#) or [eLinux](https://elinux.org/RPi_BCM2835_GPIOs)

One more thing to note on JTAG with Raspberry pi 4B is that, by default, All the
GPIO pins are pulled down, according to the [BCM2711 documentation](https://datasheets.raspberrypi.com/bcm2711/bcm2711-peripherals.pdf). This
wasn't the case in the earlier models. So in order to let the data flow freely,
we will have to disable them.

```none
# Disable pull downs
gpio=22-27=np

# Enable jtag pins (i.e. GPIO22-GPIO27)
enable_jtag_gpio=1
```

## Running Executables on QEMU

Executables generated by these BSPs can be run using the following command:

```shell
qemu-system-aarch64 -M raspi4b -serial mon:stdio -nographic \
 -kernel kernel8.img
```
