.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Non-Volatile Memory Driver
##########################

The Non-Volatile driver is responsible for providing an
interface to various types of non-volatile memory.  These
types of memory include, but are not limited to, Flash, EEPROM,
and battery backed RAM.  The capabilities provided
by this class of device driver are:

- Initialize the Non-Volatile Memory Driver

- Optional Disable Read and Write Handlers

- Open a Particular Memory Partition

- Close a Particular Memory Partition

- Read from a Particular Memory Partition

- Write to a Particular Memory Partition

- Erase the Non-Volatile Memory Area

There is currently only one non-volatile device driver included in the
RTEMS source tree.  The information provided in this chapter
is based on drivers developed for applications using RTEMS.
It is hoped that this driver model information can form the
basis for a standard non-volatile memory driver model that
can be supported in future RTEMS distribution.

Major and Minor Numbers
=======================

The *major* number of a device driver is its index in the
RTEMS Device Address Table.

A *minor* number is associated with each device instance
managed by a particular device driver.  An RTEMS minor number
is an ``unsigned32`` entity.  Convention calls
dividing the bits in the minor number down into categories
that specify an area of non-volatile memory and a partition
with that area.  This results in categories
like the following:

- *area* - indicates a block of non-volatile memory

- *partition* - indicates a particular address range with an area

From the above, it should be clear that a single device driver
can support multiple types of non-volatile memory in a single system.
The minor number is used to distinguish the types of memory and
blocks of memory used for different purposes.

Non-Volatile Memory Driver Configuration
========================================

There is not a standard non-volatile driver configuration table but some
fields are common across different drivers.  The non-volatile memory driver
configuration table is typically an array of structures with each
structure containing the information for a particular area of
non-volatile memory.
The following is a list of the type of information normally required
to configure each area of non-volatile memory.

*memory_type*
    is the type of memory device in this area.  Choices are battery backed RAM,
    EEPROM, Flash, or an optional user-supplied type.  If the user-supplied type
    is configured, then the user is responsible for providing a set of
    routines to program the memory.

*memory*
    is the base address of this memory area.

*attributes*
    is a pointer to a memory type specific attribute block.  Some of
    the fields commonly contained in this memory type specific attribute
    structure area:

    *use_protection_algorithm*

        is set to TRUE to indicate that the protection (i.e. locking) algorithm
        should be used for this area of non-volatile memory.  A particular
        type of non-volatile memory may not have a protection algorithm.

    *access*

        is an enumerated type to indicate the organization of the memory
        devices in this memory area.  The following is a list of the
        access types supported by the current driver implementation:
        - simple unsigned8
        - simple unsigned16
        - simple unsigned32
        - simple unsigned64
        - single unsigned8 at offset 0 in an unsigned16
        - single unsigned8 at offset 1 in an unsigned16
        - single unsigned8 at offset 0 in an unsigned32
        - single unsigned8 at offset 1 in an unsigned32
        - single unsigned8 at offset 2 in an unsigned32
        - single unsigned8 at offset 3 in an unsigned32

    *depth*

        is the depth of the progamming FIFO on this particular chip.  Some
        chips, particularly EEPROMs, have the same programming algorithm but
        vary in the depth of the amount of data that can be programmed in a single
        block.

*number_of_partitions*
    is the number of logical partitions within this area.

*Partitions*
    is the address of the table that contains an entry to describe each
    partition in this area.  Fields within each element of this
    table are defined as follows:

    *offset*

        is the offset of this partition from the base address of this area.

    *length*

        is the length of this partition.

By dividing an area of memory into multiple partitions, it is possible
to easily divide the non-volatile memory for different purposes.

Initialize the Non-Volatile Memory Driver
=========================================

At system initialization, the non-volatile memory driver's
initialization entry point will be invoked.  As part of
initialization, the driver will perform
whatever initializatin is required on each non-volatile memory area.

The discrete I/O driver may register device names for memory
partitions of particular interest to the system.  Normally this
will be restricted to the device "/dev/nv_memory" to indicate
the entire device driver.

Disable Read and Write Handlers
===============================

Depending on the target's non-volatile memory configuration, it may be
possible to write to a status register and make the memory area completely
inaccessible.  This is target dependent and beyond the standard capabilities
of any memory type.  The user has the optional capability to provide
handlers to disable and enable access to a partiticular memory area.

Open a Particular Memory Partition
==================================

This is the driver open call.  Usually this call does nothing other than
validate the minor number.

With some drivers, it may be necessary to allocate memory when a particular
device is opened.  If that is the case, then this is often the place
to do this operation.

Close a Particular Memory Partition
===================================

This is the driver close call.  Usually this call does nothing.

With some drivers, it may be necessary to allocate memory when a particular
device is opened.  If that is the case, then this is the place
where that memory should be deallocated.

Read from a Particular Memory Partition
=======================================

This corresponds to the driver read call.  After validating the minor
number and arguments, this call enables reads from the specified
memory area by invoking the user supplied "enable reads handler"
and then reads the indicated memory area.  When
invoked the ``argument_block`` is actually a pointer to the following
structure type:
.. code:: c

    typedef struct {
    uint32_t  offset;
    void     \*buffer;
    uint32_t  length;
    uint32_t  status;
    }   Non_volatile_memory_Driver_arguments;

The driver reads ``length`` bytes starting at ``offset`` into
the partition and places them at ``buffer``.  The result is returned
in ``status``.

After the read operation is complete, the user supplied "disable reads handler"
is invoked to protect the memory area again.

Write to a Particular Memory Partition
======================================

This corresponds to the driver write call.   After validating the minor
number and arguments, this call enables writes to the specified
memory area by invoking the "enable writes handler", then unprotecting
the memory area, and finally actually writing to the indicated memory
area.  When invoked the ``argument_block`` is actually a pointer to
the following structure type:
.. code:: c

    typedef struct {
    uint32_t   offset;
    void      \*buffer;
    uint32_t   length;
    uint32_t   status;
    }   Non_volatile_memory_Driver_arguments;

The driver writes ``length`` bytes from ``buffer`` and
writes them to the non-volatile memory starting at ``offset`` into
the partition.  The result is returned in ``status``.

After the write operation is complete, the "disable writes handler"
is invoked to protect the memory area again.

Erase the Non-Volatile Memory Area
==================================

This is one of the IOCTL functions supported by the I/O control
device driver entry point.  When this IOCTL function is invoked,
the specified area of non-volatile memory is erased.

.. COMMENT: Written by Eric Norum

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

