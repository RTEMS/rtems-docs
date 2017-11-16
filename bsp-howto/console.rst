.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Console Driver
**************

.. warning::
    The low-level driver API changed between RTEMS 4.10 and RTEMS 4.11.  The
    legacy callback API is still supported, but its use is discouraged.  The
    following functions are deprecated:

    - :c:func:`rtems_termios_open()`

    - :c:func:`rtems_termios_close()`

    This manual describes the new API.

Introduction
============

This chapter describes the operation of a console driver using the RTEMS POSIX
Termios support.  Traditionally, RTEMS has referred to all serial device drivers
as console drivers.
`Termios <http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap11.html>`_
is defined by IEEE Std 1003.1-2008 (POSIX.1-2008).  It supports various modes
of operations at application level.  This chapter focuses on the low-level
serial device driver.  Additional Termios information can be found in the
`Linux TERMIOS(3) <http://man7.org/linux/man-pages/man3/termios.3.html>`_
manpage or the
`FreeBSD TERMIOS(4) <https://www.freebsd.org/cgi/man.cgi?query=termios&sektion=4>`_
manpage.

There are the following software layers.

+-------------------------+
| Application             |
+-------------------------+
| Termios                 |
+-------------------------+
| Low-Level Device Driver |
+-------------------------+

In the default application configuration RTEMS opens during system
initialization a :file:`/dev/console` device file to create the file
descriptors 0, 1 and 2 used for standard input, output and error, respectively.
The corresponding device driver is usually a Termios serial device driver
described here.  The standard file descriptors are used by standard C library
calls such as :c:func:`printf` or :c:func:`scanf` or directly via the
:c:func:`read` or :c:func:`write` system calls.

Build System and Files
======================

A new serial device driver should consist of three parts.

- A section in the BSPs Makefile.am:

.. code-block:: makefile

      [...]
      libbsp_a_SOURCES += ../../shared/console-termios.c
      libbsp_a_SOURCES += console/console.c
      [...]

- A general serial device specific low-level driver providing the handler table
  and the device context specialization for the Termios
  :c:func:`rtems_termios_device_install()` function.  This low-level driver
  could be used for more than one BSP.

- A BSP-specific initialization routine :c:func:`console_initialize()`, that calls
  :c:func:`rtems_termios_device_install()` providing a low-level driver context for
  each installed device.  This is usually defined in the file
  :file:`console/console.c` relative to the BSP base directory.

The low-level driver should provide a specialization of the Termios device
context.  The initialization routine must provide a context for each installed
device via :c:func:`rtems_termios_device_install()`.  Here is an example header
file for a low-level serial device driver.

.. code-block:: c

    #ifndef MY_DRIVER_H
    #define MY_DRIVER_H

    #include <some-chip/serial.h>

    #include <rtems/termiostypes.h>

    /* My low-level driver specialization of Termios device context */
    typedef struct {
      rtems_termios_device_context base;
      const char *device_name;
      volatile some_chip_registers *regs;
      /* More stuff */
    } my_driver_context;

    extern const rtems_termios_device_handler my_driver_handler_polled;

    extern const rtems_termios_device_handler my_driver_handler_interrupt;

    #endif /* MY_DRIVER_H */

Driver Functioning Modes
========================

There are four main functioning modes for a Termios serial device driver.  The
mode must be set during device creation and cannot be changed afterwards.

Polled Mode (`TERMIOS_POLLED`)
    In polled mode, the processor blocks on sending/receiving characters.  This
    mode is not the most efficient way to utilize the serial device. But polled
    mode is usually necessary when one wants to print an error message in the
    event of a fatal error such as a fatal error in the BSP.  This is also the
    simplest mode to program.  Polled mode is generally preferred if the serial
    device is to be used primarily as a debug console.  In a simple polled
    driver, the software will continuously check the status of the serial
    device when it is reading or writing to the serial device.  Termios
    improves on this by delaying the caller for one clock tick between
    successive checks of the serial device on a read operation.

