% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Operations

## Creating a Partition

The `rtems_partition_create` directive creates a partition with a
user-specified name. The partition's name, starting address, length and buffer
size are all specified to the `rtems_partition_create` directive. RTEMS
allocates a Partition Control Block (PTCB) from the PTCB free list. This data
structure is used by RTEMS to manage the newly created partition. The number
of buffers in the partition is calculated based upon the specified partition
length and buffer size. If successful,the unique partition ID is returned to
the calling task.

## Obtaining Partition IDs

When a partition is created, RTEMS generates a unique partition ID and assigned
it to the created partition until it is deleted. The partition ID may be
obtained by either of two methods. First, as the result of an invocation of
the `rtems_partition_create` directive, the partition ID is stored in a user
provided location. Second, the partition ID may be obtained later using the
`rtems_partition_ident` directive. The partition ID is used by other
partition manager directives to access this partition.

## Acquiring a Buffer

A buffer can be obtained by calling the `rtems_partition_get_buffer`
directive. If a buffer is available, then it is returned immediately with a
successful return code. Otherwise, an unsuccessful return code is returned
immediately to the caller. Tasks cannot block to wait for a buffer to become
available.

## Releasing a Buffer

Buffers are returned to a partition's free buffer chain with the
`rtems_partition_return_buffer` directive. This directive returns an error
status code if the returned buffer was not previously allocated from this
partition.

## Deleting a Partition

The `rtems_partition_delete` directive allows a partition to be removed and
returned to RTEMS. When a partition is deleted, the PTCB for that partition is
returned to the PTCB free list. A partition with buffers still allocated
cannot be deleted. Any task attempting to do so will be returned an error
status code.
