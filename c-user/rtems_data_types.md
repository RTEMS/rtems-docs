% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2008, 2024 embedded brains GmbH & Co. KG

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

```{index} RTEMS Data Types
```

```{index} data types
```

# RTEMS Data Types

(Introduction)=

## Introduction

This chapter contains a complete list of the RTEMS primitive data types in
alphabetical order. This is intended to be an overview and the user is
encouraged to look at the appropriate chapters in the manual for more
information about the usage of the various data types.

(ListOfDataTypes)=

## List of Data Types

The following is a complete list of the RTEMS primitive data types in
alphabetical order:

% Generated from spec:/rtems/io/if/bsp-output-char-function-type

```{index} BSP_output_char_function_type
```

(InterfaceBSPOutputCharFunctionType)=

### BSP_output_char_function_type

Polled character output functions shall have this type.

% Generated from spec:/rtems/io/if/bsp-polling-getchar-function-type

```{index} BSP_polling_getchar_function_type
```

(InterfaceBSPPollingGetcharFunctionType)=

### BSP_polling_getchar_function_type

Polled character input functions shall have this type.

% Generated from spec:/rtems/timer/if/classes

```{index} Timer_Classes
```

(InterfaceTimerClasses)=

### Timer_Classes

The timer class indicates how the timer was most recently fired.

```{eval-rst}
.. rubric:: ENUMERATORS:
```

TIMER_DORMANT
: This timer class indicates that the timer was never in use.

TIMER_INTERVAL
: This timer class indicates that the timer is currently in use as an
  interval timer which will fire in the context of the clock tick
  {term}`ISR`.

TIMER_INTERVAL_ON_TASK
: This timer class indicates that the timer is currently in use as an
  interval timer which will fire in the context of the Timer Server task.

TIMER_TIME_OF_DAY
: This timer class indicates that the timer is currently in use as an time of
  day timer which will fire in the context of the clock tick {term}`ISR`.

TIMER_TIME_OF_DAY_ON_TASK
: This timer class indicates that the timer is currently in use as an time of
  day timer which will fire in the context of the Timer Server task.

% Generated from spec:/rtems/config/if/api-table

```{index} rtems_api_configuration_table
```

(InterfaceRtemsApiConfigurationTable)=

### rtems_api_configuration_table

This structure contains a summary of the Classic API configuration.

```{eval-rst}
.. rubric:: MEMBERS:
```

maximum_tasks
: This member contains the maximum number of Classic API Tasks configured for
  this application. See {ref}`CONFIGURE_MAXIMUM_TASKS`.

notepads_enabled
: This member is true, if the Classic API Notepads are enabled, otherwise it
  is false.

maximum_timers
: This member contains the maximum number of Classic API Timers configured
  for this application. See {ref}`CONFIGURE_MAXIMUM_TIMERS`.

maximum_semaphores
: This member contains the maximum number of Classic API Semaphores
  configured for this application. See {ref}`CONFIGURE_MAXIMUM_SEMAPHORES`.

maximum_message_queues
: This member contains the maximum number of Classic API Message Queues
  configured for this application. See
  {ref}`CONFIGURE_MAXIMUM_MESSAGE_QUEUES`.

maximum_partitions
: This member contains the maximum number of Classic API Partitions
  configured for this application. See {ref}`CONFIGURE_MAXIMUM_PARTITIONS`.

maximum_regions
: This member contains the maximum number of Classic API Regions configured
  for this application. See {ref}`CONFIGURE_MAXIMUM_REGIONS`.

maximum_ports
: This member contains the maximum number of Classic API Dual-Ported Memories
  configured for this application. See {ref}`CONFIGURE_MAXIMUM_PORTS`.

maximum_periods
: This member contains the maximum number of Classic API Rate Monotonic
  Periods configured for this application. See
  {ref}`CONFIGURE_MAXIMUM_PERIODS`.

maximum_barriers
: This member contains the maximum number of Classic API Barriers configured
  for this application. See {ref}`CONFIGURE_MAXIMUM_BARRIERS`.

number_of_initialization_tasks
: This member contains the number of Classic API Initialization Tasks
  configured for this application. See
  {ref}`CONFIGURE_RTEMS_INIT_TASKS_TABLE`.

User_initialization_tasks_table
: This member contains the pointer to Classic API Initialization Tasks Table
  of this application. See {ref}`CONFIGURE_RTEMS_INIT_TASKS_TABLE`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

Use {ref}`InterfaceRtemsConfigurationGetRtemsApiConfiguration` to get the
configuration table.

% Generated from spec:/rtems/signal/if/asr

```{index} rtems_asr
```

(InterfaceRtemsAsr)=

### rtems_asr

This type defines the return type of routines which are used to process
asynchronous signals.

```{eval-rst}
.. rubric:: NOTES:
```

This type can be used to document asynchronous signal routines in the source
code.

% Generated from spec:/rtems/signal/if/asr-entry

```{index} rtems_asr_entry
```

(InterfaceRtemsAsrEntry)=

### rtems_asr_entry

This type defines the prototype of routines which are used to process
asynchronous signals.

% Generated from spec:/rtems/fatal/if/assert-context

```{index} rtems_assert_context
```

(InterfaceRtemsAssertContext)=

### rtems_assert_context

This structure provides the context in which an assertion failed.

```{eval-rst}
.. rubric:: MEMBERS:
```

file
: This member provides the file name of the source code file containing the
  failed assertion statement.

line
: This member provides the line number in the source code file containing the
  failed assertion statement.

function
: This member provides the function name containing the failed assertion
  statement.

failed_expression
: This member provides the expression of the failed assertion statement.

% Generated from spec:/rtems/attr/if/attribute

```{index} rtems_attribute
```

(InterfaceRtemsAttribute)=

### rtems_attribute

This type represents Classic API attributes.

```{eval-rst}
.. rubric:: NOTES:
```

Attributes are primarily used when creating objects.

% Generated from spec:/rtems/io/if/device-driver

```{index} rtems_device_driver
```

(InterfaceRtemsDeviceDriver)=

### rtems_device_driver

This type shall be used in device driver entry declarations and definitions.

```{eval-rst}
.. rubric:: NOTES:
```

Device driver entries return an {c:type}`rtems_status_code` status code. This
type definition helps to document device driver entries in the source code.

% Generated from spec:/rtems/io/if/device-driver-entry

```{index} rtems_device_driver_entry
```

(InterfaceRtemsDeviceDriverEntry)=

### rtems_device_driver_entry

Device driver entries shall have this type.

% Generated from spec:/rtems/io/if/device-major-number

```{index} rtems_device_major_number
```

(InterfaceRtemsDeviceMajorNumber)=

