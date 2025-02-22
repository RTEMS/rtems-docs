% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Operations

## Register and Lookup Name

The `rtems_io_register` directive associates a name with the specified device
(i.e. major/minor number pair). Device names are typically registered as part
of the device driver initialization sequence. The `rtems_io_lookup`
directive is used to determine the major/minor number pair associated with the
specified device name. The use of these directives frees the application from
being dependent on the arbitrary assignment of major numbers in a particular
application. No device naming conventions are dictated by RTEMS.

## Accessing an Device Driver

The I/O manager provides directives which enable the application program to
utilize device drivers in a standard manner. There is a direct correlation
between the RTEMS I/O manager directives `rtems_io_initialize`,
`rtems_io_open`, `rtems_io_close`, `rtems_io_read`, `rtems_io_write`,
and `rtems_io_control` and the underlying device driver entry points.
