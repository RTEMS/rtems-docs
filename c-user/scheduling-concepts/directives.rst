.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the scheduler manager.  A subsection is dedicated to each
of these services and describes the calling sequence, related constants, usage,
and status codes.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_ident:

SCHEDULER_IDENT - Get ID of a scheduler
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_ident(
            rtems_name  name,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``id`` parameter is ``NULL``.
     * - ``RTEMS_INVALID_NAME``
       - Invalid scheduler name.

DESCRIPTION:
    Identifies a scheduler by its name.  The scheduler name is determined by
    the scheduler configuration.  See :ref:`ConfigurationSchedulerTable`
    and :ref:`CONFIGURE_SCHEDULER_NAME`.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_ident_by_processor:

SCHEDULER_IDENT_BY_PROCESSOR - Get ID of a scheduler by processor
-----------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_ident_by_processor(
            uint32_t  cpu_index,
            rtems_id *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``id`` parameter is ``NULL``.
     * - ``RTEMS_INVALID_NAME``
       - Invalid processor index.
     * - ``RTEMS_INCORRECT_STATE``
       - The processor index is valid, however, this processor is not owned by
         a scheduler.

DESCRIPTION:
    Identifies a scheduler by a processor.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_ident_by_processor_set:

SCHEDULER_IDENT_BY_PROCESSOR_SET - Get ID of a scheduler by processor set
-------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_ident_by_processor_set(
            size_t           cpusetsize,
            const cpu_set_t *cpuset,
            rtems_id        *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``id`` parameter is ``NULL``.
     * - ``RTEMS_INVALID_SIZE``
       - Invalid processor set size.
     * - ``RTEMS_INVALID_NAME``
       - The processor set contains no online processor.
     * - ``RTEMS_INCORRECT_STATE``
       - The processor set is valid, however, the highest numbered online
         processor in the specified processor set is not owned by a scheduler.

DESCRIPTION:
    Identifies a scheduler by a processor set.  The scheduler is selected
    according to the highest numbered online processor in the specified
    processor set.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_get_maximum_priority:

SCHEDULER_GET_MAXIMUM_PRIORITY - Get maximum task priority of a scheduler
-------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_get_maximum_priority(
            rtems_id             scheduler_id,
            rtems_task_priority *priority
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ID``
       - Invalid scheduler instance identifier.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``priority`` parameter is ``NULL``.

DESCRIPTION:
    Returns the maximum task priority of the specified scheduler instance in
    ``priority``.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_map_priority_to_posix:

SCHEDULER_MAP_PRIORITY_TO_POSIX - Map task priority to POSIX thread prority
---------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_map_priority_to_posix(
            rtems_id             scheduler_id,
            rtems_task_priority  priority,
            int                 *posix_priority
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``posix_priority`` parameter is ``NULL``.
     * - ``RTEMS_INVALID_ID``
       - Invalid scheduler instance identifier.
     * - ``RTEMS_INVALID_PRIORITY``
       - Invalid task priority.

DESCRIPTION:
    Maps a task priority to the corresponding POSIX thread priority.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_map_priority_from_posix:

SCHEDULER_MAP_PRIORITY_FROM_POSIX - Map POSIX thread prority to task priority
-----------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_map_priority_from_posix(
            rtems_id             scheduler_id,
            int                  posix_priority,
            rtems_task_priority *priority
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``priority`` parameter is ``NULL``.
     * - ``RTEMS_INVALID_ID``
       - Invalid scheduler instance identifier.
     * - ``RTEMS_INVALID_PRIORITY``
       - Invalid POSIX thread priority.

DESCRIPTION:
    Maps a POSIX thread priority to the corresponding task priority.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_get_processor:

SCHEDULER_GET_PROCESSOR - Get current processor index
-----------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        uint32_t rtems_scheduler_get_processor( void );

DIRECTIVE STATUS CODES:
    This directive returns the index of the current processor.

DESCRIPTION:
    In uniprocessor configurations, a value of zero will be returned.

    In SMP configurations, an architecture specific method is used to obtain the
    index of the current processor in the system.  The set of processor indices
    is the range of integers starting with zero up to the processor count minus
    one.

    Outside of sections with disabled thread dispatching the current processor
    index may change after every instruction since the thread may migrate from
    one processor to another.  Sections with disabled interrupts are sections
    with thread dispatching disabled.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_get_processor_maximum:

SCHEDULER_GET_PROCESSOR_MAXIMUM - Get processor maximum
-------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        uint32_t rtems_scheduler_get_processor_maximum( void );

DIRECTIVE STATUS CODES:
    This directive returns the processor maximum supported by the system.

DESCRIPTION:
    In uniprocessor configurations, a value of one will be returned.

    In SMP configurations, this directive returns the minimum of the processors
    (physically or virtually) available by the platform and the configured
    processor maximum.  Not all processors in the range from processor index
    zero to the last processor index (which is the processor maximum minus one)
    may be configured to be used by a scheduler or online (online processors
    have a scheduler assigned).

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_get_processor_set:

SCHEDULER_GET_PROCESSOR_SET - Get processor set of a scheduler
--------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_get_processor_set(
            rtems_id   scheduler_id,
            size_t     cpusetsize,
            cpu_set_t *cpuset
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ID``
       - Invalid scheduler instance identifier.
     * - ``RTEMS_INVALID_ADDRESS``
       - The ``cpuset`` parameter is ``NULL``.
     * - ``RTEMS_INVALID_NUMBER``
       - The processor set buffer is too small for the set of processors owned
         by the scheduler instance.

DESCRIPTION:
    Returns the processor set owned by the scheduler instance in ``cpuset``.  A
    set bit in the processor set means that this processor is owned by the
    scheduler instance and a cleared bit means the opposite.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_add_processor:

SCHEDULER_ADD_PROCESSOR - Add processor to a scheduler
------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_add_processor(
            rtems_id scheduler_id,
            uint32_t cpu_index
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ID``
       - Invalid scheduler instance identifier.
     * - ``RTEMS_NOT_CONFIGURED``
       - The processor is not configured to be used by the application.
     * - ``RTEMS_INCORRECT_STATE``
       - The processor is configured to be used by the application, however, it
         is not online.
     * - ``RTEMS_RESOURCE_IN_USE``
       - The processor is already assigned to a scheduler instance.

DESCRIPTION:
    Adds a processor to the set of processors owned by the specified scheduler
    instance.

NOTES:
    Must be called from task context.  This operation obtains and releases the
    objects allocator lock.

.. raw:: latex

   \clearpage

.. _rtems_scheduler_remove_processor:

SCHEDULER_REMOVE_PROCESSOR - Remove processor from a scheduler
--------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_scheduler_remove_processor(
            rtems_id scheduler_id,
            uint32_t cpu_index
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - Successful operation.
     * - ``RTEMS_INVALID_ID``
       - Invalid scheduler instance identifier.
     * - ``RTEMS_INVALID_NUMBER``
       - The processor is not owned by the specified scheduler instance.
     * - ``RTEMS_RESOURCE_IN_USE``
       - The set of processors owned by the specified scheduler instance would
         be empty after the processor removal and there exists a non-idle task
         that uses this scheduler instance as its home scheduler instance.
     * - ``RTEMS_RESOURCE_IN_USE``
       - A task with a restricted processor affinity exists that uses this
         scheduler instance as its home scheduler instance and it would be no
         longer possible to allocate a processor for this task after the
         removal of this processor.

DESCRIPTION:
    Removes a processor from set of processors owned by the specified scheduler
    instance.

NOTES:
    Must be called from task context.  This operation obtains and releases the
    objects allocator lock.  Removing a processor from a scheduler is a complex
    operation that involves all tasks of the system.
