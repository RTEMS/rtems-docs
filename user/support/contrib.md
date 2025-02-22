% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2024 Gedare Bloom

% Copyright (C) 2019 embedded brains GmbH & Co. KG

% Copyright (C) 2019 Sebastian Huber

% Copyright (C) 2018 Joel Sherill

% Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

```{index} community; developers
```

(contributing)=

# Contributing

## How to Contribute?

You can contribute to the RTEMS Project in various ways, for example:

- participation in mailing list discussions, helping other users
- documentation updates, clarifications, consolidation, fixes
- bug fixes, bug report consolidation
- new BSPs
- new device drivers
- new CPU (processor architecture) ports
- improvements in the existing code base (code size, code clarity, test
  coverage, performance optimizations)
- new features
- RTEMS Tools improvements

Most contributions will end up in patches of the RTEMS source code or
documentation sources. The patch integration into the RTEMS repositories is
done through a
{ref}`patch review process <PatchReviewProcess>`
on Gitlab.

## Preparing and Submitting Merge Requests

The RTEMS Project uses Git for version control and uses Gitlab for managing
changes. Contributions are made by creating a Merge Request (MR) on Gitlab. The
[Gitlab merge request documentation](https://docs.gitlab.com/ee/user/project/merge_requests/) comprehensively
explains the concepts of using merge requests. RTEMS will only accept changes
via a Merge Request. Most merge requests should have one or more Issues
associated with them, unless it is a simple, isolated change. Please do not use
merge requests to introduce new code, concepts, styles or to change existing
behaviours such as APIs or internal interfaces. Please create an issue before
you start the work so the community is aware of the changes coming. The merge
requests can then focus on the details of the implementation and approval does
not need to be about approval of change at a functional level.

We use project forks as the base of our workflow and outside of that there is
no workflow we mandate. What works for one task or work package may not work
for another. Complex tasks may affect a number of our GitLab Projects with
issues and merge requests in a number of projects. You may want to use an Epic
to bring work together.

With our GitLab instance, you fork a repo into your personal workspace and use
that to manage your changes. This means you need to keep your forked project
up to date. See the `Gitlab forking workflow documentation <https://docs.gitlab.com/ee/user/project/merge_requests/authorization_for_merge_requests.html#forking-workflow>`
for details. If you are part of a team working on a change you can `collaborate on merge requests <https://docs.gitlab.com/ee/user/project/merge_requests/allow_collaboration.html>`.
GitLab enforces branch naming rules and provides `branch naming patterns <https://docs.gitlab.com/ee/user/project/repository/branches/index.html#prefix-branch-names-with-issue-numbers>`
that simplifies code review and software change management. You can `create merge requests from your fork <https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html#when-you-work-in-a-fork>`
back to the upstream repository. We do not normally squash merge requests. A
merge request with more than one commit should be buildable at each commit so a
bisect of main does not break.

(checklistforpatches)=

## Checklist for Merge Requests

Check the following items before you publish your merge requests:

- The author name of each commit is a full name of the author.
- The author email of each commit is a valid email address for the author.
- The licence conditions of the contributed content allow an integration into
  the RTEMS code base.
- If you are the copyright holder of the entire patch content, then please
  contribute it under the
  [BSD-2-Clause](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/LICENSE.BSD-2-Clause?ref_type=heads)
  license. For documentation use
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Make sure you have a meaningful title which does not exceed 50 characters in
  one line. Use a "topic: The meaningful title" style. A topic could be the
  main component of the commit. Just have a look at existing commit messages.
- Each patch has a good commit message. It should describe the reason for the
  change. It should list alternative approaches and why they were not chosen.
- The code changes honour the coding style. At least do your changes in the
  style of the surrounding code.
- Each patch contains no spelling mistakes and grammar errors.
- Each patch is easy to review. It changes one thing only and contains no
  unrelated changes. Format changes should be separated from functional
  changes.
- If commits correspond to Issues, the merge request should have "Close #X." or
  "Update #X." to update status once it is merged.
- Each patch builds. All RTEMS tests link with every patch.
- Each patch does not introduce new compiler warnings.
- Each patch does not introduce new test failures in existing tests.

(patchreviewprocess)=

## Review Process

Merge requests sent to the RTEMS Gitlab undergo a public review process. At
least two approvals are required before a merge request can be pushed to the
RTEMS repository. It helps if you follow the {ref}`ChecklistForPatches`.
An easy to review patch series which meets the quality standards of the RTEMS
Project will be more likely to get integrated quickly.

The review process includes both objective and subjective feedback. You should
reflect upon and consider all feedback before making or refusing changes. It
is important to note that some feedback may be relevant at one point in time,
but less relevant in the future. Also, what concerns one developer may not
concern another. Just because you address all the feedback in one round of
review does not mean your submission will be approved, as someone (even the
same reviewer) may notice something that was not seen before. It is important
to have patience, humility, and open-mindedness when engaging in open-source
software review and approval processes. This is true for both contributors and
reviewers.

Reviews should be conducted primarily via the GitLab interface using the
in-line commenting feature. Follow-up comments to the same line should be
threaded, while new comments should be added to the specific, relevant line
of modified code. Although high-level comments about the entire patch set are
allowed, the most useful commments are those that are specifically targeted
to problematic lines of code.

(updatingmergerequest)=

## Updating a Merge Request

As you make changes to your merge request through the review process, you will
either be layering additional patches on top of your current patch set, or you
will be rebasing your patch set. Either approach is acceptable, but remember
that every patch in your patch set must pass continuous integration testing
and adhere to the {ref}`ChecklistForPatches`. Most often, this means that you
should rebase the patch set in your merge request to include the updates.

There are several ways you can rebase the patch set. The following is one
suggested workflow:

# Before making changes, create a new local branch of your merge request. Make

\: your changes on this branch, so that you can always go back to your previous
state. Always keep your original branch until you have pushed a new, clean
version that supersedes it. Even then, you may want to keep your original
branch around in case something went wrong that you did not notice, such as
you accidentally removed a necessary commit while rebasing.

\# Make and commit changes locally until you are satisfied with your code

# Interactively rebase your local branch using `git rebase --interactive`

\: to allow you to select the order of commits and to reword or fixup
commits. One good strategy here is to reorder and fixup commits in one round
and then reword them in a second round, so that you get your commits in
the right order and shape you want before finalizing the patch descriptions.

# Force-push your local branch to your merge request branch on your fork. If

\: something goes wrong, you can revert back to your local version.

## Rebasing a Merge Request

You can follow a similar process as {ref}`UpdatingMergeRequest` to rebase your
merge request branch to an updated target branch, e.g., to pick up changes on
`main`. In this case, after creating a local branch, use `git pull --rebase`
stopping to fix merge conflicts along the way. If it gets out of hand, you can
either `abort` the rebase or you can go back to your original branch.

When merge conflicts are too much to handle doing a rebase, you may instead
like to create a fresh branch from `main` and then use `git-cherry-pick` to
pull commits from your merge request branch on to the head of `main`. If you
are having too much trouble, ask for help.

## Approvers

Merge Request approvals must be from a code owner, identified
by the `CODEOWNERS` file and by sub-groups beneath `Approvers`.
Any one who has requested approval permission can approve a merge request.
Once a patch series is approved for integration into the RTEMS code base it can
be merged by anyone with merge rights, which may include an automated bot.

Approvers are volunteering their time so be polite. If you do not get a
response to a merge request after five working days, please send a reminder
on the merge request or send email to the {r:list}`devel`.

## Why Contribute?

If you are writing a major extension to RTEMS, such as a port
to a new CPU family (processor architecture) or model, a new target board, a
major rewrite of some existing component, or adding some missing functionality,
please keep in mind the importance of keeping other developers informed.
Part of being a good cooperating member of the RTEMS development team is the
responsibility to consider what the other developers need in order
to work effectively.

Nobody likes to do a lot of work and find it was duplicated effort.
So when you work on a major new feature, you should tell
{r:list}`devel` what you are working on, and give
occasional reports of how far you have come and how confident
you are that you will finish the job. This way, other developers
(if they are paying attention) will be aware which projects would
duplicate your effort, and can either join up with you, or at
least avoid spending time on something that will be unnecessary
because of your work. If, for whatever reason, you are not in a
position to publicly discuss your work, please at least privately
let other developers know about it so they can look out for duplicated effort
or possible collaborators.

You should also monitor the {r:list}`users` and {r:list}`devel`
to see if someone else mentions working on a similar
project to yours. If that happens, speak up!

If you are thinking of taking a contract to develop changes
under a temporary delayed-release agreement, please negotiate
the agreement so that you can give progress reports before the
release date, even though you cannot release the code itself.
Also please arrange so that, when the agreed-on date comes,
you can release whatever part of the job you succeeded in doing,
even if you have not succeeded in finishing it.
Someone else may be able to finish the job.

Many people have done RTEMS ports or BSPs on their own, to a wide
variety of processors, without much communication with the RTEMS
development team. However, much of this work has been lost over
time, or have proven very hard to integrate. So, what we are asking
is that, to the maximum extent possible, you communicate with us
as early on and as much as possible.

## Common Questions and Answers

Here are some questions RTEMS porters may have with our answers to
them. While the focus here is on new ports and BSPs, we believe that
the issues are similar for other RTEMS development efforts including
student efforts to implement new algorithmic optimizations.

> Our engineers understand our target environment better than anyone else, and
> we have a tight schedule. Why should we work with the RTEMS developers, when
> we can get the code out faster by whacking it out on our own?

You understand your target environment better than anyone else.
However, the RTEMS developers understand RTEMS better than anyone
else; furthermore, the RTEMS developers tend to have a wide breadth
of experience across a large number of processors, boards, peripherals,
and application domains. It has been our experience that few problems
encountered in embedded systems development are unique to a particular
processor or application. The vast majority of the time an issue that
arises in one project has also shown up in other projects.

The intimate knowledge of RTEMS internals as well as a wide breadth of
embedded systems knowledge means that there is a good chance that at
least one RTEMS developer has already addressed issues you are likely
to face when doing your port, BSP, or application. The developers can
help guide you towards a workable long term solution, possibly saving
you significant time in your development cycle.

If getting the sources into the official RTEMS distributions is one of
your goals, then engaging other RTEMS developers early will also likely
shorten your development time. By interacting as early as possible you
are more likely to write code which can be easily accepted into the official
sources when you are finished. If you wait until you think you are done
to begin interacting with the RTEMS team, you might find that you did
some things wrong and you may have to rewrite parts of your RTEMS port,
which is a waste of your valuable time.

> Why should we care if our port is integrated into the official RTEMS
> sources? We can distribute it ourselves to whoever is interested.

Yes, the RTEMS licenses allows you to do that. But by doing so, you end up
having to maintain that code yourself; this can be a significant
effort over time as the RTEMS sources change rapidly.

You also lose the advantage of wider exposure by including your port
in the official RTEMS sources maintained by the RTEMS Project.
The wider exposure in the RTEMS developer and tester community will
help keep your work up to date with the current sources. You may even
find that volunteers will run the ever-growing test suite on your port
and fix problems during the development cycle -- sometimes without your
intervention.

It has been our experience that integrated ports tend to ultimately
be of better quality and stay up to date from release to release.

> Why should we communicate up front? We are happy to let the RTEMS developers
> integrate our stuff later.

See above. It will save work for you over both the short and the
long term, and it is the right thing to do.

> Aspects of my target environment that my application exploits are still
> under NDA.

Nevertheless, if the target hardware is built of any commercial parts
that are generally available including, but not limited to, the CPU
or peripherals, then that portion of your work is still of general use.
Similarly, if you have written software that adheres to existing API or
interface standards, then that portion is also of general use.
Our experience is that most embedded applications do utilize a custom
mix of hardware and application, but they are built upon layers of hardware
and software components that are in no way unique to the project.

If you are porting to an unreleased CPU family or model, then just
announcing it is important because other RTEMS users may be planning
to use it and some of them may already be trying to port RTEMS on
their own. Your customers might be happier to know that your port
will eventually be available. Also, there is no requirement that RTEMS
include all features or ports at any particular time, so you are encouraged
to submit discrete pieces of functionality in stages.

Assume that your processor has some new functionality or peripherals.
However that functionality is still covered by NDA, but the basic core
architecture is not. It is still to your advantage to go ahead and work
with the developers early to provide a "base port" for the CPU family.
That base port would only use the publicly available specifications
until such time as the NDA is lifted. Once the NDA is lifted you can
work with the developers to provide the code necessary to take
advantage of the new functionality.

Ultimately, cooperating with the free software community as early as
possible helps you by decreasing your development cycle, decreasing
your long term maintenance costs and may help raise interest in your
processor by having a free compiler implementation available to
anyone who wants to take a look.
