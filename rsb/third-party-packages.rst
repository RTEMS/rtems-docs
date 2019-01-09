.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

RTEMS 3rd Party Packages
========================

This section describes how to build and add an RTEMS 3rd party package to the
RSB.

A 3rd party package is a library or software package built to run on RTEMS,
examples are NTP, Net-Snmp, libjpeg or Python. These pieces of software can be
used to help build RTEMS applications. The package is built for a specific
BSP and so requires a working RTEMS tool chain and an installed RTEMS Board
Support Package (BSP).

The RSB support for building 3rd party packages is based around the *pkconfig*
files (PC) installed with the BSP. The pkgconfig support in RTEMS is considered
experimental and can have some issues for some BSPs. This issue is rooted deep
in the RTEMS build system. If you have any issues with this support please ask
on the RTEMS developers mailing list.

Vertical Integration
--------------------

The RSB supports horizontal integration with support for multiple
architectures. Adding packages to the RSB as libraries is vertical
integration. Building the GCC tool chain requires you build an assembler before
you build a compiler. The same can be done for 3rd party libraries, you can
crate build sets that stack library dependences vertically to create a *stack*.

Building
--------

To build a package you need to have a suitable RTEMS tool chain and RTEMS BSP
installed. The set builder command line requires you provide the tools path,
the RTEMS host, and the prefix path to the installed RTEMS BSP. The prefix
needs to be the same as the prefix used to build RTEMS.

To build Net-SNMP the command is:

.. code-block:: shell

    $ cd rtems-source-builder/rtems
    $ ../source-builder/sb-set-builder --log=log_sis_net_snmp \
        --prefix=$HOME/development/rtems/bsps/4.11 \
        --with-tools=$HOME/development/rtems/4.11 \
        --host=sparc-rtems4.11 --with-rtems-bsp=erc32 4.11/net-mgmt/net-snmp
    RTEMS Source Builder - Set Builder, v0.3.0
    Build Set: 4.11/net-mgmt/net-snmp
    config: net-mgmt/net-snmp-5.7.2.1-1.cfg
    package: net-snmp-5.7.2.1-sparc-rtems4.11-1
    building: net-snmp-5.7.2.1-sparc-rtems4.11-1
    installing: net-snmp-5.7.2.1-sparc-rtems4.11-1 -> /Users/chris/development/rtems/bsps/4.11
    cleaning: net-snmp-5.7.2.1-sparc-rtems4.11-1
    Build Set: Time 0:01:10.651926

Adding
------

Adding a package requires you first build it manually by downloading the source
for the package and building it for RTEMS using the command line of a standard
shell. If the package has not been ported to RTEMS you will need to port it and
this may require you asking questions on the package's user or development
support lists as well as RTEMS's developers list. Your porting effort may end
up with a patch. RTEMS requires a patch be submitted upstream to the project's
community as well as RTEMS so it can be added to the RTEMS Tools git
repository. A patch in the RTEMS Tools git reposiitory can then be referenced
by an RSB configuration file.

A package may create executables, for example NTP normally creates executables
such as ``ntdp``, ``ntpupdate``, or ``ntpdc``. These executables can be useful
when testing the package however they are of limited use by RTEMS users because
they cannot be directly linked into a user application. Users need to link to
the functions in these executables or even the executable as a function placed
in libraries. If the package does not export the code in a suitable manner
please contact the project's commuinity and see if you can work them to provide
a way for the code to be exported. This may be difficult because exporting
internal headers and functions opens the project up to API compatibility issues
they did not have before. In the simplest case attempting to get the code into
a static library with a single call entry point exported in a header would give
RTEMS user's access to the package's main functionality.

A package requires 3 files to be created:

- The first file is the RTEMS build set file and it resides in the
  ``rtems/config/%{rtems_version}`` path in a directory tree based on the
  FreeBSD ports collection. For the NTP package and RTEMS 4.11 this is
  ``rtems/config/4.11/net/ntp.bset``. If you do not know the FreeBSD port path
  for the package you are adding please ask. The build set file references a
  specific configuration file therefore linking the RTEMS version to a specific
  version of the package you are adding. Updating the package to a new version
  requires changing the build set to the new configuration file.

- The second file is an RTEMS version specific configuration file and it
  includes the RSB RTEMS BSP support. These configuration files reside in the
  ``rtems/config`` tree again under the FreeBSD port's path name. For example
  the NTP package is found in the ``net`` directory of the FreeBSD ports tree
  so the NTP configuration path is ``rtems/config/net/ntp-4.2.6p5-1.cfg`` for
  that specific version. The configuration file name typically provides version
  specific references and the RTEMS build set file references a specific
  version. This configuration file references the build configuration file held
  in the common configuration file tree.

- The build configuration. This is a common script that builds the package. It
  resides in the ``source-builder/config`` directory and typically has the
  packages's name with the major version number. If the build script does not
  change for each major version number a *common* base script can be created
  and included by each major version configuration script. The *gcc* compiler
  configuration is an example. This approach lets you branch a version if
  something changes that is not backwards compatible. It is important to keep
  existing versions building. The build configuration should be able to build a
  package for the build host as well as RTEMS as the RSB abstracts the RTEMS
  specific parts. See :ref:`Configuration` for more details.

