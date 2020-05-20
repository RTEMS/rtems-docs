.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. _ReqEngSpecItems:

Specification Items
===================

The technical specification of RTEMS will contain requirements, specializations
of requirements, :ref:`test procedures <ReqEngTestProcedure>`,
:ref:`test suites <ReqEngTestSuite>`, :ref:`test cases <ReqEngTestCase>`, and
:ref:`requirement validations <ReqEngValidation>`.  These things will be called
*specification items* or just *items* if it is clear from the context.

The specification items are stored in files in :term:`YAML` format with a
defined set of key-value pairs called attributes.  The key name shall match
with the pattern defined by the regular expression
``[a-zA-Z0-9][a-zA-Z0-9-]+``.  In particular, key names which begin with an
underscore (``_``) are reserved for internal use in tools.

Each specification item shall have the following attributes:

enabled-by
    The value shall be a list of expressions.  An expression is an operator
    or an option.  An option evaluates to true if it is included the set of
    enabled options of the configuration.  An operator is a dictionary with
    exactly one key and a value.  Valid keys are *and*, *or*, and *not*:

    * The value of the *and* operator shall be a list of expressions.  It
      evaluates to the *logical and* of all outcomes of the expressions in
      the list.

    * The value of the *or* operator shall be a list of expressions.  It
      evaluates to the *logical or* of all outcomes of the expressions in
      the list.

    * The value of the *not* operator shall be an expression.  It negates
      the outcome of its expression.

    The outcome of a list of expressions without an operator is the
    *logical or* of all outcomes of the expressions in the list.  An empty
    list evaluates to true.  Examples:

    .. code-block:: none

        enabled-by:
        - RTEMS_SMP

    .. code-block:: none

        enabled-by:
        - and:
          - RTEMS_NETWORKING
          - not: RTEMS_SMP

    .. code-block:: none

        enabled-by:
        - and:
          - not: TEST_DEBUGGER01_EXCLUDE
          - or:
            - arm
            - i386

links
    The value shall be a list of key-value pairs defining links to other
    specification items.  The list is ordered and defines the order in
    which links are processed.  There shall be a key *role* with an
    unspecified value.  There shall be a key *uid* with a relative UID to
    the item referenced by this link.  Other keys are type-specific.
    Example:

    .. code-block:: yaml

        links:
        - role: build-dependency
          uid: optpwrdwnhlt
        - role: build-dependency
          uid: ../../bspopts
        - role: build-dependency
          uid: ../start

type
    The value shall be the specification :ref:`item type <ReqEngItemTypes>`.

The following attributes are used in specification items of various types:

.. _ReqEngItemAttrLicense:

SPDX-License-Identifier
    The value should be ``BSD-2-Clause OR CC-BY-SA-4.0``.  If content is
    imported from external sources, then the corresponding license shall be
    used.  Acceptable licenses are BSD-2-Clause and CC-BY-SA-4.0.  The
    copyright holder of the external work should be asked to allow a
    dual-licensing BSD-2-Clause or CC-BY-SA-4.0.  This allows generation of
    BSD-2-Clause licensed source code and CC-BY-SA-4.0 licensed documentation.

.. _ReqEngItemAttrCopyrights:

copyrights
    The value shall be a list of copyright statements of the following formats:

    * ``Copyright (C) <YEAR> <COPYRIGHT HOLDER>``

    * ``Copyright (C) <FIRST YEAR>, <LAST YEAR> <COPYRIGHT HOLDER>``

    See also :ref:`FileHeaderCopyright`.

.. _ReqEngItemTypes:

Item Types
----------

Specification items can have all sorts of *types*.  The selection of types and
the level of detail depends on a particular standard and product model.  We need
enough flexibility to be in line with ECSS-E-ST-10-06 and possible future
applications of other standards.  Each item may have a list of types.  Valid
types are listed below.  This list may change over time.  If new types are
added, then a mapping between types should be specified.  The item types and
their definition is work in progress.  A list of types follows:

* requirement

    * functional - Functional requirements shall describe the behaviour of the
      software product under specific conditions.

        * *capability*

        * *dependability-function*

        * *function*

        * *operational* - Operational requirements shall

            * define the operation modes (e.g. initialization, multitasking, termination),

            * describe the operation modes, and

            * describe the operation mode transitions.

        * *safety-function*

    * non-functional

        * *build-configuration*

        * *constraint*

        * *design*

        * *interface*

        * *interface-requirement*

        * *maintainability*

        * *performance*

        * *portability*

        * *quality*

        * *reliability*

        * *resource*

        * *safety*

