% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2024 Contemporary Software

% Copyright (C) 2024 Chris Johns

(Release_Process)=

# Release Maintenance

The release maintenance process manages release branches that RTEMS
uses to create releases. Development happens on the `main` branch
and any changes for releases are managed using release branches.

These procedures are designed to work within GitLab's workflows and
user interface while providing the project with control, visibility
and reporting.

The milestone is used to create the release notes. The procedures are
designed to preserve issues and merge requests on milestones so the
release notes are an accurate account of the changes made.

## Release Branch Maintenance

01. The management of release branch epics, issues and merge requests
    is the responsibility of all users with Developer or higher GitLab
    roles. Normal GitLab account holders cannot set milestones or
    labels, they cannot assign reviewers or promote issues to epics so
    issues need to be triaged before they can be worked on and
    resolved. Please help by triaging new issues and merge requests
    across all projects and repos we have when users create the issues.
02. Release branches shall only be created from a repository's `main`
    branch.
03. The release branch is the RTEMS version and is a number without
    leading zeros.
04. A tag of the form `base/<version>` where `<version>` is the
    version being branched shall be made to record the base commit of a
    release branch.
05. A release branch shall not be branched.
06. Releases are made from a release branch, and the commit on the
    release branch the release is made from shall be tagged with the
    full version string of the release.
07. APIs and features related to APIs shall not be changed on a release
    branch.
08. Non-overlapping additions can be made to release branches if APIs
    and related features are not changed. For example a network driver
    is added to a network stack. Community review by approvers shall
    determine what is suitable.
09. Development should occur on a repository's `main` branch where
    possible and any fix backported to a release branch using an issue
    attached to an epic.
10. The `main` branch shall have only one milestone, the next
    version's first release. For example if the next version is `7`
    the `main` milestone will be `7.1`.
11. A release branch shall have two milestones, the next release and
    the release that follows. Issues or merge requests for a release
    branch are assigned to the next release milestone by default and
    optionally moved to the following release milestone if not
    resolved for the next release within the release window. When a
    release is made a new milestone is added.
12. There is no dot zero (`.0`) release. That is reserved for the
    next version's development on `main` or the version of snapshots
    or git built versions taken from a release branch's repository.
13. The RTEMS Project only maintains and publishes releases from the
    previous two (2) release branches as part of its open
    processes. Releases from older release branches can be made under
    service agreements and with the support of the community.

## Release Epics and Issues

Epics and issues are used to help manage the approval process for commits
to release branches.

1. Every release branch shall have an associated Epic named `RTEMS <Major> Release` where `<Major>` is the branch name. This Epic
   shall have children Epics named `RTEMS <Major>.<Minor>` for the
   next two releases on the release branch.
2. Every Issue with a Milestone set to a release branch shall be linked to
   the Epic named `RTEMS <Major>.<Minor>` where the Major.Minor matches
   the Milestone.

## Release Merge Requests

1. Every merge request to a release branch shall have a Milestone that
   matches the next release version on that branch, and shall
   reference or close an Issue with the same Milestone. The commit
   messages within the Merge Request must refer to the Issue.
2. A merge request target branch shall be the milestone's major version
   number. If the milestone's major number is the next RTEMS Major release
   the target shall be `main`.

(Release_Backports)=

## How to Handle Backports

1. Issue triaging shall determine if an issue should be considered for
   backporting. Issues that are opened against one branch and
   requested to backport to a release branch must be cloned, which can
   be done with the GitLab Quick Action `/clone --with_notes` in a
   comment on the Issue. It is preferred to clone the notes so that
   the discussion/comment history leading to the backport request is
   preserved on the backport Issue. The milestone on the cloned issue
   shall be set to the requested backport release branch's next version.
2. Issues that are opened against a release branch milestone must be
   linked to that milestone's epic, which should be named `RTEMS <Milestone>`. Linking is accomplished by using the GitLab Quick
   Action `/epic rtems&<NNN>` where `<NNN>` is replaced with the
   Epic number for the relevant milestone's epic.
3. Issues that are determined out of scope for backporting shall be labelled
   `resolution::wontfix` and closed.
4. Merge Requests that target a release branch must reference or close
   an open Issue with a Milestone that matches the next release on that
   branch. It is the responsibility of submitters to ensure they
   close the correct Issue, and it is the responsibility of
   approvers to ensure that merge requests to a release branch close
   an open Issue with a matching milestone. When cherry-picking changes,
   commit messages will need to be modified locally to add the correct
   Issue number to the commit.
