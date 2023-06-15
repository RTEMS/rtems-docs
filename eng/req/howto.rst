.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2023 embedded brains GmbH & Co. KG

How-To
======

Getting Started
---------------

The RTEMS specification items and qualification tools are work in progress.  The
first step to work with the RTEMS specification and the corresponding tools is a
clone of the following repository:

.. code-block:: none

    git clone git://git.rtems.org/rtems-central.git
    git submodule init
    git submodule update

The tools need a virtual Python 3 environment. To set it up use:

.. code-block:: none

    cd rtems-central
    make env

Each time you want to use one of the tools, you have to activate the
environment in your shell:

.. code-block:: none

    cd rtems-central
    . env/bin/activate

View the Specification Graph
----------------------------

The specification items form directed graphs through :ref:`SpecTypeLink`
attributes.  Each link has a role.  For a particular view only specific roles
may be of interest.  For example, the requirements specification of RTEMS
starts with the ``spec:/req/root`` specification item.  It should form a tree
(connected graph without cycles).  A text representation of the tree can be
printed with the ``./specview.py`` script:

.. code-block:: none

    cd rtems-central
    . env/bin/activate
    ./specview.py

This gives the following example output (shortened):

.. code-block:: none

    /req/root (type=requirement/non-functional/design)
      /bsp/if/group (type=requirement/non-functional/design-group, role=requirement-refinement)
        /bsp/if/acfg-idle-task-body (type=interface/unspecified-define, role=interface-ingroup)
          /bsp/sparc/leon3/req/idle-task-body (type=requirement/functional/function, role=interface-function)
            /bsp/sparc/leon3/req/idle-task-power-down (type=requirement/functional/function, role=requirement-refinement)
              /bsp/sparc/leon3/val/errata-gr712rc-08 (type=validation, role=validation)
            /bsp/sparc/leon3/req/idle-task-power-down-errata (type=requirement/functional/function, role=requirement-refinement)
              /bsp/sparc/leon3/val/errata-gr712rc-08 (type=validation, role=validation)

The actual specification graph depends on build configuration options which
enable or disable specification items.  The ``--enabled`` command line option
may be used to specify the build configuration options, for example
``--enabled=sparc,bsps/sparc/leon3,sparc/gr740,RTEMS_SMP,RTEMS_QUAL``.

The ``./specview.py`` script can display other views of the specification
through the ``--filter`` command line option.  Transition maps of
:ref:`SpecTypeActionRequirementItemType` items can be printed using the
``--filter=action-table`` or ``--filter=action-list`` filters.  For example,
``./specview.py --filter=action-table /rtems/timer/req/create`` prints
something like this:

.. code-block:: none

    .. table::
        :class: longtable

        ===== ========== ======= ===== ==== ======= ======= =====
        Entry Descriptor Name    Id    Free Status  Name    IdVar
        ===== ========== ======= ===== ==== ======= ======= =====
        0     0          Valid   Valid Yes  Ok      Valid   Set
        1     0          Valid   Valid No   TooMany Invalid Nop
        2     0          Valid   Null  Yes  InvAddr Invalid Nop
        3     0          Valid   Null  No   InvAddr Invalid Nop
        4     0          Invalid Valid Yes  InvName Invalid Nop
        5     0          Invalid Valid No   InvName Invalid Nop
        6     0          Invalid Null  Yes  InvName Invalid Nop
        7     0          Invalid Null  No   InvName Invalid Nop
        ===== ========== ======= ===== ==== ======= ======= =====

For example, ``./specview.py --filter=action-list /rtems/timer/req/create``
prints something like this:

.. code-block:: none

    Status = Ok, Name = Valid, IdVar = Set

        * Name = Valid, Id = Valid, Free = Yes

    Status = TooMany, Name = Invalid, IdVar = Nop

        * Name = Valid, Id = Valid, Free = No

    Status = InvAddr, Name = Invalid, IdVar = Nop

        * Name = Valid, Id = Null, Free = { Yes, No }

    Status = InvName, Name = Invalid, IdVar = Nop

        * Name = Invalid, Id = { Valid, Null }, Free = { Yes, No }

The view above yields for each variation of post-condition states the list of
associated pre-condition state variations.

Generate Files from Specification Items
---------------------------------------

The ``./spec2modules.py`` script generates program and documentation files in
:file:`modules/rtems` and :file:`modules/rtems-docs` using the specification
items as input.  The script should be invoked whenever a specification item was
modified.  After running the script, go into the subdirectories and create
corresponding patch sets.  For these patch sets, the normal patch review
process applies, see *Support and Contributing* chapter of the *RTEMS User
Manual*.

Application Configuration Options
---------------------------------

