% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Preetam Das

(BSP_aarch64_Raspberrypi_5)=

# Raspberry Pi 5

The BSP for the Raspberry Pi 5 `raspberrypi5` is currently in early state,
but supports features for a minimal BSP. The support include:

- ARM GIC-V2 Interrupts
- ARM Generic Clock
- Debug UART Port

More features and support for other peripherals are to be added soon after a
successful PCIe bringup.

## Interrupt Driver

The Pi 5 uses the GICv2 interrupt controller which is enabled by the shared
arm-gic-v2 driver in the BSP. The ARM local interrupt controller is not
available in the Pi 5.

## Clock Driver

By default the BSP uses the Arm Generic Timer with a clock frequency of 54Mhz
for its clock operations, which is implemented using the shared
arm-generic-timer driver.

The use of System/GPU timer can be enabled by the `BSP_CLOCK_USE_SYSTEMTIMER`
config option in config.ini.

Arm local timer has been discontinued in the Pi5. The peripheral exists but has
been stubbed out.

## Console Driver

Currently, the BSP only supports the PL011 Debug UART behind the 3pin JST port.
The other UARTS are hidden behind PCIe and need to be accessed via the RP1 chip.

By default the full console driver is enabled with interrupt mode. To use it in
polled mode set `BSP_CONSOLE_USE_INTERRUPTS = False` in config.ini. The device
file is named `/dev/console`.

## Preparing to boot

You need a few things to get started. A minimal setup includes a FAT32 formatted
SD Card with the following files:

