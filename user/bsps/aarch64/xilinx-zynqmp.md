% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 On-Line Applications Research Corporation (OAR)

(bsp-aarch64-qemu-zynqmp-qemu-ilp32)=

(bsp-aarch64-qemu-zynqmp-qemu)=

(bsp-aarch64-qemu-zynqmp-apu-ilp32)=

(bsp-aarch64-qemu-zynqmp-apu)=

(bsp-aarch64-qemu-zynqmp-cfc400x)=

# Xilinx ZynqMP

This BSP family supports the following variants:

- `zynqmp_qemu_ilp32`
- `zynqmp_qemu`
- `zynqmp_apu_ilp32`
- `zynqmp_apu`
- `zynqmp_cfc400x`

Platform-specific hardware initialization is performed by ARM Trusted Firmware
(ATF). Other basic hardware initialization is performed by the BSP. These BSPs
support the GICv2 interrupt controller present in all ZynqMP systems. The
`zynqmp_apu` BSP has been tested on zu2cg, zu3eg, and zu9cg chip variants and
should also work on any other ZynqMP chip variant since the Processing Subsystem
(PS) does not vary among chip variants other than the number of CPU cores
available.

This BSP family has been tested on the following hardware:

- `Avnet UltraZed-EG SOM`
- `Innoflight CFC-400X`
- `Trenz TE0802`
- `Xilinx ZCU102`

## Boot on QEMU

The executable image is booted by Qemu in ELF format.

## Boot on ZynqMP Hardware

On ZynqMP hardware, RTEMS can be started at EL1, EL2, or EL3 by u-boot or
directly as part of BOOT.bin. Regardless of the exception level at boot, RTEMS
will drop to EL1 for execution. For quick turnaround during testing, it is
recommended to use the u-boot BOOT.bin that comes with the PetaLinux prebuilts
for the board in question.

Some systems such as the CFC-400X may require a bitstream to be loaded into the
FPGA portion of the chip to operate as expected. This bitstream must be loaded
before RTEMS begins operation since accesses to programmable logic (PL) memory
space can cause the CPU to hang if the FPGA is not initialized. This can be
performed as part of BOOT.bin or by a bootloader such as u-boot. Loading
bitstreams from RTEMS has not been tested on the ZynqMP platform and requires
additional libraries from Xilinx.

## Hardware Boot Image Generation

RTEMS expects some hardware initialization to be performed by ATF and expects
the services it provides to be present, so this must be included when generating
a direct-boot RTEMS BOOT.bin.

When booting via u-boot, RTEMS must be packaged into a u-boot image or booted
as a raw binary since u-boot does not currently support ELF64 which is required
for AArch64 ELF binaries.

## Example: Booting a RTEMS image on the ZCU102 ZynqMP board

This example will walk through the steps needed for booting RTEMS from a SD card
on the
[ZCU102 ZynqMP board.](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html)
The reference for setting up a SD card and obtaining pre-built boot images is
[here.](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841858/Board+bring+up+using+pre-built+images)

### Hardware Setup

Set the dip switch SW6 according to the table below. This will allow the board
to boot from the SD card. Connect a Micro-USB cable to the USB UART interface
J83. This is a quad USB UART interface which will show up on the development
host computer as four different serial or tty devices. Use the first channel
for the console UART. It should be set to 115k baud.

```{eval-rst}
+---------------------------+
| Dip Switch JW6            |
+------+------+------+------+
|  ON  |  OFF |  OFF |  OFF |
+------+------+------+------+
```

### Prepare a SD card with a bootable partition

The goal is to have a bootable SD card with a partition that is formatted with
the FAT file system. The file system will contain the boot artifacts including
BOOT.bin and the u-boot image. The RTEMS image will be placed on this volume. To
create the bootable SD card, follow the directions
[here.](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18842385/How+to+format+SD+card+for+SD+boot)

