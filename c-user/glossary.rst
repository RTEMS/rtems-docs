.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Glossary
********

:dfn:`active`
    A term used to describe an object which has been created by an application.

:dfn:`aperiodic task`
    A task which must execute only at irregular intervals and has only a soft
    deadline.

:dfn:`application`
    In this document, software which makes use of RTEMS.

:dfn:`ASR`
    see Asynchronous Signal Routine.

:dfn:`asynchronous`
    Not related in order or timing to other occurrences in the system.

:dfn:`Asynchronous Signal Routine`
    Similar to a hardware interrupt except that it is associated with a task
    and is run in the context of a task.  The directives provided by the signal
    manager are used to service signals.

:dfn:`atomic operations`
    Atomic operations are defined in terms of *ISO/IEC 9899:2011*.

:dfn:`awakened`
    A term used to describe a task that has been unblocked and may be scheduled
    to the CPU.

:dfn:`big endian`
    A data representation scheme in which the bytes composing a numeric value
    are arranged such that the most significant byte is at the lowest address.

:dfn:`bit-mapped`
    A data encoding scheme in which each bit in a variable is used to represent
    something different.  This makes for compact data representation.

:dfn:`block`
    A physically contiguous area of memory.

:dfn:`blocked task`
    The task state entered by a task which has been previously started and
    cannot continue execution until the reason for waiting has been satisfied.
    Blocked tasks are not an element of the set of ready tasks of a scheduler
    instance.

:dfn:`broadcast`
    To simultaneously send a message to a logical set of destinations.

:dfn:`BSP`
    see Board Support Package.

:dfn:`Board Support Package`
    A collection of device initialization and control routines specific to a
    particular type of board or collection of boards.

:dfn:`buffer`
    A fixed length block of memory allocated from a partition.

:dfn:`calling convention`
    The processor and compiler dependent rules which define the mechanism used
    to invoke subroutines in a high-level language.  These rules define the
    passing of arguments, the call and return mechanism, and the register set
    which must be preserved.

:dfn:`Central Processing Unit`
    This term is equivalent to the terms processor and microprocessor.

:dfn:`chain`
    A data structure which allows for efficient dynamic addition and removal of
    elements.  It differs from an array in that it is not limited to a
    predefined size.

:dfn:`cluster`
    We have clustered scheduling in case the set of processors of a system is
    partitioned into non-empty pairwise disjoint subsets.  These subsets are
    called:dfn:`clusters`.  Clusters with a cardinality of one are partitions.
    Each cluster is owned by exactly one scheduler instance.

:dfn:`coalesce`
    The process of merging adjacent holes into a single larger hole.  Sometimes
    this process is referred to as garbage collection.

:dfn:`Configuration Table`
    A table which contains information used to tailor RTEMS for a particular
    application.

:dfn:`context`
    All of the processor registers and operating system data structures
    associated with a task.

:dfn:`context switch`
    Alternate term for task switch.  Taking control of the processor from one
    task and transferring it to another task.

:dfn:`control block`
    A data structure used by the executive to define and control an object.

:dfn:`core`
    When used in this manual, this term refers to the internal executive
    utility functions.  In the interest of application portability, the core of
    the executive should not be used directly by applications.

:dfn:`CPU`
    An acronym for Central Processing Unit.

:dfn:`critical section`
    A section of code which must be executed indivisibly.

:dfn:`CRT`
    An acronym for Cathode Ray Tube.  Normally used in reference to the
    man-machine interface.

:dfn:`deadline`
    A fixed time limit by which a task must have completed a set of actions.
    Beyond this point, the results are of reduced value and may even be
    considered useless or harmful.

:dfn:`device`
    A peripheral used by the application that requires special operation
    software.  See also device driver.

:dfn:`device driver`
    Control software for special peripheral devices used by the application.

:dfn:`directives`
    RTEMS' provided routines that provide support mechanisms for real-time
    applications.

:dfn:`dispatch`
    The act of loading a task's context onto the CPU and transferring control
    of the CPU to that task.

:dfn:`dormant`
    The state entered by a task after it is created and before it has been
    started.

:dfn:`Device Driver Table`
    A table which contains the entry points for each of the configured device
    drivers.

:dfn:`dual-ported`
    A term used to describe memory which can be accessed at two different
    addresses.

:dfn:`embedded`
    An application that is delivered as a hidden part of a larger system.  For
    example, the software in a fuel-injection control system is an embedded
    application found in many late-model automobiles.

