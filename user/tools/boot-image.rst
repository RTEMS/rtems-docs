.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 Chris Johns <chrisj@rtems.org>

.. _RTEMSExecutableInfomation:

RTEMS Boot Image
================

.. index:: Tools, rtems-boot-image

The RTEMS Boot Image (:program:`rtems-boot-image`) command is an RTEMS
tool to create disk images suitable for SD cards to boot RTEMS on a
range of boards. The supported hosts are:

- FreeBSD

- Linux

- MacOS

The tool captures the specific details for a host operating system to
create a bootable disk image as well as capturing the specific detail
of the boards that are supported. The tool brings these detail
together under a sigle command line interface that is portable across
the supported hosts.

The boot image tool can:

- Create a disk image to boot an RTEMS executable

- Create a disk image to network boot an RTEMS executable

- Convert an RTEMS executable into the format a board's bootloader
  can load.

The disk images are suitable for booting a range of hardware that have
media interfaces, such as an SD card. The default partition type is
the Master Boot Record (MRB) and a single root DOS-FS partition is
created.

Boot Loaders
------------

The boot image tool supports the following boot loaders:

- U-boot

U-Boot
~~~~~~

The U-Boot boards supported are:

- BeagleBone (`arm-ti-am335x_evm`)

- Zedboard (`arm-xilinx-zynq-common`)

These boards can be booted with executable and Flat Device Tree (FDT)
blobs on disk or view a network if supported by the boards.

The boot image tool can create the following boot configurations for
U-Boot:

- **Executable**

  A kernel executable is copied in the disk image, loaded by U-Boot
  and control is passed to the kernel. A reset is performed if the
  load fails or the kernel returns control to U-Boot.

- **Executable and FDT**

  A kernel executable and FDT blob are copied to the disk image,
  loaded by U-boot and control is passed to the kernel. A reset is
  performed if the load fails or the kernel returns control to U-Boot.

- **Network DHCP and Executable**

  The board's network interface is initialised, a DHCP request made
  and a kernel image loaded using TFTP. The loaded kernel is passed
  control. A reset is performed if the load fails or the kernel
  returns control to U-Boot.

- **Network DHCP, Executable and FDT**

  The board's network interface is initialised, a DHCP request made
  and a kernel image loaded using TFTP. The loaded kernel is passed
  control. A reset is performed if the load fails or the kernel
  returns control to U-Boot.

  The FDT can be installed in and disk image and loaded from it on
  each boot.

- **Network Static IP and Executable**

  The board's network interface is initialised with a static IP
  address and a kernel image loaded using TFTP. The loaded kernel is
  passed control. A reset is performed if the load fails or the kernel
  returns control to U-Boot.

- **Network Static IP, Executable and FDT**

  The board's network interface is initialised with a static IP
  address and a kernel image loaded using TFTP. The loaded kernel is
  passed control. A reset is performed if the load fails or the kernel
  returns control to U-Boot.

  The FDT can be installed in and disk image and loaded from it on
  each boot.

Hosts
-----

The hosts each require specific set up to run the boot image
buildier. The tool creates special devices to access the image as a
disk and runs file system partitioning and formatting tools. These
tools typically require super user or root access. It is not good
practice to run commands like this one as root and so the tool
dispatches any specific command that needs higher privileges via
``sudo``. If you see a password prompt please enter your password, not
a root password if you have one confgiured.

FreeBSD
~~~~~~~

Install the ``sudo`` package. All commands used are in standard
operating system paths and should not require any specific
configurations.

Linux
~~~~~

The loop back kernel module needs to be loaded.

MacOS
~~~~~

All command used are part of the base OS. No external packages are
required.

Configuration
-------------

The boot image tool is configured by the file :file:`rtems-boot.ini`
that is installed in the

Command
-------

The :program:`rtems-boot-image` tool creates a boot disk image for a
specified board. The command line options are:

:program:`rtems-boot-image`

.. option:: -h, --help

   Display the command line help.

.. option:: -l, --log

   Set the log file name. The default is
   :file:`rtems-log-boot-image.txt`.

.. option:: -v, --trace

   Enable trace or debug logging.

.. option:: -s IMAGE_SIZE, --image-size IMAGE_SIZE

   Set the image size. The size can be in SI units of ``k``, ``m``, or
   ``g``. The size needs to be something the host's parition and
   format tools will accept and it must be large enough to fit the
   root partition plus any alignments. The default is ``64m``.

.. option:: -F FS_FORMAT, --fs-format FS_FORMAT

   Specify type type of format. The supported formats are ``fat16``
   and ``fat32``. The default format is ``fat16``.

.. option:: -S FS_SIZE, --fs-size FS_SIZE

   Set the size of the first partition in the disk image. The
   partition need to be less than the size of the image plus the
   alignment. The default size is ``auto`` which will fill the image
   with the partition.

.. option:: -A FS_ALIGN, --fs-align FS_ALIGN

   Set the alignment of the first partition. The default is ``1m``.

.. option:: -k KERNEL, --kernel KERNEL

   Optionally provide a kernel image that is copied into the root
   partition of the disk image and loaded and run when the board
   boots. The file is an RTEMS executable in the ELF format which is
   converted to a format the boot loader can load.

.. option:: -d FDT, --fdt FDT

   Optionally provide a FDT blob that is copied into the root
   partition of the disk image and loaded when the board boots. If a
   kernel is provided or a kernel is loaded via a net boot a kernel
   boot with FDT is executabled. The file is an FDT blob created by
   the FDT compiler.

