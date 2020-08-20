.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

.. index:: message queue attributes

Building a Message Queue Attribute Set
--------------------------------------

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
