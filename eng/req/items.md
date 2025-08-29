% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019, 2025 embedded brains GmbH & Co. KG

% This file is part of the RTEMS quality process and was automatically
% generated.  If you find something that needs to be fixed or
% worded better please post a report or patch to an RTEMS mailing list
% or raise a bug report:
%
% https://www.rtems.org/bugs.html
%
% For information on updating and regenerating please refer to the How-To
% section in the Software Requirements Engineering chapter of the
% RTEMS Software Engineering manual.  The manual is provided as a part of
% a release.  For development sources please refer to the online
% documentation at:
%
% https://docs.rtems.org

(ReqEngSpecificationItems)=

# Specification Items

(ReqEngSpecificationItemHierarchy)=

## Specification Item Hierarchy

The specification item types have the following hierarchy:

- {ref}`SpecTypeRootItemType`

  - {ref}`SpecTypeBuildItemType`

    - {ref}`SpecTypeBuildAdaTestProgramItemType`

    - {ref}`SpecTypeBuildBSPItemType`

    - {ref}`SpecTypeBuildConfigurationFileItemType`

    - {ref}`SpecTypeBuildConfigurationHeaderItemType`

    - {ref}`SpecTypeBuildGroupItemType`

    - {ref}`SpecTypeBuildLibraryItemType`

    - {ref}`SpecTypeBuildObjectsItemType`

    - {ref}`SpecTypeBuildOptionItemType`

    - {ref}`SpecTypeBuildScriptItemType`

    - {ref}`SpecTypeBuildStartFileItemType`

    - {ref}`SpecTypeBuildTestProgramItemType`

  - {ref}`SpecTypeConstraintItemType`

  - {ref}`SpecTypeGlossaryItemType`

    - {ref}`SpecTypeGlossaryGroupItemType`

    - {ref}`SpecTypeGlossaryTermItemType`

  - {ref}`SpecTypeInterfaceItemType`

    - {ref}`SpecTypeApplicationConfigurationGroupItemType`

    - {ref}`SpecTypeApplicationConfigurationOptionItemType`

      - {ref}`SpecTypeApplicationConfigurationFeatureEnableOptionItemType`

      - {ref}`SpecTypeApplicationConfigurationFeatureOptionItemType`

      - {ref}`SpecTypeApplicationConfigurationValueOptionItemType`

    - {ref}`SpecTypeInterfaceCompoundItemType`

    - {ref}`SpecTypeInterfaceDefineItemType`

    - {ref}`SpecTypeInterfaceDomainItemType`

    - {ref}`SpecTypeInterfaceEnumItemType`

    - {ref}`SpecTypeInterfaceEnumeratorItemType`

    - {ref}`SpecTypeInterfaceForwardDeclarationItemType`

    - {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

    - {ref}`SpecTypeInterfaceGroupItemType`

    - {ref}`SpecTypeInterfaceHeaderFileItemType`

    - {ref}`SpecTypeInterfaceTypedefItemType`

    - {ref}`SpecTypeInterfaceUnspecifiedHeaderFileItemType`

    - {ref}`SpecTypeInterfaceUnspecifiedItemType`

    - {ref}`SpecTypeInterfaceVariableItemType`

    - {ref}`SpecTypeRegisterBlockItemType`

  - {ref}`SpecTypeProxyItemTypes`

  - {ref}`SpecTypeRequirementItemType`

    - {ref}`SpecTypeFunctionalRequirementItemType`

      - {ref}`SpecTypeActionRequirementItemType`

      - {ref}`SpecTypeGenericFunctionalRequirementItemType`

    - {ref}`SpecTypeNonFunctionalRequirementItemType`

      - {ref}`SpecTypeDesignGroupRequirementItemType`

      - {ref}`SpecTypeDesignTargetItemType`

      - {ref}`SpecTypeGenericNonFunctionalRequirementItemType`

      - {ref}`SpecTypeRuntimeMeasurementEnvironmentItemType`

      - {ref}`SpecTypeRuntimePerformanceRequirementItemType`

  - {ref}`SpecTypeRequirementValidationItemType`

    - {ref}`SpecTypeRequirementValidationMethod`

  - {ref}`SpecTypeRuntimeMeasurementTestItemType`

  - {ref}`SpecTypeSpecificationItemType`

  - {ref}`SpecTypeTestCaseItemType`

  - {ref}`SpecTypeTestSuiteItemType`

(ReqEngSpecificationItemTypes)=

## Specification Item Types

(SpecTypeRootItemType)=

### Root Item Type

The technical specification of RTEMS will contain for example requirements,
specializations of requirements, interface specifications, test suites, test
cases, and requirement validations. These things will be called *specification
items* or just *items* if it is clear from the context.

The specification items are stored in files in {term}`YAML` format with a
defined set of key-value pairs called attributes. Each attribute key name shall
be a {ref}`SpecTypeName`. In particular, key names which begin with an
underscore (`_`) are reserved for internal use in tools.

This is the root specification item type. All explicit attributes shall be
specified. The explicit attributes for this type are:

SPDX-License-Identifier
: The attribute value shall be a {ref}`SpecTypeSPDXLicenseIdentifier`. It shall
  be the license of the item.

copyrights
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeCopyright`. It shall be the list of copyright statements of the
  item.

enabled-by
: The attribute value shall be an {ref}`SpecTypeEnabledByExpression`. It shall
  define the conditions under which the item is enabled.

links
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeLink`.

type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the item
  type. The selection of types and the level of detail depends on a particular
  standard and product model. We need enough flexibility to be in line with
  ECSS-E-ST-10-06 and possible future applications of other standards. The item
  type may be refined further with additional type-specific subtypes.

This type is refined by the following types:

- {ref}`SpecTypeBuildItemType`

- {ref}`SpecTypeConstraintItemType`

- {ref}`SpecTypeGlossaryItemType`

- {ref}`SpecTypeInterfaceItemType`

- {ref}`SpecTypeProxyItemTypes`

- {ref}`SpecTypeRequirementItemType`

- {ref}`SpecTypeRequirementValidationItemType`

- {ref}`SpecTypeRuntimeMeasurementTestItemType`

- {ref}`SpecTypeSpecificationItemType`

- {ref}`SpecTypeTestCaseItemType`

- {ref}`SpecTypeTestSuiteItemType`

(SpecTypeBuildItemType)=

### Build Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `build`. This set of attributes specifies a build item. Only
the `build-type` attribute is mandatory. The explicit attributes for this type
are:

build-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the build
  item type.

extra-files
: The attribute value shall be a list of strings. If the value is present, it
  shall be the list of extra files associated with the item.

This type is refined by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildBSPItemType`

- {ref}`SpecTypeBuildConfigurationFileItemType`

- {ref}`SpecTypeBuildConfigurationHeaderItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

- {ref}`SpecTypeBuildOptionItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildStartFileItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildAdaTestProgramItemType)=

### Build Ada Test Program Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `ada-test-program`. This set of attributes specifies
an Ada test program executable to build. Test programs may use additional
objects provided by {ref}`SpecTypeBuildObjectsItemType` items. Test programs
have an implicit `enabled-by` attribute value which is controlled by the
`set-test-state` {ref}`SpecTypeBuildOptionAction` of an
{ref}`SpecTypeBuildOptionItemType` item. If the test state is set to `exclude`,
then the test program is not built. All explicit attributes shall be specified.
The explicit attributes for this type are:

ada-main
: The attribute value shall be a string. It shall be the path to the Ada main
  body file.

ada-object-directory
: The attribute value shall be a string. It shall be the path to the Ada object
  directory (`-D` option value for `gnatmake`).

adaflags
: The attribute value shall be a list of strings. It shall be a list of options
  for the Ada compiler.

adaincludes
: The attribute value shall be a list of strings. It shall be a list of Ada
  include paths.

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

ldflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildLinkerOption`.

source
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildSource`.

stlib
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildLinkStaticLibraryDirective`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`.

use-after
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseAfterDirective`.

use-before
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

```{code-block} yaml
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
- Copyright (C) 2020 embedded brains GmbH & Co. KG
cppflags: []
cxxflags: []
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
```

(SpecTypeBuildBSPItemType)=

### Build BSP Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `bsp`. This set of attributes specifies a base BSP
variant to build. All explicit attributes shall be specified. The explicit
attributes for this type are:

arch
: The attribute value shall be a string. It shall be the target architecture of
  the BSP.

bsp
: The attribute value shall be a string. It shall be the base BSP variant name.

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

family
: The attribute value shall be a string. It shall be the BSP family name. The
  name shall be the last directory of the path to the BSP sources.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

install
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildInstallDirective`.

source
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildSource`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
arch: myarch
bsp: mybsp
build-type: bsp
cflags: []
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeBuildConfigurationFileItemType)=

### Build Configuration File Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `config-file`. This set of attributes specifies a
configuration file placed in the build tree. The configuration file is
generated during the configure command execution and is placed in the build
tree. All explicit attributes shall be specified. The explicit attributes for
this type are:

content
: The attribute value shall be a string. It shall be the content of the
  configuration file. A `${VARIABLE}` substitution is performed during the
  configure command execution using the variables of the configuration set. Use
  `$$` for a plain `$` character. To have all variables from sibling items
  available for substitution it is recommended to link them in the proper
  order.

install-path
: The attribute value shall be a {ref}`SpecTypeBuildInstallPath`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
build-type: config-file
content: |
  # ...
  Name: ${ARCH}-rtems${__RTEMS_MAJOR__}-${BSP_NAME}
  # ...
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
enabled-by: true
install-path: ${PREFIX}/lib/pkgconfig
links: []
target: ${ARCH}-rtems${__RTEMS_MAJOR__}-${BSP_NAME}.pc
type: build
```

(SpecTypeBuildConfigurationHeaderItemType)=

### Build Configuration Header Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `config-header`. This set of attributes specifies
configuration header file. The configuration header file is generated during
configure command execution and is placed in the build tree. All collected
configuration defines are written to the configuration header file during the
configure command execution. To have all configuration defines from sibling
items available it is recommended to link them in the proper order. All
explicit attributes shall be specified. The explicit attributes for this type
are:

guard
: The attribute value shall be a string. It shall be the header guard define.

include-headers
: The attribute value shall be a list of strings. It shall be a list of header
  files to include via `#include <...>`.

install-path
: The attribute value shall be a {ref}`SpecTypeBuildInstallPath`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`.

(SpecTypeBuildGroupItemType)=

### Build Group Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `group`. This set of attributes provides a means to
aggregate other build items and modify the build item context which is used by
referenced build items. The `includes`, `ldflags`, `objects`, and `use`
variables of the build item context are updated by the corresponding attributes
of the build group. All explicit attributes shall be specified. The explicit
attributes for this type are:

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

install
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildInstallDirective`.

ldflags
: The attribute value shall be a list of strings. It shall be a list of options
  for the linker. They are used to link executables referenced by this item.

use-after
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseAfterDirective`.

use-before
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
build-type: group
cflags: []
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
cppflags: []
cxxflags: []
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
```

(SpecTypeBuildLibraryItemType)=

### Build Library Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `library`. This set of attributes specifies a static
library. Library items may use additional objects provided by
{ref}`SpecTypeBuildObjectsItemType` items through the build dependency links of
the item. All explicit attributes shall be specified. The explicit attributes
for this type are:

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

install
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildInstallDirective`.

install-path
: The attribute value shall be a {ref}`SpecTypeBuildInstallPath`.

source
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildSource`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`. It shall be the
  name of the static library, e.g. `z` for `libz.a`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
build-type: library
cflags:
- -Wno-pointer-sign
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeBuildObjectsItemType)=

### Build Objects Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `objects`. This set of attributes specifies a set of
object files used to build static libraries or test programs. Objects Items
must not be included on multiple paths through the build dependency graph with
identical build options. Violating this can cause race conditions in the build
system due to duplicate installs and multiple instances of build tasks. All
explicit attributes shall be specified. The explicit attributes for this type
are:

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

install
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildInstallDirective`.

source
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildSource`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
build-type: objects
cflags: []
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeBuildOptionItemType)=

### Build Option Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `option`. This set of attributes specifies a build
option. The following explicit attributes are mandatory:

- `actions`

- `default`

- `description`

The explicit attributes for this type are:

actions
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildOptionAction`. Each action operates on the *action value*
  handed over by a previous action and action-specific attribute values. The
  actions pass the processed action value to the next action in the list. The
  first action starts with an action value of `None`. The actions are carried
  out during the configure command execution.

default
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildOptionValue`. It shall be the list of default values of
  the option. When a default value is needed, the first value on the list which
  is enabled according to the enabled set is chosen. If no value is enabled,
  then the default value is `null`.

description
: The attribute value shall be an optional string. It shall be the description
  of the option.

format
: The attribute value shall be an optional string. It shall be a
  [Python format string](https://docs.python.org/3/library/string.html#formatstrings),
  for example `'{}'` or `'{:#010x}'`.

name
: The attribute value shall be a {ref}`SpecTypeBuildOptionName`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
actions:
- get-integer: null
- define: null
build-type: option
copyrights:
- Copyright (C) 2020, 2022 embedded brains GmbH & Co. KG
default:
- enabled-by:
  - bsps/powerpc/motorola_powerpc
  - m68k/m5484FireEngine
  - powerpc/hsc_cm01
  value: 9600
- enabled-by: m68k/COBRA5475
  value: 19200
- enabled-by: true
  value: 115200
description: |
  Default baud for console and other serial devices.
enabled-by: true
format: '{}'
links: []
name: BSP_CONSOLE_BAUD
type: build
```

(SpecTypeBuildScriptItemType)=

### Build Script Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `script`. This set of attributes specifies a build
script. The optional attributes may be required by commands executed through
the scripts. The following explicit attributes are mandatory:

- `do-build`

- `do-configure`

- `prepare-build`

- `prepare-configure`

The explicit attributes for this type are:

asflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildAssemblerOption`.

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

do-build
: The attribute value shall be an optional string. If this script shall
  execute, then it shall be Python code which is executed via `exec()` in the
  context of the `do_build()` method of the {file}`wscript`. A local variable
  `bld` is available with the `waf` build context. A local variable `bic` is
  available with the build item context.

do-configure
: The attribute value shall be an optional string. If this script shall
  execute, then it shall be Python code which is executed via `exec()` in the
  context of the `do_configure()` method of the {file}`wscript`. A local
  variable `conf` is available with the `waf` configuration context. A local
  variable `cic` is available with the configuration item context.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

ldflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildLinkerOption`.

prepare-build
: The attribute value shall be an optional string. If this script shall
  execute, then it shall be Python code which is executed via `exec()` in the
  context of the `prepare_build()` method of the {file}`wscript`. A local
  variable `bld` is available with the `waf` build context. A local variable
  `bic` is available with the build item context.

prepare-configure
: The attribute value shall be an optional string. If this script shall
  execute, then it shall be Python code which is executed via `exec()` in the
  context of the `prepare_configure()` method of the {file}`wscript`. A local
  variable `conf` is available with the `waf` configuration context. A local
  variable `cic` is available with the configuration item context.

stlib
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildLinkStaticLibraryDirective`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`.

use-after
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseAfterDirective`.

use-before
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
build-type: script
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeBuildStartFileItemType)=

### Build Start File Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `start-file`. This set of attributes specifies a
start file to build. A start file is used to link an executable. All explicit
attributes shall be specified. The explicit attributes for this type are:

asflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildAssemblerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

install-path
: The attribute value shall be a {ref}`SpecTypeBuildInstallPath`.

source
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildSource`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
asflags: []
build-type: start-file
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
cppflags: []
enabled-by: true
includes: []
install-path: ${BSP_LIBDIR}
links: []
source:
- bsps/sparc/shared/start/start.S
target: start.o
type: build
```

(SpecTypeBuildTestProgramItemType)=

### Build Test Program Item Type

This type refines the {ref}`SpecTypeBuildItemType` through the `build-type`
attribute if the value is `test-program`. This set of attributes specifies a
test program executable to build. Test programs may use additional objects
provided by {ref}`SpecTypeBuildObjectsItemType` items. Test programs have an
implicit `enabled-by` attribute value which is controlled by the
`set-test-state` {ref}`SpecTypeBuildOptionAction` of an
{ref}`SpecTypeBuildOptionItemType` item. If the test state is set to `exclude`,
then the test program is not built. All explicit attributes shall be specified.
The explicit attributes for this type are:

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

cppflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCPreprocessorOption`.

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

