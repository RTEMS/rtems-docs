.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Key Concepts
************

Introduction
============

The facilities provided by RTEMS are built upon a foundation of very powerful
concepts.  These concepts must be understood before the application developer
can efficiently utilize RTEMS.  The purpose of this chapter is to familiarize
one with these concepts.

.. _objects:

.. index:: objects

Objects
=======

RTEMS provides directives which can be used to dynamically create, delete, and
manipulate a set of predefined object types.  These types include tasks,
message queues, semaphores, memory regions, memory partitions, timers, ports,
and rate monotonic periods.  The object-oriented nature of RTEMS encourages the
creation of modular applications built upon re-usable "building block"
routines.

All objects are created on the local node as required by the application and
have an RTEMS assigned ID.  All objects have a user-assigned name.  Although a
relationship exists between an object's name and its RTEMS assigned ID, the
name and ID are not identical.  Object names are completely arbitrary and
selected by the user as a meaningful "tag" which may commonly reflect the
object's use in the application.  Conversely, object IDs are designed to
facilitate efficient object manipulation by the executive.

.. index:: object name
.. index:: rtems_name

Object Names
------------

An object name is an unsigned thirty-two bit entity associated with the object
by the user.  The data type ``rtems_name`` is used to store object
names.

.. index:: rtems_build_name

Although not required by RTEMS, object names are often composed of four ASCII
characters which help identify that object.  For example, a task which causes a
light to blink might be called "LITE".  The ``rtems_build_name`` routine is
provided to build an object name from four ASCII characters.  The following
example illustrates this:

.. code-block:: c

    rtems_name my_name;
    my_name = rtems_build_name( 'L', 'I', 'T', 'E' );

However, it is not required that the application use ASCII characters to build
object names.  For example, if an application requires one-hundred tasks, it
would be difficult to assign meaningful ASCII names to each task.  A more
convenient approach would be to name them the binary values one through
one-hundred, respectively.

.. index:: rtems_object_get_name

RTEMS provides a helper routine, ``rtems_object_get_name``, which can be used
to obtain the name of any RTEMS object using just its ID.  This routine
attempts to convert the name into a printable string.

The following example illustrates the use of this method to print an object
name:

.. code-block:: c

    #include <rtems.h>
    #include <rtems/bspIo.h>
    void print_name(rtems_id id)
    {
        char  buffer[10];   /* name assumed to be 10 characters or less */
        char *result;
        result = rtems_object_get_name( id, sizeof(buffer), buffer );
        printk( "ID=0x%08x name=%s\n", id, ((result) ? result : "no name") );
    }

.. index:: object ID
.. index:: object ID composition
.. index:: rtems_id

Object IDs
----------

An object ID is a unique unsigned integer value which uniquely identifies an
object instance.  Object IDs are passed as arguments to many directives in
RTEMS and RTEMS translates the ID to an internal object pointer. The efficient
manipulation of object IDs is critical to the performance of RTEMS services.
Because of this, there are two object Id formats defined.  Each target
architecture specifies which format it will use.  There is a thirty-two bit
format which is used for most of the supported architectures and supports
multiprocessor configurations.  There is also a simpler sixteen bit format
which is appropriate for smaller target architectures and does not support
multiprocessor configurations.

Thirty-Two Object ID Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The thirty-two bit format for an object ID is composed of four parts: API,
object class, node, and index.  The data type ``rtems_id`` is used to store
object IDs.

.. code-block:: c

    31      27 26   24 23          16 15                             0
    +---------+-------+--------------+-------------------------------+
    |         |       |              |                               |
    |  Class  |  API  |     Node     |             Index             |
    |         |       |              |                               |
    +---------+-------+--------------+-------------------------------+

The most significant five bits are the object class.  The next three bits
indicate the API to which the object class belongs.  The next eight bits
(16-23) are the number of the node on which this object was created.  The node
number is always one (1) in a single processor system.  The least significant
sixteen bits form an identifier within a particular object type.  This
identifier, called the object index, ranges in value from 1 to the maximum
number of objects configured for this object type.

