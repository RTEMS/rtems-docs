.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Task Manager
************

.. index:: tasks

Introduction
============

The task manager provides a comprehensive set of directives to create, delete,
and administer tasks.  The directives provided by the task manager are:

- rtems_task_create_ - Create a task

- rtems_task_ident_ - Get ID of a task

- rtems_task_self_ - Obtain ID of caller

- rtems_task_start_ - Start a task

- rtems_task_restart_ - Restart a task

- rtems_task_delete_ - Delete a task

- rtems_task_suspend_ - Suspend a task

- rtems_task_resume_ - Resume a task

- rtems_task_is_suspended_ - Determine if a task is suspended

- rtems_task_set_priority_ - Set task priority

- rtems_task_get_priority_ - Get task priority

- rtems_task_mode_ - Change current task's mode

- rtems_task_wake_after_ - Wake up after interval

- rtems_task_wake_when_ - Wake up when specified

- rtems_task_get_scheduler_ - Get scheduler of a task

- rtems_task_set_scheduler_ - Set scheduler of a task

- rtems_task_get_affinity_ - Get task processor affinity

- rtems_task_set_affinity_ - Set task processor affinity

- rtems_task_iterate_ - Iterate Over Tasks

Background
==========

Task Definition
---------------
.. index:: task, definition

Many definitions of a task have been proposed in computer literature.
Unfortunately, none of these definitions encompasses all facets of the concept
in a manner which is operating system independent.  Several of the more common
definitions are provided to enable each user to select a definition which best
matches their own experience and understanding of the task concept:

- a "dispatchable" unit.

- an entity to which the processor is allocated.

- an atomic unit of a real-time, multiprocessor system.

- single threads of execution which concurrently compete for resources.

- a sequence of closely related computations which can execute concurrently
  with other computational sequences.

From RTEMS' perspective, a task is the smallest thread of execution which can
compete on its own for system resources.  A task is manifested by the existence
of a task control block (TCB).

Task Control Block
------------------

The Task Control Block (TCB) is an RTEMS defined data structure which contains
all the information that is pertinent to the execution of a task.  During
system initialization, RTEMS reserves a TCB for each task configured.  A TCB is
allocated upon creation of the task and is returned to the TCB free list upon
deletion of the task.

The TCB's elements are modified as a result of system calls made by the
application in response to external and internal stimuli.  TCBs are the only
RTEMS internal data structure that can be accessed by an application via user
extension routines.  The TCB contains a task's name, ID, current priority,
current and starting states, execution mode, TCB user extension pointer,
scheduling control structures, as well as data required by a blocked task.

A task's context is stored in the TCB when a task switch occurs.  When the task
regains control of the processor, its context is restored from the TCB.  When a
task is restarted, the initial state of the task is restored from the starting
context area in the task's TCB.

Task Name
---------
.. index:: task name

By default, the task name is defined by the task object name given to
:ref:`rtems_task_create() <rtems_task_create>`.  The task name can be obtained
with the `pthread_getname_np()
<http://man7.org/linux/man-pages/man3/pthread_setname_np.3.html>`_ function.
Optionally, a new task name may be set with the `pthread_setname_np()
<http://man7.org/linux/man-pages/man3/pthread_setname_np.3.html>`_ function.
The maximum size of a task name is defined by the application configuration
option :ref:`CONFIGURE_MAXIMUM_THREAD_NAME_SIZE
<CONFIGURE_MAXIMUM_THREAD_NAME_SIZE>`.

Task States
-----------
.. index:: task states

A task may exist in one of the following five states:

- *executing* - Currently scheduled to the CPU

- *ready* - May be scheduled to the CPU

- *blocked* - Unable to be scheduled to the CPU

- *dormant* - Created task that is not started

- *non-existent* - Uncreated or deleted task

An active task may occupy the executing, ready, blocked or dormant state,
otherwise the task is considered non-existent.  One or more tasks may be active
in the system simultaneously.  Multiple tasks communicate, synchronize, and
compete for system resources with each other via system calls.  The multiple
tasks appear to execute in parallel, but actually each is dispatched to the CPU
for periods of time determined by the RTEMS scheduling algorithm.  The
scheduling of a task is based on its current state and priority.

