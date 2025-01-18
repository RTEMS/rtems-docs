.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

Introduction
************

.. _Overview:

Overview
========

You are someone looking for a real-time operating system.  This document

- presents the basic features of RTEMS, so that you can decide if it is worth to
  look at,

- gives you a :ref:`quick start <QuickStart>` to install all the tools
  necessary to work with RTEMS, and

- helps you to build an example application on top of RTEMS.

Features
========

The Real-Time Executive for Multiprocessor Systems (:ref:term:`RTEMS`) is a
multi-threaded, single address-space, real-time operating system with no
kernel-space/user-space separation.  It is capable to operate in an
:ref:term:`SMP` configuration providing a state of the art feature set.

RTEMS is licensed under a
`modified GPL 2.0 or later license with an exception for static linking
<https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/LICENSE.md>`_
[#]_.  It exposes no license requirements on application code.  The third-party
software used and distributed by RTEMS which may be linked to the application
is licensed under permissive open source licenses.  Everything necessary to
build RTEMS applications is available as open source software.  This makes you
completely vendor independent.

RTEMS provides the following basic feature set:

- :ref:term:`APIs <API>`

    - :ref:term:`POSIX` with
      `pthreads <http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html>`_
      (enables a broad range of standard software to run on RTEMS)

    - `Classic <https://docs.rtems.org/branches/master/c-user.pdf>`_

    - :ref:term:`C11` (including
      `thread <https://en.cppreference.com/w/c/thread>`_ support)

    - :ref:term:`C++11` (including
      `thread <https://en.cppreference.com/w/cpp/thread>`_ support)

    - Newlib and :ref:term:`GCC` internal

- Programming languages

    - C/C++/OpenMP (RTEMS Source Builder, RSB)

    - Ada (RSB, ``--with-ada``)

    - Erlang

    - Fortran (RSB, ``--with-fortran``)

    - Python and MicroPython

    - :ref:`Rust <Rust>`

- Parallel languages

    - :ref:term:`EMB²`

    - Google Go [#]_

    - :ref:term:`OpenMP` 4.5

- Thread synchronization and communication

    - Mutexes with and without locking protocols

    - Counting semaphores

    - Binary semaphores

    - Condition variables

    - Events

    - Message queues

    - Barriers

    - :ref:term:`Futex` (used by :ref:term:`OpenMP` barriers)

    - Epoch Based Reclamation (libbsd)

- Locking protocols

    - Transitive Priority Inheritance

    - :ref:term:`OMIP` (SMP feature)

    - Priority Ceiling

    - :ref:term:`MrsP` (SMP feature)

- Scalable timer and timeout support

- Lock-free timestamps (FreeBSD timecounters)

- Responsive interrupt management

- C11/C++11 :ref:term:`TLS` [#]_

- Link-time configurable schedulers

    - Fixed-priority

    - Job-level fixed-priority (:ref:term:`EDF`)

    - Constant Bandwidth Server (experimental)

- Clustered scheduling (SMP feature)

    - Flexible link-time configuration

    - Job-level fixed-priority scheduler (:ref:term:`EDF`) with support for
      one-to-one and one-to-all thread to processor affinities (default SMP
      scheduler)

    - Fixed-priority scheduler

    - Proof-of-concept strong :ref:term:`APA` scheduler

- Focus on link-time application-specific configuration

- Linker-set based initialization (similar to global C++ constructors)

- Operating system uses fine-grained locking (SMP feature)

- Dynamic memory allocators

    - First-fit (default)

    - Universal Memory Allocator
      (`UMA <https://www.freebsd.org/cgi/man.cgi?query=uma&sektion=9>`_ ,
      libbsd)

- File systems

    - :ref:term:`IMFS`

    - :ref:term:`FAT`

    - :ref:term:`RFS`

    - :ref:term:`NFSv2`

    - :ref:term:`JFFS2` (NOR flashes)

    - :ref:term:`YAFFS2` (NAND flashes, GPL or commercial license required)

- Device drivers

    - Termios (serial interfaces)

    - I2C (Linux user-space API compatible)

    - SPI (Linux user-space API compatible)

    - Network stacks (legacy, libbsd, lwIP)

    - USB stack (libbsd)

    - SD/MMC card stack (libbsd)

    - Framebuffer (Linux user-space API compatible, Qt)

    - Application runs in kernel-space and can access hardware directly

- libbsd

    - Port of FreeBSD user-space and kernel-space components to RTEMS

    - Easy access to FreeBSD software for RTEMS

    - Support to stay in synchronization with FreeBSD

.. _ecosystem:

Ecosystem
=========
.. index:: Ecosystem

The RTEMS Ecosystem is the collection of tools, packages, code, documentation
and online content provided by the RTEMS Project. The ecosystem provides a way
to develop, maintain, and use RTEMS. It's parts interact with the user, the
host environment, and each other to make RTEMS accessible, useable and
predicable.

The ecosystem is for users, developers and maintainers and it is an ongoing
effort that needs your help and support. The RTEMS project is always improving
the way it delivers the kernel to you and your feedback is important so please
join the mailing lists and contribute back comments, success stories, bugs and
patches.

What the RTEMS project describes here to develop, maintain and use RTEMS does
not dictate what you need to use in your project. You can and should select the
work-flow that best suites the demands of your project and what you are
delivering.

Rational
--------

RTEMS is complex and the focus of the RTEMS Ecosystem is to simplify the
complexity for users by providing a stable documented way to build, configure
and run RTEMS. RTEMS is more than a kernel running real-time applications on
target hardware, it is part of a project's and therefore team's workflow and
every project and team is different.

RTEMS's ecosystem does not mandate a way to work. It is a series of parts,
components, and items that are used to create a suitable development
environment to work with. The processes explained in this manual are the same
things an RTEMS maintainer does to maintain the kernel or an experienced user
does to build their production system. It is important to keep this in mind
when working through this manual. We encourage users to explore what can be
done and to discover ways to make it fit their needs. The ecosystem provided by
the RTEMS Project will not install in a single click of a mouse because we want
users to learn the parts they will come to depend on as their project's
development matures.

The RTEMS Ecosystem provides a standard interface that is the same on all
supported host systems. Standardizing how a user interacts with RTEMS is
important and making that experience portable is also important. As a result
the ecosystem is documented at the command line level and we leave GUI and IDE
integration for users and integrators.

Standardizing the parts and how to use them lets users create processes and
procedures that are stable over releases. The RTEMS Ecosystem generates data
that can be used to audit the build process so their configuration can be
documented.

The ecosystem is based around the source code used in the various parts,
components and items of the RTEMS development environment. A user can create
an archive of the complete build process including all the source code for long
term storage. This is important for projects with a long life cycle.

Open Source
-----------

RTEMS is an open source operating system and an open source project and this
extends to the ecosystem. We encourage users to integrate the processes to
build tools, the kernel and any third-party libraries into their project's
configuration management processes.

All the parts that make up the ecosystem are open source. The ecosystem uses a
package's source code to create an executable on a host so when an example
RTEMS executable is created and run for the first time the user will have built
every tool as well as the executable from source. The RTEMS Project believes
the freedom this gives a user is as important as the freedom of having access
to the source code for a package.

Deployment
----------

The RTEMS Project provides the ecosystem as source code that users can download
to create personalised development environments. The RTEMS Project does not
provide packaging and deployment for a specific host environment, target
architecture or BSP. The RTEMS Project encourages users and organizations to
fill this role for the community. The :ref:`RTEMS Source Builder <RSB>`
provides some aid to :ref:`build and deploy tool binaries <RSBDeployment>`.

.. include:: ../../common/content/real-time-application-systems.rst

.. include:: ../../common/content/real-time-executive.rst

.. [#] The goal is to use the
       `BSD 2-Clause license
       <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/LICENSE.md>`_ for new code
       or code those copyright holder agreed to a license change, see `#3053
       <https://gitlab.rtems.org/rtems/rtos/rtems/-/issues/3053>`_ for the details.

.. [#] See `#2832 <https://gitlab.rtems.org/rtems/rtos/rtems/-/issues/2832>`_.

.. [#] Thread-local storage requires some support by the tool chain and the
       RTEMS architecture support, e.g. context-switch code.  It is supported
       at least on ARM, AArch64, PowerPC, RISC-V, SPARC, MicroBlaze, Nios II,
       and m68k.  Check the `RTEMS CPU Architecture Supplement
       <https://docs.rtems.org/branches/master/cpu-supplement.pdf>`_ if it is
       supported.
