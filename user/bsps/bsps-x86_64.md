.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 Matheus Pecoraro <matpecor@gmail.com>
.. Copyright (C) 2018 Amaan Cheval <amaan.cheval@gmail.com>
.. Copyright (C) 2018 embedded brains GmbH & Co. KG

x86_64
******

amd64
=====

This BSP offers two variants: ``amd64`` and ``amd64efi``. The BSP can run on
UEFI-capable systems by using the FreeBSD bootloader in the case of ``amd64``
or a multiboot2 compliant bootloader in the case of ``amd64efi``. The main
difference of ``amd64efi`` is that it utilizes the UEFI Boot Services for its
functionality.

Currently the console driver, clock driver, and context switching are
functional. ACPI functionality is supported through ACPICA and used for SMP
(only supported in ``amd64``).

Build Configuration Options
---------------------------

There are no BSP configuration options available at build time.

Testing with QEMU
-----------------

To test with QEMU, we need to:

- Build / install QEMU (most distributions should have it available on the
  package manager).
- Build UEFI firmware that QEMU can use to simulate an x86-64 system capable of
  booting a UEFI-aware kernel, through the ``--bios`` flag.

.. _Building TianoCore's UEFI firmware, OVMF:

Building TianoCore's UEFI firmware, OVMF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Complete detailed instructions are available at `TianoCore's Github's wiki
<https://github.com/tianocore/tianocore.github.io/wiki/How-to-build-OVMF>`_.

Quick instructions (which may fall out of date) are:

.. code-block:: none

    $ git clone git://github.com/tianocore/edk2.git
    $ cd edk2
    $ make -C BaseTools
    $ . edksetup.sh

Then edit ``Conf/target.txt`` to set:

.. code-block:: ini

    ACTIVE_PLATFORM       = OvmfPkg/OvmfPkgX64.dsc
    TARGET                = DEBUG
    TARGET_ARCH           = X64
    # You can use GCC46 as well, if you'd prefer
    TOOL_CHAIN_TAG        = GCC5

Then run ``build`` in the ``edk2`` directory - the output should list the
location of the ``OVMF.fd`` file, which can be used with QEMU to boot into a UEFI
shell.

You can find the ``OVMF.fd`` file like this as well in the edk2 directory:

.. code-block:: none

    $ find . -name "*.fd"
    ./Build/OvmfX64/DEBUG_GCC5/FV/MEMFD.fd
    ./Build/OvmfX64/DEBUG_GCC5/FV/OVMF.fd # the file we're looking for
    ./Build/OvmfX64/DEBUG_GCC5/FV/OVMF_CODE.fd
    ./Build/OvmfX64/DEBUG_GCC5/FV/OVMF_VARS.fd

Booting RTEMS in QEMU
^^^^^^^^^^^^^^^^^^^^^

The ``amd64`` variant supports being booted through the FreeBSD bootloader
(:ref:`Booting via the FreeBSD bootloader`), meanwhile the ``amd64efi`` variant
supports being booted by a multiboot2 compliant bootloader, such as GRUB
(:ref:`Booting via GRUB`).

.. _Booting via the FreeBSD bootloader:

Booting via the FreeBSD bootloader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
  The following section describes how to boot RTEMS using a FreeBSD VM, for a
  more self contained alternative check out :ref:`Creating a FreeBSD Boot Image`

The RTEMS executable produced (an ELF file) needs to be placed in the FreeBSD's
``/boot/kernel/kernel``'s place.

To do that, we first need a hard-disk image with FreeBSD installed on
it. `Download FreeBSD's installer "memstick" image for amd64
<https://www.freebsd.org/where.html>`_ and then run the following commands,
replacing paths as appropriate.

.. code-block:: none

  $ qemu-img create freebsd.img 8G
  $ OVMF_LOCATION=/path/to/ovmf/OVMF.fd
  $ FREEBSD_MEMSTICK=/path/to/FreeBSD-11.2-amd64-memstick.img
  $ qemu-system-x86_64 -m 1024 -serial stdio --bios $OVMF_LOCATION \
      -drive format=raw,file=freebsd.img \
      -drive format=raw,file=$FREEBSD_MEMSTICK

The first time you do this, continue through and install FreeBSD. `FreeBSD's
installation guide may prove useful
<https://www.freebsd.org/doc/handbook/bsdinstall-start.html>`_ if required.

Once installed, build your RTEMS executable (an ELF file), for
eg. ``hello.exe``. We need to transfer this executable into ``freebsd.img``'s
filesystem, at either ``/boot/kernel/kernel`` or ``/boot/kernel.old/kernel`` (or
elsewhere, if you don't mind user FreeBSD's ``loader``'s prompt to boot your
custom kernel).

If your host system supports mounting UFS filesystems as read-write
(eg. FreeBSD), go ahead and:

