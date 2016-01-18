Memory Management Manager
#########################

Introduction
============

The
memory management manager is ...

The directives provided by the memory management manager are:

- ``mlockall`` - Lock the Address Space of a Process

- ``munlockall`` - Unlock the Address Space of a Process

- ``mlock`` - Lock a Range of the Process Address Space

- ``munlock`` - Unlock a Range of the Process Address Space

- ``mmap`` - Map Process Addresses to a Memory Object

- ``munmap`` - Unmap Previously Mapped Addresses

- ``mprotect`` - Change Memory Protection

- ``msync`` - Memory Object Synchronization

- ``shm_open`` - Open a Shared Memory Object

- ``shm_unlink`` - Remove a Shared Memory Object

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the memory management manager's directives.
A subsection is dedicated to each of this manager's directives
and describes the calling sequence, related constants, usage,
and status codes.

mlockall - Lock the Address Space of a Process
----------------------------------------------
.. index:: mlockall
.. index:: lock the address space of a process

**CALLING SEQUENCE:**

.. code:: c

    int mlockall(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

munlockall - Unlock the Address Space of a Process
--------------------------------------------------
.. index:: munlockall
.. index:: unlock the address space of a process

**CALLING SEQUENCE:**

.. code:: c

    int munlockall(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

mlock - Lock a Range of the Process Address Space
-------------------------------------------------
.. index:: mlock
.. index:: lock a range of the process address space

**CALLING SEQUENCE:**

.. code:: c

    int mlock(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

munlock - Unlock a Range of the Process Address Space
-----------------------------------------------------
.. index:: munlock
.. index:: unlock a range of the process address space

**CALLING SEQUENCE:**

.. code:: c

    int munlock(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

mmap - Map Process Addresses to a Memory Object
-----------------------------------------------
.. index:: mmap
.. index:: map process addresses to a memory object

**CALLING SEQUENCE:**

.. code:: c

    int mmap(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

munmap - Unmap Previously Mapped Addresses
------------------------------------------
.. index:: munmap
.. index:: unmap previously mapped addresses

**CALLING SEQUENCE:**

.. code:: c

    int munmap(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

mprotect - Change Memory Protection
-----------------------------------
.. index:: mprotect
.. index:: change memory protection

**CALLING SEQUENCE:**

.. code:: c

    int mprotect(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

msync - Memory Object Synchronization
-------------------------------------
.. index:: msync
.. index:: memory object synchronization

**CALLING SEQUENCE:**

.. code:: c

    int msync(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

shm_open - Open a Shared Memory Object
--------------------------------------
.. index:: shm_open
.. index:: open a shared memory object

**CALLING SEQUENCE:**

.. code:: c

    int shm_open(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

shm_unlink - Remove a Shared Memory Object
------------------------------------------
.. index:: shm_unlink
.. index:: remove a shared memory object

**CALLING SEQUENCE:**

.. code:: c

    int shm_unlink(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

