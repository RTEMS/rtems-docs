.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2018 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the barrier manager's directives.  A subsection is
dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: create a barrier
.. index:: rtems_barrier_create

.. _rtems_barrier_create:

BARRIER_CREATE - Create a barrier
---------------------------------

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

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

.. index:: get ID of a barrier
.. index:: obtain ID of a barrier
.. index:: rtems_barrier_ident

.. _rtems_barrier_ident:

BARRIER_IDENT - Get ID of a barrier
-----------------------------------

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

.. index:: delete a barrier
.. index:: rtems_barrier_delete

.. _rtems_barrier_delete:

BARRIER_DELETE - Delete a barrier
---------------------------------

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
    This directive may cause the calling task to be preempted due to an
    obtain and release of the object allocator mutex.

    The calling task will be preempted if it is enabled by the task's execution
    mode and a higher priority local task is waiting on the deleted barrier.
    The calling task will NOT be preempted if all of the tasks that are waiting
    on the barrier are remote tasks.

    The calling task does not have to be the task that created the barrier.
    Any local task that knows the barrier id can delete the barrier.

.. raw:: latex

   \clearpage

.. index:: wait at a barrier
.. index:: rtems_barrier_wait

.. _rtems_barrier_wait:

BARRIER_WAIT - Wait at a barrier
----------------------------------

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

    This directive waits at the barrier specified by ``id``.  The timeout
    parameter specifies the maximum interval the calling task is willing to be
    blocked waiting for the barrier.  If it is set to ``RTEMS_NO_TIMEOUT``,
    then the calling task will wait until the barrier is released.

    Conceptually, the calling task should always be thought of as blocking when
    it makes this call and being unblocked when the barrier is released.  If
    the barrier is configured for manual release, this rule of thumb will
    always be valid.  If the barrier is configured for automatic release, all
    callers will block except for the one which is the Nth task which trips the
    automatic release condition.

NOTES:
    A clock tick is required to support the timeout functionality of this
    directive.

.. raw:: latex

   \clearpage

.. index:: release a barrier
.. index:: rtems_barrier_release

.. _rtems_barrier_release:

BARRIER_RELEASE - Release a barrier
-----------------------------------

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
    the barrier will be unblocked.

NOTES:
    The calling task may be preempted if it causes a higher priority task to be
    made ready for execution.
