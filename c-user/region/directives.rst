.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the region manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create a region

.. _rtems_region_create:

REGION_CREATE - Create a region
-------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_create(
          rtems_name       name,
          void            *starting_address,
          uintptr_t        length,
          uintptr_t        page_size,
          rtems_attribute  attribute_set,
          rtems_id        *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - region created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid region name
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``starting_address`` is NULL
     * - ``RTEMS_TOO_MANY``
       - too many regions created
     * - ``RTEMS_INVALID_SIZE``
       - invalid page size
     * - ``RTEMS_INVALID_SIZE``
       - the memory area defined by the starting address and the length
         parameters is too small

DESCRIPTION:
    This directive creates a region from a contiguous memory area
    which starts at starting_address and is length bytes long.  The memory area
    must be large enough to contain some internal region administration data.
    Segments allocated from the region will be a multiple of page_size bytes in
    length.  The specified page size will be aligned to an
    architecture-specific minimum alignment if necessary.

    The assigned region id is returned in id.  This region id is used as an
    argument to other region related directives to access the region.

    For control and maintenance of the region, RTEMS allocates and initializes
    an RNCB from the RNCB free pool.  Thus memory from the region is not used
    to store the RNCB.  However, some overhead within the region is required by
    RTEMS each time a segment is constructed in the region.

    Specifying ``RTEMS_PRIORITY`` in attribute_set causes tasks waiting for a
    segment to be serviced according to task priority.  Specifying
    ``RTEMS_FIFO`` in attribute_set or selecting ``RTEMS_DEFAULT_ATTRIBUTES``
    will cause waiting tasks to be serviced in First In-First Out order.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    The following region attribute constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_FIFO``
       - tasks wait by FIFO (default)
     * - ``RTEMS_PRIORITY``
       - tasks wait by priority

.. raw:: latex

   \clearpage

.. index:: get ID of a region
.. index:: obtain ID of a region
.. index:: rtems_region_ident

.. _rtems_region_ident:

REGION_IDENT - Get ID of a region
---------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_ident(
          rtems_name  name,
          rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - region identified successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_NAME``
       - region name not found

DESCRIPTION:

    This directive obtains the region id associated with the region name to be
    acquired.  If the region name is not unique, then the region id will match
    one of the regions with that name.  However, this region id is not
    guaranteed to correspond to the desired region.  The region id is used to
    access this region in other region manager directives.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. index:: delete a region
.. index:: rtems_region_delete

.. _rtems_region_delete:

REGION_DELETE - Delete a region
-------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_delete(
          rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - region deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid region id
     * - ``RTEMS_RESOURCE_IN_USE``
       - segments still in use

DESCRIPTION:
    This directive deletes the region specified by id.  The region cannot be
    deleted if any of its segments are still allocated.  The RNCB for the
    deleted region is reclaimed by RTEMS.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    The calling task does not have to be the task that created the region.  Any
    local task that knows the region id can delete the region.

.. raw:: latex

   \clearpage

.. index:: add memory to a region
.. index:: region, add memory
.. index:: rtems_region_extend

.. _rtems_region_extend:

REGION_EXTEND - Add memory to a region
--------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_extend(
          rtems_id   id,
          void      *starting_address,
          uintptr_t  length
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - region extended successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``starting_address`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id
     * - ``RTEMS_INVALID_ADDRESS``
       - invalid address of area to add

DESCRIPTION:
    This directive adds the memory area which starts at
    :c:data:`starting_address` for :c:data:`length` bytes to the region
    specified by :c:data:`id`.

    There are no alignment requirements for the memory area.  The memory area
    must be big enough to contain some maintenance blocks.  It must not overlap
    parts of the current heap memory areas.  Disconnected memory areas added to
    the heap will lead to used blocks which cover the gaps.  Extending with an
    inappropriate memory area will corrupt the heap resulting in undefined
    behaviour.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    The calling task does not have to be the task that created the region.  Any
    local task that knows the region identifier can extend the region.

.. raw:: latex

   \clearpage

.. index:: get segment from region
.. index:: rtems_region_get_segment

.. _rtems_region_get_segment:

REGION_GET_SEGMENT - Get segment from a region
----------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_get_segment(
          rtems_id         id,
          uintptr_t        size,
          rtems_option     option_set,
          rtems_interval   timeout,
          void           **segment
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - segment obtained successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``segment`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id
     * - ``RTEMS_INVALID_SIZE``
       - request is for zero bytes or exceeds the size of maximum segment which is
         possible for this region
     * - ``RTEMS_UNSATISFIED``
       - segment of requested size not available
     * - ``RTEMS_TIMEOUT``
       - timed out waiting for segment
     * - ``RTEMS_OBJECT_WAS_DELETED``
       - region deleted while waiting

DESCRIPTION:
    This directive obtains a variable size segment from the region specified by
    ``id``.  The address of the allocated segment is returned in segment.  The
    ``RTEMS_WAIT`` and ``RTEMS_NO_WAIT`` components of the options parameter
    are used to specify whether the calling tasks wish to wait for a segment to
    become available or return immediately if no segment is available.  For
    either option, if a sufficiently sized segment is available, then the
    segment is successfully acquired by returning immediately with the
    ``RTEMS_SUCCESSFUL`` status code.

    If the calling task chooses to return immediately and a segment large
    enough is not available, then an error code indicating this fact is
    returned.  If the calling task chooses to wait for the segment and a
    segment large enough is not available, then the calling task is placed on
    the region's segment wait queue and blocked.  If the region was created
    with the ``RTEMS_PRIORITY`` option, then the calling task is inserted into
    the wait queue according to its priority.  However, if the region was
    created with the ``RTEMS_FIFO`` option, then the calling task is placed at
    the rear of the wait queue.

    The timeout parameter specifies the maximum interval that a task is willing
    to wait to obtain a segment.  If timeout is set to ``RTEMS_NO_TIMEOUT``,
    then the calling task will wait forever.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    The actual length of the allocated segment may be larger than the requested
    size because a segment size is always a multiple of the region's page size.

    The following segment acquisition option constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_WAIT``
       - task will wait for segment (default)
     * - ``RTEMS_NO_WAIT``
       - task should not wait

    A clock tick is required to support the timeout functionality of this
    directive.

.. raw:: latex

   \clearpage

.. index:: return segment to region
.. index:: rtems_region_return_segment

.. _rtems_region_return_segment:

REGION_RETURN_SEGMENT - Return segment to a region
--------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_return_segment(
          rtems_id  id,
          void     *segment
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - segment returned successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``segment`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id
     * - ``RTEMS_INVALID_ADDRESS``
       - segment address not in region

DESCRIPTION:
    This directive returns the segment specified by segment to the region
    specified by id.  The returned segment is merged with its neighbors to form
    the largest possible segment.  The first task on the wait queue is examined
    to determine if its segment request can now be satisfied.  If so, it is
    given a segment and unblocked.  This process is repeated until the first
    task's segment request cannot be satisfied.

NOTES:
    This directive will cause the calling task to be preempted if one or more
    local tasks are waiting for a segment and the following conditions exist:

    - a waiting task has a higher priority than the calling task

    - the size of the segment required by the waiting task is less than or
      equal to the size of the segment returned.

.. raw:: latex

   \clearpage

.. index:: get size of segment
.. index:: rtems_region_get_segment_size

.. _rtems_region_get_segment_size:

REGION_GET_SEGMENT_SIZE - Obtain size of a segment
--------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_get_segment_size(
          rtems_id   id,
          void      *segment,
          uintptr_t *size
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - segment obtained successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``segment`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``size`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id
     * - ``RTEMS_INVALID_ADDRESS``
       - segment address not in region

DESCRIPTION:
    This directive obtains the size in bytes of the specified segment.

NOTES:
    The actual length of the allocated segment may be larger than the requested
    size because a segment size is always a multiple of the region's page size.

.. raw:: latex

   \clearpage

.. index:: resize segment
.. index:: rtems_region_resize_segment

.. _rtems_region_resize_segment:

REGION_RESIZE_SEGMENT - Change size of a segment
------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_resize_segment(
          rtems_id   id,
          void      *segment,
          uintptr_t  new_size,
          uintptr_t *old_size
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - segment obtained successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``segment`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``old_size`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id
     * - ``RTEMS_INVALID_ADDRESS``
       - segment address not in region
     * - ``RTEMS_UNSATISFIED``
       - unable to make segment larger

DESCRIPTION:
    This directive is used to increase or decrease the size of a segment.  When
    increasing the size of a segment, it is possible that there is not memory
    available contiguous to the segment.  In this case, the request is
    unsatisfied.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    If an attempt to increase the size of a segment fails, then the application
    may want to allocate a new segment of the desired size, copy the contents
    of the original segment to the new, larger segment and then return the
    original segment.

.. raw:: latex

   \clearpage

.. index:: obtain region information
.. index:: rtems_region_get_information

.. _rtems_region_get_information:

REGION_GET_INFORMATION - Get region information
-----------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_get_information(
          rtems_id                id,
          Heap_Information_block *the_info
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - information obtained successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``the_info`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id

DESCRIPTION:
    This directive is used to obtain information about the used and free memory
    in the region specified by ``id``. This is a snapshot at the time
    of the call. The information will be returned in the structure pointed to
    by ``the_info``.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    This is primarily intended as a mechanism to obtain a diagnostic information. 
    This method forms am O(n) scan of the free and an O(n) scan of the
    used blocks in the region to calculate the information provided. Given that
    the execution time is driven by the number of used and free blocks, it can
    take a non-deterministic time to execute.

.. raw:: latex

   \clearpage

.. index:: obtain region information on free blocks
.. index:: rtems_region_get_free_information

.. _rtems_region_get_free_information:

REGION_GET_FREE_INFORMATION - Get region free information
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_region_get_free_information(
          rtems_id                id,
          Heap_Information_block *the_info
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - information obtained successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``the_info`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid region id

DESCRIPTION:
    This directive is used to obtain information about the free memory
    in the region specified by ``id``. This is a snapshot at the time
    of the call. The information will be returned in the structure pointed to
    by ``the_info``.

NOTES:
    This directive will obtain the allocator mutex and may cause the calling
    task to be preempted.

    This uses the same structure to return information as the 
    ``rtems_region_get_information`` directive but does not fill in the
    used information.

    This is primarily intended as a mechanism to obtain a diagnostic information. 
    This method forms am O(n) scan of the free in the region to calculate
    the information provided. Given that the execution time is driven by
    the number of used and free blocks, it can take a non-deterministic
    time to execute. Typically, there are many used blocks and a much smaller
    number of used blocks making a call to this directive less expensive than
    a call to ``rtems_region_get_information``.
