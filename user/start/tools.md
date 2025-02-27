% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 embedded brains GmbH & Co. KG

% Copyright (C) 2019 Sebastian Huber

% Copyright (C) 2016, 2020 Chris Johns

% Copyright (C) 2020 Utkarsh Rai

(QuickStartTools)=

# Install the Tool Suite

You have chosen an installation prefix, the BSP to build, the tool's
architecure and prepared the source for the RSB in the previous sections. We
have chosen {file}`$HOME/quick-start/rtems/@rtems-ver-major@` as the installation prefix, the
`erc32` BSP and the SPARC architecture name of `sparc-rtems@rtems-ver-major@`, and unpacked
the RSB source in {file}`$HOME/quick-start/src`.

The tool suite for RTEMS and the RTEMS sources are tightly coupled. For
example, do not use a RTEMS version @rtems-ver-major@ tool suite with RTEMS version 4.11 or 5
sources and vice versa.

If you are unsure how to specify the build set for the architecture you wish to
build, just ask the tool:

```none
$ ../source-builder/sb-set-builder --list-bsets
```

Build and install the tool suite:

```none
cd $HOME/quick-start/src/rsb/rtems
../source-builder/sb-set-builder --prefix=$HOME/quick-start/rtems/@rtems-ver-major@ @rtems-ver-major@/rtems-sparc
```

This command should output something like this (omitted lines are denoted by
...). The build host appears as part of the name of the package being
built. The name you see may vary depending on the host you are using:

```none
RTEMS Source Builder - Set Builder, @rtems-ver-major@ (5e449fb5c2cb)
Build Set: @rtems-ver-major@/rtems-sparc
...
config: tools/rtems-binutils-2.36.cfg
package: sparc-rtems@rtems-ver-major@-binutils-fbb9a7e-x86_64-linux-gnu-1
building: sparc-rtems@rtems-ver-major@-binutils-fbb9a7e-x86_64-linux-gnu-1
sizes: sparc-rtems@rtems-ver-major@-binutils-fbb9a7e-x86_64-linux-gnu-1: 716.015MB (installed: 163.538MB)
cleaning: sparc-rtems@rtems-ver-major@-binutils-fbb9a7e-x86_64-linux-gnu-1
reporting: tools/rtems-binutils-2.36.cfg -> sparc-rtems@rtems-ver-major@-binutils-fbb9a7e-x86_64-linux-gnu-1.txt
reporting: tools/rtems-binutils-2.36.cfg -> sparc-rtems@rtems-ver-major@-binutils-fbb9a7e-x86_64-linux-gnu-1.xml
config: tools/rtems-gcc-10-newlib-head.cfg
package: sparc-rtems@rtems-ver-major@-gcc-6051af8-newlib-d10d0d9-x86_64-linux-gnu-1
building: sparc-rtems@rtems-ver-major@-gcc-6051af8-newlib-d10d0d9-x86_64-linux-gnu-1
....
Build Sizes: usage: 9.607GB total: 2.244GB (sources: 264.186MB, patches: 43.468KB, installed 1.986GB)
installing: @rtems-ver-major@/rtems-sparc -> $HOME/quick-start/rtems/@rtems-ver-major@
clean staging: @rtems-ver-major@/rtems-sparc
Staging Size: 5.292MB
Build Set: Time 1:01:48.019157
```

Once the build has successfully completed you can check if the cross C compiler
works with the following command:

```none
$HOME/quick-start/rtems/@rtems-ver-major@/bin/sparc-rtems@rtems-ver-major@-gcc --version
```

