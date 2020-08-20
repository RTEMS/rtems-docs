.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the partition manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create a partition
.. index:: rtems_partition_create

.. _rtems_partition_create:

PARTITION_CREATE - Create a partition
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_partition_create(
            rtems_name       name,
            void            *starting_address,
            uintptr_t        length,
            size_t           buffer_size,
            rtems_attribute  attribute_set,
            rtems_id        *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - partition created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid partition ``name``
     * - ``RTEMS_TOO_MANY``
       - too many partitions created
     * - ``RTEMS_INVALID_ADDRESS``
       - ``starting_address`` is not on a pointer size boundary
     * - ``RTEMS_INVALID_ADDRESS``
       - ``starting_address`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_SIZE``
       - ``length`` or ``buffer_size`` is 0
     * - ``RTEMS_INVALID_SIZE``
       - ``length`` is less than the ``buffer_size``
     * - ``RTEMS_INVALID_SIZE``
       - ``buffer_size`` is not an integral multiple of the pointer size
     * - ``RTEMS_INVALID_SIZE``
       - ``buffer_size`` is less than two times the pointer size
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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

    The partition buffer area specified by the ``starting_address`` must be
    properly aligned.  It must be possible to directly store target
    architecture pointers and the also the user data.  For example, if the user
    data contains some long double or vector data types, the partition buffer
    area and the buffer size must take the alignment of these types into
    account which is usually larger than the pointer alignment.  A cache line
    alignment may be also a factor.

    The ``buffer_size`` parameter must be an integral multiple of the pointer
    size on the target architecture.  Additionally, ``buffer_size`` must be
    large enough to hold two pointers on the target architecture.  This is
    required for RTEMS to manage the buffers when they are free.

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

EXAMPLE:
    .. code-block:: c

        #include <rtems.h>
        #include <rtems/chain.h>

        #include <assert.h>

        typedef struct {
          char  less;
          short more;
        } item;

        union {
          item             data;
          rtems_chain_node node;
        } items[ 13 ];

        rtems_id create_partition(void)
        {
          rtems_id          id;
          rtems_status_code sc;

          sc = rtems_partition_create(
            rtems_build_name( 'P', 'A', 'R', 'T' ),
            items,
            sizeof( items ),
            sizeof( items[ 0 ] ),
            RTEMS_DEFAULT_ATTRIBUTES,
            &id
          );
          assert(sc == RTEMS_SUCCESSFUL);

          return id;
        }

.. raw:: latex

   \clearpage

.. index:: get ID of a partition
.. index:: obtain ID of a partition
.. index:: rtems_partition_ident

.. _rtems_partition_ident:

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

.. index:: delete a partition
.. index:: rtems_partition_delete

.. _rtems_partition_delete:

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

    The calling task does not have to be the task that created the partition.
    Any local task that knows the partition id can delete the partition.

    When a global partition is deleted, the partition id must be transmitted to
    every node in the system for deletion from the local copy of the global
    object table.

    The partition must reside on the local node, even if the partition was
    created with the ``RTEMS_GLOBAL`` option.

.. raw:: latex

   \clearpage

.. index:: get buffer from partition
.. index:: obtain buffer from partition
.. index:: rtems_partition_get_buffer

.. _rtems_partition_get_buffer:

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

.. index:: return buffer to partitition
.. index:: rtems_partition_return_buffer

.. _rtems_partition_return_buffer:

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
