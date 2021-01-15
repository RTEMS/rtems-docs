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

.. Generated from spec:/rtems/message/if/group

.. _MessageManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/message/if/create
.. spec:/rtems/message/if/construct
.. spec:/rtems/message/if/ident
.. spec:/rtems/message/if/delete
.. spec:/rtems/message/if/send
.. spec:/rtems/message/if/urgent
.. spec:/rtems/message/if/broadcast
.. spec:/rtems/message/if/receive
.. spec:/rtems/message/if/get-number-pending
.. spec:/rtems/message/if/flush
.. spec:/rtems/message/if/buffer

The Message Manager provides communication and synchronization capabilities
using RTEMS message queues. The directives provided by the Message Manager are:

* :ref:`InterfaceRtemsMessageQueueCreate` - Creates a message queue.

* :ref:`InterfaceRtemsMessageQueueConstruct` - Constructs a message queue from
  the specified the message queue configuration.

* :ref:`InterfaceRtemsMessageQueueIdent` - Identifies a message queue by the
  object name.

* :ref:`InterfaceRtemsMessageQueueDelete` - Deletes the message queue.

* :ref:`InterfaceRtemsMessageQueueSend` - Puts the message at the rear of the
  queue.

* :ref:`InterfaceRtemsMessageQueueUrgent` - Puts the message at the front of
  the queue.

* :ref:`InterfaceRtemsMessageQueueBroadcast` - Broadcasts the messages to the
  tasks waiting at the queue.

* :ref:`InterfaceRtemsMessageQueueReceive` - Receives a message from the queue.

* :ref:`InterfaceRtemsMessageQueueGetNumberPending` - Gets the number of
  messages pending on the queue.

* :ref:`InterfaceRtemsMessageQueueFlush` - Flushes all messages on the queue.

* :ref:`InterfaceRTEMSMESSAGEQUEUEBUFFER` - Defines a structure which can be
  used as a message queue buffer for messages of the specified maximum size.
