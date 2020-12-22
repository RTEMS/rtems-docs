.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH
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

To use the event recording three things come into play. Firstly, there is the
generation of event records on the target system (the application running with
RTEMS).  Secondly, means to transfer the recorded events to the host computer
for analysis.  Thirdly, the analysis of the recorded events on the host
computer.

Target System: Configuration and Event Generation
-------------------------------------------------

The application enables the event recording support via the configuration
option :c:macro:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS`.  The configuration
option :c:macro:`CONFIGURE_RECORD_EXTENSIONS_ENABLED` enables the generation of
thread create, start, restart, delete, switch, begin, exitted and terminate
events.  Dumps of the event records in a fatal error handler can be enabled by
the mutually exclusive :c:macro:`CONFIGURE_RECORD_FATAL_DUMP_BASE64` and
:c:macro:`CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB` configuration options.

Custom events can be recorded for example with the
:c:func:`rtems_record_produce`, :c:func:`rtems_record_line`,
:c:func:`rtems_record_caller`, etc. functions.

.. code-block:: c

    #include <rtems/record.h>

    void f( void )
    {
      rtems_record_produce( RTEMS_RECORD_USER( 0 ), 123 );
      rtems_record_line();
      rtems_record_caller();
    }

The variants of :c:func:`rtems_record_line` and :c:func:`rtems_record_caller`
can be used to easily generate control flow events in the area of interest.
The :file:`rtems-record-lttng` tool can use these events to associate source
code files and line numbers to them using the ELF file of the application.

The following code can be used together with the GCC option
``-finstrument-functions`` to generate function entry/exit events for
instrumented functions:

.. code-block:: c

   __attribute__(( __no_instrument_function__ ))
   void __cyg_profile_func_enter( void *this_fn, void *call_site )
   {
     rtems_record_produce_2(
       RTEMS_RECORD_CALLER,
       (rtems_record_data) call_site,
       RTEMS_RECORD_FUNCTION_ENTRY,
       (rtems_record_data) this_fn
     );
   }

   __attribute__(( __no_instrument_function__ ))
   void __cyg_profile_func_exit( void *this_fn, void *call_site )
   {
     rtems_record_produce(
       RTEMS_RECORD_FUNCTION_EXIT,
       (rtems_record_data) this_fn
     );
   }

To generate interrupt handler entry/exit events, the following patch can be
used:

.. code-block:: diff

    diff --git a/bsps/arm/shared/clock/clock-armv7m.c b/bsps/arm/shared/clock/clock-armv7m.c
    index 255de1ca42..0d37c63ac6 100644
    --- a/bsps/arm/shared/clock/clock-armv7m.c
    +++ b/bsps/arm/shared/clock/clock-armv7m.c
    @@ -29,6 +29,7 @@
     #include <bsp/clock-armv7m.h>

     #include <rtems.h>
    +#include <rtems/record.h>
     #include <rtems/sysinit.h>

     #ifdef ARM_MULTILIB_ARCH_V7M
    @@ -45,9 +46,11 @@ static uint32_t _ARMV7M_TC_get_timecount(struct timecounter *base)

     void _ARMV7M_Clock_handler(void)
     {
    +  rtems_record_produce(RTEMS_RECORD_INTERRUPT_ENTRY, ARMV7M_VECTOR_SYSTICK);
       _ARMV7M_Interrupt_service_enter();
       Clock_isr(NULL);
       _ARMV7M_Interrupt_service_leave();
    +  rtems_record_produce(RTEMS_RECORD_INTERRUPT_EXIT, ARMV7M_VECTOR_SYSTICK);
     }

     static void _ARMV7M_Clock_handler_install(void)
    diff --git a/bsps/include/bsp/irq-generic.h b/bsps/include/bsp/irq-generic.h
    index 31835d07ba..2ab2f78b65 100644
    --- a/bsps/include/bsp/irq-generic.h
    +++ b/bsps/include/bsp/irq-generic.h
    @@ -30,6 +30,7 @@
     #include <stdbool.h>

     #include <rtems/irq-extension.h>
    +#include <rtems/record.h>
     #include <rtems/score/assert.h>

     #ifdef RTEMS_SMP
    @@ -258,6 +259,7 @@ void bsp_interrupt_vector_disable(rtems_vector_number vector);
      */
     static inline void bsp_interrupt_handler_dispatch(rtems_vector_number vector)
     {
    +  rtems_record_produce(RTEMS_RECORD_INTERRUPT_ENTRY, vector);
       if (bsp_interrupt_is_valid_vector(vector)) {
         const bsp_interrupt_handler_entry *e =
           &bsp_interrupt_handler_table [bsp_interrupt_handler_index(vector)];
    @@ -276,6 +278,7 @@ static inline void bsp_interrupt_handler_dispatch(rtems_vector_number vector)
       } else {
         bsp_interrupt_handler_default(vector);
       }
    +  rtems_record_produce(RTEMS_RECORD_INTERRUPT_EXIT, vector);
     }

     /**

Transfer of Event Records to the Host Computer
----------------------------------------------

Recorded events can be sent to a host computer with a record server started by
:c:func:`rtems_record_start_server` via a TCP connection.

In the fatal error handler, the event records can be dumped via
:c:func:`rtems_putc` in Base64 encoding.  Optionally, the event records can be
compressed via zlib before they are dumped in Base64 encoding.  The compression
needs roughly 512KiB of statically allocated memory.

Analysis of Event Records on the Host Computer
----------------------------------------------

Use the command line tool :file:`rtems-record-lttng` to get recorded events
from the record server running on the target system or from a file to convert
the event records into CTF.  It can be also used to read the dumps in Base64
encoding generated by the fatal error handler.  The tool outputs the event
records in the `Common Trace Format (CTF) <https://diamon.org/ctf/>`_ with some
extra support for the
`Linux Trace Toolkit Next Generation (LTTng) <https://lttng.org/>`_.  This
format can be analysed using `babeltrace <https://babeltrace.org/>`_ or
`Eclipse Trace Compass <https://www.eclipse.org/tracecompass/>`_.
The command line tool :file:`rtems-record-lttng` optionally uses
`LLVM <https://www.llvm.org/>`_ to translate addresses to functions and source
file locations.  Make sure you have the LLVM development package installed when
you build the RTEMS Tools to enable this feature.

