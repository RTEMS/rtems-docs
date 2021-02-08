.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. _ReqEngSpecificationItems:

Specification Items
===================

.. _ReqEngSpecificationItemHierarchy:

Specification Item Hierarchy
----------------------------

The specification item types have the following hierarchy:

* :ref:`SpecTypeRootItemType`

  * :ref:`SpecTypeBuildItemType`

    * :ref:`SpecTypeBuildAdaTestProgramItemType`

    * :ref:`SpecTypeBuildBSPItemType`

    * :ref:`SpecTypeBuildConfigurationFileItemType`

    * :ref:`SpecTypeBuildConfigurationHeaderItemType`

    * :ref:`SpecTypeBuildGroupItemType`

    * :ref:`SpecTypeBuildLibraryItemType`

    * :ref:`SpecTypeBuildObjectsItemType`

    * :ref:`SpecTypeBuildOptionItemType`

    * :ref:`SpecTypeBuildScriptItemType`

    * :ref:`SpecTypeBuildStartFileItemType`

    * :ref:`SpecTypeBuildTestProgramItemType`

  * :ref:`SpecTypeConstraintItemType`

  * :ref:`SpecTypeGlossaryItemType`

    * :ref:`SpecTypeGlossaryGroupItemType`

    * :ref:`SpecTypeGlossaryTermItemType`

  * :ref:`SpecTypeInterfaceItemType`

    * :ref:`SpecTypeApplicationConfigurationGroupItemType`

    * :ref:`SpecTypeApplicationConfigurationOptionItemType`

      * :ref:`SpecTypeApplicationConfigurationFeatureEnableOptionItemType`

      * :ref:`SpecTypeApplicationConfigurationFeatureOptionItemType`

      * :ref:`SpecTypeApplicationConfigurationValueOptionItemType`

    * :ref:`SpecTypeInterfaceCompoundItemType`

    * :ref:`SpecTypeInterfaceContainerItemType`

    * :ref:`SpecTypeInterfaceDefineItemType`

    * :ref:`SpecTypeInterfaceDomainItemType`

    * :ref:`SpecTypeInterfaceEnumItemType`

    * :ref:`SpecTypeInterfaceEnumeratorItemType`

    * :ref:`SpecTypeInterfaceForwardDeclarationItemType`

    * :ref:`SpecTypeInterfaceFunctionItemType`

    * :ref:`SpecTypeInterfaceGroupItemType`

    * :ref:`SpecTypeInterfaceHeaderFileItemType`

    * :ref:`SpecTypeInterfaceMacroItemType`

    * :ref:`SpecTypeInterfaceTypedefItemType`

    * :ref:`SpecTypeInterfaceUnspecifiedItemType`

    * :ref:`SpecTypeInterfaceVariableItemType`

  * :ref:`SpecTypeRequirementItemType`

    * :ref:`SpecTypeFunctionalRequirementItemType`

      * :ref:`SpecTypeActionRequirementItemType`

      * :ref:`SpecTypeGenericFunctionalRequirementItemType`

    * :ref:`SpecTypeNonFunctionalRequirementItemType`

      * :ref:`SpecTypeDesignGroupRequirementItemType`

      * :ref:`SpecTypeGenericNonFunctionalRequirementItemType`

      * :ref:`SpecTypeRuntimePerformanceRequirementItemType`

  * :ref:`SpecTypeRequirementValidationItemType`

  * :ref:`SpecTypeRuntimeMeasurementTestItemType`

  * :ref:`SpecTypeSpecificationItemType`

  * :ref:`SpecTypeTestCaseItemType`

  * :ref:`SpecTypeTestPlatformItemType`

  * :ref:`SpecTypeTestProcedureItemType`

  * :ref:`SpecTypeTestSuiteItemType`

.. _ReqEngSpecificationItemTypes:

Specification Item Types
------------------------

.. _SpecTypeRootItemType:

Root Item Type
^^^^^^^^^^^^^^

The technical specification of RTEMS will contain for example requirements,
specializations of requirements, interface specifications, test suites, test
cases, and requirement validations.  These things will be called *specification
items* or just *items* if it is clear from the context.

The specification items are stored in files in :term:`YAML` format with a
defined set of key-value pairs called attributes.  Each attribute key name
shall be a :ref:`SpecTypeName`.  In particular, key names which begin with an
underscore (``_``) are reserved for internal use in tools.

This is the root specification item type. All explicit attributes shall be
specified. The explicit attributes for this type are:

SPDX-License-Identifier
    The attribute value shall be a :ref:`SpecTypeSPDXLicenseIdentifier`. It
    shall be the license of the item.

copyrights
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeCopyright`. It shall be the list of copyright statements of
    the item.

enabled-by
    The attribute value shall be an :ref:`SpecTypeEnabledByExpression`. It
    shall define the conditions under which the item is enabled.

links
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeLink`.

type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the item
    type.  The selection of types and the level of detail depends on a
    particular standard and product model.  We need enough flexibility to be in
    line with ECSS-E-ST-10-06 and possible future applications of other
    standards.  The item type may be refined further with additional
    type-specific subtypes.

This type is refined by the following types:

* :ref:`SpecTypeBuildItemType`

* :ref:`SpecTypeConstraintItemType`

* :ref:`SpecTypeGlossaryItemType`

* :ref:`SpecTypeInterfaceItemType`

* :ref:`SpecTypeRequirementItemType`

* :ref:`SpecTypeRequirementValidationItemType`

* :ref:`SpecTypeRuntimeMeasurementTestItemType`

* :ref:`SpecTypeSpecificationItemType`

* :ref:`SpecTypeTestCaseItemType`

* :ref:`SpecTypeTestPlatformItemType`

* :ref:`SpecTypeTestProcedureItemType`

* :ref:`SpecTypeTestSuiteItemType`

.. _SpecTypeBuildItemType:

Build Item Type
^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``build``. This set of attributes specifies a build
item. All explicit attributes shall be specified. The explicit attributes for
this type are:

build-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the build
    item type.

This type is refined by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildBSPItemType`

* :ref:`SpecTypeBuildConfigurationFileItemType`

* :ref:`SpecTypeBuildConfigurationHeaderItemType`

* :ref:`SpecTypeBuildGroupItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

* :ref:`SpecTypeBuildOptionItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildStartFileItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildAdaTestProgramItemType:

Build Ada Test Program Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``ada-test-program``. This set of attributes
specifies an Ada test program executable to build. Test programs may use
additional objects provided by :ref:`SpecTypeBuildObjectsItemType` items.  Test
programs have an implicit ``enabled-by`` attribute value which is controlled by
the option action :ref:`set-test-state <SpecTypeBuildOptionItemType>`.  If the
test state is set to ``exclude``, then the test program is not built. All
explicit attributes shall be specified. The explicit attributes for this type
are:

ada-main
    The attribute value shall be a string. It shall be the path to the Ada main
    body file.

ada-object-directory
    The attribute value shall be a string. It shall be the path to the Ada
    object directory (``-D`` option value for ``gnatmake``).

adaflags
    The attribute value shall be a list of strings. It shall be a list of
    options for the Ada compiler.

adaincludes
    The attribute value shall be a list of strings. It shall be a list of Ada
    include paths.

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

ldflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildLinkerOption`.

source
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildSource`.

stlib
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildLinkStaticLibraryDirective`.

target
    The attribute value shall be a :ref:`SpecTypeBuildTarget`.

use-after
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseAfterDirective`.

use-before
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    ada-main: testsuites/ada/samples/hello/hello.adb
    ada-object-directory: testsuites/ada/samples/hello
    adaflags: []
    adaincludes:
    - cpukit/include/adainclude
    - testsuites/ada/support
    build-type: ada-test-program
    cflags: []
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    cppflags: []
    enabled-by: true
    includes: []
    ldflags: []
    links: []
    source:
    - testsuites/ada/samples/hello/init.c
    stlib: []
    target: testsuites/ada/ada_hello.exe
    type: build
    use-after: []
    use-before: []

.. _SpecTypeBuildBSPItemType:

Build BSP Item Type
^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``bsp``. This set of attributes specifies a base BSP
variant to build. All explicit attributes shall be specified. The explicit
attributes for this type are:

arch
    The attribute value shall be a string. It shall be the target architecture
    of the BSP.

bsp
    The attribute value shall be a string. It shall be the base BSP variant
    name.

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

family
    The attribute value shall be a string. It shall be the BSP family name.
    The name shall be the last directory of the path to the BSP sources.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

install
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildInstallDirective`.

source
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildSource`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    arch: myarch
    bsp: mybsp
    build-type: bsp
    cflags: []
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    cppflags: []
    enabled-by: true
    family: mybsp
    includes: []
    install:
    - destination: ${BSP_INCLUDEDIR}
      source:
      - bsps/myarch/mybsp/include/bsp.h
      - bsps/myarch/mybsp/include/tm27.h
    - destination: ${BSP_INCLUDEDIR}/bsp
      source:
      - bsps/myarch/mybsp/include/bsp/irq.h
    - destination: ${BSP_LIBDIR}
      source:
      - bsps/myarch/mybsp/start/linkcmds
    links:
    - role: build-dependency
      uid: ../../obj
    - role: build-dependency
      uid: ../../opto2
    - role: build-dependency
      uid: abi
    - role: build-dependency
      uid: obj
    - role: build-dependency
      uid: ../start
    - role: build-dependency
      uid: ../../bspopts
    source:
    - bsps/myarch/mybsp/start/bspstart.c
    type: build

.. _SpecTypeBuildConfigurationFileItemType:

Build Configuration File Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``config-file``. This set of attributes specifies a
configuration file placed in the build tree.  The configuration file is
generated during the configure command execution and is placed in the build
tree. All explicit attributes shall be specified. The explicit attributes for
this type are:

content
    The attribute value shall be a string. It shall be the content of the
    configuration file. A ${VARIABLE} substitution is performed during the
    configure command execution using the variables of the configuration set.
    Use $$ for a plain $ character. To have all variables from sibling items
    available for substitution it is recommended to link them in the proper
    order.

install-path
    The attribute value shall be a :ref:`SpecTypeBuildInstallPath`.

target
    The attribute value shall be a :ref:`SpecTypeBuildTarget`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    build-type: config-file
    content: |
      # ...
      Name: ${ARCH}-rtems${__RTEMS_MAJOR__}-${BSP_NAME}
      # ...
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    install-path: ${PREFIX}/lib/pkgconfig
    links: []
    target: ${ARCH}-rtems${__RTEMS_MAJOR__}-${BSP_NAME}.pc
    type: build

.. _SpecTypeBuildConfigurationHeaderItemType:

Build Configuration Header Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``config-header``. This set of attributes specifies
configuration header file.  The configuration header file is generated during
configure command execution and is placed in the build tree.  All collected
configuration defines are written to the configuration header file during the
configure command execution.  To have all configuration defines from sibling
items available it is recommended to link them in the proper order. All
explicit attributes shall be specified. The explicit attributes for this type
are:

guard
    The attribute value shall be a string. It shall be the header guard define.

include-headers
    The attribute value shall be a list of strings. It shall be a list of
    header files to include via ``#include <...>``.

install-path
    The attribute value shall be a :ref:`SpecTypeBuildInstallPath`.

target
    The attribute value shall be a :ref:`SpecTypeBuildTarget`.

.. _SpecTypeBuildGroupItemType:

Build Group Item Type
^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``group``. This set of attributes provides a means to
aggregate other build items and modify the build item context which is used by
referenced build items.  The ``includes``, ``ldflags``, ``objects``, and
``use`` variables of the build item context are updated by the corresponding
attributes of the build group. All explicit attributes shall be specified. The
explicit attributes for this type are:

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

install
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildInstallDirective`.

ldflags
    The attribute value shall be a list of strings. It shall be a list of
    options for the linker.  They are used to link executables referenced by
    this item.

use-after
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseAfterDirective`.

use-before
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    build-type: group
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by:
    - BUILD_TESTS
    - BUILD_SAMPLES
    includes:
    - testsuites/support/include
    install: []
    ldflags:
    - -Wl,--wrap=printf
    - -Wl,--wrap=puts
    links:
    - role: build-dependency
      uid: ticker
    type: build
    use-after: []
    use-before:
    - rtemstest

.. _SpecTypeBuildLibraryItemType:

Build Library Item Type
^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``library``. This set of attributes specifies a
static library.  Library items may use additional objects provided by
:ref:`SpecTypeBuildObjectsItemType` items through the build dependency links of
the item. All explicit attributes shall be specified. The explicit attributes
for this type are:

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

cxxflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCXXCompilerOption`.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

install
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildInstallDirective`.

install-path
    The attribute value shall be a :ref:`SpecTypeBuildInstallPath`.

source
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildSource`.

target
    The attribute value shall be a :ref:`SpecTypeBuildTarget`. It shall be the
    name of the static library, e.g. ``z`` for ``libz.a``.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    build-type: library
    cflags:
    - -Wno-pointer-sign
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    cppflags: []
    cxxflags: []
    enabled-by: true
    includes:
    - cpukit/libfs/src/jffs2/include
    install:
    - destination: ${BSP_INCLUDEDIR}/rtems
      source:
      - cpukit/include/rtems/jffs2.h
    install-path: ${BSP_LIBDIR}
    links: []
    source:
    - cpukit/libfs/src/jffs2/src/build.c
    target: jffs2
    type: build

.. _SpecTypeBuildObjectsItemType:

Build Objects Item Type
^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``objects``. This set of attributes specifies a set
of object files used to build static libraries or test programs. All explicit
attributes shall be specified. The explicit attributes for this type are:

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

cxxflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCXXCompilerOption`.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

install
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildInstallDirective`.

source
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildSource`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    build-type: objects
    cflags: []
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    cppflags: []
    cxxflags: []
    enabled-by: true
    includes: []
    install:
    - destination: ${BSP_INCLUDEDIR}/bsp
      source:
      - bsps/include/bsp/bootcard.h
      - bsps/include/bsp/default-initial-extension.h
      - bsps/include/bsp/fatal.h
    links: []
    source:
    - bsps/shared/start/bootcard.c
    - bsps/shared/rtems-version.c
    type: build

.. _SpecTypeBuildOptionItemType:

Build Option Item Type
^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``option``. This set of attributes specifies a build
option. The following explicit attributes are mandatory:

* ``actions``

* ``default``

* ``default-by-variant``

* ``description``

The explicit attributes for this type are:

actions
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildOptionAction`. Each action operates on the *action
    value* handed over by a previous action and action-specific attribute
    values.  The actions pass the processed action value to the next action in
    the list.  The first action starts with an action value of ``None``.  The
    actions are carried out during the configure command execution.

default
    The attribute value shall be a :ref:`SpecTypeBuildOptionValue`. It shall be
    the default value of the option if no variant-specific default value is
    specified.  Use ``null`` to specify that no default value exits.  The
    variant-specific default values may be specified by the
    ``default-by-variant`` attribute.

