.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Clock Driver
************

Introduction
============

The purpose of the clock driver is to provide two services for the operating
system.

- A steady time basis to the kernel, so that the RTEMS primitives that need a
  clock tick work properly.  See the *Clock Manager* chapter of the *RTEMS
  Application C User's Guide* for more details.

- An optional `timecounter <http://www.freebsd.dk/pubs/timecounter.pdf>`_ to
  provide timestamps of the uptime and wall clock time with higher resolution
  than the clock tick.

The clock driver is usually located in the :file:`clock` directory of the BSP.
Clock drivers must use the :dfn:`Clock Driver Shell` available via the
`clockdrv_shell.h <https://git.rtems.org/rtems/tree/c/src/lib/libbsp/shared/clockdrv_shell.h>`_
include file.  This include file is not a normal header file and instead
defines the clock driver functions declared in ``#include <rtems/clockdrv.h>``
which are used by RTEMS configuration file ``#include <rtems/confdefs.h>``.  In
case the application configuration defines
``#define CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``, then the clock driver is
registered and should provide its services to the operating system.  The clock
tick interval is determined by the application configuration via
``#define CONFIGURE_MICROSECONDS_PER_TICK`` and can be obtained via
``rtems_configuration_get_microseconds_per_tick()``.

A hardware-specific clock driver must provide some functions, defines and
macros for the :dfn:`Clock Driver Shell` which are explained here step by step.
A clock driver file looks in general like this.

.. code-block:: c

    /*
     * A section with functions, defines and macros to provide hardware-specific
     * functions for the Clock Driver Shell.
     */

    #include "../../../shared/clockdrv_shell.h"

Depending on the hardware capabilities one out of three clock driver variants
must be selected.

Timecounter
    The variant which provides all features needs a free running hardware
    counter and a periodic clock tick interrupt.  This variant is mandatory in
    SMP configurations.

Simple Timecounter
    A simple timecounter can be used if the hardware provides no free running
    hardware counter and only a periodic hardware counter synchronous to the
    clock tick interrupt is available.

Clock Tick Only
    The most basic clock driver provides only a periodic clock tick interrupt.
    The timestamp resolution is limited to the clock tick interval.

Initialization
==============

Timecounter Variant
~~~~~~~~~~~~~~~~~~~

This variant is preferred since it is the most efficient and yields the most
accurate timestamps.  It is also mandatory in SMP configurations to obtain
valid timestamps.  The hardware must provide a periodic interrupt to service
the clock tick and a free running counter for the timecounter.  The free
running counter must have a power of two period.  The ``tc_counter_mask`` must
be initialized to the free running counter period minus one, e.g. for a 17-bit
counter this is ``0x0001ffff``.  The ``tc_get_timecount`` function must return
the current counter value (the counter values must increase, so if the counter
counts down, a conversion is necessary).  Use
``RTEMS_TIMECOUNTER_QUALITY_CLOCK_DRIVER`` for the ``tc_quality``.  Set
``tc_frequency`` to the frequency of the free running counter in Hz.  All other
fields of the ``struct timecounter`` must be zero initialized.  Install the
initialized timecounter via ``rtems_timecounter_install()``.

For an example see the `QorIQ clock driver
<https://git.rtems.org/rtems/tree/c/src/lib/libbsp/powerpc/qoriq/clock/clock-config.c>`_.

.. code-block:: c

    #include <rtems/timecounter.h>

    static struct timecounter some_tc;

    static uint32_t some_tc_get_timecount( struct timecounter *tc )
    {
      some.free_running_counter;
    }

    static void some_support_initialize_hardware( void )
    {
      uint64_t us_per_tick;
      uint32_t counter_frequency_in_hz;
      uint32_t counter_ticks_per_clock_tick;

      us_per_tick = rtems_configuration_get_microseconds_per_tick();
      counter_frequency_in_hz = some_tc_get_frequency();

      /*
       * The multiplication must be done in 64-bit arithmetic to avoid an integer
       * overflow on targets with a high enough counter frequency.
       */
      counter_ticks_per_clock_tick =
        (uint32_t) ( counter_frequency_in_hz * us_per_tick ) / 1000000;

      /*
       * Initialize hardware and set up a periodic interrupt for the configuration
       * based counter ticks per clock tick.
       */

      some_tc.tc_get_timecount = some_tc_get_timecount;
      some_tc.tc_counter_mask = 0xffffffff;
      some_tc.tc_frequency = frequency;
      some_tc.tc_quality = RTEMS_TIMECOUNTER_QUALITY_CLOCK_DRIVER;
      rtems_timecounter_install( &some_tc );
    }

    #define Clock_driver_support_initialize_hardware() \
      some_support_initialize_hardware()

    #include "../../../shared/clockdrv_shell.h"

Simple Timecounter Variant
~~~~~~~~~~~~~~~~~~~~~~~~~~

For an example see the `ERC32 clock driver
<https://git.rtems.org/rtems/tree/c/src/lib/libbsp/sparc/erc32/clock/ckinit.c>`_.

