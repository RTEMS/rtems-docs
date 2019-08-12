.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber
.. Copyright (C) 2015 Chris Johns <chrisj@rtems.org>
.. Copyright (C) 2012 Gedare Bloom

.. index:: bugs
.. index:: reporting bugs

Report Bugs
***********

The RTEMS Project uses a ticket system to deal with bugs, organize enhancement
requests, and manage small tasks and projects.  You can `submit a bug report
<https://devel.rtems.org/newticket>`_ to the RTEMS Project ticket system.
Before you do this, please read the following information.  Good bug reports
are more likely to get addressed quickly.  If you have patches not specifically
related to bugs or existing tickets, please have a look at the
:ref:`Contributing` guidelines.

Search for Existing Bugs
========================

You can `search for existing bugs <https://devel.rtems.org/query>`_ in the
RTEMS Project ticket system.  Please try to avoid duplicate bug reports and
search for an existing bug before you report a new bug.  If you are unsure,
please ask on the :r:list:`users` and we will help you sort it out.

Not RTEMS Bugs
==============

Some issues appear to be an RTEMS bug to you, but are actually the intended
behaviour or in the scope of other projects.

* Bugs in the assembler, the linker, or the C library (Newlib) are not RTEMS
  bugs.  These are separate projects, with separate mailing lists and different
  bug reporting procedures. The RTEMS Project is happy to work with you and
  those projects to resolve the problem but we must work with those projects.
  Bugs in those products must be addressed in the corresponding project.  Report
  `assembler, linker, and GDB bugs to sourceware.org <https://sourceware.org/bugzilla/enter_bug.cgi>`_,
  `compiler bugs to GCC <https://gcc.gnu.org/bugzilla/enter_bug.cgi>`_, and
  `Newlib bugs to the Newlib mailing list <https://sourceware.org/newlib/>`_.
  If the bug was fixed, then you can update the :ref:`RSB` to pick up the fix.

* Questions about the correctness or the expected behaviour of programming
  language constructs or calls to library routines that are not part of RTEMS
  belong somewhere else.

* The POSIX standard does *not* specify the default set of thread attributes.
  Thus, when passing a NULL for attributes to pthread_create(), the application
  is not guaranteed any particular thread behaviour.

* The defaults for all
  `RTEMS Application Configuration <https://docs.rtems.org/branches/master/c-user/configuring_a_system.html>`_
  parameters are intentionally small. Thus, it is common for RTEMS tasking and
  file related calls to return errors indicating out of resources until the
  configuration parameters are properly tuned for the application. For example,
  there are only three file descriptors available by default: stdin, stdout, and
  stderr. Any attempt to open a socket or file will fail unless more file
  descriptors are configured.

* When first developing a BSP, many users encounter an unexpected interrupt or
  exception immediately upon completion of RTEMS initialization. This occurs
  because interrupts are disabled during RTEMS initialization and are
  automatically initialized as part of switching to the first task. The
  interrupted user code will be in either _CPU_Context_switch() or
  _Thread_Handler().  This indicates that an interrupt source has not been
  properly initialized or masked.

* Some users encounter a random reset during BSP initialization. This usually
  indicates that the board has a watchdog timer that is not being properly
  serviced during the BSP initialization.

* Bugs in releases or snapshots of RTEMS not issued by the RTEMS Project.
  Report them to whoever provided you with the release.

Good Bug Reports
================

Please open the page to `submit a bug <https://devel.rtems.org/newticket>`_ to
the RTEMS Project ticket system and follow the guidelines below to write a good
bug report.

* Provide a useful single line **Summary**.

* Use `WikiFormatting <https://devel.rtems.org/wiki/WikiFormatting>`_ to
  structure the information you provide.  It does help the readability of the
  information you provide.

* Add a description of the expected behaviour.  The expected behaviour may be
  obvious to you, but maybe not to someone else reading the bug report.

* Add a description of the actual undesired behaviour.

* Name the :ref:`target hardware <Hardware>` (processor architecture, chip family
  or model, and :ref:`BSP <BSPs>`) in the description.

