% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2023 On-Line Applications Research Corporation (OAR)

(regulatormanagerdirectives)=

# Directives

This section details the directives of the Regulator Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% *** START of rtems_regulator_create()

```{raw} latex
\clearpage
```

```{index} rtems_regulator_create()
```

```{index} create a regulator
```

(interfacertemsregulatorcreate)=

## rtems_regulator_create()

Creates a regulator.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_regulator_create(
  rtems_regulator_attributes  *attributes,
  rtems_regulator_instance   **regulator
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`attributes`
: This parameter is the attributes associated with the regulator
  being created.

`regulator`
: This parameter is the pointer to a regulator instance. When the
  directive call is successful, a pointer to the created regulator
  will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This function creates an instance of a regulator. It uses the provided
`attributes` to create the instance return in `regulator`. This instance
will allocate the buffers associated with the regulator instance as well
as the Delivery Thread.

The `attributes` parameter points to an instance of
{ref}`InterfaceRtemsRegulatorAttributes` which is filled in to reflect
the desired configuration of the regulator instance. It defines multiple
characteristics of the the Delivery thread dedicated to this regulator
instance including the priority and stack size. It also defines the
period of the Delivery thread and the maximum number of messages that may
be delivered per period via invocation of the delivery function.

For each regulator instance, the following resources are allocated:

- A memory area for the regulator control block using `malloc()`.
- A RTEMS Classic API Message Queue is constructed with message
  buffer memory allocated using `malloc()`. Each message consists
  of a pointer to the contents and a length field.
- A RTEMS Classic API Partition.
- A RTEMS Classic API Rate Monotonic Period.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `attributes` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `regulator` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `deliverer` field in the structure pointed to by the
  `attributes` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_SIZE`
: The `maximum_messages` field in the structure pointed to by the
  `attributes` parameter was 0.

{c:macro}`RTEMS_INVALID_NUMBER`
: The `maximum_to_dequeue_per_period` field in the structure pointed
  to by the `attributes` parameter was 0.

{c:macro}`RTEMS_NO_MEMORY`
: The allocation of memory for the regulator instance failed.

{c:macro}`RTEMS_NO_MEMORY`
: The allocation of memory for the buffers failed.

{c:macro}`RTEMS_NO_MEMORY`
: The allocation of memory for the internal message queue failed.

```{eval-rst}
.. rubric:: NOTES:
```

{ref}`InterfaceRtemsRegulatorCreate` uses
{ref}`InterfaceRtemsPartitionCreate`,
{ref}`InterfaceRtemsMessageQueueConstruct`,
{ref}`InterfaceRtemsTaskCreate`, and {ref}`InterfaceRtemsTaskStart`. If
any of those directives return a status indicating failure, it will be
returned to the caller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- The number of tasks available to the application is configured through the
  {ref}`CONFIGURE_MAXIMUM_TASKS` application configuration option.
- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

% *** START of rtems_regulator_delete()

```{raw} latex
\clearpage
```

```{index} rtems_regulator_delete()
```

```{index} delete a regulator
```

(interfacertemsregulatordelete)=

## rtems_regulator_delete()

Deletes the regulator.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_regulator_delete(
  rtems_regulator_instance    *regulator,
  rtems_interval               ticks
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`regulator`
: This parameter points to the regulator instance.

`ticks`
: This parameter specifies the maximum length of time to wait.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive is used to delete the specified `regulator`
instance. It will deallocate the resources that were allocated by the
{ref}`InterfaceRtemsRegulatorCreate` directive.

This directive ensures that no buffers are outstanding either because the
Source is holding one of more buffers or because they are being held by
the regulator instance pending delivery.

If the Delivery Thread has been created and is running, this directive will
request the thread to voluntarily exit. This call will wait up to `ticks` for the thread to exit.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `regulator` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INCORRECT_STATE`
: The `regulator` instance was not initialized.

{c:macro}`RTEMS_RESOURCE_IN_USE`
: The `regulator` instance has buffers outstanding.

{c:macro}`RTEMS_TIMEOUT`
: The `regulator` instance was not able to be deleted within the
  specific number of `ticks`.

```{eval-rst}
.. rubric:: NOTES:
```

It is the responsibility of the user to ensure that any resources
such as sockets or open file descriptors used by the Source or delivery
function are also deleted if necessary. It is likely safer to delete those
delivery resources after deleting the regulator instance rather than before.

It is the responsibility of the user to ensure that all buffers associated
with this regulator instance have been released and that none are in
the process of being delivered.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
- The calling task does not have to be the task that created the object. Any
  local task that knows the object identifier can delete the object.
- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

% *** START of rtems_regulator_obtain_buffer()

```{raw} latex
\clearpage
```

```{index} rtems_regulator_obtain_buffer()
```

```{index} obtain buffer from regulator
```

(interfacertemsregulatorobtainbuffer)=

## rtems_regulator_obtain_buffer()

Obtain buffer from regulator.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_regulator_obtain_buffer(
  rtems_regulator_instance   *regulator,
  void                      **buffer
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`regulator`
: This parameter is the regulator instance to operate upon.

`buffer`
: This parameter will point to the buffer allocated.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This function is used to obtain a buffer from the regulator's pool. The
`buffer` returned is assumed to be filled in with contents and used
in a subsequent call to {ref}`InterfaceRtemsRegulatorSend`.

When the `buffer` is delivered, it is expected to be released. If the
`buffer` is not successfully accepted by this method, then it should
be returned using {ref}`InterfaceRtemsRegulatorReleaseBuffer` or used
to send another message.

The `buffer` returned is of the maximum_message_size specified in the
attributes passed in to {ref}`InterfaceRtemsRegulatorCreate`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `regulator` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INCORRECT_STATE`
: The `regulator` instance was not initialized.

```{eval-rst}
.. rubric:: NOTES:
```

{ref}`InterfaceRtemsRegulatorObtainBuffer` uses
{ref}`InterfaceRtemsPartitionGetBuffer` and if it returns a status
indicating failure, it will be returned to the caller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.

% *** START of rtems_regulator_release_buffer()

```{raw} latex
\clearpage
```

```{index} rtems_regulator_release_buffer()
```

```{index} release buffer back to regulator
```

(interfacertemsregulatorreleasebuffer)=

## rtems_regulator_release_buffer()

Release buffer to regulator.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_regulator_release_buffer(
  rtems_regulator_instance  *regulator,
  void                      *buffer
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`regulator`
: This parameter is the regulator instance to operate upon.

`buffer`
: This parameter will point to the buffer to be released.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This function is used to release a buffer to the regulator's pool. It is
assumed that the `buffer` returned will not be used by the application
anymore.

The `buffer` must have previously been allocated by
{ref}`InterfaceRtemsRegulatorObtainBuffer` and NOT yet passed to
{ref}`InterfaceRtemsRegulatorSend`, or it has been sent and delivery
has been completed by the delivery function.

If a subsequent {ref}`InterfaceRtemsRegulatorSend` using this `buffer`
is successful, the `buffer` will eventually be processed by the delivery
thread and released.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `regulator` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INCORRECT_STATE`
: The `regulator` instance was not initialized.

```{eval-rst}
.. rubric:: NOTES:
```

{ref}`InterfaceRtemsRegulatorReleaseBuffer` uses
{ref}`InterfaceRtemsPartitionReturnBuffer` and if it returns a status
indicating failure, it will be returned to the caller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.

% *** START of rtems_regulator_send()

```{raw} latex
\clearpage
```

```{index} rtems_regulator_send()
```

```{index} send buffer to regulator for delivery
```

(interfacertemsregulatorsend)=

## rtems_regulator_send()

Send buffer to regulator.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_regulator_send(
  rtems_regulator_instance  *regulator,
  void                      *message,
  size_t                     length
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`regulator`
: This parameter is the regulator instance to operate upon.

`message`
: This parameter points to the buffer to send.

`length`
: This parameter specifies the number of bytes in the `message`.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This method is used by the producer to send a `message` to the
`regulator` for later delivery by the delivery thread. The message is
contained in the memory pointed to by `message` and is `length`
bytes in length.

It is required that the message buffer was obtained via
{ref}`InterfaceRtemsRegulatorObtainBuffer`.

It is assumed that the `message` buffer has been filled in with
application content to deliver.

If the {ref}`InterfaceRtemsRegulatorSend` is successful, the `message`
buffer is enqueued inside the regulator instance for subsequent delivery.
After the `message` is delivered, it may be released by either delivery
function or other application code depending on the implementation.

The status `RTEMS_TOO_MANY` is returned if the regulator's
internal queue is full. This indicates that the configured
maximum number of messages was insufficient. It is the
responsibility of the caller to decide whether to hold messages,
drop them, or print a message that the maximum number of messages
should be increased

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `regulator` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INCORRECT_STATE`
: The `regulator` instance was not initialized.

```{eval-rst}
.. rubric:: NOTES:
```

{ref}`InterfaceRtemsRegulatorSend` uses
{ref}`InterfaceRtemsMessageQueueSend` and if it returns a status
indicating failure, it will be returned to the caller.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.

% *** START of rtems_regulator_get_statistics()

```{raw} latex
\clearpage
```

```{index} rtems_regulator_get_statistics()
```

```{index} obtain statistics from regulator
```

(interfacertemsregulatorgetstatistics)=

## rtems_regulator_get_statistics()

Obtain statistics from regulator.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_regulator_get_statistics(
  rtems_regulator_instance   *regulator,
  rtems_regulator_statistics *statistics
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`regulator`
: This parameter is the regulator instance to operate upon.

`statistics`
: This parameter points to the statistics structure to be filled in.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This method is used by the application to obtain the current
`statistics` for this `regulator`. The statistics information
provided includes:

- the number of buffers obtained via
  {ref}`InterfaceRtemsRegulatorObtainBuffer`
- the number of buffers released via
  {ref}`InterfaceRtemsRegulatorReleaseBuffer`
- the number of buffers delivered by the Delivery
  Thread via the `deliverer` function specified in the
  {ref}`InterfaceRtemsRegulatorAttributes` structure provided to
  {ref}`InterfaceRtemsRegulatorCreate``via the`attibutes\` parameter.
- the `period_statistics` for the Delivery Thread. For more details on
  period statistics, see {ref}`InterfaceRtemsRateMonotonicPeriodStatistics`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `regulator` or `statistics` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INCORRECT_STATE`
: The `regulator` instance was not initialized.

```{eval-rst}
.. rubric:: NOTES:
```

The number of buffers outstanding is `released` minus
`obtained`. The regulator instance cannot be deleted using
{ref}`InterfaceRtemsRegulatorDelete` until all buffers are released.

The `obtained` and `released` values are cumulative over
the life of the Regulator instance and are likely to larger than the
`maximum_messages` value in the `attributes` structure
({ref}`InterfaceRtemsRegulatorAttributes`
provided to {ref}`InterfaceRtemsRegulatorCreate`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
