.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1989-2011.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Constant Bandwidth Server Scheduler API
#######################################

.. index:: cbs

Introduction
============

Unlike simple schedulers, the Constant Bandwidth Server (CBS) requires a
special API for tasks to indicate their scheduling parameters.  The directives
provided by the CBS API are:

- rtems_cbs_initialize_ - Initialize the CBS library

- rtems_cbs_cleanup_ - Cleanup the CBS library

- rtems_cbs_create_server_ - Create a new bandwidth server

- rtems_cbs_attach_thread_ - Attach a thread to server

- rtems_cbs_detach_thread_ - Detach a thread from server

- rtems_cbs_destroy_server_ - Destroy a bandwidth server

- rtems_cbs_get_server_id_ - Get an ID of a server

- rtems_cbs_get_parameters_ - Get scheduling parameters of a server

- rtems_cbs_set_parameters_ - Set scheduling parameters of a server

- rtems_cbs_get_execution_time_ - Get elapsed execution time

- rtems_cbs_get_remaining_budget_ - Get remainig execution time

- rtems_cbs_get_approved_budget_ - Get scheduler approved execution time

Background
==========

Constant Bandwidth Server Definitions
-------------------------------------
.. index:: CBS parameters

.. index:: rtems_cbs_parameters

The Constant Bandwidth Server API enables tasks to communicate with the
scheduler and indicate its scheduling parameters. The scheduler has to be set
up first (by defining ``CONFIGURE_SCHEDULER_CBS`` macro).

The difference to a plain EDF is the presence of servers.  It is a budget aware
extention of the EDF scheduler, therefore, tasks attached to servers behave in
a similar way as with EDF unless they exceed their budget.

The intention of servers is reservation of a certain computation time (budget)
of the processor for all subsequent periods. The structure
``rtems_cbs_parameters`` determines the behavior of a server. It contains
``deadline`` which is equal to period, and ``budget`` which is the time the
server is allowed to spend on CPU per each period. The ratio between those two
parameters yields the maximum percentage of the CPU the server can use
(bandwidth). Moreover, thanks to this limitation the overall utilization of CPU
is under control, and the sum of bandwidths of all servers in the system yields
the overall reserved portion of processor. The rest is still available for
ordinary tasks that are not attached to any server.

In order to make the server effective to the executing tasks, tasks have to be
attached to the servers. The ``rtems_cbs_server_id`` is a type denoting an id
of a server and ``rtems_id`` a type for id of tasks.

Handling Periodic Tasks
-----------------------
.. index:: CBS periodic tasks

Each task's execution begins with a default background priority (see the
chapter Scheduling Concepts to understand the concept of priorities in
EDF). Once you decide the tasks should start periodic execution, you have two
possibilities. Either you use only the Rate Monotonic manager which takes care
of periodic behavior, or you declare deadline and budget using the CBS API in
which case these properties are constant for all subsequent periods, unless you
change them using the CBS API again. Task now only has to indicate and end of
each period using ``rtems_rate_monotonic_period``.

Registering a Callback Function
-------------------------------
.. index:: CBS overrun handler

In case tasks attached to servers are not aware of their execution time and
happen to exceed it, the scheduler does not guarantee execution any more and
pulls the priority of the task to background, which would possibly lead to
immediate preemption (if there is at least one ready task with a higher
pirority). However, the task is not blocked but a callback function is
invoked. The callback function (``rtems_cbs_budget_overrun``) might be
optionally registered upon a server creation (``rtems_cbs_create_server``).

This enables the user to define what should happen in case of budget
overrun. There is obviously no space for huge operations because the priority
is down and not real time any more, however, you still can at least in release
resources for other tasks, restart the task or log an error information. Since
the routine is called directly from kernel, use ``printk()`` instead of
``printf()``.

The calling convention of the callback function is:

.. index:: rtems_asr

.. code-block:: c

    void overrun_handler(
        rtems_cbs_server_id server_id
    );

Limitations
-----------
.. index:: CBS limitations

When using this scheduler you have to keep in mind several things:

- it_limitations

- In the current implementation it is possible to attach only a single task to
  each server.

- If you have a task attached to a server and you voluntatily block it in the
  beginning of its execution, its priority will be probably pulled to
  background upon unblock, thus not guaranteed deadline any more. This is
  because you are effectively raising computation time of the task. When
  unbocking, you should be always sure that the ratio between remaining
  computation time and remaining deadline is not higher that the utilization
  you have agreed with the scheduler.

Operations
==========

Setting up a server
-------------------

The directive ``rtems_cbs_create_server`` is used to create a new server that
is characterized by ``rtems_cbs_parameters``. You also might want to register
the ``rtems_cbs_budget_overrun`` callback routine. After this step tasks can be
attached to the server. The directive ``rtems_cbs_set_parameters`` can change
the scheduling parameters to avoid destroying and creating a new server again.

Attaching Task to a Server
--------------------------