The application configuration options and groups are maintained by
specification items in the directory :file:`spec/acfg/if`.  Application
configuration options are grouped by
:ref:`SpecTypeApplicationConfigurationGroupItemType` items which should be
stored in files using the :file:`spec/acfg/if/group-*.yml` pattern.  Each
application configuration option shall link to exactly one group item with the
:ref:`SpecTypeInterfaceGroupMembershipLinkRole`.  There are four
application option item types available which cover all existing options:

* The *feature enable options* let the application enable a feature option.  If
  the option is not defined, then the feature is simply not available or
  active.  There should be no feature-specific code linked to the application
  if the option is not defined.  Examples are options which enable a device
  driver like ``CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER``.  These options are
  specified by
  :ref:`SpecTypeApplicationConfigurationFeatureEnableOptionItemType` items.

* The *feature options* let the application enable a specific feature option.
  If the option is not defined, then a default feature option is used.
  Regardless whether the option is defined or not defined, feature-specific
  code may be linked to the application.  Examples are options which disable a
  feature if the option is defined such as
  ``CONFIGURE_APPLICATION_DISABLE_FILESYSTEM`` and options which provide a stub
  implementation of a feature by default and a full implementation if the
  option is defined such as ``CONFIGURE_IMFS_ENABLE_MKFIFO``.  These options
  are specified by :ref:`SpecTypeApplicationConfigurationFeatureOptionItemType`
  items.

* The *integer value options* let the application define a specific value for a
  system parameter.  If the option is not defined, then a default value is used
  for the system parameter.  Examples are options which define the maximum
  count of objects available for application use such as
  ``CONFIGURE_MAXIMUM_TASKS``.  These options are specified by
  :ref:`SpecTypeApplicationConfigurationValueOptionItemType` items.

* The *initializer options* let the application define a specific initializer
  for a system parameter.  If the option is not defined, then a default setting
  is used for the system parameter.  An example option of this type is
  ``CONFIGURE_INITIAL_EXTENSIONS``.  These options are specified by
  :ref:`SpecTypeApplicationConfigurationValueOptionItemType` items.

