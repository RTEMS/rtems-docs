% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Aaron Nyholm

```{index} IO Device
```

```{index} iodev
```

# Background

The IO device API is an interface to access IO address spaces via a device node
and a file descriptor obtained after opening the device node. A registered IO
driver provides a mapping from a logical identifier to a specific address where
an IO device resides. The API does not directly interact with device hardware.
An application can use a common identifier to a local IO address map for a device
whose address can vary depending on a bus configuration or the BSP hardware.

An example use case for this API is Peripheral Component Interconnect Express
(PCIe) devices. Different hardware setups have different memory bus allocations.
This API creates a common interface for using attached device Base Address
Register (BAR) spaces via memory regions and interrupts via events.

## Events

Interrupts are supported through the use of events. IOCTL calls are provided to
identify and interact with events.

Events, when waited on, can pass a timeout. Timeouts are handled by the device
driver, allowing for hardware and device specific implementations. However, use
of a zero timeout should always result in an indefinite wait.

## mmap

`rtems_iodev` has support for `mmap` for all regions for compatibility. Calling
`mmap` with the region index as the offset will return a successful mapping of
the region.

Protections are required to be `PROT_READ` and `PROT_WRITE`, and `MAP_SHARED`
is the required flag. Additionally, the suggested address, `addr`, should be
`NULL`.
