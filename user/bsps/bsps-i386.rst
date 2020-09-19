.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 embedded brains GmbH

i386
****

pc386
=====

This BSP supports a standard Intel/AMD PC on i386 and up CPUs. If run
on a Pentium or above, the TSC register is used for timing calibration
purposes rather than relying entirely on the i8254.
Partial support is implemented for more modern PCs which do not have a
complete complement of legacy peripherals.

The BSP is able to utilize up to 3 GB of available RAM and up to 16
CPUs. Hyper-threading is supported, but may not be detected by the
BSP successfully.

.. note:: BSP capability to detect target hardware SMP details is
	  limited due to fact the SMP support is implemented based on
	  Intel Multi-Processor Specification (MPS). Final version of
	  the specification is version 1.4 which was released on July
	  1, 1995. On most newer machines the MPS functionality was
	  more or less supplanted by more modern ACPI (Advanced
	  Configuration and Power Interface). Still, on some machine
	  SMP support may be fragile at least at the platform
	  detection and initialization state depending on the target
	  BIOS/ACPI/MPS compatibility implementation.

There are several BSP variants provided which differ only in the target CPU
optimization. The most general is `pc386` which is tuned for i386. The `pc486`
variant is tuned for i486, `pc585` is tuned for Pentium, `pc586-sse` is tuned
for Pentium processor supporting SSE instructions. Finally `pc686` is tuned
for Pentium Pro processor, but generating only instructions for Pentium
and `pcp4` is tuned and generating instructions for Pentium4 processor
including SSE3 instructions.


Build Configuration Options
---------------------------

``BSP_PRESS_KEY_FOR_RESET``
  If defined to a non-zero value, then print a message and wait until
  any key is pressed before resetting board when application
  terminates (disabled by default).

``BSP_RESET_BOARD_AT_EXIT``
  If defined to a non-zero value, then reset the board when the
  application terminates (enabled by default).

``BSP_PRINT_EXCEPTION_CONTEXT``
  If defined to a non-zero value, then print the exception context
  when an unexpected exception occurs (enabled by default).

``BSP_VERBOSE_FATAL_EXTENSION``
  If defined to a non-zero value, then print more information in case
  of a fatal error (enabled by default).

``BSP_ENABLE_VGA``
  Enables VGA console driver (enabled by default).

``BSP_ENABLE_COM1_COM4``
  Enables support of COM1 thorough COM4 (enabled by default).

``USE_COM1_AS_CONSOLE``
  Enforces usage of COM1 as a console device (disabled by default).

``BSP_ENABLE_IDE``
  Enables legacy IDE driver (enabled by default).

``IDE_USE_PRIMARY_INTERFACE``
  Allows RTEMS to use storage drive(s) connected to the primary IDE
  interface. Disable if (i) the target hardware does not have primary
  IDE interface or (ii) it does not have any drive attached to the
  primary IDE interface or (iii) there is no need to use drive(s)
  attached to the primary IDE interface at all (enabled by default).

``IDE_USE_SECONDARY_INTERFACE``
  Allows RTEMS to use storage drive(s) connected to the secondary IDE
  interface. Enable if (i) the target hardware does have secondary IDE
  interface and (ii) there is at least one drive attached to the
  secondary IDE interface and (iii) there is a need to use drive(s)
  attached to the secondary IDE interface (disabled by default).

``BSP_VIDEO_80x50``
  Sets the VGA display to 80x50 character mode (disabled by default).

``CLOCK_DRIVER_USE_TSC``
  Enforces clock driver to use TSC register available on Pentium and
  higher class CPUs. If disabled and ``CLOCK_DRIVER_USE_8243`` is
  disabled too, then BSP will choose clock driver mechanism itself
  during the runtime (disabled by default).

``CLOCK_DRIVER_USE_8254``
  Enforces clock driver to use 8254 chip. If disabled and
  ``CLOCK_DRIVER_USE_TSC`` is disabled too, then BSP will choose clock
  driver mechanism itself during the runtime (disabled by default).

``NUM_APP_DRV_GDT_DESCRIPTORS``
  Defines how many descriptors in GDT may be allocated for the
  application or driver usage.

``USE_CIRRUS_GD5446``
  Enables usage of Cirrus GD5446 graphic card for RTEMS frame-buffer
  (disabled by default).

``USE_VGA``
  Enables usage of generic VGA graphic card for RTEMS frame-buffer
  (disabled by default).

``USE_VBE_RM``
  Enables usage of graphic card implementing VESA BIOS Extensions for
  RTEMS frame-buffer (enabled by default).

``BSP_GDB_STUB``
  Enables GDB support for debugging over serial port (enabled by
  default).

Runtime Options
---------------
The BSP supports several runtime options. They may be used by either setting
during boot by using target hardware bootloader or by using Qemu's
``-append`` command-line parameter in case BSP application is run
inside the Qemu emulator.

