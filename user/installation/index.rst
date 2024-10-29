.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. index:: Installation
.. _installation:

Installation
************

This section details how to set up and install the RTEMS Ecosystem. 
You will be asked to follow a few simple steps and when you have finished you
will have a development environment set up you can use to build applications
for RTEMS. You will have also created a development environment you and a team
can adapt for a project of any size and complexity.

.. index:: Tools

RTEMS applications are developed using cross-development tools running on a
development computer, more commonlly referred to as the host computer. These
are typically your desktop machine or a special build server. 


The RTEMS Project supports two set ups, release and developer
environments. Release installations create the tools and kernel in a single
pass ready for you to use. The tools and kernel are stable and only bug fixes
are added creating new dot point releases. The developer set up tracks the Git
repositories for the tools and kernel.

.. comment: code block warning is in kernel.rst

.. toctree::

   releases
   developer
   kernel
   project-sandboxing