features
: The attribute value shall be a string. It shall be the `waf` build features
  for this test program.

includes
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildIncludePath`.

ldflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildLinkerOption`.

source
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildSource`.

stlib
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildLinkStaticLibraryDirective`.

target
: The attribute value shall be a {ref}`SpecTypeBuildTarget`.

use-after
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseAfterDirective`.

use-before
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildUseBeforeDirective`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
build-type: test-program
cflags: []
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeConstraintItemType)=

### Constraint Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `constraint`. This set of attributes specifies a constraint.
All explicit attributes shall be specified. The explicit attributes for this
type are:

rationale
: The attribute value shall be an optional string. If the value is present,
  then it shall state the rationale or justification of the constraint.

text
: The attribute value shall be a {ref}`SpecTypeRequirementText`. It shall state
  the constraint.

(SpecTypeGlossaryItemType)=

### Glossary Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `glossary`. This set of attributes specifies a glossary item.
All explicit attributes shall be specified. The explicit attributes for this
type are:

glossary-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the glossary
  item type.

This type is refined by the following types:

- {ref}`SpecTypeGlossaryGroupItemType`

- {ref}`SpecTypeGlossaryTermItemType`

(SpecTypeGlossaryGroupItemType)=

### Glossary Group Item Type

This type refines the {ref}`SpecTypeGlossaryItemType` through the
`glossary-type` attribute if the value is `group`. This set of attributes
specifies a glossary group. All explicit attributes shall be specified. The
explicit attributes for this type are:

name
: The attribute value shall be a string. It shall be the human readable name of
  the glossary group.

text
: The attribute value shall be a string. It shall state the requirement for the
  glossary group.

(SpecTypeGlossaryTermItemType)=

### Glossary Term Item Type

This type refines the {ref}`SpecTypeGlossaryItemType` through the
`glossary-type` attribute if the value is `term`. This set of attributes
specifies a glossary term. All explicit attributes shall be specified. The
explicit attributes for this type are:

term
: The attribute value shall be a string. It shall be the glossary term.

text
: The attribute value shall be a string. It shall be the definition of the
  glossary term.

(SpecTypeInterfaceItemType)=

### Interface Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `interface`. This set of attributes specifies an interface
specification item. Interface items shall specify the interface of the software
product to other software products and the hardware. Use
{ref}`SpecTypeInterfaceDomainItemType` items to specify interface domains, for
example the {term}`API`, C language, compiler, interfaces to the
implementation, and the hardware. All explicit attributes shall be specified.
The explicit attributes for this type are:

index-entries
: The attribute value shall be a list of strings. It shall be a list of
  additional document index entries. A document index entry derived from the
  interface name is added automatically.

interface-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the interface
  item type.

This type is refined by the following types:

- {ref}`SpecTypeApplicationConfigurationGroupItemType`

- {ref}`SpecTypeApplicationConfigurationOptionItemType`

- {ref}`SpecTypeInterfaceCompoundItemType`

- {ref}`SpecTypeInterfaceDefineItemType`

- {ref}`SpecTypeInterfaceDomainItemType`

- {ref}`SpecTypeInterfaceEnumItemType`

- {ref}`SpecTypeInterfaceEnumeratorItemType`

- {ref}`SpecTypeInterfaceForwardDeclarationItemType`

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

- {ref}`SpecTypeInterfaceGroupItemType`

- {ref}`SpecTypeInterfaceHeaderFileItemType`

- {ref}`SpecTypeInterfaceTypedefItemType`

- {ref}`SpecTypeInterfaceUnspecifiedHeaderFileItemType`

- {ref}`SpecTypeInterfaceUnspecifiedItemType`

- {ref}`SpecTypeInterfaceVariableItemType`

- {ref}`SpecTypeRegisterBlockItemType`

(SpecTypeApplicationConfigurationGroupItemType)=

### Application Configuration Group Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `appl-config-group`. This set of
attributes specifies an application configuration group. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
: The attribute value shall be a string. It shall be the description of the
  application configuration group.

name
: The attribute value shall be a string. It shall be human readable name of the
  application configuration group.

text
: The attribute value shall be a {ref}`SpecTypeRequirementText`. It shall state
  the requirement for the application configuration group.

(SpecTypeApplicationConfigurationOptionItemType)=

### Application Configuration Option Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `appl-config-option`. This set of
attributes specifies an application configuration option. All explicit
attributes shall be specified. The explicit attributes for this type are:

appl-config-option-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  application configuration option type.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be an
  {ref}`SpecTypeApplicationConfigurationOptionName`.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

This type is refined by the following types:

- {ref}`SpecTypeApplicationConfigurationFeatureEnableOptionItemType`

- {ref}`SpecTypeApplicationConfigurationFeatureOptionItemType`

- {ref}`SpecTypeApplicationConfigurationValueOptionItemType`

(SpecTypeApplicationConfigurationFeatureEnableOptionItemType)=

### Application Configuration Feature Enable Option Item Type

This type refines the {ref}`SpecTypeApplicationConfigurationOptionItemType`
through the `appl-config-option-type` attribute if the value is
`feature-enable`. This set of attributes specifies an application configuration
feature enable option.

(SpecTypeApplicationConfigurationFeatureOptionItemType)=

### Application Configuration Feature Option Item Type

This type refines the {ref}`SpecTypeApplicationConfigurationOptionItemType`
through the `appl-config-option-type` attribute if the value is `feature`. This
set of attributes specifies an application configuration feature option. All
explicit attributes shall be specified. The explicit attributes for this type
are:

default
: The attribute value shall be a string. It shall describe what happens if the
  configuration option is undefined.

(SpecTypeApplicationConfigurationValueOptionItemType)=

### Application Configuration Value Option Item Type

This type refines the following types:

- {ref}`SpecTypeApplicationConfigurationOptionItemType` through the
  `appl-config-option-type` attribute if the value is `initializer`

- {ref}`SpecTypeApplicationConfigurationOptionItemType` through the
  `appl-config-option-type` attribute if the value is `integer`

This set of attributes specifies application configuration initializer or
integer option. All explicit attributes shall be specified. The explicit
attributes for this type are:

default-value
: The attribute value shall be an {ref}`SpecTypeIntegerOrString`. It shall
  describe the default value of the application configuration option.

(SpecTypeInterfaceCompoundItemType)=

### Interface Compound Item Type

This type refines the following types:

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `struct`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `union`

This set of attributes specifies a compound (struct or union). All explicit
attributes shall be specified. The explicit attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceCompoundMemberDefinitionDirective`.

definition-kind
: The attribute value shall be an
  {ref}`SpecTypeInterfaceCompoundDefinitionKind`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the compound
  (struct or union).

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

(SpecTypeInterfaceDefineItemType)=

### Interface Define Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `define`. This set of attributes
specifies a define. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be an {ref}`SpecTypeInterfaceDefinitionDirective`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the define.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

(SpecTypeInterfaceDomainItemType)=

### Interface Domain Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `domain`. This set of attributes
specifies an interface domain. Interface items are placed into domains through
links with the {ref}`SpecTypeInterfacePlacementLinkRole`. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
: The attribute value shall be a string. It shall be the description of the
  domain

name
: The attribute value shall be a string. It shall be the human readable name of
  the domain.

(SpecTypeInterfaceEnumItemType)=

### Interface Enum Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `enum`. This set of attributes
specifies an enum. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition-kind
: The attribute value shall be an {ref}`SpecTypeInterfaceEnumDefinitionKind`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the enum.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

(SpecTypeInterfaceEnumeratorItemType)=

### Interface Enumerator Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `enumerator`. This set of attributes
specifies an enumerator. All explicit attributes shall be specified. The
explicit attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be an {ref}`SpecTypeInterfaceDefinitionDirective`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the
  enumerator.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

(SpecTypeInterfaceForwardDeclarationItemType)=

### Interface Forward Declaration Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `forward-declaration`. Items of this
type specify a forward declaration. The item shall have exactly one link with
the {ref}`SpecTypeInterfaceTargetLinkRole` to an
{ref}`SpecTypeInterfaceCompoundItemType` item. This link defines the type
declared by the forward declaration.

(SpecTypeInterfaceFunctionOrMacroItemType)=

### Interface Function or Macro Item Type

This type refines the following types:

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `function`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `macro`

This set of attributes specifies a function or a macro. All explicit attributes
shall be specified. The explicit attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be an
  {ref}`SpecTypeInterfaceFunctionOrMacroDefinitionDirective`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the function
  or macro.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

params
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceParameter`.

return
: The attribute value shall be an {ref}`SpecTypeInterfaceReturnDirective`.

(SpecTypeInterfaceGroupItemType)=

### Interface Group Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `group`. This set of attributes
specifies an interface group. All explicit attributes shall be specified. The
explicit attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

identifier
: The attribute value shall be an {ref}`SpecTypeInterfaceGroupIdentifier`.

name
: The attribute value shall be a string. It shall be the human readable name of
  the interface group.

text
: The attribute value shall be a {ref}`SpecTypeRequirementText`. It shall state
  the requirement for the interface group.

(SpecTypeInterfaceHeaderFileItemType)=

### Interface Header File Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `header-file`. This set of
attributes specifies a header file. The item shall have exactly one link with
the {ref}`SpecTypeInterfacePlacementLinkRole` to an
{ref}`SpecTypeInterfaceDomainItemType` item. This link defines the interface
domain of the header file. All explicit attributes shall be specified. The
explicit attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

path
: The attribute value shall be a string. It shall be the path used to include
  the header file. For example {file}`rtems/confdefs.h`.

prefix
: The attribute value shall be a string. It shall be the prefix directory path
  to the header file in the interface domain. For example
  {file}`cpukit/include`.

(SpecTypeInterfaceTypedefItemType)=

### Interface Typedef Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `typedef`. This set of attributes
specifies a typedef. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be an {ref}`SpecTypeInterfaceDefinitionDirective`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the typedef.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

params
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceParameter`.

return
: The attribute value shall be an {ref}`SpecTypeInterfaceReturnDirective`.

(SpecTypeInterfaceUnspecifiedHeaderFileItemType)=

### Interface Unspecified Header File Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `unspecified-header-file`. This set
of attributes specifies an unspecified header file. All explicit attributes
shall be specified. The explicit attributes for this type are:

path
: The attribute value shall be a string. It shall be the path used to include
  the header file. For example {file}`rtems/confdefs.h`.

references
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeExternalReference`.

(SpecTypeInterfaceUnspecifiedItemType)=

### Interface Unspecified Item Type

This type refines the following types:

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-define`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-enum`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-enumerator`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-function`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-group`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-macro`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-object`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-struct`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-typedef`

- {ref}`SpecTypeInterfaceItemType` through the `interface-type` attribute if
  the value is `unspecified-union`

This set of attributes specifies an unspecified interface. All explicit
attributes shall be specified. The explicit attributes for this type are:

name
: The attribute value shall be a string. It shall be the name of the
  unspecified interface.

references
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeExternalReference`.

(SpecTypeInterfaceVariableItemType)=

### Interface Variable Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `variable`. This set of attributes
specifies a variable. All explicit attributes shall be specified. The explicit
attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be an {ref}`SpecTypeInterfaceDefinitionDirective`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name of the variable.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

(SpecTypeRegisterBlockItemType)=

### Register Block Item Type

