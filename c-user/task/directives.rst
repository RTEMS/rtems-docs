.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the task manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create a task
.. index:: rtems_task_create

.. _rtems_task_create:

TASK_CREATE - Create a task
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_create(
            rtems_name           name,
            rtems_task_priority  initial_priority,
            size_t               stack_size,
            rtems_mode           initial_modes,
            rtems_attribute      attribute_set,
            rtems_id            *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task created successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``id`` is NULL
      * - ``RTEMS_INVALID_NAME``
        - invalid task name
      * - ``RTEMS_INVALID_PRIORITY``
        - invalid task priority
      * - ``RTEMS_TOO_MANY``
        - too many tasks created
      * - ``RTEMS_UNSATISFIED``
        - not enough memory for stack/FP context
      * - ``RTEMS_UNSATISFIED``
        - non-preemption mode not supported on SMP system
      * - ``RTEMS_UNSATISFIED``
        - interrupt level mode not supported on SMP system
      * - ``RTEMS_TOO_MANY``
        - too many global objects

DESCRIPTION:
    This directive creates a task which resides on the local node.  It
    allocates and initializes a TCB, a stack, and an optional floating point
    context area.  The mode parameter contains values which sets the task's
    initial execution mode.  The ``RTEMS_FLOATING_POINT`` attribute should be
    specified if the created task is to use a numeric coprocessor.  For
    performance reasons, it is recommended that tasks not using the numeric
    coprocessor should specify the ``RTEMS_NO_FLOATING_POINT`` attribute.  If
    the ``RTEMS_GLOBAL`` attribute is specified, the task can be accessed from
    remote nodes.  The task id, returned in id, is used in other task related
    directives to access the task.  When created, a task is placed in the
    dormant state and can only be made ready to execute using the directive
    ``rtems_task_start``.

NOTES:
    This directive may cause the calling task to be preempted.

    The scheduler of the new task is the scheduler of the executing task at
    some point during the task creation.  The specified task priority must be
    valid for the selected scheduler.

    The task processor affinity is initialized to the set of online processors.

    If the requested stack size is less than the configured minimum stack size,
    then RTEMS will use the configured minimum as the stack size for this task.
    In addition to being able to specify the task stack size as a integer,
    there are two constants which may be specified:

    ``RTEMS_MINIMUM_STACK_SIZE``
      The minimum stack size *RECOMMENDED* for use on this processor.  This
      value is selected by the RTEMS developers conservatively to minimize the
      risk of blown stacks for most user applications.  Using this constant
      when specifying the task stack size, indicates that the stack size will
      be at least ``RTEMS_MINIMUM_STACK_SIZE`` bytes in size.  If the user
      configured minimum stack size is larger than the recommended minimum,
      then it will be used.

    ``RTEMS_CONFIGURED_MINIMUM_STACK_SIZE``
      Indicates this task is to be created with a stack size of the minimum
      stack size that was configured by the application.  If not explicitly
      configured by the application, the default configured minimum stack size
      is the processor dependent value ``RTEMS_MINIMUM_STACK_SIZE``.  Since
      this uses the configured minimum stack size value, you may get a stack
      size that is smaller or larger than the recommended minimum.  This can be
      used to provide large stacks for all tasks on complex applications or
      small stacks on applications that are trying to conserve memory.

    Application developers should consider the stack usage of the device
    drivers when calculating the stack size required for tasks which utilize
    the driver.

    The following task attribute constants are defined by RTEMS:

    .. list-table::
      :class: rtems-table

      * - ``RTEMS_NO_FLOATING_POINT``
        - does not use coprocessor (default)
      * - ``RTEMS_FLOATING_POINT``
        - uses numeric coprocessor
      * - ``RTEMS_LOCAL``
        - local task (default)
      * - ``RTEMS_GLOBAL``
        - global task

    The following task mode constants are defined by RTEMS:

    .. list-table::
      :class: rtems-table

      * - ``RTEMS_PREEMPT``
        - enable preemption (default)
      * - ``RTEMS_NO_PREEMPT``
        - disable preemption
      * - ``RTEMS_NO_TIMESLICE``
        - disable timeslicing (default)
      * - ``RTEMS_TIMESLICE``
        - enable timeslicing
      * - ``RTEMS_ASR``
        - enable ASR processing (default)
      * - ``RTEMS_NO_ASR``
        - disable ASR processing
      * - ``RTEMS_INTERRUPT_LEVEL(0)``
        - enable all interrupts (default)
      * - ``RTEMS_INTERRUPT_LEVEL(n)``
        - execute at interrupt level ``n``

    The interrupt level portion of the task execution mode supports a maximum
    of 256 interrupt levels.  These levels are mapped onto the interrupt
    levels actually supported by the target processor in a processor dependent
    fashion.

    Tasks should not be made global unless remote tasks must interact with
    them.  This avoids the system overhead incurred by the creation of a
    global task.  When a global task is created, the task's name and id must
    be transmitted to every node in the system for insertion in the local copy
    of the global object table.

    The total number of global objects, including tasks, is limited by the
    maximum_global_objects field in the Configuration Table.

.. raw:: latex

   \clearpage

.. index:: get ID of a task
.. index:: rtems_task_ident

.. _rtems_task_ident:

TASK_IDENT - Get ID of a task
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_ident(
            rtems_name  name,
            uint32_t    node,
            rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task identified successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``id`` is NULL
      * - ``RTEMS_INVALID_NAME``
        - invalid task name
      * - ``RTEMS_INVALID_NODE``
        - invalid node id

DESCRIPTION:
    This directive obtains the task id associated with the task name specified
    in name.  A task may obtain its own id by specifying ``RTEMS_SELF`` or its
    own task name in name.  If the task name is not unique, then the task id
    returned will match one of the tasks with that name.  However, this task id
    is not guaranteed to correspond to the desired task.  The task id, returned
    in id, is used in other task related directives to access the task.

NOTES:
    This directive will not cause the running task to be preempted.

    If node is ``RTEMS_SEARCH_ALL_NODES``, all nodes are searched with the
    local node being searched first.  All other nodes are searched with the
    lowest numbered node searched first.

    If node is a valid node number which does not represent the local node,
    then only the tasks exported by the designated node are searched.

    This directive does not generate activity on remote nodes.  It accesses
    only the local copy of the global object table.

.. raw:: latex

   \clearpage

.. index:: obtain ID of caller
.. index:: rtems_task_self

.. _rtems_task_self:

TASK_SELF - Obtain ID of caller
-------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_id rtems_task_self(void);

DIRECTIVE STATUS CODES:
    Returns the object Id of the calling task.

DESCRIPTION:
    This directive returns the Id of the calling task.

NOTES:
    If called from an interrupt service routine, this directive will return the
    Id of the interrupted task.

.. raw:: latex

   \clearpage

.. index:: starting a task
.. index:: rtems_task_start

.. _rtems_task_start:

TASK_START - Start a task
-------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_start(
            rtems_id            id,
            rtems_task_entry    entry_point,
            rtems_task_argument argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - ask started successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - invalid task entry point
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_INCORRECT_STATE``
        - task not in the dormant state
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - cannot start remote task

DESCRIPTION:
    This directive readies the task, specified by ``id``, for execution based
    on the priority and execution mode specified when the task was created.
    The starting address of the task is given in ``entry_point``.  The task's
    starting argument is contained in argument.  This argument can be a single
    value or used as an index into an array of parameter blocks.  The type of
    this numeric argument is an unsigned integer type with the property that
    any valid pointer to void can be converted to this type and then converted
    back to a pointer to void.  The result will compare equal to the original
    pointer.

NOTES:
    The calling task will be preempted if its preemption mode is enabled and
    the task being started has a higher priority.

    Any actions performed on a dormant task such as suspension or change of
    priority are nullified when the task is initiated via the
    ``rtems_task_start`` directive.

.. raw:: latex

   \clearpage

.. index:: restarting a task
.. index:: rtems_task_restart

.. _rtems_task_restart:

TASK_RESTART - Restart a task
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_restart(
           rtems_id            id,
           rtems_task_argument argument
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task restarted successfully
      * - ``RTEMS_INVALID_ID``
        - task id invalid
      * - ``RTEMS_INCORRECT_STATE``
        - task never started
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - cannot restart remote task

DESCRIPTION:
    This directive resets the task specified by id to begin execution at its
    original starting address.  The task's priority and execution mode are set
    to the original creation values.  If the task is currently blocked, RTEMS
    automatically makes the task ready.  A task can be restarted from any
    state, except the dormant state.

    The task's starting argument is contained in argument.  This argument can
    be a single value or an index into an array of parameter blocks.  The type
    of this numeric argument is an unsigned integer type with the property that
    any valid pointer to void can be converted to this type and then converted
    back to a pointer to void.  The result will compare equal to the original
    pointer.  This new argument may be used to distinguish between the initial
    ``rtems_task_start`` of the task and any ensuing calls to
    ``rtems_task_restart`` of the task.  This can be beneficial in deleting a
    task.  Instead of deleting a task using the ``rtems_task_delete``
    directive, a task can delete another task by restarting that task, and
    allowing that task to release resources back to RTEMS and then delete
    itself.

NOTES:
    If id is ``RTEMS_SELF``, the calling task will be restarted and will not
    return from this directive.

    The calling task will be preempted if its preemption mode is enabled and
    the task being restarted has a higher priority.

    The task must reside on the local node, even if the task was created with
    the ``RTEMS_GLOBAL`` option.

.. raw:: latex

   \clearpage

.. index:: deleting a task
.. index:: rtems_task_delete

.. _rtems_task_delete:

TASK_DELETE - Delete a task
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task deleted successfully
      * - ``RTEMS_INVALID_ID``
        - task id invalid
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - cannot restart remote task

DESCRIPTION:
    This directive deletes a task, either the calling task or another task, as
    specified by id.  RTEMS stops the execution of the task and reclaims the
    stack memory, any allocated delay or timeout timers, the TCB, and, if the
    task is ``RTEMS_FLOATING_POINT``, its floating point context area.  RTEMS
    does not reclaim the following resources: region segments, partition
    buffers, semaphores, timers, or rate monotonic periods.

NOTES:
    A task is responsible for releasing its resources back to RTEMS before
    deletion.  To insure proper deallocation of resources, a task should not be
    deleted unless it is unable to execute or does not hold any RTEMS
    resources.  If a task holds RTEMS resources, the task should be allowed to
    deallocate its resources before deletion.  A task can be directed to
    release its resources and delete itself by restarting it with a special
    argument or by sending it a message, an event, or a signal.

    Deletion of the current task (``RTEMS_SELF``) will force RTEMS to select
    another task to execute.

    When a global task is deleted, the task id must be transmitted to every
    node in the system for deletion from the local copy of the global object
    table.

    The task must reside on the local node, even if the task was created with
    the ``RTEMS_GLOBAL`` option.

.. raw:: latex

   \clearpage

.. index:: deleting a task
.. index:: rtems_task_exit

.. _rtems_task_exit:

TASK_EXIT - Delete the calling task
-----------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_task_exit( void ) RTEMS_NO_RETURN;

DIRECTIVE STATUS CODES:
    NONE - This function will not return to the caller.

DESCRIPTION:
    This directive deletes the calling task.

NOTES:
    This directive must be called from a regular task context with enabled
    interrupts, otherwise one of the fatal errors

    * :ref:`INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL <internal_errors>`, or
    * :ref:`INTERNAL_ERROR_BAD_THREAD_DISPATCH_ENVIRONMENT <internal_errors>`

    will occur.

    The ``rtems_task_exit()`` call is equivalent to the following code
    sequence:

    .. code-block:: c

        pthread_detach(pthread_self());
        pthread_exit(NULL);

    See also :ref:`rtems_task_delete() <rtems_task_delete>`.

.. raw:: latex

   \clearpage

.. index:: suspending a task
.. index:: rtems_task_suspend

.. _rtems_task_suspend:

TASK_SUSPEND - Suspend a task
-----------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_suspend(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task suspended successfully
      * - ``RTEMS_INVALID_ID``
        - task id invalid
      * - ``RTEMS_ALREADY_SUSPENDED``
        - task already suspended

DESCRIPTION:
    This directive suspends the task specified by id from further execution by
    placing it in the suspended state.  This state is additive to any other
    blocked state that the task may already be in.  The task will not execute
    again until another task issues the ``rtems_task_resume`` directive for
    this task and any blocked state has been removed.

NOTES:
    The requesting task can suspend itself by specifying ``RTEMS_SELF`` as id.
    In this case, the task will be suspended and a successful return code will
    be returned when the task is resumed.

    Suspending a global task which does not reside on the local node will
    generate a request to the remote node to suspend the specified task.

    If the task specified by id is already suspended, then the
    ``RTEMS_ALREADY_SUSPENDED`` status code is returned.

.. raw:: latex

   \clearpage

.. index:: resuming a task
.. index:: rtems_task_resume

.. _rtems_task_resume:

TASK_RESUME - Resume a task
---------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_resume(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task resumed successfully
      * - ``RTEMS_INVALID_ID``
        - task id invalid
      * - ``RTEMS_INCORRECT_STATE``
        - task not suspended

DESCRIPTION:
    This directive removes the task specified by id from the suspended state.
    If the task is in the ready state after the suspension is removed, then it
    will be scheduled to run.  If the task is still in a blocked state after
    the suspension is removed, then it will remain in that blocked state.

NOTES:
    The running task may be preempted if its preemption mode is enabled and the
    local task being resumed has a higher priority.

    Resuming a global task which does not reside on the local node will
    generate a request to the remote node to resume the specified task.

    If the task specified by id is not suspended, then the
    ``RTEMS_INCORRECT_STATE`` status code is returned.

.. raw:: latex

   \clearpage

.. index:: is task suspended
.. index:: rtems_task_is_suspended

.. _rtems_task_is_suspended:

TASK_IS_SUSPENDED - Determine if a task is Suspended
----------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_is_suspended(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task is NOT suspended
      * - ``RTEMS_ALREADY_SUSPENDED``
        - task is currently suspended
      * - ``RTEMS_INVALID_ID``
        - task id invalid
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive returns a status code indicating whether or not the
    specified task is currently suspended.

NOTES:
    This operation is not currently supported on remote tasks.

.. raw:: latex

   \clearpage

.. index:: rtems_task_set_priority
.. index:: current task priority
.. index:: set task priority
.. index:: get task priority
.. index:: obtain task priority

.. _rtems_task_set_priority:

TASK_SET_PRIORITY - Set task priority
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_set_priority(
            rtems_id             id,
            rtems_task_priority  new_priority,
            rtems_task_priority *old_priority
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task priority set successfully
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_INVALID_ADDRESS``
        - invalid return argument pointer
      * - ``RTEMS_INVALID_PRIORITY``
        - invalid task priority

DESCRIPTION:
    This directive manipulates the priority of the task specified by id.  An id
    of ``RTEMS_SELF`` is used to indicate the calling task.  When new_priority
    is not equal to ``RTEMS_CURRENT_PRIORITY``, the specified task's previous
    priority is returned in old_priority.  When new_priority is
    ``RTEMS_CURRENT_PRIORITY``, the specified task's current priority is
    returned in old_priority.  Valid priorities range from a high of 1 to a low
    of 255.

NOTES:
    The calling task may be preempted if its preemption mode is enabled and it
    lowers its own priority or raises another task's priority.

    In case the new priority equals the current priority of the task, then
    nothing happens.

    Setting the priority of a global task which does not reside on the local
    node will generate a request to the remote node to change the priority of
    the specified task.

    If the task specified by id is currently holding any binary semaphores
    which use the priority inheritance algorithm, then the task's priority
    cannot be lowered immediately.  If the task's priority were lowered
    immediately, then priority inversion results.  The requested lowering of
    the task's priority will occur when the task has released all priority
    inheritance binary semaphores.  The task's priority can be increased
    regardless of the task's use of priority inheritance binary semaphores.

.. raw:: latex

   \clearpage

.. index:: rtems_task_get_priority
.. index:: current task priority
.. index:: get task priority
.. index:: obtain task priority

.. _rtems_task_get_priority:

TASK_GET_PRIORITY - Get task priority
-------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_get_priority(
            rtems_id             task_id,
            rtems_id             scheduler_id,
            rtems_task_priority *priority
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - Successful operation.
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - Directive is illegal on remote tasks.
      * - ``RTEMS_INVALID_ADDRESS``
        - The priority parameter is NULL.
      * - ``RTEMS_INVALID_ID``
        - Invalid task or scheduler identifier.
      * - ``RTEMS_NOT_DEFINED``
        - The task has no priority within the specified scheduler instance.
          This error is only possible in SMP configurations.

DESCRIPTION:
    This directive returns the current priority of the task specified by
    :c:data:`task_id` with respect to the scheduler instance specified by
    :c:data:`scheduler_id`.  A task id of :c:macro:`RTEMS_SELF` is used to
    indicate the calling task.

NOTES:
    The current priority reflects temporary priority adjustments due to locking
    protocols, the rate-monotonic period objects on some schedulers and other
    mechanisms.

.. raw:: latex

   \clearpage

.. index:: current task mode
.. index:: set task mode
.. index:: get task mode
.. index:: set task preemption mode
.. index:: get task preemption mode
.. index:: obtain task mode
.. index:: rtems_task_mode

.. _rtems_task_mode:

TASK_MODE - Change the current task mode
----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_mode(
            rtems_mode  mode_set,
            rtems_mode  mask,
            rtems_mode *previous_mode_set
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - task mode set successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``previous_mode_set`` is NULL
        - not enough memory for stack/FP context
      * - ``RTEMS_NOT_IMPLEMENTED``
        - non-preemption mode not supported on SMP system
      * - ``RTEMS_NOT_IMPLEMENTED``

DESCRIPTION:
    This directive manipulates the execution mode of the calling task.  A
    task's execution mode enables and disables preemption, timeslicing,
    asynchronous signal processing, as well as specifying the current interrupt
    level.  To modify an execution mode, the mode class(es) to be changed must
    be specified in the mask parameter and the desired mode(s) must be
    specified in the mode parameter.

NOTES:
    The calling task will be preempted if it enables preemption and a higher
    priority task is ready to run.

    Enabling timeslicing has no effect if preemption is disabled.  For a task
    to be timesliced, that task must have both preemption and timeslicing
    enabled.

    A task can obtain its current execution mode, without modifying it, by
    calling this directive with a mask value of ``RTEMS_CURRENT_MODE``.

    To temporarily disable the processing of a valid ASR, a task should call
    this directive with the ``RTEMS_NO_ASR`` indicator specified in mode.

    The set of task mode constants and each mode's corresponding mask constant
    is provided in the following table:

    .. list-table::
      :class: rtems-table

      * - ``RTEMS_PREEMPT``
        - is masked by ``RTEMS_PREEMPT_MASK`` and enables preemption
      * - ``RTEMS_NO_PREEMPT``
        - is masked by ``RTEMS_PREEMPT_MASK`` and disables preemption
      * - ``RTEMS_NO_TIMESLICE``
        - is masked by ``RTEMS_TIMESLICE_MASK`` and disables timeslicing
      * - ``RTEMS_TIMESLICE``
        - is masked by ``RTEMS_TIMESLICE_MASK`` and enables timeslicing
      * - ``RTEMS_ASR``
        - is masked by ``RTEMS_ASR_MASK`` and enables ASR processing
      * - ``RTEMS_NO_ASR``
        - is masked by ``RTEMS_ASR_MASK`` and disables ASR processing
      * - ``RTEMS_INTERRUPT_LEVEL(0)``
        - is masked by ``RTEMS_INTERRUPT_MASK`` and enables all interrupts
      * - ``RTEMS_INTERRUPT_LEVEL(n)``
        - is masked by ``RTEMS_INTERRUPT_MASK`` and sets interrupts level n

.. raw:: latex

   \clearpage

.. index:: delay a task for an interval
.. index:: wake up after an interval
.. index:: rtems_task_wake_after

.. _rtems_task_wake_after:

TASK_WAKE_AFTER - Wake up after interval
----------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_wake_after(
            rtems_interval ticks
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - always successful

DESCRIPTION:
    This directive blocks the calling task for the specified number of system
    clock ticks.  When the requested interval has elapsed, the task is made
    ready.  The clock tick directives automatically updates the delay period.

NOTES:
    Setting the system date and time with the ``rtems_clock_set`` directive has
    no effect on a ``rtems_task_wake_after`` blocked task.

    A task may give up the processor and remain in the ready state by
    specifying a value of ``RTEMS_YIELD_PROCESSOR`` in ticks.

    The maximum timer interval that can be specified is the maximum value which
    can be represented by the uint32_t type.

    A clock tick is required to support the functionality of this directive.

.. raw:: latex

   \clearpage

.. index:: delay a task until a wall time
.. index:: wake up at a wall time
.. index:: rtems_task_wake_when

.. _rtems_task_wake_when:

TASK_WAKE_WHEN - Wake up when specified
---------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_wake_when(
            rtems_time_of_day *time_buffer
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - awakened at date/time successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``time_buffer`` is NULL
      * - ``RTEMS_INVALID_TIME_OF_DAY``
        - invalid time buffer
      * - ``RTEMS_NOT_DEFINED``
        - system date and time is not set

DESCRIPTION:
    This directive blocks a task until the date and time specified in
    time_buffer.  At the requested date and time, the calling task will be
    unblocked and made ready to execute.

NOTES:
    The ticks portion of time_buffer structure is ignored.  The timing
    granularity of this directive is a second.

    A clock tick is required to support the functionality of this directive.

.. raw:: latex

   \clearpage

.. _rtems_task_get_scheduler:

TASK_GET_SCHEDULER - Get scheduler of a task
--------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_get_scheduler(
            rtems_id  task_id,
            rtems_id *scheduler_id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successful operation
     * - ``RTEMS_INVALID_ADDRESS``
       - ``scheduler_id`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid task id

DESCRIPTION:
    Returns the scheduler identifier of a task identified by ``task_id`` in
    ``scheduler_id``.

NOTES:
    None.

.. raw:: latex

   \clearpage

.. _rtems_task_set_scheduler:
.. _TASK_SET_SCHEDULER - Set scheduler of a task:

TASK_SET_SCHEDULER - Set scheduler of a task
--------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_set_scheduler(
          rtems_id            task_id,
          rtems_id            scheduler_id,
          rtems_task_priority priority
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successful operation
     * - ``RTEMS_INVALID_ID``
       - invalid task or scheduler id
     * - ``RTEMS_INVALID_PRIORITY``
       - invalid task priority
     * - ``RTEMS_RESOURCE_IN_USE``
       - the task is in the wrong state to perform a scheduler change
     * - ``RTEMS_UNSATISFIED``
       - the processor set of the scheduler is empty
     * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
       - not supported on remote tasks

DESCRIPTION:
    Sets the scheduler of a task identified by ``task_id`` to the scheduler
    identified by ``scheduler_id``.  The scheduler of a task is initialized to
    the scheduler of the task that created it.  The priority of the task is set
    to ``priority``.

NOTES:
    It is recommended to set the scheduler of a task before it is started or in
    case it is guaranteed that the task owns no resources.  Otherwise, sporadic
    ``RTEMS_RESOURCE_IN_USE`` errors may occur.

EXAMPLE:
    .. code-block:: c
        :linenos:

        #include <rtems.h>
        #include <assert.h>

        rtems_task task( rtems_task_argument arg );

        void example( void )
        {
          rtems_status_code sc;
          rtems_id          task_id;
          rtems_id          scheduler_id;
          rtems_name        scheduler_name;

          scheduler_name = rtems_build_name( 'W', 'O', 'R', 'K' );

          sc = rtems_scheduler_ident( scheduler_name, &scheduler_id );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_task_create(
            rtems_build_name( 'T', 'A', 'S', 'K' ),
            1,
            RTEMS_MINIMUM_STACK_SIZE,
            RTEMS_DEFAULT_MODES,
            RTEMS_DEFAULT_ATTRIBUTES,
            &task_id
          );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_task_set_scheduler( task_id, scheduler_id, 2 );
          assert( sc == RTEMS_SUCCESSFUL );

          sc = rtems_task_start( task_id, task, 0 );
          assert( sc == RTEMS_SUCCESSFUL );
        }

.. raw:: latex

   \clearpage

.. _rtems_task_get_affinity:

TASK_GET_AFFINITY - Get task processor affinity
-----------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_get_affinity(
            rtems_id   id,
            size_t     cpusetsize,
            cpu_set_t *cpuset
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successful operation
     * - ``RTEMS_INVALID_ADDRESS``
       - ``cpuset`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid task id
     * - ``RTEMS_INVALID_NUMBER``
       - the affinity set buffer is too small for the current processor affinity
         set of the task

DESCRIPTION:
    Returns the current processor affinity set of the task in ``cpuset``.  A
    set bit in the affinity set means that the task can execute on this
    processor and a cleared bit means the opposite.

NOTES:
    The task processor affinity is initialized to the set of online processors.

.. raw:: latex

   \clearpage

.. _rtems_task_set_affinity:

TASK_SET_AFFINITY - Set task processor affinity
-----------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_set_affinity(
            rtems_id         id,
            size_t           cpusetsize,
            const cpu_set_t *cpuset
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - successful operation
     * - ``RTEMS_INVALID_ADDRESS``
       - ``cpuset`` is NULL
     * - ``RTEMS_INVALID_ID``
       - invalid task id
     * - ``RTEMS_INVALID_NUMBER``
       - invalid processor affinity set

DESCRIPTION:
    Sets the processor affinity set for the task specified by ``cpuset``.  A
    set bit in the affinity set means that the task can execute on this
    processor and a cleared bit means the opposite.

NOTES:
    This function will not change the scheduler of the task.  The intersection
    of the processor affinity set and the set of processors owned by the
    scheduler of the task must be non-empty.  It is not an error if the
    processor affinity set contains processors that are not part of the set of
    processors owned by the scheduler instance of the task.  A task will simply
    not run under normal circumstances on these processors since the scheduler
    ignores them.  Some locking protocols may temporarily use processors that
    are not included in the processor affinity set of the task.  It is also not
    an error if the processor affinity set contains processors that are not
    part of the system.

    In case a scheduler without support for task affinites is used for the
    task, then the task processor affinity set must contain all online
    processors of the system.  This prevents odd corner cases if processors are
    added/removed at run-time to/from scheduler instances.

.. raw:: latex

   \clearpage

.. index:: iterate over all threads
.. index:: rtems_task_iterate

.. _rtems_task_iterate:

TASK_ITERATE - Iterate Over Tasks
---------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        typedef bool ( *rtems_task_visitor )( rtems_tcb *tcb, void *arg );

        void rtems_task_iterate(
            rtems_task_visitor  visitor,
            void               *arg
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    Iterates over all tasks in the system.  This operation covers all tasks of
    all APIs.  The user should be careful in accessing the contents of the
    thread control block :c:data:`tcb`.  The visitor argument :c:data:`arg` is
    passed to all invocations of :c:data:`visitor` in addition to the thread
    control block.  The iteration stops immediately in case the visitor
    function returns true.

NOTES:
    Must be called from task context.  This operation obtains and releases the
    objects allocator lock.  The task visitor is called while owning the objects
    allocator lock.  It is possible to perform blocking operations in the task
    visitor, however, take care that no deadlocks via the object allocator lock
    can occur.

Deprecated Directives
=====================

.. raw:: latex

   \clearpage

.. index:: rtems_iterate_over_all_threads

.. _rtems_iterate_over_all_threads:

ITERATE_OVER_ALL_THREADS - Iterate Over Tasks
---------------------------------------------

.. warning::

    This directive is deprecated.  Its use is unsafe.  Use
    :ref:`rtems_task_iterate` instead.

CALLING SEQUENCE:
    .. code-block:: c

        typedef void (*rtems_per_thread_routine)(Thread_Control *the_thread);
        void rtems_iterate_over_all_threads(
            rtems_per_thread_routine routine
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive iterates over all of the existant threads in the system and
    invokes ``routine`` on each of them.  The user should be careful in
    accessing the contents of ``the_thread``.

    This routine is intended for use in diagnostic utilities and is not
    intented for routine use in an operational system.

NOTES:
    There is **no protection** while this routine is called.  The thread
    control block may be in an inconsistent state or may change due to
    interrupts or activity on other processors.

Removed Directives
==================

.. raw:: latex

   \clearpage

.. index:: get task notepad entry
.. index:: rtems_task_get_note

.. _rtems_task_get_note:

TASK_GET_NOTE - Get task notepad entry
--------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_get_note(
          rtems_id  id,
          uint32_t  notepad,
          uint32_t *note
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - note value obtained successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``note`` parameter is NULL
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_INVALID_NUMBER``
        - invalid notepad location

DESCRIPTION:
    This directive returns the note contained in the notepad location of the
    task specified by id.

NOTES:
    This directive will not cause the running task to be preempted.

    If id is set to ``RTEMS_SELF``, the calling task accesses its own notepad.

    The sixteen notepad locations can be accessed using the constants
    ``RTEMS_NOTEPAD_0`` through ``RTEMS_NOTEPAD_15``.

    Getting a note of a global task which does not reside on the local node
    will generate a request to the remote node to obtain the notepad entry of
    the specified task.

.. raw:: latex

   \clearpage

.. index:: set task notepad entry
.. index:: rtems_task_set_note

.. _rtems_task_set_note:

TASK_SET_NOTE - Set task notepad entry
--------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_set_note(
          rtems_id  id,
          uint32_t  notepad,
          uint32_t  note
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - note set successfully
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_INVALID_NUMBER``
        - invalid notepad location

DESCRIPTION:
    This directive sets the notepad entry for the task specified by id to the
    value note.

NOTES:
    If ``id`` is set to ``RTEMS_SELF``, the calling task accesses its own
    notepad.

    This directive will not cause the running task to be preempted.

    The sixteen notepad locations can be accessed using the constants
    ``RTEMS_NOTEPAD_0`` through ``RTEMS_NOTEPAD_15``.

    Setting a note of a global task which does not reside on the local node
    will generate a request to the remote node to set the notepad entry of the
    specified task.

.. raw:: latex

   \clearpage

.. index:: per-task variable
.. index:: task private variable
.. index:: task private data
.. index:: rtems_task_variable_add

.. _rtems_task_variable_add:

TASK_VARIABLE_ADD - Associate per task variable
-----------------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_variable_add(
            rtems_id  tid,
            void    **task_variable,
            void    (*dtor)(void *)
        );

DIRECTIVE STATUS CODES:
     .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - per task variable added successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is NULL
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_NO_MEMORY``
        - invalid task id
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive adds the memory location specified by the ptr argument to
    the context of the given task.  The variable will then be private to the
    task.  The task can access and modify the variable, but the modifications
    will not appear to other tasks, and other tasks' modifications to that
    variable will not affect the value seen by the task.  This is accomplished
    by saving and restoring the variable's value each time a task switch occurs
    to or from the calling task.  If the dtor argument is non-NULL it specifies
    the address of a 'destructor' function which will be called when the task
    is deleted.  The argument passed to the destructor function is the task's
    value of the variable.

NOTES:
    Task variables increase the context switch time to and from the tasks that
    own them so it is desirable to minimize the number of task variables.  One
    efficient method is to have a single task variable that is a pointer to a
    dynamically allocated structure containing the task's private 'global'
    data.  In this case the destructor function could be 'free'.

    Per-task variables are disabled in SMP configurations and this service is
    not available.

.. raw:: latex

   \clearpage

.. index:: get per-task variable
.. index:: obtain per-task variable
.. index:: rtems_task_variable_get

.. _rtems_task_variable_get:

TASK_VARIABLE_GET - Obtain value of a per task variable
-------------------------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_variable_get(
            rtems_id  tid,
            void    **task_variable,
            void    **task_variable_value
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - per task variable obtained successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is NULL
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable_value`` is NULL
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is not found
      * - ``RTEMS_NO_MEMORY``
        - invalid task id
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive looks up the private value of a task variable for a
    specified task and stores that value in the location pointed to by the
    result argument.  The specified task is usually not the calling task, which
    can get its private value by directly accessing the variable.

NOTES:
    If you change memory which ``task_variable_value`` points to, remember to
    declare that memory as volatile, so that the compiler will optimize it
    correctly.  In this case both the pointer ``task_variable_value`` and data
    referenced by ``task_variable_value`` should be considered volatile.

    Per-task variables are disabled in SMP configurations and this service is
    not available.

.. raw:: latex

   \clearpage

.. index:: per-task variable
.. index:: task private variable
.. index:: task private data
.. index:: rtems_task_variable_delete

.. _rtems_task_variable_delete:

TASK_VARIABLE_DELETE - Remove per task variable
-----------------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_variable_delete(
            rtems_id  id,
            void    **task_variable
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - per task variable deleted successfully
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_NO_MEMORY``
        - invalid task id
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is NULL
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive removes the given location from a task's context.

NOTES:
    Per-task variables are disabled in SMP configurations and this service is
    not available.
