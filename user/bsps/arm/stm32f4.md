% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 TBD
% Copyright (C) 2026 Moksh Panicker

# stm32f4

## Supported Hardware

The BSP is known to work on the following boards:

| Board | Notes |
|---|---|
| STM32F411 Black Pill (WeAct) | USB-C port wired to DWC2 USB OTG FS peripheral |
| NUCLEO-F401RE | On-board ST-Link; ST-Link USB is virtual COM port only |
| NUCLEO-F446RE | On-board ST-Link; ST-Link USB is virtual COM port only |
| STM32F407VG Discovery | On-board ST-Link V2 |

## Clock Driver

The clock driver uses the ARMv7-M SysTick peripheral. The STM32F411
runs at up to 100 MHz and the STM32F407 at up to 168 MHz. Clock
configuration is in `bsps/arm/stm32f4/start/bspstart.c`.

## Console Driver

The console uses a UART configured in the BSP.

On Nucleo boards the ST-Link virtual COM port connects to USART2
(PA2/PA3) at 115200 baud. The board appears as `/dev/ttyACM0` on Linux.

On the STM32F411 Black Pill the console is on USART1 (PA9 TX, PA10 RX)
at 115200 baud, 8N1. A USB-to-UART adapter connected to those pins is
required to read console output. The USB-C port on the Black Pill
connects to the DWC2 USB OTG peripheral (PA11/PA12) and does not
provide a serial console.

## How to Run an RTEMS Application on the Board

By following these simple steps, you can deploy your RTEMS application
on the board. These steps include:

- Building your RTEMS Application,
  already discussed in the {ref}`Build Your Application <QuickStartAPP>`.