Sixteen Bit Object ID Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sixteen bit format for an object ID is composed of three parts: API, object
class, and index.  The data type ``rtems_id`` is used to store object IDs.

.. code-block:: c

    15      11 10    8 7            0
    +---------+-------+--------------+
    |         |       |              |
    |  Class  |  API  |    Index     |
    |         |       |              |
    +---------+-------+--------------+

The sixteen-bit format is designed to be as similar as possible to the
thrity-two bit format.  The differences are limited to the eliminatation of the
node field and reduction of the index field from sixteen-bits to 8-bits.  Thus
the sixteen bit format only supports up to 255 object instances per API/Class
combination and single processor systems.  As this format is typically utilized
by sixteen-bit processors with limited address space, this is more than enough
object instances.

Object ID Description
---------------------

The components of an object ID make it possible to quickly locate any object in
even the most complicated multiprocessor system.  Object ID's are associated
with an object by RTEMS when the object is created and the corresponding ID is
returned by the appropriate object create directive.  The object ID is required
as input to all directives involving objects, except those which create an
object or obtain the ID of an object.

The object identification directives can be used to dynamically obtain a
particular object's ID given its name.  This mapping is accomplished by
searching the name table associated with this object type.  If the name is
non-unique, then the ID associated with the first occurrence of the name will
be returned to the application.  Since object IDs are returned when the object
is created, the object identification directives are not necessary in a
properly designed single processor application.

In addition, services are provided to portably examine the subcomponents of an
RTEMS ID.  These services are described in detail later in this manual but are
prototyped as follows:

.. index:: obtaining class from object ID
.. index:: obtaining node from object ID
.. index:: obtaining index from object ID
.. index:: get class from object ID
.. index:: get node from object ID
.. index:: get index from object ID
.. index:: rtems_object_id_get_api
.. index:: rtems_object_id_get_class
.. index:: rtems_object_id_get_node
.. index:: rtems_object_id_get_index

.. code-block:: c

    uint32_t rtems_object_id_get_api( rtems_id );
    uint32_t rtems_object_id_get_class( rtems_id );
    uint32_t rtems_object_id_get_node( rtems_id );
    uint32_t rtems_object_id_get_index( rtems_id );

An object control block is a data structure defined by RTEMS which contains the
information necessary to manage a particular object type.  For efficiency
reasons, the format of each object type's control block is different.  However,
many of the fields are similar in function.  The number of each type of control
block is application dependent and determined by the values specified in the
user's Configuration Table.  An object control block is allocated at object
create time and freed when the object is deleted.  With the exception of user
extension routines, object control blocks are not directly manipulated by user
applications.

.. index:: communication and synchronization

Communication and Synchronization
=================================

In real-time multitasking applications, the ability for cooperating execution
threads to communicate and synchronize with each other is imperative.  A
real-time executive should provide an application with the following
capabilities:

- Data transfer between cooperating tasks

- Data transfer between tasks and ISRs

- Synchronization of cooperating tasks

- Synchronization of tasks and ISRs

Most RTEMS managers can be used to provide some form of communication and/or
synchronization.  However, managers dedicated specifically to communication and
synchronization provide well established mechanisms which directly map to the
application's varying needs.  This level of flexibility allows the application
designer to match the features of a particular manager with the complexity of
communication and synchronization required.  The following managers were
specifically designed for communication and synchronization:

- Semaphore

- Message Queue

- Event

- Signal

The semaphore manager supports mutual exclusion involving the synchronization
of access to one or more shared user resources.  Binary semaphores may utilize
the optional priority inheritance algorithm to avoid the problem of priority
inversion.  The message manager supports both communication and
synchronization, while the event manager primarily provides a high performance
synchronization mechanism.  The signal manager supports only asynchronous
communication and is typically used for exception handling.

.. index:: locking protocols

Locking Protocols
=================

RTEMS supports the four locking protocols

* :ref:`PriorityCeiling`,

* :ref:`PriorityInheritance`,

* :ref:`MrsP`, and

* :ref:`OMIP`