This type refines the {ref}`SpecTypeInterfaceItemType` through the
`interface-type` attribute if the value is `register-block`. This set of
attributes specifies a register block. A register block may be used to specify
the interface of devices. Register blocks consist of register block members
specified by the `definition` attribute. Register block members are either
instances of registers specified by the `registers` attribute or instances of
other register blocks specified by links with the
{ref}`SpecTypeRegisterBlockIncludeRole`. Registers consists of bit fields (see
{ref}`SpecTypeRegisterBitsDefinition`. The register block members are placed
into the address space of the device relative to the base address of the
register block. Register member offsets and the register block size are
specified in units of the address space granule. All explicit attributes shall
be specified. The explicit attributes for this type are:

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

definition
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterBlockMemberDefinitionDirective`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

identifier
: The attribute value shall be an {ref}`SpecTypeInterfaceGroupIdentifier`.

name
: The attribute value shall be a string. It shall be the name of the register
  block.

notes
: The attribute value shall be an {ref}`SpecTypeInterfaceNotes`.

register-block-group
: The attribute value shall be a string. It shall be the name of the interface
  group defined for the register block. For the group identifier see the
  `identifier` attribute.

register-block-size
: The attribute value shall be an {ref}`SpecTypeOptionalInteger`. If the value
  is present, then it shall be the size of the register block in units of the
  address space granule.

register-prefix
: The attribute value shall be an optional string. If the value is present,
  then it will be used to prefix register bit field names, otherwise the value
  of the `name` attribute will be used.

registers
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterDefinition`.

(SpecTypeProxyItemTypes)=

### Proxy Item Types

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `proxy`. Items of similar characteristics may link to a proxy
item through links with the {ref}`SpecTypeProxyMemberLinkRole`. A proxy item
resolves to the first member item which is enabled. Proxies may be used to
provide an interface with a common name and implementations which depend on
configuration options. For example, in one configuration a constant could be a
compile time constant and in another configuration it could be a read-only
object.

(SpecTypeRequirementItemType)=

### Requirement Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `requirement`. This set of attributes specifies a requirement.
All explicit attributes shall be specified. The explicit attributes for this
type are:

rationale
: The attribute value shall be an optional string. If the value is present,
  then it shall state the rationale or justification of the requirement.

references
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeExternalReference`.

requirement-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  requirement item type.

text
: The attribute value shall be a {ref}`SpecTypeRequirementText`. It shall state
  the requirement.

This type is refined by the following types:

- {ref}`SpecTypeFunctionalRequirementItemType`

- {ref}`SpecTypeNonFunctionalRequirementItemType`

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
enabled-by: true
functional-type: capability
links: []
rationale: |
  It keeps you busy.
requirement-type: functional
text: |
  The system shall do crazy things.
type: requirement
```

(SpecTypeFunctionalRequirementItemType)=

### Functional Requirement Item Type

This type refines the {ref}`SpecTypeRequirementItemType` through the
`requirement-type` attribute if the value is `functional`. This set of
attributes specifies a functional requirement. All explicit attributes shall be
specified. The explicit attributes for this type are:

functional-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  functional type of the requirement.

This type is refined by the following types:

- {ref}`SpecTypeActionRequirementItemType`

- {ref}`SpecTypeGenericFunctionalRequirementItemType`

(SpecTypeActionRequirementItemType)=

### Action Requirement Item Type

This type refines the {ref}`SpecTypeFunctionalRequirementItemType` through the
`functional-type` attribute if the value is `action`. This set of attributes
specifies functional requirements and corresponding validation test code. The
functional requirements of an action are specified. An action performs a step
in a finite state machine. An action is implemented through a function or a
macro. The action is performed through a call of the function or an execution
of the code of a macro expansion by an actor. The actor is for example a task
or an interrupt service routine.

For action requirements which specify the function of an interface, there shall
be exactly one link with the {ref}`SpecTypeInterfaceFunctionLinkRole` to the
interface of the action.

The action requirements are specified by

- a list of pre-conditions, each with a set of states,

- a list of post-conditions, each with a set of states,

- the transition of pre-condition states to post-condition states through the
  action.

Along with the requirements, the test code to generate a validation test is
specified. For an action requirement it is verified that all variations of
pre-condition states have a set of post-condition states specified in the
transition map. All transitions are covered by the generated test code. All
explicit attributes shall be specified. The explicit attributes for this type
are:

post-conditions
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementCondition`.

pre-conditions
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementCondition`.

skip-reasons
: The attribute value shall be an {ref}`SpecTypeActionRequirementSkipReasons`.

test-action
: The attribute value shall be a string. It shall be the test action code.

test-brief
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case brief description.

test-cleanup
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test cleanup code. The code is placed in the test action
  loop body after the test post-condition checks.

test-context
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeTestContextMember`.

test-context-support
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test context support code. The context support code is
  placed at file scope before the test context definition.

test-description
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case description.

test-header
: The attribute value shall be a {ref}`SpecTypeTestHeader`.

test-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include <...>`.

test-local-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include "..."`.

test-prepare
: The attribute value shall be an optional string. If the value is present,
  then it shall be the early test preparation code. The code is placed in the
  test action loop body before the test pre-condition preparations.

test-setup
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`.

test-stop
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`.

test-support
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case support code. The support code is placed at
  file scope before the test case code.

test-target
: The attribute value shall be a string. It shall be the path to the generated
  test case source file.

test-teardown
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`.

transition-map
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementTransition`.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeGenericFunctionalRequirementItemType)=

### Generic Functional Requirement Item Type

This type refines the following types:

- {ref}`SpecTypeFunctionalRequirementItemType` through the `functional-type`
  attribute if the value is `capability`

- {ref}`SpecTypeFunctionalRequirementItemType` through the `functional-type`
  attribute if the value is `dependability-function`

- {ref}`SpecTypeFunctionalRequirementItemType` through the `functional-type`
  attribute if the value is `function`

- {ref}`SpecTypeFunctionalRequirementItemType` through the `functional-type`
  attribute if the value is `interface-define-not-defined`

- {ref}`SpecTypeFunctionalRequirementItemType` through the `functional-type`
  attribute if the value is `operational`

- {ref}`SpecTypeFunctionalRequirementItemType` through the `functional-type`
  attribute if the value is `safety-function`

Items of this type state a functional requirement with the functional type
defined by the specification type refinement.

(SpecTypeNonFunctionalRequirementItemType)=

### Non-Functional Requirement Item Type

This type refines the {ref}`SpecTypeRequirementItemType` through the
`requirement-type` attribute if the value is `non-functional`. This set of
attributes specifies a non-functional requirement. All explicit attributes
shall be specified. The explicit attributes for this type are:

non-functional-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  non-functional type of the requirement.

This type is refined by the following types:

- {ref}`SpecTypeDesignGroupRequirementItemType`

- {ref}`SpecTypeDesignTargetItemType`

- {ref}`SpecTypeGenericNonFunctionalRequirementItemType`

- {ref}`SpecTypeRuntimeMeasurementEnvironmentItemType`

- {ref}`SpecTypeRuntimePerformanceRequirementItemType`

(SpecTypeDesignGroupRequirementItemType)=

### Design Group Requirement Item Type

This type refines the {ref}`SpecTypeNonFunctionalRequirementItemType` through
the `non-functional-type` attribute if the value is `design-group`. This set of
attributes specifies a design group requirement. Design group requirements have
an explicit reference to the associated Doxygen group specified by the
`identifier` attribute. Design group requirements have an implicit validation
by inspection method. The qualification toolchain shall perform the inspection
and check that the specified Doxygen group exists in the software source code.
All explicit attributes shall be specified. The explicit attributes for this
type are:

identifier
: The attribute value shall be a
  {ref}`SpecTypeRequirementDesignGroupIdentifier`.

(SpecTypeDesignTargetItemType)=

### Design Target Item Type

This type refines the {ref}`SpecTypeNonFunctionalRequirementItemType` through
the `non-functional-type` attribute if the value is `design-target`. This set
of attributes specifies a design {term}`target`. All explicit attributes shall
be specified. The explicit attributes for this type are:

brief
: The attribute value shall be an optional string. If the value is present,
  then it shall briefly describe the target.

description
: The attribute value shall be an optional string. If the value is present,
  then it shall thoroughly describe the target.

name
: The attribute value shall be a string. It shall be the target name.

(SpecTypeGenericNonFunctionalRequirementItemType)=

### Generic Non-Functional Requirement Item Type

This type refines the following types:

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `build-configuration`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `constraint`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `design`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `documentation`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `interface`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `interface-requirement`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `maintainability`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `performance`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `performance-runtime-limits`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `portability`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `quality`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `reliability`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `resource`

- {ref}`SpecTypeNonFunctionalRequirementItemType` through the
  `non-functional-type` attribute if the value is `safety`

Items of this type state a non-functional requirement with the non-functional
type defined by the specification type refinement.

(SpecTypeRuntimeMeasurementEnvironmentItemType)=

### Runtime Measurement Environment Item Type

This type refines the {ref}`SpecTypeNonFunctionalRequirementItemType` through
the `non-functional-type` attribute if the value is
`performance-runtime-environment`. This set of attributes specifies a runtime
measurement environment. All explicit attributes shall be specified. The
explicit attributes for this type are:

name
: The attribute value shall be a string. It shall be the runtime measurement
  environment name. See also {ref}`SpecTypeRuntimeMeasurementEnvironmentName`.

(SpecTypeRuntimePerformanceRequirementItemType)=

### Runtime Performance Requirement Item Type

This type refines the {ref}`SpecTypeNonFunctionalRequirementItemType` through
the `non-functional-type` attribute if the value is `performance-runtime`. The
item shall have exactly one link with the
{ref}`SpecTypeRuntimeMeasurementRequestLinkRole`. A requirement text processor
shall support a substitution of `${.:/limit-kind}`:

- For a {ref}`SpecTypeRuntimeMeasurementValueKind` of `min-lower-bound` or
  `min-upper-bound`, the substitution of `${.:/limit-kind}` shall be
  "`minimum`".

- For a {ref}`SpecTypeRuntimeMeasurementValueKind` of `mean-lower-bound` or
  `mean-upper-bound`, the substitution of `${.:/limit-kind}` shall be "`mean`".

- For a {ref}`SpecTypeRuntimeMeasurementValueKind` of `max-lower-bound` or
  `max-upper-bound`, the substitution of `${.:/limit-kind}` shall be
  "`maximum`".

A requirement text processor shall support a substitution of
`${.:/limit-condition}`:

- For a {ref}`SpecTypeRuntimeMeasurementValueKind` of `min-lower-bound`,
  `mean-lower-bound`, or `max-lower-bound`, the substitution of
  `${.:/limit-condition}` shall be "`greater than or equal to <value>`" with
  `<value>` being the value of the corresponding entry in the
  {ref}`SpecTypeRuntimeMeasurementValueTable`.

- For a {ref}`SpecTypeRuntimeMeasurementValueKind` of `min-upper-bound`,
  `mean-upper-bound`, or `max-upper-bound`, the substitution of
  `${.:/limit-condition}` shall be "`less than or equal to <value>`" with
  `<value>` being the value of the corresponding entry in the
  {ref}`SpecTypeRuntimeMeasurementValueTable`.

A requirement text processor shall support a substitution of
`${.:/environment}`. The value of the substitution shall be
"`<environment> environment`" with `<environment>` being the environment of the
corresponding entry in the {ref}`SpecTypeRuntimeMeasurementEnvironmentTable`.

This set of attributes specifies a runtime performance requirement. Along with
the requirement, the validation test code to execute a measure runtime request
is specified. All explicit attributes shall be specified. The explicit
attributes for this type are:

params
: The attribute value shall be a {ref}`SpecTypeRuntimePerformanceParameterSet`.

test-body
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. It shall
  provide the code of the measure runtime body handler. In contrast to other
  methods, this method is mandatory.

test-cleanup
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. It may
  provide the code to clean up the measure runtime request. This method is
  called before the cleanup method of the corresponding
  {ref}`SpecTypeRuntimeMeasurementTestItemType` item and after the request.

test-prepare
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. It may
  provide the code to prepare the measure runtime request. This method is
  called after the prepare method of the corresponding
  {ref}`SpecTypeRuntimeMeasurementTestItemType` item and before the request.

test-setup
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. It may
  provide the code of the measure runtime setup handler.

test-teardown
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. It may
  provide the code of the measure runtime teardown handler.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
enabled-by: true
links:
- role: runtime-measurement-request
  uid: ../val/perf
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
  When a partition has exactly ${../val/perf:/params/buffer-count} free
  buffers, the ${.:/limit-kind} runtime of exactly
  ${../val/perf:/params/sample-count} successful calls to
  ${../if/get-buffer:/name} in the ${.:/environment} shall be
  ${.:/limit-condition}.
non-functional-type: performance-runtime
requirement-type: non-functional
type: requirement
```

(SpecTypeRequirementValidationItemType)=

### Requirement Validation Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `validation`. This set of attributes provides a requirement
validation evidence. The item shall have exactly one link to the validated
requirement with the {ref}`SpecTypeRequirementValidationLinkRole`. All explicit
attributes shall be specified. The explicit attributes for this type are:

method

: The attribute value shall be a {ref}`SpecTypeName`. It shall specify the
  requirement validation method (except validation by test). Validation by test
  is done through {ref}`SpecTypeTestCaseItemType` items.

references

: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeExternalReference`.

text

: The attribute value shall be a string. It shall provide the validation
  evidence depending on the validation method:

  - *By analysis*: A statement shall be provided how the requirement is met, by
    analysing static properties of the {term}`software product`.

  - *By inspection*: A statement shall be provided how the requirement is met,
    by inspection of the {term}`source code`.

  - *By review of design*: A rationale shall be provided to demonstrate how the
    requirement is satisfied implicitly by the software design.

This type is refined by the following types:

- {ref}`SpecTypeRequirementValidationMethod`

(SpecTypeRequirementValidationMethod)=

### Requirement Validation Method

This type refines the following types:

- {ref}`SpecTypeRequirementValidationItemType` through the `method` attribute
  if the value is `by-analysis`

- {ref}`SpecTypeRequirementValidationItemType` through the `method` attribute
  if the value is `by-inspection`

- {ref}`SpecTypeRequirementValidationItemType` through the `method` attribute
  if the value is `by-review-of-design`

(SpecTypeRuntimeMeasurementTestItemType)=

### Runtime Measurement Test Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `runtime-measurement-test`. This set of attributes specifies a
runtime measurement test case. All explicit attributes shall be specified. The
explicit attributes for this type are:

params
: The attribute value shall be a {ref}`SpecTypeRuntimeMeasurementParameterSet`.

test-brief
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case brief description.

test-cleanup
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. If the value
  is present, then it shall be the measure runtime request cleanup method. The
  method is called after each measure runtime request.

test-context
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeTestContextMember`.

test-context-support
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test context support code. The context support code is
  placed at file scope before the test context definition.

test-description
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case description.

test-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include <...>`.

test-local-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include "..."`.

test-prepare
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. If the value
  is present, then it shall be the measure runtime request prepare method. The
  method is called before each measure runtime request.

test-setup
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. If the value
  is present, then it shall be the test case setup fixture method.

test-stop
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. If the value
  is present, then it shall be the test case stop fixture method.

test-support
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case support code. The support code is placed at
  file scope before the test case code.

test-target
: The attribute value shall be a string. It shall be the path to the generated
  test case source file.

test-teardown
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`. If the value
  is present, then it shall be the test case teardown fixture method.

(SpecTypeSpecificationItemType)=

### Specification Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `spec`. This set of attributes specifies specification types.
All explicit attributes shall be specified. The explicit attributes for this
type are:

spec-description
: The attribute value shall be an optional string. It shall be the description
  of the specification type.

spec-example
: The attribute value shall be an optional string. If the value is present,
  then it shall be an example of the specification type.

spec-info
: The attribute value shall be a {ref}`SpecTypeSpecificationInformation`.

spec-name
: The attribute value shall be an optional string. It shall be the human
  readable name of the specification type.

spec-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall the
  specification type.

Please have a look at the following example:

```{code-block} yaml
SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
copyrights:
- Copyright (C) 2020 embedded brains GmbH & Co. KG
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
```

(SpecTypeTestCaseItemType)=

### Test Case Item Type

This type refines the {ref}`SpecTypeRootItemType` through the `type` attribute
if the value is `test-case`. This set of attributes specifies a test case. All
explicit attributes shall be specified. The explicit attributes for this type
are:

test-actions
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeTestCaseAction`.

test-brief
: The attribute value shall be a string. It shall be the test case brief
  description.

test-context
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeTestContextMember`.

test-context-support
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test context support code. The context support code is
  placed at file scope before the test context definition.

test-description
: The attribute value shall be an optional string. It shall be the test case
  description.

test-header
: The attribute value shall be a {ref}`SpecTypeTestHeader`.

test-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include <...>`.

test-local-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include "..."`.

test-setup
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`.

test-stop
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`.

test-support
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test case support code. The support code is placed at
  file scope before the test case code.

test-target
: The attribute value shall be a string. It shall be the path to the generated
  target test case source file.

test-teardown
: The attribute value shall be a {ref}`SpecTypeTestSupportMethod`.

(SpecTypeTestSuiteItemType)=

### Test Suite Item Type

This type refines the following types:

- {ref}`SpecTypeRootItemType` through the `type` attribute if the value is
  `memory-benchmark`

- {ref}`SpecTypeRootItemType` through the `type` attribute if the value is
  `test-suite`

This set of attributes specifies a test suite. All explicit attributes shall be
specified. The explicit attributes for this type are:

test-brief
: The attribute value shall be a string. It shall be the test suite brief
  description.

test-code
: The attribute value shall be a string. It shall be the test suite code. The
  test suite code is placed at file scope in the target source file.

test-description
: The attribute value shall be an optional string. It shall be the test suite
  description.

test-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include <...>`.

test-local-includes
: The attribute value shall be a list of strings. It shall be a list of header
  files included via `#include "..."`.

test-target
: The attribute value shall be a string. It shall be the path to the generated
  target test suite source file.

(ReqEngSpecificationAttributeSetsAndValueTypes)=

## Specification Attribute Sets and Value Types

(SpecTypeActionRequirementBooleanExpression)=

### Action Requirement Boolean Expression

A value of this type is a boolean expression.

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeActionRequirementBooleanExpression`. The *and* operator
    evaluates to the *logical and* of the evaluation results of the expressions
    in the list.

  not
  : The attribute value shall be an
    {ref}`SpecTypeActionRequirementBooleanExpression`. The *not* operator
    evaluates to the *logical not* of the evaluation results of the expression.

  or
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeActionRequirementBooleanExpression`. The *or* operator
    evaluates to the *logical or* of the evaluation results of the expressions
    in the list.

  post-conditions
  : The attribute value shall be an
    {ref}`SpecTypeActionRequirementExpressionConditionSet`. The
    *post-conditions* operator evaluates to true, if the post-condition states
    of the associated transition are contained in the specified post-condition
    set, otherwise to false.

  pre-conditions
  : The attribute value shall be an
    {ref}`SpecTypeActionRequirementExpressionConditionSet`. The
    *pre-conditions* operator evaluates to true, if the pre-condition states of
    the associated transition are contained in the specified pre-condition set,
    otherwise to false.

- The value may be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementBooleanExpression`. This list of expressions
  evaluates to the *logical or* of the evaluation results of the expressions in
  the list.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementBooleanExpression`

- {ref}`SpecTypeActionRequirementExpression`

(SpecTypeActionRequirementCondition)=

### Action Requirement Condition

This set of attributes defines an action pre-condition or post-condition. All
explicit attributes shall be specified. The explicit attributes for this type
are:

name
: The attribute value shall be an {ref}`SpecTypeActionRequirementName`.

states
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementState`.

test-epilogue
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test epilogue code. The epilogue code is placed in the
  test condition preparation or check before the state-specific code. The code
  may use a local variable `ctx` which points to the test context, see
  {ref}`SpecTypeTestContextMember`.

test-prologue
: The attribute value shall be an optional string. If the value is present,
  then it shall be the test prologue code. The prologue code is placed in the
  test condition preparation or check after the state-specific code. The code
  may use a local variable `ctx` which points to the test context, see
  {ref}`SpecTypeTestContextMember`.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementItemType`

(SpecTypeActionRequirementExpression)=

### Action Requirement Expression

This set of attributes defines an expression which may define the state of a
post-condition. The `else` and `specified-by` shall be used individually. The
`if` and `then` or `then-specified-by` expressions shall be used together. At
least one of the explicit attributes shall be specified. The explicit
attributes for this type are:

else
: The attribute value shall be an
  {ref}`SpecTypeActionRequirementExpressionStateName`. It shall be the name of
  the state of the post-condition.

if
: The attribute value shall be an
  {ref}`SpecTypeActionRequirementBooleanExpression`. If the boolean expression
  evaluates to true, then the state is defined according to the `then`
  attribute value.

specified-by
: The attribute value shall be an {ref}`SpecTypeActionRequirementName`. It
  shall be the name of a pre-condition. The name of the state of the
  pre-condition in the associated transition defines the name of the state of
  the post-condition.

then
: The attribute value shall be an
  {ref}`SpecTypeActionRequirementExpressionStateName`. It shall be the name of
  the state of the post-condition.

then-specified-by
: The attribute value shall be an {ref}`SpecTypeActionRequirementName`. It
  shall be the name of a pre-condition. The name of the state of the
  pre-condition in the associated transition defines the name of the state of
  the post-condition.

(SpecTypeActionRequirementExpressionConditionSet)=

### Action Requirement Expression Condition Set

This set of attributes defines for the specified conditions a set of states.
Generic attributes may be specified. Each generic attribute key shall be an
{ref}`SpecTypeActionRequirementName`. Each generic attribute value shall be an
{ref}`SpecTypeActionRequirementExpressionStateSet`. There shall be at most one
generic attribute key for each condition. The key name shall be the condition
name. The value of each generic attribute shall be a set of states of the
condition.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementBooleanExpression`

(SpecTypeActionRequirementExpressionStateName)=

### Action Requirement Expression State Name

The value shall be a string. It shall be the name of a state of the condition
or `N/A` if the condition is not applicable. The value

- shall match with the regular expression "`^[A-Z][a-zA-Z0-9]*$`",

- or, shall be equal to "`N/A`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementExpression`

(SpecTypeActionRequirementExpressionStateSet)=

### Action Requirement Expression State Set

A value of this type shall be of one of the following variants:

- The value may be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementExpressionStateName`. The list defines a set
  of states of the condition.

- The value may be a string. It shall be the name of a state of the condition
  or `N/A` if the condition is not applicable. The value

  - shall match with the regular expression "`^[A-Z][a-zA-Z0-9]*$`",

  - or, shall be equal to "`N/A`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementExpressionConditionSet`

(SpecTypeActionRequirementName)=

### Action Requirement Name

The value shall be a string. It shall be the name of a condition or a state of
a condition used to define pre-conditions and post-conditions of an action
requirement. It shall be formatted in CamelCase. It should be brief and
abbreviated. The rationale for this is that the names are used in tables and
the horizontal space is limited by the page width. The more conditions you have
in an action requirement, the shorter the names should be. The name `NA` is
reserved and indicates that a condition is not applicable. The value

- shall match with the regular expression "`^[A-Z][a-zA-Z0-9]*$`",

- and, shall be not equal to "`NA`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementCondition`

- {ref}`SpecTypeActionRequirementExpressionConditionSet`

- {ref}`SpecTypeActionRequirementExpression`

- {ref}`SpecTypeActionRequirementSkipReasons`

- {ref}`SpecTypeActionRequirementState`

- {ref}`SpecTypeActionRequirementTransitionPostConditions`

- {ref}`SpecTypeActionRequirementTransitionPreConditions`

(SpecTypeActionRequirementSkipReasons)=

### Action Requirement Skip Reasons

This set of attributes specifies skip reasons used to justify why transitions
in the transition map are skipped. Generic attributes may be specified. Each
generic attribute key shall be an {ref}`SpecTypeActionRequirementName`. Each
generic attribute value shall be a string. The key defines the name of a skip
reason. The name can be used in
{ref}`SpecTypeActionRequirementTransitionPostConditions` to skip the
corresponding transitions. The value shall give a reason why the transitions
are skipped.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementItemType`

(SpecTypeActionRequirementState)=

### Action Requirement State

This set of attributes defines an action pre-condition or post-condition state.
All explicit attributes shall be specified. The explicit attributes for this
type are:

name
: The attribute value shall be an {ref}`SpecTypeActionRequirementName`.

test-code
: The attribute value shall be a string. It shall be the test code to prepare
  or check the state of the condition. The code may use a local variable `ctx`
  which points to the test context, see {ref}`SpecTypeTestContextMember`.

text
: The attribute value shall be a {ref}`SpecTypeRequirementText`. It shall
  define the state of the condition.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementCondition`

(SpecTypeActionRequirementTransition)=

### Action Requirement Transition

This set of attributes defines the transition from multiple sets of states of
pre-conditions to a set of states of post-conditions through an action in an
action requirement. The ability to specify multiple sets of states of
pre-conditions which result in a common set of post-conditions may allow a more
compact specification of the transition map. For example, let us suppose you
want to specify the action of a function with a pointer parameter. The function
performs an early check that the pointer is NULL and in this case returns an
error code. The pointer condition dominates the action outcome if the pointer
is NULL. Other pre-condition states can be simply set to `all` for this
transition. All explicit attributes shall be specified. The explicit attributes
for this type are:

enabled-by
: The attribute value shall be an {ref}`SpecTypeEnabledByExpression`. The
  transition map may be customized to support configuration variants through
  this attribute. The default transitions (`enabled-by: true`) shall be
  specified before the customized variants in the list.

post-conditions
: The attribute value shall be an
  {ref}`SpecTypeActionRequirementTransitionPostConditions`.

pre-conditions
: The attribute value shall be an
  {ref}`SpecTypeActionRequirementTransitionPreConditions`.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementItemType`

(SpecTypeActionRequirementTransitionPostConditionState)=

### Action Requirement Transition Post-Condition State

A value of this type shall be of one of the following variants:

- The value may be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementExpression`. The list contains expressions to
  define the state of the corresponding post-condition.

- The value may be a string. It shall be the name of a state of the
  corresponding post-condition or `N/A` if the post-condition is not
  applicable. The value

  - shall match with the regular expression "`^[A-Z][a-zA-Z0-9]*$`",

  - or, shall be equal to "`N/A`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementTransitionPostConditions`

(SpecTypeActionRequirementTransitionPostConditions)=

### Action Requirement Transition Post-Conditions

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes defines for each
  post-condition the state after the action for a transition in an action
  requirement. Generic attributes may be specified. Each generic attribute key
  shall be an {ref}`SpecTypeActionRequirementName`. Each generic attribute
  value shall be an
  {ref}`SpecTypeActionRequirementTransitionPostConditionState`. There shall be
  exactly one generic attribute key for each post-condition. The key name shall
  be the post-condition name. The value of each generic attribute shall be the
  state of the post-condition or `N/A` if the post-condition is not applicable.

- The value may be a string. It shall be the name of a skip reason. If a skip
  reason is given instead of a listing of post-condition states, then this
  transition is skipped and no test code runs for this transition. The value

  - shall match with the regular expression "`^[A-Z][a-zA-Z0-9]*$`",

  - and, shall be not equal to "`NA`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementTransition`

(SpecTypeActionRequirementTransitionPreConditionStateSet)=

### Action Requirement Transition Pre-Condition State Set

A value of this type shall be of one of the following variants:

- The value may be a list. Each list element shall be an
  {ref}`SpecTypeActionRequirementName`. The list defines the set of states of
  the pre-condition in the transition.

- The value may be a string. The value `all` represents all states of the
  pre-condition in this transition. The value `N/A` marks the pre-condition as
  not applicable in this transition. The value shall be an element of

  - "`all`", and

  - "`N/A`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementTransitionPreConditions`

(SpecTypeActionRequirementTransitionPreConditions)=

### Action Requirement Transition Pre-Conditions

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes defines for each
  pre-condition the set of states before the action for a transition in an
  action requirement. Generic attributes may be specified. Each generic
  attribute key shall be an {ref}`SpecTypeActionRequirementName`. Each generic
  attribute value shall be an
  {ref}`SpecTypeActionRequirementTransitionPreConditionStateSet`. There shall
  be exactly one generic attribute key for each pre-condition. The key name
  shall be the pre-condition name. The value of each generic attribute shall be
  a set of states of the pre-condition.

- The value may be a string. If this name is specified instead of explicit
  pre-condition states, then the post-condition states of this entry are used
  to define all remaining transitions of the map. The value shall be equal to
  "`default`".

This type is used by the following types:

- {ref}`SpecTypeActionRequirementTransition`

(SpecTypeApplicationConfigurationOptionName)=

### Application Configuration Option Name

The value shall be a string. It shall be the name of an application
configuration option. The value shall match with the regular expression
"`^(CONFIGURE_|BSP_)[A-Z0-9_]+$`".

This type is used by the following types:

- {ref}`SpecTypeApplicationConfigurationOptionItemType`

(SpecTypeBooleanOrIntegerOrString)=

### Boolean or Integer or String

A value of this type shall be of one of the following variants:

- The value may be a boolean.

- The value may be an integer number.

- The value may be a string.

This type is used by the following types:

- {ref}`SpecTypeBuildOptionAction`

- {ref}`SpecTypeInterfaceReturnValue`

(SpecTypeBuildAssemblerOption)=

### Build Assembler Option

The value shall be a string. It shall be an option for the assembler. The
options are used to assemble the sources of this item. The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildStartFileItemType`

(SpecTypeBuildCCompilerOption)=

### Build C Compiler Option

The value shall be a string. It shall be an option for the C compiler. The
options are used to compile the sources of this item. The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildBSPItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

- {ref}`SpecTypeBuildOptionCCompilerCheckAction`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildCPreprocessorOption)=

### Build C Preprocessor Option

The value shall be a string. It shall be an option for the C preprocessor. The
options are used to preprocess the sources of this item. The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildBSPItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildStartFileItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildCXXCompilerOption)=

### Build C++ Compiler Option

The value shall be a string. It shall be an option for the C++ compiler. The
options are used to compile the sources of this item. The options defined by
this attribute succeed the options presented to the item by the build item
context.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

- {ref}`SpecTypeBuildOptionCXXCompilerCheckAction`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildDependencyConditionalLinkRole)=

### Build Dependency Conditional Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `build-dependency-conditional`. It defines the build dependency
conditional role of links. All explicit attributes shall be specified. The
explicit attributes for this type are:

enabled-by
: The attribute value shall be an {ref}`SpecTypeEnabledByExpression`. It shall
  define under which conditions the build dependency is enabled.

(SpecTypeBuildDependencyLinkRole)=

### Build Dependency Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `build-dependency`. It defines the build dependency role of links.

(SpecTypeBuildIncludePath)=

### Build Include Path

The value shall be a string. It shall be a path to header files. The path is
used by the C preprocessor to search for header files. It succeeds the includes
presented to the item by the build item context. For an
{ref}`SpecTypeBuildGroupItemType` item the includes are visible to all items
referenced by the group item. For {ref}`SpecTypeBuildBSPItemType`,
{ref}`SpecTypeBuildObjectsItemType`, {ref}`SpecTypeBuildLibraryItemType`,
{ref}`SpecTypeBuildStartFileItemType`, and
{ref}`SpecTypeBuildTestProgramItemType` items the includes are only visible to
the sources specified by the item itself and they do not propagate to
referenced items.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildBSPItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildStartFileItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildInstallDirective)=

### Build Install Directive

This set of attributes specifies files installed by a build item. All explicit
attributes shall be specified. The explicit attributes for this type are:

destination
: The attribute value shall be a string. It shall be the install destination
  directory.

source
: The attribute value shall be a list of strings. It shall be the list of
  source files to be installed in the destination directory. The path to a
  source file shall be relative to the directory of the {file}`wscript`.

This type is used by the following types:

- {ref}`SpecTypeBuildBSPItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

(SpecTypeBuildInstallPath)=

### Build Install Path

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It shall be the installation path of a
  {ref}`SpecTypeBuildTarget`.

This type is used by the following types:

- {ref}`SpecTypeBuildConfigurationFileItemType`

- {ref}`SpecTypeBuildConfigurationHeaderItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildStartFileItemType`

(SpecTypeBuildLinkStaticLibraryDirective)=

### Build Link Static Library Directive

The value shall be a string. It shall be an external static library identifier.
The library is used to link programs referenced by this item, e.g. `m` for
`libm.a`. The library is added to the build command through the `stlib`
attribute. It shall not be used for internal static libraries. Internal static
libraries shall be specified through the `use-after` and `use-before`
attributes to enable a proper build dependency tracking.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildLinkerOption)=

