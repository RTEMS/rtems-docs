.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

Project Sets
============

The RTEMS Source Builder supports project configurations. Project
configurations can be public or private and can be contained in the RTEMS
Source Builder project if suitable, other projects they use the RTEMS Source
Builder or privately on your local file system.

The configuration file loader searches the macro ``_configdir`` and by default
this is set to ``%{_topdir}/config:%{_sbdir}/config`` where ``_topdir`` is the
your current working direct, in other words the directory you invoke the RTEMS
Source Builder command in, and ``_sbdir`` is the directory where the RTEMS
Source Builder command resides. Therefore the ``config`` directory under each
of these is searched so all you need to do is create a ``config`` in your
project and add your configuration files. They do not need to be under the
RTEMS Source Builder source tree. Public projects are included in the main
RTEMS Source Builder such as RTEMS.

You can also add your own ``patches`` directory next to your ``config``
directory as the ``%patch`` command searches the ``_patchdir`` macro variable
and it is by default set to ``%{_topdir}/patches:%{_sbdir}/patches``.

The ``source-builder/config`` directory provides generic scripts for building
various tools. You can specialise these in your private configurations to make
use of them. If you add new generic configurations please contribute them back
to the project

Build sets can be controlled via the command line to enable
(``--with-<feature>``) and disable (``--without-<feature>``) various features.
There is no definitive list of build options that can be listed because they
are implemented with the configuration scripts.  The best way to find what is
available is to grep the configuration files for ``with`` and ``without``.

Bare Metal
----------

The RSB contains a 'bare' configuration tree and you can use this to add
packages you use on the hosts. For example 'qemu' is supported on a range of
hosts. RTEMS tools live in the ``rtems/config`` directory tree. RTEMS packages
include tools for use on your host computer as well as packages you can build
and run on RTEMS.

