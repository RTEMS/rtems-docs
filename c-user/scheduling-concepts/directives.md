% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2013, 2021 embedded brains GmbH & Co. KG
% Copyright (C) 1988, 2017 On-Line Applications Research Corporation (OAR)

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

(SchedulerManagerDirectives)=

# Directives

This section details the directives of the Scheduler Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/scheduler/if/ident

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_ident()
```

(InterfaceRtemsSchedulerIdent)=

## rtems_scheduler_ident()

Identifies a scheduler by the object name.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_ident( rtems_name name, rtems_id *id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`name`
: This parameter is the scheduler name to look up.

`id`
: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When the
  directive call is successful, the identifier of the scheduler will be stored
  in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive obtains a scheduler identifier associated with the scheduler
name specified in `name`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_NAME`
: There was no scheduler associated with the name.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

```{eval-rst}
.. rubric:: NOTES:
```

The scheduler name is determined by the scheduler configuration.

The scheduler identifier is used with other scheduler related directives to
access the scheduler.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/ident-by-processor

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_ident_by_processor()
```

(InterfaceRtemsSchedulerIdentByProcessor)=

## rtems_scheduler_ident_by_processor()

Identifies a scheduler by the processor index.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_ident_by_processor(
  uint32_t  cpu_index,
  rtems_id *id
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`cpu_index`
: This parameter is the processor index to identify the scheduler.

`id`
: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When the
  directive call is successful, the identifier of the scheduler will be stored
  in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_NAME`
: The processor index was invalid.

{c:macro}`RTEMS_INCORRECT_STATE`
: The processor index was valid, however, the corresponding processor was not
  owned by a scheduler.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/ident-by-processor-set

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_ident_by_processor_set()
```

(InterfaceRtemsSchedulerIdentByProcessorSet)=

## rtems_scheduler_ident_by_processor_set()

Identifies a scheduler by the processor set.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_ident_by_processor_set(
  size_t           cpusetsize,
  const cpu_set_t *cpuset,
  rtems_id        *id
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`cpusetsize`
: This parameter is the size of the processor set referenced by `cpuset` in
  bytes. The size shall be positive.

`cpuset`
: This parameter is the pointer to a {c:type}`cpu_set_t`. The referenced
  processor set will be used to identify the scheduler.

`id`
: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When the
  directive call is successful, the identifier of the scheduler will be stored
  in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The scheduler is selected according to the highest numbered online processor in
the specified processor set.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `cpuset` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_SIZE`
: The processor set size was invalid.

{c:macro}`RTEMS_INVALID_NAME`
: The processor set contained no online processor.

{c:macro}`RTEMS_INCORRECT_STATE`
: The processor set was valid, however, the highest numbered online processor
  in the processor set was not owned by a scheduler.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/get-maximum-priority

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_get_maximum_priority()
```

(InterfaceRtemsSchedulerGetMaximumPriority)=

## rtems_scheduler_get_maximum_priority()

Gets the maximum task priority of the scheduler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_get_maximum_priority(
  rtems_id             scheduler_id,
  rtems_task_priority *priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`scheduler_id`
: This parameter is the scheduler identifier.

`priority`
: This parameter is the pointer to an {ref}`InterfaceRtemsTaskPriority` object.
  When the directive the maximum priority of the scheduler will be stored in
  this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `priority` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/map-priority-to-posix

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_map_priority_to_posix()
```

(InterfaceRtemsSchedulerMapPriorityToPosix)=

## rtems_scheduler_map_priority_to_posix()

