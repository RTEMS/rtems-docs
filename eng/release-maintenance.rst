.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 Contemporary Software
.. Copyright (C) 2024 Chris Johns

.. _Release_Process:

Release Maintenance
*******************

The release maintenance process manages release branches that RTEMS
uses to create releases. Development happens on the ``main`` branch
and any changes for releases are managed using release branches.

These procedures are designed to work within GitLab's workflows and
user interface while providing the project with control, visibility
and reporting.

The milestone is used to create the release notes. The procedures are
designed to preserve issues and merge requests on milestones so the
release notes are an accurate account of the changes made.

Release Branch Maintenance
==========================

#. The management of release branch epics, issues and merge requests
   is the responsibility of all users with approver or higher GitLab
   status. Normal GitLab account holders cannot set milestones or
   labels, they cannot assign reviewers or promote issues to epics so
   issues need to be triaged before they can be worked on and
   resolved. Please help by triaging new issues and merge requests
   across all projects and repos we have when users create the issues.

#. Release branches shall only be created from a repository's ``main``
   branch.

#. The release branch is the RTEMS version and is a number without
   leading zeros.

#. A tag of the form ``base/<version>`` where ``<version>`` is the
   version being branched shall be made to record the base commit of a
   release branch.

#. A release branch shall not be branched.

#. Releases are made from a release branch, and the commit on the
   release branch the release is made from shall be tagged with the
   full version string of the release.

#. APIs and features related to APIs shall not be changed on a release
   branch.

#. Non-overlapping additions can be made to release branches if APIs
   and related features are not changed. For example a network driver
   is added to a network stack. Community review by approvers shall
   determine what is suitable.

#. Development should occur on a repository's ``main`` branch where
   possible and any fixes backported to release branches using epics.

#. The ``main`` branch shall have only one milestone, the next
   version's first release. For example if the next version is ``7``
   the ``main`` milestone will be ``7.1``.

#. A release branch shall have two milestones, the next release and
   the release that follows. Issues or merge requests for a release
   branch are assigned to the next release milestone by default and
   optionally moved to the following release milestone if not
   resolved for the next release within the release window. When a
   release is made a new milestone is added.

#. There is no dot zero (``.0``) release. That is reserved for the
   next version's development on ``main`` or the version of snapshots
   or git built versions taken from a release branch's repository.

#. The RTEMS Project only maintains and publishes releases from the
   previous two (2) release branches as part of its open
   processes. Releases from older release branches can be made under
   service agreements and with the support of the community.

Release Labels
==============

Release labels are used to help management and report release branch
epics, issues and merge requests.

#. GitLab labels for release maintenance shall use a single colon
   character (``:``) as a delimiter as double colons are scoped labels
   and you can only have one scoped label per epic, issue or merge
   request.

#. Epics and issues affecting release branches are required to
   have the ``backport`` label.

#. The ``version:<version>`` label indicates an epic or issue may
   affect a version of RTEMS. For example an issue may have
   ``version:5`` and ``version:6`` assigned to indicate the issue
   relates to RTEMS 5 and RTEMS 6.

#. The ``backport`` label indicates an epic or issue is to be resolved
   on more than one version of RTEMS. If the issue is for a single
   version of RTEMS a single version label is required.

Release Epics and Issues
========================

#. Management of an issue on more than one version of RTEMS shall use
   an epic.

#. A release branch epic is to be labelled ``backport``. This lets
   us filter release branch epics.

#. A release branch epic shall have a child issue for each version of
   RTEMS it relates to. This includes the development branch
   ``main``. Each issue shall have the milestone set to the verion of
   RTEMS effected.

#. An issue raised by a user needs to provide the version or versions
   of RTEMS it relates to in the description. The issue or merge
   request template shall provide a pre-filled field that can be
   edited.

#. Issue triaging shall promote a user issue to an epic if it effects
   more than one version of RTEMS.

#. A release branch issues that is a child of an epic can only be
   referenced by merge requests for the milestone branch.

Release Merge Requests
======================

#. A merge request for a release branch must have an issue set to the
   same milestone.

#. A merge request target branch shall be the milestone's major version
   number. If the milestone's major number is the next release the
   target shall be ``main``.
