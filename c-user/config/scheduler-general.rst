.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2010 Gedare Bloom
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

General Scheduler Configuration
===============================

This section describes configuration options related to selecting a
scheduling algorithm for an application.  A scheduler configuration is optional
and only necessary in very specific circumstances.  A normal application
configuration does not need any of the configuration options described in this
section.

By default, the :ref:`Deterministic Priority Scheduler <SchedulerPriority>`
algorithm is used in uniprocessor configurations.  In case SMP is enabled and
the configured maximum processors
(:ref:`CONFIGURE_MAXIMUM_PROCESSORS <CONFIGURE_MAXIMUM_PROCESSORS>`) is greater
than one, then the :ref:`Earliest Deadline First (EDF) SMP Scheduler
<SchedulerSMPEDF>` is selected as the default scheduler algorithm.

For the :ref:`schedulers built into
RTEMS <SchedulingConcepts>`, the configuration is straightforward.  All that is
required is to define the configuration option which specifies which scheduler
you want for in your application.

The pluggable scheduler interface also enables the user to provide their own
scheduling algorithm.  If you choose to do this, you must define multiple
configuration option.

.. index:: CONFIGURE_SCHEDULER_CBS

.. _CONFIGURE_SCHEDULER_CBS:

CONFIGURE_SCHEDULER_CBS
-----------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_CBS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Constant Bandwidth Server (CBS) Scheduler <SchedulerCBS>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for exactly one processor.

.. index:: CONFIGURE_SCHEDULER_EDF

.. _CONFIGURE_SCHEDULER_EDF:

CONFIGURE_SCHEDULER_EDF
-----------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_EDF``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Earliest Deadline First (EDF) Scheduler <SchedulerEDF>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for exactly one processor.

.. index:: CONFIGURE_SCHEDULER_EDF_SMP

.. _CONFIGURE_SCHEDULER_EDF_SMP:

CONFIGURE_SCHEDULER_EDF_SMP
---------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_EDF_SMP``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Earliest Deadline First (EDF) SMP Scheduler <SchedulerSMPEDF>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    This scheduler algorithm is only available when RTEMS is built with SMP
    support enabled.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for up to 32 processors.

    This scheduler algorithm is the default in SMP configurations if
    :ref:`CONFIGURE_MAXIMUM_PROCESSORS` is
    greater than one.

.. index:: CONFIGURE_SCHEDULER_NAME

.. _CONFIGURE_SCHEDULER_NAME:

CONFIGURE_SCHEDULER_NAME
------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_NAME``

DATA TYPE:
    RTEMS Name (``rtems_name``).

RANGE:
    Any value.

DEFAULT VALUE:
    The default name is

      - ``"MEDF"`` for the :ref:`EDF SMP Scheduler <SchedulerSMPEDF>`,
      - ``"MPA "`` for the :ref:`Arbitrary Processor Affinity Priority SMP Scheduler <SchedulerSMPPriorityAffinity>`,
      - ``"MPD "`` for the :ref:`Deterministic Priority SMP Scheduler <SchedulerSMPPriority>`,
      - ``"MPS "`` for the :ref:`Simple Priority SMP Scheduler <SchedulerSMPPrioritySimple>`,
      - ``"UCBS"`` for the :ref:`Uniprocessor CBS Scheduler <SchedulerCBS>`,
      - ``"UEDF"`` for the :ref:`Uniprocessor EDF Scheduler <SchedulerEDF>`,
      - ``"UPD "`` for the :ref:`Uniprocessor Deterministic Priority Scheduler <SchedulerPriority>`, and
      - ``"UPS "`` for the :ref:`Uniprocessor Simple Priority Scheduler <SchedulerPrioritySimple>`.

DESCRIPTION:
    Schedulers can be identified via ``rtems_scheduler_ident``.  The name of
    the scheduler is determined by the configuration.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

.. index:: CONFIGURE_SCHEDULER_PRIORITY

.. _CONFIGURE_SCHEDULER_PRIORITY:

CONFIGURE_SCHEDULER_PRIORITY
----------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_PRIORITY``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Deterministic Priority Scheduler <SchedulerPriority>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for exactly one processor.

    This scheduler algorithm is the default when
    :ref:`CONFIGURE_MAXIMUM_PROCESSORS` is
    exactly one.

    The memory allocated for this scheduler depends on the
    :ref:`CONFIGURE_MAXIMUM_PRIORITY` configuration option.

.. index:: CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP

.. _CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP:

CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP
-----------------------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_PRIORITY_AFFINITY_SMP``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Arbitrary Processor Affinity SMP Scheduler <SchedulerSMPPriorityAffinity>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    This scheduler algorithm is only available when RTEMS is built with SMP
    support enabled.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for up to 32 processors.

    The memory allocated for this scheduler depends on the
    :ref:`CONFIGURE_MAXIMUM_PRIORITY` configuration option.

.. index:: CONFIGURE_SCHEDULER_PRIORITY_SMP

.. _CONFIGURE_SCHEDULER_PRIORITY_SMP:

CONFIGURE_SCHEDULER_PRIORITY_SMP
--------------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_PRIORITY_SMP``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Deterministic Priority SMP Scheduler <SchedulerSMPPriority>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    This scheduler algorithm is only available when RTEMS is built with SMP
    support enabled.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for up to 32 processors.

    The memory allocated for this scheduler depends on the
    :ref:`CONFIGURE_MAXIMUM_PRIORITY` configuration option.

.. index:: CONFIGURE_SCHEDULER_SIMPLE

.. _CONFIGURE_SCHEDULER_SIMPLE:

CONFIGURE_SCHEDULER_SIMPLE
--------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_SIMPLE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Simple Priority Scheduler <SchedulerPrioritySimple>`
    algorithm is made available to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for exactly one processor.

.. index:: CONFIGURE_SCHEDULER_SIMPLE_SMP

.. _CONFIGURE_SCHEDULER_SIMPLE_SMP:

CONFIGURE_SCHEDULER_SIMPLE_SMP
------------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_SIMPLE_SMP``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then
    :ref:`Simple Priority SMP Scheduler <SchedulerSMPPrioritySimple>`
    algorithm is made available to the application.
    application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    This scheduler algorithm is only available when RTEMS is built with SMP
    support enabled.

    In case no explicit :ref:`clustered scheduler configuration
    <ConfigurationSchedulersClustered>` is present, then it is used as the
    scheduler for up to 32 processors.

.. index:: CONFIGURE_SCHEDULER_USER

.. _CONFIGURE_SCHEDULER_USER:

CONFIGURE_SCHEDULER_USER
------------------------

CONSTANT:
    ``CONFIGURE_SCHEDULER_USER``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the user must provide a
    scheduler algorithm to the application.

NOTES:
    This scheduler configuration option is an advanced configuration option.
    Think twice before you use it.

    RTEMS allows the application to provide its own task/thread scheduling
    algorithm. In order to do this, one must define
    ``CONFIGURE_SCHEDULER_USER`` to indicate the application provides its own
    scheduling algorithm. If ``CONFIGURE_SCHEDULER_USER`` is defined then the
    following additional macros must be defined:

    - ``CONFIGURE_SCHEDULER`` must be defined to a static definition of
      the scheduler data structures of the user scheduler.

    - ``CONFIGURE_SCHEDULER_TABLE_ENTRIES`` must be defined to a scheduler
      table entry initializer for the user scheduler.

    - ``CONFIGURE_SCHEDULER_USER_PER_THREAD`` must be defined to the type of
      the per-thread information of the user scheduler.

    At this time, the mechanics and requirements for writing a new scheduler
    are evolving and not fully documented.  It is recommended that you look at
    the existing Deterministic Priority Scheduler in
    ``cpukit/score/src/schedulerpriority*.c`` for guidance.  For guidance on
    the configuration macros, please examine ``cpukit/sapi/include/confdefs.h``
    for how these are defined for the Deterministic Priority Scheduler.
