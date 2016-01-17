System Databases Manager
########################

Introduction
============

The
system databases manager is ...

The directives provided by the system databases manager are:

- ``getgrgid`` - Get Group File Entry for ID

- ``getgrgid_r`` - Reentrant Get Group File Entry

- ``getgrnam`` - Get Group File Entry for Name

- ``getgrnam_r`` - Reentrant Get Group File Entry for Name

- ``getpwuid`` - Get Password File Entry for UID

- ``getpwuid_r`` - Reentrant Get Password File Entry for UID

- ``getpwnam`` - Get Password File Entry for Name

- ``getpwnam_r`` - Reentrant Get Password File Entry for Name

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the system databases manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

getgrgid - Get Group File Entry for ID
--------------------------------------
.. index:: getgrgid
.. index:: get group file entry for id

**CALLING SEQUENCE:**

.. code:: c

    int getgrgid(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getgrgid_r - Reentrant Get Group File Entry
-------------------------------------------
.. index:: getgrgid_r
.. index:: reentrant get group file entry

**CALLING SEQUENCE:**

.. code:: c

    int getgrgid_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getgrnam - Get Group File Entry for Name
----------------------------------------
.. index:: getgrnam
.. index:: get group file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getgrnam(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getgrnam_r - Reentrant Get Group File Entry for Name
----------------------------------------------------
.. index:: getgrnam_r
.. index:: reentrant get group file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getgrnam_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwuid - Get Password File Entry for UID
------------------------------------------
.. index:: getpwuid
.. index:: get password file entry for uid

**CALLING SEQUENCE:**

.. code:: c

    int getpwuid(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwuid_r - Reentrant Get Password File Entry for UID
------------------------------------------------------
.. index:: getpwuid_r
.. index:: reentrant get password file entry for uid

**CALLING SEQUENCE:**

.. code:: c

    int getpwuid_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwnam - Password File Entry for Name
---------------------------------------
.. index:: getpwnam
.. index:: password file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getpwnam(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getpwnam_r - Reentrant Get Password File Entry for Name
-------------------------------------------------------
.. index:: getpwnam_r
.. index:: reentrant get password file entry for name

**CALLING SEQUENCE:**

.. code:: c

    int getpwnam_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT(c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation(OAR).

.. COMMENT: All rights reserved.