### Build Linker Option

The value shall be a string. It shall be an option for the linker. The options
are used to link executables. The options defined by this attribute succeed the
options presented to the item by the build item context.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildOptionAction)=

### Build Option Action

This set of attributes specifies a build option action. Exactly one of the
explicit attributes shall be specified. The explicit attributes for this type
are:

append-test-cppflags
: The attribute value shall be a string. It shall be the name of a test
  program. The action appends the action value to the `CPPFLAGS` of the test
  program. The name shall correspond to the name of a
  {ref}`SpecTypeBuildTestProgramItemType` item. Due to the processing order of
  items, there is no way to check if the name specified by the attribute value
  is valid.

assert-aligned
: The attribute value shall be an integer number. The action asserts that the
  action value is aligned according to the attribute value.

assert-eq
: The attribute value shall be a {ref}`SpecTypeBooleanOrIntegerOrString`. The
  action asserts that the action value is equal to the attribute value.

assert-ge
: The attribute value shall be an {ref}`SpecTypeIntegerOrString`. The action
  asserts that the action value is greater than or equal to the attribute
  value.

assert-gt
: The attribute value shall be an {ref}`SpecTypeIntegerOrString`. The action
  asserts that the action value is greater than the attribute value.

assert-in-set
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeIntegerOrString`. The action asserts that the action value is
  in the attribute value set.

assert-int16
: The attribute shall have no value. The action asserts that the action value
  is a valid signed 16-bit integer.

assert-int32
: The attribute shall have no value. The action asserts that the action value
  is a valid signed 32-bit integer.

assert-int64
: The attribute shall have no value. The action asserts that the action value
  is a valid signed 64-bit integer.

assert-int8
: The attribute shall have no value. The action asserts that the action value
  is a valid signed 8-bit integer.

assert-le
: The attribute value shall be an {ref}`SpecTypeIntegerOrString`. The action
  asserts that the action value is less than or equal to the attribute value.

assert-lt
: The attribute value shall be an {ref}`SpecTypeIntegerOrString`. The action
  asserts that the action value is less than the attribute value.

assert-ne
: The attribute value shall be a {ref}`SpecTypeBooleanOrIntegerOrString`. The
  action asserts that the action value is not equal to the attribute value.

assert-power-of-two
: The attribute shall have no value. The action asserts that the action value
  is a power of two.

assert-uint16
: The attribute shall have no value. The action asserts that the action value
  is a valid unsigned 16-bit integer.

assert-uint32
: The attribute shall have no value. The action asserts that the action value
  is a valid unsigned 32-bit integer.

assert-uint64
: The attribute shall have no value. The action asserts that the action value
  is a valid unsigned 64-bit integer.

assert-uint8
: The attribute shall have no value. The action asserts that the action value
  is a valid unsigned 8-bit integer.

check-cc
: The attribute value shall be a
  {ref}`SpecTypeBuildOptionCCompilerCheckAction`.

check-cxx
: The attribute value shall be a
  {ref}`SpecTypeBuildOptionCXXCompilerCheckAction`.

comment
: The attribute value shall be a string. There is no action performed. The
  attribute value is a comment.

define
: The attribute value shall be an optional string. The action adds a define to
  the configuration set. If the attribute value is present, then it is used as
  the name of the define, otherwise the `name` of the item is used. The value
  of the define is the action value. If the action value is a string, then it
  is quoted.

define-condition
: The attribute value shall be an optional string. The action adds a
  conditional define to the configuration set. If the attribute value is
  present, then it is used as the name of the define, otherwise the `name` of
  the item is used. The value of the define is the action value.

define-unquoted
: The attribute value shall be an optional string. The action adds a define to
  the configuration set. If the attribute value is present, then it is used as
  the name of the define, otherwise the `name` of the item is used. The value
  of the define is the action value. If the action value is a string, then it
  is not quoted.

env-append
: The attribute value shall be an optional string. The action appends the
  action value to an environment of the configuration set. If the attribute
  value is present, then it is used as the name of the environment variable,
  otherwise the `name` of the item is used.

env-assign
: The attribute value shall be an optional string. The action assigns the
  action value to an environment of the configuration set. If the attribute
  value is present, then it is used as the name of the environment variable,
  otherwise the `name` of the item is used.

env-enable
: The attribute value shall be an optional string. If the action value is true,
  then a name is appended to the `ENABLE` environment variable of the
  configuration set. If the attribute value is present, then it is used as the
  name, otherwise the `name` of the item is used.

find-program
: The attribute shall have no value. The action tries to find the program
  specified by the action value. Uses the `${PATH}` to find the program.
  Returns the result of the find operation, e.g. a path to the program.

find-tool
: The attribute shall have no value. The action tries to find the tool
  specified by the action value. Uses the tool paths specified by the
  `--rtems-tools` command line option. Returns the result of the find
  operation, e.g. a path to the program.

format-and-define
: The attribute value shall be an optional string. The action adds a define to
  the configuration set. If the attribute value is present, then it is used as
  the name of the define, otherwise the `name` of the item is used. The value
  of the define is the action value. The value is formatted according to the
  `format` attribute value.

get-boolean
: The attribute shall have no value. The action gets the action value for
  subsequent actions from a configuration file variable named by the items
  `name` attribute. If no such variable exists in the configuration file, then
  the default value is used. The value is converted to a boolean.

get-env
: The attribute value shall be a string. The action gets the action value for
  subsequent actions from the environment variable of the configuration set
  named by the attribute value.

get-integer
: The attribute shall have no value. The action gets the action value for
  subsequent actions from a configuration file variable named by the items
  `name` attribute. If no such variable exists in the configuration file, then
  the default value is used. The value is converted to an integer.

get-string
: The attribute shall have no value. The action gets the action value for
  subsequent actions from a configuration file variable named by the items
  `name` attribute. If no such variable exists in the configuration file, then
  the default value is used. The value is converted to a string.

get-string-command-line
: The attribute value shall be a string. The action gets the action value for
  subsequent actions from the value of a command line option named by the items
  `name` attribute. If no such command line option is present, then the
  attribute value is used. The value is converted to a string.

script
: The attribute value shall be a string. The action executes the attribute
  value with the Python `eval()` function in the context of the script action
  handler.

set-test-state
: The attribute value shall be a {ref}`SpecTypeBuildOptionSetTestStateAction`.

set-value
: The attribute value may have any type. The action sets the action value for
  subsequent actions to the attribute value.

set-value-enabled-by
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildOptionValue`. The action sets the action value for
  subsequent actions to the first enabled attribute value.