Task Priority
-------------
.. index:: task priority
.. index:: priority, task
.. index:: rtems_task_priority

A task's priority determines its importance in relation to the other tasks
executing on the same processor.  RTEMS supports 255 levels of priority ranging
from 1 to 255.  The data type ``rtems_task_priority`` is used to store task
priorities.

Tasks of numerically smaller priority values are more important tasks than
tasks of numerically larger priority values.  For example, a task at priority
level 5 is of higher privilege than a task at priority level 10.  There is no
limit to the number of tasks assigned to the same priority.

Each task has a priority associated with it at all times.  The initial value of
this priority is assigned at task creation time.  The priority of a task may be
changed at any subsequent time.

Priorities are used by the scheduler to determine which ready task will be
allowed to execute.  In general, the higher the logical priority of a task, the
more likely it is to receive processor execution time.

Task Mode
---------
.. index:: task mode
.. index:: rtems_task_mode

A task's execution mode is a combination of the following four components:

- preemption

- ASR processing

- timeslicing

- interrupt level

It is used to modify RTEMS' scheduling process and to alter the execution
environment of the task.  The data type ``rtems_task_mode`` is used to manage
the task execution mode.

.. index:: preemption

The preemption component allows a task to determine when control of the
processor is relinquished.  If preemption is disabled (``RTEMS_NO_PREEMPT``),
the task will retain control of the processor as long as it is in the executing
state - even if a higher priority task is made ready.  If preemption is enabled
(``RTEMS_PREEMPT``) and a higher priority task is made ready, then the
processor will be taken away from the current task immediately and given to the
higher priority task.

.. index:: timeslicing

The timeslicing component is used by the RTEMS scheduler to determine how the
processor is allocated to tasks of equal priority.  If timeslicing is enabled
(``RTEMS_TIMESLICE``), then RTEMS will limit the amount of time the task can
execute before the processor is allocated to another ready task of equal
priority. The length of the timeslice is application dependent and specified in
the Configuration Table.  If timeslicing is disabled (``RTEMS_NO_TIMESLICE``),
then the task will be allowed to execute until a task of higher priority is
made ready.  If ``RTEMS_NO_PREEMPT`` is selected, then the timeslicing component
is ignored by the scheduler.

The asynchronous signal processing component is used to determine when received
signals are to be processed by the task.  If signal processing is enabled
(``RTEMS_ASR``), then signals sent to the task will be processed the next time
the task executes.  If signal processing is disabled (``RTEMS_NO_ASR``), then
all signals received by the task will remain posted until signal processing is
enabled.  This component affects only tasks which have established a routine to
process asynchronous signals.

.. index:: interrupt level, task

The interrupt level component is used to determine which interrupts will be
enabled when the task is executing. ``RTEMS_INTERRUPT_LEVEL(n)`` specifies that
the task will execute at interrupt level n.

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
   - execute at interrupt level n

The set of default modes may be selected by specifying the
``RTEMS_DEFAULT_MODES`` constant.

Accessing Task Arguments
------------------------
.. index:: task arguments
.. index:: task prototype

All RTEMS tasks are invoked with a single argument which is specified when they
are started or restarted.  The argument is commonly used to communicate startup
information to the task.  The simplest manner in which to define a task which
accesses it argument is:

.. index:: rtems_task

.. code-block:: c

    rtems_task user_task(
        rtems_task_argument argument
    );

Application tasks requiring more information may view this single argument as
an index into an array of parameter blocks.

Floating Point Considerations
-----------------------------
.. index:: floating point

Creating a task with the ``RTEMS_FLOATING_POINT`` attribute flag results in
additional memory being allocated for the TCB to store the state of the numeric
coprocessor during task switches.  This additional memory is *NOT* allocated for
``RTEMS_NO_FLOATING_POINT`` tasks. Saving and restoring the context of a
``RTEMS_FLOATING_POINT`` task takes longer than that of a
``RTEMS_NO_FLOATING_POINT`` task because of the relatively large amount of time
required for the numeric coprocessor to save or restore its computational
state.

