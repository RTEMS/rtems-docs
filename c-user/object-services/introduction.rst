.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2009 On-Line Applications Research Corporation (OAR)

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

.. Generated from spec:/rtems/object/if/group

.. _ObjectServicesIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/object/if/build-id
.. spec:/rtems/object/if/build-name
.. spec:/rtems/object/if/get-classic-name
.. spec:/rtems/object/if/get-name
.. spec:/rtems/object/if/set-name
.. spec:/rtems/object/if/id-get-api
.. spec:/rtems/object/if/id-get-class
.. spec:/rtems/object/if/id-get-node
.. spec:/rtems/object/if/id-get-index
.. spec:/rtems/object/if/id-api-minimum
.. spec:/rtems/object/if/id-api-maximum
.. spec:/rtems/object/if/api-minimum-class
.. spec:/rtems/object/if/api-maximum-class
.. spec:/rtems/object/if/get-api-name
.. spec:/rtems/object/if/get-api-class-name
.. spec:/rtems/object/if/get-class-information
.. spec:/rtems/object/if/get-local-node
.. spec:/rtems/object/if/id-initial

RTEMS provides a collection of services to assist in the management and usage
of the objects created and utilized via other managers.  These services assist
in the manipulation of RTEMS objects independent of the API used to create
them. The directives provided by the Object Services are:

* :ref:`InterfaceRtemsBuildId` - Builds the object identifier from the API,
  class, MPCI node, and index components.

* :ref:`InterfaceRtemsBuildName` - Builds the object name composed of the four
  characters.

* :ref:`InterfaceRtemsObjectGetClassicName` - Gets the object name associated
  with the object identifier.

* :ref:`InterfaceRtemsObjectGetName` - Gets the object name associated with the
  object identifier as a string.

* :ref:`InterfaceRtemsObjectSetName` - Sets the object name of the object
  associated with the object identifier.

* :ref:`InterfaceRtemsObjectIdGetApi` - Gets the API component of the object
  identifier.

* :ref:`InterfaceRtemsObjectIdGetClass` - Gets the class component of the
  object identifier.

* :ref:`InterfaceRtemsObjectIdGetNode` - Gets the MPCI node component of the
  object identifier.

* :ref:`InterfaceRtemsObjectIdGetIndex` - Gets the index component of the
  object identifier.

* :ref:`InterfaceRtemsObjectIdApiMinimum` - Gets the lowest valid value for the
  API component of an object identifier.

* :ref:`InterfaceRtemsObjectIdApiMaximum` - Gets the highest valid value for
  the API component of an object identifier.

* :ref:`InterfaceRtemsObjectApiMinimumClass` - Gets the lowest valid class
  value of the object API.

* :ref:`InterfaceRtemsObjectApiMaximumClass` - Gets the highest valid class
  value of the object API.

* :ref:`InterfaceRtemsObjectGetApiName` - Gets a descriptive name of the object
  API.

* :ref:`InterfaceRtemsObjectGetApiClassName` - Gets a descriptive name of the
  object class of the object API.

* :ref:`InterfaceRtemsObjectGetClassInformation` - Gets the object class
  information of the object class of the object API.

* :ref:`InterfaceRtemsObjectGetLocalNode` - Gets the local MPCI node number.

* :ref:`InterfaceRTEMSOBJECTIDINITIAL` - Builds the object identifier with the
  lowest index from the API, class, and MPCI node components.
