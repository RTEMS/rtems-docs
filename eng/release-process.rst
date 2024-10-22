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

Releases are grouped under the major version number as a collection of
directories consisting of the version number. This is termed a release
series. A release may also contain release candidates and snapshots.

All releases must have a three digit version number and this can be optionally
followed by a dash character (``-``) and an identifier, e.g. ``5.1.0-acme-1``.

The RTEMS Project reserves releases with only the three digit version number,
e.g. ``5.1.0``. This identifies an RTEMS Project release.

Release Layout
--------------

* All released source archives are XZ compressed tar files.

* Top level contains:

  :file:`README.txt`:
      A set of brief release links and instructions in text format
      generated from the :file:`README` markdown file.

  :file:`index.txt`:
      A set of brief release links and instructions as an HTML web
      page generated from the :file:`README` markdown file.

  :file:`contrib`:
      Contributed sources. For example the release scripts used to
      create the release.

  :file:`docs`:
      Compressed documentation in HTML, Single page HTML and PDF
      formats. The directory contains compressed files for each
      document and a single archive of all the documentation. An
      SHA512 checksum file is also provided to allow verification of
      the files. The HTML documentation is available in the
      :file:`docs/html` directory the :file:`docs` directory contains
      the PDF documentation. Links are provided in release cover page.

  :file:`rtems-<VERSION>-release-notes`:
      RTEMS Release notes as an HTML web site. This is a capture of
      the Gitlab milestone issues and merge requests in the release.

  :file:`rtems-<VERSION>-release-notes.pdf`:
      RTEMS Release notes as a PDF document. This is a capture of the
      Gitlab milestone issues and merge request.

  :file:`rtems-<VERSION>-release-notes.jzon.xz`:
      RTEMS Release JSON data captured from Gitlab for the release
      milestone abnd used to create the release notes.

  :file:`rtems-docs-<VERSION>.tar.xz`:
      RTEMS Release Documentation source code.

  :file:`sha512sum.txt`:
      SHA512 checksum of all files in this directory.

  :file:`sources`:
      All source code referenced by the release.

Release Version Numbering
-------------------------

The release numbering scheme changed with RTEMS 5. The project moved
to two release numbers from the traditional three numbers. The major
number was not being used and there was no easy clear process we could
use to decide when to increment it. The major number role was
deprecated and the numbers moved one to the left.

The RTEMS Project reserves release versions with ``major.minor.0``
version numbers and an empty release label. If the sources deployed to
end users or systems contain changes to a release you are required to
add a unique identifier to the release label.

Version string must be unique for every released version of RTEMS. The
release label provides a way for deployed RTEMS sources to have a
unique version string.

Release Number
^^^^^^^^^^^^^^

A release number has the following fields separated by the dot (``.``)
character:

``RTEMS_MAJOR``
  The major version number. This number increments with each
  release. The value is updated after a release branch has been
  created.

``RTEMS_MINOR``
  The minor version number is the branch release number and it
  increments with each release made on that release branch. The minor
  version number shall be ``0`` on all branches in the repository. The
  value is set using the release generated ``VERSION`` file.

``RTEMS_REVISION``

  The revision field is not used by the RTEMS Project and all releases
  it makes shall have a value of ``0``. This field can used by users
  deploying modified releases with a suitable release label.

The main branch tracks the version ``N.0.0`` with ``N`` being the next
major release number.

Examples:

 - ``5.0.0`` is the version number of the development main for the 5 series

 - ``5.1.0`` is the first release of the 5 series

 - ``5.2.0`` is the first bugfix release of the 5 series

 - ``5.3.0`` is the second bugfix release of the 5 series

 - ``6.0.0`` is the version number of the development main for the 6 series

Release Label
^^^^^^^^^^^^^

The release label is a string that can be used to provide context
specific information about a release. The default value for the
release label shall be ``not-released``.

The users and vendors releasing RTEMS can use the release label for
their own purposes. It can contain unique labels and specific versions
identifiers.

The release can set the release label by:

#. A ``VERSION`` file that sets the release label.

#. No ``VERSION`` file and the sources resides in a valid version
   controlled repository. The release label shall be a version control
   system identifer that identifies a unique commit and the state of
   the sources under the control of the repository.

#. If there is no ``VERSION`` file and no valid version contolled
   repository found the release label shall be the default value.