Since RTEMS was designed specifically for embedded military applications which
are floating point intensive, the executive is optimized to avoid unnecessarily
saving and restoring the state of the numeric coprocessor.  The state of the
numeric coprocessor is only saved when a ``RTEMS_FLOATING_POINT`` task is
dispatched and that task was not the last task to utilize the coprocessor.  In
a system with only one ``RTEMS_FLOATING_POINT`` task, the state of the numeric
coprocessor will never be saved or restored.

Although the overhead imposed by ``RTEMS_FLOATING_POINT`` tasks is minimal,
some applications may wish to completely avoid the overhead associated with
``RTEMS_FLOATING_POINT`` tasks and still utilize a numeric coprocessor.  By
preventing a task from being preempted while performing a sequence of floating
point operations, a ``RTEMS_NO_FLOATING_POINT`` task can utilize the numeric
coprocessor without incurring the overhead of a ``RTEMS_FLOATING_POINT``
context switch.  This approach also avoids the allocation of a floating point
context area.  However, if this approach is taken by the application designer,
NO tasks should be created as ``RTEMS_FLOATING_POINT`` tasks.  Otherwise, the
floating point context will not be correctly maintained because RTEMS assumes
that the state of the numeric coprocessor will not be altered by
``RTEMS_NO_FLOATING_POINT`` tasks.

If the supported processor type does not have hardware floating capabilities or
a standard numeric coprocessor, RTEMS will not provide built-in support for
hardware floating point on that processor.  In this case, all tasks are
considered ``RTEMS_NO_FLOATING_POINT`` whether created as
``RTEMS_FLOATING_POINT`` or ``RTEMS_NO_FLOATING_POINT`` tasks.  A floating
point emulation software library must be utilized for floating point
operations.

On some processors, it is possible to disable the floating point unit
dynamically.  If this capability is supported by the target processor, then
RTEMS will utilize this capability to enable the floating point unit only for
tasks which are created with the ``RTEMS_FLOATING_POINT`` attribute.  The
consequence of a ``RTEMS_NO_FLOATING_POINT`` task attempting to access the
floating point unit is CPU dependent but will generally result in an exception
condition.

Building a Task Attribute Set
-----------------------------
.. index:: task attributes, building

In general, an attribute set is built by a bitwise OR of the desired
components.  The set of valid task attribute components is listed below:

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

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list.  A component listed as a default is
not required to appear in the component list, although it is a good programming
practice to specify default components.  If all defaults are desired, then
``RTEMS_DEFAULT_ATTRIBUTES`` should be used.

This example demonstrates the attribute_set parameter needed to create a local
task which utilizes the numeric coprocessor.  The attribute_set parameter could
be ``RTEMS_FLOATING_POINT`` or ``RTEMS_LOCAL | RTEMS_FLOATING_POINT``.  The
attribute_set parameter can be set to ``RTEMS_FLOATING_POINT`` because
``RTEMS_LOCAL`` is the default for all created tasks.  If the task were global
and used the numeric coprocessor, then the attribute_set parameter would be
``RTEMS_GLOBAL | RTEMS_FLOATING_POINT``.

Building a Mode and Mask
------------------------
.. index:: task mode, building

In general, a mode and its corresponding mask is built by a bitwise OR of the
desired components.  The set of valid mode constants and each mode's
corresponding mask constant is listed below:

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

Mode values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each mode appears
exactly once in the component list.  A mode component listed as a default is
not required to appear in the mode component list, although it is a good
programming practice to specify default components.  If all defaults are
desired, the mode ``RTEMS_DEFAULT_MODES`` and the mask ``RTEMS_ALL_MODE_MASKS``
should be used.

The following example demonstrates the mode and mask parameters used with the
``rtems_task_mode`` directive to place a task at interrupt level 3 and make it
non-preemptible.  The mode should be set to ``RTEMS_INTERRUPT_LEVEL(3) |
RTEMS_NO_PREEMPT`` to indicate the desired preemption mode and interrupt level,
while the mask parameter should be set to ``RTEMS_INTERRUPT_MASK |
RTEMS_NO_PREEMPT_MASK`` to indicate that the calling task's interrupt level and
preemption mode are being altered.

Operations
==========

Creating Tasks
--------------