.. code-block:: c

    #include <rtems/timecounter.h>

    static rtems_timecounter_simple some_tc;

    static uint32_t some_tc_get( rtems_timecounter_simple *tc )
    {
      return some.counter;
    }

    static bool some_tc_is_pending( rtems_timecounter_simple *tc )
    {
      return some.is_pending;
    }

    static uint32_t some_tc_get_timecount( struct timecounter *tc )
    {
      return rtems_timecounter_simple_downcounter_get(
        tc,
        some_tc_get,
        some_tc_is_pending
      );
    }

    static void some_tc_tick( void )
    {
      rtems_timecounter_simple_downcounter_tick( &some_tc, some_tc_get );
    }

    static void some_support_initialize_hardware( void )
    {
      uint64_t us_per_tick;
      uint32_t counter_frequency_in_hz;
      uint32_t counter_ticks_per_clock_tick;

      us_per_tick = rtems_configuration_get_microseconds_per_tick();
      counter_frequency_in_hz = some_tc_get_frequency();
      counter_ticks_per_clock_tick =
        (uint32_t) ( counter_frequency_in_hz * us_per_tick ) / 1000000;

      /* Initialize hardware */

      rtems_timecounter_simple_install(
        &some_tc,
        counter_frequency_in_hz,
        counter_ticks_per_clock_tick,
        some_tc_get_timecount
      );
    }

    #define Clock_driver_support_initialize_hardware() \
      some_support_initialize_hardware()
    #define Clock_driver_timecounter_tick() \
      some_tc_tick()

    #include "../../../shared/clockdrv_shell.h"

Clock Tick Only Variant
~~~~~~~~~~~~~~~~~~~~~~~

For an example see the `Motrola 68360 clock driver
<https://git.rtems.org/rtems/tree/c/src/lib/libbsp/m68k/gen68360/clock/clock.c>`_.

.. code-block:: c

    static void some_support_initialize_hardware( void )
    {
      /* Initialize hardware */
    }

    #define Clock_driver_support_initialize_hardware() \
      some_support_initialize_hardware()

    /* Indicate that this clock driver lacks a proper timecounter in hardware */

    #define CLOCK_DRIVER_USE_DUMMY_TIMECOUNTER

    #include "../../../shared/clockdrv_shell.h"

Install Clock Tick Interrupt Service Routine
============================================

The clock driver must provide a function to install the clock tick interrupt
service routine via ``Clock_driver_support_install_isr()``.

.. code-block:: c

    #include <bsp/irq.h>
    #include <bsp/fatal.h>

    static void some_support_install_isr( rtems_interrupt_handler isr )
    {
      rtems_status_code sc;
      sc = rtems_interrupt_handler_install(
        SOME_IRQ,
        "Clock",
        RTEMS_INTERRUPT_UNIQUE,
        isr,
        NULL
      );
      if ( sc != RTEMS_SUCCESSFUL ) {
        bsp_fatal( SOME_FATAL_IRQ_INSTALL );
      }
    }

    #define Clock_driver_support_install_isr( isr, old ) \
      some_support_install_isr( isr )

    #include "../../../shared/clockdrv_shell.h"

Support At Tick
===============

The hardware-specific support at tick is specified by
``Clock_driver_support_at_tick()``.

.. code-block:: c

    static void some_support_at_tick( void )
    {
      /* Clear interrupt */
    }

    #define Clock_driver_support_at_tick() \
      some_support_at_tick()

    #include "../../../shared/clockdrv_shell.h"

System Shutdown Support
=======================

Optionally, the :dfn:`Clock Driver Shell` provides the routine ``Clock_exit()``
that is scheduled to be run during system shutdown via the ``atexit()``
routine.  The hardware-specific shutdown support is specified by
``Clock_driver_support_shutdown_hardware()`` which is used by ``Clock_exit()``.
It should disable the clock tick source if it was enabled.  This can be used to
prevent clock ticks after the system is shutdown.  The
``Clock_driver_support_shutdown_hardware()`` must be provided as a macro.  In
case this macro is undefined, then the shutdown support is disabled.  This is
useful for example on memory constrained systems to avoid the ``atexit()``
overhead.

.. code-block:: c

    static void some_support_shutdown_hardware( void )
    {
      /* Shutdown hardware */
    }

    #define Clock_driver_support_shutdown_hardware() \
      some_support_shutdown_hardware()

    #include "../../../shared/clockdrv_shell.h"

SMP Support
===========

In SMP configurations, the clock tick service must be executed for each
processor used by RTEMS.  By default, the clock tick interrupt must be
distributed to all processors used by RTEMS and each processor invokes the
clock tick service individually.  A clock driver may delegate all the work to
the boot processor.  It must define ``CLOCK_DRIVER_USE_ONLY_BOOT_PROCESSOR`` in
this case.

Clock drivers must define
``Clock_driver_support_set_interrupt_affinity(online_processors)`` to set the
interrupt affinity of the clock tick interrupt.

Multiple Clock Driver Ticks Per Clock Tick
==========================================

In case the hardware needs more than one clock driver tick per clock tick (e.g.
due to a limited range of the hardware timer), then this can be specified with
the optional ``#define CLOCK_DRIVER_ISRS_PER_TICK`` and ``#define
CLOCK_DRIVER_ISRS_PER_TICK_VALUE`` defines.  This is currently used only for
x86 and it hopefully remains that way.

.. code-block:: c

    /* Enable multiple clock driver ticks per clock tick */
    #define CLOCK_DRIVER_ISRS_PER_TICK 1

    /* Specifiy the clock driver ticks per clock tick value */
    #define CLOCK_DRIVER_ISRS_PER_TICK_VALUE 123

    #include "../../../shared/clockdrv_shell.h"

Clock Driver Ticks Counter
==========================

The :dfn:`Clock Driver Shell` provide a global variable that is simply a count
of the number of clock driver interrupt service routines that have occurred.
This information is valuable when debugging a system.  This variable is
declared as follows:

.. code-block:: c

    volatile uint32_t Clock_driver_ticks;