Sphinx documentation sources and header files with Doxygen markup are generated
from the specification items.  The descriptions in the items shall use a
restricted Sphinx formatting.  Emphasis via one asterisk ("*"), strong emphasis
via two asterisk ("**"), code samples via blockquotes ("``"), code blocks ("..
code-block:: c") and lists are allowed.  References to interface items are also
allowed, for example "${appl-needs-clock-driver:/name}" and
"${/rtems/task/if/create:/name}".  References to other parts of the
documentation are possible, however, they have to be provided by
:file:`spec:/doc/if/*` items.

Modify an Existing Group
^^^^^^^^^^^^^^^^^^^^^^^^

Search for the group by its section header and edit the specification item
file.  For example:

.. code-block:: none

    $ grep -rl "name: General System Configuration" spec/acfg/if
    spec/acfg/if/group-general.yml
    $ vi spec/acfg/if/group-general.yml

Modify an Existing Option
^^^^^^^^^^^^^^^^^^^^^^^^^

Search for the option by its C preprocessor define name and edit the
specification item file.  For example:

.. code-block:: none

    $ grep -rl CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER spec/acfg/if
    spec/acfg/if/appl-needs-clock-driver.yml
    $ vi spec/acfg/if/appl-needs-clock-driver.yml

Add a New Group
^^^^^^^^^^^^^^^

Let ``new`` be the UID name part of the new group.  Create the file
:file:`spec/acfg/if/group-new.yml` and provide all attributes for an
:ref:`SpecTypeApplicationConfigurationGroupItemType` item.  For example:

.. code-block:: none

    $ vi spec/acfg/if/group-new.yml

Add a New Option
^^^^^^^^^^^^^^^^

Let ``my-new-option`` be the UID name of the option.  Create the file
:file:`if/acfg/my-new-option.yml` and provide all attributes for an appropriate
refinement of :ref:`SpecTypeApplicationConfigurationOptionItemType`.  For
example:

.. code-block:: none

    $ vi spec/acfg/if/my-new-option.yml

Generate Content after Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you are done with the modifications of an existing item or the creation of
a new item, the changes need to be propagated to generated source files.  This
is done by the :file:`spec2modules.py` script.  Before you call this script,
make sure the Git submodules are up-to-date.

.. code-block:: none

    $ ./spec2modules.py

The script modifies or creates source files in :file:`modules/rtems` and
:file:`modules/rtems-docs`.  Create patch sets for these changes just as if
these were work done by a human and follow the normal patch review process
described in the *RTEMS User Manual*.  When the changes are integrated, update
the Git submodules and check in the changed items.

Glossary Specification
----------------------

The glossary of terms for the RTEMS Project is defined by
:ref:`SpecTypeGlossaryTermItemType` items in the :file:`spec/glossary`
directory.  For a new glossary term add a glossary item to this directory.  As
the file name use the term in lower case with all white space and special
characters removed or replaced by alphanumeric characters, for example
:file:`spec/glossary/magicpower.yml` for the term `magic power`.

Use ``${uid:/attribute}`` substitutions to reference other parts of the
specification.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH & Co. KG
    enabled-by: true
    glossary-type: term
    links:
    - role: glossary-member
      uid: ../glossary-general
    term: magic power
    text: |
      Magic power enables a caller to create magic objects using a
      ${magicwand:/term}.
    type: glossary

Define acronyms with the phrase `This term is an acronym for *.` in the
``text`` attribute:

.. code-block:: yaml

    ...
    term: MP
    ...
    text: |
      This term is an acronym for Magic Power.
    ...

Once you are done with the glossary items, run the script
:file:`spec2modules.py` to generate the derived documentation content.  Send
patches for the generated documentation and the specification to the
:r:list:`devel` and follow the normal patch review process.

Interface Specification
-----------------------

.. _ReqEngAddAPIHeaderFile:

Specify an API Header File
^^^^^^^^^^^^^^^^^^^^^^^^^^

The RTEMS :term:`API` header files are specified under ``spec:/rtems/*/if``.
Create a subdirectory with a corresponding name for the API, for example in
:file:`spec/rtems/foo/if` for the `foo` API.  In this new subdirectory place an
:ref:`SpecTypeInterfaceHeaderFileItemType` item named :file:`header.yml`
(:file:`spec/rtems/foo/if/header.yml`) and populate it with the required
attributes.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH & Co. KG
    enabled-by: true
    interface-type: header-file
    links:
    - role: interface-placement
      uid: /if/domain
    - role: interface-ingroup
      uid: ../req/group
    path: rtems/rtems/foo.h
    prefix: cpukit/include
    type: interface

Specify an API Element
^^^^^^^^^^^^^^^^^^^^^^

Figure out the corresponding header file item.  If it does not exist, see
:ref:`ReqEngAddAPIHeaderFile`.  Place a specialization of an
:ref:`SpecTypeInterfaceItemType` item into the directory of the header file
item, for example :file:`spec/rtems/foo/if/bar.yml` for the :c:func:`bar`
function.  Add the required attributes for the new interface item.  Do not hard
code interface names which are used to define the new interface.  Use
``${uid-of-interface-item:/name}`` instead.  If the referenced interface is
specified in the same directory, then use a relative UID.  Using interface
references creates implicit dependencies and helps the header file generator to
resolve the interface dependencies and header file includes for you.  Use
:ref:`SpecTypeInterfaceUnspecifiedItemType` items for interface dependencies to
other domains such as the C language, the compiler, the implementation, or
user-provided defines.  To avoid cyclic dependencies between types you may use
an :ref:`SpecTypeInterfaceForwardDeclarationItemType` item.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    brief: Tries to create a magic object and returns it.
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH & Co. KG
    definition:
      default:
        body: null
        params:
        - ${magic-wand:/name} ${.:/params[0]/name}
        return: ${magic-type:/name} *
      variants: []
    description: |
      The magic object is created out of nothing with the help of a magic wand.
    enabled-by: true
    interface-type: function
    links:
    - role: interface-placement
      uid: header
    - role: interface-ingroup
      uid: /groups/api/classic/foo
    name: bar
    notes: null
    params:
    - description: is the magic wand.
      dir: null
      name: magic_wand
    return:
      return: Otherwise, the magic object is returned.
      return-values:
      - description: The caller did not have enough magic power.
        value: ${/c/if/null}
    type: interface

Requirements Depending on Build Configuration Options
-----------------------------------------------------

Use the ``enabled-by`` attribute of items or parts of an item to make it
dependent on build configuration options such as :c:data:`RTEMS_SMP` or
architecture-specific options such as
:c:data:`CPU_ENABLE_ROBUST_THREAD_DISPATCH`, see
:ref:`SpecTypeEnabledByExpression`.  With this attribute the specification can
be customized at the level of an item or parts of an item.  If the
``enabled-by`` attribute evaluates to false for a particular configuration,
then the item or the associated part is disabled in the specification.  The
``enabled-by`` attribute acts as a formalized *where* clause, see
:ref:`recommended requirements syntax <ReqEngSyntax>`.

Please have a look at the following example which specifies the transition map
of :c:func:`rtems_signal_catch`:

.. code-block:: yaml

    transition-map:
    - enabled-by: true
      post-conditions:
        Status: Ok
        ASRInfo:
        - if:
            pre-conditions:
              Handler: Valid
          then: New
        - else: Inactive
      pre-conditions:
        Pending: all
        Handler: all
        Preempt: all
        Timeslice: all
        ASR: all
        IntLvl: all
    - enabled-by: CPU_ENABLE_ROBUST_THREAD_DISPATCH
      post-conditions:
        Status: NotImplIntLvl
        ASRInfo: NopIntLvl
      pre-conditions:
        Pending: all
        Handler:
        - Valid
        Preempt: all
        Timeslice: all
        ASR: all
        IntLvl:
        - Positive
    - enabled-by: RTEMS_SMP
      post-conditions:
        Status: NotImplNoPreempt
        ASRInfo: NopNoPreempt
      pre-conditions:
        Pending: all
        Handler:
        - Valid
        Preempt:
        - 'No'
        Timeslice: all
        ASR: all
        IntLvl: all

Requirements Depending on Application Configuration Options
-----------------------------------------------------------

Requirements which depend on application configuration options such as
:c:data:`CONFIGURE_MAXIMUM_PROCESSORS` should be written in the following
:ref:`syntax <ReqEngSyntax>`:

    **Where** <feature is included>, the <system name> shall <system response>.

Use these clauses with care.  Make sure all feature combinations are covered.
Using a truth table may help.  If a requirement depends on multiple features,
use:

    **Where** <feature 0>, **where** <feature 1>, **where** <feature ...>, the
    <system name> shall <system response>.

For application configuration options, use the clauses like this:

:c:data:`CONFIGURE_MAXIMUM_PROCESSORS` equal to one

   **Where** the system was configured with a processor maximum of exactly
   one, ...

:c:data:`CONFIGURE_MAXIMUM_PROCESSORS` greater than one

   **Where** the system was configured with a processor maximum greater than
   one, ...

Please have a look at the following example used to specify
:c:func:`rtems_signal_catch`.  The example is a post-condition state
specification of an action requirement, so there is an implicit set of
pre-conditions and the trigger:

   **While** <pre-condition(s)>, **when** rtems_signal_catch() is called, ...

The *where* clauses should be mentally placed before the *while* clauses.

.. code-block:: yaml

    post-conditions:
    - name: ASRInfo
      states:
      - name: NopNoPreempt
        test-code: |
          if ( rtems_configuration_get_maximum_processors() > 1 ) {
            CheckNoASRChange( ctx );
          } else {
            CheckNewASRSettings( ctx );
          }
        text: |
          Where the scheduler does not support the no-preempt mode, the ASR
          information of the caller of ${../if/catch:/name} shall not be
          changed by the ${../if/catch:/name} call.

          Where the scheduler does support the no-preempt mode, the ASR
          processing for the caller of ${../if/catch:/name} shall be done using
          the handler specified by ${../if/catch:/params[0]/name} in the mode
          specified by ${../if/catch:/params[1]/name}.

Action Requirements
-------------------

:ref:`SpecTypeActionRequirementItemType` items may be used to specify and
validate directive calls.  They are a generator for event-driven requirements.
Event-driven requirements should be written in the following :ref:`syntax
<ReqEngSyntax>`:

    **While** <pre-condition 0>, **while** <pre-condition 1>, ..., **while**
    <pre-condition *n*>, **when** <trigger>, the <system name> shall <system
    response>.

The list of *while* <pre-condition *i*> clauses for *i* from 1 to *n* in the
EARS notation is generated by *n* pre-condition states in the action
requirement item, see the ``pre-condition`` attribute in the
:ref:`SpecTypeActionRequirementItemType`.

The <trigger> in the EARS notation is defined for an action requirement item by
the link to an :ref:`SpecTypeInterfaceFunctionItemType` or an
:ref:`SpecTypeInterfaceMacroItemType` item using the
:ref:`SpecTypeInterfaceFunctionLinkRole`.  The code provided by the
``test-action`` attribute defines the action code which should invoke the
trigger directive in a particular set of pre-condition states.

Each post-condition state of the action requirement item generates a <system
name> shall <system response> clause in the EARS notation, see the
``post-condition`` attribute in the :ref:`SpecTypeActionRequirementItemType`.

Each entry in the transition map is an event-driven requirement composed of the
pre-condition states, the trigger defined by the link to a directive, and the
post-condition states.  The transition map is defined by a list of
:ref:`SpecTypeActionRequirementTransition` descriptors.

Use ``CamelCase`` for the pre-condition names, post-condition names, and state
names in action requirement items.  The more conditions a directive has, the
shorter should be the names.  The transition map may be documented as a table
and more conditions need more table columns.  Use item attribute references in
the ``text`` attributes.  This allows context-sensitive substitutions.

Example
^^^^^^^

Lets have a look at an example of an action requirement item.  We would like to
specify and validate the behaviour of the

.. code-block:: c

    rtems_status_code rtems_timer_create( rtems_name name, rtems_id *id );

directive which is particularly simple.  For a more complex example see the
specification of :c:func:`rtems_signal_catch` or :c:func:`rtems_signal_send` in
``spec:/rtems/signal/req/catch`` or ``spec:/rtems/signal/send`` respectively.

The event triggers are calls to :c:func:`rtems_timer_create`.  Firstly, we need
the list of pre-conditions relevant to this directive.  Good candidates are the
directive parameters, this gives us the ``Name`` and ``Id`` conditions.  A
system condition is if an inactive timer object is available so that we can
create a timer, this gives us the ``Free`` condition.  Secondly, we need the
list of post-conditions relevant to this directive.  They are the return status
of the directive, ``Status``, the validity of a unique object name, ``Name``,
and the value of an object identifier variable, ``IdVar``.  Each condition has
a set of states, see the YAML data below for the details.  The specified
conditions and states yield the following transition map:

.. table::
    :class: longtable

    ===== ========== ======= ===== ==== ======= ======= =====
    Entry Descriptor Name    Id    Free Status  Name    IdVar
    ===== ========== ======= ===== ==== ======= ======= =====
    0     0          Valid   Valid Yes  Ok      Valid   Set
    1     0          Valid   Valid No   TooMany Invalid Nop
    2     0          Valid   Null  Yes  InvAddr Invalid Nop
    3     0          Valid   Null  No   InvAddr Invalid Nop
    4     0          Invalid Valid Yes  InvName Invalid Nop
    5     0          Invalid Valid No   InvName Invalid Nop
    6     0          Invalid Null  Yes  InvName Invalid Nop
    7     0          Invalid Null  No   InvName Invalid Nop
    ===== ========== ======= ===== ==== ======= ======= =====

Not all transition maps are that small, the transition map of
:c:func:`rtems_task_mode` has more than 8000 entries.  We can construct
requirements from the clauses of the entries.  For example, the three
requirements of entry 0 (Name=Valid, Id=Valid, and Free=Yes results in
Status=Ok, Name=Valid, and IdVar=Set) are:

    While the ``name`` parameter is valid, while the ``id`` parameter
    references an object of type rtems_id, while the system has at least one
    inactive timer object available, when rtems_timer_create() is called, the
    return status of rtems_timer_create() shall be RTEMS_SUCCESSFUL.

    While the ``name`` parameter is valid, while the ``id`` parameter
    references an object of type rtems_id, while the system has at least one
    inactive timer object available, when rtems_timer_create() is called, the
    unique object name shall identify the timer created by the
    rtems_timer_create() call.

    While the ``name`` parameter is valid, while the ``id`` parameter
    references an object of type rtems_id, while the system has at least one
    inactive timer object available, when rtems_timer_create() is called, the
    value of the object referenced by the ``id`` parameter shall be set to the
    object identifier of the created timer after the return of the
    rtems_timer_create() call.

Now we will have a look at the specification item line by line.  The top-level
attributes are normally in alphabetical order in an item file.  For this
presentation we use a structured order.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2021 embedded brains GmbH & Co. KG
    enabled-by: true
    functional-type: action
    rationale: null
    references: []
    requirement-type: functional

The specification items need a bit of boilerplate to tell you what they are,
who wrote them, and what their license is.

.. code-block:: yaml

    text: ${.:text-template}

Each requirement item needs a ``text`` attribute.  For the action requirements,
we do not have a single requirement. There is just a template indicator and no
plain text.  Several event-driven requirements are defined by the
pre-conditions, the trigger, and the post-conditions.

.. code-block:: yaml

    pre-conditions:
    - name: Name
      states:
      - name: Valid
        test-code: |
          ctx->name = NAME;
        text: |
          While the ${../if/create:/params[0]/name} parameter is valid.
      - name: Invalid
        test-code: |
          ctx->name = 0;
        text: |
          While the ${../if/create:/params[0]/name} parameter is invalid.
      test-epilogue: null
      test-prologue: null
    - name: Id
      states:
      - name: Valid
        test-code: |
          ctx->id = &ctx->id_value;
        text: |
          While the ${../if/create:/params[1]/name} parameter references an object
          of type ${../../type/if/id:/name}.
      - name: 'Null'
        test-code: |
          ctx->id = NULL;
        text: |
          While the ${../if/create:/params[1]/name} parameter is
          ${/c/if/null:/name}.
      test-epilogue: null
      test-prologue: null
    - name: Free
      states:
      - name: 'Yes'
        test-code: |
          /* Ensured by the test suite configuration */
        text: |
          While the system has at least one inactive timer object available.
      - name: 'No'
        test-code: |
          ctx->seized_objects = T_seize_objects( Create, NULL );
        text: |
          While the system has no inactive timer object available.
      test-epilogue: null
      test-prologue: null

This list defines the pre-conditions.  Each pre-condition has a list of states
and corresponding validation test code.

.. code-block:: yaml

    links:
    - role: interface-function
      uid: ../if/create
    test-action: |
      ctx->status = rtems_timer_create( ctx->name, ctx->id );

The link to the :c:func:`rtems_timer_create` interface specification item with
the ``interface-function`` link role defines the trigger.  The ``test-action``
defines the how the triggering directive is invoked for the validation test
depending on the pre-condition states.  The code is not always as simple as in
this example.  The validation test is defined in this item along with the
specification.

.. code-block:: yaml

    post-conditions:
    - name: Status
      states:
      - name: Ok
        test-code: |
          T_rsc_success( ctx->status );
        text: |
          The return status of ${../if/create:/name} shall be
          ${../../status/if/successful:/name}.
      - name: InvName
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_NAME );
        text: |
          The return status of ${../if/create:/name} shall be
          ${../../status/if/invalid-name:/name}.
      - name: InvAddr
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_ADDRESS );
        text: |
          The return status of ${../if/create:/name} shall be
          ${../../status/if/invalid-address:/name}.
      - name: TooMany
        test-code: |
          T_rsc( ctx->status, RTEMS_TOO_MANY );
        text: |
          The return status of ${../if/create:/name} shall be
          ${../../status/if/too-many:/name}.
      test-epilogue: null
      test-prologue: null
    - name: Name
      states:
      - name: Valid
        test-code: |
          id = 0;
          sc = rtems_timer_ident( NAME, &id );
          T_rsc_success( sc );
          T_eq_u32( id, ctx->id_value );
        text: |
          The unique object name shall identify the timer created by the
          ${../if/create:/name} call.
      - name: Invalid
        test-code: |
          sc = rtems_timer_ident( NAME, &id );
          T_rsc( sc, RTEMS_INVALID_NAME );
        text: |
          The unique object name shall not identify a timer.
      test-epilogue: null
      test-prologue: |
        rtems_status_code sc;
        rtems_id          id;
    - name: IdVar
      states:
      - name: Set
        test-code: |
          T_eq_ptr( ctx->id, &ctx->id_value );
          T_ne_u32( ctx->id_value, INVALID_ID );
        text: |
          The value of the object referenced by the ${../if/create:/params[1]/name}
          parameter shall be set to the object identifier of the created timer
          after the return of the ${../if/create:/name} call.
      - name: Nop
        test-code: |
          T_eq_u32( ctx->id_value, INVALID_ID );
        text: |
          Objects referenced by the ${../if/create:/params[1]/name} parameter in
          past calls to ${../if/create:/name} shall not be accessed by the
          ${../if/create:/name} call.
      test-epilogue: null
      test-prologue: null