The ``rtems_task_create`` directive creates a task by allocating a task control
block, assigning the task a user-specified name, allocating it a stack and
floating point context area, setting a user-specified initial priority, setting
a user-specified initial mode, and assigning it a task ID.  Newly created tasks
are initially placed in the dormant state.  All RTEMS tasks execute in the most
privileged mode of the processor.

Obtaining Task IDs
------------------

When a task is created, RTEMS generates a unique task ID and assigns it to the
created task until it is deleted.  The task ID may be obtained by either of two
methods.  First, as the result of an invocation of the ``rtems_task_create``
directive, the task ID is stored in a user provided location.  Second, the task
ID may be obtained later using the ``rtems_task_ident`` directive.  The task ID
is used by other directives to manipulate this task.

Starting and Restarting Tasks
-----------------------------

The ``rtems_task_start`` directive is used to place a dormant task in the ready
state.  This enables the task to compete, based on its current priority, for
the processor and other system resources.  Any actions, such as suspension or
change of priority, performed on a task prior to starting it are nullified when
the task is started.

With the ``rtems_task_start`` directive the user specifies the task's starting
address and argument.  The argument is used to communicate some startup
information to the task.  As part of this directive, RTEMS initializes the
task's stack based upon the task's initial execution mode and start address.
The starting argument is passed to the task in accordance with the target
processor's calling convention.

The ``rtems_task_restart`` directive restarts a task at its initial starting
address with its original priority and execution mode, but with a possibly
different argument.  The new argument may be used to distinguish between the
original invocation of the task and subsequent invocations.  The task's stack
and control block are modified to reflect their original creation values.
Although references to resources that have been requested are cleared,
resources allocated by the task are NOT automatically returned to RTEMS.  A
task cannot be restarted unless it has previously been started (i.e. dormant
tasks cannot be restarted).  All restarted tasks are placed in the ready state.

Suspending and Resuming Tasks
-----------------------------

The ``rtems_task_suspend`` directive is used to place either the caller or
another task into a suspended state.  The task remains suspended until a
``rtems_task_resume`` directive is issued.  This implies that a task may be
suspended as well as blocked waiting either to acquire a resource or for the
expiration of a timer.

The ``rtems_task_resume`` directive is used to remove another task from the
suspended state. If the task is not also blocked, resuming it will place it in
the ready state, allowing it to once again compete for the processor and
resources.  If the task was blocked as well as suspended, this directive clears
the suspension and leaves the task in the blocked state.

Suspending a task which is already suspended or resuming a task which is not
suspended is considered an error.  The ``rtems_task_is_suspended`` can be used
to determine if a task is currently suspended.

Delaying the Currently Executing Task
-------------------------------------

The ``rtems_task_wake_after`` directive creates a sleep timer which allows a
task to go to sleep for a specified interval.  The task is blocked until the
delay interval has elapsed, at which time the task is unblocked.  A task
calling the ``rtems_task_wake_after`` directive with a delay interval of
``RTEMS_YIELD_PROCESSOR`` ticks will yield the processor to any other ready
task of equal or greater priority and remain ready to execute.

The ``rtems_task_wake_when`` directive creates a sleep timer which allows a
task to go to sleep until a specified date and time.  The calling task is
blocked until the specified date and time has occurred, at which time the task
is unblocked.

Changing Task Priority
----------------------

The ``rtems_task_set_priority`` directive is used to obtain or change the
current priority of either the calling task or another task.  If the new
priority requested is ``RTEMS_CURRENT_PRIORITY`` or the task's actual priority,
then the current priority will be returned and the task's priority will remain
unchanged.  If the task's priority is altered, then the task will be scheduled
according to its new priority.

The ``rtems_task_restart`` directive resets the priority of a task to its
original value.

Changing Task Mode
------------------

The ``rtems_task_mode`` directive is used to obtain or change the current
execution mode of the calling task.  A task's execution mode is used to enable
preemption, timeslicing, ASR processing, and to set the task's interrupt level.

The ``rtems_task_restart`` directive resets the mode of a task to its original
value.

Task Deletion
-------------

