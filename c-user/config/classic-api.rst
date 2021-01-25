.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/acfg/if/max-message-queues

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

.. Generated from spec:/acfg/if/max-partitions

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

.. Generated from spec:/acfg/if/max-periods

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

.. Generated from spec:/acfg/if/max-ports

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

.. Generated from spec:/acfg/if/max-regions

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

.. Generated from spec:/acfg/if/max-semaphores

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

.. Generated from spec:/acfg/if/max-tasks

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
      overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

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
    support enabled.  The configuration option :ref:`CONFIGURE_EXTRA_TASK_STACKS` is used
    to specify task stack requirements *above* the minimum size required.

    The maximum number of POSIX threads is specified by
    :ref:`CONFIGURE_MAXIMUM_POSIX_THREADS`.

    A future enhancement to ``<rtems/confdefs.h>`` could be to eliminate the
    assumption that all tasks have floating point enabled. This would require
    the addition of a new configuration parameter to specify the number of
    tasks which enable floating point support.

.. Generated from spec:/acfg/if/max-thread-local-storage-size

.. index:: CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE

.. _CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE:

CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE
-------------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

DESCRIPTION:
    If the value of this configuration option is greater than zero, then it
    defines the maximum thread-local storage size, otherwise the thread-local
    storage size is defined by the linker depending on the thread-local storage
    objects used by the application in the statically-linked executable.

NOTES:
    This configuration option can be used to reserve space for the dynamic linking
    of modules with thread-local storage objects.

    If the thread-local storage size defined by the thread-local storage
    objects used by the application in the statically-linked executable is greater
    than a non-zero value of this configuration option, then a fatal error will
    occur during system initialization.

    Use :c:func:`RTEMS_ALIGN_UP` and
    :c:macro:`RTEMS_TASK_STORAGE_ALIGNMENT` to adjust the size to meet the
    minimum alignment requirement of a thread-local storage area.

    The actual thread-local storage size is determined when the application
    executable is linked.  The ``rtems-exeinfo`` command line tool included in
    the RTEMS Tools can be used to obtain the thread-local storage size and
    alignment of an application executable.

.. Generated from spec:/acfg/if/max-timers

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

.. Generated from spec:/acfg/if/max-user-extensions

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

.. Generated from spec:/acfg/if/min-tasks-with-user-provided-storage

.. index:: CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE

.. _CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE:

CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE
--------------------------------------------------

CONSTANT:
    ``CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to :ref:`CONFIGURE_MAXIMUM_TASKS`.

DESCRIPTION:
    The value of this configuration option defines the minimum count of Classic
    API Tasks which are constructed by :c:func:`rtems_task_construct`.

NOTES:
    By default, the calculation for the required memory in the RTEMS Workspace
    for tasks assumes that all Classic API Tasks are created by
    :c:func:`rtems_task_create`.  This configuration option can be used to
    reduce the required memory for the system-provided task storage areas since
    tasks constructed by :c:func:`rtems_task_construct` use a user-provided
    task storage area.