### rtems_device_major_number

This integer type represents the major number of devices.

```{eval-rst}
.. rubric:: NOTES:
```

The major number of a device is determined by
{ref}`InterfaceRtemsIoRegisterDriver` and the application configuration (see
{ref}`CONFIGURE_MAXIMUM_DRIVERS`) .

% Generated from spec:/rtems/io/if/device-minor-number

```{index} rtems_device_minor_number
```

(InterfaceRtemsDeviceMinorNumber)=

### rtems_device_minor_number

This integer type represents the minor number of devices.

```{eval-rst}
.. rubric:: NOTES:
```

The minor number of devices is managed by the device driver.

% Generated from spec:/rtems/io/if/driver-address-table

```{index} rtems_driver_address_table
```

(InterfaceRtemsDriverAddressTable)=

### rtems_driver_address_table

This structure contains the device driver entries.

```{eval-rst}
.. rubric:: MEMBERS:
```

initialization_entry
: This member is the device driver initialization entry. This entry is called
  by {ref}`InterfaceRtemsIoInitialize`.

open_entry
: This member is the device driver open entry. This entry is called by
  {ref}`InterfaceRtemsIoOpen`.

close_entry
: This member is the device driver close entry. This entry is called by
  {ref}`InterfaceRtemsIoClose`.

read_entry
: This member is the device driver read entry. This entry is called by
  {ref}`InterfaceRtemsIoRead`.

write_entry
: This member is the device driver write entry. This entry is called by
  {ref}`InterfaceRtemsIoWrite`.

control_entry
: This member is the device driver control entry. This entry is called by
  {ref}`InterfaceRtemsIoControl`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This structure is used to register a device driver via
{ref}`InterfaceRtemsIoRegisterDriver`.

% Generated from spec:/rtems/event/if/set

```{index} rtems_event_set
```

(InterfaceRtemsEventSet)=

### rtems_event_set

This integer type represents a bit field which can hold exactly 32 individual
events.

% Generated from spec:/rtems/fatal/if/exception-frame

```{index} rtems_exception_frame
```

(InterfaceRtemsExceptionFrame)=

### rtems_exception_frame

This structure represents an architecture-dependent exception frame.

% Generated from spec:/rtems/userext/if/table

```{index} rtems_extensions_table
```

(InterfaceRtemsExtensionsTable)=

### rtems_extensions_table

The extensions table contains a set of extensions which may be registered in
the system through the {ref}`CONFIGURE_INITIAL_EXTENSIONS` application
configuration option or the {ref}`InterfaceRtemsExtensionCreate` directive.

% Generated from spec:/rtems/userext/if/fatal-code

```{index} rtems_fatal_code
```

(InterfaceRtemsFatalCode)=

### rtems_fatal_code

This integer type represents system termination codes.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This integer type is large enough to store a 32-bit integer or a pointer.

```{eval-rst}
.. rubric:: NOTES:
```

The interpretation of a system termination code depends on the system
termination source, see {ref}`InterfaceRtemsFatalSource`.

% Generated from spec:/rtems/userext/if/fatal

```{index} rtems_fatal_extension
```

(InterfaceRtemsFatalExtension)=

### rtems_fatal_extension

Fatal extensions are invoked when the system should terminate.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`source`
: This parameter is the system termination source. The source indicates the
  component which caused the system termination request, see
  {ref}`InterfaceRtemsFatalSource`. The system termination code may provide
  additional information related to the system termination request.

`always_set_to_false`
: This parameter is a value equal to {c:macro}`false`.

`code`
: This parameter is the system termination code. This value must be
  interpreted with respect to the source.

```{eval-rst}
.. rubric:: NOTES:
```

The fatal extensions are invoked in {term}`extension forward order` and with
maskable interrupts disabled.

The fatal extension should be extremely careful with respect to the RTEMS
directives it calls. Depending on the system termination source, the system
may be in an undefined and corrupt state.

It is recommended to register fatal extensions through {term}`initial extension sets`, see {ref}`CONFIGURE_INITIAL_EXTENSIONS`.

% Generated from spec:/rtems/userext/if/fatal-source

```{index} rtems_fatal_source
```

(InterfaceRtemsFatalSource)=

### rtems_fatal_source

This enumeration represents system termination sources.

```{eval-rst}
.. rubric:: NOTES:
```

The system termination code may provide additional information depending on the
system termination source, see {ref}`InterfaceRtemsFatalCode`.

% Generated from spec:/rtems/type/if/id

```{index} rtems_id
```

(InterfaceRtemsId)=

### rtems_id

This type represents RTEMS object identifiers.

% Generated from spec:/rtems/task/if/initialization-table

```{index} rtems_initialization_tasks_table
```

(InterfaceRtemsInitializationTasksTable)=

### rtems_initialization_tasks_table

This structure defines the properties of the Classic API user initialization
task.

```{eval-rst}
.. rubric:: MEMBERS:
```

name
: This member defines the task name.

stack_size
: This member defines the task stack size in bytes.

initial_priority
: This member defines the initial task priority.

attribute_set
: This member defines the attribute set of the task.

entry_point
: This member defines the entry point of the task.

mode_set
: This member defines the initial modes of the task.

argument
: This member defines the entry point argument of the task.

% Generated from spec:/rtems/intr/if/attributes

```{index} rtems_interrupt_attributes
```

(InterfaceRtemsInterruptAttributes)=

### rtems_interrupt_attributes

This structure provides the attributes of an interrupt vector.

```{eval-rst}
.. rubric:: MEMBERS:
```

is_maskable
: This member is true, if the interrupt vector is maskable by
  {ref}`InterfaceRtemsInterruptLocalDisable`, otherwise it is false.
  Interrupt vectors which are not maskable by
  {ref}`InterfaceRtemsInterruptLocalDisable` should be used with care since
  they cannot use most operating system services.

can_enable
: This member is true, if the interrupt vector can be enabled by
  {ref}`InterfaceRtemsInterruptVectorEnable`, otherwise it is false. When an
  interrupt vector can be enabled, this means that the enabled state can
  always be changed from disabled to enabled. For an interrupt vector which
  can be enabled it follows that it may be enabled.

maybe_enable
: This member is true, if the interrupt vector may be enabled by
  {ref}`InterfaceRtemsInterruptVectorEnable`, otherwise it is false. When an
  interrupt vector may be enabled, this means that the enabled state may be
  changed from disabled to enabled. The requested enabled state change
  should be checked by {ref}`InterfaceRtemsInterruptVectorIsEnabled`. Some
  interrupt vectors may be optionally available and cannot be enabled on a
  particular {term}`target`.

