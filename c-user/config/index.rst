.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. index:: configuring a system
.. _Configuring a System:

Configuring a System
********************

.. toctree::

    intro
    general
    classic-api
    classic-init-task
    posix-api
    posix-init-thread
    task-stack-alloc
    msg-queue-buffer
    filesystem
    bdbuf
    bsp-related
    idle-task
    scheduler-general
    scheduler-clustered
    device-driver
    mpci
    libpci

Event Recording Configuration
=============================

.. index:: CONFIGURE_RECORD_EXTENSIONS_ENABLED

.. _CONFIGURE_RECORD_EXTENSIONS_ENABLED:

CONFIGURE_RECORD_EXTENSIONS_ENABLED
-----------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_EXTENSIONS_ENABLED``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    If defined and :ref:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS
    <CONFIGURE_RECORD_PER_PROCESSOR_ITEMS>` is also defined properly, then the
    record extensions are enabled.

NOTES:
    The record extensions capture thread create, start, restart, delete,
    switch, begin, exitted and terminate events.

.. index:: CONFIGURE_RECORD_PER_PROCESSOR_ITEMS

.. _CONFIGURE_RECORD_PER_PROCESSOR_ITEMS:

CONFIGURE_RECORD_PER_PROCESSOR_ITEMS
------------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_PER_PROCESSOR_ITEMS``

DATA TYPE:
    Unsigned integer (``unsigned int``).

RANGE:
    A power of two greater than or equal to 16.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    If defined, then a record item buffer of the specified item count is
    statically allocated for each configured processor
    (:ref:`CONFIGURE_MAXIMUM_PROCESSORS <CONFIGURE_MAXIMUM_PROCESSORS>`).

NOTES:
    None.

.. _ConfigAda:

Ada Configuration
=================

The GNU Ada runtime library (libgnarl) uses threads, mutexes, condition
variables, and signals from the pthreads API.  It uses also thread-local storage
for the Ada Task Control Block (ATCB).  From these resources only the threads
need to be accounted for in the configuration.  You should include the Ada tasks
in your setting of the :ref:`CONFIGURE_MAXIMUM_POSIX_THREADS` configuration
option.

Obsolete Configuration Options
==============================

.. index:: CONFIGURE_BDBUF_BUFFER_COUNT

CONFIGURE_BDBUF_BUFFER_COUNT
----------------------------

This configuration option was introduced in RTEMS 4.7.0 and is obsolete since
RTEMS 4.10.0.

.. index:: CONFIGURE_BDBUF_BUFFER_SIZE

CONFIGURE_BDBUF_BUFFER_SIZE
---------------------------

This configuration option was introduced in RTEMS 4.7.0 and is obsolete since
RTEMS 4.10.0.

.. index:: CONFIGURE_DISABLE_CLASSIC_API_NOTEPADS

CONFIGURE_DISABLE_CLASSIC_API_NOTEPADS
--------------------------------------

This configuration option was introduced in RTEMS 4.9.0 and is obsolete since
RTEMS 5.1.

.. index:: CONFIGURE_ENABLE_GO

CONFIGURE_ENABLE_GO
-------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_GNAT_RTEMS

CONFIGURE_GNAT_RTEMS
--------------------

This configuration option was present in all RTEMS versions since at 1997 and is
obsolete since RTEMS 5.1.  See also :ref:`ConfigAda`.

.. index:: CONFIGURE_HAS_OWN_CONFIGURATION_TABLE

CONFIGURE_HAS_OWN_CONFIGURATION_TABLE
-------------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_HAS_OWN_BDBUF_TABLE

CONFIGURE_HAS_OWN_BDBUF_TABLE
-----------------------------

This configuration option was introduced in RTEMS 4.7.0 and is obsolete since
RTEMS 4.10.0.

.. index:: CONFIGURE_HAS_OWN_DEVICE_DRIVER_TABLE

CONFIGURE_HAS_OWN_DEVICE_DRIVER_TABLE
-------------------------------------

This configuration option was present in all RTEMS versions since at least 1995
and is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_HAS_OWN_INIT_TASK_TABLE

.. _CONFIGURE_HAS_OWN_INIT_TASK_TABLE:

CONFIGURE_HAS_OWN_INIT_TASK_TABLE
---------------------------------

This configuration option was present in all RTEMS versions since at least 1995
and is obsolete since RTEMS 5.1.  If you used this configuration option or you
think that there should be a way to configure more than one Classic API
initialization task, then please ask on the :r:list:`users`.

.. index:: CONFIGURE_HAS_OWN_MOUNT_TABLE

CONFIGURE_HAS_OWN_MOUNT_TABLE
-----------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_HAS_OWN_MULTIPROCESSING_TABLE

CONFIGURE_HAS_OWN_MULTIPROCESSING_TABLE
---------------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_LIBIO_MAXIMUM_FILE_DESCRIPTORS

CONFIGURE_LIBIO_MAXIMUM_FILE_DESCRIPTORS
--------------------------------

This configuration option was present in all RTEMS versions since at 1998 and is
obsolete since RTEMS 5.1.  See also :ref:`CONFIGURE_MAXIMUM_FILE_DESCRIPTORS`.

.. index:: CONFIGURE_MAXIMUM_ADA_TASKS

CONFIGURE_MAXIMUM_ADA_TASKS
---------------------------

This configuration option was present in all RTEMS versions since at 1997 and is
obsolete since RTEMS 5.1.  See also :ref:`ConfigAda`.

.. index:: CONFIGURE_MAXIMUM_FAKE_ADA_TASKS

CONFIGURE_MAXIMUM_FAKE_ADA_TASKS
--------------------------------

This configuration option was present in all RTEMS versions since at 1997 and is
obsolete since RTEMS 5.1.  See also :ref:`ConfigAda`.

.. index:: CONFIGURE_MAXIMUM_GO_CHANNELS

CONFIGURE_MAXIMUM_GO_CHANNELS
-----------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_GOROUTINES

CONFIGURE_MAXIMUM_GOROUTINES
----------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_MRSP_SEMAPHORES

CONFIGURE_MAXIMUM_MRSP_SEMAPHORES
---------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_NUMBER_OF_TERMIOS_PORTS

CONFIGURE_NUMBER_OF_TERMIOS_PORTS
---------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_POSIX_BARRIERS

CONFIGURE_MAXIMUM_POSIX_BARRIERS
--------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_POSIX_CONDITION_VARIABLES

CONFIGURE_MAXIMUM_POSIX_CONDITION_VARIABLES
-------------------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUE_DESCRIPTORS

CONFIGURE_MAXIMUM_POSIX_MESSAGE_QUEUE_DESCRIPTORS
-------------------------------

This configuration option was introduced in RTEMS 4.10.0 and is obsolete since
RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_POSIX_MUTEXES

CONFIGURE_MAXIMUM_POSIX_MUTEXES
-------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_POSIX_RWLOCKS

CONFIGURE_MAXIMUM_POSIX_RWLOCKS
-------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_MAXIMUM_POSIX_SPINLOCKS

CONFIGURE_MAXIMUM_POSIX_SPINLOCKS
---------------------------------

This configuration option is obsolete since RTEMS 5.1.

.. index:: CONFIGURE_POSIX_HAS_OWN_INIT_THREAD_TABLE

.. _CONFIGURE_POSIX_HAS_OWN_INIT_THREAD_TABLE:

CONFIGURE_POSIX_HAS_OWN_INIT_THREAD_TABLE
-----------------------------------------

This configuration option was present in all RTEMS versions since at least 1995
and is obsolete since RTEMS 5.1.  If you used this configuration option or you
think that there should be a way to configure more than one POSIX initialization
thread, then please ask on the  :r:list:`users`.

.. index:: CONFIGURE_SMP_APPLICATION

CONFIGURE_SMP_APPLICATION
-------------------------

This configuration option was introduced in RTEMS 4.11.0 and is obsolete since
RTEMS 5.1.

.. index:: CONFIGURE_SMP_MAXIMUM_PROCESSORS

CONFIGURE_SMP_MAXIMUM_PROCESSORS
--------------------------------

This configuration option was introduced in RTEMS 4.11.0 and is obsolete since
RTEMS 5.1.  See also :ref:`CONFIGURE_MAXIMUM_PROCESSORS`.

.. index:: CONFIGURE_TERMIOS_DISABLED

CONFIGURE_TERMIOS_DISABLED
--------------------------

This configuration option is obsolete since RTEMS 5.1.