split
: The attribute shall have no value. The action splits the action value.

substitute
: The attribute shall have no value. The action performs a `${VARIABLE}`
  substitution on the action value. Use `$$` for a plain `$` character.

This type is used by the following types:

- {ref}`SpecTypeBuildOptionItemType`

(SpecTypeBuildOptionCCompilerCheckAction)=

### Build Option C Compiler Check Action

This set of attributes specifies a check done using the C compiler. All
explicit attributes shall be specified. The explicit attributes for this type
are:

cflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCCompilerOption`.

fragment
: The attribute value shall be a string. It shall be a code fragment used to
  check the availability of a certain feature through compilation with the C
  compiler. The resulting object is not linked to an executable.

message
: The attribute value shall be a string. It shall be a description of the
  feature to check.

This type is used by the following types:

- {ref}`SpecTypeBuildOptionAction`

(SpecTypeBuildOptionCXXCompilerCheckAction)=

### Build Option C++ Compiler Check Action

This set of attributes specifies a check done using the C++ compiler. All
explicit attributes shall be specified. The explicit attributes for this type
are:

cxxflags
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeBuildCXXCompilerOption`.

fragment
: The attribute value shall be a string. It shall be a code fragment used to
  check the availability of a certain feature through compilation with the C++
  compiler. The resulting object is not linked to an executable.

message
: The attribute value shall be a string. It shall be a description of the
  feature to check.

This type is used by the following types:

- {ref}`SpecTypeBuildOptionAction`

(SpecTypeBuildOptionName)=

### Build Option Name

The value shall be a string. It shall be the name of the build option. The
value shall match with the regular expression "`^[a-zA-Z_][a-zA-Z0-9_]*$`".

This type is used by the following types:

- {ref}`SpecTypeBuildOptionItemType`

(SpecTypeBuildOptionSetTestStateAction)=

### Build Option Set Test State Action

This set of attributes specifies the test state for a set of test programs with
an optional reason. All explicit attributes shall be specified. The explicit
attributes for this type are:

reason
: The attribute value shall be an optional string. If the value is present,
  then it shall be the reason for the test state definition.

state
: The attribute value shall be a {ref}`SpecTypeBuildTestState`. It shall be the
  test state for the associated list of tests.

tests
: The attribute value shall be a list of strings. It shall be the list of test
  program names associated with the test state. The names shall correspond to
  the name of a {ref}`SpecTypeBuildTestProgramItemType` or
  {ref}`SpecTypeBuildAdaTestProgramItemType` item. Due to the processing order
  of items, there is no way to check if a specified test program name is valid.

This type is used by the following types:

- {ref}`SpecTypeBuildOptionAction`

(SpecTypeBuildOptionValue)=

### Build Option Value

This set of attributes specifies an optional build option value. All explicit
attributes shall be specified. The explicit attributes for this type are:

enabled-by
: The attribute value shall be an {ref}`SpecTypeEnabledByExpression`.

value
: The attribute value may have any type. If the associated enabled-by
  expression evaluates to true for the current enabled set, then the attribute
  value is active and may get selected.

This type is used by the following types:

- {ref}`SpecTypeBuildOptionAction`

- {ref}`SpecTypeBuildOptionItemType`

(SpecTypeBuildSource)=

### Build Source

The value shall be a string. It shall be a source file. The path to a source
file shall be relative to the directory of the {file}`wscript`.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildBSPItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildObjectsItemType`

- {ref}`SpecTypeBuildStartFileItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildTarget)=

### Build Target

The value shall be a string. It shall be the target file path. The path to the
target file shall be relative to the directory of the {file}`wscript`. The
target file is located in the build tree.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildConfigurationFileItemType`

- {ref}`SpecTypeBuildConfigurationHeaderItemType`

- {ref}`SpecTypeBuildLibraryItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildStartFileItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildTestState)=

### Build Test State

The value shall be a string. This string defines a test state. The value shall
be an element of

- "`benchmark`",

- "`exclude`",

- "`expected-fail`",

- "`indeterminate`", and

- "`user-input`".

This type is used by the following types:

- {ref}`SpecTypeBuildOptionSetTestStateAction`

(SpecTypeBuildUseAfterDirective)=

### Build Use After Directive

The value shall be a string. It shall be an internal static library identifier.
The library is used to link programs referenced by this item, e.g. `z` for
`libz.a`. The library is placed after the use items of the build item context.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeBuildUseBeforeDirective)=

### Build Use Before Directive

The value shall be a string. It shall be an internal static library identifier.
The library is used to link programs referenced by this item, e.g. `z` for
`libz.a`. The library is placed before the use items of the build item context.

This type is used by the following types:

- {ref}`SpecTypeBuildAdaTestProgramItemType`

- {ref}`SpecTypeBuildGroupItemType`

- {ref}`SpecTypeBuildScriptItemType`

- {ref}`SpecTypeBuildTestProgramItemType`

(SpecTypeConstraintLinkRole)=

### Constraint Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `constraint`. It defines the constraint role of links. The link target
shall be a constraint.

(SpecTypeCopyright)=

### Copyright

The value shall be a string. It shall be a copyright statement of a copyright
holder of the specification item. The value

- shall match with the regular expression
  "`^\s*Copyright\s+\(C\)\s+[0-9]+,\s*[0-9]+\s+.+\s*$`",

- or, shall match with the regular expression
  "`^\s*Copyright\s+\(C\)\s+[0-9]+\s+.+\s*$`",

- or, shall match with the regular expression
  "`^\s*Copyright\s+\(C\)\s+.+\s*$`".

This type is used by the following types:

- {ref}`SpecTypeRootItemType`

(SpecTypeEnabledByExpression)=

### Enabled-By Expression

A value of this type shall be an expression which defines under which
conditions the specification item or parts of it are enabled. The expression is
evaluated with the use of an *enabled set*. This is a set of strings which
indicate enabled features.

A value of this type shall be of one of the following variants:

- The value may be a boolean. This expression evaluates directly to the boolean
  value.

- The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeEnabledByExpression`. The *and* operator evaluates to the
    *logical and* of the evaluation results of the expressions in the list.

  not
  : The attribute value shall be an {ref}`SpecTypeEnabledByExpression`. The
    *not* operator evaluates to the *logical not* of the evaluation results of
    the expression.

  or
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeEnabledByExpression`. The *or* operator evaluates to the
    *logical or* of the evaluation results of the expressions in the list.

- The value may be a list. Each list element shall be an
  {ref}`SpecTypeEnabledByExpression`. This list of expressions evaluates to the
  *logical or* of the evaluation results of the expressions in the list.

- The value may be a string. If the value is in the *enabled set*, this
  expression evaluates to true, otherwise to false.

This type is used by the following types:

- {ref}`SpecTypeActionRequirementTransition`

- {ref}`SpecTypeBuildDependencyConditionalLinkRole`

- {ref}`SpecTypeBuildOptionValue`

- {ref}`SpecTypeEnabledByExpression`

- {ref}`SpecTypeInterfaceIncludeLinkRole`

- {ref}`SpecTypeRootItemType`

Please have a look at the following example:

```{code-block} yaml
enabled-by:
  and:
  - RTEMS_NETWORKING
  - not: RTEMS_SMP
```

(SpecTypeExternalDocumentReference)=

### External Document Reference

This type refines the {ref}`SpecTypeExternalReference` through the `type`
attribute if the value is `document`. It specifies a reference to a document.

All explicit attributes shall be specified. The explicit attributes for this
type are:

name
: The attribute value shall be a string. It shall be the name of the document.

(SpecTypeExternalFileReference)=

### External File Reference

This type refines the {ref}`SpecTypeExternalReference` through the `type`
attribute if the value is `file`. It specifies a reference to a file.

All explicit attributes shall be specified. The explicit attributes for this
type are:

hash
: The attribute value shall be a {ref}`SpecTypeSHA256HashValue`. It shall be
  the SHA256 hash value of the content of the referenced file.

(SpecTypeExternalReference)=

### External Reference

This set of attributes specifies a reference to some object external to the
specification. All explicit attributes shall be specified. The explicit
attributes for this type are:

identifier
: The attribute value shall be a string. It shall be the type-specific
  identifier of the referenced object. For *group* references use the Doxygen
  group identifier. For *file* references use a file system path to the file.

type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the type of
  the referenced object.

This type is refined by the following types:

- {ref}`SpecTypeExternalDocumentReference`

- {ref}`SpecTypeExternalFileReference`

- {ref}`SpecTypeGenericExternalReference`

This type is used by the following types:

- {ref}`SpecTypeInterfaceUnspecifiedHeaderFileItemType`

- {ref}`SpecTypeInterfaceUnspecifiedItemType`

- {ref}`SpecTypeRequirementItemType`

- {ref}`SpecTypeRequirementValidationItemType`

(SpecTypeFunctionImplementationLinkRole)=

### Function Implementation Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `function-implementation`. It defines the function implementation role
of links. It is used to indicate that a
{ref}`SpecTypeFunctionalRequirementItemType` item specifies parts of the
function.

(SpecTypeGenericExternalReference)=

### Generic External Reference

This type refines the following types:

- {ref}`SpecTypeExternalReference` through the `type` attribute if the value is
  `define`

- {ref}`SpecTypeExternalReference` through the `type` attribute if the value is
  `function`

- {ref}`SpecTypeExternalReference` through the `type` attribute if the value is
  `group`

- {ref}`SpecTypeExternalReference` through the `type` attribute if the value is
  `macro`

- {ref}`SpecTypeExternalReference` through the `type` attribute if the value is
  `url`

- {ref}`SpecTypeExternalReference` through the `type` attribute if the value is
  `variable`

It specifies a reference to an object of the specified type.

(SpecTypeGlossaryMembershipLinkRole)=

### Glossary Membership Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `glossary-member`. It defines the glossary membership role of links.

(SpecTypeIntegerOrString)=

### Integer or String

A value of this type shall be of one of the following variants:

- The value may be an integer number.

- The value may be a string.

This type is used by the following types:

- {ref}`SpecTypeApplicationConfigurationValueOptionItemType`

- {ref}`SpecTypeBuildOptionAction`

(SpecTypeInterfaceBriefDescription)=

### Interface Brief Description

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It shall be the brief description of the
  interface. It should be a single sentence. The value shall not match with the
  regular expression "`\n\n`".

This type is used by the following types:

- {ref}`SpecTypeInterfaceCompoundItemType`

- {ref}`SpecTypeInterfaceCompoundMemberDefinition`

- {ref}`SpecTypeInterfaceDefineItemType`

- {ref}`SpecTypeInterfaceEnumItemType`

- {ref}`SpecTypeInterfaceEnumeratorItemType`

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

- {ref}`SpecTypeInterfaceGroupItemType`

- {ref}`SpecTypeInterfaceHeaderFileItemType`

- {ref}`SpecTypeInterfaceTypedefItemType`

- {ref}`SpecTypeInterfaceVariableItemType`

- {ref}`SpecTypeRegisterBitsDefinition`

- {ref}`SpecTypeRegisterBlockItemType`

- {ref}`SpecTypeRegisterDefinition`

(SpecTypeInterfaceCompoundDefinitionKind)=

### Interface Compound Definition Kind

The value shall be a string. It specifies how the interface compound is
defined. It may be a typedef only, the struct or union only, or a typedef with
a struct or union definition. The value shall be an element of

- "`struct-only`",

- "`typedef-and-struct`",

- "`typedef-and-union`",

- "`typedef-only`", and

- "`union-only`".

This type is used by the following types:

- {ref}`SpecTypeInterfaceCompoundItemType`

(SpecTypeInterfaceCompoundMemberCompound)=

### Interface Compound Member Compound

This type refines the following types:

- {ref}`SpecTypeInterfaceCompoundMemberDefinition` through the `kind` attribute
  if the value is `struct`

- {ref}`SpecTypeInterfaceCompoundMemberDefinition` through the `kind` attribute
  if the value is `union`

This set of attributes specifies an interface compound member compound. All
explicit attributes shall be specified. The explicit attributes for this type
are:

definition
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceCompoundMemberDefinitionDirective`.

(SpecTypeInterfaceCompoundMemberDeclaration)=

### Interface Compound Member Declaration

This type refines the {ref}`SpecTypeInterfaceCompoundMemberDefinition` through
the `kind` attribute if the value is `member`. This set of attributes specifies
an interface compound member declaration. All explicit attributes shall be
specified. The explicit attributes for this type are:

definition
: The attribute value shall be a string. It shall be the interface compound
  member declaration. On the declaration a context-sensitive substitution of
  item variables is performed.

(SpecTypeInterfaceCompoundMemberDefinition)=

### Interface Compound Member Definition

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes specifies an
  interface compound member definition. All explicit attributes shall be
  specified. The explicit attributes for this type are:

  brief
  : The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

  description
  : The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

  kind
  : The attribute value shall be a string. It shall be the interface compound
    member kind.

  name
  : The attribute value shall be a string. It shall be the interface compound
    member name.

- There may be no value (null).

This type is refined by the following types:

- {ref}`SpecTypeInterfaceCompoundMemberCompound`

- {ref}`SpecTypeInterfaceCompoundMemberDeclaration`

This type is used by the following types:

- {ref}`SpecTypeInterfaceCompoundMemberDefinitionDirective`

- {ref}`SpecTypeInterfaceCompoundMemberDefinitionVariant`

(SpecTypeInterfaceCompoundMemberDefinitionDirective)=

### Interface Compound Member Definition Directive

This set of attributes specifies an interface compound member definition
directive. All explicit attributes shall be specified. The explicit attributes
for this type are:

default
: The attribute value shall be an
  {ref}`SpecTypeInterfaceCompoundMemberDefinition`. The default definition will
  be used if no variant-specific definition is enabled.

variants
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceCompoundMemberDefinitionVariant`.

