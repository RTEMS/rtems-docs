% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2025 embedded brains GmbH & Co. KG

# stm32u5

This BSP supports the
[STM32U5 Series](https://www.st.com/en/microcontrollers-microprocessors/stm32u5-series.html).

The BSP is known to run on the following boards:

- [GRiSP nano](https://www.grisp.org/hardware) (BSP variant
  `arm/stm32u5-grisp-nano`)

## Clocks

The clocks for this BSP are configured using structures that are defined in the
`start/stm32u5-config-{clk,osc,per}.c` files. An application can overwrite the
definitions if different clocks are required.

## Console Driver

The console supports the on-chip USARTs. The BSP options allow selecting
different pins and a different default console instance. Please check the
default BSP options (via `./waf bspdefaults --rtems-bsp arm/stm32u5-grisp-nano`)
for details.

## Memory configurations

The BSP supports to run from different memory. So for example, internal Flash
and RAM can be used for a bootloader and external OctoSPI memory can be used for
an application. The target memory can be selected by using one of the provided
linker command files.

### OctoSPI memory

The `arm/stm32u5-grisp-nano` BSP supports an external OctoSPI RAM. It is
configured in the `start/stm32u5-init-octospi.c`. Other memory chips (RAM or
Flash) need modified values in that file.

## USB Driver

Currently, the drivers in `LibBSD` do not support the used USB controller.
USB via HAL should be possible but is not yet tested.

## SD/MMC Driver

The `st_sdmmc` provided by the `LibBSD` can be used with small modifications to
`LibBSD` (smaller `RTEMS_BSD_CONFIG_DOMAIN_PAGE_MBUFS_SIZE`). Depending on the
`LibBSD` version, the internal memory is not enough and external memory is
required.