A release with no release label is resevered for the RTEMS
Project. This helps the project identify the origin of the release
sources and how to help users with support questions.

Production builds of RTEMS from the RTEMS Projects's version
controlled repository can use the version controlled identifier as a
release label.

Examples the RTEMS RTOS version string:

 - ``6.1.0`` is the version number of the first RTEMS 6 release made
   by the RTEMS project.

 - ``6.0.0.b45cf44489`` is a build of RTEMS without a ``VERSION`` file
   and with the sources in a version controlled repository. The
   identifer is the git commit hash.

 - ``6.0.0.b45cf44489-modified`` is the same build of source in the
   previous example with a locally modified file.

 - ``6.3.0.rc1`` is the first release candidate from the second bug
   fix release of RTEMS 6.

 - ``6.1.0.acme-corp`` is the vendor release from the fictional Acme
   Corporation based on the RTEMS 6.1.0 release.

Version String
^^^^^^^^^^^^^^

#. The version string is the release number and release label
   separated by a dash (``-``) character.

#. The RTEMS RTOS kernel version string is the release number and
   release label separated by a dot (``.``) character. The RTEMS
   version string is the only place a ``.`` is used to separate the
   version number from the release label.

Release Scripts
----------------

#. The release scripts are held in the
   `RTEMS Release repository <https://gitlab.rtems.org/rtems/rtos/rtems-release>`_.

#. The release scripts are not branched and the only branch is
   ``main``. The script are maintained to make a release back to the
   4.11 series.

#. The scripts are written for FreeBSD and can run on FreeBSD 10
   through FreeBSD 14. No other host operating system is supported for
   the releases. Updates for other operating systems are welcome if
   the changes do not affect the operation on FreeBSD.

#. A Python ``virutalenv`` environment is required to runs the tools
   needed to make a release. The top level ``README.md`` file provides
   the specific list of packages you are required to install.

#. The release notes are generated from Issue and Merge Request data
   in the RTEMS Project's Gitlab instance. A read only API key is
   needed to create the release notes. The ``README.md`` provides the
   details about the Gitlab key and required configuration file
   format.

#. Building a standard release requires you provide the release major
   number, the release's minor number and optionally a release label:

   .. code-block:: none

      ./rtems-release 6 1

   To create a release release candidate:

   .. code-block:: none

      ./rtems-release 6 1-rc1

   To create a snapshot:

   .. code-block:: none

      ./rtems-release 6 0-m2410

#. A 3rd option of a release URL can be provided to create a test or deployable
   release. The URL is a base path the RSB uses to download the release source
   files from:

   .. code-block:: none

     ./rtems-release \
         -u https://ftp.rtems.org/pub/rtems/people/chrisj/releases \
         6 0.0-m2410-test

Release Snapshots
-----------------

#. Release snapshots are only created for the current development
   version of RTEMS. For example RTEMS 5 snapshot path is
   :file:`5/5.0.0/5.0.0-m2003`.

#. Release snapshots are based on the development sources and may be
   unstable or not suitable for use in production.

#. A release snapshot is created each month and is named as
   ``<major>/<version>/<version>-<YYMM>`` where ``YY`` is the last two
   digits of the current year and ``MM`` is the month as a two digit
   number.

#. In the lead up to a release more than one snapshot can be created
   by appending ``-<count>`` to the snapshot version string where
   ``<count>`` is incremented starting from ``1``. The first snapshot
   without a count is considered number ``0``.

#. Release snapshots maybe removed from the RTEMS servers at the
   discretion of the RTEMS project

Release Repositories
====================

The following are the repositories that a release effects. Any repository
action is to be performed in the following repositories:

* ``rtems.git``

* ``rtems-deployment.git``

* ``rtems-docs.git``

* ``rtems-examples.git``

* ``rtems-libbsd.git``

* ``rtems-lwip.git``

* ``rtems-net-legacy.git``

* ``rtems-net-services.git``

* ``rtems-release.git``

* ``rtems-source-builder.git``

* ``rtems-tools.git``

* ``rtems_waf.git``

Pre-Release Procedure
=====================

#. All issues and merge requests for the release milestone must be
   resolved, closed, or moved to a later milestone. Issues can exist
   that are specific to the branch to be resolved before the first
   release is made.

#. Create release snapshots and post suitable build and test results.

Release Branching
=================

A release has a release branch in each of the release repositories. A
release is created from a release branch. The release branch label is
the RTEMS major version number.