can_disable
: This member is true, if the interrupt vector can be disabled by
  {ref}`InterfaceRtemsInterruptVectorDisable`, otherwise it is false. When an
  interrupt vector can be disabled, this means that the enabled state can be
  changed from enabled to disabled. For an interrupt vector which can be
  disabled it follows that it may be disabled.

maybe_disable
: This member is true, if the interrupt vector may be disabled by
  {ref}`InterfaceRtemsInterruptVectorDisable`, otherwise it is false. When an
  interrupt vector may be disabled, this means that the enabled state may be
  changed from enabled to disabled. The requested enabled state change
  should be checked by {ref}`InterfaceRtemsInterruptVectorIsEnabled`. Some
  interrupt vectors may be always enabled and cannot be disabled on a
  particular {term}`target`.

can_raise
: This member is true, if the interrupt vector can be raised by
  {ref}`InterfaceRtemsInterruptRaise`, otherwise it is false.

can_raise_on
: This member is true, if the interrupt vector can be raised on a processor
  by {ref}`InterfaceRtemsInterruptRaiseOn`, otherwise it is false.

can_clear
: This member is true, if the interrupt vector can be cleared by
  {ref}`InterfaceRtemsInterruptClear`, otherwise it is false.

cleared_by_acknowledge
: This member is true, if the pending status of the interrupt associated with
  the interrupt vector is cleared by an interrupt acknowledge from the
  processor, otherwise it is false.

can_get_affinity
: This member is true, if the affinity set of the interrupt vector can be
  obtained by {ref}`InterfaceRtemsInterruptGetAffinity`, otherwise it is
  false.

can_set_affinity
: This member is true, if the affinity set of the interrupt vector can be set
  by {ref}`InterfaceRtemsInterruptSetAffinity`, otherwise it is false.

can_be_triggered_by_message
: This member is true, if the interrupt associated with the interrupt vector
  can be triggered by a message. Interrupts may be also triggered by signals,
  {ref}`InterfaceRtemsInterruptRaise`, or
  {ref}`InterfaceRtemsInterruptRaiseOn`. Examples for message triggered
  interrupts are the PCIe MSI/MSI-X and the ARM GICv3 Locality-specific
  Peripheral Interrupts (LPI).

trigger_signal
: This member describes the trigger signal of the interrupt associated with
  the interrupt vector. Interrupts are normally triggered by signals which
  indicate an interrupt request from a peripheral. Interrupts may be also
  triggered by messages, {ref}`InterfaceRtemsInterruptRaise`, or
  {ref}`InterfaceRtemsInterruptRaiseOn`.

can_get_priority
: This member is true, if the priority of the interrupt vector can be
  obtained by {ref}`InterfaceRtemsInterruptGetPriority`, otherwise it is
  false.

can_set_priority
: This member is true, if the priority of the interrupt vector can be set by
  {ref}`InterfaceRtemsInterruptSetPriority`, otherwise it is false.

maximum_priority
: This member represents the maximum priority value of the interrupt vector.
  By convention, the minimum priority value is zero. Lower priority values
  shall be associated with a higher importance. The higher the priority
  value, the less important is the service of the associated interrupt
  vector. Where nested interrupts are supported, interrupts with a lower
  priority value may preempt other interrupts having a higher priority value.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The {ref}`InterfaceRtemsInterruptGetAttributes` directive may be used to obtain
the attributes of an interrupt vector.

% Generated from spec:/rtems/intr/if/entry

```{index} rtems_interrupt_entry
```

(InterfaceRtemsInterruptEntry)=

### rtems_interrupt_entry

This structure represents an interrupt entry.

```{eval-rst}
.. rubric:: MEMBERS:
```

Members of the type shall not be accessed directly by the application.

```{eval-rst}
.. rubric:: NOTES:
```

This structure shall be treated as an opaque data type from the {term}`API`
point of view. Members shall not be accessed directly. An entry may be
initialized by {ref}`InterfaceRTEMSINTERRUPTENTRYINITIALIZER` or
{ref}`InterfaceRtemsInterruptEntryInitialize`. It may be installed for an
interrupt vector with {ref}`InterfaceRtemsInterruptEntryInstall` and removed
from an interrupt vector by {ref}`InterfaceRtemsInterruptEntryRemove`.

% Generated from spec:/rtems/intr/if/handler

```{index} rtems_interrupt_handler
```

(InterfaceRtemsInterruptHandler)=

### rtems_interrupt_handler

Interrupt handler routines shall have this type.

% Generated from spec:/rtems/intr/if/level

```{index} rtems_interrupt_level
```

(InterfaceRtemsInterruptLevel)=

### rtems_interrupt_level

This integer type represents interrupt levels.

% Generated from spec:/rtems/intr/if/lock

```{index} rtems_interrupt_lock
```

(InterfaceRtemsInterruptLock)=

### rtems_interrupt_lock

This structure represents an ISR lock.

```{eval-rst}
.. rubric:: NOTES:
```

Lock objects are only needed in some RTEMS build configurations, for example
where the SMP support is enabled. The
{c:macro}`RTEMS_INTERRUPT_LOCK_NEEDS_OBJECT` constant can be used to determine
whether a lock object is needed or not. This may help to reduce the memory
demands of an application. All lock operations do not use the lock object
parameter if lock objects are not needed.

```{code-block} c
---
linenos: true
---
#include <rtems.h>

#if RTEMS_INTERRUPT_LOCK_NEEDS_OBJECT
rtems_interrupt_lock lock = RTEMS_INTERRUPT_LOCK_INITIALIZER( "name" );
#endif

struct s {
#if RTEMS_INTERRUPT_LOCK_NEEDS_OBJECT
  rtems_interrupt_lock lock;
#endif
  int foobar;
};
```

% Generated from spec:/rtems/intr/if/lock-context

```{index} rtems_interrupt_lock_context
```

(InterfaceRtemsInterruptLockContext)=

### rtems_interrupt_lock_context

This structure provides an ISR lock context for acquire and release pairs.

% Generated from spec:/rtems/intr/if/per-handler-routine

```{index} rtems_interrupt_per_handler_routine
```

(InterfaceRtemsInterruptPerHandlerRoutine)=

### rtems_interrupt_per_handler_routine

Visitor routines invoked by {ref}`InterfaceRtemsInterruptHandlerIterate` shall
have this type.

% Generated from spec:/rtems/intr/if/server-action

```{index} rtems_interrupt_server_action
```

(InterfaceRtemsInterruptServerAction)=

### rtems_interrupt_server_action

This structure represents an interrupt server action.

```{eval-rst}
.. rubric:: MEMBERS:
```

Members of the type shall not be accessed directly by the application.