This list defines the post-conditions.  Each post-condition has a list of
states and corresponding validation test code.

.. code-block:: yaml

    skip-reasons: {}
    transition-map:
    - enabled-by: true
      post-conditions:
        Status:
        - if:
            pre-conditions:
              Name: Invalid
          then: InvName
        - if:
            pre-conditions:
              Id: 'Null'
          then: InvAddr
        - if:
            pre-conditions:
              Free: 'No'
          then: TooMany
        - else: Ok
        Name:
        - if:
            post-conditions:
              Status: Ok
          then: Valid
        - else: Invalid
        IdVar:
        - if:
            post-conditions:
              Status: Ok
          then: Set
        - else: Nop
      pre-conditions:
        Name: all
        Id: all
        Free: all
    type: requirement

This list of transition descriptors defines the transition map.  For the
post-conditions, you can use expressions to ease the specification, see
:ref:`SpecTypeActionRequirementTransitionPostConditionState`.  The
``skip-reasons`` can be used to skip entire entries in the transition map, see
:ref:`SpecTypeActionRequirementSkipReasons`.

.. code-block:: yaml

    test-brief: null
    test-description: null

The item contains the validation test code.  The validation test in general can
be described by these two attributes.

.. code-block:: yaml

    test-target: testsuites/validation/tc-timer-create.c

