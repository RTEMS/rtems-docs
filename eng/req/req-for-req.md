% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019, 2020 embedded brains GmbH & Co. KG

# Requirements for Requirements

(reqengident)=

## Identification

Each requirement shall have a unique identifier (UID). The question is in
which scope should it be unique? Ideally, it should be universally unique.
Therefore all UIDs used to link one specification item to another should use
relative UIDs. This ensures that the RTEMS requirements can be referenced
easily in larger systems though a system-specific prefix. The standard
ECSS-E-ST-10-06C recommends in section 8.2.6 that the identifier should reflect
the type of the requirement and the life profile situation. Other standards
may have other recommendations. To avoid a bias of RTEMS in the direction of
ECSS, this recommendation will not be followed.

The *absolute UID* of a specification item (for example a requirement) is
defined by a leading `/` and the path of directories from the specification
base directory to the file of the item separated by `/` characters and the
file name without the `.yml` extension. For example, a specification item
contained in the file {file}`build/cpukit/librtemscpu.yml` inside a
{file}`spec` directory has the absolute UID of `/build/cpukit/librtemscpu`.

The *relative UID* to a specification item is defined by the path of
directories from the file containing the source specification item to the file
of the destination item separated by `/` characters and the file name of the
destination item without the `.yml` extension. For example the relative UID
from `/build/bsps/sparc/leon3/grp` to `/build/bsps/bspopts` is
`../../bspopts`.

Basically, the valid characters of an UID are determined by the file system
storing the item files. By convention, UID characters shall be restricted to
the following set defined by the regular expression `[a-zA-Z0-9_-]+`. Use
`-` as a separator inside an UID part.

In documents the URL-like prefix `spec:` shall be used to indicated
specification item UIDs.

The UID scheme for RTEMS requirements shall be component based. For example,
the UID `spec:/classic/task/create-err-invaddr` may specify that the
{c:func}`rtems_task_create` directive shall return a status of
`RTEMS_INVALID_ADDRESS` if the `id` parameter is `NULL`.

A initial requirement item hierarchy could be this:

- build (building RTEMS BSPs and libraries)

- acfg (application configuration groups)

  > - opt (application configuration options)

- classic

  > - task
  >
  >   > - create-\* (requirements for {c:func}`rtems_task_create`)
  >   > - delete-\* (requirements for {c:func}`rtems_task_delete`)
  >   > - exit-\* (requirements for {c:func}`rtems_task_exit`)
  >   > - getaff-\* (requirements for {c:func}`rtems_task_get_affinity`)
  >   > - getpri-\* (requirements for {c:func}`rtems_task_get_priority`)
  >   > - getsched-\* (requirements for {c:func}`rtems_task_get_scheduler`)
  >   > - ident-\* (requirements for {c:func}`rtems_task_ident`)
  >   > - issusp-\* (requirements for {c:func}`rtems_task_is_suspended`)
  >   > - iter-\* (requirements for {c:func}`rtems_task_iterate`)
  >   > - mode-\* (requirements for {c:func}`rtems_task_mode`)
  >   > - restart-\* (requirements for {c:func}`rtems_task_restart`)
  >   > - resume\* (requirements for {c:func}`rtems_task_resume`)
  >   > - self\* (requirements for {c:func}`rtems_task_self`)
  >   > - setaff-\* (requirements for {c:func}`rtems_task_set_affinity`)
  >   > - setpri-\* (requirements for {c:func}`rtems_task_set_priority`)
  >   > - setsched\* (requirements for {c:func}`rtems_task_set_scheduler`)
  >   > - start-\* (requirements for {c:func}`rtems_task_start`)
  >   > - susp-\* (requirements for {c:func}`rtems_task_suspend`)
  >   > - wkafter-\* (requirements for {c:func}`rtems_task_wake_after`)
  >   > - wkwhen-\* (requirements for {c:func}`rtems_task_wake_when`)
  >
  > - sema
  >
  >   > - ...

- posix

- ...

A more detailed naming scheme and guidelines should be established. We have to
find the right balance between the length of UIDs and self-descriptive UIDs. A
clear scheme for all Classic API managers may help to keep the UIDs short and
descriptive.

The specification of the validation of requirements should be maintained also
by specification items. For each requirement directory there should be a
validation subdirectory named *test*, e.g. {file}`spec/classic/task/test`. A
test specification directory may contain also validations by analysis, by
inspection, and by design, see {ref}`ReqEngValidation`.

## Level of Requirements

