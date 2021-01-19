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

.. Generated from spec:/rtems/userext/if/group

.. _UserExtensionsManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/userext/if/create
.. spec:/rtems/userext/if/delete
.. spec:/rtems/userext/if/ident

The User Extensions Manager allows the application developer to augment the
executive by allowing them to supply extension routines which are invoked at
critical system events. The directives provided by the User Extensions Manager
are:

* :ref:`InterfaceRtemsExtensionCreate` - Creates an extension set.

* :ref:`InterfaceRtemsExtensionDelete` - Deletes the extension set.

* :ref:`InterfaceRtemsExtensionIdent` - Identifies an extension set by the
  object name.
