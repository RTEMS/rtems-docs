% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 Contemporary Software

% Copyright (C) 2020 Chris Johns

(QuickStartBSPPackages)=

# Build an RSB Package

This section describes how to build an RTEMS package using the RSB. Before we
start to build a package with the RSB you need to complete these steps:

- {ref}`QuickStartPrefixes`
- {ref}`QuickStartSources`.

Return to here once you have completed these steps.

You have chosen an installation prefix, the BSP to build, the tool's
architecure and prepared the source for the RSB in the previous sections. We
have chosen {file}`$HOME/quick-start/rtems/5` as the installation prefix, the
`erc32` BSP and the SPARC architecture name of `sparc-rtems5`, and unpacked
the RSB source in {file}`$HOME/quick-start/src`.

You are now able to build {ref}`BSP Packages` or 3rd party libraries of code if you
have built a BSP.

## RTEMS Packages

RTEMS Packages are source packages the RSB build to run on RTEMS. An installed
package is a set of header files and libraries. Your application include the
packages header files to make calls to the package's code and include the
libraries in it's linker options.

RTEMS packages can be part of the RTEMS Project or they can be external
packages from 3rd parties. RTEMS Project packages include the BSPs and BSD
Library package called `libbsd`. External 3rd party packages include
networking such has `curl` or `libcurl` to graphics libraries.

Packages can depend on other packages and need to be build in the corret
order. For example the FreeBSD Library package depends on the BSP package and a
3rd party library such as `curl` depends on the FreeBSD Library package. We
call this layering a vertical software stack.

RTEMS applications are cross-compiled and this adds complexity when building
libraries of code. RTEMS Packages build with the RSB manage this complexity for
you.

Package are libraries so they will not be linked into your application until
you make calls to the the code and add the library to your application's linker
command line.

% QuickStartRSBPackage_BSPStack:

## BSP Stack Build

A BSP stack build is a single command that uses the RSB to build a BSP software
stack of:

- Tool suite
- BSP
- Packages

The packages built depend on the BSP and the default will build all packages for a
BSP.

```none
cd $HOME/quick-start/src/rsb/rtems
../source-builder/sb-set-builder --prefix=$HOME/quick-start/rtems/5 \
    --with-rtems-tests=yes bsps/erc32
```

This command should output something like this:

```none
RTEMS Source Builder - Set Builder, 5.1.0
Build Set: bsps/erc32
Build Set: 5/rtems-sparc.bset
Build Set: 5/rtems-autotools.bset
Build Set: 5/rtems-autotools-internal.bset
config: tools/rtems-autoconf-2.69-1.cfg
package: autoconf-2.69-x86_64-freebsd12.1-1
building: autoconf-2.69-x86_64-freebsd12.1-1
sizes: autoconf-2.69-x86_64-freebsd12.1-1: 7.505MB (installed: 0.000B)
...
building: protobuf-2.6.1-sparc-rtems5-1
sizes: protobuf-2.6.1-sparc-rtems5-1: 228.079MB (installed: 84.408MB)
cleaning: protobuf-2.6.1-sparc-rtems5-1
reporting: net/protobuf-2.6.1-1.cfg -> protobuf-2.6.1-sparc-rtems5-1.txt
reporting: net/protobuf-2.6.1-1.cfg -> protobuf-2.6.1-sparc-rtems5-1.xml
staging: protobuf-2.6.1-sparc-rtems5-1 -> $HOME/quick-start/src/rsb/rtems/build/tmp/sb-500-staging
cleaning: protobuf-2.6.1-sparc-rtems5-1
Build Set: Time 0:00:23.564992
Build Set: Time 0:02:27.380299
installing: bsps/erc32 -> $HOME/quick-start/rtems/
clean staging: bsps/erc32
Staging Size: 1.372GB
Build Set: Time 0:24:17.83979
```

The RSB BSP build can be customised with following RSB command line options:

`--with-rtems-tests`:
: Build the test suite. If `yes` is provided all tests in the testsuite are
  build. If `no` is provided no tests are built and if `samples` is
  provided only the sample executables are built, e.g.
  `--with-rtems-tests=yes`.

`--with-rtems-smp`:
: Build with SMP support. The BSP has to have SMP support or this option will
  fail with an error.

`--with-rtems-bspopts`:
: Build the BSP with BSP specific options. This is an advanced option. Please
  refer to the BSP specific details in the {ref}`Board Support Packages (BSPs)` of this manual or the BSP source code in the RTEMS source
  directory. To supply a list of options quote then list with `"`, e.g.
  `--with-rtems-bspopts="BSP_POWER_DOWN_AT_FATAL_HALT=1"`

Only a limited number of BSPs have RSB support to build as a software stack. To
see which BSPs are supported run this command:

```none
cd $HOME/quick-start/src/rsb/rtems
../source-builder/sb-set-builder --list-bsets | grep bsps
```

## Package Build

Packages are built using RSB build sets. A build set is a set of builds need to
build a packages. The build steps can be dependencies a package has or it could
be a stack of software to provide specific functionality, i.e. a build set can
be a list of build sets. To view the avaliable build sets run this command:

```none
cd $HOME/quick-start/src/rsb/rtems
../source-builder/sb-set-builder --list-bsets
```

RTEMS package naming is based on the naming FreeBSD uses in its ports
collection.

This Quick Start Guide will build the BSD Library or {file}`5/rtems-libbsd`.

An RTEMS package is hosted on RTEMS so the tool suite name needs to be supplied
using the `--host` option, e.g. `--host=sparc-rtem5`. The BSP needs to be
provided using the `--with-rtems-bsp` option,
e.g. `--with-rtems-bsp=erc32`. The commands to build `libbsd` for the
`erc32` BSP are:

```none
cd $HOME/quick-start/src/rsb/rtems
../source-builder/sb-set-builder --prefix=$HOME/quick-start/rtems/5 \
  --host=sparc-rtems5 --with-rtems-bsp=erc32 5/rtems-libbsd
```

This command should output something like this:

```none
RTEMS Source Builder - Set Builder, 5.1.0
Build Set: 5/rtems-libbsd
config: tools/rtems-libbsd-5.cfg
package: rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1
building: rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1
sizes: rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1: 1.199GB (installed: 116.541MB)
cleaning: rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1
reporting: tools/rtems-libbsd-5.cfg -> rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1.txt
reporting: tools/rtems-libbsd-5.cfg -> rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1.xml
installing: rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1 -> $HOME/quick-start/rtems/5
cleaning: rtems-libbsd-v3cc039cdac77272a8e16b33ae5a53ccd89edf989-sparc-rtems5-1
Build Set: Time 0:00:51.898231
```

```{note}
Not all packages will build or run with all BSPs. Please ask on the
{r:list}`users` if you have any issues.
```
