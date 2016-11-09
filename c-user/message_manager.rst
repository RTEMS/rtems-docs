.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Message Manager
***************

.. index:: messages
.. index:: message queues

Introduction
============

The message manager provides communication and synchronization capabilities
using RTEMS message queues.  The directives provided by the message manager
are:

- rtems_message_queue_create_ - Create a queue

- rtems_message_queue_ident_ - Get ID of a queue

- rtems_message_queue_delete_ - Delete a queue

- rtems_message_queue_send_ - Put message at rear of a queue

- rtems_message_queue_urgent_ - Put message at front of a queue

- rtems_message_queue_broadcast_ - Broadcast N messages to a queue

- rtems_message_queue_receive_ - Receive message from a queue

- rtems_message_queue_get_number_pending_ - Get number of messages pending on a queue

- rtems_message_queue_flush_ - Flush all messages on a queue

Background
==========

Messages
--------

A message is a variable length buffer where information can be stored to
support communication.  The length of the message and the information stored in
that message are user-defined and can be actual data, pointer(s), or empty.

Message Queues
--------------

A message queue permits the passing of messages among tasks and ISRs.  Message
queues can contain a variable number of messages.  Normally messages are sent
to and received from the queue in FIFO order using the
``rtems_message_queue_send`` directive.  However, the
``rtems_message_queue_urgent`` directive can be used to place messages at the
head of a queue in LIFO order.

Synchronization can be accomplished when a task can wait for a message to
arrive at a queue.  Also, a task may poll a queue for the arrival of a message.

The maximum length message which can be sent is set on a per message queue
basis.  The message content must be copied in general to/from an internal
buffer of the message queue or directly to a peer in certain cases.  This copy
operation is performed with interrupts disabled.  So it is advisable to keep
the messages as short as possible.

Building a Message Queue Attribute Set
--------------------------------------
.. index:: message queue attributes

In general, an attribute set is built by a bitwise OR of the desired attribute
components.  The set of valid message queue attributes is provided in the
following table:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_FIFO``
   - tasks wait by FIFO (default)
 * - ``RTEMS_PRIORITY``
   - tasks wait by priority
 * - ``RTEMS_LOCAL``
   - local message queue (default)
 * - ``RTEMS_GLOBAL``
   - global message queue

An attribute listed as a default is not required to appear in the attribute
list, although it is a good programming practice to specify default attributes.
If all defaults are desired, the attribute ``RTEMS_DEFAULT_ATTRIBUTES`` should
be specified on this call.

This example demonstrates the attribute_set parameter needed to create a local
message queue with the task priority waiting queue discipline.  The
attribute_set parameter to the ``rtems_message_queue_create`` directive could
be either ``RTEMS_PRIORITY`` or ``RTEMS_LOCAL | RTEMS_PRIORITY``.  The
attribute_set parameter can be set to ``RTEMS_PRIORITY`` because
``RTEMS_LOCAL`` is the default for all created message queues.  If a similar
message queue were to be known globally, then the attribute_set parameter would
be ``RTEMS_GLOBAL | RTEMS_PRIORITY``.

Building a MESSAGE_QUEUE_RECEIVE Option Set
-------------------------------------------

In general, an option is built by a bitwise OR of the desired option
components.  The set of valid options for the ``rtems_message_queue_receive``
directive are listed in the following table:

.. list-table::
 :class: rtems-table

 * - ``RTEMS_WAIT``
   - task will wait for a message (default)
 * - ``RTEMS_NO_WAIT``
   - task should not wait

An option listed as a default is not required to appear in the option OR list,
although it is a good programming practice to specify default options.  If all
defaults are desired, the option ``RTEMS_DEFAULT_OPTIONS`` should be specified
on this call.

This example demonstrates the option parameter needed to poll for a message to
arrive.  The option parameter passed to the ``rtems_message_queue_receive``
directive should be ``RTEMS_NO_WAIT``.

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

Directives
==========

This section details the message manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_create:

MESSAGE_QUEUE_CREATE - Create a queue
-------------------------------------
.. index:: create a message queue
.. index:: rtems_message_queue_create

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_create(
            rtems_name        name,
            uint32_t          count,
            size_t            max_message_size,
            rtems_attribute   attribute_set,
            rtems_id         *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - queue created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid queue name
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_NUMBER``
       - invalid message count
     * - ``RTEMS_INVALID_SIZE``
       - invalid message size
     * - ``RTEMS_TOO_MANY``
       - too many queues created
     * - ``RTEMS_UNSATISFIED``
       - unable to allocate message buffers
     * - ``RTEMS_MP_NOT_CONFIGURED``
       - multiprocessing not configured
     * - ``RTEMS_TOO_MANY``
       - too many global objects

DESCRIPTION:
    This directive creates a message queue which resides on the local node with
    the user-defined name specified in name.  For control and maintenance of
    the queue, RTEMS allocates and initializes a QCB.  Memory is allocated from
    the RTEMS Workspace for the specified count of messages, each of
    max_message_size bytes in length.  The RTEMS-assigned queue id, returned in
    id, is used to access the message queue.

    Specifying ``RTEMS_PRIORITY`` in attribute_set causes tasks waiting for a
    message to be serviced according to task priority.  When ``RTEMS_FIFO`` is
    specified, waiting tasks are serviced in First In-First Out order.

NOTES:
    This directive will not cause the calling task to be preempted.

    The following message queue attribute constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_FIFO``
       - tasks wait by FIFO (default)
     * - ``RTEMS_PRIORITY``
       - tasks wait by priority
     * - ``RTEMS_LOCAL``
       - local message queue (default)
     * - ``RTEMS_GLOBAL``
       - global message queue

    Message queues should not be made global unless remote tasks must interact
    with the created message queue.  This is to avoid the system overhead
    incurred by the creation of a global message queue.  When a global message
    queue is created, the message queue's name and id must be transmitted to
    every node in the system for insertion in the local copy of the global
    object table.

    For GLOBAL message queues, the maximum message size is effectively limited
    to the longest message which the MPCI is capable of transmitting.

    The total number of global objects, including message queues, is limited by
    the ``maximum_global_objects`` field in the configuration table.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_ident:

MESSAGE_QUEUE_IDENT - Get ID of a queue
---------------------------------------
.. index:: get ID of a message queue
.. index:: rtems_message_queue_ident

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_ident(
            rtems_name  name,
            uint32_t    node,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - queue identified successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_INVALID_NAME``
       - queue name not found
     * - ``RTEMS_INVALID_NODE``
       - invalid node id

DESCRIPTION:
    This directive obtains the queue id associated with the queue name
    specified in name.  If the queue name is not unique, then the queue id will
    match one of the queues with that name.  However, this queue id is not
    guaranteed to correspond to the desired queue.  The queue id is used with
    other message related directives to access the message queue.

NOTES:
    This directive will not cause the running task to be preempted.

    If node is ``RTEMS_SEARCH_ALL_NODES``, all nodes are searched with the
    local node being searched first.  All other nodes are searched with the
    lowest numbered node searched first.

    If node is a valid node number which does not represent the local node,
    then only the message queues exported by the designated node are searched.

    This directive does not generate activity on remote nodes.  It accesses
    only the local copy of the global object table.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_delete:

MESSAGE_QUEUE_DELETE - Delete a queue
-------------------------------------
.. index:: delete a message queue
.. index:: rtems_message_queue_delete

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - queue deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid queue id
     * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
       - cannot delete remote queue

DESCRIPTION:
    This directive deletes the message queue specified by ``id``.  As a result
    of this directive, all tasks blocked waiting to receive a message from this
    queue will be readied and returned a status code which indicates that the
    message queue was deleted.  If no tasks are waiting, but the queue contains
    messages, then RTEMS returns these message buffers back to the system
    message buffer pool.  The QCB for this queue as well as the memory for the
    message buffers is reclaimed by RTEMS.

NOTES:
    The calling task will be preempted if its preemption mode is enabled and
    one or more local tasks with a higher priority than the calling task are
    waiting on the deleted queue.  The calling task will NOT be preempted if
    the tasks that are waiting are remote tasks.

    The calling task does not have to be the task that created the queue,
    although the task and queue must reside on the same node.

    When the queue is deleted, any messages in the queue are returned to the
    free message buffer pool.  Any information stored in those messages is
    lost.

    When a global message queue is deleted, the message queue id must be
    transmitted to every node in the system for deletion from the local copy of
    the global object table.

    Proxies, used to represent remote tasks, are reclaimed when the message
    queue is deleted.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_send:

MESSAGE_QUEUE_SEND - Put message at rear of a queue
---------------------------------------------------
.. index:: send message to a queue
.. index:: rtems_message_queue_send

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_send(
            rtems_id   id,
            cons void *buffer,
            size_t     size
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - message sent successfully
     * - ``RTEMS_INVALID_ID``
       - invalid queue id
     * - ``RTEMS_INVALID_SIZE``
       - invalid message size
     * - ``RTEMS_INVALID_ADDRESS``
       - ``buffer`` is NULL
     * - ``RTEMS_UNSATISFIED``
       - out of message buffers
     * - ``RTEMS_TOO_MANY``
       - queue's limit has been reached

DESCRIPTION:
    This directive sends the message buffer of size bytes in length to the
    queue specified by id.  If a task is waiting at the queue, then the message
    is copied to the waiting task's buffer and the task is unblocked. If no
    tasks are waiting at the queue, then the message is copied to a message
    buffer which is obtained from this message queue's message buffer pool.
    The message buffer is then placed at the rear of the queue.

NOTES:
    The calling task will be preempted if it has preemption enabled and a
    higher priority task is unblocked as the result of this directive.

    Sending a message to a global message queue which does not reside on the
    local node will generate a request to the remote node to post the message
    on the specified message queue.

    If the task to be unblocked resides on a different node from the message
    queue, then the message is forwarded to the appropriate node, the waiting
    task is unblocked, and the proxy used to represent the task is reclaimed.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_urgent:

MESSAGE_QUEUE_URGENT - Put message at front of a queue
------------------------------------------------------
.. index:: put message at front of queue
.. index:: rtems_message_queue_urgent

**CALLING SEQUENCE:**
    .. code-block:: c

        rtems_status_code rtems_message_queue_urgent(
            rtems_id    id,
            const void *buffer,
            size_t      size
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - message sent successfully
     * - ``RTEMS_INVALID_ID``
       - invalid queue id
     * - ``RTEMS_INVALID_SIZE``
       - invalid message size
     * - ``RTEMS_INVALID_ADDRESS``
       - ``buffer`` is NULL
     * - ``RTEMS_UNSATISFIED``
       - out of message buffers
     * - ``RTEMS_TOO_MANY``
       - queue's limit has been reached

DESCRIPTION:
    This directive sends the message buffer of size bytes in length to the
    queue specified by id.  If a task is waiting on the queue, then the message
    is copied to the task's buffer and the task is unblocked.  If no tasks are
    waiting on the queue, then the message is copied to a message buffer which
    is obtained from this message queue's message buffer pool.  The message
    buffer is then placed at the front of the queue.

NOTES:
    The calling task will be preempted if it has preemption enabled and a
    higher priority task is unblocked as the result of this directive.

    Sending a message to a global message queue which does not reside on the
    local node will generate a request telling the remote node to post the
    message on the specified message queue.

    If the task to be unblocked resides on a different node from the message
    queue, then the message is forwarded to the appropriate node, the waiting
    task is unblocked, and the proxy used to represent the task is reclaimed.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_broadcast:

MESSAGE_QUEUE_BROADCAST - Broadcast N messages to a queue
---------------------------------------------------------
.. index:: broadcast message to a queue
.. index:: rtems_message_queue_broadcast

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_broadcast(
            rtems_id    id,
            const void *buffer,
            size_t      size,
            uint32_t   *count
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - message broadcasted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid queue id
     * - ``RTEMS_INVALID_ADDRESS``
       - ``buffer`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``count`` is NULL
     * - ``RTEMS_INVALID_SIZE``
       - invalid message size

DESCRIPTION:
    This directive causes all tasks that are waiting at the queue specified by
    id to be unblocked and sent the message contained in buffer.  Before a task
    is unblocked, the message buffer of size byes in length is copied to that
    task's message buffer.  The number of tasks that were unblocked is returned
    in count.

NOTES:
    The calling task will be preempted if it has preemption enabled and a
    higher priority task is unblocked as the result of this directive.

    The execution time of this directive is directly related to the number of
    tasks waiting on the message queue, although it is more efficient than the
    equivalent number of invocations of ``rtems_message_queue_send``.

    Broadcasting a message to a global message queue which does not reside on
    the local node will generate a request telling the remote node to broadcast
    the message to the specified message queue.

    When a task is unblocked which resides on a different node from the message
    queue, a copy of the message is forwarded to the appropriate node, the
    waiting task is unblocked, and the proxy used to represent the task is
    reclaimed.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_receive:

MESSAGE_QUEUE_RECEIVE - Receive message from a queue
----------------------------------------------------
.. index:: receive message from a queue
.. index:: rtems_message_queue_receive

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_receive(
            rtems_id        id,
            void           *buffer,
            size_t         *size,
            rtems_option    option_set,
            rtems_interval  timeout
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - message received successfully
     * - ``RTEMS_INVALID_ID``
       - invalid queue id
     * - ``RTEMS_INVALID_ADDRESS``
       - ``buffer`` is NULL
     * - ``RTEMS_INVALID_ADDRESS``
       - ``size`` is NULL
     * - ``RTEMS_UNSATISFIED``
       - queue is empty
     * - ``RTEMS_TIMEOUT``
       - timed out waiting for message
     * - ``RTEMS_OBJECT_WAS_DELETED``
       - queue deleted while waiting

DESCRIPTION:
    This directive receives a message from the message queue specified in id.
    The ``RTEMS_WAIT`` and ``RTEMS_NO_WAIT`` options of the options parameter
    allow the calling task to specify whether to wait for a message to become
    available or return immediately.  For either option, if there is at least
    one message in the queue, then it is copied to buffer, size is set to
    return the length of the message in bytes, and this directive returns
    immediately with a successful return code.  The buffer has to be big enough
    to receive a message of the maximum length with respect to this message
    queue.

    If the calling task chooses to return immediately and the queue is empty,
    then a status code indicating this condition is returned.  If the calling
    task chooses to wait at the message queue and the queue is empty, then the
    calling task is placed on the message wait queue and blocked.  If the queue
    was created with the ``RTEMS_PRIORITY`` option specified, then the calling
    task is inserted into the wait queue according to its priority.  But, if
    the queue was created with the ``RTEMS_FIFO`` option specified, then the
    calling task is placed at the rear of the wait queue.

    A task choosing to wait at the queue can optionally specify a timeout value
    in the timeout parameter.  The timeout parameter specifies the maximum
    interval to wait before the calling task desires to be unblocked.  If it is
    set to ``RTEMS_NO_TIMEOUT``, then the calling task will wait forever.

NOTES:
    The following message receive option constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_WAIT``
       - task will wait for a message (default)
     * - ``RTEMS_NO_WAIT``
       - task should not wait

    Receiving a message from a global message queue which does not reside on
    the local node will generate a request to the remote node to obtain a
    message from the specified message queue.  If no message is available and
    ``RTEMS_WAIT`` was specified, then the task must be blocked until a message
    is posted.  A proxy is allocated on the remote node to represent the task
    until the message is posted.

    A clock tick is required to support the timeout functionality of this
    directive.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_get_number_pending:

MESSAGE_QUEUE_GET_NUMBER_PENDING - Get number of messages pending on a queue
----------------------------------------------------------------------------
.. index:: get number of pending messages
.. index:: rtems_message_queue_get_number_pending

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_get_number_pending(
            rtems_id  id,
            uint32_t *count
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - number of messages pending returned successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``count`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid queue id

DESCRIPTION:
    This directive returns the number of messages pending on this message queue
    in count.  If no messages are present on the queue, count is set to zero.

NOTES:
    Getting the number of pending messages on a global message queue which does
    not reside on the local node will generate a request to the remote node to
    actually obtain the pending message count for the specified message queue.

.. raw:: latex

   \clearpage

.. _rtems_message_queue_flush:

MESSAGE_QUEUE_FLUSH - Flush all messages on a queue
---------------------------------------------------
.. index:: flush messages on a queue
.. index:: rtems_message_queue_flush

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_flush(
            rtems_id  id,
            uint32_t *count
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - message queue flushed successfully
     * - ``RTEMS_INVALID_ADDRESS``
       - ``count`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid queue id

DESCRIPTION:
    This directive removes all pending messages from the specified queue id.
    The number of messages removed is returned in count.  If no messages are
    present on the queue, count is set to zero.

NOTES:
    Flushing all messages on a global message queue which does not reside on
    the local node will generate a request to the remote node to actually flush
    the specified message queue.