for synchronization objects providing mutual-exclusion (mutex).  The OMIP is
only available in SMP configurations and replaces the priority inheritance
protocol in this case.  One aim of the locking protocols is to avoid priority
inversion.

Since RTEMS 5.1, priority updates due to the locking protocols take place
immediately and are propagated recursively.  The mutex owner and wait for mutex
relationships define a directed acyclic graph (DAG).  The run-time of the mutex
obtain, release and timeout operations depend on the complexity of this
resource dependency graph.

.. index:: priority inversion

.. _PriorityInversion:

Priority Inversion
------------------

Priority inversion is a form of indefinite postponement which is common in
multitasking, preemptive executives with shared resources.  Priority inversion
occurs when a high priority tasks requests access to shared resource which is
currently allocated to a low priority task.  The high priority task must block
until the low priority task releases the resource.  This problem is exacerbated
when the low priority task is prevented from executing by one or more medium
priority tasks.  Because the low priority task is not executing, it cannot
complete its interaction with the resource and release that resource.  The high
priority task is effectively prevented from executing by lower priority tasks.

.. index:: priority ceiling protocol
.. index:: immediate ceiling priority protocol

.. _PriorityCeiling:

Immediate Ceiling Priority Protocol (ICPP)
------------------------------------------

Each mutex using the Immediate Ceiling Priority Protocol (ICPP) has a ceiling
priority.  The priority of the mutex owner is immediately raised to the ceiling
priority of the mutex.  In case the thread owning the mutex releases the mutex,
then the normal priority of the thread is restored.  This locking protocol is
beneficial for schedulability analysis, see also
:cite:`Burns:2001:RealTimeSystems`.

This protocol avoids the possibility of changing the priority of the mutex
owner multiple times since the ceiling priority must be set to the one of
highest priority thread which will ever attempt to acquire that mutex.  This
requires an overall knowledge of the application as a whole.  The need to
identify the highest priority thread which will attempt to obtain a particular
mutex can be a difficult task in a large, complicated system.  Although the
priority ceiling protocol is more efficient than the priority inheritance
protocol with respect to the maximum number of thread priority changes which
may occur while a thread owns a particular mutex, the priority inheritance
protocol is more forgiving in that it does not require this apriori
information.

.. index:: priority inheritance protocol

.. _PriorityInheritance:

Priority Inheritance Protocol
-----------------------------

The priority of the mutex owner is raised to the highest priority of all
threads that currently wait for ownership of this mutex :cite:`Sha:1990:PI`.
Since RTEMS 5.1, priority updates due to the priority inheritance protocol
take place immediately and are propagated recursively.

.. index:: Multiprocessor Resource Sharing Protocol (MrsP)

.. _MrsP:

Multiprocessor Resource Sharing Protocol (MrsP)
-----------------------------------------------

The Multiprocessor Resource Sharing Protocol (MrsP) is a generalization of the
priority ceiling protocol to clustered scheduling :cite:`Burns:2013:MrsP`.  One
of the design goals of MrsP is to enable an effective schedulability analysis
using the sporadic task model.  Each mutex using the MrsP has a ceiling
priority for each scheduler instance.  The priority of the mutex owner is
immediately raised to the ceiling priority of the mutex defined for its home
scheduler instance.  In case the thread owning the mutex releases the mutex,
then the normal priority of the thread is restored.  Threads that wait for
mutex ownership are not blocked with respect to the scheduler and instead
perform a busy wait.  The MrsP uses temporary thread migrations to foreign
scheduler instances in case of a preemption of the mutex owner.  This locking
protocol is available since RTEMS 4.11. It was re-implemented in RTEMS 5.1 to
overcome some shortcomings of the original implementation
:cite:`Catellani:2015:MrsP`.

.. index:: O(m) Independence-Preserving Protocol (OMIP)

.. _OMIP:

O(m) Independence-Preserving Protocol (OMIP)
----------------------------------------------------

