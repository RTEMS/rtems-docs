.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. index:: Stack Bounds Checker
.. index:: stack

Stack Bounds Checker
********************

Introduction
============

The stack bounds checker is an RTEMS support component that determines if a
task has overrun its run-time stack.  The routines provided by the stack bounds
checker manager are:

- rtems_stack_checker_is_blown_ - Has the Current Task Blown its Stack

- rtems_stack_checker_report_usage_ - Report Task Stack Usage

Background
==========

Task Stack
----------

Each task in a system has a fixed size stack associated with it.  This stack is
allocated when the task is created.  As the task executes, the stack is used to
contain parameters, return addresses, saved registers, and local variables.
The amount of stack space required by a task is dependent on the exact set of
routines used.  The peak stack usage reflects the worst case of subroutine
pushing information on the stack.  For example, if a subroutine allocates a
local buffer of 1024 bytes, then this data must be accounted for in the stack
of every task that invokes that routine.

Recursive routines make calculating peak stack usage difficult, if not
impossible.  Each call to the recursive routine consumes *n* bytes of stack
space.  If the routine recursives 1000 times, then ``1000 * n`` bytes of
stack space are required.

Execution
---------

The stack bounds checker operates as a set of task extensions.  At task
creation time, the task's stack is filled with a pattern to indicate the stack
is unused.  As the task executes, it will overwrite this pattern in memory.  At
each task switch, the stack bounds checker's task switch extension is executed.
This extension checks that:

- the last ``n`` bytes of the task's stack have not been overwritten.  If this
  pattern has been damaged, it indicates that at some point since this task was
  context switch to the CPU, it has used too much stack space.

- the current stack pointer of the task is not within the address range
  allocated for use as the task's stack.

If either of these conditions is detected, then a blown stack error is reported
using the ``printk`` routine.

The number of bytes checked for an overwrite is processor family dependent.
The minimum stack frame per subroutine call varies widely between processor
families.  On CISC families like the Motorola MC68xxx and Intel ix86, all that
is needed is a return address.  On more complex RISC processors, the minimum
stack frame per subroutine call may include space to save a significant number
of registers.

Another processor dependent feature that must be taken into account by the
stack bounds checker is the direction that the stack grows.  On some processor
families, the stack grows up or to higher addresses as the task executes.  On
other families, it grows down to lower addresses.  The stack bounds checker
implementation uses the stack description definitions provided by every RTEMS
port to get for this information.

Operations
==========

Initializing the Stack Bounds Checker
-------------------------------------

The stack checker is initialized automatically when its task create extension
runs for the first time.

The application must include the stack bounds checker extension set in its set
of Initial Extensions.  This set of extensions is defined as
``STACK_CHECKER_EXTENSION``.  If using ``<rtems/confdefs.h>`` for Configuration
Table generation, then all that is necessary is to define the macro
``CONFIGURE_STACK_CHECKER_ENABLED`` before including ``<rtems/confdefs.h>`` as
shown below:

.. code-block:: c

    #define CONFIGURE_STACK_CHECKER_ENABLED
    ...
    #include <rtems/confdefs.h>

Checking for Blown Task Stack
-----------------------------

The application may check whether the stack pointer of currently executing task
is within proper bounds at any time by calling the
``rtems_stack_checker_is_blown`` method.  This method return ``FALSE`` if the
task is operating within its stack bounds and has not damaged its pattern area.

Reporting Task Stack Usage
--------------------------

The application may dynamically report the stack usage for every task in the
system by calling the ``rtems_stack_checker_report_usage`` routine.  This
routine prints a table with the peak usage and stack size of every task in the
system.  The following is an example of the report generated:

.. code-block:: c

    ID      NAME       LOW        HIGH     AVAILABLE      USED
    0x04010001  IDLE  0x003e8a60  0x003e9667       2952        200
    0x08010002  TA1   0x003e5750  0x003e7b57       9096       1168
    0x08010003  TA2   0x003e31c8  0x003e55cf       9096       1168
    0x08010004  TA3   0x003e0c40  0x003e3047       9096       1104
    0xffffffff  INTR  0x003ecfc0  0x003effbf      12160        128

Notice the last line.  The task id is ``0xffffffff`` and its name is ``INTR``.
This is not actually a task, it is the interrupt stack.

When a Task Overflows the Stack
-------------------------------

When the stack bounds checker determines that a stack overflow has occurred, it
will attempt to print a message using ``printk`` identifying the task and then
shut the system down.  If the stack overflow has caused corruption, then it is
possible that the message cannot be printed.

The following is an example of the output generated:

.. code-block:: c

    BLOWN STACK!!! Offending task(0x3eb360): id=0x08010002; name=0x54413120
    stack covers range 0x003e5750 - 0x003e7b57 (9224 bytes)
    Damaged pattern begins at 0x003e5758 and is 128 bytes long

The above includes the task id and a pointer to the task control block as well
as enough information so one can look at the task's stack and see what was
happening.

Routines
========

This section details the stack bounds checker's routines.  A subsection is
dedicated to each of routines and describes the calling sequence, related
constants, usage, and status codes.

.. COMMENT: rtems_stack_checker_is_blown

.. _rtems_stack_checker_is_blown:

STACK_CHECKER_IS_BLOWN - Has Current Task Blown Its Stack
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        bool rtems_stack_checker_is_blown( void );

STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``TRUE``
       - Stack is operating within its stack limits
     * - ``FALSE``
       - Current stack pointer is outside allocated area

DESCRIPTION:
    This method is used to determine if the current stack pointer of the
    currently executing task is within bounds.

NOTES:
    This method checks the current stack pointer against the high and low
    addresses of the stack memory allocated when the task was created and it
    looks for damage to the high water mark pattern for the worst case usage of
    the task being called.

.. _rtems_stack_checker_report_usage:

STACK_CHECKER_REPORT_USAGE - Report Task Stack Usage
----------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_stack_checker_report_usage( void );

STATUS CODES:
    NONE

DESCRIPTION:
    This routine prints a table with the peak stack usage and stack space
    allocation of every task in the system.

NOTES:
    NONE
