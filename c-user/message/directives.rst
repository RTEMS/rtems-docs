.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the message manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create a message queue
.. index:: rtems_message_queue_create

.. _rtems_message_queue_create:

MESSAGE_QUEUE_CREATE - Create a queue
-------------------------------------

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

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

.. index:: get ID of a message queue
.. index:: rtems_message_queue_ident

.. _rtems_message_queue_ident:

MESSAGE_QUEUE_IDENT - Get ID of a queue
---------------------------------------

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

.. index:: delete a message queue
.. index:: rtems_message_queue_delete

.. _rtems_message_queue_delete:

MESSAGE_QUEUE_DELETE - Delete a queue
-------------------------------------

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

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

.. index:: send message to a queue
.. index:: rtems_message_queue_send

.. _rtems_message_queue_send:

MESSAGE_QUEUE_SEND - Put message at rear of a queue
---------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_message_queue_send(
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

.. index:: put message at front of queue
.. index:: rtems_message_queue_urgent

.. _rtems_message_queue_urgent:

MESSAGE_QUEUE_URGENT - Put message at front of a queue
------------------------------------------------------

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

.. index:: broadcast message to a queue
.. index:: rtems_message_queue_broadcast

.. _rtems_message_queue_broadcast:

MESSAGE_QUEUE_BROADCAST - Broadcast N messages to a queue
---------------------------------------------------------

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

.. index:: receive message from a queue
.. index:: rtems_message_queue_receive

.. _rtems_message_queue_receive:

MESSAGE_QUEUE_RECEIVE - Receive message from a queue
----------------------------------------------------

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

.. index:: get number of pending messages
.. index:: rtems_message_queue_get_number_pending

.. _rtems_message_queue_get_number_pending:

MESSAGE_QUEUE_GET_NUMBER_PENDING - Get number of messages pending on a queue
----------------------------------------------------------------------------

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

.. index:: flush messages on a queue
.. index:: rtems_message_queue_flush

.. _rtems_message_queue_flush:

MESSAGE_QUEUE_FLUSH - Flush all messages on a queue
---------------------------------------------------

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