1. Mount ``freebsd.img`` as read-write
2. Within the filesystem, back the existing FreeBSD kernel up (i.e. effectively
   ``cp -r /boot/kernel /boot/kernel.old``).
3. Place your RTEMS executable at ``/boot/kernel/kernel``

If your host doesn't support mounting UFS filesystems (eg. most Linux kernels),
do something to the effect of the following.

On the host

.. code-block:: none

   # Upload hello.exe anywhere accessible within the host
   $ curl --upload-file hello.exe https://transfer.sh/rtems

Then on the guest (FreeBSD), login with ``root`` and

.. code-block:: none

   # Back the FreeBSD kernel up
   $ cp -r /boot/kernel/ /boot/kernel.old
   # Bring networking online if it isn't already
   $ dhclient em0
   # You may need to add the --no-verify-peer depending on your server
   $ fetch https://host.com/path/to/rtems/hello.exe
   # Replace default kernel
   $ cp hello.exe /boot/kernel/kernel
   $ reboot

After rebooting, the RTEMS kernel should run after the UEFI firmware and
FreeBSD's bootloader. The ``-serial stdio`` QEMU flag will let the RTEMS console
send its output to the host's ``stdio`` stream.

.. _Booting via GRUB:

Booting via GRUB
~~~~~~~~~~~~~~~~

All that is required is for GRUB to be configured to boot the executable through
multiboot2. This section simply shows a possible way of achieving this.

We are going to create a single EFI System Partition (ESP) containing the
GRUB binary and our executable. First, create the proper file structure for the
ESP:

.. code-block:: none

  $ mkdir -p RTEMS-GRUB/EFI/BOOT

We are going to need a valid ``grub.cfg`` file. The following example will
configure GRUB to search for a file named "rtems" in the root of the partition
and boot it with multiboot2 instantly:

.. code-block:: none

  set timeout=0
  set default=0

  search --file --set=root /rtems

  menuentry 'RTEMS' {
      multiboot2 /rtems
      boot
  }

With this in place we can generate a GRUB binary containing the ``grub.cfg`` and
required modules on ``EFI/BOOT/BOOTX64.EFI`` (the default boot loader file for
UEFI systems):

.. code-block:: none

  $ grub-mkstandalone --format=x86_64-efi --fonts="" --locales="" --themes="" \
      --install-modules="normal search fat multiboot2"                        \
      boot/grub/grub.cfg=grub.cfg -o RTEMS-GRUB/EFI/BOOT/BOOTX64.EFI

And then copy the executable you desire to boot to ``/rtems`` (as specified by
our ``grub.cfg``) in our ESP:

.. code-block:: none

  $ cp ${rtems-executable} RTEMS-GRUB/rtems

With all this in place we will use the ``makefs`` tool (which is contained in
the x86_64 build set in the RTEMS Source Builder) to create a FAT32 image out of
the file structure:

.. code-block:: none

  $ makefs -t msdos -s 50m RTEMS-GRUB.img RTEMS-GRUB

And now all that is left is booting the image with QEMU:

.. code-block:: none

  $ qemu-system-x86_64 -m 512 -serial stdio --bios $OVMF_LOCATION \
      -drive format=raw,file=RTEMS-GRUB.img

.. note::
  The guide in this section uses the makefs tool to create the final FAT32 image
  out of the ESP file structure. Using makefs is not required as long as you can
  create a FAT32 image containing the same exact file structure.

Using the RTEMS tester
----------------------

Both ``amd64`` and ``amd64efi`` contain tester configuration files for using the
RTEMS tester tool, but they require user configuration.

The ``amd64`` requires the path to the FreeBSD boot image which will be used by
the tester tool (:ref:`Creating a FreeBSD Boot Image`). Meanwhile both ``amd64``
and ``amd64efi`` require the path to OVMF
(:ref:`Building TianoCore's UEFI firmware, OVMF`).

An example of the user configuration file:

.. code-block:: none

  [amd64_qemu]
  amd64_ovmf_path = {OVMF_PATH}
  amd64_freebsd_boot_image_path = {FREEBSD_BOOT_IMAGE_PATH}

  [amd64efi_grub_qemu]
  amd64_ovmf_path = {OVMF_PATH}

.. _Creating a FreeBSD Boot Image:

Creating a FreeBSD Boot Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  You can instead choose to download a working boot image `here
  <https://ftp.rtems.org/pub/rtems/archive/misc/FreeBSD/boot/2024-10-01/>`_.
  For directly using the boot image with QEMU go to
  :ref:`Booting in QEMU Using the Boot Image`

To acquire or build the FreeBSD bootloader a FreeBSD machine or VM is required.
You can either copy the files already present under ``/boot`` or build them
yourself.