* Add the toolchain version used (GCC, Binutils, Newlib) to the description.
  Custom toolchain builds are discouraged.  To avoid problems caused by custom
  builds of the toolchain, please build your toolchain with the :ref:`RSB`.  If
  you use a custom build of the toolchain, then try to reproduce the bug first
  using a toolchain built by the RSB.

* Provide the configuration options used to build the RTEMS BSP in the
  description.  This helps to reproduce the issue.

* Make the bug reproducible by others.  Write a self-contained piece of source
  code which can be compiled and reproduces the bug.  Avoid adding assembly
  files (\*.s) produced by the compiler, or any binary files, such as object
  files, executables, core files, or precompiled header files.  If it is
  difficult or time consuming to reproduce the bug, then it may not get the
  attention it deserves from others.  Developing and debugging real-time
  embedded systems can be difficult.  Exercise caution in reporting an error
  that occurs only some of the times a certain program is executed, such that
  retrying a sufficient number of times results in a successful compilation;
  this is often a symptom of a hardware problem or application issue, not of a
  RTEMS bug (sorry). We do recognise that sometimes a timing bug will exist in
  RTEMS, but we want you to exercise due diligence before pointing fingers.

* Only when your bug report requires multiple source files to be reproduced
  should you attach an archive. Otherwise, the uploaded individual source file
  or diff should contain the minimal source code needed to reproduce the bug.
  In any case, make sure the above are included in the body of your bug report
  as plain text, even if needlessly duplicated as part of an archive.

* Please try to reproduce the bug on the current Git master.  If it is not
  reproducible on the Git master, you should figure out if the bug was already
  fixed.  You can search the existing bugs once again, ask on the
  :r:list:`users`, or do a Git bisect to find a commit which fixed the bug.

* Include only information relevant to the bug.

* Write separate bug reports for different bugs.

* Select a **Type** for the ticket.

  * Use ``defect`` for a bug.

  * Use ``enhancement`` for a feature request in the software or an addition to
    the documentation.

  * Note ``infra`` is used to report issues with the RTEMS servers at OSUOSL.

* Select a **Version** for the ticket.  This should be the first RTEMS version
  which is affected by this bug.  If this is the current Git master branch use
  the version of the next release.  Please provide the exact version of RTEMS
  in the description.  If you use an RTEMS release, then the release number.
  If you use a Git clone, then the commit hash.  The commit hash should be
  present in an RTEMS Project repository.  Commit hashes of private branches
  are not interesting.

* Select a **Component** for the ticket.  Use ``unspecified`` if you are unsure.

* Select a **Severity** for the ticket.

* The fields **Milestone** and **Priority** will be most likely set by an RTEMS
  maintainer.

* You can relate your new bug to existing bugs through the **Blocked by** and
  **Blocking** fields.

* If you have any external files, such as screenshots or examples, please
  *attach* these as files to the ticket.  *Do not use external hosting* because
  if you do use external hosting, then our historical record is broken when
  those files are no longer available.

* Some fields should only be set by the maintainers, as it is not always clear
  what they should be set to.  Feel free to make your own choices.

When you have checked that your report meets the criteria for a good bug
report, please click on the ``Create ticket`` button to submit it to the RTEMS
Project ticket system.

If you fail to supply enough information for a bug report to be reproduced,
someone will probably ask you to post additional information. In this case,
please post the additional information and not just to the person who requested
it, unless explicitly told so.

Nobody Fixes my Bug
===================

Sometimes, you may notice that after some time your bug report gets no
attention and the bug is not magically fixed.  This may have several reasons

* the bug report is incomplete or confusing,

* the target hardware is not available to others,

* the bug is not reproducible on the Git master,

* the bug is not reproducible at all,

* the RTEMS version is quite old and no longer used by RTEMS maintainers, or

* fixing the bug has a low priority for others.

Please note that you do not have a service contract with the RTEMS Project.
The RTEMS Project is run by volunteers and persons who take care about how
RTEMS performs in their application domain.  If your bug does not affect the
interest of someone else, then you should try to fix the bug on your own, see
the :ref:`Contributing` guidelines.  To change the priorities of others with
respect to your bug, you may refer to the :ref:`SupportCommercial`.
