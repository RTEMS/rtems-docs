% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Aaron Nyholm

```{index} IO Device
```

```{index} iodev
```

# Introduction

The IO device API is an interface to interact with IO devices. The API is as
follows:

- `rtems_iodev_alloc_and_init` - Allocate and initialise `rtems_iodev`
- `rtems_iodev_init` - Initialise `rtems_iodev`
- `rtems_iodev_register` - Register `rtems_iodev`
- `rtems_iodev_unregister_and_destroy` - Unregister `rtems_iodev`
- `rtems_iodev_destroy_unregistered` - Destroy `rtems_iodev` that has not been successfully registered

Registering a iodev creates a device file with the following `ioctl` calls:

- `RTEMS_IODEV_IOCTL_OBTAIN` - Obtains the iodev
- `RTEMS_IODEV_IOCTL_RELEASE` - Releases the iodev
- `RTEMS_IODEV_IOCTL_DEVICE_INFO` - Get the device information, defined by the driver
- `RTEMS_IODEV_IOCTL_REGION_COUNT` - Get the number of regions
- `RTEMS_IODEV_IOCTL_REGION_GET` - Get region information
- `RTEMS_IODEV_IOCTL_EVENT_COUNT` - Get the number of events
- `RTEMS_IODEV_IOCTL_EVENT_INFO` - Get event information
- `RTEMS_IODEV_IOCTL_EVENT_WAIT` - Wait or poll on an event

## IO Device Driver

A device driver is required to provide hardware specific functions for the `rtems_iodev`.
These functions are:

- `get_device_info` - Return device information
- `get_event_count` - Return event count
- `get_event_info` - Return event info
- `event_wait` - Return when requested event occurs or times out
- `get_regions` - Return pointer to array of regions
- `get_region_count` - Return region count
- `priv_destroy` - Destroy privately owned data

Device drivers handle allocation and management of memory regions and events.
Event management is handled by device drivers including if and how event queueing is handled.

Device drivers can define driver specific structs with additional information that
are returned with `get_event_info`, `event_wait` and `get_device_info`.