This is the target file for the generated validation test code.  Make sure this
file is included in the build specification, otherwise the test code generation
will fail.

.. code-block:: yaml

    test-includes:
    - rtems.h
    - string.h
    test-local-includes: []

You can specify a list of includes for the validation test.

.. code-block:: yaml

    test-header: null

A test header may be used to create a parameterized validation test, see
:ref:`SpecTypeTestHeader`.  This is an advanced topic, see the specification of
:c:func:`rtems_task_ident` for an example.

.. code-block:: yaml

    test-context-support: null
    test-context:
    - brief: |
        This member is used by the T_seize_objects() and T_surrender_objects()
        support functions.
      description: null
      member: |
        void *seized_objects
    - brief: |
        This member may contain the object identifier returned by
        rtems_timer_create().
      description: null
      member: |
        rtems_id id_value
    - brief: |
        This member specifies the ${../if/create:/params[0]/name} parameter for the
        action.
      description: null
      member: |
        rtems_name name
    - brief: |
        This member specifies the ${../if/create:/params[1]/name} parameter for the
        action.
      description: null
      member: |
        rtems_id *id
    - brief: |
        This member contains the return status of the action.
      description: null
      member: |
        rtems_status_code status

You can specify a list of validation test context members which can be used to
maintain the state of the validation test.  The context is available through an
implicit ``ctx`` variable in all code blocks except the support blocks.  The
context support code can be used to define test-specific types used by context
members.  Do not use global variables.

