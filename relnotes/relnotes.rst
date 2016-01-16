:orphan:



.. COMMENT: %**end of header

.. COMMENT: COPYRIGHT (c) 1989-2013.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

.. COMMENT: Master file

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

.. COMMENT: @set LANGUAGE C

.. COMMENT: the language is @value{LANGUAGE}

.. COMMENT: NOTE:  don't use underscore in the name

.. COMMENT: Title Page Stuff

.. COMMENT: I don't really like having a short title page.  -joel

.. COMMENT: @shorttitlepage RTEMS Release Notes

===================
RTEMS Release Notes
===================

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

RTEMS Release Notes
###################

.. COMMENT: COPYRIGHT (c) 1989-2014.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Introduction
############

This document describes the contents, installation
procedure, and current status of Release 4.10.99.0 of the RTEMS
executive.  An installation procedure is provided which
describes the steps necessary to load and configure the RTEMS
environment, including the GNU Development Environment and the
NEWLIB ANSI C Library, on a host computer.  The status of
the RTEMS environment is given, which includes supported
processors and target boards, versions of the GNU utilities
which were used by the RTEMS developers for this release,
support libraries status, features which are not implemented,
and any known existing problems.

This RTEMS release package contains the following general components:

- RTEMS C Executive

- RTEMS C Documentation Set

- RTEMS NEWLIB ANSI C Library

- Patches to GNU Development Tools

There are multiple mailing lists dedicated to RTEMS.
Each list may be subscribed to, archives view, etc. by visitinghttp://www.rtems.org/mailman/listinfo.

Supporting Tools
================

This section discusses the freely available tools and
libraries which are part of the RTEMS Development Environment.
None of the tools discussed in this section were developed by
the RTEMS project, although many do include submissions from the
project.  All of the tools and libraries required to build RTEMS
are freely available.  The home ftp site for most of the non-RTEMS
specific tools is either prep.ai.mit.edu (18.71.0.38) or
ftp.cygnus.com (140.174.1.3).

Specifically of interest to embedded systems developers
using the GNU tools is the crossgcc mailing list.  This is
a Majordomo style mailing list and may be subscribed to
by sending a message to crossgcc-request@cygnus.com with
the following line as the body:
.. code:: c

    subscribe rtems_user@your_email_goes_here.com

Please replace rtems_user@your_email_goes_here.com with your
email address.  The FAQ for crossgcc is in the /pub/embedded/crossgcc
directory on ftp.cygnus.com (205.180.83.42).

GNU Development Tools
---------------------

Numerous GNU tools are used in the RTEMS Development
Environment including C and Ada compilers, the GNU make program,
GNU m4, the GNU assembler and binary utilities (linker,
librarian, etc.), GNU tar, GNU zip, and the GNU debugger.  These
tools are distributed in source form and are all licensed under
the GNU Public License which allows for unrestricted
distribution under the condition that source code always be
available.  The Free Software Foundation is officially the
originator of most of the GNU tools although many individuals
have contributed to the GNU projects.  In keeping with the
spirit of the GPL,  most of the time the GNU tools are
distributed as source code without executables.  It is the
responsibility of the local site to install each tool.  Numerous
organizations and individuals supply executables for the GNU
tools.  All are required by the terms of the GPL to also make
the source code available to the end user.

The primary ftp site for the FSF GNU tools is
prep.ai.mit.edu (18.71.0.38) in the /pub/gnu directory.  These
tools are mirrored on numerous ftp sites.

ANSI C Libraries
----------------

This section discusses the following freely
distributable ANSI C Libraries:

- GNU C Library, and

- NEWLIB

No C Library is included in the standard RTEMS
distribution.  It is the responsibility of the user to obtain
and install a C Library separately.

GNU C Library
-------------

The GNU C Library is a robust and well-documented C
Library which is distributed under the terms of the Library GNU
Public License (LGPL).  This library was not designed for use in
real-time, embedded systems and the resource requirements of
some of the routines in this library are an obvious indication
of this.  Additionally, this library does not have support for
reentrancy in the sense that each task in a multitasking system
could safely invoke every routine in the library.  Finally, the
distribution terms of the LGPL are considered undesirable by
many embedded systems developers.  However, the GNU C Library is
very complete and is compliant with as many standards as
possible.  Because of this, it may be the only choice for many
developers.

