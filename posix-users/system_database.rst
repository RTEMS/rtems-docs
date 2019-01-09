.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)
.. COMMENT: All rights reserved.

System Databases Manager
########################

Introduction
============

The system databases manager is ...

The directives provided by the system databases manager are:

- getgrgid_ - Get Group File Entry for ID

- getgrgid_r_ - Reentrant Get Group File Entry

- getgrnam_ - Get Group File Entry for Name

- getgrnam_r_ - Reentrant Get Group File Entry for Name

- getpwuid_ - Get Password File Entry for UID

- getpwuid_r_ - Reentrant Get Password File Entry for UID

- getpwnam_ - Get Password File Entry for Name

- getpwnam_r_ - Reentrant Get Password File Entry for Name

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the system databases manager's directives.  A subsection
is dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

.. _getgrgid:

getgrgid - Get Group File Entry for ID
--------------------------------------
.. index:: getgrgid
.. index:: get group file entry for id

**CALLING SEQUENCE:**

.. code-block:: c

    #include <grp.h>
    struct group *getgrgid(
        gid_t gid
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getgrgid_r:

getgrgid_r - Reentrant Get Group File Entry
-------------------------------------------
.. index:: getgrgid_r
.. index:: reentrant get group file entry

**CALLING SEQUENCE:**

.. code-block:: c

    #include <grp.h>
    int getgrgid_r(
        gid_t gid,
        struct group *grp,
        char *buffer,
        size_t bufsize,
        struct group **result
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getgrnam:

getgrnam - Get Group File Entry for Name
----------------------------------------
.. index:: getgrnam
.. index:: get group file entry for name

**CALLING SEQUENCE:**

.. code-block:: c

    #include <grp.h>
    struct group *getgrnam(
        const char *name
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getgrnam_r:

getgrnam_r - Reentrant Get Group File Entry for Name
----------------------------------------------------
.. index:: getgrnam_r
.. index:: reentrant get group file entry for name

**CALLING SEQUENCE:**

.. code-block:: c

    #include <grp.h>
    int getgrnam_r(
        const char *name,
        struct group *grp,
        char *buffer,
        size_t bufsize,
        struct group **result
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getpwuid:

getpwuid - Get Password File Entry for UID
------------------------------------------
.. index:: getpwuid
.. index:: get password file entry for uid

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pwd.h>
    struct passwd *getpwuid(
        uid_t uid
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getpwuid_r:

getpwuid_r - Reentrant Get Password File Entry for UID
------------------------------------------------------
.. index:: getpwuid_r
.. index:: reentrant get password file entry for uid

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pwd.h>
    int getpwuid_r(
        uid_t uid,
        struct passwd *pwd,
        char *buffer,
        size_t bufsize,
        struct passwd **result
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getpwnam:

getpwnam - Password File Entry for Name
---------------------------------------
.. index:: getpwnam
.. index:: password file entry for name

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pwd.h>
    struct passwd *getpwnam(
        const char *name
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getpwnam_r:

getpwnam_r - Reentrant Get Password File Entry for Name
-------------------------------------------------------
.. index:: getpwnam_r
.. index:: reentrant get password file entry for name

**CALLING SEQUENCE:**

.. code-block:: c

    #include <pwd.h>
    int getpwnam_r(
        const char *name,
        struct passwd *pwd,
        char *buffer,
        size_t bufsize,
        struct passwd **result
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**
