.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH
.. Copyright (C) 2019, 2020 Sebastian Huber

.. index:: BSP build system
.. index:: build system

.. _BSPBuildSystem:

BSP Build System
****************

The purpose of the build system is to produce and install artefacts from the
RTEMS sources such as static libraries, start files, linker command files,
configuration header files, header files, test programs, package description
files, and third-party build system support files for a specific BSP in a user
controlled configuration.

Overview
========

The build system consists of three components which are all included in the
RTEMS sources

* the `waf <https://waf.io/>`_ meta build system command line tool,

* a `wscript <https://git.rtems.org/rtems/tree/wcript>`_ file used by ``waf``,
  and

* a
  `set of build specification items <https://git.rtems.org/rtems/tree/spec/build>`_
  maintained by a text editor just like other source files.

The build system is controlled by the user through

* commands passed to the ``waf`` command line tool,

* command line options passed to ``waf``, and

* configuration files (e.g. ``config.ini``) used by ``wscript`` through ``waf``
  invocations.

Configurable things which are subject to a local installation variant such as
paths to tools are intended to be passed as command line options to the ``waf``
command line tool.  Which BSPs are built and how they are configured by means of
options is placed in configuration files (e.g. ``config.ini``).  The
configuration files may reside anywhere in the file system and the goal is to
have it under version control by the user.

Work Flow
=========

There are five steps necessary to build and install one or more BSPs.

1. Select which BSPs you want to build.  See also :ref:`BSPs` and
   ``./waf bsp_list``.

2. Write a BSP build configuration file (e.g. ``config.ini``) which determines
   which BSPs are built and how they are configured.

3. Run the ``./waf configure`` command to generate the build
   environment.

4. Build the BSP artefacts with ``./waf``.  The build uses the build environment
   created by ``./waf configure``.  The BSP build configuration file (e.g.
   ``config.ini``) is no longer used and may be deleted.

5. Install the BSP artefacts with ``./waf install``.

Commands
========

The build system is controlled by invocations of the ``./waf`` command line
tool instead of the well known ``make``.  Since waf is written in Python, a
standard Python 2.7 or 3 installation without third-party packages is required
to run it.  The ``./waf`` command line tool must be invoked in the RTEMS source
tree top-level directory.

Some commands accept the ``--rtems-specs`` command line option.  This option
specifies paths to build specification items.  It is an advanced option and
there is normally no need to use it.  It may be used to customize the build at
the level of the build specification.  For more information see the
`Build System` chapter of the
`RTEMS Software Engineering <https://docs.rtems.org/branches/master/eng/build-system.rst>`_
guide.

Help
----

Use ``./waf --help`` to get a list of commands and options.

BSP List
--------

The BSP list command ``./waf bsp_list`` loads the build specification items and
generates a list of base BSPs from it.  The list is sorted by architecture and
base BSP name.  Which base BSPs are listed can be controlled by the
``--rtems-bsps`` command line option.  It expects a comma-separated list of
`Python regular expressions <https://docs.python.org/3/library/re.html#regular-expression-syntax>`_
which select the desired BSP variants.  The path to the build specification
items can be specified by the ``--rtems-specs`` command line option.

.. code-block:: none

    $ ./waf bsp_list --rtems-bsps=sparc/
    sparc/at697f
    sparc/erc32
    sparc/gr712rc
    sparc/gr740
    sparc/leon2
    sparc/leon3
    sparc/ut699
    sparc/ut700

.. code-block:: none

    $ ./waf bsp_list --rtems-bsps='/leon,/rv64imac$'
    riscv/rv64imac
    sparc/leon2
    sparc/leon3

BSP Defaults
------------

The BSP defaults command ``./waf bspdefaults`` loads the build specification
items and generates a list options with default values for each base BSP from
it.  The list is sorted by architecture and base BSP name.  Which base BSPs are
listed can be controlled by the ``--rtems-bsps`` command line option.  Default
values may depend on the selected compiler.  The compiler can be specified by
the ``--rtems-compiler`` command line option.  The path to the build
specification items can be specified by the ``--rtems-specs`` command line
option.

.. code-block:: none

    $ ./waf bspdefaults --rtems-bsps=gr712rc --rtems-compiler=gcc | grep ABI_FLAGS
    ABI_FLAGS = -mcpu=leon3 -mfix-gr712rc

