.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

Project Sets
------------

The RTEMS Source Builder supports project configurations. Project
configurations can be public or private and can be contained in the RTEMS
Source Builder project if suitable.

The configuration file loader searches the macro ``_configdir`` and by default
this is set to ``%{_topdir}/config:%{_sbdir}/config`` where ``_topdir`` is your
current working directory, or the directory you invoke the RTEMS Source Builder
command in. The macro ``_sbdir`` is the directory where the RTEMS Source
Builder command resides. Therefore the ``config`` directory under each of these
is searched so all you need to do is create a ``config`` in your project and
add your configuration files. They do not need to be under the RTEMS Source
Builder source tree. Public projects are included in the main RTEMS Source
Builder such as RTEMS.

You can add your own ``patches`` directory next to your ``config`` directory as
the ``%patch`` command searches the ``_patchdir`` macro variable and it is by
default set to ``%{_topdir}/patches:%{_sbdir}/patches``.

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
^^^^^^^^^^

The RSB contains a ``bare`` configuration tree and you can use this to add
packages you use on the hosts. For example 'qemu' is supported on a range of
hosts. RTEMS tools live in the ``rtems/config`` directory tree. RTEMS packages
include tools for use on your host computer as well as packages you can build
and run on RTEMS.

The **bare metal** support for GNU Tool chains. An example is the
``lang/gcc491`` build set. You need to provide a target via the command line
``--target`` option and this is in the standard 2 or 3 tuple form. For example
for an ARM compiler you would use ``arm-eabi`` or ``arm-eabihf``, and for SPARC
you would use ``sparc-elf``:

.. code-block:: none

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
^^^^^

The RTEMS Configurations are found in the ``rtems`` directory. The
configurations are grouped by RTEMS version and a release normally only
contains the configurations for that release.. In RTEMS the tools are specific
to a specific version because of variations between Newlib and
RTEMS. Restructuring in RTEMS and Newlib sometimes moves *libc* functionality
between these two parts and this makes existing tools incompatible with RTEMS.

RTEMS allows architectures to have different tool versions and patches. The
large number of architectures RTEMS supports can make it difficult to get a
common stable version of all the packages. An architecture may require a recent
GCC because an existing bug has been fixed, however the more recent version may
have a bug in other architecture. Architecture specific patches should only be
appliaed when build the related architecture. A patch may fix a problem on one
architecture however it could introduce a problem in another
architecture. Limiting exposure limits any possible crosstalk between
architectures.

If you have a configuation issue try adding the ``--dry-run`` option. This will
run through all the configuration files and if any checks fail you will see
this quickly rather than waiting for until the build fails a check.

Following features can be enabled/disabled via the command line for the RTEMS
build sets:

``--without-cxx``
  Do not build a C++ compiler.

``--with-ada``
  Attempt to build an Ada compiler.  You need a native GNAT installed.

``--with-fortran``
  Attempt to build a Fortran compiler.

``--with-objc``
  Attempt to build a C++ compiler.

``--with-newlib-tls`` or ``--without-newlib-tls``
  Enable or disable the ``--enable-newlib-reent-thread-local`` Newlib
  configuration option.  This option is enabled by default on the aarch64, arm,
  nios2, powerpc, riscv, and sparc targets.  If this option is enabled, then
  each member of the Newlib struct _reent is replaced by a dedicated
  thread-local object.  The thread-local objects are defined in translation
  units which use the corresponding object so that only objects used by the
  application are linked in.

The RSB provides build sets for some BSPs. These build sets will build:

- Compiler, linker, debugger and RTEMS Tools.

- RTEMS Kernel for the BSP

- Optionally LibBSD if supported by the BSP.

- Third party packages if supported by the BSP.

Patches
^^^^^^^

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

Referenced patches should be placed in a location that is easy to access and
download with a stable URL. We recommend attaching a patch to an RTEMS ticket
in it's bug reporting system or posting to a mailing list with online archives.

RTEMS's former practice of placing patches in the RTEMS Tools Git repository
has been stopped.

Patches are added to a component's name and in the ``%prep:`` section the
patches can be set up, meaning they are applied to source. The patches are
applied in the order they are added. If there is a dependency make sure you
order the patches correctly when you add them. You can add any number of
patches and the RSB will handle them efficiently.

Patches can have options. These are added before the patch URL. If no options
are provided the patch's setup default options are used.

Patches can be declared in build set up files.

This example shows how to declare a patch for gdb in the ``sparc`` architecture:

.. code-block:: spec

    %patch add <1> gdb <2> %{rtems_gdb_patches}/gdb-8.2.1-disable-sis.patch <3>

.. topic:: Items:

  1. The patch's ``add`` command.

  2. The group of patches this patch belongs too.

  3. The patch's URL. It is downloaded from here.

Patches require a checksum to avoid a warning. The ``%hash`` directive can be
used to add a checksum for a patch that is used to verify the patch:

.. code-block:: spec

    %hash sha512 <1> gdb-8.2.1-disable-sis.patch <2> 295f91 ... 051c6960 <3>

.. topic:: Items:

  1. The type of checksum, in the case an SHA512 hash.

  2. The patch file the checksum is for.

  3. The SHA512 hash.

The patches are applied when a patch ``setup`` command is issued in the
``%prep:`` section. All patches in the group are applied. To apply the GDB
patch above use:

.. code-block:: spec

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
it and add it to the RTEMS Tools git repository.

Testing a Newlib Patch
~~~~~~~~~~~~~~~~~~~~~~

To test a local patch for newlib, you need to add the following
two lines to the ``.cfg`` file in ``rsb/rtems/config/tools/`` that is included
by the bset you use:

.. topic:: Steps:

  1. Create patches for the changes you want to test. (Note: For RSB, before
     creating Newlib patch, you must run ``autoreconf -fvi`` in the required
     directory after you make changes to the code. This is not required when
     you create patch to send to ``newlib-devel``. But if you want RSB to
     address your changes, your patch should also include regenerated files.)

  2. Calculate ``sha512`` of your patch.

  3. Place the patches in ``rsb/rtems/patches`` directory.

  4. Open the ``.bset`` file used by your BSP in ``rsb/rtems/config``.
     For example, for ``rtems5``, ``SPARC``, the file will be
     ``rsb/rtems/config/5/rtems-sparc.bset``.

  5. Inside it you will find the name of ``.cfg`` file for Newlib, used by
     your BSP.
     For example, I found ``tools/rtems-gcc-7.4.0-newlib-1d35a003f``.

  6. Edit your ``.cfg`` file. In my case it will be,
     ``rsb/rtems/config/tools/rtems-gcc-7.4.0-newlib-1d35a003f.cfg``. And
     add the information about your patch as mentioned below.

.. code-block:: spec

    %patch add newlib -p1 file://0001-Port-ndbm.patch <1>
    %hash sha512 0001-Port-ndbm.patch 7d999ceeea4f3dc82e8e0aadc09d983a7a68b44470da8a3d61ab6fc558fdba6f2c2de3acc2f32c0b0b97fcc9ab799c27e87afe046544a69519881f947e7881d1 <2>

.. topic:: Items:

  1. The diff file prepended with ``file://`` to tell RSB this is a local file.

  2. The output from sha512sum on the patch file.
