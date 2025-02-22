% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2008, 2024 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

% This file is part of the RTEMS quality process and was automatically

% generated.  If you find something that needs to be fixed or

% worded better please post a report or patch to an RTEMS mailing list

% or raise a bug report:

%

% https://www.rtems.org/bugs.html

%

% For information on updating and regenerating please refer to the How-To

% section in the Software Requirements Engineering chapter of the

% RTEMS Software Engineering manual.  The manual is provided as a part of

% a release.  For development sources please refer to the online

% documentation at:

%

% https://docs.rtems.org

(interruptmanagerdirectives)=

# Directives

This section details the directives of the Interrupt Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/intr/if/catch

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_catch()
```

```{index} establish an ISR
```

```{index} install an ISR
```

(interfacertemsinterruptcatch)=

## rtems_interrupt_catch()

Establishes an interrupt service routine.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_catch(
  rtems_isr_entry     new_isr_handler,
  rtems_vector_number vector,
  rtems_isr_entry    *old_isr_handler
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`new_isr_handler`

: This parameter is the new interrupt service routine.

`vector`

: This parameter is the interrupt vector number.

`old_isr_handler`

: This parameter is the pointer to an {ref}`InterfaceRtemsIsrEntry` object.
  When the directive call is successful, the previous interrupt service
  routine established for this interrupt vector will be stored in this
  object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive establishes an interrupt service routine (ISR) for the interrupt
specified by the `vector` number. The `new_isr_handler` parameter
specifies the entry point of the ISR. The entry point of the previous ISR for
the specified vector is returned in `old_isr_handler`.

To release an interrupt vector, pass the old handler's address obtained when
the vector was first capture.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_NUMBER`

: The interrupt vector number was illegal.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `new_isr_handler` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `old_isr_handler` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.
- The directive is only available where the {term}`target architecture` support
  enabled simple vectored interrupts.

% Generated from spec:/rtems/intr/if/disable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_disable()
```

```{index} disable interrupts
```

(interfacertemsinterruptdisable)=

## rtems_interrupt_disable()

Disables the maskable interrupts on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_disable( rtems_interrupt_level isr_cookie );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`isr_cookie`

: This parameter is a variable of type {ref}`InterfaceRtemsInterruptLevel`
  which will be used to save the previous interrupt level.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive disables all maskable interrupts on the current processor and
returns the previous interrupt level in `isr_cookie`.

```{eval-rst}
.. rubric:: NOTES:
```

A later invocation of the {ref}`InterfaceRtemsInterruptEnable` directive should
be used to restore the previous interrupt level.

This directive is implemented as a macro which sets the `isr_cookie`
parameter.

```{code-block} c
:linenos: true

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
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.
- Where the system was built with SMP support enabled, the directive is not
  available. Its use will result in compiler warnings and linker errors. The
  {ref}`InterfaceRtemsInterruptLocalDisable` and
  {ref}`InterfaceRtemsInterruptLocalEnable` directives are available in all
  build configurations.

% Generated from spec:/rtems/intr/if/enable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_enable()
```

```{index} enable interrupts
```

```{index} restore interrupt level
```

(interfacertemsinterruptenable)=

## rtems_interrupt_enable()

Restores the previous interrupt level on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_enable( rtems_interrupt_level isr_cookie );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`isr_cookie`

: This parameter is the previous interrupt level to restore. The value must
  be obtained by a previous call to {ref}`InterfaceRtemsInterruptDisable` or
  {ref}`InterfaceRtemsInterruptFlash`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive restores the interrupt level specified by `isr_cookie` on the
current processor.

```{eval-rst}
.. rubric:: NOTES:
```

The `isr_cookie` parameter value must be obtained by a previous call to
{ref}`InterfaceRtemsInterruptDisable` or {ref}`InterfaceRtemsInterruptFlash`.
Using an otherwise obtained value is undefined behaviour.

This directive is unsuitable to enable particular interrupt sources, for
example in an interrupt controller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.
- While at least one maskable interrupt is pending, when the directive enables
  maskable interrupts, the pending interrupts are immediately serviced. The
  interrupt service routines may unblock higher priority tasks which may
  preempt the calling task.
- Where the system was built with SMP support enabled, the directive is not
  available. Its use will result in compiler warnings and linker errors. The
  {ref}`InterfaceRtemsInterruptLocalDisable` and
  {ref}`InterfaceRtemsInterruptLocalEnable` directives are available in all
  build configurations.

% Generated from spec:/rtems/intr/if/flash

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_flash()
```

```{index} flash interrupts
```

(interfacertemsinterruptflash)=

## rtems_interrupt_flash()

Flashes interrupts on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_flash( rtems_interrupt_level isr_cookie );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`isr_cookie`

: This parameter is the previous interrupt level.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive is functionally equivalent to a calling
{ref}`InterfaceRtemsInterruptEnable` immediately followed by a
{ref}`InterfaceRtemsInterruptDisable`. On some architectures it is possible to
provide an optimized implementation for this sequence.

```{eval-rst}
.. rubric:: NOTES:
```

The `isr_cookie` parameter value must be obtained by a previous call to
{ref}`InterfaceRtemsInterruptDisable` or {ref}`InterfaceRtemsInterruptFlash`.
Using an otherwise obtained value is undefined behaviour.

Historically, the interrupt flash directive was heavily used in the operating
system implementation. However, this is no longer the case. The interrupt
flash directive is provided for backward compatibility reasons.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.
- Where the system was built with SMP support enabled, the directive is not
  available. Its use will result in compiler warnings and linker errors. The
  {ref}`InterfaceRtemsInterruptLocalDisable` and
  {ref}`InterfaceRtemsInterruptLocalEnable` directives are available in all
  build configurations.

% Generated from spec:/rtems/intr/if/local-disable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_local_disable()
```

```{index} disable interrupts
```

(interfacertemsinterruptlocaldisable)=

## rtems_interrupt_local_disable()

Disables the maskable interrupts on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_local_disable( rtems_interrupt_level isr_cookie );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`isr_cookie`

: This parameter is a variable of type {ref}`InterfaceRtemsInterruptLevel`
  which will be used to save the previous interrupt level.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive disables all maskable interrupts on the current processor and
returns the previous interrupt level in `isr_cookie`.

```{eval-rst}
.. rubric:: NOTES:
```

A later invocation of the {ref}`InterfaceRtemsInterruptLocalEnable` directive
should be used to restore the previous interrupt level.

This directive is implemented as a macro which sets the `isr_cookie`
parameter.

Where the system was built with SMP support enabled, this will not ensure
system wide mutual exclusion. Use interrupt locks instead, see
{ref}`InterfaceRtemsInterruptLockAcquire`. Interrupt disabled critical
sections may be used to access processor-specific data structures or disable
thread dispatching.

```{code-block} c
:linenos: true

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
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/local-enable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_local_enable()
```

```{index} enable interrupts
```

```{index} restore interrupt level
```

(interfacertemsinterruptlocalenable)=

## rtems_interrupt_local_enable()

Restores the previous interrupt level on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_local_enable( rtems_interrupt_level isr_cookie );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`isr_cookie`

: This parameter is the previous interrupt level to restore. The value must
  be obtained by a previous call to
  {ref}`InterfaceRtemsInterruptLocalDisable`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive restores the interrupt level specified by `isr_cookie` on the
current processor.

```{eval-rst}
.. rubric:: NOTES:
```

The `isr_cookie` parameter value must be obtained by a previous call to
{ref}`InterfaceRtemsInterruptLocalDisable`. Using an otherwise obtained value
is undefined behaviour.

This directive is unsuitable to enable particular interrupt sources, for
example in an interrupt controller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.
- While at least one maskable interrupt is pending, when the directive enables
  maskable interrupts, the pending interrupts are immediately serviced. The
  interrupt service routines may unblock higher priority tasks which may
  preempt the calling task.

% Generated from spec:/rtems/intr/if/is-in-progress

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_is_in_progress()
```

