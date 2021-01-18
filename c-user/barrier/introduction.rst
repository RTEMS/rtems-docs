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

.. Generated from spec:/rtems/barrier/if/group

.. _BarrierManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/barrier/if/create
.. spec:/rtems/barrier/if/ident
.. spec:/rtems/barrier/if/delete
.. spec:/rtems/barrier/if/wait
.. spec:/rtems/barrier/if/release

The Barrier Manager provides a unique synchronization capability which can be
used to have a set of tasks block and be unblocked as a set. The directives
provided by the Barrier Manager are:

* :ref:`InterfaceRtemsBarrierCreate` - Creates a barrier.

* :ref:`InterfaceRtemsBarrierIdent` - Identifies a barrier by the object name.

* :ref:`InterfaceRtemsBarrierDelete` - Deletes the barrier.

* :ref:`InterfaceRtemsBarrierWait` - Waits at the barrier.

* :ref:`InterfaceRtemsBarrierRelease` - Releases the barrier.
