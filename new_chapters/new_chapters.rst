:orphan:



.. COMMENT: %**end of header

.. COMMENT: COPYRIGHT (c) 1989-2013.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: Master file for the C User's Guide

.. COMMENT: Joel's Questions

.. COMMENT: 1.  Why does paragraphindent only impact makeinfo?

.. COMMENT: 2.  Why does paragraphindent show up in HTML?

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: The following determines which set of the tables and figures we will use.

.. COMMENT: We default to ASCII but if available TeX or HTML versions will

.. COMMENT: be used instead.

.. COMMENT: @clear use-html

.. COMMENT: @clear use-tex

.. COMMENT: The following variable says to use texinfo or html for the two column

.. COMMENT: texinfo tables.  For somethings the format does not look good in html.

.. COMMENT: With our adjustment to the left column in TeX, it nearly always looks

.. COMMENT: good printed.

.. COMMENT: Custom whitespace adjustments.  We could fiddle a bit more.

.. COMMENT: variable substitution info:

.. COMMENT: Note: At the moment we do not document the Ada interface but by building

.. COMMENT: in the infrastructure Florist support should be simple to add.

.. COMMENT: the language is @value{LANGUAGE}

.. COMMENT: NOTE:  don't use underscore in the name

.. COMMENT: Title Page Stuff

.. COMMENT: I don't really like having a short title page.  -joel

.. COMMENT: @shorttitlepage New Chapters

============
New Chapters
============

.. COMMENT: COPYRIGHT (c) 1988-2015.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: The following puts a space somewhere on an otherwise empty page so we

.. COMMENT: can force the copyright description onto a left hand page.

COPYRIGHT © 1988 - 2015.

On-Line Applications Research Corporation (OAR).

The authors have used their best efforts in preparing
this material.  These efforts include the development, research,
and testing of the theories and programs to determine their
effectiveness.  No warranty of any kind, expressed or implied,
with regard to the software or the material contained in this
document is provided.  No liability arising out of the
application or use of any product described in this document is
assumed.  The authors reserve the right to revise this material
and to make changes from time to time in the content hereof
without obligation to notify anyone of such revision or changes.

The RTEMS Project is hosted at http://www.rtems.org.  Any
inquiries concerning RTEMS, its related support components, or its
documentation should be directed to the Community Project hosted athttp://www.rtems.org.

Any inquiries for commercial services including training, support, custom
development, application development assistance should be directed tohttp://www.rtems.com.

.. COMMENT: This prevents a black box from being printed on "overflow" lines.

.. COMMENT: The alternative is to rework a sentence to avoid this problem.

RTEMS POSIX API User’s Guide
############################

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Error Reporting Support
#######################

Introduction
============

These error reporting facilities are an RTEMS support
component that provide convenient facilities for handling
error conditions in an RTEMS application.
of each task using a period.  The services provided by the error
reporting support component are:

- ``rtems_error`` - Report an Error

- ``rtems_panic`` - Report an Error and Panic

- ``rtems_status_text`` - ASCII Version of RTEMS Status

Background
==========

Error Handling in an Embedded System
------------------------------------

Error handling in an embedded system is a difficult problem.  If the error
is severe, then the only recourse is to shut the system down in a safe
manner.  Other errors can be detected and compensated for.  The
error reporting routines in this support component – ``rtems_error``
and ``rtems_panic`` assume that if the error is severe enough,
then the system should be shutdown.  If a simple shutdown with
some basic diagnostic information is not sufficient, then
these routines should not be used in that particular system.  In this case,
use the ``rtems_status_text`` routine to construct an application
specific error reporting routine.

Operations
==========

Reporting an Error
------------------

The ``rtems_error`` and ``rtems_panic`` routines
can be used to print some diagnostic information and
shut the system down.  The ``rtems_error`` routine
is invoked with a user specified error level indicator.
This error indicator is used to determine if the system
should be shutdown after reporting this error.

Routines
========

This section details the error reporting support compenent’s routine.
A subsection is dedicated to each of this manager’s routines
and describes the calling sequence, related constants, usage,
and status codes.

rtems_status_text - ASCII Version of RTEMS Status
-------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    const char \*rtems_status_text(
    rtems_status_code status
    );

**STATUS CODES:**

Returns a pointer to a constant string that describes the given
RTEMS status code.

**DESCRIPTION:**

This routine returns a pointer to a string that describes
the RTEMS status code specified by ``status``.

**NOTES:**

NONE

rtems_error - Report an Error
-----------------------------

**CALLING SEQUENCE:**

.. code:: c

    int rtems_error(
    int         error_code,
    const char \*printf_format,
    ...
    );

**STATUS CODES:**

Returns the number of characters written.

**DESCRIPTION:**

This routine prints the requested information as specified by the``printf_format`` parameter and the zero or more optional arguments
following that parameter.  The ``error_code`` parameter is an error
number with either ``RTEMS_ERROR_PANIC`` or ``RTEMS_ERROR_ABORT``
bitwise or’ed with it.  If the ``RTEMS_ERROR_PANIC`` bit is set, then
then the system is system is shutdown via a call to ``_exit``.
If the ``RTEMS_ERROR_ABORT`` bit is set, then
then the system is system is shutdown via a call to ``abort``.

**NOTES:**

NONE

rtems_panic - Report an Error and Panic
---------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    int rtems_panic(
    const char \*printf_format,
    ...
    );

**STATUS CODES:**

Returns the number of characters written.

**DESCRIPTION:**

This routine is a wrapper for the ``rtems_error`` routine with
an implied error level of ``RTEMS_ERROR_PANIC``.  See``rtems_error`` for more information.