.. option:: -f FILE, --file FILE

   Optionally provide a file to be copied to the root partition of the
   disk image. This option can be provided more than once if more than
   one file needs to be installed.

.. option:: --net-boot

   Not used and will be removed.

.. option:: --net-boot-dhcp

   Configure a network boot using DHCP. The kernel will be loaded
   using TFTP and the file request can be specific by the
   ``--net-boot-file`` option.

.. option:: --net-boot-ip NET_BOOT_IP

   Configure a network boot using a static IP address. The kernel will
   be loaded using TFTP and the file request can be specific by the
   ``--net-boot-file`` option. A server IP needs to be specified using
   the ``--net-boot-server``.

.. option:: --net-boot-file NET_BOOT_FILE

   Specify the kernel image file name requested using the TFTP
   protocol. The default is :file:`rtems.img`.

.. option:: --net-boot-fdt NET_BOOT_FDT

   Optionally specify the file name of a FDT blob loaded using the
   TFTP protocol. If a net boot FDT file is provide the kernel will be
   executable with a suitable kernel and FDT boot command.

.. option:: -U CUSTOM_UENV, --custom-uenv CUSTOM_UENV

   Optionally provide a custom U-boot :file:`uEnv.txt` file that is
   copied to into the root directory of the root partition of the disk
   image.

.. option:: -b BOARD, --board BOARD

   Specify the board the disk image is built for. The default board is
   ``list`` which lists the available board configurations.

.. option:: --convert-kernel

   Convert an RTEMS ELF executable into an image file the selected
   board's bootloader can load. This option does not create a disk
   image. The option can be used to create images that can be loaded
   when network booting.

.. option:: --no-clean

   If provided the :file:`build` directory will not be removed after
   the disk image has been created.

.. option:: -o OUTPUT, --output OUTPUT

   The output file name for the image. If the ``--convert-kernel``
   option is used the conversion is written as this file name and if
   it is not provided the output file is the built disk image.

.. option:: paths [paths ...]

   The required paths depend on the mix of other options.

   If the ``--convert-kernel`` option is provided a single path to an
   RTEMS executable file is required. If this option is not provided
   the number of paths provided determine how they are processed.

   If a single path a built U-boot directory is provided the board
   configuration will automatically find and pick up the first and
   second stage boot loader executables.

   If two paths are provided they are paths to the first and second
   stage boot loader executables. This can be used with loader images
   they you have not built.

Examples
--------

The examples show the output for FreeBSD. It may vary depending on
your type of host, how it is configured and what is running.

If the board option is not provided a list of boards is displayed:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img u-boot
  RTEMS Tools - Boot Image, 5.0.not_released
   Board list: bootloaders (1)
    u-boot: 2
     u-boot-beaglebone
     u-boot-zedboard

Create a disk image from a built U-Boot sandbox:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone u-boot
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 64m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Finished
  Cleaning up

Create a 32M byte SD card image with the testsuite's hello world
executable (``hello.exe``):

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone -s 32m -k hello.exe u-boot
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 32m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Install: hello.exe.img
  Uenv template: uenv_exe
  Install: uEnv.txt
  Finished
  Cleaning up

Build the same image using the first and second stage boot loaders:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone -s 32m -k hello.exe MLO u-boot.img
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 32m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Install: hello.exe.img
  Uenv template: uenv_exe
  Install: uEnv.txt
  Finished
  Cleaning up

Install and load the TI standard FDT for the Beaglebone Black board
with the LibBSD DHCP 01 test application:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone -s 32m \
    -k dhcpcd01.exe -d am335x-boneblack.dtb MLO u-boot.img
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 32m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Install: dhcpcd01.exe.img
  Install: am335x-boneblack.dtb
  Uenv template: uenv_exe_fdt
  Install: uEnv.txt
  Finished
  Cleaning up

Create a DHCP network boot image where the TFTP client requests ``rtems.img``:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone -s 32m \
    --net-boot-dhcp MLO u-boot.img
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 32m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Uenv template: uenv_net_dhcp
  Install: uEnv.txt
  Finished
  Cleaning up

Select a specific kernel image to load using TFTP and load a FDT blob
from the SD card:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone -s 32m \
    --net-boot-dhcp --net-boot-file bbb1a.img \
    -d am335x-boneblack.dtb MLO u-boot.img
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 32m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Install: am335x-boneblack.dtb
  Uenv template: uenv_net_dhcp
  Install: uEnv.txt
  Finished
  Cleaning up

Create an image where a specific kernel image and FDT blob is loaded
using the TFTP protocol:

.. code-block:: none

  $ rtems-boot-image -o sd-card.img -b u-boot-beaglebone -s 32m \
    --net-boot-dhcp --net-boot-file bbb1a.img \
    --net-boot-fdt bbb/am335x-boneblack.dtb MLO u-boot.img
  RTEMS Tools - Boot Image, 5.0.not_released
  Create image: sd-card.img size 32m
  Attach image to device: sd-card.img
  Password:
  Partition device: md0 as MBR
  Format: /dev/md0s1 as fat16
  Mount: /dev/md0s1
  Install: MLO
  Install: u-boot.img
  Uenv template: uenv_net_dhcp_net_fdt
  Install: uEnv.txt
  Finished
  Cleaning up