```{index} is interrupt in progress
```

(interfacertemsinterruptisinprogress)=

## rtems_interrupt_is_in_progress()

Checks if an ISR is in progress on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
bool rtems_interrupt_is_in_progress( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns `true`, if the current processor is currently
servicing an interrupt, and `false` otherwise. A return value of `true`
indicates that the caller is an interrupt service routine, **not** a task. The
directives available to an interrupt service routine are restricted.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns true, if the current processor is currently servicing an interrupt,
otherwise false.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/lock-initialize

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_initialize()
```

(interfacertemsinterruptlockinitialize)=

## rtems_interrupt_lock_initialize()

Initializes the ISR lock.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_initialize(
  rtems_interrupt_lock *lock,
  const char           *name
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock`

: This parameter is the ISR lock to initialize.

`name`

: This parameter is the ISR lock name. It shall be a string. The name is
  only used where the system was built with profiling support enabled.

```{eval-rst}
.. rubric:: NOTES:
```

ISR locks may also be statically defined by
{ref}`InterfaceRTEMSINTERRUPTLOCKDEFINE` or statically initialized by
{ref}`InterfaceRTEMSINTERRUPTLOCKINITIALIZER`.

% Generated from spec:/rtems/intr/if/lock-destroy

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_destroy()
```

(interfacertemsinterruptlockdestroy)=

## rtems_interrupt_lock_destroy()

Destroys the ISR lock.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_destroy( rtems_interrupt_lock *lock );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock`

: This parameter is the ISR lock to destroy.

```{eval-rst}
.. rubric:: NOTES:
```

The lock must have been dynamically initialized by
{ref}`InterfaceRtemsInterruptLockInitialize`, statically defined by
{ref}`InterfaceRTEMSINTERRUPTLOCKDEFINE`, or statically initialized by
{ref}`InterfaceRTEMSINTERRUPTLOCKINITIALIZER`.

Concurrent lock use during the destruction or concurrent destruction leads to
unpredictable results.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/lock-acquire

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_acquire()
```

(interfacertemsinterruptlockacquire)=

## rtems_interrupt_lock_acquire()

Acquires the ISR lock.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_acquire(
  rtems_interrupt_lock         *lock,
  rtems_interrupt_lock_context *lock_context
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock`

: This parameter is the ISR lock to acquire.

`lock_context`

: This parameter is the ISR lock context. This lock context shall be used to
  release the lock by calling {ref}`InterfaceRtemsInterruptLockRelease`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive acquires the ISR lock specified by `lock` using the lock
context provided by `lock_context`. Maskable interrupts will be disabled on
the current processor.

```{eval-rst}
.. rubric:: NOTES:
```

A caller-specific lock context shall be provided for each acquire/release pair,
for example an automatic variable.

Where the system was built with SMP support enabled, this directive acquires an
SMP lock. An attempt to recursively acquire the lock may result in an infinite
loop with maskable interrupts disabled.

This directive establishes a non-preemptive critical section with system wide
mutual exclusion on the local node in all RTEMS build configurations.

```{code-block} c
:linenos: true

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
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/lock-release

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_release()
```

(interfacertemsinterruptlockrelease)=

## rtems_interrupt_lock_release()

Releases the ISR lock.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_release( rtems_interrupt_lock_context *lock );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock`

: This parameter is the ISR lock to release.

`lock_context`

: This parameter is the ISR lock context. This lock context shall have been
  used to acquire the lock by calling
  {ref}`InterfaceRtemsInterruptLockAcquire`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive releases the ISR lock specified by `lock` using the lock
context provided by `lock_context`. The previous interrupt level will be
restored on the current processor.

```{eval-rst}
.. rubric:: NOTES:
```

The lock context shall be the one used to acquire the lock, otherwise the
result is unpredictable.

Where the system was built with SMP support enabled, this directive releases an
SMP lock.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.
- While at least one maskable interrupt is pending, when the directive enables
  maskable interrupts, the pending interrupts are immediately serviced. The
  interrupt service routines may unblock higher priority tasks which may
  preempt the calling task.

% Generated from spec:/rtems/intr/if/lock-acquire-isr

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_acquire_isr()
```

(interfacertemsinterruptlockacquireisr)=

## rtems_interrupt_lock_acquire_isr()

Acquires the ISR lock from within an ISR.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_acquire_isr(
  rtems_interrupt_lock         *lock,
  rtems_interrupt_lock_context *lock_context
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock`

: This parameter is the ISR lock to acquire within an ISR.

`lock_context`

: This parameter is the ISR lock context. This lock context shall be used to
  release the lock by calling {ref}`InterfaceRtemsInterruptLockReleaseIsr`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive acquires the ISR lock specified by `lock` using the lock
context provided by `lock_context`. The interrupt level will remain
unchanged.

```{eval-rst}
.. rubric:: NOTES:
```

A caller-specific lock context shall be provided for each acquire/release pair,
for example an automatic variable.

Where the system was built with SMP support enabled, this directive acquires an
SMP lock. An attempt to recursively acquire the lock may result in an infinite
loop.

This directive is intended for device drivers and should be called from the
corresponding interrupt service routine.

In case the corresponding interrupt service routine can be interrupted by
higher priority interrupts and these interrupts enter the critical section
protected by this lock, then the result is unpredictable. This directive may
be used under specific circumstances as an optimization. In doubt, use
{ref}`InterfaceRtemsInterruptLockAcquire` and
{ref}`InterfaceRtemsInterruptLockRelease`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/lock-release-isr

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_release_isr()
```

(interfacertemsinterruptlockreleaseisr)=

## rtems_interrupt_lock_release_isr()

Releases the ISR lock from within an ISR.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_release_isr(
  rtems_interrupt_lock         *lock,
  rtems_interrupt_lock_context *lock_context
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock`

: This parameter is the ISR lock to release within an ISR.

`lock_context`

: This parameter is the ISR lock context. This lock context shall have been
  used to acquire the lock by calling
  {ref}`InterfaceRtemsInterruptLockAcquireIsr`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive releases the ISR lock specified by `lock` using the lock
context provided by `lock_context`. The interrupt level will remain
unchanged.

```{eval-rst}
.. rubric:: NOTES:
```

The lock context shall be the one used to acquire the lock, otherwise the
result is unpredictable.

Where the system was built with SMP support enabled, this directive releases an
SMP lock.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/lock-isr-disable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_lock_interrupt_disable()
```

(interfacertemsinterruptlockinterruptdisable)=

## rtems_interrupt_lock_interrupt_disable()

Disables maskable interrupts on the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_lock_interrupt_disable(
  rtems_interrupt_lock_context *lock_context
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`lock_context`

: This parameter is the ISR lock context for an acquire and release pair.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive disables maskable interrupts on the current processor and stores
the previous interrupt level in `lock_context`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/lock-declare

```{raw} latex
\clearpage
```

```{index} RTEMS_INTERRUPT_LOCK_DECLARE()
```

(interfacertemsinterruptlockdeclare)=

## RTEMS_INTERRUPT_LOCK_DECLARE()

Declares an ISR lock object.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
RTEMS_INTERRUPT_LOCK_DECLARE( specifier, designator );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`specifier`

: This parameter is the storage-class specifier for the ISR lock to declare,
  for example `extern` or `static`.

`designator`

: This parameter is the ISR lock object designator.

```{eval-rst}
.. rubric:: NOTES:
```

Do not add a ";" after this macro.

% Generated from spec:/rtems/intr/if/lock-define

```{raw} latex
\clearpage
```

```{index} RTEMS_INTERRUPT_LOCK_DEFINE()
```

(interfacertemsinterruptlockdefine)=

## RTEMS_INTERRUPT_LOCK_DEFINE()

Defines an ISR lock object.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
RTEMS_INTERRUPT_LOCK_DEFINE( specifier, designator, const char *name );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`specifier`

: This parameter is the storage-class specifier for the ISR lock to declare,
  for example `extern` or `static`.

`designator`

: This parameter is the ISR lock object designator.

`name`

: This parameter is the ISR lock name. It shall be a string. The name is
  only used where the system was built with profiling support enabled.

```{eval-rst}
.. rubric:: NOTES:
```

Do not add a ";" after this macro.

ISR locks may also be dynamically initialized by
{ref}`InterfaceRtemsInterruptLockInitialize` or statically by
{ref}`InterfaceRTEMSINTERRUPTLOCKINITIALIZER`.

% Generated from spec:/rtems/intr/if/lock-initializer

```{raw} latex
\clearpage
```

```{index} RTEMS_INTERRUPT_LOCK_INITIALIZER()
```

(interfacertemsinterruptlockinitializer)=

## RTEMS_INTERRUPT_LOCK_INITIALIZER()

Statically initializes an ISR lock object.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
RTEMS_INTERRUPT_LOCK_INITIALIZER( const char *name );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`name`

: This parameter is the ISR lock name. It shall be a string. The name is
  only used where the system was built with profiling support enabled.

```{eval-rst}
.. rubric:: NOTES:
```

ISR locks may also be dynamically initialized by
{ref}`InterfaceRtemsInterruptLockInitialize` or statically defined by
{ref}`InterfaceRTEMSINTERRUPTLOCKDEFINE`.

% Generated from spec:/rtems/intr/if/lock-member

```{raw} latex
\clearpage
```

```{index} RTEMS_INTERRUPT_LOCK_MEMBER()
```

(interfacertemsinterruptlockmember)=

## RTEMS_INTERRUPT_LOCK_MEMBER()

Defines an ISR lock member.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
RTEMS_INTERRUPT_LOCK_MEMBER( designator );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`designator`

: This parameter is the ISR lock member designator.

```{eval-rst}
.. rubric:: NOTES:
```

Do not add a ";" after this macro.

% Generated from spec:/rtems/intr/if/lock-reference

```{raw} latex
\clearpage
```

```{index} RTEMS_INTERRUPT_LOCK_REFERENCE()
```

(interfacertemsinterruptlockreference)=

## RTEMS_INTERRUPT_LOCK_REFERENCE()

Defines an ISR lock object reference.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
RTEMS_INTERRUPT_LOCK_REFERENCE( designator, rtems_interrupt_lock *target );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`designator`

: This parameter is the ISR lock reference designator.

`target`

: This parameter is the target object to reference.

```{eval-rst}
.. rubric:: NOTES:
```

Do not add a ";" after this macro.

% Generated from spec:/rtems/intr/if/entry-initializer

```{raw} latex
\clearpage
```

```{index} RTEMS_INTERRUPT_ENTRY_INITIALIZER()
```

(interfacertemsinterruptentryinitializer)=

## RTEMS_INTERRUPT_ENTRY_INITIALIZER()

Statically initializes an interrupt entry object.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
RTEMS_INTERRUPT_ENTRY_INITIALIZER(
  rtems_interrupt_handler routine,
  void                   *arg,
  const char             *info
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`routine`

: This parameter is the interrupt handler routine for the entry.

`arg`

: This parameter is the interrupt handler argument for the entry.

`info`

: This parameter is the descriptive information for the entry.

```{eval-rst}
.. rubric:: NOTES:
```

Alternatively, {ref}`InterfaceRtemsInterruptEntryInitialize` may be used to
dynamically initialize an interrupt entry.

% Generated from spec:/rtems/intr/if/entry-initialize

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_entry_initialize()
```

(interfacertemsinterruptentryinitialize)=

## rtems_interrupt_entry_initialize()

Initializes the interrupt entry.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_entry_initialize(
  rtems_interrupt_entry  *entry,
  rtems_interrupt_handler routine,
  void                   *arg,
  const char             *info
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`entry`

: This parameter is the interrupt entry to initialize.

`routine`

: This parameter is the interrupt handler routine for the entry.

`arg`

: This parameter is the interrupt handler argument for the entry.

`info`

: This parameter is the descriptive information for the entry.

```{eval-rst}
.. rubric:: NOTES:
```

Alternatively, {ref}`InterfaceRTEMSINTERRUPTENTRYINITIALIZER` may be used to
statically initialize an interrupt entry.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/entry-install

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_entry_install()
```

(interfacertemsinterruptentryinstall)=

## rtems_interrupt_entry_install()

Installs the interrupt entry at the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_entry_install(
  rtems_vector_number    vector,
  rtems_option           options,
  rtems_interrupt_entry *entry
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`options`

: This parameter is the interrupt entry install option set.

`entry`

: This parameter is the interrupt entry to install.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

One of the following mutually exclusive options

- {c:macro}`RTEMS_INTERRUPT_UNIQUE`, and
- {c:macro}`RTEMS_INTERRUPT_SHARED`

shall be set in the `options` parameter.

The handler routine of the entry specified by `entry` will be called with the
handler argument of the entry when dispatched. The order in which shared
interrupt handlers are dispatched for one vector is defined by the installation
order. The first installed handler is dispatched first.

If the option {c:macro}`RTEMS_INTERRUPT_UNIQUE` is set, then it will be ensured
that the handler will be the only one for the interrupt vector.

If the option {c:macro}`RTEMS_INTERRUPT_SHARED` is set, then multiple handlers
may be installed for the interrupt vector.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `entry` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INCORRECT_STATE`

: The service was not initialized.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The handler routine of the entry was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

{c:macro}`RTEMS_INVALID_NUMBER`

: An option specified by `options` was not applicable.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The {c:macro}`RTEMS_INTERRUPT_UNIQUE` option was set in `entry` and the
  interrupt vector was already occupied by a handler.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The {c:macro}`RTEMS_INTERRUPT_SHARED` option was set in `entry` and the
  interrupt vector was already occupied by a unique handler.

{c:macro}`RTEMS_TOO_MANY`

: The handler routine of the entry specified by `entry` was already
  installed for the interrupt vector specified by `vector` with an argument
  equal to the handler argument of the entry.

```{eval-rst}
.. rubric:: NOTES:
```

When the directive call was successful, the ownership of the interrupt entry
has been transferred from the caller to the interrupt service. An installed
interrupt entry may be removed from the interrupt service by calling
{ref}`InterfaceRtemsInterruptEntryRemove`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- The interrupt entry shall have been initialized by
  {ref}`InterfaceRtemsInterruptEntryInitialize` or
  {ref}`InterfaceRTEMSINTERRUPTENTRYINITIALIZER`.

% Generated from spec:/rtems/intr/if/entry-remove

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_entry_remove()
```

(interfacertemsinterruptentryremove)=

## rtems_interrupt_entry_remove()

Removes the interrupt entry from the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_entry_remove(
  rtems_vector_number    vector,
  rtems_interrupt_entry *entry
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`entry`

: This parameter is the interrupt entry to remove.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INCORRECT_STATE`

: The service was not initialized.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `entry` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

{c:macro}`RTEMS_UNSATISFIED`

: The entry specified by `entry` was not installed at the interrupt vector
  specified by `vector`.

```{eval-rst}
.. rubric:: NOTES:
```

When the directive call was successful, the ownership of the interrupt entry
has been transferred from the interrupt service to the caller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- The interrupt entry shall have been installed by
  {ref}`InterfaceRtemsInterruptEntryInstall`.

% Generated from spec:/rtems/intr/if/handler-install

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_handler_install()
```

(interfacertemsinterrupthandlerinstall)=

## rtems_interrupt_handler_install()

Installs the interrupt handler routine and argument at the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_handler_install(
  rtems_vector_number     vector,
  const char             *info,
  rtems_option            options,
  rtems_interrupt_handler routine,
  void                   *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`info`

: This parameter is the descriptive information of the interrupt handler to
  install.

`options`

: This parameter is the interrupt handler install option set.

`routine`

: This parameter is the interrupt handler routine to install.

`arg`

: This parameter is the interrupt handler argument to install.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

One of the following mutually exclusive options

- {c:macro}`RTEMS_INTERRUPT_UNIQUE`,
- {c:macro}`RTEMS_INTERRUPT_SHARED`, and
- {c:macro}`RTEMS_INTERRUPT_REPLACE`

shall be set in the `options` parameter.

The handler routine will be called with the argument specified by `arg` when
dispatched. The order in which shared interrupt handlers are dispatched for
one vector is defined by the installation order. The first installed handler
is dispatched first.

If the option {c:macro}`RTEMS_INTERRUPT_UNIQUE` is set, then it will be ensured
that the handler will be the only one for the interrupt vector.

If the option {c:macro}`RTEMS_INTERRUPT_SHARED` is set, then multiple handler
may be installed for the interrupt vector.

If the option {c:macro}`RTEMS_INTERRUPT_REPLACE` is set, then the handler
specified by `routine` will replace the first handler with the same argument
for the interrupt vector if it exists, otherwise an error status will be
returned. A second handler with the same argument for the interrupt vector
will remain unchanged. The new handler will inherit the unique or shared
options from the replaced handler.

An informative description may be provided in `info`. It may be used for
system debugging and diagnostic tools. The referenced string has to be
persistent as long as the handler is installed.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INCORRECT_STATE`

: The service was not initialized.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `routine` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

{c:macro}`RTEMS_NO_MEMORY`

: There was not enough memory available to allocate data structures to
  install the handler.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The {c:macro}`RTEMS_INTERRUPT_UNIQUE` option was set in `options` and the
  interrupt vector was already occupied by a handler.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The {c:macro}`RTEMS_INTERRUPT_SHARED` option was set in `options` and the
  interrupt vector was already occupied by a unique handler.

{c:macro}`RTEMS_TOO_MANY`

: The handler specified by `routine` was already installed for the
  interrupt vector specified by `vector` with an argument equal to the
  argument specified by `arg`.

{c:macro}`RTEMS_UNSATISFIED`

: The {c:macro}`RTEMS_INTERRUPT_REPLACE` option was set in `options` and no
  handler to replace was installed.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/handler-remove

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_handler_remove()
```

(interfacertemsinterrupthandlerremove)=

## rtems_interrupt_handler_remove()

Removes the interrupt handler routine and argument from the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_handler_remove(
  rtems_vector_number     vector,
  rtems_interrupt_handler routine,
  void                   *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`routine`

: This parameter is the interrupt handler routine to remove.

`arg`

: This parameter is the interrupt handler argument to remove.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INCORRECT_STATE`

: The service was not initialized.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `routine` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

{c:macro}`RTEMS_UNSATISFIED`

: There was no handler routine and argument pair installed specified by
  `routine` and `arg`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/vector-is-enabled

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_vector_is_enabled()
```

(interfacertemsinterruptvectorisenabled)=

## rtems_interrupt_vector_is_enabled()

Checks if the interrupt vector is enabled.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_vector_is_enabled(
  rtems_vector_number vector,
  bool               *enabled
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`enabled`

: This parameter is the pointer to a `bool` object. When the directive
  call is successful, the enabled status of the interrupt associated with the
  interrupt vector specified by `vector` will be stored in this object.
  When the interrupt was enabled for the processor executing the directive
  call at some time point during the call, the object value will be set to
  {c:macro}`true`, otherwise to {c:macro}`false`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive checks if the interrupt associated with the interrupt vector
specified by `vector` was enabled for the processor executing the directive
call at some time point during the call.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `enabled` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

```{eval-rst}
.. rubric:: NOTES:
```

Interrupt vectors may be enabled by {ref}`InterfaceRtemsInterruptVectorEnable`
and disabled by {ref}`InterfaceRtemsInterruptVectorDisable`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/vector-enable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_vector_enable()
```

(interfacertemsinterruptvectorenable)=

## rtems_interrupt_vector_enable()

Enables the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_vector_enable( rtems_vector_number vector );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the number of the interrupt vector to enable.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive enables the interrupt vector specified by `vector`. This allows
that interrupt service requests are issued to the target processors of the
interrupt vector. Interrupt service requests for an interrupt vector may be
raised by {ref}`InterfaceRtemsInterruptRaise`,
{ref}`InterfaceRtemsInterruptRaiseOn`, external signals, or messages.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: The request to enable the interrupt vector has not been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to check
if an interrupt vector can be enabled. Interrupt vectors may be disabled by
{ref}`InterfaceRtemsInterruptVectorDisable`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/vector-disable

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_vector_disable()
```

(interfacertemsinterruptvectordisable)=

## rtems_interrupt_vector_disable()

Disables the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_vector_disable( rtems_vector_number vector );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the number of the interrupt vector to disable.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive disables the interrupt vector specified by `vector`. This
prevents that an interrupt service request is issued to the target processors
of the interrupt vector.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: The request to disable the interrupt vector has not been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to check
if an interrupt vector can be disabled. Interrupt vectors may be enabled by
{ref}`InterfaceRtemsInterruptVectorEnable`. There may be targets on which some
interrupt vectors cannot be disabled, for example a hardware watchdog interrupt
or software generated interrupts.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/is-pending

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_is_pending()
```

(interfacertemsinterruptispending)=

## rtems_interrupt_is_pending()

Checks if the interrupt is pending.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_is_pending(
  rtems_vector_number vector,
  bool               *pending
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`pending`

: This parameter is the pointer to a `bool` object. When the directive
  call is successful, the pending status of the interrupt associated with the
  interrupt vector specified by `vector` will be stored in this object.
  When the interrupt was pending for the processor executing the directive
  call at some time point during the call, the object value will be set to
  {c:macro}`true`, otherwise to {c:macro}`false`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive checks if the interrupt associated with the interrupt vector
specified by `vector` was pending for the processor executing the directive
call at some time point during the call.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `pending` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: The request to get the pending status has not been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

Interrupts may be made pending by calling the
{ref}`InterfaceRtemsInterruptRaise` or {ref}`InterfaceRtemsInterruptRaiseOn`
directives or due to external signals or messages. The pending state may be
cleared by {ref}`InterfaceRtemsInterruptClear`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/raise

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_raise()
```

(interfacertemsinterruptraise)=

## rtems_interrupt_raise()

Raises the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_raise( rtems_vector_number vector );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the number of the interrupt vector to raise.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: The request to raise the interrupt vector has not been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to check
if an interrupt vector can be raised.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/raise-on

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_raise_on()
```

(interfacertemsinterruptraiseon)=

## rtems_interrupt_raise_on()

Raises the interrupt vector on the processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_raise_on(
  rtems_vector_number vector,
  uint32_t            cpu_index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the number of the interrupt vector to raise.

`cpu_index`

: This parameter is the index of the target processor of the interrupt vector
  to raise.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_NOT_CONFIGURED`

: The processor specified by `cpu_index` was not configured to be used by
  the application.

{c:macro}`RTEMS_INCORRECT_STATE`

: The processor specified by `cpu_index` was configured to be used by the
  application, however, it was not online.

{c:macro}`RTEMS_UNSATISFIED`

: The request to raise the interrupt vector has not been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to check
if an interrupt vector can be raised on a processor.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/clear

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_clear()
```

(interfacertemsinterruptclear)=

## rtems_interrupt_clear()

Clears the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_clear( rtems_vector_number vector );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the number of the interrupt vector to clear.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: The request to raise the interrupt vector has not been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to check
if an interrupt vector can be cleared.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/get-priority

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_get_priority()
```

(interfacertemsinterruptgetpriority)=

## rtems_interrupt_get_priority()

Gets the priority of the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_get_priority(
  rtems_vector_number vector,
  uint32_t           *priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`priority`

: This parameter is the pointer to an [uint32_t](https://en.cppreference.com/w/c/types/integer) object. When the
  directive call is successful, the priority of the interrupt vector will be
  stored in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `priority` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: There is no priority associated with the interrupt vector.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptSetPriority` directive may be used to set the
priority associated with an interrupt vector.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/set-priority

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_set_priority()
```

(interfacertemsinterruptsetpriority)=

## rtems_interrupt_set_priority()

Sets the priority of the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_set_priority(
  rtems_vector_number vector,
  uint32_t            priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`priority`

: This parameter is the new priority for the interrupt vector.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive sets the priority of the interrupt specified by `vector` to
the priority specified by `priority`.

For processor-specific interrupts, the priority of the interrupt specific to a
processor executing the directive call will be set.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_INVALID_PRIORITY`

: The priority specified by `priority` was not a valid new priority for the
  interrupt vector.

{c:macro}`RTEMS_UNSATISFIED`

: The request to set the priority of the interrupt vector has not been
  satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetPriority` directive may be used to get the
priority associated with an interrupt vector.

The interrupt prioritization support depends on the interrupt controller of the
{term}`target`. It is strongly recommended to read the relevant hardware
documentation. What happens when the priority of a pending or active interrupt
is changed, depends on the interrupt controller. In general, you should set
the interrupt priority of an interrupt vector before a handler is installed.
On some interrupt controllers, setting the priority to the maximum value
(lowest importance) effectively disables the interrupt.

On some architectures, a range of interrupt priority values may be not disabled
by the interrupt disable directives such as
{ref}`InterfaceRtemsInterruptDisable` and
{ref}`InterfaceRtemsInterruptLocalDisable`. These interrupts are called
non-maskable interrupts. Handlers of non-maskable interrupts shall not use
operating system services. In addition, non-maskable interrupts may be not
installable through {ref}`InterfaceRtemsInterruptEntryInstall` or
{ref}`InterfaceRtemsInterruptHandlerInstall`, and may require
architecture-specific prologue and epilogue code.

The interrupt priority settings affect the maximum nesting depth while
servicing interrupts. The interrupt stack size calculation needs to take this
into account, see also {ref}`CONFIGURE_INTERRUPT_STACK_SIZE`.

For the ARM Generic Interrupt Controller (GIC), an 8-bit priority value is
supported. The granularity of the priority levels depends on the interrupt
controller configuration. Some low-order bits of a priority value may be
read-as-zero (RAZ) and writes are ignored (WI). Where group 0 (FIQ) and group
1 (IRQ) interrupts are used, it is recommended to use the lower half of the
supported priority value range for the group 0 interrupts and the upper half
for group 1 interrupts. This ensures that group 1 interrupts cannot preempt
group 0 interrupts.

For the Armv7-M Nested Vector Interrupt Controller (NVIC), an 8-bit priority
value is supported. The granularity of the priority levels depends on the
interrupt controller configuration. Some lower bits of a priority value may be
read-as-zero (RAZ) and writes are ignored (WI). Interrupts with a priority
value less than 128 are not disabled by the RTEMS interrupt disable directives.
Handlers of such interrupts shall not use operating system services.

For the RISC-V Platform-Level Interrupt Controller (PLIC), all priority values
from 0 up to and including the 0xffffffff are supported since the priority for
the PLIC is defined by a write-any-read-legal (WARL) register. Please note that
for this directive in contrast to the PLIC, a higher priority value is
associated with a lower importance. The maximum priority value (mapped to the
value 0 for the PLIC) is reserved to mean "never interrupt" and effectively
disables the interrupt.

For the QorIQ Multicore Programmable Interrupt Controller (MPIC), a 4-bit
priority value is supported. Please note that for this directive in contrast
to the MPIC, a higher priority value is associated with a lower importance. The
maximum priority value of 15 (mapped to the value 0 for the MPIC) inhibits
signalling of this interrupt.

Consult the *RTEMS CPU Architecture Supplement* and the {term}`BSP`
documentation in the *RTEMS User Manual* for further information.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/get-affinity

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_get_affinity()
```

(interfacertemsinterruptgetaffinity)=

## rtems_interrupt_get_affinity()

Gets the processor affinity set of the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_get_affinity(
  rtems_vector_number vector,
  size_t              affinity_size,
  cpu_set_t          *affinity
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`affinity_size`

: This parameter is the size of the processor set referenced by `affinity`
  in bytes.

`affinity`

: This parameter is the pointer to a {c:type}`cpu_set_t` object. When the
  directive call is successful, the processor affinity set of the interrupt
  vector will be stored in this object. A set bit in the processor set means
  that the corresponding processor is in the processor affinity set of the
  interrupt vector, otherwise the bit is cleared.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `affinity` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_INVALID_SIZE`

: The size specified by `affinity_size` of the processor set was too small
  for the processor affinity set of the interrupt vector.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/set-affinity

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_set_affinity()
```

(interfacertemsinterruptsetaffinity)=

## rtems_interrupt_set_affinity()

Sets the processor affinity set of the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_set_affinity(
  rtems_vector_number vector,
  size_t              affinity_size,
  const cpu_set_t    *affinity
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`affinity_size`

: This parameter is the size of the processor set referenced by `affinity`
  in bytes.

`affinity`

: This parameter is the pointer to a {c:type}`cpu_set_t` object. The
  processor set defines the new processor affinity set of the interrupt
  vector. A set bit in the processor set means that the corresponding
  processor shall be in the processor affinity set of the interrupt vector,
  otherwise the bit shall be cleared.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `affinity` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_INVALID_NUMBER`

: The referenced processor set was not a valid new processor affinity set for
  the interrupt vector.

{c:macro}`RTEMS_UNSATISFIED`

: The request to set the processor affinity of the interrupt vector has not
  been satisfied.

```{eval-rst}
.. rubric:: NOTES:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to check
if the processor affinity of an interrupt vector can be set.

Only online processors of the affinity set specified by `affinity_size` and
`affinity` are considered by the directive. Other processors of the set are
ignored. If the set contains no online processor, then the set is invalid and
an error status is returned.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/get-attributes

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_get_attributes()
```

(interfacertemsinterruptgetattributes)=

## rtems_interrupt_get_attributes()

Gets the attributes of the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_get_attributes(
  rtems_vector_number         vector,
  rtems_interrupt_attributes *attributes
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`attributes`

: This parameter is the pointer to an
  {ref}`InterfaceRtemsInterruptAttributes` object. When the directive call
  is successful, the attributes of the interrupt vector will be stored in
  this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `attributes` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/handler-iterate

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_handler_iterate()
```

(interfacertemsinterrupthandleriterate)=

## rtems_interrupt_handler_iterate()

Iterates over all interrupt handler installed at the interrupt vector.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_handler_iterate(
  rtems_vector_number                 vector,
  rtems_interrupt_per_handler_routine routine,
  void                               *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`vector`

: This parameter is the interrupt vector number.

`routine`

: This parameter is the visitor routine.

`arg`

: This parameter is the visitor argument.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

For each installed handler at the interrupt vector the visitor function
specified by `routine` will be called with the argument specified by `arg`
and the handler information, options, routine and argument.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INCORRECT_STATE`

: The service was not initialized.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `routine` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

```{eval-rst}
.. rubric:: NOTES:
```

The directive is intended for system information and diagnostics.

Never install or remove an interrupt handler within the visitor function. This
may result in a deadlock.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-initialize

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_initialize()
```

(interfacertemsinterruptserverinitialize)=

## rtems_interrupt_server_initialize()

Initializes the interrupt server tasks.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_initialize(
  rtems_task_priority priority,
  size_t              stack_size,
  rtems_mode          modes,
  rtems_attribute     attributes,
  uint32_t           *server_count
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`priority`

: This parameter is the initial {term}`task priority` of the created
  interrupt servers.

`stack_size`

: This parameter is the task stack size of the created interrupt servers.

`modes`

: This parameter is the initial mode set of the created interrupt servers.

`attributes`

: This parameter is the attribute set of the created interrupt servers.

`server_count`

: This parameter is the pointer to an [uint32_t](https://en.cppreference.com/w/c/types/integer) object or [NULL](https://en.cppreference.com/w/c/types/NULL). When the pointer is not
  equal to [NULL](https://en.cppreference.com/w/c/types/NULL), the count of
  successfully created interrupt servers is stored in this object regardless
  of the return status.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive tries to create an interrupt server task for each online
processor in the system. The tasks will have the initial priority specified by
`priority`, the stack size specified by `stack_size`, the initial mode set
specified by `modes`, and the attribute set specified by `attributes`. The
count of successfully created server tasks will be returned in `server_count`
if the pointer is not equal to [NULL](https://en.cppreference.com/w/c/types/NULL).

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INCORRECT_STATE`

: The interrupt servers were already initialized.

The directive uses {ref}`InterfaceRtemsTaskCreate`. If this directive fails,
then its error status will be returned.

```{eval-rst}
.. rubric:: NOTES:
```

Interrupt handlers may be installed on an interrupt server with
{ref}`InterfaceRtemsInterruptServerHandlerInstall` and removed with
{ref}`InterfaceRtemsInterruptServerHandlerRemove` using a server index. In
case of an interrupt, the request will be forwarded to the interrupt server.
The handlers are executed within the interrupt server context. If one handler
blocks on something this may delay the processing of other handlers.

Interrupt servers may be deleted by {ref}`InterfaceRtemsInterruptServerDelete`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-create

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_create()
```

(interfacertemsinterruptservercreate)=

## rtems_interrupt_server_create()

Creates an interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_create(
  rtems_interrupt_server_control      *control,
  const rtems_interrupt_server_config *config,
  uint32_t                            *server_index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`control`

: This parameter is the pointer to an
  {ref}`InterfaceRtemsInterruptServerControl` object. When the directive
  call was successful, the ownership of the object was transferred from the
  caller of the directive to the interrupt server management.

`config`

: This parameter is the interrupt server configuration.

`server_index`

: This parameter is the pointer to an [uint32_t](https://en.cppreference.com/w/c/types/integer) object. When the
  directive call was successful, the index of the created interrupt server
  will be stored in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

The directive uses {ref}`InterfaceRtemsTaskCreate`. If this directive fails,
then its error status will be returned.

```{eval-rst}
.. rubric:: NOTES:
```

See also {ref}`InterfaceRtemsInterruptServerInitialize` and
{ref}`InterfaceRtemsInterruptServerDelete`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-handler-install

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_handler_install()
```

(interfacertemsinterruptserverhandlerinstall)=

## rtems_interrupt_server_handler_install()

Installs the interrupt handler routine and argument at the interrupt vector on
the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_handler_install(
  uint32_t                server_index,
  rtems_vector_number     vector,
  const char             *info,
  rtems_option            options,
  rtems_interrupt_handler routine,
  void                   *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the interrupt server index. The constant
  {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify the
  default interrupt server.

`vector`

: This parameter is the interrupt vector number.

`info`

: This parameter is the descriptive information of the interrupt handler to
  install.

`options`

: This parameter is the interrupt handler install option set.

`routine`

: This parameter is the interrupt handler routine to install.

`arg`

: This parameter is the interrupt handler argument to install.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The handler routine specified by `routine` will be executed within the
context of the interrupt server task specified by `server_index`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `routine` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_INVALID_NUMBER`

: An option specified by `info` was not applicable.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The {c:macro}`RTEMS_INTERRUPT_UNIQUE` option was set in `info` and the
  interrupt vector was already occupied by a handler.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The {c:macro}`RTEMS_INTERRUPT_SHARED` option was set in `info` and the
  interrupt vector was already occupied by a unique handler.

{c:macro}`RTEMS_TOO_MANY`

: The handler specified by `routine` was already installed for the
  interrupt vector specified by `vector` with an argument equal to the
  argument specified by `arg`.

{c:macro}`RTEMS_UNSATISFIED`

: The {c:macro}`RTEMS_INTERRUPT_REPLACE` option was set in `info` and no
  handler to replace was installed.

```{eval-rst}
.. rubric:: NOTES:
```

See also {ref}`InterfaceRtemsInterruptHandlerInstall`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-handler-remove

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_handler_remove()
```

(interfacertemsinterruptserverhandlerremove)=

## rtems_interrupt_server_handler_remove()

Removes the interrupt handler routine and argument from the interrupt vector
and the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_handler_remove(
  uint32_t                server_index,
  rtems_vector_number     vector,
  rtems_interrupt_handler routine,
  void                   *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the interrupt server index. The constant
  {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify the
  default interrupt server.

`vector`

: This parameter is the interrupt vector number.

`routine`

: This parameter is the interrupt handler routine to remove.

`arg`

: This parameter is the interrupt handler argument to remove.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

{c:macro}`RTEMS_UNSATISFIED`

: There was no handler routine and argument pair installed specified by
  `routine` and `arg`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.

% Generated from spec:/rtems/intr/if/server-set-affinity

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_set_affinity()
```

(interfacertemsinterruptserversetaffinity)=

## rtems_interrupt_server_set_affinity()

Sets the processor affinity of the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_set_affinity(
  uint32_t            server_index,
  size_t              affinity_size,
  const cpu_set_t    *affinity,
  rtems_task_priority priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the interrupt server index. The constant
  {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify the
  default interrupt server.

`affinity_size`

: This parameter is the size of the processor set referenced by `affinity`
  in bytes.

`affinity`

: This parameter is the pointer to a {c:type}`cpu_set_t` object. The
  processor set defines the new processor affinity set of the interrupt
  server. A set bit in the processor set means that the corresponding
  processor shall be in the processor affinity set of the task, otherwise the
  bit shall be cleared.

`priority`

: This parameter is the new {term}`real priority` for the interrupt server.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

The directive uses {ref}`InterfaceRtemsSchedulerIdentByProcessorSet`,
{ref}`InterfaceRtemsTaskSetScheduler`, and
{ref}`InterfaceRtemsTaskSetAffinity`. If one of these directive fails, then
its error status will be returned.

```{eval-rst}
.. rubric:: NOTES:
```

The scheduler is set determined by the highest numbered processor in the
affinity set specified by `affinity`.

This operation is only reliable in case the interrupt server was suspended via
{ref}`InterfaceRtemsInterruptServerSuspend`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may change the processor affinity of a task. This may cause
  the calling task to be preempted.
- The directive may change the priority of a task. This may cause the calling
  task to be preempted.

% Generated from spec:/rtems/intr/if/server-delete

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_delete()
```

(interfacertemsinterruptserverdelete)=

## rtems_interrupt_server_delete()

Deletes the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_delete( uint32_t server_index );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the index of the interrupt server to delete.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the server index specified by
  `server_index`.

```{eval-rst}
.. rubric:: NOTES:
```

The interrupt server deletes itself, so after the return of the directive the
interrupt server may be still in the termination process depending on the task
priorities of the system.

See also {ref}`InterfaceRtemsInterruptServerCreate`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.

% Generated from spec:/rtems/intr/if/server-suspend

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_suspend()
```

(interfacertemsinterruptserversuspend)=

## rtems_interrupt_server_suspend()

Suspends the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_suspend( uint32_t server_index );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the index of the interrupt server to suspend. The
  constant {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify
  the default interrupt server.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

```{eval-rst}
.. rubric:: NOTES:
```

Interrupt server may be resumed by {ref}`InterfaceRtemsInterruptServerResume`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.

% Generated from spec:/rtems/intr/if/server-resume

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_resume()
```

(interfacertemsinterruptserverresume)=

## rtems_interrupt_server_resume()

Resumes the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_resume( uint32_t server_index );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the index of the interrupt server to resume. The
  constant {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify
  the default interrupt server.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

```{eval-rst}
.. rubric:: NOTES:
```

Interrupt server may be suspended by
{ref}`InterfaceRtemsInterruptServerSuspend`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.

% Generated from spec:/rtems/intr/if/server-move

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_move()
```

(interfacertemsinterruptservermove)=

## rtems_interrupt_server_move()

Moves the interrupt handlers installed at the interrupt vector and the source
interrupt server to the destination interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_move(
  uint32_t            source_server_index,
  rtems_vector_number vector,
  uint32_t            destination_server_index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`source_server_index`

: This parameter is the index of the source interrupt server. The constant
  {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify the
  default interrupt server.

`vector`

: This parameter is the interrupt vector number.

`destination_server_index`

: This parameter is the index of the destination interrupt server. The
  constant {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify
  the default interrupt server.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `source_server_index`.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `destination_server_index`.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.

% Generated from spec:/rtems/intr/if/server-handler-iterate

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_handler_iterate()
```

(interfacertemsinterruptserverhandleriterate)=

## rtems_interrupt_server_handler_iterate()

Iterates over all interrupt handler installed at the interrupt vector and
interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_handler_iterate(
  uint32_t                            server_index,
  rtems_vector_number                 vector,
  rtems_interrupt_per_handler_routine routine,
  void                               *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the index of the interrupt server.

`vector`

: This parameter is the interrupt vector number.

`routine`

: This parameter is the visitor routine.

`arg`

: This parameter is the visitor argument.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

For each installed handler at the interrupt vector and interrupt server the
visitor function specified by `vector` will be called with the argument
specified by `routine` and the handler information, options, routine and
argument.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt vector associated with the number specified by
  `vector`.

```{eval-rst}
.. rubric:: NOTES:
```

The directive is intended for system information and diagnostics.

Never install or remove an interrupt handler within the visitor function. This
may result in a deadlock.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-entry-initialize

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_entry_initialize()
```

(interfacertemsinterruptserverentryinitialize)=

## rtems_interrupt_server_entry_initialize()

Initializes the interrupt server entry.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_entry_initialize(
  uint32_t                      server_index,
  rtems_interrupt_server_entry *entry
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the interrupt server index. The constant
  {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify the
  default interrupt server.

`entry`

: This parameter is the interrupt server entry to initialize.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

```{eval-rst}
.. rubric:: NOTES:
```

After initialization, the list of actions of the interrupt server entry is
empty. Actions may be prepended by
{ref}`InterfaceRtemsInterruptServerActionPrepend`. Interrupt server entries may
be moved to another interrupt vector with
{ref}`InterfaceRtemsInterruptServerEntryMove`. Server entries may be submitted
to get serviced by the interrupt server with
{ref}`InterfaceRtemsInterruptServerEntrySubmit`. Server entries may be
destroyed by {ref}`InterfaceRtemsInterruptServerEntryDestroy`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-action-prepend

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_action_prepend()
```

(interfacertemsinterruptserveractionprepend)=

## rtems_interrupt_server_action_prepend()

Prepends the interrupt server action to the list of actions of the interrupt
server entry.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_server_action_prepend(
  rtems_interrupt_server_entry  *entry,
  rtems_interrupt_server_action *action,
  rtems_interrupt_handler        routine,
  void                          *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`entry`

: This parameter is the interrupt server entry to prepend the interrupt
  server action. It shall have been initialized via
  {ref}`InterfaceRtemsInterruptServerEntryInitialize`.

`action`

: This parameter is the interrupt server action to initialize and prepend to
  the list of actions of the entry.

`routine`

: This parameter is the interrupt handler routine to set in the action.

`arg`

: This parameter is the interrupt handler argument to set in the action.

```{eval-rst}
.. rubric:: NOTES:
```

No error checking is performed by the directive.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.
- The interrupt server entry shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerEntryInitialize` and further optional
  calls to {ref}`InterfaceRtemsInterruptServerActionPrepend`.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerActionPrepend` with the same interrupt
  server entry. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerEntryMove` with the same interrupt server
  entry. Calling the directive under this condition is undefined behaviour.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerEntrySubmit` with the same interrupt
  server entry. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called while the interrupt server entry is pending
  on or serviced by its current interrupt server. Calling the directive under
  these conditions is undefined behaviour.

% Generated from spec:/rtems/intr/if/server-entry-destroy

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_entry_destroy()
```

(interfacertemsinterruptserverentrydestroy)=

## rtems_interrupt_server_entry_destroy()

Destroys the interrupt server entry.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_server_entry_destroy(
  rtems_interrupt_server_entry *entry
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`entry`

: This parameter is the interrupt server entry to destroy.

```{eval-rst}
.. rubric:: NOTES:
```

No error checking is performed by the directive.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.
- The interrupt server entry shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerEntryInitialize` and further optional
  calls to {ref}`InterfaceRtemsInterruptServerActionPrepend`.

% Generated from spec:/rtems/intr/if/server-entry-submit

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_entry_submit()
```

(interfacertemsinterruptserverentrysubmit)=

## rtems_interrupt_server_entry_submit()

Submits the interrupt server entry to be serviced by the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_server_entry_submit(
  rtems_interrupt_server_entry *entry
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`entry`

: This parameter is the interrupt server entry to submit.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive appends the entry to the pending entries of the interrupt server.
The interrupt server is notified that a new entry is pending. Once the
interrupt server is scheduled it services the actions of all pending entries.

```{eval-rst}
.. rubric:: NOTES:
```

This directive may be used to do a two-step interrupt processing. The first
step is done from within interrupt context by a call to this directive. The
second step is then done from within the context of the interrupt server.

No error checking is performed by the directive.

A submitted entry may be destroyed by
{ref}`InterfaceRtemsInterruptServerEntryDestroy`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may unblock a task. This may cause the calling task to be
  preempted.
- The interrupt server entry shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerEntryInitialize` and further optional
  calls to {ref}`InterfaceRtemsInterruptServerActionPrepend`.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerActionPrepend` with the same interrupt
  server entry. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerEntryMove` with the same interrupt server
  entry. Calling the directive under this condition is undefined behaviour.

% Generated from spec:/rtems/intr/if/server-entry-move

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_entry_move()
```

(interfacertemsinterruptserverentrymove)=

## rtems_interrupt_server_entry_move()

Moves the interrupt server entry to the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_entry_move(
  rtems_interrupt_server_entry *entry,
  uint32_t                      server_index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`entry`

: This parameter is the interrupt server entry to move.

`server_index`

: This parameter is the index of the destination interrupt server. The
  constant {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify
  the default interrupt server.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- The interrupt server entry shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerEntryInitialize` and further optional
  calls to {ref}`InterfaceRtemsInterruptServerActionPrepend`.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerActionPrepend` with the same interrupt
  server entry. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerEntryMove` with the same interrupt server
  entry. Calling the directive under this condition is undefined behaviour.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerEntrySubmit` with the same interrupt
  server entry. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called while the interrupt server entry is pending
  on or serviced by its current interrupt server. Calling the directive under
  these conditions is undefined behaviour.

% Generated from spec:/rtems/intr/if/server-request-initialize

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_request_initialize()
```

(interfacertemsinterruptserverrequestinitialize)=

## rtems_interrupt_server_request_initialize()

Initializes the interrupt server request.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_interrupt_server_request_initialize(
  uint32_t                        server_index,
  rtems_interrupt_server_request *request,
  rtems_interrupt_handler         routine,
  void                           *arg
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`server_index`

: This parameter is the interrupt server index. The constant
  {c:macro}`RTEMS_INTERRUPT_SERVER_DEFAULT` may be used to specify the
  default interrupt server.

`request`

: This parameter is the interrupt server request to initialize.

`routine`

: This parameter is the interrupt handler routine for the request action.

`arg`

: This parameter is the interrupt handler argument for the request action.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no interrupt server associated with the index specified by
  `server_index`.

```{eval-rst}
.. rubric:: NOTES:
```

An interrupt server requests consists of an interrupt server entry and exactly
one interrupt server action. The interrupt vector of the request may be
changed with {ref}`InterfaceRtemsInterruptServerRequestSetVector`. Interrupt
server requests may be submitted to get serviced by the interrupt server with
{ref}`InterfaceRtemsInterruptServerRequestSubmit`. Requests may be destroyed
by {ref}`InterfaceRtemsInterruptServerRequestDestroy`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/intr/if/server-request-set-vector

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_request_set_vector()
```

(interfacertemsinterruptserverrequestsetvector)=

## rtems_interrupt_server_request_set_vector()

Sets the interrupt vector in the interrupt server request.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_server_request_set_vector(
  rtems_interrupt_server_request *request,
  rtems_vector_number             vector
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`request`

: This parameter is the interrupt server request to change.

`vector`

: This parameter is the interrupt vector number to be used by the request.

```{eval-rst}
.. rubric:: NOTES:
```

By default, the interrupt vector of an interrupt server request is set to a
special value which is outside the range of vectors supported by the interrupt
controller hardware.

Calls to {ref}`InterfaceRtemsInterruptServerRequestSubmit` will disable the
interrupt vector of the request. After processing of the request by the
interrupt server the interrupt vector will be enabled again.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.
- The interrupt server request shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerRequestInitialize`.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerRequestSetVector` with the same interrupt
  server request. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerRequestSubmit` with the same interrupt
  server request. Calling the directive under this condition is undefined
  behaviour.
- The directive shall not be called while the interrupt server entry is pending
  on or serviced by its current interrupt server. Calling the directive under
  these conditions is undefined behaviour.

% Generated from spec:/rtems/intr/if/server-request-destroy

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_request_destroy()
```

(interfacertemsinterruptserverrequestdestroy)=

## rtems_interrupt_server_request_destroy()

Destroys the interrupt server request.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_server_request_destroy(
  rtems_interrupt_server_request *request
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`request`

: This parameter is the interrupt server request to destroy.

```{eval-rst}
.. rubric:: NOTES:
```

No error checking is performed by the directive.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive shall not be called from within the context of an interrupt
  server. Calling the directive from within the context of an interrupt server
  is undefined behaviour.
- The directive sends a request to another task and waits for a response. This
  may cause the calling task to be blocked and unblocked.
- The interrupt server request shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerRequestInitialize`.

% Generated from spec:/rtems/intr/if/server-request-submit

```{raw} latex
\clearpage
```

```{index} rtems_interrupt_server_request_submit()
```

(interfacertemsinterruptserverrequestsubmit)=

## rtems_interrupt_server_request_submit()

Submits the interrupt server request to be serviced by the interrupt server.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_interrupt_server_request_submit(
  rtems_interrupt_server_request *request
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`request`

: This parameter is the interrupt server request to submit.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The directive appends the interrupt server entry of the request to the pending
entries of the interrupt server. The interrupt server is notified that a new
entry is pending. Once the interrupt server is scheduled it services the
actions of all pending entries.

```{eval-rst}
.. rubric:: NOTES:
```

This directive may be used to do a two-step interrupt processing. The first
step is done from within interrupt context by a call to this directive. The
second step is then done from within the context of the interrupt server.

No error checking is performed by the directive.

A submitted request may be destroyed by
{ref}`InterfaceRtemsInterruptServerRequestDestroy`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may unblock a task. This may cause the calling task to be
  preempted.
- The interrupt server request shall have been initialized by
  {ref}`InterfaceRtemsInterruptServerRequestInitialize`.
- The directive shall not be called concurrently with
  {ref}`InterfaceRtemsInterruptServerRequestSetVector` with the same interrupt
  server request. Calling the directive under this condition is undefined
  behaviour.
