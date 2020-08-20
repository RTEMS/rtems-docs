.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Creating a Message Queue
------------------------

The ``rtems_message_queue_create`` directive creates a message queue with the
user-defined name.  The user specifies the maximum message size and maximum
number of messages which can be placed in the message queue at one time.  The
user may select FIFO or task priority as the method for placing waiting tasks
in the task wait queue.  RTEMS allocates a Queue Control Block (QCB) from the
QCB free list to maintain the newly created queue as well as memory for the
message buffer pool associated with this message queue.  RTEMS also generates a
message queue ID which is returned to the calling task.

For GLOBAL message queues, the maximum message size is effectively limited to
the longest message which the MPCI is capable of transmitting.

Obtaining Message Queue IDs
---------------------------

When a message queue is created, RTEMS generates a unique message queue ID.
The message queue ID may be obtained by either of two methods.  First, as the
result of an invocation of the ``rtems_message_queue_create`` directive, the
queue ID is stored in a user provided location.  Second, the queue ID may be
obtained later using the ``rtems_message_queue_ident`` directive.  The queue ID
is used by other message manager directives to access this message queue.

Receiving a Message
-------------------

The ``rtems_message_queue_receive`` directive attempts to retrieve a message
from the specified message queue.  If at least one message is in the queue,
then the message is removed from the queue, copied to the caller's message
buffer, and returned immediately along with the length of the message.  When
messages are unavailable, one of the following situations applies:

- By default, the calling task will wait forever for the message to arrive.

- Specifying the ``RTEMS_NO_WAIT`` option forces an immediate return with an
  error status code.

- Specifying a timeout limits the period the task will wait before returning
  with an error status.

If the task waits for a message, then it is placed in the message queue's task
wait queue in either FIFO or task priority order.  All tasks waiting on a
message queue are returned an error code when the message queue is deleted.

Sending a Message
-----------------

Messages can be sent to a queue with the ``rtems_message_queue_send`` and
``rtems_message_queue_urgent`` directives.  These directives work identically
when tasks are waiting to receive a message.  A task is removed from the task
waiting queue, unblocked, and the message is copied to a waiting task's message
buffer.

When no tasks are waiting at the queue, ``rtems_message_queue_send`` places the
message at the rear of the message queue, while ``rtems_message_queue_urgent``
places the message at the front of the queue.  The message is copied to a
message buffer from this message queue's buffer pool and then placed in the
message queue.  Neither directive can successfully send a message to a message
queue which has a full queue of pending messages.

Broadcasting a Message
----------------------

The ``rtems_message_queue_broadcast`` directive sends the same message to every
task waiting on the specified message queue as an atomic operation.  The
message is copied to each waiting task's message buffer and each task is
unblocked.  The number of tasks which were unblocked is returned to the caller.

Deleting a Message Queue
------------------------

The ``rtems_message_queue_delete`` directive removes a message queue from the
system and frees its control block as well as the memory associated with this
message queue's message buffer pool.  A message queue can be deleted by any
local task that knows the message queue's ID.  As a result of this directive,
all tasks blocked waiting to receive a message from the message queue will be
readied and returned a status code which indicates that the message queue was
deleted.  Any subsequent references to the message queue's name and ID are
invalid.  Any messages waiting at the message queue are also deleted and
deallocated.
