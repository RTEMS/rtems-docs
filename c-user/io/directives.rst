.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