This type is used by the following types:

- {ref}`SpecTypeInterfaceCompoundItemType`

- {ref}`SpecTypeInterfaceCompoundMemberCompound`

(SpecTypeInterfaceCompoundMemberDefinitionVariant)=

### Interface Compound Member Definition Variant

This set of attributes specifies an interface compound member definition
variant. All explicit attributes shall be specified. The explicit attributes
for this type are:

definition
: The attribute value shall be an
  {ref}`SpecTypeInterfaceCompoundMemberDefinition`. The definition will be used
  if the expression defined by the `enabled-by` attribute evaluates to true. In
  generated header files, the expression is evaluated by the C preprocessor.

enabled-by
: The attribute value shall be an {ref}`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

- {ref}`SpecTypeInterfaceCompoundMemberDefinitionDirective`

(SpecTypeInterfaceDefinition)=

### Interface Definition

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It shall be the definition. On the definition a
  context-sensitive substitution of item variables is performed.

This type is used by the following types:

- {ref}`SpecTypeInterfaceDefinitionDirective`

- {ref}`SpecTypeInterfaceDefinitionVariant`

(SpecTypeInterfaceDefinitionDirective)=

### Interface Definition Directive

This set of attributes specifies an interface definition directive. All
explicit attributes shall be specified. The explicit attributes for this type
are:

default
: The attribute value shall be an {ref}`SpecTypeInterfaceDefinition`. The
  default definition will be used if no variant-specific definition is enabled.

variants
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceDefinitionVariant`.

This type is used by the following types:

- {ref}`SpecTypeInterfaceDefineItemType`

- {ref}`SpecTypeInterfaceEnumeratorItemType`

- {ref}`SpecTypeInterfaceTypedefItemType`

- {ref}`SpecTypeInterfaceVariableItemType`

(SpecTypeInterfaceDefinitionVariant)=

### Interface Definition Variant

This set of attributes specifies an interface definition variant. All explicit
attributes shall be specified. The explicit attributes for this type are:

definition
: The attribute value shall be an {ref}`SpecTypeInterfaceDefinition`. The
  definition will be used if the expression defined by the `enabled-by`
  attribute evaluates to true. In generated header files, the expression is
  evaluated by the C preprocessor.

enabled-by
: The attribute value shall be an {ref}`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

- {ref}`SpecTypeInterfaceDefinitionDirective`

(SpecTypeInterfaceDescription)=

### Interface Description

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It shall be the description of the interface. The
  description should be short and concentrate on the average case. All special
  cases, usage notes, constraints, error conditions, configuration
  dependencies, references, etc. should be described in the
  {ref}`SpecTypeInterfaceNotes`.

This type is used by the following types:

- {ref}`SpecTypeApplicationConfigurationOptionItemType`

- {ref}`SpecTypeInterfaceCompoundItemType`

- {ref}`SpecTypeInterfaceCompoundMemberDefinition`

- {ref}`SpecTypeInterfaceDefineItemType`

- {ref}`SpecTypeInterfaceEnumItemType`

- {ref}`SpecTypeInterfaceEnumeratorItemType`

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

- {ref}`SpecTypeInterfaceGroupItemType`

- {ref}`SpecTypeInterfaceParameter`

- {ref}`SpecTypeInterfaceReturnValue`

- {ref}`SpecTypeInterfaceTypedefItemType`

- {ref}`SpecTypeInterfaceVariableItemType`

- {ref}`SpecTypeRegisterBitsDefinition`

- {ref}`SpecTypeRegisterBlockItemType`

- {ref}`SpecTypeRegisterDefinition`

(SpecTypeInterfaceEnabledByExpression)=

### Interface Enabled-By Expression

A value of this type shall be an expression which defines under which
conditions an interface definition is enabled. In generated header files, the
expression is evaluated by the C preprocessor.

A value of this type shall be of one of the following variants:

- The value may be a boolean. It is converted to 0 or 1. It defines a symbol in
  the expression.

- The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeInterfaceEnabledByExpression`. The *and* operator defines a
    *logical and* of the expressions in the list.

  not
  : The attribute value shall be an
    {ref}`SpecTypeInterfaceEnabledByExpression`. The *not* operator defines a
    *logical not* of the expression.

  or
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeInterfaceEnabledByExpression`. The *or* operator defines a
    *logical or* of the expressions in the list.

- The value may be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceEnabledByExpression`. It defines a *logical or* of the
  expressions in the list.

- The value may be a string. It defines a symbol in the expression.

This type is used by the following types:

- {ref}`SpecTypeInterfaceCompoundMemberDefinitionVariant`

- {ref}`SpecTypeInterfaceDefinitionVariant`

- {ref}`SpecTypeInterfaceEnabledByExpression`

- {ref}`SpecTypeInterfaceFunctionOrMacroDefinitionVariant`

- {ref}`SpecTypeRegisterBitsDefinitionVariant`

- {ref}`SpecTypeRegisterBlockMemberDefinitionVariant`

(SpecTypeInterfaceEnumDefinitionKind)=

### Interface Enum Definition Kind

The value shall be a string. It specifies how the enum is defined. It may be a
typedef only, the enum only, or a typedef with an enum definition. The value
shall be an element of

- "`enum-only`",

- "`typedef-and-enum`", and

- "`typedef-only`".

This type is used by the following types:

- {ref}`SpecTypeInterfaceEnumItemType`

(SpecTypeInterfaceEnumeratorLinkRole)=

### Interface Enumerator Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-enumerator`. It defines the interface enumerator role of
links.

(SpecTypeInterfaceFunctionLinkRole)=

### Interface Function Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-function`. It defines the interface function role of links.
It is used to indicate that a {ref}`SpecTypeActionRequirementItemType` item
specifies functional requirements of an
{ref}`SpecTypeInterfaceFunctionOrMacroItemType` item.

(SpecTypeInterfaceFunctionOrMacroDefinition)=

### Interface Function or Macro Definition

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes specifies a
  function definition. All explicit attributes shall be specified. The explicit
  attributes for this type are:

  attributes
  : The attribute value shall be an optional string. If the value is present,
    then it shall be the function attributes. On the attributes a
    context-sensitive substitution of item variables is performed. A function
    attribute is for example the indication that the function does not return
    to the caller.

  body
  : The attribute value shall be an optional string. If the value is present,
    then it shall be the definition of a static inline function. On the
    function definition a context-sensitive substitution of item variables is
    performed. If no value is present, then the function is declared as an
    external function.

  params
  : The attribute value shall be a list of strings. It shall be the list of
    parameter declarations of the function. On the function parameter
    declarations a context-sensitive substitution of item variables is
    performed.

  return
  : The attribute value shall be an optional string. If the value is present,
    then it shall be the function return type. On the return type a
    context-sensitive substitution of item variables is performed.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeInterfaceFunctionOrMacroDefinitionDirective`

- {ref}`SpecTypeInterfaceFunctionOrMacroDefinitionVariant`

(SpecTypeInterfaceFunctionOrMacroDefinitionDirective)=

### Interface Function or Macro Definition Directive

This set of attributes specifies a function or macro definition directive. All
explicit attributes shall be specified. The explicit attributes for this type
are:

default
: The attribute value shall be an
  {ref}`SpecTypeInterfaceFunctionOrMacroDefinition`. The default definition
  will be used if no variant-specific definition is enabled.

variants
: The attribute value shall be a list. Each list element shall be an
  {ref}`SpecTypeInterfaceFunctionOrMacroDefinitionVariant`.

This type is used by the following types:

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

(SpecTypeInterfaceFunctionOrMacroDefinitionVariant)=

### Interface Function or Macro Definition Variant

This set of attributes specifies a function or macro definition variant. All
explicit attributes shall be specified. The explicit attributes for this type
are:

definition
: The attribute value shall be an
  {ref}`SpecTypeInterfaceFunctionOrMacroDefinition`. The definition will be
  used if the expression defined by the `enabled-by` attribute evaluates to
  true. In generated header files, the expression is evaluated by the C
  preprocessor.

enabled-by
: The attribute value shall be an {ref}`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

- {ref}`SpecTypeInterfaceFunctionOrMacroDefinitionDirective`

(SpecTypeInterfaceGroupIdentifier)=

### Interface Group Identifier

The value shall be a string. It shall be the identifier of the interface group.
The value shall match with the regular expression "`^[A-Z][a-zA-Z0-9]*$`".

This type is used by the following types:

- {ref}`SpecTypeInterfaceGroupItemType`

- {ref}`SpecTypeRegisterBlockItemType`

(SpecTypeInterfaceGroupMembershipLinkRole)=

### Interface Group Membership Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-ingroup`. It defines the interface group membership role of
links.

(SpecTypeInterfaceHiddenGroupMembershipLinkRole)=

### Interface Hidden Group Membership Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-ingroup-hidden`. It defines the interface hidden group
membership role of links. This role may be used to make an interface a group
member and hide this relationship in the documentation. An example is an
optimized macro implementation of a directive which has the same name as the
corresponding directive.

(SpecTypeInterfaceIncludeLinkRole)=

### Interface Include Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-include`. It defines the interface include role of links
and is used to indicate that an interface container includes another interface
container. For example, one header file includes another header file. All
explicit attributes shall be specified. The explicit attributes for this type
are:

enabled-by
: The attribute value shall be an {ref}`SpecTypeEnabledByExpression`. It shall
  define under which conditions the interface container is included.

(SpecTypeInterfaceNotes)=

### Interface Notes

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It shall be the notes for the interface.

This type is used by the following types:

- {ref}`SpecTypeApplicationConfigurationOptionItemType`

- {ref}`SpecTypeInterfaceCompoundItemType`

- {ref}`SpecTypeInterfaceDefineItemType`

- {ref}`SpecTypeInterfaceEnumeratorItemType`

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

- {ref}`SpecTypeInterfaceTypedefItemType`

- {ref}`SpecTypeInterfaceVariableItemType`

- {ref}`SpecTypeRegisterBlockItemType`

(SpecTypeInterfaceParameter)=

### Interface Parameter

This set of attributes specifies an interface parameter. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

dir
: The attribute value shall be an {ref}`SpecTypeInterfaceParameterDirection`.

name
: The attribute value shall be a string. It shall be the interface parameter
  name.

This type is used by the following types:

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

- {ref}`SpecTypeInterfaceTypedefItemType`

(SpecTypeInterfaceParameterDirection)=

### Interface Parameter Direction

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It specifies the interface parameter direction.
  The value shall be an element of

  - "`in`",

  - "`out`", and

  - "`inout`".

This type is used by the following types:

- {ref}`SpecTypeInterfaceParameter`

- {ref}`SpecTypeTestRunParameter`

(SpecTypeInterfacePlacementLinkRole)=

### Interface Placement Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-placement`. It defines the interface placement role of
links. It is used to indicate that an interface definition is placed into an
interface container, for example a header file.

(SpecTypeInterfaceReturnDirective)=

### Interface Return Directive

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes specifies an
  interface return. All explicit attributes shall be specified. The explicit
  attributes for this type are:

  return
  : The attribute value shall be an optional string. It shall describe the
    interface return for unspecified return values.

  return-values
  : The attribute value shall be a list. Each list element shall be an
    {ref}`SpecTypeInterfaceReturnValue`.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeInterfaceFunctionOrMacroItemType`

- {ref}`SpecTypeInterfaceTypedefItemType`

(SpecTypeInterfaceReturnValue)=

### Interface Return Value

This set of attributes specifies an interface return value. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

value
: The attribute value shall be a {ref}`SpecTypeBooleanOrIntegerOrString`. It
  shall be the described interface return value.

This type is used by the following types:

- {ref}`SpecTypeInterfaceReturnDirective`

(SpecTypeInterfaceTargetLinkRole)=

### Interface Target Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `interface-target`. It defines the interface target role of links. It
is used for interface forward declarations.

(SpecTypeLink)=

### Link

This set of attributes specifies a link from one specification item to another
specification item. The links in a list are ordered. The first link in the list
is processed first. All explicit attributes shall be specified. The explicit
attributes for this type are:

role
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the role of
  the link.

uid
: The attribute value shall be an {ref}`SpecTypeUID`. It shall be the absolute
  or relative UID of the link target item.

This type is refined by the following types:

- {ref}`SpecTypeBuildDependencyConditionalLinkRole`

- {ref}`SpecTypeBuildDependencyLinkRole`

- {ref}`SpecTypeConstraintLinkRole`

- {ref}`SpecTypeFunctionImplementationLinkRole`

- {ref}`SpecTypeGlossaryMembershipLinkRole`

- {ref}`SpecTypeInterfaceEnumeratorLinkRole`

- {ref}`SpecTypeInterfaceFunctionLinkRole`

- {ref}`SpecTypeInterfaceGroupMembershipLinkRole`

- {ref}`SpecTypeInterfaceHiddenGroupMembershipLinkRole`

- {ref}`SpecTypeInterfaceIncludeLinkRole`

- {ref}`SpecTypeInterfacePlacementLinkRole`

- {ref}`SpecTypeInterfaceTargetLinkRole`

- {ref}`SpecTypePerformanceRuntimeLimitsLinkRole`

- {ref}`SpecTypePlacementOrderLinkRole`

- {ref}`SpecTypeProxyMemberLinkRole`

- {ref}`SpecTypeRegisterBlockIncludeRole`

- {ref}`SpecTypeRequirementRefinementLinkRole`

- {ref}`SpecTypeRequirementValidationLinkRole`

- {ref}`SpecTypeRuntimeMeasurementRequestLinkRole`

- {ref}`SpecTypeSpecificationMemberLinkRole`

- {ref}`SpecTypeSpecificationRefinementLinkRole`

- {ref}`SpecTypeUnitTestLinkRole`

This type is used by the following types:

- {ref}`SpecTypeRootItemType`

- {ref}`SpecTypeTestCaseAction`

- {ref}`SpecTypeTestCaseCheck`

(SpecTypeName)=

### Name

The value shall be a string. It shall be an attribute name. The value shall
match with the regular expression
"`^([a-z][a-z0-9-]*|SPDX-License-Identifier)$`".

This type is used by the following types:

- {ref}`SpecTypeApplicationConfigurationOptionItemType`

- {ref}`SpecTypeBuildItemType`

- {ref}`SpecTypeExternalReference`

- {ref}`SpecTypeFunctionalRequirementItemType`

- {ref}`SpecTypeGlossaryItemType`

- {ref}`SpecTypeInterfaceItemType`

- {ref}`SpecTypeLink`

- {ref}`SpecTypeNonFunctionalRequirementItemType`

- {ref}`SpecTypeRegisterDefinition`

- {ref}`SpecTypeRequirementItemType`

- {ref}`SpecTypeRequirementValidationItemType`

- {ref}`SpecTypeRootItemType`

- {ref}`SpecTypeRuntimeMeasurementParameterSet`

- {ref}`SpecTypeRuntimePerformanceParameterSet`

- {ref}`SpecTypeSpecificationAttributeValue`

- {ref}`SpecTypeSpecificationExplicitAttributes`

- {ref}`SpecTypeSpecificationGenericAttributes`

- {ref}`SpecTypeSpecificationItemType`

- {ref}`SpecTypeSpecificationList`

- {ref}`SpecTypeSpecificationRefinementLinkRole`

(SpecTypeOptionalFloatingPointNumber)=

### Optional Floating-Point Number

A value of this type shall be of one of the following variants:

- The value may be a floating-point number.

- There may be no value (null).

(SpecTypeOptionalInteger)=

### Optional Integer

A value of this type shall be of one of the following variants:

- The value may be an integer number.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeRegisterBlockItemType`

