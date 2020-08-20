.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Introduction
============

Any real-time executive must provide a mechanism for quick response to
externally generated interrupts to satisfy the critical time constraints of the
application.  The interrupt manager provides this mechanism for RTEMS.  This
manager permits quick interrupt response times by providing the critical
ability to alter task execution which allows a task to be preempted upon exit
from an ISR.  The interrupt manager includes the following directive:

- :ref:`rtems_interrupt_catch`

- :ref:`rtems_interrupt_disable`

- :ref:`rtems_interrupt_enable`

- :ref:`rtems_interrupt_flash`

- :ref:`rtems_interrupt_local_disable`

- :ref:`rtems_interrupt_local_enable`

- :ref:`rtems_interrupt_lock_initialize`

- :ref:`rtems_interrupt_lock_acquire`

- :ref:`rtems_interrupt_lock_release`

- :ref:`rtems_interrupt_lock_acquire_isr`

- :ref:`rtems_interrupt_lock_release_isr`

- :ref:`rtems_interrupt_is_in_progress`
