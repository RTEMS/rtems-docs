.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2018 On-Line Applications Research Corporation (OAR)

Operations
==========

Creating a Barrier
------------------

The ``rtems_barrier_create`` directive creates a barrier with a user-specified
name and the desired attributes.  RTEMS allocates a Barrier Control Block (BCB)
from the BCB free list.  This data structure is used by RTEMS to manage the
newly created barrier.  Also, a unique barrier ID is generated and returned to
the calling task.

Obtaining Barrier IDs
---------------------

When a barrier is created, RTEMS generates a unique barrier ID and assigns it
to the created barrier until it is deleted.  The barrier ID may be obtained by
either of two methods.  First, as the result of an invocation of the
``rtems_barrier_create`` directive, the barrier ID is stored in a user provided
location.  Second, the barrier ID may be obtained later using the
``rtems_barrier_ident`` directive.  The barrier ID is used by other barrier
manager directives to access this barrier.

Waiting at a Barrier
--------------------

The ``rtems_barrier_wait`` directive is used to wait at
the specified barrier.  The task may wait forever for the barrier to be
released or it may specify a timeout.  Specifying a timeout limits the interval
the task will wait before returning with an error status code.

If the barrier is configured as automatic and there are already one less then
the maximum number of waiters, then the call will unblock all tasks waiting at
the barrier and the caller will return immediately.

When the task does wait to acquire the barrier, then it is placed in the
barrier's task wait queue in FIFO order.  All tasks waiting on a barrier are
returned an error code when the barrier is deleted.

Releasing a Barrier
-------------------

The ``rtems_barrier_release`` directive is used to release the specified
barrier.  When the ``rtems_barrier_release`` is invoked, all tasks waiting at
the barrier are immediately made ready to execute and begin to compete for the
processor to execute.

Deleting a Barrier
------------------

The ``rtems_barrier_delete`` directive removes a barrier from the system and
frees its control block.  A barrier can be deleted by any local task that knows
the barrier's ID.  As a result of this directive, all tasks blocked waiting for
the barrier to be released, will be readied and returned a status code which
indicates that the barrier was deleted.  Any subsequent references to the
barrier's name and ID are invalid.
