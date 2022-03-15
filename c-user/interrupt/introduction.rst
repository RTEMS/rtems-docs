.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2008, 2022 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/rtems/intr/if/group

.. _InterruptManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/intr/if/catch
.. spec:/rtems/intr/if/disable
.. spec:/rtems/intr/if/enable
.. spec:/rtems/intr/if/flash
.. spec:/rtems/intr/if/local-disable
.. spec:/rtems/intr/if/local-enable
.. spec:/rtems/intr/if/is-in-progress
.. spec:/rtems/intr/if/lock-initialize
.. spec:/rtems/intr/if/lock-destroy
.. spec:/rtems/intr/if/lock-acquire
.. spec:/rtems/intr/if/lock-release
.. spec:/rtems/intr/if/lock-acquire-isr
.. spec:/rtems/intr/if/lock-release-isr
.. spec:/rtems/intr/if/lock-isr-disable
.. spec:/rtems/intr/if/lock-declare
.. spec:/rtems/intr/if/lock-define
.. spec:/rtems/intr/if/lock-initializer
.. spec:/rtems/intr/if/lock-member
.. spec:/rtems/intr/if/lock-reference
.. spec:/rtems/intr/if/entry-initializer
.. spec:/rtems/intr/if/entry-initialize
.. spec:/rtems/intr/if/entry-install
.. spec:/rtems/intr/if/entry-remove
.. spec:/rtems/intr/if/handler-install
.. spec:/rtems/intr/if/handler-remove
.. spec:/rtems/intr/if/vector-is-enabled
.. spec:/rtems/intr/if/vector-enable
.. spec:/rtems/intr/if/vector-disable
.. spec:/rtems/intr/if/is-pending
.. spec:/rtems/intr/if/raise
.. spec:/rtems/intr/if/raise-on
.. spec:/rtems/intr/if/clear
.. spec:/rtems/intr/if/get-affinity
.. spec:/rtems/intr/if/set-affinity
.. spec:/rtems/intr/if/get-attributes
.. spec:/rtems/intr/if/handler-iterate
.. spec:/rtems/intr/if/server-initialize
.. spec:/rtems/intr/if/server-create
.. spec:/rtems/intr/if/server-handler-install
.. spec:/rtems/intr/if/server-handler-remove
.. spec:/rtems/intr/if/server-set-affinity
.. spec:/rtems/intr/if/server-delete
.. spec:/rtems/intr/if/server-suspend
.. spec:/rtems/intr/if/server-resume
.. spec:/rtems/intr/if/server-move
.. spec:/rtems/intr/if/server-handler-iterate
.. spec:/rtems/intr/if/server-entry-initialize
.. spec:/rtems/intr/if/server-action-prepend
.. spec:/rtems/intr/if/server-entry-destroy
.. spec:/rtems/intr/if/server-entry-submit
.. spec:/rtems/intr/if/server-entry-move
.. spec:/rtems/intr/if/server-request-initialize
.. spec:/rtems/intr/if/server-request-set-vector
.. spec:/rtems/intr/if/server-request-destroy
.. spec:/rtems/intr/if/server-request-submit

Any real-time executive must provide a mechanism for quick response to
externally generated interrupts to satisfy the critical time constraints of the
application.  The Interrupt Manager provides this mechanism for RTEMS. This
manager permits quick interrupt response times by providing the critical
ability to alter task execution which allows a task to be preempted upon exit
from an ISR. The directives provided by the Interrupt Manager are:

* :ref:`InterfaceRtemsInterruptCatch` - Establishes an interrupt service
  routine.

* :ref:`InterfaceRtemsInterruptDisable` - Disables the maskable interrupts on
  the current processor.

* :ref:`InterfaceRtemsInterruptEnable` - Restores the previous interrupt level
  on the current processor.

* :ref:`InterfaceRtemsInterruptFlash` - Flashes interrupts on the current
  processor.

* :ref:`InterfaceRtemsInterruptLocalDisable` - Disables the maskable interrupts
  on the current processor.

* :ref:`InterfaceRtemsInterruptLocalEnable` - Restores the previous interrupt
  level on the current processor.

* :ref:`InterfaceRtemsInterruptIsInProgress` - Checks if an ISR is in progress
  on the current processor.

* :ref:`InterfaceRtemsInterruptLockInitialize` - Initializes the ISR lock.

* :ref:`InterfaceRtemsInterruptLockDestroy` - Destroys the ISR lock.

* :ref:`InterfaceRtemsInterruptLockAcquire` - Acquires the ISR lock.

* :ref:`InterfaceRtemsInterruptLockRelease` - Releases the ISR lock.

* :ref:`InterfaceRtemsInterruptLockAcquireIsr` - Acquires the ISR lock from
  within an ISR.

* :ref:`InterfaceRtemsInterruptLockReleaseIsr` - Releases the ISR lock from
  within an ISR.

* :ref:`InterfaceRtemsInterruptLockInterruptDisable` - Disables maskable
  interrupts on the current processor.

