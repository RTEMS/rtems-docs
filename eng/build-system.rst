.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. _BSPBuildSystem:

BSP Build System
****************

The purpose of the build system is to produce and install artefacts from the
RTEMS sources such as static libraries, start files, linker command files,
configuration header files, header files, test programs, package description
files, and third-party build system support files for a specific BSP in a user
controlled configuration.

Goals
=====

The system should meet the following goals:

* The install location of artefacts should be the same as in previous build
  systems

* Easy build configuration of BSPs through configuration options

* Enable the BSP build configuration to be placed in a version control system
  (e.g. no local paths)

* Fast builds (also on Windows)

* Easy to maintain, e.g. add/remove a BSP, add/change/remove configuration
  options, add/remove a library, add/remove an object to/from a library,
  add/remove tests

* Reusable build specifications (e.g. generate documentation for BSP options for
  the user manual)

* Validation of built artefacts (e.g. ensure that the objects are built as
  specified using the DWARF debug information)

* Support building of BSPs external to the project

* Customization of the build (e.g. build only a subset of the RTEMS functions)

* Support alternative compilers such as clang instead of GCC

* Ability to unit test the build system

* Version control system friendly change sets (e.g. most changes are line based
  in text files)

Configurable things which depend on the host computer environment such as paths
to tools are intended to be passed as command line options to the ``waf``
command line tool.  Configurable things which define what is built and how the
artefacts are configured are intended to be placed in configuration files that
can be configuration controlled.  The ``waf`` build script file called
``wscript`` should know nothing about the layout of the sources.  What is built
and how it is built should be completely defined by the user configuration and
the build specification items.

Overview
========

For an overview of the build system, see the *BSP Build System* chapter of the
`RTEMS User Manual <https://docs.rtems.org/branches/master/user/bld/>`_.

Commands
========

This section explains how the :ref:`SpecTypeBuildItemType` items determine what
the following ``waf`` commands do.

BSP List
--------

In the ``./waf bsp_list`` command, the BSP list is generated from the
:ref:`SpecTypeBuildBSPItemType` items.

BSP Defaults
------------

In the ``./waf bsp_defaults`` command, the BSP defaults are generated from the
:ref:`SpecTypeBuildBSPItemType` and :ref:`SpecTypeBuildOptionItemType` items.
Build specification items contribute to the command through the
``do_defaults()`` method in the ``wscript``.

Configure
---------

In the ``./waf configure`` command, the build specification items contribute to
the command through the ``prepare_configure()`` and ``do_configure()`` methods
in the ``wscript``.

Build, Clean, and Install
-------------------------

In the ``./waf``, ``./waf clean``, and ``./waf install`` commands, the build
specification items contribute to the commands through the ``prepare_build()``
and ``do_build()`` methods in the ``wscript``.

UID Naming Conventions
======================

Use the following patterns for :ref:`UID names <ReqEngIdent>`:

abi
    Use the name ``abi`` for the GCC-specific ABI flags item of a BSP family.
    Each BSP family should have exactly one :ref:`SpecTypeBuildOptionItemType`
    item which defines the GCC-specific ABI flags for all base BSPs of the
    family.  For an architecture named *arch* and a BSP family named *family*,
    the file path is ``spec/build/bsps/arch/family/abi.yml``.

abiclang
    Use the name ``abiclang`` for the clang-specific ABI flags item of a BSP
    family.  Each BSP family may have at most one
    :ref:`SpecTypeBuildOptionItemType` item which defines the clang-specific
    ABI flags for all base BSPs of the family.  For an architecture named
    *arch* and a BSP family named *family*, the file path is
    ``spec/build/bsps/arch/family/abiclang.yml``.

bsp*
    Use the prefix ``bsp`` for base BSPs.

cfg*
    Use the prefix ``cfg`` for ``config.h`` header options.

grp*
    Use the prefix ``grp`` for groups.

lib*
    Use the prefix ``lib`` for libraries.

linkcmds*
    Use the prefix ``linkcmds`` for linker command files.

obj*
    Use the prefix ``obj`` for objects.  Use

    * ``objmpci`` for objects which are enabled by ``RTEMS_MULTIPROCESSING``,

    * ``objnet`` for objects which are enabled by ``RTEMS_NETWORKING``,

    * ``objnetnosmp`` for objects which are enabled by ``RTEMS_NETWORKING`` and
      not ``RTEMS_SMP``, and

    * ``objsmp`` for objects which are enabled by ``RTEMS_SMP``.

opt*
    Use the prefix ``opt`` for options.  Use 

    * ``optclock*`` for options which have something to do with the clock
      driver,

    * ``optconsole*`` for options which have something to do with the console
      driver,

    * ``optirq*`` for options which have something to do with interrupt
      processing,

    * ``optmem*`` for options which have something to do with the memory
      configuration, map, settings, etc., and

    * ``optosc*`` for options which have something to do with oscillators.

