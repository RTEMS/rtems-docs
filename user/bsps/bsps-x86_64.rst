.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 Amaan Cheval <amaan.cheval@gmail.com>
.. Copyright (C) 2018 embedded brains GmbH

x86_64
******

amd64
=====

This BSP offers only one variant, ``amd64``. The BSP can run on UEFI-capable
systems by using FreeBSD's bootloader, which then loads the RTEMS executable (an
ELF image).

Currently only the console driver and context initialization and switching are
functional (to a bare minimum), but this is enough to run the ``hello.exe`` sample
in the RTEMS testsuite.

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

Boot RTEMS via FreeBSD's bootloader
-----------------------------------

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

  IRQ255 is reserved by default for the APIC's spurious vector.

.. warning::
  Besides the first 33 vectors (0 through 32), and vector 255 (the APIC spurious
  vector), no other handlers are attached by default.

Clock Driver
------------

The clock driver currently uses the APIC timer. Since the APIC timer runs at the
CPU bus frequency, which can't be detected easily, the PIT is used to calibrate
the APIC timer, and then the APIC timer is enabled in periodic mode, with the
initial counter setup such that interrupts fire at the same frequency as the
clock tick frequency, as requested by ``CONFIGURE_MICROSECONDS_PER_TICK``.

Console Driver
--------------

The console driver defaults to using the ``COM1`` UART port (at I/O port
``0x3F8``), using the ``NS16550`` polled driver.