If a task is attached to a server using ``rtems_cbs_attach_thread``, the task's
computation time per period is limited by the server and the deadline (period)
of task is equal to deadline of the server which means if you conclude a period
using ``rate_monotonic_period``, the length of next period is always determined
by the server's property.

The task has a guaranteed bandwidth given by the server but should not exceed
it, otherwise the priority is pulled to background until the start of next
period and the ``rtems_cbs_budget_overrun`` callback function is invoked.

When attaching a task to server, the preemptability flag of the task is raised,
otherwise it would not be possible to control the execution of the task.

Detaching Task from a Server
----------------------------

The directive ``rtems_cbs_detach_thread`` is just an inverse operation to the
previous one, the task continues its execution with the initial priority.

Preemptability of the task is restored to the initial value.

Examples
--------

The following example presents a simple common use of the API.

You can see the initialization and cleanup call here, if there are multiple
tasks in the system, it is obvious that the initialization should be called
before creating the task.

Notice also that in this case we decided to register an overrun handler,
instead of which there could be ``NULL``. This handler just prints a message to
terminal, what else may be done here depends on a specific application.

During the periodic execution, remaining budget should be watched to avoid
overrun.

.. code-block:: c

    void overrun_handler (
        rtems_cbs_server_id server_id
    )
    {
        printk( "Budget overrun, fixing the task\\n" );
        return;
    }

    rtems_task Tasks_Periodic(
        rtems_task_argument argument
    )
    {
        rtems_id             rmid;
        rtems_cbs_server_id  server_id;
        rtems_cbs_parameters params;

        params.deadline = 10;
        params.budget = 4;

        rtems_cbs_initialize();
        rtems_cbs_create_server( &params, &overrun_handler, &server_id )
        rtems_cbs_attach_thread( server_id, SELF );
        rtems_rate_monotonic_create( argument, &rmid );

        while ( 1 ) {
            if (rtems_rate_monotonic_period(rmid, params.deadline) == RTEMS_TIMEOUT)
                break;
            /* Perform some periodic action */
        }

        rtems_rate_monotonic_delete( rmid );
        rtems_cbs_cleanup();
        exit( 1 );
    }

Directives
==========

This section details the Constant Bandwidth Server's directives.  A subsection
is dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_cbs_initialize:

CBS_INITIALIZE - Initialize the CBS library
-------------------------------------------
.. index:: initialize the CBS library
.. index:: rtems_cbs_initialize

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_initialize( void );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful initialization
     * - ``RTEMS_CBS_ERROR_NO_MEMORY``
       - not enough memory for data

DESCRIPTION:
    This routine initializes the library in terms of allocating necessary
    memory for the servers. In case not enough memory is available in the
    system, ``RTEMS_CBS_ERROR_NO_MEMORY`` is returned, otherwise
    ``RTEMS_CBS_OK``.

NOTES:
    Additional memory per each server is allocated upon invocation of
    ``rtems_cbs_create_server``.

    Tasks in the system are not influenced, they still keep executing with
    their initial parameters.

.. raw:: latex

   \clearpage

.. _rtems_cbs_cleanup:

CBS_CLEANUP - Cleanup the CBS library
-------------------------------------
.. index:: cleanup the CBS library
.. index:: rtems_cbs_cleanup

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_cleanup( void );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - always successful

DESCRIPTION:
    This routine detaches all tasks from their servers, destroys all servers
    and returns memory back to the system.

NOTES:
    All tasks continue executing with their initial priorities.

.. raw:: latex

   \clearpage

.. _rtems_cbs_create_server:

CBS_CREATE_SERVER - Create a new bandwidth server
-------------------------------------------------
.. index:: create a new bandwidth server
.. index:: rtems_cbs_create_server

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_create_server (
            rtems_cbs_parameters     *params,
            rtems_cbs_budget_overrun  budget_overrun_callback,
            rtems_cbs_server_id      *server_id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successfully created
     * - ``RTEMS_CBS_ERROR_NO_MEMORY``
       - not enough memory for data
     * - ``RTEMS_CBS_ERROR_FULL``
       - maximum servers exceeded
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument

DESCRIPTION:
    This routine prepares an instance of a constant bandwidth server.  The
    input parameter ``rtems_cbs_parameters`` specifies scheduling parameters of
    the server (period and budget). If these are not valid,
    ``RTEMS_CBS_ERROR_INVALID_PARAMETER`` is returned.  The
    ``budget_overrun_callback`` is an optional callback function, which is
    invoked in case the server's budget within one period is exceeded.  Output
    parameter ``server_id`` becomes an id of the newly created server.  If
    there is not enough memory, the ``RTEMS_CBS_ERROR_NO_MEMORY`` is
    returned. If the maximum server count in the system is exceeded,
    ``RTEMS_CBS_ERROR_FULL`` is returned.

NOTES:
    No task execution is being influenced so far.

.. raw:: latex

   \clearpage

.. _rtems_cbs_attach_thread:

CBS_ATTACH_THREAD - Attach a thread to server
---------------------------------------------
.. index:: attach a thread to server
.. index:: rtems_cbs_attach_thread

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_attach_thread (
            rtems_cbs_server_id server_id,
            rtems_id            task_id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successfully attached
     * - ``RTEMS_CBS_ERROR_FULL``
       - server maximum tasks exceeded
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    Attaches a task (``task_id``) to a server (``server_id``).  The server has
    to be previously created. Now, the task starts to be scheduled according to
    the server parameters and not using initial priority. This implementation
    allows only one task per server, if the user tries to bind another task to
    the same server, ``RTEMS_CBS_ERROR_FULL`` is returned.

NOTES:
    Tasks attached to servers become preemptible.

.. raw:: latex

   \clearpage

.. _rtems_cbs_detach_thread:

CBS_DETACH_THREAD - Detach a thread from server
-----------------------------------------------
.. index:: detach a thread from server
.. index:: rtems_cbs_detach_thread

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_detach_thread (
            rtems_cbs_server_id server_id,
            rtems_id            task_id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successfully detached
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive detaches a thread from server. The task continues its
    execution with initial priority.

NOTES:
    The server can be reused for any other task.

.. raw:: latex

   \clearpage

.. _rtems_cbs_destroy_server:

CBS_DESTROY_SERVER - Destroy a bandwidth server
-----------------------------------------------
.. index:: destroy a bandwidth server
.. index:: rtems_cbs_destroy_server

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_destroy_server (
            rtems_cbs_server_id server_id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successfully destroyed
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive destroys a server. If any task was attached to the server,
    the task is detached and continues its execution according to EDF rules
    with initial properties.

NOTES:
    This again enables one more task to be created.

.. raw:: latex

   \clearpage

.. _rtems_cbs_get_server_id:

CBS_GET_SERVER_ID - Get an ID of a server
-----------------------------------------
.. index:: get an ID of a server
.. index:: rtems_cbs_get_server_id

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_get_server_id (
            rtems_id             task_id,
            rtems_cbs_server_id *server_id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive returns an id of server belonging to a given task.

.. raw:: latex

   \clearpage

.. _rtems_cbs_get_parameters:

CBS_GET_PARAMETERS - Get scheduling parameters of a server
----------------------------------------------------------
.. index:: get scheduling parameters of a server
.. index:: rtems_cbs_get_parameters

CALLING SEQUENCE:
    .. code-block:: c

        rtems_cbs_get_parameters (
            rtems_cbs_server_id   server_id,
            rtems_cbs_parameters *params
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive returns a structure with current scheduling parameters of a
    given server (period and execution time).

NOTES:
    It makes no difference if any task is assigned or not.

.. raw:: latex

   \clearpage

.. _rtems_cbs_set_parameters:

CBS_SET_PARAMETERS - Set scheduling parameters
----------------------------------------------
.. index:: set scheduling parameters
.. index:: rtems_cbs_set_parameters

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_set_parameters (
            rtems_cbs_server_id   server_id,
            rtems_cbs_parameters *params
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive sets new scheduling parameters to the server. This operation
    can be performed regardless of whether a task is assigned or not.  If a
    task is assigned, the parameters become effective imediately, therefore it
    is recommended to apply the change between two subsequent periods.

NOTES:
    There is an upper limit on both period and budget equal to (2^31)-1 ticks.

.. raw:: latex

   \clearpage

.. _rtems_cbs_get_execution_time:

CBS_GET_EXECUTION_TIME - Get elapsed execution time
---------------------------------------------------
.. index:: get elapsed execution time
.. index:: rtems_cbs_get_execution_time

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_get_execution_time (
            rtems_cbs_server_id    server_id,
            time_t                *exec_time,
            time_t                *abs_time
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This routine returns consumed execution time (``exec_time``) of a server
    during the current period.

NOTES:
    Absolute time (``abs_time``) not supported now.

.. raw:: latex

   \clearpage

.. _rtems_cbs_get_remaining_budget:

CBS_GET_REMAINING_BUDGET - Get remaining execution time
-------------------------------------------------------
.. index:: get remaining execution time
.. index:: rtems_cbs_get_remaining_budget

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_get_remaining_budget (
            rtems_cbs_server_id  server_id,
            time_t              *remaining_budget
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive returns remaining execution time of a given server for
    current period.

NOTES:
    If the execution time approaches zero, the assigned task should finish
    computations of the current period.

.. raw:: latex

   \clearpage

.. _rtems_cbs_get_approved_budget:

CBS_GET_APPROVED_BUDGET - Get scheduler approved execution time
---------------------------------------------------------------
.. index:: get scheduler approved execution time
.. index:: rtems_cbs_get_approved_budget

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_cbs_get_approved_budget (
            rtems_cbs_server_id  server_id,
            time_t              *appr_budget
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_CBS_OK``
       - successful
     * - ``RTEMS_CBS_ERROR_INVALID_PARAMETER``
       - invalid input argument
     * - ``RTEMS_CBS_ERROR_NOSERVER``
       - server is not valid

DESCRIPTION:
    This directive returns server's approved budget for subsequent periods.
