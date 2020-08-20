.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

.. index:: region, definition
.. index:: segment, definition

Region Manager Definitions
--------------------------

A region makes up a physically contiguous memory space with user-defined
boundaries from which variable-sized segments are dynamically allocated and
deallocated.  A segment is a variable size section of memory which is allocated
in multiples of a user-defined page size.  This page size is required to be a
multiple of four greater than or equal to four.  For example, if a request for
a 350-byte segment is made in a region with 256-byte pages, then a 512-byte
segment is allocated.

Regions are organized as doubly linked chains of variable sized memory blocks.
Memory requests are allocated using a first-fit algorithm.  If available, the
requester receives the number of bytes requested (rounded up to the next page
size).  RTEMS requires some overhead from the region's memory for each segment
that is allocated.  Therefore, an application should only modify the memory of
a segment that has been obtained from the region.  The application should NOT
modify the memory outside of any obtained segments and within the region's
boundaries while the region is currently active in the system.

Upon return to the region, the free block is coalesced with its neighbors (if
free) on both sides to produce the largest possible unused block.

.. index:: region attribute set, building

Building an Attribute Set
-------------------------

In general, an attribute set is built by a bitwise OR of the desired attribute
components.  The set of valid region attributes is provided in the following
table:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_FIFO``
   - tasks wait by FIFO (default)
 * - ``RTEMS_PRIORITY``
   - tasks wait by priority

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list.  An attribute listed as a default
is not required to appear in the attribute list, although it is a good
programming practice to specify default attributes.  If all defaults are
desired, the attribute ``RTEMS_DEFAULT_ATTRIBUTES`` should be specified on this
call.

This example demonstrates the attribute_set parameter needed to create a region
with the task priority waiting queue discipline.  The attribute_set parameter
to the ``rtems_region_create`` directive should be ``RTEMS_PRIORITY``.

Building an Option Set
----------------------

In general, an option is built by a bitwise OR of the desired option
components.  The set of valid options for the ``rtems_region_get_segment``
directive are listed in the following table:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_WAIT``
   - task will wait for segment (default)
 * - ``RTEMS_NO_WAIT``
   - task should not wait

Option values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each option
appears exactly once in the component list.  An option listed as a default is
not required to appear in the option list, although it is a good programming
practice to specify default options.  If all defaults are desired, the
option ``RTEMS_DEFAULT_OPTIONS`` should be specified on this call.

This example demonstrates the option parameter needed to poll for a segment.
The option parameter passed to the ``rtems_region_get_segment`` directive
should be ``RTEMS_NO_WAIT``.