**NOTES:**

NONE

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Monitor Task
############

Introduction
============

The monitor task is a simple interactive shell that allows the user to
make inquries about he state of various system objects.  The routines
provided by the monitor task manager are:

- ``rtems_monitor_init`` - Initialize the Monitor Task

- ``rtems_monitor_wakeup`` - Wakeup the Monitor Task

Background
==========

There is no background information.

Operations
==========

Initializing the Monitor
------------------------

The monitor is initialized by calling ``rtems_monitor_init``.  When
initialized, the monitor is created as an independent task.  An example
of initializing the monitor is shown below:
.. code:: c

    #include <rtems/monitor.h>
    ...
    rtems_monitor_init(0);

The "0" parameter to the ``rtems_monitor_init`` routine
causes the monitor to immediately enter command mode.
This parameter is a bitfield.  If the monitor is to suspend
itself on startup, then the ``RTEMS_MONITOR_SUSPEND`` bit
should be set.

Routines
========

This section details the monitor task manager’s routines.
A subsection is dedicated to each of this manager’s routines
and describes the calling sequence, related constants, usage,
and status codes.

rtems_monitor_init - Initialize the Monitor Task
------------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    void rtems_monitor_init(
    unsigned32 monitor_flags
    );

**STATUS CODES: NONE**

**DESCRIPTION:**

This routine initializes the RTEMS monitor task.  The``monitor_flags`` parameter indicates how the server
task is to start.  This parameter is a bitfield and
has the following constants associated with it:

- *RTEMS_MONITOR_SUSPEND* - suspend monitor on startup

- *RTEMS_MONITOR_GLOBAL* - monitor should be global

If the ``RTEMS_MONITOR_SUSPEND`` bit is set, then the
monitor task will suspend itself after it is initialized.
A subsequent call to ``rtems_monitor_wakeup`` will be required
to activate it.

**NOTES:**

The monitor task is created with priority 1.  If there are
application tasks at priority 1, then there may be times
when the monitor task is not executing.

rtems_monitor_wakeup - Wakeup the Monitor Task
----------------------------------------------

**CALLING SEQUENCE:**

.. code:: c

    void rtems_monitor_wakeup( void );

**STATUS CODES: NONE**

**DESCRIPTION:**

This routine is used to activate the monitor task if it is suspended.

**NOTES:**

NONE

Monitor Interactive Commands
============================

The following commands are supported by the monitor task:

- ``help`` - Obtain Help

- ``pause`` - Pause Monitor for a Specified Number of Ticks

- ``exit`` - Invoke a Fatal RTEMS Error

- ``symbol`` - Show Entries from Symbol Table

- ``continue`` - Put Monitor to Sleep Waiting for Explicit Wakeup

- ``config`` - Show System Configuration

- ``itask`` - List Init Tasks

- ``mpci`` - List MPCI Config

- ``task`` - Show Task Information

- ``queue`` - Show Message Queue Information

- ``extension`` - User Extensions

- ``driver`` - Show Information About Named Drivers

- ``dname`` - Show Information About Named Drivers

- ``object`` - Generic Object Information

- ``node`` - Specify Default Node for Commands That Take IDs

help - Obtain Help
------------------

The ``help`` command prints out the list of commands.  If invoked
with a command name as the first argument, detailed help information
on that command is printed.

pause - Pause Monitor for a Specified Number of Ticks
-----------------------------------------------------

The ``pause`` command cause the monitor task to suspend itself
for the specified number of ticks.  If this command is invoked with
no arguments, then the task is suspended for 1 clock tick.

exit - Invoke a Fatal RTEMS Error
---------------------------------

The ``exit`` command invokes ``rtems_error_occurred`` directive
with the specified error code.  If this command is invoked with
no arguments, then the ``rtems_error_occurred`` directive is
invoked with an arbitrary error code.

symbol - Show Entries from Symbol Table
---------------------------------------

The ``symbol`` command lists the specified entries in the symbol table.
If this command is invoked with no arguments, then all the
symbols in the symbol table are printed.

continue - Put Monitor to Sleep Waiting for Explicit Wakeup
-----------------------------------------------------------

The ``continue`` command suspends the monitor task with no timeout.

config - Show System Configuration
----------------------------------

The ``config`` command prints the system configuration.

itask - List Init Tasks
-----------------------

The ``itask`` command lists the tasks in the initialization tasks table.

mpci - List MPCI Config
-----------------------

The ``mpci`` command shows the MPCI configuration information

task - Show Task Information
----------------------------

The ``task`` command prints out information about one or more tasks in
the system.  If invoked with no arguments, then
information on all the tasks in the system is printed.

queue - Show Message Queue Information
--------------------------------------

The ``queue`` command prints out information about one or more
message queues in the system.  If invoked with no arguments, then
information on all the message queues in the system is printed.

extension - User Extensions
---------------------------

The ``extension`` command prints out information about the user
extensions.

driver - Show Information About Named Drivers
---------------------------------------------

The ``driver`` command prints information about the device driver table.

dname - Show Information About Named Drivers
--------------------------------------------

The ``dname`` command prints information about the named device drivers.

object - Generic Object Information
-----------------------------------

The ``object`` command prints information about RTEMS objects.

node - Specify Default Node for Commands That Take IDs
------------------------------------------------------

The ``node`` command sets the default node for commands that look
at object ID ranges.

Command and Variable Index
##########################

There are currently no Command and Variable Index entries.

.. COMMENT: @printindex fn

Concept Index
#############

There are currently no Concept Index entries.

.. COMMENT: @printindex cp 
