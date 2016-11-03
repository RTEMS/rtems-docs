.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Process Environment Manager
###########################

Introduction
============

The process environment manager is responsible for providing the functions
related to user and group Id management.

The directives provided by the process environment manager are:

- getpid_ - Get Process ID

- getppid_ - Get Parent Process ID

- getuid_ - Get User ID

- geteuid_ - Get Effective User ID

- getgid_ - Get Real Group ID

- getegid_ - Get Effective Group ID

- setuid_ - Set User ID

- setgid_ - Set Group ID

- getgroups_ - Get Supplementary Group IDs

- getlogin_ - Get User Name

- getlogin_r_ - Reentrant Get User Name

- getpgrp_ - Get Process Group ID

- setsid_ - Create Session and Set Process Group ID

- setpgid_ - Set Process Group ID for Job Control

- uname_ - Get System Name

- times_ - Get Process Times

- getenv_ - Get Environment Variables

- setenv_ - Set Environment Variables

- ctermid_ - Generate Terminal Pathname

- ttyname_ - Determine Terminal Device Name

- ttyname_r_ - Reentrant Determine Terminal Device Name

- isatty_ - Determine if File Descriptor is Terminal

- sysconf_ - Get Configurable System Variables

Background
==========

Users and Groups
----------------

RTEMS provides a single process, multi-threaded execution environment.  In this
light, the notion of user and group is somewhat without meaning.  But RTEMS
does provide services to provide a synthetic version of user and group.  By
default, a single user and group is associated with the application.  Thus
unless special actions are taken, every thread in the application shares the
same user and group Id.  The initial rationale for providing user and group Id
functionality in RTEMS was for the filesystem infrastructure to implement file
permission checks.  The effective user/group Id capability has since been used
to implement permissions checking by the ``ftpd`` server.

In addition to the "real" user and group Ids, a process may have an effective
user/group Id.  This allows a process to function using a more limited
permission set for certain operations.

User and Group Names
--------------------

POSIX considers user and group Ids to be a unique integer that may be
associated with a name.  This is usually accomplished via a file named
:file:`/etc/passwd` for user Id mapping and :file:`/etc/groups` for group Id
mapping.  Again, although RTEMS is effectively a single process and thus single
user system, it provides limited support for user and group names.  When
configured with an appropriate filesystem, RTEMS will access the appropriate
files to map user and group Ids to names.

If these files do not exist, then RTEMS will synthesize a minimal version so
this family of services return without error.  It is important to remember that
a design goal of the RTEMS POSIX services is to provide useable and meaningful
results even though a full process model is not available.

Environment Variables
---------------------

POSIX allows for variables in the run-time environment.  These are name/value
pairs that make be dynamically set and obtained by programs.  In a full POSIX
environment with command line shell and multiple processes, environment
variables may be set in one process - such as the shell - and inherited by
child processes.  In RTEMS, there is only one process and thus only one set of
environment variables across all processes.

Operations
==========

Accessing User and Group Ids
----------------------------

The user Id associated with the current thread may be obtain using the
``getuid()`` service.  Similarly, the group Id may be obtained using the
``getgid()`` service.

Accessing Environment Variables
-------------------------------

The value associated with an environment variable may be obtained using the
``getenv()`` service and set using the ``putenv()`` service.

Directives
==========

This section details the process environment manager's directives.  A
subsection is dedicated to each of this manager's directives and describes the
calling sequence, related constants, usage, and status codes.

.. _getpid:

getpid - Get Process ID
-----------------------
.. index:: getpid
.. index:: get process id

**CALLING SEQUENCE:**

.. code-block:: c

    int getpid( void );

**STATUS CODES:**

The process Id is returned.

**DESCRIPTION:**

This service returns the process Id.

**NOTES:**

NONE

.. _getppid:

getppid - Get Parent Process ID
-------------------------------
.. index:: getppid
.. index:: get parent process id

**CALLING SEQUENCE:**

.. code-block:: c

    int getppid( void );

**STATUS CODES:**

The parent process Id is returned.

**DESCRIPTION:**

This service returns the parent process Id.

**NOTES:**

NONE

.. _getuid:

getuid - Get User ID
--------------------
.. index:: getuid
.. index:: get user id

**CALLING SEQUENCE:**

.. code-block:: c

    int getuid( void );

**STATUS CODES:**

The effective user Id is returned.

**DESCRIPTION:**

This service returns the effective user Id.

**NOTES:**

NONE

.. _geteuid:

geteuid - Get Effective User ID
-------------------------------
.. index:: geteuid
.. index:: get effective user id

**CALLING SEQUENCE:**

.. code-block:: c

    int geteuid( void );

**STATUS CODES:**

The effective group Id is returned.

**DESCRIPTION:**

This service returns the effective group Id.

**NOTES:**

NONE

.. _getgid:

getgid - Get Real Group ID
--------------------------
.. index:: getgid
.. index:: get real group id

**CALLING SEQUENCE:**

.. code-block:: c

    int getgid( void );

