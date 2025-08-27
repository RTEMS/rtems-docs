% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG

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

% Generated from spec:/acfg/if/group-posixinit

# POSIX Initialization Thread Configuration

This section describes configuration options related to the POSIX
initialization thread.

% Generated from spec:/acfg/if/posix-init-thread-entry-point

```{raw} latex
\clearpage
```

```{index} CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT
```

(CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT)=

## CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_POSIX_INIT_THREAD_ENTRY_POINT`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is an initializer define.

```{eval-rst}
.. rubric:: DEFAULT VALUE:
```

The default value is `POSIX_Init`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The value of this configuration option initializes the entry point of the POSIX
API initialization thread.

```{eval-rst}
.. rubric:: NOTES:
```

The application shall provide the function referenced by this configuration
option.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The value of the configuration option shall be defined to a valid function
pointer of the type `void *( *entry_point )( void * )`.

% Generated from spec:/acfg/if/posix-init-thread-stack-size

```{raw} latex
\clearpage
```

```{index} CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE
```

(CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE)=

## CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_POSIX_INIT_THREAD_STACK_SIZE`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is an integer define.

```{eval-rst}
.. rubric:: DEFAULT VALUE:
```

The default value is {ref}`CONFIGURE_MINIMUM_POSIX_THREAD_STACK_SIZE`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The value of this configuration option defines the thread stack size of the
POSIX API initialization thread.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this configuration option:

- The value of the configuration option shall be greater than or equal to
  {ref}`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.
- The value of the configuration option shall be small enough so that the task
  stack space calculation carried out by `<rtems/confdefs.h>` does not overflow
  an integer of type
  [uintptr_t](https://en.cppreference.com/w/c/types/integer).

% Generated from spec:/acfg/if/posix-init-thread-table

```{raw} latex
\clearpage
```

```{index} CONFIGURE_POSIX_INIT_THREAD_TABLE
```

(CONFIGURE_POSIX_INIT_THREAD_TABLE)=

## CONFIGURE_POSIX_INIT_THREAD_TABLE

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_POSIX_INIT_THREAD_TABLE`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is a boolean feature define.

```{eval-rst}
.. rubric:: DEFAULT CONFIGURATION:
```

If this configuration option is undefined, then the described feature is not
enabled.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

In case this configuration option is defined, then exactly one POSIX
initialization thread is configured.

```{eval-rst}
.. rubric:: NOTES:
```

The application shall define at least one of the following configuration
options

- {ref}`CONFIGURE_RTEMS_INIT_TASKS_TABLE`,
- `CONFIGURE_POSIX_INIT_THREAD_TABLE`, or
- {ref}`CONFIGURE_IDLE_TASK_INITIALIZES_APPLICATION`

otherwise a compile time error in the configuration file will occur.

If no Classic API initialization task is configured, then the POSIX API
initialization thread performs the {ref}`GlobalConstruction`.