Interrupt Driven Mode (`TERMIOS_IRQ_DRIVEN`)
    In interrupt driven mode, the processor does not block on sending/receiving
    characters.  Data is buffered between the interrupt service routine and
    application code.  Two buffers are used to insulate the application from
    the relative slowness of the serial device.  One of the buffers is used for
    incoming characters, while the other is used for outgoing characters.

    An interrupt is raised when a character is received by the serial device.
    The interrupt routine places the incoming character at the end of the input
    buffer.  When an application asks for input, the characters at the front of
    the buffer are returned.

    When the application prints to the serial device, the outgoing characters
    are placed at the end of the output buffer.  The driver will place one or
    more characters in the serial device (the exact number depends on the
    serial device) An interrupt will be raised when all the characters have
    been transmitted.  The interrupt service routine has to send the characters
    remaining in the output buffer the same way.  When the transmitting side of
    the serial device is idle, it is typically necessary to prime the
    transmitter before the first interrupt will occur.

Interrupt Server Driven Mode (`TERMIOS_IRQ_SERVER_DRIVEN`)
    The interrupt server driven mode is identical to the interrupt driven mode,
    except that a mutex is used to protect the low-level device state instead
    of an interrupt lock (disabled interrupts).  Use this mode in case the
    serial device is connected via I2C or SPI and the I2C or SPI framework is
    used.

Task Driven Mode (`TERMIOS_TASK_DRIVEN`)
    The task driven mode is similar to interrupt driven mode, but the actual
    data processing is done in dedicated tasks instead of interrupt routines.
    This mode is not available in SMP configurations.  It has some
    implementation flaws and it is not well tested.

Polled Mode
===========

The handler table for the polled mode should look like the following.

.. code-block:: c

    const rtems_termios_device_handler my_driver_handler_polled = {
      .first_open = my_driver_first_open,
      .last_close = my_driver_last_close,
      .poll_read = my_driver_poll_read,
      .write = my_driver_poll_write,
      .set_attributes = my_driver_set_attributes,
      .ioctl = my_driver_ioctl, /* optional, may be NULL */
      .mode = TERMIOS_POLLED
    }

The :c:func:`my_driver_poll_write()` routine is responsible for writing ``n``
characters from ``buf`` to the serial device specified by ``base``.

.. code-block:: c

    static void my_driver_poll_write(
      rtems_termios_device_context *base,
      const char                   *buf,
      size_t                        n
    )
    {
      my_driver_context *ctx;
      size_t             i;

      ctx = (my_driver_context *) base;

      for ( i = 0 ; i < n ; ++i ) {
        my_driver_write_char( ctx, buf[ i ] );
      }
    }

The :c:func:`my_driver_poll_read` routine is responsible for reading a single
character from the serial device specified by ``base``.  If no character is
available, then the routine should immediately return minus one.

.. code-block:: c

    static int my_driver_poll_read( rtems_termios_device_context *base )
    {
      my_driver_context *ctx;

      ctx = (my_driver_context *) base;

      if ( my_driver_can_read_char( ctx ) ) {
        /* Return the character (must be unsigned) */
        return my_driver_read_char( ctx );
      } else {
        /* Return -1 to indicate that no character is available */
        return -1;
      }
    }

Interrupt Driven Mode
=====================

The handler table for the interrupt driven mode should look like the following.

.. code-block:: c

    const rtems_termios_device_handler my_driver_handler_interrupt = {
      .first_open = my_driver_first_open,
      .last_close = my_driver_last_close,
      .poll_read = NULL,
      .write = my_driver_interrupt_write,
      .set_attributes = my_driver_set_attributes,
      .ioctl = my_driver_ioctl, /* optional, may be NULL */
      .mode = TERMIOS_IRQ_DRIVEN
    };

There is no device driver read handler to be passed to Termios.  Indeed a
:c:func:`read()` call returns the contents of Termios input buffer.  This
buffer is filled in the driver interrupt routine.

A serial device generally generates interrupts when it is ready to accept or to
emit a number of characters.  In this mode, the interrupt routine is the core
of the driver.

