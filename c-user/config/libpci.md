% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# PCI Library Configuration

This section defines the system configuration parameters supported by
`rtems/confdefs.h` related to configuring the PCI Library for RTEMS.

The PCI Library startup behaviour can be configured in four different ways
depending on how `CONFIGURE_PCI_CONFIG_LIB` is defined:

```{index} PCI_LIB_AUTO
```

`PCI_LIB_AUTO`
: Used to enable the PCI auto configuration software. PCI will be automatically
  probed, PCI buses enumerated, all devices and bridges will be initialized
  using Plug & Play software routines. The PCI device tree will be populated
  based on the PCI devices found in the system, PCI devices will be configured
  by allocating address region resources automatically in PCI space according
  to the BSP or host bridge driver set up.

```{index} PCI_LIB_READ
```

`PCI_LIB_READ`
: Used to enable the PCI read configuration software. The current PCI
  configuration is read to create the RAM representation (the PCI device tree)
  of the PCI devices present. PCI devices are assumed to already have been
  initialized and PCI buses enumerated, it is therefore required that a BIOS or
  a boot loader has set up configuration space prior to booting into RTEMS.

```{index} PCI_LIB_STATIC
```

`PCI_LIB_STATIC`
: Used to enable the PCI static configuration software. The user provides a PCI
  tree with information how all PCI devices are to be configured at compile
  time by linking in a custom `struct pci_bus pci_hb` tree. The static PCI
  library will not probe PCI for devices, instead it will assume that all
  devices defined by the user are present, it will enumerate the PCI buses and
  configure all PCI devices in static configuration accordingly. Since probe
  and allocation software is not needed the startup is faster, has smaller
  footprint and does not require dynamic memory allocation.

```{index} PCI_LIB_PERIPHERAL
```

`PCI_LIB_PERIPHERAL`
: Used to enable the PCI peripheral configuration. It is similar to
  `PCI_LIB_STATIC`, but it will never write the configuration to the PCI
  devices since PCI peripherals are not allowed to access PCI configuration
  space.

Note that selecting `PCI_LIB_STATIC` or `PCI_LIB_PERIPHERAL` but not
defining `pci_hb` will reuslt in link errors. Note also that in these modes
Plug & Play is not performed.
