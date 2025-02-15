.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
