.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2017 On-Line Applications Research Corporation (OAR)

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

.. Generated from spec:/rtems/task/if/group

.. _TaskManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/task/if/create
.. spec:/rtems/task/if/construct
.. spec:/rtems/task/if/ident
.. spec:/rtems/task/if/self
.. spec:/rtems/task/if/start
.. spec:/rtems/task/if/restart
.. spec:/rtems/task/if/delete
.. spec:/rtems/task/if/exit
.. spec:/rtems/task/if/suspend
.. spec:/rtems/task/if/resume
.. spec:/rtems/task/if/is-suspended
.. spec:/rtems/task/if/set-priority
.. spec:/rtems/task/if/get-priority
.. spec:/rtems/task/if/mode
.. spec:/rtems/task/if/wake-after
.. spec:/rtems/task/if/wake-when
.. spec:/rtems/task/if/get-scheduler
.. spec:/rtems/task/if/set-scheduler
.. spec:/rtems/task/if/get-affinity
.. spec:/rtems/task/if/set-affinity
.. spec:/rtems/task/if/iterate
.. spec:/rtems/task/if/storage-size

The Task Manager provides a comprehensive set of directives to create, delete,
and administer tasks. The directives provided by the Task Manager are:

* :ref:`InterfaceRtemsTaskCreate` - Creates a task.

* :ref:`InterfaceRtemsTaskConstruct` - Constructs a task from the specified
  task configuration.

* :ref:`InterfaceRtemsTaskIdent` - Identifies a task by the object name.

* :ref:`InterfaceRtemsTaskSelf` - Gets the task identifier of the calling task.

* :ref:`InterfaceRtemsTaskStart` - Starts the task.

* :ref:`InterfaceRtemsTaskRestart` - Restarts the task.

* :ref:`InterfaceRtemsTaskDelete` - Deletes the task.

* :ref:`InterfaceRtemsTaskExit` - Deletes the calling task.

* :ref:`InterfaceRtemsTaskSuspend` - Suspends the task.

* :ref:`InterfaceRtemsTaskResume` - Resumes the task.

* :ref:`InterfaceRtemsTaskIsSuspended` - Checks if the task is suspended.

* :ref:`InterfaceRtemsTaskSetPriority` - Sets the real priority or gets the
  current priority of the task.

* :ref:`InterfaceRtemsTaskGetPriority` - Gets the current priority of the task
  with respect to the scheduler.

* :ref:`InterfaceRtemsTaskMode` - Gets and optionally sets the mode of the
  calling task.

* :ref:`InterfaceRtemsTaskWakeAfter` - Wakes up after an interval in
  :term:`clock ticks <clock tick>` or yields the processor.

* :ref:`InterfaceRtemsTaskWakeWhen` - Wakes up when specified.

* :ref:`InterfaceRtemsTaskGetScheduler` - Gets the home scheduler of the task.

* :ref:`InterfaceRtemsTaskSetScheduler` - Sets the home scheduler for the task.

* :ref:`InterfaceRtemsTaskGetAffinity` - Gets the processor affinity of the
  task.

* :ref:`InterfaceRtemsTaskSetAffinity` - Sets the processor affinity of the
  task.

* :ref:`InterfaceRtemsTaskIterate` - Iterates over all tasks and invokes the
  visitor routine for each task.

* :ref:`InterfaceRTEMSTASKSTORAGESIZE` - Gets the recommended task storage area
  size for the size and task attributes.
