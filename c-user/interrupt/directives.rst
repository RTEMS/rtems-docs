.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. _InterruptManagerDirectives:

Directives
==========

This section details the directives of the Interrupt Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/intr/if/catch

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_catch()
.. index:: establish an ISR
.. index:: install an ISR

.. _InterfaceRtemsInterruptCatch:

rtems_interrupt_catch()
-----------------------

Establishes an interrupt service routine.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    rtems_status_code rtems_interrupt_catch(
      rtems_isr_entry     new_isr_handler,
      rtems_vector_number vector,
      rtems_isr_entry    *old_isr_handler
    );

.. rubric:: PARAMETERS:

``new_isr_handler``
    This parameter is the new interrupt service routine.

``vector``
    This parameter is the interrupt vector number.

``old_isr_handler``
    This parameter is the pointer to an :c:type:`rtems_isr_entry` object.  When
    the directive call is successful, the previous interrupt service routine
    established for this interrupt vector will be stored in this object.

.. rubric:: DESCRIPTION:

This directive establishes an interrupt service routine (ISR) for the interrupt
specified by the ``vector`` number.  The ``new_isr_handler`` parameter
specifies the entry point of the ISR.  The entry point of the previous ISR for
the specified vector is returned in ``old_isr_handler``.

To release an interrupt vector, pass the old handler's address obtained when
the vector was first capture.

.. rubric:: RETURN VALUES:

:c:macro:`RTEMS_SUCCESSFUL`
    The requested operation was successful.

:c:macro:`RTEMS_INVALID_NUMBER`
    The interrupt vector number was illegal.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``new_isr_handler`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

:c:macro:`RTEMS_INVALID_ADDRESS`
    The ``old_isr_handler`` parameter was `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within interrupt context.

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive will not cause the calling task to be preempted.

* The directive is only available where the :term:`target architecture` support
  enabled simple vectored interrupts.

.. Generated from spec:/rtems/intr/if/disable

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_disable()
.. index:: disable interrupts

.. _InterfaceRtemsInterruptDisable:

rtems_interrupt_disable()
-------------------------

Disables the maskable interrupts on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_disable( isr_cookie )

.. rubric:: PARAMETERS:

``isr_cookie``
    This parameter is a variable of type :c:type:`rtems_interrupt_level` which
    will be used to save the previous interrupt level.

.. rubric:: DESCRIPTION:

This directive disables all maskable interrupts on the current processor and
returns the previous interrupt level in ``isr_cookie``.

.. rubric:: NOTES:

A later invocation of the :ref:`InterfaceRtemsInterruptEnable` directive should
be used to restore the previous interrupt level.

This directive is implemented as a macro which sets the ``isr_cookie``
parameter.

.. code-block:: c
    :linenos:

    #include <rtems.h>

    void local_critical_section( void )
    {
      rtems_interrupt_level level;

      // Please note that the rtems_interrupt_disable() is a macro.  The
      // previous interrupt level (before the maskable interrupts are
      // disabled) is returned here in the level macro parameter.  This
      // would be wrong:
      //
      // rtems_interrupt_disable( &level );
      rtems_interrupt_disable( level );

      // Here is the critical section: maskable interrupts are disabled

      {
        rtems_interrupt_level nested_level;

        rtems_interrupt_disable( nested_level );

        // Here is a nested critical section

        rtems_interrupt_enable( nested_level );
      }

      // Maskable interrupts are still disabled

      rtems_interrupt_enable( level );
    }

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* Where the system was built with SMP support enabled, the directive is not
  available.  Its use will result in compiler warnings and linker errors.  The
  :ref:`InterfaceRtemsInterruptLocalDisable` and
  :ref:`InterfaceRtemsInterruptLocalEnable` directives are available in all
  build configurations.

.. Generated from spec:/rtems/intr/if/enable

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_enable()
.. index:: enable interrupts
.. index:: restore interrupt level

.. _InterfaceRtemsInterruptEnable:

rtems_interrupt_enable()
------------------------

Restores the previous interrupt level on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_enable( isr_cookie )

.. rubric:: PARAMETERS:

``isr_cookie``
    This parameter is the previous interrupt level to restore.  The value must
    be obtained by a previous call to :ref:`InterfaceRtemsInterruptDisable` or
    :ref:`InterfaceRtemsInterruptFlash`.

.. rubric:: DESCRIPTION:

This directive restores the interrupt level specified by ``isr_cookie`` on the
current processor.

