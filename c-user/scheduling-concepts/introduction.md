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

% Generated from spec:/rtems/scheduler/if/group

(SchedulerManagerIntroduction)=

# Introduction

% The following list was generated from:

% spec:/rtems/scheduler/if/ident

% spec:/rtems/scheduler/if/ident-by-processor

% spec:/rtems/scheduler/if/ident-by-processor-set

% spec:/rtems/scheduler/if/get-maximum-priority

% spec:/rtems/scheduler/if/map-priority-to-posix

% spec:/rtems/scheduler/if/map-priority-from-posix

% spec:/rtems/scheduler/if/get-processor

% spec:/rtems/scheduler/if/get-processor-maximum

% spec:/rtems/scheduler/if/get-processor-set

% spec:/rtems/scheduler/if/add-processor

% spec:/rtems/scheduler/if/remove-processor

The scheduling concepts relate to the allocation of processing time for tasks.

The concept of scheduling in real-time systems dictates the ability to provide
an immediate response to specific external events, particularly the necessity
of scheduling tasks to run within a specified time limit after the occurrence
of an event. For example, software embedded in life-support systems used to
monitor hospital patients must take instant action if a change in the patient's
status is detected.

The component of RTEMS responsible for providing this capability is
appropriately called the scheduler. The scheduler's sole purpose is to allocate
the all important resource of processor time to the various tasks competing for
attention. The directives provided by the Scheduler Manager are:

- {ref}`InterfaceRtemsSchedulerIdent` - Identifies a scheduler by the object
  name.
- {ref}`InterfaceRtemsSchedulerIdentByProcessor` - Identifies a scheduler by
  the processor index.
- {ref}`InterfaceRtemsSchedulerIdentByProcessorSet` - Identifies a scheduler by
  the processor set.
- {ref}`InterfaceRtemsSchedulerGetMaximumPriority` - Gets the maximum task
  priority of the scheduler.
- {ref}`InterfaceRtemsSchedulerMapPriorityToPosix` - Maps a Classic API task
  priority to the corresponding POSIX thread priority.
- {ref}`InterfaceRtemsSchedulerMapPriorityFromPosix` - Maps a POSIX thread
  priority to the corresponding Classic API task priority.
- {ref}`InterfaceRtemsSchedulerGetProcessor` - Returns the index of the current
  processor.
- {ref}`InterfaceRtemsSchedulerGetProcessorMaximum` - Returns the processor
  maximum supported by the system.
- {ref}`InterfaceRtemsSchedulerGetProcessorSet` - Gets the set of processors
  owned by the scheduler.
- {ref}`InterfaceRtemsSchedulerAddProcessor` - Adds the processor to the set of
  processors owned by the scheduler.
- {ref}`InterfaceRtemsSchedulerRemoveProcessor` - Removes the processor from
  the set of processors owned by the scheduler.