LibBSD Release Branch
---------------------

The ``rtems-libbsd.git`` is an exception as it has two active release
branches. The repository has a release branch based on the ``main``
like all the release repositories and it can have a FreeBSD version
specific release branch that is used in the release.

LibBSD runs two branches during it's development cycle. The ``main``
branch tracks the FreeBSD ``current`` branch. This means LibBSD tracks
FreeBSD's development. LibBSD also tracks a FreeBSD branch for the
RTEMS release. For example RTEMS 5 tracks FreeBSD 12 as it's release
base. This provides functional stability to the RTEMS 5 release by
allowing a control process to track bug fixes in FreeBSD 12.

Pre-Branch Procedure
--------------------

#. All issues and merge requests assigned to the release's first
   milestone must be resolved. Issues can exist that are specific to
   the branch and are to be resolved before the first release is
   made. All merge requests must be resolved.

#. The following BSP must build using the RSB:

   - ``arm/beagleboneblack``

#. Run the RSB command ``sb-rtems-pkg`` command to make sure the RSB
   kernel, libbsd and tools configurations reference the ``main`` when
   the branch is made.

   The RSB Git build references a specific commit so it is important
   the relevant configurations are valid. RSB release builds reference
   the source tar file in the release's :file:`sources` directory.

Branch Procedure
----------------

#. Branch labels are the major number as branch releases increment the
   minor number. A branch is only created when the first major release
   is to be made.

#. The main project repositories in Gitlab are protected so branches
   need to be made by a Gitlab administrator. To branch the main
   repositories create an issue in
   https://gitlab.rtems.org/administration/gitlab and provide the
   following list of repositories that need to be branched for the
   release and the commit hash in each repository to branch:

    * https://gitlab.rtems.org/rtems/docs/rtems-docs/-/branches

    * https://gitlab.rtems.org/rtems/tools/rtems-source-builder/-/branches

    * https://gitlab.rtems.org/rtems/tools/rtems-tools/-/branches

    * https://gitlab.rtems.org/rtems/rtos/rtems/-/branches

    * https://gitlab.rtems.org/rtems/pkg/rtems-libbsd/-/branches

    * https://gitlab.rtems.org/rtems/pkg/rtems-net-legacy/-/branches

    * https://gitlab.rtems.org/rtems/pkg/rtems-lwip/-/branches

    * https://gitlab.rtems.org/rtems/pkg/rtems-net-services/-/branches

    * https://gitlab.rtems.org/rtems/tools/rtems_waf/-/branches

    * https://gitlab.rtems.org/rtems/tools/rtems-deployment/-/branches

    * https://gitlab.rtems.org/rtems/rtos/rtems-examples/-/branches

    * https://gitlab.rtems.org/rtems/pkg/rtems-littlevgl/-/branches

#. Check and make sure the RSB kernel, libbsd and tools reference the
   branch commit.

Post-Branch Procedure
---------------------

#. Create a milestone for the next version of RTEMS. To create a new
   milestone open an issue in
   https://gitlab.rtems.org/administration/gitlab  If no start date is
   provided it will be set to the end date of the previous release in
   series.

#. Create the next RC release candidate with the source as close the
   branch point as possible.

#. Create a ticket to the clean the RSB for the release. The RSB's
   ``main`` branch carries a number of older configurations and new
   release configurations. These can be confusing to a new user and
   add no value to a released RSB. For example leaving RTEMS 7 tool
   building configurations in the RTEMS 6 release.

#. Check out the release branch of ``rtems-central.git``.  Change all Git
   submodules to reference commits of the corresponding release branch.  Run
   ``./spec2modules.py``.  Inspect all Git submodules for changes.  If there
   are locally modified files, then there are two options.  Firstly, integrate
   the changes in the release branches.  Afterwards update the Git submodule
   commit.  Secondly, change the specification so that a particular change is
   not made.  Make sure that there are no changes after this procedure.

Post-Branch Version Number Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the release repositories have been branched the ``main``
branches of some repositories have to have the major version number
updated. The following is a list of the needed changes.

#. RTEMS requires the following files be changed:

    * :file:`Doxyfile`: Update ``PROJECT_NUMBER``.

    * :file:`rtems-bsps`: Update ``rtems_version``.

    * :file:`wscript`: Update ``version["__RTEMS_MAJOR__"]``.

