.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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
