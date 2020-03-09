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

Device Driver Configuration
===========================

This section defines the configuration parameters related to the automatic
generation of a Device Driver Table.  As ``<rtems/confdefs.h>`` only is aware
of a small set of standard device drivers, the generated Device Driver Table is
suitable for simple applications with no custom device drivers.

Note that network device drivers are not configured in the Device Driver Table.

.. index:: CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER

.. _CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER:

CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER
------------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`` is defined when the
    application does *NOT* want the Clock Device Driver and is *NOT* using the
    Timer Driver.  The inclusion or exclusion of the Clock Driver must be
    explicit in user applications.

NOTES:
    This configuration parameter is intended to prevent the common user error
    of using the Hello World example as the baseline for an application and
    leaving out a clock tick source.

.. index:: CONFIGURE_APPLICATION_EXTRA_DRIVERS

.. _CONFIGURE_APPLICATION_EXTRA_DRIVERS:

CONFIGURE_APPLICATION_EXTRA_DRIVERS
-----------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_EXTRA_DRIVERS``

DATA TYPE:
    device driver entry structures

RANGE:
    Undefined or set of device driver entry structures

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_EXTRA_DRIVERS`` is defined if the application has
    device drivers it needs to include in the Device Driver Table.  This should
    be defined to the set of device driver entries that will be placed in the
    table at the *END* of the Device Driver Table.

NOTES:
    None.

.. index:: CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER:

CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
----------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER`` is defined if the application
    wishes to include the Clock Device Driver.

NOTES:
    This device driver is responsible for providing a regular interrupt which
    invokes a clock tick directive.

    If neither the Clock Driver not Benchmark Timer is enabled and the
    configuration parameter
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`` is not defined, then a
    compile time error will occur.

.. index:: CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER
------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER`` is defined if the
    application wishes to include the Console Device Driver.

NOTES:
    This device driver is responsible for providing the :file:`/dev/console`
    device file.  This device is used to initialize the standard input, output,
    and error file descriptors.

    BSPs should be constructed in a manner that allows ``printk()`` to work
    properly without the need for the console driver to be configured.

    The

    * ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

    configuration options are mutually exclusive.

.. index:: CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER:

CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER
-----------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_FRAME_BUFFER_DRIVER`` is defined if the
    application wishes to include the BSP's Frame Buffer Device Driver.

NOTES:
    Most BSPs do not include support for a Frame Buffer Device Driver. This is
    because many boards do not include the required hardware.

    If this is defined and the BSP does not have this device driver, then the
    user will get a link time error for an undefined symbol.

.. index:: CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER
.. index:: /dev/null

.. _CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER:

CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER
---------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_NULL_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    This configuration variable is specified to enable ``/dev/null`` device driver.

NOTES:
    This device driver is supported by all BSPs.

.. index:: CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER:

CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER
--------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_RTC_DRIVER`` is defined if the application
    wishes to include the Real-Time Clock Driver.

NOTES:
    Most BSPs do not include support for a real-time clock. This is because
    many boards do not include the required hardware.

    If this is defined and the BSP does not have this device driver, then the
    user will get a link time error for an undefined symbol.

.. index:: CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER
-------------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER`` is defined if the
    application wishes to include the Simple Console Device Driver.

NOTES:
    This device driver is responsible for providing the :file:`/dev/console`
    device file.  This device is used to initialize the standard input, output,
    and error file descriptors.

    This device driver reads via ``getchark()``.

    This device driver writes via ``rtems_putc()``.

    The Termios framework is not used.  There is no support to change device
    settings, e.g. baud, stop bits, parity, etc.

    The

    * ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

    configuration options are mutually exclusive.

.. index:: CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER:

CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER
------------------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER`` is defined if
    the application wishes to include the Simple Task Console Device Driver.

NOTES:
    This device driver is responsible for providing the :file:`/dev/console`
    device file.  This device is used to initialize the standard input, output,
    and error file descriptors.

    This device driver reads via ``getchark()``.

    This device driver writes into a write buffer.  The count of characters
    written into the write buffer is returned.  It might be less than the
    requested count, in case the write buffer is full.  The write is
    non-blocking and may be called from interrupt context.  A dedicated task
    reads from the write buffer and outputs the characters via
    ``rtems_putc()``.  This task runs with the least important priority.  The
    write buffer size is 2047 characters and it is not configurable.

    Use ``fsync(STDOUT_FILENO)`` or ``fdatasync(STDOUT_FILENO)`` to drain the
    write buffer.

    The Termios framework is not used.  There is no support to change device
    settings, e.g.  baud, stop bits, parity, etc.

    The

    * ``CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER``,

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_CONSOLE_DRIVER``, and

    * ``CONFIGURE_APPLICATION_NEEDS_SIMPLE_TASK_CONSOLE_DRIVER``

    configuration options are mutually exclusive.

