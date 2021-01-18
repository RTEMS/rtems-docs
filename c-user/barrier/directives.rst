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

.. _BarrierManagerDirectives:

Directives
==========

This section details the directives of the Barrier Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/barrier/if/create

.. raw:: latex

    \clearpage

.. index:: rtems_barrier_create()
.. index:: create a barrier

.. _InterfaceRtemsBarrierCreate:

rtems_barrier_create()
----------------------

Creates a barrier.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_barrier_create(
      rtems_name      name,
      rtems_attribute attribute_set,
      uint32_t        maximum_waiters,
      rtems_id       *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name of the barrier.

``attribute_set``
    This parameter is the attribute set of the barrier.

``maximum_waiters``
    This parameter is the maximum count of waiters on an automatic release
    barrier.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the identifier of the created barrier will be
    stored in this variable.

.. rubric:: DESCRIPTION:

This directive creates a barrier which resides on the local node.  The barrier
has the user-defined object name specified in ``name`` and the initial count
specified in ``attribute_set``.  The assigned object identifier is returned in
``id``.  This identifier is used to access the barrier with other barrier
related directives.

The **attribute set** specified in ``attribute_set`` is built through a
*bitwise or* of the attribute constants described below.  Not all combinations
of attributes are allowed.  Some attributes are mutually exclusive.  If
mutually exclusive attributes are combined, the behaviour is undefined.
Attributes not mentioned below are not evaluated by this directive and have no
effect.  Default attributes can be selected by using the
:c:macro:`RTEMS_DEFAULT_ATTRIBUTES` constant.

The **barrier class** is selected by the mutually exclusive
:c:macro:`RTEMS_BARRIER_MANUAL_RELEASE` and
:c:macro:`RTEMS_BARRIER_AUTOMATIC_RELEASE` attributes.

* The **manual release class** is the default and can be emphasized through use
  of the :c:macro:`RTEMS_BARRIER_MANUAL_RELEASE` attribute.  For this class,
  there is no limit on the number of tasks that will block at the barrier. Only
  when the :ref:`InterfaceRtemsBarrierRelease` directive is invoked, are the
  tasks waiting at the barrier unblocked.

* The **automatic release class** is selected by the
  :c:macro:`RTEMS_BARRIER_AUTOMATIC_RELEASE` attribute.  For this class, tasks
  calling the :ref:`InterfaceRtemsBarrierWait` directive will block until there
  are ``maximum_waiters`` minus one tasks waiting at the barrier.  When the
  ``maximum_waiters`` task invokes the :ref:`InterfaceRtemsBarrierWait`
  directive, the previous ``maximum_waiters`` - 1 tasks are automatically
  released and the caller returns.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NUMBER`
    The ``maximum_waiters`` parameter was 0 for an automatic release barrier.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive object available to create a barrier.  The number of
    barriers available to the application is configured through the
    :ref:`CONFIGURE_MAXIMUM_BARRIERS` application configuration option.

.. rubric:: NOTES:

For control and maintenance of the barrier, RTEMS allocates a :term:`BCB` from
the local BCB free pool and initializes it.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* The number of barriers available to the application is configured through the
  :ref:`CONFIGURE_MAXIMUM_BARRIERS` application configuration option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

.. Generated from spec:/rtems/barrier/if/ident

.. raw:: latex

    \clearpage

.. index:: rtems_barrier_ident()

.. _InterfaceRtemsBarrierIdent:

rtems_barrier_ident()
---------------------

Identifies a barrier by the object name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_barrier_ident( rtems_name name, rtems_id *id );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name to look up.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the object identifier of an object with the
    specified name will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive obtains a barrier identifier associated with the barrier name
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

If the barrier name is not unique, then the barrier identifier will match the
first barrier with that name in the search order.  However, this barrier
identifier is not guaranteed to correspond to the desired barrier.

The objects are searched from lowest to the highest index.  Only the local node
is searched.

The barrier identifier is used with other barrier related directives to access
the barrier.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/barrier/if/delete

.. raw:: latex

    \clearpage

.. index:: rtems_barrier_delete()
.. index:: delete a barrier

.. _InterfaceRtemsBarrierDelete:

rtems_barrier_delete()
----------------------

Deletes the barrier.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_barrier_delete( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the barrier identifier.

.. rubric:: DESCRIPTION:

This directive deletes the barrier specified by ``id``.  All tasks blocked
waiting for the barrier to be released will be readied and returned a status
code which indicates that the barrier was deleted.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no barrier associated with the identifier specified by ``id``.

.. rubric:: NOTES:

The :term:`BCB` for the deleted barrier is reclaimed by RTEMS.

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

.. Generated from spec:/rtems/barrier/if/wait

.. raw:: latex

    \clearpage

.. index:: rtems_barrier_wait()
.. index:: wait at a barrier

.. _InterfaceRtemsBarrierWait:

rtems_barrier_wait()
--------------------

Waits at the barrier.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_barrier_wait( rtems_id id, rtems_interval timeout );

.. rubric:: PARAMETERS:

``id``
    This parameter is the barrier identifier.

``timeout``
    This parameter is the timeout in clock ticks.  Use
    :c:macro:`RTEMS_NO_TIMEOUT` to wait potentially forever.

.. rubric:: DESCRIPTION:

This directive waits at the barrier specified by ``id``.  The ``timeout``
parameter defines how long the calling task is willing to wait.  Use
:c:macro:`RTEMS_NO_TIMEOUT` to wait potentially forever, otherwise set a
timeout interval in clock ticks.

Conceptually, the calling task should always be thought of as blocking when it
makes this call and being unblocked when the barrier is released.  If the
barrier is configured for manual release, this rule of thumb will always be
valid.  If the barrier is configured for automatic release, all callers will
block except for the one which trips the automatic release condition.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no barrier associated with the identifier specified by ``id``.

:c:macro:`RTEMS_TIMEOUT`
    The timeout happened while the calling task was waiting at the barrier.

:c:macro:`RTEMS_OBJECT_WAS_DELETED`
    The barrier was deleted while the calling task was waiting at the barrier.

.. rubric:: NOTES:

For automatic release barriers, the maximum count of waiting tasks is defined
during barrier creation, see :ref:`InterfaceRtemsBarrierCreate`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The timeout functionality of the directive requires a :term:`clock tick`.

.. Generated from spec:/rtems/barrier/if/release

.. raw:: latex

    \clearpage

.. index:: rtems_barrier_release()
.. index:: release a barrier

.. _InterfaceRtemsBarrierRelease:

rtems_barrier_release()
-----------------------

Releases the barrier.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_barrier_release( rtems_id id, uint32_t *released );

.. rubric:: PARAMETERS:

``id``
    This parameter is the barrier identifier.

``released``
    This parameter is the pointer to an integer variable.  When the directive
    call is successful, the number of released tasks will be stored in this
    variable.

.. rubric:: DESCRIPTION:

This directive releases the barrier specified by ``id``.  All tasks waiting at
the barrier will be unblocked.  The number of released tasks will be returned
in ``released``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``released`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ID`
    There was no barrier associated with the identifier specified by ``id``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within task context.

* The directive may unblock another task which may preempt the calling task.
