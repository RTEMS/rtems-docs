% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 embedded brains GmbH & Co. KG

% Copyright (c) 2024 Purva Yeshi <purvayeshi550@gmail.com>

# riscv (RISC-V)

## riscv

**Each variant in this first group corresponds to a GCC multilib option with
different RISC-V standard extensions.**

- rv32i
- rv32iac
- rv32im
- rv32imac
- rv32imafc
- rv32imafd
- rv32imafdc
- rv64imac
- rv64imafd
- rv64imafdc

Each variant reflects an ISA with ABI and code model choice. All rv64 BSPs have
medany code model by default, while rv32 BSPs are medlow. The reason is that
RV32 medlow can access the entire 32-bit address space, while RV64 medlow can
only access addresses below 0x80000000. With RV64 medany, it's possible to
perform accesses above 0x80000000. The BSP must be started in machine mode.

The reference platforms for the rv\* variants include the QEMU `virt` and
`spike` machines and the Spike RISC-V ISA simulator.

**The BSP also provides the following variants for specific hardware targets:**

- frdme310arty - The reference platform for this variant is the Arty FPGA board
  with the SiFive Freedom E310 reference design.
- mpfs64imafdc - The reference platform for this variant is the Microchip
  PolarFire SoC Icicle Kit.
- kendrytek210 - The reference platform for this variant is the Kendryte K210
  SoC on the Sipeed MAiX BiT or Maixduino board.

### Build Configuration Options

The following options can be used in the BSP section of the `waf`
configuration INI file. The `waf` defaults can be used to inspect the values.

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

: The maximum size of the device tree blob in bytes (default is 65536).

`BSP_DTB_IS_SUPPORTED`

: If defined to a non-zero value, then the device tree blob is embedded in
  the BSP.

`BSP_DTB_HEADER_PATH`

: The path to the header file containing the device tree blob.

`BSP_CONSOLE_BAUD`

: The default baud for console driver devices (default is 115200).

`RISCV_MAXIMUM_EXTERNAL_INTERRUPTS`

: The maximum number of external interrupts supported by the BSP (default
  is 64).

`RISCV_ENABLE_HTIF_SUPPORT`

: Enable the Host/Target Interface (HTIF) support (enabled by default).

`RISCV_CONSOLE_MAX_NS16550_DEVICES`

: The maximum number of NS16550 devices supported by the console driver
  (default is 2).

`RISCV_ENABLE_SIFIVE_UART_SUPPORT`

: Enable the SiFive console UART (disabled by default).

`RISCV_RAM_REGION_BEGIN`

: The begin of the RAM region for linker command file
  (default is 0x80000000).

`RISCV_RAM_REGION_SIZE`

: The size of the RAM region for linker command file (default 64MiB).

`RISCV_ENABLE_FRDME310ARTY_SUPPORT`

: Enables support sifive Freedom E310 Arty board if defined to a non-zero
  value,otherwise it is disabled (disabled by default).

`RISCV_ENABLE_MPFS_SUPPORT`

: Enables support Microchip PolarFire SoC if defined to a non-zero
  value, otherwise it is disabled (disabled by default).

`RISCV_ENABLE_KENDRYTE_K210_SUPPORT`

: Enables support for the Kendtryte K210 SoC if defined to a non-zero
  value, otherwise it is disabled (disabled by default).

`RISCV_BOOT_HARTID`

: The boot hartid (processor number) of risc-v cpu by default 0.

### Interrupt Controller

Exactly one Core Local Interruptor (CLINT) and exactly one Platform-Level
Interrupt Controller (PLIC) are supported. The maximum number of external
interrupts supported by the BSP is defined by the
`RISCV_MAXIMUM_EXTERNAL_INTERRUPTS` BSP option.

### Clock Driver

The clock driver uses the CLINT timer.

### Console Driver

The console driver supports devices compatible to:

