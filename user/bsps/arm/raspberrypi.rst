.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 G S Niteesh <gsnb.gn@gmail.com>

raspberrypi
===========

The 'raspberrypi' BSP supports the single core models (Zero,  Zero W, A+, B+),
and the 'raspberrypi2' BSP supports the Raspberry Pi 2, Raspberry Pi 3 A+, and
Raspberry Pi 3. The Raspberry Pi 4 is supported by the AArch64 Raspberry Pi BSP.
The default bootloader on the Raspberry Pi which is used to boot Raspbian or
other OS can be also used to boot RTEMS. U-boot can also be used.

Setup SD card
-------------

The Raspberry Pis have an unconventional booting mechanism. The GPU
boots first, initializes itself, runs the bootloader and starts the CPU.
The bootloader looks for a kernel image, by default the kernel images must
have a name of the form ``kernel*.img`` but this can be changed by adding
`kernel=<img_name>` to ``config.txt``.

You must provide the required firmware files on the SD card for the GPU to
proceed, and thereby to boot RTEMS.  The BSP currently boots up with an older
version of the official firmware. These files can be downloaded from `the
Raspberry Pi Firmware Repository
<https://github.com/raspberrypi/firmware/tree/1.20200601/boot>`_.  You can
remove the ``kernel*.img`` files if you want to, but don't touch the other
files.

Copy these files in to a SD card with FAT filesystem.

Kernel image
------------

The following steps show how to run ``hello.exe`` on a Raspberry Pi 2.
The same instructions can be applied to Raspberry Pi 1 also.
Other executables can be processed in a similar way.

To create the kernel image:

.. code-block:: none

     $ arm-rtems@rtems-ver-major@-objcopy -Obinary hello.exe kernel.img

Copy the kernel image to the SD card.

Make sure you have these lines below, in your ``config.txt``.

.. code-block:: none

     dtoverlay=disable-bt
     kernel_address=0x200000
     kernel=kernel.img

SPI Driver
----------

SPI drivers are registered by the ``rpi_spi_init(bool bidirectional_mode)``
function.

.. code-block:: none

     #include <assert.h>
     #include <bsp.h>

     void spi_init(void)
     {
       int rv;

       rv = rpi_spi_init(false);
       assert(rv == 0);
     }

I2C Driver
----------

I2C drivers are registered by the ``rpi_setup_i2c_bus()`` function.

.. code-block:: none

     #include <assert.h>
     #include <bsp.h>

     void i2c_init(void)
     {
       int rv;

       rv = rpi_setup_i2c_bus();
       assert(rv == 0);
     }

Testing using QEMU
------------------

QEMU can be built using RSB. Navigate to ``<SOURCE_BUILDER_DIR>/rtems``
and run this command.

.. code-block:: none

     $ ../source-builder/sb-set-builder --prefix=<TOOLCHAIN_DIR> devel/qemu

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

     $ arm-rtems@rtems-ver-major@-gdb hello.exe

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