.. code-block:: none

    $ ./waf bspdefaults --rtems-bsps=gr712rc --rtems-compiler=clang | grep ABI_FLAGS
    ABI_FLAGS = -mcpu=gr712rc

Configure
---------

The configure command ``./waf configure`` loads the BSP build configuration
files and the build specification items and configures the build environment
accordingly.  The configuration files can be specified by the ``--rtems-config``
command line option.  It expects a comma-separated list of paths to the
configuration files.  By default, the file ``config.ini`` is used.  The paths to
RTEMS tools can be specified by the ``--rtems-tools`` command line option.  It
expects a comma-separated list of prefix paths to tools, e.g.  compiler, linker,
etc.  By default, the installation prefix is used for the RTEMS tools.  Tools
are searched in the prefix path and also in a ``bin`` subdirectory of the prefix
path.  The path to the build specification items can be specified by the
``--rtems-specs`` command line option.

Build, Clean, and Install
-------------------------

The commands ``./waf``, ``./waf clean``, and ``./waf install`` load the build
specification items according to the specification paths stored in the build
environment.  The BSP build configuration files (e.g. ``config.ini``) used by
the ``./waf configure`` command to create the build environment are not longer
used and may be deleted.  The build commands perform a dependency tracking and
re-build artefacts if input sources changed.  Input sources are also the build
specification.

Configuration
=============

The BSP build configuration is done via INI-style configuration files.  The
configuration files are consumed by the ``./waf configure`` command.  By
default, the file ``config.ini`` is used.  You can specify other configuration
files with the ``--rtems-config`` command line option.  The configuration files
consist of sections and options (key-value pairs).

To build a particular BSP, you have to create a section with the BSP variant
name.

.. code-block:: ini

    [sparc/erc32]

This one line configuration file is sufficient to build the base BSP
`sparc/erc32` with default values for all options.  The base BSPs are determined
by the build specification.  The ``./waf bsp_list`` command lists all base BSPs.
You can create your own BSP names.  However, in this case you have to inherit
from a base BSP.  The inheritance works only within an architecture, e.g. a
`riscv` BSP cannot inherit options from an `arm` BSP.

.. code-block:: ini

    [sparc/foobar]
    INHERIT = erc32

The inheritance works recursively and must end up in a base BSP.

.. code-block:: ini

    [sparc/foo]
    INHERIT = erc32

    [sparc/bar]
    INHERIT = foo

A child BSP variant inherits all options from the parent BSP variant.  The child
BSP can override the inherited options.

You can determine the compiler used to build the BSP with the ``COMPILER``
option.

.. code-block:: ini

    [sparc/gr740_gcc]
    INHERIT = gr740
    COMPILER = gcc

    [sparc/gr740_clang]
    INHERIT = gr740
    COMPILER = clang

Use the ``./waf bspdefaults`` command to get a list of all configuration
options with default values.

.. code-block:: none

    $ ./waf bspdefaults --rtems-bsps=sparc/erc32
    [sparc/erc32]
    # Flags passed to the library archiver
    ARFLAGS = crD
    # Warning flags passed to the C compiler
    CC_WARNING_FLAGS = -Wmissing-prototypes -Wimplicit-function-declaration -Wstrict-prototypes -Wnested-externs
    # Warning flags passed to the C++ compiler
    CXX_WARNING_FLAGS =
    # Flags passed to the linker (GNU ld)
    LDFLAGS = -Wl,--gc-sections
    # Enable the Ada support
    __RTEMS_ADA__ = False
    # Enable the RTEMS internal debug support
    RTEMS_DEBUG = False
    ...
    # Install the legacy application Makefile framework.
    INSTALL_LEGACY_MAKEFILES = True

It is not recommended to blindly add all the options obtained through the
``./waf bspdefaults`` command to custom configuration files.  The specified
options should be kept at the necessary minimum to get the desired build.

Some projects may still want to specify all options in a configuration file to
be independent of changes in the base BSP.  You can review differences between
the user and base BSP values with the ``diff`` command.

