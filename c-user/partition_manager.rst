.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

.. index:: partitions

Partition Manager
*****************

Introduction
============

The partition manager provides facilities to dynamically allocate memory in
fixed-size units.  The directives provided by the partition manager are:

- rtems_partition_create_ - Create a partition

- rtems_partition_ident_ - Get ID of a partition

- rtems_partition_delete_ - Delete a partition

- rtems_partition_get_buffer_ - Get buffer from a partition

- rtems_partition_return_buffer_ - Return buffer to a partition

Background
==========

.. index:: partition, definition

Partition Manager Definitions
-----------------------------

A partition is a physically contiguous memory area divided into fixed-size
buffers that can be dynamically allocated and deallocated.

.. index:: buffers, definition

Partitions are managed and maintained as a list of buffers.  Buffers are
obtained from the front of the partition's free buffer chain and returned to
the rear of the same chain.  When a buffer is on the free buffer chain, RTEMS
uses two pointers of memory from each buffer as the free buffer chain.  When a
buffer is allocated, the entire buffer is available for application use.
Therefore, modifying memory that is outside of an allocated buffer could
destroy the free buffer chain or the contents of an adjacent allocated buffer.

.. index:: partition attribute set, building

Building a Partition Attribute Set
----------------------------------

In general, an attribute set is built by a bitwise OR of the desired attribute
components.  The set of valid partition attributes is provided in the following
table:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_LOCAL``
   - local partition (default)
 * - ``RTEMS_GLOBAL``
   - global partition

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list.  An attribute listed as a default
is not required to appear in the attribute list, although it is a good
programming practice to specify default attributes.  If all defaults are
desired, the attribute ``RTEMS_DEFAULT_ATTRIBUTES`` should be specified on this
call.  The attribute_set parameter should be ``RTEMS_GLOBAL`` to indicate that
the partition is to be known globally.

Operations
==========

Creating a Partition
--------------------

The ``rtems_partition_create`` directive creates a partition with a
user-specified name.  The partition's name, starting address, length and buffer
size are all specified to the ``rtems_partition_create`` directive.  RTEMS
allocates a Partition Control Block (PTCB) from the PTCB free list.  This data
structure is used by RTEMS to manage the newly created partition.  The number
of buffers in the partition is calculated based upon the specified partition
length and buffer size. If successful,the unique partition ID is returned to
the calling task.

Obtaining Partition IDs
-----------------------

When a partition is created, RTEMS generates a unique partition ID and assigned
it to the created partition until it is deleted.  The partition ID may be
obtained by either of two methods.  First, as the result of an invocation of
the ``rtems_partition_create`` directive, the partition ID is stored in a user
provided location.  Second, the partition ID may be obtained later using the
``rtems_partition_ident`` directive.  The partition ID is used by other
partition manager directives to access this partition.

Acquiring a Buffer
------------------

A buffer can be obtained by calling the ``rtems_partition_get_buffer``
directive.  If a buffer is available, then it is returned immediately with a
successful return code.  Otherwise, an unsuccessful return code is returned
immediately to the caller.  Tasks cannot block to wait for a buffer to become
available.

Releasing a Buffer
------------------

Buffers are returned to a partition's free buffer chain with the
``rtems_partition_return_buffer`` directive.  This directive returns an error
status code if the returned buffer was not previously allocated from this
partition.

Deleting a Partition
--------------------

The ``rtems_partition_delete`` directive allows a partition to be removed and
returned to RTEMS.  When a partition is deleted, the PTCB for that partition is
returned to the PTCB free list.  A partition with buffers still allocated
cannot be deleted.  Any task attempting to do so will be returned an error
status code.

Directives
==========

This section details the partition manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_partition_create:
.. index:: create a partition
.. index:: rtems_partition_create

