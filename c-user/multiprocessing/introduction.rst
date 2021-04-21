.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. Generated from spec:/rtems/mp/if/group

.. _MultiprocessingManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/mp/if/announce

The Multiprocessing Manager provides support for heterogeneous multiprocessing
systems based on message passing in a network of multiprocessing nodes.

In multiprocessor real-time systems, new requirements, such as sharing data and
global resources between processors, are introduced.  This requires an
efficient and reliable communications vehicle which allows all processors to
communicate with each other as necessary.  In addition, the ramifications of
multiple processors affect each and every characteristic of a real-time system,
almost always making them more complicated.

RTEMS addresses these issues by providing simple and flexible real-time
multiprocessing capabilities.  The executive easily lends itself to both
tightly-coupled and loosely-coupled configurations of the target system
hardware.  In addition, RTEMS supports systems composed of both homogeneous and
heterogeneous mixtures of processors and target boards.

A major design goal of the RTEMS executive was to transcend the physical
boundaries of the target hardware configuration.  This goal is achieved by
presenting the application software with a logical view of the target system
where the boundaries between processor nodes are transparent.  As a result, the
application developer may designate objects such as tasks, queues, events,
signals, semaphores, and memory blocks as global objects.  These global objects
may then be accessed by any task regardless of the physical location of the
object and the accessing task.  RTEMS automatically determines that the object
being accessed resides on another processor and performs the actions required
to access the desired object.  Simply stated, RTEMS allows the entire system,
both hardware and software, to be viewed logically as a single system. The
directives provided by the Multiprocessing Manager are:

* :ref:`InterfaceRtemsMultiprocessingAnnounce` - Announces the arrival of a
  packet.