RTEMS provides the ``rtems_task_delete`` directive to allow a task to delete
itself or any other task.  This directive removes all RTEMS references to the
task, frees the task's control block, removes it from resource wait queues, and
deallocates its stack as well as the optional floating point context.  The
task's name and ID become inactive at this time, and any subsequent references
to either of them is invalid.  In fact, RTEMS may reuse the task ID for another
task which is created later in the application.

Unexpired delay timers (i.e. those used by ``rtems_task_wake_after`` and
``rtems_task_wake_when``) and timeout timers associated with the task are
automatically deleted, however, other resources dynamically allocated by the
task are NOT automatically returned to RTEMS.  Therefore, before a task is
deleted, all of its dynamically allocated resources should be deallocated by
the user.  This may be accomplished by instructing the task to delete itself
rather than directly deleting the task.  Other tasks may instruct a task to
delete itself by sending a "delete self" message, event, or signal, or by
restarting the task with special arguments which instruct the task to delete
itself.

Setting Affinity to a Single Processor
--------------------------------------

On some embedded applications targeting SMP systems, it may be beneficial to
lock individual tasks to specific processors.  In this way, one can designate a
processor for I/O tasks, another for computation, etc..  The following
illustrates the code sequence necessary to assign a task an affinity for
processor with index ``processor_index``.

.. code-block:: c

    #include <rtems.h>
    #include <assert.h>

    void pin_to_processor(rtems_id task_id, int processor_index)
    {
        rtems_status_code sc;
        cpu_set_t         cpuset;
        CPU_ZERO(&cpuset);
        CPU_SET(processor_index, &cpuset);
        sc = rtems_task_set_affinity(task_id, sizeof(cpuset), &cpuset);
        assert(sc == RTEMS_SUCCESSFUL);
    }

It is important to note that the ``cpuset`` is not validated until the
``rtems_task_set_affinity`` call is made. At that point, it is validated
against the current system configuration.

Transition Advice for Obsolete Notepads
---------------------------------------

.. index:: rtems_task_get_note
.. index:: rtems_task_set_note

Task notepads and the associated directives :ref:`rtems_task_get_note` and
:ref:`rtems_task_set_note` were removed in RTEMS 4.12. These were never
thread-safe to access and subject to conflicting use of the notepad index by
libraries which were designed independently.

It is recommended that applications be modified to use services which are
thread safe and not subject to issues with multiple applications conflicting
over the key (e.g. notepad index) selection. For most applications, POSIX Keys
should be used. These are available in all RTEMS build configurations. It is
also possible that thread-local storage (TLS) is an option for some use cases.

Transition Advice for Obsolete Task Variables
---------------------------------------------

.. index:: rtems_task_variable_add
.. index:: rtems_task_variable_get
.. index:: rtems_task_variable_delete

Task notepads and the associated directives :ref:`rtems_task_variable_add`,
:ref:`rtems_task_variable_get` and :ref:`rtems_task_variable_delete` were
removed in RTEMS 4.12.  Task variables must be replaced by POSIX Keys or
thread-local storage (TLS).  POSIX Keys are available in all configurations and
support value destructors.  For the TLS support consult the :title:`RTEMS CPU
Architecture Supplement`.

Directives
==========

This section details the task manager's directives.  A subsection is dedicated
to each of this manager's directives and describes the calling sequence,
related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_task_create:

TASK_CREATE - Create a task
---------------------------
.. index:: create a task
.. index:: rtems_task_create

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
      * - ``RTEMS_MP_NOT_CONFIGURED``
        - multiprocessing not configured
      * - ``RTEMS_TOO_MANY``
        - too many tasks created
      * - ``RTEMS_UNSATISFIED``
        - not enough memory for stack/FP context
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
    This directive will not cause the calling task to be preempted.

    Valid task priorities range from a high of 1 to a low of 255.

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

.. _rtems_task_ident:

TASK_IDENT - Get ID of a task
-----------------------------
.. index:: get ID of a task
.. index:: rtems_task_ident

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

.. _rtems_task_self:

TASK_SELF - Obtain ID of caller
-------------------------------
.. index:: obtain ID of caller
.. index:: rtems_task_self

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

.. _rtems_task_start:

TASK_START - Start a task
-------------------------
.. index:: starting a task
.. index:: rtems_task_start

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

.. _rtems_task_restart:

TASK_RESTART - Restart a task
-----------------------------
.. index:: restarting a task
.. index:: rtems_task_restart

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

.. _rtems_task_delete:

TASK_DELETE - Delete a task
---------------------------
.. index:: deleting a task
.. index:: rtems_task_delete

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

.. _rtems_task_suspend:

TASK_SUSPEND - Suspend a task
-----------------------------
.. index:: suspending a task
.. index:: rtems_task_suspend

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

.. _rtems_task_resume:

TASK_RESUME - Resume a task
---------------------------
.. index:: resuming a task
.. index:: rtems_task_resume

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

.. _rtems_task_is_suspended:

TASK_IS_SUSPENDED - Determine if a task is Suspended
----------------------------------------------------
.. index:: is task suspended
.. index:: rtems_task_is_suspended

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

.. _rtems_task_set_priority:

TASK_SET_PRIORITY - Set task priority
-------------------------------------
.. index:: rtems_task_set_priority
.. index:: current task priority
.. index:: set task priority
.. index:: get task priority
.. index:: obtain task priority

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

.. _rtems_task_get_priority:

TASK_GET_PRIORITY - Get task priority
-------------------------------------
.. index:: rtems_task_get_priority
.. index:: current task priority
.. index:: get task priority
.. index:: obtain task priority

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

.. _rtems_task_mode:

TASK_MODE - Change the current task mode
----------------------------------------
.. index:: current task mode
.. index:: set task mode
.. index:: get task mode
.. index:: set task preemption mode
.. index:: get task preemption mode
.. index:: obtain task mode
.. index:: rtems_task_mode

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

.. _rtems_task_wake_after:

TASK_WAKE_AFTER - Wake up after interval
----------------------------------------
.. index:: delay a task for an interval
.. index:: wake up after an interval
.. index:: rtems_task_wake_after

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

.. _rtems_task_wake_when:

TASK_WAKE_WHEN - Wake up when specified
---------------------------------------
.. index:: delay a task until a wall time
.. index:: wake up at a wall time
.. index:: rtems_task_wake_when

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

        void task( rtems_task_argument arg );

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

.. _rtems_task_iterate:

TASK_ITERATE - Iterate Over Tasks
---------------------------------
.. index:: iterate over all threads
.. index:: rtems_task_iterate

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

Deprecated and Removed Directives
=================================

.. raw:: latex

   \clearpage

.. _rtems_iterate_over_all_threads:

ITERATE_OVER_ALL_THREADS - Iterate Over Tasks
---------------------------------------------
.. index:: rtems_iterate_over_all_threads

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

.. raw:: latex

   \clearpage

.. _rtems_task_get_note:

TASK_GET_NOTE - Get task notepad entry
--------------------------------------
.. index:: get task notepad entry
.. index:: rtems_task_get_note

.. warning::

    This directive was removed in RTEMS 4.12.

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

.. _rtems_task_set_note:

TASK_SET_NOTE - Set task notepad entry
--------------------------------------
.. index:: set task notepad entry
.. index:: rtems_task_set_note

.. warning::

    This directive was removed in RTEMS 4.12.

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

.. _rtems_task_variable_add:

TASK_VARIABLE_ADD - Associate per task variable
-----------------------------------------------
.. index:: per-task variable
.. index:: task private variable
.. index:: task private data
.. index:: rtems_task_variable_add

.. warning::

    This directive was removed in RTEMS 4.12.

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

.. _rtems_task_variable_get:

TASK_VARIABLE_GET - Obtain value of a per task variable
-------------------------------------------------------
.. index:: get per-task variable
.. index:: obtain per-task variable
.. index:: rtems_task_variable_get

.. warning::

    This directive was removed in RTEMS 4.12.

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

.. _rtems_task_variable_delete:

TASK_VARIABLE_DELETE - Remove per task variable
-----------------------------------------------
.. index:: per-task variable
.. index:: task private variable
.. index:: task private data
.. index:: rtems_task_variable_delete

.. warning::

    This directive was removed in RTEMS 4.12.

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
