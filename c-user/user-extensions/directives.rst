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

.. _UserExtensionsManagerDirectives:

Directives
==========

This section details the directives of the User Extensions Manager. A
subsection is dedicated to each of this manager's directives and lists the
calling sequence, parameters, description, return values, and notes of the
directive.

.. Generated from spec:/rtems/userext/if/create

.. raw:: latex

    \clearpage

.. index:: rtems_extension_create()
.. index:: create an extension set

.. _InterfaceRtemsExtensionCreate:

rtems_extension_create()
------------------------

Creates an extension set.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_extension_create(
      rtems_name                    name,
      const rtems_extensions_table *extension_table,
      rtems_id                     *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name of the extension set.

``extension_table``
    This parameter is the table with the extensions to be used by the extension
    set.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the identifier of the created extension set
    will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive creates an extension set which resides on the local node.  The
extension set has the user-defined object name specified in ``name``.  The
assigned object identifier is returned in ``id``.  This identifier is used to
access the extension set with other extension set related directives.

The extension set is initialized using the extension table specified in
``extension_table``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``extension_table`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive object available to create an extension set.  The
    number of extension sets available to the application is configured through
    the :ref:`CONFIGURE_MAXIMUM_USER_EXTENSIONS` application configuration
    option.

.. rubric:: NOTES:

The user-provided extension set table is not used after the return of the
directive.

Newly created extension sets are immediately installed and are invoked upon the
next system event supporting an extension.

An alternative to dynamically created extension sets are initial extensions,
see :ref:`CONFIGURE_INITIAL_EXTENSIONS`.  Initial extensions are recommended
for extension sets which provide a fatal error extension.

For control and maintenance of the extension set, RTEMS allocates a
:term:`ESCB` from the local ESCB free pool and initializes it.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The number of extension sets available to the application is configured
  through the :ref:`CONFIGURE_MAXIMUM_USER_EXTENSIONS` application
  configuration option.

.. Generated from spec:/rtems/userext/if/delete

.. raw:: latex

    \clearpage

.. index:: rtems_extension_delete()
.. index:: delete an extension set

.. _InterfaceRtemsExtensionDelete:

rtems_extension_delete()
------------------------

Deletes the extension set.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_extension_delete( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the extension set identifier.

.. rubric:: DESCRIPTION:

This directive deletes the extension set specified by ``id``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no extension set associated with the identifier specified by
    ``id``.

.. rubric:: NOTES:

The :term:`ESCB` for the deleted extension set is reclaimed by RTEMS.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The calling task does not have to be the task that created the object.  Any
  local task that knows the object identifier can delete the object.

.. Generated from spec:/rtems/userext/if/ident

.. raw:: latex

    \clearpage

.. index:: rtems_extension_ident()

.. _InterfaceRtemsExtensionIdent:

rtems_extension_ident()
-----------------------

Identifies an extension set by the object name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_extension_ident( rtems_name name, rtems_id *id );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name to look up.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the object identifier of an object with the
    specified name will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive obtains an extension set identifier associated with the
extension set name specified in ``name``.

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

If the extension set name is not unique, then the extension set identifier will
match the first extension set with that name in the search order. However, this
extension set identifier is not guaranteed to correspond to the desired
extension set.

The objects are searched from lowest to the highest index.  Only the local node
is searched.

The extension set identifier is used with other extension related directives to
access the extension set.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive will not cause the calling task to be preempted.