**STATUS CODES:**

The group Id is returned.

**DESCRIPTION:**

This service returns the group Id.

**NOTES:**

NONE

.. _getegid:

getegid - Get Effective Group ID
--------------------------------
.. index:: getegid
.. index:: get effective group id

**CALLING SEQUENCE:**

.. code-block:: c

    int getegid( void );

**STATUS CODES:**

The effective group Id is returned.

**DESCRIPTION:**

This service returns the effective group Id.

**NOTES:**

NONE

.. _setuid:

setuid - Set User ID
--------------------
.. index:: setuid
.. index:: set user id

**CALLING SEQUENCE:**

.. code-block:: c

    int setuid(
        uid_t uid
    );

**STATUS CODES:**

This service returns 0.

**DESCRIPTION:**

This service sets the user Id to ``uid``.

**NOTES:**

NONE

.. _setgid:

setgid - Set Group ID
---------------------
.. index:: setgid
.. index:: set group id

**CALLING SEQUENCE:**

.. code-block:: c

    int setgid(
        gid_t  gid
    );

**STATUS CODES:**

This service returns 0.

**DESCRIPTION:**

This service sets the group Id to ``gid``.

**NOTES:**

NONE

.. _getgroups:

getgroups - Get Supplementary Group IDs
---------------------------------------
.. index:: getgroups
.. index:: get supplementary group ids

**CALLING SEQUENCE:**

.. code-block:: c

    int getgroups(
        int    gidsetsize,
        gid_t  grouplist[]
    );

**STATUS CODES:**

NA

**DESCRIPTION:**

This service is not implemented as RTEMS has no notion of supplemental groups.

**NOTES:**

If supported, this routine would only be allowed for the super-user.

.. _getlogin:

getlogin - Get User Name
------------------------
.. index:: getlogin
.. index:: get user name

**CALLING SEQUENCE:**

.. code-block:: c

    char *getlogin( void );

**STATUS CODES:**

Returns a pointer to a string containing the name of the current user.

**DESCRIPTION:**

This routine returns the name of the current user.

**NOTES:**

This routine is not reentrant and subsequent calls to ``getlogin()`` will
overwrite the same buffer.

.. _getlogin_r:

getlogin_r - Reentrant Get User Name
------------------------------------
.. index:: getlogin_r
.. index:: reentrant get user name
.. index:: get user name, reentrant

**CALLING SEQUENCE:**