The :c:func:`my_driver_interrupt_handler` is responsible for processing
asynchronous interrupts from the serial device.  There may be multiple
interrupt handlers for a single serial device.  Some serial devices can
generate a unique interrupt vector for each interrupt source such as a
character has been received or the transmitter is ready for another character.

In the simplest case, the :c:func:`my_driver_interrupt_handler` will have to
check the status of the serial device and determine what caused the interrupt.
The following describes the operation of an
:c:func:`my_driver_interrupt_handler` which has to do this:

.. code-block:: c

    static void my_driver_interrupt_handler( void *arg )
    {
      rtems_termios_tty *tty;
      my_driver_context *ctx;
      char               buf[N];
      size_t             n;

      tty = arg;
      ctx = rtems_termios_get_device_context( tty );

      /*
       * Check if we have received something.  The function reads the
       * received characters from the device and stores them in the
       * buffer.  It returns the number of read characters.
       */
      n = my_driver_read_received_chars( ctx, buf, N );
      if ( n > 0 ) {
        /* Hand the data over to the Termios infrastructure */
        rtems_termios_enqueue_raw_characters( tty, buf, n );
      }

      /*
       * Check if we have something transmitted.  The functions returns
       * the number of transmitted characters since the last write to the
       * device.
       */
      n = my_driver_transmitted_chars( ctx );
      if ( n > 0 ) {
        /*
         * Notify Termios that we have transmitted some characters.  It
         * will call now the interrupt write function if more characters
         * are ready for transmission.
         */
        rtems_termios_dequeue_characters( tty, n );
      }
    }

The :c:func:`my_driver_interrupt_write()` handler is responsible for telling
the device that the ``n`` characters at ``buf`` are to be transmitted.  It the
value ``n`` is zero to indicate that no more characters are to send.  The
driver can disable the transmit interrupts now.  This routine is invoked either
from task context with disabled interrupts to start a new transmission process
with exactly one character in case of an idle output state or from the
interrupt handler to refill the transmitter.  If the routine is invoked to
start the transmit process the output state will become busy and Termios starts
to fill the output buffer.  If the transmit interrupt arises before Termios was
able to fill the transmit buffer you will end up with one interrupt per
character.

.. code-block:: c

    static void my_driver_interrupt_write(
      rtems_termios_device_context  *base,
      const char                    *buf,
      size_t                         n
    )
    {
      my_driver_context *ctx;

      ctx = (my_driver_context *) base;

      if ( n > 0 ) {
        /*
         * Tell the device to transmit some characters from buf (less than
         * or equal to n).  When the device is finished it should raise an
         * interrupt.  The interrupt handler will notify Termios that these
         * characters have been transmitted and this may trigger this write
         * function again.  You may have to store the number of outstanding
         * characters in the device data structure.
         */
      } else {
        /*
         * Termios will set n to zero to indicate that the transmitter is
         * now inactive.  The output buffer is empty in this case.  The
         * driver may disable the transmit interrupts now.
         */
      }
    }

First Open
==========

Upon first open of the device, the :c:func:`my_driver_first_open` handler is
called by Termios.  The device registered as :file:`/dev/console` (or
``CONSOLE_DEVICE_NAME``) is opened automatically during RTEMS initialization.

.. code-block:: c

    static bool my_driver_first_open(
      rtems_termios_tty             *tty,
      rtems_termios_device_context  *base,
      struct termios                *term,
      rtems_libio_open_close_args_t *args
    )
    {
      my_driver_context *ctx;
      rtems_status_code  sc;
      bool               ok;

      ctx = (my_driver_context *) base;

      /*
       * You may add some initialization code here.
       */

      /*
       * Sets the initial baud rate.  This should be set to the value of
       * the boot loader.  This function accepts only exact Termios baud
       * values.
       */
      sc = rtems_termios_set_initial_baud( tty, MY_DRIVER_BAUD_RATE );
      if ( sc != RTEMS_SUCCESSFUL ) {
        /* Not a valid Termios baud */
      }

      /*
       * Alternatively you can set the best baud.
       */
      rtems_termios_set_best_baud( term, MY_DRIVER_BAUD_RATE );

      /*
       * To propagate the initial Termios attributes to the device use
       * this.
      */
      ok = my_driver_set_attributes( base, term );
      if ( !ok ) {
        /* This is bad */
      }

      /*
       * Return true to indicate a successful set attributes, and false
       * otherwise.
       */
      return true;
    }

