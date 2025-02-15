.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. index:: dual ported memory, definition
.. index:: external addresses, definition
.. index:: internal addresses, definition

Background
==========

A dual-ported memory area (DPMA) is an contiguous block of RAM owned by a
particular processor but which can be accessed by other processors in the
system.  The owner accesses the memory using internal addresses, while other
processors must use external addresses.  RTEMS defines a port as a particular
mapping of internal and external addresses.

There are two system configurations in which dual-ported memory is commonly
found.  The first is tightly-coupled multiprocessor computer systems where the
dual-ported memory is shared between all nodes and is used for inter-node
communication.  The second configuration is computer systems with intelligent
peripheral controllers.  These controllers typically utilize the DPMA for
high-performance data transfers.
