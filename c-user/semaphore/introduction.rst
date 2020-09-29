.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/rtems/sem/if/group

.. _SemaphoreManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/sem/if/create
.. spec:/rtems/sem/if/ident
.. spec:/rtems/sem/if/delete
.. spec:/rtems/sem/if/obtain
.. spec:/rtems/sem/if/release
.. spec:/rtems/sem/if/flush
.. spec:/rtems/sem/if/set-priority

The Semaphore Manager utilizes standard Dijkstra counting semaphores to provide
synchronization and mutual exclusion capabilities. The directives provided by
the Semaphore Manager are:

* :ref:`InterfaceRtemsSemaphoreCreate` - Creates a semaphore.

* :ref:`InterfaceRtemsSemaphoreIdent` - Identifies a semaphore by the object
  name.

* :ref:`InterfaceRtemsSemaphoreDelete` - Deletes the semaphore.

* :ref:`InterfaceRtemsSemaphoreObtain` - Obtains the semaphore.

* :ref:`InterfaceRtemsSemaphoreRelease` - Releases the semaphore.

* :ref:`InterfaceRtemsSemaphoreFlush` - Flushes the semaphore.

* :ref:`InterfaceRtemsSemaphoreSetPriority` - Sets the priority by scheduler
  for the semaphore.