#. RTEMS Documentation the following files be changed:

    * :file:`wscript`: Update ``rtems_major_version``.

#. RSB requires the following files be changed:

    * :file:`source-builder/sb/version.py`: Update ``_version``.

#. RTEMS Tools requires the following files be changed:

    * :file:`config/rtems-version.ini`: Update ``revision``.

    * :file:`tester/rtems/version.cfg`: Update ``rtems_version``.

#. ``rtems-libbsd`` requires the following files and branches be changed:

    * :file:`README.md`: Update ``Branches`` section.

    * :file:`wscript`: Update ``rtems_version``.

    * Create a new branch for tracking the FreeBSD stable version, for example
      ``6-freebsd-12``.

#. ``rtems-examples`` requires the following files be changed:

    * :file:`wscript`: Update ``rtems_version``.

Release Procedure
=================

The release procedure can be performed on any FreeBSD machine and uploaded to
the RTEMS FTP server. You will need ssh access to the RTEMS server
``dispatch.rtems.org`` and suitable permissions to write into the FTP release
path on the RTEMS server.

#. The release process starts by branching the repositories. The
   `Branch Procedure`_ details how to branch the main repositories.

#. To create the RTEMS release run the release script:

   .. code-block:: none

       ./rtems-release <VERSION> <REVISION>

   Example:

   .. code-block:: none

       ./rtems-release 6 1

#. Copy the release to the RTEMS FTP server:

   .. code-block:: none

       ssh <user>@dispatch.rtems.org mkdir -p /data/ftp/pub/rtems/releases/<VERSION>
       scp -r <VERSION>.<REVISION> <user>@dispatch.rtems.org:/data/ftp/pub/rtems/releases/<VERSION>/.

   Example:

   .. code-block:: none

       ssh chrisj@dispatch.rtems.org mkdir -p /data/ftp/pub/rtems/releases/5
       scp -r 5.1.0 chrisj@dispatch.rtems.org:/data/ftp/pub/rtems/releases/5/.

#. Verify the release has been uploaded by checking the link:

   ``https://ftp.rtems.org/pub/rtems/releases/<VERSION>/<VERSION>``

#. Tag the release repositories by creating an issue in
   https://gitlab.rtems.org/administration/gitlab and provide the tag,
   the same list of repositories used to create the release branch for
   the release and the commit hash in each repository to tag. See the
   `Branch Procedure`_ for the list of repositories to tag.

Post-Release Procedure
======================

The following procedures are performed after a release has been created.

#. Update the release to the RTEMS servers:

   .. code-block:: none

     rsync --rsh=ssh -arv 6.1 chrisj@dispatch.rtems.org:/data/ftp/pub/rtems/releases/6/.

#. Test a build of the ``beagleboneblack`` BSP.

VERSION File Format
===================

#. The ``VERSION`` is generated when making releases by the release
   procedure and is contained in the relased source tar file. It shall
   not be placed under version control.

#. The file is in the INI format.

#. The ``[DEFAULT]`` section is ignored.

#. Sections not listed here are ignored.

#. The file is required to have a ``[version]`` section.

#. The ``[version]`` section is required to have a ``revision``
   option. The revision option is a version string as defined by
   `Version String`_. The revision label separator is a dash (``-``).

#. The ``[version]`` section can optionally contain a ``release_path``
   option. The release path is a URL the RSB supports to the released
   :file:`sources` directory. The RSB uses this field to fetch all
   sources used in a build.

#. An optional section ``[hashes]`` can be used to hold the checksums
   for files downloaded by the RSB. The source tar files created by
   the release procedure for some packages downloaded by the RSB
   have different checksums to the values held in the RSB
   repository. A checksum hash in the ``VERSION`` file overrides the
   checksum in the RSB configuration files.

Examples:

* Version only configuration:

  .. code-block:: ini

    [version]
    revision = 6.1

* RSB configuration:

  .. code-block:: ini

    [version]
    revision = 6.1
    release_path = https://ftp.rtems.org/pub/rtems/releases/6/6.1/sources

    [hashes]
    rtems-tools-6.1.tar.xz = sha512 837d9ec058e14f26fe69a702729a7
    rtems-6.1.tar.xz = sha512 b37079591a35d0601a73b32912f8773bc40
    rtems-libbsd-6.1.tar.xz = sha512 768546b80cd8c8ca20fb1b695b56
