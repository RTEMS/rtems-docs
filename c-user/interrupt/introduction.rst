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
.. spec:/rtems/intr/if/cause
.. spec:/rtems/intr/if/clear
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

* :ref:`InterfaceRtemsInterruptCause` - Causes the interrupt.

* :ref:`InterfaceRtemsInterruptClear` - Clears the interrupt.

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