.. rubric:: NOTES:

The ``isr_cookie`` parameter value must be obtained by a previous call to
:ref:`InterfaceRtemsInterruptDisable` or :ref:`InterfaceRtemsInterruptFlash`.
Using an otherwise obtained value is undefined behaviour.

This directive is unsuitable to enable particular interrupt sources, for
example in an interrupt controller.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* While at least one maskable interrupt is pending, when the directive enables
  maskable interrupts, the pending interrupts are immediately serviced.  The
  interrupt service routines may unblock higher priority tasks which may
  preempt the calling task.

* Where the system was built with SMP support enabled, the directive is not
  available.  Its use will result in compiler warnings and linker errors.  The
  :ref:`InterfaceRtemsInterruptLocalDisable` and
  :ref:`InterfaceRtemsInterruptLocalEnable` directives are available in all
  build configurations.

.. Generated from spec:/rtems/intr/if/flash

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_flash()
.. index:: flash interrupts

.. _InterfaceRtemsInterruptFlash:

rtems_interrupt_flash()
-----------------------

Flashes interrupts on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_flash( isr_cookie )

.. rubric:: PARAMETERS:

``isr_cookie``
    This parameter is the previous interrupt level.

.. rubric:: DESCRIPTION:

This directive is functionally equivalent to a calling
:ref:`InterfaceRtemsInterruptEnable` immediately followed by a
:ref:`InterfaceRtemsInterruptDisable`.  On some architectures it is possible to
provide an optimized implementation for this sequence.

.. rubric:: NOTES:

The ``isr_cookie`` parameter value must be obtained by a previous call to
:ref:`InterfaceRtemsInterruptDisable` or :ref:`InterfaceRtemsInterruptFlash`.
Using an otherwise obtained value is undefined behaviour.

Historically, the interrupt flash directive was heavily used in the operating
system implementation.  However, this is no longer the case.  The interrupt
flash directive is provided for backward compatibility reasons.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* Where the system was built with SMP support enabled, the directive is not
  available.  Its use will result in compiler warnings and linker errors.  The
  :ref:`InterfaceRtemsInterruptLocalDisable` and
  :ref:`InterfaceRtemsInterruptLocalEnable` directives are available in all
  build configurations.

.. Generated from spec:/rtems/intr/if/local-disable

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_local_disable()
.. index:: disable interrupts

.. _InterfaceRtemsInterruptLocalDisable:

rtems_interrupt_local_disable()
-------------------------------

Disables the maskable interrupts on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_local_disable( isr_cookie )

.. rubric:: PARAMETERS:

``isr_cookie``
    This parameter is a variable of type :c:type:`rtems_interrupt_level` which
    will be used to save the previous interrupt level.

.. rubric:: DESCRIPTION:

This directive disables all maskable interrupts on the current processor and
returns the previous interrupt level in ``isr_cookie``.

.. rubric:: NOTES:

A later invocation of the :ref:`InterfaceRtemsInterruptLocalEnable` directive
should be used to restore the previous interrupt level.

This directive is implemented as a macro which sets the ``isr_cookie``
parameter.

Where the system was built with SMP support enabled, this will not ensure
system wide mutual exclusion.  Use interrupt locks instead, see
:ref:`InterfaceRtemsInterruptLockAcquire`.  Interrupt disabled critical
sections may be used to access processor-specific data structures or disable
thread dispatching.

.. code-block:: c
    :linenos:

    #include <rtems.h>

    void local_critical_section( void )
    {
      rtems_interrupt_level level;

      // Please note that the rtems_interrupt_local_disable() is a macro.
      // The previous interrupt level (before the maskable interrupts are
      // disabled) is returned here in the level macro parameter.  This would
      // be wrong:
      //
      // rtems_interrupt_local_disable( &level );
      rtems_interrupt_local_disable( level );

      // Here is the critical section: maskable interrupts are disabled

      {
        rtems_interrupt_level nested_level;

        rtems_interrupt_local_disable( nested_level );

        // Here is a nested critical section

        rtems_interrupt_local_enable( nested_level );
      }

      // Maskable interrupts are still disabled

      rtems_interrupt_local_enable( level );
    }

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/local-enable

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_local_enable()
.. index:: enable interrupts
.. index:: restore interrupt level

.. _InterfaceRtemsInterruptLocalEnable:

rtems_interrupt_local_enable()
------------------------------

Restores the previous interrupt level on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_local_enable( isr_cookie )

