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

.. _PartitionManagerDirectives:

Directives
==========

This section details the directives of the Partition Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/part/if/create

.. raw:: latex

    \clearpage

.. index:: rtems_partition_create()
.. index:: create a partition

.. _InterfaceRtemsPartitionCreate:

rtems_partition_create()
------------------------

Creates a partition.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_partition_create(
      rtems_name      name,
      void           *starting_address,
      uintptr_t       length,
      size_t          buffer_size,
      rtems_attribute attribute_set,
      rtems_id       *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name of the partition.

``starting_address``
    This parameter is the starting address of the buffer area used by the
    partition.

``length``
    This parameter is the length in bytes of the buffer area used by the
    partition.

``buffer_size``
    This parameter is the size in bytes of a buffer managed by the partition.

``attribute_set``
    This parameter is the attribute set of the partition.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the identifier of the created partition will
    be stored in this variable.

.. rubric:: DESCRIPTION:

This directive creates a partition of fixed size buffers from a physically
contiguous memory space which starts at ``starting_address`` and is ``length``
bytes in size.  Each allocated buffer is to be of ``buffer_size`` in bytes.
The partition has the user-defined object name specified in ``name``.  The
assigned object identifier is returned in ``id``.  This identifier is used to
access the partition with other partition related directives.

The **attribute set** specified in ``attribute_set`` is built through a
*bitwise or* of the attribute constants described below.  Not all combinations
of attributes are allowed.  Some attributes are mutually exclusive.  If
mutually exclusive attributes are combined, the behaviour is undefined.
Attributes not mentioned below are not evaluated by this directive and have no
effect.  Default attributes can be selected by using the
:c:macro:`RTEMS_DEFAULT_ATTRIBUTES` constant.

The partition has a local or global **scope** in a multiprocessing network
(this attribute does not refer to SMP systems).  The scope is selected by the
mutually exclusive :c:macro:`RTEMS_LOCAL` and :c:macro:`RTEMS_GLOBAL`
attributes.

* A **local scope** is the default and can be emphasized through the use of the
  :c:macro:`RTEMS_LOCAL` attribute.  A local partition can be only used by the
  node which created it.

* A **global scope** is established if the :c:macro:`RTEMS_GLOBAL` attribute is
  set.  The memory space used for the partition must reside in shared memory.
  Setting the global attribute in a single node system has no effect.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_SIZE`
    The ``length`` parameter was 0.

:c:macro:`RTEMS_INVALID_SIZE`
    The ``buffer_size`` parameter was 0.

:c:macro:`RTEMS_INVALID_SIZE`
    The ``length`` parameter was less than the ``buffer_size`` parameter.

:c:macro:`RTEMS_INVALID_SIZE`
    The ``buffer_size`` parameter was not an integral multiple of the pointer
    size.

:c:macro:`RTEMS_INVALID_SIZE`
    The ``buffer_size`` parameter was less than two times the pointer size.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``starting_address`` parameter was not on a pointer size boundary.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive object available to create a partition.  The number
    of partitions available to the application is configured through the
    :ref:`CONFIGURE_MAXIMUM_PARTITIONS` application configuration option.

:c:macro:`RTEMS_TOO_MANY`
    In multiprocessing configurations, there was no inactive global object
    available to create a global semaphore.  The number of global objects
    available to the application is configured through the
    :ref:`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application configuration
    option.

.. rubric:: NOTES:

The partition buffer area specified by the ``starting_address`` must be
properly aligned.  It must be possible to directly store target architecture
pointers and also the user data.  For example, if the user data contains some
long double or vector data types, the partition buffer area and the buffer size
must take the alignment of these types into account which is usually larger
than the pointer alignment.  A cache line alignment may be also a factor.  Use
:c:macro:`RTEMS_PARTITION_ALIGNMENT` to specify the minimum alignment of a
partition buffer type.

The ``buffer_size`` parameter must be an integral multiple of the pointer size
on the target architecture.  Additionally, ``buffer_size`` must be large enough
to hold two pointers on the target architecture.  This is required for RTEMS to
manage the buffers when they are free.

For control and maintenance of the partition, RTEMS allocates a :term:`PTCB`
from the local PTCB free pool and initializes it. Memory from the partition
buffer area is not used by RTEMS to store the PTCB.

The PTCB for a global partition is allocated on the local node.  Partitions
should not be made global unless remote tasks must interact with the partition.
This is to avoid the overhead incurred by the creation of a global partition.
When a global partition is created, the partition's name and identifier must be
transmitted to every node in the system for insertion in the local copy of the
global object table.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* When the directive operates on a global object, the directive sends a message
  to remote nodes.  This may preempt the calling task.

* The number of partitions available to the application is configured through
  the :ref:`CONFIGURE_MAXIMUM_PARTITIONS` application configuration option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

* The number of global objects available to the application is configured
  through the :ref:`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application
  configuration option.

.. Generated from spec:/rtems/part/if/ident

.. raw:: latex

    \clearpage

.. index:: rtems_partition_ident()
.. index:: get ID of a partition
.. index:: obtain ID of a partition

.. _InterfaceRtemsPartitionIdent:

rtems_partition_ident()
-----------------------

Identifies a partition by the object name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_partition_ident(
      rtems_name name,
      uint32_t   node,
      rtems_id  *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name to look up.

``node``
    This parameter is the node or node set to search for a matching object.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the object identifier of an object with the
    specified name will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive obtains a partition identifier associated with the partition
name specified in ``name``.

The node to search is specified in ``node``.  It shall be

* a valid node number,

* the constant :c:macro:`RTEMS_SEARCH_ALL_NODES` to search in all nodes,

* the constant :c:macro:`RTEMS_SEARCH_LOCAL_NODE` to search in the local node
  only, or

* the constant :c:macro:`RTEMS_SEARCH_OTHER_NODES` to search in all nodes
  except the local node.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was 0.

:c:macro:`RTEMS_INVALID_NAME`
    There was no object with the specified name on the specified nodes.

:c:macro:`RTEMS_INVALID_NODE`
    In multiprocessing configurations, the specified node was invalid.

.. rubric:: NOTES:

If the partition name is not unique, then the partition identifier will match
the first partition with that name in the search order.  However, this
partition identifier is not guaranteed to correspond to the desired partition.

The objects are searched from lowest to the highest index.  If ``node`` is
:c:macro:`RTEMS_SEARCH_ALL_NODES`, all nodes are searched with the local node
being searched first.  All other nodes are searched from lowest to the highest
node number.

If node is a valid node number which does not represent the local node, then
only the partitions exported by the designated node are searched.

This directive does not generate activity on remote nodes.  It accesses only
the local copy of the global object table.

The partition identifier is used with other partition related directives to
access the partition.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/part/if/delete

.. raw:: latex

    \clearpage

.. index:: rtems_partition_delete()
.. index:: delete a partition

.. _InterfaceRtemsPartitionDelete:

rtems_partition_delete()
------------------------

Deletes the partition.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_partition_delete( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the partition identifier.

.. rubric:: DESCRIPTION:

This directive deletes the partition specified by ``id``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no partition associated with the identifier specified by ``id``.

:c:macro:`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`
    The partition resided on a remote node.

:c:macro:`RTEMS_RESOURCE_IN_USE`
    There were buffers of the partition still in use.

.. rubric:: NOTES:

The partition cannot be deleted if any of its buffers are still allocated.

The :term:`PTCB` for the deleted partition is reclaimed by RTEMS.

When a global partition is deleted, the partition identifier must be
transmitted to every node in the system for deletion from the local copy of the
global object table.

The partition must reside on the local node, even if the partition was created
with the :c:macro:`RTEMS_GLOBAL` attribute.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* When the directive operates on a global object, the directive sends a message
  to remote nodes.  This may preempt the calling task.

* The calling task does not have to be the task that created the object.  Any
  local task that knows the object identifier can delete the object.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

.. Generated from spec:/rtems/part/if/get-buffer

.. raw:: latex

    \clearpage

.. index:: rtems_partition_get_buffer()
.. index:: get buffer from partition
.. index:: obtain buffer from partition

.. _InterfaceRtemsPartitionGetBuffer:

rtems_partition_get_buffer()
----------------------------

Tries to get a buffer from the partition.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_partition_get_buffer( rtems_id id, void **buffer );

.. rubric:: PARAMETERS:

``id``
    This parameter is the partition identifier.

``buffer``
    This parameter is the pointer to a buffer pointer variable.  When the
    directive call is successful, the pointer to the allocated buffer will be
    stored in this variable.

.. rubric:: DESCRIPTION:

This directive allows a buffer to be obtained from the partition specified by
``id``.  The address of the allocated buffer is returned through the ``buffer``
parameter.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no partition associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``buffer`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_UNSATISFIED`
    There was no free buffer available to allocate and return.

.. rubric:: NOTES:

The buffer start alignment is determined by the memory area and buffer size
used to create the partition.

A task cannot wait on a buffer to become available.

Getting a buffer from a global partition which does not reside on the local
node will generate a request telling the remote node to allocate a buffer from
the partition.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* When the directive operates on a local object, the directive may be called
  from within interrupt context.

* The directive may be called from within task context.

* When the directive operates on a local object, the directive will not cause
  the calling task to be preempted.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/part/if/return-buffer

.. raw:: latex

    \clearpage

.. index:: rtems_partition_return_buffer()
.. index:: return buffer to partition

.. _InterfaceRtemsPartitionReturnBuffer:

rtems_partition_return_buffer()
-------------------------------

Returns the buffer to the partition.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_partition_return_buffer( rtems_id id, void *buffer );

.. rubric:: PARAMETERS:

``id``
    This parameter is the partition identifier.

``buffer``
    This parameter is the pointer to the buffer to return.

.. rubric:: DESCRIPTION:

This directive returns the buffer specified by ``buffer`` to the partition
specified by ``id``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no partition associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The buffer referenced by ``buffer`` was not in the partition.

.. rubric:: NOTES:

Returning a buffer multiple times is an error.  It will corrupt the internal
state of the partition.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* When the directive operates on a local object, the directive may be called
  from within interrupt context.

* The directive may be called from within task context.

* When the directive operates on a local object, the directive will not cause
  the calling task to be preempted.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.
