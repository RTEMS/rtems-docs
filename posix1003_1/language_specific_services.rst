.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Language-Specific Services for the C Programming Language
#########################################################

Referenced C Language Routines
==============================

ANSI C Section 4.2 - Diagnostics
.. code:: c

    assert(), Function, Implemented

ANSI C Section 4.3 - Character Handling
.. code:: c

    isalnum(), Function, Implemented
    isalpha(), Function, Implemented
    iscntrl(), Function, Implemented
    isdigit(), Function, Implemented
    isgraph(), Function, Implemented
    islower(), Function, Implemented
    isprint(), Function, Implemented
    ispunct(), Function, Implemented
    isspace(), Function, Implemented
    isupper(), Function, Implemented
    isxdigit(), Function, Implemented
    tolower(), Function, Implemented
    toupper(), Function, Implemented

ANSI C Section 4.4 - Localization
.. code:: c

    setlocale(), Function, Implemented

ANSI C Section 4.5 - Mathematics
.. code:: c

    acos(), Function, Implemented
    asin(), Function, Implemented
    atan(), Function, Implemented
    atan2(), Function, Implemented
    cos(), Function, Implemented
    sin(), Function, Implemented
    tan(), Function, Implemented
    cosh(), Function, Implemented
    sinh(), Function, Implemented
    tanh(), Function, Implemented
    exp(), Function, Implemented
    frexp(), Function, Implemented
    ldexp(), Function, Implemented
    log(), Function, Implemented
    log10(), Function, Implemented
    modf(), Function, Implemented
    pow(), Function, Implemented
    sqrt(), Function, Implemented
    ceil(), Function, Implemented
    fabs(), Function, Implemented
    floor(), Function, Implemented
    fmod(), Function, Implemented

ANSI C Section 4.6 - Non-Local Jumps
.. code:: c

    setjmp(), Function, Implemented
    longjmp(), Function, Implemented

ANSI C Section 4.9 - Input/Output
.. code:: c

    FILE, Type, Implemented
    clearerr(), Function, Implemented
    fclose(), Function, Implemented
    feof(), Function, Implemented
    ferror(), Function, Implemented
    fflush(), Function, Implemented
    fgetc(), Function, Implemented
    fgets(), Function, Implemented
    fopen(), Function, Implemented
    fputc(), Function, Implemented
    fputs(), Function, Implemented
    fread(), Function, Implemented
    freopen(), Function, Implemented
    fseek(), Function, Implemented
    ftell(), Function, Implemented
    fwrite(), Function, Implemented
    getc(), Function, Implemented
    getchar(), Function, Implemented
    gets(), Function, Implemented
    perror(), Function, Implemented
    printf(), Function, Implemented
    fprintf(), Function, Implemented
    sprintf(), Function, Implemented
    putc(), Function, Implemented
    putchar(), Function, Implemented
    puts(), Function, Implemented
    remove(), Function, Implemented
    rename(), Function, Partial Implementation
    rewind(), Function, Implemented
    scanf(), Function, Implemented
    fscanf(), Function, Implemented
    sscanf(), Function, Implemented
    setbuf(), Function, Implemented
    tmpfile(), Function, Implemented
    tmpnam(), Function, Implemented
    ungetc(), Function, Implemented

NOTE: ``rename`` is also included in another section.  `Rename a File`_.

ANSI C Section 4.10 - General Utilities
.. code:: c

    abs(), Function, Implemented
    atof(), Function, Implemented
    atoi(), Function, Implemented
    atol(), Function, Implemented
    rand(), Function, Implemented
    srand(), Function, Implemented
    calloc(), Function, Implemented
    free(), Function, Implemented
    malloc(), Function, Implemented
    realloc(), Function, Implemented
    abort(), Function, Implemented
    exit(), Function, Implemented
    bsearch(), Function, Implemented
    qsort(), Function, Implemented

NOTE: ``getenv`` is also included in another section. `Environment Access`_.

ANSI C Section 4.11 - String Handling
.. code:: c

    strcpy(), Function, Implemented
    strncpy(), Function, Implemented
    strcat(), Function, Implemented
    strncat(), Function, Implemented
    strcmp(), Function, Implemented
    strncmp(), Function, Implemented
    strchr(), Function, Implemented
    strcspn(), Function, Implemented
    strpbrk(), Function, Implemented
    strrchr(), Function, Implemented
    strspn(), Function, Implemented
    strstr(), Function, Implemented
    strtok(), Function, Implemented
    strlen(), Function, Implemented

ANSI C Section 4.12 - Date and Time Handling
.. code:: c

    asctime(), Function, Implemented
    ctime(), Function, Implemented
    gmtime(), Function, Implemented
    localtime(), Function, Implemented
    mktime(), Function, Implemented
    strftime(), Function, Implemented

NOTE: RTEMS has no notion of time zones.

NOTE: ``time`` is also included in another section. `Get System Time`_.

From Surrounding Text
.. code:: c

    EXIT_SUCCESS, Constant, Implemented
    EXIT_FAILURE, Constant, Implemented

Extensions to Time Functions
----------------------------

Extensions to setlocale Function
--------------------------------

.. code:: c

    LC_CTYPE, Constant, Implemented
    LC_COLLATE, Constant, Implemented
    LC_TIME, Constant, Implemented
    LC_NUMERIC, Constant, Implemented
    LC_MONETARY, Constant, Implemented
    LC_ALL, Constant, Implemented

C Language Input/Output Functions
=================================

Map a Stream Pointer to a File Descriptor
-----------------------------------------

.. code:: c

    fileno(), Function, Implemented
    STDIN_FILENO, Constant, Implemented
    STDOUT_FILENO, Constant, Implemented
    STDERR_FILENO, Constant, Implemented

Open a Stream on a File Descriptor
----------------------------------

.. code:: c

    fdopen(), Function, Implemented

Interactions of Other FILE-Type C Functions
-------------------------------------------

Operations on Files - the remove Function
-----------------------------------------

Temporary File Name - the tmpnam Function
-----------------------------------------

Stdio Locking Functions
-----------------------

.. code:: c

    flockfile(), Function, Unimplemented
    ftrylockfile(), Function, Unimplemented
    funlockfile(), Function, Unimplemented

Stdio With Explicit Client Locking
----------------------------------

.. code:: c

    getc_unlocked(), Function, Unimplemented
    getchar_unlocked(), Function, Unimplemented
    putc_unlocked(), Function, Unimplemented
    putchar_unlocked(), Function, Unimplemented

Other C Language Functions
==========================

Nonlocal Jumps
--------------

.. code:: c

    sigjmp_buf, Type, Implemented
    sigsetjmp(), Function, Implemented
    siglongjmp(), Function, Implemented

Set Time Zone
-------------

.. code:: c

    tzset(), Function, Unimplemented

Find String Token
-----------------

.. code:: c

    strtok_r(), Function, Implemented

ASCII Time Representation
-------------------------

.. code:: c

    asctime_r(), Function, Implemented

Current Time Representation
---------------------------

.. code:: c

    ctime_r(), Function, Implemented

Coordinated Universal Time
--------------------------

.. code:: c

    gmtime_r(), Function, Implemented

Local Time
----------

.. code:: c

    localtime_r(), Function, Implemented

Pseudo-Random Sequence Generation Functions
-------------------------------------------

.. code:: c

    rand_r(), Function, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

