.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2017 On-Line Applications Research Corporation (OAR)

Preface
=======

RTEMS supports a variety of POSIX and BSD features including some POSIX
methods that are now deemed obsolete and some methods for compatibility
with GNU/Linux and FreeBSD. There are multiple POSIX standard versions
as well as multiple efforts to tailor (e.g. profile) POSIX for embedded
environments. They range in size from less than 200 required capabilities
to the full POSIX standard which has over 1200 required capabilities. This
document reports on the alignment of RTEMS with various standard versions
and defined profiles.

RTEMS supports a number of POSIX process, user, and group oriented
routines in what is referred to as a "SUSP" (Single-User, Single
Process) manner.  RTEMS supports a single process, multithreaded
POSIX environment.  In a pure world, there would be no reason to even
include routines like ``getpid()`` when there can only be one process.
But providing routines like ``getpid()`` and making them work in
a sensible fashion for an embedded environment while not returning
``ENOSYS`` (for not implemented) makes it significantly easier to port
code from a UNIX environment without modifying it.

In general, adding missing methods is always an open project for a
volunteer. If considering addressing missing methods, please discuss
this on mailing list. Some are properly implemented in the Newlib
C Standard Library used by RTEMS. Others may require target architecture
specific implementations. Still others may be impossible to implement
without multiple processes or can only be implemented in a restricted
fashion.

Missing methods required by the C99 standard or FACE Technical
Standard Edition 3.0 General Purpose Profile are good candidates to add.
Proposals to add missing methods from the C11 standard should be reviewed
by RTEMS core developers to ensure the effort is well spent. There are
rumors that some optional methods that are not being widely implemented
will be removed in a future versino of the C Programming Language standard.

The next chapter in this document describes each of the standards
with which the RTEMS alignment is tracked.  Each subsequent chapter in
this document presents the alignment of RTEMS with a specific standard
version or defined profile.  Each section with a chapter details the
alignment of a specific header file relative to the chapter's standard
or profile.  The implementation status of the items required by the
standard are listed.