.. rubric:: PARAMETERS:

``isr_cookie``
    This parameter is the previous interrupt level to restore.  The value must
    be obtained by a previous call to
    :ref:`InterfaceRtemsInterruptLocalDisable`.

.. rubric:: DESCRIPTION:

This directive restores the interrupt level specified by ``isr_cookie`` on the
current processor.

.. rubric:: NOTES:

The ``isr_cookie`` parameter value must be obtained by a previous call to
:ref:`InterfaceRtemsInterruptLocalDisable`.  Using an otherwise obtained value
is undefined behaviour.

This directive is unsuitable to enable particular interrupt sources, for
example in an interrupt controller.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* While at least one maskable interrupt is pending, when the directive enables
  maskable interrupts, the pending interrupts are immediately serviced.  The
  interrupt service routines may unblock higher priority tasks which may
  preempt the calling task.

.. Generated from spec:/rtems/intr/if/is-in-progress

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_is_in_progress()
.. index:: is interrupt in progress

.. _InterfaceRtemsInterruptIsInProgress:

rtems_interrupt_is_in_progress()
--------------------------------

Checks if an ISR is in progress on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_is_in_progress()

.. rubric:: DESCRIPTION:

This directive returns ``true``, if the current processor is currently
servicing an interrupt, and ``false`` otherwise.  A return value of ``true``
indicates that the caller is an interrupt service routine, **not** a task. The
directives available to an interrupt service routine are restricted.

.. rubric:: RETURN VALUES:

Returns true, if the current processor is currently servicing an interrupt,
otherwise false.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/cause

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_cause()

.. _InterfaceRtemsInterruptCause:

rtems_interrupt_cause()
-----------------------

Causes the interrupt.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_cause( vector )

.. rubric:: PARAMETERS:

``vector``
    This parameter is the vector number of the interrupt to cause.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive is not implemented.

.. Generated from spec:/rtems/intr/if/clear

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_clear()

.. _InterfaceRtemsInterruptClear:

rtems_interrupt_clear()
-----------------------

Clears the interrupt.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_clear( vector )

.. rubric:: PARAMETERS:

``vector``
    This parameter is the vector number of the interrupt to clear.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive is not implemented.

.. Generated from spec:/rtems/intr/if/lock-initialize

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_initialize()

.. _InterfaceRtemsInterruptLockInitialize:

rtems_interrupt_lock_initialize()
---------------------------------

Initializes the ISR lock.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_initialize( lock, name )

.. rubric:: PARAMETERS:

``lock``
    This parameter is the ISR lock to initialize.

``name``
    This parameter is the ISR lock name.  It shall be a string.  The name is
    only used where the system was built with profiling support enabled.

.. rubric:: NOTES:

ISR locks may also be statically defined by
:ref:`InterfaceRTEMSINTERRUPTLOCKDEFINE` or statically initialized by
:ref:`InterfaceRTEMSINTERRUPTLOCKINITIALIZER`.

.. Generated from spec:/rtems/intr/if/lock-destroy

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_destroy()

.. _InterfaceRtemsInterruptLockDestroy:

rtems_interrupt_lock_destroy()
------------------------------

Destroys the ISR lock.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_destroy( lock )

.. rubric:: PARAMETERS:

``lock``
    This parameter is the ISR lock to destroy.

.. rubric:: NOTES:

The lock must have been dynamically initialized by
:ref:`InterfaceRtemsInterruptLockInitialize`, statically defined by
:ref:`InterfaceRTEMSINTERRUPTLOCKDEFINE`, or statically initialized by
:ref:`InterfaceRTEMSINTERRUPTLOCKINITIALIZER`.

Concurrent lock use during the destruction or concurrent destruction leads to
unpredictable results.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/lock-acquire

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_acquire()

.. _InterfaceRtemsInterruptLockAcquire:

rtems_interrupt_lock_acquire()
------------------------------

Acquires the ISR lock.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_acquire( lock, lock_context )

.. rubric:: PARAMETERS:

``lock``
    This parameter is the ISR lock to acquire.

``lock_context``
    This parameter is the ISR lock context.  This lock context shall be used to
    release the lock by calling :ref:`InterfaceRtemsInterruptLockRelease`.

.. rubric:: DESCRIPTION:

This directive acquires the ISR lock specified by ``lock`` using the lock
context provided by ``lock_context``.  Maskable interrupts will be disabled on
the current processor.

.. rubric:: NOTES:

A caller-specific lock context shall be provided for each acquire/release pair,
for example an automatic variable.

Where the system was built with SMP support enabled, this directive acquires an
SMP lock.  An attempt to recursively acquire the lock may result in an infinite
loop with maskable interrupts disabled.

This directive establishes a non-preemptive critical section with system wide
mutual exclusion on the local node in all RTEMS build configurations.

.. code-block:: c
    :linenos:

    #include <rtems.h>

    void critical_section( rtems_interrupt_lock *lock )
    {
      rtems_interrupt_lock_context lock_context;

      rtems_interrupt_lock_acquire( lock, &lock_context );

      // Here is the critical section.  Maskable interrupts are disabled.
      // Where the system was built with SMP support enabled, this section
      // is protected by an SMP lock.

      rtems_interrupt_lock_release( lock, &lock_context );
    }

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/lock-release

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_release()

.. _InterfaceRtemsInterruptLockRelease:

rtems_interrupt_lock_release()
------------------------------

Releases the ISR lock.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_release( lock, lock_context )

.. rubric:: PARAMETERS:

``lock``
    This parameter is the ISR lock to release.

``lock_context``
    This parameter is the ISR lock context.  This lock context shall have been
    used to acquire the lock by calling
    :ref:`InterfaceRtemsInterruptLockAcquire`.

.. rubric:: DESCRIPTION:

This directive releases the ISR lock specified by ``lock`` using the lock
context provided by ``lock_context``.  The previous interrupt level will be
restored on the current processor.

.. rubric:: NOTES:

The lock context shall be the one used to acquire the lock, otherwise the
result is unpredictable.

Where the system was built with SMP support enabled, this directive releases an
SMP lock.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* While at least one maskable interrupt is pending, when the directive enables
  maskable interrupts, the pending interrupts are immediately serviced.  The
  interrupt service routines may unblock higher priority tasks which may
  preempt the calling task.

.. Generated from spec:/rtems/intr/if/lock-acquire-isr

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_acquire_isr()

.. _InterfaceRtemsInterruptLockAcquireIsr:

rtems_interrupt_lock_acquire_isr()
----------------------------------

Acquires the ISR lock from within an ISR.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_acquire_isr( lock, lock_context )

.. rubric:: PARAMETERS:

``lock``
    This parameter is the ISR lock to acquire within an ISR.

``lock_context``
    This parameter is the ISR lock context.  This lock context shall be used to
    release the lock by calling :ref:`InterfaceRtemsInterruptLockReleaseIsr`.

.. rubric:: DESCRIPTION:

This directive acquires the ISR lock specified by ``lock`` using the lock
context provided by ``lock_context``.  The interrupt level will remain
unchanged.

.. rubric:: NOTES:

A caller-specific lock context shall be provided for each acquire/release pair,
for example an automatic variable.

Where the system was built with SMP support enabled, this directive acquires an
SMP lock.  An attempt to recursively acquire the lock may result in an infinite
loop.

This directive is intended for device drivers and should be called from the
corresponding interrupt service routine.

In case the corresponding interrupt service routine can be interrupted by
higher priority interrupts and these interrupts enter the critical section
protected by this lock, then the result is unpredictable.  This directive may
be used under specific circumstances as an optimization.  In doubt, use
:ref:`InterfaceRtemsInterruptLockAcquire` and
:ref:`InterfaceRtemsInterruptLockRelease`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/lock-release-isr

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_release_isr()

.. _InterfaceRtemsInterruptLockReleaseIsr:

rtems_interrupt_lock_release_isr()
----------------------------------

Releases the ISR lock from within an ISR.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_release_isr( lock, lock_context )

.. rubric:: PARAMETERS:

``lock``
    This parameter is the ISR lock to release within an ISR.

``lock_context``
    This parameter is the ISR lock context.  This lock context shall have been
    used to acquire the lock by calling
    :ref:`InterfaceRtemsInterruptLockAcquireIsr`.

.. rubric:: DESCRIPTION:

This directive releases the ISR lock specified by ``lock`` using the lock
context provided by ``lock_context``.  The interrupt level will remain
unchanged.

.. rubric:: NOTES:

The lock context shall be the one used to acquire the lock, otherwise the
result is unpredictable.

Where the system was built with SMP support enabled, this directive releases an
SMP lock.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/lock-isr-disable

.. raw:: latex

    \clearpage

.. index:: rtems_interrupt_lock_interrupt_disable()

