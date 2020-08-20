.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the user extension manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create an extension set
.. index:: rtems_extension_create

.. _rtems_extension_create:

EXTENSION_CREATE - Create a extension set
-----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_extension_create(
          rtems_name                    name,
          const rtems_extensions_table *table,
          rtems_id                     *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - extension set created successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``table`` or ``id`` are NULL
     * - ``RTEMS_INVALID_NAME``
       - invalid extension set name
     * - ``RTEMS_TOO_MANY``
       - too many extension sets created

DESCRIPTION:

    This directive creates an extension set object and initializes it using the
    specified extension set table.  The assigned extension set identifier is
    returned in :c:data:`id`.  This identifier is used to access the extension
    set with other user extension manager directives.  For control and
    maintenance of the extension set, RTEMS allocates an Extension Set Control
    Block (ESCB) from the local ESCB free pool and initializes it.  The
    user-specified :c:data:`name` is assigned to the ESCB and may be used to
    identify the extension set via
    :ref:`rtems_extension_ident() <rtems_extension_ident>`.  The extension set
    specified by :c:data:`table` is copied to the ESCB.

NOTES:
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

.. raw:: latex

   \clearpage

.. index:: get ID of an extension set
.. index:: obtain ID of an extension set
.. index:: rtems_extension_ident

.. _rtems_extension_ident:

EXTENSION_IDENT - Get ID of a extension set
-------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_extension_ident(
          rtems_name  name,
          rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - extension set identified successfully
     * - ``RTEMS_INVALID_NAME``
       - extension set name not found

DESCRIPTION:
    This directive obtains the extension set identifier associated with the
    extension set :c:data:`name` to be acquired and returns it in :c:data:`id`.
    If the extension set name is not unique, then the extension set identifier
    will match one of the extension sets with that name.  However, this
    extension set identifier is not guaranteed to correspond to the desired
    extension set.  The extension set identifier is used to access this
    extension set in other extension set related directives.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: delete an extension set
.. index:: rtems_extension_delete

.. _rtems_extension_delete:

EXTENSION_DELETE - Delete a extension set
-----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_extension_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - extension set deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid extension set id

DESCRIPTION:
    This directive deletes the extension set specified by :c:data:`id`.  If the
    extension set is running, it is automatically canceled.  The ESCB for the
    deleted extension set is reclaimed by RTEMS.

NOTES:
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

    A extension set can be deleted by a task other than the task which created
    the extension set.
