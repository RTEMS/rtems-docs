(PatchReviewProcess)=

## Merge Request Review Process

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

Threads usually should be resolved by the first author of the thread, i.e., the
reviewer who wrote the first comment. In particular, code submitters should not
resolve the threads but should reply to the thread to indicate that they think
they have addressed the concern.

### Approvers

Merge Request approvals must be from a code owner, identified
by the `CODEOWNERS` file and by sub-groups beneath `Approvers`.
Any one who has requested approval permission can approve a merge request.
Once a patch series is approved for integration into the RTEMS code base it can
be merged by anyone with merge rights, which may include an automated bot.

Approvers are volunteering their time so be polite. If you do not get a
response to a merge request after five working days, please send a reminder
on the merge request or send email to the {r:list}`devel`.
