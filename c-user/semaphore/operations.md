% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Operations

(Creating a Semaphore)=

## Creating a Semaphore

The `rtems_semaphore_create` directive creates a binary or counting semaphore
with a user-specified name as well as an initial count. If a binary semaphore
is created with a count of zero (0) to indicate that it has been allocated,
then the task creating the semaphore is considered the current holder of the
semaphore. At create time the method for ordering waiting tasks in the
semaphore's task wait queue (by FIFO or task priority) is specified.
Additionally, the priority inheritance or priority ceiling algorithm may be
selected for local, binary semaphores that use the priority task wait queue
blocking discipline. If the priority ceiling algorithm is selected, then the
highest priority of any task which will attempt to obtain this semaphore must
be specified. RTEMS allocates a Semaphore Control Block (SMCB) from the SMCB
free list. This data structure is used by RTEMS to manage the newly created
semaphore. Also, a unique semaphore ID is generated and returned to the
calling task.

(Obtaining Semaphore IDs)=

## Obtaining Semaphore IDs

When a semaphore is created, RTEMS generates a unique semaphore ID and assigns
it to the created semaphore until it is deleted. The semaphore ID may be
obtained by either of two methods. First, as the result of an invocation of
the `rtems_semaphore_create` directive, the semaphore ID is stored in a user
provided location. Second, the semaphore ID may be obtained later using the
`rtems_semaphore_ident` directive. The semaphore ID is used by other
semaphore manager directives to access this semaphore.

(Acquiring a Semaphore)=

## Acquiring a Semaphore

The `rtems_semaphore_obtain` directive is used to acquire the
specified semaphore. A simplified version of the `rtems_semaphore_obtain`
directive can be described as follows:

> If the semaphore's count is greater than zero then decrement the
> semaphore's count else wait for release of semaphore then return
> SUCCESSFUL.

When the semaphore cannot be immediately acquired, one of the following
situations applies:

- By default, the calling task will wait forever to acquire the semaphore.
- Specifying `RTEMS_NO_WAIT` forces an immediate return with an error status
  code.
- Specifying a timeout limits the interval the task will wait before returning
  with an error status code.

If the task waits to acquire the semaphore, then it is placed in the
semaphore's task wait queue in either FIFO or task priority order. If the task
blocked waiting for a binary semaphore using priority inheritance and the
task's priority is greater than that of the task currently holding the
semaphore, then the holding task will inherit the priority of the blocking
task. All tasks waiting on a semaphore are returned an error code when the
semaphore is deleted.

When a task successfully obtains a semaphore using priority ceiling and the
priority ceiling for this semaphore is greater than that of the holder, then
the holder's priority will be elevated.

(Releasing a Semaphore)=

## Releasing a Semaphore

The `rtems_semaphore_release` directive is used to release the specified
semaphore. A simplified version of the `rtems_semaphore_release` directive
can be described as follows:

> If there are no tasks are waiting on this semaphore then increment the
> semaphore's count else assign semaphore to a waiting task and return
> SUCCESSFUL.

If this is the outermost release of a binary semaphore that uses priority
inheritance or priority ceiling and the task does not currently hold any other
binary semaphores, then the task performing the `rtems_semaphore_release`
will have its priority restored to its normal value.

(Deleting a Semaphore)=

## Deleting a Semaphore

The `rtems_semaphore_delete` directive removes a semaphore from the system
and frees its control block. A semaphore can be deleted by any local task that
knows the semaphore's ID. As a result of this directive, all tasks blocked
waiting to acquire the semaphore will be readied and returned a status code
which indicates that the semaphore was deleted. Any subsequent references to
the semaphore's name and ID are invalid.