.. code-block:: yaml

    test-support: |
      #define NAME rtems_build_name( 'T', 'E', 'S', 'T' )

      #define INVALID_ID 0xffffffff

      static rtems_status_code Create( void *arg, uint32_t *id )
      {
        return rtems_timer_create( rtems_build_name( 'S', 'I', 'Z', 'E' ), id );
      }

The support code block can be used to provide functions, data structures, and
constants for the validation test.

.. code-block:: yaml

    test-prepare: null
    test-cleanup: |
      if ( ctx->id_value != INVALID_ID ) {
        rtems_status_code sc;

        sc = rtems_timer_delete( ctx->id_value );
        T_rsc_success( sc );

        ctx->id_value = INVALID_ID;
      }

      T_surrender_objects( &ctx->seized_objects, rtems_timer_delete );

The validation test basically executes a couple of nested for loops to iterate
over each pre-condition and each state of the pre-conditions.  These two
optional code blocks can be used to prepare the pre-condition state
preparations and clean up after the post-condition checks in each loop
iteration.

.. code-block:: yaml

    test-setup:
      brief: null
      code: |
        memset( ctx, 0, sizeof( *ctx ) );
        ctx->id_value = INVALID_ID;
      description: null
    test-stop: null
    test-teardown: null

These optional code blocks correspond to test fixture methods, see
:ref:`RTEMSTestFrameworkFixture`.

