.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

Third-Party Packages
--------------------

This section describes how to build and add an RTEMS third-party package to the
RSB.

A third-party package is a library or software package built to run on RTEMS,
examples are Curl, NTP, Net-Snmp, libjpeg and more. These pieces of software
can be used to help build RTEMS applications. The package is built for a
specific BSP and so requires a working RTEMS tool chain, an installed RTEMS
Board Support Package (BSP), and a network stack if the package uses
networking resources.

.. sidebar:: Help

   If you have any issues using, building or adding third party packages please
   ask on the RTEMS users mailing list.


The RSB support for building third-party packages is based around the
*pkconfig* files (PC) installed with the BSP. The pkgconfig support in RTEMS is
considered experimental and can have some issues for some BSPs. This issue is
rooted deep in the RTEMS build system.

Vertical Integration
^^^^^^^^^^^^^^^^^^^^

The RSB supports horizontal integration with support for multiple
architectures. Adding packages to the RSB as libraries is vertical
integration. Building the GCC tool chain requires you build an assembler
before you build a compiler. The same can be done for third-party libraries,
you can create build sets that stack library dependences vertically to create
a *stack*.

Building
^^^^^^^^

To build a package you need to have a suitable RTEMS tool chain and RTEMS BSP
installed. The set builder command line requires you provide the tools path,
the RTEMS architecture (host), the BSP, and the prefix path used to the
install RTEMS BSP.

The RSB prefix option (``--prefix``) provided when building a package is the
path to:

#. The tools, RTEMS kernel and any dependent libraries such as LibBSD. The
   package will be installed into the prefix path. This build configuration can
   be used to make a complete set of development tools and libraries for a
   project or product under a single path.

#. The RTEMS kernel and any dependent libraries such as LibBSD. The tools path
   needs to be in the environment path (not recommended) or provided to the set
   builder command by the ``--with-tools`` option. The package will be
   installed into the prefix path. This build configuration can be used when
   you have a set of tools used with a number of RTEMS BSPs. The tools can be
   shared between the different BSPs.

#. The path the package is installed into. The tools path needs to be in the
   environment path (not recommended) or provided to the set builder command
   using the ``--with-tools`` option. The path to the RTEMS kernel and any
   dependent libraries such as LibBSD needs to be supplied to the set builder
   command using the ``--with-rtems`` option. This build configuration can be
   used when you have a set of libraries you are testing with a changing RTEMS
   kernel. Becareful using this configuration as changes in RTEMS interfaces
   may require rebuilding these packages.

The set builder command option ``--host`` is used to provide the RTEMS
architecture the package is being built for. For example ``--host=arm-rtems5``
is used for any ARM BSP.

The set builder command option ``--with-rtems-bsp`` is the RTEMS BSP the
package is being built for. The BSP is searched for under the path provided by
the command option ``--with-rtems`` and if this option is not provided the
provided prefix is searched.

The following example builds and installs the Curl networking package for the
ARM BeagleBone Black BSP installing it into the same path the tools, RTEMS
kernel and LibBSD are installed in.

.. code-block:: none

 $ ../source-builder/sb-set-builder --prefix=$HOME/development/cs/rtems/5 \
       --log=curl.txt --host=arm-rtems5 --with-rtems-bsp=beagleboneblack ftp/curl
 RTEMS Source Builder - Set Builder, 5 (2bdae1f169e4)
 Build Set: ftp/curl
 config: ftp/curl-7.65.1-1.cfg
 package: curl-v7.65.1-arm-rtems5-1
 download: https://curl.haxx.se/download/curl-7.65.1.tar.xz -> sources/curl-7.65.1.tar.xz
 downloading: sources/curl-7.65.1.tar.xz - 2.3MB of 2.3MB (100%)
 building: curl-v7.65.1-arm-rtems5-1
 sizes: curl-v7.65.1-arm-rtems5-1: 87.055MB (installed: 2.238MB)
 cleaning: curl-v7.65.1-arm-rtems5-1
 reporting: ftp/curl-7.65.1-1.cfg -> curl-v7.65.1-arm-rtems5-1.txt
 reporting: ftp/curl-7.65.1-1.cfg -> curl-v7.65.1-arm-rtems5-1.xml
 installing: curl-v7.65.1-arm-rtems5-1 -> /Users/chris/development/cs/rtems/5
 cleaning: curl-v7.65.1-arm-rtems5-1
 Build Set: Time 0:01:10.006872

Adding
^^^^^^