* :ref:`InterfaceRTEMSINTERRUPTLOCKDECLARE` - Declares an ISR lock object.

* :ref:`InterfaceRTEMSINTERRUPTLOCKDEFINE` - Defines an ISR lock object.

* :ref:`InterfaceRTEMSINTERRUPTLOCKINITIALIZER` - Statically initializes an ISR
  lock object.

* :ref:`InterfaceRTEMSINTERRUPTLOCKMEMBER` - Defines an ISR lock member.

* :ref:`InterfaceRTEMSINTERRUPTLOCKREFERENCE` - Defines an ISR lock object
  reference.

* :ref:`InterfaceRTEMSINTERRUPTENTRYINITIALIZER` - Statically initializes an
  interrupt entry object.

* :ref:`InterfaceRtemsInterruptEntryInitialize` - Initializes the interrupt
  entry.

* :ref:`InterfaceRtemsInterruptEntryInstall` - Installs the interrupt entry at
  the interrupt vector.

* :ref:`InterfaceRtemsInterruptEntryRemove` - Removes the interrupt entry from
  the interrupt vector.

* :ref:`InterfaceRtemsInterruptHandlerInstall` - Installs the interrupt handler
  routine and argument at the interrupt vector.

* :ref:`InterfaceRtemsInterruptHandlerRemove` - Removes the interrupt handler
  routine and argument from the interrupt vector.

* :ref:`InterfaceRtemsInterruptVectorIsEnabled` - Checks if the interrupt
  vector is enabled.

* :ref:`InterfaceRtemsInterruptVectorEnable` - Enables the interrupt vector.

* :ref:`InterfaceRtemsInterruptVectorDisable` - Disables the interrupt vector.

* :ref:`InterfaceRtemsInterruptIsPending` - Checks if the interrupt is pending.

* :ref:`InterfaceRtemsInterruptRaise` - Raises the interrupt vector.

* :ref:`InterfaceRtemsInterruptRaiseOn` - Raises the interrupt vector on the
  processor.

* :ref:`InterfaceRtemsInterruptClear` - Clears the interrupt vector.

* :ref:`InterfaceRtemsInterruptGetAffinity` - Gets the processor affinity set
  of the interrupt vector.

* :ref:`InterfaceRtemsInterruptSetAffinity` - Sets the processor affinity set
  of the interrupt vector.

* :ref:`InterfaceRtemsInterruptGetAttributes` - Gets the attributes of the
  interrupt vector.

* :ref:`InterfaceRtemsInterruptHandlerIterate` - Iterates over all interrupt
  handler installed at the interrupt vector.

* :ref:`InterfaceRtemsInterruptServerInitialize` - Initializes the interrupt
  server tasks.

* :ref:`InterfaceRtemsInterruptServerCreate` - Creates an interrupt server.

* :ref:`InterfaceRtemsInterruptServerHandlerInstall` - Installs the interrupt
  handler routine and argument at the interrupt vector on the interrupt server.

* :ref:`InterfaceRtemsInterruptServerHandlerRemove` - Removes the interrupt
  handler routine and argument from the interrupt vector and the interrupt
  server.

* :ref:`InterfaceRtemsInterruptServerSetAffinity` - Sets the processor affinity
  of the interrupt server.

* :ref:`InterfaceRtemsInterruptServerDelete` - Deletes the interrupt server.

* :ref:`InterfaceRtemsInterruptServerSuspend` - Suspends the interrupt server.

* :ref:`InterfaceRtemsInterruptServerResume` - Resumes the interrupt server.

* :ref:`InterfaceRtemsInterruptServerMove` - Moves the interrupt handlers
  installed at the interrupt vector and the source interrupt server to the
  destination interrupt server.

* :ref:`InterfaceRtemsInterruptServerHandlerIterate` - Iterates over all
  interrupt handler installed at the interrupt vector and interrupt server.

* :ref:`InterfaceRtemsInterruptServerEntryInitialize` - Initializes the
  interrupt server entry.

* :ref:`InterfaceRtemsInterruptServerActionPrepend` - Prepends the interrupt
  server action to the list of actions of the interrupt server entry.

* :ref:`InterfaceRtemsInterruptServerEntryDestroy` - Destroys the interrupt
  server entry.

* :ref:`InterfaceRtemsInterruptServerEntrySubmit` - Submits the interrupt
  server entry to be serviced by the interrupt server.

* :ref:`InterfaceRtemsInterruptServerEntryMove` - Moves the interrupt server
  entry to the interrupt server.

* :ref:`InterfaceRtemsInterruptServerRequestInitialize` - Initializes the
  interrupt server request.

* :ref:`InterfaceRtemsInterruptServerRequestSetVector` - Sets the interrupt
  vector in the interrupt server request.

* :ref:`InterfaceRtemsInterruptServerRequestDestroy` - Destroys the interrupt
  server request.

* :ref:`InterfaceRtemsInterruptServerRequestSubmit` - Submits the interrupt
  server request to be serviced by the interrupt server.
