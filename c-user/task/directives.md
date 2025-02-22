% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2023 On-Line Applications Research Corporation (OAR)

% This file is part of the RTEMS quality process and was automatically

% generated.  If you find something that needs to be fixed or

% worded better please post a report or patch to an RTEMS mailing list

% or raise a bug report:

%

% https://www.rtems.org/bugs.html

%

% For information on updating and regenerating please refer to the How-To

% section in the Software Requirements Engineering chapter of the

% RTEMS Software Engineering manual.  The manual is provided as a part of

% a release.  For development sources please refer to the online

% documentation at:

%

% https://docs.rtems.org

(taskmanagerdirectives)=

# Directives

This section details the directives of the Task Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/task/if/create

```{raw} latex
\clearpage
```

```{index} rtems_task_create()
```

```{index} create a task
```

(interfacertemstaskcreate)=

## rtems_task_create()

Creates a task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_create(
  rtems_name          name,
  rtems_task_priority initial_priority,
  size_t              stack_size,
  rtems_mode          initial_modes,
  rtems_attribute     attribute_set,
  rtems_id           *id
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`name`

: This parameter is the object name of the task.

`initial_priority`

: This parameter is the initial task priority.

`stack_size`

: This parameter is the task stack size in bytes.

`initial_modes`

: This parameter is the initial mode set of the task.

`attribute_set`

: This parameter is the attribute set of the task.

`id`

: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When
  the directive call is successful, the identifier of the created task will
  be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive creates a task which resides on the local node. The task has
the user-defined object name specified in `name`. The assigned object
identifier is returned in `id`. This identifier is used to access the task
with other task related directives.

The **initial priority** of the task is specified in `initial_priority`. The
{term}`home scheduler` of the created task is the home scheduler of the calling
task at some time point during the task creation. The initial task priority
specified in `initial_priority` shall be valid for this scheduler.

The **stack size** of the task is specified in `stack_size`. If the
requested stack size is less than the configured minimum stack size, then RTEMS
will use the configured minimum as the stack size for this task. The
configured minimum stack size is defined by the
{ref}`CONFIGURE_MINIMUM_TASK_STACK_SIZE` application configuration option. In
addition to being able to specify the task stack size as a integer, there are
two constants which may be specified:

- The {c:macro}`RTEMS_MINIMUM_STACK_SIZE` constant can be specified to use the
  **recommended minimum stack size** for the target processor. This value is
  selected by the RTEMS maintainers conservatively to minimize the risk of
  blown stacks for most user applications. Using this constant when specifying
  the task stack size, indicates that the stack size will be at least
  {c:macro}`RTEMS_MINIMUM_STACK_SIZE` bytes in size. If the user configured
  minimum stack size is larger than the recommended minimum, then it will be
  used.
- The {c:macro}`RTEMS_CONFIGURED_MINIMUM_STACK_SIZE` constant can be specified
  to use the minimum stack size that was configured by the application. If not
  explicitly configured by the application, the default configured minimum
  stack size is the target processor dependent value
  {c:macro}`RTEMS_MINIMUM_STACK_SIZE`. Since this uses the configured minimum
  stack size value, you may get a stack size that is smaller or larger than the
  recommended minimum. This can be used to provide large stacks for all tasks
  on complex applications or small stacks on applications that are trying to
  conserve memory.

The **initial mode set** specified in `initial_modes` is built through a
*bitwise or* of the mode constants described below. Not all combinations of
modes are allowed. Some modes are mutually exclusive. If mutually exclusive
modes are combined, the behaviour is undefined. Default task modes can be
selected by using the {c:macro}`RTEMS_DEFAULT_MODES` constant. The task mode
set defines

- the preemption mode of the task: {c:macro}`RTEMS_PREEMPT` (default) or
  {c:macro}`RTEMS_NO_PREEMPT`,
- the timeslicing mode of the task: {c:macro}`RTEMS_TIMESLICE` or
  {c:macro}`RTEMS_NO_TIMESLICE` (default),
- the {term}`ASR` processing mode of the task: {c:macro}`RTEMS_ASR` (default)
  or {c:macro}`RTEMS_NO_ASR`,
- the interrupt level of the task: {c:func}`RTEMS_INTERRUPT_LEVEL` with a
  default of `RTEMS_INTERRUPT_LEVEL( 0 )` which is associated with enabled
  interrupts.

The **initial preemption mode** of the task is enabled or disabled.

- An **enabled preemption** is the default and can be emphasized through the
  use of the {c:macro}`RTEMS_PREEMPT` mode constant.
- A **disabled preemption** is set by the {c:macro}`RTEMS_NO_PREEMPT` mode
  constant.

The **initial timeslicing mode** of the task is enabled or disabled.

- A **disabled timeslicing** is the default and can be emphasized through the
  use of the {c:macro}`RTEMS_NO_TIMESLICE` mode constant.
- An **enabled timeslicing** is set by the {c:macro}`RTEMS_TIMESLICE` mode
  constant.

The **initial ASR processing mode** of the task is enabled or disabled.

- An **enabled ASR processing** is the default and can be emphasized through
  the use of the {c:macro}`RTEMS_ASR` mode constant.
- A **disabled ASR processing** is set by the {c:macro}`RTEMS_NO_ASR` mode
  constant.

The **initial interrupt level mode** of the task is defined by
{c:func}`RTEMS_INTERRUPT_LEVEL`.

- Task execution with **interrupts enabled** the default and can be emphasized
  through the use of the {c:func}`RTEMS_INTERRUPT_LEVEL` mode macro with a
  value of zero (0) for the parameter. An interrupt level of zero is
  associated with enabled interrupts on all target processors.
- Task execution at a **non-zero interrupt level** can be specified by the
  {c:func}`RTEMS_INTERRUPT_LEVEL` mode macro with a non-zero value for the
  parameter. The interrupt level portion of the task mode supports a maximum
  of 256 interrupt levels. These levels are mapped onto the interrupt levels
  actually supported by the target processor in a processor dependent fashion.

The **attribute set** specified in `attribute_set` is built through a
*bitwise or* of the attribute constants described below. Not all combinations
of attributes are allowed. Some attributes are mutually exclusive. If
mutually exclusive attributes are combined, the behaviour is undefined.
Attributes not mentioned below are not evaluated by this directive and have no
effect. Default attributes can be selected by using the
{c:macro}`RTEMS_DEFAULT_ATTRIBUTES` constant. The attribute set defines

- the scope of the task: {c:macro}`RTEMS_LOCAL` (default) or
  {c:macro}`RTEMS_GLOBAL` and
- the floating-point unit use of the task: {c:macro}`RTEMS_FLOATING_POINT` or
  {c:macro}`RTEMS_NO_FLOATING_POINT` (default).

The task has a local or global **scope** in a multiprocessing network (this
attribute does not refer to SMP systems). The scope is selected by the
mutually exclusive {c:macro}`RTEMS_LOCAL` and {c:macro}`RTEMS_GLOBAL`
attributes.

- A **local scope** is the default and can be emphasized through the use of the
  {c:macro}`RTEMS_LOCAL` attribute. A local task can be only used by the node
  which created it.
- A **global scope** is established if the {c:macro}`RTEMS_GLOBAL` attribute is
  set. Setting the global attribute in a single node system has no effect.the

The **use of the floating-point unit** is selected by the mutually exclusive
{c:macro}`RTEMS_FLOATING_POINT` and {c:macro}`RTEMS_NO_FLOATING_POINT`
attributes. On some target processors, the use of the floating-point unit can
be enabled or disabled for each task. Other target processors may have no
hardware floating-point unit or enable the use of the floating-point unit for
all tasks. Consult the *RTEMS CPU Architecture Supplement* for the details.

- A **disabled floating-point unit** is the default and can be emphasized
  through use of the {c:macro}`RTEMS_NO_FLOATING_POINT` attribute. For
  performance reasons, it is recommended that tasks not using the
  floating-point unit should specify this attribute.
- An **enabled floating-point unit** is selected by the
  {c:macro}`RTEMS_FLOATING_POINT` attribute.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_NAME`

: The `name` parameter was invalid.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_PRIORITY`

: The `initial_priority` was invalid.

{c:macro}`RTEMS_TOO_MANY`

: There was no inactive object available to create a task. The number of
  tasks available to the application is configured through the
  {ref}`CONFIGURE_MAXIMUM_TASKS` application configuration option.

{c:macro}`RTEMS_TOO_MANY`

: In multiprocessing configurations, there was no inactive global object
  available to create a global task. The number of global objects available
  to the application is configured through the
  {ref}`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application configuration
  option.

{c:macro}`RTEMS_UNSATISFIED`

: There was not enough memory to allocate the task storage area. The task
  storage area contains the task stack, the thread-local storage, and the
  floating point context.

{c:macro}`RTEMS_UNSATISFIED`

: One of the task create extensions failed to create the task.

{c:macro}`RTEMS_UNSATISFIED`

: In SMP configurations, the non-preemption mode was not supported.

{c:macro}`RTEMS_UNSATISFIED`

: In SMP configurations, the interrupt level mode was not supported.

```{eval-rst}
.. rubric:: NOTES:
```

The task processor affinity is initialized to the set of online processors.

When created, a task is placed in the dormant state and can only be made ready
to execute using the directive {ref}`InterfaceRtemsTaskStart`.

Application developers should consider the stack usage of the device drivers
when calculating the stack size required for tasks which utilize the driver.
The task stack size shall account for an target processor dependent interrupt
stack frame which may be placed on the stack of the interrupted task while
servicing an interrupt. The stack checker may be used to monitor the stack
usage, see {ref}`CONFIGURE_STACK_CHECKER_ENABLED`.

For control and maintenance of the task, RTEMS allocates a {term}`TCB` from the
local TCB free pool and initializes it.

The TCB for a global task is allocated on the local node. Task should not be
made global unless remote tasks must interact with the task. This is to avoid
the system overhead incurred by the creation of a global task. When a global
task is created, the task's name and identifier must be transmitted to every
node in the system for insertion in the local copy of the global object table.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- When the directive operates on a global object, the directive sends a message
  to remote nodes. This may preempt the calling task.
- The number of tasks available to the application is configured through the
  {ref}`CONFIGURE_MAXIMUM_TASKS` application configuration option.
- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.
- The number of global objects available to the application is configured
  through the {ref}`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application
  configuration option.

% Generated from spec:/rtems/task/if/construct

```{raw} latex
\clearpage
```

```{index} rtems_task_construct()
```

(interfacertemstaskconstruct)=

## rtems_task_construct()

Constructs a task from the specified task configuration.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_construct(
  const rtems_task_config *config,
  rtems_id                *id
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`config`

: This parameter is the pointer to an {ref}`InterfaceRtemsTaskConfig` object.
  It configures the task.

`id`

: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When
  the directive call is successful, the identifier of the constructed task
  will be stored in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `config` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_NAME`

: The task name was invalid.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_PRIORITY`

: The initial task priority was invalid.

{c:macro}`RTEMS_INVALID_SIZE`

: The thread-local storage size is greater than the maximum thread-local
  storage size specified in the task configuration. The thread-local storage
  size is determined by the thread-local variables used by the application
  and {ref}`CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE`.

{c:macro}`RTEMS_INVALID_SIZE`

: The task storage area was too small to provide a task stack of the
  configured minimum size, see {ref}`CONFIGURE_MINIMUM_TASK_STACK_SIZE`. The
  task storage area contains the task stack, the thread-local storage, and
  the floating-point context on architectures with a separate floating-point
  context.

{c:macro}`RTEMS_TOO_MANY`

: There was no inactive task object available to construct a task.

{c:macro}`RTEMS_TOO_MANY`

: In multiprocessing configurations, there was no inactive global object
  available to construct a global task.

{c:macro}`RTEMS_UNSATISFIED`

: One of the task create extensions failed during the task construction.

{c:macro}`RTEMS_UNSATISFIED`

: In SMP configurations, the non-preemption mode was not supported.

{c:macro}`RTEMS_UNSATISFIED`

: In SMP configurations, the interrupt level mode was not supported.

```{eval-rst}
.. rubric:: NOTES:
```

In contrast to tasks created by {ref}`InterfaceRtemsTaskCreate`, the tasks
constructed by this directive use a user-provided task storage area. The task
storage area contains the task stack, the thread-local storage, and the
floating-point context on architectures with a separate floating-point context.

This directive is intended for applications which do not want to use the RTEMS
Workspace and instead statically allocate all operating system resources. It
is not recommended to use {ref}`InterfaceRtemsTaskCreate` and
{ref}`InterfaceRtemsTaskConstruct` together in an application. It is also not
recommended to use {ref}`InterfaceRtemsTaskConstruct` for drivers or general
purpose libraries. The reason for these recommendations is that the task
configuration needs settings which can be only given with a through knowledge
of the application resources.

An application based solely on static allocation can avoid any runtime memory
allocators. This can simplify the application architecture as well as any
analysis that may be required.

The stack space estimate done by `<rtems/confdefs.h>` assumes that all tasks
are created by {ref}`InterfaceRtemsTaskCreate`. The estimate can be adjusted
to take user-provided task storage areas into account through the
{ref}`CONFIGURE_MINIMUM_TASKS_WITH_USER_PROVIDED_STORAGE` application
configuration option.

The {ref}`CONFIGURE_MAXIMUM_TASKS` should include tasks constructed by
{ref}`InterfaceRtemsTaskConstruct`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- When the directive operates on a global object, the directive sends a message
  to remote nodes. This may preempt the calling task.
- The number of tasks available to the application is configured through the
  {ref}`CONFIGURE_MAXIMUM_TASKS` application configuration option.
- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.
- The number of global objects available to the application is configured
  through the {ref}`CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS` application
  configuration option.

% Generated from spec:/rtems/task/if/ident

```{raw} latex
\clearpage
```

```{index} rtems_task_ident()
```

(interfacertemstaskident)=

## rtems_task_ident()

Identifies a task by the object name.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_ident(
  rtems_name name,
  uint32_t   node,
  rtems_id  *id
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`name`

: This parameter is the object name to look up.

`node`

: This parameter is the node or node set to search for a matching object.

`id`

: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When
  the directive call is successful, the object identifier of an object with
  the specified name will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive obtains a task identifier associated with the task name
specified in `name`.

A task may obtain its own identifier by specifying {c:macro}`RTEMS_WHO_AM_I`
for the name.

The node to search is specified in `node`. It shall be

- a valid node number,
- the constant {c:macro}`RTEMS_SEARCH_ALL_NODES` to search in all nodes,
- the constant {c:macro}`RTEMS_SEARCH_LOCAL_NODE` to search in the local node
  only, or
- the constant {c:macro}`RTEMS_SEARCH_OTHER_NODES` to search in all nodes
  except the local node.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_NAME`

: There was no object with the specified name on the specified nodes.

{c:macro}`RTEMS_INVALID_NODE`

: In multiprocessing configurations, the specified node was invalid.

```{eval-rst}
.. rubric:: NOTES:
```

If the task name is not unique, then the task identifier will match the first
task with that name in the search order. However, this task identifier is not
guaranteed to correspond to the desired task.

The objects are searched from lowest to the highest index. If `node` is
{c:macro}`RTEMS_SEARCH_ALL_NODES`, all nodes are searched with the local node
being searched first. All other nodes are searched from lowest to the highest
node number.

If node is a valid node number which does not represent the local node, then
only the tasks exported by the designated node are searched.

This directive does not generate activity on remote nodes. It accesses only
the local copy of the global object table.

The task identifier is used with other task related directives to access the
task.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/self

```{raw} latex
\clearpage
```

```{index} rtems_task_self()
```

```{index} obtain ID of caller
```

(interfacertemstaskself)=

## rtems_task_self()

Gets the task identifier of the calling task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_id rtems_task_self( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns the task identifier of the calling task.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the task identifier of the calling task.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/start

```{raw} latex
\clearpage
```

```{index} rtems_task_start()
```

```{index} starting a task
```

(interfacertemstaskstart)=

## rtems_task_start()

Starts the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_start(
  rtems_id            id,
  rtems_task_entry    entry_point,
  rtems_task_argument argument
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`entry_point`

: This parameter is the task entry point.

`argument`

: This parameter is the task entry point argument.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive readies the task, specified by `id`, for execution based on
the priority and execution mode specified when the task was created. The
{term}`task entry` point of the task is given in `entry_point`. The task's
entry point argument is contained in `argument`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `entry_point` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_INCORRECT_STATE`

: The task was not in the dormant state.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: NOTES:
```

The type of the entry point argument is an unsigned integer type. However, the
integer type has the property that any valid pointer to `void` can be
converted to this type and then converted back to a pointer to `void`. The
result will compare equal to the original pointer. The type can represent at
least 32 bits. Some applications use the entry point argument as an index into
a parameter table to get task-specific parameters.

Any actions performed on a dormant task such as suspension or change of
priority are nullified when the task is initiated via the
{ref}`InterfaceRtemsTaskStart` directive.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may unblock a task. This may cause the calling task to be
  preempted.

% Generated from spec:/rtems/task/if/restart

```{raw} latex
\clearpage
```

```{index} rtems_task_restart()
```

```{index} restarting a task
```

(interfacertemstaskrestart)=

## rtems_task_restart()

Restarts the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_restart(
  rtems_id            id,
  rtems_task_argument argument
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`argument`

: This parameter is the task entry point argument.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive resets the task specified by `id` to begin execution at its
original entry point. The task's priority and execution mode are set to the
original creation values. If the task is currently blocked, RTEMS
automatically makes the task ready. A task can be restarted from any state,
except the dormant state. The task's entry point argument is contained in
`argument`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_INCORRECT_STATE`

: The task never started.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: NOTES:
```

The type of the entry point argument is an unsigned integer type. However, the
integer type has the property that any valid pointer to `void` can be
converted to this type and then converted back to a pointer to `void`. The
result will compare equal to the original pointer. The type can represent at
least 32 bits. Some applications use the entry point argument as an index into
a parameter table to get task-specific parameters.

A new entry point argument may be used to distinguish between the initial
{ref}`InterfaceRtemsTaskStart` of the task and any ensuing calls to
{ref}`InterfaceRtemsTaskRestart` of the task. This can be beneficial in
deleting a task. Instead of deleting a task using the
{ref}`InterfaceRtemsTaskDelete` directive, a task can delete another task by
restarting that task, and allowing that task to release resources back to RTEMS
and then delete itself.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may change the priority of a task. This may cause the calling
  task to be preempted.
- The directive may unblock a task. This may cause the calling task to be
  preempted.

% Generated from spec:/rtems/task/if/delete

```{raw} latex
\clearpage
```

```{index} rtems_task_delete()
```

```{index} delete a task
```

(interfacertemstaskdelete)=

## rtems_task_delete()

Deletes the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_delete( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive deletes the task, either the calling task or another task, as
specified by `id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_CALLED_FROM_ISR`

: The directive was called from within interrupt context.

{c:macro}`RTEMS_INCORRECT_STATE`

: The task termination procedure was started, however, waiting for the
  terminating task would have resulted in a deadlock.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: NOTES:
```

The task deletion is done in several steps. Firstly, the task is marked as
terminating. While the task life of the terminating task is protected, it
executes normally until it disables the task life protection or it deletes
itself. A terminating task will eventually stop its normal execution and start
its termination procedure. The procedure executes in the context of the
terminating task. The task termination procedure involves the destruction of
POSIX key values and running the task termination user extensions. Once
complete the execution of the task is stopped and task-specific resources are
reclaimed by the system, such as the stack memory, any allocated delay or
timeout timers, the {term}`TCB`, and, if the task is
{c:macro}`RTEMS_FLOATING_POINT`, its floating point context area. RTEMS
explicitly does not reclaim the following resources: region segments, partition
buffers, semaphores, timers, or rate monotonic periods.

A task is responsible for releasing its resources back to RTEMS before
deletion. To insure proper deallocation of resources, a task should not be
deleted unless it is unable to execute or does not hold any RTEMS resources. If
a task holds RTEMS resources, the task should be allowed to deallocate its
resources before deletion. A task can be directed to release its resources and
delete itself by restarting it with a special argument or by sending it a
message, an event, or a signal.

Deletion of the calling task ({c:macro}`RTEMS_SELF`) will force RTEMS to select
another task to execute.

When a task deletes another task, the calling task waits until the task
termination procedure of the task being deleted has completed. The terminating
task inherits the {term}`eligible priorities <eligible priority>` of the
calling task.

When a global task is deleted, the task identifier must be transmitted to every
node in the system for deletion from the local copy of the global object table.

The task must reside on the local node, even if the task was created with the
{c:macro}`RTEMS_GLOBAL` attribute.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- When the directive operates on a global object, the directive sends a message
  to remote nodes. This may preempt the calling task.
- The calling task does not have to be the task that created the object. Any
  local task that knows the object identifier can delete the object.
- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

% Generated from spec:/rtems/task/if/exit

```{raw} latex
\clearpage
```

```{index} rtems_task_exit()
```

```{index} deleting a task
```

(interfacertemstaskexit)=

## rtems_task_exit()

Deletes the calling task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_task_exit( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive deletes the calling task.

```{eval-rst}
.. rubric:: NOTES:
```

The directive is an optimized variant of the following code sequences, see also
{ref}`InterfaceRtemsTaskDelete`:

```c
#include <pthread.h>
#include <rtems.h>

void classic_delete_self( void )
{
  (void) rtems_task_delete( RTEMS_SELF );
}

void posix_delete_self( void )
{
  (void) pthread_detach( pthread_self() );
  (void) pthread_exit( NULL);
}
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive will not return to the caller.
- While thread dispatching is disabled, if the directive performs a thread
  dispatch, then the fatal error with the fatal source
  {ref}`INTERNAL_ERROR_CORE <FatalErrorSources>` and the fatal code
  {ref}`INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL <internal_errors>`
  will occur.

% Generated from spec:/rtems/task/if/suspend

```{raw} latex
\clearpage
```

```{index} rtems_task_suspend()
```

```{index} suspending a task
```

(interfacertemstasksuspend)=

## rtems_task_suspend()

Suspends the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_suspend( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive suspends the task specified by `id` from further execution by
placing it in the suspended state. This state is additive to any other blocked
state that the task may already be in. The task will not execute again until
another task issues the {ref}`InterfaceRtemsTaskResume` directive for this task
and any blocked state has been removed. The {ref}`InterfaceRtemsTaskRestart`
directive will also remove the suspended state.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_ALREADY_SUSPENDED`

: The task was already suspended.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: NOTES:
```

The requesting task can suspend itself for example by specifying
{c:macro}`RTEMS_SELF` as `id`. In this case, the task will be suspended and
a successful return code will be returned when the task is resumed.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply. This will preempt the calling
  task.

% Generated from spec:/rtems/task/if/resume

```{raw} latex
\clearpage
```

```{index} rtems_task_resume()
```

```{index} resuming a task
```

(interfacertemstaskresume)=

## rtems_task_resume()

Resumes the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_resume( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive removes the task specified by `id` from the suspended state.
If the task is in the ready state after the suspension is removed, then it will
be scheduled to run. If the task is still in a blocked state after the
suspension is removed, then it will remain in that blocked state.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_INCORRECT_STATE`

: The task was not suspended.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may unblock a task. This may cause the calling task to be
  preempted.
- When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply. This will preempt the calling
  task.

% Generated from spec:/rtems/task/if/is-suspended

```{raw} latex
\clearpage
```

```{index} rtems_task_is_suspended()
```

(interfacertemstaskissuspended)=

## rtems_task_is_suspended()

Checks if the task is suspended.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_is_suspended( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns a status code indicating whether or not the task
specified by `id` is currently suspended.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The task was **not** suspended.

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_ALREADY_SUSPENDED`

: The task was suspended.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/set-priority

```{raw} latex
\clearpage
```

```{index} rtems_task_set_priority()
```

```{index} current task priority
```

```{index} set task priority
```

```{index} get task priority
```

```{index} obtain task priority
```

(interfacertemstasksetpriority)=

## rtems_task_set_priority()

Sets the real priority or gets the current priority of the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_set_priority(
  rtems_id             id,
  rtems_task_priority  new_priority,
  rtems_task_priority *old_priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`new_priority`

: This parameter is the new real priority or
  {c:macro}`RTEMS_CURRENT_PRIORITY` to get the current priority.

`old_priority`

: This parameter is the pointer to an {ref}`InterfaceRtemsTaskPriority`
  object. When the directive call is successful, the current or previous
  priority of the task with respect to its {term}`home scheduler` will be
  stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive manipulates the priority of the task specified by `id`. When
`new_priority` is not equal to {c:macro}`RTEMS_CURRENT_PRIORITY`, the
specified task's previous priority is returned in `old_priority`. When
`new_priority` is {c:macro}`RTEMS_CURRENT_PRIORITY`, the specified task's
current priority is returned in `old_priority`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `old_priority` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_INVALID_PRIORITY`

: The task priority specified in `new_priority` was invalid with respect to
  the {term}`home scheduler` of the task.

```{eval-rst}
.. rubric:: NOTES:
```

Valid priorities range from one to a maximum value which depends on the
configured scheduler. The lower the priority value the higher is the
importance of the task.

If the task is currently holding any binary semaphores which use a locking
protocol, then the task's priority cannot be lowered immediately. If the
task's priority were lowered immediately, then this could violate properties of
the locking protocol and may result in priority inversion. The requested
lowering of the task's priority will occur when the task has released all
binary semaphores which make the task more important. The task's priority can
be increased regardless of the task's use of binary semaphores with locking
protocols.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may change the priority of a task. This may cause the calling
  task to be preempted.
- When the directive operates on a remote object, the directive sends a message
  to the remote node and waits for a reply. This will preempt the calling
  task.

% Generated from spec:/rtems/task/if/get-priority

```{raw} latex
\clearpage
```

```{index} rtems_task_get_priority()
```

```{index} current task priority
```

```{index} get task priority
```

```{index} obtain task priority
```

(interfacertemstaskgetpriority)=

## rtems_task_get_priority()

Gets the current priority of the task with respect to the scheduler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_get_priority(
  rtems_id             task_id,
  rtems_id             scheduler_id,
  rtems_task_priority *priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`task_id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`scheduler_id`

: This parameter is the scheduler identifier.

`priority`

: This parameter is the pointer to an {ref}`InterfaceRtemsTaskPriority`
  object. When the directive call is successful, the current priority of the
  task with respect to the specified scheduler will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns the current priority in `priority` of the task
specified by `task_id` with respect to the scheduler specified by
`scheduler_id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `priority` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `task_id`.

{c:macro}`RTEMS_INVALID_ID`

: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_NOT_DEFINED`

: The task had no priority with respect to the scheduler.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: NOTES:
```

The current priority reflects temporary priority adjustments due to locking
protocols, the rate-monotonic period objects on some schedulers such as EDF,
and the POSIX sporadic server.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/mode

```{raw} latex
\clearpage
```

```{index} rtems_task_mode()
```

```{index} current task mode
```

```{index} set task mode
```

```{index} get task mode
```

```{index} set task preemption mode
```

```{index} get task preemption mode
```

```{index} obtain task mode
```

(interfacertemstaskmode)=

## rtems_task_mode()

Gets and optionally sets the mode of the calling task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_mode(
  rtems_mode  mode_set,
  rtems_mode  mask,
  rtems_mode *previous_mode_set
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`mode_set`

: This parameter is the mode set to apply to the calling task. When `mask`
  is set to {c:macro}`RTEMS_CURRENT_MODE`, the value of this parameter is
  ignored. Only modes requested by `mask` are applied to the calling task.

`mask`

: This parameter is the mode mask which specifies which modes in `mode_set`
  are applied to the calling task. When the value is
  {c:macro}`RTEMS_CURRENT_MODE`, the mode of the calling task is not changed.

`previous_mode_set`

: This parameter is the pointer to an {c:type}`rtems_mode` object. When the
  directive call is successful, the mode of the task before any mode changes
  done by the directive call will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive queries and optionally manipulates the execution mode of the
calling task. A task's execution mode enables and disables preemption,
timeslicing, asynchronous signal processing, as well as specifying the
interrupt level. To modify an execution mode, the mode class(es) to be changed
must be specified in the `mask` parameter and the desired mode(s) must be
specified in the `mode_set` parameter.

A task can obtain its current execution mode, without modifying it, by calling
this directive with a `mask` value of {c:macro}`RTEMS_CURRENT_MODE`.

The **mode set** specified in `mode_set` is built through a *bitwise or* of
the mode constants described below. Not all combinations of modes are allowed.
Some modes are mutually exclusive. If mutually exclusive modes are combined,
the behaviour is undefined. Default task modes can be selected by using the
{c:macro}`RTEMS_DEFAULT_MODES` constant. The task mode set defines

- the preemption mode of the task: {c:macro}`RTEMS_PREEMPT` (default) or
  {c:macro}`RTEMS_NO_PREEMPT`,
- the timeslicing mode of the task: {c:macro}`RTEMS_TIMESLICE` or
  {c:macro}`RTEMS_NO_TIMESLICE` (default),
- the {term}`ASR` processing mode of the task: {c:macro}`RTEMS_ASR` (default)
  or {c:macro}`RTEMS_NO_ASR`,
- the interrupt level of the task: {c:func}`RTEMS_INTERRUPT_LEVEL` with a
  default of `RTEMS_INTERRUPT_LEVEL( 0 )` which is associated with enabled
  interrupts.

The **mode mask** specified in `mask` is built through a *bitwise or* of the
mode mask constants described below.

When the {c:macro}`RTEMS_PREEMPT_MASK` is set in `mask`, the **preemption
mode** of the calling task is

- enabled by using the {c:macro}`RTEMS_PREEMPT` mode constant in `mode_set`
  and
- disabled by using the {c:macro}`RTEMS_NO_PREEMPT` mode constant in
  `mode_set`.

When the {c:macro}`RTEMS_TIMESLICE_MASK` is set in `mask`, the **timeslicing
mode** of the calling task is

- enabled by using the {c:macro}`RTEMS_TIMESLICE` mode constant in `mode_set`
  and
- disabled by using the {c:macro}`RTEMS_NO_TIMESLICE` mode constant in
  `mode_set`.

Enabling timeslicing has no effect if preemption is disabled. For a task to be
timesliced, that task must have both preemption and timeslicing enabled.

When the {c:macro}`RTEMS_ASR_MASK` is set in `mask`, the **ASR processing
mode** of the calling task is

- enabled by using the {c:macro}`RTEMS_ASR` mode constant in `mode_set` and
- disabled by using the {c:macro}`RTEMS_NO_ASR` mode constant in `mode_set`.

When the {c:macro}`RTEMS_INTERRUPT_MASK` is set in `mask`, **interrupts** of
the calling task are

- enabled by using the {c:func}`RTEMS_INTERRUPT_LEVEL` mode macro with a value
  of zero (0) in `mode_set` and
- disabled up to the specified level by using the
  {c:func}`RTEMS_INTERRUPT_LEVEL` mode macro with a positive value in
  `mode_set`.

An interrupt level of zero is associated with enabled interrupts on all target
processors. The interrupt level portion of the task mode supports a maximum of
256 interrupt levels. These levels are mapped onto the interrupt levels
actually supported by the target processor in a processor dependent fashion.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_NOT_IMPLEMENTED`

: The {c:macro}`RTEMS_NO_PREEMPT` was set in `mode_set` and setting the
  preemption mode was requested by {c:macro}`RTEMS_PREEMPT_MASK` in `mask`
  and the system configuration had no implementation for this mode.

{c:macro}`RTEMS_NOT_IMPLEMENTED`

: The {c:func}`RTEMS_INTERRUPT_LEVEL` was set to a positive level in
  `mode_set` and setting the interrupt level was requested by
  {c:macro}`RTEMS_INTERRUPT_MASK` in `mask` and the system configuration
  had no implementation for this mode.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- When the directive enables preemption for the calling task, another task may
  preempt the calling task.
- While thread dispatching is disabled, if the directive performs a thread
  dispatch, then the fatal error with the fatal source
  {ref}`INTERNAL_ERROR_CORE <FatalErrorSources>` and the fatal code
  {ref}`INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL <internal_errors>`
  will occur.

% Generated from spec:/rtems/task/if/wake-after

```{raw} latex
\clearpage
```

```{index} rtems_task_wake_after()
```

```{index} delay a task for a count of clock ticks
```

```{index} wake up after a count of clock ticks
```

(interfacertemstaskwakeafter)=

## rtems_task_wake_after()

Wakes up after a count of {term}`clock ticks <clock tick>` have occurred or
yields the processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_wake_after( rtems_interval ticks );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`ticks`

: This parameter is the count of {term}`clock ticks <clock tick>` to delay
  the task or {c:macro}`RTEMS_YIELD_PROCESSOR` to yield the processor.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive blocks the calling task for the specified `ticks` count of
clock ticks if the value is not equal to {c:macro}`RTEMS_YIELD_PROCESSOR`. When
the requested count of ticks have occurred, the task is made ready. The clock
tick directives automatically update the delay period. The calling task may
give up the processor and remain in the ready state by specifying a value of
{c:macro}`RTEMS_YIELD_PROCESSOR` in `ticks`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

```{eval-rst}
.. rubric:: NOTES:
```

Setting the system date and time with the {ref}`InterfaceRtemsClockSet`
directive and similar directives which set {term}`CLOCK_REALTIME` have no
effect on a {ref}`InterfaceRtemsTaskWakeAfter` blocked task. The delay until
first clock tick will never be a whole clock tick interval since this directive
will never execute exactly on a clock tick. Applications requiring use of a
clock ({term}`CLOCK_REALTIME` or {term}`CLOCK_MONOTONIC`) instead of clock
ticks should make use of [clock_nanosleep()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/clock_nanosleep.html).

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive requires a {term}`Clock Driver`.
- While thread dispatching is disabled, if the directive performs a thread
  dispatch, then the fatal error with the fatal source
  {ref}`INTERNAL_ERROR_CORE <FatalErrorSources>` and the fatal code
  {ref}`INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL <internal_errors>`
  will occur.

% Generated from spec:/rtems/task/if/wake-when

```{raw} latex
\clearpage
```

```{index} rtems_task_wake_when()
```

```{index} delay a task until a wall time
```

```{index} wake up at a wall time
```

(interfacertemstaskwakewhen)=

## rtems_task_wake_when()

Wakes up when specified.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_wake_when( const rtems_time_of_day *time_buffer );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`time_buffer`

: This parameter is the date and time to wake up.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive blocks a task until the date and time specified in
`time_buffer`. At the requested date and time, the calling task will be
unblocked and made ready to execute.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_NOT_DEFINED`

: The system date and time was not set.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `time_buffer` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_CLOCK`

: The time of day was invalid.

```{eval-rst}
.. rubric:: NOTES:
```

The ticks portion of `time_buffer` structure is ignored. The timing
granularity of this directive is a second.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive requires a {term}`Clock Driver`.
- While thread dispatching is disabled, if the directive performs a thread
  dispatch, then the fatal error with the fatal source
  {ref}`INTERNAL_ERROR_CORE <FatalErrorSources>` and the fatal code
  {ref}`INTERNAL_ERROR_BAD_THREAD_DISPATCH_DISABLE_LEVEL <internal_errors>`
  will occur.

% Generated from spec:/rtems/task/if/get-scheduler

```{raw} latex
\clearpage
```

```{index} rtems_task_get_scheduler()
```

(interfacertemstaskgetscheduler)=

## rtems_task_get_scheduler()

Gets the home scheduler of the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_get_scheduler(
  rtems_id  task_id,
  rtems_id *scheduler_id
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`task_id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`scheduler_id`

: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When
  the directive call is successful, the identifier of the {term}`home
  scheduler` of the task will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns the identifier of the {term}`home scheduler` of the task
specified by `task_id` in `scheduler_id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `scheduler_id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `task_id`.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/set-scheduler

```{raw} latex
\clearpage
```

```{index} rtems_task_set_scheduler()
```

(interfacertemstasksetscheduler)=

## rtems_task_set_scheduler()

Sets the home scheduler for the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_set_scheduler(
  rtems_id            task_id,
  rtems_id            scheduler_id,
  rtems_task_priority priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`task_id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`scheduler_id`

: This parameter is the scheduler identifier of the new {term}`home
  scheduler` for the task specified by `task_id`.

`priority`

: This parameter is the new real priority for the task with respect to the
  scheduler specified by `scheduler_id`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive sets the {term}`home scheduler` to the scheduler specified by
`scheduler_id` for the task specified by `task_id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`

: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_INVALID_PRIORITY`

: The {term}`task priority` specified by `priority` was invalid with
  respect to the scheduler specified by `scheduler_id`.

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `task_id`.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The task specified by `task_id` was enqueued on a {term}`wait queue`.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The task specified by `task_id` had a {term}`current priority` which
  consisted of more than the {term}`real priority`.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The task specified by `task_id` had a {term}`helping scheduler`.

{c:macro}`RTEMS_RESOURCE_IN_USE`

: The task specified by `task_id` was pinned.

{c:macro}`RTEMS_UNSATISFIED`

: The scheduler specified by `scheduler_id` owned no processor.

{c:macro}`RTEMS_UNSATISFIED`

: The scheduler specified by `scheduler_id` did not support the affinity
  set of the task specified by `task_id`.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may change the priority of a task. This may cause the calling
  task to be preempted.

% Generated from spec:/rtems/task/if/get-affinity

```{raw} latex
\clearpage
```

```{index} rtems_task_get_affinity()
```

(interfacertemstaskgetaffinity)=

## rtems_task_get_affinity()

Gets the processor affinity of the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_get_affinity(
  rtems_id   id,
  size_t     cpusetsize,
  cpu_set_t *cpuset
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`cpusetsize`

: This parameter is the size of the processor set referenced by `cpuset` in
  bytes.

`cpuset`

: This parameter is the pointer to a {c:type}`cpu_set_t` object. When the
  directive call is successful, the processor affinity set of the task will
  be stored in this object. A set bit in the processor set means that the
  corresponding processor is in the processor affinity set of the task,
  otherwise the bit is cleared.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns the processor affinity of the task in `cpuset` of the
task specified by `id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `cpuset` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_INVALID_SIZE`

: The size specified by `cpusetsize` of the processor set was too small for
  the processor affinity set of the task.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/set-affinity

```{raw} latex
\clearpage
```

```{index} rtems_task_set_affinity()
```

(interfacertemstasksetaffinity)=

## rtems_task_set_affinity()

Sets the processor affinity of the task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_task_set_affinity(
  rtems_id         id,
  size_t           cpusetsize,
  const cpu_set_t *cpuset
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`

: This parameter is the task identifier. The constant {c:macro}`RTEMS_SELF`
  may be used to specify the calling task.

`cpusetsize`

: This parameter is the size of the processor set referenced by `cpuset` in
  bytes.

`cpuset`

: This parameter is the pointer to a {c:type}`cpu_set_t` object. The
  processor set defines the new processor affinity set of the task. A set
  bit in the processor set means that the corresponding processor shall be in
  the processor affinity set of the task, otherwise the bit shall be cleared.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive sets the processor affinity of the task specified by `id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`

: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`

: The `cpuset` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`

: There was no task associated with the identifier specified by `id`.

{c:macro}`RTEMS_INVALID_NUMBER`

: The referenced processor set was not a valid new processor affinity set for
  the task.

{c:macro}`RTEMS_ILLEGAL_ON_REMOTE_OBJECT`

: The task resided on a remote node.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may change the processor affinity of a task. This may cause
  the calling task to be preempted.

% Generated from spec:/rtems/task/if/iterate

```{raw} latex
\clearpage
```

```{index} rtems_task_iterate()
```

(interfacertemstaskiterate)=

## rtems_task_iterate()

Iterates over all tasks and invokes the visitor routine for each task.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_task_iterate( rtems_task_visitor visitor, void *arg );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`visitor`

: This parameter is the visitor routine invoked for each task.

`arg`

: This parameter is the argument passed to each visitor routine invocation
  during the iteration.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive iterates over all tasks in the system. This operation covers
all tasks of all APIs. The user should be careful in accessing the contents of
the {term}`TCB`. The visitor argument `arg` is passed to all invocations of
`visitor` in addition to the TCB. The iteration stops immediately in case the
visitor routine returns true.

```{eval-rst}
.. rubric:: NOTES:
```

The visitor routine is invoked while owning the objects allocator lock. It is
allowed to perform blocking operations in the visitor routine, however, care
must be taken so that no deadlocks via the object allocator lock can occur.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/task/if/storage-size

```{raw} latex
\clearpage
```

```{index} RTEMS_TASK_STORAGE_SIZE()
```

(interfacertemstaskstoragesize)=

## RTEMS_TASK_STORAGE_SIZE()

Gets the recommended task storage area size for the size and task attributes.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
size_t RTEMS_TASK_STORAGE_SIZE( size_t size, rtems_attribute attributes );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`size`

: This parameter is the size dedicated to the task stack and thread-local
  storage in bytes.

`attributes`

: This parameter is the attribute set of the task using the storage area.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the recommended task storage area size calculated from the input
parameters.
