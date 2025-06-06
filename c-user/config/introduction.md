% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2009, 2021 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2021 On-Line Applications Research Corporation (OAR)

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

% Generated from spec:/rtems/config/if/group

(ApplicationConfigurationInformationIntroduction)=

# Introduction

% The following list was generated from:

% spec:/rtems/config/if/get-build-label

% spec:/rtems/config/if/get-copyright-notice

% spec:/rtems/config/if/get-target-hash

% spec:/rtems/config/if/get-version-string

% spec:/rtems/config/if/get-do-zero-of-workspace

% spec:/rtems/config/if/get-idle-task-stack-size

% spec:/rtems/config/if/get-idle-task

% spec:/rtems/config/if/get-interrupt-stack-size

% spec:/rtems/config/if/get-maximum-barriers

% spec:/rtems/config/if/get-maximum-extensions

% spec:/rtems/config/if/get-maximum-message-queues

% spec:/rtems/config/if/get-maximum-partitions

% spec:/rtems/config/if/get-maximum-periods

% spec:/rtems/config/if/get-maximum-ports

% spec:/rtems/config/if/get-maximum-processors

% spec:/rtems/config/if/get-maximum-regions

% spec:/rtems/config/if/get-maximum-semaphores

% spec:/rtems/config/if/get-maximum-tasks

% spec:/rtems/config/if/get-maximum-timers

% spec:/rtems/config/if/get-microseconds-per-tick

% spec:/rtems/config/if/get-milliseconds-per-tick

% spec:/rtems/config/if/get-nanoseconds-per-tick

% spec:/rtems/config/if/get-number-of-initial-extensions

% spec:/rtems/config/if/get-stack-allocate-for-idle-hook

% spec:/rtems/config/if/get-stack-allocate-hook

% spec:/rtems/config/if/get-stack-allocate-init-hook

% spec:/rtems/config/if/get-stack-allocator-avoids-work-space

% spec:/rtems/config/if/get-stack-free-hook

% spec:/rtems/config/if/get-stack-space-size

% spec:/rtems/config/if/get-ticks-per-timeslice

% spec:/rtems/config/if/get-unified-work-area

% spec:/rtems/config/if/get-user-extension-table

% spec:/rtems/config/if/get-user-multiprocessing-table

% spec:/rtems/config/if/get-work-space-size

% spec:/rtems/config/if/get-api-configuration

% spec:/rtems/config/if/resource-is-unlimited

% spec:/rtems/config/if/resource-maximum-per-allocation

% spec:/rtems/config/if/resource-unlimited

The application configuration information group provides an API to get the
configuration of an application.

RTEMS must be configured for an application. This configuration encompasses a
variety of information including the length of each clock tick, the maximum
number of each information RTEMS object that can be created, the application
initialization tasks, the task scheduling algorithm to be used, and the device
drivers in the application.

Although this information is contained in data structures that are used by
RTEMS at system initialization time, the data structures themselves must not be
generated by hand. RTEMS provides a set of macros system which provides a
simple standard mechanism to automate the generation of these structures.

The RTEMS header file `<rtems/confdefs.h>` is at the core of the automatic
generation of system configuration. It is based on the idea of setting macros
which define configuration parameters of interest to the application and
defaulting or calculating all others. This variety of macros can automatically
produce all of the configuration data required for an RTEMS application. The
term `confdefs` is shorthand for a *Configuration Defaults*.

As a general rule, application developers only specify values for the
configuration parameters of interest to them. They define what resources or
features they require. In most cases, when a parameter is not specified, it
defaults to zero (0) instances, a standards compliant value, or disabled as
appropriate. For example, by default there will be 256 task priority levels but
this can be lowered by the application. This number of priority levels is
required to be compliant with the RTEID/ORKID standards upon which the Classic
API is based. There are similar cases where the default is selected to be
compliant with the POSIX standard.

For each configuration parameter in the configuration tables, the macro
corresponding to that field is discussed. The RTEMS Maintainers expect that all
systems can be easily configured using the `<rtems/confdefs.h>` mechanism and
that using this mechanism will avoid internal RTEMS configuration changes
impacting applications.

Some application configuration settings and other system parameters can be
queried by the application. The directives provided by the Application
Configuration Information are:

- {ref}`InterfaceRtemsGetBuildLabel` - Gets the RTEMS build label.
- {ref}`InterfaceRtemsGetCopyrightNotice` - Gets the RTEMS copyright notice.
- {ref}`InterfaceRtemsGetTargetHash` - Gets the RTEMS target hash.
- {ref}`InterfaceRtemsGetVersionString` - Gets the RTEMS version string.
- {ref}`InterfaceRtemsConfigurationGetDoZeroOfWorkspace` - Indicates if the
  RTEMS Workspace is configured to be zeroed during system initialization for
  this application.
