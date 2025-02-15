.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

.. index:: initialization tasks

Initialization Tasks
--------------------

Initialization task(s) are the mechanism by which RTEMS transfers initial
control to the user's application.  Initialization tasks differ from other
application tasks in that they are defined in the User Initialization Tasks
Table and automatically created and started by RTEMS as part of its
initialization sequence.  Since the initialization tasks are scheduled using
the same algorithm as all other RTEMS tasks, they must be configured at a
priority and mode which will ensure that they will complete execution before
other application tasks execute.  Although there is no upper limit on the
number of initialization tasks, an application is required to define at least
one.

A typical initialization task will create and start the static set of
application tasks.  It may also create any other objects used by the
application.  Initialization tasks which only perform initialization should
delete themselves upon completion to free resources for other tasks.
Initialization tasks may transform themselves into a "normal" application task.
This transformation typically involves changing priority and execution mode.
RTEMS does not automatically delete the initialization tasks.

The Idle Task
-------------

The Idle Task is the lowest priority task in a system and executes only when no
other task is ready to execute.  The default implementation of this task
consists of an infinite loop. RTEMS allows the Idle Task body to be replaced by
a CPU specific implementation, a BSP specific implementation or an application
specific implementation.

The Idle Task is preemptible and *WILL* be preempted when any other task is
made ready to execute.  This characteristic is critical to the overall behavior
of any application.

Initialization Manager Failure
------------------------------

System initialization errors are fatal.  See :ref:`internal_errors`.