* *test-procedure*

* *test-suite*

* *test-case*

* *validation-by-analysis*

* *validation-by-inspection*

* *validation-by-review-of-design*

* *validation-platform*

.. image:: ../../images/eng/req-spec-items.*
    :scale: 70
    :align: center

Requirements
------------

All requirement specification items shall have the following attribute:

rationale:
    The rationale or justification of the specification item.

Build Configuration
-------------------

Build configuration requirements define what needs to be built (libraries,
object files, test executables, etc.) and how (configuration option header
files, compiler flags, linker flags, etc.).  The goal is to generate build
files (Makefile or waf) and content for the Software Configuration File (SCF)
from it.  A YAML scheme needs to be defined for this purpose.

.. _ReqEngInterfaceReq:

Interface Requirement
---------------------

Interface requirements shall describe the high level aspects of interfaces.
The item type shall be *interface-requirement*.

.. _ReqEngInterface:

Interface
---------

.. warning::

    This is work in progress.

Interface items shall specify the interface of the software product to other
software products and the hardware.  The item type shall be *interface*.  The
interface items shall have an *interface-category* which is one of the
following and nothing else:

* *application*: Application interface items shall describe the interface
  between the software product and the application (:term:`API`).  The goal is
  to generate header files with Doxygen markup and user manual documentation
  parts from the application interface specification.

* *application-configuration*: Application configuration items shall define
  parameters of the software product which can be set by the application at
  link-time.  The goal is to generate user manual documentation parts and test
  cases from the application configuration specification.

* *architecture*: Architecture interface items shall define the
  interface between the software product and the processor architecture
  (:term:`ABI`).

* *gcc*: GCC interface items shall define the interface between the software
  product and GCC components such as libgcc.a, libatomic.a, libgomp.a,
  libstdc++.a, etc.

* *hardware*: Hardware interface items shall define the interface between the
  software product and the hardware.

* *newlib*: Newlib interface items shall define the interface between the
  software product and the Newlib (libc.a).

The interface items shall have an *interface-type* which is one of the
following and nothing else:

* *configuration-option*

* *define*

* *enum*

* *function*

* *header*

* *macro*

* *register-block*

* *structure*

* *typedef*

* *union*

* *variable*

.. _ReqEngInterfaceApplicationConfigGroups:

Interface - Application Configuration Groups
--------------------------------------------

The application configuration group items shall have the following attribute
specializations:

SPDX-License-Identifier
    See :ref:`SPDX-License-Identifier <ReqEngItemAttrLicense>`.

appl-config-group-description:
    The value shall be the description of this application configuration group.

appl-config-group-name:
    The value shall be the name of this application configuration group.

copyrights
    See :ref:`copyrights <ReqEngItemAttrCopyrights>`.

interface-type
    The interface type value shall be *appl-config-group*.

link
    There shall be a link to a higher level requirement.

text
    The application configuration group requirement.

type
    The type value shall be *interface*.

.. _ReqEngInterfaceApplicationConfigOptions:

Interface - Application Configuration Options
---------------------------------------------

The application configuration option items shall have the following attribute
specializations:

SPDX-License-Identifier
    See :ref:`SPDX-License-Identifier <ReqEngItemAttrLicense>`.

appl-config-option-constraint
    This attribute shall be present only for *initializer* and *integer*
    type options.  The value shall be a dictionary of the following optional
    key-value pairs.

    custom
        The value shall be a list of constraints in natural language.  Use the
        following wording:

            The value of this configuration option shall be ...

    min
        The value shall be the minimum value of the option.

    max
        The value shall be the maximum value of the option.

    links
        The value shall be a list of relative UIDs to constraints.

    set
        The value shall be the list of valid values of the option.

appl-config-option-default
    This attribute shall be present only for *feature* type options.  The value
    shall be a description of the default configuration in case this boolean
    feature define is undefined.  Use the following wording:

        If this configuration option is undefined, then ...

appl-config-option-default-value
    This attribute shall be present only for *initializer* and *integer*
    type options.  The value shall be an initializer, an integer, or a
    descriptive text.

