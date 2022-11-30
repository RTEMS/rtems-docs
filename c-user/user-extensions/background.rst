.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Background
==========

User extensions (call-back functions) are invoked by the system when the
following events occur

- thread creation,

- thread start,

- thread restart,

- thread switch,

- thread begin,

- thread exitted (return from thread entry function),

- thread termination,

- thread deletion, and

- fatal error detection (system termination).

The user extensions have event-specific arguments, invocation orders and
execution contexts.  Extension sets can be installed at run-time via
:ref:`rtems_extension_create() <rtems_extension_create>` (dynamic extension
sets) or at link-time via the application configuration option
:ref:`CONFIGURE_INITIAL_EXTENSIONS <CONFIGURE_INITIAL_EXTENSIONS>` (initial
extension sets).

The execution context of user extensions varies.  Some user extensions are
invoked with ownership of the allocator mutex.  The allocator mutex protects
dynamic memory allocations and object creation/deletion.  Some user extensions
are invoked with thread dispatching disabled.  The fatal error extension is
invoked in an arbitrary context.

.. index:: user extension set
.. index:: rtems_extensions_table

Extension Sets
--------------

User extensions are maintained as a set.  All user extensions are optional and
may be `NULL`.  Together a set of these user extensions typically performs a
specific functionality such as performance monitoring or debugger support.  The
extension set is defined via the following structure.

.. code-block:: c

    typedef struct {
      rtems_task_create_extension    thread_create;
      rtems_task_start_extension     thread_start;
      rtems_task_restart_extension   thread_restart;
      rtems_task_delete_extension    thread_delete;
      rtems_task_switch_extension    thread_switch;
      rtems_task_begin_extension     thread_begin;
      rtems_task_exitted_extension   thread_exitted;
      rtems_fatal_extension          fatal;
      rtems_task_terminate_extension thread_terminate;
    } rtems_extensions_table;

.. index:: TCB extension area

TCB Extension Area
------------------

There is no system-provided storage for the initial extension sets.

The task control block (TCB) contains a pointer for each dynamic extension set.
The pointer is initialized to `NULL` during thread initialization before the
thread create extension is invoked.  The pointer may be used by the dynamic
extension set to maintain thread-specific data.

The TCB extension is an array of pointers in the TCB. The index into the table
can be obtained from the extension identifier returned when the extension
object is created:

.. index:: rtems extensions table index

.. code-block:: c

    index = rtems_object_id_get_index( extension_id );

The number of pointers in the area is the same as the number of dynamic user
extension sets configured.  This allows an application to augment the TCB with
user-defined information.  For example, an application could implement task
profiling by storing timing statistics in the TCB's extended memory area.  When
a task context switch is being executed, the thread switch extension could read
a real-time clock to calculate how long the task being swapped out has run as
well as timestamp the starting time for the task being swapped in.

If used, the extended memory area for the TCB should be allocated and the TCB
extension pointer should be set at the time the task is created or started by
either the thread create or thread start extension.  The application is
responsible for managing this extended memory area for the TCBs.  The memory
may be reinitialized by the thread restart extension and should be deallocated
by the thread delete extension  when the task is deleted.  Since the TCB
extension buffers would most likely be of a fixed size, the RTEMS partition
manager could be used to manage the application's extended memory area.  The
application could create a partition of fixed size TCB extension buffers and
use the partition manager's allocation and deallocation directives to obtain
and release the extension buffers.

Order of Invocation
-------------------

The user extensions are invoked in either :term:`extension forward order` or
:term:`extension reverse order`.  By invoking the user extensions in these
orders, extensions can be built upon one another.  At the following system
events, the user extensions are invoked in `forward` order

- thread creation,

- thread start,

- thread restart,

- thread switch,

- thread begin,

- thread exitted (return from thread entry function), and

- fatal error detection.

At the following system events, the user extensions are invoked in `reverse`
order:

- thread termination, and

- thread deletion.

