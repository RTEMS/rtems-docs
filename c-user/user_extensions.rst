.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

.. _User Extensions Manager:

User Extensions Manager
***********************

.. index:: user extensions

Introduction
============

The user extensions manager allows the application developer to augment the
executive by allowing them to supply extension routines which are invoked at
critical system events.  The directives provided by the user extensions manager
are:

- rtems_extension_create_ - Create an extension set

- rtems_extension_ident_ - Get ID of an extension set

- rtems_extension_delete_ - Delete an extension set

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

Extension Sets
--------------
.. index:: user extension set
.. index:: rtems_extensions_table

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

TCB Extension Area
------------------
.. index:: TCB extension area

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

The user extensions are invoked in either `forward` or `reverse` order.  In
forward order, the user extensions of initial extension sets are invoked before
the user extensions of the dynamic extension sets.  The forward order of
initial extension sets is defined by the initial extension sets table index.
The forward order of dynamic extension sets is defined by the order in which
the dynamic extension sets were created.  The reverse order is defined
accordingly.  By invoking the user extensions in this order, extensions can be
built upon one another.  At the following system events, the user extensions
are invoked in `forward` order

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

Thread Create Extension
-----------------------

The thread create extension is invoked during thread creation, for example
via :ref:`rtems_task_create() <rtems_task_create>` or :c:func:`pthread_create`.
The thread create extension is defined as follows.

.. index:: rtems_task_create_extension

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

Thread Start Extension
----------------------

The thread start extension is invoked during a thread start, for example
via :ref:`rtems_task_start() <rtems_task_start>` or :c:func:`pthread_create`.
The thread start extension is defined as follows.

.. index:: rtems_task_start_extension

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
invoked.

The thread start extension is invoked in forward order with thread dispatching
disabled.

Thread Restart Extension
------------------------

The thread restart extension is invoked during a thread restart, for example
via :ref:`rtems_task_restart() <rtems_task_start>`.
The thread restart extension is defined as follows.

.. index:: rtems_task_restart_extension

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
extensions lead to recursion.

Thread Switch Extension
-----------------------

The thread switch extension is invoked before the context switch from the
currently executing thread to the heir thread.  The thread switch extension is
defined as follows.

.. index:: rtems_task_switch_extension

.. code-block:: c

    typedef void ( *rtems_task_switch_extension )(
      rtems_tcb *executing,
      rtems_tcb *heir
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.  The :c:data:`heir` is a pointer to the TCB of the heir thread.

The thread switch extension is invoked in forward order with thread dispatching
disabled.  In SMP configurations, interrupts are disabled and the per-processor
SMP lock is owned.

The context switches initiated through the multitasking start are not covered
by the thread switch extension.

Thread Begin Extension
----------------------

The thread begin extension is invoked during a thread begin before the thread
entry function is called.  The thread begin extension is defined as follows.

.. index:: rtems_task_begin_extension

.. code-block:: c

    typedef void ( *rtems_task_begin_extension )(
      rtems_tcb *executing
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.  The thread begin extension executes in a normal thread context and may
allocate resources for the thread.  In particular it has access to thread-local
storage of the thread.

The thread begin extension is invoked in forward order with thread dispatching
enabled.  The thread switch extension may be called multiple times for this
thread before the thread begin extension is invoked.

Thread Exitted Extension
------------------------

The thread exitted extension is invoked once the thread entry function returns.
The thread exitted extension is defined as follows.

.. index:: rtems_task_exitted_extension

.. code-block:: c

    typedef void ( *rtems_task_exitted_extension )(
      rtems_tcb *executing
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.

This extension is invoked in forward order with thread dispatching enabled.

Thread Termination Extension
----------------------------

The thread termination extension is invoked in case a termination request is
recognized by the currently executing thread.  Termination requests may result
due to calls of :ref:`rtems_task_delete() <rtems_task_delete>`,
:c:func:`pthread_exit`, or :c:func:`pthread_cancel`.  The thread termination
extension is defined as follows.

.. index:: rtems_task_terminate_extension

.. code-block:: c

    typedef void ( *rtems_task_terminate_extension )(
      rtems_tcb *executing
    );

The :c:data:`executing` is a pointer to the TCB of the currently executing
thread.

It is invoked in the context of the terminated thread right before the
thread dispatch to the heir thread.  The POSIX cleanup and key destructors
execute in this context.  The thread termination extension has access to
thread-local storage and thread-specific data of POSIX keys.

The thread terminate extension is invoked in reverse order with thread
dispatching enabled.  The thread life is protected.  Thread restart and delete
requests issued by thread terminate extensions lead to recursion.

Thread Delete Extension
-----------------------

The thread delete extension is invoked in case a zombie thread is killed.  A
thread becomes a zombie thread after it terminated.  The thread delete
extension is defined as follows.

.. index:: rtems_task_delete_extension

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

Fatal Error Extension
---------------------

The fatal error extension is invoked during :ref:`system termination
<Terminate>`.  The fatal error extension is defined as follows.

.. index:: rtems_fatal_extension

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

Directives
==========

This section details the user extension manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_extension_create:

EXTENSION_CREATE - Create a extension set
-----------------------------------------
.. index:: create an extension set
.. index:: rtems_extension_create

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_extension_create(
          rtems_name                    name,
          const rtems_extensions_table *table,
          rtems_id                     *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - extension set created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid extension set name
     * - ``RTEMS_TOO_MANY``
       - too many extension sets created

DESCRIPTION:

    This directive creates an extension set object and initializes it using the
    specified extension set table.  The assigned extension set identifier is
    returned in :c:data:`id`.  This identifier is used to access the extension
    set with other user extension manager directives.  For control and
    maintenance of the extension set, RTEMS allocates an Extension Set Control
    Block (ESCB) from the local ESCB free pool and initializes it.  The
    user-specified :c:data:`name` is assigned to the ESCB and may be used to
    identify the extension set via
    :ref:`rtems_extension_ident() <rtems_extension_ident>`.  The extension set
    specified by :c:data:`table` is copied to the ESCB.

NOTES:

    This directive will not cause the calling task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_extension_ident:

EXTENSION_IDENT - Get ID of a extension set
-------------------------------------------
.. index:: get ID of an extension set
.. index:: obtain ID of an extension set
.. index:: rtems_extension_ident

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_extension_ident(
          rtems_name  name,
          rtems_id   *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - extension set identified successfully
     * - ``RTEMS_INVALID_NAME``
       - extension set name not found

DESCRIPTION:
    This directive obtains the extension set identifier associated with the
    extension set :c:data:`name` to be acquired and returns it in :c:data:`id`.
    If the extension set name is not unique, then the extension set identifier
    will match one of the extension sets with that name.  However, this
    extension set identifier is not guaranteed to correspond to the desired
    extension set.  The extension set identifier is used to access this
    extension set in other extension set related directives.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_extension_delete:

EXTENSION_DELETE - Delete a extension set
-----------------------------------------
.. index:: delete an extension set
.. index:: rtems_extension_delete

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_extension_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - extension set deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid extension set id

DESCRIPTION:
    This directive deletes the extension set specified by :c:data:`id`.  If the
    extension set is running, it is automatically canceled.  The ESCB for the
    deleted extension set is reclaimed by RTEMS.

NOTES:
    This directive will not cause the running task to be preempted.

    A extension set can be deleted by a task other than the task which created
    the extension set.
