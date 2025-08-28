% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG
% Copyright (C) 2017 Kuan-Hsun Chen
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

(RateMonotonicManagerDirectives)=

# Directives

This section details the directives of the Rate-Monotonic Manager. A subsection
is dedicated to each of this manager's directives and lists the calling
sequence, parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/ratemon/if/create

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_create()
```

```{index} create a period
```

(InterfaceRtemsRateMonotonicCreate)=

## rtems_rate_monotonic_create()

Creates a period.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_create( rtems_name name, rtems_id *id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`name`
: This parameter is the object name of the period.

`id`
: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When the
  directive call is successful, the identifier of the created period will be
  stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive creates a period which resides on the local node. The period has
the user-defined object name specified in `name` The assigned object identifier
is returned in `id`. This identifier is used to access the period with other
rate monotonic related directives.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_NAME`
: The `name` parameter was invalid.

{c:macro}`RTEMS_TOO_MANY`
: There was no inactive object available to create a period. The number of
  periods available to the application is configured through the
  {ref}`CONFIGURE_MAXIMUM_PERIODS` application configuration option.

```{eval-rst}
.. rubric:: NOTES:
```

The calling task is registered as the owner of the created period. Some
directives can be only used by this task for the created period.

For control and maintenance of the period, RTEMS allocates a {term}`PCB` from
the local PCB free pool and initializes it.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

- The number of periods available to the application is configured through the
  {ref}`CONFIGURE_MAXIMUM_PERIODS` application configuration option.

- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may allocate memory from the RTEMS
  Workspace.

% Generated from spec:/rtems/ratemon/if/ident

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_ident()
```

(InterfaceRtemsRateMonotonicIdent)=

## rtems_rate_monotonic_ident()

Identifies a period by the object name.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_ident( rtems_name name, rtems_id *id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`name`
: This parameter is the object name to look up.

`id`
: This parameter is the pointer to an {ref}`InterfaceRtemsId` object. When the
  directive call is successful, the object identifier of an object with the
  specified name will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive obtains a period identifier associated with the period name
specified in `name`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `id` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_NAME`
: The `name` parameter was 0.

{c:macro}`RTEMS_INVALID_NAME`
: There was no object with the specified name on the local node.

```{eval-rst}
.. rubric:: NOTES:
```

If the period name is not unique, then the period identifier will match the
first period with that name in the search order. However, this period
identifier is not guaranteed to correspond to the desired period.

The objects are searched from lowest to the highest index. Only the local node
is searched.

The period identifier is used with other rate monotonic related directives to
access the period.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/ratemon/if/cancel

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_cancel()
```

```{index} cancel a period
```

(InterfaceRtemsRateMonotonicCancel)=

## rtems_rate_monotonic_cancel()

Cancels the period.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_cancel( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the rate monotonic period identifier.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive cancels the rate monotonic period specified by `id`. This period
may be reinitiated by the next invocation of
{ref}`InterfaceRtemsRateMonotonicPeriod`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no rate monotonic period associated with the identifier specified
  by `id`.

{c:macro}`RTEMS_NOT_OWNER_OF_RESOURCE`
: The rate monotonic period was not created by the calling task.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive will not cause the calling task to be preempted.

- The directive may be used exclusively by the task which created the
  associated object.

% Generated from spec:/rtems/ratemon/if/delete

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_delete()
```

```{index} delete a period
```

(InterfaceRtemsRateMonotonicDelete)=

## rtems_rate_monotonic_delete()

