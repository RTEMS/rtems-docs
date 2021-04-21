.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Introduction
============

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
both hardware and software, to be viewed logically as a single system.

The directives provided by the  Manager are:

- :ref:`rtems_multiprocessing_announce`