NEWLIB C Library
----------------

The NEWLIB C Library was specifically designed for real-time embedded
systems.  It is a small, reasonably documented Library with support
for reentrancy.  This library is a collection of freely distributable
and public domain source code and is freely distributable with as few
restrictions as possible placed on the end user.

Documentation
=============

The RTEMS Documentation Set is provided online at http://www.rtems.org/onlinedocs.html
as reference information for all levels of RTEMS users.

The RTEMS documentation set is available in HTML, PostScript, PDF, and DVI.

.. COMMENT: COPYRIGHT (c) 1989-2011.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Installation Procedure
######################

Introduction
============

This chapter describes the process of installing and
configuring RTEMS and a cross-development environment based on
freely available tools and libraries.

RTEMS FTP Site Organization
===========================

RTEMS is distributed only via anonymous ftp.

This section will discuss how to navigate the RTEMS
ftp site and unarchive the files in the RTEMS and GNU package
distributions.  All example commands will be given in a shell
independent fashion unless otherwise noted.

Throughout the rest of this manual
<RTEMS_distribution> will be used as the parent of components
within the RTEMS distribution.  For persons using the ftp
distribution found on the primary ftp site for RTEMS,
<RTEMS_distribution> are found under this directoryftp://ftp.rtems.com/pub/rtems/.  HTTP access to the
ftp site is available via http://www.rtems.org/ftp/pub/rtems.

The archive files for RTEMS Release 4.10.99.0 are found
under the directory <RTEMS_distribution>.  This directory
contains the files which comprise this relase as well as any
patches which may be required for other tools.

The complete source code and documentation set for
the C language implementation of RTEMS is provided.

Unarchiving the RTEMS and GNU Components
========================================

Many of the components of the RTEMS release are
"tarred, zipped" files and have the .tar.gz or .tgz extension.
The GNU zip package is required to unarchives these files on the
RTEMS ftp site.  If this package is not installed, the source
can be found in the filesftp://ftp.gnu.org/pub/gnu/gzip/gzip-1.2.4.shar orftp://ftp.gnu.org/pub/gnu/gzip/gzip-1.2.4.tar.  It may be
restored using a command similar to the following:
.. code:: c

    tar xvf gzip-1.2.4.tar
    OR
    sh gzip-1.2.4.shar

This will create a subdirectory gzip-1.2.4 in the
current directory.  Please examine the files README and INSTALL
and follow the instructions provided there.

[Note: The GNU tools follow a standard packaging procedure
They will unarchive into a directory based on the package name and version
number.  For detailed instructions on compilation and
installation of the GNU tools, please refer to the instructions for
each GNU tool.]

Files which have been "tarred, zipped" (i.e.  .tar.gz
or .tgz extension) may be unarchived with a command similar to
one of the following:
.. code:: c

    gzcat <file>.tgz | tar xvof -
    OR
    gunzip -c <file>.tgz | tar xvof -
    OR
    gtar xzvf <file>.tgz

NOTE: gunzip -c is equivalent to gzcat, while gtar is GNU tar.

Given that the necessary utility programs are
installed, any of the above commands will extract the contents
of <file>.tar.gz into the current directory.  All of the RTEMS
components will be extracted into the subdirectory rtems-4.10.99.0.
To view the contents of a component without restoring any files,
use a command similar to the following:
.. code:: c

    gzcat <file>.tgz | tar tvf -

Installing a Cross-Development GNU Toolset
==========================================

This sections describes how to build and install the
FSF GNU tools for use as a cross-compilation system.  These
tools are used by the RTEMS developers.  Every effort has been
made to make these instructions accurate and complete.  However,
it is recommended that the individual doing the installation
read the appropriate installation notes for each of the tools in
the cross toolset.  This will help insure that there are no
special requirements for a particular host.

If the host and target processors are the same, then
it may be possible to use the host development tools.  An
example of this scenario is using a SPARC based workstation
to develop an RTEMS application for the SPARC processor.  Although
the native toolset is useable in this scenario, it is ultimately
more desirable to build a toolset specifically for the embedded environment.

Instructions for building a cross environment using the GNU
tools is provided in the crossgcc FAQ available from ftp.cygnus.com
in /pub/embedded/crossgcc.  It is recommended that the user following
these instructions.