default-by-variant
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildOptionDefaultByVariant`. The list is processed from top
    to bottom.  If a matching variant is found, then the processing stops.

description
    The attribute value shall be an optional string. It shall be the
    description of the option.

format
    The attribute value shall be an optional string. It shall be a `Python
    format string
    <https://docs.python.org/3/library/string.html#formatstrings>`_, for
    example ``'{}'`` or ``'{:#010x}'``.

name
    The attribute value shall be a :ref:`SpecTypeBuildOptionName`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    actions:
    - get-integer: null
    - define: null
    build-type: option
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    default: 115200
    default-by-variant:
    - value: 9600
      variants:
      - m68k/m5484FireEngine
      - powerpc/hsc_cm01
    - value: 19200
      variants:
      - m68k/COBRA5475
    description: |
      Default baud for console and other serial devices.
    enabled-by: true
    format: '{}'
    links: []
    name: BSP_CONSOLE_BAUD
    type: build

.. _SpecTypeBuildScriptItemType:

Build Script Item Type
^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``script``. This set of attributes specifies a build
script.  The optional attributes may be required by commands executed through
the scripts. The following explicit attributes are mandatory:

* ``do-build``

* ``do-configure``

* ``prepare-build``

* ``prepare-configure``

The explicit attributes for this type are:

asflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildAssemblerOption`.

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

cxxflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCXXCompilerOption`.

do-build
    The attribute value shall be an optional string. If this script shall
    execute, then it shall be Python code which is executed via ``exec()`` in
    the context of the ``do_build()`` method of the :file:`wscript`.  A local
    variable ``bld`` is available with the ``waf`` build context.  A local
    variable ``bic`` is available with the build item context.

do-configure
    The attribute value shall be an optional string. If this script shall
    execute, then it shall be Python code which is executed via ``exec()`` in
    the context of the ``do_configure()`` method of the :file:`wscript`.  A
    local variable ``conf`` is available with the ``waf`` configuration
    context.  A local variable ``cic`` is available with the configuration item
    context.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

ldflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildLinkerOption`.

prepare-build
    The attribute value shall be an optional string. If this script shall
    execute, then it shall be Python code which is executed via ``exec()`` in
    the context of the ``prepare_build()`` method of the :file:`wscript`.  A
    local variable ``bld`` is available with the ``waf`` build context.  A
    local variable ``bic`` is available with the build item context.

prepare-configure
    The attribute value shall be an optional string. If this script shall
    execute, then it shall be Python code which is executed via ``exec()`` in
    the context of the ``prepare_configure()`` method of the :file:`wscript`.
    A local variable ``conf`` is available with the ``waf`` configuration
    context.  A local variable ``cic`` is available with the configuration item
    context.

stlib
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildLinkStaticLibraryDirective`.

use-after
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseAfterDirective`.

use-before
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    build-type: script
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    default: null
    default-by-variant: []
    do-build: |
      bld.install_as(
          "${BSP_LIBDIR}/linkcmds",
          "bsps/" + bld.env.ARCH + "/" + bld.env.BSP_FAMILY +
          "/start/linkcmds." + bld.env.BSP_BASE
      )
    do-configure: |
      conf.env.append_value(
          "LINKFLAGS",
          ["-qnolinkcmds", "-T", "linkcmds." + conf.env.BSP_BASE]
      )
    enabled-by: true
    links: []
    prepare-build: null
    prepare-configure: null
    type: build

.. _SpecTypeBuildStartFileItemType:

Build Start File Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``start-file``. This set of attributes specifies a
start file to build.  A start file is used to link an executable. All explicit
attributes shall be specified. The explicit attributes for this type are:

asflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildAssemblerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

install-path
    The attribute value shall be a :ref:`SpecTypeBuildInstallPath`.

source
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildSource`.

target
    The attribute value shall be a :ref:`SpecTypeBuildTarget`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    asflags: []
    build-type: start-file
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    cppflags: []
    enabled-by: true
    includes: []
    install-path: ${BSP_LIBDIR}
    links: []
    source:
    - bsps/sparc/shared/start/start.S
    target: start.o
    type: build

.. _SpecTypeBuildTestProgramItemType:

Build Test Program Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeBuildItemType` through the ``build-type``
attribute if the value is ``test-program``. This set of attributes specifies a
test program executable to build. Test programs may use additional objects
provided by :ref:`SpecTypeBuildObjectsItemType` items.  Test programs have an
implicit ``enabled-by`` attribute value which is controlled by the option
action :ref:`set-test-state <SpecTypeBuildOptionItemType>`.  If the test state
is set to ``exclude``, then the test program is not built. All explicit
attributes shall be specified. The explicit attributes for this type are:

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

cppflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCPreprocessorOption`.

cxxflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCXXCompilerOption`.

features
    The attribute value shall be a string. It shall be the ``waf`` build
    features for this test program.

includes
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildIncludePath`.

ldflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildLinkerOption`.

source
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildSource`.

stlib
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildLinkStaticLibraryDirective`.

target
    The attribute value shall be a :ref:`SpecTypeBuildTarget`.

use-after
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseAfterDirective`.

use-before
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    build-type: test-program
    cflags: []
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    cppflags: []
    cxxflags: []
    enabled-by: true
    features: c cprogram
    includes: []
    ldflags: []
    links: []
    source:
    - testsuites/samples/ticker/init.c
    - testsuites/samples/ticker/tasks.c
    stlib: []
    target: testsuites/samples/ticker.exe
    type: build
    use-after: []
    use-before: []

.. _SpecTypeConstraintItemType:

Constraint Item Type
^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``constraint``. This set of attributes specifies a
constraint. All explicit attributes shall be specified. The explicit attributes
for this type are:

rationale
    The attribute value shall be an optional string. If the value is present,
    then it shall state the rationale or justification of the constraint.

scope
    The attribute value shall be a string. It shall be the scope of the
    constraint.

text
    The attribute value shall be a :ref:`SpecTypeRequirementText`. It shall
    state the constraint.

.. _SpecTypeGlossaryItemType:

Glossary Item Type
^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``glossary``. This set of attributes specifies a
glossary item. All explicit attributes shall be specified. The explicit
attributes for this type are:

glossary-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    glossary item type.

This type is refined by the following types:

* :ref:`SpecTypeGlossaryGroupItemType`

* :ref:`SpecTypeGlossaryTermItemType`

.. _SpecTypeGlossaryGroupItemType:

Glossary Group Item Type
^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeGlossaryItemType` through the
``glossary-type`` attribute if the value is ``group``. This set of attributes
specifies a glossary group. All explicit attributes shall be specified. The
explicit attributes for this type are:

name
    The attribute value shall be a string. It shall be the human readable name
    of the glossary group.

text
    The attribute value shall be a string. It shall state the requirement for
    the glossary group.

.. _SpecTypeGlossaryTermItemType:

Glossary Term Item Type
^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeGlossaryItemType` through the
``glossary-type`` attribute if the value is ``term``. This set of attributes
specifies a glossary term. All explicit attributes shall be specified. The
explicit attributes for this type are:

term
    The attribute value shall be a string. It shall be the glossary term.

text
    The attribute value shall be a string. It shall be the definition of the
    glossary term.

.. _SpecTypeInterfaceItemType:

Interface Item Type
^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``interface``. This set of attributes specifies an
interface specification item. Interface items shall specify the interface of
the software product to other software products and the hardware.  Use
:ref:`SpecTypeInterfaceDomainItemType` items to specify interface domains, for
example the :term:`API`, C language, compiler, interfaces to the
implementation, and the hardware. All explicit attributes shall be specified.
The explicit attributes for this type are:

index-entries
    The attribute value shall be a list of strings. It shall be a list of
    additional document index entries.  A document index entry derived from the
    interface name is added automatically.

interface-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    interface item type.

This type is refined by the following types:

* :ref:`SpecTypeApplicationConfigurationGroupItemType`

* :ref:`SpecTypeApplicationConfigurationOptionItemType`

* :ref:`SpecTypeInterfaceCompoundItemType`

* :ref:`SpecTypeInterfaceContainerItemType`

* :ref:`SpecTypeInterfaceDefineItemType`

* :ref:`SpecTypeInterfaceDomainItemType`

* :ref:`SpecTypeInterfaceEnumItemType`

* :ref:`SpecTypeInterfaceEnumeratorItemType`

* :ref:`SpecTypeInterfaceForwardDeclarationItemType`

* :ref:`SpecTypeInterfaceFunctionItemType`

* :ref:`SpecTypeInterfaceGroupItemType`

* :ref:`SpecTypeInterfaceHeaderFileItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

* :ref:`SpecTypeInterfaceTypedefItemType`

* :ref:`SpecTypeInterfaceUnspecifiedItemType`

* :ref:`SpecTypeInterfaceVariableItemType`

.. _SpecTypeApplicationConfigurationGroupItemType:

Application Configuration Group Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``appl-config-group``. This set of
attributes specifies an application configuration group. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
    The attribute value shall be a string. It shall be the description of the
    application configuration group.

name
    The attribute value shall be a string. It shall be human readable name of
    the application configuration group.

text
    The attribute value shall be a :ref:`SpecTypeRequirementText`. It shall
    state the requirement for the application configuration group.

.. _SpecTypeApplicationConfigurationOptionItemType:

Application Configuration Option Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``appl-config-option``. This set
of attributes specifies an application configuration option. All explicit
attributes shall be specified. The explicit attributes for this type are:

appl-config-option-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    application configuration option type.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`. The
    :ref:`SpecTypeApplicationConfigurationValueOptionItemType` items have an
    attribute for constraints.

name
    The attribute value shall be an
    :ref:`SpecTypeApplicationConfigurationOptionName`.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

text
    The attribute value shall be a :ref:`SpecTypeRequirementText`. It shall
    state the requirement for the application configuration option.

This type is refined by the following types:

* :ref:`SpecTypeApplicationConfigurationFeatureEnableOptionItemType`

* :ref:`SpecTypeApplicationConfigurationFeatureOptionItemType`

* :ref:`SpecTypeApplicationConfigurationValueOptionItemType`

.. _SpecTypeApplicationConfigurationFeatureEnableOptionItemType:

Application Configuration Feature Enable Option Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeApplicationConfigurationOptionItemType`
through the ``appl-config-option-type`` attribute if the value is
``feature-enable``. This set of attributes specifies an application
configuration feature enable option.

.. _SpecTypeApplicationConfigurationFeatureOptionItemType:

Application Configuration Feature Option Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeApplicationConfigurationOptionItemType`
through the ``appl-config-option-type`` attribute if the value is ``feature``.
This set of attributes specifies an application configuration feature option.
All explicit attributes shall be specified. The explicit attributes for this
type are:

default
    The attribute value shall be a string. It shall describe what happens if
    the configuration option is undefined.

.. _SpecTypeApplicationConfigurationValueOptionItemType:

Application Configuration Value Option Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the following types:

* :ref:`SpecTypeApplicationConfigurationOptionItemType` through the
  ``appl-config-option-type`` attribute if the value is ``initializer``

* :ref:`SpecTypeApplicationConfigurationOptionItemType` through the
  ``appl-config-option-type`` attribute if the value is ``integer``

This set of attributes specifies application configuration initializer or
integer option. All explicit attributes shall be specified. The explicit
attributes for this type are:

constraints
    The attribute value shall be an
    :ref:`SpecTypeApplicationConfigurationOptionConstraintSet`.

default-value
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. It shall
    shall describe the default value of the application configuration option.

.. _SpecTypeInterfaceCompoundItemType:

Interface Compound Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the following types:

* :ref:`SpecTypeInterfaceItemType` through the ``interface-type`` attribute if
  the value is ``struct``

* :ref:`SpecTypeInterfaceItemType` through the ``interface-type`` attribute if
  the value is ``union``

This set of attributes specifies a compound (struct or union). All explicit
attributes shall be specified. The explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceCompoundMemberDefinitionDirective`.

definition-kind
    The attribute value shall be an
    :ref:`SpecTypeInterfaceCompoundDefinitionKind`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the compound
    (struct or union).

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

.. _SpecTypeInterfaceContainerItemType:

Interface Container Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``container``. Items of this type
specify an interface container.  The item shall have exactly one link with the
:ref:`SpecTypeInterfacePlacementLinkRole` to an
:ref:`SpecTypeInterfaceDomainItemType` item.  This link defines the interface
domain of the container.

.. _SpecTypeInterfaceDefineItemType:

Interface Define Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``define``. This set of attributes
specifies a define. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceDefinitionDirective`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the define.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

.. _SpecTypeInterfaceDomainItemType:

Interface Domain Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``domain``. This set of attributes
specifies an interface domain.  Items of the types
:ref:`SpecTypeInterfaceContainerItemType` and
:ref:`SpecTypeInterfaceHeaderFileItemType` are placed into domains through
links with the :ref:`SpecTypeInterfacePlacementLinkRole`. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
    The attribute value shall be a string. It shall be the description of the
    domain

name
    The attribute value shall be a string. It shall be the human readable name
    of the domain.

.. _SpecTypeInterfaceEnumItemType:

Interface Enum Item Type
^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``enum``. This set of attributes
specifies an enum. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition-kind
    The attribute value shall be an :ref:`SpecTypeInterfaceEnumDefinitionKind`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the enum.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

.. _SpecTypeInterfaceEnumeratorItemType:

Interface Enumerator Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``enumerator``. This set of
attributes specifies an enumerator. All explicit attributes shall be specified.
The explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceDefinitionDirective`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the
    enumerator.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

.. _SpecTypeInterfaceForwardDeclarationItemType:

Interface Forward Declaration Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``forward-declaration``. Items of
this type specify a forward declaration.  The item shall have exactly one link
with the :ref:`SpecTypeInterfaceTargetLinkRole` to an
:ref:`SpecTypeInterfaceCompoundItemType` item.  This link defines the type
declared by the forward declaration.

.. _SpecTypeInterfaceFunctionItemType:

Interface Function Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``function``. This set of
attributes specifies a function. All explicit attributes shall be specified.
The explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceFunctionDefinitionDirective`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the
    function.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

params
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceParameter`.

return
    The attribute value shall be an :ref:`SpecTypeInterfaceReturnDirective`.

.. _SpecTypeInterfaceGroupItemType:

Interface Group Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``group``. This set of attributes
specifies an interface group. All explicit attributes shall be specified. The
explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

identifier
    The attribute value shall be an :ref:`SpecTypeInterfaceGroupIdentifier`.

name
    The attribute value shall be a string. It shall be the human readable name
    of the interface group.

text
    The attribute value shall be a :ref:`SpecTypeRequirementText`. It shall
    state the requirement for the interface group.

.. _SpecTypeInterfaceHeaderFileItemType:

Interface Header File Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``header-file``. This set of
attributes specifies a header file.  The item shall have exactly one link with
the :ref:`SpecTypeInterfacePlacementLinkRole` to an
:ref:`SpecTypeInterfaceDomainItemType` item.  This link defines the interface
domain of the header file. All explicit attributes shall be specified. The
explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

path
    The attribute value shall be a string. It shall be the path used to include
    the header file.  For example :file:`rtems/confdefs.h`.

prefix
    The attribute value shall be a string. It shall be the prefix directory
    path to the header file in the interface domain.  For example
    :file:`cpukit/include`.

.. _SpecTypeInterfaceMacroItemType:

Interface Macro Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``macro``. This set of attributes
specifies a macro. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceDefinitionDirective`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the macro.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

