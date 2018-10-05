.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008, 2018.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Barrier Manager
***************

.. index:: barrier

Introduction
============

The barrier manager provides a unique synchronization capability which can be
used to have a set of tasks block and be unblocked as a set.  The directives
provided by the barrier manager are:

- rtems_barrier_create_ - Create a barrier

- rtems_barrier_ident_ - Get ID of a barrier

- rtems_barrier_delete_ - Delete a barrier

- rtems_barrier_wait_ - Wait at a barrier

- rtems_barrier_release_ - Release a barrier

Background
==========

A barrier can be viewed as a gate at which tasks wait until the gate is opened.
This has many analogies in the real world.  Horses and other farm animals may
approach a closed gate and gather in front of it, waiting for someone to open
the gate so they may proceed.  Similarly, cticket holders gather at the gates
of arenas before concerts or sporting events waiting for the arena personnel to
open the gates so they may enter.

Barriers are useful during application initialization.  Each application task
can perform its local initialization before waiting for the application as a
whole to be initialized.  Once all tasks have completed their independent
initializations, the "application ready" barrier can be released.

Automatic Versus Manual Barriers
--------------------------------

Just as with a real-world gate, barriers may be configured to be manually
opened or automatically opened.  All tasks calling the ``rtems_barrier_wait``
directive will block until a controlling task invokes
the ``rtems_barrier_release`` directive.

Automatic barriers are created with a limit to the number of tasks which may
simultaneously block at the barrier.  Once this limit is reached, all of the
tasks are released.  For example, if the automatic limit is ten tasks, then the
first nine tasks calling the ``rtems_barrier_wait`` directive will block.  When
the tenth task calls the ``rtems_barrier_wait`` directive, the nine blocked
tasks will be released and the tenth task returns to the caller without
blocking.

Building a Barrier Attribute Set
--------------------------------

In general, an attribute set is built by a bitwise OR of the desired attribute
components.  The following table lists the set of valid barrier attributes:

``RTEMS_BARRIER_AUTOMATIC_RELEASE``
  automatically release the barrier when the configured number of tasks are
  blocked

``RTEMS_BARRIER_MANUAL_RELEASE``
  only release the barrier when the application invokes the
  ``rtems_barrier_release`` directive.  (default)

.. note::

  Barriers only support FIFO blocking order because all waiting tasks are
  released as a set.  Thus the released tasks will all become ready to execute
  at the same time and compete for the processor based upon their priority.

Attribute values are specifically designed to be mutually exclusive, therefore
bitwise OR and addition operations are equivalent as long as each attribute
appears exactly once in the component list.  An attribute listed as a default
is not required to appear in the attribute list, although it is a good
programming practice to specify default attributes.  If all defaults are
desired, the attribute ``RTEMS_DEFAULT_ATTRIBUTES`` should be specified on this
call.

This example demonstrates the attribute_set parameter needed to create a
barrier with the automatic release policy.  The ``attribute_set`` parameter
passed to the ``rtems_barrier_create`` directive will be
``RTEMS_BARRIER_AUTOMATIC_RELEASE``.  In this case, the user must also specify
the ``maximum_waiters`` parameter.

Operations
==========

Creating a Barrier
------------------

The ``rtems_barrier_create`` directive creates a barrier with a user-specified
name and the desired attributes.  RTEMS allocates a Barrier Control Block (BCB)
from the BCB free list.  This data structure is used by RTEMS to manage the
newly created barrier.  Also, a unique barrier ID is generated and returned to
the calling task.

Obtaining Barrier IDs
---------------------

When a barrier is created, RTEMS generates a unique barrier ID and assigns it
to the created barrier until it is deleted.  The barrier ID may be obtained by
either of two methods.  First, as the result of an invocation of the
``rtems_barrier_create`` directive, the barrier ID is stored in a user provided
location.  Second, the barrier ID may be obtained later using the
``rtems_barrier_ident`` directive.  The barrier ID is used by other barrier
manager directives to access this barrier.

Waiting at a Barrier
--------------------