The :math:`O(m)` Independence-Preserving Protocol (OMIP) is a generalization of
the priority inheritance protocol to clustered scheduling which avoids the
non-preemptive sections present with priority boosting
:cite:`Brandenburg:2013:OMIP`.  The :math:`m` denotes the number of processors
in the system.  Similar to the uni-processor priority inheritance protocol, the
OMIP mutexes do not need any external configuration data, e.g. a ceiling
priority.  This makes them a good choice for general purpose libraries that
need internal locking.  The complex part of the implementation is contained in
the thread queues and shared with the MrsP support.  This locking protocol is
available since RTEMS 5.1.

.. index:: thread queues

Thread Queues
=============

In case more than one :term:`thread` may wait on a synchronization object, e.g.
a semaphore or a message queue, then the waiting threads are added to a data
structure called the thread queue.  Thread queues are named task wait queues in
the Classic API.  There are two thread queuing disciplines available which
define the order of the threads on a particular thread queue.  Threads can wait
in FIFO or priority order.

In uni-processor configurations, the priority queuing discipline just orders
the threads according to their current priority and in FIFO order in case of
equal priorities.  However, in SMP configurations, the situation is a bit more
difficult due to the support for clustered scheduling.  It makes no sense to
compare the priority values of two different scheduler instances.  Thus, it is
impossible to simply use one plain priority queue for threads of different
clusters.  Two levels of queues can be used as one way to solve the problem.
The top-level queue provides FIFO ordering and contains priority queues.  Each
priority queue is associated with a scheduler instance and contains only
threads of this scheduler instance.  Threads are enqueued in the priority
queues corresponding to their scheduler instances.  To dequeue a thread, the
highest priority thread of the first priority queue is selected.  Once this is
done, the first priority queue is appended to the top-level FIFO queue.  This
guarantees fairness with respect to the scheduler instances.

Such a two-level queue needs a considerable amount of memory if fast enqueue
and dequeue operations are desired.  Providing this storage per thread queue
would waste a lot of memory in typical applications.  Instead, each thread has
a queue attached which resides in a dedicated memory space independent of other
memory used for the thread (this approach was borrowed from FreeBSD).  In case
a thread needs to block, there are two options

* the object already has a queue, then the thread enqueues itself to this
  already present queue and the queue of the thread is added to a list of free
  queues for this object, or

* otherwise, the queue of the thread is given to the object and the thread
  enqueues itself to this queue.

In case the thread is dequeued, there are two options

* the thread is the last thread in the queue, then it removes this queue
  from the object and reclaims it for its own purpose, or

* otherwise, the thread removes one queue from the free list of the object
  and reclaims it for its own purpose.

Since there are usually more objects than threads, this actually reduces the
memory demands.  In addition the objects only contain a pointer to the queue
structure.  This helps to hide implementation details.  Inter-cluster priority
queues are available since RTEMS 5.1.

A doubly-linked list (chain) is used to implement the FIFO queues yielding a
:math:`O(1)` worst-case time complexity for enqueue and dequeue operations.

A red-black tree is used to implement the priority queues yielding a
:math:`O(log(n))` worst-case time complexity for enqueue and dequeue operations
with :math:`n` being the count of threads already on the queue.

.. index:: time

Time
====

The development of responsive real-time applications requires an understanding
of how RTEMS maintains and supports time-related operations.  The basic unit of
time in RTEMS is known as a `clock tick` or simply `tick`.  The tick interval
is defined by the application configuration option
:ref:`CONFIGURE_MICROSECONDS_PER_TICK <CONFIGURE_MICROSECONDS_PER_TICK>`.  The
tick interval defines the basic resolution of all interval and calendar time
operations.  Obviously, the directives which use intervals or wall time cannot
operate without some external mechanism which provides a periodic clock tick.
This clock tick is provided by the clock driver.  The tick precision and
stability depends on the clock driver and interrupt latency.  Most clock
drivers provide a timecounter to measure the time with a higher resolution than
the tick.

.. index:: rtems_interval

By tracking time in units of ticks, RTEMS is capable of supporting interval
timing functions such as task delays, timeouts, timeslicing, the delayed
execution of timer service routines, and the rate monotonic scheduling of
tasks.  An interval is defined as a number of ticks relative to the current
time.  For example, when a task delays for an interval of ten ticks, it is
implied that the task will not execute until ten clock ticks have occurred.
All intervals are specified using data type :c:type:`rtems_interval`.