(SpecTypeOptionalString)=

### Optional String

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string.

(SpecTypePerformanceRuntimeLimitsLinkRole)=

### Performance Runtime Limits Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `performance-runtime-limits`. It defines the performance runtime
limits role of links. All explicit attributes shall be specified. The explicit
attributes for this type are:

limits
: The attribute value shall be a
  {ref}`SpecTypeRuntimeMeasurementEnvironmentTable`.

(SpecTypePlacementOrderLinkRole)=

### Placement Order Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `placement-order`. This link role defines the placement order of items
in a container item (for example an interface function in a header file or a
documentation section).

(SpecTypeProxyMemberLinkRole)=

### Proxy Member Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `proxy-member`. It defines the proxy member role of links. Items may
use this role to link to {ref}`SpecTypeProxyItemTypes` items.

(SpecTypeRegisterBitsDefinition)=

### Register Bits Definition

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes specifies a
  register bit field. Single bits are bit fields with a width of one. All
  explicit attributes shall be specified. The explicit attributes for this type
  are:

  brief
  : The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

  description
  : The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

  name
  : The attribute value shall be a string. It shall be the name of the register
    bit field.

  properties
  : The attribute value shall be a list of strings. It shall be the list of bit
    field properties. Properties are for example if the bit field can be read
    or written, or an access has side-effects such as clearing a status.

  start
  : The attribute value shall be an integer number. It shall be the start bit
    of the bit field. Bit `0` is the least-significant bit.

  width
  : The attribute value shall be an integer number. It shall be the width in
    bits of the bit field.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeRegisterBitsDefinitionDirective`

- {ref}`SpecTypeRegisterBitsDefinitionVariant`

(SpecTypeRegisterBitsDefinitionDirective)=

### Register Bits Definition Directive

This set of attributes specifies a register bits directive. All explicit
attributes shall be specified. The explicit attributes for this type are:

default
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterBitsDefinition`. The default definition will be used if
  no variant-specific definition is enabled.

variants
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterBitsDefinitionVariant`.

This type is used by the following types:

- {ref}`SpecTypeRegisterDefinition`

(SpecTypeRegisterBitsDefinitionVariant)=

### Register Bits Definition Variant

This set of attributes specifies a register bits variant. All explicit
attributes shall be specified. The explicit attributes for this type are:

definition
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterBitsDefinition`. The definition will be used if the
  expression defined by the `enabled-by` attribute evaluates to true. In
  generated header files, the expression is evaluated by the C preprocessor.

enabled-by
: The attribute value shall be an {ref}`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

- {ref}`SpecTypeRegisterBitsDefinitionDirective`

(SpecTypeRegisterBlockIncludeRole)=

### Register Block Include Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `register-block-include`. It defines the register block include role
of links. Links of this role are used to build register blocks using other
register blocks. All explicit attributes shall be specified. The explicit
attributes for this type are:

name
: The attribute value shall be a string. It shall be a name to identify the
  included register block within the item. The name shall be unique within the
  scope of the item links of this role and the {ref}`SpecTypeRegisterList`.

(SpecTypeRegisterBlockMemberDefinition)=

### Register Block Member Definition

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes specifies a
  register block member definition. All explicit attributes shall be specified.
  The explicit attributes for this type are:

  count
  : The attribute value shall be an integer number. It shall be the count of
    registers of the register block member.

  name
  : The attribute value shall be a {ref}`SpecTypeRegisterName`.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeRegisterBlockMemberDefinitionDirective`

- {ref}`SpecTypeRegisterBlockMemberDefinitionVariant`

(SpecTypeRegisterBlockMemberDefinitionDirective)=

### Register Block Member Definition Directive

This set of attributes specifies a register block member definition directive.
All explicit attributes shall be specified. The explicit attributes for this
type are:

default
: The attribute value shall be a {ref}`SpecTypeRegisterBlockMemberDefinition`.
  The default definition will be used if no variant-specific definition is
  enabled.

offset
: The attribute value shall be an integer number. It shall be the address of
  the register block member relative to the base address of the register block.

variants
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterBlockMemberDefinitionVariant`.

This type is used by the following types:

- {ref}`SpecTypeRegisterBlockItemType`

(SpecTypeRegisterBlockMemberDefinitionVariant)=

### Register Block Member Definition Variant

This set of attributes specifies a register block member definition variant.
All explicit attributes shall be specified. The explicit attributes for this
type are:

definition
: The attribute value shall be a {ref}`SpecTypeRegisterBlockMemberDefinition`.
  The definition will be used if the expression defined by the `enabled-by`
  attribute evaluates to true. In generated header files, the expression is
  evaluated by the C preprocessor.

enabled-by
: The attribute value shall be an {ref}`SpecTypeInterfaceEnabledByExpression`.

This type is used by the following types:

- {ref}`SpecTypeRegisterBlockMemberDefinitionDirective`

(SpecTypeRegisterDefinition)=

### Register Definition

This set of attributes specifies a register. All explicit attributes shall be
specified. The explicit attributes for this type are:

bits
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeRegisterBitsDefinitionDirective`.

brief
: The attribute value shall be an {ref}`SpecTypeInterfaceBriefDescription`.

description
: The attribute value shall be an {ref}`SpecTypeInterfaceDescription`.

name
: The attribute value shall be a string. It shall be the name to identify the
  register definition. The name shall be unique within the scope of the
  {ref}`SpecTypeRegisterBlockIncludeRole` links of the item and the
  {ref}`SpecTypeRegisterList`.

width
: The attribute value shall be an integer number. It shall be the width of the
  register in bits.

In addition to the explicit attributes, generic attributes may be specified.
Each generic attribute key shall be a {ref}`SpecTypeName`. The attribute value
may have any type.

This type is used by the following types:

- {ref}`SpecTypeRegisterBlockItemType`

(SpecTypeRegisterName)=

### Register Name

The value shall be a string. The name consists either of an identifier, or an
identifier and an alias. The identifier and alias are separated by a colon
(`:`). The identifier shall match with the name of a register definition of the
item (see {ref}`SpecTypeRegisterDefinition`) or the name of a register block
include of the item (see {ref}`SpecTypeRegisterBlockIncludeRole`). If no alias
is specified, then the identifier is used for the register block member name,
otherwise the alias is used. If the register block member names are not unique
within the item, then a postfix number is appended to the names. The number
starts with zero for each set of names. The value shall match with the regular
expression "`^[a-zA-Z_][a-zA-Z0-9_]*(:[a-zA-Z_][a-zA-Z0-9_]*)?$`".

This type is used by the following types:

- {ref}`SpecTypeRegisterBlockMemberDefinition`

(SpecTypeRequirementDesignGroupIdentifier)=

### Requirement Design Group Identifier

A value of this type shall be of one of the following variants:

- There may be no value (null).

- The value may be a string. It shall be the identifier of the requirement
  design group. The value shall match with the regular expression
  "`^[a-zA-Z0-9_]*$`".

This type is used by the following types:

- {ref}`SpecTypeDesignGroupRequirementItemType`

(SpecTypeRequirementRefinementLinkRole)=

### Requirement Refinement Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `requirement-refinement`. It defines the requirement refinement role
of links.

(SpecTypeRequirementText)=

### Requirement Text

The value shall be a string. It shall state a requirement or constraint. The
text should not use one of the following words or phrases:

- acceptable

- adequate

- almost always

- and/or

- appropriate

- approximately

- as far as possible

- as much as practicable

- best

- best possible

- easy

- efficient

- e.g.

- enable

- enough

- etc.

- few

- first rate

- flexible

- generally

- goal

- graceful

- great

- greatest

- ideally

- i.e.

- if possible

- in most cases

- large

- many

- maximize

- minimize

- most

- multiple

- necessary

- numerous

- optimize

- ought to

- probably

- quick

- rapid

- reasonably

- relevant

- robust

- satisfactory

- several

- shall be included but not limited to

- simple

- small

- some

- state of the art

- sufficient

- suitable

- support

- systematically

- transparent

- typical

- user friendly

- usually

- versatile

- when necessary

This type is used by the following types:

- {ref}`SpecTypeActionRequirementState`

- {ref}`SpecTypeApplicationConfigurationGroupItemType`

- {ref}`SpecTypeConstraintItemType`

- {ref}`SpecTypeInterfaceGroupItemType`

- {ref}`SpecTypeRequirementItemType`

(SpecTypeRequirementValidationLinkRole)=

### Requirement Validation Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `validation`. It defines the requirement validation role of links.

(SpecTypeRuntimeMeasurementEnvironmentName)=

### Runtime Measurement Environment Name

The value shall be a string. It specifies the runtime measurement environment
name. The value

- shall be an element of

  - "`FullCache`",

  - "`HotCache`", and

  - "`DirtyCache`",

- or, shall match with the regular expression "`^Load/[1-9][0-9]*$`".

This type is used by the following types:

- {ref}`SpecTypeRuntimeMeasurementEnvironmentTable`

(SpecTypeRuntimeMeasurementEnvironmentTable)=

### Runtime Measurement Environment Table

This set of attributes provides runtime performance limits for a set of runtime
measurement environments. Generic attributes may be specified. Each generic
attribute key shall be a {ref}`SpecTypeRuntimeMeasurementEnvironmentName`. Each
generic attribute value shall be a {ref}`SpecTypeRuntimeMeasurementValueTable`.

This type is used by the following types:

- {ref}`SpecTypePerformanceRuntimeLimitsLinkRole`

(SpecTypeRuntimeMeasurementParameterSet)=

### Runtime Measurement Parameter Set

This set of attributes defines parameters of the runtime measurement test case.
All explicit attributes shall be specified. The explicit attributes for this
type are:

sample-count
: The attribute value shall be an integer number. It shall be the sample count
  of the runtime measurement context.

In addition to the explicit attributes, generic attributes may be specified.
Each generic attribute key shall be a {ref}`SpecTypeName`. The attribute value
may have any type.

This type is used by the following types:

- {ref}`SpecTypeRuntimeMeasurementTestItemType`

(SpecTypeRuntimeMeasurementRequestLinkRole)=

### Runtime Measurement Request Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `runtime-measurement-request`. It defines the runtime measurement
request role of links. The link target shall be a
{ref}`SpecTypeRuntimeMeasurementTestItemType` item.

(SpecTypeRuntimeMeasurementValueKind)=

### Runtime Measurement Value Kind

The value shall be a string. It specifies the kind of a runtime measurement
value. The value shall be an element of

- "`max-lower-bound`",

- "`max-upper-bound`",

- "`mean-lower-bound`",

- "`mean-upper-bound`",

- "`median-lower-bound`",

- "`median-upper-bound`",

- "`min-lower-bound`", and

- "`min-upper-bound`".

This type is used by the following types:

- {ref}`SpecTypeRuntimeMeasurementValueTable`

(SpecTypeRuntimeMeasurementValueTable)=

### Runtime Measurement Value Table

This set of attributes provides a set of runtime measurement values each of a
specified kind. The unit of the values shall be one second. Generic attributes
may be specified. Each generic attribute key shall be a
{ref}`SpecTypeRuntimeMeasurementValueKind`. Each generic attribute value shall
be a floating-point number.

This type is used by the following types:

- {ref}`SpecTypeRuntimeMeasurementEnvironmentTable`

(SpecTypeRuntimePerformanceParameterSet)=

### Runtime Performance Parameter Set

This set of attributes defines parameters of the runtime performance
requirement. Generic attributes may be specified. Each generic attribute key
shall be a {ref}`SpecTypeName`. The attribute value may have any type.

This type is used by the following types:

- {ref}`SpecTypeRuntimePerformanceRequirementItemType`

(SpecTypeSHA256HashValue)=

### SHA256 Hash Value

The value shall be a string. It shall be a SHA256 hash value encoded in
base64url. The value shall match with the regular expression
"`^[A-Za-z0-9+_=-]{44}$`".

This type is used by the following types:

- {ref}`SpecTypeExternalFileReference`

(SpecTypeSPDXLicenseIdentifier)=

### SPDX License Identifier

The value shall be a string. It defines the license of the item expressed
though an SPDX License Identifier. The value

- shall be equal to "`CC-BY-SA-4.0 OR BSD-2-Clause`",

- or, shall be equal to "`BSD-2-Clause`",

- or, shall be equal to "`CC-BY-SA-4.0`".

This type is used by the following types:

- {ref}`SpecTypeRootItemType`

(SpecTypeSpecificationAttributeSet)=

### Specification Attribute Set

This set of attributes specifies a set of attributes. The following explicit
attributes are mandatory:

- `attributes`

- `description`

- `mandatory-attributes`

The explicit attributes for this type are:

attributes
: The attribute value shall be a
  {ref}`SpecTypeSpecificationExplicitAttributes`. It shall specify the explicit
  attributes of the attribute set.

description
: The attribute value shall be an optional string. It shall be the description
  of the attribute set.

generic-attributes
: The attribute value shall be a {ref}`SpecTypeSpecificationGenericAttributes`.
  It shall specify the generic attributes of the attribute set.

mandatory-attributes
: The attribute value shall be a
  {ref}`SpecTypeSpecificationMandatoryAttributes`. It shall specify the
  mandatory attributes of the attribute set.

This type is used by the following types:

- {ref}`SpecTypeSpecificationInformation`

(SpecTypeSpecificationAttributeValue)=

### Specification Attribute Value

This set of attributes specifies an attribute value. All explicit attributes
shall be specified. The explicit attributes for this type are:

description
: The attribute value shall be an optional string. It shall be the description
  of the attribute value.

spec-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  specification type of the attribute value.

This type is used by the following types:

- {ref}`SpecTypeSpecificationExplicitAttributes`

(SpecTypeSpecificationBooleanValue)=

### Specification Boolean Value

This attribute set specifies a boolean value. Only the `description` attribute
is mandatory. The explicit attributes for this type are:

assert
: The attribute value shall be a boolean. This optional attribute defines the
  value constraint of the specified boolean value. If the value of the assert
  attribute is true, then the value of the specified boolean value shall be
  true. If the value of the assert attribute is false, then the value of the
  specified boolean value shall be false. In case the assert attribute is not
  present, then the value of the specified boolean value may be true or false.

description
: The attribute value shall be an optional string. It shall be the description
  of the specified boolean value.

This type is used by the following types:

- {ref}`SpecTypeSpecificationInformation`

(SpecTypeSpecificationExplicitAttributes)=

### Specification Explicit Attributes

Generic attributes may be specified. Each generic attribute key shall be a
{ref}`SpecTypeName`. Each generic attribute value shall be a
{ref}`SpecTypeSpecificationAttributeValue`. Each generic attribute specifies an
explicit attribute of the attribute set. The key of the each generic attribute
defines the attribute key of the explicit attribute.

This type is used by the following types:

- {ref}`SpecTypeSpecificationAttributeSet`

(SpecTypeSpecificationFloatingPointAssert)=

### Specification Floating-Point Assert

A value of this type shall be an expression which asserts that the
floating-point value of the specified attribute satisfies the required
constraints.

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeSpecificationFloatingPointAssert`. The *and* operator
    evaluates to the *logical and* of the evaluation results of the expressions
    in the list.

  eq
  : The attribute value shall be a floating-point number. The *eq* operator
    evaluates to true, if the value to check is equal to the value of this
    attribute, otherwise to false.

  ge
  : The attribute value shall be a floating-point number. The *ge* operator
    evaluates to true, if the value to check is greater than or equal to the
    value of this attribute, otherwise to false.

  gt
  : The attribute value shall be a floating-point number. The *gt* operator
    evaluates to true, if the value to check is greater than the value of this
    attribute, otherwise to false.

  le
  : The attribute value shall be a floating-point number. The *le* operator
    evaluates to true, if the value to check is less than or equal to the value
    of this attribute, otherwise to false.

  lt
  : The attribute value shall be a floating-point number. The *lt* operator
    evaluates to true, if the value to check is less than the value of this
    attribute, otherwise to false.

  ne
  : The attribute value shall be a floating-point number. The *ne* operator
    evaluates to true, if the value to check is not equal to the value of this
    attribute, otherwise to false.

  not
  : The attribute value shall be a
    {ref}`SpecTypeSpecificationFloatingPointAssert`. The *not* operator
    evaluates to the *logical not* of the evaluation results of the expression.

  or
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeSpecificationFloatingPointAssert`. The *or* operator
    evaluates to the *logical or* of the evaluation results of the expressions
    in the list.