At these system events, the user extensions are invoked in reverse order to insure
that if an extension set is built upon another, the more complicated user extension
is invoked before the user extension it is built upon.  An example is use of the
thread delete extension by the Standard C Library.  Extension sets which are
installed after the Standard C Library will operate correctly even if they
utilize the C Library because the C Library's thread delete extension is
invoked after that of the other thread delete extensions.

.. index:: rtems_task_create_extension()

Thread Create Extension
-----------------------

The thread create extension is invoked during thread creation, for example
via :ref:`rtems_task_create() <rtems_task_create>` or :c:func:`pthread_create`.
The thread create extension is defined as follows.

.. code-block:: c

    typedef bool ( *rtems_task_create_extension )(
      rtems_tcb *executing,
      rtems_tcb *created
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.  The :c:data:`created` is a pointer to the TCB of the created thread.
The created thread is completely initialized with respect to the operating
system.

The executing thread is the owner of the allocator mutex except during creation
of the idle threads.  Since the allocator mutex allows nesting the normal
memory allocation routines can be used.

A thread create extension will frequently attempt to allocate resources.  If
this allocation fails, then the thread create extension must return
:c:data:`false` and the entire thread create operation will fail, otherwise it
must return :c:data:`true`.

The thread create extension is invoked in forward order with thread dispatching
enabled (except during system initialization).

.. index:: rtems_task_start_extension

Thread Start Extension
----------------------

The thread start extension is invoked during a thread start, for example
via :ref:`rtems_task_start() <rtems_task_start>` or :c:func:`pthread_create`.
The thread start extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_start_extension )(
      rtems_tcb *executing,
      rtems_tcb *started
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.  The :c:data:`started` is a pointer to the TCB of the started thread.
It is invoked after the environment of the started thread has been loaded and the
started thread has been made ready.  So, in SMP configurations, the thread may
already run on another processor before the thread start extension is actually
invoked.  Thread switch and thread begin extensions may run before or in
parallel with the thread start extension in SMP configurations.

The thread start extension is invoked in forward order with thread dispatching
disabled.

.. index:: rtems_task_restart_extension

Thread Restart Extension
------------------------

The thread restart extension is invoked during a thread restart, for example
via :ref:`rtems_task_restart() <rtems_task_start>`.
The thread restart extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_restart_extension )(
      rtems_tcb *executing,
      rtems_tcb *restarted
    );

Both :c:data:`executing` and :c:data:`restarted` are pointers the TCB of the
currently executing thread.  It is invoked in the context of the executing
thread right before the execution context is reloaded.  The thread stack
reflects the previous execution context.

The thread restart extension is invoked in forward order with thread
dispatching enabled (except during system initialization).  The thread life is
protected.  Thread restart and delete requests issued by thread restart
extensions lead to recursion.  The POSIX cleanup handlers, POSIX key
destructors and thread-local object destructors run in this context.

.. index:: rtems_task_switch_extension

Thread Switch Extension
-----------------------

The thread switch extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_switch_extension )(
      rtems_tcb *executing,
      rtems_tcb *heir
    );

The invocation conditions of the thread switch extension depend on whether RTEMS
was configured for uniprocessor or SMP systems.  A user must pay attention to
the differences to correctly implement a thread switch extension.

In uniprocessor configurations, the thread switch extension is invoked before
the context switch from the currently executing thread to the heir thread.  The
:c:data:`executing` is a pointer to the TCB of the currently executing thread.
The :c:data:`heir` is a pointer to the TCB of the heir thread.  The context
switch initiated through the multitasking start is not covered by the thread
switch extension.

In SMP configurations, the thread switch extension is invoked after the context
switch to the new executing thread (previous heir thread).  The
:c:data:`executing` is a pointer to the TCB of the previously executing thread.
Despite the name, this is not the currently executing thread.  The
:c:data:`heir` is a pointer to the TCB of the newly executing thread.  This is
the currently executing thread.  The context switches initiated through the
multitasking start are covered by the thread switch extension.  The reason for
the differences to uniprocessor configurations is that the context switch may
update the heir thread of the processor, see :ref:`SMPThreadDispatchDetails`.
The thread switch extensions are invoked with disabled interrupts and with
ownership of a per-processor SMP lock.  Thread switch extensions may run in
parallel on multiple processors.  It is recommended to use thread-local or
per-processor data structures for thread switch extensions.  A global SMP lock
should be avoided for performance reasons.

