.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _EventRecording:

Event Recording
===============

The `event recording` support focuses on the recording of high frequency
events such as

     * thread switches,
     * thread queue enqueue and surrender,
     * interrupt entry and exit,
     * heap/workspace memory allocate/free,
     * UMA zone allocate/free,
     * Ethernet packet input/output, and
     * etc.

There is a fixed set of 512 system reserved and 512 user defined events which
are identified by an event number (:c:type:`rtems_record_event`).

The event recording support allows post-mortem analysis in fatal error
handlers, e.g. the last events are in the record buffers, the newest event
overwrites the oldest event.  It is possible to detect record buffer overflows
for consumers that expect a continuous stream of events, e.g. to display the
system state changes in real-time.

The implementation supports high-end SMP machines (more than 1GHz processor
frequency, more than four processors).  It uses per-processor ring buffers to
record the events.  Synchronization is done without atomic read-modify-write
operations.  The CPU counter is used to get the time of events. It is combined
with periodic uptime events to synchronize it with the monotonic system clock
(:c:macro:`CLOCK_MONOTONIC`).

The application must configure the event recording via the configuration options
:c:macro:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` and
:c:macro:`CONFIGURE_RECORD_EXTENSIONS_ENABLED`.

Events can be recorded for example with the :c:func:`rtems_record_produce`
function.

.. code-block:: c

    #include <rtems/record.h>

    void f( void )
    {
      rtems_record_produce( RTEMS_RECORD_USER( 0 ), 123 );
    }

Recorded events can be sent to a host computer with a very simple record server
started by :c:func:`rtems_record_start_server` via a TCP connection.

On the host computer you may use the command line tool :file:`rtems-record` to
get recorded events from the record server running on the target system.
