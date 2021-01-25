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

.. Generated from spec:/acfg/if/group-posix

POSIX API Configuration
=======================

This section describes configuration options related to the POSIX API.  Most
POSIX API objects are available by default since RTEMS 5.1.  The queued signals
and timers are only available if RTEMS was built with the ``--enable-posix``
build configuration option.

.. Generated from spec:/acfg/if/max-posix-keys

.. index:: CONFIGURE_MAXIMUM_POSIX_KEYS

.. _CONFIGURE_MAXIMUM_POSIX_KEYS:

CONFIGURE_MAXIMUM_POSIX_KEYS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_KEYS``

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
    The value of this configuration option defines the maximum number of POSIX
    API Keys that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. Generated from spec:/acfg/if/max-posix-key-value-pairs

.. index:: CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS

.. _CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS:

CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS
---------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_KEY_VALUE_PAIRS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is
    :ref:`CONFIGURE_MAXIMUM_POSIX_KEYS` *
    :ref:`CONFIGURE_MAXIMUM_TASKS` +
    :ref:`CONFIGURE_MAXIMUM_POSIX_THREADS`.

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
    The value of this configuration option defines the maximum number of key
    value pairs used by POSIX API Keys that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

    A key value pair is created by :c:func:`pthread_setspecific` if the value
    is not `NULL <https://en.cppreference.com/w/c/types/NULL>`_, otherwise it is deleted.

.. Generated from spec:/acfg/if/max-posix-message-queues

.. index:: CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES

.. _CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES:

CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES
--------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUES``

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

    * It shall be small enough so that the
      RTEMS Workspace size calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of POSIX
    API Message Queues that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.  You have to account for the memory used to
    store the messages of each message queue, see
    :ref:`CONFIGURE_MESSAGE_BUFFER_MEMORY`.

.. Generated from spec:/acfg/if/max-posix-queued-signals

.. index:: CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS

.. _CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS:

CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS
--------------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_QUEUED_SIGNALS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

    * It shall be small enough so that the
      RTEMS Workspace size calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

    * It shall be zero if the POSIX API is not
      enabled (e.g. RTEMS was built without the ``--enable-posix`` build
      configuration option).  Otherwise a compile time error in the configuration
      file will occur.

DESCRIPTION:
    The value of this configuration option defines the maximum number of POSIX
    API Queued Signals that can be concurrently active.

NOTES:
    Unlimited objects are not available for queued signals.

    Queued signals are only available if RTEMS was built with the
    ``--enable-posix`` build configuration option.

.. Generated from spec:/acfg/if/max-posix-semaphores

.. index:: CONFIGURE_MAXIMUM_POSIX_SEMAPHORES

.. _CONFIGURE_MAXIMUM_POSIX_SEMAPHORES:

CONFIGURE_MAXIMUM_POSIX_SEMAPHORES
----------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_SEMAPHORES``

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

    * It shall be small enough so that the
      RTEMS Workspace size calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of POSIX
    API Named Semaphores that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

    Named semaphores are created with :c:func:`sem_open`.  Semaphores
    initialized with :c:func:`sem_init` are not affected by this
    configuration option since the storage space for these semaphores is
    user-provided.

.. Generated from spec:/acfg/if/max-posix-shms

.. index:: CONFIGURE_MAXIMUM_POSIX_SHMS

.. _CONFIGURE_MAXIMUM_POSIX_SHMS:

CONFIGURE_MAXIMUM_POSIX_SHMS
----------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_SHMS``

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

    * It shall be small enough so that the
      RTEMS Workspace size calculation carried out by ``<rtems/confdefs.h>`` does
      not overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

    * It may be defined through
      :c:func:`rtems_resource_unlimited` the enable unlimited objects for this
      object class, if the value passed to :c:func:`rtems_resource_unlimited`
      satisfies all other constraints of this configuration option.

DESCRIPTION:
    The value of this configuration option defines the maximum number of POSIX
    API Shared Memory objects that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

.. Generated from spec:/acfg/if/max-posix-threads

.. index:: CONFIGURE_MAXIMUM_POSIX_THREADS

.. _CONFIGURE_MAXIMUM_POSIX_THREADS:

CONFIGURE_MAXIMUM_POSIX_THREADS
-------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_THREADS``

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

DESCRIPTION:
    The value of this configuration option defines the maximum number of POSIX
    API Threads that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

    This calculations for the required memory in the RTEMS Workspace for threads
    assume that each thread has a minimum stack size and has floating point
    support enabled.  The configuration option :ref:`CONFIGURE_EXTRA_TASK_STACKS` is used
    to specify thread stack requirements **above** the minimum size required.

    The maximum number of Classic API Tasks is specified by
    :ref:`CONFIGURE_MAXIMUM_TASKS`.

    All POSIX threads have floating point enabled.

.. Generated from spec:/acfg/if/max-posix-timers

.. index:: CONFIGURE_MAXIMUM_POSIX_TIMERS

.. _CONFIGURE_MAXIMUM_POSIX_TIMERS:

CONFIGURE_MAXIMUM_POSIX_TIMERS
------------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_POSIX_TIMERS``

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

    * It shall be zero if the POSIX API is not
      enabled (e.g. RTEMS was built without the ``--enable-posix`` build
      configuration option).  Otherwise a compile time error in the configuration
      file will occur.

DESCRIPTION:
    The value of this configuration option defines the maximum number of POSIX
    API Timers that can be concurrently active.

NOTES:
    This object class can be configured in unlimited allocation mode, see
    :ref:`ConfigUnlimitedObjects`.

    Timers are only available if RTEMS was built with the
    ``--enable-posix`` build configuration option.

.. Generated from spec:/acfg/if/min-posix-thread-stack-size

.. index:: CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE
.. index:: minimum POSIX thread stack size

.. _CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE:

CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE
-----------------------------------------

CONSTANT:
    ``CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is two times the value of
    :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be small enough so that the task
      stack space calculation carried out by ``<rtems/confdefs.h>`` does not
      overflow an integer of type `uintptr_t <https://en.cppreference.com/w/c/types/integer>`_.

    * It shall be greater than or equal to a
      BSP-specific and application-specific minimum value.

DESCRIPTION:
    The value of this configuration option defines the minimum stack size in
    bytes for every POSIX thread in the system.

NOTES:
    None.