After the cross development toolset has been built
and installed, it will be necessary to modify the environment of
each RTEMS application developer to reflect at least the path of
the newly installed cross development toolset.

The documentation for the FSF GNU and open source tools is
formatted using TeX.  The RTEMS developers use TeX to
format the manuals for their own use.  This document does not
contain instructions on the acquisition or installation of TeX
and supporting tools.

NOTE: For "UNIX" processors, the native compiler binary utilities
should be used.

Installing RTEMS
================

For instructions on building and installing RTEMS, please refer to
the file README.configure in the source distribution.

.. COMMENT: COPYRIGHT (c) 1989-2014.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Development Environment Status
##############################

This chapter will describe the current status of
release version 4.10.99.0 of the RTEMS Development Environment.

RTEMS Executive Status
======================

Release 4.10.99.0 of the RTEMS Executive contains support
for both the classic RTEMS API based on the RTEID specification as well
as support for POSIX threads and real-time extensions.

The classic RTEMS API has the following managers based upon the RTEID
specification:

- Task

- Initialization

- Clock

- Timer

- Interrupt

- Fatal Error

- Message

- Semaphore

- Event

- Signal

- Region

- Partition

- Dual Ported Memory

- I/O

- Multiprocessing

- Rate Monotonic

- User Extensions

RTEMS also has support for the following managers based upon the POSIX threads
and real-time extensions:

- Thread

- Clock

- Key

- Condition Variable

- Mutex

- Signal

- Scheduler

This release of the C implementation supports the
following processors and target boards:

- Motorola M68k family
  - - DY-4 DMV152, SVME153
  - - Motorola IDP
  - - Motorola MVME135, MVME136
  - - Motorola MVME147, MVME147S
  - - Motorola MVME162
  - - EFI 68000 and 68332
  - - Generic 68302
  - - Generic 68360 and 68360 in companion mode with 68040

- Intel i386 family
  - - Force CPU386
  - - Intel i386ex eval board
  - - PC-AT i386 and above (go32)

- PowerPC
  - - Papyrus (proprietary controller)

- SPARC
  - - ERC32 (space-hardened V7)

- MIPS
  - - P4000 with R4600 or R4650

Support for the NEWLIB Standard C Library is
provided with this release which may be used on any of the RTEMS
supported targets.  The BSPs only provide support for console
I/O only using this library.  Support for the reentrancy
capabilities of newlib is provided in the RTEMS distribution.

Development Environment Status
==============================

This section details the versions of the tools used
to develop and maintain RTEMS 4.10.99.0:

- Cross Tools
  - - gcc - 2.7.2.2 with rtems patch
  - - binutils - 2.7 with rtems patch
  - - zip - 1.2.4
  - - make - 3.74

Known Problems
==============

Problems which are known to exist at the time of
release are described in the following sections.  These are
provided as warnings to the user and where possible, workarounds
are provided until the problem is corrected.

Executive Problems
------------------

There are no known bugs in the executive itself.

Development Environment Problems
--------------------------------

There are no known major problems with the
development environment.

RTEMS Problem Reporting
-----------------------

The RTEMS Project uses the Bugzilla Problem Reporting and Tracking System.
Instructions for reporting a problem are located athttp://rtems.org/wiki/index.php/RTEMSBugReporting.

.. COMMENT: COPYRIGHT (c) 1989-2011.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

RTEMS PROBLEM REPORT
####################

.. code:: c

    Customer (Company) Name:
    Customer Address:
    Contact Name:
    Telephone Voice:                         Fax:
    Product:                                 Version:
    Target Processor:                        Target System:
    Host Computer System:
    Host Operating System:                   Version:
    Report Type:                    Customer Impact:
    [ ] Problem/Error               [ ] System is inoperable, cannot proceed
    [ ] Enhancement                 [ ] Must be corrected in the near future
    [ ] Inquiry Suggestion          [ ] Problem may be avoided until fixed
    [ ] Other______________         [ ] Problem is not time critical
    [ ] Minor problem

Please provide a detailed description of the
problem (Attachments including source code, example code,
makefiles, possible solutions, and any other information
describing the problem will be appreciated):

Command and Variable Index
##########################

There are currently no Command and Variable Index entries.

.. COMMENT: @printindex fn

Concept Index
#############

There are currently no Concept Index entries.

.. COMMENT: @printindex cp 
