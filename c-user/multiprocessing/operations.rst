.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Announcing a Packet
-------------------

The ``rtems_multiprocessing_announce`` directive is called by the MPCI layer to
inform RTEMS that a packet has arrived from another node.  This directive can
be called from an interrupt service routine or from within a polling routine.