Adding a package requires you first build it manually by downloading the
source for the package and building it for RTEMS using the command line of a
standard shell. If the package has not been ported to RTEMS you will need to
port it and this may require asking questions on the package's user or
development support lists as well as RTEMS's developers list. Your porting
effort may end up with a patch. RTEMS requires a patch be submitted upstream
to the project's community as well as RTEMS. The RTEMS submission is best as a
patch attached to ticket in Trac. A patch attached to a ticket can be
referenced by an RSB configuration file and used in a build.

.. sidebar:: Patches in Trac

   Attaching patches for packages to Trac tickets provides an easy to reference
   URL the RSB can fetch. The patch URL does not change across RTEMS versions
   and it does not depend on the state or layout of a git repo.


A package may create executables, for example Curl normally creates an
executable called ``curl`` how ever it will probailty not run because the
needed RTEMS configuration is not suitable. If found the RSB automatically
adds the RTEMS library ``librtemsdefaultconfig.a`` to the ``LIBS`` variable
used to link executables. This library provides a limited configuraiton
suitable for linking an executable however it is not a set up that allows the
resulting executable to run correctly. As a result it is best not to install
these executables.

A custom RTEMS patch to an executate's source code can turn it into a function
that can be called by the RTEMS shell. Users can call the function in their
executables simulating the running of the package's command. If the package
does not export the code in a suitable manner please contact the project's
community and see if you can work with them to provide a way for the code to
be exported. This may be difficult because exporting internal headers and
functions opens the project up to API compatibility issues they did not have
before. In the simplest case attempting to get the code into a static library
with a single call entry point exported in a header would give RTEMS user's
access to the package's main functionality.

A package requires at least three (3) files to be created:

  Published Package Name:
    The first file is the RTEMS build set file and it resides under the
    ``rtems/config`` path in a directory tree based on the FreeBSD ports
    collection. For the Curl package and RTEMS 5 this is
    ``rtems/config/ftp/curl.bset``. If you do not know the FreeBSD port path
    for the package you are adding please ask. The build set file references a
    specific configuration file therefore linking the RTEMS version to a
    specific version of the package you are adding. Updating the package to a
    new version requires changing the build set to the new configuration file.

  Package Version Configuration File:
    The second file is an RTEMS version specific configuration file and it
    includes the RSB RTEMS BSP support. These configuration files reside in
    the ``rtems/config`` tree and under the FreeBSD port's path name. For
    example the Curl package is found in the ``ftp`` directory of the FreeBSD
    ports tree so the Curl configuration path is
    ``rtems/config/ftp/curl-7.65.1-1.cfg`` for that specific version. The
    configuration file name typically provides version specific references and
    the RTEMS build set file references a specific version. This configuration
    file references the build configuration file held in the common
    configuration file tree. An SHA512 hash is required to verify the source
    package that is downloaded.

  Build Configuration File:
    The build configuration. This is a common script that builds the
    package. It resides in the ``source-builder/config`` directory and
    typically has the packages's name with the major version number. If the
    build script does not change for each major version number a *common* base
    script can be created and included by each major version configuration
    script. The *gcc* compiler configuration is an example. This approach lets
    you branch a version if something changes that is not backwards
    compatible. It is important to keep existing versions building. The build
    configuration should be able to build a package for the build host as well
    as RTEMS as the RSB abstracts the RTEMS specific parts. See
    :ref:`Configuration` for more details.

Host and Build Flags
^^^^^^^^^^^^^^^^^^^^

