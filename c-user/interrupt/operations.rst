.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Establishing an ISR
-------------------

The ``rtems_interrupt_catch`` directive establishes an ISR for the system.  The
address of the ISR and its associated CPU vector number are specified to this
directive.  This directive installs the RTEMS interrupt wrapper in the
processor's Interrupt Vector Table and the address of the user's ISR in the
RTEMS' Vector Table.  This directive returns the previous contents of the
specified vector in the RTEMS' Vector Table.

Directives Allowed from an ISR
------------------------------

Using the interrupt manager ensures that RTEMS knows when a directive is being
called from an ISR.  The ISR may then use system calls to synchronize itself
with an application task.  The synchronization may involve messages, events or
signals being passed by the ISR to the desired task.  Directives invoked by an
ISR must operate only on objects which reside on the local node.  The following
is a list of RTEMS system calls that may be made from an ISR:

- Task Management
  Although it is acceptable to operate on the RTEMS_SELF task (e.g.  the
  currently executing task), while in an ISR, this will refer to the
  interrupted task.  Most of the time, it is an application implementation
  error to use RTEMS_SELF from an ISR.

  - rtems_task_suspend
  - rtems_task_resume

- Interrupt Management

  - rtems_interrupt_enable
  - rtems_interrupt_disable
  - rtems_interrupt_flash
  - rtems_interrupt_lock_acquire
  - rtems_interrupt_lock_release
  - rtems_interrupt_lock_acquire_isr
  - rtems_interrupt_lock_release_isr
  - rtems_interrupt_is_in_progress
  - rtems_interrupt_catch

- Clock Management

  - rtems_clock_set
  - rtems_clock_get_tod
  - rtems_clock_get_tod_timeval
  - rtems_clock_get_seconds_since_epoch
  - rtems_clock_get_ticks_per_second
  - rtems_clock_get_ticks_since_boot
  - rtems_clock_get_uptime

- Timer Management

  - rtems_timer_cancel
  - rtems_timer_reset
  - rtems_timer_fire_after
  - rtems_timer_fire_when
  - rtems_timer_server_fire_after
  - rtems_timer_server_fire_when

- Event Management

  - rtems_event_send
  - rtems_event_system_send
  - rtems_event_transient_send

- Semaphore Management

  - rtems_semaphore_release

- Message Management

  - rtems_message_queue_broadcast
  - rtems_message_queue_send
  - rtems_message_queue_urgent

- Signal Management

  - rtems_signal_send

- Dual-Ported Memory Management

  - rtems_port_external_to_internal
  - rtems_port_internal_to_external

- IO Management
  The following services are safe to call from an ISR if and only if
  the device driver service invoked is also safe.  The IO Manager itself
  is safe but the invoked driver entry point may or may not be.

  - rtems_io_initialize
  - rtems_io_open
  - rtems_io_close
  - rtems_io_read
  - rtems_io_write
  - rtems_io_control

- Fatal Error Management

  - rtems_fatal
  - rtems_fatal_error_occurred

- Multiprocessing

  - rtems_multiprocessing_announce
