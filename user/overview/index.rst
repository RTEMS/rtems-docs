
.. _overview:

Overview
=========

Welcome to the :ref:term:`RTEMS` User Manual.

This document covers all the topics required as a user of RTEMS to use the
RTEMS operating system.

RTEMS, Real-Time Executive for Multiprocessor Systems, is a real-time executive
(kernel) which provides a high performance environment for embedded
applications including the following features:

.. sidebar:: Developers

  Developers should look at the :r:url:`devel` for technical information. The
  design and development of RTEMS is located there.

- multitasking capabilities

- homogeneous and heterogeneous multiprocessor systems

- event-driven, priority-based, preemptive scheduling

- optional rate monotonic scheduling

- intertask communication and synchronization

- priority inheritance

- responsive interrupt management

- dynamic memory allocation

- high level of user configurability

RTEMS provides features found in modern operating systems:

- file systems

- networking

- USB

- permanent media such as flash disks, cards and USB devices

Real-time Application Systems
=============================

Real-time application systems are a special class of computer applications.
They have a complex set of characteristics that distinguish them from other
software problems.  Generally, they must adhere to more rigorous requirements.
The correctness of the system depends not only on the results of computations,
but also on the time at which the results are produced.  The most important and
complex characteristic of real-time application systems is that they must
receive and respond to a set of external stimuli within rigid and critical time
constraints referred to as deadlines.  Systems can be buried by an avalanche of
interdependent, asynchronous or cyclical event streams.

Deadlines can be further characterized as either hard or soft based upon the
value of the results when produced after the deadline has passed.  A deadline
is hard if the results have no value after the deadline has passed, or a
catastophic event results from their intended use if not completed on time.  In
contrast, results produced after a soft deadline may still have some value.

Another distinguishing requirement of real-time application systems is the
ability to coordinate or manage a large number of concurrent activities. Since
software is a synchronous entity, this presents special problems.  One
instruction follows another in a repeating synchronous cycle.  Even though
mechanisms have been developed to allow for the processing of external
asynchronous events, the software design efforts required to process and manage
these events and tasks are growing more complicated.

The design process is complicated further by spreading this activity over a set
of processors instead of a single processor. The challenges associated with
designing and building real-time application systems become very complex when
multiple processors are involved.  New requirements such as interprocessor
communication channels and global resources that must be shared between
competing processors are introduced.  The ramifications of multiple processors
complicate each and every characteristic of a real-time system.

Real-time Executive
===================

Fortunately, real-time operating systems, or real-time executives, serve as a
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

By properly grouping stimuli responses into separate tasks a system can now
asynchronously switch between independent streams of execution. This allows the
system to directly respond to external stimuli as they occur, as well as meet
critical performance specifications that are typically measured by guaranteed
response time and transaction throughput.  The multiprocessor extensions of
RTEMS provide the features necessary to manage the extra requirements
introduced by a system distributed across several processors.  It removes the
physical barriers of processor boundaries from the world of the system
designer, enabling more critical aspects of the system to receive the required
attention. Such a system, based on an efficient real-time, multiprocessor
executive, is a more realistic model of the outside world or environment for
which it is designed.  As a result, the system will always be more logical,
efficient, and reliable.

By using the directives provided by RTEMS, the real-time applications developer
is freed from the problem of controlling and synchronizing multiple tasks and
processors.  In addition, one need not develop, test, debug, and document
routines to manage memory, pass messages, or provide mutual exclusion.  The
developer is then able to concentrate solely on the application.  By using
standard software components, the time and cost required to develop
sophisticated real-time applications is significantly reduced.

Open Source
===========

RTEMS is an open source operating system and an open source project. As a user,
you have access to all the source code. We encourage you to work with the
source code and integrate the provided processes used to build tools, the
kernel and any 3rd party libraries into your project's configuration management
processes. The RTEMS project is always improving the way it develivers the
kernel to you and so your feedback is important.

What we used in the RTEMS project to develop and maintain RTEMS does not
dictate what you use to develop and maintain your project. You can, and should,
select the work-flow that best suites the demands of your project and what you
are delivering.
