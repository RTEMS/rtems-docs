.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)
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

    #include <locale.h>
    char *setlocale(int category, const char *locale);

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

    #include <stdio.h>
    int fileno(FILE *stream);

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

    #include <stdio.h>
    FILE *fdopen(int fildes, const char *mode);

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

    #include <stdio.h>
    void flockfile(FILE *file);

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

    #include <stdio.h>
    int ftrylockfile(FILE *file);

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

    #include <stdio.h>
    void funlockfile(FILE *file);

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

    #include <stdio.h>
    int getc_unlocked(FILE *stream);

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

    #include <stdio.h>
    int getchar_unlocked(void);

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

    #include <stdio.h>
    int putc_unlocked(int c, FILE *stream);

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

    #include <stdio.h>
    int putchar_unlocked(int c);

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

    #include <setjmp.h>
    int setjmp(jmp_buf env);

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

    #include <setjmp.h>
    void longjmp(jmp_buf env, int val);

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

    #include <setjmp.h>
    int sigsetjmp(sigjmp_buf env, int savemask);

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

    #include <setjmp.h>
    void siglongjmp(sigjmp_buf env, int val);

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

    #include <time.h>
    extern int daylight;
    extern long timezone;
    extern char *tzname[2];
    void tzset(void);

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

    #include <string.h>
    char *strtok_r(char *restrict s, const char *restrict sep,
    char **restrict state);

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

    #include <time.h>
    char *asctime_r(const struct tm *restrict tm, char *restrict buf);

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

    #include <time.h>
    char *ctime_r(const time_t *clock, char *buf);

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

    #include <time.h>
    struct tm *gmtime_r(const time_t *restrict timer,
    struct tm *restrict result);

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

    #include <time.h>
    struct tm *localtime_r(const time_t *restrict timer,
    struct tm *restrict result);

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

    #include <stdlib.h>
    int rand_r(unsigned *seed);

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**
