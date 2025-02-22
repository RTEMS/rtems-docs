% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Background

A semaphore can be viewed as a protected variable whose value can be modified
only with the `rtems_semaphore_create`, `rtems_semaphore_obtain`, and
`rtems_semaphore_release` directives. RTEMS supports both binary and
counting semaphores. A binary semaphore is restricted to values of zero or one,
while a counting semaphore can assume any non-negative integer value.

A binary semaphore (not a simple binary semaphore) can be used to control
access to a single resource. In particular, it can be used to enforce mutual
exclusion for a critical section in user code (mutex). In this instance, the
semaphore would be created with an initial count of one to indicate that no
task is executing the critical section of code. Upon entry to the critical
section, a task must issue the `rtems_semaphore_obtain` directive to prevent
other tasks from entering the critical section. Upon exit from the critical
section, the task that obtained the binary semaphore must issue the
`rtems_semaphore_release` directive to allow another task to execute the
critical section. A binary semaphore must be released by the task that
obtained it.

A counting semaphore can be used to control access to a pool of two or more
resources. For example, access to three printers could be administered by a
semaphore created with an initial count of three. When a task requires access
to one of the printers, it issues the `rtems_semaphore_obtain` directive to
obtain access to a printer. If a printer is not currently available, the task
can wait for a printer to become available or return immediately. When the
task has completed printing, it should issue the `rtems_semaphore_release`
directive to allow other tasks access to the printer.

Task synchronization may be achieved by creating a semaphore with an initial
count of zero. One task waits for the arrival of another task by issuing a
`rtems_semaphore_obtain` directive when it reaches a synchronization point.
The other task performs a corresponding `rtems_semaphore_release` operation
when it reaches its synchronization point, thus unblocking the pending task.

(nested-resource-access)=

## Nested Resource Access

Deadlock occurs when a task owning a binary semaphore attempts to acquire that
same semaphore and blocks as result. Since the semaphore is allocated to a
task, it cannot be deleted. Therefore, the task that currently holds the
semaphore and is also blocked waiting for that semaphore will never execute
again.

RTEMS addresses this problem by allowing the task holding the binary semaphore
to obtain the same binary semaphore multiple times in a nested manner. Each
`rtems_semaphore_obtain` must be accompanied with a
`rtems_semaphore_release`. The semaphore will only be made available for
acquisition by other tasks when the outermost `rtems_semaphore_obtain` is
matched with a `rtems_semaphore_release`.

Simple binary semaphores do not allow nested access and so can be used for task
synchronization.

(priority-inheritance)=

## Priority Inheritance

RTEMS supports {ref}`priority inheritance <PriorityInheritance>` for local,
binary semaphores that use the priority task wait queue blocking discipline.
In SMP configurations, the {ref}`OMIP` is used instead.

(priority-ceiling)=

## Priority Ceiling

RTEMS supports {ref}`priority ceiling <PriorityCeiling>` for local, binary
semaphores that use the priority task wait queue blocking discipline.

(multiprocessor-resource-sharing-protocol)=

## Multiprocessor Resource Sharing Protocol

RTEMS supports the {ref}`MrsP` for local, binary semaphores that use the
priority task wait queue blocking discipline. In uniprocessor configurations,
the {ref}`PriorityCeiling` is used instead.

(building-a-semaphore-attribute-set)=

## Building a Semaphore Attribute Set

In general, an attribute set is built by a bitwise OR of the desired attribute
components. The following table lists the set of valid semaphore attributes:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``RTEMS_FIFO``
   - tasks wait by FIFO (default)
 * - ``RTEMS_PRIORITY``
   - tasks wait by priority
 * - ``RTEMS_BINARY_SEMAPHORE``
   - restrict values to 0 and 1
 * - ``RTEMS_COUNTING_SEMAPHORE``
   - no restriction on values (default)
 * - ``RTEMS_SIMPLE_BINARY_SEMAPHORE``
   - restrict values to 0 and 1, do not allow nested access, allow deletion of
     locked semaphore.
 * - ``RTEMS_NO_INHERIT_PRIORITY``
   - do not use priority inheritance (default)
 * - ``RTEMS_INHERIT_PRIORITY``
   - use priority inheritance
 * - ``RTEMS_NO_PRIORITY_CEILING``
   - do not use priority ceiling (default)
 * - ``RTEMS_PRIORITY_CEILING``
   - use priority ceiling
 * - ``RTEMS_NO_MULTIPROCESSOR_RESOURCE_SHARING``
   - do not use Multiprocessor Resource Sharing Protocol (default)
 * - ``RTEMS_MULTIPROCESSOR_RESOURCE_SHARING``
   - use Multiprocessor Resource Sharing Protocol
 * - ``RTEMS_LOCAL``
   - local semaphore (default)
 * - ``RTEMS_GLOBAL``
   - global semaphore
```

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list. An attribute listed as a default
is not required to appear in the attribute list, although it is a good
programming practice to specify default attributes. If all defaults are
desired, the attribute `RTEMS_DEFAULT_ATTRIBUTES` should be specified on this
call.

This example demonstrates the attribute_set parameter needed to create a local
semaphore with the task priority waiting queue discipline. The attribute_set
parameter passed to the `rtems_semaphore_create` directive could be either
`RTEMS_PRIORITY` or `RTEMS_LOCAL | RTEMS_PRIORITY`. The attribute_set
parameter can be set to `RTEMS_PRIORITY` because `RTEMS_LOCAL` is the
default for all created tasks. If a similar semaphore were to be known
globally, then the attribute_set parameter would be `RTEMS_GLOBAL |
RTEMS_PRIORITY`.

Some combinatinos of these attributes are invalid. For example, priority
ordered blocking discipline must be applied to a binary semaphore in order to
use either the priority inheritance or priority ceiling functionality. The
following tree figure illustrates the valid combinations.

```{figure} ../../images/c_user/semaphore_attributes.png
:align: center
:alt: Semaphore Attributes
:width: 90%
```

(building-a-semaphore-obtain-option-set)=

## Building a SEMAPHORE_OBTAIN Option Set

In general, an option is built by a bitwise OR of the desired option
components. The set of valid options for the `rtems_semaphore_obtain`
directive are listed in the following table:

```{eval-rst}
.. list-table::
 :class: rtems-table

 * - ``RTEMS_WAIT``
   - task will wait for semaphore (default)
 * - ``RTEMS_NO_WAIT``
   - task should not wait
```

Option values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list. An option listed as a default is
not required to appear in the list, although it is a good programming practice
to specify default options. If all defaults are desired, the option
`RTEMS_DEFAULT_OPTIONS` should be specified on this call.

This example demonstrates the option parameter needed to poll for a semaphore.
The option parameter passed to the `rtems_semaphore_obtain` directive should
be `RTEMS_NO_WAIT`.
