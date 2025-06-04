% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018.

% COMMENT: RTEMS Foundation, The RTEMS Documentation Project

# Change Control with GitLab

## Updating GitLab Metadata

Only GitLab accounts with a role of Developer or above have permissions to
modify the metadata of Issues and Merge Requests. This section is intended
for those individuals.

### Assignee

The assignee of a merge request should usually be set to the submitter.  Not
all users will appear in the Edit boxes. Add the user by a @user in a comment,
refresh your browser and then you can edit the assignee.

The assignee of an Issue should be set to someone (accepting to be) responsible
for handling it.

### Reviewers

You may add reviewers to a Merge Request to ensure specific individuals are in
the approval chain. This should be done (or undone) at your discretion.

### Labels

Until further guidance can be determined, use your best effort to assign one
or more relevant labels to Issues and Merge Requests.

### Milestones

The milestone assigned to a Merge Request must match the branch that it
targets. Usually, the target branch should be `main` and you should set
the milestone to the next release. See below in case a Merge Request targets
a release branch.

### Release Branches

There are additional checks to use for any changes that directly apply or are
backported to a release branch. These checks need to satisfy the requirements
of the {ref}`Release_Process`. For requested backports, please refer directly
to {ref}`Release_Backports`. With any Merge Request targeting a release branch,
ensure that:

* The commit messages of the Merge Request refer to an Issue with the Milestone
  that matches the release branch. Add this Milestone to the Merge Request.

* The Issue referenced by the Merge Request is linked to the Epic for the
  target release.

## Approving Merge Requests

This section is intended for those individuals who are `Approvers` and for
anyone else who wants to participate in the {ref}`PatchReviewProcess` as a code
reviewer.

### Conflict of Interest Rules

We do not have formally adopted Conflict of Interest rules, but we generally
avoid public review and approval by individuals who (should) have privately
reviewed code. This means that you should not approve code that is submitted by
someone who works with you commercially. Instead, you could provide input to
the review or to assist your colleague in resolving review feedback.

### Continuous Integration Pipelines

Check the status of the pipelines and give feedback to help contributors to fix
errors.

### Check the Commits

Ensure the commits are properly made according to the {ref}`Commit_Messages`.
For new contributors, download the patch file (under the Code button) and make
sure they have set a name and email address in their git metadata.

### Creating a Review

Navigate to the `Changes` tab in GitLab, and provide inline comments. It is up
to you if you want to add comments one at a time or in bulk using the "Start a
review" option. 

Avoid adding comments directly in the `Overview` tab. If you do make comments
there that need to be addressed, you should ensure they show up as "threads" by
either checking that option when you write the comment, or by replying to your
own comment to turn it into a thread.

Each comment that you add should only be on one concern. Grouping multiple
review concerns in the same comment makes it harder to check that all concerns
are resolved satisfactorily.

### Marking a Merge Request as a Draft

You can mark a Merge Request as a Draft if there are deficiencies that will
take some time to resolve or simply to prevent it from being merged.
In general, other reviewers will ignore such Draft Merge Requests. This should
be used to reduce reviewer burden or to indicate the change should be held off
regardless of the approval. For example, during the preparation of a release
the pending Merge Requests may be marked as Draft to prevent them from being
merged.

### Cloning a Merge Request

Prior to approving, it is your responsibility to ensure that the change works
as intended. In some cases this may be done without having to clone and test
changes, but often you will need to do some work locally. There are a few ways
you can do this.

### Approving

Approve! Merge! If you think it should be merged but cannot, check for reasons
that block it. For example, if it just needs to be rebased, do it! If the
rebase has conflicts, you can either ask the submitter to handle it, or you can
use the preceding instructions for cloning the Merge Request to fix it
yourself. It is generally preferable to give the submitter a chance to fix it
on their own. If you cannot see why a Merge Request cannot be merged, please
make an inquiry in the {r:url}`discord`.

