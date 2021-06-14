.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. _DualPortedMemoryManagerDirectives:

Directives
==========

This section details the directives of the Dual-Ported Memory Manager. A
subsection is dedicated to each of this manager's directives and lists the
calling sequence, parameters, description, return values, and notes of the
directive.

.. Generated from spec:/rtems/dpmem/if/create

.. raw:: latex

    \clearpage

.. index:: rtems_port_create()
.. index:: create a port

.. _InterfaceRtemsPortCreate:

rtems_port_create()
-------------------

Creates a port.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_port_create(
      rtems_name name,
      void      *internal_start,
      void      *external_start,
      uint32_t   length,
      rtems_id  *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name of the port.

``internal_start``
    This parameter is the internal start address of the memory area.

``external_start``
    This parameter is the external start address of the memory area.

``length``
    This parameter is the length in bytes of the memory area.

``id``
    This parameter is the pointer to an :c:type:`rtems_id` object.  When the
    directive call is successful, the identifier of the created port will be
    stored in this object.

.. rubric:: DESCRIPTION:

This directive creates a port which resides on the local node.  The port has
the user-defined object name specified in ``name``.  The assigned object
identifier is returned in ``id``.  This identifier is used to access the port
with other dual-ported memory port related directives.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``internal_start`` parameter was not properly aligned.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``external_start`` parameter was not properly aligned.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive object available to create a port.  The number of
    port available to the application is configured through the
    :ref:`CONFIGURE_MAXIMUM_PORTS` application configuration option.

.. rubric:: NOTES:

The ``internal_start`` and ``external_start`` parameters must be on a boundary
defined by the target processor architecture.

For control and maintenance of the port, RTEMS allocates a :term:`DPCB` from
the local DPCB free pool and initializes it.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The number of ports available to the application is configured through the
  :ref:`CONFIGURE_MAXIMUM_PORTS` application configuration option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

.. Generated from spec:/rtems/dpmem/if/ident

.. raw:: latex

    \clearpage

.. index:: rtems_port_ident()

.. _InterfaceRtemsPortIdent:

rtems_port_ident()
------------------

Identifies a port by the object name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_port_ident( rtems_name name, rtems_id *id );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name to look up.

``id``
    This parameter is the pointer to an :c:type:`rtems_id` object.  When the
    directive call is successful, the object identifier of an object with the
    specified name will be stored in this object.

.. rubric:: DESCRIPTION:

This directive obtains a port identifier associated with the port name
specified in ``name``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was 0.

:c:macro:`RTEMS_INVALID_NAME`
    There was no object with the specified name on the local node.

.. rubric:: NOTES:

If the port name is not unique, then the port identifier will match the first
port with that name in the search order.  However, this port identifier is not
guaranteed to correspond to the desired port.

The objects are searched from lowest to the highest index.  Only the local node
is searched.

The port identifier is used with other dual-ported memory related directives to
access the port.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/dpmem/if/delete

.. raw:: latex

    \clearpage

.. index:: rtems_port_delete()
.. index:: delete a port

.. _InterfaceRtemsPortDelete:

rtems_port_delete()
-------------------

Deletes the port.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_port_delete( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the port identifier.

.. rubric:: DESCRIPTION:

This directive deletes the port specified by ``id``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no port associated with the identifier specified by ``id``.

.. rubric:: NOTES:

The :term:`DPCB` for the deleted port is reclaimed by RTEMS.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The calling task does not have to be the task that created the object.  Any
  local task that knows the object identifier can delete the object.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

.. Generated from spec:/rtems/dpmem/if/external-to-internal

.. raw:: latex

    \clearpage

.. index:: rtems_port_external_to_internal()
.. index:: convert external to internal address

.. _InterfaceRtemsPortExternalToInternal:

rtems_port_external_to_internal()
---------------------------------

Converts the external address to the internal address.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_port_external_to_internal(
      rtems_id id,
      void    *external,
      void   **internal
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the port identifier.

``external``
    This parameter is the external address to convert.

``internal``
    This parameter is the pointer to a ``void`` pointer object.  When the
    directive call is successful, the external address associated with the
    internal address will be stored in this object.

.. rubric:: DESCRIPTION:

This directive converts a dual-ported memory address from external to internal
representation for the specified port.  If the given external address is
invalid for the specified port, then the internal address is set to the given
external address.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``id`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``internal`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/dpmem/if/internal-to-external

.. raw:: latex

    \clearpage

.. index:: rtems_port_internal_to_external()
.. index:: convert internal to external address

.. _InterfaceRtemsPortInternalToExternal:

rtems_port_internal_to_external()
---------------------------------

Converts the internal address to the external address.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_port_internal_to_external(
      rtems_id id,
      void    *internal,
      void   **external
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the port identifier.

``internal``
    This parameter is the internal address to convert.

``external``
    This parameter is the pointer to a ``void`` pointer object.  When the
    directive call is successful, the external address associated with the
    internal address will be stored in this object.

.. rubric:: DESCRIPTION:

This directive converts a dual-ported memory address from internal to external
representation so that it can be passed to owner of the DPMA represented by the
specified port.  If the given internal address is an invalid dual-ported
address, then the external address is set to the given internal address.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``id`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``external`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.
