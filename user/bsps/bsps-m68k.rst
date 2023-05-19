.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 embedded brains GmbH & Co. KG

m68k (Motorola 68000 / ColdFire)
********************************

av5282
======

TODO.

csb360
======

TODO.

gen68340
========

TODO.

gen68360
========

TODO.

genmcf548x
==========

TODO.

mcf5206elite
============

TODO.

mcf52235
========

TODO.

mcf5225x
========

TODO.

mcf5235
=======

TODO.

mcf5329
=======

Overview
--------

This BSP is heavily based on the MCF5235 BSP. The MCF5329EVB is a Motorola
evaluation board (Zoom) with a LogicPD MCF5329-10 SODIMM-144 card. The
development kit features the MCF5329 based Fire Engine, as well as a plug-in
system-on-module containing 32 MB of DDR-SDRAM. The board also includes 2 MB of
boot flash, 16 MB of NAND flash, a core frequency of 240MHz, an onboard 800x600
LCD controller, FEC, USB, uarts, CAN bus, QSPI, I2C, and 10/100 Ethernet.

You can find the link to MCF5329 Reference Manual below:

* `MCF5329 Reference Manual <https://www.nxp.com/docs/en/reference-manual/MCF5329RM.pdf>`_

mrm332
======

TODO.

mvme147
=======

TODO.

mvme147s
========

TODO.

mvme162
=======

Overview
--------

The MVME162 family provides OEMs and solution developers an ideal platform for
embedded monitoring and control apllications it allows an OEM to minimize
engineering expenses while integrating value-added hardware and software
applications onto an off-the-shelf product. In order to provide the wide range
of solutions, the MVME162 allows a variety of MPU, memory, and interface
options such as floating-point, Ethernet, SCSI, and VME. The result is a
variation of the MVME162 which most closely fits the application requirement.

There are a large number of model variations on this board. This was the first
user submitted BSP and continues to be a fairly popular simply because at one
point it was the highest selling VMEBus board of all time.

Board Setup
-----------

We will setup the RTEMS Lab Board initally to proceed further for the setup
of TFTP transfer.

The env settings are:

.. code-block:: none

    MPU Clock Speed =25Mhz
    162-Bug>env
    Bug or System environment [B/S] = B?
    Field Service Menu Enable [Y/N] = N?
	Remote Start Method Switch [G/M/B/N] = B?
	Probe System for Supported I/O Controllers [Y/N] = Y?
	Negate VMEbus SYSFAIL* Always [Y/N] = N?
	Local SCSI Bus Reset on Debugger Startup [Y/N] = N?
	Local SCSI Bus Negotiations Type [A/S/N]       = A?
	Industry Pack Reset on Debugger Startup [Y/N]  = Y?
	Ignore CFGA Block on a Hard Disk Boot [Y/N]    = Y?
	Auto Boot Enable [Y/N]   = N?
	Auto Boot at power-up only [Y/N] = Y?
	Auto Boot Controller LUN = 00?
	Auto Boot Device LUN     = 00?
	Auto Boot Abort Delay    = 15?
	Auto Boot Default String [NULL for a empty string] = ?
	ROM Boot Enable [Y/N]            = N?
	ROM Boot at power-up only [Y/N]  = Y?
	ROM Boot Enable search of VMEbus [Y/N] = N?
	ROM Boot Abort Delay             = 0?
	ROM Boot Direct Starting Address = FF800000?
	ROM Boot Direct Ending Address   = FFDFFFFC?
	Network Auto Boot Enable [Y/N]   = N?
	Network Auto Boot at power-up only [Y/N] = Y?
	Network Auto Boot Controller LUN = 00?
	Network Auto Boot Device LUN     = 00?
	Network Auto Boot Abort Delay    = 5?
	Network Auto Boot Configuration Parameters Pointer (NVRAM) = FFE0FF00?
	Memory Search Starting Address   = 00000000?
	Memory Search Ending Address     = 01000000?
	Memory Search Increment Size     = 00010000?
	Memory Search Delay Enable [Y/N] = N?
	Memory Search Delay Address      = FFFFD20F?
	Memory Size Enable [Y/N]         = Y?
	Memory Size Starting Address     = 00000000?
	Memory Size Ending Address       = 01000000?
	Base Address of Dynamic Memory   = 00000000?
	Size of Parity Memory            = 00000000?
	Size of ECC Memory Board #0      = 01000000?
	Size of ECC Memory Board #1      = 00000000?
	Base Address of Static Memory    = FFE00000?
	Size of Static Memory            = 00020000?
	Slave Enable #1 [Y/N] = Y?
	Slave Starting Address #1 = 00000000?
	Slave Ending Address #1   = 00FFFFFF?
	Slave Address Translation Address #1 = 00000000?
	Slave Address Translation Select #1  = 00000000?
	Slave Control #1 = 03FF?
	Slave Enable #2 [Y/N] = N?
	Slave Starting Address #2 = 00000000?
	Slave Ending Address #2   = 00000000?
	Slave Address Translation Address #2 = 00000000?
	Slave Address Translation Select #2  = 00000000?
	Slave Control #2 = 0000?
	Master Enable #1 [Y/N] = Y?
	Master Starting Address #1 = 01000000?
	Master Ending Address #1   = EFFFFFFF?
	Master Control #1 = 0D?
	Master Enable #2 [Y/N] = N?
	Master Starting Address #2 = 00000000?
	Master Ending Address #2   = 00000000?
	Master Control #2 = 00?
	Master Enable #3 [Y/N] = N?
	Master Starting Address #3 = 00000000?
	Master Ending Address #3   = 00000000?
	Master Control #3 = 00?
	Master Enable #4 [Y/N] = N?
	Master Starting Address #4 = 00000000?
	Master Ending Address #4   = 00000000?
	Master Address Translation Address #4 = 00000000?
	Master Address Translation Select #4  = 00000000?
	Master Control #4 = 00?
	Short I/O (VMEbus A16) Enable [Y/N] = Y?
	Short I/O (VMEbus A16) Control      = 01?
	F-Page (VMEbus A24) Enable [Y/N]    = Y?
	F-Page (VMEbus A24) Control         = 02?
	ROM Access Time Code          = 03?
	FLASH Access Time Code        = 02?
	MCC Vector Base               = 05?
	VMEC2 Vector Base #1          = 06?
	VMEC2 Vector Base #2          = 07?
	VMEC2 GCSR Group Base Address = D2?
	VMEC2 GCSR Board Base Address = 00?
	VMEbus Global Time Out Code   = 01?
	Local Bus Time Out Code       = 02?
	VMEbus Access Time Out Code   = 02?
	IP A Base Address              = 00000000?
	IP B Base Address              = 00000000?
	IP C Base Address              = 00000000?
	IP D Base Address              = 00000000?
	IP D/C/B/A Memory Size         = 00000000?
	IP D/C/B/A General Control     = 00000000?
	IP D/C/B/A Interrupt 0 Control = 00000000?
	IP D/C/B/A Interrupt 1 Control = 00000000?