.. _InterfaceRtemsInterruptLockInterruptDisable:

rtems_interrupt_lock_interrupt_disable()
----------------------------------------

Disables maskable interrupts on the current processor.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define rtems_interrupt_lock_interrupt_disable( lock_context )

.. rubric:: PARAMETERS:

``lock_context``
    This parameter is the ISR lock context for an acquire and release pair.

.. rubric:: DESCRIPTION:

This directive disables maskable interrupts on the current processor and stores
the previous interrupt level in ``lock_context``.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/intr/if/lock-declare

.. raw:: latex

    \clearpage

.. index:: RTEMS_INTERRUPT_LOCK_DECLARE()

.. _InterfaceRTEMSINTERRUPTLOCKDECLARE:

RTEMS_INTERRUPT_LOCK_DECLARE()
------------------------------

Declares an ISR lock object.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define RTEMS_INTERRUPT_LOCK_DECLARE( specifier, designator )

.. rubric:: PARAMETERS:

``specifier``
    This parameter is the storage-class specifier for the ISR lock to declare,
    for example ``extern`` or ``static``.

``designator``
    This parameter is the ISR lock object designator.

.. rubric:: NOTES:

Do not add a ";" after this macro.

.. Generated from spec:/rtems/intr/if/lock-define

.. raw:: latex

    \clearpage

.. index:: RTEMS_INTERRUPT_LOCK_DEFINE()

.. _InterfaceRTEMSINTERRUPTLOCKDEFINE:

RTEMS_INTERRUPT_LOCK_DEFINE()
-----------------------------

Defines an ISR lock object.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define RTEMS_INTERRUPT_LOCK_DEFINE( specifier, designator, name )

.. rubric:: PARAMETERS:

``specifier``
    This parameter is the storage-class specifier for the ISR lock to declare,
    for example ``extern`` or ``static``.

``designator``
    This parameter is the ISR lock object designator.

``name``
    This parameter is the ISR lock name.  It shall be a string.  The name is
    only used where the system was built with profiling support enabled.

.. rubric:: NOTES:

Do not add a ";" after this macro.

ISR locks may also be dynamically initialized by
:ref:`InterfaceRtemsInterruptLockInitialize` or statically by
:ref:`InterfaceRTEMSINTERRUPTLOCKINITIALIZER`.

.. Generated from spec:/rtems/intr/if/lock-initializer

.. raw:: latex

    \clearpage

.. index:: RTEMS_INTERRUPT_LOCK_INITIALIZER()

.. _InterfaceRTEMSINTERRUPTLOCKINITIALIZER:

RTEMS_INTERRUPT_LOCK_INITIALIZER()
----------------------------------

Statically initializes an ISR lock object.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define RTEMS_INTERRUPT_LOCK_INITIALIZER( name )

.. rubric:: PARAMETERS:

``name``
    This parameter is the ISR lock name.  It shall be a string.  The name is
    only used where the system was built with profiling support enabled.

.. rubric:: NOTES:

ISR locks may also be dynamically initialized by
:ref:`InterfaceRtemsInterruptLockInitialize` or statically defined by
:ref:`InterfaceRTEMSINTERRUPTLOCKDEFINE`.

.. Generated from spec:/rtems/intr/if/lock-member

.. raw:: latex

    \clearpage

.. index:: RTEMS_INTERRUPT_LOCK_MEMBER()

.. _InterfaceRTEMSINTERRUPTLOCKMEMBER:

RTEMS_INTERRUPT_LOCK_MEMBER()
-----------------------------

Defines an ISR lock member.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define RTEMS_INTERRUPT_LOCK_MEMBER( designator )

.. rubric:: PARAMETERS:

``designator``
    This parameter is the ISR lock member designator.

.. rubric:: NOTES:

Do not add a ";" after this macro.

.. Generated from spec:/rtems/intr/if/lock-reference

.. raw:: latex

    \clearpage

.. index:: RTEMS_INTERRUPT_LOCK_REFERENCE()

.. _InterfaceRTEMSINTERRUPTLOCKREFERENCE:

RTEMS_INTERRUPT_LOCK_REFERENCE()
--------------------------------

Defines an ISR lock object reference.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    #define RTEMS_INTERRUPT_LOCK_REFERENCE( designator, target )

.. rubric:: PARAMETERS:

``designator``
    This parameter is the ISR lock reference designator.

``target``
    This parameter is the target object to reference.

.. rubric:: NOTES:

Do not add a ";" after this macro.