Pre-Condition Templates
^^^^^^^^^^^^^^^^^^^^^^^

Specify all directive parameters as separate pre-conditions.  Use the following
syntax for directive object identifier parameters:

.. code-block:: yaml

    - name: Id
      states:
      - name: NoObj
        test-code: |
          ctx->id = 0xffffffff;
        text: |
          While the ${../if/directive:/params[0]/name} parameter is not
          associated with a thing.
      - name: ClassA
        test-code: |
          ctx->id = ctx->class_a_id;
        text: |
          While the ${../if/directive:/params[0]/name} parameter is associated
          with a class A thing.
      - name: ClassB
        test-code: |
          ctx->id = ctx->class_b_id;
        text: |
          While the ${../if/directive:/params[0]/name} parameter is associated
          with a class B thing.
      test-epilogue: null
      test-prologue: null

Do not add specifications for invalid pointers.  In general, there are a lot of
invalid pointers and the use of an invalid pointer is in almost all cases
undefined behaviour in RTEMS.  There may be specifications for special cases
which deal with some very specific invalid pointers such as the :c:data:`NULL`
pointer or pointers which do not satisfy a range or boundary condition.  Use
the following syntax for directive pointer parameters:

.. code-block:: yaml

    - name: Id
      states:
      - name: Valid
        test-code: |
          ctx->id = &ctx->id_value;
        text: |
          While the ${../if/directive:/params[3]/name} parameter references an
          object of type ${../../type/if/id:/name}.
      - name: 'Null'
        test-code: |
          ctx->id = NULL;
        text: |
          While the ${../if/directive:/params[3]/name} parameter is
          ${/c/if/null:/name}.
      test-epilogue: null
      test-prologue: null

Use the following syntax for other directive parameters:

.. code-block:: yaml

    - name: Name
      states:
      - name: Valid
        test-code: |
          ctx->name = NAME;
        text: |
          While the ${../if/directive:/params[0]/name} parameter is valid.
      - name: Invalid
        test-code: |
          ctx->name = 0;
        text: |
          While the ${../if/directive:/params[0]/name} parameter is invalid.
      test-epilogue: null
      test-prologue: null

Post-Condition Templates
^^^^^^^^^^^^^^^^^^^^^^^^

Do not mix different things into one post-condition.  If you write multiple
sentences to describe what happened, then think about splitting up the
post-condition.  Keep the post-condition simple and focus on one testable
aspect which may be changed by a directive call.

For directives returning an :c:type:`rtems_status_code` use the following
post-condition states.  Specify only status codes which may be returned by the
directive.  Use it as the first post-condition.  The first state shall be
``Ok``.  The other states shall be listed in the order in which they can occur.

