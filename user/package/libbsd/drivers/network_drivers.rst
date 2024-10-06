.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 embedded brains GmbH & Co. KG
.. Copyright (C) 2024 Christian Mauderer

LibBSD Network Drivers
======================

Tips for Testing a driver
-------------------------

If you ported or wrote a driver and it does not work, try the following steps:

#. Connect the target to a separate network interface on a PC via a switch.
   Configure a fixed IP address on that interface. If possible: Disable checksum
   offload for the network interface (`ethtool` on Linux, driver settings on
   Windows). Otherwise, Wireshark can not detect checksum errors. Start
   Wireshark on that interface on the PC.
#. Start LibBSD `ftpd01` test on the target.
#. Configure a fixed IP address on the target using `ifconfig` on the RTEMS
   shell.
#. Ping the IP of your PC from the target and the target from the PC.
#. Check on the Wireshark if your PC receives packets from the target. If yes:
   Check if the PC responds to them.
   - If it responds, the target can send correctly formatted packets.
   - If your PC does not respond, check the packet content and checksums for
     errors like endianness, missing bytes, wrong bytes (can be a cache issue),
     wrong checksum (only works if checksum offloading has been disabled).
#. Check interface statistics. Some drivers offer statistics via `sysctl`. Some
   basic information can also be printed using `netstat` independent of the
   driver.
#. `ftpd01` also provides a `tcpdump` that you can use to dump received
   packets on the target. With that it is possible to check whether the target
   receives packets but can not send them.

Cache Issues
------------

If you have problems with cache (wrong data sent or received, old data sent or
received), check whether `CPU_DATA_CACHE_ALIGNMENT` is correctly defined for
your target. Otherwise the `bus_dma*` functions will not work correctly.
