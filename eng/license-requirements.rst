.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

.. _LicensingRequirements:

Licensing Requirements
**********************

All artifacts shall adhere to RTEMS Project licensing
requirements. Currently, the preferred licenses are:

* "Two Clause BSD" (BSD-2-Clause) for source code, and
* CC-BY-SA-4.0 license for documentation

Historically, RTEMS has been licensed under the GPL v2 with linking
exception (https://www.rtems.org/license). It is preferred that new
submissions be under one of the two preferred licenses. If you have
previously submitted code to RTEMS under a historical license, please
grant the project permission to relicense. See
https://devel.rtems.org/ticket/3053 for details.

For example templates for what to include in source code and 
documentation, see :ref:`FileHeaderCopyright`.


Rationale
---------
.. COMMENT: Thanks to Gedare Bloom for his 2013 blog which
.. COMMENT: discussed the rationale for RTEMS License section.
.. COMMENT: http://gedare-csphd.blogspot.com/2013/05/software-licenses-with-rtems.html

RTEMS is intended for use in real-time embedded systems in which the
application is statically linked with the operating system and all
support libraries. Given this use case, the RTEMS development team
evaluated a variety of licenses with with the goal of promoting use
while protecting both users and the developers.

Using the GNU General Public License Version 2 (GPLv2) unmodified
was considered but discarded because the GPL can only be linked statically
with other GPL code. Put simply, linking your application code statically
with GPL code would cause your code to become GPL code. This would force
both licensing and redistribution requirements onto RTEMS users. This
was completely unacceptable. 

The GNU Lesser General Public License Version 2 (LGPLv2) was also 
considered and deemed to not be a suitable license for RTEMS. This is
because it either requires use of a shared library that can be re-linked,
or release of the linked (application) code. This would require an
RTEMS-based embedded system to provide a "relinking kit." Again, this 
license would force an unacceptable requirement on RTEMS users and deemed
unacceptable.

Newer versions of the GPL (i.e. version 3) are completely unsuitable
for embedded systems due to the additions which add further restrictions
on end user applications. 

The historical RTEMS `License <https://www.rtems.org/license>`_ is a
modified version of the GPL version 2 that includes an exception to permit
including headers and linking against RTEMS object files statically. This
was based on the license used by GCC language runtime libraries at that
time. This license allows the static linking of RTEMS with applications
without forcing obligations and restrictions on users.

A problem for RTEMS is there are no copyleft licenses that are compatible
with the deployment model of RTEMS. Thus, RTEMS Project has to reject any
code that uses the GPL or LGPL, even though RTEMS has historically appeared
to use the GPL itself -- but with the exception for static linking, and also
because an upstream GPL version 2 project could at any time switch to
GPL version 3 and become totally unusable. In practice, RTEMS can only
accept original code contributed under the RTEMS License and code that
has a permissive license.

As stated above, the RTEMS Project has defined its preferred licenses.
These allow generation of documentation and software from specification
as well as allow end users to statically link with RTEMS and not incur
obligations.

In some cases, RTEMS includes software from third-party projects. In those
cases, the license is carefully evaluated to meet the project licensing
goals.  The RTEMS Project can only include software under licenses which follow
these guidelines:

* 2- and 3-clause BSD, MIT, and other OSI-approved non-copyleft licenses
  that permit statically linking with the code of different licenses
  are acceptable.

* The historical RTEMS `License <https://www.rtems.org/license>`_ is 
  acceptable for software already in the tree. This software is being
  relicensed to BSD-2-Clause, rewritten, or removed.

* GPL licensed code is NOT acceptable, neither is LGPL.

* Software which is dual-licensed in a manner which prevents free use
  in commercial applications is not acceptable.

* Advertising obligations are not acceptable.

* Some license restrictions may be permissible. These will be considered
  on a case-by-case basis. See below for a list of such restrictions.

In practice, these guidelines are not hard to follow. Critically,
they protect the freedom of the RTEMS source code and that of end users
to select the license and distribution terms they prefer for their
RTEMS-based application.

License restrictions
--------------------

* Apache License 2.0 in section 4 (b) requires modified files to carry
  prominent notice about performed modification. In case you modify such
  file and the notice is not there yet you are required to put notice
  below at the top of the modified file. If the notice is already
  there you don't need to add it second time.
  The notice should look:

  .. code-block:: c

     /*
      * The file was modified by RTEMS contributors.
      */

 .. warning:: Do not import any project or files covered by the Apache
              License 2.0 into the RTEMS project source tree without
              discussing first with developers on the mailing list!
              Handling of Apache License 2.0 projects is a bit
              sensitive manner and RTEMS project is not prepared to
              handle one kind of those projects yet. E.g. the projects
              with NOTICE file present in the source tree.
