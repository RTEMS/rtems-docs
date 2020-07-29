.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 Contemporary Software
.. Copyright (C) 2020 Chris Johns

.. _Release_Process:

Release Process
***************

The release process creates an RTEMS release. The process has a number of
stages that happen before a release can be made, during the creation of the
release and after the release has been made.

Releases
========

RTEMS is released as a collection of ready to use source code and built
documentation. Releases are publicly available on the RTEMS servers under
https://ftp.rtems.org/pub/rtems/releases.

Releases are group under the major version number as a collection of
directories consisting of the version number. This is termed a release
series. A release may also contain release snapshots.

All releases must have a three digit version number and this can be optionally
followed by a dash character (``-``) and an identifier, e.g. ``5.1.0-acme-1``.

The RTEMS Project reserves releases with only the three digit version number,
e.g. ``5.1.0``. This identifies an RTEMS Project release.

Release Layout
--------------

* All released source archives are XZ compressed tar files.

* Top level contains:

:file:`README.txt`:
    A set of brief release instructions.

:file:`contrib`:
    Contributed sources. For example the release scripts used to create the
    release.

:file:`docs`:
    Compressed documentation build in HTML, Single page HTML and PDF
    formats. Provide compressed files for each document and a single archive
    of all the documentation. Provide an SHA512 check sum file.

:file:`rtems-<VERSION>-release-notes.pdf`:
    RTEMS Release notes document the changes in a release. This is a capture
    of the Trac report for the release's milestone in PDF format.

:file:`sha512sum.txt`:
    SHA512 checksum of all files in this directory.

:file:`sources`:
    All source code referenced by the release.

Release Version Numbering
-------------------------

The release numbering scheme changed with RTEMS 5.

The master branch has the version N.0.0 with N being the next major release
number. The release branch in a repository will be just the major number.

The first release of this series will have the version number N.1.0. The first
bugfix release (minor release) of this series will have the version number
N.2.0.

The release branch will have the version number N.M.1 with M being the last
minor release of this series. Tools will use N as the version number and must
be compatible with all releases and the release branch of the N series.

Examples:

 - ``5.0.0`` is the version number of the development master for the 5 series

 - ``5.1.0`` is the first release of the 5 series

 - ``5.1.1`` is the version number of the 5 series release branch right after
   the 5.1.0 release until 5.2.0 is released

 - ``5.2.0`` is the first bugfix release of the 5 series

 - ``5.2.1`` is the version number of the 5 series release branch right after
   the 5.2.0 release until 5.3.0 is released

 - ``6.0.0`` is the version number of the development master for the 6 series

Release Scripts
----------------

* The release scripts are held in the top level repository
  https://git.rtems.org/rtems-release.git.

* The scripts are written for FreeBSD and can run on FreeBSD 10 through
  FreeBSD 12. No other host operating system is supported for the release
  scripts. Updates are welcome if the changes do not affect the operation on
  FreeBSD.

* A Python ``virutalenv`` environment is required for a working Sphinx
  documentation building environment. Follow the procedure in the
  ``rtems-docs.git`` top level ``README`` file.

* Building a standard release requires you provide the release major number
  and the release's remaining version string including any additional
  identifiers:

  .. code-block:: none

     ./rtems-release 5 1.0

  To create a release snapshot:

  .. code-block:: none

    ./rtems-release 5 0.0-m2003

* A 3rd option of a release URL can be provided to create a test or deployable
  release. The URL is a base path the RSB uses to download the release source
  files from:

  .. code-block:: none

    ./rtems-release \
        -u https://ftp.rtems.org/pub/rtems/people/chrisj/releases \
        5 0.0-m2003-2

* Building the release notes requires the Web Toolkit HTML to PDF converter be
  installed. The FreeBSD package is ``wkhtmltopdf``.

Release Snapshots
-----------------

* Release snapshots are only created for the current development version of
  RTEMS. For example RTEMS 5 snapshot path is :file:`5/5.0.0/5.0.0-m2003`.

* Release snapshots are based on the development sources and may be unstable or
  not suitable for use in production.

* A release snapshot is created each month and is named as
  ``<major>/<version>/<version>-<YYMM>`` where ``YY`` is the last two digits of
  the current year and ``MM`` is the month as a two digit number.

