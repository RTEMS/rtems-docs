.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Discrete Driver
***************

The Discrete driver is responsible for providing an interface to Discrete
Input/Outputs.  The capabilities provided by this class of device driver are:

- Initialize a Discrete I/O Board

- Open a Particular Discrete Bitfield

- Close a Particular Discrete Bitfield

- Read from a Particular Discrete Bitfield

- Write to a Particular Discrete Bitfield

- Reset DACs

- Reinitialize DACS

Most discrete I/O devices are found on I/O cards that support many bits of
discrete I/O on a single card.  This driver model is centered on the notion of
reading bitfields from the card.

There are currently no discrete I/O device drivers included in the RTEMS source
tree.  The information provided in this chapter is based on drivers developed
for applications using RTEMS.  It is hoped that this driver model information
can form the discrete I/O driver model that can be supported in future RTEMS
distribution.

Major and Minor Numbers
=======================

The ``major`` number of a device driver is its index in the RTEMS Device
Address Table.

A ``minor`` number is associated with each device instance managed by a
particular device driver.  An RTEMS minor number is an ``unsigned32`` entity.
Convention calls for dividing the bits in the minor number down into categories
that specify a particular bitfield.  This results in categories like the
following:

- ``board`` - indicates the board a particular bitfield is located on

- ``word`` - indicates the particular word of discrete bits the bitfield is
  located within

- ``start`` - indicates the starting bit of the bitfield

- ``width`` - indicates the width of the bitfield

From the above, it should be clear that a single device driver can support
multiple copies of the same board in a single system.  The minor number is used
to distinguish the devices.

By providing a way to easily access a particular bitfield from the device
driver, the application is insulated with knowing how to mask fields in and out
of a discrete I/O.

Discrete I/O Driver Configuration
=================================

There is not a standard discrete I/O driver configuration table but some fields
are common across different drivers.  The discrete I/O driver configuration
table is typically an array of structures with each structure containing the
information for a particular board.  The following is a list of the type of
information normally required to configure an discrete I/O board:

``board_offset``
    is the base address of a board.

``relay_initial_values``
    is an array of the values that should be written to each output word on the
    board during initialization.  This allows the driver to start with the
    board's output in a known state.

Initialize a Discrete I/O Board
===============================

At system initialization, the discrete I/O driver's initialization entry point
will be invoked.  As part of initialization, the driver will perform whatever
board initializatin is required and then set all outputs to their configured
initial state.

The discrete I/O driver may register a device name for bitfields of particular
interest to the system.  Normally this will be restricted to the names of each
word and, if the driver supports it, an "all words".

Open a Particular Discrete Bitfield
===================================

This is the driver open call.  Usually this call does nothing other than
validate the minor number.

With some drivers, it may be necessary to allocate memory when a particular
device is opened.  If that is the case, then this is often the place to do this
operation.

Close a Particular Discrete Bitfield
====================================

This is the driver close call.  Usually this call does nothing.

With some drivers, it may be necessary to allocate memory when a particular
device is opened.  If that is the case, then this is the place where that
memory should be deallocated.

Read from a Particular Discrete Bitfield
========================================

This corresponds to the driver read call.  After validating the minor number
and arguments, this call reads the indicated bitfield.  A discrete I/O devices
may have to store the last value written to a discrete output.  If the bitfield
is output only, saving the last written value gives the appearance that it can
be read from also.  If the bitfield is input, then it is sampled.

.. note::

   Many discrete inputs have a tendency to bounce.  The application may have to
   take account for bounces.

The value returned is an ``unsigned32`` number representing the bitfield read.
This value is stored in the ``argument_block`` passed in to the call.

.. note::

   Some discrete I/O drivers have a special minor number used to access all
   discrete I/O bits on the board.  If this special minor is used, then the
   area pointed to by ``argument_block`` must be the correct size.

Write to a Particular Discrete Bitfield
=======================================

This corresponds to the driver write call.  After validating the minor number
and arguments, this call writes the indicated device.  If the specified device
is an ADC, then an error is usually returned.

The value written is an ``unsigned32`` number representing the value to be
written to the specified bitfield.  This value is stored in the
``argument_block`` passed in to the call.

.. note::

   Some discrete I/O drivers have a special minor number used to access all
   discrete I/O bits on the board.  If this special minor is used, then the
   area pointed to by ``argument_block`` must be the correct size.

Disable Discrete Outputs
========================

This is one of the IOCTL functions supported by the I/O control device driver
entry point.  When this IOCTL function is invoked, the discrete outputs are
disabled.

.. note::

   It may not be possible to disable/enable discrete output on all discrete I/O
   boards.

Enable Discrete Outputs
=======================

This is one of the IOCTL functions supported by the I/O control device driver
entry point.  When this IOCTL function is invoked, the discrete outputs are
enabled.

.. note::

    It may not be possible to disable/enable discrete output on all discrete
    I/O boards.

Reinitialize Outputs
====================

This is one of the IOCTL functions supported by the I/O control device driver
entry point.  When this IOCTL function is invoked, the discrete outputs are
rewritten with the configured initial output values.

Get Last Written Values
=======================

This is one of the IOCTL functions supported by the I/O control device driver
entry point.  When this IOCTL function is invoked, the following information is
returned to the caller:

- last value written to the specified output word

- timestamp of when the last write was performed