1. config.txt
2. [bcm2712-rpi-5-b.dtb](https://github.com/raspberrypi/firmware/blob/master/boot/bcm2712-rpi-5-b.dtb)
3. kernel8.img

The config.txt file can be empty but it must be present else the Pi won't boot.

You can skip the device tree blob by putting `os_check=0` in config.txt but
better to just leave it there for now. Support for device tree is to come in the
future.

By default the firmware looks for the kernel_2712.img and falls back to
kernel8.img. If you want to specify your own kernel name like `kernel.img` you
can do so in config.txt by adding `kernel=kernel.img`.

To create the kernel image for your application you can use the `objcopy` tool:

```shell
$ aarch64-rtems@rtems-ver-major@-objcopy -Obinary hello.exe kernel8.img
```

A successful boot log will look something like this:

```shell
  0.87 RPi: BOOTSYS release VERSION:69471177 DATE: 2025/05/08 TIME: 15:13:17
  0.88 BOOTMODE: 0x06 partition 0 build-ts BUILD_TIMESTAMP=1746713597 serial fdb367bd boardrev c04170 stc 880031
  0.88 AON_RESET: 00000003 PM_RSTS 00001000
  0.89 POWER_OFF_ON_HALT: 0 WAIT_FOR_POWER_BUTTON 0 power-on-reset 1
  0.90 RP1_BOOT chip ID: 0x20001927
  0.90 PCIEx1: PWR 0 DET_WAKE 0
  0.90 part 00000000 reset_info 00000000
  0.91 PMIC reset-event 00000000 rtc 00000000 alarm 00000000 enabled 0
  0.91 uSD voltage 3.3V
  1.03 Initialising SDRAM rank 2 total-size: 32 Gbit 4267 (0x15 0x00)
  1.04 DDR 4267 1 0 32 152 BL:1
  2.79 OTP boardrev c04170 bootrom a a
  2.79 Customer key hash 0000000000000000000000000000000000000000000000000000000000000000
  2.80 VC-JTAG unlocked
  2.82 RP1_BOOT chip ID: 0x20001927

  3.46 RP1_BOOT chip ID: 0x20001927
  3.46 RP1_BOOT: fw size 46888
  4.10 PCI2 init
  4.10 PCI2 reset
  4.14 PCIe scan 00001de4:00000001
  4.14 RP1_CHIP_INFO 20001927

  4.15 RPi: BOOTLOADER release VERSION:69471177 DATE: 2025/05/08 TIME: 15:13:17
  4.15 BOOTMODE: 0x06 partition 0 build-ts BUILD_TIMESTAMP=1746713597 serial fdb367bd boardrev c04170 stc 4159326
  4.19 usb_pd_init status 3
  4.19 USB_PD CONFIG 0 41
  4.19 XHCI-STOP
  4.19 xHC0 ver: 272 HCS: 03000440 140000f1 07ff000a HCC: 0240fe6d
  4.20 USBSTS 1
  4.21 xHC0 ver: 272 HCS: 03000440 140000f1 07ff000a HCC: 0240fe6d
  4.21 xHC0 ports 3 slots 64 intrs 4
  4.22 XHCI-STOP
  4.22 xHC1 ver: 272 HCS: 03000440 140000f1 07ff000a HCC: 0240fe6d
  4.23 USBSTS 1
  4.23 xHC1 ver: 272 HCS: 03000440 140000f1 07ff000a HCC: 0240fe6d
  4.24 xHC1 ports 3 slots 64 intrs 4
  4.24 USB-PD: src-cap PDO object1 0x0a0191f4
  4.25 Current 5000 mA
  4.25 Voltage 5000 mV
  4.25 USB-PD: src-cap PDO object2 0x0002d12c
  4.25 Current 3000 mA
  4.26 Voltage 9000 mV
  4.26 USB-PD: src-cap PDO object3 0x0003c0e1
  4.26 Current 2250 mA
  4.26 Voltage 12000 mV
  4.27 USB-PD: src-cap PDO object4 0x0004b0b4
  4.27 Current 1800 mA
  4.27 Voltage 15000 mV
  4.79 Boot mode: SD (01) order f4
  4.79 SD HOST: 200000000 CTL0: 0x00800000 BUS: 400000 Hz actual: 390625 HZ div: 512 (256) status: 0x1fff0000 delay: 276
  4.80 SD HOST: 200000000 CTL0: 0x00800f00 BUS: 400000 Hz actual: 390625 HZ div: 512 (256) status: 0x1fff0000 delay: 276
  4.90 OCR c0ff8000 [148]
CID: 00ad4c5355534430301038942790018a
CSD: 400e0032db790000ec537f800a400000
  4.91 SD: bus-width: 4 spec: 2 SCR: 0x02358487 0x00000000
  4.92 SD HOST: 200000000 CTL0: 0x00800f04 BUS: 50000000 Hz actual: 50000000 HZ div: 4 (2) status: 0x1fff0000 delay: 2
  4.93 MBR: 0x00000800,61949952 type: 0x0c
  4.93 MBR: 0x00000000,       0 type: 0x00
  4.94 MBR: 0x00000000,       0 type: 0x00
  4.94 MBR: 0x00000000,       0 type: 0x00
  4.48 Trying partition: 0
  4.50 type: 32 lba: 2048 'mkfs.fat' ' RTEMS      ' clusters 1934989 (32)
  4.95 rsc 32 fat-sectors 15136 root dir cluster 2 sectors 0 entries 0
  4.96 FAT32 clusters 1934989
  4.96 [sdcard] autoboot.txt not found
  4.96 Select partition rsts 0 C(boot_partition) 0 EEPROM config 0 result 1
  4.76 Trying partition: 1
  4.78 type: 32 lba: 2048 'mkfs.fat' ' RTEMS      ' clusters 1934989 (32)
  4.98 rsc 32 fat-sectors 15136 root dir cluster 2 sectors 0 entries 0
  4.99 FAT32 clusters 1934989
  4.95 Read config.txt bytes        0 hnd 0x0
  4.99 [sdcard] pieeprom.upd not found
  5.01 usb_max_current_enable default 0 max-current 5000
  5.13 Read bcm2712-rpi-5-b.dtb bytes    78744 hnd 0x1088
  5.01 dt-match: compatible: raspberrypi,5-model-b match: brcm,bcm2712
  5.02 dt-match: compatible: brcm,bcm2712 match: brcm,bcm2712
  5.02 MESS:00:00:05.029887:0: *** Restart logging
  5.32 Read /config.txt bytes        0 hnd 0x0
  5.37 Read /config.txt bytes        0 hnd 0x0
  5.04 MESS:00:00:05.043586:0: Initial voltage 800000 temp 31235
  5.24 MESS:00:00:05.244180:0: avs_2712: AVS pred 8815 881500 temp 30136
  5.24 MESS:00:00:05.247781:0: vpred 881 mV +0
  5.25 MESS:00:00:05.256462:0: FB framebuffer_swap 1
  5.27 MESS:00:00:05.275844:0: Select resolution HDMI0/2 hotplug 0 max_mode 2
  5.27 MESS:00:00:05.279898:0: Select resolution HDMI1/2 hotplug 0 max_mode 2
  5.28 BMD "kernel_2712.img" not found
  5.90 fs_open: 'kernel_2712.img' 
  5.30 MESS:00:00:05.302956:0: dtb_file 'bcm2712-rpi-5-b.dtb'
  5.30 Loading 'bcm2712-rpi-5-b.dtb' to 0x00000000 offset 0x100
  5.16 Read bcm2712-rpi-5-b.dtb bytes    78744 hnd 0x1088
  5.38  /overlays/overlay_map.dtb 
  5.36 PCIEx1: PWR 0 DET_WAKE 0
  5.76 Read /config.txt bytes        0 hnd 0x0
  5.44 [sdcard] /cmdline.txt not found
  5.40  /cmdline.txt 
  5.44 MESS:00:00:05.442765:0: Failed to open command line file 'cmdline.txt'
  5.62 MESS:00:00:05.626856:0: RPM 204, max RPM 296
  5.68 BMD "armstub8-2712.bin" not found
  5.83 fs_open: 'armstub8-2712.bin' 
  5.68 Loading 'kernel8.img' to 0x00000000 offset 0x200000
  5.15 Read kernel8.img bytes   526992 hnd 0x108f
  5.71 MESS:00:00:05.717674:0: Kernel relocated to 0x80000
  5.72 MESS:00:00:05.722644:0: Device tree loaded to 0x2efec600 (size 0x1392c)
  5.72 PCI1 reset
  5.74 PCI2 reset
  5.75 set_reboot_order 0
  5.75 set_reboot_arg1 0
  5.75 USB-OTG disconnect
  5.79 MESS:00:00:05.794805:0: Starting OS 5794 ms
  5.80 MESS:00:00:05.800330:0: 00000040: -> 00000480
  5.80 MESS:00:00:05.802180:0: 00000030: -> 00100080
  5.80 MESS:00:00:05.806893:0: 00000034: -> 00100080
  5.81 MESS:00:00:05.811606:0: 00000038: -> 00100080
  5.81 MESS:00:00:05.816319:0: 0000003c: -> 00100080

NOTICE:  BL31: v2.6(release):v2.6-240-gfc45bc492
NOTICE:  BL31: Built : 12:55:13, Dec  4 2024
```


More information here:

https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#boot-sequence

https://www.raspberrypi.com/documentation/computers/config_txt.html
