Language-Specific Services for the C Programming Language Manager
#################################################################

Introduction
============

The
language-specific services for the C programming language manager is ...

The directives provided by the language-specific services for the C programming language manager are:

- ``setlocale`` - Set the Current Locale

- ``fileno`` - Obtain File Descriptor Number for this File

- ``fdopen`` - Associate Stream with File Descriptor

- ``flockfile`` - Acquire Ownership of File Stream

- ``ftrylockfile`` - Poll to Acquire Ownership of File Stream

- ``funlockfile`` - Release Ownership of File Stream

- ``getc_unlocked`` - Get Character without Locking

- ``getchar_unlocked`` - Get Character from stdin without Locking

- ``putc_unlocked`` - Put Character without Locking

- ``putchar_unlocked`` - Put Character to stdin without Locking

- ``setjmp`` - Save Context for Non-Local Goto

- ``longjmp`` - Non-Local Jump to a Saved Context

- ``sigsetjmp`` - Save Context with Signal Status for Non-Local Goto

- ``siglongjmp`` - Non-Local Jump with Signal Status to a Saved Context

- ``tzset`` - Initialize Time Conversion Information

- ``strtok_r`` - Reentrant Extract Token from String

- ``asctime_r`` - Reentrant struct tm to ASCII Time Conversion

- ``ctime_r`` - Reentrant time_t to ASCII Time Conversion

- ``gmtime_r`` - Reentrant UTC Time Conversion

- ``localtime_r`` - Reentrant Local Time Conversion

- ``rand_r`` - Reentrant Random Number Generation

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the language-specific services for the C programming language manager’s directives.
A subsection is dedicated to each of this manager’s directives
and describes the calling sequence, related constants, usage,
and status codes.

setlocale - Set the Current Locale
----------------------------------
.. index:: setlocale
.. index:: set the current locale

**CALLING SEQUENCE:**

.. code:: c

    int setlocale(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

fileno - Obtain File Descriptor Number for this File
----------------------------------------------------
.. index:: fileno
.. index:: obtain file descriptor number for this file

**CALLING SEQUENCE:**

.. code:: c

    int fileno(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

fdopen - Associate Stream with File Descriptor
----------------------------------------------
.. index:: fdopen
.. index:: associate stream with file descriptor

**CALLING SEQUENCE:**

.. code:: c

    int fdopen(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

flockfile - Acquire Ownership of File Stream
--------------------------------------------
.. index:: flockfile
.. index:: acquire ownership of file stream

**CALLING SEQUENCE:**

.. code:: c

    int flockfile(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

ftrylockfile - Poll to Acquire Ownership of File Stream
-------------------------------------------------------
.. index:: ftrylockfile
.. index:: poll to acquire ownership of file stream

**CALLING SEQUENCE:**

.. code:: c

    int ftrylockfile(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

funlockfile - Release Ownership of File Stream
----------------------------------------------
.. index:: funlockfile
.. index:: release ownership of file stream

**CALLING SEQUENCE:**

.. code:: c

    int funlockfile(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getc_unlocked - Get Character without Locking
---------------------------------------------
.. index:: getc_unlocked
.. index:: get character without locking

**CALLING SEQUENCE:**

.. code:: c

    int getc_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

getchar_unlocked - Get Character from stdin without Locking
-----------------------------------------------------------
.. index:: getchar_unlocked
.. index:: get character from stdin without locking

**CALLING SEQUENCE:**

.. code:: c

    int getchar_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

putc_unlocked - Put Character without Locking
---------------------------------------------
.. index:: putc_unlocked
.. index:: put character without locking

**CALLING SEQUENCE:**

.. code:: c

    int putc_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

putchar_unlocked - Put Character to stdin without Locking
---------------------------------------------------------
.. index:: putchar_unlocked
.. index:: put character to stdin without locking

**CALLING SEQUENCE:**

.. code:: c

    int putchar_unlocked(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

setjmp - Save Context for Non-Local Goto
----------------------------------------
.. index:: setjmp
.. index:: save context for non

**CALLING SEQUENCE:**

.. code:: c

    int setjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

longjmp - Non-Local Jump to a Saved Context
-------------------------------------------
.. index:: longjmp
.. index:: non

**CALLING SEQUENCE:**

.. code:: c

    int longjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

sigsetjmp - Save Context with Signal Status for Non-Local Goto
--------------------------------------------------------------
.. index:: sigsetjmp
.. index:: save context with signal status for non

**CALLING SEQUENCE:**

.. code:: c

    int sigsetjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

siglongjmp - Non-Local Jump with Signal Status to a Saved Context
-----------------------------------------------------------------
.. index:: siglongjmp
.. index:: non

**CALLING SEQUENCE:**

.. code:: c

    int siglongjmp(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

tzset - Initialize Time Conversion Information
----------------------------------------------
.. index:: tzset
.. index:: initialize time conversion information

**CALLING SEQUENCE:**

.. code:: c

    int tzset(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

strtok_r - Reentrant Extract Token from String
----------------------------------------------
.. index:: strtok_r
.. index:: reentrant extract token from string

**CALLING SEQUENCE:**

.. code:: c

    int strtok_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

asctime_r - Reentrant struct tm to ASCII Time Conversion
--------------------------------------------------------
.. index:: asctime_r
.. index:: reentrant struct tm to ascii time conversion

**CALLING SEQUENCE:**

.. code:: c

    int asctime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

ctime_r - Reentrant time_t to ASCII Time Conversion
---------------------------------------------------
.. index:: ctime_r
.. index:: reentrant time_t to ascii time conversion

**CALLING SEQUENCE:**

.. code:: c

    int ctime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

gmtime_r - Reentrant UTC Time Conversion
----------------------------------------
.. index:: gmtime_r
.. index:: reentrant utc time conversion

**CALLING SEQUENCE:**

.. code:: c

    int gmtime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

localtime_r - Reentrant Local Time Conversion
---------------------------------------------
.. index:: localtime_r
.. index:: reentrant local time conversion

**CALLING SEQUENCE:**

.. code:: c

    int localtime_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

rand_r - Reentrant Random Number Generation
-------------------------------------------
.. index:: rand_r
.. index:: reentrant random number generation

**CALLING SEQUENCE:**

.. code:: c

    int rand_r(
    );

**STATUS CODES:**

*E*
    The

**DESCRIPTION:**

**NOTES:**

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

