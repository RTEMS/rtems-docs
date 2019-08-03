.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 Vijay Kumar Banerjee <vijaykumar9597@gmail.com>

Device Tree
===========
.. index:: Device Tree

A Device Tree is a data structure that is used to describe properties of
non-discoverable hardware instead of hardcoding them in the kernel. The device
tree data is generally stored in a `.dts` or a Device Tree Source (DTS) file.
This file is then compiled into a binary format called Device Tree Blob (DTB)
with `.dtb` extension. RTEMS preferably uses a DTB built from the FreeBSD source
tree matching the freebsd-org HEAD commit hash in libBSD.

Building the DTB
----------------

A single DTB file can be built using the `dtc` tool in libfdt using the
following command:

.. code-block:: none

    dtc -@ -I dts -O dtb -o my-devicetree.dtb my-devicetree.dts

For building the DTB from the FreeBSD source, the `make_dtb.sh` script
from `freebsd/sys/tools/fdt` must be used as most of the DTS files in FreeBSD
have included `.dtsi` files from their source tree. An example is given below as
a reference for how to build the device tree from the FreeBSD source.

`NOTE: The following example uses FreeBSD master branch from github mirror as
an example. It is advised to always use the source from the commit matching the
freebsd-org HEAD in libBSD.`

.. code-block:: shell
   :linenos:

     #We're using the script from freebsd/sys/tools/make_dtb.sh
     #Target device: Beaglebone Black.
     #Architecture: Arm.
     #DTS source name: am335x-boneblack.dts

     #The make_dtb.sh script uses environment variable MACHINE
     export MACHINE='arm'

     SCRIPT_DIR=$HOME/freebsd/sys/tools/fdt

     #The arguments to the script are
     # $1 -> Build Tree (This is the path to freebsd/sys/ directory)
     # $2 -> DTS source file
     # $3 -> output path of the DTB file

     ${SCRIPT_DIR}/make_dtb.sh ${SCRIPT_DIR}/../../ \
     ${SCRIPT_DIR}/../../gnu/dts/arm/am335x-boneblack.dts \
     $(pwd)

Using Device Tree Overlay
-------------------------

Device tree overlay is used either to add properties or devices to the existing
device tree. Adding any property to DTS using an overlay will override the
current values in the DTB. The Overlays enable us to modify the device tree
using a small maintainable plugin without having to edit the whole Base Tree.

There are two ways of applying an overlay on top of the built DTB.

#. Use fdtoverlay from libfdt

#. Add the overlay in the root partition of the SD card and apply it using U-Boot

The fdtoverlay command can be used as follows:

.. code-block:: none

    fdtoverlay -i my-base-tree.dtb -o output-tree.dtb my-overlay.dtbo

To apply it from U-Boot during system initialization we have to add the device
tree overlay file in the root directory of the SD card and use U-Boot commands
to apply the overlay.

Below is given the series of U-Boot commands that can be used to apply the
overlay, given that the overlay blob (.dtbo) file is already in the card.

.. code-block:: shell

    fatload mmc 0:1 0x80800000 rtems-app.img
    fatload mmc 0:1 0x88000000 my-base-tree.dtb
    fdt addr 0x88000000
    fatload mmc 0:1 0x88100000 my-overlay.dtbo
    fdt resize 0x1000
    fdt apply 0x88100000
    bootm 0x80800000-0x88000000
