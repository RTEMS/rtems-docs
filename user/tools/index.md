.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017 Chris Johns <chrisj@rtems.org>

.. _HostTools:

Host Tools
**********

The RTEMS kernel is developed on host computers cross-compiled and linking the
kernel, language runtime libraries, third-party packages and application source
code so it can run on target hardware. RTEMS and some of the hardware it
support cannot self-host so we need a range of tools to support the wide range
of avaliable host computers users wish to develop on. This section details the
tools available on the host computers to help support RTEMS users and
developers.

.. toctree::

   linker
   symbols
   exeinfo
   bsp-builder
   tester
   boot-image
   tftp-proxy