Once you have the card formatted correctly, you need to place the files from
[this archive](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/2202763266/2021.2+Release#Downloads)
on the FAT partition. The following file was used for this example:
[xilinx-vck190-v2021.2-final.bsp](https://www.xilinx.com/member/forms/download/xef.html?filename=xilinx-vck190-v2021.2-final.bsp)

In order to download these files, you need to have a Xilinx account login. As an
alternative, you can download a bootable image for Ubuntu 20.04 and write it to
an SD card using a utility such as [Balena Etcher](https://www.balena.io/etcher)
or dd. The Ubuntu image is available [here.](https://ubuntu.com/download/xilinx)
Download the image for the Zynq Ultrascale+ MPSoC Development boards, uncompress
it and write it to the SD card. This image creates multiple partitions, but we
only need to use the FAT partition with the boot artifacts on it.

### Verify that the board can boot from the SD card

It is worth booting the board from the SD card before trying to boot RTEMS.
Insert the card and power on the board. You should see the messages on the first
console indicating the various boot loader stages and eventually the Linux
kernel. The goal is to interrupt u-boot when given the chance to access the
u-boot command prompt.

### Build RTEMS with examples

Build the RTEMS `zynqmp_apu` BSP. Use the ticker.exe sample which
can be found in the directory:

```shell
build/aarch64/zynqmp_apu/testsuites/samples
```

### Prepare the RTEMS image

Prepare your RTEMS image to boot from u-boot with the following commands:

```shell
$ aarch64-rtems@rtems-ver-major@-objcopy -Obinary ticker.exe ticker.bin
$ gzip -9 ticker.bin
$ mkimage -A arm64 -O rtems -T kernel -a 0x10000 -e 0x10000 -n RTEMS -d ticker.bin.gz rtems.img
```

Note: If the start address has been changed in the BSP configuration, you have
to adapt the `-a` and `-e` parameters accordingly. To find out the start address
of an application, `aarch64-rtems6-nm ticker.exe | grep \ _start` can be used.
That will show the address of the `_start` symbol which is the value that has to
be used for the two parameters.

### Boot the RTEMS image

Copy the prepared RTEMS image to the SD card and insert the SD crd in the ZCU102
board. Power on the board. When you see the prompt on the console to interupt
u-boot, hit a key to bring up the u-boot command prompt. On the u-boot command
prompt you can boot your RTEMS image:

```shell
Zynq-MP> fatload mmc 0:1 0x1000 rtems.img
Zynq-MP> bootm 0x1000
```

This is the entire boot sequence:

```shell
Pre-FSBL boot Started
Xilinx Zynq MP First Stage Boot Loader
Release 2020.2   Nov 18 2020  -  11:46:01
NOTICE:  ATF running on XCZU9EG/silicon v1/RTL5.1 at 0xfffea000
NOTICE:  BL31: v2.2(release):xilinx_rebase_v2.2_2020.1-10-ge6eea88b1
NOTICE:  BL31: Built : 12:28:45, Nov 17 2020

U-Boot 2020.01 (Jun 15 2021 - 14:24:32 +0000)

Model: ZynqMP ZCU102 Rev1.0
Board: Xilinx ZynqMP
DRAM:  4 GiB
PMUFW:  v1.1
EL Level:       EL2
Chip ID:        zu9eg
NAND:  0 MiB
MMC:   mmc@ff170000: 0
In:    serial@ff000000
Out:   serial@ff000000
Err:   serial@ff000000
Bootmode: SD_MODE1
Reset reason:   SOFT
Net:
ZYNQ GEM: ff0e0000, mdio bus ff0e0000, phyaddr 12, interface rgmii-id

Warning: ethernet@ff0e0000 (eth0) using random MAC address - 82:32:1d:80:d9:c9
eth0: ethernet@ff0e0000
Hit any key to stop autoboot:  0

ZynqMP> fatload mmc 0:1 0x1000 rtems.img
46669 bytes read in 27 ms (1.6 MiB/s)
ZynqMP> bootm 0x1000
## Booting kernel from Legacy Image at 00001000 ...
   Image Name:   RTEMS
   Image Type:   AArch64 RTEMS Kernel Image (gzip compressed)
   Data Size:    46605 Bytes = 45.5 KiB
   Load Address: 10000000
   Entry Point:  10000000
   Verifying Checksum ... OK
   Uncompressing Kernel Image
## Transferring control to RTEMS (at address 10000000) ...

*** BEGIN OF TEST CLOCK TICK ***
*** TEST VERSION: @rtems-version@.f381e9bab29278e4434b1a93e70d17a7562dc64c
*** TEST STATE: EXPECTED_PASS
*** TEST BUILD: RTEMS_POSIX_API RTEMS_SMP
*** TEST TOOLS: 10.3.1 20210409 (RTEMS 6, RSB ad54d1dd3cf8249d9d39deb1dd28b2f294df062d, Newlib eb03ac1)
TA1  - rtems_clock_get_tod - 09:00:00   12/31/1988
TA2  - rtems_clock_get_tod - 09:00:00   12/31/1988
TA3  - rtems_clock_get_tod - 09:00:00   12/31/1988
TA1  - rtems_clock_get_tod - 09:00:05   12/31/1988
TA2  - rtems_clock_get_tod - 09:00:10   12/31/1988
TA1  - rtems_clock_get_tod - 09:00:10   12/31/1988
TA1  - rtems_clock_get_tod - 09:00:15   12/31/1988
TA3  - rtems_clock_get_tod - 09:00:15   12/31/1988
TA2  - rtems_clock_get_tod - 09:00:20   12/31/1988
TA1  - rtems_clock_get_tod - 09:00:20   12/31/1988
TA1  - rtems_clock_get_tod - 09:00:25   12/31/1988
TA2  - rtems_clock_get_tod - 09:00:30   12/31/1988
TA1  - rtems_clock_get_tod - 09:00:30   12/31/1988
TA3  - rtems_clock_get_tod - 09:00:30   12/31/1988

*** END OF TEST CLOCK TICK ***

[ RTEMS shutdown ]
```

### Follow up

This is just one possible way to boot the RTEMS image. For a development
environment you may wish to configure u-boot to boot the RTEMS image from a TFTP
server. For a production environment, you may wish to download, configure, and
build u-boot, or develop a BOOT.BIN image with the RTEMS application.

## Clock Driver

The clock driver uses the `ARM Generic Timer`.

## Console Driver

The console driver supports the default Qemu emulated ARM PL011 PrimeCell UART
as well as the physical ARM PL011 PrimeCell UART in the ZynqMP hardware.

## SDHCI Driver

The ZynqMP bsp has an SDHCI driver which allows writing to and reading from SD
cards. These can be tested in qemu using the "-sd" option. For example:

```shell
qemu-system-aarch64 -no-reboot -nographic -serial mon:stdio \
 -machine xlnx-zcu102 -m 4096 -kernel media01.exe -sd example.img
```

The SD card image should have an MSDOS partition table with a single partition
containing a FAT file system.

## Network Configuration

When used with LibBSD, these BSP variants support networking via the four
Cadence GEM instances present on all ZynqMP hardware variants. All interfaces
are enabled by default, but only interfaces with operational MII busses will be
recognized and usable in RTEMS. Most ZynqMP dev boards use RGMII with CGEM3.

When used with lwIP from the rtems-lwip integration repository, these BSP
variants support networking via CGEM0 and one of the other CGEM\* instances
simultaneously. This is a limitation of the Xilinx driver, specifically
in code referring directly to XPAR_XEMACPS_0_BASEADDR. Attempting to use more
than two interfaces simultaneously may cause unexpected behavior. Attempting to
use a set of two interfaces that does not include CGEM0 may cause unexpected
behavior.

The interfaces will not come up by default under lwIP and must be configured
manually. There are examples of this in the start_networking() implementation
in netstart.c as used by the network tests.

## Running Executables on QEMU

Executables generated by these BSPs can be run using the following command:

```shell
qemu-system-aarch64 -no-reboot -nographic -serial mon:stdio \
 -machine xlnx-zcu102 -m 4096 -kernel example.exe
```
