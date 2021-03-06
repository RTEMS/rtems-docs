.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: On-Line Applications Research Corporation (OAR).
 | **COPYRIGHT (c) 20188.**
.. **RTEMS Foundation, The RTEMS Documentation Project**

Standards 
=========

This chapter describes each of the standards which RTEMS tracks
API alignment with. As a general rules, these standards are related
to the POSIX or C programming language standards. Many are the result
of domain specific efforts to define subsets or profiles or the full
POSIX standard which are suitable for a specific domain. Each 
API set is considered a "profile" against which the full capability
set of RTEMS is evaluated.

The RTEMS Complete Profile is the complete set of POSIX, BSD, and
C programming language methods supported by RTEMS. This profile is
independent of any standard and represents a union of multiple
standards. For example, RTEMS supports BSD derived methods that
are not in POSIX.

The IEEE Standard 1003.1 is the POSIX standard which is maintained by The
Open Group.  Specifically, IEEE Standard 1003.1-2003 is the 2003 edition
of the POSIX standard which is referred to by The Open Group as Issue 6.
IEEE Standard 1003.1-2008 is the 2003 Edition of the standard with two
Technical Corrigenda applied. It does not have an issue number associated
with it.  IEEE Standard 1003.1-2017 is also known as Issue 7. Each edition
of the POSIX standard tends to add some methods, deprecate some methods,
and obsolete (e.g. remove) other methods. 

API differences between Issue 5 and Issue 6 are documented at
https://pubs.opengroup.org/onlinepubs/009695399/xrat/xsh_chap01.html.
There is not a summary for the changes between Issue 6 as published
and what was released as 1003.1-2008.  However, there is a summary
of API changes from Issue 6 to Issue 7 (POSIX 1003.1-2017) at
https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_xsh_chap01.html.

PSE51 through PSE54 are Open Group defined profiles of the 2003 edition
of the POSIX standard. These profiles are:

* Profile 54 - Multipurpose

  * 1003.1-2003 Base Multi-process, Threads and File System

* Profile 53 - Dedicated

  * Multi-process, Threads and File System

* Profile 52 - Controller

  * Single Process, Threads, and File System

* Profile 51 - Minimal

  * Single Process, Threads, with No File System

The C99 Programming Language standard defines the Standard C Library. This
library is largely included by reference in the POSIX standard. 

The C11 Programming Language standard defines also defines an
updated version of the Standard C Library. It deletes a few methods
from the C99 version but adds many methods. A large portion of these
methods are optional and not commonly implemented.

The Open Group FACE Consortium (https://www.opengroup.org/face)
has defined four POSIX profiles targetting the avionics application
domain. The FACE Technical Standard has been through multiple revisions
and the POSIX API profiles are identical in Editions 1.0, 2.0, 2.1,
and 2.1.1. In these editions, the profiles are as follows:

* Security - 163 APIs, single process, no FILE *

* Safety Basic - 246 APIs, single process, some FILE *

* Safety Extended - 335 APIs, multi-process, more FILE *

* General Purpose - 812 APIs, multi-process, much more

FACE Technical Standard, Edition 3.0 adds the requirement for an
operating system to support ``clock_nanosleep()`` in all profiles and
defines one additional subcommand for the ``posix_devctl()`` methods.

FACE Technical Standard, Edition 3.1 has a number of minor changes
to the profiles. Most of these were to improve alignment with the 
Software Communications Architecture (SCA) profiles. Additionally,
some inconsistencies in the profiles were noticed and addressed while
doing the alignment review.

RTEMS provides all of the methods required by the FACE Safety BASE profile
and all of the methods in the Safety Extended profile which do not require
multiple processes. Similarly, RTEMS provides most of the methods in the
General Purpose profile which do not require multiple processes.

The SCA specification targets the requirements for software-defined
radios. This specification was originally developed in support of the
Joint Tactical Radio System (JTRS) program in conjunction with the Object
Management Group (OMG). This standard is now maintained by the Wireless
Innovation Forum with support from the U.S. Navy Joint Tactical Network
Center (JTNC). Some URLs of interest:

* SCA at Wireless Innovation Forum - http://www.wirelessinnovation.org/sca-based-standards-library

* JTRS - https://en.wikipedia.org/wiki/Joint_Tactical_Radio_System

* JTNC - http://www.public.navy.mil/jtnc/Pages/home.aspx

The SCA standard is hosted at the Wireless Innovation Forum with JTNC
hosting supplemental information.

RTEMS includes all methods required by the SCA POSIX profiles.
