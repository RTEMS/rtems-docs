.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Introduction
============

The concept of scheduling in real-time systems dictates the ability to provide
an immediate response to specific external events, particularly the necessity of
scheduling tasks to run within a specified time limit after the occurrence of
an event.  For example, software embedded in life-support systems used to
monitor hospital patients must take instant action if a change in the patient's
status is detected.

The component of RTEMS responsible for providing this capability is
appropriately called the scheduler.  The scheduler's sole purpose is to
allocate the all important resource of processor time to the various tasks
competing for attention.

The directives provided by the scheduler manager are:

- :ref:`rtems_scheduler_ident`

- :ref:`rtems_scheduler_ident_by_processor`

- :ref:`rtems_scheduler_ident_by_processor_set`

- :ref:`rtems_scheduler_get_maximum_priority`

- :ref:`rtems_scheduler_map_priority_to_posix`

- :ref:`rtems_scheduler_map_priority_from_posix`

- :ref:`rtems_scheduler_get_processor`

- :ref:`rtems_scheduler_get_processor_maximum`

- :ref:`rtems_scheduler_get_processor_set`

- :ref:`rtems_scheduler_add_processor`

- :ref:`rtems_scheduler_remove_processor`
