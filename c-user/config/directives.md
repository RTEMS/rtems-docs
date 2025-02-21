.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2009, 2021 embedded brains GmbH & Co. KG
.. Copyright (C) 1988, 2021 On-Line Applications Research Corporation (OAR)

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

.. _ApplicationConfigurationInformationDirectives:

Directives
==========

This section details the directives of the Application Configuration
Information. A subsection is dedicated to each of this manager's directives and
lists the calling sequence, parameters, description, return values, and notes
of the directive.

.. Generated from spec:/rtems/config/if/get-build-label

.. raw:: latex

    \clearpage

.. index:: rtems_get_build_label()

.. _InterfaceRtemsGetBuildLabel:

rtems_get_build_label()
-----------------------

Gets the RTEMS build label.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const char *rtems_get_build_label( void );

.. rubric:: DESCRIPTION:

The build label is a user-provided string defined by the build configuration
through the ``RTEMS_BUILD_LABEL`` build option.  The format of the string is
completely user-defined.

.. rubric:: RETURN VALUES:

Returns a pointer to the RTEMS build label.

.. rubric:: NOTES:

The build label can be used to distinguish test suite results obtained from
different build configurations.  A use case is to record test results with
performance data to track performance regressions.  For this a database of
performance limits is required.  The build label and the target hash obtained
from :ref:`InterfaceRtemsGetTargetHash` can be used as a key to obtain
performance limits.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-copyright-notice

.. raw:: latex

    \clearpage

.. index:: rtems_get_copyright_notice()

.. _InterfaceRtemsGetCopyrightNotice:

rtems_get_copyright_notice()
----------------------------

Gets the RTEMS copyright notice.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const char *rtems_get_copyright_notice( void );

.. rubric:: RETURN VALUES:

Returns a pointer to the RTEMS copyright notice.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-target-hash

.. raw:: latex

    \clearpage

.. index:: rtems_get_target_hash()

.. _InterfaceRtemsGetTargetHash:

rtems_get_target_hash()
-----------------------

Gets the RTEMS target hash.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const char *rtems_get_target_hash( void );

.. rubric:: DESCRIPTION:

The target hash is calculated from BSP-specific values which characterize a
target system.  The target hash is encoded as a base64url string.  The target
hash algorithm is unspecified.

.. rubric:: RETURN VALUES:

Returns a pointer to the RTEMS target hash.

.. rubric:: NOTES:

For example, the device tree, settings of the memory controller, processor and
bus frequencies, a serial number of a chip may be used to calculate the target
hash.

The target hash can be used to distinguish test suite results obtained from
different target systems.  See also :ref:`InterfaceRtemsGetBuildLabel`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-version-string

.. raw:: latex

    \clearpage

.. index:: rtems_get_version_string()

.. _InterfaceRtemsGetVersionString:

rtems_get_version_string()
--------------------------

Gets the RTEMS version string.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const char *rtems_get_version_string( void );

.. rubric:: RETURN VALUES:

Returns a pointer to the RTEMS version string.

.. rubric:: NOTES:

The version string has no particular format.  Parsing the string may break
across RTEMS releases.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-do-zero-of-workspace

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_do_zero_of_workspace()

.. _InterfaceRtemsConfigurationGetDoZeroOfWorkspace:

rtems_configuration_get_do_zero_of_workspace()
----------------------------------------------

Indicates if the RTEMS Workspace is configured to be zeroed during system
initialization for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    bool rtems_configuration_get_do_zero_of_workspace( void );

.. rubric:: RETURN VALUES:

Returns true, if the RTEMS Workspace is configured to be zeroed during system
initialization for this application, otherwise false.

.. rubric:: NOTES:

The setting is defined by the :ref:`CONFIGURE_ZERO_WORKSPACE_AUTOMATICALLY`
application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-idle-task-stack-size

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_idle_task_stack_size()

.. _InterfaceRtemsConfigurationGetIdleTaskStackSize:

rtems_configuration_get_idle_task_stack_size()
----------------------------------------------

Gets the IDLE task stack size in bytes of this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_configuration_get_idle_task_stack_size( void );

