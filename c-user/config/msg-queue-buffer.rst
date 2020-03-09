.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Message Queue Buffer Configuration
==================================

This section describes the configuration parameters related to specifying the
amount of memory reserved for message queue message buffers.  See
:ref:`CONFIGURE_MAXIMUM_MESSAGE_QUEUES` and
:ref:`CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES`.

.. index:: CONFIGURE_MESSAGE_BUFFER_MEMORY
.. index:: configure message queue buffer memory

.. _CONFIGURE_MESSAGE_BUFFER_MEMORY:

CONFIGURE_MESSAGE_BUFFER_MEMORY
-------------------------------

CONSTANT:
    ``CONFIGURE_MESSAGE_BUFFER_MEMORY``

DATA TYPE:
    integer summation macro

RANGE:
    undefined (zero) or calculation resulting in a positive integer

DEFAULT VALUE:
    This is not defined by default, and zero (0) memory is reserved.

DESCRIPTION:
    This macro is set to the number of bytes the application requires to be
    reserved for pending Classic API Message Queue buffers.

NOTES:
    The following illustrates how the help macro
    :ref:`CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE` can be used to assist in
    calculating the message buffer memory required.  In this example, there are
    two message queues used in this application.  The first message queue has
    maximum of 24 pending messages with the message structure defined by the
    type ``one_message_type``.  The other message queue has maximum of 500
    pending messages with the message structure defined by the type
    ``other_message_type``.

    .. code-block:: c

        #define CONFIGURE_MESSAGE_BUFFER_MEMORY \
                    (CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE( \
                         24, sizeof(one_message_type) \
                     ) + \
                     CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE( \
                         500, sizeof(other_message_type) \
                     )

.. index:: CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE
.. index:: memory for a single message queue's buffers

.. _CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE:

CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE
-----------------------------------

CONSTANT:
    ``CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE(max_messages, size_per)``

DATA TYPE:
    Unsigned integer (``size_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is None.

DESCRIPTION:
    This is a helper macro which is used to assist in computing the total
    amount of memory required for message buffers.  Each message queue will
    have its own configuration with maximum message size and maximum number of
    pending messages.

    The interface for this macro is as follows:

    .. code-block:: c

        CONFIGURE_MESSAGE_BUFFERS_FOR_QUEUE(max_messages, size_per)

    Where ``max_messages`` is the maximum number of pending messages and
    ``size_per`` is the size in bytes of the user message.

NOTES:
    This macro is only used in support of :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.
