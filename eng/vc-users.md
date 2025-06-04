% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018.

% COMMENT: RTEMS Foundation, The RTEMS Documentation Project

# Software Development with GitLab

## Browse the Git Repository Online

You can browse repositories from [your home page](https://gitlab.rtems.org)
or from <https://gitlab.rtems.org/explore/projects> to see a global view
including all forks and most starred projects on the RTEMS gitlab instance.

The sort order can be changed by the drop-down at the far right of the GUI. If
you are logged in, your preferences should be saved so that the sort order is
persistent.

From your home page, you can also view
[your starred repositories](https://gitlab.rtems.org/dashboard/projects/starred).
This is a handy page to use to navigate to the repositories that interest you
the most. In addition, you can
[change your preferences](https://gitlab.rtems.org/-/profile/preferences)
for your Homepage to show the Starred Projects among other possibly useful
landing pages.

## Using Git

An exhaustive treatment here is not possible. We suggest availing yourself of
online resources to learn how to use Git, such as:

- <http://gitready.com/> - An excellent resource from beginner to very advanced.
- <https://git-scm.com/docs> - The official Git reference.
- <https://docs.gitlab.com/> - GitLab's documentation.

## Making Changes with Branches

Git allows you to make changes in the RTEMS source tree and track those changes
locally. We recommend you make all your changes in local branches. If you are
working on a few different changes or a progression of changes it is best to
use a local branch for each change.

A branch for each change lets your repo's main branch track the upstream
RTEMS' main branch without interacting with any of the changes you are
working on. A completed change is submitted as Merge Request for review
and this can take time. While this is happening the upstream's main branch
may be updated and you may need to rebase your work and test again if you are
required to change or update your patch. A local branch isolates a specific
change from others and helps you manage the process.

## Working with Remote Branches

The previous releases of RTEMS are available through remote branches. To check
out a remote branch, first query the Git repository for the list of branches:

```shell
git branch origin -r
```

Then check out the desired remote branch, for example:

```shell
git checkout -t rtems@rtems-ver-major@@rtems-ver-minor@ origin/@rtems-ver-major@.@rtems-ver-minor@
```

Or if you have previously checked out the remote branch then you should see it
in your local branches:

```shell
git branch
```

## Rebasing

An alternative to the merge command is rebase, which replays the changes
(commits) on one branch onto another. `git rebase` finds the common ancestor
of the two branches, stores each commit of the branch you are on to temporary
files and applies each commit in order.

Rebasing makes a cleaner history than merging; the log of a rebased branch
looks like a linear history as if the work was done serially rather than in
parallel. A primary reason to rebase is to ensure commits apply cleanly on a
remote branch, e.g. when submitting patches to RTEMS that you create by working
on a branch in a personal repository. Using rebase to merge your work with the
remote branch eliminates most integration work for the committer/maintainer.
We require maintaining a linear history in our repositories.

There is one caveat to using rebase: Do not rebase commits that you have pushed
to a public repository. Rebase abandons existing commits and creates new ones
that are similar but different. If you push commits that others pull down, and
then you rewrite those commits with `git rebase` and push them up again, the
others will have to re-merge their work and trying to integrate their work
into yours can become messy.

(Commit_Messages)=

## Commit Message Guidance

The commit message associated with a change to any software project
is of critical importance. It is the explanation of the change and the
rationale for it. Future users looking back through the project history
will rely on it. Even the author of the change will likely rely on it
once they have forgotten the details of the change. It is important to
make the message useful. Here are some guidelines followed by the RTEMS
Project to help improve the quality of our commit messages.

- When committing a change the first line is a summary. Please make it short
  while hinting at the nature of the change. You can discuss the change
  if you wish in a ticket that has a PR number which can be referenced in
  the commit message. After the first line, leave an empty line and add
  whatever required details you feel are needed.
- Patches should be as single purpose as possible. This is reflected in
  the first line summary message. If you find yourself writing something
  like "Fixed X and Y", "Updated A and B", or similar, then evaluate
  whether the patch should really be a patch series rather than a single
  larger patch.
- Format the commit message so it is readable and clear. If you have
  specific points related to the change make them with separate paragraphs
  and if you wish you can optionally uses a `-` marker with suitable
  indents and alignment to aid readability.
- Limit the line length to less than 80 characters
- Please use a real name with a valid email address. Please do not use
  pseudonyms or provide anonymous contributions.
- Please do not use terms such as "Fix bug", "With this change it
  works", or "Bump hash". If you fix a bug please state the nature of the
  bug and why this change fixes it. If a change makes something work then
  detail the reason. You do not need to explain the change line by line
  as the commits diff and associated ticket will.
- If you change the formatting of source code in a repository please
  make that a separate patch and use "Formatting changes only" on the first
  line. Please indicate the reason or process. For example to "Conforming
  to code standing", "Reverting to upstream format", "Result of automatic
  formatting".
- Similarly, if addressing a spelling, grammar, or Doxygen issue, please
  put that in a commit by itself separate from technical changes.

An example commit message:

```shell
test/change: Test message on formatting of commits

- Shows a simple single first line

- Has an empty second line

- Shows the specifics of adding separate points in the commit message as
  separate paragraphs. It also shows a `-` separator and multilines
  that are less than the 80 character width

- Show a ticket update and close

Updates #9876
Closes #8765
```

The first line generally starts with a file or directory name which
indicates the area in RTEMS to which the commit applies. For a patch
series which impacts multiple BSPs, it is common to put each BSP into
a separate patch. This improves the quality and specificity of the
commit messages.

```{include} ../../common/content/merge-request-creation.rst
```

```{include} ../../common/content/merge-request-review.rst
```