.. index:: CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER:

CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER
---------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_STUB_DRIVER`` is defined if the application
    wishes to include the Stub Device Driver.

NOTES:
    This device driver simply provides entry points that return successful and
    is primarily a test fixture. It is supported by all BSPs.

.. index:: CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER:

CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER
----------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_TIMER_DRIVER`` is defined if the application
    wishes to include the Timer Driver.  This device driver is used to
    benchmark execution times by the RTEMS Timing Test Suites.

NOTES:
    If neither the Clock Driver not Benchmark Timer is enabled and the
    configuration parameter
    ``CONFIGURE_APPLICATION_DOES_NOT_NEED_CLOCK_DRIVER`` is not defined, then a
    compile time error will occur.

.. index:: CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER

.. _CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER:

CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER
-------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_NEEDS_WATCHDOG_DRIVER`` is defined if the
    application wishes to include the Watchdog Driver.

NOTES:
    Most BSPs do not include support for a watchdog device driver. This is
    because many boards do not include the required hardware.

    If this is defined and the BSP does not have this device driver, then the
    user will get a link time error for an undefined symbol.

.. index:: CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER
.. index:: /dev/zero

.. _CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER:

CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER
---------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_NEEDS_ZERO_DRIVER``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    This configuration variable is specified to enable ``/dev/zero`` device driver.

NOTES:
    This device driver is supported by all BSPs.

.. index:: CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS

.. _CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS:

CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS
------------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS``

DATA TYPE:
    device driver entry structures

RANGE:
    Undefined or set of device driver entry structures

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_APPLICATION_PREREQUISITE_DRIVERS`` is defined if the
    application has device drivers it needs to include in the Device Driver
    Table.  This should be defined to the set of device driver entries that
    will be placed in the table at the *FRONT* of the Device Driver Table and
    initialized before any other drivers *EXCEPT* any BSP prerequisite drivers.

NOTES:
    In some cases, it is used by System On Chip BSPs to support peripheral
    buses beyond those normally found on the System On Chip. For example, this
    is used by one RTEMS system which has implemented a SPARC/ERC32 based board
    with VMEBus. The VMEBus Controller initialization is performed by a device
    driver configured via this configuration parameter.

.. index:: CONFIGURE_MAXIMUM_DRIVERS

.. _CONFIGURE_MAXIMUM_DRIVERS:

CONFIGURE_MAXIMUM_DRIVERS
-------------------------

CONSTANT:
    ``CONFIGURE_MAXIMUM_DRIVERS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Zero or positive.

DEFAULT VALUE:
    This is computed by default, and is set to the number of device drivers
    configured using the ``CONFIGURE_APPLICATIONS_NEEDS_XXX_DRIVER``
    configuration parameters.

DESCRIPTION:
    ``CONFIGURE_MAXIMUM_DRIVERS`` is defined as the number of device drivers
    per node.

NOTES:
    If the application will dynamically install device drivers, then this
    configuration parameter must be larger than the number of statically
    configured device drivers. Drivers configured using the
    ``CONFIGURE_APPLICATIONS_NEEDS_XXX_DRIVER`` configuration parameters are
    statically installed.

Multiprocessing Configuration
=============================

This section defines the multiprocessing related system configuration
parameters supported by ``<rtems/confdefs.h>``.  They are only used if RTEMS
was built with the ``--enable-multiprocessing`` build configuration option.
The multiprocessing (MPCI) support must not be confused with the SMP support.

Additionally, this class of Configuration Constants are only applicable if
``CONFIGURE_MP_APPLICATION`` is defined.

.. index:: CONFIGURE_MP_APPLICATION

.. _CONFIGURE_MP_APPLICATION:

CONFIGURE_MP_APPLICATION
------------------------

CONSTANT:
    ``CONFIGURE_MP_APPLICATION``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    This configuration parameter must be defined to indicate that the
    application intends to be part of a multiprocessing
    configuration. Additional configuration parameters are assumed to be
    provided.

NOTES:
    This has no impact unless RTEMS was built with the
    ``--enable-multiprocessing`` build configuration option.

.. index:: CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS

.. _CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS:

CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS
-----------------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 32.

DESCRIPTION:
    ``CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS`` is the maximum number of
    concurrently active global objects in a multiprocessor system.

NOTES:
    This value corresponds to the total number of objects which can be created
    with the ``RTEMS_GLOBAL`` attribute.

.. index:: CONFIGURE_MP_MAXIMUM_NODES

.. _CONFIGURE_MP_MAXIMUM_NODES:

