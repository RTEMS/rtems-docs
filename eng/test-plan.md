% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018.

% COMMENT: RTEMS Foundation, The RTEMS Documentation Project

# Software Test Plan Assurance and Procedures

## Testing and Coverage

Testing to verify that requirements are implemented is a critical part of
the high integrity processes. Similarly, measuring and reporting source
and decision path coverage of source code is critical.

Needed improvements to the RTEMS testing infrastructure should be done
as part of the open project. Similarly, improvements in RTEMS coverage
reporting should be done as part of the open project. Both of these
capabilities are part of the RTEMS Tester toolset.

Assuming that a requirements focused test suite is added to the open
RTEMS, tools will be needed to assist in verifying that requirements are
"fully tested." A fully tested requirement is one which is implemented
and tested with associated logical tracing. Tools automating this analysis
and generating reporting and alerts will be a critical part of ensuring
the source technical data does not bit rot.

Must use tools from:

RTEMS Tools Project: <https://gitlab.rtems.org/rtems/tools/rtems-tools>

Scope, Procedures, Methodologies, Tools
TBD - Write content

% COMMENT: Subsections

```{toctree}
test-suites
tester
```
