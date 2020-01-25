.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 TBD

raspberrypi
===========

This BSP supports `Raspberry Pi 1` and `Raspberry Pi 2` currently.
The support for `Raspberry Pi 3` is work under progress.
The default bootloader on the Raspberry Pi which is used to boot Raspbian
or other OS can be also used to boot RTEMS. U-boot can also be used.

Setup SD card
----------------

The Raspberry Pis have an unconventional booting mechanism. The GPU
boots first, initializes itself, runs the bootloader and starts the CPU.
The bootloader looks for a kernel image, by default the kernel images must
have a name of the form ``kernel*.img`` but this can be changed by adding
`kernel=<img_name>` to ``config.txt``.

You must provide the required files for the GPU to proceed. These files
can be downloaded from
`the Raspberry Pi Firmware Repository <https://github.com/raspberrypi/firmware/tree/master/boot>`_.
You can remove the ``kernel*.img`` files if you want too, but don't touch
the other files.

Copy these files in to a SD card with FAT filesystem.

Kernel image
------------

The following steps show how to run ``hello.exe`` on a Raspberry Pi 2.
The same instructions can be applied to Raspberry Pi 1 also.
Other executables can be processed in a similar way.

To create the kernel image:

.. code-block:: none

     $ arm-rtems5-objcopy -Obinary hello.exe kernel.img

Copy the kernel image to the SD card.

Make sure you have these lines below, in your ``config.txt``.

.. code-block:: none

     enable-uart=1
     kernel_address=0x200000
     kernel=kernel.img

Testing using QEMU
------------------

QEMU can be built using RSB. Navigate to ``<SOURCE_BUILDER_DIR>/rtems``
and run this command.

.. code-block:: none

     $ ../source-builder/sb-set-builder --prefix=<TOOLCHAIN_DIR> devel/qemu4.bset

**Note**: Replace ``<SOURCE_BUILDER_DIR>`` and ``<TOOLCHAIN_DIR>`` with the
correct path of the directories. For example, if you used quick-start section
as your reference, these two will be ``$HOME/quick-start/src/rsb`` and
``$HOME/quick-start/rtems/5`` respectively,

QEMU along with GDB can be used for debugging, but it only supports
Raspberry Pi 2 and the emulation is also incomplete. So some of the
features might not work as expected.

Make sure your version of QEMU is newer than v2.6, because older ones don't
support Raspberry Pis.

.. code-block:: none

     $ qemu-system-arm -M raspi2 -m 1G -kernel hello.exe -serial mon:stdio -nographic -S -s

This starts QEMU and creates a socket at port ``localhost:1234`` for GDB to
connect.

The Device Tree Blob (DTB) is needed to load the device tree while starting up
the kernel. The BSP uses information from this file to initialize the drivers.

Make sure you pass in the correct DTB file. There are currently two version of
DTB for the Raspberry Pi 2 ``bcm2709-rpi-2-b.dtb`` and ``bcm2710-rpi-2-b.dtb``.
The ``bcm2709-rpi-2-b.dtb`` is for Raspberry Pi 2 Model B and
``bcm2710-rpi-2-b.dtb`` is for Raspberry Pi 2 Model B v1.2

We need to pass in the DTB file to GDB before running the example.

In a new terminal, run GDB using

.. code-block:: none

     $ arm-rtems5-gdb hello.exe

This will open GDB and will load the symbol table from hello.exe. Issue the
following commands in the GDB prompt.

.. code-block:: none

     (gdb) tar remote:1234
     (gdb) load
     (gdb) restore bcm2709-rpi-2-b.dtb binary 0x2ef00000
     (gdb) set $r2 = 0x2ef00000

This will connect GDB to QEMU and will load the DTB file and the application.

.. code-block:: none

     (gdb) continue

The ``continue`` command will run the executable.

**Note**: Add ``set scheduler-locking on`` in GDB if you have any issues
running the examples.
