.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1989, 2010 On-Line Applications Research Corporation (OAR)

Introduction
************

This document describes the RTEMS development environment.  Discussions are
provided for the following topics:

- the directory structure used by RTEMS,

- usage of the GNU Make utility within the RTEMS development environment,

- sample applications, and

- the RTEMS specific utilities.

RTEMS was designed as a reusable software component.  Highly reusable software
such as RTEMS is typically distributed in the form of source code without
providing any support tools.  RTEMS is the foundation for a complex family of
facilities including board support packages, device drivers, and support
libraries.  The RTEMS Development Environment is not a CASE tool.  It is a
collection of tools designed to reduce the complexity of using and enhancing
the RTEMS family.  Tools are provided which aid in the management of the
development, maintenance, and usage of RTEMS, its run-time support facilities,
and applications which utilize the executive.

A key component of the RTEMS development environment is the GNU family of free
tools.  This is robust set of development and POSIX compatible tools for which
source code is freely available.  The primary compilers, assemblers, linkers,
and make utility used by the RTEMS development team are the GNU tools.  They
are highly portable supporting a wide variety of host computers and, in the
case of the development tools, a wide variety of target processors.

It is recommended that the RTEMS developer become familiar with the RTEMS
Development Environment before proceeding with any modifications to the
executive source tree.  The source code for the executive is very modular and
source code is divided amongst directories based upon functionality as well as
dependencies on CPU and target board.  This organization is aimed at isolating
and minimizing non-portable code.  This has the immediate result that adding
support for a new CPU or target board requires very little "wandering" around
the source tree.
