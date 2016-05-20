.. comment SPDX-License-Identifier: CC-BY-SA-4.0

System Databases
################

System Databases Section
========================

Database Access
===============

Group Database Access
---------------------

.. code:: c

    struct group, Type, Implemented
    getgrgid(), Function, Implemented
    getgrgid_r(), Function, Implemented
    getgrname(), Function, Implemented
    getgrnam_r(), Function, Implemented

NOTE: Creates /etc/group if none exists.

User Database Access
--------------------

.. code:: c

    struct passwd, Type, Implemented
    getpwuid(), Function, Implemented
    getpwuid_r(), Function, Implemented
    getpwnam(), Function, Implemented
    getpwnam_r(), Function, Implemented

NOTE: Creates /etc/passwd if none exists.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

