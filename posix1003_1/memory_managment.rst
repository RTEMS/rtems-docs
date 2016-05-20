.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Memory Management
#################

Memory Locking Functions
========================

Lock/Unlock the Address Space of a Process
------------------------------------------

.. code:: c

    mlockall(), Function, Unimplemented
    munlockall(), Function, Unimplemented
    MCL_CURRENT, Constant, Unimplemented
    MCL_FUTURE, Constant,  Unimplemented

Lock/Unlock a Rand of Process Address Space
-------------------------------------------

.. code:: c

    mlock(), Function, Unimplemented
    munlock(), Function, Unimplemented

Memory Mapping Functions
========================

Map Process Addresses to a Memory Object
----------------------------------------

.. code:: c

    mmap(), Function, Unimplemented
    PROT_READ, Constant,  Unimplemented
    PROT_WRITE, Constant,  Unimplemented
    PROT_EXEC, Constant,  Unimplemented
    PROT_NONE, Constant,  Unimplemented
    MAP_SHARED, Constant,  Unimplemented
    MAP_PRIVATE, Constant,  Unimplemented
    MAP_FIXED, Constant,  Unimplemented

Unmap Previously Mapped Addresses
---------------------------------

.. code:: c

    munmap(), Function, Unimplemented

Change Memory Protection
------------------------

.. code:: c

    mprotect(), Function, Unimplemented

Memory Object Synchronization
-----------------------------

.. code:: c

    msync(), Function, Unimplemented, Unimplemented
    MS_ASYNC, Constant, Unimplemented
    MS_SYNC, Constant,  Unimplemented
    MS_INVALIDATE, Constant,  Unimplemented

Shared Memory Functions
=======================

Open a Shared Memory Object
---------------------------

.. code:: c

    shm_open(), Function, Unimplemented

Remove a Shared Memory Object
-----------------------------

.. code:: c

    shm_unlink(), Function, Unimplemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

