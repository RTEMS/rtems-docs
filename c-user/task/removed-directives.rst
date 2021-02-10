.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Removed Directives
==================

.. raw:: latex

   \clearpage

.. index:: get task notepad entry
.. index:: rtems_task_get_note

.. _rtems_task_get_note:

TASK_GET_NOTE - Get task notepad entry
--------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_get_note(
          rtems_id  id,
          uint32_t  notepad,
          uint32_t *note
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - note value obtained successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``note`` parameter is NULL
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_INVALID_NUMBER``
        - invalid notepad location

DESCRIPTION:
    This directive returns the note contained in the notepad location of the
    task specified by id.

NOTES:
    This directive will not cause the running task to be preempted.

    If id is set to ``RTEMS_SELF``, the calling task accesses its own notepad.

    The sixteen notepad locations can be accessed using the constants
    ``RTEMS_NOTEPAD_0`` through ``RTEMS_NOTEPAD_15``.

    Getting a note of a global task which does not reside on the local node
    will generate a request to the remote node to obtain the notepad entry of
    the specified task.

.. raw:: latex

   \clearpage

.. index:: set task notepad entry
.. index:: rtems_task_set_note

.. _rtems_task_set_note:

TASK_SET_NOTE - Set task notepad entry
--------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_set_note(
          rtems_id  id,
          uint32_t  notepad,
          uint32_t  note
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - note set successfully
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_INVALID_NUMBER``
        - invalid notepad location

DESCRIPTION:
    This directive sets the notepad entry for the task specified by id to the
    value note.

NOTES:
    If ``id`` is set to ``RTEMS_SELF``, the calling task accesses its own
    notepad.

    This directive will not cause the running task to be preempted.

    The sixteen notepad locations can be accessed using the constants
    ``RTEMS_NOTEPAD_0`` through ``RTEMS_NOTEPAD_15``.

    Setting a note of a global task which does not reside on the local node
    will generate a request to the remote node to set the notepad entry of the
    specified task.

.. raw:: latex

   \clearpage

.. index:: per-task variable
.. index:: task private variable
.. index:: task private data
.. index:: rtems_task_variable_add

.. _rtems_task_variable_add:

TASK_VARIABLE_ADD - Associate per task variable
-----------------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_variable_add(
            rtems_id  tid,
            void    **task_variable,
            void    (*dtor)(void *)
        );

DIRECTIVE STATUS CODES:
     .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - per task variable added successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is NULL
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_NO_MEMORY``
        - invalid task id
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive adds the memory location specified by the ptr argument to
    the context of the given task.  The variable will then be private to the
    task.  The task can access and modify the variable, but the modifications
    will not appear to other tasks, and other tasks' modifications to that
    variable will not affect the value seen by the task.  This is accomplished
    by saving and restoring the variable's value each time a task switch occurs
    to or from the calling task.  If the dtor argument is non-NULL it specifies
    the address of a 'destructor' function which will be called when the task
    is deleted.  The argument passed to the destructor function is the task's
    value of the variable.

NOTES:
    Task variables increase the context switch time to and from the tasks that
    own them so it is desirable to minimize the number of task variables.  One
    efficient method is to have a single task variable that is a pointer to a
    dynamically allocated structure containing the task's private 'global'
    data.  In this case the destructor function could be 'free'.

    Per-task variables are disabled in SMP configurations and this service is
    not available.

.. raw:: latex

   \clearpage

.. index:: get per-task variable
.. index:: obtain per-task variable
.. index:: rtems_task_variable_get

.. _rtems_task_variable_get:

TASK_VARIABLE_GET - Obtain value of a per task variable
-------------------------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_variable_get(
            rtems_id  tid,
            void    **task_variable,
            void    **task_variable_value
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - per task variable obtained successfully
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is NULL
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable_value`` is NULL
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is not found
      * - ``RTEMS_NO_MEMORY``
        - invalid task id
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive looks up the private value of a task variable for a
    specified task and stores that value in the location pointed to by the
    result argument.  The specified task is usually not the calling task, which
    can get its private value by directly accessing the variable.

NOTES:
    If you change memory which ``task_variable_value`` points to, remember to
    declare that memory as volatile, so that the compiler will optimize it
    correctly.  In this case both the pointer ``task_variable_value`` and data
    referenced by ``task_variable_value`` should be considered volatile.

    Per-task variables are disabled in SMP configurations and this service is
    not available.

.. raw:: latex

   \clearpage

.. index:: per-task variable
.. index:: task private variable
.. index:: task private data
.. index:: rtems_task_variable_delete

.. _rtems_task_variable_delete:

TASK_VARIABLE_DELETE - Remove per task variable
-----------------------------------------------

.. warning::

    This directive was removed in RTEMS 5.1.

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_task_variable_delete(
            rtems_id  id,
            void    **task_variable
        );

DIRECTIVE STATUS CODES:
    .. list-table::
      :class: rtems-table

      * - ``RTEMS_SUCCESSFUL``
        - per task variable deleted successfully
      * - ``RTEMS_INVALID_ID``
        - invalid task id
      * - ``RTEMS_NO_MEMORY``
        - invalid task id
      * - ``RTEMS_INVALID_ADDRESS``
        - ``task_variable`` is NULL
      * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
        - not supported on remote tasks

DESCRIPTION:
    This directive removes the given location from a task's context.

NOTES:
    Per-task variables are disabled in SMP configurations and this service is
    not available.