The level of a requirement shall be expressed with one of the verbal forms
listed below and nothing else. The level of requirements are derived from RFC
2119 {cite}`RFC2119` and ECSS-E-ST-10-06C {cite}`ECSS_E_ST_10_06C`.

### Absolute Requirements

Absolute requirements shall be expressed with the verbal form *shall* and no
other terms.

### Absolute Prohibitions

Absolute prohibitions shall be expressed with the verbal form *shall not* and
no other terms.

```{warning}
Absolute prohibitions may be difficult to validate. They should not be
used.
```

### Recommendations

Recommendations shall be expressed with the verbal forms *should* and
*should not* and no other terms with guidance from RFC 2119:

> SHOULD This word, or the adjective "RECOMMENDED", mean that there
> may exist valid reasons in particular circumstances to ignore a
> particular item, but the full implications must be understood and
> carefully weighed before choosing a different course.
>
> SHOULD NOT This phrase, or the phrase "NOT RECOMMENDED" mean that
> there may exist valid reasons in particular circumstances when the
> particular behavior is acceptable or even useful, but the full
> implications should be understood and the case carefully weighed
> before implementing any behavior described with this label.

### Permissions

Permissions shall be expressed with the verbal form *may* and no other terms
with guidance from RFC 2119:

> MAY This word, or the adjective "OPTIONAL", mean that an item is
> truly optional. One vendor may choose to include the item because a
> particular marketplace requires it or because the vendor feels that
> it enhances the product while another vendor may omit the same item.
> An implementation which does not include a particular option MUST be
> prepared to interoperate with another implementation which does
> include the option, though perhaps with reduced functionality. In the
> same vein an implementation which does include a particular option
> MUST be prepared to interoperate with another implementation which
> does not include the option (except, of course, for the feature the
> option provides.)

### Possibilities and Capabilities

Possibilities and capabilities shall be expressed with the verbal form *can*
and no other terms.

(reqengsyntax)=

## Syntax