BSP Support
-----------

The RSB provides support to help build packages for RTEMS. RTEMS applications
can be viewed as statically linked executables operating in a single address
space. As a result only the static libraries a package builds are required and
these libraries need to be ABI compatible with the RTEMS kernel and application
code meaning compiler ABI flags cannot be mixed when building code. The 3rd
party package need to use the same compiler flags as the BSP used to build
RTEMS.

.. note::

    RTEMS's dynamic loading support does not use the standard shared library
    support found in Unix and the ELF standard. RTEMS's loader uses static
    libraries and the runtime link editor performs a similar function to a host
    based static linker. RTEMS will only reference static libraries even if
    dynamic libraries are created and installed.

The RSB provides the configuration file ``rtems/config/rtems-bsp.cfg`` to
support building 3rd party packages and you need to include this file in your
RTEMS version specific configuration file. For example the Net-SNMP
configuration file ``rtems/config/net-mgmt/net-snmp-5.7.2.1-1.cfg``::

    #
    # NetSNMP 5.7.2.1
    #
    %if %{release} == %{nil}
     %define release 1    <1>
    %endif

    %include %{_configdir}/rtems-bsp.cfg   <2>

    #
    # NetSNMP Version
    #
    %define net_snmp_version 5.7.2.1   <3>

    #
    # We need some special flags to build this version.
    #
    %define net_snmp_cflags <4> -DNETSNMP_CAN_USE_SYSCTL=1 -DARP_SCAN_FOUR_ARGUMENTS=1 -DINP_IPV6=0

    #
    # Patch for RTEMS support.
    #
    %patch add net-snmp %{rtems_git_tools}/net-snmp/rtems-net-snmp-5.7.2.1-20140623.patch <5>

    #
    # NetSNMP Build configuration
    #
    %include %{_configdir}/net-snmp-5-1.cfg   <6>

.. topic:: Items:

  1. The release number.

  2. Include the RSB RTEMS BSP support.

  3. The Net-SNMP package's version.

  4. Add specific CFLAGS to the build process. See the
    ``net-snmp-5.7.2.1-1.cfg`` for details.

  5. The RTEMS Net-SNMP patch downloaded from the RTEMS Tools git repo.

  6. The Net-SNMP standard build configuration.

The RSB RTEMS BSP support file ``rtems/config/rtems-bsp.cfg`` checks to make
sure standard command line options are provided. These include ``--host`` and
``--with-rtems-bsp``. If the ``--with-tools`` command line option is not given
the ``${_prefix}`` is used::

    %if %{_host} == %{nil} <1>
     %error No RTEMS target specified: --host=host
    %endif

    %ifn %{defined with_rtems_bsp} <2>
     %error No RTEMS BSP specified: --with-rtems-bsp=bsp
    %endif

    %ifn %{defined with_tools} <3>
     %define with_tools %{_prefix}
    %endif

    #
    # Set the path to the tools.
    #
    %{path prepend %{with_tools}/bin} <4>

.. topic:: Items:

  1. Check the host has been set.

  2. Check a BSP has been specified.

  3. If no tools path has been provided assume they are under the
     ``%{_prefix}``.

  4. Add the tools ``bin`` path to the system path.

RTEMS exports the build flags used in *pkgconfig* (.pc) files and the RSB can
read and manage them even when there is no pkgconfig support installed on your
build machine. Using this support we can obtain a BSP's configuration and set
some standard macros variables (``rtems/config/rtems-bsp.cfg``)::

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

  2. Let pkgconfig know this is a cross-compile build.

  3. Filter flags such as warnings. Warning flags are specific to a package.

  4. Ask pkgconfig for the various items we require.

The flags obtain by pkgconfig and given a ``rtems_bsp_`` prefix and we uses these
to set the RSB host support CFLAGS, LDFLAGS and LIBS flags. When we build a 3rd
party library your host computer is the _build_ machine and RTEMS is the _host_
machine therefore we set the ``host`` variables
(``rtems/config/rtems-bsp.cfg``)::

    %define host_cflags  %{rtems_bsp_cflags}
    %define host_ldflags %{rtems_bsp_ldflags}
    %define host_libs    %{rtems_bsp_libs}

Finally we provide all the paths you may require when configuring a
package. Packages by default consider the ``_prefix`` the base and install
various files under this tree. The package you are building is specific to a
BSP and so needs to install into the specific BSP path under the
``_prefix``. This allows more than BSP build of this package to be install
under the same ``_prefix`` at the same time (``rtems/config/rtems-bsp.cfg``)::

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

  1. The path to the BSP.

When you configure a package you can reference these paths and the RSB will
provide sensible default or in this case map them to the BSP
(``source-builder/config/ntp-4-1.cfg``)::

      ../${source_dir_ntp}/configure \ <1>
        --host=%{_host} \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --exec_prefix=%{_exec_prefix} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --datadir=%{_datadir} \
        --disable-ipv6 \
        --disable-HOPFPCI

.. topic:: Items:

  1. The configure command for NTP.

RTEMS BSP Configuration
-----------------------

To build a package for RTEMS you need to build it with the matching BSP
configuration. A BSP can be built with specific flags that require all code
being used needs to be built with the same flags.
