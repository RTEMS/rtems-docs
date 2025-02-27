% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

(TesterConsoles)=

# Consoles

The RTEMS Tester uses the target's console output to determine the state of a
test. Console interfaces vary depending on the testing mode, the BSP, and the
target hardware.

Consoles for simulator work best if mapped to the simulator's `stdout`
interface. The RTEMS Tester can capture and process the `stdout` data from a
simulator while it is running.

Target hardware console interfaces can vary. The most universal and stable
interface target hardware is a UART interface. There are a number of physical
interfaces for UART data these days. They are:

1. RS232
2. TTL
3. USB

RS232 is still present on a number of targets. The best solution is to use a
RS232 to USB pod and convert the port to USB.

TTL is common on a number of boards where cost is important. A console
interface is typically a development tool and removing the extra devices need
to convert the signal to RS232 or directly to USB is not needed on production
builds of the target. There is a standard header pin out for TTL UART consoles
and you can purchase low cost cables with the header and a built in UART to USB
converter. The cables come is different voltage levels so make sure you check
and use the correct voltage level.

The USB interface on a target is typcially a slave or OTG interface and all you
need to a standard USB cable.

We recommend a low cost and low power device to be a terminal server. A
Raspberry Pi or similar low cost computer running Linux can be set up quickly
and with a powered USB hub and can support a number of USB UART ports. A USB
hub with a high power port is recommended that can suppy the Raspberry Pi.

The open source daemon `ser2net` is easy to configure to map the USB UART
ports to the Telnet protocol. There is no need for security because a typical
test environment is part of a lab network that should be partitioned off from
an enginnering or corportate network and not directly connected to the
internet.

A test set up like this lets you place a terminal server close to your target
hardware providing you with the flexibility to select where you run the RTEMS
Tester. It could be your desktop or an expensive fast host machine in a server
rack. None of this equipment needs to directly interface to the target
hardware.

The RTEMS Tester directly supports the telnet protcol as a console and can
interface to the `ser1net` server. The telnet console will poll the server
waiting for the remote port to connect. If the terminal server `ser2net` does
not have a `tty` device it will not listen on the port assigned to that
`tty`. A USB `tty` can come and go depending on the power state of the
hardware and the target hardware's design and this can cause timing issues if
the target hardware is power cycled as part of a reset process.
