% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 embedded brains GmbH & Co. KG

% Copyright (C) 2019 Sebastian Huber

% Copyright (C) 2020 Chris Johns

(QuickStartSources)=

# Obtain the Sources

You have considered and chosen a suitable installation prefix in the previous
section. For example, if you are building RTEMS with version
`@rtems-ver-major@` tools we have chosen
{file}`$HOME/quick-start/rtems/@rtems-ver-major@` as the installation prefix.
We will show how to use a released version of RTEMS and then as an alternative
we will show you using the {ref}`RSB Git repository <QuickStartSources_Git>`.
Consider using a Git clone if you wish to make contributions to the RTEMS
Project.

You need the RTEMS Source Builder (RSB) to work with RTEMS. You should use the
same version of the RSB as you plan to use for RTEMS, for example
`@rtems-ver-major@` for the development head of RTEMS, or a released version
of the RSB matching the released version of RTEMS.
A released version of the RSB downloads all source code from the RTEMS servers.
Each release archives all the referenced source providing long term stability
as changes in upstream projects do not effect a release's build.

You will need approximately 1.5G bytes of disk space to build the tools, RTEMS
kernel, network stack and 3rd party packages for the ERC32 BSP.

(QuickStartSources_Released)=

## Releases

You can download the source archives for a released RTEMS version from RTEMS'
servers. Releases can be viewed at <https://ftp.rtems.org/pub/rtems/releases> with
the releases listed as a series under a release's major number. For RTEMS 5.1
the release series is [5](https://ftp.rtems.org/pub/rtems/releases/5) and the
release path is <https://ftp.rtems.org/pub/rtems/releases/5/5.1>.

To work with the archives of a released RTEMS version, simply replace the
version major number `5` and minor number `1` used throughout this section with
the version number you selected, e.g., `sparc-rtems4.11`, `sparc-rtems6`, and
so on. The specific instructions for working with released versions of RTEMS
are available in the released documents associated with those versions.
However, the procedures should generally work fine replacing `@rtems-ver-major@`
with the release version major number you are using.

Download and unpack using the `curl` and `tar` command with these commands:

```none
mkdir -p $HOME/quick-start/src
cd $HOME/quick-start/src
curl https://ftp.rtems.org/pub/rtems/releases/5/5.1/sources/rtems-source-builder-5.1.tar.xz | tar xJf -
```

If `curl` does not work consider using `wget` or a browser.

The RSB is unpacked under the path `rtems-source-builder-5.1`. We rename this
to `rsb` so that the subsequent directions are consistent regardless of what
version is being used. This has the added benefit of using shorter paths during
the tool suite build. To do this run these commands:

```none
cd $HOME/quick-start/src
mv rtems-source-builder-5.1 rsb
```

(QuickStartSources_Released_RTEMS)=

If you wish to build the RTEMS kernel from source obtain the RTEMS kernel
sources:

```none
cd $HOME/quick-start/src
curl https://ftp.rtems.org/pub/rtems/releases/5/5.1/sources/rtems-5.1.tar.xz | tar xJf -
```

(QuickStartSources_Git)=

## Git

Alternatively, clone the Git repositories into {file}`$HOME/quick-start/src`.

A Git repository clone gives you some flexibility with the added complexity of
needing to use a Git tag or branch to build a released version. With Git you can
switch between branches to try out different RTEMS versions and you have access
to the RTEMS source history. The RTEMS Project welcomes contributions. The Git
repositories enable you to easily create patches and track local changes.

You can clone the Git repository to get all versions of RTEMS including the
development head. Release branches in Git are kept stable however they may
differ from a release's source archive.

```none
mkdir -p $HOME/quick-start/src
cd $HOME/quick-start/src
git clone https://gitlab.rtems.org/rtems/tools/rtems-source-builder.git rsb
git clone https://gitlab.rtems.org/rtems/rtos/rtems.git
```

The {file}`rsb` repository clone contains the {ref}`RTEMS Source Builder (RSB) <RSB>`. We clone it into {file}`rsb` to get a consistent (and shorter) path for
the subsequent instructions. This renaming is optional.
The {file}`rtems` repository clone contains the RTEMS sources.
These two repositories are enough to get started. There are [more repositories](https://gitlab.rtems.org/explore/projects) available.

```{warning}
The development version is not for use in production and it can break from
time to time.
```

## Offline Download

If you have limited Internet access you can download the source before you
start building. If you are permanently connected to the Internet you do not
need to do this and the sources will be automatically download on demand when
needed.

Once the sources have been downloaded you could disconnect your host computer
from the Internet. It is no longer required to work with RTEMS. To download
the sources to build the ERC 32 BSP before building run the following commands:

```none
cd $HOME/quick-start/src/rsb/rtems
../source-builder/sb-set-builder --source-only-download @rtems-ver-major@/rtems-sparc
```

This command should output something like this (omitted lines are denoted by
`...`):

```none
RTEMS Source Builder - Set Builder, @rtems-ver-major@ (5e449fb5c2cb)
Build Set: @rtems-ver-major@/rtems-sparc
Build Set: @rtems-ver-major@/rtems-autotools.bset
Build Set: @rtems-ver-major@/rtems-autotools-internal.bset
...
download: https://gitlab.rtems.org/rtems-tools/snapshot/rtems-tools-90342feb4dd63d188ce945adfb0a769...<see log> -> sources/rtems-tools-90342feb4dd63d188ce945adfb0a7694a42a65cd.tar.bz2
...
Build Sizes: usage: 0.000B total: 264.228MB (sources: 264.186MB, patches: 43.468KB, installed 0.000B)
Build Set: Time 0:06:34.357125
```

If you encounter errors, check your internet connection, firewall settings,
virus scanners and the availability of the download servers.
