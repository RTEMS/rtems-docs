.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 Contemporary Software
.. Copyright (C) 2020 Chris Johns

.. _Release_Process:

Release Process
***************

The release process creates an RTEMS release. The process has a number of
stages that happen before a release can be made, during the creation of the
release procedure and after the release has been made.

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

#. rtems.git

#. rtems-docs.git

#. rtems-examples.git

#. rtems-libbsd.git

#. rtems-source-builder.git

#. rtems-tools

#. rtems_waf

Pre-Release Procedure
=====================

* All tickets must be resolved, closed or moved to a later milestone.

* The following BSP must build using the RSB:

  - ``arm/beagleboneblack``

* Branch labels are the major number as branch releases increment the minor
  number. A branch is only created when the first major release is made.

  The commands to set a remote branch for a release in a repository are:

  .. code-block:: none

      git checkout -b <VERSION> origin/master
      git push origin <VERSION>

  Example:

  .. code-block:: none

      git clone ssh://chrisj@dispatch.rtems.org/data/git/rtems.git rtems.git
      cd rtems.git
      git checkout -b 5 origin/master
      git push origin 5

Release Procedure
=================

The release procedure can be performed on any FreeBSD machine and uploaded to
the RTEMS FTP server. You will need ssh access to the RTEMS server
``dispatch.rtems.org`` and suitable permissions to write into the FTP release
path on the RTEMS server.

#. To create the RTEMS release run the release script:

   .. code-block:: none

       ./rtems-release <VERSION> <REVISION>

   Example:

   .. code-block:: none

       cd
       mkdir -p development/rtems/releases
       cd development/rtems/releases
       git clone git://git.rtems.org/rtems-release.git rtems-release.git
       cd rtems-release.git
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

#. TBD