.. rubric:: RETURN VALUES:

Returns the IDLE task stack size in bytes of this application.

.. rubric:: NOTES:

The IDLE task stack size is defined by the
:ref:`CONFIGURE_IDLE_TASK_STACK_SIZE` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-idle-task

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_idle_task()

.. _InterfaceRtemsConfigurationGetIdleTask:

rtems_configuration_get_idle_task()
-----------------------------------

Gets the IDLE task body of this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void *( * )( uintptr_t ) rtems_configuration_get_idle_task( void );

.. rubric:: RETURN VALUES:

Returns the IDLE task body of this application.

.. rubric:: NOTES:

The IDLE task body is defined by the :ref:`CONFIGURE_IDLE_TASK_BODY`
application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-interrupt-stack-size

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_interrupt_stack_size()

.. _InterfaceRtemsConfigurationGetInterruptStackSize:

rtems_configuration_get_interrupt_stack_size()
----------------------------------------------

Gets the interrupt stack size in bytes of this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_configuration_get_interrupt_stack_size( void );

.. rubric:: RETURN VALUES:

Returns the interrupt stack size in bytes of this application.

.. rubric:: NOTES:

The interrupt stack size is defined by the
:ref:`CONFIGURE_INTERRUPT_STACK_SIZE` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-barriers

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_barriers()

.. _InterfaceRtemsConfigurationGetMaximumBarriers:

rtems_configuration_get_maximum_barriers()
------------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicBarrier` objects configured
for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_barriers( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicBarrier` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_BARRIERS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-extensions

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_extensions()

.. _InterfaceRtemsConfigurationGetMaximumExtensions:

rtems_configuration_get_maximum_extensions()
--------------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicUserExt` objects configured
for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_extensions( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicUserExt` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_USER_EXTENSIONS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-message-queues

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_message_queues()

.. _InterfaceRtemsConfigurationGetMaximumMessageQueues:

rtems_configuration_get_maximum_message_queues()
------------------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicMessage` objects configured
for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_message_queues( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicMessage` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_MESSAGE_QUEUES`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-partitions

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_partitions()

.. _InterfaceRtemsConfigurationGetMaximumPartitions:

rtems_configuration_get_maximum_partitions()
--------------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicPart` objects configured for
this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_partitions( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicPart` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_PARTITIONS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-periods

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_periods()

.. _InterfaceRtemsConfigurationGetMaximumPeriods:

rtems_configuration_get_maximum_periods()
-----------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicRatemon` objects configured
for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_periods( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicRatemon` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_PERIODS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-ports

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_ports()

.. _InterfaceRtemsConfigurationGetMaximumPorts:

rtems_configuration_get_maximum_ports()
---------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicDPMem` objects configured for
this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_ports( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicDPMem` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_PORTS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-processors

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_processors()

.. _InterfaceRtemsConfigurationGetMaximumProcessors:

rtems_configuration_get_maximum_processors()
--------------------------------------------

Gets the maximum number of processors configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_processors( void );

.. rubric:: RETURN VALUES:

Returns the maximum number of processors configured for this application.

.. rubric:: NOTES:

The actual number of processors available to the application is returned by
:ref:`InterfaceRtemsSchedulerGetProcessorMaximum` which less than or equal to
the configured maximum number of processors
(:ref:`CONFIGURE_MAXIMUM_PROCESSORS`).

In uniprocessor configurations, this macro is a compile time constant which
evaluates to one.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-regions

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_regions()

.. _InterfaceRtemsConfigurationGetMaximumRegions:

rtems_configuration_get_maximum_regions()
-----------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicRegion` objects configured for
this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_regions( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicRegion` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_REGIONS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-semaphores

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_semaphores()

.. _InterfaceRtemsConfigurationGetMaximumSemaphores:

rtems_configuration_get_maximum_semaphores()
--------------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicSem` objects configured for
this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_semaphores( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicSem` objects configured for
this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_SEMAPHORES`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-tasks

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_tasks()

.. _InterfaceRtemsConfigurationGetMaximumTasks:

rtems_configuration_get_maximum_tasks()
---------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicTasks` objects configured for
this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_tasks( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicTasks` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_TASKS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-maximum-timers

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_maximum_timers()

.. _InterfaceRtemsConfigurationGetMaximumTimers:

rtems_configuration_get_maximum_timers()
----------------------------------------

Gets the resource number of :ref:`RTEMSAPIClassicTimer` objects configured for
this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_maximum_timers( void );

.. rubric:: RETURN VALUES:

Returns the resource number of :ref:`RTEMSAPIClassicTimer` objects configured
for this application.

.. rubric:: NOTES:

The resource number is defined by the :ref:`CONFIGURE_MAXIMUM_TIMERS`
application configuration option.  See also
:ref:`InterfaceRtemsResourceIsUnlimited` and
:ref:`InterfaceRtemsResourceMaximumPerAllocation`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-microseconds-per-tick

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_microseconds_per_tick()

.. _InterfaceRtemsConfigurationGetMicrosecondsPerTick:

rtems_configuration_get_microseconds_per_tick()
-----------------------------------------------

Gets the number of microseconds per clock tick configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_microseconds_per_tick( void );

.. rubric:: RETURN VALUES:

Returns the number of microseconds per clock tick configured for this
application.

.. rubric:: NOTES:

The number of microseconds per :term:`clock tick` is defined by the
:ref:`CONFIGURE_MICROSECONDS_PER_TICK` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-milliseconds-per-tick

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_milliseconds_per_tick()

.. _InterfaceRtemsConfigurationGetMillisecondsPerTick:

rtems_configuration_get_milliseconds_per_tick()
-----------------------------------------------

Gets the number of milliseconds per clock tick configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_milliseconds_per_tick( void );

.. rubric:: RETURN VALUES:

Returns the number of milliseconds per clock tick configured for this
application.

.. rubric:: NOTES:

The number of milliseconds per :term:`clock tick` is defined by the
:ref:`CONFIGURE_MICROSECONDS_PER_TICK` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-nanoseconds-per-tick

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_nanoseconds_per_tick()

.. _InterfaceRtemsConfigurationGetNanosecondsPerTick:

rtems_configuration_get_nanoseconds_per_tick()
----------------------------------------------

Gets the number of microseconds per clock tick configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_nanoseconds_per_tick( void );

.. rubric:: RETURN VALUES:

Returns the number of microseconds per clock tick configured for this
application.

.. rubric:: NOTES:

The number of nanoseconds per :term:`clock tick` is defined by the
:ref:`CONFIGURE_MICROSECONDS_PER_TICK` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-number-of-initial-extensions

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_number_of_initial_extensions()

.. _InterfaceRtemsConfigurationGetNumberOfInitialExtensions:

rtems_configuration_get_number_of_initial_extensions()
------------------------------------------------------

Gets the number of initial extensions configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_number_of_initial_extensions( void );

.. rubric:: RETURN VALUES:

Returns the number of initial extensions configured for this application.

.. rubric:: NOTES:

The number of initial extensions is defined by the
:ref:`CONFIGURE_INITIAL_EXTENSIONS` application configuration option and
related options.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-stack-allocate-for-idle-hook

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_stack_allocate_for_idle_hook()

.. _InterfaceRtemsConfigurationGetStackAllocateForIdleHook:

rtems_configuration_get_stack_allocate_for_idle_hook()
------------------------------------------------------

Gets the task stack allocator allocate hook used to allocate the stack of each
:term:`IDLE task` configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void *( * )( uint32_t, size_t * )
    rtems_configuration_get_stack_allocate_for_idle_hook( void );

.. rubric:: RETURN VALUES:

Returns the task stack allocator allocate hook used to allocate the stack of
each :term:`IDLE task` configured for this application.

.. rubric:: NOTES:

The task stack allocator allocate hook for idle tasks is defined by the
:ref:`CONFIGURE_TASK_STACK_ALLOCATOR_FOR_IDLE` application configuration
option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-stack-allocate-hook

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_stack_allocate_hook()

.. _InterfaceRtemsConfigurationGetStackAllocateHook:

rtems_configuration_get_stack_allocate_hook()
---------------------------------------------

Gets the task stack allocator allocate hook configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void *( * )( size_t ) rtems_configuration_get_stack_allocate_hook( void );

.. rubric:: RETURN VALUES:

Returns the task stack allocator allocate hook configured for this application.

.. rubric:: NOTES:

The task stack allocator allocate hook is defined by the
:ref:`CONFIGURE_TASK_STACK_ALLOCATOR` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-stack-allocate-init-hook

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_stack_allocate_init_hook()

.. _InterfaceRtemsConfigurationGetStackAllocateInitHook:

rtems_configuration_get_stack_allocate_init_hook()
--------------------------------------------------

Gets the task stack allocator initialization hook configured for this
application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void ( * )( size_t ) rtems_configuration_get_stack_allocate_init_hook( void );

.. rubric:: RETURN VALUES:

Returns the task stack allocator initialization hook configured for this
application.

.. rubric:: NOTES:

The task stack allocator initialization hook is defined by the
:ref:`CONFIGURE_TASK_STACK_ALLOCATOR_INIT` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-stack-allocator-avoids-work-space

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_stack_allocator_avoids_work_space()

.. _InterfaceRtemsConfigurationGetStackAllocatorAvoidsWorkSpace:

rtems_configuration_get_stack_allocator_avoids_work_space()
-----------------------------------------------------------

Indicates if the task stack allocator is configured to avoid the RTEMS
Workspace for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    bool rtems_configuration_get_stack_allocator_avoids_work_space( void );

.. rubric:: RETURN VALUES:

Returns true, if the task stack allocator is configured to avoid the RTEMS
Workspace for this application, otherwise false.

.. rubric:: NOTES:

The setting is defined by the
:ref:`CONFIGURE_TASK_STACK_ALLOCATOR_AVOIDS_WORK_SPACE` application
configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-stack-free-hook

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_stack_free_hook()

.. _InterfaceRtemsConfigurationGetStackFreeHook:

rtems_configuration_get_stack_free_hook()
-----------------------------------------

Gets the task stack allocator free hook configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void ( * )( void * ) rtems_configuration_get_stack_free_hook( void );

.. rubric:: RETURN VALUES:

Returns the task stack allocator free hook configured for this application.

.. rubric:: NOTES:

The task stack allocator free hook is defined by the
:ref:`CONFIGURE_TASK_STACK_DEALLOCATOR` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-stack-space-size

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_stack_space_size()

.. _InterfaceRtemsConfigurationGetStackSpaceSize:

rtems_configuration_get_stack_space_size()
------------------------------------------

Gets the configured size in bytes of the memory space used to allocate thread
stacks for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uintptr_t rtems_configuration_get_stack_space_size( void );

.. rubric:: RETURN VALUES:

Returns the configured size in bytes of the memory space used to allocate
thread stacks for this application.

.. rubric:: NOTES:

The size takes only threads and tasks into account with are known at the
application configuration time.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-ticks-per-timeslice

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_ticks_per_timeslice()

.. _InterfaceRtemsConfigurationGetTicksPerTimeslice:

rtems_configuration_get_ticks_per_timeslice()
---------------------------------------------

Gets the clock ticks per timeslice configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_configuration_get_ticks_per_timeslice( void );

.. rubric:: RETURN VALUES:

Returns the clock ticks per timeslice configured for this application.

.. rubric:: NOTES:

The :term:`clock ticks <clock tick>` per timeslice is defined by the
:ref:`CONFIGURE_TICKS_PER_TIMESLICE` application configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-unified-work-area

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_unified_work_area()

.. _InterfaceRtemsConfigurationGetUnifiedWorkArea:

rtems_configuration_get_unified_work_area()
-------------------------------------------

Indicates if the RTEMS Workspace and C Program Heap are configured to be
unified for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    bool rtems_configuration_get_unified_work_area( void );

.. rubric:: RETURN VALUES:

Returns true, if the RTEMS Workspace and C Program Heap are configured to be
unified for this application, otherwise false.

.. rubric:: NOTES:

The setting is defined by the :ref:`CONFIGURE_UNIFIED_WORK_AREAS` application
configuration option.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-user-extension-table

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_user_extension_table()

.. _InterfaceRtemsConfigurationGetUserExtensionTable:

rtems_configuration_get_user_extension_table()
----------------------------------------------

Gets the initial extensions table configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const rtems_extensions_table *rtems_configuration_get_user_extension_table(
      void
    );

.. rubric:: RETURN VALUES:

Returns a pointer to the initial extensions table configured for this
application.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-user-multiprocessing-table

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_user_multiprocessing_table()

.. _InterfaceRtemsConfigurationGetUserMultiprocessingTable:

rtems_configuration_get_user_multiprocessing_table()
----------------------------------------------------

Gets the MPCI configuration table configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const MPCI_Configuration *rtems_configuration_get_user_multiprocessing_table(
      void
    );

.. rubric:: RETURN VALUES:

Returns a pointer to the MPCI configuration table configured for this
application.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-work-space-size

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_work_space_size()

.. _InterfaceRtemsConfigurationGetWorkSpaceSize:

rtems_configuration_get_work_space_size()
-----------------------------------------

Gets the RTEMS Workspace size in bytes configured for this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uintptr_t rtems_configuration_get_work_space_size( void );

.. rubric:: RETURN VALUES:

Returns the RTEMS Workspace size in bytes configured for this application.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/get-api-configuration

.. raw:: latex

    \clearpage

.. index:: rtems_configuration_get_rtems_api_configuration()

.. _InterfaceRtemsConfigurationGetRtemsApiConfiguration:

rtems_configuration_get_rtems_api_configuration()
-------------------------------------------------

Gets the Classic API Configuration Table of this application.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    const rtems_api_configuration_table *
    rtems_configuration_get_rtems_api_configuration( void );

.. rubric:: RETURN VALUES:

Returns a pointer to the Classic API Configuration Table of this application.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/resource-is-unlimited

.. raw:: latex

    \clearpage

.. index:: rtems_resource_is_unlimited()

.. _InterfaceRtemsResourceIsUnlimited:

rtems_resource_is_unlimited()
-----------------------------

Indicates if the resource is unlimited.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    bool rtems_resource_is_unlimited( uint32_t resource );

.. rubric:: PARAMETERS:

``resource``
    This parameter is the resource number.

.. rubric:: RETURN VALUES:

Returns true, if the resource is unlimited, otherwise false.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive is implemented by a macro and may be called from within C/C++
  constant expressions.  In addition, a function implementation of the
  directive exists for bindings to other programming languages.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/resource-maximum-per-allocation

.. raw:: latex

    \clearpage

.. index:: rtems_resource_maximum_per_allocation()

.. _InterfaceRtemsResourceMaximumPerAllocation:

rtems_resource_maximum_per_allocation()
---------------------------------------

Gets the maximum number per allocation of a resource number.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_resource_maximum_per_allocation( uint32_t resource );

.. rubric:: PARAMETERS:

``resource``
    This parameter is the resource number.

.. rubric:: RETURN VALUES:

Returns the maximum number per allocation of a resource number.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive is implemented by a macro and may be called from within C/C++
  constant expressions.  In addition, a function implementation of the
  directive exists for bindings to other programming languages.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/config/if/resource-unlimited

.. raw:: latex

    \clearpage

.. index:: rtems_resource_unlimited()

.. _InterfaceRtemsResourceUnlimited:

rtems_resource_unlimited()
--------------------------

Augments the resource number so that it indicates an unlimited resource.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    uint32_t rtems_resource_unlimited( uint32_t resource );

.. rubric:: PARAMETERS:

``resource``
    This parameter is the resource number to augment.

.. rubric:: RETURN VALUES:

Returns the resource number augmented to indicate an unlimited resource.

.. rubric:: NOTES:

This directive should be used to configure unlimited objects, see
:ref:`ConfigUnlimitedObjects`.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive is implemented by a macro and may be called from within C/C++
  constant expressions.  In addition, a function implementation of the
  directive exists for bindings to other programming languages.

* The directive will not cause the calling task to be preempted.
