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

(ChecklistForPatches)=

### Checklist for Merge Requests

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

(UpdatingMergeRequest)=

### Updating a Merge Request

As you make changes to your merge request through the review process, you will
either be layering additional patches on top of your current patch set, or you
will be rebasing your patch set. Either approach is acceptable, but remember
that every patch in your patch set must pass continuous integration testing
and adhere to the {ref}`ChecklistForPatches`. Most often, this means that you
should rebase the patch set in your merge request to include the updates.

There are several ways you can rebase the patch set. The following is one
suggested workflow:

- Before making changes, create a new local branch of your merge request. Make
  your changes on this branch, so that you can always go back to your previous
  state. Always keep your original branch until you have pushed a new, clean
  version that supersedes it. Even then, you may want to keep your original
  branch around in case something went wrong that you did not notice, such as
  you accidentally removed a necessary commit while rebasing.

- Make and commit changes locally until you are satisfied with your code

- Interactively rebase your local branch using `git rebase --interactive`
  to allow you to select the order of commits and to reword or fixup
  commits. One good strategy here is to reorder and fixup commits in one round
  and then reword them in a second round, so that you get your commits in
  the right order and shape you want before finalizing the patch descriptions.

- Force-push your local branch to your merge request branch on your fork. If
  something goes wrong, you can revert back to your local version.

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