.. code-block:: c

    int getlogin_r(
        char   *name,
        size_t  namesize
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EINVAL``
   - The arguments were invalid.

**DESCRIPTION:**

This is a reentrant version of the ``getlogin()`` service.  The caller
specified their own buffer, ``name``, as well as the length of this buffer,
``namesize``.

**NOTES:**

NONE

.. _getpgrp:

getpgrp - Get Process Group ID
------------------------------
.. index:: getpgrp
.. index:: get process group id

**CALLING SEQUENCE:**

.. code-block:: c

    pid_t getpgrp( void );

**STATUS CODES:**

The procress group Id is returned.

**DESCRIPTION:**

This service returns the current progress group Id.

**NOTES:**

This routine is implemented in a somewhat meaningful way for RTEMS but is truly
not functional.

.. _setsid:

setsid - Create Session and Set Process Group ID
------------------------------------------------
.. index:: setsid
.. index:: create session and set process group id

**CALLING SEQUENCE:**

.. code-block:: c

    pid_t setsid( void );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EPERM``
   - The application does not have permission to create a process group.

**DESCRIPTION:**

This routine always returns ``EPERM`` as RTEMS has no way to create new
processes and thus no way to create a new process group.

**NOTES:**

NONE

.. _setpgid:

setpgid - Set Process Group ID for Job Control
----------------------------------------------
.. index:: setpgid
.. index:: set process group id for job control

**CALLING SEQUENCE:**

.. code-block:: c

    int setpgid(
        pid_t pid,
        pid_t pgid
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``ENOSYS``
   - The routine is not implemented.

**DESCRIPTION:**

This service is not implemented for RTEMS as process groups are not supported.

**NOTES:**

NONE

.. _uname:

uname - Get System Name
-----------------------
.. index:: uname
.. index:: get system name

**CALLING SEQUENCE:**

.. code-block:: c

    int uname(
        struct utsname *name
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EPERM``
   - The provided structure pointer is invalid.

**DESCRIPTION:**

This service returns system information to the caller.  It does this by filling
in the ``struct utsname`` format structure for the caller.

**NOTES:**

The information provided includes the operating system (RTEMS in all
configurations), the node number, the release as the RTEMS version, and the CPU
family and model.  The CPU model name will indicate the multilib executive
variant being used.

.. _times:

times - Get process times
-------------------------
.. index:: times
.. index:: get process times

**CALLING SEQUENCE:**

.. code-block:: c

    #include <sys/time.h>
    clock_t times(
        struct tms *ptms
    );

**STATUS CODES:**

This routine returns the number of clock ticks that have elapsed since the
system was initialized (e.g. the application was started).

**DESCRIPTION:**

``times`` stores the current process times in ``ptms``.  The format of ``struct
tms`` is as defined in ``<sys/times.h>``.  RTEMS fills in the field
``tms_utime`` with the number of ticks that the calling thread has executed and
the field ``tms_stime`` with the number of clock ticks since system boot (also
returned).  All other fields in the ``ptms`` are left zero.

**NOTES:**

RTEMS has no way to distinguish between user and system time so this routine
returns the most meaningful information possible.

.. _getenv:

getenv - Get Environment Variables
----------------------------------
.. index:: getenv
.. index:: get environment variables

**CALLING SEQUENCE:**

.. code-block:: c

    char *getenv(
        const char *name
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``NULL``
   - when no match
 * - `pointer to value`
   - when successful

**DESCRIPTION:**

This service searches the set of environment variables for a string that
matches the specified ``name``.  If found, it returns the associated value.

**NOTES:**

The environment list consists of name value pairs that are of the form ``name =
value``.

.. _setenv:

setenv - Set Environment Variables
----------------------------------
.. index:: setenv
.. index:: set environment variables

**CALLING SEQUENCE:**

.. code-block:: c

    int setenv(
        const char *name,
        const char *value,
        int overwrite
    );

**STATUS CODES:**

Returns 0 if successful and -1 otherwise.

**DESCRIPTION:**

This service adds the variable ``name`` to the environment with ``value``.  If
``name`` is not already exist, then it is created.  If ``name`` exists and
``overwrite`` is zero, then the previous value is not overwritten.

**NOTES:**

NONE

.. _ctermid:

ctermid - Generate Terminal Pathname
------------------------------------
.. index:: ctermid
.. index:: generate terminal pathname

**CALLING SEQUENCE:**

.. code-block:: c

    char *ctermid(
        char *s
    );

**STATUS CODES:**

Returns a pointer to a string indicating the pathname for the controlling
terminal.

**DESCRIPTION:**

This service returns the name of the terminal device associated with this
process.  If ``s`` is NULL, then a pointer to a static buffer is returned.
Otherwise, ``s`` is assumed to have a buffer of sufficient size to contain the
name of the controlling terminal.

**NOTES:**

By default on RTEMS systems, the controlling terminal is :file:`/dev/console`.
Again this implementation is of limited meaning, but it provides true and
useful results which should be sufficient to ease porting applications from a
full POSIX implementation to the reduced profile supported by RTEMS.

.. _ttyname:

ttyname - Determine Terminal Device Name
----------------------------------------
.. index:: ttyname
.. index:: determine terminal device name

**CALLING SEQUENCE:**

.. code-block:: c

    char *ttyname(
        int fd
    );

**STATUS CODES:**

Pointer to a string containing the terminal device name or ``NULL`` is returned
on any error.

**DESCRIPTION:**

This service returns a pointer to the pathname of the terminal device that is
open on the file descriptor ``fd``.  If ``fd`` is not a valid descriptor for a
terminal device, then NULL is returned.

**NOTES:**

This routine uses a static buffer.

.. _ttyname_r:

ttyname_r - Reentrant Determine Terminal Device Name
----------------------------------------------------
.. index:: ttyname_r
.. index:: reentrant determine terminal device name

**CALLING SEQUENCE:**

.. code-block:: c

    int ttyname_r(
        int   fd,
        char *name,
        int   namesize
    );

**STATUS CODES:**

This routine returns -1 and sets ``errno`` as follows:

.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - If not a valid descriptor for a terminal device.
 * - ``EINVAL``
   - If ``name`` is ``NULL`` or ``namesize`` are insufficient.

**DESCRIPTION:**

This service the pathname of the terminal device that is open on the file
descriptor ``fd``.

**NOTES:**

NONE

.. _isatty:

isatty - Determine if File Descriptor is Terminal
-------------------------------------------------
.. index:: isatty
.. index:: determine if file descriptor is terminal

**CALLING SEQUENCE:**

.. code-block:: c

    int isatty(
        int fd
    );

**STATUS CODES:**

Returns 1 if ``fd`` is a terminal device and 0 otherwise.

**DESCRIPTION:**

This service returns 1 if ``fd`` is an open file descriptor connected to a
terminal and 0 otherwise.

**NOTES:**

.. _sysconf:

sysconf - Get Configurable System Variables
-------------------------------------------
.. index:: sysconf
.. index:: get configurable system variables

**CALLING SEQUENCE:**

.. code-block:: c

    long sysconf(
        int name
    );

**STATUS CODES:**

The value returned is the actual value of the system resource.  If the
requested configuration name is a feature flag, then 1 is returned if the
available and 0 if it is not.  On any other error condition, -1 is returned.

**DESCRIPTION:**

This service is the mechanism by which an application determines values for
system limits or options at runtime.

**NOTES:**

Much of the information that may be obtained via ``sysconf`` has equivalent
macros in ``unistd.h``.  However, those macros reflect conservative limits
which may have been altered by application configuration.
