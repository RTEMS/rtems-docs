.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Memory Management Manager
#########################

Introduction
============

The
memory management manager is ...

The directives provided by the memory management manager are:

- mlockall_ - Lock the Address Space of a Process

- munlockall_ - Unlock the Address Space of a Process

- mlock_ - Lock a Range of the Process Address Space

- munlock_ - Unlock a Range of the Process Address Space

- mmap_ - Map Process Addresses to a Memory Object

- munmap_ - Unmap Previously Mapped Addresses

- mprotect_ - Change Memory Protection

- msync_ - Memory Object Synchronization

- shm_open_ - Open a Shared Memory Object

- shm_unlink_ - Remove a Shared Memory Object

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the memory management manager's directives.  A subsection
is dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. _mlockall:

mlockall - Lock the Address Space of a Process
----------------------------------------------
.. index:: mlockall
.. index:: lock the address space of a process

**CALLING SEQUENCE:**

.. code-block:: c

    int mlockall(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _munlockall:

munlockall - Unlock the Address Space of a Process
--------------------------------------------------
.. index:: munlockall
.. index:: unlock the address space of a process

**CALLING SEQUENCE:**

.. code-block:: c

    int munlockall(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _mlock:

mlock - Lock a Range of the Process Address Space
-------------------------------------------------
.. index:: mlock
.. index:: lock a range of the process address space

**CALLING SEQUENCE:**

.. code-block:: c

    int mlock(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _munlock:

munlock - Unlock a Range of the Process Address Space
-----------------------------------------------------
.. index:: munlock
.. index:: unlock a range of the process address space

**CALLING SEQUENCE:**

.. code-block:: c

    int munlock(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _mmap:

mmap - Map Process Addresses to a Memory Object
-----------------------------------------------
.. index:: mmap
.. index:: map process addresses to a memory object

**CALLING SEQUENCE:**

.. code-block:: c

    int mmap(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _munmap:

munmap - Unmap Previously Mapped Addresses
------------------------------------------
.. index:: munmap
.. index:: unmap previously mapped addresses

**CALLING SEQUENCE:**

.. code-block:: c

    int munmap(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _mprotect:

mprotect - Change Memory Protection
-----------------------------------
.. index:: mprotect
.. index:: change memory protection

**CALLING SEQUENCE:**

.. code-block:: c

    int mprotect(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _msync:

msync - Memory Object Synchronization
-------------------------------------
.. index:: msync
.. index:: memory object synchronization

**CALLING SEQUENCE:**

.. code-block:: c

    int msync(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _shm_open:

shm_open - Open a Shared Memory Object
--------------------------------------
.. index:: shm_open
.. index:: open a shared memory object

**CALLING SEQUENCE:**

.. code-block:: c

    int shm_open(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _shm_unlink:

shm_unlink - Remove a Shared Memory Object
------------------------------------------
.. index:: shm_unlink
.. index:: remove a shared memory object

**CALLING SEQUENCE:**

.. code-block:: c

    int shm_unlink(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**
