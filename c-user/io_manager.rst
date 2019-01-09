.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. COMMENT: All rights reserved.

.. index:: device drivers
.. index:: IO Manager

I/O Manager
***********

Introduction
============

The input/output interface manager provides a well-defined mechanism for
accessing device drivers and a structured methodology for organizing device
drivers.  The directives provided by the I/O manager are:

- rtems_io_initialize_ - Initialize a device driver

- rtems_io_register_driver_ - Register a device driver

- rtems_io_unregister_driver_ - Unregister a device driver

- rtems_io_register_name_ - Register a device name

- rtems_io_lookup_name_ - Look up a device name

- rtems_io_open_ - Open a device

- rtems_io_close_ - Close a device

- rtems_io_read_ - Read from a device

- rtems_io_write_ - Write to a device

- rtems_io_control_ - Special device services

Background
==========

.. index:: Device Driver Table

Device Driver Table
-------------------

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
in the Configuration Table should be NULL.  RTEMS will return
``RTEMS_SUCCESSFUL`` as the executive's and zero (0) as the device driver's
return code for these device driver entry points.

Applications can register and unregister drivers with the RTEMS I/O manager
avoiding the need to have all drivers statically defined and linked into this
table.

The :file:`confdefs.h` entry ``CONFIGURE_MAXIMUM_DRIVERS`` configures the
number of driver slots available to the application.

.. index:: major device number
.. index:: minor device number

Major and Minor Device Numbers
------------------------------

Each call to the I/O manager must provide a device's major and minor numbers as
arguments.  The major number is the index of the requested driver's entry
points in the Device Driver Table, and is used to select a specific device
driver.  The exact usage of the minor number is driver specific, but is
commonly used to distinguish between a number of devices controlled by the same
driver.

.. index:: rtems_device_major_number
.. index:: rtems_device_minor_number

The data types ``rtems_device_major_number`` and ``rtems_device_minor_number``
are used to manipulate device major and minor numbers, respectively.

.. index:: device names

Device Names
------------

The I/O Manager provides facilities to associate a name with a particular
device.  Directives are provided to register the name of a device and to look
up the major/minor number pair associated with a device name.

Device Driver Environment
-------------------------

Application developers, as well as device driver developers, must be aware of
the following regarding the RTEMS I/O Manager:

- A device driver routine executes in the context of the invoking task.  Thus
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

.. index:: runtime driver registration

Runtime Driver Registration
---------------------------

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

.. index:: device driver interface

Device Driver Interface
-----------------------

When an application invokes an I/O manager directive, RTEMS determines which
device driver entry point must be invoked.  The information passed by the
application to RTEMS is then passed to the correct device driver entry point.
RTEMS will invoke each device driver entry point assuming it is compatible with
the following prototype:

.. code-block:: c

    rtems_device_driver io_entry(
        rtems_device_major_number  major,
        rtems_device_minor_number  minor,
        void                      *argument_block
    );

The format and contents of the parameter block are device driver and entry
point dependent.

It is recommended that a device driver avoid generating error codes which
conflict with those used by application components.  A common technique used to
generate driver specific error codes is to make the most significant part of
the status indicate a driver specific code.

Device Driver Initialization
----------------------------

RTEMS automatically initializes all device drivers when multitasking is
initiated via the ``rtems_initialize_executive`` directive.  RTEMS initializes
the device drivers by invoking each device driver initialization entry point
with the following parameters:

``major``
    the major device number for this device driver.

``minor``
    zero.

``argument_block``
    will point to  the Configuration Table.

The returned status will be ignored by RTEMS.  If the driver cannot
successfully initialize the device, then it should invoke the
fatal_error_occurred directive.

Operations
==========

Register and Lookup Name
------------------------

The ``rtems_io_register`` directive associates a name with the specified device
(i.e. major/minor number pair).  Device names are typically registered as part
of the device driver initialization sequence.  The ``rtems_io_lookup``
directive is used to determine the major/minor number pair associated with the
specified device name.  The use of these directives frees the application from
being dependent on the arbitrary assignment of major numbers in a particular
application.  No device naming conventions are dictated by RTEMS.

Accessing an Device Driver
--------------------------

The I/O manager provides directives which enable the application program to
utilize device drivers in a standard manner.  There is a direct correlation
between the RTEMS I/O manager directives ``rtems_io_initialize``,
``rtems_io_open``, ``rtems_io_close``, ``rtems_io_read``, ``rtems_io_write``,
and ``rtems_io_control`` and the underlying device driver entry points.

Directives
==========

This section details the I/O manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: register a device driver
.. index:: rtems_io_register_driver

.. _rtems_io_register_driver:

IO_REGISTER_DRIVER - Register a device driver
---------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_register_driver(
            rtems_device_major_number   major,
            rtems_driver_address_table *driver_table,
            rtems_device_major_number  *registered_major
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully registered
     * - ``RTEMS_INVALID_ADDRESS``
       - invalid registered major pointer
     * - ``RTEMS_INVALID_ADDRESS``
       - invalid driver table
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number
     * - ``RTEMS_TOO_MANY``
       - no available major device table slot
     * - ``RTEMS_RESOURCE_IN_USE``
       - major device number entry in use

DESCRIPTION:
    This directive attempts to add a new device driver to the Device Driver
    Table. The user can specify a specific major device number via the
    directive's ``major`` parameter, or let the registration routine find the
    next available major device number by specifing a major number of
    ``0``. The selected major device number is returned via the
    ``registered_major`` directive parameter. The directive automatically
    allocation major device numbers from the highest value down.

    This directive automatically invokes the ``IO_INITIALIZE`` directive if the
    driver address table has an initialization and open entry.

    The directive returns ``RTEMS_TOO_MANY`` if Device Driver Table is full,
    and ``RTEMS_RESOURCE_IN_USE`` if a specific major device number is
    requested and it is already in use.

NOTES:
    The Device Driver Table size is specified in the Configuration Table
    condiguration. This needs to be set to maximum size the application
    requires.

.. raw:: latex

   \clearpage

.. index:: unregister a device driver
.. index:: rtems_io_unregister_driver

.. _rtems_io_unregister_driver:

IO_UNREGISTER_DRIVER - Unregister a device driver
-------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_unregister_driver(
            rtems_device_major_number   major
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully registered
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive removes a device driver from the Device Driver Table.

NOTES:
    Currently no specific checks are made and the driver is not closed.

.. raw:: latex

   \clearpage

.. index:: initialize a device driver
.. index:: rtems_io_initialize

.. _rtems_io_initialize:

IO_INITIALIZE - Initialize a device driver
------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_initialize(
            rtems_device_major_number  major,
            rtems_device_minor_number  minor,
            void                      *argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive calls the device driver initialization routine specified in
    the Device Driver Table for this major number. This directive is
    automatically invoked for each device driver when multitasking is initiated
    via the initialize_executive directive.

    A device driver initialization module is responsible for initializing all
    hardware and data structures associated with a device. If necessary, it can
    allocate memory to be used during other operations.

NOTES:
    This directive may or may not cause the calling task to be preempted.  This
    is dependent on the device driver being initialized.

.. raw:: latex

   \clearpage

.. index:: register device
.. index:: rtems_io_register_name

.. _rtems_io_register_name:

IO_REGISTER_NAME - Register a device
------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_register_name(
            const char                *name,
            rtems_device_major_number  major,
            rtems_device_minor_number  minor
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_TOO_MANY``
       - too many devices registered

DESCRIPTION:
    This directive associates name with the specified major/minor number pair.

NOTES:
    This directive will not cause the calling task to be preempted.

.. raw:: latex

   \clearpage

.. index:: lookup device major and minor number
.. index:: rtems_io_lookup_name

.. _rtems_io_lookup_name:

IO_LOOKUP_NAME - Lookup a device
--------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_lookup_name(
            const char          *name,
            rtems_driver_name_t *device_info
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_UNSATISFIED``
       - name not registered

DESCRIPTION:
    This directive returns the major/minor number pair associated with the
    given device name in ``device_info``.

NOTES:
    This directive will not cause the calling task to be preempted.

.. raw:: latex

   \clearpage

.. index:: open a devive
.. index:: rtems_io_open

.. _rtems_io_open:

IO_OPEN - Open a device
-----------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_open(
            rtems_device_major_number  major,
            rtems_device_minor_number  minor,
            void                      *argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive calls the device driver open routine specified in the Device
    Driver Table for this major number.  The open entry point is commonly used
    by device drivers to provide exclusive access to a device.

NOTES:
    This directive may or may not cause the calling task to be preempted.  This
    is dependent on the device driver being invoked.

.. raw:: latex

   \clearpage

.. index:: close a device
.. index:: rtems_io_close

.. _rtems_io_close:

IO_CLOSE - Close a device
-------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_close(
            rtems_device_major_number  major,
            rtems_device_minor_number  minor,
            void                      *argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive calls the device driver close routine specified in the
    Device Driver Table for this major number.  The close entry point is
    commonly used by device drivers to relinquish exclusive access to a device.

NOTES:
    This directive may or may not cause the calling task to be preempted.  This
    is dependent on the device driver being invoked.

.. raw:: latex

   \clearpage

.. index:: read from a device
.. index:: rtems_io_read

.. _rtems_io_read:

IO_READ - Read from a device
----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_read(
            rtems_device_major_number  major,
            rtems_device_minor_number  minor,
            void                      *argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive calls the device driver read routine specified in the Device
    Driver Table for this major number.  Read operations typically require a
    buffer address as part of the argument parameter block.  The contents of
    this buffer will be replaced with data from the device.

NOTES:
    This directive may or may not cause the calling task to be preempted.  This
    is dependent on the device driver being invoked.

.. raw:: latex

   \clearpage

.. index:: write to a device
.. index:: rtems_io_write

.. _rtems_io_write:

IO_WRITE - Write to a device
----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_write(
            rtems_device_major_number  major,
            rtems_device_minor_number  minor,
            void                      *argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive calls the device driver write routine specified in the
    Device Driver Table for this major number.  Write operations typically
    require a buffer address as part of the argument parameter block.  The
    contents of this buffer will be sent to the device.

NOTES:
    This directive may or may not cause the calling task to be preempted.  This
    is dependent on the device driver being invoked.

.. raw:: latex

   \clearpage

.. index:: special device services
.. index:: IO Control
.. index:: rtems_io_control

.. _rtems_io_control:

IO_CONTROL - Special device services
------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_io_control(
            rtems_device_major_number  major,
            rtems_device_minor_number  minor,
            void                      *argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successfully initialized
     * - ``RTEMS_INVALID_NUMBER``
       - invalid major device number

DESCRIPTION:
    This directive calls the device driver I/O control routine specified in the
    Device Driver Table for this major number.  The exact functionality of the
    driver entry called by this directive is driver dependent.  It should not
    be assumed that the control entries of two device drivers are compatible.
    For example, an RS-232 driver I/O control operation may change the baud
    rate of a serial line, while an I/O control operation for a floppy disk
    driver may cause a seek operation.

NOTES:
    This directive may or may not cause the calling task to be preempted.  This
    is dependent on the device driver being invoked.
