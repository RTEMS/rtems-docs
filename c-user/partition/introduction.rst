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

.. Generated from spec:/rtems/part/if/group

.. _PartitionManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/part/if/create
.. spec:/rtems/part/if/ident
.. spec:/rtems/part/if/delete
.. spec:/rtems/part/if/get-buffer
.. spec:/rtems/part/if/return-buffer

The Partition Manager provides facilities to dynamically allocate memory in
fixed-size units. The directives provided by the Partition Manager are:

* :ref:`InterfaceRtemsPartitionCreate` - Creates a partition.

* :ref:`InterfaceRtemsPartitionIdent` - Identifies a partition by the object
  name.

* :ref:`InterfaceRtemsPartitionDelete` - Deletes the partition.

* :ref:`InterfaceRtemsPartitionGetBuffer` - Tries to get a buffer from the
  partition.

* :ref:`InterfaceRtemsPartitionReturnBuffer` - Returns the buffer to the
  partition.