:dfn:`envelope`
    A buffer provided by the MPCI layer to RTEMS which is used to pass messages
    between nodes in a multiprocessor system.  It typically contains routing
    information needed by the MPCI.  The contents of an envelope are referred
    to as a packet.

:dfn:`entry point`
    The address at which a function or task begins to execute.  In C, the entry
    point of a function is the function's name.

:dfn:`events`
    A method for task communication and synchronization. The directives
    provided by the event manager are used to service events.

:dfn:`exception`
    A synonym for interrupt.

:dfn:`executing task`
    The task state entered by a task after it has been given control of the
    processor.  On SMP configurations a task may be registered as executing on
    more than one processor for short time frames during task migration.
    Blocked tasks can be executing until they issue a thread dispatch.

:dfn:`executive`
    In this document, this term is used to referred to RTEMS.  Commonly, an
    executive is a small real-time operating system used in embedded systems.

:dfn:`exported`
    An object known by all nodes in a multiprocessor system.  An object created
    with the GLOBAL attribute will be exported.

:dfn:`external address`
    The address used to access dual-ported memory by all the nodes in a system
    which do not own the memory.

:dfn:`FIFO`
    An acronym for First In First Out.

:dfn:`First In First Out`
    A discipline for manipulating entries in a data structure.

:dfn:`floating point coprocessor`
    A component used in computer systems to enhance performance in
    mathematically intensive situations.  It is typically viewed as a logical
    extension of the primary processor.

:dfn:`freed`
    A resource that has been released by the application to RTEMS.

:dfn:`global`
    An object that has been created with the GLOBAL attribute and exported to
    all nodes in a multiprocessor system.

:dfn:`handler`
    The equivalent of a manager, except that it is internal to RTEMS and forms
    part of the core.  A handler is a collection of routines which provide a
    related set of functions.  For example, there is a handler used by RTEMS to
    manage all objects.

:dfn:`hard real-time system`
    A real-time system in which a missed deadline causes the worked performed
    to have no value or to result in a catastrophic effect on the integrity of
    the system.

:dfn:`heap`
    A data structure used to dynamically allocate and deallocate variable sized
    blocks of memory.

:dfn:`heir task`
    A task is an :dfn:`heir` if it is registered as an heir in a processor of
    the system.  A task can be the heir on at most one processor in the system.
    In case the executing and heir tasks differ on a processor and a thread
    dispatch is marked as necessary, then the next thread dispatch will make
    the heir task the executing task.

:dfn:`heterogeneous`
    A multiprocessor computer system composed of dissimilar processors.

:dfn:`homogeneous`
    A multiprocessor computer system composed of a single type of processor.

:dfn:`ID`
    An RTEMS assigned identification tag used to access an active object.

:dfn:`IDLE task`
    A special low priority task which assumes control of the CPU when no other
    task is able to execute.

:dfn:`interface`
    A specification of the methodology used to connect multiple independent
    subsystems.

:dfn:`internal address`
    The address used to access dual-ported memory by the node which owns the
    memory.

:dfn:`interrupt`
    A hardware facility that causes the CPU to suspend execution, save its
    status, and transfer control to a specific location.

:dfn:`interrupt level`
    A mask used to by the CPU to determine which pending interrupts should be
    serviced.  If a pending interrupt is below the current interrupt level,
    then the CPU does not recognize that interrupt.

:dfn:`Interrupt Service Routine`
    An ISR is invoked by the CPU to process a pending interrupt.

:dfn:`I/O`
    An acronym for Input/Output.

:dfn:`ISR`
    An acronym for Interrupt Service Routine.

:dfn:`kernel`
    In this document, this term is used as a synonym for executive.

:dfn:`list`
    A data structure which allows for dynamic addition and removal of entries.
    It is not statically limited to a particular size.

:dfn:`little endian`
    A data representation scheme in which the bytes composing a numeric value
    are arranged such that the least significant byte is at the lowest address.

:dfn:`local`
    An object which was created with the LOCAL attribute and is accessible only
    on the node it was created and resides upon.  In a single processor
    configuration, all objects are local.

:dfn:`local operation`
    The manipulation of an object which resides on the same node as the calling
    task.

:dfn:`logical address`
    An address used by an application.  In a system without memory management,
    logical addresses will equal physical addresses.

:dfn:`loosely-coupled`
    A multiprocessor configuration where shared memory is not used for
    communication.

:dfn:`major number`
    The index of a device driver in the Device Driver Table.

:dfn:`manager`
    A group of related RTEMS' directives which provide access and control over
    resources.

:dfn:`memory pool`
    Used interchangeably with heap.