- Flashing the application onto your board using either
  [OpenOCD](#flashing-with-openocd-nucleo-boards) or
  [stlink tools](#flashing-with-stlink-tools-all-boards).
- Viewing the serial output over
  [UART](#serial-monitor-output).

## Flashing with OpenOCD (Nucleo Boards)

This method uses OpenOCD and works well with Nucleo boards where the
on-board ST-Link exposes a GDB server.

Download and install OpenOCD for your host operating system.

Start OpenOCD using the configuration file for your board:

```shell
openocd -f board/st_nucleo_f4.cfg
```

Upon a successful connection you will see output similar to this:

```none
Open On-Chip Debugger 0.12.0
...
Info : [stm32f4x.cpu] Cortex-M4 r0p1 processor detected
Info : starting gdb server for stm32f4x.cpu on 3333
Info : Listening on port 3333 for gdb connections
```

Open another terminal and launch GDB with your compiled application:

```shell
arm-rtems7-gdb path/to/your/compiled/application
```

Connect to the OpenOCD GDB server, load, and run:

```none
(gdb) target remote :3333
(gdb) load
(gdb) cont
```

## Flashing with stlink Tools (All Boards)

The open-source `stlink` tools work with both Nucleo boards and the
STM32F411 Black Pill without requiring OpenOCD.

Install on Ubuntu or Debian:

```shell
sudo apt install stlink-tools
```

Verify the programmer is detected after connecting via USB:

```shell
st-info --probe
```

Expected output for an STM32F411:

```none
Found 1 stlink programmers
  version:    V2J45S7
  flash:      524288 (pagesize: 16384)
  sram:       131072
  chipid:     0x0431
  descr:      F411xC/E
```

If the output shows `Found 0 stlink programmers`, check that the USB
cable carries data (not power only) and install the udev rules:

```shell
sudo cp /usr/share/doc/stlink-tools/49-stlink.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
```

Unplug and reconnect the ST-Link, then retry `st-info --probe`.

Convert the ELF executable to a flat binary and flash it:

```shell
arm-rtems7-objcopy build/arm/stm32f4/testsuites/samples/hello.exe hello.bin
st-flash write hello.bin 0x8000000
```

A successful flash ends with:

```none
INFO common.c: Flash written and verified! jolly good!
```

If the board does not respond to flashing, try the reset variant:

```shell
st-flash --connect-under-reset write hello.bin 0x8000000
```

To debug with GDB using stlink tools, open two terminals.

**Terminal 1** — start the GDB server:

```shell
st-util
```

**Terminal 2** — connect GDB:

```shell
arm-rtems7-gdb build/arm/stm32f4/testsuites/samples/hello.exe
```

Inside GDB:

```none
(gdb) target extended-remote :4242
(gdb) load
(gdb) cont
```

## Serial Monitor Output

```{important}
The correct serial device depends on your board. Nucleo boards appear
as `/dev/ttyACM0` (ST-Link virtual COM port). The STM32F411 Black Pill
requires a USB-to-UART adapter on PA9 (TX) and PA10 (RX), which
typically appears as `/dev/ttyUSB0`.
```

Make sure your board is connected and minicom is installed:

```shell
sudo apt install minicom
```

Open the minicom configuration menu:

```shell
sudo minicom -s
```

- Go into **Serial port setup** and press **a** to select **Serial Device**.
- Change the device to `/dev/ttyACM0` (Nucleo) or `/dev/ttyUSB0` (Black Pill
  with USB-UART adapter) and press **Enter**.
- Press **f** to change hardware flow control from **Yes** to **No**.
- Scroll to **Exit** and press **Enter**.

Press the reset button on your board. Example output:

```none
*** BEGIN OF TEST HELLO WORLD ***
*** TEST VERSION: 7.0.0.a413333f2f04130e82e15addba402887222c345f
*** TEST STATE: EXPECTED_PASS
Hello World
*** END OF TEST HELLO WORLD ***

[ RTEMS shutdown ]
RTEMS version: 7.0.0.a413333f2f04130e82e15addba402887222c345f
RTEMS tools: 15.2.0 20250808 (RTEMS 7, ...)
executing thread ID: 0x0a010001
executing thread name: UI1
```

## Known Limitations

**No user USB connector on Nucleo boards:**
The NUCLEO-F401RE and NUCLEO-F446RE connect the STM32 USB OTG pins
(PA11, PA12) to the chip but do not expose them on a USB connector.
The only USB port on those boards is the ST-Link port, which handles
programming and the virtual COM port only. For USB peripheral
development or TinyUSB testing, use the STM32F411 Black Pill, which
has a USB-C connector wired to PA11/PA12 via the internal DWC2
Full Speed peripheral.

**No USB-to-serial bridge on Black Pill:**
The STM32F411 Black Pill USB-C port connects directly to the DWC2 USB
OTG peripheral, not to a serial bridge. Console output requires a
separate USB-to-UART adapter (CP2102 or CH340) on PA9 and PA10.

**Black Pill BOOT0 recovery:**
If the board enters the ROM bootloader and does not respond to
`st-flash`, hold BOOT0, press and release NRST, wait one second,
release BOOT0, then retry the flash command.

## Memory Map

| Region | Start address | Size |
|---|---|---|
| Flash | `0x08000000` | 512 KB (F411), 1 MB (F446), 1 MB (F407VG) |
| SRAM | `0x20000000` | 128 KB (F411), 128 KB (F446), 192 KB (F407VG) |

Measured footprint of RTEMS hello world on STM32F411 (arm/stm32f4 BSP,
GCC 15.2.0):

| Section | Size |
|---|---|
| Flash (.text + .rodata + .data load) | ~75 KB |
| RAM (.data + .bss) | ~6.5 KB |

## USB Support

The STM32F4 contains a Synopsys DWC2 USB OTG Full Speed peripheral
(USB\_OTG\_FS on PA11/PA12). This peripheral is supported by TinyUSB
via the `dwc2` driver. Porting TinyUSB to RTEMS with the STM32F411
Black Pill as the reference hardware platform is tracked in
{issue}`gsoc#38 <https://gitlab.rtems.org/rtems/programs/gsoc/-/issues/38>`.
