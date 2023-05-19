.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2022 embedded brains GmbH & Co. KG
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

.. index:: task, definition

Task Definition
---------------

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

.. _TaskControlBlock:

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

.. index:: task memory

Task Memory
-----------

The system uses two separate memory areas to manage a task.  One memory area is
the :ref:`TaskControlBlock`.  The other memory area is allocated from the stack
space or provided by the user and contains

* the task stack,

* the thread-local storage (:term:`TLS`), and

* an optional architecture-specific floating-point context.

The size of the thread-local storage is determined at link time.  A
user-provided task stack must take the size of the thread-local storage into
account.

On architectures with a dedicated floating-point context, the application
configuration assumes that every task is a floating-point task, but whether or
not a task is actually floating-point is determined at runtime during task
creation (see :ref:`TaskFloatingPointConsiderations`).  In highly memory
constrained systems this potential overestimate of the task stack space can be
mitigated through the :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE` configuration
option and aligned task stack sizes for the tasks.  A user-provided task stack
must take the potential floating-point context into account.

.. index:: task name

Task Name
---------

By default, the task name is defined by the task object name given to
:ref:`rtems_task_create() <rtems_task_create>`.  The task name can be obtained
with the `pthread_getname_np()
<http://man7.org/linux/man-pages/man3/pthread_setname_np.3.html>`_ function.
Optionally, a new task name may be set with the `pthread_setname_np()
<http://man7.org/linux/man-pages/man3/pthread_setname_np.3.html>`_ function.
The maximum size of a task name is defined by the application configuration
option :ref:`CONFIGURE_MAXIMUM_THREAD_NAME_SIZE
<CONFIGURE_MAXIMUM_THREAD_NAME_SIZE>`.

.. index:: task states

Task States
-----------

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

.. index:: task priority
.. index:: priority, task
.. index:: rtems_task_priority

.. _TaskPriority:

Task Priority
-------------

A task's :term:`priority` determines its importance in relation to the other
tasks executing on the processor set owned by a :term:`scheduler`.  Normally,
RTEMS supports 256 levels of priority ranging from 0 to 255.  The priority
level 0 represents a special priority reserved for the operating system.  The
data type :c:type:`rtems_task_priority` is used to store task priorities.  The
maximum priority level depends on the configured scheduler, see
:ref:`CONFIGURE_MAXIMUM_PRIORITY`, :ref:`ConfigurationSchedulersClustered`, and
:ref:`RTEMSAPIClassicScheduler`.

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

.. index:: task mode
.. index:: rtems_task_mode

Task Mode
---------

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

.. index:: task life states

Task Life States
----------------

Independent of the task state with respect to the scheduler, the task life is
determined by several orthogonal states:

* *protected* or *unprotected*

* *deferred life changes* or *no deferred life changes*

* *restarting* or *not restarting*

* *terminating* or *not terminating*

* *detached* or *not detached*

While the task life is *protected*, asynchronous task restart and termination
requests are blocked.  A task may still restart or terminate itself.  All tasks
are created with an unprotected task life.  The task life protection is used by
the system to prevent system resources being affected by asynchronous task
restart and termination requests.  The task life protection can be enabled
(``PTHREAD_CANCEL_DISABLE``) or disabled (``PTHREAD_CANCEL_ENABLE``) for the
calling task through the ``pthread_setcancelstate()`` directive.

While *deferred life changes* are enabled, asynchronous task restart and
termination requests are delayed until the task performs a life change itself
or calls ``pthread_testcancel()``.  Cancellation points are not implemented in
RTEMS.  Deferred task life changes can be enabled (``PTHREAD_CANCEL_DEFERRED``)
or disabled (``PTHREAD_CANCEL_ASYNCHRONOUS``) for the calling task through the
``pthread_setcanceltype()`` directive.  Classic API tasks are created with
deferred life changes disabled.  POSIX threads are created with deferred life
changes enabled.

A task is made *restarting* by issuing a task restart request through the
:ref:`InterfaceRtemsTaskRestart` directive.

A task is made *terminating* by issuing a task termination request through the
:ref:`InterfaceRtemsTaskExit`, :ref:`InterfaceRtemsTaskDelete`,
``pthread_exit()``, and ``pthread_cancel()`` directives.

When a *detached* task terminates, the termination procedure completes without
the need for another task to join with the terminated task.  Classic API tasks
are created as not detached.  The detached state of created POSIX threads is
determined by the thread attributes.  They are created as not detached by
default.  The calling task is made detached through the ``pthread_detach()``
directive.  The :ref:`InterfaceRtemsTaskExit` directive and self deletion
though :ref:`InterfaceRtemsTaskDelete` directive make the calling task
detached.  In contrast, the ``pthread_exit()`` directive does not change the
detached state of the calling task.

.. index:: task arguments
.. index:: task prototype

Accessing Task Arguments
------------------------

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

.. index:: floating point

.. _TaskFloatingPointConsiderations:

Floating Point Considerations
-----------------------------

Please consult the *RTEMS CPU Architecture Supplement* if this section is
relevant on your architecture.  On some architectures the floating-point context
is contained in the normal task context and this section does not apply.

Creating a task with the ``RTEMS_FLOATING_POINT`` attribute flag results in
additional memory being allocated for the task to store the state of the numeric
coprocessor during task switches.  This additional memory is **not** allocated
for ``RTEMS_NO_FLOATING_POINT`` tasks. Saving and restoring the context of a
``RTEMS_FLOATING_POINT`` task takes longer than that of a
``RTEMS_NO_FLOATING_POINT`` task because of the relatively large amount of time
required for the numeric coprocessor to save or restore its computational state.

Since RTEMS was designed specifically for embedded military applications which
are floating point intensive, the executive is optimized to avoid unnecessarily
saving and restoring the state of the numeric coprocessor.  In uniprocessor
configurations, the state of the numeric coprocessor is only saved when a
``RTEMS_FLOATING_POINT`` task is dispatched and that task was not the last task
to utilize the coprocessor.  In a uniprocessor system with only one
``RTEMS_FLOATING_POINT`` task, the state of the numeric coprocessor will never
be saved or restored.

Although the overhead imposed by ``RTEMS_FLOATING_POINT`` tasks is minimal,
some applications may wish to completely avoid the overhead associated with
``RTEMS_FLOATING_POINT`` tasks and still utilize a numeric coprocessor.  By
preventing a task from being preempted while performing a sequence of floating
point operations, a ``RTEMS_NO_FLOATING_POINT`` task can utilize the numeric
coprocessor without incurring the overhead of a ``RTEMS_FLOATING_POINT``
context switch.  This approach also avoids the allocation of a floating point
context area.  However, if this approach is taken by the application designer,
**no** tasks should be created as ``RTEMS_FLOATING_POINT`` tasks.  Otherwise, the
floating point context will not be correctly maintained because RTEMS assumes
that the state of the numeric coprocessor will not be altered by
``RTEMS_NO_FLOATING_POINT`` tasks.  Some architectures with a dedicated
floating-point context raise a processor exception if a task with
``RTEMS_NO_FLOATING_POINT`` issues a floating-point instruction, so this
approach may not work at all.

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

.. index:: task attributes, building

Building a Task Attribute Set
-----------------------------

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

.. index:: task mode, building

Building a Mode and Mask
------------------------

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