.. option:: --console=<dev>

	    specifies console
	    device. E.g. ``--console=/dev/com1``. COM device name may
	    also be followed by a baud rate like ``--console=/dev/com2,19200``

            .. note:: pc386 BSP family is using 9600 as a default baud rate
                      for console over UART (/dev/comX). It is also using
                      8 data bits, no parity and 1 stop bit.

.. option:: --printk=<dev>

	    specifies target device for printk/getk
	    calls. E.g. ``--printk=/dev/vgacons``

If the specified console device is not present then suitable fallback
device is selected based on the device order specified in `Console Drivers`.

.. option:: --video=<mode>

	    specifies required video mode. The options applies only to
	    the systems supporting VESA BIOS Extensions. Choices are
	    ``auto`` which selects graphic mode automatically or
	    ``none``/``off`` which disables initialization of the
	    graphic driver or direct specification of resolution
	    and/or color depth by
	    ``<resX>x<resY>[-<bpp>]``. E.g. ``--video=none`` disables
	    graphic driver. Using ``--video=1280x1024`` sets video
	    mode to 1280x1024 pixels mode while ``--video=800x600-32``
	    sets video mode to 800x600 pixels with 32bit color depth.

.. option:: --disable-com1-com4

	    disables usage of COM1 thorough COM4.

.. option:: --gdb=<dev>

            specifies UART device for communication between BSP's
            GDB stub and GDB running on a host system. Option accepts device
            and baud rate like the ``--console`` option above.
            E.g. ``--gdb=/dev/com2,115200`` instructs BSP to use COM2 device
            for GDB stub/host communication with the speed of 115200 bauds.

            .. note:: default GDB stub/host communication speed and other
                      communication properties are same like for console over
                      UART. E.g. 9600 baud rate, 8 data bits, no parity
                      and 1 stop bit.

.. option:: --gdb-break

            halts BSP execution at a break point in the BSP initialization code
            and waits for GDB connection.

.. option:: --gdb-remote-debug

            outputs the GDB remote protocol data to printk.

Testing with Qemu
-----------------

To test with Qemu, we need to:

- Build / install Qemu (most distributions should have it available on the
  package manager).

Booting RTEMS in Qemu
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

  $ qemu-system-i386 -m 128 -no-reboot -append \
  "--video=off --console=/dev/com1" -nographic -kernel ./hello.exe

This command boots ``hello.exe`` application located in current
directory and sets Qemu to provide 128MB RAM and to switch both Qemu's
and BSP's video off.

Booting RTEMS in KVM accelerated Qemu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When the Qemu host hardware and OS support KVM, it is possible to use it
to accelerate BSP run by using ``-machine type=q35,accel=kvm`` Qemu option.
Depending on the Qemu host configuration it may or may not require
administrator privileges to run the command.

.. code-block:: none

  $ sudo qemu-system-i386 -machine type=q35,accel=kvm -m 128 -no-reboot \
      -append "--video=off --console=/dev/com1" -nographic -kernel \
      ./dhrystone.exe

This command boots ``dhrystone.exe`` application and sets Qemu to use
KVM acceleration.


Running on a PC hardware
----------------------

There are several ways how to start RTEMS BSP application on the real
PC hardware.

Booting with GRUB boot-loader
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case the target machine does already have Linux with GRUB boot
loader installed, then the most easy way to load and boot RTEMS is
to use GRUB. This may be done in following steps:

(i) prepare RTEMS binary and save it either to Linux
    partition/directory accessible from GRUB or to an USB stick.

(ii) boot machine to GRUB menu.

.. note:: Some Linux installations hide GRUB menu by default and
	  quickly continues with booting default Linux option. If this
	  is the case, then during the boot hold down 'Shift' key to
	  un-hide the menu.

(iii) press ``c`` key to get into the GRUB's command-line mode.

(iv) use ``ls`` command to observe drives and partitions on them. If
     unsure, use 'ls' command with drive/partition description to show
     the target file system content. E.g. ``ls (hd1,msdos1)/`` will list
     files on the second drive, first partition which is formatted
     using fat/vfat file-system.

.. note:: Use `ls (hdX, partY)` without a slash at the end to show
	  information about the partition.

(v) use ``multiboot`` command to load the RTEMS application binary for
    boot. E.g. ``multiboot (hd1,msdos2)/rtems/ticker.exe`` will load
    ticker.exe from the second drive, second partition with fat/vfat
    file-system and its rtems directory.

(vi) use ``boot`` command to boot loaded binary.

.. note:: Advantage of using GRUB for booting RTEMS is the GRUB's
	  support for both classical BIOS and UEFI boot. This way
	  RTEMS may be booted even on UEFI only systems.

Booting with PXE/iPXE
^^^^^^^^^^^^^^^^
PXE booting is more complex than GRUB based booting and hence requires
more infrastructure configuration. The booting may be done in two
possible ways:

(i) using iPXE booted from an USB stick or a hard drive

It may be done using following steps:

- Download iPXE ISO image from http://boot.ipxe.org/ipxe.iso
- Either record it to CD/DVD or copy it to an USB stick
- boot from the medium above on the target hardware
- wait for ``Press Ctrl-B for the iPXE command line...`` prompt and once
  it appears press ``Ctrl-B`` key.
- use 'dhcp' command to configure network interface card
- use 'boot' command to boot RTEMS application from specified tftp
  server. E.g. ``boot tftp://10.0.0.5/hello.exe`` will boot hello.exe
  application from the tftp server on host with 10.0.0.5 IP address.

Whole interaction may look as:

.. code-block:: none

   Press Ctrl-B for the iPXE command line...
   iPXE> dhcp
   Configuring (net0 <mac address>)..... ok
   iPXE> boot tftp://10.0.0.5/hello.exe


(ii) using built in network card's PXE BIOS to boot into iPXE

This way is more complex and requires network infrastructure
configuration changes which description is out of the scope of this
documentation. Generic steps how to achieve this are:

- use target hardware BIOS/SETUP to enable PXE booting on the board
- setup network router to announce tftp server and file on it as a
  part of the router's BOOTP/DHCP protocol reply. You should use
  http://boot.ipxe.org/undionly.kpxe as a payload for non-UEFI based
  booting. Put that file into tftp server served/root directory.
- reboot target hardware and it should run network card PXE BIOS which
  should obtain IP address from the network router and load
  undionly.kpxe file from the tftp server. Once this is done, familiar
  iPXE UI appears. Follow steps described in previous paragraph to
  boot RTEMS application.

.. note:: It is not possible to use UEFI based PXE booting. Neither
	  directly by the network card PXE BIOS nor indirectly by
	  booting into iPXE. UEFI booting in both cases is not
	  currently supported.

Clock Drivers
-------------

The BSP supports two clock drivers. If there is no build option used
(see `Build Configuration Options`) for selecting particular clock
driver, then the decision which is used is done during the runtime.

- i8254 based driver. It is used on pre-Pentium CPUs by default.
- TSC register based driver. It is used on Pentium and later CPUs by
  default.

Console Drivers
---------------

The BSP console supports device drivers for a variety of devices
including VGA/keyboard and a number of serial ports. The default
console is selected based on which devices are present in the
following order of priority:

- VGA with PS/2 keyboard
- COM1 thorough COM4
- Any COM devices on the PCI bus including IO and memory mapped

PCI-based UART devices are named ``/dev/pcicom<number>`` as they are
probed and found. The numbers sequence starts with 1. E.g. first PCI
UART device found is accessible with ``/dev/pcicom1`` name.

Besides supporting generic devices above, the BSP also support
specific UART chips. The drivers for those are not initialized
automatically, but requires initialization from the application code:

- Exar 17d15x (NS16550 compatible multiport PCI UART)

Frame-Buffer Drivers
--------------------

The BSP supports several drivers implementing RTEMS frame-buffer
API. The default driver is for card(s) implementing VESA BIOS
Extensions. Others may be enabled by using appropriate build option
(see `Build Configuration Options`). Available drivers support:

- generic VGA graphic card
- Cirrus Logic GD5446
- generic graphic card supporting VESA BIOS Extensions

Network Interface Drivers
-------------------------

The network interface drivers are provided by the `libbsd`.

USB Host Drivers
----------------

The USB host drivers are provided by the `libbsd`.

RTC Drivers
-----------

There are several real time clock devices supported by drivers in the
BSP.

- Maxim DS1375
- Mostek M48T08/M48T18 (Maxim/Dallas Semiconductor DS1643 compatible)
- Motorola MC146818A
- Renesas ICM7170

I2C Drivers
-----------
There are several drivers for various I2C bus connected peripherals
supported by the BSP. Supported peripherals are:

- EEPROM
- Maxim DS1621 temperature sensor
- Semtech SC620 Octal LED Driver

SPI Drivers
-----------
There are several devices which connect to serial peripheral interfaces
supported by the BSP.

- M25P40 flash
- FM25L256 fram
- memory devices
- SD card

Legacy Drivers
--------------

The BSP source code provides legacy drivers for storage and network
devices.
The usage of legacy drivers is discouraged and description of such use
is out of the scope of this documentation. Interested users should
consult BSP source code directly but use legacy driver only when it is
not possible to use similar driver provided by `libbsd`.

Storage Drivers
^^^^^^^^^^^^^^^
- IDE/ATA
- AM26LV160/M29W160D flash

Network Drivers
^^^^^^^^^^^^^^^
- 3Com 3c509
- 3Com 3c90x (Etherlink XL family)
- Novell NE2000
- Western Digital WD8003
- Intel 82586
- Intel EtherExpress PRO/100
- Cirrus Logic CS8900
- DEC/Intel 21140
- SMC 91111
- Opencores Ethernet Controller
- National Semiconductor SONIC DP83932
