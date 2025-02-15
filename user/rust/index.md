.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 embedded brains GmbH & Co. KG

.. index:: Rust

.. _Rust:

Rust
****

The number of users of the modern programming language Rust grows
steadily. Fans can opt for RTEMS as OS when writing Rust
applications on embedded devices. The sections of this chapter
provide step by step instructions to get started.

There are two basic approaches to use Rust together with RTEMS:

Bare metal Rust
  The Rust compiler translates the application code for a target
  without operating system -- for example ``sparc-unknown-none-elf``.
  The disadvantage of this approach is that no standard Rust library
  is available (``#![no_std]`` in Rust code). The advantage is
  that all targets supported by both Rust and RTEMS can
  immediately be used.

Rust with std lib
  The Rust compiler translates the application code for an RTEMS
  specific target -- for example ``armv7-unknown-rtems-eabi``.
  The advantage is that all functions from the standard Rust library
  are available. The disadvantage is that such targets are rare.

  At the time of writing no such target exists. A first target for ARM
  is planed to be published soon. The reason for the lack of targets is
  that one must be implemented for each architecture, published to the
  Rust compiler sources and maintained by someone.

Common to all approaches is the general way how Rust is used with RTEMS:

1. The RTEMS tools for the architecture are needed. See
   :ref:`Install the Tool Suite <QuickStartTools>`.

2. The RTEMS kernel for the BSP is compiled to libraries. See
   :ref:`Build a Board Support Package (BSP) <QuickStartBSPBuild>`.

3. A Rust project for the application code is created and configured.

4. The Rust code of the application is compiled into a library
   for the target.

5. The Rust application library and the RTEMS kernel libraries are
   linked together into a single executable file.

6. The executable file is either run in an emulator or loaded onto
   the hardware and executed there.

At the time of writing, there is no common Rust interface for the
pubic RTEMS functions available. Currently, developers must declare RTEMS
functions they want to call. This is especially relevant when the
*Bare metal Rust* approach is used.

.. toctree::

    bare-metal
