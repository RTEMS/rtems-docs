.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _posix-hosts:

POSIX Hosts
~~~~~~~~~~~

POSIX hosts are most Unix operating systems such as Linux, FreeBSD and
NetBSD. RTEMS development works well on Unix and can scale from a single user
and a desktop machine to a team with decentralised or centralised development
infrastructure.

Root Access
^^^^^^^^^^^

You either have ``root`` access to your host development machine or you do
not. Some users are given hardware that is centrally managed. If you do not
have ``root`` access you can create your work environment in your home
directory. You could use a prefix of :file:`$HOME/development/rtems` or
:file:`$HOME/rtems`. Note, the ``$HOME`` environment variable can be
substituted with ``~``.

:ref:`prefixes` details using Prefixes to manage the installation.

RTEMS Tools and packages do not require ``root`` access
to be built and we encourage you to not build the tools as ``root``. If you
need to control write access then it is best to manage this with groups
assigned to users.

If you have ``root`` access you can decide to install the tools under any
suitable prefix. This may depend on the hardware in your host development
machine. If the machine is a centralised build server the prefix may be used to
separate production versions from the test versions and the prefix paths may
have restricted access rights to only those who manage and have configuration
control of the machine. We call this project sandboxing and
:ref:`project-sandboxing` explains this in more detail.