:dfn:`message`
    A sixteen byte entity used to communicate between tasks.  Messages are sent
    to message queues and stored in message buffers.

:dfn:`message buffer`
    A block of memory used to store messages.

:dfn:`message queue`
    An RTEMS object used to synchronize and communicate between tasks by
    transporting messages between sending and receiving tasks.

:dfn:`Message Queue Control Block`
    A data structure associated with each message queue used by RTEMS to manage
    that message queue.

:dfn:`minor number`
    A numeric value passed to a device driver, the exact usage of which is
    driver dependent.

:dfn:`mode`
    An entry in a task's control block that is used to determine if the task
    allows preemption, timeslicing, processing of signals, and the interrupt
    disable level used by the task.

:dfn:`MPCI`
    An acronym for Multiprocessor Communications Interface Layer.

:dfn:`multiprocessing`
    The simultaneous execution of two or more processes by a multiple processor
    computer system.

:dfn:`multiprocessor`
    A computer with multiple CPUs available for executing applications.

:dfn:`Multiprocessor Communications Interface Layer`
    A set of user-provided routines which enable the nodes in a multiprocessor
    system to communicate with one another.

:dfn:`Multiprocessor Configuration Table`
    The data structure defining the characteristics of the multiprocessor
    target system with which RTEMS will communicate.

:dfn:`multitasking`
    The alternation of execution amongst a group of processes on a single CPU.
    A scheduling algorithm is used to determine which process executes at which
    time.

:dfn:`mutual exclusion`
    A term used to describe the act of preventing other tasks from accessing a
    resource simultaneously.

:dfn:`nested`
    A term used to describe an ASR that occurs during another ASR or an ISR
    that occurs during another ISR.

:dfn:`node`
    A term used to reference a processor running RTEMS in a multiprocessor
    system.

:dfn:`non-existent`
    The state occupied by an uncreated or deleted task.

:dfn:`numeric coprocessor`
    A component used in computer systems to enhance performance in
    mathematically intensive situations.  It is typically viewed as a logical
    extension of the primary processor.

:dfn:`object`
    In this document, this term is used to refer collectively to tasks, timers,
    message queues, partitions, regions, semaphores, ports, and rate monotonic
    periods.  All RTEMS objects have IDs and user-assigned names.

:dfn:`object-oriented`
    A term used to describe systems with common mechanisms for utilizing a
    variety of entities.  Object-oriented systems shield the application from
    implementation details.

:dfn:`operating system`
    The software which controls all the computer's resources and provides the
    base upon which application programs can be written.

:dfn:`overhead`
    The portion of the CPUs processing power consumed by the operating system.

:dfn:`packet`
    A buffer which contains the messages passed between nodes in a
    multiprocessor system.  A packet is the contents of an envelope.

:dfn:`partition`
    An RTEMS object which is used to allocate and deallocate fixed size blocks
    of memory from an dynamically specified area of memory.

:dfn:`partition`
    Clusters with a cardinality of one are :dfn:`partitions`.

:dfn:`Partition Control Block`
    A data structure associated with each partition used by RTEMS to manage
    that partition.

:dfn:`pending`
    A term used to describe a task blocked waiting for an event, message,
    semaphore, or signal.

:dfn:`periodic task`
    A task which must execute at regular intervals and comply with a hard
    deadline.

:dfn:`physical address`
    The actual hardware address of a resource.

:dfn:`poll`
    A mechanism used to determine if an event has occurred by periodically
    checking for a particular status.  Typical events include arrival of data,
    completion of an action, and errors.

:dfn:`pool`
    A collection from which resources are allocated.

:dfn:`portability`
    A term used to describe the ease with which software can be rehosted on
    another computer.

:dfn:`posting`
    The act of sending an event, message, semaphore, or signal to a task.

:dfn:`preempt`
    The act of forcing a task to relinquish the processor and dispatching to
    another task.

:dfn:`priority`
    A mechanism used to represent the relative importance of an element in a
    set of items.  RTEMS uses priority to determine which task should execute.

:dfn:`priority boosting`
    A simple approach to extend the priority inheritance protocol for clustered
    scheduling is :dfn:`priority boosting`.  In case a mutex is owned by a task
    of another cluster, then the priority of the owner task is raised to an
    artificially high priority, the pseudo-interrupt priority.

:dfn:`priority inheritance`
    An algorithm that calls for the lower priority task holding a resource to
    have its priority increased to that of the highest priority task blocked
    waiting for that resource.  This avoids the problem of priority inversion.

