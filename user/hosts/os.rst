.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _host-os:

Host Operating Systems
~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: *GDB and Python*

   RTEMS uses Python in GDB to aid debugging which means GDB needs to be built
   with Python development libraries. Please check the RSB documentation and
   install the packages specified for your host. Make sure a python development
   package is included.

A wide range of host operating systems and hardware can be used. The host
operating systems supported are:

- Linux
- FreeBSD
- NetBSD
- Apple OS X
- Windows
- Solaris

The functionality on a POSIX operating such as Linux and FreeBSD is similar and
most features on Windows are supported but you are best to ask on the
:r:list:`users` if you have a specific question.

We recommend you maintain your operating system by installing any updates.
