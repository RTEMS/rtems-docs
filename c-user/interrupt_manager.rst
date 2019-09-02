.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. index:: interrupts

Interrupt Manager
*****************

Introduction
============

Any real-time executive must provide a mechanism for quick response to
externally generated interrupts to satisfy the critical time constraints of the
application.  The interrupt manager provides this mechanism for RTEMS.  This
manager permits quick interrupt response times by providing the critical
ability to alter task execution which allows a task to be preempted upon exit
from an ISR.  The interrupt manager includes the following directive:

- rtems_interrupt_catch_ - Establish an ISR

- rtems_interrupt_disable_ - Disable Interrupts

- rtems_interrupt_enable_ - Restore Interrupt Level

- rtems_interrupt_flash_ - Flash Interrupt

- rtems_interrupt_local_disable_ - Disable Interrupts on Current Processor

- rtems_interrupt_local_enable_ - Restore Interrupt Level on Current Processor

- rtems_interrupt_lock_initialize_ - Initialize an ISR Lock

- rtems_interrupt_lock_acquire_ - Acquire an ISR Lock

- rtems_interrupt_lock_release_ - Release an ISR Lock

- rtems_interrupt_lock_acquire_isr_ - Acquire an ISR Lock from ISR

- rtems_interrupt_lock_release_isr_ - Release an ISR Lock from ISR

- rtems_interrupt_is_in_progress_ - Is an ISR in Progress

Background
==========

.. index:: interrupt processing

Processing an Interrupt
-----------------------

The interrupt manager allows the application to connect a function to a
hardware interrupt vector.  When an interrupt occurs, the processor will
automatically vector to RTEMS.  RTEMS saves and restores all registers which
are not preserved by the normal C calling convention for the target processor
and invokes the user's ISR.  The user's ISR is responsible for processing the
interrupt, clearing the interrupt if necessary, and device specific
manipulation.

.. index:: rtems_vector_number

The ``rtems_interrupt_catch`` directive connects a procedure to an interrupt
vector.  The vector number is managed using the ``rtems_vector_number`` data
type.

The interrupt service routine is assumed to abide by these conventions and have
a prototype similar to the following:

.. index:: rtems_isr

.. code-block:: c

    rtems_isr user_isr(
      rtems_vector_number vector
    );

The vector number argument is provided by RTEMS to allow the application to
identify the interrupt source.  This could be used to allow a single routine to
service interrupts from multiple instances of the same device.  For example, a
single routine could service interrupts from multiple serial ports and use the
vector number to identify which port requires servicing.

To minimize the masking of lower or equal priority level interrupts, the ISR
should perform the minimum actions required to service the interrupt.  Other
non-essential actions should be handled by application tasks.  Once the user's
ISR has completed, it returns control to the RTEMS interrupt manager which will
perform task dispatching and restore the registers saved before the ISR was
invoked.

The RTEMS interrupt manager guarantees that proper task scheduling and
dispatching are performed at the conclusion of an ISR.  A system call made by
the ISR may have readied a task of higher priority than the interrupted task.
Therefore, when the ISR completes, the postponed dispatch processing must be
performed.  No dispatch processing is performed as part of directives which
have been invoked by an ISR.

Applications must adhere to the following rule if proper task scheduling and
dispatching is to be performed:

.. note::

  The interrupt manager must be used for all ISRs which may be interrupted by
  the highest priority ISR which invokes an RTEMS directive.

Consider a processor which allows a numerically low interrupt level to
interrupt a numerically greater interrupt level.  In this example, if an RTEMS
directive is used in a level 4 ISR, then all ISRs which execute at levels 0
through 4 must use the interrupt manager.

Interrupts are nested whenever an interrupt occurs during the execution of
another ISR.  RTEMS supports efficient interrupt nesting by allowing the nested
ISRs to terminate without performing any dispatch processing.  Only when the
outermost ISR terminates will the postponed dispatching occur.

.. index:: interrupt levels

RTEMS Interrupt Levels
----------------------

