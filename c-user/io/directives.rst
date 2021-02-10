.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. _IOManagerDirectives:

Directives
==========

This section details the directives of the I/O Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/io/if/register-driver

.. raw:: latex

    \clearpage

.. index:: rtems_io_register_driver()
.. index:: register a device driver

.. _InterfaceRtemsIoRegisterDriver:

rtems_io_register_driver()
--------------------------

Registers and initializes the device with the specified device driver address
table and device major number in the Device Driver Table.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_register_driver(
      rtems_device_major_number         major,
      const rtems_driver_address_table *driver_table,
      rtems_device_major_number        *registered_major
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the device major number.  Use a value of zero to let the
    system obtain a device major number automatically.

``driver_table``
    This parameter is the device driver address table.

``registered_major``
    This parameter is the pointer to a device major number variable.  When the
    directive call is successful, the device major number of the registered
    device will be stored in this variable.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The device major number of the device was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The device driver address table was empty.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number of the device was out of range, see
    :ref:`CONFIGURE_MAXIMUM_DRIVERS`.

:c:macro:`RTEMS_TOO_MANY`
    The system was unable to obtain a device major number.

:c:macro:`RTEMS_RESOURCE_IN_USE`
    The device major number was already in use.

:c:macro:`RTEMS_CALLED_FROM_ISR`
    The directive was called from interrupt context.

Other status codes may be returned by :ref:`InterfaceRtemsIoInitialize`.

.. rubric:: NOTES:

If the device major number equals zero a device major number will be obtained.
The device major number of the registered driver will be returned.

After a successful registration, the :ref:`InterfaceRtemsIoInitialize`
directive will be called to initialize the device.

.. Generated from spec:/rtems/io/if/unregister-driver

.. raw:: latex

    \clearpage

.. index:: rtems_io_unregister_driver()
.. index:: unregister a device driver

.. _InterfaceRtemsIoUnregisterDriver:

rtems_io_unregister_driver()
----------------------------

Removes a device driver specified by the device major number from the Device
Driver Table.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_unregister_driver(
      rtems_device_major_number major
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_UNSATISFIED`
    The device major number was invalid.

:c:macro:`RTEMS_CALLED_FROM_ISR`
    The directive was called from interrupt context.

.. rubric:: NOTES:

Currently no specific checks are made and the driver is not closed.

.. Generated from spec:/rtems/io/if/initialize

.. raw:: latex

    \clearpage

.. index:: rtems_io_initialize()
.. index:: initialize a device driver

.. _InterfaceRtemsIoInitialize:

rtems_io_initialize()
---------------------

Initializes the device specified by the device major and minor numbers.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_initialize(
      rtems_device_major_number major,
      rtems_device_minor_number minor,
      void                     *argument
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

``minor``
    This parameter is the minor number of the device.

``argument``
    This parameter is the argument passed to the device driver initialization
    entry.

.. rubric:: DESCRIPTION:

This directive calls the device driver initialization entry registered in the
Device Driver Table for the specified device major number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number was invalid.

Other status codes may be returned by the device driver initialization entry.

.. rubric:: NOTES:

This directive is automatically invoked for each device driver defined by the
application configuration during the system initialization and via the
:ref:`InterfaceRtemsIoRegisterDriver` directive.

A device driver initialization entry is responsible for initializing all
hardware and data structures associated with a device.  If necessary, it can
allocate memory to be used during other operations.

.. Generated from spec:/rtems/io/if/register-name

.. raw:: latex

    \clearpage

.. index:: rtems_io_register_name()
.. index:: register a device in the file system

.. _InterfaceRtemsIoRegisterName:

rtems_io_register_name()
------------------------

Registers the device specified by the device major and minor numbers in the
file system under the specified name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_register_name(
      const char               *device_name,
      rtems_device_major_number major,
      rtems_device_minor_number minor
    );

.. rubric:: PARAMETERS:

``device_name``
    This parameter is the device name in the file system.

``major``
    This parameter is the device major number.

``minor``
    This parameter is the device minor number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_TOO_MANY`
    The name was already in use or other errors occurred.

.. rubric:: NOTES:

The device is registered as a character device.

.. Generated from spec:/rtems/io/if/open

.. raw:: latex

    \clearpage

.. index:: rtems_io_open()
.. index:: open a device

.. _InterfaceRtemsIoOpen:

rtems_io_open()
---------------

Opens the device specified by the device major and minor numbers.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_open(
      rtems_device_major_number major,
      rtems_device_minor_number minor,
      void                     *argument
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

``minor``
    This parameter is the minor number of the device.

``argument``
    This parameter is the argument passed to the device driver close entry.

.. rubric:: DESCRIPTION:

This directive calls the device driver open entry registered in the Device
Driver Table for the specified device major number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number was invalid.

Other status codes may be returned by the device driver open entry.

.. rubric:: NOTES:

The open entry point is commonly used by device drivers to provide exclusive
access to a device.

.. Generated from spec:/rtems/io/if/close

.. raw:: latex

    \clearpage

.. index:: rtems_io_close()
.. index:: close a device

.. _InterfaceRtemsIoClose:

rtems_io_close()
----------------

Closes the device specified by the device major and minor numbers.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_close(
      rtems_device_major_number major,
      rtems_device_minor_number minor,
      void                     *argument
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

``minor``
    This parameter is the minor number of the device.

``argument``
    This parameter is the argument passed to the device driver close entry.

.. rubric:: DESCRIPTION:

This directive calls the device driver close entry registered in the Device
Driver Table for the specified device major number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number was invalid.

Other status codes may be returned by the device driver close entry.

.. rubric:: NOTES:

The close entry point is commonly used by device drivers to relinquish
exclusive access to a device.

.. Generated from spec:/rtems/io/if/read

.. raw:: latex

    \clearpage

.. index:: rtems_io_read()
.. index:: read from a device

.. _InterfaceRtemsIoRead:

rtems_io_read()
---------------

Reads from the device specified by the device major and minor numbers.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_read(
      rtems_device_major_number major,
      rtems_device_minor_number minor,
      void                     *argument
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

``minor``
    This parameter is the minor number of the device.

``argument``
    This parameter is the argument passed to the device driver read entry.

.. rubric:: DESCRIPTION:

This directive calls the device driver read entry registered in the Device
Driver Table for the specified device major number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number was invalid.

Other status codes may be returned by the device driver read entry.

.. rubric:: NOTES:

Read operations typically require a buffer address as part of the argument
parameter block.  The contents of this buffer will be replaced with data from
the device.

.. Generated from spec:/rtems/io/if/write

.. raw:: latex

    \clearpage

.. index:: rtems_io_write()
.. index:: write to a device

.. _InterfaceRtemsIoWrite:

rtems_io_write()
----------------

Writes to the device specified by the device major and minor numbers.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_write(
      rtems_device_major_number major,
      rtems_device_minor_number minor,
      void                     *argument
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

``minor``
    This parameter is the minor number of the device.

``argument``
    This parameter is the argument passed to the device driver write entry.

.. rubric:: DESCRIPTION:

This directive calls the device driver write entry registered in the Device
Driver Table for the specified device major number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number was invalid.

Other status codes may be returned by the device driver write entry.

.. rubric:: NOTES:

Write operations typically require a buffer address as part of the argument
parameter block.  The contents of this buffer will be sent to the device.

.. Generated from spec:/rtems/io/if/control

.. raw:: latex

    \clearpage

.. index:: rtems_io_control()
.. index:: IO control
.. index:: special device services

.. _InterfaceRtemsIoControl:

rtems_io_control()
------------------

Controls the device specified by the device major and minor numbers.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_io_control(
      rtems_device_major_number major,
      rtems_device_minor_number minor,
      void                     *argument
    );

.. rubric:: PARAMETERS:

``major``
    This parameter is the major number of the device.

``minor``
    This parameter is the minor number of the device.

``argument``
    This parameter is the argument passed to the device driver I/O control
    entry.

.. rubric:: DESCRIPTION:

This directive calls the device driver I/O control entry registered in the
Device Driver Table for the specified device major number.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The device major number was invalid.

Other status codes may be returned by the device driver I/O control entry.

.. rubric:: NOTES:

The exact functionality of the driver entry called by this directive is driver
dependent.  It should not be assumed that the control entries of two device
drivers are compatible.  For example, an RS-232 driver I/O control operation
may change the baud of a serial line, while an I/O control operation for a
floppy disk driver may cause a seek operation.