To setup the Server/Client IP Addresses for the TFTP Transfer, we will use the
NIOT command. NIOT (Network I/O Teach) is a 162-Bug's debugger command commonly
used to setup the Server/Client IP Addresses for the TFTP Transfer.

The NIOT command goes something like this:

.. code-block:: none

    162-Bug>niot
	Controller LUN =00?
	Device LUN     =00?
	Node Control Memory Address =FFE10000?
	Client IP Address      =192.168.1.245?
	Server IP Address      =192.168.1.92?
	Subnet IP Address Mask =255.255.255.0?
	Broadcast IP Address   =192.168.1.255?
	Gateway IP Address     =0.0.0.0?
	Boot File Name ("NULL" for None)     =/mvme162.img?
	Argument File Name ("NULL" for None) =?
	Boot File Load Address         =00020000?
	Boot File Execution Address    =00020000?
	Boot File Execution Delay      =00000000?
	Boot File Length               =00000000?
	Boot File Byte Offset          =00000000?
	BOOTP/RARP Request Retry       =00?
	TFTP/ARP Request Retry         =00?
	Trace Character Buffer Address =00000000?
	BOOTP/RARP Request Control: Always/When-Needed (A/W)=A?
	BOOTP/RARP Reply Update Control: Yes/No (Y/N)       =Y?

Downloading and Executing
--------------------------
Download from the TFTP server using the 162-Bug's "NBO"
(Network Boot Operating System) command:

.. code-block:: none

    162-Bug>nbo
    Network Booting from: VME162, Controller 0, Device 0
	Loading: /mvme162.img

	Client IP Address      = 192.168.1.245
	Server IP Address      = 192.168.1.92
	Gateway IP Address     = 0.0.0.0
	Subnet IP Address Mask = 255.255.255.0
	Boot File Name         = /mvme162.img
	Argument File Name     =

	Network Boot File load in progress... To abort hit <BREAK>

	Bytes Received =&356528, Bytes Loaded =&356528
	Bytes/Second   =&89132, Elapsed Time =4 Second(s)

The program will automatically run when download is complete.

mvme167
=======

TODO.

uC5282
======

TODO.