- "ucb,htif0" (depending on the `RISCV_ENABLE_HTIF_SUPPORT` BSP option),
- "ns16550a" (see `RISCV_CONSOLE_MAX_NS16550_DEVICES` BSP option),
- "ns16750" (see `RISCV_CONSOLE_MAX_NS16550_DEVICES` BSP option), and
- "sifive,uart0" (see `RISCV_ENABLE_SIFIVE_UART_SUPPORT` BSP option).

They are initialized according to the device tree. The console driver does not
configure the pins or peripheral clocks. The console device is selected
according to the device tree "/chosen/stdout-path" property value.

### QEMU

All of the BSP variants that start with rv can be run on QEMU's virt
and spike machines. For instance, to run the `rv64imafdc` BSP with the
following "config.ini" file.

```none
[riscv/rv64imafdc]
```

Run the following QEMU command.

```shell
$ qemu-system-riscv64 -M virt -nographic -bios $RTEMS_EXE
$ qemu-system-riscv64 -M spike -nographic -bios $RTEMS_EXE
```

### Spike

All of the BSP variants that start with rv can be run on Spike. For instance,
to run the `rv64imafdc` BSP with the following "config.ini" file.

```none
[riscv/rv64imafdc]
```

Run the following Spike command.

```shell
$ spike --isa=rv64imafdc $RTEMS_EXE
```

Unlike QEMU, Spike supports enabling/disabling a subset of the imafdc
extensions and has support for further RISC-V extensions as well. A fault will
be triggered if an executable built with rv64imafdc RISC-V's -march option run
on Spike with --isa=rv64i option. If no --isa option is specified, the default
is rv64imafdc.

## Microchip PolarFire SoC

The PolarFire SoC is the 4x 64-bit RISC-V U54 cores and a 64-bit RISC-V E51
monitor core SoC from the Microchip.

The `mpfs64imafdc` BSP variant supports the U54 cores but not the E51 because
the E51 monitor core is reserved for the first stage bootloader (Hart Software
Services). In order to boot from the first U54 core, `RISCV_BOOT_HARTID` is
set to 1 by default.

The device tree blob is embedded in the `mpfs64imafdc` BSP variant by default
with the `BSP_DTB_IS_SUPPORTED` enabled and the DTB header path
`BSP_DTB_HEADER_PATH` is set to bsp/mpfs-dtb.h.

**SMP test procedure for the Microchip PolarFire Icicle Kit:**

The "config.ini" file.

```none
[riscv/mpfs64imafdc]
BUILD_TESTS = True
RTEMS_POSIX_API=True
RTEMS_SMP = True
BSP_START_COPY_FDT_FROM_U_BOOT=False
BSP_VERBOSE_FATAL_EXTENSION = False
```

Build RTEMS.

```shell
$ ./waf configure --prefix=$HOME/rtems-start/rtems/@rtems-ver-major@
$ ./waf
```

Convert .exe to .elf file.

```shell
$ riscv-rtems@rtems-ver-major@-objcopy build/riscv/mpfs64imafdc/testsuites/smptests/smp01.exe build/riscv/mpfs64imafdc/testsuites/smptests/smp01.elf
```