Use the Easy Approach to Requirements Syntax ({term}`EARS`) to formulate
requirements. A recommended reading list to get familiar with this approach is
{cite}`Mavin:2009:EARS`, {cite}`Mavin:2010:BigEars`,
{cite}`Mavin:2016:LLEARS`, and [Alisair Mavin's web site](https://alistairmavin.com/ears/). The patterns are:

- Ubiquitous

  > The \<system name> shall \<system response>.

- Event-driven

  > **When** \<trigger>, the \<system name> shall \<system response>.

- State-driven

  > **While** \<pre-condition>, the \<system name> shall \<system response>.

- Unwanted behaviour

  > **If** \<trigger>, **then** the \<system name> shall \<system response>.

- Optional

  > **Where** \<feature is included>, the \<system name> shall \<system response>.

- Complex

  > **Where** \<feature 0 is included>, **where** \<feature 1 is included>, ...,
  > **where** \<feature *n* is included>, **while** \<pre-condition 0>, **while**
  > \<pre-condition 1>, ..., **while** \<pre-condition *m*>, **when** \<trigger>,
  > the \<system name> shall \<system response>.
  >
  > **Where** \<feature 0 is included>, **where** \<feature 1 is included>, ...,
  > **where** \<feature *n* is included>, **while** \<pre-condition 0>, **while**
  > \<pre-condition 1>, ..., **while** \<pre-condition *m*>, **if** \<trigger>,
  > **then** the \<system name> shall \<system response>.

The optional pattern should be only used for application configuration
options. The goal is to use the `enabled-by` attribute to enable or disable
requirements based on configuration parameters that define the RTEMS artefacts
used to build an application executable (header files, libraries, linker command
files). Such configuration parameters are for example the architecture, the
platform, CPU port options, and build configuration options (e.g. uniprocessor
vs. SMP).

## Wording Restrictions

To prevent the expression of imprecise requirements, the following terms shall
not be used in requirement formulations:

- "acceptable"
- "adequate"
- "almost always"
- "and/or"
- "appropriate"
- "approximately"
- "as far as possible"
- "as much as practicable"
- "best"
- "best possible"
- "easy"
- "efficient"
- "e.g."
- "enable"
- "enough"
- "etc."
- "few"
- "first rate"
- "flexible"
- "generally"
- "goal"
- "graceful"
- "great"
- "greatest"
- "ideally"
- "i.e."
- "if possible"
- "in most cases"
- "large"
- "many"
- "maximize"
- "minimize"
- "most"
- "multiple"
- "necessary"
- "numerous"
- "optimize"
- "ought to"
- "probably"
- "quick"
- "rapid"
- "reasonably"
- "relevant"
- "robust"
- "satisfactory"
- "several"
- "shall be included but not limited to"
- "simple"
- "small"
- "some"
- "state-of-the-art".
- "sufficient"
- "suitable"
- "support"
- "systematically"
- "transparent"
- "typical"
- "user-friendly"
- "usually"
- "versatile"
- "when necessary"

For guidelines to avoid these terms see Table 11-2, "Some ambiguous terms to
avoid in requirements" in {cite}`Wiegers:2013:SR`. There should be some means
to enforce that these terms are not used, e.g. through a client-side pre-commit
Git hook, a server-side pre-receive Git hook, or some scripts run by special
build commands.

## Separate Requirements

Requirements shall be stated separately. A bad example is:

spec:/classic/task/create
: The task create directive shall evaluate the parameters, allocate a task
  object and initialize it.

To make this a better example, it should be split into separate requirements:

spec:/classic/task/create

: When the task create directive is called with valid parameters and a free
  task object exists, the task create directive shall assign the identifier of
  an initialized task object to the `id` parameter and return the
  `RTEMS_SUCCESSFUL` status.

spec:/classic/task/create-err-toomany

: If no free task objects exists, the task create directive shall return the
  `RTEMS_TOO_MANY` status.

spec:/classic/task/create-err-invaddr

: If the `id` parameter is `NULL`, the task create directive shall return the
  `RTEMS_INVALID_ADDRESS` status.

spec:/classic/task/create-err-invname

: If the `name` parameter is invalid, the task create directive shall
  return the `RTEMS_INVALID_NAME` status.

  ...

## Conflict Free Requirements

Requirements shall not be in conflict with each other inside a specification.
A bad example is:

spec:/classic/sema/mtx-obtain-wait
: When a mutex is not available, the mutex obtain directive shall enqueue the
  calling thread on the wait queue of the mutex.

spec:/classic/sema/mtx-obtain-err-unsat
: If a mutex is not available, the mutex obtain directive shall return the
  RTEMS_UNSATISFIED status.

To resolve this conflict, a condition may be added:

spec:/classic/sema/mtx-obtain-wait
: When a mutex is not available and the RTEMS_WAIT option is set, the mutex
  obtain directive shall enqueue the calling thread on the wait queue of the
  mutex.

spec:/classic/sema/mtx-obtain-err-unsat
: If a mutex is not available, when the RTEMS_WAIT option is not set, the
  mutex obtain directive shall return the RTEMS_UNSATISFIED status.

## Use of Project-Specific Terms and Abbreviations

All project-specific terms and abbreviations used to formulate requirements
shall be defined in the project glossary.

(reqengjustreq)=

## Justification of Requirements

Each requirement shall have a rationale or justification recorded in a
dedicated section of the requirement file. See `rationale` attribute for
{ref}`ReqEngSpecificationItems`.

(reqengvalidation)=

## Requirement Validation

The validation of each {ref}`SpecTypeRequirementItemType` item shall be
accomplished by one or more specification items of the types
{ref}`SpecTypeTestCaseItemType` or {ref}`SpecTypeRequirementValidationItemType`
through a link from the validation item to the requirement item with the
{ref}`SpecTypeRequirementValidationLinkRole`.

Validation by test is strongly recommended. The choice of any other validation
method shall be strongly justified. The requirements author is obligated to
provide the means to validate the requirement with detailed instructions.

(reqengresandperf)=

## Resources and Performance

Normally, resource and performance requirements are formulated like this:

- The resource U shall need less than V storage units.
- The operation Y shall complete within X time units.

Such statements are difficult to make for a software product like RTEMS which
runs on many different target platforms in various configurations. So, the
performance requirements of RTEMS shall be stated in terms of benchmarks. The
benchmarks are run on the project-specific target platform and configuration.
The results obtained by the benchmark runs are reported in a human readable
presentation. The application designer can then use the benchmark results to
determine if its system performance requirements are met. The benchmarks shall
be executed under different environment conditions, e.g. varying cache states
(dirty, empty, valid) and system bus load generated by other processors. The
application designer shall have the ability to add additional environment
conditions, e.g. system bus load by DMA engines or different system bus
arbitration schemes.

To catch resource and performance regressions via test suite runs there shall be
a means to specify threshold values for the measured quantities. The threshold
values should be provided for each validation platform. How this can be done
and if the threshold values are maintained by the RTEMS Project is subject to
discussion.
