% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 Chris Johns <chrisj@rtems.org>

(rtemstftpproxy)=

# RTEMS TFTP Proxy

```{index} Tools, rtems-tftp-proxy
```

The RTEMS TFTP Proxy ({program}`rtems-tftp-proxy`) command is an RTEMS
tool to simplify hardware testing using the RTEMS Test and Run
commands. This command lets a test set up support a number of
similarly configured boards running tests at the same time by proxying
the TFTP session requests. The {ref}`tftp-and-uboot` section details
the process to run a test executable on a network connected board.

The TFTP Proxy approach does not require any special modifications in
a boot loader to work and works with any compliant TFTP boot client.

An identical SD card boot configuration can be used in similar board
when a test set up has a number of similar boards. There is no need to
specialize boot configurations. The TFTP proxy server identifies each
board by MAC address.

A configuration file maps a board's MAC address to a TFTP server's IP
address and port number. This provides a centralized means to
partition hardware in a test rack between members of a team, continuous
integration services or any other project demands.

The TFTP port number a proixed service runs with does not need to be
the privileged TFTP port number removing the need to be root to run
the RTEMS Test or Run commands. Only the TFTP Proxy needs to running
as a privileged user. The RTEMS Test and Run commands lets you
specified the TFTP port to bind too.

## Operation

A network connected board with a suitable boot loader such as U-Boot
is configured to boot using TFTP. The boot loader's configured TFTP
server IP address is the address of the host computer running the TFTP
Proxy server or the proxy. The TFTP Proxy runs as root or an
administrator as it binds by default to the default TFTP port of 69.

A reset board sends a TFTP read request (`RRQ`) packet to the host
machine running the TFTP proxy on the standard TFTP port (69). The
proxy server searches the configuration data for a matching MAC
address. A configuration match creates a session, forwarding the
read request to the proxied IP and port.

The response from the proxied server identifies the remote session
port number and the proxy server knows the board's client port number
from the initial request. The proxy transfers the TFTP data
transparently between the session's ports until the transfer finishes.

An example configuration is three different types of boards used for
RTEMS kernel regression testing and application development.

(fig-tftp-proxy-1)=

```{figure} ../../images/user/tftp-proxy-1.png
---
alt: RTEMS TFTP Proxy Test Lab
figclass: align-center
width: 75%
---
RTEMS TFTP Proxy Test Lab
```

The project has a continuous integration (CI) server on address
`10.0.0.100` and two boards, a BeagleBone Black and Xilinx MicroZed
board, are confgured for testing. A developer on another host machine
is using a RaspberryPi to develop an application. The configuration
file is:

```none
;
; Project Foo Test network.
;
[default]
clients = bbb, uzed, rpi2

[bbb]
mac = 1c:ba:8c:96:20:bc
host = 10.0.0.100:9001

[uzed]
mac = 6e:3a:1c:22:aa:5f, 8a:3d:5f:67:55:cb
host = 10.0.0.100:9002

[rpi2]
mac = b8:27:eb:29:6b:bc
host = 10.0.0.110:9001
```

The MicroZed board can be seen by different MAC addresses depending on
how U-Boot starts. As a result both are listed.

## Configuration

The boot image tool is configured by an INI file that is passed to the
TFTP proxy on the command line when it starts.

The `[default]` section has to contain a `clients` entry that
lists the clients. There needs to be a client section for each listed
client.

A client section header is a client name listed in the `clients`
record in the `defaults` section. A client section has to contain a
`mac` record and a `host` record. The MAC record is a comma
separated list of MAC addresses in the standard 6 octet hex format
separated by `:`. A list of MAC addresses will match for any address
listed. The host record is the IP address and port number of the
proxied TFTP server.

## Command

The {program}`rtems-tftp-proxy` tool runs a TFTP proxy server using a
user provided configuration file. The command line options are:

{program}`rtems-tftp-proxy`

```{eval-rst}
.. option:: -h, --help

   Display the command line help.
```

```{eval-rst}
.. option:: -l, --log

   Set the log file name.
```

```{eval-rst}
.. option:: -v, --trace

   Enable trace or debug logging.
```

```{eval-rst}
.. option:: -c CONFIG, --config CONFIG

   The INI format configuration file.
```

```{eval-rst}
.. option:: -B BIND, --bind BIND

   The interface address the proxy binds too. The default is ``all``
   which means the proxy binds to all interfaces.
```

```{eval-rst}
.. option:: -P PORT, --port PORT

   The port the proxy server binds too. The default is the TFTP
   standard port of 69. This is a privileged port so if using this
   port number run the TFTP proxy with root or administrator
   privileges.
```

## Examples

The examples show running the TFTP Proxy as a privileged user:

```none
$ sudo rtems-tftp-proxy -c foo-test-lab.ini
Password:
RTEMS Tools - TFTP Proxy, 5.1.0
 Command Line: rtems-tftp-proxy -c foo-test-lab.ini
 Host: FreeBSD ruru 12.0-RELEASE-p3 FreeBSD 12.0-RELEASE-p3 GENERIC amd64
 Python: 3.6.9 (default, Nov 14 2019, 01:16:50) [GCC 4.2.1 Compatible FreeBSD Clang 6.0.1 (tags/RELEASE_601/final 335540)]
Proxy: all:6
```
