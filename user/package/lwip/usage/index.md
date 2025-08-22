% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2025 Kinsey Moore

(lwip_user)=

# lwIP Usage

This chapter is written for people who want to use lwIP in an application. It
describes basic initialization and how to use various features of lwIP.

## Setting Up The Environment

The rtems-lwip project uses the `rtems_waf` submodule common to many RTEMS
projects. The submodule must be initialized and updated with the appropriate git
commands:

```
git submodule init
git submodule update rtems_waf
```

As with other RTEMS projects utilizing the `rtems_waf` submodule, the desired
toolchain must be accessible via the PATH environment variable or may instead be
provided as part of the waf configuration command using the
`--rtems-tools=/absolute/path/to/toolchain` option (not including the trailing
"/bin").

The rtems-lwip project expects to build against an installed RTEMS BSP and to be
installed before it is usable by an application. The output directory can be
provided using the `--prefix=...` argument. The output directory can be
specified as the BSP install directory or the BSP install directory can be
provided separately using the `--rtems=...` argument.

## Basic Configuration

It is possible to select the BSPs to be built via the waf configuration command
argument `--rtems-bsps`, but this is not recommended as it provides no way to
enable debugging or alter BSP settings.

The recommended method of configuring a BSP is to use `config.ini`. This allows
for easier configuration management and for alteration of the configuration
defaults.

Below is an example configuration for the ARM ZynqMP RPU:

```ini
[arm/zynqmp_rpu_split_0]
LWIP_DEBUG=LWIP_DBG_ON
DHCP_DEBUG=LWIP_DBG_ON
ZYNQMP_DEFAULT_INTERFACE=XPAR_PSU_ETHERNET_0_BASEADDR
```

This configuration enables general lwIP debugging and specifically DHCP
debugging. This configuration also sets the default ethernet interface to
interface 0.

Once the configuration in `config.ini` is complete, the `./waf configure`
command must be executed with appropriate command line arguments.

## Debugging

By default, no debugging is enabled in lwIP. This means that generally, lwIP
will not output text to the console, even when intentionally dropping packets
due to resource constraints. As shown in the example above, debugging must be
enabled globally using `LWIP_DEBUG=LWIP_DBG_ON` in `config.ini` before it can be
enabled for various subsystems in lwIP. A full listing of lwIP's debug options
can be found in the lwIP documentation for the version of lwIP in use. A
non-exhaustive selection of debug flags can be found below:

```
API_LIB_DEBUG = LWIP_DBG_ON
API_MSG_DEBUG = LWIP_DBG_ON
AUTOIP_DEBUG = LWIP_DBG_ON
BRIDGEIF_DEBUG = LWIP_DBG_ON
BRIDGEIF_FDB_DEBUG = LWIP_DBG_ON
BRIDGEIF_FW_DEBUG = LWIP_DBG_ON
DHCP_DEBUG = LWIP_DBG_ON
DNS_DEBUG = LWIP_DBG_ON
ETHARP_DEBUG = LWIP_DBG_ON
ICMP_DEBUG = LWIP_DBG_ON
IGMP_DEBUG = LWIP_DBG_ON
INET_DEBUG = LWIP_DBG_ON
IP_DEBUG = LWIP_DBG_ON
IP_REASS_DEBUG = LWIP_DBG_ON
MEM_DEBUG = LWIP_DBG_ON
MEMP_DEBUG = LWIP_DBG_ON
NETIF_DEBUG = LWIP_DBG_ON
PBUF_DEBUG = LWIP_DBG_ON
RAW_DEBUG = LWIP_DBG_ON
SOCKETS_DEBUG = LWIP_DBG_ON
SYS_DEBUG = LWIP_DBG_ON
TCP_DEBUG = LWIP_DBG_ON
TCP_INPUT_DEBUG = LWIP_DBG_ON
TCPIP_DEBUG = LWIP_DBG_ON
TCP_OUTPUT_DEBUG = LWIP_DBG_ON
TIMERS_DEBUG = LWIP_DBG_ON
UDP_DEBUG = LWIP_DBG_ON
```

## Tests

Some sample applications are provided under `rtemslwip/test/` that allow for
verification of basic functionality. Additional applications can be found in the
`rtems-net-services` project.

## Tuning

The rtems-lwip project as configured by default is set up for very basic
functionality such that it can pass light network traffic. If there is a need
for more intense network traffic, adjustments need to be made. This will
typically take the form of increased memory pools and mailboxes to reduce
dropped packets.

It is important to enable the correct debugging to understand the limitations
being encountered. Typically, `IP_DEBUG`, `ETHARP_DEBUG`, and `API_MSG_DEBUG`
will expose the majority of these issues.

Common tuning parameters include `MEMP_NUM_NETBUF`, `MEMP_NUM_TCPIP_MSG_INPKT`,
`MEMP_NUM_REASSDATA`, `IP_REASS_MAX_PBUFS`, `MEMP_NUM_PBUF`, and
`PBUF_POOL_SIZE`, but every application is different and may require additional
configuration options.
