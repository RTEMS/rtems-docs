.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2023 On-Line Applications Research Corporation (OAR)

.. _RegulatorManagerBackground:

Background
==========
The regulator provides facilities to accept bursty input and buffer it
as needed before delivering it at a pre-defined periodic rate. The input
is referred to as the Source, with the output referred to as the
Destination. Messages are accepted from the Source and delivered to
the Destination by a user-provided Delivery function.

The Regulator implementation uses the RTEMS Classic API Partition Manager
to manage the buffer pool and the RTEMS Classic API Message Queue
Manager to send the buffer to the Delivery thread. The Delivery thread
invokes a user-provided delivery function to get the message to the
Destination.

Regulator Buffering
-------------------
The regulator is designed to sit logically between two entities -- a
source and a destination, where it limits the traffic sent to the
destination to prevent it from being flooded with messages from the
source. This can be used to accommodate bursts of input from a source
and meter it out to a destination.  The maximum number of messages
which can be buffered in the regulator is specified by the
``maximum_messages`` field in the :ref:`InterfaceRtemsRegulatorAttributes`
structure passed as an argument to :ref:`InterfaceRtemsRegulatorCreate`.

The regulator library accepts an input stream of messages from a
source and delivers them to a destination. The regulator assumes that the
input stream from the source contains sporadic bursts of data which can
exceed the acceptable rate of the destination. By limiting the message rate,
the regulator prevents an overflow of messages.

The regulator can be configured for the input buffering required to manage
the maximum burst and for the metering rate for the delivery. The delivery
rate is in messages per second. If the sender produces data too fast,
the regulator will buffer the configured number of messages.

A configuration capability is provided to allow for adaptation to different
message streams. The regulator can also support running multiple instances,
which could be used on independent message streams.

It is assumed that the application has a design limit on the number of
messages which may be buffered. All messages accepted by the regulator,
assuming no overflow on input, will eventually be output by the Delivery
thread.

Message Delivery Rate
---------------------

The Source sends buffers to the Regulator instance. The Regulator
then sends the buffer via a message queue which delivers them to the
Delivery thread.  The Delivery thread executes periodically at a rate
specified by the ``delivery_thread_period`` field in the
:ref:`InterfaceRtemsRegulatorAttributes` structure passed as an argument
to :ref:`InterfaceRtemsRegulatorCreate`.

During each period, the Delivery thread attempts to receive
up to ``maximum_to_dequeue_per_period`` number of buffers and
invoke the Delivery function to deliver each of them to the
Destination. The ``maximum_to_dequeue_per_period`` field in the
:ref:`InterfaceRtemsRegulatorAttributes` structure passed as an argument
to :ref:`InterfaceRtemsRegulatorCreate`.

For example, consider a Source that may produce a burst of up to seven
messages every five seconds. But the Destination cannot handle a burst
of seven and either drops messages or gives an error. This can be
accommodated by a Regulator instance configured as follows:

* ``maximum_messages`` - 7
* ``delivery_thread_period`` - one second
* ``maximum_to_dequeue_per_period`` - 3

In this scenario, the application will use the Delivery thread
:ref:`InterfaceRtemsRegulatorSend` to enqueue the seven messages when they
arrive. The Delivery thread will deliver three messages per second. The
following illustrates this sequence:

* Time 0: Source sends seven messages
* Time 1: Delivery of messages 1 to 3
* Time 3: Delivery of messages 4 to 6
* Time 3: Delivery of message 7
* Time 4: No messages to deliver

This configuration of the regulator ensures that the Destination does
not overflow.
