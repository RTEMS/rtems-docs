.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. COMMENT: All rights reserved.

Preface
*******

Real-time embedded systems vary widely based upon their operational and
maintenance requirements. Some of these systems provide ways for the user or
developer to interact with them.  This interaction could be used for
operational, diagnostic, or configuration purposes.  The capabilities described
in this manual are those provided with RTEMS to provide a command line
interface for user access.  Some of these commands will be familiar as standard
POSIX utilities while others are RTEMS specific or helpful in debugging and
analyzing an embedded system. As a simple example of the powerful and very
familiar capabilities that the RTEMS Shell provides to an application, consider
the following example which hints at some of the capabilities available:

.. code-block:: shell

    Welcome to rtems-4.10.99.0(SPARC/w/FPU/sis)
    COPYRIGHT (c) 1989-2011.
    On-Line Applications Research Corporation (OAR).
    Login into RTEMS
    login: rtems
    Password:
    RTEMS SHELL (Ver.1.0-FRC):/dev/console. Feb 28 2008. 'help' to list commands.
    SHLL [/] $ cat /etc/passwd
    root:*:0:0:root::/:/bin/sh
    rtems:*:1:1:RTEMS Application::/:/bin/sh
    tty:!:2:2:tty owner::/:/bin/false
    SHLL [/] $ ls /dev
    -rwxr-xr-x   1  rtems   root           0 Jan 01 00:00 console
    -rwxr-xr-x   1   root   root           0 Jan 01 00:00 console_b
    2 files 0 bytes occupied
    SHLL [/] $ stackuse
    Stack usage by thread
    ID      NAME    LOW          HIGH     CURRENT     AVAILABLE     USED
    0x09010001  IDLE 0x023d89a0 - 0x023d99af 0x023d9760      4096        608
    0x0a010001  UI1  0x023d9f30 - 0x023daf3f 0x023dad18      4096       1804
    0x0a010002  SHLL 0x023db4c0 - 0x023df4cf 0x023de9d0     16384       6204
    0xffffffff  INTR 0x023d2760 - 0x023d375f 0x00000000      4080        316
    SHLL [/] $ mount -L
    File systems: msdos
    SHLL [/] $

In the above example, the user *rtems* logs into a SPARC based RTEMS system.
The first command is ``cat /etc/passwd``.  This simple command lets us know
that this application is running the In Memory File System (IMFS) and that the
infrastructure has provided dummy entries for */etc/passwd* and a few other
files.  The contents of */etc/passwd* let us know that the user could have
logged in as ``root``.  In fact, the ``root`` user has more permissions than
``rtems`` who is not allowed to write into the filesystem.

The second command is ``ls /dev`` which lets us know that RTEMS has POSIX-style
device nodes which can be accesses through standard I/O function calls.

The third command executed is the RTEMS specific ``stackuse`` which gives a
report on the stack usage of each thread in the system.  Since stack overflows
are a common error in deeply embedded systems, this is a surprising simple, yet
powerful debugging aid.

Finally, the last command, ``mount -L`` hints that RTEMS supports a variety of
mountable filesystems. With support for MS-DOS FAT on IDE/ATA and Flash devices
as well as network-based filesystens such as NFS and TFTP, the standard free
RTEMS provides a robuse infrastructure for embedded applications.

This manual describes the RTEMS Shell and its command set.  In our terminology,
the Shell is just a loop reading user input and turning that input into
commands with argument.  The Shell provided with RTEMS is a simple command
reading loop with limited scripting capabilities.  It can be connected to via a
standard serial port or connected to the RTEMS ``telnetd`` server for use across
a network.

Each command in the command set is implemented as a single subroutine which has
a *main-style* prototype.  The commands interpret their arguments and operate
upon stdin, stdout, and stderr by default.  This allows each command to be
invoked independent of the shell.

The described separation of shell from commands from communications mechanism
was an important design goal.  At one level, the RTEMS Shell is a complete
shell environment providing access to multiple POSIX compliant filesystems and
TCP/IP stack.  The subset of capabilities available is easy to configure and
the standard Shell can be logged into from either a serial port or via telnet.
But at another level, the Shell is a large set of components which can be
integrated into the user's developed command interpreter.  In either case, it
is trivial to add custom commands to the command set available.

Acknowledgements
================

.. COMMENT: The RTEMS Project has been granted permission from The Open Group
.. COMMENT: IEEE to excerpt and use portions of the POSIX standards documents
.. COMMENT: in the RTEMS POSIX API User's Guide and RTEMS Shell User's Guide.
.. COMMENT: We have to include a specific acknowledgement paragraph in these
.. COMMENT: documents (e.g. preface or copyright page) and another slightly
.. COMMENT: different paragraph for each manual page that excerpts and uses
.. COMMENT: text from the standards.
.. COMMENT: This file should help ensure that the paragraphs are consistent
.. COMMENT: and not duplicated

The Institute of Electrical and Electronics Engineers, Inc and The Open Group,
have given us permission to reprint portions of their documentation.

.. pull-quote::

    Portions of this text are reprinted and reproduced in electronic form from
    IEEE Std 1003.1, 2004 Edition, Standard for Information Technology
    Operating System Interface (POSIX), The Open Group Base Specifications
    Issue 6, Copyright (c) 2001-2004 by the Institute of Electrical and
    Electronics Engineers, Inc and The Open Group. In the event of any
    discrepancy between this version and the original IEEE and The Open Group
    Standard, the original IEEE and The Open Group Standard is the referee
    document. The original Standard can be obtained online at
    http://www.opengroup.org/unix/online.html.  This notice shall appear on any
    product containing this material.
