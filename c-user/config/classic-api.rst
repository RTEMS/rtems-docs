.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Classic API Configuration
=========================

This section describes configuration options related to the Classic API.

.. index:: CONFIGURE_MAXIMUM_BARRIERS

.. _CONFIGURE_MAXIMUM_BARRIERS:

CONFIGURE_MAXIMUM_BARRIERS
--------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_BARRIERS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Barriers that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. index:: CONFIGURE_MAXIMUM_MESSAGE_QUEUES

.. _CONFIGURE_MAXIMUM_MESSAGE_QUEUES:

CONFIGURE_MAXIMUM_MESSAGE_QUEUES
--------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_MESSAGE_QUEUES``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Message Queues that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.  You have to account for the memory used to
    store the messages of each message queue, see
    :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.

.. index:: CONFIGURE_MAXIMUM_PARTITIONS

.. _CONFIGURE_MAXIMUM_PARTITIONS:

CONFIGURE_MAXIMUM_PARTITIONS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PARTITIONS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Partitions that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. index:: CONFIGURE_MAXIMUM_PERIODS

.. _CONFIGURE_MAXIMUM_PERIODS:

CONFIGURE_MAXIMUM_PERIODS
-------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PERIODS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Periods that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. index:: CONFIGURE_MAXIMUM_PORTS

.. _CONFIGURE_MAXIMUM_PORTS:

CONFIGURE_MAXIMUM_PORTS
-----------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_PORTS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Ports that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. index:: CONFIGURE_MAXIMUM_REGIONS

.. _CONFIGURE_MAXIMUM_REGIONS:

CONFIGURE_MAXIMUM_REGIONS
-------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_REGIONS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Regions that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. index:: CONFIGURE_MAXIMUM_SEMAPHORES

.. _CONFIGURE_MAXIMUM_SEMAPHORES:

CONFIGURE_MAXIMUM_SEMAPHORES
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_SEMAPHORES``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Semaphore that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

    In SMP configurations, the size of a Semaphore Control Block depends on the
    scheduler count (see :ref:`ConfigurationSchedulerTable`).  The semaphores
    using the :ref:`MrsP` need a ceiling priority per scheduler.

.. index:: CONFIGURE_MAXIMUM_TASKS

.. _CONFIGURE_MAXIMUM_TASKS:

CONFIGURE_MAXIMUM_TASKS
-----------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_TASKS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It shall be small enough so that the task
      stack space calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type ``uintptr_t``.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Tasks that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

    The calculations for the required memory in the RTEMS Workspace for tasks
    assume that each task has a minimum stack size and has floating point
    support enabled.  The configuration parameter
    ``CONFIGURE_EXTRA_TASK_STACKS`` is used to specify task stack requirements
    *ABOVE* the minimum size required.  See :ref:`Reserve Task/Thread Stack
    Memory Above Minimum` for more information about
    ``CONFIGURE_EXTRA_TASK_STACKS``.

    The maximum number of POSIX threads is specified by
    :ref:`CONFIGURE_MAXIMUM_POSIX_THREADS`.

    A future enhancement to ``<rtems/confdefs.h>`` could be to eliminate the
    assumption that all tasks have floating point enabled. This would require
    the addition of a new configuration parameter to specify the number of
    tasks which enable floating point support.

.. index:: CONFIGURE_MAXIMUM_TIMERS

.. _CONFIGURE_MAXIMUM_TIMERS:

CONFIGURE_MAXIMUM_TIMERS
------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_TIMERS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API Timers that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. index:: CONFIGURE_MAXIMUM_USER_EXTENSIONS

.. _CONFIGURE_MAXIMUM_USER_EXTENSIONS:

CONFIGURE_MAXIMUM_USER_EXTENSIONS
---------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_USER_EXTENSIONS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to 65535.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

DESCRIPTION:
    The value of this configuration option defines the maximum number of Classic
    API User Extensions that can be concurrently active.

NOTES:
    This object class cannot be configured in unlimited allocation mode.