For example, to get the event records from the record server running on the
target use:

.. code-block:: none

    mkdir new-trace
    cd new-trace
    rtems-record-lttng -e application.exe -H 192.168.188.84 -l 100000

If everything is set up correctly, then the command produces a :file:`metadata`
file and one stream file :file:`stream_0`, etc. for each processor which
generated event records.

.. code-block:: none

    $ ls -l
    total 120
    -rw-r--r-- 1 user group 108339 Apr 11 15:28 metadata
    -rw-r--r-- 1 user group   8701 Apr 11 15:28 stream_0

This output in CTF can be used by :file:`babeltrace` and
`Eclipse Trace Compass` for further analysis, for example:

.. code-block:: none

    $ babeltrace .
    [07:28:15.909340000] (+?.?????????) RTEMS THREAD_STACK_CURRENT: { cpu_id = 0 }, { data = 0xB10 }
    [07:28:15.909340000] (+0.000000000) RTEMS sched_switch: { cpu_id = 0 }, { prev_comm = "UI1 ", prev_tid = 167837697, prev_prio = 0, prev_state = 0, next_comm = "IDLE/0", next_tid = 0, next_prio = 0 }
    [07:28:15.909519999] (+0.000179999) RTEMS THREAD_STACK_CURRENT: { cpu_id = 0 }, { data = 0xD68 }
    [07:28:15.909519999] (+0.000000000) RTEMS sched_switch: { cpu_id = 0 }, { prev_comm = "IDLE/0", prev_tid = 0, prev_prio = 0, prev_state = 1026, next_comm = "UI1 ", next_tid = 167837697, next_prio = 0 }
    [07:28:15.909579999] (+0.000060000) RTEMS THREAD_STACK_CURRENT: { cpu_id = 0 }, { data = 0xB10 }
    ...
    [07:28:15.999940999] (+0.000000000) RTEMS USER_4: { cpu_id = 0 }, { data = 0x4000192C }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_0: { cpu_id = 0 }, { data = 0x0 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_1: { cpu_id = 0 }, { data = 0x1 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_2: { cpu_id = 0 }, { data = 0x2 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_3: { cpu_id = 0 }, { data = 0x3 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_4: { cpu_id = 0 }, { data = 0x4 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_5: { cpu_id = 0 }, { data = 0x5 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_6: { cpu_id = 0 }, { data = 0x6 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_7: { cpu_id = 0 }, { data = 0x7 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_8: { cpu_id = 0 }, { data = 0x8 }
    [07:28:15.999940999] (+0.000000000) RTEMS RETURN_9: { cpu_id = 0 }, { data = 0x9 }
    [07:28:15.999940999] (+0.000000000) RTEMS ISR_DISABLE: { cpu_id = 0 }, { code = "generate_events at init.c:154" }
    [07:28:15.999940999] (+0.000000000) RTEMS ISR_ENABLE: { cpu_id = 0 }, { code = "Init at init.c:181" }

A dump from the fatal error handler looks like this:

.. code-block:: none

    *** BEGIN OF RECORDS BASE64 ZLIB ***
    eNqtlE1vE1cUhsdJWgg0jU2GABILpxUVkaJcTxzH8QqThKpRKTIJlcoyeIKIhGCCEFnAAtAoKgXa
    phqx6gKk/AAXWHTpTMYZlg0rdpBdF7Dvsuec91jYFEo+HOnq0b33Oe/9mOtks9ns7Y1TK5ZlJah1
    Uluw8HfJstqYA1b3WJG4a+p4aZpJbZzaXOlrw+4cte+p2Zcuz15kUstS3FhmZGiWOTs6nGM65Xye
    6TqZEeZQNnOOWZh1y8KZfEHG3ewMszyE+XJ2hHNyg7lBrs9lhtIZpuMUHObR9LDwuxNnppgDufQ0
    c2x6Ko35nLBcKOSEeXeYOXM+P8o8lR7oZ85dXJB1HDfN6+aGnbx4/YUR3t/+zgTfUaL3xMmJSe7v
    0X7ameTzX9N7m6d7WyNetqyOI93HVgx7xKOWtTdJHOSc7rElo6TxrgvEQfHGbxkl/PFb8F/2GSX8
    l33wX6WMEv6rlPjJ638YpfhE8ZM3Hhml+ETxUwdOG6X4RPFTB48bpfhE+E82jBL+kw34T9eNEv7T
    dfH3leaNUnyi+PtOzxil+ET4r1NGCf91Cv6bhFHCf5MQv+fHR0YpPlH8njtLRik+UXz7iGOU4hPF
    t7/qM0rxifCr60YJv7oOv/rX2aLVk1QetqvP5RFoP0N9/l2R95x/TG32SsTjo8Td4qE/0dDvFB/j
    Z94zvqch58L/zO8ltqt3cxPeZ8QO9X/fgt9F/ETrqtuo+5z4qdb/vYP6bv7fZIcVyrFtInLCCnLC
    CnLCCnLCCnLCCnLCCnLCSj0nSdytecUW5qX4/yyxt2gdGtD8b97p/2CHjy1dr3Hco3G8p/Bxm67f
    OH+jYZ+N4/fes//G+YcfPN/qMrzVZfb+JMJbXYa3ulz3cA/N/otN+Li35rp/tlCH+26q3394G/X4
    Xs05EzvIwXdvzvNakId3FAXIjQLOfUhEbhQgNwqQGwXIjQLkRgFyowC5UYDcKKjn4n1GD9qRX2c9
    /91+fb0Pjdf38bH5+j436+l5aovwaz78mg+/5sOv+fBrvvo+zr/tOh/3tuN6H/feshwf36/leT7e
    Q22xQ3LXrii9O5L/to/11jys9x/P+wnj3l3Zx0fnvXuyz0173n05z5Z972c5/7brvF/k3nZc7/0q
    9x6fR07sIid2kRO7yIld5MQucmIXObGLnNjVHHdJvl/L89zf5D3E7rdF6+BV4knJf1b6Uuqelb7g
    df4FFmd4DQ==
    *** END OF RECORDS BASE64 ZLIB ***

Copy everything between the ``*** BEGIN OF RECORDS BASE64 ZLIB ***`` and the
``*** END OF RECORDS BASE64 ZLIB ***`` markers into a file, for example
:file:`dump.txt`.  Use this command to convert the event records into the CTF
for further analysis:

.. code-block:: none

    rtems-record-lttng -e application.exe -b -z dump.txt
