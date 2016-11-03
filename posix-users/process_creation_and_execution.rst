.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Process Creation and Execution Manager
######################################

Introduction
============

The process creation and execution manager provides the functionality
associated with the creation and termination of processes.

The directives provided by the process creation and execution manager are:

- fork_ - Create a Process

- execl_ - Execute a File

- execv_ - Execute a File

- execle_ - Execute a File

- execve_ - Execute a File

- execlp_ - Execute a File

- execvp_ - Execute a File

- pthread_atfork_ - Register Fork Handlers

- wait_ - Wait for Process Termination

- waitpid_ - Wait for Process Termination

- `_exit`_ - Terminate a Process

Background
==========

POSIX process functionality can not be completely supported by RTEMS.  This is
because RTEMS provides no memory protection and implements a *single process,
multi-threaded execution model*.  In this light, RTEMS provides none of the
routines that are associated with the creation of new processes.  However,
since the entire RTEMS application (e.g. executable) is logically a single
POSIX process, RTEMS is able to provide implementations of many operations on
processes.  The rule of thumb is that those routines provide a meaningful
result.  For example, ``getpid()`` returns the node number.

Operations
==========

The only functionality method defined by this manager which is supported by
RTEMS is the ``_exit`` service.  The implementation of ``_exit`` shuts the
application down and is equivalent to invoking either ``exit`` or
``rtems_shutdown_executive``.

Directives
==========

This section details the process creation and execution manager's directives.
A subsection is dedicated to each of this manager's directives and describes
the calling sequence, related constants, usage, and status codes.

.. _fork:

fork - Create a Process
-----------------------
.. index:: fork
.. index:: create a process

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sys/types.h>
    int fork( void );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _execl:

execl - Execute a File
----------------------
.. index:: execl
.. index:: execute a file

**CALLING SEQUENCE:**

.. code-block:: c

    int execl(
        const char *path,
        const char *arg,
        ...
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _execv:

execv - Execute a File
----------------------
.. index:: execv
.. index:: execute a file

**CALLING SEQUENCE:**

.. code-block:: c

    int execv(
        const char *path,
        char const *argv[],
        ...
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _execle:

execle - Execute a File
-----------------------
.. index:: execle
.. index:: execute a file

**CALLING SEQUENCE:**

.. code-block:: c

    int execle(
        const char *path,
        const char *arg,
        ...
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _execve:

execve - Execute a File
-----------------------
.. index:: execve
.. index:: execute a file

**CALLING SEQUENCE:**

.. code-block:: c

    int execve(
        const char *path,
        char *const argv[],
        char *const envp[]
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _execlp:

execlp - Execute a File
-----------------------
.. index:: execlp
.. index:: execute a file

**CALLING SEQUENCE:**

.. code-block:: c

    int execlp(
        const char *file,
        const char *arg,
        ...
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _execvp:

execvp - Execute a File
-----------------------
.. index:: execvp
.. index:: execute a file

**CALLING SEQUENCE:**

.. code-block:: c

    int execvp(
        const char *file,
        char *const argv[],
        ...
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _pthread_atfork:

pthread_atfork - Register Fork Handlers
---------------------------------------
.. index:: pthread_atfork
.. index:: register fork handlers

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sys/types.h>
    int pthread_atfork(
        void (*prepare)(void),
        void (*parent)(void),
        void (*child)(void)
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _wait:

wait - Wait for Process Termination
-----------------------------------
.. index:: wait
.. index:: wait for process termination

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sys/types.h>
    #include <sys/wait.h>
    int wait(
        int *stat_loc
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _waitpid:

waitpid - Wait for Process Termination
--------------------------------------
.. index:: waitpid
.. index:: wait for process termination

**CALLING SEQUENCE:**

.. code-block:: c

    int wait(
        pid_t  pid,
        int   *stat_loc,
        int    options
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - This routine is not supported by RTEMS.

**DESCRIPTION:**

This routine is not supported by RTEMS.

**NOTES:**

NONE

.. _\_exit:

_exit - Terminate a Process
---------------------------
.. index:: _exit
.. index:: terminate a process

**CALLING SEQUENCE:**

.. code-block:: c

    void _exit(
        int status
    );

**STATUS CODES:**

NONE

**DESCRIPTION:**

The ``_exit()`` function terminates the calling process.

**NOTES:**

In RTEMS, a process is equivalent to the entire application on a single
processor. Invoking this service terminates the application.
