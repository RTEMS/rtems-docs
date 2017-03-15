.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2017 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

Tools
*****

The RTEMS kernel is developed on a host computer where the user's application
code is cross-compiled to the target hardware's processor instructions and
linked to the RTEMS kernel and language runtime libraries, and any 3rd party
packages. RTEMS is not a multiprocess operating system and self hosting the
types of tools need to create executables is not feasable. As a result a range
of support tools are needed and they need run on the wide range of avaliable
host computers users wish to develop on. This section details the tools
available on host computers RTEMS users and developers need to create RTEMS
executables.

.. include:: linker.rst
.. include:: symbols.rst
.. include:: exeinfo.rst
.. include:: trace-linker.rst
.. include:: bsp-builder.rst