To build the bootloader yourself, assuming the FreeBSD source tree is under
``/usr/src``, head over to ``/usr/src/stand`` and run the following commands:

.. code-block:: none

  $ make
  $ make install DESTDIR={bootloader-path}

.. note::
  The directories ``usr/share/man/man3``, ``usr/share/man/man5``, and
  ``usr/share/man/man8`` must be created under ``{bootloader-path}`` before
  running ``make install``

Next create the EFI disk image with the FreeBSD bootloader under
``EFI/BOOT/BOOTX64.EFI`` (the default boot loader file for UEFI systems):

.. code-block:: none

  $ mkdir -p efi-image/EFI/BOOT/
  $ cp {bootloader-path}/loader.efi efi-image/EFI/BOOT/BOOTX64.EFI
  $ makefs -t msdos -s 1m EFI.img efi-image

And then the FreeBSD Root FS disk image:

.. code-block:: none

  $ mkdir -p rootfs-image/boot/
  $ cp -r {bootloader-path}/defaults rootfs-image/boot/
  $ cp -r {bootloader-path}/lua rootfs-image/boot/

The following configuration file will instruct the FreeBSD loader to instantly
load the file ``/rtems`` contained in the second disk. It should be created
under ``rootfs-image/boot/loader.conf``

.. code-block:: none

  beastie_disable="YES"
  kernel="/rtems"
  currdev="disk1"
  autoboot_delay="0"

And then we can convert ``rootfs-image`` to an UFS disk image and use the
``mkimg`` tool to create a singular image with both partitions:

.. code-block:: none

  makefs -t ffs -o version=2 ROOTFS.img rootfs-image
  mkimg -s gpt -p efi:=EFI.img -p freebsd-ufs:=ROOTFS.img -o FreeBSDBoot.img

.. _Booting in QEMU Using the Boot Image:

Booting in QEMU Using the Boot Image:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the boot image to run any rtems executable with QEMU as such:

.. code-block:: none

  $ mkdir rtems-image
  $ cp {rtems-executable} rtems-image/rtems
  $ makefs -t ffs -o version=2 rtems.img rtems-image
  $ qemu-system-x86_64 -m 1024 -serial stdio --bios {OVMF_LOCATION} \
      -drive format=raw,file=FreeBSDBoot.img \
      -drive format=raw,file=rtems.img

Paging
------

During the BSP's initialization, the paging tables are setup to identity-map the
first 512GiB, i.e. virtual addresses are the same as physical addresses for the
first 512GiB.

The page structures are set up statically with 1GiB super-pages.

.. note::
  Page-faults are not handled.

.. warning::
  RAM size is not detected dynamically and defaults to 1GiB, if the
  configuration-time ``RamSize`` parameter is not used.

Interrupt Setup
---------------

Interrupt vectors ``0`` through ``32`` (i.e. 33 interrupt vectors in total) are
setup as "RTEMS interrupts", which can be hooked through
``rtems_interrupt_handler_install``.

The Interrupt Descriptor Table supports a total of 256 possible vectors (0
through 255), which leaves a lot of room for "raw interrupts", which can be
hooked through ``_CPU_ISR_install_raw_handler``.

Since the APIC needs to be used for the clock driver, the PIC is remapped (IRQ0
of the PIC is redirected to vector 32, and so on), and then all interrupts are
masked to disable the PIC. In this state, the PIC may _still_ produce spurious
interrupts (IRQ7 and IRQ15, redirected to vector 39 and vector 47 respectively).

The clock driver triggers the initialization of the APIC and then the APIC
timer.

The I/O APIC is not supported at the moment.

.. note::
  IRQ32 is reserved by default for the APIC timer (see following section).

  IRQ33 is reserved by default for interprocessor interrupts if SMP is enabled.

  IRQ255 is reserved by default for the APIC's spurious vector.

.. warning::
  Besides the first 33 vectors (0 through 32), and vector 255 (the APIC spurious
  vector), no other handlers are attached by default.

Clock Driver
------------

amd64
^^^^^

The clock driver currently uses the APIC timer. Since the APIC timer runs at the
CPU bus frequency, which can't be detected easily, the PIT is used to calibrate
the APIC timer, and then the APIC timer is enabled in periodic mode, with the
initial counter setup such that interrupts fire at the same frequency as the
clock tick frequency, as requested by ``CONFIGURE_MICROSECONDS_PER_TICK``.

amd64efi
^^^^^^^^

The clock driver uses the **SetTimer** UEFI boot service.

Console Driver
--------------

amd64
^^^^^

The console driver defaults to using the ``COM1`` UART port (at I/O port
``0x3F8``), using the ``NS16550`` polled driver.

amd64efi
^^^^^^^^

The console driver uses the UEFI Simple Text Output Protocol