:dfn:`priority inversion`
    A form of indefinite postponement which occurs when a high priority tasks
    requests access to shared resource currently allocated to low priority
    task.  The high priority task must block until the low priority task
    releases the resource.

:dfn:`processor utilization`
    The percentage of processor time used by a task or a set of tasks.

:dfn:`proxy`
    An RTEMS control structure used to represent, on a remote node, a task
    which must block as part of a remote operation.

:dfn:`Proxy Control Block`
    A data structure associated with each proxy used by RTEMS to manage that
    proxy.

:dfn:`PTCB`
    An acronym for Partition Control Block.

:dfn:`PXCB`
    An acronym for Proxy Control Block.

:dfn:`quantum`
    The application defined unit of time in which the processor is allocated.

:dfn:`queue`
    Alternate term for message queue.

:dfn:`QCB`
    An acronym for Message Queue Control Block.

:dfn:`ready task`
    A task occupies this state when it is available to be given control of a
    processor.  A ready task has no processor assigned.  The scheduler decided
    that other tasks are currently more important.  A task that is ready to
    execute and has a processor assigned is called scheduled.

:dfn:`real-time`
    A term used to describe systems which are characterized by requiring
    deterministic response times to external stimuli.  The external stimuli
    require that the response occur at a precise time or the response is
    incorrect.

:dfn:`reentrant`
    A term used to describe routines which do not modify themselves or global
    variables.

:dfn:`region`
    An RTEMS object which is used to allocate and deallocate variable size
    blocks of memory from a dynamically specified area of memory.

:dfn:`Region Control Block`
    A data structure associated with each region used by RTEMS to manage that
    region.

:dfn:`registers`
    Registers are locations physically located within a component, typically
    used for device control or general purpose storage.

:dfn:`remote`
    Any object that does not reside on the local node.

:dfn:`remote operation`
    The manipulation of an object which does not reside on the same node as the
    calling task.

:dfn:`return code`
    Also known as error code or return value.

:dfn:`resource`
    A hardware or software entity to which access must be controlled.

:dfn:`resume`
    Removing a task from the suspend state.  If the task's state is ready
    following a call to the ``rtems_task_resume`` directive, then the task is
    available for scheduling.

:dfn:`return code`
    A value returned by RTEMS directives to indicate the completion status of
    the directive.

:dfn:`RNCB`
    An acronym for Region Control Block.

:dfn:`round-robin`
    A task scheduling discipline in which tasks of equal priority are executed
    in the order in which they are made ready.

:dfn:`RS-232`
    A standard for serial communications.

:dfn:`running`
    The state of a rate monotonic timer while it is being used to delineate a
    period.  The timer exits this state by either expiring or being canceled.

:dfn:`schedulable`
    A set of tasks which can be guaranteed to meet their deadlines based upon a
    specific scheduling algorithm.

:dfn:`schedule`
    The process of choosing which task should next enter the executing state.

:dfn:`scheduled task`
    A task is :dfn:`scheduled` if it is allowed to execute and has a processor
    assigned.  Such a task executes currently on a processor or is about to
    start execution.  A task about to start execution it is an heir task on
    exactly one processor in the system.

:dfn:`scheduler`
    A :dfn:`scheduler` or :dfn:`scheduling algorithm` allocates processors to a
    subset of its set of ready tasks.  So it manages access to the processor
    resource.  Various algorithms exist to choose the tasks allowed to use a
    processor out of the set of ready tasks.  One method is to assign each task
    a priority number and assign the tasks with the lowest priority number to
    one processor of the set of processors owned by a scheduler instance.

:dfn:`scheduler instance`
    A :dfn:`scheduler instance` is a scheduling algorithm with a corresponding
    context to store its internal state.  Each processor in the system is owned
    by at most one scheduler instance.  The processor to scheduler instance
    assignment is determined at application configuration time.  See
    :ref:`Configuring a System`.

:dfn:`segments`
    Variable sized memory blocks allocated from a region.

:dfn:`semaphore`
    An RTEMS object which is used to synchronize tasks and provide mutually
    exclusive access to resources.

:dfn:`Semaphore Control Block`
    A data structure associated with each semaphore used by RTEMS to manage
    that semaphore.

:dfn:`shared memory`
    Memory which is accessible by multiple nodes in a multiprocessor system.

:dfn:`signal`
    An RTEMS provided mechanism to communicate asynchronously with a task.
    Upon reception of a signal, the ASR of the receiving task will be invoked.

:dfn:`signal set`
    A thirty-two bit entity which is used to represent a task's collection of
    pending signals and the signals sent to a task.

:dfn:`SMCB`
    An acronym for Semaphore Control Block.