Many processors support multiple interrupt levels or priorities.  The exact
number of interrupt levels is processor dependent.  RTEMS internally supports
256 interrupt levels which are mapped to the processor's interrupt levels.  For
specific information on the mapping between RTEMS and the target processor's
interrupt levels, refer to the Interrupt Processing chapter of the Applications
Supplement document for a specific target processor.

.. index:: disabling interrupts

Disabling of Interrupts by RTEMS
--------------------------------

During the execution of directive calls, critical sections of code may be
executed.  When these sections are encountered, RTEMS disables all maskable
interrupts before the execution of the section and restores them to the
previous level upon completion of the section.  RTEMS has been optimized to
ensure that interrupts are disabled for a minimum length of time.  The maximum
length of time interrupts are disabled by RTEMS is processor dependent and is
detailed in the Timing Specification chapter of the Applications Supplement
document for a specific target processor.

Non-maskable interrupts (NMI) cannot be disabled, and ISRs which execute at
this level MUST NEVER issue RTEMS system calls.  If a directive is invoked,
unpredictable results may occur due to the inability of RTEMS to protect its
critical sections.  However, ISRs that make no system calls may safely execute
as non-maskable interrupts.

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

Directives
==========

This section details the interrupt manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: establish an ISR
.. index:: install an ISR
.. index:: rtems_interrupt_catch

.. _rtems_interrupt_catch:

INTERRUPT_CATCH - Establish an ISR
----------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_interrupt_catch(
          rtems_isr_entry      new_isr_handler,
          rtems_vector_number  vector,
          rtems_isr_entry     *old_isr_handler
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-wrap

     * - ``RTEMS_SUCCESSFUL``
       -  ISR established successfully
     * - ``RTEMS_INVALID_NUMBER``
       -  illegal vector number
     * - ``RTEMS_INVALID_ADDRESS``
       -  illegal ISR entry point or invalid ``old_isr_handler``

DESCRIPTION:
    This directive establishes an interrupt service routine (ISR) for the
    specified interrupt vector number.  The ``new_isr_handler`` parameter
    specifies the entry point of the ISR.  The entry point of the previous ISR
    for the specified vector is returned in ``old_isr_handler``.

    To release an interrupt vector, pass the old handler's address obtained
    when the vector was first capture.

NOTES:
    This directive will not cause the calling task to be preempted.

.. raw:: latex

   \clearpage

.. index:: disable interrupts
.. index:: rtems_interrupt_disable

.. _rtems_interrupt_disable:

INTERRUPT_DISABLE - Disable Interrupts
--------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_disable(
          rtems_interrupt_level level
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive disables all maskable interrupts and returns the previous
    interrupt level in ``level``.

NOTES:
    A later invocation of the ``rtems_interrupt_enable`` directive should be
    used to restore the interrupt level.

    This directive is implemented as a macro which sets the ``level``
    parameter.

    This directive will not cause the calling task to be preempted.

    This directive is only available in uniprocessor configurations.  The
    directive ``rtems_interrupt_local_disable`` is available in all
    configurations.

    .. code-block:: c

        void critical_section( void )
        {
          rtems_interrupt_level level;

          /*
           * Please note that the rtems_interrupt_disable() is a macro.  The
           * previous interrupt level (before the maskable interrupts are
           * disabled) is returned here in the level macro parameter.  This
           * would be wrong:
           *
           * rtems_interrupt_disable( &level );
           */
          rtems_interrupt_disable( level );

          /* Critical section, maskable interrupts are disabled */

          {
            rtems_interrupt_level level2;

            rtems_interrupt_disable( level2 );

            /* Nested critical section */

            rtems_interrupt_enable( level2 );
          }

          /* Maskable interrupts are still disabled */

          rtems_interrupt_enable( level );
        }

.. raw:: latex

   \clearpage

.. index:: enable interrupts
.. index:: restore interrupt level
.. index:: rtems_interrupt_enable

.. _rtems_interrupt_enable:

INTERRUPT_ENABLE - Restore Interrupt Level
------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_enable(
          rtems_interrupt_level level
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive restores the interrupt level specified by ``level``.

NOTES:
    The ``level`` parameter value must be obtained by a previous call to
    ``rtems_interrupt_disable`` or ``rtems_interrupt_flash``.  Using an
    otherwise obtained value is undefined behaviour.

    This directive is unsuitable to enable particular interrupt sources, for
    example in an interrupt controller.

    This directive will not cause the calling task to be preempted.

    This directive is only available in uniprocessor configurations.  The
    directive ``rtems_interrupt_local_enable`` is available in all
    configurations.

.. raw:: latex

   \clearpage

.. index:: flash interrupts
.. index:: rtems_interrupt_flash

.. _rtems_interrupt_flash:

INTERRUPT_FLASH - Flash Interrupts
----------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_flash(
          rtems_interrupt_level level
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive is functionally equivalent to a
    ``rtems_interrupt_enable( level )`` immediately followed by a
    ``rtems_interrupt_disable( level )``.  On some
    architectures it is possible to provide an optimized implementation for
    this sequence.

NOTES:
    The ``level`` parameter value must be obtained by a previous call to
    ``rtems_interrupt_disable`` or ``rtems_interrupt_flash``.  Using an
    otherwise obtained value is undefined behaviour.

    This directive will not cause the calling task to be preempted.

    This directive is only available in uniprocessor configurations.  The
    directives ``rtems_interrupt_local_disable`` and
    ``rtems_interrupt_local_enable`` are available in all configurations.

    Historically, the interrupt flash directive was heavily used in the
    operating system implementation.  However, this is no longer the case.  The
    interrupt flash directive is provided for backward compatibility reasons.

.. raw:: latex

   \clearpage

.. index:: disable interrupts
.. index:: rtems_interrupt_local_disable

.. _rtems_interrupt_local_disable:

INTERRUPT_LOCAL_DISABLE - Disable Interrupts on Current Processor
-----------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_local_disable(
          rtems_interrupt_level level
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive disables all maskable interrupts on the current processor
    and returns the previous interrupt level in ``level``.

NOTES:
    A later invocation of the ``rtems_interrupt_local_enable`` directive should
    be used to restore the interrupt level.

    This directive is implemented as a macro which sets the ``level``
    parameter.

    This directive will not cause the calling task to be preempted.

    In SMP configurations, this will not ensure system wide mutual exclusion.
    Use interrupt locks instead.

    .. code-block:: c

        void local_critical_section( void )
        {
          rtems_interrupt_level level;

          /*
           * Please note that the rtems_interrupt_local_disable() is a macro.
           * The previous interrupt level (before the maskable interrupts are
           * disabled) is returned here in the level macro parameter.  This
           * would be wrong:
           *
           * rtems_interrupt_local_disable( &level );
           */
          rtems_interrupt_local_disable( level );

          /*
           * Local critical section, maskable interrupts on the current
           * processor are disabled.
           */

          {
            rtems_interrupt_level level2;

            rtems_interrupt_local_disable( level2 );

            /* Nested local critical section */

            rtems_interrupt_local_enable( level2 );
          }

          /* Maskable interrupts are still disabled */

          rtems_interrupt_local_enable( level );
        }

.. raw:: latex

   \clearpage

.. index:: enable interrupts
.. index:: restore interrupt level
.. index:: rtems_interrupt_local_enable

.. _rtems_interrupt_local_enable:

INTERRUPT_LOCAL_ENABLE - Restore Interrupt Level on Current Processor
---------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_local_enable(
          rtems_interrupt_level level
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive restores the interrupt level specified by ``level`` on the
    current processor.

NOTES:
    The ``level`` parameter value must be obtained by a previous call to
    ``rtems_interrupt_local_disable``.  Using an otherwise obtained value is
    undefined behaviour.

    This directive is unsuitable to enable particular interrupt sources, for
    example in an interrupt controller.

    This directive will not cause the calling task to be preempted.

.. raw:: latex

   \clearpage

.. index:: rtems_interrupt_lock_initialize

.. _rtems_interrupt_lock_initialize:

INTERRUPT_LOCK_INITIALIZE - Initialize an ISR Lock
--------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_lock_initialize(
          rtems_interrupt_lock *lock,
          const char           *name
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    Initializes an interrupt lock.  The name must be persistent throughout the
    lifetime of the lock.

NOTES:
    Concurrent initialization leads to unpredictable results.

.. raw:: latex

   \clearpage

.. index:: rtems_interrupt_lock_acquire

.. _rtems_interrupt_lock_acquire:

INTERRUPT_LOCK_ACQUIRE - Acquire an ISR Lock
--------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_lock_acquire(
          rtems_interrupt_lock         *lock,
          rtems_interrupt_lock_context *lock_context
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    Maskable interrupts will be disabled.  In SMP configurations, this
    directive acquires an SMP lock.

NOTES:
    A separate lock context must be provided for each acquire/release pair, for
    example an automatic variable.

    An attempt to recursively acquire the lock may result in an infinite loop
    with maskable interrupts disabled.

    This directive will not cause the calling thread to be preempted.  This
    directive can be used in thread and interrupt context.

.. raw:: latex

   \clearpage

.. index:: rtems_interrupt_lock_release

.. _rtems_interrupt_lock_release:

INTERRUPT_LOCK_RELEASE - Release an ISR Lock
--------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_lock_release(
          rtems_interrupt_lock         *lock,
          rtems_interrupt_lock_context *lock_context
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    The interrupt level will be restored.  In SMP configurations, this
    directive releases an SMP lock.

NOTES:
    The lock context must be the one used to acquire the lock, otherwise the
    result is unpredictable.

    This directive will not cause the calling thread to be preempted.  This
    directive can be used in thread and interrupt context.

.. raw:: latex

   \clearpage

.. index:: rtems_interrupt_lock_acquire_isr

.. _rtems_interrupt_lock_acquire_isr:

INTERRUPT_LOCK_ACQUIRE_ISR - Acquire an ISR Lock from ISR
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_lock_acquire_isr(
          rtems_interrupt_lock         *lock,
          rtems_interrupt_lock_context *lock_context
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    The interrupt level will remain unchanged.  In SMP configurations, this
    directive acquires an SMP lock.

NOTES:
    A separate lock context must be provided for each acquire/release pair, for
    example an automatic variable.

    An attempt to recursively acquire the lock may result in an infinite loop.

    This directive is intended for device drivers and should be called from the
    corresponding interrupt service routine.

    In case the corresponding interrupt service routine can be interrupted by
    higher priority interrupts and these interrupts enter the critical section
    protected by this lock, then the result is unpredictable.

.. raw:: latex

   \clearpage

.. index:: rtems_interrupt_lock_release_isr

.. _rtems_interrupt_lock_release_isr:

INTERRUPT_LOCK_RELEASE_ISR - Release an ISR Lock from ISR
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_interrupt_lock_release_isr(
          rtems_interrupt_lock         *lock,
          rtems_interrupt_lock_context *lock_context
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    The interrupt level will remain unchanged.  In SMP configurations, this
    directive releases an SMP lock.

NOTES:
    The lock context must be the one used to acquire the lock, otherwise the
    result is unpredictable.

    This directive is intended for device drivers and should be called from the
    corresponding interrupt service routine.

.. raw:: latex

   \clearpage

.. index:: is interrupt in progress
.. index:: rtems_interrupt_is_in_progress

.. _rtems_interrupt_is_in_progress:

INTERRUPT_IS_IN_PROGRESS - Is an ISR in Progress
------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        bool rtems_interrupt_is_in_progress( void );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive returns ``TRUE`` if the processor is currently servicing an
    interrupt and ``FALSE`` otherwise.  A return value of ``TRUE`` indicates
    that the caller is an interrupt service routine, *NOT* a task.  The
    directives available to an interrupt service routine are restricted.

NOTES:
    This directive will not cause the calling task to be preempted.