CONFIGURE_MP_MAXIMUM_NODES
--------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_NODES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 2.

DESCRIPTION:
    ``CONFIGURE_MP_MAXIMUM_NODES`` is the maximum number of nodes in a
    multiprocessor system.

NOTES:
    None.

.. index:: CONFIGURE_MP_MAXIMUM_PROXIES

.. _CONFIGURE_MP_MAXIMUM_PROXIES:

CONFIGURE_MP_MAXIMUM_PROXIES
----------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_PROXIES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    The default value is 32.

DESCRIPTION:
    ``CONFIGURE_MP_MAXIMUM_PROXIES`` is the maximum number of concurrently
    active thread/task proxies on this node in a multiprocessor system.

NOTES:
    Since a proxy is used to represent a remote task/thread which is blocking
    on this node. This configuration parameter reflects the maximum number of
    remote tasks/threads which can be blocked on objects on this node.

.. COMMENT: XXX - add xref to proxy discussion in MP chapter

.. index:: CONFIGURE_MP_MPCI_TABLE_POINTER

.. _CONFIGURE_MP_MPCI_TABLE_POINTER:

CONFIGURE_MP_MPCI_TABLE_POINTER
-------------------------------

CONSTANT:
    ``CONFIGURE_MP_MPCI_TABLE_POINTER``

DATA TYPE:
    pointer to ``rtems_mpci_table``

RANGE:
    undefined or valid pointer

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_MP_MPCI_TABLE_POINTER`` is the pointer to the MPCI
    Configuration Table.  The default value of this field is``&MPCI_table``.

NOTES:
    RTEMS provides a Shared Memory MPCI Device Driver which can be used on any
    Multiprocessor System assuming the BSP provides the proper set of
    supporting methods.

.. index:: CONFIGURE_MP_NODE_NUMBER

.. _CONFIGURE_MP_NODE_NUMBER:

CONFIGURE_MP_NODE_NUMBER
------------------------

CONSTANT:
    ``CONFIGURE_MP_NODE_NUMBER``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is ``NODE_NUMBER``, which is assumed to be set by the
    compilation environment.

DESCRIPTION:
    ``CONFIGURE_MP_NODE_NUMBER`` is the node number of this node in a
    multiprocessor system.

NOTES:
    In the RTEMS Multiprocessing Test Suite, the node number is derived from
    the Makefile variable ``NODE_NUMBER``. The same code is compiled with the
    ``NODE_NUMBER`` set to different values. The test programs behave
    differently based upon their node number.

PCI Library Configuration
=========================

This section defines the system configuration parameters supported by
``rtems/confdefs.h`` related to configuring the PCI Library for RTEMS.

The PCI Library startup behaviour can be configured in four different ways
depending on how ``CONFIGURE_PCI_CONFIG_LIB`` is defined:

.. index:: PCI_LIB_AUTO

``PCI_LIB_AUTO``
  Used to enable the PCI auto configuration software. PCI will be automatically
  probed, PCI buses enumerated, all devices and bridges will be initialized
  using Plug & Play software routines. The PCI device tree will be populated
  based on the PCI devices found in the system, PCI devices will be configured
  by allocating address region resources automatically in PCI space according
  to the BSP or host bridge driver set up.

.. index:: PCI_LIB_READ

``PCI_LIB_READ``
  Used to enable the PCI read configuration software. The current PCI
  configuration is read to create the RAM representation (the PCI device tree)
  of the PCI devices present. PCI devices are assumed to already have been
  initialized and PCI buses enumerated, it is therefore required that a BIOS or
  a boot loader has set up configuration space prior to booting into RTEMS.

.. index:: PCI_LIB_STATIC

``PCI_LIB_STATIC``
  Used to enable the PCI static configuration software. The user provides a PCI
  tree with information how all PCI devices are to be configured at compile
  time by linking in a custom ``struct pci_bus pci_hb`` tree. The static PCI
  library will not probe PCI for devices, instead it will assume that all
  devices defined by the user are present, it will enumerate the PCI buses and
  configure all PCI devices in static configuration accordingly. Since probe
  and allocation software is not needed the startup is faster, has smaller
  footprint and does not require dynamic memory allocation.

.. index:: PCI_LIB_PERIPHERAL

``PCI_LIB_PERIPHERAL``
  Used to enable the PCI peripheral configuration. It is similar to
  ``PCI_LIB_STATIC``, but it will never write the configuration to the PCI
  devices since PCI peripherals are not allowed to access PCI configuration
  space.

Note that selecting ``PCI_LIB_STATIC`` or ``PCI_LIB_PERIPHERAL`` but not
defining ``pci_hb`` will reuslt in link errors. Note also that in these modes
Plug & Play is not performed.

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