PARTITION_CREATE - Create a partition
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_partition_create(
            rtems_name       name,
            void            *starting_address,
            uint32_t         length,
            uint32_t         buffer_size,
            rtems_attribute  attribute_set,
            rtems_id        *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - partition created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid partition name
     * - ``RTEMS_TOO_MANY``
       - too many partitions created
     * - ``RTEMS_INVALID_ADDRESS``
       - address not on four byte boundary
     * - ``RTEMS_INVALID_ADDRESS``
       - ``starting_address`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_SIZE``
       - length or buffer size is 0
     * - ``RTEMS_INVALID_SIZE``
       - length is less than the buffer size
     * - ``RTEMS_INVALID_SIZE``
       - buffer size not a multiple of 4
     * - ``RTEMS_MP_NOT_CONFIGURED``
       - multiprocessing not configured
     * - ``RTEMS_TOO_MANY``
       - too many global objects

DESCRIPTION:
    This directive creates a partition of fixed size buffers from a physically
    contiguous memory space which starts at starting_address and is length
    bytes in size.  Each allocated buffer is to be of ``buffer_size`` in bytes.
    The assigned partition id is returned in ``id``.  This partition id is used
    to access the partition with other partition related directives.  For
    control and maintenance of the partition, RTEMS allocates a PTCB from the
    local PTCB free pool and initializes it.

NOTES:
    This directive will not cause the calling task to be preempted.

    The ``starting_address`` must be properly aligned for the target
    architecture.

    The ``buffer_size`` parameter must be a multiple of the CPU alignment
    factor.  Additionally, ``buffer_size`` must be large enough to hold two
    pointers on the target architecture.  This is required for RTEMS to manage
    the buffers when they are free.

    Memory from the partition is not used by RTEMS to store the Partition
    Control Block.

    The following partition attribute constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_LOCAL``
       - local partition (default)
     * - ``RTEMS_GLOBAL``
       - global partition

    The PTCB for a global partition is allocated on the local node.  The memory
    space used for the partition must reside in shared memory. Partitions
    should not be made global unless remote tasks must interact with the
    partition.  This is to avoid the overhead incurred by the creation of a
    global partition.  When a global partition is created, the partition's name
    and id must be transmitted to every node in the system for insertion in the
    local copy of the global object table.

    The total number of global objects, including partitions, is limited by the
    maximum_global_objects field in the Configuration Table.

.. raw:: latex

   \clearpage

.. _rtems_partition_ident:
.. index:: get ID of a partition
.. index:: obtain ID of a partition
.. index:: rtems_partition_ident

PARTITION_IDENT - Get ID of a partition
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_partition_ident(
            rtems_name  name,
            uint32_t    node,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - partition identified successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_NAME``
       - partition name not found
     * - ``RTEMS_INVALID_NODE``
       - invalid node id

DESCRIPTION:
    This directive obtains the partition id associated with the partition name.
    If the partition name is not unique, then the partition id will match one
    of the partitions with that name.  However, this partition id is not
    guaranteed to correspond to the desired partition.  The partition id is
    used with other partition related directives to access the partition.

NOTES:
    This directive will not cause the running task to be preempted.

    If node is ``RTEMS_SEARCH_ALL_NODES``, all nodes are searched with the
    local node being searched first.  All other nodes are searched with the
    lowest numbered node searched first.

    If node is a valid node number which does not represent the local node,
    then only the partitions exported by the designated node are searched.

    This directive does not generate activity on remote nodes.  It accesses
    only the local copy of the global object table.

.. raw:: latex

   \clearpage

.. _rtems_partition_delete:
.. index:: delete a partition
.. index:: rtems_partition_delete

PARTITION_DELETE - Delete a partition
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_partition_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - partition deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid partition id
     * - ``RTEMS_RESOURCE_IN_USE``
       - buffers still in use
     * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
       - cannot delete remote partition

DESCRIPTION:
    This directive deletes the partition specified by id.  The partition cannot
    be deleted if any of its buffers are still allocated.  The PTCB for the
    deleted partition is reclaimed by RTEMS.

NOTES:
    This directive will not cause the calling task to be preempted.

    The calling task does not have to be the task that created the partition.
    Any local task that knows the partition id can delete the partition.

    When a global partition is deleted, the partition id must be transmitted to
    every node in the system for deletion from the local copy of the global
    object table.

    The partition must reside on the local node, even if the partition was
    created with the ``RTEMS_GLOBAL`` option.

.. raw:: latex

   \clearpage

.. _rtems_partition_get_buffer:
.. index:: get buffer from partition
.. index:: obtain buffer from partition
.. index:: rtems_partition_get_buffer

PARTITION_GET_BUFFER - Get buffer from a partition
--------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_partition_get_buffer(
            rtems_id   id,
            void     **buffer
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - buffer obtained successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``buffer`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid partition id
     * - ``RTEMS_UNSATISFIED``
       - all buffers are allocated

DESCRIPTION:
    This directive allows a buffer to be obtained from the partition specified
    in id.  The address of the allocated buffer is returned in buffer.

NOTES:
    This directive will not cause the running task to be preempted.

    All buffers begin on a four byte boundary.

    A task cannot wait on a buffer to become available.

    Getting a buffer from a global partition which does not reside on the local
    node will generate a request telling the remote node to allocate a buffer
    from the specified partition.

.. raw:: latex

   \clearpage

.. _rtems_partition_return_buffer:
.. index:: return buffer to partitition
.. index:: rtems_partition_return_buffer

PARTITION_RETURN_BUFFER - Return buffer to a partition
------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_partition_return_buffer(
            rtems_id  id,
            void     *buffer
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - buffer returned successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``buffer`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid partition id
     * - ``RTEMS_INVALID_ADDRESS``
       - buffer address not in partition

DESCRIPTION:
    This directive returns the buffer specified by buffer to the partition
    specified by id.

NOTES:
    This directive will not cause the running task to be preempted.

    Returning a buffer to a global partition which does not reside on the local
    node will generate a request telling the remote node to return the buffer
    to the specified partition.

    Returning a buffer multiple times is an error.  It will corrupt the
    internal state of the partition.