The **bare metal** support for GNU Tool chains. An example is the
``lang/gcc491`` build set. You need to provide a target via the command line
``--target`` option and this is in the standard 2 or 3 tuple form. For example
for an ARM compiler you would use ``arm-eabi`` or ``arm-eabihf`, and for SPARC
you would use `sparc-elf`::

    $ cd rtems-source-builder/bare
    $ ../source-builder/sb-set-builder --log=log_arm_eabihf \
        --prefix=$HOME/development/bare --target=arm-eabihf lang/gcc491
    RTEMS Source Builder - Set Builder, v0.3.0
    Build Set: lang/gcc491
    config: devel/expat-2.1.0-1.cfg
    package: expat-2.1.0-x86_64-apple-darwin13.2.0-1
    building: expat-2.1.0-x86_64-apple-darwin13.2.0-1
    config: devel/binutils-2.24-1.cfg
    package: arm-eabihf-binutils-2.24-1
    building: arm-eabihf-binutils-2.24-1
    config: devel/gcc-4.9.1-newlib-2.1.0-1.cfg
    package: arm-eabihf-gcc-4.9.1-newlib-2.1.0-1
    building: arm-eabihf-gcc-4.9.1-newlib-2.1.0-1
    config: devel/gdb-7.7-1.cfg
    package: arm-eabihf-gdb-7.7-1
    building: arm-eabihf-gdb-7.7-1
    installing: expat-2.1.0-x86_64-apple-darwin13.2.0-1 -> /Users/chris/development/bare
    installing: arm-eabihf-binutils-2.24-1 -> /Users/chris/development/bare
    installing: arm-eabihf-gcc-4.9.1-newlib-2.1.0-1 -> /Users/chris/development/bare
    installing: arm-eabihf-gdb-7.7-1 -> /Users/chris/development/bare
    cleaning: expat-2.1.0-x86_64-apple-darwin13.2.0-1
    cleaning: arm-eabihf-binutils-2.24-1
    cleaning: arm-eabihf-gcc-4.9.1-newlib-2.1.0-1
    cleaning: arm-eabihf-gdb-7.7-1

RTEMS
-----

The RTEMS Configurations found in the ``rtems`` directory. The configurations
are grouped by RTEMS version. In RTEMS the tools are specific to a specific
version because of variations between Newlib and RTEMS. Restructuring in RTEMS
and Newlib sometimes moves *libc* functionality between these two parts and
this makes existing tools incompatible with RTEMS.

RTEMS allows architectures to have different tool versions and patches. The
large number of architectures RTEMS supports can make it difficult to get a
common stable version of all the packages. An architecture may require a recent
GCC because an existing bug has been fixed, however the more recent version may
have a bug in other architecture. Architecture specific patches should be
limited to the architecture it relates to. The patch may fix a problem on the
effect architecture however it could introduce a problem in another
architecture. Limit exposure limits any possible crosstalk between
architectures.

If you are building a released version of RTEMS the release RTEMS tar file will
be downloaded and built as part of the build process. If you are building a
tool set for use with the development branch of RTEMS, the development branch
will be cloned directly from the RTEMS GIT repository and built.

When building RTEMS within the RTEMS Source Builder it needs a suitable working
``autoconf`` and ``automake``. These packages need to built and installed in their
prefix in order for them to work. The RTEMS Source Builder installs all
packages only after they have been built so if you host does not have a
recent enough version of ``autoconf`` and ``automake`` you first need to build them
and install them then build your tool set. The commands are::

    $ ../source-builder/sb-set-builder --log=l-4.11-at.txt \
       --prefix=$HOME/development/rtems/4.11 4.11/rtems-autotools
    $ export PATH=~/development/rtems/4.11/bin:$PATH    <1>
    $ ../source-builder/sb-set-builder --log=l-4.11-sparc.txt \
       --prefix=$HOME/development/rtems/4.11 4.11/rtems-sparc

.. topic:: Items:

  1. Setting the path.

If this is your first time building the tools and RTEMS it pays to add the
``--dry-run`` option. This will run through all the configuration files and if
any checks fail you will see this quickly rather than waiting for until the
build fails a check.

To build snapshots for testing purposes you use the available macro maps
passing them on the command line using the ``--macros`` option. For RTEMS these
are held in ``config/snapshots`` directory. The following builds *newlib* from
CVS::

    $ ../source-builder/sb-set-builder --log=l-4.11-sparc.txt \
       --prefix=$HOME/development/rtems/4.11 \
       --macros=snapshots/newlib-head.mc \
       4.11/rtems-sparc

and the following uses the version control heads for ``binutils``, ``gcc``,
``newlib``, ``gdb`` and *RTEMS*::

    $ ../source-builder/sb-set-builder --log=l-heads-sparc.txt \
       --prefix=$HOME/development/rtems/4.11-head \
       --macros=snapshots/binutils-gcc-newlib-gdb-head.mc \
       4.11/rtems-sparc

Following features can be enabled/disabled via the command line for the RTEMS
build sets:

``--without-rtems``
  Do not build RTEMS when building an RTEMS build set.

``--without-cxx``
  Do not build a C++ compiler.

``--with-ada``
  Attempt to build an Ada compiler.  You need a native GNAT installed.

``--with-fortran``
  Attempt to build a Fortran compiler.

``--with-objc``
  Attempt to build a C++ compiler.

Patches
-------

Packages being built by the RSB need patches from time to time and the RSB
supports patching upstream packages. The patches are held in a seperate
directory called ``patches`` relative to the configuration directory you are
building. For example ``%{_topdir}/patches:%{_sbdir}/patches``. Patches are
declared in the configuration files in a similar manner to the package's source
so please refer to the ``%source`` documentation. Patches, like the source, are
to be made publically available for configurations that live in the RSB package
and are downloaded on demand.

If a package has a patch management tool it is recommended you reference the
package's patch management tools directly. If the RSB does not support the
specific patch manage tool please contact the mailing list to see if support
can be added.

Patches for packages developed by the RTEMS project can be placed in the RTEMS
Tools Git repository. The ``tools`` directory in the repository has various
places a patch can live. The tree is broken down in RTEMS releases and then
tools within that release. If the package is not specific to any release the
patch can be added closer to the top under the package's name. Patches to fix
specific tool related issues for a specific architecture should be grouped
under the specific architecture and only applied when building that
architecture avoiding a patch breaking an uneffected architecture.

Patches in the RTEMS Tools repository need to be submitted to the upstream
project. It should not be a clearing house for patches that will not be
accepted upstream.

Patches are added to a component's name and in the ``%prep:`` section the
patches can be set up, meaning they are applied to source. The patches
are applied in the order they are added. If there is a dependency make
sure you order the patches correctly when you add them. You can add any
number of patches and the RSB will handle them efficently.

Patches can have options. These are added before the patch URL. If no options
are provided the patch's setup default options are used.

Patches can be declared in build set up files.

This examples shows how to declare a patch for gdb in the ``lm32`` architecture::

    %patch add <1> gdb <2> %{rtems_gdb_patches}/lm32/gdb-sim-lm32uart.diff <3>

.. topic:: Items:

  1. The patch's ``add`` command.

  2. The group of patches this patch belongs too.

  3. The patch's URL. It is downloaded from here.

Patches require a checksum to avoid a warning. The ``%hash`` directive can be
used to add a checksum for a patch that is used to verify the patch::

    %hash md5 <1> gdb-sim-lm32uart.diff <2> 77d070878112783292461bd6e7db17fb <3>

.. topic:: Items:

  1. The type of checksum, in the case an MD5 hash.

  2. The patch file the checksum is for.

  3. The MD5 hash.

The patches are applied when a patch ``setup`` command is issued in the
``%prep:`` section. All patches in the group are applied. To apply the GDB
patch above use::

    %patch setup <1> gdb <2> -p1 <3>

.. topic:: Items:

  1. The patch's ``setup`` command.

  2. The group of patches to apply.

  3. The patch group's default options. If no option is given with the patch
     these options are used.

Architecture specific patches live in the architecture build set file isolating
the patch to that specific architecture. If a patch is common to a tool it
resides in the RTEMS tools configuration file. Do not place patches for tools
in the ``source-builder/config`` template configuration files.

To test a patch simply copy it to your local ``patches`` directory. The RSB
will see the patch is present and will not attempt to download it. Once you are
happy with the patch submit it to the project and a core developer will review
it and add it to the RTEMS Tools git repository.  For example, to test a local
patch for newlib, add the following two lines to the .cfg file in
``rtems/config/tools/`` that is included by the bset you use:

.. code-block:: auto

    %patch add newlib file://0001-this-is-a-newlib-patch.patch   <1>
    %hash md5 0001-this-is-a-newlib-patch.diff 77d070878112783292461bd6e7db17fb <2>

.. topic:: Items:

  1. The diff file prepended with ``file://`` to tell RSB this is a local file.

  2. The output from md5sum on the diff file.
