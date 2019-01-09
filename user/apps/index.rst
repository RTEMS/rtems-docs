.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _applications:

Applications
============
.. index:: Applications

this section discusses RTEMS Applications and guides you on how to create an
application.

Executables
-----------

The RTEMS applications are statically linked executable that run on bare target
hardware in a single address space. The application code, RTEMS kernel and any
libraries are linked to a fixed address. The applications are loaded into the
target's address space and run with full control of the processor and all
hardware connected.

The RTEMS tools generate Extendable Loadable Format or ELF format files by
default and we recommend your build script alwas