Last Close
==========

Termios will call the :c:func:`my_driver_last_close` handler if the last close
happens on the device.

.. code-block:: c

    static void my_driver_last_close(
      rtems_termios_tty             *tty,
      rtems_termios_device_context  *base,
      rtems_libio_open_close_args_t *args
    )
    {
      my_driver_context *ctx;

      ctx = (my_driver_context *) base;

      /*
       * The driver may do some cleanup here.
       */
    }

Set Attributes
==============

Termios will call the :c:func:`my_driver_set_attributes` handler if a serial
line configuration parameter changed, e.g. baud, character size, number of stop
bits, parity, etc.

.. code-block:: c

    static bool my_driver_set_attributes(
      rtems_termios_device_context *base,
      const struct termios         *term
    )
    {
      my_driver_context *ctx;

      ctx = (my_driver_context *) base;

      /*
       * Inspect the termios data structure and configure the device
       * appropriately.  The driver should only be concerned with the
       * parts of the structure that specify hardware setting for the
       * communications channel such as baud, character size, etc.
       */

      /*
       * Return true to indicate a successful set attributes, and false
       * otherwise.
       */
      return true;
    }

IO Control
==========

Optionally, the :c:func:`my_driver_ioctl()` routine may be provided for
arbitrary device-specific functions.

.. code-block:: c

    static int my_driver_ioctl(
      rtems_termios_device_context *base,
      ioctl_command_t               request,
      void                         *buffer
    )
    {
      my_driver_context *ctx;

      ctx = (my_driver_context *) base;

      switch ( request ) {
        case MY_DRIVER_DO_XYZ:
          my_driver_do_xyz(ctx, buffer);
          break;
        default:
          rtems_set_errno_and_return_minus_one( EINVAL );
      }

      return 0;
    }

Flow Control
============

You can also provide handler for remote transmission control.  This is not
covered in this manual.

General Initialization
======================

The BSP-specific driver initialization is called once during the RTEMS
initialization process.

The :c:func:`console_initialize()` function may look like this:

.. code-block:: c

    #include <my-driver.h>

    #include <rtems/console.h>

    #include <bsp.h>
    #include <bsp/fatal.h>

    static my_driver_context driver_context_table[] = {
      { /* Some values for device 0 */ },
      { /* Some values for device 1 */ }
    };

    rtems_device_driver console_initialize(
      rtems_device_major_number  major,
      rtems_device_minor_number  minor,
      void                      *arg
    )
    {
      const rtems_termios_device_handler *handler;
      rtems_status_code                   sc;
      size_t                              i;

      #ifdef SOME_BSP_USE_INTERRUPTS
        handler = &my_driver_handler_interrupt;
      #else
        handler = &my_driver_handler_polled;
      #endif

      /*
       * Initialize the Termios infrastructure.  If Termios has already
       * been initialized by another device driver, then this call will
       * have no effect.
       */
      rtems_termios_initialize();

      /* Initialize each device */
      for ( i = 0; i < RTEMS_ARRAY_SIZE( driver_context_table ) ; ++i ) {
        my_driver_context *ctx;

        ctx = &driver_context_table[ i ];

        /*
         * Install this device in the file system and Termios.  In order
         * to use the console (i.e. being able to do printf, scanf etc.
         * on stdin, stdout and stderr), one device must be registered as
         * "/dev/console" (CONSOLE_DEVICE_NAME).
         */
        sc = rtems_termios_device_install( ctx->device_name, handler, NULL, ctx );
        if ( sc != RTEMS_SUCCESSFUL ) {
          bsp_fatal( SOME_BSP_FATAL_CONSOLE_DEVICE_INSTALL );
        }
      }

      return RTEMS_SUCCESSFUL;
    }
