.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Deprecated Directives
=====================

.. raw:: latex

   \clearpage

.. index:: rtems_iterate_over_all_threads

.. _rtems_iterate_over_all_threads:

ITERATE_OVER_ALL_THREADS - Iterate Over Tasks
---------------------------------------------

.. warning::

    This directive is deprecated.  Its use is unsafe.  Use
    :ref:`rtems_task_iterate` instead.

CALLING SEQUENCE:
    .. code-block:: c

        typedef void (*rtems_per_thread_routine)(Thread_Control *the_thread);
        void rtems_iterate_over_all_threads(
            rtems_per_thread_routine routine
        );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive iterates over all of the existant threads in the system and
    invokes ``routine`` on each of them.  The user should be careful in
    accessing the contents of ``the_thread``.

    This routine is intended for use in diagnostic utilities and is not
    intented for routine use in an operational system.

NOTES:
    There is **no protection** while this routine is called.  The thread
    control block may be in an inconsistent state or may change due to
    interrupts or activity on other processors.