params
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceParameter`.

return
    The attribute value shall be an :ref:`SpecTypeInterfaceReturnDirective`.

.. _SpecTypeInterfaceTypedefItemType:

Interface Typedef Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``typedef``. This set of
attributes specifies a typedef. All explicit attributes shall be specified. The
explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceDefinitionDirective`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the typedef.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

.. _SpecTypeInterfaceUnspecifiedItemType:

Interface Unspecified Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the following types:

* :ref:`SpecTypeInterfaceItemType` through the ``interface-type`` attribute if
  the value is ``unspecified``

* :ref:`SpecTypeInterfaceItemType` through the ``interface-type`` attribute if
  the value is ``unspecified-define``

* :ref:`SpecTypeInterfaceItemType` through the ``interface-type`` attribute if
  the value is ``unspecified-function``

* :ref:`SpecTypeInterfaceItemType` through the ``interface-type`` attribute if
  the value is ``unspecified-type``

This set of attributes specifies an unspecified interface. All explicit
attributes shall be specified. The explicit attributes for this type are:

name
    The attribute value shall be a string. It shall be the name of the
    unspecified interface.

reference
    The attribute value shall be an optional string. If the value is present,
    then it shall be an URL to the standard or specification of the interface.

.. _SpecTypeInterfaceVariableItemType:

Interface Variable Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceItemType` through the
``interface-type`` attribute if the value is ``variable``. This set of
attributes specifies a variable. All explicit attributes shall be specified.
The explicit attributes for this type are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceDefinitionDirective`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

name
    The attribute value shall be a string. It shall be the name of the
    variable.

notes
    The attribute value shall be an :ref:`SpecTypeInterfaceNotes`.

.. _SpecTypeRequirementItemType:

Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``requirement``. This set of attributes specifies a
requirement. All explicit attributes shall be specified. The explicit
attributes for this type are:

rationale
    The attribute value shall be an optional string. If the value is present,
    then it shall state the rationale or justification of the requirement.

references
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeRequirementReference`.

requirement-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    requirement item type.

text
    The attribute value shall be a :ref:`SpecTypeRequirementText`. It shall
    state the requirement.

This type is refined by the following types:

* :ref:`SpecTypeFunctionalRequirementItemType`

* :ref:`SpecTypeNonFunctionalRequirementItemType`

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de
    enabled-by: true
    functional-type: capability
    links: []
    rationale: |
      It keeps you busy.
    requirement-type: functional
    text: |
      The system shall do crazy things.
    type: requirement

.. _SpecTypeFunctionalRequirementItemType:

Functional Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRequirementItemType` through the
``requirement-type`` attribute if the value is ``functional``. This set of
attributes specifies a functional requirement. All explicit attributes shall be
specified. The explicit attributes for this type are:

functional-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    functional type of the requirement.

This type is refined by the following types:

* :ref:`SpecTypeActionRequirementItemType`

* :ref:`SpecTypeGenericFunctionalRequirementItemType`

.. _SpecTypeActionRequirementItemType:

Action Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeFunctionalRequirementItemType` through the
``functional-type`` attribute if the value is ``action``. This set of
attributes specifies functional requirements and corresponding validation test
code.  The functional requirements of an action are specified.  An action
performs a step in a finite state machine.  An action is implemented through a
function or a macro.  The action is performed through a call of the function or
an execution of the code of a macro expansion by an actor.  The actor is for
example a task or an interrupt service routine.

For action requirements which specify the function of an interface, there shall
be exactly one link with the :ref:`SpecTypeInterfaceFunctionLinkRole` to the
interface of the action.

The action requirements are specified by

* a list of pre-conditions, each with a set of states,

* a list of post-conditions, each with a set of states,

* the transition of pre-condition states to post-condition states through the
  action.

Along with the requirements, the test code to generate a validation test is
specified.  For an action requirement it is verified that all variations of
pre-condition states have a set of post-condition states specified in the
transition map.  All transitions are covered by the generated test code. All
explicit attributes shall be specified. The explicit attributes for this type
are:

post-conditions
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeActionRequirementCondition`.

pre-conditions
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeActionRequirementCondition`.

skip-reasons
    The attribute value shall be an
    :ref:`SpecTypeActionRequirementSkipReasons`.

test-action
    The attribute value shall be a string. It shall be the test action code.

test-brief
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case brief description.

test-cleanup
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test cleanup code.  The code is placed in the test
    action loop body after the test post-condition checks.

test-context
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeTestContextMember`.

test-context-support
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test context support code.  The context support code
    is placed at file scope before the test context definition.

test-description
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case description.

test-header
    The attribute value shall be a :ref:`SpecTypeTestHeader`.

test-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include <...>``.

test-local-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include "..."``.

test-prepare
    The attribute value shall be an optional string. If the value is present,
    then it shall be the early test preparation code.  The code is placed in
    the test action loop body before the test pre-condition preparations.

test-setup
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`.

test-stop
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`.

test-support
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case support code. The support code is placed at
    file scope before the test case code.

test-target
    The attribute value shall be a string. It shall be the path to the
    generated test case source file.

test-teardown
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`.

transition-map
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeActionRequirementTransition`.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    functional-type: action
    links: []
    post-conditions:
    - name: Status
      states:
      - name: Success
        test-code: |
          /* Check that the status is SUCCESS */
        text: |
          The status shall be SUCCESS.
      - name: Error
        test-code: |
          /* Check that the status is ERROR */
        text: |
          The status shall be ERROR.
      test-epilogue: null
      test-prologue: null
    - name: Data
      states:
      - name: Unchanged
        test-code: |
          /* Check that the data is unchanged */
        text: |
          The data shall be unchanged by the action.
      - name: Red
        test-code: |
          /* Check that the data is red */
        text: |
          The data shall be red.
      - name: Green
        test-code: |
          /* Check that the data is green */
        text: |
          The data shall be green.
      test-epilogue: null
      test-prologue: null
    pre-conditions:
    - name: Data
      states:
      - name: NullPtr
        test-code: |
          /* Set data pointer to NULL */
        text: |
          The data pointer shall be NULL.
      - name: Valid
        test-code: |
          /* Set data pointer to reference a valid data buffer */
        text: |
          The data pointer shall reference a valid data buffer.
      test-epilogue: null
      test-prologue: null
    - name: Option
      states:
      - name: Red
        test-code: |
          /* Set option to RED */
        text: |
          The option shall be RED.
      - name: Green
        test-code: |
          /* Set option to GREEN */
        text: |
          The option shall be GREEN.
      test-epilogue: null
      test-prologue: null
    requirement-type: functional
    skip-reasons: {}
    test-action: |
      /* Call the function of the action */
    test-brief: null
    test-cleanup: null
    test-context:
    - brief: null
      description: null
      member: void *data
    - brief: null
      description: null
      member: option_type option
    test-context-support: null
    test-description: null
    test-header: null
    test-includes: []
    test-local-includes: []
    test-prepare: null
    test-setup: null
    test-stop: null
    test-support: null
    test-target: tc-red-green-data.c
    test-teardown: null
    transition-map:
    - enabled-by: true
      post-conditions:
        Status: Error
        Data: Unchanged
      pre-conditions:
        Data: NullPtr
        Option: all
    - enabled-by: true
      post-conditions:
        Status: Success
        Data: Red
      pre-conditions:
        Data: Valid
        Option: Red
    - enabled-by: true
      post-conditions:
        Status: Success
        Data: Green
      pre-conditions:
        Data: Valid
        Option: Green
    rationale: null
    references: []
    text: |
      ${.:/text-template}
    type: requirement

.. _SpecTypeGenericFunctionalRequirementItemType:

Generic Functional Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the following types:

* :ref:`SpecTypeFunctionalRequirementItemType` through the ``functional-type``
  attribute if the value is ``capability``

* :ref:`SpecTypeFunctionalRequirementItemType` through the ``functional-type``
  attribute if the value is ``dependability-function``

* :ref:`SpecTypeFunctionalRequirementItemType` through the ``functional-type``
  attribute if the value is ``function``

* :ref:`SpecTypeFunctionalRequirementItemType` through the ``functional-type``
  attribute if the value is ``operational``

* :ref:`SpecTypeFunctionalRequirementItemType` through the ``functional-type``
  attribute if the value is ``safety-function``

Items of this type state a functional requirement with the functional type
defined by the specification type refinement.

.. _SpecTypeNonFunctionalRequirementItemType:

Non-Functional Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRequirementItemType` through the
``requirement-type`` attribute if the value is ``non-functional``. This set of
attributes specifies a non-functional requirement. All explicit attributes
shall be specified. The explicit attributes for this type are:

non-functional-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    non-functional type of the requirement.

This type is refined by the following types:

* :ref:`SpecTypeDesignGroupRequirementItemType`

* :ref:`SpecTypeGenericNonFunctionalRequirementItemType`

* :ref:`SpecTypeRuntimePerformanceRequirementItemType`

.. _SpecTypeDesignGroupRequirementItemType:

Design Group Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeNonFunctionalRequirementItemType` through
the ``non-functional-type`` attribute if the value is ``design-group``. This
set of attributes specifies a design group requirement.  Design group
requirements have an explicit reference to the associated Doxygen group
specified by the ``identifier`` attribute.  Design group requirements have an
implicit validation by inspection method.  The qualification toolchain shall
perform the inspection and check that the specified Doxygen group exists in the
software source code. All explicit attributes shall be specified. The explicit
attributes for this type are:

identifier
    The attribute value shall be an :ref:`SpecTypeInterfaceGroupIdentifier`.

.. _SpecTypeGenericNonFunctionalRequirementItemType:

Generic Non-Functional Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the following types:

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``build-configuration``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``constraint``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``design``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``documentation``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``interface``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``interface-requirement``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``maintainability``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``performance``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``portability``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``quality``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``reliability``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``resource``

* :ref:`SpecTypeNonFunctionalRequirementItemType` through the
  ``non-functional-type`` attribute if the value is ``safety``

Items of this type state a non-functional requirement with the non-functional
type defined by the specification type refinement.

.. _SpecTypeRuntimePerformanceRequirementItemType:

Runtime Performance Requirement Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeNonFunctionalRequirementItemType` through
the ``non-functional-type`` attribute if the value is ``performance-runtime``.
The item shall have exactly one link with the
:ref:`SpecTypeRuntimeMeasurementRequestLinkRole`.  A requirement text processor
shall support a substitution of ${.:/limit-kind}:

* For a :ref:`SpecTypeRuntimeMeasurementValueKind` of ``min-lower-bound`` or
  ``min-upper-bound``, the substitution of ${.:/limit-kind} shall be
  ``"minimum"``.

* For a :ref:`SpecTypeRuntimeMeasurementValueKind` of ``mean-lower-bound`` or
  ``mean-upper-bound``, the substitution of ${.:/limit-kind} shall be
  ``"mean"``.

* For a :ref:`SpecTypeRuntimeMeasurementValueKind` of ``max-lower-bound`` or
  ``max-upper-bound``, the substitution of ${.:/limit-kind} shall be
  ``"maximum"``.

A requirement text processor shall support a substitution of
${.:/limit-condition}:

* For a :ref:`SpecTypeRuntimeMeasurementValueKind` of ``min-lower-bound``,
  ``mean-lower-bound``, or ``max-lower-bound``, the substitution of
  ${.:/limit-condition} shall be ``"greater than or equal to <value>"`` with
  <value> being the value of the corresponding entry in the
  :ref:`SpecTypeRuntimeMeasurementValueTable`.

* For a :ref:`SpecTypeRuntimeMeasurementValueKind` of ``min-upper-bound``,
  ``mean-upper-bound``, or ``max-upper-bound``, the substitution of
  ${.:/limit-condition} shall be ``"less than or equal to <value>"`` with
  <value> being the value of the corresponding entry in the
  :ref:`SpecTypeRuntimeMeasurementValueTable`.

A requirement text processor shall support a substitution of ${.:/environment}.
The value of the substitution shall be ``"<environment> environment"`` with
<environment> being the environment of the corresponding entry in the
:ref:`SpecTypeRuntimeMeasurementEnvironmentTable`.

This set of attributes specifies a runtime performance requirement. Along with
the requirement, the validation test code to execute a measure runtime request
is specified. All explicit attributes shall be specified. The explicit
attributes for this type are:

limits
    The attribute value shall be a :ref:`SpecTypeRuntimePerformanceLimitTable`.

params
    The attribute value shall be a
    :ref:`SpecTypeRuntimePerformanceParameterSet`.

test-body
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. It shall
    provide the code of the measure runtime body handler.  In contrast to other
    methods, this method is mandatory.

test-cleanup
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. It may
    provide the code to clean up the measure runtime request. This method is
    called before the cleanup method of the corresponding
    :ref:`SpecTypeRuntimeMeasurementTestItemType` item and after the request.

test-prepare
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. It may
    provide the code to prepare the measure runtime request.  This method is
    called after the prepare method of the corresponding
    :ref:`SpecTypeRuntimeMeasurementTestItemType` item and before the request.

test-setup
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. It may
    provide the code of the measure runtime setup handler.

test-teardown
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. It may
    provide the code of the measure runtime teardown handler.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    links:
    - role: runtime-measurement-request
      uid: ../val/performance
    limits:
      sparc/leon3:
        DirtyCache:
          max-upper-bound: 0.000005
          mean-upper-bound: 0.000005
        FullCache:
          max-upper-bound: 0.000005
          mean-upper-bound: 0.000005
        HotCache:
          max-upper-bound: 0.000005
          mean-upper-bound: 0.000005
        Load/1:
          max-upper-bound: 0.00001
          mean-upper-bound: 0.00001
        Load/2:
          max-upper-bound: 0.00001
          mean-upper-bound: 0.00001
        Load/3:
          max-upper-bound: 0.00001
          mean-upper-bound: 0.00001
        Load/4:
          max-upper-bound: 0.00001
          mean-upper-bound: 0.00001
    params: {}
    rationale: null
    references: []
    test-body:
      brief: |
        Get a buffer.
      code: |
        ctx->status = rtems_partition_get_buffer( ctx->part_many, &ctx->buffer );
      description: null
    test-cleanup: null
    test-prepare: null
    test-setup: null
    test-teardown:
      brief: |
        Return the buffer.
      code: |
        rtems_status_code sc;

        T_quiet_rsc_success( ctx->status );

        sc = rtems_partition_return_buffer( ctx->part_many, ctx->buffer );
        T_quiet_rsc_success( sc );

        return tic == toc;
      description: null
    text: |
      When a partition has exactly ${../val/performance:/params/buffer-count} free
      buffers, the ${.:limit-kind} runtime of exactly
      ${../val/performance:/params/sample-count} successful calls to
      ${../if/get-buffer:/name} in the ${.:/environment} shall be
      ${.:limit-condition}.
    non-functional-type: performance-runtime
    requirement-type: non-functional
    type: requirement

.. _SpecTypeRequirementValidationItemType:

Requirement Validation Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``validation``. This set of attributes provides a
requirement validation evidence.  The item shall have exactly one link to the
validated requirement with the :ref:`SpecTypeRequirementValidationLinkRole`.
All explicit attributes shall be specified. The explicit attributes for this
type are:

method
    The attribute value shall be a :ref:`SpecTypeRequirementValidationMethod`.
    Validation by test is done through :ref:`SpecTypeTestCaseItemType` items.

text
    The attribute value shall be a string. It shall provide the validation
    evidence depending on the validation method:

    * *By analysis*: A statement shall be provided how the requirement is met,
      by analysing static properties of the :term:`software product`.

    * *By inspection*: A statement shall be provided how the requirement is
      met, by inspection of the :term:`source code`.

    * *By review of design*: A rationale shall be provided to demonstrate how
      the requirement is satisfied implicitly by the software design.

.. _SpecTypeRuntimeMeasurementTestItemType:

Runtime Measurement Test Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``runtime-measurement-test``. This set of attributes
specifies a runtime measurement test case. All explicit attributes shall be
specified. The explicit attributes for this type are:

params
    The attribute value shall be a
    :ref:`SpecTypeRuntimeMeasurementParameterSet`.

test-brief
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case brief description.

test-cleanup
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. If the
    value is present, then it shall be the measure runtime request cleanup
    method.  The method is called after each measure runtime request.

test-context
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeTestContextMember`.

