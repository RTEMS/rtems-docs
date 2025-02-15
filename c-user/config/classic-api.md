.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG
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

.. Generated from spec:/acfg/if/group-classic

Classic API Configuration
=========================

This section describes configuration options related to the Classic API.

.. Generated from spec:/acfg/if/max-barriers

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_BARRIERS

.. _CONFIGURE_MAXIMUM_BARRIERS:

CONFIGURE_MAXIMUM_BARRIERS
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_BARRIERS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Barriers that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-message-queues

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_MESSAGE_QUEUES

.. _CONFIGURE_MAXIMUM_MESSAGE_QUEUES:

CONFIGURE_MAXIMUM_MESSAGE_QUEUES
--------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_MESSAGE_QUEUES``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Message Queues that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.  You have to account for the memory used to
store the messages of each message queue, see
:ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-partitions

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_PARTITIONS

.. _CONFIGURE_MAXIMUM_PARTITIONS:

CONFIGURE_MAXIMUM_PARTITIONS
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_PARTITIONS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Partitions that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-periods

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_PERIODS

.. _CONFIGURE_MAXIMUM_PERIODS:

CONFIGURE_MAXIMUM_PERIODS
-------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_PERIODS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Periods that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-ports

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_PORTS

.. _CONFIGURE_MAXIMUM_PORTS:

CONFIGURE_MAXIMUM_PORTS
-----------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_PORTS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Ports that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-regions

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_REGIONS

.. _CONFIGURE_MAXIMUM_REGIONS:

CONFIGURE_MAXIMUM_REGIONS
-------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_REGIONS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Regions that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-semaphores

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_SEMAPHORES

.. _CONFIGURE_MAXIMUM_SEMAPHORES:

CONFIGURE_MAXIMUM_SEMAPHORES
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_SEMAPHORES``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Semaphore that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

In SMP configurations, the size of a Semaphore Control Block depends on the
scheduler count (see :ref:`ConfigurationSchedulerTable`).  The semaphores
using the :ref:`MrsP` need a ceiling priority per scheduler.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-tasks

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_TASKS

.. _CONFIGURE_MAXIMUM_TASKS:

CONFIGURE_MAXIMUM_TASKS
-----------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_TASKS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Tasks that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

The calculations for the required memory in the RTEMS Workspace for tasks
assume that each task has a minimum stack size and has floating point
support enabled.  The configuration option :ref:`CONFIGURE_EXTRA_TASK_STACKS` is used
to specify task stack requirements *above* the minimum size required.

The maximum number of POSIX threads is specified by
:ref:`CONFIGURE_MAXIMUM_POSIX_THREADS`.

A future enhancement to ``<rtems/confdefs.h>`` could be to eliminate the
assumption that all tasks have floating point enabled. This would require
the addition of a new configuration parameter to specify the number of
tasks which enable floating point support.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option shall be small enough so that the task
  stack space calculation carried out by ``<rtems/confdefs.h>`` does not
  overflow an integer of type `uintptr_t
  <https://en.cppreference.com/w/c/types/integer>`_.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-timers

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_TIMERS

.. _CONFIGURE_MAXIMUM_TIMERS:

CONFIGURE_MAXIMUM_TIMERS
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_TIMERS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API Timers that can be concurrently active.

.. rubric:: NOTES:

This object class can be configured in unlimited allocation mode, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

* The value of the configuration option may be defined through
  :ref:`InterfaceRtemsResourceUnlimited` the enable unlimited objects for the
  object class, if the value passed to :ref:`InterfaceRtemsResourceUnlimited`
  satisfies all other constraints of the configuration option.

.. Generated from spec:/acfg/if/max-user-extensions

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MAXIMUM_USER_EXTENSIONS

.. _CONFIGURE_MAXIMUM_USER_EXTENSIONS:

CONFIGURE_MAXIMUM_USER_EXTENSIONS
---------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MAXIMUM_USER_EXTENSIONS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of Classic
API User Extensions that can be concurrently active.

.. rubric:: NOTES:

This object class cannot be configured in unlimited allocation mode.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to 65535.

* The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.

.. Generated from spec:/acfg/if/min-tasks-with-user-provided-storage

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE

.. _CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE:

CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE
--------------------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the minimum count of Classic
API Tasks which are constructed by :ref:`InterfaceRtemsTaskConstruct`.

.. rubric:: NOTES:

By default, the calculation for the required memory in the RTEMS Workspace
for tasks assumes that all Classic API Tasks are created by
:ref:`InterfaceRtemsTaskCreate`.  This configuration option can be used to
reduce the required memory for the system-provided task storage areas since
tasks constructed by :ref:`InterfaceRtemsTaskConstruct` use a user-provided
task storage area.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  :ref:`CONFIGURE_MAXIMUM_TASKS`.