This command should output something like below. The version informtion helps
you to identify the exact sources used to build the cross compiler of your
RTEMS tool suite. In the output you see the version of RTEMS or the hash from
the RSB repository if you are building using a Git repository clone. The Newlib
hash is the version of Newlib in the RTEMS's github
[sourceware-mirror-newlib-cygwin](https://github.com/RTEMS/sourceware-mirror-newlib-cygwin) repository. The
`sources` and `patches` directories created by the RSB contain all the
source code used.

```none
sparc-rtems@rtems-ver-major@-gcc (GCC) 10.2.1 20210309 (RTEMS @rtems-ver-major@, RSB 5e449fb5c2cb6812a238f9f9764fd339cbbf05c2, Newlib d10d0d9)
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Add `--verbose` to the GCC command for the verbose version details.

## Creating a Tool Archive

Since the RTEMS Project does not provide binary tool distributions, some users
may need to create their own relocatable toolchains. This need can be due to
Canadian Cross-Compilation (CxC or three-way), configuration control, or
because a user wants to synchronize development environments across multiple
workstations or to share tools among multiple developers. To support such
needs, the RSB can create tar files of the built package set by adding
`--bset-tar-file` to the `sb-set-builder` command line. These tar files can
then be relocated or adapted as needed to suit the user's needs.

## Need for RTEMS-Specific Cross-Compiler

New users are often confused as to why they cannot use their distribution's
cross-compiler for their target on RTEMS, e.g., the riscv64-linux-gnu or the
arm-none-eabi-gcc. Below mentioned are some of the reasons for using
the RTEMS cross-compiler.

> Correct configuration of Newlib
> : Newlib is a C standard library implementation intended for use on embedded
>   systems. Most of the POSIX and libc support for RTEMS is derived from
>   Newlib. The RTEMS cross-compiler configures Newlib correctly for RTEMS.
>
> Threading in GCC support libraries
> : Several threading packages in GCC such as Go threads (libgo), OpenMP
>   (libgomp), and OpenACC need to be customized according to RTEMS. This is
>   done by the RTEMS specific cross-compiler.
>
> Provide preprocessor define \_\_rtems\_\_
> : The `__rtems__` preprocessor define is used to provide conditional code
>   compilation in source files that are shared with other projects e.g. in
>   Newlib or imported code from FreeBSD.
>
> Multilib variants to match the BSP
> : RTEMS configures GCC to create separate runtime libraries for each
>   supported instruction set, floating point unit, vector unit, word size
>   (e.g. 32-bit and 64-bit), endianness, ABI, processor errata workarounds,
>   and so on in the architecture. These libraries are termed as {ref}`Multilib <TargetArchitectures>` variants. Multilib variants to match the BSP are set
>   by selecting a specific set of machine options using the RTEMS
>   cross-compiler.

(ProjectSandboxing)=

## Project Sandboxing

Project specific sandboxes let you have a number of projects running in
parallel with each project in its own sandbox. You simply have a
{ref:term}`prefix` per project and under that prefix you create a simple yet
repeatable structure.

As an example lets say I have a large disk mounted under {file}`/bd` for *Big
Disk*. As `root` create a directory called `projects` and give the
directory suitable permissions to be writable by you as a user.

Lets create a project sandbox for my *Box Sorter* project. First create a
project directory called {file}`/bd/projects/box-sorter`. Under this create
{file}`rtems` and under that create {file}`rtems-@rtems-ver-majminrev@`. Under
this path you can follow the {ref}`released-version` procedure to build a tool
set using the prefix of
{file}`/bd/projects/box-sorter/rtems/@rtems-ver-majminrev@`. You are free to
create your project specific directories under
{file}`/bd/projects/box-sorter`. The top level directories would be:

{file}`/bd/projects`
: Project specific development trees.

{file}`/bd/projects/box-sorter`
: Box Sorter project sandbox.

{file}`/bd/projects/box-sorter/rtems/@rtems-ver-majminrev@`
: Project prefix for RTEMS @rtems-ver-majminrev@ compiler, debuggers, tools and
  installed Board Support Package (BSP).

A variation is to use the `--without-rtems` option with the RSB to not build
the BSPs when building the tools and to build RTEMS specifically for each
project. This lets you have a production tools installed at a top level on your
disk and each project can have a specific and possibly customised version of
RTEMS. The top level directories would be:

{file}`/bd/rtems`
: The top path to production tools.

{file}`/bd/rtems/@rtems-ver-majminrev@`
: Production prefix for RTEMS @rtems-ver-majminrev@ compiler, debuggers and
  tools.

{file}`/bd/projects`
: Project specific development trees.

{file}`/bd/projects/box-sorter`
: Box Sorter project sandbox.

{file}`/bd/projects/box-sorter/rtems`
: Box Sorter project's custom RTEMS kernel source and installed BSP.

A further varation if there is an RTEMS kernel you want to share between
projects is it to move this to a top level and share. In this case you will end
up with:

{file}`/bd/rtems`
: The top path to production tools and kernels.

{file}`/bd/rtems/@rtems-ver-majminrev@`
: Production prefix for RTEMS @rtems-ver-majminrev@.

{file}`/bd/rtems/@rtems-ver-majminrev@/tools`
: Production prefix for RTEMS @rtems-ver-majminrev@ compiler, debuggers and
  tools.

{file}`/bd/rtems/@rtems-ver-majminrev@/bsps`
: Production prefix for RTEMS @rtems-ver-majminrev@ Board Support Packages
  (BSPs).

{file}`/bd/projects`
: Project specific development trees.

{file}`/bd/projects/box-sorter`
: Box Sorter project sandbox.

Finally you can have a single set of *production* tools and RTEMS BSPs on the
disk under {file}`/bd/rtems` you can share between your projects. The top level
directories would be:

{file}`/bd/rtems`
: The top path to production tools and kernels.

{file}`/bd/rtems/@rtems-ver-majminrev@`
: Production prefix for RTEMS @rtems-ver-majminrev@ compiler, debuggers, tools
  and Board Support Packages (BSPs).

{file}`/bd/projects`
: Project specific development trees.

{file}`/bd/projects/box-sorter`
: Box Sorter project sandbox.

The project sandoxing approach allows you move a specific production part into
the project's sandbox to allow you to customise it. This is useful if you are
testing new releases. The typical dependency is the order listed above. You can
test new RTEMS kernels with production tools but new tools will require you
build the kernel with them. Release notes with each release will let know
what you need to update.

If the machine is a central project development machine simply replace
{file}`projects` with {file}`users` and give each user a personal directory.
