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

.. Generated from spec:/rtems/timer/if/group

.. _TimerManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/timer/if/create
.. spec:/rtems/timer/if/ident
.. spec:/rtems/timer/if/cancel
.. spec:/rtems/timer/if/delete
.. spec:/rtems/timer/if/fire-after
.. spec:/rtems/timer/if/fire-when
.. spec:/rtems/timer/if/initiate-server
.. spec:/rtems/timer/if/server-fire-after
.. spec:/rtems/timer/if/server-fire-when
.. spec:/rtems/timer/if/reset
.. spec:/rtems/timer/if/get-information

The Timer Manager provides support for timer facilities. The directives
provided by the Timer Manager are:

* :ref:`InterfaceRtemsTimerCreate` - Creates a timer.

* :ref:`InterfaceRtemsTimerIdent` - Identifies a timer by the object name.

* :ref:`InterfaceRtemsTimerCancel` - Cancels the timer.

* :ref:`InterfaceRtemsTimerDelete` - Deletes the timer.

* :ref:`InterfaceRtemsTimerFireAfter` - Fires the timer after the interval.

* :ref:`InterfaceRtemsTimerFireWhen` - Fires the timer at the time of day.

* :ref:`InterfaceRtemsTimerInitiateServer` - Initiates the Timer Server.

* :ref:`InterfaceRtemsTimerServerFireAfter` - Fires the timer after the
  interval using the Timer Server.

* :ref:`InterfaceRtemsTimerServerFireWhen` - Fires the timer at the time of day
  using the Timer Server.

* :ref:`InterfaceRtemsTimerReset` - Resets the timer.

* :ref:`InterfaceRtemsTimerGetInformation` - Gets information about the timer.
