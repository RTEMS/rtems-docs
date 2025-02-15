Real-time Executive
===================

Fortunately, real-time operating systems or real-time executives serve as a
cornerstone on which to build the application system.  A real-time multitasking
executive allows an application to be cast into a set of logical, autonomous
processes or tasks which become quite manageable.  Each task is internally
synchronous, but different tasks execute independently, resulting in an
asynchronous processing stream.  Tasks can be dynamically paused for many
reasons resulting in a different task being allowed to execute for a period of
time.  The executive also provides an interface to other system components such
as interrupt handlers and device drivers.  System components may request the
executive to allocate and coordinate resources, and to wait for and trigger
synchronizing conditions.  The executive system calls effectively extend the
CPU instruction set to support efficient multitasking.  By causing tasks to
travel through well-defined state transitions, system calls permit an
application to demand-switch between tasks in response to real-time events.

By proper grouping of responses to stimuli into separate tasks, a system can
now asynchronously switch between independent streams of execution, directly
responding to external stimuli as they occur.  This allows the system design to
meet critical performance specifications which are typically measured by
guaranteed response time and transaction throughput.  The multiprocessor
extensions of RTEMS provide the features necessary to manage the extra
requirements introduced by a system distributed across several processors.  It
removes the physical barriers of processor boundaries from the world of the
system designer, enabling more critical aspects of the system to receive the
required attention. Such a system, based on an efficient real-time,
multiprocessor executive, is a more realistic model of the outside world or
environment for which it is designed.  As a result, the system will always be
more logical, efficient, and reliable.

By using the directives provided by RTEMS, the real-time applications developer
is freed from the problem of controlling and synchronizing multiple tasks and
processors.  In addition, one need not develop, test, debug, and document
routines to manage memory, pass messages, or provide mutual exclusion.  The
developer is then able to concentrate solely on the application.  By using
standard software components, the time and cost required to develop
sophisticated real-time applications is significantly reduced.