test-context-support
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test context support code.  The context support code
    is placed at file scope before the test context definition.

test-description
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case description.

test-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include <...>``.

test-local-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include "..."``.

test-prepare
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. If the
    value is present, then it shall be the measure runtime request prepare
    method.  The method is called before each measure runtime request.

test-setup
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. If the
    value is present, then it shall be the test case setup fixture method.

test-stop
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. If the
    value is present, then it shall be the test case stop fixture method.

test-support
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case support code. The support code is placed at
    file scope before the test case code.

test-target
    The attribute value shall be a string. It shall be the path to the
    generated test case source file.

test-teardown
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`. If the
    value is present, then it shall be the test case teardown fixture method.

.. _SpecTypeSpecificationItemType:

Specification Item Type
^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``spec``. This set of attributes specifies
specification types. All explicit attributes shall be specified. The explicit
attributes for this type are:

spec-description
    The attribute value shall be an optional string. It shall be the
    description of the specification type.

spec-example
    The attribute value shall be an optional string. If the value is present,
    then it shall be an example of the specification type.

spec-info
    The attribute value shall be a :ref:`SpecTypeSpecificationInformation`.

spec-name
    The attribute value shall be an optional string. It shall be the human
    readable name of the specification type.

spec-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall the
    specification type.

Please have a look at the following example:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    links:
    - role: spec-member
      uid: root
    - role: spec-refinement
      spec-key: type
      spec-value: example
      uid: root
    spec-description: null
    spec-example: null
    spec-info:
      dict:
        attributes:
          an-example-attribute:
            description: |
              It shall be an example.
            spec-type: optional-str
          example-number:
            description: |
              It shall be the example number.
            spec-type: int
        description: |
          This set of attributes specifies an example.
        mandatory-attributes: all
    spec-name: Example Item Type
    spec-type: spec
    type: spec

.. _SpecTypeTestCaseItemType:

Test Case Item Type
^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``test-case``. This set of attributes specifies a
test case. All explicit attributes shall be specified. The explicit attributes
for this type are:

test-actions
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeTestCaseAction`.

test-brief
    The attribute value shall be a string. It shall be the test case brief
    description.

test-context
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeTestContextMember`.

test-context-support
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test context support code.  The context support code
    is placed at file scope before the test context definition.

test-description
    The attribute value shall be an optional string. It shall be the test case
    description.

test-header
    The attribute value shall be a :ref:`SpecTypeTestHeader`.

test-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include <...>``.

test-local-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include "..."``.

test-setup
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`.

test-stop
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`.

test-support
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test case support code. The support code is placed at
    file scope before the test case code.

test-target
    The attribute value shall be a string. It shall be the path to the
    generated target test case source file.

test-teardown
    The attribute value shall be a :ref:`SpecTypeTestSupportMethod`.

.. _SpecTypeTestPlatformItemType:

Test Platform Item Type
^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``test-platform``. Please note:

.. warning::

     This item type is work in progress.

This set of attributes specifies a test platform. All explicit attributes shall
be specified. The explicit attributes for this type are:

description
    The attribute value shall be a string. It shall be the description of the
    test platform.

name
    The attribute value shall be a string. It shall be the human readable name
    of the test platform.

.. _SpecTypeTestProcedureItemType:

Test Procedure Item Type
^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``test-procedure``. Please note:

.. warning::

     This item type is work in progress.

This set of attributes specifies a test procedure. All explicit attributes
shall be specified. The explicit attributes for this type are:

name
    The attribute value shall be a string. It shall be the human readable name
    of the test procedure.

purpose
    The attribute value shall be a string. It shall state the purpose of the
    test procedure.

steps
    The attribute value shall be a string. It shall describe the steps of the
    test procedure execution.

.. _SpecTypeTestSuiteItemType:

Test Suite Item Type
^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeRootItemType` through the ``type``
attribute if the value is ``test-suite``. This set of attributes specifies a
test suite. All explicit attributes shall be specified. The explicit attributes
for this type are:

test-brief
    The attribute value shall be a string. It shall be the test suite brief
    description.

test-code
    The attribute value shall be a string. It shall be the test suite code.
    The test suite code is placed at file scope in the target source file.

test-description
    The attribute value shall be an optional string. It shall be the test suite
    description.

test-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include <...>``.

test-local-includes
    The attribute value shall be a list of strings. It shall be a list of
    header files included via ``#include "..."``.

test-target
    The attribute value shall be a string. It shall be the path to the
    generated target test suite source file.

.. _ReqEngSpecificationAttributeSetsAndValueTypes:

Specification Attribute Sets and Value Types
--------------------------------------------

.. _SpecTypeActionRequirementCondition:

Action Requirement Condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines an action pre-condition or post-condition. All
explicit attributes shall be specified. The explicit attributes for this type
are:

name
    The attribute value shall be an :ref:`SpecTypeActionRequirementName`.

states
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeActionRequirementState`.

test-epilogue
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test epilogue code. The epilogue code is placed in the
    test condition preparation or check before the state-specific code.  The
    code may use a local variable ``ctx`` which points to the test context, see
    :ref:`SpecTypeTestContextMember`.

test-prologue
    The attribute value shall be an optional string. If the value is present,
    then it shall be the test prologue code. The prologue code is placed in the
    test condition preparation or check after the state-specific code.  The
    code may use a local variable ``ctx`` which points to the test context, see
    :ref:`SpecTypeTestContextMember`.

This type is used by the following types:

* :ref:`SpecTypeActionRequirementItemType`

.. _SpecTypeActionRequirementName:

Action Requirement Name
^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be the name of a condition or a state of
a condition used to define pre-conditions and post-conditions of an action
requirement.  It shall be formatted in CamelCase.  It should be brief and
abbreviated. The rationale for this is that the names are used in tables and
the horizontal space is limited by the page width.  The more conditions you
have in an action requirement, the shorter the names should be.  The name
``NA`` is reserved and indicates that a condition is not applicable. The value

* shall match with the regular expression "``^[A-Z][a-zA-Z0-9]+$``",

* and, shall be not equal to "``NA``".

This type is used by the following types:

* :ref:`SpecTypeActionRequirementCondition`

* :ref:`SpecTypeActionRequirementSkipReasons`

* :ref:`SpecTypeActionRequirementState`

* :ref:`SpecTypeActionRequirementTransitionPostConditions`

* :ref:`SpecTypeActionRequirementTransitionPreConditions`

.. _SpecTypeActionRequirementSkipReasons:

Action Requirement Skip Reasons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies skip reasons used to justify why transitions
in the transition map are skipped. Generic attributes may be specified. Each
generic attribute key shall be an :ref:`SpecTypeActionRequirementName`. Each
generic attribute value shall be a string. The key defines the name of a skip
reason.  The name can be used in
:ref:`SpecTypeActionRequirementTransitionPostConditions` to skip the
corresponding transitions.  The value shall give a reason why the transitions
are skipped.

This type is used by the following types:

* :ref:`SpecTypeActionRequirementItemType`

.. _SpecTypeActionRequirementState:

Action Requirement State
^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines an action pre-condition or post-condition state.
All explicit attributes shall be specified. The explicit attributes for this
type are:

name
    The attribute value shall be an :ref:`SpecTypeActionRequirementName`.

test-code
    The attribute value shall be a string. It shall be the test code to prepare
    or check the state of the condition.  The code may use a local variable
    ``ctx`` which points to the test context, see
    :ref:`SpecTypeTestContextMember`.

text
    The attribute value shall be a :ref:`SpecTypeRequirementText`. It shall
    define the state of the condition.

This type is used by the following types:

* :ref:`SpecTypeActionRequirementCondition`

.. _SpecTypeActionRequirementTransition:

Action Requirement Transition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines the transition from multiple sets of states of
pre-conditions to a set of states of post-conditions through an action in an
action requirement.  The ability to specify multiple sets of states of
pre-conditions which result in a common set of post-conditions may allow a more
compact specification of the transition map.  For example, let us suppose you
want to specify the action of a function with a pointer parameter.  The
function performs an early check that the pointer is NULL and in this case
returns an error code.  The pointer condition dominates the action outcome if
the pointer is NULL.  Other pre-condition states can be simply set to ``all``
for this transition. All explicit attributes shall be specified. The explicit
attributes for this type are:

enabled-by
    The attribute value shall be an :ref:`SpecTypeEnabledByExpression`. The
    transition map may be customized to support configuration variants through
    this attribute.  The default transitions (``enabled-by: true``) shall be
    specified before the customized variants in the list.

post-conditions
    The attribute value shall be an
    :ref:`SpecTypeActionRequirementTransitionPostConditions`.

pre-conditions
    The attribute value shall be an
    :ref:`SpecTypeActionRequirementTransitionPreConditions`.

This type is used by the following types:

* :ref:`SpecTypeActionRequirementItemType`

.. _SpecTypeActionRequirementTransitionPostConditions:

Action Requirement Transition Post-Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. This set of attributes defines for each
  post-condition the state after the action for a transition in an action
  requirement. Generic attributes may be specified. Each generic attribute key
  shall be an :ref:`SpecTypeActionRequirementName`. Each generic attribute
  value shall be an :ref:`SpecTypeActionRequirementName`. There shall be
  exactly one generic attribute key for each post-condition.  The key name
  shall be the post-condition name.  The value of each generic attribute shall
  be the state of the post-condition.

* The value may be a string. It shall be the name of a skip reason.  If a skip
  reason is given instead of a listing of post-condition states, then this
  transition is skipped and no test code runs for this transition. The value

  * shall match with the regular expression "``^[A-Z][a-zA-Z0-9]+$``",

  * and, shall be not equal to "``NA``".

This type is used by the following types:

* :ref:`SpecTypeActionRequirementTransition`

.. _SpecTypeActionRequirementTransitionPreConditionStateSet:

Action Requirement Transition Pre-Condition State Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a list. Each list element shall be an
  :ref:`SpecTypeActionRequirementName`. The list defines the set of states of
  the pre-condition in the transition.

* The value may be a string. The value ``all`` represents all states of the
  pre-condition in this transition.  The value ``N/A`` marks the pre-condition
  as not applicable in this transition. The value shall be an element of

  * "``all``", and

  * "``N/A``".

This type is used by the following types:

* :ref:`SpecTypeActionRequirementTransitionPreConditions`

.. _SpecTypeActionRequirementTransitionPreConditions:

Action Requirement Transition Pre-Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines for each pre-condition the set of states before
the action for a transition in an actin requirement. Generic attributes may be
specified. Each generic attribute key shall be an
:ref:`SpecTypeActionRequirementName`. Each generic attribute value shall be an
:ref:`SpecTypeActionRequirementTransitionPreConditionStateSet`. There shall be
exactly one generic attribute key for each pre-condition.  The key name shall
be the pre-condition name.  The value of each generic attribute shall be a set
of states of the pre-condition.

This type is used by the following types:

* :ref:`SpecTypeActionRequirementTransition`

.. _SpecTypeApplicationConfigurationGroupMemberLinkRole:

Application Configuration Group Member Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``appl-config-group-member``. It defines the application configuration
group membership role of links.

.. _SpecTypeApplicationConfigurationOptionConstraintSet:

Application Configuration Option Constraint Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines application configuration option constraints.
Additional constraints can be added through the links of the item using the
:ref:`SpecTypeConstraintLinkRole`. None of the explicit attributes is
mandatory, they are all optional. The explicit attributes for this type are:

max
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. It shall be
    the maximum value of the application configuration option.

min
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. It shall be
    the minimum value of the application configuration option.

set
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeIntegerOrString`. It shall be the set of valid values for the
    application configuration option.

texts
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeRequirementText`. It shall be a list of constraints specific
    to this application configuration option.  For general constraints, use a
    link with the :ref:`SpecTypeConstraintLinkRole` to a constraint item.

This type is used by the following types:

* :ref:`SpecTypeApplicationConfigurationValueOptionItemType`

.. _SpecTypeApplicationConfigurationOptionName:

Application Configuration Option Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be the name of an application
configuration option. The value shall match with the regular expression
"``^(CONFIGURE_|BSP_)[A-Z0-9_]+$``".

This type is used by the following types:

* :ref:`SpecTypeApplicationConfigurationOptionItemType`

.. _SpecTypeBooleanOrIntegerOrString:

Boolean or Integer or String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a boolean.

* The value may be an integer number.

* The value may be a string.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionAction`

* :ref:`SpecTypeInterfaceReturnValue`

.. _SpecTypeBuildAssemblerOption:

Build Assembler Option
^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an option for the assembler.  The
options are used to assemble the sources of this item.  The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildStartFileItemType`

.. _SpecTypeBuildCCompilerOption:

Build C Compiler Option
^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an option for the C compiler.  The
options are used to compile the sources of this item.  The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildBSPItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

* :ref:`SpecTypeBuildOptionCCompilerCheckAction`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildCPreprocessorOption:

Build C Preprocessor Option
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an option for the C preprocessor.  The
options are used to preprocess the sources of this item.  The options defined
by this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildBSPItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildStartFileItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildCXXCompilerOption:

Build C++ Compiler Option
^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an option for the C++ compiler.  The
options are used to compile the sources of this item.  The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

* :ref:`SpecTypeBuildOptionCXXCompilerCheckAction`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildDependencyLinkRole:

Build Dependency Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``build-dependency``. It defines the build dependency role of links.

.. _SpecTypeBuildIncludePath:

Build Include Path
^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be a path to header files.  The path is
used by the C preprocessor to search for header files.  It succeeds the
includes presented to the item by the build item context.  For an
:ref:`SpecTypeBuildGroupItemType` item the includes are visible to all items
referenced by the group item.  For :ref:`SpecTypeBuildBSPItemType`,
:ref:`SpecTypeBuildObjectsItemType`, :ref:`SpecTypeBuildLibraryItemType`,
:ref:`SpecTypeBuildStartFileItemType`, and
:ref:`SpecTypeBuildTestProgramItemType` items the includes are only visible to
the sources specified by the item itself and they do not propagate to
referenced items.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildBSPItemType`

* :ref:`SpecTypeBuildGroupItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildStartFileItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildInstallDirective:

Build Install Directive
^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies files installed by a build item. All explicit
attributes shall be specified. The explicit attributes for this type are:

destination
    The attribute value shall be a string. It shall be the install destination
    directory.

source
    The attribute value shall be a list of strings. It shall be the list of
    source files to be installed in the destination directory.  The path to a
    source file shall be relative to the directory of the :file:`wscript`.

This type is used by the following types:

* :ref:`SpecTypeBuildBSPItemType`

* :ref:`SpecTypeBuildGroupItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

.. _SpecTypeBuildInstallPath:

Build Install Path
^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string. It shall be the installation path of a
  :ref:`SpecTypeBuildTarget`.

This type is used by the following types:

* :ref:`SpecTypeBuildConfigurationFileItemType`

* :ref:`SpecTypeBuildConfigurationHeaderItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildStartFileItemType`

.. _SpecTypeBuildLinkStaticLibraryDirective:

Build Link Static Library Directive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an external static library identifier.
The library is used to link programs referenced by this item, e.g. ``m`` for
``libm.a``.  The library is added to the build command through the ``stlib``
attribute. It shall not be used for internal static libraries.  Internal static
libraries shall be specified through the ``use-after`` and ``use-before``
attributes to enable a proper build dependency tracking.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildLinkerOption:

Build Linker Option
^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an option for the linker.  The options
are used to link executables.  The options defined by this attribute succeed
the options presented to the item by the build item context.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildOptionAction:

Build Option Action
^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a build option action. Exactly one of the
explicit attributes shall be specified. The explicit attributes for this type
are:

append-test-cppflags
    The attribute value shall be a string. It shall be the name of a test
    program.  The action appends the action value to the ``CPPFLAGS`` of the
    test program.  The name shall correspond to the name of a
    :ref:`SpecTypeBuildTestProgramItemType` item. Due to the processing order
    of items, there is no way to check if the name specified by the attribute
    value is valid.

assert-aligned
    The attribute value shall be an integer number. The action asserts that the
    action value is aligned according to the attribute value.

assert-eq
    The attribute value shall be a :ref:`SpecTypeBooleanOrIntegerOrString`. The
    action asserts that the action value is equal to the attribute value.

assert-ge
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. The action
    asserts that the action value is greater than or equal to the attribute
    value.

assert-gt
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. The action
    asserts that the action value is greater than the attribute value.

assert-int16
    The attribute shall have no value. The action asserts that the action value
    is a valid signed 16-bit integer.

assert-int32
    The attribute shall have no value. The action asserts that the action value
    is a valid signed 32-bit integer.

assert-int64
    The attribute shall have no value. The action asserts that the action value
    is a valid signed 64-bit integer.

assert-int8
    The attribute shall have no value. The action asserts that the action value
    is a valid signed 8-bit integer.

assert-le
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. The action
    asserts that the action value is less than or equal to the attribute value.

assert-lt
    The attribute value shall be an :ref:`SpecTypeIntegerOrString`. The action
    asserts that the action value is less than the attribute value.

assert-ne
    The attribute value shall be a :ref:`SpecTypeBooleanOrIntegerOrString`. The
    action asserts that the action value is not equal to the attribute value.

assert-power-of-two
    The attribute shall have no value. The action asserts that the action value
    is a power of two.

assert-uint16
    The attribute shall have no value. The action asserts that the action value
    is a valid unsigned 16-bit integer.

assert-uint32
    The attribute shall have no value. The action asserts that the action value
    is a valid unsigned 32-bit integer.

assert-uint64
    The attribute shall have no value. The action asserts that the action value
    is a valid unsigned 64-bit integer.

assert-uint8
    The attribute shall have no value. The action asserts that the action value
    is a valid unsigned 8-bit integer.

check-cc
    The attribute value shall be a
    :ref:`SpecTypeBuildOptionCCompilerCheckAction`.

check-cxx
    The attribute value shall be a
    :ref:`SpecTypeBuildOptionCXXCompilerCheckAction`.

define
    The attribute value shall be an optional string. The action adds a define
    to the configuration set.  If the attribute value is present, then it is
    used as the name of the define, otherwise the ``name`` of the item is used.
    The value of the define is the action value.  If the action value is a
    string, then it is quoted.

define-condition
    The attribute value shall be an optional string. The action adds a
    conditional define to the configuration set.  If the attribute value is
    present, then it is used as the name of the define, otherwise the ``name``
    of the item is used.  The value of the define is the action value.

define-unquoted
    The attribute value shall be an optional string. The action adds a define
    to the configuration set.  If the attribute value is present, then it is
    used as the name of the define, otherwise the ``name`` of the item is used.
    The value of the define is the action value.  If the action value is a
    string, then it is not quoted.

env-append
    The attribute value shall be an optional string. The action appends the
    action value to an environment of the configuration set.  If the attribute
    value is present, then it is used as the name of the environment variable,
    otherwise the ``name`` of the item is used.

env-assign
    The attribute value shall be an optional string. The action assigns the
    action value to an environment of the configuration set.  If the attribute
    value is present, then it is used as the name of the environment variable,
    otherwise the ``name`` of the item is used.

env-enable
    The attribute value shall be an optional string. If the action value is
    true, then a name is appended to the ``ENABLE`` environment variable of the
    configuration set.  If the attribute value is present, then it is used as
    the name, otherwise the ``name`` of the item is used.

find-program
    The attribute shall have no value. The action tries to find the program
    specified by the action value. Uses the ``${PATH}`` to find the program.
    Returns the result of the find operation, e.g. a path to the program.

find-tool
    The attribute shall have no value. The action tries to find the tool
    specified by the action value. Uses the tool paths specified by the
    ``--rtems-tools`` command line option.  Returns the result of the find
    operation, e.g. a path to the program.

format-and-define
    The attribute value shall be an optional string. The action adds a define
    to the configuration set.  If the attribute value is present, then it is
    used as the name of the define, otherwise the ``name`` of the item is used.
    The value of the define is the action value.  The value is formatted
    according to the ``format`` attribute value.

get-boolean
    The attribute shall have no value. The action gets the action value for
    subsequent actions from a configuration file variable named by the items
    ``name`` attribute. If no such variable exists in the configuration file,
    then the default value is used.  The value is converted to a boolean.

get-env
    The attribute value shall be a string. The action gets the action value for
    subsequent actions from the environment variable of the configuration set
    named by the attribute value.

get-integer
    The attribute shall have no value. The action gets the action value for
    subsequent actions from a configuration file variable named by the items
    ``name`` attribute. If no such variable exists in the configuration file,
    then the default value is used.  The value is converted to an integer.

get-string
    The attribute shall have no value. The action gets the action value for
    subsequent actions from a configuration file variable named by the items
    ``name`` attribute. If no such variable exists in the configuration file,
    then the default value is used.  The value is converted to a string.

script
    The attribute value shall be a string. The action executes the attribute
    value with the Python ``eval()`` function in the context of the script
    action handler.

set-test-state
    The attribute value shall be a
    :ref:`SpecTypeBuildOptionSetTestStateAction`.

set-value
    The attribute value shall be a :ref:`SpecTypeBuildOptionValue`. The action
    sets the action value for subsequent actions to the attribute value.

split
    The attribute shall have no value. The action splits the action value.

substitute
    The attribute shall have no value. The action performs a ``${VARIABLE}``
    substitution on the action value.  Use ``$$`` for a plain ``$`` character.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionItemType`

.. _SpecTypeBuildOptionCCompilerCheckAction:

Build Option C Compiler Check Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a check done using the C compiler. All
explicit attributes shall be specified. The explicit attributes for this type
are:

cflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCCompilerOption`.

fragment
    The attribute value shall be a string. It shall be a code fragment used to
    check the availability of a certain feature through compilation with the C
    compiler.  The resulting object is not linked to an executable.

message
    The attribute value shall be a string. It shall be a description of the
    feature to check.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionAction`

.. _SpecTypeBuildOptionCXXCompilerCheckAction:

Build Option C++ Compiler Check Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a check done using the C++ compiler. All
explicit attributes shall be specified. The explicit attributes for this type
are:

cxxflags
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeBuildCXXCompilerOption`.

fragment
    The attribute value shall be a string. It shall be a code fragment used to
    check the availability of a certain feature through compilation with the
    C++ compiler.  The resulting object is not linked to an executable.

message
    The attribute value shall be a string. It shall be a description of the
    feature to check.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionAction`

.. _SpecTypeBuildOptionDefaultByVariant:

Build Option Default by Variant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies build option default values by variant. All
explicit attributes shall be specified. The explicit attributes for this type
are:

value
    The attribute value shall be a :ref:`SpecTypeBuildOptionValue`. It value
    shall be the default value for the matching variants.

variants
    The attribute value shall be a list of strings. It shall be a list of
    Python regular expression matching with the desired variants.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionItemType`

.. _SpecTypeBuildOptionName:

Build Option Name
^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be the name of the build option. The
value shall match with the regular expression "``^[a-zA-Z_][a-zA-Z0-9_]*$``".

This type is used by the following types:

* :ref:`SpecTypeBuildOptionItemType`

.. _SpecTypeBuildOptionSetTestStateAction:

Build Option Set Test State Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies test states for a set of test programs.
Generic attributes may be specified. Each generic attribute key shall be a
:ref:`SpecTypeName`. Each generic attribute value shall be a
:ref:`SpecTypeBuildTestState`. The keys shall be test program names.  The names
shall correspond to the name of a :ref:`SpecTypeBuildTestProgramItemType` or
:ref:`SpecTypeBuildAdaTestProgramItemType` item.  Due to the processing order
of items, there is no way to check if the name specified by the attribute key
is valid.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionAction`

.. _SpecTypeBuildOptionValue:

Build Option Value
^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a boolean.

* The value may be an integer number.

* The value may be a list. Each list element shall be a string.

* There may by be no value (null).

* The value may be a string.

This type is used by the following types:

* :ref:`SpecTypeBuildOptionAction`

* :ref:`SpecTypeBuildOptionDefaultByVariant`

* :ref:`SpecTypeBuildOptionItemType`

.. _SpecTypeBuildSource:

Build Source
^^^^^^^^^^^^

The value shall be a string. It shall be a source file.  The path to a source
file shall be relative to the directory of the :file:`wscript`.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildBSPItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildObjectsItemType`

* :ref:`SpecTypeBuildStartFileItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildTarget:

Build Target
^^^^^^^^^^^^

The value shall be a string. It shall be the target file path.  The path to the
target file shall be relative to the directory of the :file:`wscript`.  The
target file is located in the build tree.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildConfigurationFileItemType`

* :ref:`SpecTypeBuildConfigurationHeaderItemType`

* :ref:`SpecTypeBuildLibraryItemType`

* :ref:`SpecTypeBuildStartFileItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildTestState:

Build Test State
^^^^^^^^^^^^^^^^

The value shall be a string. This string defines a test state. The value shall
be an element of

* "``benchmark``",

* "``exclude``",

* "``expected-fail``",

* "``indeterminate``", and

* "``user-input``".

This type is used by the following types:

* :ref:`SpecTypeBuildOptionSetTestStateAction`

.. _SpecTypeBuildUseAfterDirective:

Build Use After Directive
^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an internal static library identifier.
The library is used to link programs referenced by this item, e.g. ``z`` for
``libz.a``.  The library is placed after the use items of the build item
context.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildGroupItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeBuildUseBeforeDirective:

Build Use Before Directive
^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be an internal static library identifier.
The library is used to link programs referenced by this item, e.g. ``z`` for
``libz.a``.  The library is placed before the use items of the build item
context.

This type is used by the following types:

* :ref:`SpecTypeBuildAdaTestProgramItemType`

* :ref:`SpecTypeBuildGroupItemType`

* :ref:`SpecTypeBuildScriptItemType`

* :ref:`SpecTypeBuildTestProgramItemType`

.. _SpecTypeConstraintLinkRole:

Constraint Link Role
^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``constraint``. It defines the constraint role of links.  The link
target shall be a constraint.

.. _SpecTypeCopyright:

Copyright
^^^^^^^^^

The value shall be a string. It shall be a copyright statement of a copyright
holder of the specification item. The value

* shall match with the regular expression
  "``^\s*Copyright\s+\(C\)\s+[0-9]+,\s*[0-9]+\s+.+\s*$``",

* or, shall match with the regular expression
  "``^\s*Copyright\s+\(C\)\s+[0-9]+\s+.+\s*$``",

* or, shall match with the regular expression
  "``^\s*Copyright\s+\(C\)\s+.+\s*$``".

This type is used by the following types:

* :ref:`SpecTypeRootItemType`

.. _SpecTypeEnabledByExpression:

Enabled-By Expression
^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be an expression which defines under which
conditions the specification item or parts of it are enabled.  The expression
is evaluated with the use of an *enabled set*.  This is a set of strings which
indicate enabled features.

A value of this type shall be of one of the following variants:

* The value may be a boolean. This expression evaluates directly to the boolean
  value.

* The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
      The attribute value shall be a list. Each list element shall be an
      :ref:`SpecTypeEnabledByExpression`. The *and* operator evaluates to the
      *logical and* of the evaluation results of the expressions in the list.

  not
      The attribute value shall be an :ref:`SpecTypeEnabledByExpression`. The
      *not* operator evaluates to the *logical not* of the evaluation results
      of the expression.

  or
      The attribute value shall be a list. Each list element shall be an
      :ref:`SpecTypeEnabledByExpression`. The *or* operator evaluates to the
      *logical or* of the evaluation results of the expressions in the list.

* The value may be a list. Each list element shall be an
  :ref:`SpecTypeEnabledByExpression`. This list of expressions evaluates to the
  *logical or* of the evaluation results of the expressions in the list.

* The value may be a string. If the value is in the *enabled set*, this
  expression evaluates to true, otherwise to false.

This type is used by the following types:

* :ref:`SpecTypeActionRequirementTransition`

* :ref:`SpecTypeEnabledByExpression`

* :ref:`SpecTypeInterfaceIncludeLinkRole`

* :ref:`SpecTypeRootItemType`

Please have a look at the following example:

.. code-block:: yaml

    enabled-by:
      and:
      - RTEMS_NETWORKING
      - not: RTEMS_SMP

.. _SpecTypeGlossaryMembershipLinkRole:

Glossary Membership Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``glossary-member``. It defines the glossary membership role of links.

.. _SpecTypeIntegerOrString:

Integer or String
^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be an integer number.

* The value may be a string.

This type is used by the following types:

* :ref:`SpecTypeApplicationConfigurationOptionConstraintSet`

* :ref:`SpecTypeApplicationConfigurationValueOptionItemType`

* :ref:`SpecTypeBuildOptionAction`

.. _SpecTypeInterfaceBriefDescription:

Interface Brief Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string. It shall be the brief description of the
  interface.  It should be a single sentence. The value shall not match with
  the regular expression "``\n\n``".

This type is used by the following types:

* :ref:`SpecTypeInterfaceCompoundItemType`

* :ref:`SpecTypeInterfaceCompoundMemberDefinition`

* :ref:`SpecTypeInterfaceDefineItemType`

* :ref:`SpecTypeInterfaceEnumItemType`

* :ref:`SpecTypeInterfaceEnumeratorItemType`

* :ref:`SpecTypeInterfaceFunctionItemType`

* :ref:`SpecTypeInterfaceGroupItemType`

* :ref:`SpecTypeInterfaceHeaderFileItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