* In the lead up to a release more than one snapshot can be created by
  appending ``-<count>`` to the snapshot version string where ``<count>`` is
  incremented starting from ``1``. The first snapshot without a count is
  considered number ``0``.

* Release snapshots maybe removed from the RTEMS servers at the discretion of
  the RTEMS project

Release Repositories
====================

The following are the repositories that a release effects. Any repository
action is to be performed in the following repositories:

#. ``rtems.git``

#. ``rtems-docs.git``

#. ``rtems-examples.git``

#. ``rtems-libbsd.git``

#. ``rtems-source-builder.git``

#. ``rtems-tools.git``

#. ``rtems_waf.git``

#. ``rtems-release.git``

Pre-Release Procedure
=====================

* All tickets must be resolved, closed or moved to a later
  milestone. Tickets can exist that are specific to the branch and are
  to be resolved before the first release is made.

* Create release snapshots and post suitable build and test results.

Release Branching
=================

A release has a release branch in each of the release repositories. A
release is a created from a release branch. The release branch label
is the RTEMS major version number.

LibBSD Release Branch
---------------------

The ``rtems-libbsd.git`` is an exception as it has two active release
branches. The repository has a release branch based on the ``master``
like all the release repositories and it can have a FreeBSD version
specific release branch that is used in the release.

LibBSD runs two branches during it's development cycle. The ``master``
branch tracks the FreeBSD ``master`` branch. This means LibBSD tracks
FreeBSD's development. LibBSD also tracks a FreeBSD branch for the
RTEMS release. For example RTEMS 5 tracks FreeBSD 12 as it's release
base. This provides functionaly stability to the RTEMS 5 release by
allowing a control process to track bug fixes in FreeBSD 12.

Pre-Branch Procedure
--------------------

* All tickets assigned to the release's first milestone must be
  resolved. Tickets can exist that are specific to the branch and are
  to be resolved before the first release is made.

* The following BSP must build using the RSB:

  - ``arm/beagleboneblack``

* Check and make sure the RSB kernel, libbsd and tools configurations
  reference the ``master`` when the branch is made.

  The RSB GIT builds reference a specific commit so it is important
  the relevant configurations are valid.

Branch Procedure
----------------

* Branch labels are the major number as branch releases increment the minor
  number. A branch is only created when the first major release is made.

  The commands to set a remote branch for a release in a repository are:

  .. code-block:: none

      git clone <URL>/<REPO> <REPO>
      cd <REPO>
      git checkout -b <VERSION> origin/master
      git push origin <VERSION>

  Example:

  .. code-block:: none

      git clone ssh://chrisj@dispatch.rtems.org/data/git/rtems.git rtems.git
      cd rtems.git
      git checkout -b 5 origin/master
      git push origin 5

* Check and make sure the RSB kernel, libbsd and tools reference the
  branch commit.

Post-Branch Procedure
---------------------

#. Create a release page for the next RTEMS release in Trac.

#. Update the releases table. The page link is:

     https://devel.rtems.org/wiki/Release

   Update the table adding the new development release to the top
   moving down the previous releases.

   Label the new release branch as "Releasing". The documentation link
   is left pointing to ``master`` until the release is made and the
   documentation is installed on the RTEMS Documentation web site.

#. Update the release table in the front page of the Trac Wiki. The
   page link is:

     https://devel.rtems.org/wiki/

#. Add the milestones for the new development branch. The Trac page
   is:

  .. code-block:: none

    = 6.1 (open)

    == Statistics

    ||   '''Total'''||[[TicketQuery(milestone=6.1,count)]]                                      ||
    ||         Fixed||[[TicketQuery(status=closed&milestone=6.1,resolution=fixed,count,)]]      ||
    ||       Invalid||[[TicketQuery(status=closed&milestone=6.1,resolution=invalid,count,)]]    ||
    ||  Works for me||[[TicketQuery(status=closed&milestone=6.1,resolution=worksforme,count,)]] ||
    ||     Duplicate||[[TicketQuery(status=closed&milestone=6.1,resolution=duplicate,count,)]]  ||
    ||     Won't fix||[[TicketQuery(status=closed&milestone=6.1,resolution=wontfix,count,)]]    ||

    == Distribution
    [[TicketQuery(milestone=6.1&group=type,format=progress)]]

    == Summary
    [[TicketQuery(milestone=6.1)]]

    == Details
    [[TicketQuery(col=id|time|resolution|component|reporter|owner|changetime,status=closed&milestone=6.1,rows=summary|description,table)]]

  Replace ``6.1`` with the required milestone.