- The value may be a list. Each list element shall be a
  {ref}`SpecTypeSpecificationFloatingPointAssert`. This list of expressions
  evaluates to the *logical or* of the evaluation results of the expressions in
  the list.

This type is used by the following types:

- {ref}`SpecTypeSpecificationFloatingPointAssert`

- {ref}`SpecTypeSpecificationFloatingPointValue`

(SpecTypeSpecificationFloatingPointValue)=

### Specification Floating-Point Value

This set of attributes specifies a floating-point value. Only the `description`
attribute is mandatory. The explicit attributes for this type are:

assert
: The attribute value shall be a
  {ref}`SpecTypeSpecificationFloatingPointAssert`. This optional attribute
  defines the value constraints of the specified floating-point value. In case
  the assert attribute is not present, then the value of the specified
  floating-point value may be every valid floating-point number.

description
: The attribute value shall be an optional string. It shall be the description
  of the specified floating-point value.

This type is used by the following types:

- {ref}`SpecTypeSpecificationInformation`

(SpecTypeSpecificationGenericAttributes)=

### Specification Generic Attributes

This set of attributes specifies generic attributes. Generic attributes are
attributes which are not explicitly specified by
{ref}`SpecTypeSpecificationExplicitAttributes`. They are restricted to uniform
attribute key and value types. All explicit attributes shall be specified. The
explicit attributes for this type are:

description
: The attribute value shall be an optional string. It shall be the description
  of the generic attributes.

key-spec-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  specification type of the generic attribute keys.

value-spec-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  specification type of the generic attribute values.

This type is used by the following types:

- {ref}`SpecTypeSpecificationAttributeSet`

(SpecTypeSpecificationInformation)=

### Specification Information

This set of attributes specifies attribute values. At least one of the explicit
attributes shall be specified. The explicit attributes for this type are:

bool
: The attribute value shall be a {ref}`SpecTypeSpecificationBooleanValue`. It
  shall specify a boolean value.

dict
: The attribute value shall be a {ref}`SpecTypeSpecificationAttributeSet`. It
  shall specify a set of attributes.

float
: The attribute value shall be a
  {ref}`SpecTypeSpecificationFloatingPointValue`. It shall specify a
  floating-point value.

int
: The attribute value shall be a {ref}`SpecTypeSpecificationIntegerValue`. It
  shall specify an integer value.

list
: The attribute value shall be a {ref}`SpecTypeSpecificationList`. It shall
  specify a list of attributes or values.

none
: The attribute shall have no value. It specifies that no value is required.

str
: The attribute value shall be a {ref}`SpecTypeSpecificationStringValue`. It
  shall specify a string.

This type is used by the following types:

- {ref}`SpecTypeSpecificationItemType`

(SpecTypeSpecificationIntegerAssert)=

### Specification Integer Assert

A value of this type shall be an expression which asserts that the integer
value of the specified attribute satisfies the required constraints.

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeSpecificationIntegerAssert`. The *and* operator evaluates to
    the *logical and* of the evaluation results of the expressions in the list.

  eq
  : The attribute value shall be an integer number. The *eq* operator evaluates
    to true, if the value to check is equal to the value of this attribute,
    otherwise to false.

  ge
  : The attribute value shall be an integer number. The *ge* operator evaluates
    to true, if the value to check is greater than or equal to the value of
    this attribute, otherwise to false.

  gt
  : The attribute value shall be an integer number. The *gt* operator evaluates
    to true, if the value to check is greater than the value of this attribute,
    otherwise to false.

  le
  : The attribute value shall be an integer number. The *le* operator evaluates
    to true, if the value to check is less than or equal to the value of this
    attribute, otherwise to false.

  lt
  : The attribute value shall be an integer number. The *lt* operator evaluates
    to true, if the value to check is less than the value of this attribute,
    otherwise to false.

  ne
  : The attribute value shall be an integer number. The *ne* operator evaluates
    to true, if the value to check is not equal to the value of this attribute,
    otherwise to false.

  not
  : The attribute value shall be a {ref}`SpecTypeSpecificationIntegerAssert`.
    The *not* operator evaluates to the *logical not* of the evaluation results
    of the expression.

  or
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeSpecificationIntegerAssert`. The *or* operator evaluates to
    the *logical or* of the evaluation results of the expressions in the list.

- The value may be a list. Each list element shall be a
  {ref}`SpecTypeSpecificationIntegerAssert`. This list of expressions evaluates
  to the *logical or* of the evaluation results of the expressions in the list.

This type is used by the following types:

- {ref}`SpecTypeSpecificationIntegerAssert`

- {ref}`SpecTypeSpecificationIntegerValue`

(SpecTypeSpecificationIntegerValue)=

### Specification Integer Value

This set of attributes specifies an integer value. Only the `description`
attribute is mandatory. The explicit attributes for this type are:

assert
: The attribute value shall be a {ref}`SpecTypeSpecificationIntegerAssert`.
  This optional attribute defines the value constraints of the specified
  integer value. In case the assert attribute is not present, then the value of
  the specified integer value may be every valid integer number.

description
: The attribute value shall be an optional string. It shall be the description
  of the specified integer value.

This type is used by the following types:

- {ref}`SpecTypeSpecificationInformation`

(SpecTypeSpecificationList)=

### Specification List

This set of attributes specifies a list of attributes or values. All explicit
attributes shall be specified. The explicit attributes for this type are:

description
: The attribute value shall be an optional string. It shall be the description
  of the list.

spec-type
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  specification type of elements of the list.

This type is used by the following types:

- {ref}`SpecTypeSpecificationInformation`

(SpecTypeSpecificationMandatoryAttributes)=

### Specification Mandatory Attributes

It defines which explicit attributes are mandatory.

A value of this type shall be of one of the following variants:

- The value may be a list. Each list element shall be a {ref}`SpecTypeName`.
  The list defines the mandatory attributes through their key names.

- The value may be a string. It defines how many explicit attributes are
  mandatory. If `none` is used, then none of the explicit attributes is
  mandatory, they are all optional. The value shall be an element of

  - "`all`",

  - "`at-least-one`",

  - "`at-most-one`",

  - "`exactly-one`", and

  - "`none`".

This type is used by the following types:

- {ref}`SpecTypeSpecificationAttributeSet`

(SpecTypeSpecificationMemberLinkRole)=

### Specification Member Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `spec-member`. It defines the specification membership role of links.

(SpecTypeSpecificationRefinementLinkRole)=

### Specification Refinement Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `spec-refinement`. It defines the specification refinement role of
links. All explicit attributes shall be specified. The explicit attributes for
this type are:

spec-key
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  specification type refinement attribute key of the specification refinement.

spec-value
: The attribute value shall be a {ref}`SpecTypeName`. It shall be the
  specification type refinement attribute value of the specification
  refinement.

(SpecTypeSpecificationStringAssert)=

### Specification String Assert

A value of this type shall be an expression which asserts that the string of
the specified attribute satisfies the required constraints.

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. Each attribute defines an operator.
  Exactly one of the explicit attributes shall be specified. The explicit
  attributes for this type are:

  and
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeSpecificationStringAssert`. The *and* operator evaluates to
    the *logical and* of the evaluation results of the expressions in the list.

  contains
  : The attribute value shall be a list of strings. The *contains* operator
    evaluates to true, if the string to check converted to lower case with all
    white space characters converted to a single space character contains a
    string of the list of strings of this attribute, otherwise to false.

  eq
  : The attribute value shall be a string. The *eq* operator evaluates to true,
    if the string to check is equal to the value of this attribute, otherwise
    to false.

  ge
  : The attribute value shall be a string. The *ge* operator evaluates to true,
    if the string to check is greater than or equal to the value of this
    attribute, otherwise to false.

  gt
  : The attribute value shall be a string. The *gt* operator evaluates to true,
    if the string to check is greater than the value of this attribute,
    otherwise to false.

  in
  : The attribute value shall be a list of strings. The *in* operator evaluates
    to true, if the string to check is contained in the list of strings of this
    attribute, otherwise to false.

  le
  : The attribute value shall be a string. The *le* operator evaluates to true,
    if the string to check is less than or equal to the value of this
    attribute, otherwise to false.

  lt
  : The attribute value shall be a string. The *lt* operator evaluates to true,
    if the string to check is less than the value of this attribute, otherwise
    to false.

  ne
  : The attribute value shall be a string. The *ne* operator evaluates to true,
    if the string to check is not equal to the value of this attribute,
    otherwise to false.

  not
  : The attribute value shall be a {ref}`SpecTypeSpecificationStringAssert`.
    The *not* operator evaluates to the *logical not* of the evaluation results
    of the expression.

  or
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeSpecificationStringAssert`. The *or* operator evaluates to
    the *logical or* of the evaluation results of the expressions in the list.

  re
  : The attribute value shall be a string. The *re* operator evaluates to true,
    if the string to check matches with the regular expression of this
    attribute, otherwise to false.

  uid
  : The attribute shall have no value. The *uid* operator evaluates to true, if
    the string is a valid UID, otherwise to false.

- The value may be a list. Each list element shall be a
  {ref}`SpecTypeSpecificationStringAssert`. This list of expressions evaluates
  to the *logical or* of the evaluation results of the expressions in the list.

This type is used by the following types:

- {ref}`SpecTypeSpecificationStringAssert`

- {ref}`SpecTypeSpecificationStringValue`

(SpecTypeSpecificationStringValue)=

### Specification String Value

This set of attributes specifies a string. Only the `description` attribute is
mandatory. The explicit attributes for this type are:

assert
: The attribute value shall be a {ref}`SpecTypeSpecificationStringAssert`. This
  optional attribute defines the constraints of the specified string. In case
  the assert attribute is not present, then the specified string may be every
  valid string.

description
: The attribute value shall be an optional string. It shall be the description
  of the specified string attribute.

This type is used by the following types:

- {ref}`SpecTypeSpecificationInformation`

(SpecTypeTestCaseAction)=

### Test Case Action

This set of attributes specifies a test case action. All explicit attributes
shall be specified. The explicit attributes for this type are:

action-brief
: The attribute value shall be an optional string. It shall be the test case
  action brief description.

action-code
: The attribute value shall be a string. It shall be the test case action code.

checks
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeTestCaseCheck`.

links
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeLink`. The links should use the
  {ref}`SpecTypeRequirementValidationLinkRole` for validation tests and the
  {ref}`SpecTypeUnitTestLinkRole` for unit tests.

This type is used by the following types:

- {ref}`SpecTypeTestCaseItemType`

(SpecTypeTestCaseCheck)=

### Test Case Check

This set of attributes specifies a test case check. All explicit attributes
shall be specified. The explicit attributes for this type are:

brief
: The attribute value shall be an optional string. It shall be the test case
  check brief description.

code
: The attribute value shall be a string. It shall be the test case check code.

links
: The attribute value shall be a list. Each list element shall be a
  {ref}`SpecTypeLink`. The links should use the
  {ref}`SpecTypeRequirementValidationLinkRole` for validation tests and the
  {ref}`SpecTypeUnitTestLinkRole` for unit tests.

This type is used by the following types:

- {ref}`SpecTypeTestCaseAction`

(SpecTypeTestContextMember)=

### Test Context Member

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes defines an
  action requirement test context member. All explicit attributes shall be
  specified. The explicit attributes for this type are:

  brief
  : The attribute value shall be an optional string. It shall be the test
    context member brief description.

  description
  : The attribute value shall be an optional string. It shall be the test
    context member description.

  member
  : The attribute value shall be a string. It shall be the test context member
    definition. It shall be a valid C structure member definition without a
    trailing `;`.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeActionRequirementItemType`

- {ref}`SpecTypeRuntimeMeasurementTestItemType`

- {ref}`SpecTypeTestCaseItemType`

(SpecTypeTestHeader)=

### Test Header

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes specifies a test
  header. In case a test header is specified, then instead of a test case a
  test run function will be generated. The test run function will be declared
  in the test header target file and defined in the test source target file.
  The test run function can be used to compose test cases. The test header file
  is not automatically included in the test source file. It should be added to
  the includes or local includes of the test. All explicit attributes shall be
  specified. The explicit attributes for this type are:

  code
  : The attribute value shall be an optional string. If the value is present,
    then it shall be the test header code. The header code is placed at file
    scope after the general test declarations and before the test run function
    declaration.

  freestanding
  : The attribute value shall be a boolean. The value shall be `true`, if the
    test case is freestanding, otherwise `false`. Freestanding test cases are
    not statically registered. Instead the generated test runner uses
    {c:func}`T_case_begin` and {c:func}`T_case_end`.

  includes
  : The attribute value shall be a list of strings. It shall be a list of
    header files included by the header file via `#include <...>`.

  local-includes
  : The attribute value shall be a list of strings. It shall be a list of
    header files included by the header file via `#include "..."`.

  run-params
  : The attribute value shall be a list. Each list element shall be a
    {ref}`SpecTypeTestRunParameter`.

  target
  : The attribute value shall be a string. It shall be the path to the
    generated test header file.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeActionRequirementItemType`

- {ref}`SpecTypeTestCaseItemType`

(SpecTypeTestRunParameter)=

### Test Run Parameter

This set of attributes specifies a parameter for the test run function. In case
this parameter is used in an {ref}`SpecTypeActionRequirementItemType` item,
then the parameter is also added as a member to the test context, see
{ref}`SpecTypeTestContextMember`. All explicit attributes shall be specified.
The explicit attributes for this type are:

description
: The attribute value shall be a string. It shall be the description of the
  parameter.

dir
: The attribute value shall be an {ref}`SpecTypeInterfaceParameterDirection`.

name
: The attribute value shall be a string. It shall be the parameter name.

specifier
: The attribute value shall be a string. It shall be the complete function
  parameter specifier. Use `${.:name}` for the parameter name, for example
  `"int ${.:name}"`.

This type is used by the following types:

- {ref}`SpecTypeTestHeader`

(SpecTypeTestSupportMethod)=

### Test Support Method

A value of this type shall be of one of the following variants:

- The value may be a set of attributes. This set of attributes defines an
  action requirement test support method. All explicit attributes shall be
  specified. The explicit attributes for this type are:

  brief
  : The attribute value shall be an optional string. It shall be the test
    support method brief description.

  code
  : The attribute value shall be a string. It shall be the test support method
    code. The code may use a local variable `ctx` which points to the test
    context, see {ref}`SpecTypeTestContextMember`.

  description
  : The attribute value shall be an optional string. It shall be the test
    support method description.

- There may be no value (null).

This type is used by the following types:

- {ref}`SpecTypeActionRequirementItemType`

- {ref}`SpecTypeRuntimeMeasurementTestItemType`

- {ref}`SpecTypeRuntimePerformanceRequirementItemType`

- {ref}`SpecTypeTestCaseItemType`

(SpecTypeUID)=

### UID

The value shall be a string. It shall be a valid absolute or relative item UID.

This type is used by the following types:

- {ref}`SpecTypeLink`

(SpecTypeUnitTestLinkRole)=

### Unit Test Link Role

This type refines the {ref}`SpecTypeLink` through the `role` attribute if the
value is `unit-test`. It defines the unit test role of links. For unit tests
the link target should be the {ref}`SpecTypeInterfaceDomainItemType` containing
the software unit. All explicit attributes shall be specified. The explicit
attributes for this type are:

name
: The attribute value shall be a string. It shall be the name of the tested
  software unit.