A package's build is controlled by setting the compiler names and flags that
are used when building. The RSB provides a macro called
``%{host_build_flags}`` to define these flags for you. Use this macro in the
```%build`` section of your config script file to define the set up needed to
build a native package or to cross-compile to a specific host such as RTEMS
. The typical ``%build`` section is:

.. code-block:: spec

 %build
   build_top=$(pwd)

   %{build_directory}

   mkdir -p ${build_dir}
   cd ${build_dir}

   %{host_build_flags}

   ../${source_dir_curl}/configure \
     --host=%{_host} \
     --prefix=%{_prefix} \
     --bindir=%{_bindir} \
     --exec_prefix=%{_exec_prefix} \
     --includedir=%{_includedir} \
     --libdir=%{_libdir} \
     --libexecdir=%{_libexecdir} \
     --mandir=%{_mandir} \
     --infodir=%{_infodir} \
     --datadir=%{_datadir}

   %{__make} %{?_smp_mflags} all

   cd ${build_top}

The ``%{host_build_flags}`` checks if the build is native for the development
host or a cross-compile build.

For a cross-complication build the flags are:

``CC``, ``CC_FOR_HOST``:
 The C compiler used to build the package. For an RTEMS build this is the
 RTEMS C compiler. For example the ARM architecture and RTEMS 5 the value is
 set to ``arm-rtems5-gcc``.

``CXX``, ``CXX_FOR_HOST``:
 The C++ compiler used to build the package. For an RTEMS build this is the
 RTEMS C++ compiler. For example the ARM architecture and RTEMS 5 the value is
 set to ``arm-rtems5-g++``.

``CPPFLAGS``, ``CPPFLAGS_FOR_HOST``:
 The C compiler preprocessor flags used to build the package. Set any include
 paths in this variable as some configure scripts will warns you if include
 paths are set in the ``CFLAGS``.

``CFLAGS``, ``CFLAGS_FOR_HOST``:
 The C compiler flags used when running the C compiler. Set any include paths
 in the ``CPPFLAGS`` variable as some configure scripts will warn you if
 include paths in this variable.

``CXXFLAGS``, ``CXXFLAGS_FOR_HOST``:
 The C++ compiler flags used when running the C++ compiler. Set any include
 paths in the ``CPPFLAGS`` variable as some configure scripts will warn you if
 include paths in this variable.

``LDFLAGS``, ``LDFLAGS_FOR_HOST``:
 The linker flags used whne link package executables. The C or C++ compiler
 is used to run the linker.

``LIBS``, ``LIBS_FOR_HOST``:
 A list of libraries passed to the linker when linking an executable.

``CC_FOR_BUILD``:
 The native C compiler.

``CXX_FOR_BUILD``:
 The native C++ compiler.

``CPPFLAGS_FOR_BUILD``:
 The C preprocessor flags used when preprocessoring a native C source file.

``CFLAGS_FOR_BUILD``:
 The native C compiler flags used when running the native C compiler.

``CXXFLAGS_FOR_BUILD``:
 The native C++ compiler flags used when running the native C++ compiler.

``LDFLAGS_FOR_BUILD``:
 The native linker flags used when linking a native executable.

``LIBS_FOR_BUILD``:
 The native libraries used to when linking a native executable.

For a native build the flags are:

``CC``, ``CC_FOR_BUILD``:
 The native C compiler.

``CXX``, ``CXX_FOR_BUILD``:
 The native C++ compiler.

``CPPFLAGS``, ``CPPFLAGS_FOR_BUILD``:
 The C preprocessor flags used when preprocessoring a native C source file.

``CFLAGS``, ``CFLAGS_FOR_BUILD``:
 The native C compiler flags used when running the native C compiler.

``CXXFLAGS``, ``CXXFLAGS_FOR_BUILD``:
 The native C++ compiler flags used when running the native C++ compiler.

``LDFLAGS``, ``LDFLAGS_FOR_BUILD``:
 The native linker flags used when linking a native executable.

``LIBS``, ``LIBS_FOR_BUILD``:
 The native libraries used to when linking a native executable.

BSP Support
^^^^^^^^^^^

The RSB provides support to build packages for RTEMS. RTEMS applications can
be viewed as statically linked executables operating in a single address
space. As a result only the static libraries a package builds are required and
these libraries need to be ABI compatible with the RTEMS kernel and
application code. This means the compiler ABI flags used to build all the code
in the executable must be the same. A 3rd party package must use the same
compiler flags as the BSP used to build RTEMS.

.. note::

    RTEMS's dynamic loading support does not use the standard shared library
    support found in Unix and the ELF standard. RTEMS's loader uses static
    libraries and the runtime link editor performs a similar function to a host
    based static linker. RTEMS will only reference static libraries even if
    dynamic libraries are created and installed.

The RSB provides the configuration file ``rtems/config/rtems-bsp.cfg`` to
support building third-party packages and you need to include this file in your
RTEMS version specific configuration file. For example the Curl configuration
file ``rtems/config/curl/curl-7.65.1-1.cfg``:

.. code-block:: spec

 #
 # Curl 7.65.1
 #

 %if %{release} == %{nil}
  %define release 1  <1>
 %endif

 %include %{_configdir}/rtems-bsp.cfg   <2>

 #
 # Curl Version
 #
 %define curl_version 7.65.1   <3>

 %hash sha512 curl-%{curl_version}.tar.xz aba2d979a...72b6ac55df4   <4>

 #
 # Curl Build configuration
 #
 %include %{_configdir}/curl-1.cfg <5>

.. topic:: Items:

  1. The release number.

  2. Include the RSB RTEMS BSP support.

  3. The Curl package's version.

  4. The SHA512 hash for the source file. The hash here has been shortened.

  5. The Curl standard build configuration.

The RSB RTEMS BSP support file ``rtems/config/rtems-bsp.cfg`` checks to make
sure the required RSB command line options are provided. These include
``--host`` and ``--with-rtems-bsp``. If the ``--with-tools`` command line
option is not given the ``${_prefix}`` is used as the path to the tools. If
the ``--with-rtems`` command line option is not given the ``${_prefix}`` is
used as the path to the installed RTEMS BSP.

.. note::

   The RTEMS BSP and any dependent 3rd party packages must be installed to be
   seen as available. A path to the location the BSP has been built will not
   work.

The first check is to make sure a target is not specified. This is only used
for Canadian cross-compilication builds and currently there is no support for
RTEMS third party packages to build that way:

.. code-block:: spec

 #
 # The target is used by compilers or Cxc builds.
 #
 %if %{_target} != %{nil}
  %error RTEMS BSP builds use --host and not --target
 %endif

A host is required using the ``--host`` option:

.. code-block:: spec

 #
 # We need a host from the user to specifiy the RTEMS architecture and major
 # version.
 #
 %if %{_host} == %{nil} && %{rtems_bsp_error} <1>
  %error No RTEMS host or BSP specified: --host=<arch>-rtems<ver>
 %endif

An RTEMS BSP is required using the ``--with-bsp`` option:

.. code-block:: spec

 #
 # We need a BSP from the user.
 #
 %ifn %{defined with_rtems_bsp}
  %if %{rtems_bsp_error}
   %error No RTEMS BSP specified: --rtems-bsp=arch/bsp (or --with-rtems-bsp=bsp)
  %endif
  %define with_rtems_bsp sparc/erc32
 %endif

Check if the ``--with-tools`` or ``--with-rtems`` options have been provided
and if they are not provided use the ``--prefix`` path:

.. code-block:: spec

 #
 # If no tools or RTEMS provided use the prefix.
 #
 %ifn %{defined with_tools}
  %define with_tools %{_prefix}
 %endif

 %ifn %{defined with_rtems}
  %define with_rtems %{_prefix}
 %endif

Add the tools path to the envnironment path:

.. code-block:: spec

 #
 # Set the path to the tools.
 #
 %{path prepend %{with_tools}/bin}

RTEMS exports the build configuration in *pkgconfig* (.pc) files. The RSB can
read these files even when there is no ``pkgconfig`` support installed on your
development machine. The *pkgconfig* support provides a BSP's configuration and
the RSB uses it to set the followng RSB macros variables:

.. code-block:: spec

    %{pkgconfig prefix %{_prefix}/lib/pkgconfig} <1>
    %{pkgconfig crosscompile yes} <2>
    %{pkgconfig filter-flags yes} <3>

    #
    # The RTEMS BSP Flags
    #
    %define rtems_bsp           %{with_rtems_bsp}
    %define rtems_bsp_ccflags   %{pkgconfig ccflags %{_host}-%{rtems_bsp}} <4>
    %define rtems_bsp_cflags    %{pkgconfig cflags  %{_host}-%{rtems_bsp}}
    %define rtems_bsp_ldflags   %{pkgconfig ldflags %{_host}-%{rtems_bsp}}
    %define rtems_bsp_libs      %{pkgconfig libs    %{_host}-%{rtems_bsp}}

.. topic:: Items:

  1. Set the path to the BSP's pkgconfig file.

  2. Let *pkgconfig* know this is a cross-compile build.

  3. Filter flags such as warnings. Warning flags are specific to a package and
     RTEMS exports it's warnings flags in the BSP configuration settings.

  4. Ask *pkgconfig* for the various settings we require.

The flags obtained by *pkgconfig* and given a ``rtems_bsp`` prefix are used to
set the RTEMS host variables ``CFLAGS``, ``LDFLAGS`` and ``LIBS``. When we
build a third party library your host computer is the **build** machine and
RTEMS is the **host** machine therefore we set the ``host`` variables:

.. code-block:: spec

    %define host_cflags  %{rtems_bsp_cflags}
    %define host_ldflags %{rtems_bsp_ldflags}
    %define host_libs    %{rtems_bsp_libs}

Finally we provide all the paths you may require when configuring a
package. Packages by default consider the ``_prefix`` the base and install
various files under this tree. The package you are building is specific to a
BSP and needs to install it's files into the RTEMS specific BSP path under the
``_prefix``. This allows more than BSP build of this package to be installed
under the same ``_prefix`` at the same time:

.. code-block:: spec

    %define rtems_bsp_prefix  %{_prefix}/%{_host}/%{rtems_bsp} <1>
    %define _exec_prefix      %{rtems_bsp_prefix}
    %define _bindir           %{_exec_prefix}/bin
    %define _sbindir          %{_exec_prefix}/sbin
    %define _libexecdir       %{_exec_prefix}/libexec
    %define _datarootdir      %{_exec_prefix}/share
    %define _datadir          %{_datarootdir}
    %define _sysconfdir       %{_exec_prefix}/etc
    %define _sharedstatedir   %{_exec_prefix}/com
    %define _localstatedir    %{_exec_prefix}/var
    %define _includedir       %{_libdir}/include
    %define _lib              lib
    %define _libdir           %{_exec_prefix}/%{_lib}
    %define _libexecdir       %{_exec_prefix}/libexec
    %define _mandir           %{_datarootdir}/man
    %define _infodir          %{_datarootdir}/info
    %define _localedir        %{_datarootdir}/locale
    %define _localedir        %{_datadir}/locale
    %define _localstatedir    %{_exec_prefix}/var

.. topic:: Items:

  1. The path to the installed BSP.

When you configure a package you can reference these paths and the RSB will
provide sensible default or in this case map them to the BSP:

.. code-block:: spec

      ../${source_dir_curl}/configure \ <1>
        --host=%{_host} \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --exec_prefix=%{_exec_prefix} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --datadir=%{_datadir}

.. topic:: Items:

  1. The configure command for Curl.


BSP Configuration
^^^^^^^^^^^^^^^^^

The following RSB macros are defined when building a package for RTEMS:

.. note::

    A complete list can be obtained by building with the ``--trace`` flag. The
    log will contain a listing of all macros before and after the configuration
    is loaded.

``%{rtems_bsp}``:
 The name of the RTEMS BSP.

``%{rtems_bsp_cc}``:
 The C compiler name for the RTEMS BSP.

``%{rtems_bsp_cflags}``:
 The C compiler flags for the RTEMS BSP.

``%{rtems_bsp_ccflags}``:
 The C++ compiler flags for the RTEMS BSP.

``%{rtems_bsp_incpath}``:
 The include path to teh RTEMS BSP header files.

``%{rtems_bsp_ldflags}``:
 The linker flags for the RTEMS BSP.

``%{rtems_bsp_libs}``:
 The libraries used when linking an RTEMS BSP executable.

``%{rtems_bsp_prefix}``:
 The prefix for the RTEMS BSP.

``%{rtems-libbsd}``:
 The variable is set to ``found`` if LibBSD is available.

``%{rtems-defaultconfig}``:
 The path of the RSB helper script to locate find header files or libraries.

``%{_host}``
 The host triplet passed on the command line to the set builder using the
 ``--host`` options. This is the RTEMS architecture and version. For example
 ``arm-rtems5``.

``%{host_cflags}``:
 The BSP ``CFLAGS`` returned by ``pkgconfig``.

``%{host_cxxflags}``:
 The BSP ``CXXFLAGS`` returned by ``pkgconfig``.

``%{host_includes}``:
 The BSP include paths returned by ``pkgconfig``.

``%{host_ldflags}``:
 The BSP ``LDFLAGS`` returned by ``pkgconfig``.

``%{host_libs}``:
 The libraries needed to be linked to create an executable. If LibBSD is
 installed the library ``-lbsd`` is added. If the BSP has installed the RTEMS
 default configuration library (``-lrtemsdefaultconfig``) it is added to the
 list of libraries.

``%{host_build_flags}``:
 This macro is defined in ``defaults.mc`` and is a series of shell commands
 that set up the environment to build an RTEMS package. If the host and the
 build triplets are the same it is a native build for your development host. If
 the host is not the build machine it is a cross-complitation build. For either
 case the following are defined.

``%{_host_os}``:
 The host operating system extracted from the ``--host`` command line
 option. For example the operating sstem for the host of ``arm-rtems5`` is
 ``rtems5``.

``%{_host_arch}``:
 The host architecture extracted from the ``--host`` command line option. For
 example the architecture for the host of ``arm-rtems5`` is ``arm``.

``%{_host_cpu}``:
 The host cpu extracted from the ``--host`` command line option. For
 example the cpu for the host of ``arm-rtems5`` is ``arm``.
