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

.. Generated from spec:/rtems/event/if/group

.. _EventManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/event/if/send
.. spec:/rtems/event/if/receive

The Event Manager provides a high performance method of inter-task
communication and synchronization. The directives provided by the Event Manager
are:

* :ref:`InterfaceRtemsEventSend` - Sends the event set to the task.

* :ref:`InterfaceRtemsEventReceive` - Receives or gets an event set from the
  calling task.
