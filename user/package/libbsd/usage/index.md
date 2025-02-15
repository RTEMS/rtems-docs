.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 embedded brains GmbH & Co. KG

.. _libbsd_user:

LibBSD Usage
************

This chapter is thought for people who want to mainly use LibBSD in an
application. It describes basic initialization and how to use various features
of LibBSD.

FIXME: This documentation is still under construction. Contributions are
welcome.

Basics
------

There are two basic configuration models:

1. Using a configuration that is as close as possible to the FreeBSD
   configuration. That usually means that you create a `/etc/rc.conf` and some
   other configuration files. Advantage of this model is that it is simple and
   straightforward. Usually the FreeBSD documentation can be used to find out
   how to configure something. The disadvantage is that the configuration is not
   known at compile time and therefore extra code has to be linked in which
   results in bigger code sizes. This method is recommended for systems that
   do not have serious memory limitations.

2. Alternatively it is possible to do the configuration with calls to certain
   functions (like `ifconfig`). Disadvantage is that this needs a lot more
   detail knowledge about the internals of LibBSD and what has to be
   initialized. The advantage is that the linker can remove unused code and
   therefore it is more suitable for systems with a relatively small memory
   footprint.