start
    Use the name ``start`` for BSP start file items.  Each architecture or BSP
    family should have a :ref:`SpecTypeBuildStartFileItemType` item which
    builds the start file of a BSP.  For an architecture named *arch* and a BSP
    family named *family*, the file path is ``spec/build/bsps/arch/start.yml``
    or ``spec/build/bsps/arch/family/start.yml``.  It is preferable to have a
    shared start file for the architecture instead of a start file for each BSP
    family.

tst*
    Use the prefix ``tst`` for test states.

.. _BuildSpecItems:

Build Specification Items
=========================

Specification items of refinements of the :ref:`SpecTypeBuildItemType` are used
by the ``wscript`` to determine what it should do.  The ``wscript`` does not
provide default values.  All values are defined by specification items.  The
entry point to what is built are the :ref:`SpecTypeBuildBSPItemType` items and
the top-level :ref:`SpecTypeBuildGroupItemType` item.  The user configuration
defines which BSPs are built.  The top-level group defaults to ``/grp`` and can
be changed by the ``--rtems-top-level`` command line option given to the ``waf
configure`` command.

The top-level group is a trade-off between the specification complexity and a
strict dependency definition.  Dependencies are normally explicit though the
item links.  However, using only explicit dependencies would make the
specification quite complex, see :numref:`BuildExplicitDeps`.  The top-level
group and explicit :ref:`SpecTypeBuildBSPItemType` items reduce the
specification complexity since they use a priori knowledge of global build
dependencies, see :numref:`BuildOrderDeps` for an example.  This approach makes
the build system easier, but less general.

.. _BuildExplicitDeps:

.. figure:: ../images/eng/bld-deps.*
    :width: 100%

    Example with Explicit Item Links

    This example shows how build item dependencies are specified explicitly
    by item links.  In this example, a user wants to build a group of tests.
    Each test program has a dependency on the standard RTEMS libraries.  The
    first issue is that the ``librtemsbsp.a`` needs dependencies to all base
    BSP variants (more than 100).  The dependencies are the values of the
    ``links`` attribute in the library item files.  External BSPs would have
    to modify the library item files.  This is quite undesirable.  The
    second issue is that the source files of the ``librtemscpu.a`` need a
    dependency to the ABI compiler flags specified by each BSP.  The third
    issue is that each BSP has to define its own ``bspopts.h`` configuration
    header item.

.. _BuildOrderDeps:

.. figure:: ../images/eng/bld-deps2.*
    :width: 50%

    Example with Implicit Ordering Rules

    This example shows how build item dependencies are specified by dedicated
    BSP items, a top-level group, and ordered item links.  The BSP is
    configured after the top-level group item and built before the top-level
    group item (defined by ``wscript`` source code).  The library group is
    configured and built before the test group as specified by the item link
    order in the top-level group.  The BSP options are processed before the
    results are written to the configuration header ``bspopts.h`` as defined by
    the BSP item link order.

.. _BuildHowTo:

How-To
======

This section presents how to do common maintenance tasks in the build system.

Find the Right Item
-------------------

You find all build specification items in the RTEMS sources under the
``spec/build`` directory.  You can use the ``grep`` command line tool to search
in the build specification items.

Create a BSP Architecture
-------------------------

Let *arch* be the name of the architecture.  You can add the new BSP
architecture with:

.. code-block:: none

    $ mkdir spec/build/bsps/arch

For a new architecture try to use a shared start file which can be used by all
BSPs of the architecture.  Add a :ref:`SpecTypeBuildStartFileItemType` item for
it:

.. code-block:: none

    $ vi spec/build/bsps/arch/start.yml

Create a BSP Family
-------------------

Let *family* be the BSP family name and *arch* the name of the architecture.
You can add the new BSP family with:

.. code-block:: none

    $ mkdir spec/build/bsps/arch/family

Add a :ref:`SpecTypeBuildOptionItemType` item for the ABI flags of the BSP family:

.. code-block:: none

    $ vi spec/build/bsps/arch/family/abi.yml

Define the ABI flags for each base BSP of the family.  The ``${ABI_FLAGS}`` are
used for the ``${ASFLAGS}``, ``${CFLAGS}``, ``${CXXFLAGS}``, and ``${LDFLAGS}``
build environment variables.  Please have a look at the following example which
shows the GCC-specific ABI flags item of the ``sparc/leon3`` BSP family:

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    actions:
    - get-string: null
    - split: null
    - env-append: null
    build-type: option
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    default:
    - -mcpu=leon3
    default-by-variant:
    - value:
      - -mcpu=leon3
      - -mfix-ut700
      variants:
      - sparc/ut700
    - value:
      - -mcpu=leon
      - -mfix-ut699
      variants:
      - sparc/ut699
    - value:
      - -mcpu=leon3
      - -mfix-gr712rc
      variants:
      - sparc/gr712rc
    description: |
      ABI flags
    enabled-by: gcc
    links: []
    name: ABI_FLAGS
    type: build