* :ref:`SpecTypeInterfaceTypedefItemType`

* :ref:`SpecTypeInterfaceVariableItemType`

.. _SpecTypeInterfaceCompoundDefinitionKind:

Interface Compound Definition Kind
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It specifies how the interface compound is
defined.  It may be a typedef only, the struct or union only, or a typedef with
a struct or union definition. The value shall be an element of

* "``struct-only``",

* "``typedef-and-struct``",

* "``typedef-and-union``",

* "``typedef-only``", and

* "``union-only``".

This type is used by the following types:

* :ref:`SpecTypeInterfaceCompoundItemType`

.. _SpecTypeInterfaceCompoundMemberCompound:

Interface Compound Member Compound
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the following types:

* :ref:`SpecTypeInterfaceCompoundMemberDefinition` through the ``kind``
  attribute if the value is ``struct``

* :ref:`SpecTypeInterfaceCompoundMemberDefinition` through the ``kind``
  attribute if the value is ``union``

This set of attributes specifies an interface compound member compound. All
explicit attributes shall be specified. The explicit attributes for this type
are:

definition
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceCompoundMemberDefinitionDirective`.

.. _SpecTypeInterfaceCompoundMemberDeclaration:

Interface Compound Member Declaration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeInterfaceCompoundMemberDefinition` through
the ``kind`` attribute if the value is ``member``. This set of attributes
specifies an interface compound member declaration. All explicit attributes
shall be specified. The explicit attributes for this type are:

definition
    The attribute value shall be a string. It shall be the interface compound
    member declaration.  On the declaration a context-sensitive substitution of
    item variables is performed.

.. _SpecTypeInterfaceCompoundMemberDefinition:

Interface Compound Member Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface compound member definition. All
explicit attributes shall be specified. The explicit attributes for this type
are:

brief
    The attribute value shall be an :ref:`SpecTypeInterfaceBriefDescription`.

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

kind
    The attribute value shall be a string. It shall be the interface compound
    member kind.

name
    The attribute value shall be a string. It shall be the interface compound
    member name.

This type is refined by the following types:

* :ref:`SpecTypeInterfaceCompoundMemberCompound`

* :ref:`SpecTypeInterfaceCompoundMemberDeclaration`

This type is used by the following types:

* :ref:`SpecTypeInterfaceCompoundMemberDefinitionDirective`

* :ref:`SpecTypeInterfaceCompoundMemberDefinitionVariant`

.. _SpecTypeInterfaceCompoundMemberDefinitionDirective:

Interface Compound Member Definition Directive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface compound member definition
directive. All explicit attributes shall be specified. The explicit attributes
for this type are:

default
    The attribute value shall be an
    :ref:`SpecTypeInterfaceCompoundMemberDefinition`. The default definition
    will be used if no variant-specific definition is enabled.

variants
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceCompoundMemberDefinitionVariant`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceCompoundItemType`

* :ref:`SpecTypeInterfaceCompoundMemberCompound`

.. _SpecTypeInterfaceCompoundMemberDefinitionVariant:

Interface Compound Member Definition Variant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface compound member definition
variant. All explicit attributes shall be specified. The explicit attributes
for this type are:

definition
    The attribute value shall be an
    :ref:`SpecTypeInterfaceCompoundMemberDefinition`. The definition will be
    used if the expression defined by the ``enabled-by`` attribute evaluates to
    true.  In generated header files, the expression is evaluated by the C
    preprocessor.

enabled-by
    The attribute value shall be an
    :ref:`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceCompoundMemberDefinitionDirective`

.. _SpecTypeInterfaceDefinition:

Interface Definition
^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string. It shall be the definition.  On the definition a
  context-sensitive substitution of item variables is performed.

This type is used by the following types:

* :ref:`SpecTypeInterfaceDefinitionDirective`

* :ref:`SpecTypeInterfaceDefinitionVariant`

.. _SpecTypeInterfaceDefinitionDirective:

Interface Definition Directive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface definition directive. All
explicit attributes shall be specified. The explicit attributes for this type
are:

default
    The attribute value shall be an :ref:`SpecTypeInterfaceDefinition`. The
    default definition will be used if no variant-specific definition is
    enabled.

variants
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceDefinitionVariant`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceDefineItemType`

* :ref:`SpecTypeInterfaceEnumeratorItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

* :ref:`SpecTypeInterfaceTypedefItemType`

* :ref:`SpecTypeInterfaceVariableItemType`

.. _SpecTypeInterfaceDefinitionVariant:

Interface Definition Variant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface definition variant. All explicit
attributes shall be specified. The explicit attributes for this type are:

definition
    The attribute value shall be an :ref:`SpecTypeInterfaceDefinition`. The
    definition will be used if the expression defined by the ``enabled-by``
    attribute evaluates to true.  In generated header files, the expression is
    evaluated by the C preprocessor.

enabled-by
    The attribute value shall be an
    :ref:`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceDefinitionDirective`

.. _SpecTypeInterfaceDescription:

Interface Description
^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string. It shall be the description of the interface.  The
  description should be short and concentrate on the average case.  All special
  cases, usage notes, constraints, error conditions, configuration
  dependencies, references, etc. should be described in the
  :ref:`SpecTypeInterfaceNotes`.

This type is used by the following types:

* :ref:`SpecTypeApplicationConfigurationOptionItemType`

* :ref:`SpecTypeInterfaceCompoundItemType`

* :ref:`SpecTypeInterfaceCompoundMemberDefinition`

* :ref:`SpecTypeInterfaceDefineItemType`

* :ref:`SpecTypeInterfaceEnumItemType`

* :ref:`SpecTypeInterfaceEnumeratorItemType`

* :ref:`SpecTypeInterfaceFunctionItemType`

* :ref:`SpecTypeInterfaceGroupItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

* :ref:`SpecTypeInterfaceParameter`

* :ref:`SpecTypeInterfaceReturnValue`

* :ref:`SpecTypeInterfaceTypedefItemType`

* :ref:`SpecTypeInterfaceVariableItemType`

.. _SpecTypeInterfaceEnabledByExpression:

Interface Enabled-By Expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be an expression which defines under which
conditions an interface definition is enabled.  In generated header files, the
expression is evaluated by the C preprocessor.

A value of this type shall be of one of the following variants:

* The value may be a boolean. It is converted to 0 or 1.  It defines a symbol
  in the expression.

* The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
      The attribute value shall be a list. Each list element shall be an
      :ref:`SpecTypeInterfaceEnabledByExpression`. The *and* operator defines a
      *logical and* of the expressions in the list.

  not
      The attribute value shall be an
      :ref:`SpecTypeInterfaceEnabledByExpression`. The *not* operator defines a
      *logical not* of the expression.

  or
      The attribute value shall be a list. Each list element shall be an
      :ref:`SpecTypeInterfaceEnabledByExpression`. The *or* operator defines a
      *logical or* of the expressions in the list.

* The value may be a list. Each list element shall be an
  :ref:`SpecTypeInterfaceEnabledByExpression`. It defines a *logical or* of the
  expressions in the list.

* The value may be a string. It defines a symbol in the expression.

This type is used by the following types:

* :ref:`SpecTypeInterfaceCompoundMemberDefinitionVariant`

* :ref:`SpecTypeInterfaceDefinitionVariant`

* :ref:`SpecTypeInterfaceEnabledByExpression`

* :ref:`SpecTypeInterfaceFunctionDefinitionVariant`

.. _SpecTypeInterfaceEnumDefinitionKind:

Interface Enum Definition Kind
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It specifies how the enum is defined.  It may be a
typedef only, the enum only, or a typedef with an enum definition. The value
shall be an element of

* "``enum-only``",

* "``typedef-and-enum``", and

* "``typedef-only``".

This type is used by the following types:

* :ref:`SpecTypeInterfaceEnumItemType`

.. _SpecTypeInterfaceEnumeratorLinkRole:

Interface Enumerator Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``interface-enumerator``. It defines the interface enumerator role of
links.

.. _SpecTypeInterfaceFunctionDefinition:

Interface Function Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a function definition. All explicit attributes
shall be specified. The explicit attributes for this type are:

attributes
    The attribute value shall be an optional string. If the value is present,
    then it shall be the function attributes. On the attributes a
    context-sensitive substitution of item variables is performed.  A function
    attribute is for example the indication that the function does not return
    to the caller.

body
    The attribute value shall be an optional string. If the value is present,
    then it shall be the definition of a static inline function.  On the
    function definition a context-sensitive substitution of item variables is
    performed.  If no value is present, then the function is declared as an
    external function.

params
    The attribute value shall be a list of strings. It shall be the list of
    parameter declarations of the function.  On the function parameter
    declarations a context-sensitive substitution of item variables is
    performed.

return
    The attribute value shall be a string. It shall be the function return
    type.  On the return type a context-sensitive substitution of item
    variables is performed.

This type is used by the following types:

* :ref:`SpecTypeInterfaceFunctionDefinitionDirective`

* :ref:`SpecTypeInterfaceFunctionDefinitionVariant`

.. _SpecTypeInterfaceFunctionDefinitionDirective:

Interface Function Definition Directive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a function definition directive. All explicit
attributes shall be specified. The explicit attributes for this type are:

default
    The attribute value shall be an :ref:`SpecTypeInterfaceFunctionDefinition`.
    The default definition will be used if no variant-specific definition is
    enabled.

variants
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceFunctionDefinitionVariant`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceFunctionItemType`

.. _SpecTypeInterfaceFunctionDefinitionVariant:

Interface Function Definition Variant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a function definition variant. All explicit
attributes shall be specified. The explicit attributes for this type are:

definition
    The attribute value shall be an :ref:`SpecTypeInterfaceFunctionDefinition`.
    The definition will be used if the expression defined by the ``enabled-by``
    attribute evaluates to true.  In generated header files, the expression is
    evaluated by the C preprocessor.

enabled-by
    The attribute value shall be an
    :ref:`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceFunctionDefinitionDirective`

.. _SpecTypeInterfaceFunctionLinkRole:

Interface Function Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``interface-function``. It defines the interface function role of
links.  It is used to indicate that a :ref:`SpecTypeActionRequirementItemType`
item specifies functional requirements of an
:ref:`SpecTypeInterfaceFunctionItemType` or a
:ref:`SpecTypeInterfaceMacroItemType` item.

.. _SpecTypeInterfaceGroupIdentifier:

Interface Group Identifier
^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It shall be the identifier of the interface group.
The value shall match with the regular expression "``^[A-Z][a-zA-Z0-9]*$``".

This type is used by the following types:

* :ref:`SpecTypeDesignGroupRequirementItemType`

* :ref:`SpecTypeInterfaceGroupItemType`

.. _SpecTypeInterfaceGroupMembershipLinkRole:

Interface Group Membership Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``interface-ingroup``. It defines the interface group membership role
of links.

.. _SpecTypeInterfaceIncludeLinkRole:

Interface Include Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``interface-include``. It defines the interface include role of links
and is used to indicate that an interface container includes another interface
container.  For example, one header file includes another header file. All
explicit attributes shall be specified. The explicit attributes for this type
are:

enabled-by
    The attribute value shall be an :ref:`SpecTypeEnabledByExpression`. It
    shall define under which conditions the interface container is included.

.. _SpecTypeInterfaceNotes:

Interface Notes
^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string. It shall be the notes for the interface.

This type is used by the following types:

* :ref:`SpecTypeApplicationConfigurationOptionItemType`

* :ref:`SpecTypeInterfaceCompoundItemType`

* :ref:`SpecTypeInterfaceDefineItemType`

* :ref:`SpecTypeInterfaceEnumeratorItemType`

* :ref:`SpecTypeInterfaceFunctionItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

* :ref:`SpecTypeInterfaceTypedefItemType`

* :ref:`SpecTypeInterfaceVariableItemType`

.. _SpecTypeInterfaceParameter:

Interface Parameter
^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface parameter. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

dir
    The attribute value shall be an :ref:`SpecTypeInterfaceParameterDirection`.

name
    The attribute value shall be a string. It shall be the interface parameter
    name.

This type is used by the following types:

* :ref:`SpecTypeInterfaceFunctionItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

.. _SpecTypeInterfaceParameterDirection:

Interface Parameter Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string. It specifies the interface parameter direction.
  The value shall be an element of

  * "``in``",

  * "``out``", and

  * "``inout``".

This type is used by the following types:

* :ref:`SpecTypeInterfaceParameter`

* :ref:`SpecTypeTestRunParameter`

.. _SpecTypeInterfacePlacementLinkRole:

Interface Placement Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``interface-placement``. It defines the interface placement role of
links.  It is used to indicate that an interface definition is placed into an
interface container, for example a header file.

.. _SpecTypeInterfaceReturnDirective:

Interface Return Directive
^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface return. All explicit attributes
shall be specified. The explicit attributes for this type are:

return
    The attribute value shall be an optional string. It shall describe the
    interface return for unspecified return values.

return-values
    The attribute value shall be a list. Each list element shall be an
    :ref:`SpecTypeInterfaceReturnValue`.

This type is used by the following types:

* :ref:`SpecTypeInterfaceFunctionItemType`

* :ref:`SpecTypeInterfaceMacroItemType`