:dfn:`SMP locks`
    The :dfn:`SMP locks` ensure mutual exclusion on the lowest level and are a
    replacement for the sections of disabled interrupts.  Interrupts are
    usually disabled while holding an SMP lock.  They are implemented using
    atomic operations.  Currently a ticket lock is used in RTEMS.

:dfn:`SMP barriers`
    The :dfn:`SMP barriers` ensure that a defined set of independent threads of
    execution on a set of processors reaches a common synchronization point in
    time.  They are implemented using atomic operations.  Currently a sense
    barrier is used in RTEMS.

:dfn:`soft real-time system`
    A real-time system in which a missed deadline does not compromise the
    integrity of the system.

:dfn:`sporadic task`
    A task which executes at irregular intervals and must comply with a hard
    deadline.  A minimum period of time between successive iterations of the
    task can be guaranteed.

:dfn:`stack`
    A data structure that is managed using a Last In First Out (LIFO)
    discipline.  Each task has a stack associated with it which is used to
    store return information and local variables.

:dfn:`status code`
    Also known as error code or return value.

:dfn:`suspend`
    A term used to describe a task that is not competing for the CPU because it
    has had a ``rtems_task_suspend`` directive.

:dfn:`synchronous`
    Related in order or timing to other occurrences in the system.

:dfn:`system call`
    In this document, this is used as an alternate term for directive.

:dfn:`target`
    The system on which the application will ultimately execute.

.. _task:

:dfn:`task`
    A logically complete thread of execution.  It consists normally of a set of
    registers and a stack.  The scheduler assigns processors to a subset of the
    ready tasks.  The terms :dfn:`task` and :dfn:`thread` are synonym in RTEMS.
    The term :dfn:`task` is used throughout the Classic API, however,
    internally in the operating system implementation and the POSIX API the
    term :dfn:`thread` is used.

:dfn:`Task Control Block`
    A data structure associated with each task used by RTEMS to manage that
    task.

:dfn:`task migration`
    :dfn:`Task migration` happens in case a task stops execution on one
    processor and resumes execution on another processor.

:dfn:`task processor affinity`
    The set of processors on which a task is allowed to execute.

:dfn:`task switch`
    Alternate terminology for context switch.  Taking control of the processor
    from one task and given to another.

:dfn:`TCB`
    An acronym for Task Control Block.

:dfn:`thread`
    See :ref:`task <task>`.

:dfn:`thread dispatch`
    The :dfn:`thread dispatch` transfers control of the processor from the
    currently executing thread to the heir thread of the processor.

:dfn:`tick`
    The basic unit of time used by RTEMS.  It is a user-configurable number of
    microseconds.  The current tick expires when a clock tick directive is
    invoked.

:dfn:`tightly-coupled`
    A multiprocessor configuration system which communicates via shared memory.

:dfn:`timeout`
    An argument provided to a number of directives which determines the maximum
    length of time an application task is willing to wait to acquire the
    resource if it is not immediately available.

:dfn:`timer`
    An RTEMS object used to invoke subprograms at a later time.

:dfn:`Timer Control Block`
    A data structure associated with each timer used by RTEMS to manage that
    timer.

:dfn:`timeslicing`
    A task scheduling discipline in which tasks of equal priority are executed
    for a specific period of time before being preempted by another task.

:dfn:`timeslice`
    The application defined unit of time in which the processor is allocated.

:dfn:`TMCB`
    An acronym for Timer Control Block.

:dfn:`transient overload`
    A temporary rise in system activity which may cause deadlines to be missed.
    Rate Monotonic Scheduling can be used to determine if all deadlines will be
    met under transient overload.

:dfn:`user extensions`
    Software routines provided by the application to enhance the functionality
    of RTEMS.

:dfn:`User Extension Table`
    A table which contains the entry points for each user extensions.

:dfn:`User Initialization Tasks Table`
    A table which contains the information needed to create and start each of
    the user initialization tasks.

:dfn:`user-provided`
    Alternate term for user-supplied.  This term is used to designate any
    software routines which must be written by the application designer.

:dfn:`user-supplied`
    Alternate term for user-provided.  This term is used to designate any
    software routines which must be written by the application designer.

:dfn:`vector`
    Memory pointers used by the processor to fetch the address of routines
    which will handle various exceptions and interrupts.

:dfn:`wait queue`
    The list of tasks blocked pending the release of a particular resource.
    Message queues, regions, and semaphores have a wait queue associated with
    them.

:dfn:`yield`
    When a task voluntarily releases control of the processor.