If the architecture has no shared start file, then add a
:ref:`SpecTypeBuildStartFileItemType` item for the new BSP family:

.. code-block:: none

    $ vi spec/build/bsps/arch/family/start.yml

Add a Base BSP to a BSP Family
------------------------------

.. _BuildBSPFamilyOneBSP:

.. figure:: ../images/eng/bld-bsp.*
    :width: 40%
    :figclass: align-center

    This example shows a BSP family named *family* in the architecture *arch*
    which consists of only one base BSP named *xyz*.  The BSP sources and
    installation information is contained in the
    ``spec:/build/bsps/arch/family/bspxyz`` BSP item.  The items linked by the
    BSP item are shown using relative UIDs.

.. _BuildBSPFamilyManyBSPs:

.. figure:: ../images/eng/bld-bsp2.*
    :width: 50%
    :figclass: align-center

    This example shows a BSP family named *family* in the architecture *arch*
    which consists of three base BSPs named *rst*, *uvw*, and *xyz*.  The BSP
    sources and installation information is contained in the *obj* objects
    item.  The group *grp* defines the main BSP constituents.  The base BSP
    items ``spec:/build/bsps/arch/family/bsprst``,
    ``spec:/build/bsps/arch/family/bspuvw``, and
    ``spec:/build/bsps/arch/family/bspxyz`` just define the name of the base
    BSP and set a link to the group item.  The base BSP names can be used for
    example in the ``default-by-variant`` attribute of
    :ref:`SpecTypeBuildOptionItemType` items.  The items linked by the BSP
    items are shown using relative UIDs.

Let *family* be the BSP family name, *arch* the name of the architecture, and
*new* the name of the new base BSP.  You can add the new base BSP with:

.. code-block:: none

    $ vi spec/build/bsps/arch/family/bspnew.yml

Define the attributes of your new base BSP according to
:ref:`SpecTypeBuildBSPItemType`.

In case the BSP family has no group, then create a group if it is likely that
the BSP family will contain more than one base BSP (see
:ref:`BuildHowToBSPFamilyGroup`).

If the BSP family has a group, then link the new base BSP to the group with:

.. code-block:: none

    $ vi spec/build/bsps/arch/familiy/grp.yml

Add a link using a relative UID to the new base BSP item:

.. code-block:: yaml

   links:
   - role: build-dependency
     uid: bspnew

Add a BSP Option
----------------

Let *family* be the BSP family name, *arch* the name of the architecture, and
*new* the name of the new BSP option.  You can add the new BSP option with:

.. code-block:: none

    $ vi spec/build/bsps/arch/family/optnew.yml

Define the attributes of your new BSP option according to
:ref:`SpecTypeBuildOptionItemType`.  Link the option item to the corresponding
group or BSP item using a relative UID:

.. code-block:: yaml

   links:
   - role: build-dependency
     uid: optnew

.. _BuildHowToBSPFamilyGroup:

Extend a BSP Family with a Group
--------------------------------

Let *family* be the BSP family name and *arch* the name of the architecture.  If
you want to have more than one base BSP in a BSP family, then you have to use a
group item (see :ref:`SpecTypeBuildGroupItemType`).  Add the group item named *grp* to the
family with:

.. code-block:: none

    $ vi spec/build/bsps/arch/family/grp.yml

Define the attributes of your new group according to
:ref:`SpecTypeBuildGroupItemType` and move the links of the existing base BSP
item to the group item.  Add a link to *obj*.

Add an objects item named *obj* to the family with:

.. code-block:: none

    $ vi spec/build/bsps/arch/family/obj.yml

Define the attributes of your new objects item according to
:ref:`SpecTypeBuildObjectsItemType` and move the ``cflags``, ``cppflags``,
``includes``, ``install`` and ``source`` attribute values of the
existing base BSP item to the objects item.

Add a Test Program
------------------

Let *collection* be the name of a test program collection and *new* the name of
the new test program.  You can add the new test program with:

.. code-block:: none

    $ vi spec/build/testsuites/collection/new.yml

Define the attributes of your new test program according to
:ref:`SpecTypeBuildTestProgramItemType`.

Edit corresponding group item of the test program collection:

.. code-block:: none

    $ vi spec/build/testsuites/collection/grp.yml

Add a link to the new test program item using a relative UID:

.. code-block:: yaml

   links:
   - role: build-dependency
     uid: new

Add a Library
-------------

Let *new* be the name of the new library.  You can add the new library with:

.. code-block:: none

    $ vi spec/build/cpukit/libnew.yml

Define the attributes of your new library according to
:ref:`SpecTypeBuildLibraryItemType`.

Edit corresponding group item:

.. code-block:: none

    $ vi spec/build/cpukit/grp.yml

Add a link to the new library item using a relative UID:

.. code-block:: yaml

   links:
   - role: build-dependency
     uid: libnew
