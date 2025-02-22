% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 embedded brains GmbH & Co. KG

% Copyright (C) 2020 Chris Johns

# sparc (SPARC / LEON)

(bsp-sparc-erc32)=

## erc32

TODO.

(bsp-sparc-leon2)=

## leon2

This BSP supports LEON2 systems, in particular the [Microchip AT697F](https://www.microchip.com/en-us/product/AT697F). The following
default build configurations are provided:

- leon2 - A generic LEON2 system with memory at 0x4000000.
- at697f - For the AT697F. Built with `-mcpu=leon -mfix-at697f`.

The BSP contains UART, timer, and interrupt controller drivers.
Drivers for PCI are available through the {ref}`driver manager <BSP_sparc_leon3_drv_mgr>`.

(bsp-sparc-leon3)=

## leon3

This BSP supports the LEON3/4/5 systems from Cobham Gaisler.
The following default build configurations are provided:

- leon3 - A generic [LEON3/4/5](https://www.gaisler.com/leon5) system with memory at 0x4000000.
- ut700 - For the [UT700](https://caes.com/product/ut700). Built with `-mcpu=leon3 -mfix-ut700`.
- ut699 - For the [UT699](https://caes.com/product/ut699). Built with `-mcpu=leon -mfix-ut699`.
- gr712rc - For the [GR712RC](https://www.gaisler.com/gr712rc). Built with `-mcpu=leon3 -mfix-gr712rc`.
- gr740 - For the [GR740](https://www.gaisler.com/gr740). Memory located at address 0x0.

The BSP contains UART, timer, and interrupt controller drivers. Drivers for additional
peripherals are available through the driver manager.

(bsp-sparc-leon3-drv-mgr)=

### Driver Manager

The leon3 BSP includes an optional driver manager that handles drivers and
devices on the AMBA and PCI Plug & Play buses. The driver manager can either
be initialized manually by the user, or started automatically on startup by
setting the `RTEMS_DRVMGR_STARTUP` option. It can be configured to
automatically instantiate a driver for each hardware device found.

Drivers for the following devices are provided and handled via the driver manager:

- SpaceWire (GRSPW, GRSPW2, GRSPW2_DMA)
- SpaceWire Router (GRSPWROUTER)
- SpaceWire Time Distribution Protocol (SPWTDP)
- CAN - non-DMA (OCCAN) and DMA (GRCAN, GRCANFD)
- GPIO (GRGPIO)
- L2 Cache (L2CACHE)
- IOMMU (GRIOMMU)
- ADC/DAC (GRADCDAC)
- Timers (GPTIMER, GRTIMER)
- 1553 BC, RT and BM support (GR1553B)
- I2C Master (I2CMST)
- PCI (GRPCI2, GRPCI, PCIF)
- Memory Controller (MCTRL)
- Memory Scrubber (MEMSCRUB)
- Pulse Width Modulation Generator (GRPWM)
- CCSDS/ECSS Telemetry Encoder/Decoder (GRTM/GRTC)
- CSDS Time Manager (GRCTM)
- Ethernet (GRETH 10/100/1000) (requires network stack)
- Performance counters (L4STAT)
- Serial Peripheral Interface (AHBSTAT)
- AHB Status (AHBSTAT)

### Build Configuration Options

The following options can be used in the BSP section of the `waf`
configuration INI file. The `waf` defaults can be used to inspect the values.

`CONSOLE_USE_INTERRUPTS`

: Use the Termios interrupt mode in the console driver (false by default).

`RTEMS_DRVMGR_STARTUP`

: Enable the Driver Manager at startup (false by default).
