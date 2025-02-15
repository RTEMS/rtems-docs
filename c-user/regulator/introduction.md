.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2023 On-Line Applications Research Corporation (OAR)

.. _RegulatorManagerIntroduction:

Introduction
============

The Regulator Manager provides a set of directives to manage a data flow
from a source to a destination. The focus is on regulating the bursty
input so that it is delivered to the destination at a regular rate.
The directives provided by the Regulator Manager are:

* :ref:`InterfaceRtemsRegulatorCreate` - Creates a regulator.

* :ref:`InterfaceRtemsRegulatorDelete` - Deletes the regulator.

* :ref:`InterfaceRtemsRegulatorObtainBuffer` - Obtain buffer from a regulator.

* :ref:`InterfaceRtemsRegulatorReleaseBuffer` - Release buffer to a regulator.

* :ref:`InterfaceRtemsRegulatorSend` - Send buffer to a regulator.

* :ref:`InterfaceRtemsRegulatorGetStatistics` - Obtain statistics for a regulator.
