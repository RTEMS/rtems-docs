.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Creating a Region
-----------------

The ``rtems_region_create`` directive creates a region with the user-defined
name.  The user may select FIFO or task priority as the method for placing
waiting tasks in the task wait queue.  RTEMS allocates a Region Control Block
(RNCB) from the RNCB free list to maintain the newly created region.  RTEMS
also generates a unique region ID which is returned to the calling task.

It is not possible to calculate the exact number of bytes available to the user
since RTEMS requires overhead for each segment allocated.  For example, a
region with one segment that is the size of the entire region has more
available bytes than a region with two segments that collectively are the size
of the entire region.  This is because the region with one segment requires
only the overhead for one segment, while the other region requires the overhead
for two segments.

Due to automatic coalescing, the number of segments in the region dynamically
changes.  Therefore, the total overhead required by RTEMS dynamically changes.

Obtaining Region IDs
--------------------

When a region is created, RTEMS generates a unique region ID and assigns it to
the created region until it is deleted.  The region ID may be obtained by
either of two methods.  First, as the result of an invocation of the
``rtems_region_create`` directive, the region ID is stored in a user provided
location.  Second, the region ID may be obtained later using the
``rtems_region_ident`` directive.  The region ID is used by other region
manager directives to access this region.

Adding Memory to a Region
-------------------------

The ``rtems_region_extend`` directive may be used to add memory to an existing
region.  The caller specifies the size in bytes and starting address of the
memory being added.

Acquiring a Segment
-------------------

The ``rtems_region_get_segment`` directive attempts to acquire a segment from a
specified region.  If the region has enough available free memory, then a
segment is returned successfully to the caller.  When the segment cannot be
allocated, one of the following situations applies:

- By default, the calling task will wait forever to acquire the segment.

- Specifying the ``RTEMS_NO_WAIT`` option forces an immediate return with an
  error status code.

- Specifying a timeout limits the interval the task will wait before returning
  with an error status code.

If the task waits for the segment, then it is placed in the region's task wait
queue in either FIFO or task priority order.  All tasks waiting on a region are
returned an error when the message queue is deleted.

Releasing a Segment
-------------------

When a segment is returned to a region by the ``rtems_region_return_segment``
directive, it is merged with its unallocated neighbors to form the largest
possible segment.  The first task on the wait queue is examined to determine if
its segment request can now be satisfied.  If so, it is given a segment and
unblocked.  This process is repeated until the first task's segment request
cannot be satisfied.

Obtaining the Size of a Segment
-------------------------------

The ``rtems_region_get_segment_size`` directive returns the size in bytes of
the specified segment.  The size returned includes any "extra" memory included
in the segment because of rounding up to a page size boundary.

Changing the Size of a Segment
------------------------------

The ``rtems_region_resize_segment`` directive is used to change the size in
bytes of the specified segment.  The size may be increased or decreased.  When
increasing the size of a segment, it is possible that the request cannot be
satisfied.  This directive provides functionality similar to the ``realloc()``
function in the Standard C Library.

Deleting a Region
-----------------

A region can be removed from the system and returned to RTEMS with the
``rtems_region_delete`` directive.  When a region is deleted, its control block
is returned to the RNCB free list.  A region with segments still allocated is
not allowed to be deleted.  Any task attempting to do so will be returned an
error.  As a result of this directive, all tasks blocked waiting to obtain a
segment from the region will be readied and returned a status code which
indicates that the region was deleted.
