% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Background

```{index} Device Driver Table
```

## Device Driver Table

Each application utilizing the RTEMS I/O manager must specify the address of a
Device Driver Table in its Configuration Table. This table contains each device
driver's entry points that is to be initialised by RTEMS during initialization.
Each device driver may contain the following entry points:

- Initialization
- Open
- Close
- Read
- Write
- Control

If the device driver does not support a particular entry point, then that entry
in the Configuration Table should be NULL. RTEMS will return
`RTEMS_SUCCESSFUL` as the executive's and zero (0) as the device driver's
return code for these device driver entry points.

Applications can register and unregister drivers with the RTEMS I/O manager
avoiding the need to have all drivers statically defined and linked into this
table.

The {file}`confdefs.h` entry `CONFIGURE_MAXIMUM_DRIVERS` configures the
number of driver slots available to the application.

```{index} major device number
```

```{index} minor device number
```

## Major and Minor Device Numbers

Each call to the I/O manager must provide a device's major and minor numbers as
arguments. The major number is the index of the requested driver's entry
points in the Device Driver Table, and is used to select a specific device
driver. The exact usage of the minor number is driver specific, but is
commonly used to distinguish between a number of devices controlled by the same
driver.

```{index} rtems_device_major_number
```

```{index} rtems_device_minor_number
```

The data types `rtems_device_major_number` and `rtems_device_minor_number`
are used to manipulate device major and minor numbers, respectively.

```{index} device names
```

## Device Names

The I/O Manager provides facilities to associate a name with a particular
device. Directives are provided to register the name of a device and to look
up the major/minor number pair associated with a device name.

## Device Driver Environment

Application developers, as well as device driver developers, must be aware of
the following regarding the RTEMS I/O Manager:

- A device driver routine executes in the context of the invoking task. Thus
  if the driver blocks, the invoking task blocks.
- The device driver is free to change the modes of the invoking task, although
  the driver should restore them to their original values.
- Device drivers may be invoked from ISRs.
- Only local device drivers are accessible through the I/O manager.
- A device driver routine may invoke all other RTEMS directives, including I/O
  directives, on both local and global objects.

Although the RTEMS I/O manager provides a framework for device drivers, it
makes no assumptions regarding the construction or operation of a device
driver.

```{index} runtime driver registration
```

## Runtime Driver Registration

Board support package and application developers can select wether a device
driver is statically entered into the default device table or registered at
runtime.

Dynamic registration helps applications where:

- The BSP and kernel libraries are common to a range of applications for a
  specific target platform. An application may be built upon a common library
  with all drivers. The application selects and registers the drivers. Uniform
  driver name lookup protects the application.
- The type and range of drivers may vary as the application probes a bus during
  initialization.
- Support for hot swap bus system such as Compact PCI.
- Support for runtime loadable driver modules.

```{index} device driver interface
```

## Device Driver Interface

When an application invokes an I/O manager directive, RTEMS determines which
device driver entry point must be invoked. The information passed by the
application to RTEMS is then passed to the correct device driver entry point.
RTEMS will invoke each device driver entry point assuming it is compatible with
the following prototype:

```c
rtems_device_driver io_entry(
    rtems_device_major_number  major,
    rtems_device_minor_number  minor,
    void                      *argument_block
);
```

The format and contents of the parameter block are device driver and entry
point dependent.

It is recommended that a device driver avoid generating error codes which
conflict with those used by application components. A common technique used to
generate driver specific error codes is to make the most significant part of
the status indicate a driver specific code.

## Device Driver Initialization

RTEMS automatically initializes all device drivers when multitasking is
initiated via the `rtems_initialize_executive` directive. RTEMS initializes
the device drivers by invoking each device driver initialization entry point
with the following parameters:

`major`
: the major device number for this device driver.

`minor`
: zero.

`argument_block`
: will point to the Configuration Table.

The returned status will be ignored by RTEMS. If the driver cannot
successfully initialize the device, then it should invoke the
fatal_error_occurred directive.