.. code-block:: none

    $ ./waf bspdefaults --rtems-bsps=sparc/erc32 > config.ini
    $ sed -i 's/BUILD_TESTS = False/BUILD_TESTS = True/' config.ini
    $ ./waf bspdefaults --rtems-bsps=sparc/erc32 | diff -u - config.ini
    --- config.ini  2019-12-04 08:21:36.049335872 +0100
    +++ -   2019-12-04 08:21:41.187432405 +0100
    @@ -31,7 +31,7 @@
     # Build the Ada test programs (may be also enabled by BUILD_TESTS)
     BUILD_ADATESTS = False
     # Build the test programs
    -BUILD_TESTS = False
    +BUILD_TESTS = True
     # Build the benchmark programs (may be also enabled by BUILD_TESTS)
     BUILD_BENCHMARKS = False
     # Build the file system test programs (may be also enabled by

There is a special section ``DEFAULT`` which can be used to specify default
values for all other sections of the configuration file.  In the following
example configuration file, building of the tests is enabled for the
`sparc/erc32` and the `riscv/griscv` BSP.

.. code-block:: ini

    [DEFAULT]
    BUILD_TESTS = True

    [sparc/erc32]

    [riscv/griscv]

Migration from Autoconf/Automake
================================

The Autoconf/Automake based build system used a ``configure`` command to
configure a single target architecture and one or more BSPs.  The ``make``
command was used to build it.  The ``configure`` command is replaced by a
``./waf configure`` invocation with configuration file.  The ``make`` command
is replaced by ``./waf`` and ``make install`` is replaced by ``./waf install``.

Here are some hints for how a configure command line can be converted to
options in the configuration file of the ``waf`` based build system.  BSP
options given at the configure command line have to be added to the BSP section
in the configuration file.

``--target=${arch}-rtems6`` ``--enable-rtembsp=${bsp}``
        To build a BSP add ``[${arch}/${bsp}]`` to the configuration file.

``--enable-ada`` | ``--disable-ada``
        Set ``__RTEMS_ADA__`` to ``True`` or ``False`` in the BSP section of
        the configuration file.

``--enable-multiprocessing`` | ``--disable-multiprocessing``
        Set ``RTEMS_MULTIPROCESSING`` to ``True`` or ``False`` in the BSP
        section of the configuration file.

``--enable-paravirt`` | ``--disable-paravirt``
        Set ``RTEMS_PARAVIRT`` to ``True`` or ``False`` in the BSP section of
        the configuration file.

``--enable-profiling`` | ``--disable-profiling``
        Set ``RTEMS_PROFILING`` to ``True`` or ``False`` in the BSP section of
        the configuration file.

``--enable-posix`` | ``--disable-posix``
        Set ``RTEMS_POSIX_API`` to ``True`` or ``False`` in the BSP section of
        the configuration file.

``--enable-rtems-debug`` | ``--disable-rtems-debug``
        Set ``RTEMS_DEBUG`` to ``True`` or ``False`` in the BSP section of the
        configuration file.

``--enable-smp`` | ``--disable-smp``
        Set ``RTEMS_SMP`` to ``True`` or ``False`` in the BSP section of the
        configuration file.

``--enable-tests`` | ``--disable-tests``
        Set ``BUILD_TESTS`` to ``True`` or ``False`` in the BSP section of the
        configuration file.

``--enable-tests=samples``
        Set ``BUILD_SAMPLES`` to ``True`` or ``False`` in the BSP section of
        the configuration file.

Please have a look at the following example configuration file.

.. code-block:: ini

    # --target=sparc-rtems6 --enable-rtemsbsp=erc32
    [sparc/erc32]

    # --enable-ada
    __RTEMS_ADA__ = True

    # --enable-multiprocessing
    RTEMS_MULTIPROCESSING = False

    # --disable-paravirt
    RTEMS_PARAVIRT = False

    # --enable-profiling
    RTEMS_PROFILING = True

    # --disable-posix
    RTEMS_POSIX_API = False

    # --enable-rtems-debug
    RTEMS_DEBUG = True

    # --disable-smp
    RTEMS_SMP = False

    # --enable-tests
    BUILD_TESTS = True

    # BSP_POWER_DOWN_AT_FATAL_HALT=
    BSP_POWER_DOWN_AT_FATAL_HALT = False