```{eval-rst}
.. rubric:: NOTES:
```

This structure shall be treated as an opaque data type from the {term}`API`
point of view. Members shall not be accessed directly.

% Generated from spec:/rtems/intr/if/server-config

```{index} rtems_interrupt_server_config
```

(InterfaceRtemsInterruptServerConfig)=

### rtems_interrupt_server_config

This structure defines an interrupt server configuration.

```{eval-rst}
.. rubric:: MEMBERS:
```

Members of the type shall not be accessed directly by the application.

```{eval-rst}
.. rubric:: NOTES:
```

See also {ref}`InterfaceRtemsInterruptServerCreate`.

% Generated from spec:/rtems/intr/if/server-control

```{index} rtems_interrupt_server_control
```

(InterfaceRtemsInterruptServerControl)=

### rtems_interrupt_server_control

This structure represents an interrupt server.

```{eval-rst}
.. rubric:: MEMBERS:
```

Members of the type shall not be accessed directly by the application.

```{eval-rst}
.. rubric:: NOTES:
```

This structure shall be treated as an opaque data type from the {term}`API`
point of view. Members shall not be accessed directly. The structure is
initialized by {ref}`InterfaceRtemsInterruptServerCreate` and maintained by the
interrupt server support.

% Generated from spec:/rtems/intr/if/server-entry

```{index} rtems_interrupt_server_entry
```

(InterfaceRtemsInterruptServerEntry)=

### rtems_interrupt_server_entry

This structure represents an interrupt server entry.

```{eval-rst}
.. rubric:: MEMBERS:
```

Members of the type shall not be accessed directly by the application.

```{eval-rst}
.. rubric:: NOTES:
```

This structure shall be treated as an opaque data type from the {term}`API`
point of view. Members shall not be accessed directly. An entry is
initialized by {ref}`InterfaceRtemsInterruptServerEntryInitialize` and
destroyed by {ref}`InterfaceRtemsInterruptServerEntryDestroy`. Interrupt
server actions can be prepended to the entry by
{ref}`InterfaceRtemsInterruptServerActionPrepend`. The entry is submitted to
be serviced by {ref}`InterfaceRtemsInterruptServerEntrySubmit`.

% Generated from spec:/rtems/intr/if/server-request

```{index} rtems_interrupt_server_request
```

(InterfaceRtemsInterruptServerRequest)=

### rtems_interrupt_server_request

This structure represents an interrupt server request.

```{eval-rst}
.. rubric:: MEMBERS:
```

Members of the type shall not be accessed directly by the application.

```{eval-rst}
.. rubric:: NOTES:
```

This structure shall be treated as an opaque data type from the {term}`API`
point of view. Members shall not be accessed directly. A request is
initialized by {ref}`InterfaceRtemsInterruptServerRequestInitialize` and
destroyed by {ref}`InterfaceRtemsInterruptServerRequestDestroy`. The interrupt
vector of the request can be set by
{ref}`InterfaceRtemsInterruptServerRequestSetVector`. The request is submitted
to be serviced by {ref}`InterfaceRtemsInterruptServerRequestSubmit`.

% Generated from spec:/rtems/intr/if/signal-variant

```{index} rtems_interrupt_signal_variant
```

(InterfaceRtemsInterruptSignalVariant)=

### rtems_interrupt_signal_variant

This enumeration provides interrupt trigger signal variants.

```{eval-rst}
.. rubric:: ENUMERATORS:
```

RTEMS_INTERRUPT_UNSPECIFIED_SIGNAL
: This interrupt signal variant indicates that the interrupt trigger signal
  is unspecified.

RTEMS_INTERRUPT_NO_SIGNAL
: This interrupt signal variant indicates that the interrupt cannot be
  triggered by a signal.

RTEMS_INTERRUPT_SIGNAL_LEVEL_LOW
: This interrupt signal variant indicates that the interrupt is triggered by
  a low level signal.

RTEMS_INTERRUPT_SIGNAL_LEVEL_HIGH
: This interrupt signal variant indicates that the interrupt is triggered by
  a high level signal.

RTEMS_INTERRUPT_SIGNAL_EDGE_FALLING
: This interrupt signal variant indicates that the interrupt is triggered by
  a falling edge signal.

RTEMS_INTERRUPT_SIGNAL_EDGE_RAISING
: This interrupt signal variant indicates that the interrupt is triggered by
  a raising edge signal.

% Generated from spec:/rtems/type/if/interval

```{index} rtems_interval
```

(InterfaceRtemsInterval)=

### rtems_interval

This type represents clock tick intervals.

% Generated from spec:/rtems/intr/if/isr

```{index} rtems_isr
```

(InterfaceRtemsIsr)=

### rtems_isr

This type defines the return type of interrupt service routines.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This type can be used to document interrupt service routines in the source
code.

% Generated from spec:/rtems/intr/if/isr-entry

```{index} rtems_isr_entry
```

(InterfaceRtemsIsrEntry)=

### rtems_isr_entry

Interrupt service routines installed by {ref}`InterfaceRtemsInterruptCatch`
shall have this type.

% Generated from spec:/rtems/message/if/config

```{index} rtems_message_queue_config
```

(InterfaceRtemsMessageQueueConfig)=

### rtems_message_queue_config

This structure defines the configuration of a message queue constructed by
{ref}`InterfaceRtemsMessageQueueConstruct`.

```{eval-rst}
.. rubric:: MEMBERS:
```

name
: This member defines the name of the message queue.

maximum_pending_messages
: This member defines the maximum number of pending messages supported by the
  message queue.

maximum_message_size
: This member defines the maximum message size supported by the message
  queue.

storage_area
: This member shall point to the message buffer storage area begin. The
  message buffer storage area for the message queue shall be an array of the
  type defined by {ref}`InterfaceRTEMSMESSAGEQUEUEBUFFER` with a maximum
  message size equal to the maximum message size of this configuration.

storage_size
: This member defines size of the message buffer storage area in bytes.

