% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020, 2022 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

% Generated from spec:/acfg/if/group-idle

# Idle Task Configuration

This section describes configuration options related to the idle tasks.

% Generated from spec:/acfg/if/idle-task-body

```{raw} latex
\clearpage
```

```{index} CONFIGURE_IDLE_TASK_BODY
```

(configure-idle-task-body)=

## CONFIGURE_IDLE_TASK_BODY

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_IDLE_TASK_BODY`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is an initializer define.

```{eval-rst}
.. rubric:: DEFAULT VALUE:
```

If the {ref}`CONFIGURE_DISABLE_BSP_SETTINGS` configuration option is not defined and
{c:macro}`BSP_IDLE_TASK_BODY` is provided by the
{term}`BSP`, then the default value is defined by
{c:macro}`BSP_IDLE_TASK_BODY`, otherwise the default value is
`_CPU_Thread_Idle_body`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The value of this configuration option initializes the IDLE thread body.

```{eval-rst}
.. rubric:: NOTES:
```

IDLE threads shall not block. A blocking IDLE thread results in undefined
system behaviour because the scheduler assume that at least one ready thread
exists.

IDLE threads can be used to initialize the application, see configuration
option {ref}`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`.

The BSP may have knowledge of the specific CPU model, system controller
logic, and peripheral buses, so a BSP-specific IDLE task may be capable of
turning components off to save power during extended periods of no task
activity.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The value of the configuration option shall be defined to a valid function
pointer of the type `void *( *idle_body )( uintptr_t )`.

% Generated from spec:/acfg/if/idle-task-init-appl

```{raw} latex
\clearpage
```

```{index} CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION
```

(configure-idle-task-initializes-application)=

## CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is a boolean feature define.

```{eval-rst}
.. rubric:: DEFAULT CONFIGURATION:
```

If this configuration option is undefined, then the user is assumed to
provide one or more initialization tasks.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This configuration option is defined to indicate that the user has configured
**no** user initialization tasks or threads and that the user provided IDLE
task will perform application initialization and then transform itself into
an IDLE task.

```{eval-rst}
.. rubric:: NOTES:
```

If you use this option be careful, the user IDLE task **cannot** block at all
during the initialization sequence. Further, once application
initialization is complete, it shall make itself preemptible and enter an idle
body loop.

The IDLE task shall run at the lowest priority of all tasks in the system.

If this configuration option is defined, then it is mandatory to configure a
user IDLE task with the {ref}`CONFIGURE_IDLE_TASK_BODY` configuration option,
otherwise a compile time error in the configuration file will occur.

The application shall define at least one of the following configuration
options

- {ref}`CONFIGURE_RTEMS_INIT_TASKS_TABLE`,
- {ref}`CONFIGURE_POSIX_INIT_THREAD_TABLE`, or
- `CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`

otherwise a compile time error in the configuration file will occur.

If no Classic API initialization task and no POSIX API initialization thread
is configured, then no {ref}`GlobalConstruction` is performed.

% Generated from spec:/acfg/if/idle-task-stack-size

```{raw} latex
\clearpage
```

```{index} CONFIGURE_IDLE_TASK_STACK_SIZE
```

(configure-idle-task-stack-size)=

## CONFIGURE_IDLE_TASK_STACK_SIZE

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_IDLE_TASK_STACK_SIZE`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is an integer define.

```{eval-rst}
.. rubric:: DEFAULT VALUE:
```

If the {ref}`CONFIGURE_DISABLE_BSP_SETTINGS` configuration option is not defined and
{c:macro}`BSP_IDLE_TASK_STACK_SIZE` is provided by the
{term}`BSP`, then the default value is defined by
{c:macro}`BSP_IDLE_TASK_STACK_SIZE`, otherwise the default value is
defined by the {ref}`CONFIGURE_MINIMUM_TASK_STACK_SIZE` configuration option.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The value of this configuration option defines the task stack size for an
IDLE task.

```{eval-rst}
.. rubric:: NOTES:
```

In SMP configurations, there is one IDLE task per configured processor, see
{ref}`CONFIGURE_MAXIMUM_PROCESSORS`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this configuration option:

- The value of the configuration option shall be greater than or equal to a
  BSP-specific and application-specific minimum value.
- The value of the configuration option shall be small enough so that the IDLE
  task stack area calculation carried out by `<rtems/confdefs.h>` does not
  overflow an integer of type [size_t](https://en.cppreference.com/w/c/types/size_t).

% Generated from spec:/acfg/if/idle-task-storage-size

```{raw} latex
\clearpage
```

```{index} CONFIGURE_IDLE_TASK_STORAGE_SIZE
```

```{index} IDLE task storage size
```

(configure-idle-task-storage-size)=

## CONFIGURE_IDLE_TASK_STORAGE_SIZE

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_IDLE_TASK_STORAGE_SIZE`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is an integer define.

```{eval-rst}
.. rubric:: DEFAULT VALUE:
```

This configuration option has no default value. If it is not specified, then
the task storage area for each {term}`IDLE task` will allocated
from the RTEMS Workspace or through a custom IDLE task stack allocator.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

If this configuration option is specified, then the task storage areas for
the {term}`IDLE tasks <IDLE task>` are statically allocated by
`<rtems/confdefs.h>`. The value of this configuration option defines the
size in bytes of the task storage area of each IDLE task in the system.

```{eval-rst}
.. rubric:: NOTES:
```

By default, the IDLE task storage areas are allocated from the RTEMS
Workspace. Applications which do not want to use a heap allocator can use
this configuration option to use statically allocated memory for the IDLE
task storage areas. The task storage area contains the task stack, the
thread-local storage, and the floating-point context on architectures with a
separate floating-point context. The size of the thread-local storage area
is defined at link time or by the {ref}`CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE`
configuration option. You have to estimate the actual thread-local storage
size if you want to use this configuration option. If the IDLE task stack
size would be less than the value defined by the
{ref}`CONFIGURE_IDLE_TASK_STACK_SIZE` configuration option, for example because the
thread-local storage size is larger than expected, then the system terminates
with the {ref}`INTERNAL_ERROR_CORE <FatalErrorSources>` fatal source and the
{ref}`INTERNAL_ERROR_IDLE_THREAD_STACK_TOO_SMALL <internal_errors>` fatal code during
system initialization.

The value of this configuration option is passed to
{ref}`InterfaceRTEMSTASKSTORAGESIZE` by `<rtems/confdefs.h>` to determine
the actual size of the statically allocated area to take
architecture-specific overheads into account.

The

- `CONFIGURE_IDLE_TASK_STORAGE_SIZE`, and
- {ref}`CONFIGURE_TASK_STACK_ALLOCATOR_FOR_IDLE`

configuration options are mutually exclusive.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The value of the configuration option shall be greater than or equal to
{ref}`CONFIGURE_IDLE_TASK_STACK_SIZE`.