The thread switch extension is invoked in forward order with thread dispatching
disabled.

.. index:: rtems_task_begin_extension

Thread Begin Extension
----------------------

The thread begin extension is invoked during a thread begin before the thread
entry function is called.  The thread begin extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_begin_extension )(
      rtems_tcb *executing
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.  The thread begin extension executes in a normal thread context and may
allocate resources for the executing thread.  In particular, it has access to
thread-local storage of the executing thread.

The thread begin extension is invoked in forward order with thread dispatching
enabled.  The thread switch extension may be called multiple times for this
thread before or during the thread begin extension is invoked.

.. index:: rtems_task_exitted_extension

Thread Exitted Extension
------------------------

The thread exitted extension is invoked once the thread entry function returns.
The thread exitted extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_exitted_extension )(
      rtems_tcb *executing
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.

This extension is invoked in forward order with thread dispatching enabled.

.. index:: rtems_task_terminate_extension

Thread Termination Extension
----------------------------

The thread termination extension is invoked in case a termination request is
recognized by the currently executing thread.  Termination requests may result
due to calls of :ref:`rtems_task_delete() <rtems_task_delete>`,
:c:func:`pthread_exit`, or :c:func:`pthread_cancel`.  The thread termination
extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_terminate_extension )(
      rtems_tcb *executing
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.

It is invoked in the context of the terminated thread right before the thread
dispatch to the heir thread.  The POSIX cleanup handlers, POSIX key destructors
and thread-local object destructors run in this context.  Depending on the
order, the thread termination extension has access to thread-local storage and
thread-specific data of POSIX keys.

The thread terminate extension is invoked in reverse order with thread
dispatching enabled.  The thread life is protected.  Thread restart and delete
requests issued by thread terminate extensions lead to recursion.

.. index:: rtems_task_delete_extension

Thread Delete Extension
-----------------------

The thread delete extension is invoked in case a zombie thread is killed.  A
thread becomes a zombie thread after it terminated.  The thread delete
extension is defined as follows.

.. code-block:: c

    typedef void ( *rtems_task_delete_extension )(
      rtems_tcb *executing,
      rtems_tcb *deleted
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.  The :c:data:`deleted` is a pointer to the TCB of the deleted thread.
The :c:data:`executing` and :c:data:`deleted` pointers are never equal.

The executing thread is the owner of the allocator mutex.  Since the allocator
mutex allows nesting the normal memory allocation routines can be used.

The thread delete extension is invoked in reverse order with thread dispatching
enabled.

Please note that a thread delete extension is not immediately invoked with a
call to :ref:`rtems_task_delete() <rtems_task_delete>` or similar.  The thread
must first terminate and this may take some time.  The thread delete extension
is invoked by :ref:`rtems_task_create() <rtems_task_create>` or similar as a
result of a lazy garbage collection of zombie threads.

.. index:: rtems_fatal_extension

Fatal Error Extension
---------------------

The fatal error extension is invoked during :ref:`system termination
<Terminate>`.  The fatal error extension is defined as follows.

.. code-block:: c

    typedef void( *rtems_fatal_extension )(
      rtems_fatal_source source,
      bool               always_set_to_false,
      rtems_fatal_code   code
    );

The :c:data:`source` parameter is the fatal source indicating the subsystem the
fatal condition originated in.  The :c:data:`always_set_to_false` parameter is
always set to :c:data:`false` and provided only for backward compatibility
reasons.  The :c:data:`code` parameter is the fatal error code.  This value
must be interpreted with respect to the source.

The fatal error extension is invoked in forward order.

It is strongly advised to use initial extension sets to install a fatal error
extension.  Usually, the initial extension set of board support package
provides a fatal error extension which resets the board.  In this case, the
dynamic fatal error extensions are not invoked.
