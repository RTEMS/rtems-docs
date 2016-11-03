.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Language-Specific Services for the C Programming Language Manager
#################################################################

Introduction
============

The language-specific services for the C programming language manager is ...

The directives provided by the language-specific services for the C programming language manager are:

- setlocale_ - Set the Current Locale

- fileno_ - Obtain File Descriptor Number for this File

- fdopen_ - Associate Stream with File Descriptor

- flockfile_ - Acquire Ownership of File Stream

- ftrylockfile_ - Poll to Acquire Ownership of File Stream

- funlockfile_ - Release Ownership of File Stream

- getc_unlocked_ - Get Character without Locking

- getchar_unlocked_ - Get Character from stdin without Locking

- putc_unlocked_ - Put Character without Locking

- putchar_unlocked_ - Put Character to stdin without Locking

- setjmp_ - Save Context for Non-Local Goto

- longjmp_ - Non-Local Jump to a Saved Context

- sigsetjmp_ - Save Context with Signal Status for Non-Local Goto

- siglongjmp_ - Non-Local Jump with Signal Status to a Saved Context

- tzset_ - Initialize Time Conversion Information

- strtok_r_ - Reentrant Extract Token from String

- asctime_r_ - Reentrant struct tm to ASCII Time Conversion

- ctime_r_ - Reentrant time_t to ASCII Time Conversion

- gmtime_r_ - Reentrant UTC Time Conversion

- localtime_r_ - Reentrant Local Time Conversion

- rand_r_ - Reentrant Random Number Generation

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the language-specific services for the C programming
language manager's directives.  A subsection is dedicated to each of this
manager's directives and describes the calling sequence, related constants,
usage, and status codes.

.. _setlocale:

setlocale - Set the Current Locale
----------------------------------
.. index:: setlocale
.. index:: set the current locale

**CALLING SEQUENCE:**

.. code-block:: c

    int setlocale(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _fileno:

fileno - Obtain File Descriptor Number for this File
----------------------------------------------------
.. index:: fileno
.. index:: obtain file descriptor number for this file

**CALLING SEQUENCE:**

.. code-block:: c

    int fileno(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _fdopen:

fdopen - Associate Stream with File Descriptor
----------------------------------------------
.. index:: fdopen
.. index:: associate stream with file descriptor

**CALLING SEQUENCE:**

.. code-block:: c

    int fdopen(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _flockfile:

flockfile - Acquire Ownership of File Stream
--------------------------------------------
.. index:: flockfile
.. index:: acquire ownership of file stream

**CALLING SEQUENCE:**

.. code-block:: c

    int flockfile(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _ftrylockfile:

ftrylockfile - Poll to Acquire Ownership of File Stream
-------------------------------------------------------
.. index:: ftrylockfile
.. index:: poll to acquire ownership of file stream

**CALLING SEQUENCE:**

.. code-block:: c

    int ftrylockfile(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _funlockfile:

funlockfile - Release Ownership of File Stream
----------------------------------------------
.. index:: funlockfile
.. index:: release ownership of file stream

**CALLING SEQUENCE:**

.. code-block:: c

    int funlockfile(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getc_unlocked:

getc_unlocked - Get Character without Locking
---------------------------------------------
.. index:: getc_unlocked
.. index:: get character without locking

**CALLING SEQUENCE:**

.. code-block:: c

    int getc_unlocked(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _getchar_unlocked:

getchar_unlocked - Get Character from stdin without Locking
-----------------------------------------------------------
.. index:: getchar_unlocked
.. index:: get character from stdin without locking

**CALLING SEQUENCE:**

.. code-block:: c

    int getchar_unlocked(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _putc_unlocked:

putc_unlocked - Put Character without Locking
---------------------------------------------
.. index:: putc_unlocked
.. index:: put character without locking

**CALLING SEQUENCE:**

.. code-block:: c

    int putc_unlocked(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _putchar_unlocked:

putchar_unlocked - Put Character to stdin without Locking
---------------------------------------------------------
.. index:: putchar_unlocked
.. index:: put character to stdin without locking

**CALLING SEQUENCE:**

.. code-block:: c

    int putchar_unlocked(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _setjmp:

setjmp - Save Context for Non-Local Goto
----------------------------------------
.. index:: setjmp
.. index:: save context for non

**CALLING SEQUENCE:**

.. code-block:: c

    int setjmp(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _longjmp:

longjmp - Non-Local Jump to a Saved Context
-------------------------------------------
.. index:: longjmp
.. index:: non

**CALLING SEQUENCE:**

.. code-block:: c

    int longjmp(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _sigsetjmp:

sigsetjmp - Save Context with Signal Status for Non-Local Goto
--------------------------------------------------------------
.. index:: sigsetjmp
.. index:: save context with signal status for non

**CALLING SEQUENCE:**

.. code-block:: c

    int sigsetjmp(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _siglongjmp:

siglongjmp - Non-Local Jump with Signal Status to a Saved Context
-----------------------------------------------------------------
.. index:: siglongjmp
.. index:: non

**CALLING SEQUENCE:**

.. code-block:: c

    int siglongjmp(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _tzset:

tzset - Initialize Time Conversion Information
----------------------------------------------
.. index:: tzset
.. index:: initialize time conversion information

**CALLING SEQUENCE:**

.. code-block:: c

    int tzset(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _strtok_r:

strtok_r - Reentrant Extract Token from String
----------------------------------------------
.. index:: strtok_r
.. index:: reentrant extract token from string

**CALLING SEQUENCE:**

.. code-block:: c

    int strtok_r(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _asctime_r:

asctime_r - Reentrant struct tm to ASCII Time Conversion
--------------------------------------------------------
.. index:: asctime_r
.. index:: reentrant struct tm to ascii time conversion

**CALLING SEQUENCE:**

.. code-block:: c

    int asctime_r(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _ctime_r:

ctime_r - Reentrant time_t to ASCII Time Conversion
---------------------------------------------------
.. index:: ctime_r
.. index:: reentrant time_t to ascii time conversion

**CALLING SEQUENCE:**

.. code-block:: c

    int ctime_r(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _gmtime_r:

gmtime_r - Reentrant UTC Time Conversion
----------------------------------------
.. index:: gmtime_r
.. index:: reentrant utc time conversion

**CALLING SEQUENCE:**

.. code-block:: c

    int gmtime_r(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _localtime_r:

localtime_r - Reentrant Local Time Conversion
---------------------------------------------
.. index:: localtime_r
.. index:: reentrant local time conversion

**CALLING SEQUENCE:**

.. code-block:: c

    int localtime_r(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _rand_r:

rand_r - Reentrant Random Number Generation
-------------------------------------------
.. index:: rand_r
.. index:: reentrant random number generation

**CALLING SEQUENCE:**

.. code-block:: c

    int rand_r(
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**