.. _SpecTypeInterfaceReturnValue:

Interface Return Value
^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an interface return value. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
    The attribute value shall be an :ref:`SpecTypeInterfaceDescription`.

value
    The attribute value shall be a :ref:`SpecTypeBooleanOrIntegerOrString`. It
    shall be the described interface return value.

This type is used by the following types:

* :ref:`SpecTypeInterfaceReturnDirective`

.. _SpecTypeInterfaceTargetLinkRole:

Interface Target Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``interface-target``. It defines the interface target role of links.
It is used for interface forward declarations.

.. _SpecTypeLink:

Link
^^^^

This set of attributes specifies a link from one specification item to another
specification item.  The links in a list are ordered.  The first link in the
list is processed first. All explicit attributes shall be specified. The
explicit attributes for this type are:

role
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the role of
    the link.

uid
    The attribute value shall be an :ref:`SpecTypeUID`. It shall be the
    absolute or relative UID of the link target item.

This type is refined by the following types:

* :ref:`SpecTypeApplicationConfigurationGroupMemberLinkRole`

* :ref:`SpecTypeBuildDependencyLinkRole`

* :ref:`SpecTypeConstraintLinkRole`

* :ref:`SpecTypeGlossaryMembershipLinkRole`

* :ref:`SpecTypeInterfaceEnumeratorLinkRole`

* :ref:`SpecTypeInterfaceFunctionLinkRole`

* :ref:`SpecTypeInterfaceGroupMembershipLinkRole`

* :ref:`SpecTypeInterfaceIncludeLinkRole`

* :ref:`SpecTypeInterfacePlacementLinkRole`

* :ref:`SpecTypeInterfaceTargetLinkRole`

* :ref:`SpecTypePlacementOrderLinkRole`

* :ref:`SpecTypeRequirementRefinementLinkRole`

* :ref:`SpecTypeRequirementValidationLinkRole`

* :ref:`SpecTypeRuntimeMeasurementRequestLinkRole`

* :ref:`SpecTypeSpecificationMemberLinkRole`

* :ref:`SpecTypeSpecificationRefinementLinkRole`

This type is used by the following types:

* :ref:`SpecTypeRootItemType`

* :ref:`SpecTypeTestCaseAction`

* :ref:`SpecTypeTestCaseCheck`

.. _SpecTypeName:

Name
^^^^

The value shall be a string. A string is a valid name if it matches with the
``^([a-z][a-z0-9-]*|SPDX-License-Identifier)$`` regular expression.

This type is used by the following types:

* :ref:`SpecTypeApplicationConfigurationOptionItemType`

* :ref:`SpecTypeBuildItemType`

* :ref:`SpecTypeBuildOptionSetTestStateAction`

* :ref:`SpecTypeFunctionalRequirementItemType`

* :ref:`SpecTypeGlossaryItemType`

* :ref:`SpecTypeInterfaceItemType`

* :ref:`SpecTypeLink`

* :ref:`SpecTypeNonFunctionalRequirementItemType`

* :ref:`SpecTypeRequirementItemType`

* :ref:`SpecTypeRootItemType`

* :ref:`SpecTypeRuntimeMeasurementParameterSet`

* :ref:`SpecTypeRuntimePerformanceParameterSet`

* :ref:`SpecTypeSpecificationAttributeValue`

* :ref:`SpecTypeSpecificationExplicitAttributes`

* :ref:`SpecTypeSpecificationGenericAttributes`

* :ref:`SpecTypeSpecificationItemType`

* :ref:`SpecTypeSpecificationList`

* :ref:`SpecTypeSpecificationRefinementLinkRole`

.. _SpecTypeOptionalString:

Optional String
^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* There may by be no value (null).

* The value may be a string.

.. _SpecTypePlacementOrderLinkRole:

Placement Order Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``placement-order``. This link role defines the placement order of
items in a container item (for example an interface function in a header file
or a documentation section).

.. _SpecTypeRequirementReference:

Requirement Reference
^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a requirement reference. All explicit
attributes shall be specified. The explicit attributes for this type are:

identifier
    The attribute value shall be a string. It shall be the type-specific
    identifier of the reference target. For *group* references use the Doxygen
    group identifier.

type
    The attribute value shall be a :ref:`SpecTypeRequirementReferenceType`.

This type is used by the following types:

* :ref:`SpecTypeRequirementItemType`

.. _SpecTypeRequirementReferenceType:

Requirement Reference Type
^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It specifies the type of a requirement reference.
The value shall be an element of

* "``define``",

* "``file``",

* "``function``",

* "``group``",

* "``macro``", and

* "``variable``".

This type is used by the following types:

* :ref:`SpecTypeRequirementReference`

.. _SpecTypeRequirementRefinementLinkRole:

Requirement Refinement Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``requirement-refinement``. It defines the requirement refinement role
of links.

.. _SpecTypeRequirementText:

Requirement Text
^^^^^^^^^^^^^^^^

The value shall be a string. It shall state a requirement or constraint. The
value shall not contain an element of

* "``acceptable``",

* "``adequate``",

* "``almost always``",

* "``and/or``",

* "``appropriate``",

* "``approximately``",

* "``as far as possible``",

* "``as much as practicable``",

* "``best``",

* "``best possible``",

* "``easy``",

* "``efficient``",

* "``e.g.``",

* "``enable``",

* "``enough``",

* "``etc.``",

* "``few``",

* "``first rate``",

* "``flexible``",

* "``generally``",

* "``goal``",

* "``graceful``",

* "``great``",

* "``greatest``",

* "``ideally``",

* "``i.e.``",

* "``if possible``",

* "``in most cases``",

* "``large``",

* "``many``",

* "``maximize``",

* "``minimize``",

* "``most``",

* "``multiple``",

* "``necessary``",

* "``numerous``",

* "``optimize``",

* "``ought to``",

* "``probably``",

* "``quick``",

* "``rapid``",

* "``reasonably``",

* "``relevant``",

* "``robust``",

* "``satisfactory``",

* "``several``",

* "``shall be included but not limited to``",

* "``simple``",

* "``small``",

* "``some``",

* "``state of the art``",

* "``sufficient``",

* "``suitable``",

* "``support``",

* "``systematically``",

* "``transparent``",

* "``typical``",

* "``user friendly``",

* "``usually``",

* "``versatile``", and

* "``when necessary``".

This type is used by the following types:

* :ref:`SpecTypeActionRequirementState`

* :ref:`SpecTypeApplicationConfigurationGroupItemType`

* :ref:`SpecTypeApplicationConfigurationOptionConstraintSet`

* :ref:`SpecTypeApplicationConfigurationOptionItemType`

* :ref:`SpecTypeConstraintItemType`

* :ref:`SpecTypeInterfaceGroupItemType`

* :ref:`SpecTypeRequirementItemType`

.. _SpecTypeRequirementValidationLinkRole:

Requirement Validation Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``validation``. It defines the requirement validation role of links.

.. _SpecTypeRequirementValidationMethod:

Requirement Validation Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. This value type characterizes a requirement
validation method (except validation by test). The value shall be an element of

* "``by-analysis``",

* "``by-inspection``", and

* "``by-review-of-design``".

This type is used by the following types:

* :ref:`SpecTypeRequirementValidationItemType`

.. _SpecTypeRuntimeMeasurementEnvironment:

Runtime Measurement Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It specifies the runtime measurement environment.
The value

* shall be an element of

  * "``FullCache``",

  * "``HotCache``", and

  * "``DirtyCache``",

* or, shall match with the regular expression "``^Load/[1-9][0-9]*$``".

This type is used by the following types:

* :ref:`SpecTypeRuntimeMeasurementEnvironmentTable`

.. _SpecTypeRuntimeMeasurementEnvironmentTable:

Runtime Measurement Environment Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes provides runtime performance limits for a set of runtime
measurement environments. Generic attributes may be specified. Each generic
attribute key shall be a :ref:`SpecTypeRuntimeMeasurementEnvironment`. Each
generic attribute value shall be a :ref:`SpecTypeRuntimeMeasurementValueTable`.

This type is used by the following types:

* :ref:`SpecTypeRuntimePerformanceLimitTable`

.. _SpecTypeRuntimeMeasurementParameterSet:

Runtime Measurement Parameter Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines parameters of the runtime measurement test case.
All explicit attributes shall be specified. The explicit attributes for this
type are:

sample-count
    The attribute value shall be an integer number. It shall be the sample
    count of the runtime measurement context.

In addition to the explicit attributes, generic attributes may be specified.
Each generic attribute key shall be a :ref:`SpecTypeName`. The attribute value
may have any type.

This type is used by the following types:

* :ref:`SpecTypeRuntimeMeasurementTestItemType`

.. _SpecTypeRuntimeMeasurementRequestLinkRole:

Runtime Measurement Request Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``runtime-measurement-request``. It defines the runtime measurement
request role of links.  The link target shall be a
:ref:`SpecTypeRuntimeMeasurementTestItemType` item.

.. _SpecTypeRuntimeMeasurementValueKind:

Runtime Measurement Value Kind
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It specifies the kind of a runtime measurement
value. The value shall be an element of

* "``max-lower-bound``",

* "``max-upper-bound``",

* "``mean-lower-bound``",

* "``mean-upper-bound``",

* "``min-lower-bound``", and

* "``min-upper-bound``".

This type is used by the following types:

* :ref:`SpecTypeRuntimeMeasurementValueTable`

.. _SpecTypeRuntimeMeasurementValueTable:

Runtime Measurement Value Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes provides a set of runtime measurement values each of a
specified kind.  The unit of the values shall be one second. Generic attributes
may be specified. Each generic attribute key shall be a
:ref:`SpecTypeRuntimeMeasurementValueKind`. Each generic attribute value shall
be a floating-point number.

This type is used by the following types:

* :ref:`SpecTypeRuntimeMeasurementEnvironmentTable`

.. _SpecTypeRuntimePerformanceLimitTable:

Runtime Performance Limit Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes provides runtime performance limits for BSP variants
specified by ``"<arch>/<bsp>"`` with <arch> being the architecture of the BSP
and <bsp> being the base name of the BSP. Generic attributes may be specified.
Each generic attribute key shall be a string. Each generic attribute value
shall be a :ref:`SpecTypeRuntimeMeasurementEnvironmentTable`.

This type is used by the following types:

* :ref:`SpecTypeRuntimePerformanceRequirementItemType`

.. _SpecTypeRuntimePerformanceParameterSet:

Runtime Performance Parameter Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes defines parameters of the runtime performance
requirement. Generic attributes may be specified. Each generic attribute key
shall be a :ref:`SpecTypeName`. The attribute value may have any type.

This type is used by the following types:

* :ref:`SpecTypeRuntimePerformanceRequirementItemType`

.. _SpecTypeSPDXLicenseIdentifier:

SPDX License Identifier
^^^^^^^^^^^^^^^^^^^^^^^

The value shall be a string. It defines the license of the item expressed
though an SPDX License Identifier. The value

* shall be equal to "``CC-BY-SA-4.0 OR BSD-2-Clause``",

* or, shall be equal to "``BSD-2-Clause``",

* or, shall be equal to "``CC-BY-SA-4.0``".

This type is used by the following types:

* :ref:`SpecTypeRootItemType`

.. _SpecTypeSpecificationAttributeSet:

Specification Attribute Set
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a set of attributes. The following explicit
attributes are mandatory:

* ``attributes``

* ``description``

* ``mandatory-attributes``

The explicit attributes for this type are:

attributes
    The attribute value shall be a
    :ref:`SpecTypeSpecificationExplicitAttributes`. It shall specify the
    explicit attributes of the attribute set.

description
    The attribute value shall be an optional string. It shall be the
    description of the attribute set.

generic-attributes
    The attribute value shall be a
    :ref:`SpecTypeSpecificationGenericAttributes`. It shall specify the generic
    attributes of the attribute set.

mandatory-attributes
    The attribute value shall be a
    :ref:`SpecTypeSpecificationMandatoryAttributes`. It shall specify the
    mandatory attributes of the attribute set.

This type is used by the following types:

* :ref:`SpecTypeSpecificationInformation`

.. _SpecTypeSpecificationAttributeValue:

Specification Attribute Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an attribute value. All explicit attributes
shall be specified. The explicit attributes for this type are:

description
    The attribute value shall be an optional string. It shall be the
    description of the attribute value.

spec-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    specification type of the attribute value.

This type is used by the following types:

* :ref:`SpecTypeSpecificationExplicitAttributes`

.. _SpecTypeSpecificationBooleanValue:

Specification Boolean Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This attribute set specifies a boolean value. Only the ``description``
attribute is mandatory. The explicit attributes for this type are:

assert
    The attribute value shall be a boolean. This optional attribute defines the
    value constraint of the specified boolean value.  If the value of the
    assert attribute is true, then the value of the specified boolean value
    shall be true.  If the value of the assert attribute is false, then the
    value of the specified boolean value shall be false.  In case the assert
    attribute is not present, then the value of the specified boolean value may
    be true or false.

description
    The attribute value shall be an optional string. It shall be the
    description of the specified boolean value.

This type is used by the following types:

* :ref:`SpecTypeSpecificationInformation`

.. _SpecTypeSpecificationExplicitAttributes:

Specification Explicit Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generic attributes may be specified. Each generic attribute key shall be a
:ref:`SpecTypeName`. Each generic attribute value shall be a
:ref:`SpecTypeSpecificationAttributeValue`. Each generic attribute specifies an
explicit attribute of the attribute set.  The key of the each generic attribute
defines the attribute key of the explicit attribute.

This type is used by the following types:

* :ref:`SpecTypeSpecificationAttributeSet`

.. _SpecTypeSpecificationFloatingPointAssert:

Specification Floating-Point Assert
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be an expression which asserts that the
floating-point value of the specified attribute satisfies the required
constraints.

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeSpecificationFloatingPointAssert`. The *and* operator
      evaluates to the *logical and* of the evaluation results of the
      expressions in the list.

  eq
      The attribute value shall be a floating-point number. The *eq* operator
      evaluates to true, if the value to check is equal to the value of this
      attribute, otherwise to false.

  ge
      The attribute value shall be a floating-point number. The *ge* operator
      evaluates to true, if the value to check is greater than or equal to the
      value of this attribute, otherwise to false.

  gt
      The attribute value shall be a floating-point number. The *gt* operator
      evaluates to true, if the value to check is greater than the value of
      this attribute, otherwise to false.

  le
      The attribute value shall be a floating-point number. The *le* operator
      evaluates to true, if the value to check is less than or equal to the
      value of this attribute, otherwise to false.

  lt
      The attribute value shall be a floating-point number. The *lt* operator
      evaluates to true, if the value to check is less than the value of this
      attribute, otherwise to false.

  ne
      The attribute value shall be a floating-point number. The *ne* operator
      evaluates to true, if the value to check is not equal to the value of
      this attribute, otherwise to false.

  not
      The attribute value shall be a
      :ref:`SpecTypeSpecificationFloatingPointAssert`. The *not* operator
      evaluates to the *logical not* of the evaluation results of the
      expression.

  or
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeSpecificationFloatingPointAssert`. The *or* operator
      evaluates to the *logical or* of the evaluation results of the
      expressions in the list.