A characteristic of interval timing is that the actual interval period may be a
fraction of a tick less than the interval requested.  This occurs because the
time at which the delay timer is set up occurs at some time between two clock
ticks.  Therefore, the first countdown tick occurs in less than the complete
time interval for a tick.  This can be a problem if the tick resolution is
large.

The rate monotonic scheduling algorithm is a hard real-time scheduling
methodology.  This methodology provides rules which allows one to guarantee
that a set of independent periodic tasks will always meet their deadlines even
under transient overload conditions.  The rate monotonic manager provides
directives built upon the Clock Manager's interval timer support routines.

Interval timing is not sufficient for the many applications which require that
time be kept in wall time or true calendar form.  Consequently, RTEMS maintains
the current date and time.  This allows selected time operations to be
scheduled at an actual calendar date and time.  For example, a task could
request to delay until midnight on New Year's Eve before lowering the ball at
Times Square.  The data type :c:type:`rtems_time_of_day` is used to specify calendar
time in RTEMS services.  See :ref:`Time and Date Data Structures`.

.. index:: rtems_time_of_day

Timer and Timeouts
==================

Timer and timeout services are a standard component of an operating system.
The use cases fall roughly into two categories:

* Timeouts -- used to detect if some operations need more time than expected.
  Since the unexpected happens hopefully rarely, timeout timers are usually
  removed before they expire. The critical operations are insert and removal.
  For example, they are important for the performance of a network stack.

* Timers -- used to carry out some work in the future. They usually expire
  and need a high resolution. An example use case is a time driven scheduler,
  e.g.  rate-monotonic or EDF.

In RTEMS versions prior to 5.1 the timer and timeout support was implemented
by means of delta chains.  This implementation was unfit for SMP systems due to
several reasons.  The new implementation present since RTEMS 5.1 uses a
red-black tree with the expiration time as the key.  This leads to
:math:`O(log(n))` worst-case insert and removal operations for :math:`n` active
timer or timeouts.  Each processor provides its own timer and timeout service
point so that it scales well with the processor count of the system.  For each
operation it is sufficient to acquire and release a dedicated SMP lock only
once. The drawback is that a 64-bit integer type is required internally for the
intervals to avoid a potential overflow of the key values.

An alternative to the red-black tree based implementation would be the use of a
timer wheel based algorithm :cite:`Varghese:1987:TimerWheel` which is used in
Linux and FreeBSD :cite:`Varghese:1995:BSDCallout` for example.  A timer wheel
based algorithm offers :math:`O(1)` worst-case time complexity for insert and
removal operations.  The drawback is that the run-time of the clock tick
procedure is unpredictable due to the use of a hash table or cascading.

The red-black tree approach was selected for RTEMS, since it offers a more
predictable run-time behaviour.  However, this sacrifices the constant insert
and removal operations offered by the timer wheel algorithms.  See also
:cite:`Gleixner:2006:Hrtimers`.  The implementation can re-use the red-black
tree support already used in other areas, e.g. for the thread priority queues.
Less code is a good thing for size, testing and verification.

.. index:: memory management

Memory Management
=================

RTEMS memory management facilities can be grouped into two classes: dynamic
memory allocation and address translation.  Dynamic memory allocation is
required by applications whose memory requirements vary through the
application's course of execution.  Address translation is needed by
applications which share memory with another CPU or an intelligent Input/Output
processor.  The following RTEMS managers provide facilities to manage memory:

- Region

- Partition

- Dual Ported Memory

RTEMS memory management features allow an application to create simple memory
pools of fixed size buffers and/or more complex memory pools of variable size
segments.  The partition manager provides directives to manage and maintain
pools of fixed size entities such as resource control blocks.  Alternatively,
the region manager provides a more general purpose memory allocation scheme
that supports variable size blocks of memory which are dynamically obtained and
freed by the application.  The dual-ported memory manager provides executive
support for address translation between internal and external dual-ported RAM
address space.