storage_free
: This member defines the optional handler to free the message buffer storage
  area. It is called when the message queue is deleted. It is called from
  task context under protection of the object allocator lock. It is allowed
  to call {c:func}`free` in this handler. If handler is [NULL](https://en.cppreference.com/w/c/types/NULL), then no action will be
  performed.

attributes
: This member defines the attributes of the message queue.

% Generated from spec:/rtems/mode/if/mode

```{index} rtems_mode
```

(InterfaceRtemsMode)=

### rtems_mode

This type represents a Classic API task mode set.

% Generated from spec:/rtems/type/if/mp-packet-classes

```{index} rtems_mp_packet_classes
```

(InterfaceRtemsMpPacketClasses)=

### rtems_mp_packet_classes

This enumeration defines the MPCI packet classes.

% Generated from spec:/rtems/type/if/mpci-entry

```{index} rtems_mpci_entry
```

(InterfaceRtemsMpciEntry)=

### rtems_mpci_entry

MPCI handler routines shall have this return type.

% Generated from spec:/rtems/type/if/mpci-get-packet-entry

```{index} rtems_mpci_get_packet_entry
```

(InterfaceRtemsMpciGetPacketEntry)=

### rtems_mpci_get_packet_entry

MPCI get packet routines shall have this type.

% Generated from spec:/rtems/type/if/mpci-initialization-entry

```{index} rtems_mpci_initialization_entry
```

(InterfaceRtemsMpciInitializationEntry)=

### rtems_mpci_initialization_entry

MPCI initialization routines shall have this type.

% Generated from spec:/rtems/type/if/mpci-receive-packet-entry

```{index} rtems_mpci_receive_packet_entry
```

(InterfaceRtemsMpciReceivePacketEntry)=

### rtems_mpci_receive_packet_entry

MPCI receive packet routines shall have this type.

% Generated from spec:/rtems/type/if/mpci-return-packet-entry

```{index} rtems_mpci_return_packet_entry
```

(InterfaceRtemsMpciReturnPacketEntry)=

### rtems_mpci_return_packet_entry

MPCI return packet routines shall have this type.

% Generated from spec:/rtems/type/if/mpci-send-packet-entry

```{index} rtems_mpci_send_packet_entry
```

(InterfaceRtemsMpciSendPacketEntry)=

### rtems_mpci_send_packet_entry

MPCI send packet routines shall have this type.

% Generated from spec:/rtems/type/if/mpci-table

```{index} rtems_mpci_table
```

(InterfaceRtemsMpciTable)=

### rtems_mpci_table

This type represents the user-provided MPCI control.

% Generated from spec:/rtems/type/if/multiprocessing-table

```{index} rtems_multiprocessing_table
```

(InterfaceRtemsMultiprocessingTable)=

### rtems_multiprocessing_table

This type represents the user-provided MPCI configuration.

% Generated from spec:/rtems/type/if/name

```{index} rtems_name
```

(InterfaceRtemsName)=

### rtems_name

This type represents Classic API object names.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

It is an unsigned 32-bit integer which can be treated as a numeric value or
initialized using {ref}`InterfaceRtemsBuildName` to encode four ASCII
characters. A value of zero may have a special meaning in some directives.

% Generated from spec:/rtems/object/if/api-class-information

```{index} rtems_object_api_class_information
```

(InterfaceRtemsObjectApiClassInformation)=

### rtems_object_api_class_information

This structure is used to return information to the application about the
objects configured for a specific API/Class combination.

```{eval-rst}
.. rubric:: MEMBERS:
```

minimum_id
: This member contains the minimum valid object identifier for this class.

maximum_id
: This member contains the maximum valid object identifier for this class.

maximum
: This member contains the maximum number of active objects configured for
  this class.

auto_extend
: This member is true, if this class is configured for automatic object
  extension, otherwise it is false.

unallocated
: This member contains the number of currently inactive objects of this
  class.

% Generated from spec:/rtems/option/if/option

```{index} rtems_option
```

(InterfaceRtemsOption)=

### rtems_option

This type represents a Classic API directive option set.

% Generated from spec:/rtems/type/if/packet-prefix

```{index} rtems_packet_prefix
```

(InterfaceRtemsPacketPrefix)=

### rtems_packet_prefix

This type represents the prefix found at the beginning of each MPCI packet sent
between nodes.

% Generated from spec:/rtems/ratemon/if/period-states

```{index} rtems_rate_monotonic_period_states
```

(InterfaceRtemsRateMonotonicPeriodStates)=

### rtems_rate_monotonic_period_states

This enumeration defines the states in which a period may be.

```{eval-rst}
.. rubric:: ENUMERATORS:
```

RATE_MONOTONIC_INACTIVE
: This status indicates the period is off the watchdog chain, and has never
  been initialized.

RATE_MONOTONIC_ACTIVE
: This status indicates the period is on the watchdog chain, and running.
  The owner may be executing or blocked waiting on another object.

RATE_MONOTONIC_EXPIRED
: This status indicates the period is off the watchdog chain, and has
  expired. The owner may still execute and has taken too much time to
  complete this iteration of the period.

% Generated from spec:/rtems/ratemon/if/period-statistics

```{index} rtems_rate_monotonic_period_statistics
```

(InterfaceRtemsRateMonotonicPeriodStatistics)=

### rtems_rate_monotonic_period_statistics

This structure provides the statistics of a period.

```{eval-rst}
.. rubric:: MEMBERS:
```

count
: This member contains the number of periods executed.

missed_count
: This member contains the number of periods missed.

min_cpu_time
: This member contains the least amount of processor time used in a period.

max_cpu_time
: This member contains the highest amount of processor time used in a period.

total_cpu_time
: This member contains the total amount of processor time used in a period.

min_wall_time
: This member contains the least amount of {term}`CLOCK_MONOTONIC` time used
  in a period.

max_wall_time
: This member contains the highest amount of {term}`CLOCK_MONOTONIC` time
  used in a period.

total_wall_time
: This member contains the total amount of {term}`CLOCK_MONOTONIC` time used
  in a period.

% Generated from spec:/rtems/ratemon/if/period-status

```{index} rtems_rate_monotonic_period_status
```

(InterfaceRtemsRateMonotonicPeriodStatus)=

### rtems_rate_monotonic_period_status

This structure provides the detailed status of a period.

```{eval-rst}
.. rubric:: MEMBERS:
```

owner
: This member contains the identifier of the owner task of the period.

state
: This member contains the state of the period.

since_last_period
: This member contains the time elapsed since the last successful invocation
  {ref}`InterfaceRtemsRateMonotonicPeriod` using {term}`CLOCK_MONOTONIC`. If
  the period is expired or has not been initiated, then this value has no
  meaning.

executed_since_last_period
: This member contains the processor time consumed by the owner task since
  the last successful invocation {ref}`InterfaceRtemsRateMonotonicPeriod`. If
  the period is expired or has not been initiated, then this value has no
  meaning.

postponed_jobs_count
: This member contains the count of jobs which are not released yet.

% Handwritten

```{index} rtems_regulator_attributes
```

(InterfaceRtemsRegulatorAttributes)=

### rtems_regulator_attributes

This structure defines the configuration of a regulator created by
{ref}`InterfaceRtemsRegulatorCreate`.

```{eval-rst}
.. rubric:: MEMBERS:
```

deliverer
: This member contains a pointer to an application function invoked by
  the Delivery thread to output a message to the destination.

deliverer_context
: This member contains a pointer to an application defined context which
  is passed to delivery function.

maximum_message_size
: This member contains the maximum size message to process.

maximum_messages
: This member contains the maximum number of messages to be able to buffer.

output_thread_priority
: This member contains the priority of output thread.

output_thread_stack_size
: This member contains the Stack size of output thread.

output_thread_period
: This member contains the period (in ticks) of output thread.

maximum_to_dequeue_per_period
: This member contains the maximum number of messages the output thread
  should dequeue and deliver per period.

```{eval-rst}
.. rubric:: NOTES:
```

This type is passed as an argument to {ref}`InterfaceRtemsRegulatorCreate`.

% Handwritten

```{index} rtems_regulator_deliverer
```

(InterfaceRtemsRegulatorDeliverer)=

### rtems_regulator_deliverer

This type represents the function signature used to specify a delivery
function for the RTEMS Regulator.

```{eval-rst}
.. rubric:: NOTES:
```

This type is used in the {ref}`InterfaceRtemsRegulatorAttributes`
structure which is passed as an argument to
{ref}`InterfaceRtemsRegulatorCreate`.

% Handwritten

```{index} rtems_regulator_statistics
```

(InterfaceRtemsRegulatorStatistics)=

### rtems_regulator_statistics

This structure defines the statistics maintained by each Regulator instance.

```{eval-rst}
.. rubric:: MEMBERS:
```

obtained
: This member contains the number of successfully obtained buffers.

released
: This member contains the number of successfully released buffers.

delivered
: This member contains the number of successfully delivered buffers.

period_statistics
: This member contains the Rate Monotonic Period
  statistics for the Delivery Thread. It is an instance of the
  {ref}`InterfaceRtemsRateMonotonicPeriodStatistics` structure.

```{eval-rst}
.. rubric:: NOTES:
```

This type is passed as an argument to
{ref}`InterfaceRtemsRegulatorGetStatistics`.

% Generated from spec:/rtems/signal/if/set

```{index} rtems_signal_set
```

(InterfaceRtemsSignalSet)=

### rtems_signal_set

This integer type represents a bit field which can hold exactly 32 individual
signals.

% Generated from spec:/rtems/config/if/stack-allocate-hook

```{index} rtems_stack_allocate_hook
```

(InterfaceRtemsStackAllocateHook)=

### rtems_stack_allocate_hook

A thread stack allocator allocate handler shall have this type.

% Generated from spec:/rtems/config/if/stack-allocate-init-hook

```{index} rtems_stack_allocate_init_hook
```

(InterfaceRtemsStackAllocateInitHook)=

### rtems_stack_allocate_init_hook

A task stack allocator initialization handler shall have this type.

% Generated from spec:/rtems/config/if/stack-free-hook

```{index} rtems_stack_free_hook
```

(InterfaceRtemsStackFreeHook)=

### rtems_stack_free_hook

A task stack allocator free handler shall have this type.

% Generated from spec:/rtems/status/if/code

```{index} rtems_status_code
```

(InterfaceRtemsStatusCode)=

### rtems_status_code

This enumeration provides status codes for directives of the Classic API.

```{eval-rst}
.. rubric:: ENUMERATORS:
```

RTEMS_SUCCESSFUL
: This status code indicates successful completion of a requested operation.

RTEMS_TASK_EXITTED
: This status code indicates that a thread exitted.

RTEMS_MP_NOT_CONFIGURED
: This status code indicates that multiprocessing was not configured.

RTEMS_INVALID_NAME
: This status code indicates that an object name was invalid.

RTEMS_INVALID_ID
: This status code indicates that an object identifier was invalid.

RTEMS_TOO_MANY
: This status code indicates you have attempted to create too many instances
  of a particular object class.

RTEMS_TIMEOUT
: This status code indicates that a blocking directive timed out.

RTEMS_OBJECT_WAS_DELETED
: This status code indicates the object was deleted while the thread was
  blocked waiting.

RTEMS_INVALID_SIZE
: This status code indicates that a specified size was invalid.

RTEMS_INVALID_ADDRESS
: This status code indicates that a specified address was invalid.

RTEMS_INVALID_NUMBER
: This status code indicates that a specified number was invalid.

RTEMS_NOT_DEFINED
: This status code indicates that the item has not been initialized.

RTEMS_RESOURCE_IN_USE
: This status code indicates that the object still had resources in use.

RTEMS_UNSATISFIED
: This status code indicates that the request was not satisfied.

RTEMS_INCORRECT_STATE
: This status code indicates that an object was in wrong state for the
  requested operation.

RTEMS_ALREADY_SUSPENDED
: This status code indicates that the thread was already suspended.

RTEMS_ILLEGAL_ON_SELF
: This status code indicates that the operation was illegal on the calling
  thread.

RTEMS_ILLEGAL_ON_REMOTE_OBJECT
: This status code indicates that the operation was illegal on a remote
  object.

RTEMS_CALLED_FROM_ISR
: This status code indicates that the operation should not be called from
  this execution environment.

RTEMS_INVALID_PRIORITY
: This status code indicates that an invalid thread priority was provided.

RTEMS_INVALID_CLOCK
: This status code indicates that a specified date or time was invalid.

RTEMS_INVALID_NODE
: This status code indicates that a specified node identifier was invalid.

RTEMS_NOT_CONFIGURED
: This status code indicates that the directive was not configured.

RTEMS_NOT_OWNER_OF_RESOURCE
: This status code indicates that the caller was not the owner of the
  resource.

RTEMS_NOT_IMPLEMENTED
: This status code indicates the directive or requested portion of the
  directive is not implemented. This is a hint that you have stumbled across
  an opportunity to submit code to the RTEMS Project.

RTEMS_INTERNAL_ERROR
: This status code indicates that an internal RTEMS inconsistency was
  detected.

RTEMS_NO_MEMORY
: This status code indicates that the directive attempted to allocate memory
  but was unable to do so.

RTEMS_IO_ERROR
: This status code indicates a device driver IO error.

RTEMS_INTERRUPTED
: This status code is used internally by the implementation to indicate a
  blocking device driver call has been interrupted and should be reflected to
  the caller as interrupted.

RTEMS_PROXY_BLOCKING
: This status code is used internally by the implementation when performing
  operations on behalf of remote tasks. This is referred to as proxying
  operations and this status indicates that the operation could not be
  completed immediately and the proxy is blocking.

% Generated from spec:/rtems/task/if/task

```{index} rtems_task
```

(InterfaceRtemsTask)=

### rtems_task

This type defines the return type of task entry points.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This type can be used to document task entry points in the source code.

% Generated from spec:/rtems/task/if/argument

```{index} rtems_task_argument
```

(InterfaceRtemsTaskArgument)=

### rtems_task_argument

This integer type represents task argument values.

```{eval-rst}
.. rubric:: NOTES:
```

The type is an architecture-specific unsigned integer type which is large
enough to represent pointer values and 32-bit unsigned integers.

% Generated from spec:/rtems/userext/if/task-begin

```{index} rtems_task_begin_extension
```

(InterfaceRtemsTaskBeginExtension)=

### rtems_task_begin_extension

Task begin extensions are invoked when a task begins execution.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread.

```{eval-rst}
.. rubric:: NOTES:
```

The task begin extensions are invoked in {term}`extension forward order`.

Task begin extensions are invoked with thread dispatching enabled. This allows
the use of dynamic memory allocation, creation of POSIX keys, and use of C++
thread-local storage. Blocking synchronization primitives are allowed also.

The task begin extensions are invoked before the global construction.

The task begin extensions may be called as a result of a task restart through
{ref}`InterfaceRtemsTaskRestart`.

% Generated from spec:/rtems/task/if/config

```{index} rtems_task_config
```

(InterfaceRtemsTaskConfig)=

### rtems_task_config

This structure defines the configuration of a task constructed by
{ref}`InterfaceRtemsTaskConstruct`.

```{eval-rst}
.. rubric:: MEMBERS:
```

name

: This member defines the name of the task.

initial_priority

: This member defines the initial priority of the task.

storage_area

: This member shall point to the task storage area begin. The task storage
  area will contain the task stack, the thread-local storage, and the
  floating-point context on architectures with a separate floating-point
  context.

  The task storage area begin address and size should be aligned by
  {c:macro}`RTEMS_TASK_STORAGE_ALIGNMENT`. To avoid memory waste, use
  {c:func}`RTEMS_ALIGNED` and {c:macro}`RTEMS_TASK_STORAGE_ALIGNMENT` to
  enforce the recommended alignment of a statically allocated task storage
  area.

storage_size

: This member defines size of the task storage area in bytes. Use the
  {ref}`InterfaceRTEMSTASKSTORAGESIZE` macro to determine the recommended
  task storage area size.

maximum_thread_local_storage_size

: This member defines the maximum thread-local storage size supported by the
  task storage area. Use {c:func}`RTEMS_ALIGN_UP` and
  {c:macro}`RTEMS_TASK_STORAGE_ALIGNMENT` to adjust the size to meet the
  minimum alignment requirement of a thread-local storage area used to
  construct a task.

  If the value is less than the actual thread-local storage size, then the
  task construction by {ref}`InterfaceRtemsTaskConstruct` fails.

  If the is less than the task storage area size, then the task construction
  by {ref}`InterfaceRtemsTaskConstruct` fails.

  The actual thread-local storage size is determined when the application
  executable is linked. The `rtems-exeinfo` command line tool included in
  the RTEMS Tools can be used to obtain the thread-local storage size and
  alignment of an application executable.

  The application may configure the maximum thread-local storage size for all
  threads explicitly through the
  {ref}`CONFIGURE_MAXIMUM_THREAD_LOCAL_STORAGE_SIZE` configuration option.

storage_free

: This member defines the optional handler to free the task storage area. It
  is called on exactly two mutually exclusive occasions. Firstly, when the
  task construction aborts due to a failed task create extension, or
  secondly, when the task is deleted. It is called from task context under
  protection of the object allocator lock. It is allowed to call
  {c:func}`free` in this handler. If handler is [NULL](https://en.cppreference.com/w/c/types/NULL), then no action will be
  performed.

initial_modes

: This member defines the initial modes of the task.

attributes

: This member defines the attributes of the task.

% Generated from spec:/rtems/userext/if/task-create

```{index} rtems_task_create_extension
```

(InterfaceRtemsTaskCreateExtension)=

### rtems_task_create_extension

Task create extensions are invoked when a task is created.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread. When the idle
  thread is created, the executing thread is equal to [NULL](https://en.cppreference.com/w/c/types/NULL).

`created`
: This parameter is the {term}`TCB` of the created thread.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns true, if the task create extension was successful, otherwise false.

```{eval-rst}
.. rubric:: NOTES:
```

The task create extensions are invoked in {term}`extension forward order`.

The task create extensions are invoked after a new task has been completely
initialized, but before it is started.

While normal tasks are created, the executing thread is the owner of the object
allocator mutex. The object allocator mutex allows nesting, so the normal
memory allocation routines can be used allocate memory for the created thread.

If the task create extension returns {c:macro}`false`, then the task create
operation stops immediately and the entire task create operation will fail. In
this case, all task delete extensions are invoked, see
{ref}`InterfaceRtemsTaskDeleteExtension`.

% Generated from spec:/rtems/userext/if/task-delete

```{index} rtems_task_delete_extension
```

(InterfaceRtemsTaskDeleteExtension)=

### rtems_task_delete_extension

Task delete extensions are invoked when a task is deleted.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread. If the idle
  thread is created and one of the initial task create extension fails, then
  the executing thread is equal to [NULL](https://en.cppreference.com/w/c/types/NULL).

`created`
: This parameter is the {term}`TCB` of the deleted thread. The executing and
  deleted arguments are never equal.

```{eval-rst}
.. rubric:: NOTES:
```

The task delete extensions are invoked in {term}`extension reverse order`.

The task delete extensions are invoked by task create directives before an
attempt to allocate a {term}`TCB` is made.

If a task create extension failed, then a task delete extension may be invoked
without a previous invocation of the corresponding task create extension of the
extension set.

% Generated from spec:/rtems/task/if/entry

```{index} rtems_task_entry
```

(InterfaceRtemsTaskEntry)=

### rtems_task_entry

This type defines the {term}`task entry` point of an RTEMS task.

% Generated from spec:/rtems/userext/if/task-exitted

```{index} rtems_task_exitted_extension
```

(InterfaceRtemsTaskExittedExtension)=

### rtems_task_exitted_extension

Task exitted extensions are invoked when a task entry returns.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread.

```{eval-rst}
.. rubric:: NOTES:
```

The task exitted extensions are invoked in {term}`extension forward order`.

% Generated from spec:/rtems/type/if/priority

```{index} rtems_task_priority
```

(InterfaceRtemsTaskPriority)=

### rtems_task_priority

This integer type represents task priorities of the Classic API.

% Generated from spec:/rtems/userext/if/task-restart

```{index} rtems_task_restart_extension
```

(InterfaceRtemsTaskRestartExtension)=

### rtems_task_restart_extension

Task restart extensions are invoked when a task restarts.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread.

`restarted`
: This parameter is the {term}`TCB` of the executing thread. Yes, the
  executing thread.

```{eval-rst}
.. rubric:: NOTES:
```

The task restart extensions are invoked in {term}`extension forward order`.

The task restart extensions are invoked in the context of the restarted thread
right before the execution context is reloaded. The thread stack reflects the
previous execution context.

Thread restart and delete requests issued by restart extensions lead to
recursion.

% Generated from spec:/rtems/userext/if/task-start

```{index} rtems_task_start_extension
```

(InterfaceRtemsTaskStartExtension)=

### rtems_task_start_extension

Task start extensions are invoked when a task was made ready for the first
time.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread.

`started`
: This parameter is the {term}`TCB` of the started thread.

```{eval-rst}
.. rubric:: NOTES:
```

The task start extensions are invoked in {term}`extension forward order`.

In SMP configurations, the thread may already run on another processor before
the task start extensions are actually invoked. Task switch and task begin
extensions may run before or in parallel with the thread start extension in SMP
configurations, see {ref}`InterfaceRtemsTaskSwitchExtension` and
{ref}`InterfaceRtemsTaskBeginExtension`.

% Generated from spec:/rtems/userext/if/task-switch

```{index} rtems_task_switch_extension
```

(InterfaceRtemsTaskSwitchExtension)=

### rtems_task_switch_extension

Task switch extensions are invoked when a thread switch from an executing
thread to a heir thread takes place.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread. In SMP
  configurations, this is the previously executing thread also known as the
  ancestor thread.

`heir`
: This parameter is the {term}`TCB` of the heir thread. In SMP
  configurations, this is the executing thread.

```{eval-rst}
.. rubric:: NOTES:
```

The task switch extensions are invoked in {term}`extension forward order`.

The invocation conditions of the task switch extensions depend on whether RTEMS
was built with SMP support enabled or disabled. A user must pay attention to
the differences to correctly implement a task switch extension.

Where the system was built with SMP support disabled, the task switch
extensions are invoked before the context switch from the currently executing
thread to the heir thread. The `executing` is a pointer to the {term}`TCB`
of the currently executing thread. The `heir` is a pointer to the TCB of the
heir thread. The context switch initiated through the multitasking start is
not covered by the task switch extensions.

Where the system was built with SMP support enabled, the task switch extensions
are invoked after the context switch to the heir thread. The `executing` is
a pointer to the TCB of the previously executing thread. Despite the name, this
is not the currently executing thread. The `heir` is a pointer to the TCB of
the newly executing thread. This is the currently executing thread. The context
switches initiated through the multitasking start are covered by the task
switch extensions. The reason for the differences to uniprocessor
configurations is that the context switch may update the heir thread of the
processor. The task switch extensions are invoked with maskable interrupts
disabled and with ownership of a processor-specific SMP lock. Task switch
extensions may run in parallel on multiple processors. It is recommended to
use thread-local or processor-specific data structures for task switch
extensions. A global SMP lock should be avoided for performance reasons, see
{ref}`InterfaceRtemsInterruptLockInitialize`.

% Generated from spec:/rtems/userext/if/task-terminate

```{index} rtems_task_terminate_extension
```

(InterfaceRtemsTaskTerminateExtension)=

### rtems_task_terminate_extension

Task terminate extensions are invoked when a task terminates.

```{eval-rst}
.. rubric:: PARAMETERS:
```

`executing`
: This parameter is the {term}`TCB` of the executing thread. This is the
  terminating thread.

```{eval-rst}
.. rubric:: NOTES:
```

The task terminate extensions are invoked in {term}`extension reverse order`.

The task terminate extensions are invoked in the context of the terminating
thread right before the thread dispatch to the heir thread should take place.
The thread stack reflects the previous execution context. The POSIX cleanup
and key destructors execute in this context.

Thread restart and delete requests issued by terminate extensions lead to
recursion.

% Generated from spec:/rtems/task/if/visitor

```{index} rtems_task_visitor
```

(InterfaceRtemsTaskVisitor)=

### rtems_task_visitor

Visitor routines invoked by {ref}`InterfaceRtemsTaskIterate` shall have this
type.

% Generated from spec:/rtems/task/if/tcb

```{index} rtems_tcb
```

(InterfaceRtemsTcb)=

### rtems_tcb

This structure represents the {term}`TCB`.

% Generated from spec:/rtems/type/if/time-of-day

```{index} rtems_time_of_day
```

(InterfaceRtemsTimeOfDay)=

### rtems_time_of_day

This type represents Classic API calendar times.

```{eval-rst}
.. rubric:: MEMBERS:
```

year
: This member contains the year A.D.

month
: This member contains the month of the year with values from 1 to 12.

day
: This member contains the day of the month with values from 1 to 31.

hour
: This member contains the hour of the day with values from 0 to 23.

minute
: This member contains the minute of the hour with values from 0 to 59.

second
: This member contains the second of the minute with values from 0 to 59.

ticks
: This member contains the clock tick of the second with values from 0 to
  {ref}`InterfaceRtemsClockGetTicksPerSecond` minus one.

% Generated from spec:/rtems/timer/if/information

```{index} rtems_timer_information
```

(InterfaceRtemsTimerInformation)=

### rtems_timer_information

The structure contains information about a timer.

```{eval-rst}
.. rubric:: MEMBERS:
```

the_class
: The timer class member indicates how the timer was most recently fired.

initial
: This member indicates the initial requested interval.

start_time
: This member indicates the time the timer was initially scheduled. The time
  is in clock ticks since the clock driver initialization or the last clock
  tick counter overflow.

stop_time
: This member indicates the time the timer was scheduled to fire. The time is
  in clock ticks since the clock driver initialization or the last clock tick
  counter overflow.

% Generated from spec:/rtems/timer/if/service-routine

```{index} rtems_timer_service_routine
```

(InterfaceRtemsTimerServiceRoutine)=

### rtems_timer_service_routine

This type defines the return type of routines which can be fired by directives
of the Timer Manager.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This type can be used to document timer service routines in the source code.

% Generated from spec:/rtems/timer/if/service-routine-entry

```{index} rtems_timer_service_routine_entry
```

(InterfaceRtemsTimerServiceRoutineEntry)=

### rtems_timer_service_routine_entry

This type defines the prototype of routines which can be fired by directives of
the Timer Manager.

% Generated from spec:/rtems/intr/if/vector-number

```{index} rtems_vector_number
```

(InterfaceRtemsVectorNumber)=

### rtems_vector_number

This integer type represents interrupt vector numbers.
