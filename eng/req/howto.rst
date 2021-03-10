.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)

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

Application Configuration Options
---------------------------------

The application configuration options and groups are maintained by
specification items in the directory :file:`spec/if/acfg`.  Application
configuration options are grouped by
:ref:`SpecTypeApplicationConfigurationGroupItemType` items which should be
stored in files using the :file:`spec/if/acfg/group-*.yml` pattern.  Each
application configuration option shall link to exactly one group item with the
:ref:`SpecTypeApplicationConfigurationGroupMemberLinkRole`.  There are four
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
"${../rtems/tasks/create:/name}".  References to other parts of the
documentation are possible, however, they are currently provided by hard-coded
tables in :file:`rtemsspec/applconfig.py`.

Modify an Existing Group
^^^^^^^^^^^^^^^^^^^^^^^^

Search for the group by its section header and edit the specification item
file.  For example:

.. code-block:: none

    $ grep -rl "name: General System Configuration" spec/if/acfg
    spec/if/acfg/group-general.yml
    $ vi spec/if/acfg/group-general.yml

Modify an Existing Option
^^^^^^^^^^^^^^^^^^^^^^^^^

Search for the option by its C preprocessor define name and edit the
specification item file.  For example:

.. code-block:: none

    $ grep -rl CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER spec/if/acfg
    spec/if/acfg/appl-needs-clock-driver.yml
    $ vi spec/if/acfg/appl-needs-clock-driver.yml

Add a New Group
^^^^^^^^^^^^^^^

Let ``new`` be the UID name part of the new group.  Create the file
:file:`spec/if/acfg/group-new.yml` and provide all attributes for an
:ref:`SpecTypeApplicationConfigurationGroupItemType` item.  For example:

.. code-block:: none

    $ vi spec/if/acfg/group-new.yml

Add a New Option
^^^^^^^^^^^^^^^^

Let ``my-new-option`` be the UID name of the option.  Create the file
:file:`if/acfg/my-new-option.yml` and provide all attributes for an appropriate
refinement of :ref:`SpecTypeApplicationConfigurationOptionItemType`.  For
example:

.. code-block:: none

    $ vi spec/if/acfg/my-new-option.yml

Generate Content after Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you are done with the modifications of an existing item or the creation of
a new item, the changes need to be propagated to generated source files.  This
is done by the :file:`spec2modules.py` script.  Before you call this script,
make sure the Git submodules are up-to-date.

.. code-block:: none

    $ ./spec2dmodules.py

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
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
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

The RTEMS :term:`API` header files are specified under ``spec:/if/rtems/*``.
Create a subdirectory with a corresponding name for the API, for example in
:file:`spec/if/rtems/foo` for the `foo` API.  In this new subdirectory place an
:ref:`SpecTypeInterfaceHeaderFileItemType` item named :file:`header.yml`
(:file:`spec/if/rtems/foo/header.yml`) and populate it with the required
attributes.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    interface-type: header-file
    links:
    - role: interface-placement
      uid: /if/domains/api
    path: rtems/rtems/foo.h
    prefix: cpukit/include
    type: interface

Specify an API Element
^^^^^^^^^^^^^^^^^^^^^^

Figure out the corresponding header file item.  If it does not exist, see
:ref:`ReqEngAddAPIHeaderFile`.  Place a specialization of an
:ref:`SpecTypeInterfaceItemType` item into the directory of the header file
item, for example :file:`spec/if/rtems/foo/bar.yml` for the :c:func:`bar`
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
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
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
        value: ${/if/c/null}
    type: interface

Action Requirements
-------------------

Use :ref:`SpecTypeActionRequirementItemType` items to specify and validate
directive calls.  Action requirements are a generator for event-driven
requirements which should be written in the following :ref:`syntax
<ReqEngSyntax>`:

    *When* <optional preconditions> <trigger>, the <system name> shall
    <system response>.

The <optional preconditions> are the pre-conditions of the action requirement.
The <trigger> is the action of the action requirement.  The post-conditions
should provide a list of the <system name> shall <system response> clauses.
Each transition in the transition map is an event-driven requirement composed
of the pre-condition states, the action, and the post-condition states defined
by the map entry.

Use ``CamelCase`` for the pre-condition names, post-condition
names, and state names.  The more conditions a directive has, the shorter
should be the names.  The transition map may be documented as a table and more
conditions need more table columns.  Use item attribute references in the
``text`` attributes.  This allows context-sensitive substitutions.

Link the action requirement item to an :ref:`SpecTypeInterfaceFunctionItemType`
or an :ref:`SpecTypeInterfaceMacroItemType` item using the
:ref:`SpecTypeInterfaceFunctionLinkRole`.

Pre-Conditions
^^^^^^^^^^^^^^

Specify all directive parameters as separate pre-conditions.  Use the following
syntax for directive object identifier parameters:

.. code-block:: yaml

    - name: Id
      states:
      - name: NoObj
        test-code: |
          ctx->id = 0xffffffff;
        text: |
          The ${../if/directive:/params[0]/name} parameter shall not be
          associated with a thing.
      - name: ClassA
        test-code: |
          ctx->id = ctx->class_a_id;
        text: |
          The ${../if/directive:/params[0]/name} parameter shall be associated with a
          class A thing.
      - name: ClassB
        test-code: |
          ctx->id = ctx->class_b_id;
        text: |
          The ${../if/directive:/params[0]/name} parameter shall be associated with a
          class B thing.
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
          The ${../if/directive:/params[3]/name} parameter shall reference an
          object of type ${../../type/if/id:/name}.
      - name: 'Null'
        test-code: |
          ctx->id = NULL;
        text: |
          The ${../if/directive:/params[3]/name} parameter shall be
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
          The ${../if/directive:/params[0]/name} parameter shall be valid.
      - name: Invalid
        test-code: |
          ctx->name = 0;
        text: |
          The ${../if/directive:/params[0]/name} parameter shall be invalid.
      test-epilogue: null
      test-prologue: null

Post-Conditions
^^^^^^^^^^^^^^^

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

    - name: SomeParam
      states:
      - name: Nop
        test-code: |
          /* Add code to check that the object was not modified. */
        text: |
          Objects referenced by the ${../if/directive:/params[0]/name}
          parameter in past calls to ${../if/directive:/name} shall not be
          accessed by the ${../if/directive:/name} call.
      - name: Set
        test-code: |
          /* Add code to check that the object was set to a particular value. */
        text: |
          The value of the object referenced by the
          ${../if/directive:/params[0]/name} parameter shall be set to X after
          the return of the ${../if/directive:/name} call.