* The value may be a list. Each list element shall be a
  :ref:`SpecTypeSpecificationFloatingPointAssert`. This list of expressions
  evaluates to the *logical or* of the evaluation results of the expressions in
  the list.

This type is used by the following types:

* :ref:`SpecTypeSpecificationFloatingPointAssert`

* :ref:`SpecTypeSpecificationFloatingPointValue`

.. _SpecTypeSpecificationFloatingPointValue:

Specification Floating-Point Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a floating-point value. Only the
``description`` attribute is mandatory. The explicit attributes for this type
are:

assert
    The attribute value shall be a
    :ref:`SpecTypeSpecificationFloatingPointAssert`. This optional attribute
    defines the value constraints of the specified floating-point value.  In
    case the assert attribute is not present, then the value of the specified
    floating-point value may be every valid floating-point number.

description
    The attribute value shall be an optional string. It shall be the
    description of the specified floating-point value.

This type is used by the following types:

* :ref:`SpecTypeSpecificationInformation`

.. _SpecTypeSpecificationGenericAttributes:

Specification Generic Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies generic attributes.  Generic attributes are
attributes which are not explicitly specified by
:ref:`SpecTypeSpecificationExplicitAttributes`.  They are restricted to uniform
attribute key and value types. All explicit attributes shall be specified. The
explicit attributes for this type are:

description
    The attribute value shall be an optional string. It shall be the
    description of the generic attributes.

key-spec-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    specification type of the generic attribute keys.

value-spec-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    specification type of the generic attribute values.

This type is used by the following types:

* :ref:`SpecTypeSpecificationAttributeSet`

.. _SpecTypeSpecificationInformation:

Specification Information
^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies attribute values. At least one of the explicit
attributes shall be specified. The explicit attributes for this type are:

bool
    The attribute value shall be a :ref:`SpecTypeSpecificationBooleanValue`. It
    shall specify a boolean value.

dict
    The attribute value shall be a :ref:`SpecTypeSpecificationAttributeSet`. It
    shall specify a set of attributes.

float
    The attribute value shall be a
    :ref:`SpecTypeSpecificationFloatingPointValue`. It shall specify a
    floating-point value.

int
    The attribute value shall be a :ref:`SpecTypeSpecificationIntegerValue`. It
    shall specify an integer value.

list
    The attribute value shall be a :ref:`SpecTypeSpecificationList`. It shall
    specify a list of attributes or values.

none
    The attribute shall have no value. It specifies that no value is required.

str
    The attribute value shall be a :ref:`SpecTypeSpecificationStringValue`. It
    shall specify a string.

This type is used by the following types:

* :ref:`SpecTypeSpecificationItemType`

.. _SpecTypeSpecificationIntegerAssert:

Specification Integer Assert
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be an expression which asserts that the integer
value of the specified attribute satisfies the required constraints.

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeSpecificationIntegerAssert`. The *and* operator evaluates
      to the *logical and* of the evaluation results of the expressions in the
      list.

  eq
      The attribute value shall be an integer number. The *eq* operator
      evaluates to true, if the value to check is equal to the value of this
      attribute, otherwise to false.

  ge
      The attribute value shall be an integer number. The *ge* operator
      evaluates to true, if the value to check is greater than or equal to the
      value of this attribute, otherwise to false.

  gt
      The attribute value shall be an integer number. The *gt* operator
      evaluates to true, if the value to check is greater than the value of
      this attribute, otherwise to false.

  le
      The attribute value shall be an integer number. The *le* operator
      evaluates to true, if the value to check is less than or equal to the
      value of this attribute, otherwise to false.

  lt
      The attribute value shall be an integer number. The *lt* operator
      evaluates to true, if the value to check is less than the value of this
      attribute, otherwise to false.

  ne
      The attribute value shall be an integer number. The *ne* operator
      evaluates to true, if the value to check is not equal to the value of
      this attribute, otherwise to false.

  not
      The attribute value shall be a :ref:`SpecTypeSpecificationIntegerAssert`.
      The *not* operator evaluates to the *logical not* of the evaluation
      results of the expression.

  or
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeSpecificationIntegerAssert`. The *or* operator evaluates to
      the *logical or* of the evaluation results of the expressions in the
      list.

* The value may be a list. Each list element shall be a
  :ref:`SpecTypeSpecificationIntegerAssert`. This list of expressions evaluates
  to the *logical or* of the evaluation results of the expressions in the list.

This type is used by the following types:

* :ref:`SpecTypeSpecificationIntegerAssert`

* :ref:`SpecTypeSpecificationIntegerValue`

.. _SpecTypeSpecificationIntegerValue:

Specification Integer Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies an integer value. Only the ``description``
attribute is mandatory. The explicit attributes for this type are:

assert
    The attribute value shall be a :ref:`SpecTypeSpecificationIntegerAssert`.
    This optional attribute defines the value constraints of the specified
    integer value.  In case the assert attribute is not present, then the value
    of the specified integer value may be every valid integer number.

description
    The attribute value shall be an optional string. It shall be the
    description of the specified integer value.

This type is used by the following types:

* :ref:`SpecTypeSpecificationInformation`

.. _SpecTypeSpecificationList:

Specification List
^^^^^^^^^^^^^^^^^^

This set of attributes specifies a list of attributes or values. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
    The attribute value shall be an optional string. It shall be the
    description of the list.

spec-type
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    specification type of elements of the list.

This type is used by the following types:

* :ref:`SpecTypeSpecificationInformation`

.. _SpecTypeSpecificationMandatoryAttributes:

Specification Mandatory Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It defines which explicit attributes are mandatory.

A value of this type shall be of one of the following variants:

* The value may be a list. Each list element shall be a :ref:`SpecTypeName`.
  The list defines the mandatory attributes through their key names.

* The value may be a string. It defines how many explicit attributes are
  mandatory.  If `none` is used, then none of the explicit attributes is
  mandatory, they are all optional. The value shall be an element of

  * "``all``",

  * "``at-least-one``",

  * "``at-most-one``",

  * "``exactly-one``", and

  * "``none``".

This type is used by the following types:

* :ref:`SpecTypeSpecificationAttributeSet`

.. _SpecTypeSpecificationMemberLinkRole:

Specification Member Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``spec-member``. It defines the specification membership role of
links.

.. _SpecTypeSpecificationRefinementLinkRole:

Specification Refinement Link Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type refines the :ref:`SpecTypeLink` through the ``role`` attribute if the
value is ``spec-refinement``. It defines the specification refinement role of
links. All explicit attributes shall be specified. The explicit attributes for
this type are:

spec-key
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    specification type refinement attribute key of the specification
    refinement.

spec-value
    The attribute value shall be a :ref:`SpecTypeName`. It shall be the
    specification type refinement attribute value of the specification
    refinement.

.. _SpecTypeSpecificationStringAssert:

Specification String Assert
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A value of this type shall be an expression which asserts that the string of
the specified attribute satisfies the required constraints.

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeSpecificationStringAssert`. The *and* operator evaluates to
      the *logical and* of the evaluation results of the expressions in the
      list.

  contains
      The attribute value shall be a list of strings. The *contains* operator
      evaluates to true, if the string to check converted to lower case with
      all white space characters converted to a single space character contains
      a string of the list of strings of this attribute, otherwise to false.

  eq
      The attribute value shall be a string. The *eq* operator evaluates to
      true, if the string to check is equal to the value of this attribute,
      otherwise to false.

  ge
      The attribute value shall be a string. The *ge* operator evaluates to
      true, if the string to check is greater than or equal to the value of
      this attribute, otherwise to false.

  gt
      The attribute value shall be a string. The *gt* operator evaluates to
      true, if the string to check is greater than the value of this attribute,
      otherwise to false.

  in
      The attribute value shall be a list of strings. The *in* operator
      evaluates to true, if the string to check is contained in the list of
      strings of this attribute, otherwise to false.

  le
      The attribute value shall be a string. The *le* operator evaluates to
      true, if the string to check is less than or equal to the value of this
      attribute, otherwise to false.

  lt
      The attribute value shall be a string. The *lt* operator evaluates to
      true, if the string to check is less than the value of this attribute,
      otherwise to false.

  ne
      The attribute value shall be a string. The *ne* operator evaluates to
      true, if the string to check is not equal to the value of this attribute,
      otherwise to false.

  not
      The attribute value shall be a :ref:`SpecTypeSpecificationStringAssert`.
      The *not* operator evaluates to the *logical not* of the evaluation
      results of the expression.

  or
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeSpecificationStringAssert`. The *or* operator evaluates to
      the *logical or* of the evaluation results of the expressions in the
      list.

  re
      The attribute value shall be a string. The *re* operator evaluates to
      true, if the string to check matches with the regular expression of this
      attribute, otherwise to false.

  uid
      The attribute shall have no value. The *uid* operator evaluates to true,
      if the string is a valid UID, otherwise to false.

* The value may be a list. Each list element shall be a
  :ref:`SpecTypeSpecificationStringAssert`. This list of expressions evaluates
  to the *logical or* of the evaluation results of the expressions in the list.

This type is used by the following types:

* :ref:`SpecTypeSpecificationStringAssert`

* :ref:`SpecTypeSpecificationStringValue`

.. _SpecTypeSpecificationStringValue:

Specification String Value
^^^^^^^^^^^^^^^^^^^^^^^^^^

This set of attributes specifies a string. Only the ``description`` attribute
is mandatory. The explicit attributes for this type are:

assert
    The attribute value shall be a :ref:`SpecTypeSpecificationStringAssert`.
    This optional attribute defines the constraints of the specified string.
    In case the assert attribute is not present, then the specified string may
    be every valid string.

description
    The attribute value shall be an optional string. It shall be the
    description of the specified string attribute.

This type is used by the following types:

* :ref:`SpecTypeSpecificationInformation`

.. _SpecTypeTestCaseAction:

Test Case Action
^^^^^^^^^^^^^^^^

This set of attributes specifies a test case action. All explicit attributes
shall be specified. The explicit attributes for this type are:

action-brief
    The attribute value shall be an optional string. It shall be the test case
    action brief description.

action-code
    The attribute value shall be a string. It shall be the test case action
    code.

checks
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeTestCaseCheck`.

links
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeLink`.

This type is used by the following types:

* :ref:`SpecTypeTestCaseItemType`

.. _SpecTypeTestCaseCheck:

Test Case Check
^^^^^^^^^^^^^^^

This set of attributes specifies a test case check. All explicit attributes
shall be specified. The explicit attributes for this type are:

brief
    The attribute value shall be an optional string. It shall be the test case
    check brief description.

code
    The attribute value shall be a string. It shall be the test case check
    code.

links
    The attribute value shall be a list. Each list element shall be a
    :ref:`SpecTypeLink`.

This type is used by the following types:

* :ref:`SpecTypeTestCaseAction`

.. _SpecTypeTestContextMember:

Test Context Member
^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. This set of attributes defines an
  action requirement test context member. All explicit attributes shall be
  specified. The explicit attributes for this type are:

  brief
      The attribute value shall be an optional string. It shall be the test
      context member brief description.

  description
      The attribute value shall be an optional string. It shall be the test
      context member description.

  member
      The attribute value shall be a string. It shall be the test context
      member definition.  It shall be a valid C structure member definition
      without a trailing ``;``.

* There may by be no value (null).

This type is used by the following types:

* :ref:`SpecTypeActionRequirementItemType`

* :ref:`SpecTypeRuntimeMeasurementTestItemType`

* :ref:`SpecTypeTestCaseItemType`

.. _SpecTypeTestHeader:

Test Header
^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. This set of attributes specifies a test
  header.  In case a test header is specified, then instead of a test case a
  test run function will be generated.  The test run function will be declared
  in the test header target file and defined in the test source target file.
  The test run function can be used to compose test cases.  The test header
  file is not automatically included in the test source file.  It should be
  added to the includes or local includes of the test. All explicit attributes
  shall be specified. The explicit attributes for this type are:

  code
      The attribute value shall be an optional string. If the value is present,
      then it shall be the test header code.  The header code is placed at file
      scope after the general test declarations and before the test run
      function declaration.

  includes
      The attribute value shall be a list of strings. It shall be a list of
      header files included by the header file via ``#include <...>``.

  local-includes
      The attribute value shall be a list of strings. It shall be a list of
      header files included by the header file via ``#include "..."``.

  run-params
      The attribute value shall be a list. Each list element shall be a
      :ref:`SpecTypeTestRunParameter`.

  target
      The attribute value shall be a string. It shall be the path to the
      generated test header file.

* There may by be no value (null).

This type is used by the following types:

* :ref:`SpecTypeActionRequirementItemType`

* :ref:`SpecTypeTestCaseItemType`

.. _SpecTypeTestRunParameter:

Test Run Parameter
^^^^^^^^^^^^^^^^^^

This set of attributes specifies a parameter for the test run function. In case
this parameter is used in an :ref:`SpecTypeActionRequirementItemType` item,
then the parameter is also added as a member to the test context, see
:ref:`SpecTypeTestContextMember`. All explicit attributes shall be specified.
The explicit attributes for this type are:

description
    The attribute value shall be a string. It shall be the description of the
    parameter.

dir
    The attribute value shall be an :ref:`SpecTypeInterfaceParameterDirection`.

name
    The attribute value shall be a string. It shall be the parameter name.

specifier
    The attribute value shall be a string. It shall be the complete function
    parameter specifier.  Use ``${.:name}`` for the parameter name, for example
    ``"int ${.:name}"``.

This type is used by the following types:

* :ref:`SpecTypeTestHeader`

.. _SpecTypeTestSupportMethod:

Test Support Method
^^^^^^^^^^^^^^^^^^^

A value of this type shall be of one of the following variants:

* The value may be a set of attributes. This set of attributes defines an
  action requirement test support method. All explicit attributes shall be
  specified. The explicit attributes for this type are:

  brief
      The attribute value shall be an optional string. It shall be the test
      support method brief description.

  code
      The attribute value shall be a string. It shall be the test support
      method code.  The code may use a local variable ``ctx`` which points to
      the test context, see :ref:`SpecTypeTestContextMember`.

  description
      The attribute value shall be an optional string. It shall be the test
      support method description.

* There may by be no value (null).

This type is used by the following types:

* :ref:`SpecTypeActionRequirementItemType`

* :ref:`SpecTypeRuntimeMeasurementTestItemType`

* :ref:`SpecTypeRuntimePerformanceRequirementItemType`

* :ref:`SpecTypeTestCaseItemType`

.. _SpecTypeUID:

UID
^^^

The value shall be a string. The string shall be a valid absolute or relative
item UID.

This type is used by the following types:

* :ref:`SpecTypeLink`