Generate a payload for the `smp01.elf` using the [hss-payload-generator](https://github.com/polarfire-soc/hart-software-services/blob/master/tools/hss-payload-generator).

- Copy `smp01.elf` file to the HSS/tools/hss-payload-generator/test directory.
- Go to hss-payload-generator source directory.

```shell
$ cd hart-software-services/tools/hss-payload-generator
```

- Edit test/uboot.yaml file for the hart entry points and correct name of the
  binary file.

```none
set-name: 'PolarFire-SoC-HSS::RTEMS'
hart-entry-points: {u54_1: '0x1000000000', u54_2: '0x1000000000', u54_3: '0x1000000000', u54_4: '0x1000000000'}
payloads:
 test/smp01.elf: {exec-addr: '0x1000000000', owner-hart: u54_1, secondary-hart: u54_2, secondary-hart: u54_3, secondary-hart: u54_4, priv-mode: prv_m, skip-opensbi: true}
```

- Generate payload

```shell
$ ./hss-payload-generator -c test/uboot.yaml payload.bin
```

Once the payload binary is generated, it should be copied to the eMMC/SD.

[FPGA design with HSS programming file](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/boards/mpfs-icicle-kit-es/updating-icicle-kit/updating-icicle-kit-design-and-linux.md).

Program the eMMC/SD with the payload binary.

- Power Cycle the Microchip PolarFire Icicle Kit and stop at the HSS.
- type "mmc" and then "usbdmsc" on the HSS terminal(UART0).
- Load the payload.bin from the Host PC.

```shell
$ sudo dd if=payload.bin of=/dev/sdb bs=512
```

Reset the Microchip PolarFire SoC Icicle Kit.

Serial terminal UART1 displays the SMP example messages

```none
*** BEGIN OF TEST SMP 1 ***
*** TEST VERSION: 6.0.0.ef33f861e16de9bf4190a36e4d18062c7300986c
*** TEST STATE: EXPECTED_PASS
*** TEST BUILD: RTEMS_POSIX_API RTEMS_SMP
*** TEST TOOLS: 12.1.1 20220622 (RTEMS 6, RSB 3cb78b0b815ba05d17f5c6
            5865d246a8333aa087, Newlib ea99f21)

CPU 3 start task TA0
CPU 2 running Task TA0
CPU 3 start task TA1
CPU 1 running Task TA1
CPU 3 start task TA2
CPU 0 running Task TA2

*** END OF TEST SMP 1 ***
```

## Kendryte K210

The Kendryte K210 SoC is a dual core 64-bit RISC-V SoC with an AI NPU, built in
SRAM, and a variety of peripherals. Currently just the console UART, interrupt
controller, and timer are supported.

The device tree blob is embedded in the `kendrytek210` BSP variant by
default. When the kendrytek210 BSP variant is selected,
`BSP_DTB_IS_SUPPORTED` enabled and the DTB header path
`BSP_DTB_HEADER_PATH` is set to `bsp/kendryte-k210-dtb.h`.

The `kendrytek210` BSP variant has been tested on the following simulator and
boards:

- Renode.io simulator using the Kendrtye k210 model
- Sipeed MAiX BiT board
- Sipeed Maixduino board
- Sipeed MAiX Dock board

**Building the Kendryte K210 BSP**

Configuration file `config.ini`:

```none
[riscv/kendrytek210]
RTEMS_SMP = True
```

Build RTEMS:

```shell
$ ./waf configure --prefix=$HOME/rtems-start/rtems/@rtems-ver-major@
$ ./waf
```

**Flash an executable to a supported K210 board**

Binary images can be flashed to the Sipeed boards through the USB port using
the `kflash.py` utility available from the python pip utility.

```shell
$ riscv-rtems@rtems-ver-major@-objcopy -Obinary ticker.exe ticker.bin
$ kflash.py --uart /dev/ttyUSB0 ticker.bin
```

After the image is flashed, the RTEMS image will automatically boot. It will
also run when the board is reset or powered through the USB cable. The USB port
provides the power and console UART. Plug the USB cable into a host PC and
bring up a terminal emulator at 115200 baud, 8 data bits, 1 stop bit, no
parity, and no flow control. On Linux the UART device is often
`/dev/ttyUSB0`.

**Run a RTEMS application on the Renode.io simulator**

RTEMS executables compiled with the kendrytek210 BSP can run on the renode.io
simulator using the built-in K210 model. The simulator currently supports the
console UART, interrupt controller, and timer.

To install renode.io please refer to the [installation instructions](https://github.com/renode/renode#installation).
Once installed, save the following file as `k210_rtems.resc`.

```shell
using sysbus

$bin?=@ticker.exe

mach create "K210"

machine LoadPlatformDescription @platforms/cpus/kendryte_k210.repl

showAnalyzer uart

sysbus Tag <0x50440000 0x10000> "SYSCTL"
sysbus Tag <0x50440018 0x4> "pll_lock" 0xFFFFFFFF
sysbus Tag <0x5044000C 0x4> "pll1"
sysbus Tag <0x50440008 0x4> "pll0"
sysbus Tag <0x50440020 0x4> "clk_sel0"
sysbus Tag <0x50440028 0x4> "clk_en_cent"
sysbus Tag <0x5044002c 0x4> "clk_en_peri"

macro reset
"""
   sysbus LoadELF $bin
"""
runMacro $reset
```

After saving the above file in in the same directory as your RTEMS ELF images,
start renode and load the `k210_rtems.resc` script to start the emulation.

```shell
(monitor) s @k210_rtems.resc
```

You should see a renode UART window and the RTEMS ticker example output. If you
want to run a different RTEMS image, you can edit the file or enter the
following on the renode console.

```shell
(monitor) $bin=@smp08.exe
(monitor) s @k210_rtems.resc
```

The above example will run the SMP08 example instead of ticker.

**Generating the Device Tree Header**

The kendrytek210 BSP uses a built in device tree blob. If additional peripheral
support is added to the BSP, the device tree may need to be updated. After
editing the device tree source, compile it to a device tree blob with the
following command:

```shell
$ dtc -O dtb -b 0 -o kendryte-k210.dtb kendryte-k210.dts
```

The dtb file can then be converted to a C array using the rtems-bin2c tool.
The data for the device tree binary can then replace the existing device tree
binary data in the `kendryte-k210-dtb.h` header file.

## BeagleV-Fire

The BeagleV-Fire board is equipped with the Microchip’s PolarFire MPFS025T
System on Chip (SoC), featuring a 5-core configuration. It includes 4 RV64GC
cores for U54 and 1 RV64IMAC core for E51.

The Base BSP `riscv/beaglevfire` for BeagleV-Fire board supports Clock, IRQs, Console and UART.

**Configure the BSP:** Following section in the INI-style configuration
file, config.ini instructs the build system to build a
`riscv/beaglevfire` BSP variant

```shell
$ cd $HOME/quick-start/src/rtems

$ echo "[riscv/beaglevfire]" > config.ini
$ echo "BUILD_TESTS = True" >> config.ini
$ echo "RTEMS_POSIX_API = True" >> config.ini
$ echo "RTEMS_SMP = False" >> config.ini
$ echo "BSP_START_COPY_FDT_FROM_U_BOOT = False" >> config.ini
$ echo "BSP_VERBOSE_FATAL_EXTENSION = False" >> config.ini
```

The BeagleV-Fire supports Symmetric Multiprocessing (SMP) with its
quad-core configuration. SMP enables efficient parallel processing
across multiple cores, enhancing performance for multi-threaded
applications.

`RTEMS_SMP`: Set to `False` to run the system in uniprocessor mode,
where only one core (e.g., U54_1) handles processing.

To enable multiprocessing and utilize all available cores, set
`RTEMS_SMP = True` in config.ini. This configuration allows the
BeagleV-Fire to utilize all cores efficiently for parallel processing
tasks.

**Generate a payload for executables using
the**[hss-payload-generator](https://github.com/polarfire-soc/hart-software-services/tree/master/tools/hss-payload-generator)

- Copy executable file (e.g., hello.exe) to the HSS/tools/hss-payload-generator/test
  directory.
- Go to hss-payload-generator source directory.

```shell
$ cd hart-software-services/tools/hss-payload-generator
```

- Edit test/hss.yaml file for the hart entry points and correct name
  of the binary file (e.g., hello.exe).

  A modified test/hss.yaml file is [directly accessible in a fork](https://github.com/purviyeshi/hart-software-services.git)

For `uni-processing`:

```none
set-name: 'PolarFire-SoC-HSS::RTEMS'
hart-entry-points: {u54_1: '0x1000000000'}
payloads:
  test/hello.elf: {exec-addr: '0x1000000000', owner-hart: u54_1, priv-mode: prv_m, skip-opensbi: true}
```

For `multi-processing`:

```none
set-name: 'PolarFire-SoC-HSS::RTEMS'
hart-entry-points: {u54_1: '0x1000000000', u54_2: '0x1000000000', u54_3: '0x1000000000', u54_4: '0x1000000000'}
payloads:
  test/hello.elf: {exec-addr: '0x1000000000', owner-hart: u54_1, secondary-hart: u54_2, secondary-hart: u54_3, secondary-hart: u54_4, priv-mode: prv_m, skip-opensbi: true}
```

Generate payload:

```shell
$ make
$ ./hss-payload-generator -c test/uboot.yaml payload.bin
```

Once the payload binary is generated, it should be copied to the
eMMC/SD.

**Program the eMMC/SD with the payload binary:**

- Setting Up UART Communication via the Debug serial console from the Host PC

  1. List USB Serial Devices

  ```shell
  $ ls /dev | grep -i ttyUSB
  ```

  This will vary by host. The command lists all connected USB serial devices.
  Look for `ttyUSB0` or similar entries. See also the BeagleV-Fire docs.

  2. Modify the permissions of the identified USB serial device to
     allow read and write access

  ```shell
  $ sudo chmod 777 /dev/ttyUSB0
  ```

  3. Start a terminal session with the specified USB serial device at a
     baud rate of `115200`. This opens a communication channel
     between your host PC and the connected device

  ```shell
  $ screen /dev/ttyUSB0 115200
  ```

- Power up BeagleV-Fire board and stop at the HSS by pressing any key
  from keyboard (eg. Press `ENTER`)

- Enter HSS CLI commands

  ```shell
  $ MMC
  ```

  ```shell
  $ USBDMSC
  ```

  These commands switch the HSS to handle MMC (MultiMediaCard) and USB
  Device Mass Storage Class operations, preparing it for the binary
  payload transfer.

- Load the Payload from Host PC, use the `dd` command to
  copy the payload binary to the eMMC/SD card.
  Ensure the correct device path for eMMC/SD card. You can figure out which
  device to use for example by executing `ls -lt /dev/sd*` and seeing the
  most recently created disk, for example it could be `/dev/sdg`. You
  should be careful to check this before running the command to flash the
  device:

  ```shell
  $ sudo dd if=payload.bin of=/dev/sdg bs=512
  ```

**Reset the BeagleV-Fire board and check the output**

```none
*** BEGIN OF TEST HELLO WORLD ***
*** TEST VERSION: 6.0.0
*** TEST STATE: EXPECTED_PASS
*** TEST BUILD: RTEMS_POSIX_API
*** TEST TOOLS: 13.2.0 20230727 (RTEMS 6, RSB d24131ac781eeff8be5a4a5fd185d1be20176461, Newlib 176b19f)
Hello World

*** END OF TEST HELLO WORLD ***
```

## noel

This BSP supports the [NOEL-V](https://gaisler.com/noel-v) systems from
Cobham Gaisler. The NOEL-V is a synthesizable VHDL model of a processor that
implements the RISC-V architecture. It is part of the open source [GRLIB](https://gaisler.com/grlib) IP Library. The following BSP variants correspond
to common NOEL-V configurations:

- noel32im
- noel32imafd
- noel64imac
- noel64imafd
- noel64imafdc

The start of the memory is set to 0x0 to match a standard NOEL-V system, but
can be changed using the `RISCV_RAM_REGION_BEGIN` configuration option. The
size of the memory is taken from the information available in the device tree.

### Reference Designs

The BSP has been tested with NOEL-V reference designs for [Digilent Arty A7](https://gaisler.com/noel-artya7), [Microchip PolarFire Splash Kit](https://gaisler.com/noel-pf), and [Xilinx KCU105](https://gaisler.com/noel-xcku). See the accompanying quickstart guide for
each reference design to determine which BSP configuration to use.

### Build Configuration Options

The following options can be used in the BSP section of the `waf`
configuration INI file. The `waf` defaults can be used to inspect the values.

`BSP_CONSOLE_USE_INTERRUPTS`

: Use the Termios interrupt mode in the console driver (true by default).

`BSP_FDT_BLOB_SIZE_MAX`

: The maximum size of the device tree blob in bytes (262144 by default).

`RISCV_CONSOLE_MAX_APBUART_DEVICES`

: The maximum number of APBUART devices supported by the console driver
  (2 by default).

`RISCV_RAM_REGION_BEGIN`

: The begin of the RAM region for linker command file (0x0 by default).

`RISCV_MAXIMUM_EXTERNAL_INTERRUPTS`

: The maximum number of external interrupts supported by the BSP (64 by
  default).

## griscv

This RISC-V BSP supports chips using the
[GRLIB](https://www.gaisler.com/products/grlib/grlib.pdf).

## NIOS V

This BSP supports the [NIOS V](https://www.intel.com/content/www/us/en/products/details/fpga/intellectual-property/processors-peripherals/niosv.html)
systems from Intel. The NIOS V is a synthesizable Verilog model of a processor
that implements the RISC-V architecture. It is part of the Intel [Quartus Prime](https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html)
Design Software and free licenses can be obtained from the [Intel FPGA Self-
Service Licensing Center](https://licensing.intel.com/psg/s/?language=en_US).
The following BSP variant corresponds to an example configuration of a NIOS V
system running on an Intel FPGA Development Board:

- niosvc10lp - Cyclone 10 LP Evaluation Board (\$99)

The NIOS V IP comes in three variants: `NIOS V/c`, `NIOS V/m`, and
`NIOS V/g`. The `NIOS V/c` does not support an OS (no interrupt controller).
The `NIOS V/m` is a bare bones CPU with an interrupt controller, trap
controller, ECC module, timer, arihmetic logic unit, general purpose registers,
control and status registers, instruction/data buses, and JTAG debug module. The
`NIOS V/g` includes all the features of the `NIOS V/m` but adds an integer
mul/div unit, a floating point unit, support for custom instructions, tightly
coupled memory, and instruction/data caches. The floating point unit can be
disabled on the NIOS V/g to save resources.

### Reference Designs

The BSP has been tested on the [Intel Cyclone 10 LP Evaluation board](https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/cyclone/10-lp-evaluation-kit.html).
The reference design and how it was made can be found [here](https://ftp.rtems.org/pub/rtems/archive/misc/rtems/riscv-niosv-supporting-2024-10-23.tar.xz).
This compressed folder contains a `README.md` file which describes how the
reference design was built. The reference design implemented three different
variants of the NIOS V processor: V/m, V/g, V/g with FPU.

### Build Configuration Options

The following options will need to be used in the BSP section of the `waf`
configuration INI file. The `waf` defaults can be used to inspect the values.

`NIOSV_EPCQ_ROM_REGION_BEGIN`

: The starting address of the EPCQ device connected to the NIOS V
  (0x11000000 by default).

`NIOSV_EPCQ_ROM_REGION_SIZE`

: The size of the EPCQ device connected to the NIOS V
  (0x01000000 by default).

`NIOSV_ONCHIP_ROM_REGION_BEGIN`

: The starting address of the On-Chip ROM connected to the NIOS V
  (0x10010000 by default).

`NIOSV_ONCHIP_ROM_REGION_SIZE`

: The size of the On-Chip ROM connected to the NIOS V
  (4096 by default).

`NIOSV_ONCHIP_RAM_REGION_BEGIN`

: The starting address of the On-Chip RAM connected to the NIOS V
  (0x10020000 by default).

`NIOSV_ONCHIP_RAM_REGION_SIZE`

: The size of the On-Chip RAM connected to the NIOS V
  (8192 by default).

`NIOSV_EXT_RAM_REGION_BEGIN`

: The starting address of the external RAM connected to the NIOS V
  (0x01000000 by default).

`NIOSV_EXT_RAM_REGION_SIZE`

: The size of the external RAM connected to the NIOS V
  (0x00800000 by default).

`NIOSV_IS_NIOSVG`

: Whether or not the `NIOS V/g` processor is used
  (false by default).

`NIOSV_HAS_FP`

: Whether or not the `NIOS V/g` processor has a FPU
  (false by default).

### Building the Cyclone 10 LP BSP

Configuration file `config.ini` for NIOS V/m:

```none
[riscv/niosvc10lp]
NIOSV_EPCQ_ROM_REGION_BEGIN = 0x11000000
NIOSV_EPCQ_ROM_REGION_SIZE = 0x01000000
NIOSV_ONCHIP_ROM_REGION_BEGIN = 0x10010000
NIOSV_ONCHIP_ROM_REGION_SIZE = 4096
NIOSV_ONCHIP_RAM_REGION_BEGIN = 0x10020000
NIOSV_ONCHIP_RAM_REGION_SIZE = 8192
NIOSV_EXT_RAM_REGION_BEGIN = 0x01000000
NIOSV_EXT_RAM_REGION_SIZE = 0x00800000
NIOSV_IS_NIOSVG = False
NIOSV_HAS_FP = False
```

Configuration file `config.ini` for NIOS V/g:

```none
[riscv/niosvc10lp]
NIOSV_EPCQ_ROM_REGION_BEGIN = 0x11000000
NIOSV_EPCQ_ROM_REGION_SIZE = 0x01000000
NIOSV_ONCHIP_ROM_REGION_BEGIN = 0x10010000
NIOSV_ONCHIP_ROM_REGION_SIZE = 4096
NIOSV_ONCHIP_RAM_REGION_BEGIN = 0x10020000
NIOSV_ONCHIP_RAM_REGION_SIZE = 8192
NIOSV_EXT_RAM_REGION_BEGIN = 0x01000000
NIOSV_EXT_RAM_REGION_SIZE = 0x00800000
NIOSV_IS_NIOSVG = True
NIOSV_HAS_FP = False
```

Configuration file `config.ini` for NIOS V/g with FPU:

```none
[riscv/niosvc10lp]
NIOSV_EPCQ_ROM_REGION_BEGIN = 0x11000000
NIOSV_EPCQ_ROM_REGION_SIZE = 0x01000000
NIOSV_ONCHIP_ROM_REGION_BEGIN = 0x10010000
NIOSV_ONCHIP_ROM_REGION_SIZE = 4096
NIOSV_ONCHIP_RAM_REGION_BEGIN = 0x10020000
NIOSV_ONCHIP_RAM_REGION_SIZE = 8192
NIOSV_EXT_RAM_REGION_BEGIN = 0x01000000
NIOSV_EXT_RAM_REGION_SIZE = 0x00800000
NIOSV_IS_NIOSVG = True
NIOSV_HAS_FP = True
```

Build RTEMS:

```shell
$ ./waf configure --prefix=$HOME/rtems-start/rtems/@rtems-ver-major@
$ ./waf
```

### Program Cyclone 10 LP Evaluation Board

The `README.md` file in the compressed folder describes how to build
the FPGA configuration file, On-Chip ROM boot loader to load an executable from
the EPCQ device to external RAM, an application executable, and a `rtems_xx.jic`
file for programming onto the EPCQ device using the Quartus programmer.