Deletes the period.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_delete( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the period identifier.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive deletes the period specified by `id`. If the period is running,
it is automatically canceled.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no period associated with the identifier specified by `id`.

```{eval-rst}
.. rubric:: NOTES:
```

The {term}`PCB` for the deleted period is reclaimed by RTEMS.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

- The calling task does not have to be the task that created the object. Any
  local task that knows the object identifier can delete the object.

- Where the object class corresponding to the directive is configured to use
  unlimited objects, the directive may free memory to the RTEMS Workspace.

% Generated from spec:/rtems/ratemon/if/period

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_period()
```

```{index} conclude current period
```

```{index} start current period
```

```{index} period initiation
```

(InterfaceRtemsRateMonotonicPeriod)=

## rtems_rate_monotonic_period()

Concludes the current period and start the next period, or gets the period
status.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_period(
  rtems_id       id,
  rtems_interval length
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the rate monotonic period identifier.

`length`
: This parameter is the period length in {term}`clock ticks <clock tick>` or
  {c:macro}`RTEMS_PERIOD_STATUS` to get the period status.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive initiates the rate monotonic period specified by `id` with a
length of period ticks specified by `length`. If the period is running, then
the calling task will block for the remainder of the period before reinitiating
the period with the specified period length. If the period was not running
(either expired or never initiated), the period is immediately initiated and
the directive returns immediately. If the period has expired, the postponed job
will be released immediately and the following calls of this directive will
release postponed jobs until there is no more deadline miss.

If invoked with a period length of {c:macro}`RTEMS_PERIOD_STATUS` ticks, the
current state of the period will be returned. The directive status indicates
the current state of the period. This does not alter the state or period length
of the period.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no rate monotonic period associated with the identifier specified
  by `id`.

{c:macro}`RTEMS_NOT_OWNER_OF_RESOURCE`
: The rate monotonic period was not created by the calling task.

{c:macro}`RTEMS_NOT_DEFINED`
: The rate monotonic period has never been initiated (only possible when the
  `length` parameter was equal to {c:macro}`RTEMS_PERIOD_STATUS`).

{c:macro}`RTEMS_TIMEOUT`
: The rate monotonic period has expired.

```{eval-rst}
.. rubric:: NOTES:
```

Resetting the processor usage time of tasks has no impact on the period status
and statistics.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may be used exclusively by the task which created the
  associated object.

% Generated from spec:/rtems/ratemon/if/get-status

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_get_status()
```

```{index} get status of period
```

```{index} obtain status of period
```

(InterfaceRtemsRateMonotonicGetStatus)=

## rtems_rate_monotonic_get_status()

Gets the detailed status of the period.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_get_status(
  rtems_id                            id,
  rtems_rate_monotonic_period_status *status
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the rate monotonic period identifier.

`status`
: This parameter is the pointer to an
  {ref}`InterfaceRtemsRateMonotonicPeriodStatus` object. When the directive
  call is successful, the detailed period status will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns the detailed status of the rate monotonic period
specified by `id`. The detailed status of the period will be returned in the
members of the period status object referenced by `status`:

- The `owner` member is set to the identifier of the owner task of the period.

- The `state` member is set to the current state of the period.

- The `postponed_jobs_count` member is set to the count of jobs which are not
  released yet.

- If the current state of the period is {c:macro}`RATE_MONOTONIC_INACTIVE`, the
  `since_last_period` and `executed_since_last_period` members will be set to
  zero. Otherwise, both members will contain time information since the last
  successful invocation of the {ref}`InterfaceRtemsRateMonotonicPeriod`
  directive by the owner task. More specifically, the `since_last_period`
  member will be set to the time elapsed since the last successful invocation.
  The `executed_since_last_period` member will be set to the processor time
  consumed by the owner task since the last successful invocation.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no rate monotonic period associated with the identifier specified
  by `id`.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `status` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may be called from within interrupt context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/ratemon/if/get-statistics

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_get_statistics()
```

```{index} get statistics of period
```

```{index} obtain statistics of period
```

(InterfaceRtemsRateMonotonicGetStatistics)=

## rtems_rate_monotonic_get_statistics()

Gets the statistics of the period.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_get_statistics(
  rtems_id                                id,
  rtems_rate_monotonic_period_statistics *status
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the rate monotonic period identifier.

`status`
: This parameter is the pointer to an
  {ref}`InterfaceRtemsRateMonotonicPeriodStatistics` object. When the directive
  call is successful, the period statistics will be stored in this object.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive returns the statistics of the rate monotonic period specified by
`id`. The statistics of the period will be returned in the members of the
period statistics object referenced by `status`:

- The `count` member is set to the number of periods executed.

- The `missed_count` member is set to the number of periods missed.

- The `min_cpu_time` member is set to the least amount of processor time used
  in the period.

- The `max_cpu_time` member is set to the highest amount of processor time used
  in the period.

- The `total_cpu_time` member is set to the total amount of processor time used
  in the period.

- The `min_wall_time` member is set to the least amount of
  {term}`CLOCK_MONOTONIC` time used in the period.

- The `max_wall_time` member is set to the highest amount of
  {term}`CLOCK_MONOTONIC` time used in the period.

- The `total_wall_time` member is set to the total amount of
  {term}`CLOCK_MONOTONIC` time used in the period.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no rate monotonic period associated with the identifier specified
  by `id`.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `status` parameter was
  [NULL](https://en.cppreference.com/w/c/types/NULL).

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may be called from within interrupt context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/ratemon/if/reset-statistics

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_reset_statistics()
```

```{index} reset statistics of period
```

(InterfaceRtemsRateMonotonicResetStatistics)=

## rtems_rate_monotonic_reset_statistics()

Resets the statistics of the period.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_status_code rtems_rate_monotonic_reset_statistics( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the rate monotonic period identifier.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive resets the statistics of the rate monotonic period specified by
`id`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ID`
: There was no rate monotonic period associated with the identifier specified
  by `id`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may be called from within interrupt context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/ratemon/if/reset-all-statistics

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_reset_all_statistics()
```

```{index} reset statistics of all periods
```

(InterfaceRtemsRateMonotonicResetAllStatistics)=

## rtems_rate_monotonic_reset_all_statistics()

Resets the statistics of all periods.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_rate_monotonic_reset_all_statistics( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive resets the statistics information associated with all rate
monotonic period instances.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/ratemon/if/report-statistics

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_report_statistics()
```

```{index} print period statistics report
```

```{index} period statistics report
```

(InterfaceRtemsRateMonotonicReportStatistics)=

## rtems_rate_monotonic_report_statistics()

Reports the period statistics using the {ref}`InterfacePrintk` printer.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_rate_monotonic_report_statistics( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive prints a report on all active periods which have executed at
least one period using the {ref}`InterfacePrintk` printer.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/ratemon/if/report-statistics-with-plugin

```{raw} latex
\clearpage
```

```{index} rtems_rate_monotonic_report_statistics_with_plugin()
```

```{index} print period statistics report
```

```{index} period statistics report
```

(InterfaceRtemsRateMonotonicReportStatisticsWithPlugin)=

## rtems_rate_monotonic_report_statistics_with_plugin()

Reports the period statistics using the printer plugin.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_rate_monotonic_report_statistics_with_plugin(
  const struct rtems_printer *printer
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`printer`
: This parameter is the printer plugin to output the report.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive prints a report on all active periods which have executed at
least one period using the printer plugin specified by `printer`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