appl-config-option-description
    For *feature* and *feature-enable* type options, the value shall be a
    description of the configuration in case this boolean feature define is
    defined.  Use the following wording:

        In case this configuration option is defined, then ...

    For *initializer* and *integer* options, the value shall describe the
    effect of the option value.  The description should focus on the average
    use-case.  It should not cover potential problems, constraints, obscure
    use-cases, corner cases and everything which makes matters complicated.
    Add these things to *appl-config-option-constraint* and
    *appl-config-option-notes*.  Use the following wording:

        The value of this configuration option defines ...

appl-config-option-index
    The value shall be a list of entries for the document index.  By default,
    the application configuration option name is added to the index.

appl-config-option-name
    The value shall be the name of the application configuration option.  Use a
    pattern of ``CONFIGURE_[A-Z0-9_]+`` for the name.

appl-config-option-notes
    The value shall be the notes for this option.  The notes should explain
    everything which was omitted from the description.  It should cover all the
    details, special cases, usage notes, error conditions, configuration
    dependencies, and references.

appl-config-option-type
    The value shall be one of the following and nothing else:

    feature
        Use this type for boolean feature opions which have a behaviour in the
        default configuration which is not just that the feature is disabled.

    feature-enable
        Use this type for boolean feature opions which just enables a feature.

    initializer
        Use this type for options which initialize a data structure.

    integer
        Use this type for integer options.

copyrights
    See :ref:`copyrights <ReqEngItemAttrCopyrights>`.

interface-type
    The interface type value shall be *appl-config-option*.

link
    There shall be a link to the application configuration group to which this
    option belongs.

text
    The application configuration option requirement.

type
    The type value shall be *interface*.

.. _ReqEngTestProcedure:

Test Procedure
--------------

Test procedures shall be executed by the Qualification Toolchain.

The test procedure items shall have the following attribute
specializations:

type
    The type value shall be *test-procedure*.

text
    The purpose of this test procedure.

platform
    There shall be links to validation platform requirements.

steps
    The test procedure steps.  Could be a list of key-value pairs.  The key
    is the step name and the value is a description of the actions
    performed in this step.

.. _ReqEngTestSuite:

Test Suite
----------

Test suites shall use the :ref:`RTEMS Test Framework <RTEMSTestFramework>`.

The test suite items shall have the following attribute specializations:

type
    The type value shall be *test-suite*.

text
    The test suite description.

.. _ReqEngTestCase:

Test Case
---------

Test cases shall use the :ref:`RTEMS Test Framework <RTEMSTestFramework>`.

The test case items shall have the following attribute specializations:

type
    The type value shall be *test-case*.

link
    The link to the requirement validated by this test case or no links if
    this is a unit or integration test case.

ref
    If this is a unit test case, then a reference to the :term:`software
    item` under test shall be provided.  If this is an integration test
    case, then a reference to the integration under test shall be provided.
    The integration is identified by its Doxygen group name.

text
    A short description of the test case.

inputs
    The inputs to execute the test case.

outputs
    The expected outputs.

The test case code may be also contained in the test case specification
item in a *code* attribute.  This is subject to discussion on the RTEMS
mailing list.  Alternatively, the test code could be placed directly in
source files.  A method is required to find the test case specification of
a test case code and vice versa.

.. _ReqEngResAndPerf:

Resources and Performance
-------------------------

Normally, resource and performance requirements are formulated like this:

* The resource U shall need less than V storage units.

* The operation Y shall complete within X time units.

Such statements are difficult to make for a software product like RTEMS which
runs on many different target platforms in various configurations.  So, the
performance requirements of RTEMS shall be stated in terms of benchmarks.  The
benchmarks are run on the project-specific target platform and configuration.
The results obtained by the benchmark runs are reported in a human readable
presentation.  The application designer can then use the benchmark results to
determine if its system performance requirements are met.  The benchmarks shall
be executed under different environment conditions, e.g. varying cache states
(dirty, empty, valid) and system bus load generated by other processors.  The
application designer shall have the ability to add additional environment
conditions, e.g. system bus load by DMA engines or different system bus
arbitration schemes.

To catch resource and performance regressions via test suite runs there shall be
a means to specify threshold values for the measured quantities.  The threshold
values should be provided for each validation platform.  How this can be done
and if the threshold values are maintained by the RTEMS Project is subject to
discussion.