.. code-block:: yaml

    - name: Status
      states:
      - name: Ok
        test-code: |
          T_rsc_success( ctx->status );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/successful:/name}.
      - name: IncStat
        test-code: |
          T_rsc( ctx->status, RTEMS_INCORRECT_STATE );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/incorrect-state:/name}.
      - name: InvAddr
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_ADDRESS );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/invalid-address:/name}.
      - name: InvName
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_NAME );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/invalid-name:/name}.
      - name: InvNum
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_NUMBER );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/invalid-number:/name}.
      - name: InvSize
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_SIZE );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/invalid-size:/name}.
      - name: InvPrio
        test-code: |
          T_rsc( ctx->status, RTEMS_INVALID_PRIORITY );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/invalid-priority:/name}.
      - name: NotConf
        test-code: |
          T_rsc( ctx->status, RTEMS_NOT_CONFIGURED );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/not-configured:/name}.
      - name: NotDef
        test-code: |
          T_rsc( ctx->status, RTEMS_NOT_DEFINED );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/not-defined:/name}.
      - name: NotImpl
        test-code: |
          T_rsc( ctx->status, RTEMS_NOT_IMPLEMENTED );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/not-implemented:/name}.
      - name: TooMany
        test-code: |
          T_rsc( ctx->status, RTEMS_TOO_MANY );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/too-many:/name}.
      - name: Unsat
        test-code: |
          T_rsc( ctx->status, RTEMS_UNSATISFIED  );
        text: |
          The return status of ${../if/directive:/name} shall be
          ${../../status/if/unsatisfied:/name}.
      test-epilogue: null
      test-prologue: null

For values which are returned by reference through directive parameters, use
the following post-condition states.

.. code-block:: yaml

    - name: SomeParamVar
      states:
      - name: Set
        test-code: |
          /* Add code to check that the object value was set to X */
        text: |
          The value of the object referenced by the
          ${../if/directive:/params[0]/name} parameter shall be set to X after
          the return of the ${../if/directive:/name} call.
      - name: Nop
        test-code: |
          /* Add code to check that the object was not modified */
        text: |
          Objects referenced by the ${../if/directive:/params[0]/name}
          parameter in past calls to ${../if/directive:/name} shall not be
          accessed by the ${../if/directive:/name} call.

Validation Test Guidelines
--------------------------

The validation test cases, test runners, and test suites are generated by the
``./spec2modules.py`` script from specification items.  For the placement and
naming of the generated sources use the following rules:

* Place architecture-specific validation test sources and programs into the
  ``testsuites/validation/cpu`` directory.

* Place BSP-specific validation test sources and programs into the
  ``testsuites/validation/bsps`` directory.

* Place all other validation test sources and programs into the
  ``testsuites/validation`` directory.

* Place architecture-specific unit test sources and programs into the
  ``testsuites/unit/cpu`` directory.

* Place BSP-specific unit test sources and programs into the
  ``testsuites/unit/bsps`` directory.

* Place all other unit test sources and programs into the
  ``testsuites/unit`` directory.

* Use dashes (``-``) to separate parts of a file name.  Use only dashes, the
  digits ``0`` to ``9``, and the lower case characters ``a`` to ``z`` for file
  names.  In particular, do not use underscores (``_``).

* The parts of a file name shall be separated by dashes and ordered from most
  general (left) to more specific (right), for example ``tc-task-construct.c``.

* The file names associated with tests shall be unique within the system since
  the test framework prints out only the base file names.

* Use the prefix ``tc-`` for test case files.

* Use the prefix ``tr-`` for test runner files.

* Use the prefix ``ts-`` for test suite files.

* Use the prefix ``tx-`` for test extension files (test support code).

* Tests for fatal errors shall have ``fatal`` as the most general file part,
  for example ``ts-fatal-too-large-tls-size.c``.

* Validation test suites shall have ``validation`` as the most general file
  part, for example ``ts-validation-no-clock-0.c``.

* Unit test suites shall have ``unit`` as the most general file part, for
  example ``ts-unit-no-clock-0.c``.

* Architecture-specific files shall have the architecture name as a file part,
  for example ``ts-fatal-sparc-leon3-clock-initialization.c``.

* BSP-specific files shall have the BSP family or variant name as a file part,
  for example ``tc-sparc-gr712rc.c``.

* Architecture-specific or BSP-specific tests shall use the ``enabled-by``
  attribute of the associated specification item to make the build item
  conditional, for example:

  .. code-block:: yaml

      ...
      build-type: objects
      enabled-by: arm
      type: build
      ...

  .. code-block:: yaml

      ...
      build-type: test-program
      enabled-by: bsps/sparc/leon3
      type: build
      ...

Verify the Specification Items
------------------------------

The ``./specverify.py`` script verifies that the specification items have the
format documented in :ref:`ReqEngSpecificationItems`.  To some extent the
values of attributes are verified as well.