- {ref}`InterfaceRtemsConfigurationGetIdleTaskStackSize` - Gets the IDLE task
  stack size in bytes of this application.
- {ref}`InterfaceRtemsConfigurationGetIdleTask` - Gets the IDLE task body of
  this application.
- {ref}`InterfaceRtemsConfigurationGetInterruptStackSize` - Gets the interrupt
  stack size in bytes of this application.
- {ref}`InterfaceRtemsConfigurationGetMaximumBarriers` - Gets the resource
  number of {ref}`RTEMSAPIClassicBarrier` objects configured for this
  application.
- {ref}`InterfaceRtemsConfigurationGetMaximumExtensions` - Gets the resource
  number of {ref}`RTEMSAPIClassicUserExt` objects configured for this
  application.
- {ref}`InterfaceRtemsConfigurationGetMaximumMessageQueues` - Gets the resource
  number of {ref}`RTEMSAPIClassicMessage` objects configured for this
  application.
- {ref}`InterfaceRtemsConfigurationGetMaximumPartitions` - Gets the resource
  number of {ref}`RTEMSAPIClassicPart` objects configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMaximumPeriods` - Gets the resource
  number of {ref}`RTEMSAPIClassicRatemon` objects configured for this
  application.
- {ref}`InterfaceRtemsConfigurationGetMaximumPorts` - Gets the resource number
  of {ref}`RTEMSAPIClassicDPMem` objects configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMaximumProcessors` - Gets the maximum
  number of processors configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMaximumRegions` - Gets the resource
  number of {ref}`RTEMSAPIClassicRegion` objects configured for this
  application.
- {ref}`InterfaceRtemsConfigurationGetMaximumSemaphores` - Gets the resource
  number of {ref}`RTEMSAPIClassicSem` objects configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMaximumTasks` - Gets the resource number
  of {ref}`RTEMSAPIClassicTasks` objects configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMaximumTimers` - Gets the resource number
  of {ref}`RTEMSAPIClassicTimer` objects configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMicrosecondsPerTick` - Gets the number of
  microseconds per clock tick configured for this application.
- {ref}`InterfaceRtemsConfigurationGetMillisecondsPerTick` - Gets the number of
  milliseconds per clock tick configured for this application.
- {ref}`InterfaceRtemsConfigurationGetNanosecondsPerTick` - Gets the number of
  microseconds per clock tick configured for this application.
- {ref}`InterfaceRtemsConfigurationGetNumberOfInitialExtensions` - Gets the
  number of initial extensions configured for this application.
- {ref}`InterfaceRtemsConfigurationGetStackAllocateForIdleHook` - Gets the task
  stack allocator allocate hook used to allocate the stack of each {term}`IDLE task` configured for this application.
- {ref}`InterfaceRtemsConfigurationGetStackAllocateHook` - Gets the task stack
  allocator allocate hook configured for this application.
- {ref}`InterfaceRtemsConfigurationGetStackAllocateInitHook` - Gets the task
  stack allocator initialization hook configured for this application.
- {ref}`InterfaceRtemsConfigurationGetStackAllocatorAvoidsWorkSpace` -
  Indicates if the task stack allocator is configured to avoid the RTEMS
  Workspace for this application.
- {ref}`InterfaceRtemsConfigurationGetStackFreeHook` - Gets the task stack
  allocator free hook configured for this application.
- {ref}`InterfaceRtemsConfigurationGetStackSpaceSize` - Gets the configured
  size in bytes of the memory space used to allocate thread stacks for this
  application.
- {ref}`InterfaceRtemsConfigurationGetTicksPerTimeslice` - Gets the clock ticks
  per timeslice configured for this application.
- {ref}`InterfaceRtemsConfigurationGetUnifiedWorkArea` - Indicates if the RTEMS
  Workspace and C Program Heap are configured to be unified for this
  application.
- {ref}`InterfaceRtemsConfigurationGetUserExtensionTable` - Gets the initial
  extensions table configured for this application.
- {ref}`InterfaceRtemsConfigurationGetUserMultiprocessingTable` - Gets the MPCI
  configuration table configured for this application.
- {ref}`InterfaceRtemsConfigurationGetWorkSpaceSize` - Gets the RTEMS Workspace
  size in bytes configured for this application.
- {ref}`InterfaceRtemsConfigurationGetRtemsApiConfiguration` - Gets the Classic
  API Configuration Table of this application.
- {ref}`InterfaceRtemsResourceIsUnlimited` - Indicates if the resource is
  unlimited.
- {ref}`InterfaceRtemsResourceMaximumPerAllocation` - Gets the maximum number
  per allocation of a resource number.
- {ref}`InterfaceRtemsResourceUnlimited` - Augments the resource number so that
  it indicates an unlimited resource.