The ``rtems_barrier_wait`` directive is used to wait at
the specified barrier.  Since a barrier is, by definition, never immediately,
the task may wait forever for the barrier to be released or it may
specify a timeout.  Specifying a timeout limits the interval the task will
wait before returning with an error status code.

If the barrier is configured as automatic and there are already one less then
the maximum number of waiters, then the call will unblock all tasks waiting at
the barrier and the caller will return immediately.

When the task does wait to acquire the barrier, then it is placed in the
barrier's task wait queue in FIFO order.  All tasks waiting on a barrier are
returned an error code when the barrier is deleted.

Releasing a Barrier
-------------------

The ``rtems_barrier_release`` directive is used to release the specified
barrier.  When the ``rtems_barrier_release`` is invoked, all tasks waiting at
the barrier are immediately made ready to execute and begin to compete for the
processor to execute.

Deleting a Barrier
------------------

The ``rtems_barrier_delete`` directive removes a barrier from the system and
frees its control block.  A barrier can be deleted by any local task that knows
the barrier's ID.  As a result of this directive, all tasks blocked waiting for
the barrier to be released, will be readied and returned a status code which
indicates that the barrier was deleted.  Any subsequent references to the
barrier's name and ID are invalid.

Directives
==========

This section details the barrier manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. _rtems_barrier_create:

BARRIER_CREATE - Create a barrier
---------------------------------
.. index:: create a barrier
.. index:: rtems_barrier_create

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_barrier_create(
            rtems_name           name,
            rtems_attribute      attribute_set,
            uint32_t             maximum_waiters,
            rtems_id            *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - barrier created successfully
     * - ``RTEMS_INVALID_NAME``
       - invalid barrier name
     * - ``RTEMS_INVALID_ADDRESS``
       - ``id`` is NULL
     * - ``RTEMS_TOO_MANY``
       - too many barriers created

DESCRIPTION:
    This directive creates a barrier which resides on the local node. The
    created barrier has the user-defined name specified in ``name`` and the
    initial count specified in ``count``.  For control and maintenance of the
    barrier, RTEMS allocates and initializes a BCB.  The RTEMS-assigned barrier
    id is returned in ``id``.  This barrier id is used with other barrier
    related directives to access the barrier.

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_BARRIER_MANUAL_RELEASE``
       - only release

    Specifying ``RTEMS_BARRIER_AUTOMATIC_RELEASE`` in ``attribute_set`` causes
    tasks calling the ``rtems_barrier_wait`` directive to block until there are
    ``maximum_waiters - 1`` tasks waiting at the barrier.  When the
    ``maximum_waiters`` task invokes the ``rtems_barrier_wait`` directive, the
    previous ``maximum_waiters - 1`` tasks are automatically released and the
    caller returns.

    In contrast, when the ``RTEMS_BARRIER_MANUAL_RELEASE`` attribute is
    specified, there is no limit on the number of tasks that will block at the
    barrier. Only when the ``rtems_barrier_release`` directive is invoked, are
    the tasks waiting at the barrier unblocked.

NOTES:
    This directive will not cause the calling task to be preempted.

    The following barrier attribute constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_BARRIER_AUTOMATIC_RELEASE``
       - automatically release the barrier when the configured number of tasks are
         blocked
     * - ``RTEMS_BARRIER_MANUAL_RELEASE``
       - only release the barrier when the application invokes
         the ``rtems_barrier_release`` directive.  (default)

.. raw:: latex

   \clearpage

.. _rtems_barrier_ident:

BARRIER_IDENT - Get ID of a barrier
-----------------------------------
.. index:: get ID of a barrier
.. index:: obtain ID of a barrier
.. index:: rtems_barrier_ident

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_barrier_ident(
            rtems_name        name,
            rtems_id         *id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - barrier identified successfully
     * - ``RTEMS_INVALID_NAME``
       - barrier name not found
     * - ``RTEMS_INVALID_NODE``
       - invalid node id

DESCRIPTION:
    This directive obtains the barrier id associated with the barrier name.  If
    the barrier name is not unique, then the barrier id will match one of the
    barriers with that name.  However, this barrier id is not guaranteed to
    correspond to the desired barrier.  The barrier id is used by other barrier
    related directives to access the barrier.

NOTES:
    This directive will not cause the running task to be preempted.

.. raw:: latex

   \clearpage

.. _rtems_barrier_delete:

BARRIER_DELETE - Delete a barrier
---------------------------------
.. index:: delete a barrier
.. index:: rtems_barrier_delete

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_barrier_delete(
            rtems_id id
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - barrier deleted successfully
     * - ``RTEMS_INVALID_ID``
       - invalid barrier id

DESCRIPTION:
    This directive deletes the barrier specified by ``id``.  All tasks blocked
    waiting for the barrier to be released will be readied and returned a
    status code which indicates that the barrier was deleted.  The BCB for this
    barrier is reclaimed by RTEMS.

NOTES:
    The calling task will be preempted if it is enabled by the task's execution
    mode and a higher priority local task is waiting on the deleted barrier.
    The calling task will NOT be preempted if all of the tasks that are waiting
    on the barrier are remote tasks.

    The calling task does not have to be the task that created the barrier.
    Any local task that knows the barrier id can delete the barrier.

.. raw:: latex

   \clearpage

.. _rtems_barrier_wait:

BARRIER_OBTAIN - Wait at a barrier
----------------------------------
.. index:: obtain a barrier
.. index:: lock a barrier
.. index:: rtems_barrier_wait

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_barrier_wait(
            rtems_id         id,
            rtems_interval   timeout
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - barrier released and task unblocked
     * - ``RTEMS_UNSATISFIED``
       - barrier not available
     * - ``RTEMS_TIMEOUT``
       - timed out waiting for barrier
     * - ``RTEMS_OBJECT_WAS_DELETED``
       - barrier deleted while waiting
     * - ``RTEMS_INVALID_ID``
       - invalid barrier id

DESCRIPTION:

    This directive acquires the barrier specified by ``id``.  The
    ``RTEMS_WAIT`` and ``RTEMS_NO_WAIT`` components of the options parameter
    indicate whether the calling task wants to wait for the barrier to become
    available or return immediately if the barrier is not currently available.
    With either ``RTEMS_WAIT`` or ``RTEMS_NO_WAIT``, if the current barrier
    count is positive, then it is decremented by one and the barrier is
    successfully acquired by returning immediately with a successful return
    code.

    Conceptually, the calling task should always be thought of as blocking when
    it makes this call and being unblocked when the barrier is released.  If
    the barrier is configured for manual release, this rule of thumb will
    always be valid.  If the barrier is configured for automatic release, all
    callers will block except for the one which is the Nth task which trips the
    automatic release condition.

    The timeout parameter specifies the maximum interval the calling task is
    willing to be blocked waiting for the barrier.  If it is set to
    ``RTEMS_NO_TIMEOUT``, then the calling task will wait forever.  If the
    barrier is available or the ``RTEMS_NO_WAIT`` option component is set, then
    timeout is ignored.

NOTES:

    The following barrier acquisition option constants are defined by RTEMS:

    .. list-table::
     :class: rtems-table

     * - ``RTEMS_WAIT``
       - task will wait for barrier (default)
     * - ``RTEMS_NO_WAIT``
       - task should not wait

    A clock tick is required to support the timeout functionality of this
    directive.

.. raw:: latex

   \clearpage

.. _rtems_barrier_release:

BARRIER_RELEASE - Release a barrier
-----------------------------------
.. index:: wait at a barrier
.. index:: release a barrier
.. index:: rtems_barrier_release

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_barrier_release(
            rtems_id  id,
            uint32_t *released
        );

DIRECTIVE STATUS CODES:
    .. list-table::
     :class: rtems-table

     * - ``RTEMS_SUCCESSFUL``
       - barrier released successfully
     * - ``RTEMS_INVALID_ID``
       - invalid barrier id

DESCRIPTION:
    This directive releases the barrier specified by id.  All tasks waiting at
    the barrier will be unblocked.  If the running task's preemption mode is
    enabled and one of the unblocked tasks has a higher priority than the
    running task.

NOTES:
    The calling task may be preempted if it causes a higher priority task to be
    made ready for execution.
