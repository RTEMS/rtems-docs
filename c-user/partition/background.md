% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Background

```{index} partition, definition
```

## Partition Manager Definitions

A partition is a physically contiguous memory area divided into fixed-size
buffers that can be dynamically allocated and deallocated.

```{index} buffers, definition
```

Partitions are managed and maintained as a list of buffers. Buffers are
obtained from the front of the partition's free buffer chain and returned to
the rear of the same chain. When a buffer is on the free buffer chain, RTEMS
uses two pointers of memory from each buffer as the free buffer chain. When a
buffer is allocated, the entire buffer is available for application use.
Therefore, modifying memory that is outside of an allocated buffer could
destroy the free buffer chain or the contents of an adjacent allocated buffer.

```{index} partition attribute set, building
```

## Building a Partition Attribute Set

In general, an attribute set is built by a bitwise OR of the desired attribute
components. The set of valid partition attributes is provided in the following
table:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``RTEMS_LOCAL``
   - local partition (default)
 * - ``RTEMS_GLOBAL``
   - global partition
```

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list. An attribute listed as a default
is not required to appear in the attribute list, although it is a good
programming practice to specify default attributes. If all defaults are
desired, the attribute `RTEMS_DEFAULT_ATTRIBUTES` should be specified on this
call. The attribute_set parameter should be `RTEMS_GLOBAL` to indicate that
the partition is to be known globally.