Maps a Classic API task priority to the corresponding POSIX thread priority.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_map_priority_to_posix(
  rtems_id            scheduler_id,
  rtems_task_priority priority,
  int                *posix_priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`scheduler_id`
: This parameter is the scheduler identifier.

`priority`
: This parameter is the Classic API task priority to map.

`posix_priority`
: This parameter is the pointer to an `int` object. When the directive call is
  successful, the POSIX thread priority value corresponding to the specified
  Classic API task priority value will be stored in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `posix_priority` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`
: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_INVALID_PRIORITY`
: The Classic API task priority was invalid.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/map-priority-from-posix

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_map_priority_from_posix()
```

(InterfaceRtemsSchedulerMapPriorityFromPosix)=

## rtems_scheduler_map_priority_from_posix()

Maps a POSIX thread priority to the corresponding Classic API task priority.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_map_priority_from_posix(
  rtems_id             scheduler_id,
  int                  posix_priority,
  rtems_task_priority *priority
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`scheduler_id`
: This parameter is the scheduler identifier.

`posix_priority`
: This parameter is the POSIX thread priority to map.

`priority`
: This parameter is the pointer to an {ref}`InterfaceRtemsTaskPriority` object.
  When the directive call is successful, the Classic API task priority value
  corresponding to the specified POSIX thread priority value will be stored in
  this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `priority` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`
: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_INVALID_PRIORITY`
: The POSIX thread priority was invalid.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/get-processor

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_get_processor()
```

(InterfaceRtemsSchedulerGetProcessor)=

## rtems_scheduler_get_processor()

Returns the index of the current processor.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
uint32_t rtems_scheduler_get_processor( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

Where the system was built with SMP support disabled, this directive evaluates
to a compile time constant of zero.

Where the system was built with SMP support enabled, this directive returns the
index of the current processor. The set of processor indices is the range of
integers starting with zero up to
{ref}`InterfaceRtemsSchedulerGetProcessorMaximum` minus one.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the index of the current processor.

```{eval-rst}
.. rubric:: NOTES:
```

Outside of sections with disabled thread dispatching the current processor
index may change after every instruction since the thread may migrate from one
processor to another. Sections with disabled interrupts are sections with
thread dispatching disabled.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/get-processor-maximum

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_get_processor_maximum()
```

(InterfaceRtemsSchedulerGetProcessorMaximum)=

## rtems_scheduler_get_processor_maximum()

Returns the processor maximum supported by the system.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
uint32_t rtems_scheduler_get_processor_maximum( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

Where the system was built with SMP support disabled, this directive evaluates
to a compile time constant of one.

Where the system was built with SMP support enabled, this directive returns the
minimum of the processors (physically or virtually) available at the
{term}`target` and the configured processor maximum (see
{ref}`CONFIGURE_MAXIMUM_PROCESSORS`). Not all processors in the range from
processor index zero to the last processor index (which is the processor
maximum minus one) may be configured to be used by a scheduler or may be online
(online processors have a scheduler assigned).

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the processor maximum supported by the system.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/get-processor-set

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_get_processor_set()
```

(InterfaceRtemsSchedulerGetProcessorSet)=

## rtems_scheduler_get_processor_set()

Gets the set of processors owned by the scheduler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_get_processor_set(
  rtems_id   scheduler_id,
  size_t     cpusetsize,
  cpu_set_t *cpuset
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`scheduler_id`
: This parameter is the scheduler identifier.

`cpusetsize`
: This parameter is the size of the processor set referenced by `cpuset` in
  bytes.

`cpuset`
: This parameter is the pointer to a {c:type}`cpu_set_t` object. When the
  directive call is successful, the processor set of the scheduler will be
  stored in this object. A set bit in the processor set means that the
  corresponding processor is owned by the scheduler, otherwise the bit is
  cleared.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `cpuset` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`
: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_INVALID_SIZE`
: The provided processor set was too small for the set of processors owned by
  the scheduler.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/add-processor

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_add_processor()
```

(InterfaceRtemsSchedulerAddProcessor)=

## rtems_scheduler_add_processor()

Adds the processor to the set of processors owned by the scheduler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_add_processor(
  rtems_id scheduler_id,
  uint32_t cpu_index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`scheduler_id`
: This parameter is the scheduler identifier.

`cpu_index`
: This parameter is the index of the processor to add.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive adds the processor specified by the `cpu_index` to the scheduler
specified by `scheduler_id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_NOT_CONFIGURED`
: The processor was not configured to be used by the application.

{c:macro}`RTEMS_INCORRECT_STATE`
: The processor was configured to be used by the application, however, it was
  not online.

{c:macro}`RTEMS_RESOURCE_IN_USE`
: The processor was already assigned to a scheduler.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/scheduler/if/remove-processor

```{raw} latex
\clearpage
```

```{index} rtems_scheduler_remove_processor()
```

(InterfaceRtemsSchedulerRemoveProcessor)=

## rtems_scheduler_remove_processor()

Removes the processor from the set of processors owned by the scheduler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_scheduler_remove_processor(
  rtems_id scheduler_id,
  uint32_t cpu_index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`scheduler_id`
: This parameter is the scheduler identifier.

`cpu_index`
: This parameter is the index of the processor to remove.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive removes the processor specified by the `cpu_index` from the
scheduler specified by `scheduler_id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no scheduler associated with the identifier specified by
  `scheduler_id`.

{c:macro}`RTEMS_INVALID_NUMBER`
: The processor was not owned by the scheduler.

{c:macro}`RTEMS_RESOURCE_IN_USE`
: The processor was required by at least one non-idle task that used the
  scheduler as its {term}`home scheduler`.

{c:macro}`RTEMS_RESOURCE_IN_USE`
: The processor was the last processor owned by the scheduler and there was at
  least one task that used the scheduler as a {term}`helping scheduler`.

```{eval-rst}
.. rubric:: NOTES:
```

Removing a processor from a scheduler is a complex operation that involves all
tasks of the system.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