#. Create the RC1 release candidate with the source as close the
   branch point as possible.

#. Create a ticket to the clean the RSB for the release. The RSB's
   ``master`` branch carries a number of older configurations and new
   release configurations. These can be confusing to a new user and
   add no value to a released RSB. For example leaving RTEMS 6 tool
   building configurations in the RTEMS 5 release.

Post-Branch Version Number Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the release repositored have been branched the ``master`` branch
has to have the major version number updated. The follow is a list of
the needed changes.

#. RTEMS requires the following files be changed:

    * :file:`aclocal/version.m4`

    * :file:`c/src/aclocal/version.m4`

    * :file:`cpukit/aclocal/version.m4`

    * :file:`testsuites/aclocal/version.m4`

    * :file:`rtems-bsps`

#. RTEMS Documentation the following files be changed:

    * :file:`wscript`: Update ``rtems_major_version``.

#. RSB requires the following files be changed:

    * :file:`source-builder/sb/version.py`: Update ``_version``.

#. RTEMS Tools requires the following files be changed:

    * :file:`config/rtems-version.ini`: Update ``revision``.

    * :file:`tester/rtems/version.cfg`: Update ``rtems_version``.

#. rtems_libbsd requires the following files and branches be changed:

    * :file:`README.md`: Update ``Branches`` section.

    * :file:`wscript`: Update ``rtems_version``.

    * Create a new branch for tracking the FreeBSD stable version. E.g.
      ``6-freebsd-12``.

Release Procedure
=================

The release procedure can be performed on any FreeBSD machine and uploaded to
the RTEMS FTP server. You will need ssh access to the RTEMS server
``dispatch.rtems.org`` and suitable permissions to write into the FTP release
path on the RTEMS server.

#. The release process starts by branching the repositories. To branch
   run the script:

   .. code-block:: none

       ./rtems-release-branch [-p] <USER> <VERSION> <REVISION>

   Example:

   .. code-block:: none

       cd
       mkdir -p development/rtems/releases
       cd development/rtems/releases
       git clone git://git.rtems.org/rtems-release.git rtems-release.git
       cd rtems-release.git
       ./rtems-release-branch -p chrisj 5

   You need to have suitable commit access to the repositories.

#. To create the RTEMS release run the release script:

   .. code-block:: none

       ./rtems-release <VERSION> <REVISION>

   Example:

   .. code-block:: none

       ./rtems-release 5 1.0

#. Copy the release to the RTEMS FTP server:

   .. code-block:: none

       ssh <user>@dispatch.rtems.org mkdir -p /data/ftp/pub/rtems/releases/<VERSION>
       scp -r <VERSION>.<REVISION> <user>@dispatch.rtems.org:/data/ftp/pub/rtems/releases/<VERSION>/.

   Example:

   .. code-block:: none

       ssh chrisj@dispatch.rtems.org mkdir -p /data/ftp/pub/rtems/releases/5
       scp -r 5.1.0 chrisj@dispatch.rtems.org:/data/ftp/pub/rtems/releases/5/.

#. Verify the release has been uploaded by checking the link:

   https://ftp.rtems.org/pub/rtems/releases/<VERSION>/<VERSION>.<REVISION>

#. Tag the release repositories with the following command:

   .. code-block:: none

       git checkout -b origin/<VERSION>
       git tag <TAG>
       git push origin <TAG>

   Example:

   .. code-block:: none

      git clone ssh://chrisj@dispatch.rtems.org/data/git/rtems.git rtems.git
      cd rtems.git
      git checkout -b origin/5
      git tag 5.1.0
      git push origin 5.1.0

Post-Release Procedure
======================

The following procedures are performed after a release has been created.

#. Update the release to the RTEMS servers:

   .. code-block:: none

     rsync --rsh=ssh -arv 5.1.0 chrisj@dispatch.rtems.org:/data/ftp/pub/rtems/releases/5/.

#. Test a build of the ``beagleboneblack`` BSP.
