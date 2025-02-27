% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1989, 2017 On-Line Applications Research Corporation (OAR)

```{index} Ada
```

(ada_support)=

# Ada Support

## Introduction

RTEMS has long had support for the Ada programming language
by supporting the GNU Ada Compiler (GNAT). There are two primary
components to this support:

- Ada Programming Language Support
- Classic API Ada Bindings

## Ada Programming Language Support

The Ada programming natively supports multi-threaded programming
with its own tasking and concurrency model. Native Ada multi-threaded
applications should work using GNAT/RTEMS with no changes.

The application developer will have to account for the specific
requirements of the GNAT Run-Time when configuring RTEMS. There
are example Ada programs with RTEMS configuration and startup sequences.

## Classic API Ada Bindings

An Ada language binding exists for a subset of the RTEMS Classic
API. In the early 1990's, there were C and Ada implementations of
RTEMS which were functionally equivalent. The source structure was as
similar as possible. In fact, the top level `c/` directory at one point
had a sibling `ada/`. The current Ada language bindings and test code was
derived from that Ada implementation.

The Ada binding specifically excludes some methods which are either not
safe or not intended for use from Ada programs. However, methods are
generally only added to this binding when a user makes a requests. Thus
some methods that could be supported are not. If in doubt, ask about a
methods and contribute bindings.

The bindings are located in the `c/src/ada` directory of the RTEMS source
tree. The tests are in `c/src/ada-tests`. The bindings following a simple
pattern to map the C Classic API calls into Ada subprograms. The following
rules are used:

- All RTEMS interfaces are in the RTEMS Ada package. The rtems\_ and
  RTEMS\_ prefixes in the C version of the Classic API thus correspond to
  "RTEMS." in Ada symbol nomenclature. For example, `rtems_task_create()`
  in C is `RTEMS.Task_Create()` in Ada.
- Classic API directives tend to return an `rtems_status_code`. Some
  directives also have an output parameter such as an object id on a create
  operation. Ada subprograms are either pure functions with only a single
  return value or subprograms. For consistency, the returned status code
  is always the last parameter of the Ada calling sequence.

Caution should be exercised when writing programs which mix Ada tasks,
Classic API tasks, and POSIX API threads. Ada tasks use a priority
numbering scheme defined by the Ada programming language. Each Ada task
is implemented in GNAT/RTEMS as a single POSIX thread. Thus Ada task
priorities must be mapped onto POSIX thread priorities. Complicating
matters, Classic API tasks and POSIX API threads use different numbering
schemes for priority. Low numbers are high priority in the Classic
API while indicating low priority in the POSIX threads API. Experience
writing mixed threading model programs teaches that creating a table
of the priorities used in the application with the value in all tasking
models used is helpful.

The GNAT run-time uses a priority ceiling mutex to protect its data
structures. The priority ceiling value is one priority more important
than the most important Ada task priority (in POSIX API terms). Do not
invoke any services implemented in Ada from a thread or task which is
of greater priority. This will result in a priority ceiling violation
error and lead to a failure in the Ada run-time.

Exercise extreme caution when considering writing code in Ada which
will execute in the context of an interrupt handler. Hardware interrupts are
processed outside the context of any thread in RTEMS and this can lead
to violating assumptions in the GNAT run-time. Specifically a priority
ceiling mutex should never be used from an ISR and it is difficult to
predict when the Ada compiler or run-time will use a mutex.

RTEMS has two capabilities which can assist in avoiding this problem. The
Classic API Timer Manager allows the creation of Timer Service Routines
which execute in the context of a task rather than the clock tick
Interrupt Service Routine. Similarly, there is support for Interrupt Tasks
which is a mechanism to defer the processing of the event from the
hardware interrupt level to a thread.
