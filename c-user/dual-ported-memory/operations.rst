.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Creating a Port
---------------

The ``rtems_port_create`` directive creates a port into a DPMA with the
user-defined name.  The user specifies the association between internal and
external representations for the port being created.  RTEMS allocates a
Dual-Ported Memory Control Block (DPCB) from the DPCB free list to maintain the
newly created DPMA.  RTEMS also generates a unique dual-ported memory port ID
which is returned to the calling task.  RTEMS does not initialize the
dual-ported memory area or access any memory within it.

Obtaining Port IDs
------------------

When a port is created, RTEMS generates a unique port ID and assigns it to the
created port until it is deleted.  The port ID may be obtained by either of two
methods.  First, as the result of an invocation of the``rtems_port_create``
directive, the task ID is stored in a user provided location.  Second, the port
ID may be obtained later using the ``rtems_port_ident`` directive.  The port ID
is used by other dual-ported memory manager directives to access this port.

Converting an Address
---------------------

The ``rtems_port_external_to_internal`` directive is used to convert an address
from external to internal representation for the specified port.  The
``rtems_port_internal_to_external`` directive is used to convert an address
from internal to external representation for the specified port.  If an attempt
is made to convert an address which lies outside the specified DPMA, then the
address to be converted will be returned.

Deleting a DPMA Port
--------------------

A port can be removed from the system and returned to RTEMS with the
``rtems_port_delete`` directive.  When a port is deleted, its control block is
returned to the DPCB free list.
