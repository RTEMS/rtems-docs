.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. _MessageManagerDirectives:

Directives
==========

This section details the directives of the Message Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/message/if/create

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_create()
.. index:: create a message queue

.. _InterfaceRtemsMessageQueueCreate:

rtems_message_queue_create()
----------------------------

Creates a message queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_create(
      rtems_name      name,
      uint32_t        count,
      size_t          max_message_size,
      rtems_attribute attribute_set,
      rtems_id       *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name of the message queue.

``count``
    This parameter is the maximum count of pending messages supported by the
    message queue.

``max_message_size``
    This parameter is the maximum size in bytes of a message supported by the
    message queue.

``attribute_set``
    This parameter is the attribute set of the message queue.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the identifier of the created message queue
    will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive creates a message queue which resides on the local node.  The
message queue has the user-defined object name specified in ``name``.  Memory
is allocated from the RTEMS Workspace for the count of messages specified in
``count``, each of ``max_message_size`` bytes in length.  The assigned object
identifier is returned in ``id``.  This identifier is used to access the
message queue with other message queue related directives.

The **attribute set** specified in ``attribute_set`` is built through a
*bitwise or* of the attribute constants described below.  Not all combinations
of attributes are allowed.  Some attributes are mutually exclusive.  If
mutually exclusive attributes are combined, the behaviour is undefined.
Attributes not mentioned below are not evaluated by this directive and have no
effect.  Default attributes can be selected by using the
:c:macro:`RTEMS_DEFAULT_ATTRIBUTES` constant.  The attribute set defines

* the scope of the message queue: :c:macro:`RTEMS_LOCAL` (default) or
  :c:macro:`RTEMS_GLOBAL` and

* the task wait queue discipline used by the message queue:
  :c:macro:`RTEMS_FIFO` (default) or :c:macro:`RTEMS_PRIORITY`.

The message queue has a local or global **scope** in a multiprocessing network
(this attribute does not refer to SMP systems).  The scope is selected by the
mutually exclusive :c:macro:`RTEMS_LOCAL` and :c:macro:`RTEMS_GLOBAL`
attributes.

* A **local scope** is the default and can be emphasized through the use of the
  :c:macro:`RTEMS_LOCAL` attribute.  A local message queue can be only used by
  the node which created it.

* A **global scope** is established if the :c:macro:`RTEMS_GLOBAL` attribute is
  set.  Setting the global attribute in a single node system has no effect.

The **task wait queue discipline** is selected by the mutually exclusive
:c:macro:`RTEMS_FIFO` and :c:macro:`RTEMS_PRIORITY` attributes. The discipline
defines the order in which tasks wait for a message to receive on a currently
empty message queue.

* The **FIFO discipline** is the default and can be emphasized through use of
  the :c:macro:`RTEMS_FIFO` attribute.

* The **priority discipline** is selected by the :c:macro:`RTEMS_PRIORITY`
  attribute.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NUMBER`
    The ``count`` parameter was invalid.

:c:macro:`RTEMS_INVALID_SIZE`
    The ``max_message_size`` parameter was invalid.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive object available to create a message queue.  The
    number of message queue available to the application is configured through
    the :ref:`CONFIGURE_MAXIMUM_MESSAGE_QUEUES` application configuration
    option.

:c:macro:`RTEMS_TOO_MANY`
    In multiprocessing configurations, there was no inactive global object
    available to create a global message queue.  The number of global objects
    available to the application is configured through the
    :ref:`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application configuration
    option.

:c:macro:`RTEMS_INVALID_NUMBER`
    The product of ``count`` and ``max_message_size`` is greater than the
    maximum storage size.

:c:macro:`RTEMS_UNSATISFIED`
    There was not enough memory available in the RTEMS Workspace to allocate
    the message buffers for the message queue.

.. rubric:: NOTES:

For message queues with a global scope, the maximum message size is effectively
limited to the longest message which the :term:`MPCI` is capable of
transmitting.

For control and maintenance of the message queue, RTEMS allocates a :term:`QCB`
from the local QCB free pool and initializes it.

The QCB for a global message queue is allocated on the local node.  Message
queues should not be made global unless remote tasks must interact with the
message queue.  This is to avoid the system overhead incurred by the creation
of a global message queue.  When a global message queue is created, the message
queue's name and identifier must be transmitted to every node in the system for
insertion in the local copy of the global object table.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* When the directive operates on a global object, the directive sends a message
  to remote nodes.  This may preempt the calling task.

* The number of message queues available to the application is configured
  through the :ref:`CONFIGURE_MAXIMUM_MESSAGE_QUEUES` application configuration
  option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

* The number of global objects available to the application is configured
  through the :ref:`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application
  configuration option.

.. Generated from spec:/rtems/message/if/construct

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_construct()

.. _InterfaceRtemsMessageQueueConstruct:

rtems_message_queue_construct()
-------------------------------

Constructs a message queue from the specified the message queue configuration.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_construct(
      const rtems_message_queue_config *config,
      rtems_id                         *id
    );

.. rubric:: PARAMETERS:

``config``
    This parameter is the message queue configuration.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the identifier of the constructed message
    queue will be stored in this variable.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``config`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NAME`
    The message queue name in the configuration was invalid.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NUMBER`
    The maximum number of pending messages in the configuration was zero.

:c:macro:`RTEMS_INVALID_SIZE`
    The maximum message size in the configuration was zero.

:c:macro:`RTEMS_TOO_MANY`
    There was no inactive message queue object available to construct a message
    queue.

:c:macro:`RTEMS_TOO_MANY`
    In multiprocessing configurations, there was no inactive global object
    available to construct a global message queue.

:c:macro:`RTEMS_INVALID_SIZE`
    The maximum message size in the configuration was too big and resulted in
    integer overflows in calculations carried out to determine the size of the
    message buffer area.

:c:macro:`RTEMS_INVALID_NUMBER`
    The maximum number of pending messages in the configuration was too big and
    resulted in integer overflows in calculations carried out to determine the
    size of the message buffer area.

:c:macro:`RTEMS_UNSATISFIED`
    The message queue storage area begin pointer in the configuration was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_UNSATISFIED`
    The message queue storage area size in the configuration was not equal to
    the size calculated from the maximum number of pending messages and the
    maximum message size.

.. rubric:: NOTES:

In contrast to message queues created by
:ref:`InterfaceRtemsMessageQueueCreate`, the message queues constructed by this
directive use a user-provided message buffer storage area.

This directive is intended for applications which do not want to use the RTEMS
Workspace and instead statically allocate all operating system resources.  An
application based solely on static allocation can avoid any runtime memory
allocators.  This can simplify the application architecture as well as any
analysis that may be required.

The value for :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY` should not include memory
for message queues constructed by :ref:`InterfaceRtemsMessageQueueConstruct`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* When the directive operates on a global object, the directive sends a message
  to remote nodes.  This may preempt the calling task.

* The number of message queues available to the application is configured
  through the :ref:`CONFIGURE_MAXIMUM_MESSAGE_QUEUES` application configuration
  option.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

* The number of global objects available to the application is configured
  through the :ref:`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application
  configuration option.

.. Generated from spec:/rtems/message/if/ident

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_ident()

.. _InterfaceRtemsMessageQueueIdent:

rtems_message_queue_ident()
---------------------------

Identifies a message queue by the object name.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_ident(
      rtems_name name,
      uint32_t   node,
      rtems_id  *id
    );

.. rubric:: PARAMETERS:

``name``
    This parameter is the object name to look up.

``node``
    This parameter is the node or node set to search for a matching object.

``id``
    This parameter is the pointer to an object identifier variable.  When the
    directive call is successful, the object identifier of an object with the
    specified name will be stored in this variable.

.. rubric:: DESCRIPTION:

This directive obtains a message queue identifier associated with the message
queue name specified in ``name``.

The node to search is specified in ``node``.  It shall be

* a valid node number,

* the constant :c:macro:`RTEMS_SEARCH_ALL_NODES` to search in all nodes,

* the constant :c:macro:`RTEMS_SEARCH_LOCAL_NODE` to search in the local node
  only, or

* the constant :c:macro:`RTEMS_SEARCH_OTHER_NODES` to search in all nodes
  except the local node.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``id`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_NAME`
    The ``name`` parameter was 0.

:c:macro:`RTEMS_INVALID_NAME`
    There was no object with the specified name on the specified nodes.

:c:macro:`RTEMS_INVALID_NODE`
    In multiprocessing configurations, the specified node was invalid.

.. rubric:: NOTES:

If the message queue name is not unique, then the message queue identifier will
match the first message queue with that name in the search order. However, this
message queue identifier is not guaranteed to correspond to the desired message
queue.

The objects are searched from lowest to the highest index.  If ``node`` is
:c:macro:`RTEMS_SEARCH_ALL_NODES`, all nodes are searched with the local node
being searched first.  All other nodes are searched from lowest to the highest
node number.

If node is a valid node number which does not represent the local node, then
only the message queues exported by the designated node are searched.

This directive does not generate activity on remote nodes.  It accesses only
the local copy of the global object table.

The message queue identifier is used with other message related directives to
access the message queue.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/message/if/delete

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_delete()
.. index:: delete a message queue

.. _InterfaceRtemsMessageQueueDelete:

rtems_message_queue_delete()
----------------------------

Deletes the message queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_delete( rtems_id id );

.. rubric:: PARAMETERS:

``id``
    This parameter is the message queue identifier.

.. rubric:: DESCRIPTION:

This directive deletes the message queue specified by ``id``. As a result of
this directive, all tasks blocked waiting to receive a message from this queue
will be readied and returned a status code which indicates that the message
queue was deleted.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no message queue associated with the identifier specified by
    ``id``.

:c:macro:`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`
    The message queue resided on a remote node.

.. rubric:: NOTES:

When the message queue is deleted, any messages in the queue are returned to
the free message buffer pool.  Any information stored in those messages is
lost.  The message buffers allocated for the message queue are reclaimed.

The :term:`QCB` for the deleted message queue is reclaimed by RTEMS.

When a global message queue is deleted, the message queue identifier must be
transmitted to every node in the system for deletion from the local copy of the
global object table.

The message queue must reside on the local node, even if the message queue was
created with the :c:macro:`RTEMS_GLOBAL` attribute.

Proxies, used to represent remote tasks, are reclaimed when the message queue
is deleted.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.

* When the directive operates on a global object, the directive sends a message
  to remote nodes.  This may preempt the calling task.

* The calling task does not have to be the task that created the object.  Any
  local task that knows the object identifier can delete the object.

* Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

.. Generated from spec:/rtems/message/if/send

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_send()
.. index:: send message to a queue

.. _InterfaceRtemsMessageQueueSend:

rtems_message_queue_send()
--------------------------

Puts the message at the rear of the queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_send(
      rtems_id    id,
      const void *buffer,
      size_t      size
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the queue identifier.

``buffer``
    This parameter is the begin address of the message buffer to send.

``size``
    This parameter is the size in bytes of the message buffer to send.

.. rubric:: DESCRIPTION:

This directive sends the message ``buffer`` of ``size`` bytes in length to the
queue specified by ``id``.  If a task is waiting at the queue, then the message
is copied to the waiting task's buffer and the task is unblocked. If no tasks
are waiting at the queue, then the message is copied to a message buffer which
is obtained from this message queue's message buffer pool.  The message buffer
is then placed at the rear of the queue.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no queue associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``buffer`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_SIZE`
    The size of the message exceeded the maximum message size of the queue as
    defined by :ref:`InterfaceRtemsMessageQueueCreate` or
    :ref:`InterfaceRtemsMessageQueueConstruct`.

:c:macro:`RTEMS_TOO_MANY`
    The maximum number of pending messages supported by the queue as defined by
    :ref:`InterfaceRtemsMessageQueueCreate` or
    :ref:`InterfaceRtemsMessageQueueConstruct` has been reached.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The directive may be called from within interrupt context.

* The directive may unblock a task.  This may cause the calling task to be
  preempted.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/message/if/urgent

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_urgent()
.. index:: put message at front of queue

.. _InterfaceRtemsMessageQueueUrgent:

rtems_message_queue_urgent()
----------------------------

Puts the message at the front of the queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_urgent(
      rtems_id    id,
      const void *buffer,
      size_t      size
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the queue identifier.

``buffer``
    This parameter is the begin address of the message buffer to send urgently.

``size``
    This parameter is the size in bytes of the message buffer to send urgently.

.. rubric:: DESCRIPTION:

This directive sends the message ``buffer`` of ``size`` bytes in length to the
queue specified by ``id``.  If a task is waiting at the queue, then the message
is copied to the waiting task's buffer and the task is unblocked. If no tasks
are waiting at the queue, then the message is copied to a message buffer which
is obtained from this message queue's message buffer pool.  The message buffer
is then placed at the front of the queue.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no queue associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``buffer`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_SIZE`
    The size of the message exceeded the maximum message size of the queue as
    defined by :ref:`InterfaceRtemsMessageQueueCreate` or
    :ref:`InterfaceRtemsMessageQueueConstruct`.

:c:macro:`RTEMS_TOO_MANY`
    The maximum number of pending messages supported by the queue as defined by
    :ref:`InterfaceRtemsMessageQueueCreate` or
    :ref:`InterfaceRtemsMessageQueueConstruct` has been reached.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The directive may be called from within interrupt context.

* The directive may unblock a task.  This may cause the calling task to be
  preempted.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/message/if/broadcast

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_broadcast()
.. index:: broadcast message to a queue

.. _InterfaceRtemsMessageQueueBroadcast:

rtems_message_queue_broadcast()
-------------------------------

Broadcasts the messages to the tasks waiting at the queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_broadcast(
      rtems_id    id,
      const void *buffer,
      size_t      size,
      uint32_t   *count
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the queue identifier.

``buffer``
    This parameter is the begin address of the message buffer to broadcast.

``size``
    This parameter is the size in bytes of the message buffer to broadcast.

``count``
    This parameter is the pointer to an `uint32_t
    <https://en.cppreference.com/w/c/types/integer>`_ variable.  When the
    directive call is successful, the number of unblocked tasks will be stored
    in this variable.

.. rubric:: DESCRIPTION:

This directive causes all tasks that are waiting at the queue specified by
``id`` to be unblocked and sent the message contained in ``buffer``.  Before a
task is unblocked, the message ``buffer`` of ``size`` byes in length is copied
to that task's message buffer.  The number of tasks that were unblocked is
returned in ``count``.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no queue associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``buffer`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``count`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_SIZE`
    The size of the message exceeded the maximum message size of the queue as
    defined by :ref:`InterfaceRtemsMessageQueueCreate` or
    :ref:`InterfaceRtemsMessageQueueConstruct`.

.. rubric:: NOTES:

The execution time of this directive is directly related to the number of tasks
waiting on the message queue, although it is more efficient than the equivalent
number of invocations of :ref:`InterfaceRtemsMessageQueueSend`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The directive may be called from within interrupt context.

* The directive may unblock a task.  This may cause the calling task to be
  preempted.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/message/if/receive

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_receive()
.. index:: receive message from a queue

.. _InterfaceRtemsMessageQueueReceive:

rtems_message_queue_receive()
-----------------------------

Receives a message from the queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_receive(
      rtems_id       id,
      void          *buffer,
      size_t        *size,
      rtems_option   option_set,
      rtems_interval timeout
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the queue identifier.

``buffer``
    This parameter is the begin address of the buffer to receive the message.
    The buffer shall be large enough to receive a message of the maximum length
    of the queue as defined by :ref:`InterfaceRtemsMessageQueueCreate` or
    :ref:`InterfaceRtemsMessageQueueConstruct`.  The ``size`` parameter cannot
    be used to specify the size of the buffer.

``size``
    This parameter is the pointer to a `size_t
    <https://en.cppreference.com/w/c/types/size_t>`_ variable.  When the
    directive call is successful, the size in bytes of the received messages
    will be stored in this variable.  This parameter cannot be used to specify
    the size of the buffer.

``option_set``
    This parameter is the option set.

``timeout``
    This parameter is the timeout in :term:`clock ticks <clock tick>` if the
    :c:macro:`RTEMS_WAIT` option is set.  Use :c:macro:`RTEMS_NO_TIMEOUT` to
    wait potentially forever.

.. rubric:: DESCRIPTION:

This directive receives a message from the queue specified by ``id``.

The **option set** specified in ``option_set`` is built through a *bitwise or*
of the option constants described below.  Not all combinations of options are
allowed.  Some options are mutually exclusive.  If mutually exclusive options
are combined, the behaviour is undefined.  Options not mentioned below are not
evaluated by this directive and have no effect. Default options can be selected
by using the :c:macro:`RTEMS_DEFAULT_OPTIONS` constant.

The calling task can **wait** or **try to receive** a message from the queue
according to the mutually exclusive :c:macro:`RTEMS_WAIT` and
:c:macro:`RTEMS_NO_WAIT` options.

* **Waiting to receive** a message from the queue is the default and can be
  emphasized through the use of the :c:macro:`RTEMS_WAIT` option. The
  ``timeout`` parameter defines how long the calling task is willing to wait.
  Use :c:macro:`RTEMS_NO_TIMEOUT` to wait potentially forever, otherwise set a
  timeout interval in clock ticks.

* **Trying to receive** a message from the queue is selected by the
  :c:macro:`RTEMS_NO_WAIT` option.  If this option is defined, then the
  ``timeout`` parameter is ignored.  When a message from the queue cannot be
  immediately received, then the :c:macro:`RTEMS_UNSATISFIED` status is
  returned.

With either :c:macro:`RTEMS_WAIT` or :c:macro:`RTEMS_NO_WAIT` if there is at
least one message in the queue, then it is copied to the buffer, the size is
set to return the length of the message in bytes, and this directive returns
immediately with the :c:macro:`RTEMS_SUCCESSFUL` status code.  The buffer has
to be big enough to receive a message of the maximum length with respect to
this message queue.

If the calling task chooses to return immediately and the queue is empty, then
the directive returns immediately with the :c:macro:`RTEMS_UNSATISFIED` status
cod.  If the calling task chooses to wait at the message queue and the queue is
empty, then the calling task is placed on the message wait queue and blocked.
If the queue was created with the :c:macro:`RTEMS_PRIORITY` option specified,
then the calling task is inserted into the wait queue according to its
priority.  But, if the queue was created with the :c:macro:`RTEMS_FIFO` option
specified, then the calling task is placed at the rear of the wait queue.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no queue associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``buffer`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``size`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_UNSATISFIED`
    The queue was empty.

:c:macro:`RTEMS_UNSATISFIED`
    The queue was flushed while the calling task was waiting to receive a
    message.

:c:macro:`RTEMS_TIMEOUT`
    The timeout happened while the calling task was waiting to receive a
    message

:c:macro:`RTEMS_OBJECT_WAS_DELETED`
    The queue was deleted while the calling task was waiting to receive a
    message.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* When a local queue is accessed and the :c:macro:`RTEMS_NO_WAIT` option is
  set, the directive may be called from within interrupt context.

* The directive may be called from within task context.

* When the request cannot be immediately satisfied and the
  :c:macro:`RTEMS_WAIT` option is set, the calling task blocks at some point
  during the directive call.

* The timeout functionality of the directive requires a :term:`clock tick`.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/message/if/get-number-pending

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_get_number_pending()
.. index:: get number of pending messages

.. _InterfaceRtemsMessageQueueGetNumberPending:

rtems_message_queue_get_number_pending()
----------------------------------------

Gets the number of messages pending on the queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_get_number_pending(
      rtems_id  id,
      uint32_t *count
    );

.. rubric:: PARAMETERS:

``id``
    This parameter is the queue identifier.

``count``
    This parameter is the pointer to an `uint32_t
    <https://en.cppreference.com/w/c/types/integer>`_ variable.  When the
    directive call is successful, the number of pending messages will be stored
    in this variable.

.. rubric:: DESCRIPTION:

This directive returns the number of messages pending on the queue specified by
``id`` in ``count``.  If no messages are present on the queue, count is set to
zero.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no queue associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``count`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The directive may be called from within interrupt context.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/message/if/flush

.. raw:: latex

    \clearpage

.. index:: rtems_message_queue_flush()
.. index:: flush messages on a queue

.. _InterfaceRtemsMessageQueueFlush:

rtems_message_queue_flush()
---------------------------

Flushes all messages on the queue.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_message_queue_flush( rtems_id id, uint32_t *count );

.. rubric:: PARAMETERS:

``id``
    This parameter is the queue identifier.

``count``
    This parameter is the pointer to an `uint32_t
    <https://en.cppreference.com/w/c/types/integer>`_ variable.  When the
    directive call is successful, the number of unblocked tasks will be stored
    in this variable.

.. rubric:: DESCRIPTION:

This directive removes all pending messages from the queue specified by ``id``.
The number of messages removed is returned in ``count``.  If no messages are
present on the queue, count is set to zero.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_ID`
    There was no queue associated with the identifier specified by ``id``.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``count`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within task context.

* The directive may be called from within interrupt context.

* When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply.  This will preempt the calling
  task.

.. Generated from spec:/rtems/message/if/buffer

.. raw:: latex

    \clearpage

.. index:: RTEMS_MESSAGE_QUEUE_BUFFER()

.. _InterfaceRTEMSMESSAGEQUEUEBUFFER:

RTEMS_MESSAGE_QUEUE_BUFFER()
----------------------------

Defines a structure which can be used as a message queue buffer for messages of
the specified maximum size.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define RTEMS_MESSAGE_QUEUE_BUFFER( maximum_message_size )

.. rubric:: PARAMETERS:

``maximum_message_size``
    This parameter is the maximum message size in bytes.

.. rubric:: NOTES:

Use this macro to define the message buffer storage area for
:ref:`InterfaceRtemsMessageQueueConstruct`.
