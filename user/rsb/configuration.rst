.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

.. _Configuration:

Configuration
-------------

The RTEMS Source Builder has two types of configuration data:

- Build Sets

- Package Build Configurations

By default these files can be located in two separate directories and
searched. The first directory is ``config`` in your current working directory
(``_topdir``) and the second is ``config`` located in the base directory of the
RTEMS Source Builder command you run (``_sbdir``). The RTEMS directory
``rtems``` located at the top of the RTEMS Source Builder source code is an
example of a specific build configuration directory. You can create custom or
private build configurations and if you run the RTEMS Source Builder command
from that directory your configurations will be used.

The configuration search path is a macro variable and is reference as
``%{_configdir}``. It's default is defined as:

.. code-block:: spec

    _configdir   : dir  optional  %{_topdir}/config:%{_sbdir}/config

.. topic:: Items:

  1. The ``_topdir`` is the directory you run the command from and ``_sbdir``
     is the location of the RTEMS Source Builder command.

  2. A macro definition in a macro file has 4 fields, the label, type,
     constraint and the definition.

Build set files have the file extension ``.bset`` and the package build
configuration files have the file extension of ``.cfg``. The ``sb-set-builder``
command will search for *build sets* and the ``sb-builder`` commands works with
package build configuration files.

Both types of configuration files use the ``#`` character as a comment
character. Anything after this character on the line is ignored. There is no
block comment.

Source and Patches
^^^^^^^^^^^^^^^^^^

The RTEMS Source Builder provides a flexible way to manage source. Source and
patches are declare in configurations file using the ``source`` and ``patch``
directives. These are a single line containing a Universal Resource Location or
URL and can contain macros and shell expansions. The :ref:`prep` section
details the *source* and *patch* directives

The URL can reference remote and local source and patch resources. The
following schemes are provided:

``http``:
  Remote access using the HTTP protocol.

``https``:
  Remote access using the Secure HTTP protocol.

``ftp``:
  Remote access using the FTP protocol.

``git``:
  Remote access to a GIT repository.

``pm``:
  Remote access to a patch management repository.

``file``:
 Local access to an existing source directory.

HTTP, HTTPS, and FTP
~~~~~~~~~~~~~~~~~~~~

Remote access to TAR or ZIP files is provided using HTTP, HTTPS and FTP
protocols. The full URL provided is used to access the remote file including
any query components. The URL is parsed to extract the file component and the
local source directory is checked for that file. If the file is located locally
the remote file is not downloaded. Currently no other checks are made. If a
download fails you need to manually remove the file from the source directory
and start the build process again.

The URL can contain macros. These are expanded before issuing the request to
download the file. The standard GNU GCC compiler source URL is:

.. code-block:: spec

    %source set gcc ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.bz2

.. topic:: Items:

  1. The ``%source`` command's ``set`` command sets the source. The
     first is set and following sets are ignored.

  2. The source package is part of the ``gcc`` group.

The type of compression is automatically detected from the file extension. The
supported compression formats are:

``gz``:
  GNU ZIP

``bzip2``:
  BZIP2

``zip``:
  ZIP

``xy``:
  XY

The output of the decompression tool is fed to the standard ``tar`` utility if
not a ZIP file and unpacked into the build directory. ZIP files are unpacked by
the decompression tool and all other files must be in the tar file format.

The ``%source`` directive typically supports a single source file tar or zip
file. The ``set`` command is used to set the URL for a specific source
group. The first set command encountered is registered and any further set
commands are ignored. This allows you to define a base standard source location
and override it in build and architecture specific files. You can also add
extra source files to a group. This is typically done when a collection of
source is broken down in a number of smaller files and you require the full
package. The source's ``setup`` command must reside in the ``%prep:`` section
and it unpacks the source code ready to be built.

If the source URL references the GitHub API server https://api.github.com/ a
tarball of the specified version is download. For example the URL for the
STLINK project on GitHub and version is:

.. code-block:: spec

    %define stlink_version 3494c11
    %source set stlink https://api.github.com/repos/texane/stlink/texane-stlink-%{stlink_version}.tar.gz

GIT
~~~

A GIT repository can be cloned and used as source. The GIT repository resides
in the 'source' directory under the ``git`` directory. You can edit, update and
use the repository as you normally do and the results will used to build the
tools. This allows you to prepare and test patches in the build environment the
tools are built in. The GIT URL only supports the GIT protocol. You can control
the repository via the URL by appending options and arguments to the GIT
path. The options are delimited by ``?`` and option arguments are delimited
from the options with ``=``. The options are:

``protocol``:
  Use a specific protocol. The supported values are ``ssh``, ``git``, ``http``,
  ``https``, ``ftp``, ``ftps``, ``rsync``, and ``none``.

``branch``:
  Checkout the specified branch.

``pull``:
  Perform a pull to update the repository.

``fetch``:
  Perform a fetch to get any remote updates.

``reset``:
  Reset the repository. Useful to remove any local changes. You can pass the
  ``hard`` argument to force a hard reset.

An example is:

.. code-block:: spec

    %source set gcc git://gcc.gnu.org/git/gcc.git?branch=gcc-4_7-branch?reset=hard

This will clone the GCC git repository and checkout the 4.7-branch and perform
a hard reset. You can select specific branches and apply patches. The
repository is cleaned up before each build to avoid various version control
errors that can arise.

The protocol option lets you set a specific protocol. The ``git://`` prefix
used by the RSB to select a git repository can be removed using *none* or
replaced with one of the standard git protcols.

CVS
~~~

A CVS repository can be checked out. CVS is more complex than GIT to handle
because of the modules support. This can effect the paths the source ends up
in. The CVS URL only supports the CVS protocol. You can control the repository
via the URL by appending options and arguments to the CVS path. The options are
delimited by ``?`` and option arguments are delimited from the options with
``=``. The options are:

``module``:
  The module to checkout.

``src-prefix``:
  The path into the source where the module starts.

``tag``:
  The CVS tag to checkout.

``date``:
  The CVS date to checkout.

The following is an example of checking out from a CVS repository:

.. code-block:: spec

    %source set newlib cvs://pserver:anoncvs@sourceware.org/cvs/src?module=newlib?src-prefix=src

Macros and Defaults
^^^^^^^^^^^^^^^^^^^

The RTEMS Source Builder uses tables of *macros* read in when the tool
runs. The initial global set of macros is called the *defaults*. These values
are read from a file called ``defaults.mc`` and modified to suite your
host. This host specific adaption lets the Source Builder handle differences in
the build hosts.

Build set and configuration files can define new values updating and extending
the global macro table. For example builds are given a release number. This is
typically a single number at the end of the package name. For example:

.. code-block:: spec

    %define release 1

Once defined if can be accessed in a build set or package configuration file
with:

.. code-block:: spec

    %{release}

The ``sb-defaults`` command lists the defaults for your host. I will not include
the output of this command because of its size:

.. code-block:: shell

    $ ../source-builder/sb-defaults

A nested build set is given a separate copy of the global macro maps. Changes
in one change set are not seen in other build sets. That same happens with
configuration files unless inline includes are used. Inline includes are seen
as part of the same build set and configuration and changes are global to that
build set and configuration.

Macro Maps and Files
~~~~~~~~~~~~~~~~~~~~

Macros are read in from files when the tool starts. The default settings are
read from the defaults macro file called ``defaults.mc`` located in the top
level RTEMS Source Builder command directory. User macros can be read in at
start up by using the ``--macros`` command line option.

The format for a macro in macro files is:

.. code-block:: ini

  Name Type Attribute String

where ``Name`` is a case insensitive macro name, the ``Type`` field is:

``none``:
  Nothing, ignore.

``dir``:
  A directory path.

``exe``:
  An executable path.

``triplet``:
  A GNU style architecture, platform, operating system string.

the ``Attribute`` field is:

``none``:
  Nothing, ignore

``required``:
  The host check must find the executable or path.

``optional``:
  The host check generates a warning if not found.

``override``:
  Only valid outside of the ``global`` map to indicate this macro overrides the
  same one in the ``global`` map when the map containing it is selected.

``undefine``:
  Only valid outside of the ``global`` map to undefine the macro if it exists
  in the ``global`` map when the map containing it is selected. The ``global``
  map's macro is not visible but still exists.

and the ``String`` field is a single or tripled multiline quoted string. The
'String' can contain references to other macros. Macro that loop are not
currently detected and will cause the tool to lock up.

Maps are declared anywhere in the map using the map directive:

.. code-block:: ini

    # Comments
    [my-special-map] <1>
    _host:  none, override, 'abc-xyz'
    multiline: none, override, '''First line,
    second line,
    and finally the last line'''

.. topic:: Items:

  1. The map is set to ``my-special-map``.

Any macro defintions following a map declaration are placed in that map and the
default map is ``global`` when loading a file. Maps are selected in
configuration files by using the ``%select`` directive:

.. code-block:: spec

    %select my-special-map

Selecting a map means all requests for a macro first check the selected map and
if present return that value else the ``global`` map is used. Any new macros or
changes update only the ``global`` map. This may change in future releases so
please make sure you use the ``override`` attribute.

The macro files specificed on the command line are looked for in the
``_configdir`` paths. See <<X1,``_configdir``>> variable for details. Included
files need to add the ``%{_configdir}`` macro to the start of the file.

Macro map files can include other macro map files using the ``%include``
directive. The macro map to build *binutils*, *gcc*, *newlib*, *gdb* and
RTEMS from version control heads is:

.. code-block:: spec

    #
    # Build all tool parts from version control head.
    #
    %include %{_configdir}/snapshots/binutils-head.mc
    %include %{_configdir}/snapshots/gcc-head.mc
    %include %{_configdir}/snapshots/newlib-head.mc
    %include %{_configdir}/snapshots/gdb-head.mc

.. topic:: Items:

  1. The file is ``config/snapshots/binutils-gcc-newlib-gdb-head.mc``.

The macro map defaults to ``global`` at the start of each included file and the
map setting of the macro file including the other macro files does not change.

Personal Macros
~~~~~~~~~~~~~~~

When the tools start to run they will load personal macros. Personal macros are
in the standard format for macros in a file. There are two places personal
macros can be configured. The first is the environment variable
``RSB_MACROS``. If present the macros from the file the environment variable
points to are loaded. The second is a file called ``.rsb_macros`` in your home
directory. You need to have the environment variable ``HOME`` defined for this
work.

Report Mailing
^^^^^^^^^^^^^^

The build reports can be mailed to a specific email address to logging and
monitoring. Mailing requires a number of parameters to function. These are:

- To mail address

- From mail address

- SMTP host

.. _To Mail Address:

The ``to`` mail address is taken from the macro ``%{_mail_tools_to}`` and the
default is *rtems-tooltestresults at rtems.org*. You can override the default
with a personal or user macro file or via the command line option
``--mail-to``.

.. _From Mail Address:

The ``from`` mail address is taken from:

- GIT configuration

- User ``.mailrc`` file

- Command line

If you have configured an email and name in git it will be used used. If you do
not a check is made for a ``.mailrc`` file. The environment variable ``MAILRC``
is used if present else your home directory is check. If found the file is
scanned for the ``from`` setting:

.. code-block:: shell

  set from="Foo Bar <foo@bar>"

You can also support a from address on the command line with the ``--mail-from``
option.

The SMTP host is taken from the macro ``%{_mail_smtp_host}`` and the
default is ``localhost``. You can override the default with a personal
or user macro file or via the command line option ``--smtp-host``.

Build Set Files
^^^^^^^^^^^^^^^

Build set files lets you list the packages in the build set you are defining
and have a file extension of ``.bset``. Build sets can define macro variables,
inline include other files and reference other build set or package
configuration files.

Defining macros is performed with the ``%define`` macro:

.. code-block:: spec

    %define _target m32r-rtems4.11

Inline including another file with the ``%include`` macro continues processing
with the specified file returning to carry on from just after the include
point:

.. code-block:: spec

    %include rtems-4.11-base.bset

This includes the RTEMS 4.11 base set of defines and checks. The configuration
paths as defined by ``_configdir`` are scanned. The file extension is optional.

You reference build set or package configuration files by placing the file name
on a single line:

.. code-block:: spec

    tools/rtems-binutils-2.22-1

The ``_configdir`` path is scanned for ``tools/rtems-binutils-2.22-1.bset`` or
``tools/rtems-binutils-2.22-1.cfg``. Build set files take precedent over
package configuration files. If ``tools/rtems-binutils-2.22-1`` is a build set
a new instance of the build set processor is created and if the file is a
package configuration the package is built with the package builder. This all
happens once the build set file has finished being scanned.

Configuration Control
^^^^^^^^^^^^^^^^^^^^^

The RTEMS Souce Builder is designed to fit within most verification and
validation processes. All of the RTEMS Source Builder is source code. The
Python code is source and comes with a commercial friendly license. All
configuration data is text and can be read or parsed with standard text based
tools.

File naming provides configuration management. A specific version of a package
is captured in a specific set of configuration files. The top level
configuration file referenced in a *build set* or passed to the ``sb-builder``
command relates to a specific configuration of the package being built. For
example the RTEMS configuration file ``rtems-gcc-4.7.2-newlib-2.0.0-1.cfg``
creates an RTEMS GCC and Newlib package where the GCC version is 4.7.2, the
Newlib version is 2.0.0, plus any RTEMS specific patches that related to this
version. The configuration defines the version numbers of the various parts
that make up this package:

.. code-block:: spec

    %define gcc_version    4.7.2
    %define newlib_version 2.0.0
    %define mpfr_version   3.0.1
    %define mpc_version    0.8.2
    %define gmp_version    5.0.5

The package build options, if there are any are also defined:

.. code-block:: spec

    %define with_threads 1
    %define with_plugin  0
    %define with_iconv   1

The generic configuration may provide defaults in case options are not
specified. The patches this specific version of the package requires can be
included:

.. code-block:: spec

    Patch0: gcc-4.7.2-rtems4.11-20121026.diff

Finally including the GCC 4.7 configuration script:

.. code-block:: spec

    %include %{_configdir}/gcc-4.7-1.cfg

The ``gcc-4.7-1.cfg`` file is a generic script to build a GCC 4.7 compiler with
Newlib. It is not specific to RTEMS. A bare no operating system tool set can be
built with this file.

The ``-1`` part of the file names is a revision. The GCC 4.7 script maybe
revised to fix a problem and if this fix effects an existing script the file is
copied and given a ``-2`` revision number. Any dependent scripts referencing
the earlier revision number will not be effected by the change. This locks down
a specific configuration over time.

Personal Configurations
^^^^^^^^^^^^^^^^^^^^^^^

The RSB supports personal configurations. You can view the RTEMS support in the
``rtems`` directory as a private configuration tree that resides within the RSB
source. There is also the ``bare`` set of configurations. You can create your
own configurations away from the RSB source tree yet use all that the RSB
provides.

To create a private configuration change to a suitable directory:

.. code-block:: shell

    $ cd ~/work
    $ mkdir test
    $ cd test
    $ mkdir config

and create a ``config`` directory. Here you can add a new configuration or
build set file. The section 'Adding New Configurations' details how to add a
new confguration.

New Configurations
^^^^^^^^^^^^^^^^^^

This section describes how to add a new configuration to the RSB. We will add a
configuration to build the Device Tree Compiler. The Device Tree Compiler or
DTC is part of the Flattened Device Tree project and compiles Device Tree
Source (DTS) files into Device Tree Blobs (DTB). DTB files can be loaded by
operating systems and used to locate the various resources such as base
addresses of devices or interrupt numbers allocated to devices. The Device Tree
Compiler source code can be downloaded from http://www.jdl.com/software. The
DTC is supported in the RSB and you can find the configuration files under the
``bare/config`` tree. I suggest you have a brief look over these files.

Layering by Including
~~~~~~~~~~~~~~~~~~~~~

Configurations can be layered using the ``%include`` directive. The user
invokes the outer layers which include inner layers until all the required
configuration is present and the package can be built. The outer layers can
provide high level details such as the version and the release and the inner
layers provide generic configuration details that do not change from one
release to another. Macro variables are used to provide the specific
configuration details.

Configuration File Numbering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration files have a number at the end. This is a release number for that
configuration and it gives us the ability to track a specific configuration for
a specific version. For example lets say the developers of the DTC package
change the build system from a single makefile to autoconf and automake between
version 1.3.0 and version 1.4.0. The configuration file used to build the
package would change have to change. If we did not number the configuration
files the ability to build 1.1.0, 1.2.0 or 1.3.0 would be lost if we update a
common configuration file to build an autoconf and automake version. For
version 1.2.0 the same build script can be used so we can share the same
configuration file between version 1.1.0 and version 1.2.0. An update to any
previous release lets us still build the package.

Common Configuration Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common configuration scripts that are independent of version, platform and
architecture are useful to everyone. These live in the Source Builder's
configuration directory. Currently there are scripts to build binutils, expat,
DTC, GCC, GDB and libusb. These files contain the recipes to build these
package without the specific details of the versions or patches being
built. They expect to be wrapped by a configuration file that ties the package
to a specific version and optionally specific patches.

DTC Example
~~~~~~~~~~~

We will be building the DTC for your host rather than a package for RTEMS. We
will create a file called ``source-builder/config/dtc-1-1.cfg``. This is a
common script that can be used to build a specific version using a general
recipe. The file name is ``dtc-1-1.cfg`` where the ``cfg`` extension indicates
this is a configuration file. The first ``1`` says this is for the major
release 1 of the package and the last ``1`` is the build configuration version.

The file starts with some comments that detail the configuration. If there is
anything unusual about the configuration it is a good idea to add something in
the comments here. The comments are followed by a check for the release. In
this case if a release is not provided a default of 1 is used:

.. code-block:: spec

    #
    # DTC 1.x.x Version 1.
    #
    # This configuration file configure's, make's and install's DTC.
    #

    %if %{release} == %{nil}
    %define release 1
    %endif

The next section defines some information about the package. It does not effect
the build and is used to annotate the reports. It is recommended this
information is kept updated and accurate:

.. code-block:: spec

    Name:      dtc-%{dtc_version}-%{_host}-%{release}
    Summary:   Device Tree Compiler v%{dtc_version} for target %{_target} on host %{_host}
    Version:   %{dtc_version}
    Release:   %{release}
    URL: 	   http://www.jdl.com/software/
    BuildRoot: %{_tmppath}/%{name}-root-%(%{__id_u} -n)

The next section defines the source and any patches. In this case there is a
single source package and it can be downloaded using the HTTP protocol. The RSB
knows this is GZip'ped tar file. If more than one package is needed, add
them increasing the index. The ``gcc-4.8-1.cfg`` configuration contains
examples of more than one source package as well as conditionally including
source packages based on the outer configuration options:

.. code-block:: spec

    #
    # Source
    #
    %source set dtc http://www.jdl.com/software/dtc-v%{dtc_version}.tgz

The remainder of the script is broken in to the various phases of a build. They
are:

. Preperation
. Bulding
. Installing, and
. Cleaning

Preparation is the unpacking of the source, applying any patches as well as any
package specific set ups. This part of the script is a standard Unix shell
script. Be careful with the use of ``%`` and ``$``. The RSB uses ``%`` while
the shell scripts use ``$``.

A standard pattern you will observe is the saving of the build's top
directory. This is used instead of changing into a subdirectory and then
changing to the parent when finished. Some hosts will change in a subdirectory
that is a link however changing to the parent does not change back to the
parent of the link rather it changes to the parent of the target of the link
and that is something the RSB nor you can track easily. The RSB configuration
script's are a collection of various subtle issues so please ask if you are
unsure why something is being done a particular way.

The preparation phase will often include source and patch setup commands. Outer
layers can set the source package and add patches as needed while being able to
use a common recipe for the build. Users can override the standard build and
supply a custom patch for testing using the user macro command line interface:

.. code-block:: spec

    #
    # Prepare the source code.
    #
    %prep
      build_top=$(pwd)

      %source setup dtc -q -n dtc-v%{dtc_version}
      %patch setup dtc -p1

      cd ${build_top}

The configuration file ``gcc-common-1.cfg`` is a complex example of source
preparation. It contains a number of source packages and patches and it
combines these into a single source tree for building. It uses links to map
source into the GCC source tree so GCC can be built using the *single source
tree* method. It also shows how to fetch source code from version
control. Newlib is taken directly from its CVS repository.

Next is the building phase and for the DTC example this is simply a matter of
running ``make``. Note the use of the RSB macros for commands. In the case of
``%{__make}`` it maps to the correct make for your host. In the case of BSD
systems we need to use the BSD make and not the GNU make.

If your package requires a configuration stage you need to run this before the
make stage. Again the GCC common configuration file provides a detailed example:

.. code-block:: spec

    %build
      build_top=$(pwd)

      cd dtc-v%{dtc_version}

      %{build_build_flags}

      %{__make} PREFIX=%{_prefix}

      cd ${build_top}

You can invoke make with the macro ``%{?_smp_flags}`` as a command line
argument. This macro is controlled by the ``--jobs`` command line option and
the host CPU detection support in the RSB. If you are on a multicore host you
can increase the build speed using this macro. It also lets you disabled
building on multicores to aid debugging when testing.

Next is the install phase. This phase is a little more complex because you may
be building a tar file and the end result of the build is never actually
installed into the prefix on the build host and you may not even have
permissions to perform a real install. Most packages install to the ``prefix``
and the prefix is typically supplied via the command to the RSB or the
package's default is used. The default can vary depending on the host's
operating system. To install to a path that is not the prefix the ``DESTDIR`` 
make variable is used. Most packages should honour the ``DISTDIR`` make
variables and you can typically specify it on the command line to make when
invoking the install target. This results in the package being installed to a
location that is not the prefix but one you can control. The RSB provides a
shell variable called ``SB_BUILD_ROOT`` you can use. In a build set where you
are building a number of packages you can collect all the built packages in a
single tree that is captured in the tar file.

Also note the use of the macro ``%{__rmdir}``. The use of these macros allow
the RSB to vary specific commands based on the host. This can help on hosts
like Windows where bugs can effect the standard commands such as ``rm``. There
are many many macros to help you. You can find these listed in the
``defaults.mc`` file and in the trace output. If you are new to creating and
editing configurations learning these can take a little time:

.. code-block:: spec

    %install
      build_top=$(pwd)

      %{__rmdir} -rf $SB_BUILD_ROOT

      cd dtc-v%{dtc_version}
      %{__make} DESTDIR=$SB_BUILD_ROOT PREFIX=%{_prefix} install

      cd ${build_top}

Finally there is an optional clean section. The RSB will run this section if
``--no-clean`` has not been provided on the command line. The RSB does clean up
for you.

Once we have the configuration files we can execute the build using the
``sb-builder`` command. The command will perform the build and create a tar file
in the ``tar`` directory:

.. code-block:: shell

    $  ../source-builder/sb-builder --prefix=/usr/local \
         --log=log_dtc devel/dtc-1.2.0
    RTEMS Source Builder, Package Builder v0.2.0
    config: devel/dtc-1.2.0
    package: dtc-1.2.0-x86_64-freebsd9.1-1
    download: http://www.jdl.com/software/dtc-v1.2.0.tgz -> sources/dtc-v1.2.0.tgz
    building: dtc-1.2.0-x86_64-freebsd9.1-1
    $ ls tar
    dtc-1.2.0-x86_64-freebsd9.1-1.tar.bz2

If you want to have the package installed automatically you need to create a
build set. A build set can build one or more packages from their configurations
at once to create a single package. For example the GNU tools is typically seen
as binutils, GCC and GDB and a build set will build each of these packages and
create a single build set tar file or install the tools on the host into the
prefix path.

The DTC build set file is called ``dtc.bset`` and contains:

.. code-block:: spec

    #
    # Build the DTC.
    #

    %define release 1

    devel/dtc-1.2.0.cfg

To build this you can use something similar to:

.. code-block:: shell

    $ ../source-builder/sb-set-builder --prefix=/usr/local --log=log_dtc \
       --trace --bset-tar-file --no-install dtc
    RTEMS Source Builder - Set Builder, v0.2.0
    Build Set: dtc
    config: devel/dtc-1.2.0.cfg
    package: dtc-1.2.0-x86_64-freebsd9.1-1
    building: dtc-1.2.0-x86_64-freebsd9.1-1
    tarball: tar/x86_64-freebsd9.1-dtc-set.tar.bz2
    cleaning: dtc-1.2.0-x86_64-freebsd9.1-1
    Build Set: Time 0:00:02.865758
    $ ls tar
    dtc-1.2.0-x86_64-freebsd9.1-1.tar.bz2   x86_64-freebsd9.1-dtc-set.tar.bz2

The build is for a FreeBSD host and the prefix is for user installed
packages. In this example I cannot let the source builder perform the install
because I never run the RSB with root priviledges so a build set or bset tar
file is created. This can then be installed using root priviledges.

The command also supplies the ``--trace`` option. The output in the log file
will contain all the macros.

Debugging
~~~~~~~~~

New configuration files require debugging. There are two types of
debugging. The first is debugging RSB script bugs. The ``--dry-run`` option is
used here. Suppling this option will result in most of the RSB processing to be
performed and suitable output placed in the log file. This with the ``--trace``
option should help you resolve any issues.

The second type of bug to fix are related to the execution of one of
phases. These are usually a mix of shell script bugs or package set up or
configuration bugs. Here you can use any normal shell script type debug
technique such as ``set +x`` to output the commands or ``echo``
statements. Debugging package related issues may require you start a build with
the RSB and supply ``--no-clean`` option and then locate the build directories
and change directory into them and manually run commands until to figure what
the package requires.

Scripting
^^^^^^^^^

Configuration files specify how to build a package. Configuration files are
scripts and have a ``.cfg`` file extension. The script format is based loosely
on the RPM spec file format however the use and purpose in this tool does not
compare with the functionality and therefore the important features of the spec
format RPM needs and uses.

The script language is implemented in terms of macros. The built-in list is:

``%{}``:
  Macro expansion with conditional logic.

``%()``:
  Shell expansion.

``%prep``:
  The source preparation shell commands.

``%build``:
  The build shell commands.

``%install``:
  The package install shell commands.

``%clean``:
  The package clean shell commands.

``%include``:
  Inline include another configuration file.

``%name``:
  The name of the package.

``%summary``:
  A brief package description. Useful when reporting about a build.

``%release``:
  The package release. A number that is the release as built by this tool.

``%version``:
  The package's version string.

``%buildarch``:
  The build architecture.

``%source``:
  Define a source code package. This macro has a number appended.

``%patch``:
  Define a patch. This macro has a number appended.

``%hash``:
  Define a checksum for a source or patch file.

``%echo``:
  Print the following string as a message.

``%warning``:
  Print the following string as a warning and continue.

``%error``:
  Print the following string as an error and exit.

``%select``:
  Select the macro map. If there is no map nothing is reported.

``%define``:
  Define a macro. Macros cannot be redefined, you must first undefine it.

``%undefine``:
  Undefine a macro.

``%if``:
  Start a conditional logic block that ends with a ``%endif``.

``%ifn``:
  Inverted start of a conditional logic block.

``%ifarch``:
  Test the architecture against the following string.

``%ifnarch``:
  Inverted test of the architecture

``%ifos``:
  Test the host operating system.

``%else``:
  Start the *else* conditional logic block.

``%endfi``:
  End the conditional logic block.

``%bconf_with``:
  Test the build condition *with* setting. This is the ``--with-*`` command
  line option.

``%bconf_without``:
  Test the build condition *without* setting. This is the ``--without-*``
  command line option.

Expanding
~~~~~~~~~

A macro can be ``%{string}`` or the equivalent of ``%string``. The following macro
expansions supported are:

``%{string}``:
  Expand the 'string' replacing the entire macro text with the text in the
  table for the entry 'string . For example if 'var' is 'foo' then ``${var}``
  would become ``foo``.

``%{expand: string}``:
  Expand the 'string' and then use it as a ``string`` to the macro expanding
  the macro. For example if ``foo`` is set to ``bar`` and ``bar`` is set to
  ``foobar`` then ``%{expand:foo}`` would result in ``foobar``. Shell expansion
  can also be used.

``%{with string}``:
  Expand the macro to ``1`` if the macro ``with_string`` is defined else expand
  to ``0``. Macros with the name ``with_string`` can be define with command
  line arguments to the RTEMS Source Builder commands.

``%{defined string}``:
  Expand the macro to ``1`` if a macro of name ``string`` is defined else
  expand to '0'.

``%{?string: expression}``:
  Expand the macro to ``expression`` if a macro of name ``string`` is defined
  else expand to ``%{nil}``.

``%{!?string: expression}``:
  Expand the macro to ``expression`` if a macro of name ``string`` is not
  defined. If the macro is define expand to ``%{nil}``.

``%(expression)``:
  Expand the macro to the result of running the ``expression`` in a host
  shell. It is assumed this is a Unix type shell. For example ``%(whoami)``
  will return your user name and ``%(date)`` will return the current date
  string.

.. _prep:

%prep
~~~~~

The +%prep+ macro starts a block that continues until the next block macro. The
*prep* or preparation block defines the setup of the package's source and is a
mix of RTEMS Source Builder macros and shell scripting. The sequence is
typically +%source+ macros for source, +%patch+ macros to patch the source
mixed with some shell commands to correct any source issues:

.. code-block:: spec

    %source setup gcc -q -c -T -n %{name}-%{version}

.. topic:: Items:

  1. The source group to set up is ``gcc``.

  2. The source's name is the macro ``%{name}``.

  3. The version of the source is the macro ``%{version}``.

The source set up are declared with the source ``set`` and ``add`` commands. For
example:

.. code-block:: spec

    %source set gdb http://ftp.gnu.org/gnu/gdb/gdb-%{gdb_version}.tar.bz2

This URL is the primary location of the GNU GDB source code and the RTEMS
Source Builder can download the file from this location and by inspecting the
file extension use ``bzip2`` decompression with +tar+. When the ``%prep``
section is processed a check of the local ``source`` directory is made to see
if the file has already been downloaded. If not found in the source cache
directory the package is downloaded from the URL. You can append other base
URLs via the command line option ``--url``. This option accepts a comma
delimited list of sites to try.

You could optionally have a few source files that make up the package. For
example GNU's GCC was a few tar files for a while and it is now a single tar
file. Support for multiple source files can be conditionally implemented with
the following scripting:

.. code-block:: spec

    %source set gcc ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-code-%{gcc_version}.tar.bz2
    %source add gcc ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-g++-%{gcc_version}.tar.bz2
    %source setup gcc -q -T -D -n gcc-%{gcc_version}

Separate modules use separate source groups. The GNU GCC compiler for RTEMS
uses Newlib, MPFR, MPC, and GMP source packages. You define the source with:

.. code-block:: spec

    %source set gcc ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.bz2
    %source set newlib ftp://sourceware.org/pub/newlib/newlib-%{newlib_version}.tar.gz
    %source set mpfr http://www.mpfr.org/mpfr-%{mpfr_version}/mpfr-%{mpfr_version}.tar.bz2
    %source set mpc http://www.multiprecision.org/mpc/download/mpc-%{mpc_version}.tar.gz
    %source set gmp ftp://ftp.gnu.org/gnu/gmp/gmp-%{gmp_version}.tar.bz2

and set up with:

.. code-block:: spec

    %source setup gcc -q -n gcc-%{gcc_version}
    %source setup newlib -q -D -n newlib-%{newlib_version}
    %source setup mpfr -q -D -n mpfr-%{mpfr_version}
    %source setup mpc -q -D -n mpc-%{mpc_version}
    %source setup gmp -q -D -n gmp-%{gmp_version}

Patching also occurs during the preparation stage. Patches are handled in a
similar way to the source packages except you only ``add`` patches. Patches are
applied using the +setup+ command. The +setup+ command takes the default patch
option. You can provide options with each patch by adding them as arguments
before the patch URL. Patches with no options uses the +setup+ default.

.. code-block:: spec

    %patch add gdb %{rtems_gdb_patches}/gdb-sim-arange-inline.diff
    %patch add gdb -p0 %{rtems_gdb_patches}/gdb-sim-cgen-inline.diff

.. topic:: Items:

  1. This patch has the custom option of ``-p0``.

To apply these patches:

.. code-block:: spec

    %patch setup gdb -p1

.. topic:: Items:

  1. The default options for ``gdb`` set up.

.. _build:

%build
~~~~~~

The ``%build`` macro starts a block that continues until the next block
macro. The build block is a series of shell commands that execute to build the
package. It assumes all source code has been unpacked, patch and adjusted so
the build will succeed.

The following is an example take from the GitHub STLink project. The STLink is
a JTAG debugging device for the ST ARM family of processors:

.. code-block:: spec

    %build
      export PATH="%{_bindir}:${PATH}"

      cd texane-stlink-%{stlink_version}

      ./autogen.sh

    %if "%{_build}" != "%{_host}"
      CFLAGS_FOR_BUILD="-g -O2 -Wall" \
    %endif
      CPPFLAGS="-I $SB_TMPPREFIX/include/libusb-1.0" \
      CFLAGS="$SB_OPT_FLAGS" \
      LDFLAGS="-L $SB_TMPPREFIX/lib" \
      ./configure \
        --build=%{_build} --host=%{_host} \
        --verbose \
        --prefix=%{_prefix} --bindir=%{_bindir} \
        --exec-prefix=%{_exec_prefix} \
        --includedir=%{_includedir} --libdir=%{_libdir} \
        --mandir=%{_mandir} --infodir=%{_infodir}

      %{__make} %{?_smp_mflags} all

      cd ..

.. topic:: Items:

  1. Set up the PATH environment variable by setting the ``PATH`` environment
     variable. This is not always needed.

  2. This package builds in the source tree
     ``texane-stlink-%{stlink_version}`` so enter it before building.

  3. The package is actually checked directly out from the github project and
     so it needs its ``autoconf`` and ``automake`` files generated. Invoke the
     provided script ``autogen.sh``

  4. If the build machine and host are not the same the build is a
     cross-compile. Update the flags for a cross-compiled build.

  5. The flags set in the environment before ``configure`` are various
     settings that need to be passed to customise the build. In this example
     an include path is being set to the install point of ``libusb``. This
     package requires ``libusb`` is built before it.

  6. The ``configure`` command. The RTEMS Source Builder provides all the
     needed paths as macro variables. You just need to provide them to
     ``configure``.

  7. Run ``make``. Do not use ``make`` directly, use the RTEMS Source
     Builder's defined value. This value is specific to the host. A large
     number of packages need GNU make and on BSD systems this is
     ``gmake``. You can optionally add the SMP flags if the packages build
     system can handle parallel building with multiple jobs. The
     ``_smp_mflags`` value is automatically setup for SMP hosts to match the
     number of cores the host has.

%install
~~~~~~~~

The ``%install`` macro starts a block that continues until the next block
macro. The install block is a series of shell commands that execute to install
the package. You can assume the package has built correctly when this block
starts executing.

Never install the package to the actual *prefix* the package was built
with. Always install to the RTEMS Source Builder's temporary path defined in
the macro variable ``__tmpdir``. The RTEMS Source Builder sets up a shell
environment variable called ``SB_BUILD_ROOT`` as the standard install point. Most
packages support adding ``DESTDIR=`` to the ``make install`` command.

Looking at the same example as in :ref:`build`:

.. code-block:: spec

    %install
      export PATH="%{_bindir}:${PATH}" <1>
      rm -rf $SB_BUILD_ROOT <2>

      cd texane-stlink-%{stlink_version} <3>
      %{__make} DESTDIR=$SB_BUILD_ROOT install <4>

      cd ..

.. topic:: Items:

  1. Setup the PATH environment variable. This is not always needed.

  2. Clean any installed files. This makes sure the install is just what the
     package installs and not any left over files from a broken build or
     install.

  3. Enter the build directory. In this example it just happens to be the
     source directory.

  4. Run ``make install`` to install the package overriding the ``DESTDIR``
     make variable.

%clean
~~~~~~

The ``%clean`` macro starts a block that continues until the next block
macro. The clean block is a series of shell commands that execute to clean up
after a package has been built and install. This macro is currenly not been
used because the RTEMS Source Builder automatically cleans up.

%include
~~~~~~~~

The ``%include`` macro inline includes the specific file. The ``__confdir``
path is searched. Any relative path component of the include file is appended
to each part of the ``__configdir``. Adding an extension is optional as files
with ``.bset`` and ``.cfg`` are automatically searched for.

Inline including means the file is processed as part of the configuration at
the point it is included. Parsing continues from the next line in the
configuration file that contains the ``%include`` macro.

Including files allow a kind of configuration file reuse. The outer
configuration files provide specific information such as package version
numbers and patches and then include a generic configuration script which
builds the package:

.. code-block:: spec

    %include %{_configdir}/gcc-4.7-1.cfg

%name
~~~~~

The name of the package being built. The name typically contains the components
of the package and their version number plus a revision number. For the GCC
with Newlib configuration the name is typically::

    Name: %{_target}-gcc-%{gcc_version}-newlib-%{newlib_version}-%{release}

%summary
~~~~~~~~

The ``%summary`` is a brief description of the package. It is useful when
reporting. This information is not capture in the package anywhere. For the GCC
with Newlib configuration the summary is typically:

.. code-block:: spec

    Summary: GCC v%{gcc_version} and Newlib v%{newlib_version} for target %{_target} on host %{_host}

%release
~~~~~~~~

The ``%release`` is a packaging number that allows revisions of a package to
happen where no package versions change. This value typically increases when
the configuration building the package changes:

.. code-block:: spec

    %define release 1

%version
~~~~~~~~

The ``%version`` macro sets the version the package. If the package is a single
component it tracks that component's version number. For example in the
``libusb`` configuration the ``%version`` is the same as ``%libusb_version``,
however in a GCC with Newlib configuration there is no single version
number. In this case the GCC version is used:

.. code-block:: spec

    Version: %{gcc_version}

%buildarch
~~~~~~~~~~

The ``%buildarch`` macro is set to the architecture the package contains. This
is currently not used in the RTEMS Source Builder and may go away. This macro
is more important in a real packaging system where the package could end up on
the wrong architecture.

%source
~~~~~~~

The ``%source`` macro has 3 commands that controls what it does. You can
``set`` the source files, ``add`` source files to a source group, and ``setup``
the source file group getting it ready to be used.

Source files are source code files in tar or zip files that are unpacked,
copied or symbolically linked into the package's build tree. Building a package
requires one or more dependent packages. These are typically the packages
source code plus dependent libraries or modules. You can create any number of
these source groups and set each of them up with a separate source group for
each needed library or module. Each source group normally has a single tar, zip
or repository and the ``set`` defines this. Some projects split the source code
into separate tar or zip files and you install them by using the ``add``
command.

The first instance of a ``set`` command creates the source group and sets the
source files to be set up. Subsequent ``set`` commands for the same source
group are ignored. this lets you define the standard source files and override
them for specific releases or snapshots. To set a source file group:

.. code-block:: spec

    %source set gcc ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.bz2

.. topic:: Items:

  1. The source group is ``gcc``.

To add another source package to be installed into the same source tree you use
the ``add`` command:

.. code-block:: spec

    %source add gcc ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/g++-%{gcc_version}.tar.bz2

The source ``setup`` command can only be issued in the ``%prep:`` section. The
setup is:

.. code-block:: spec

    %source gcc setup -q -T -D -n %{name}-%{version}

Accepted options are:

``-n``:
  The ``-n`` option is used to set the name of the software's build
  directory. This is necessary only when the source archive unpacks into a
  directory named other than ``<name>-<version>``.

``-c``:
  The ``-c`` option is used to direct ``%setup`` to create the top-level build
  directory before unpacking the sources.

``-D``:
  The ``-D`` option is used to direct ``%setup`` to not delete the build
  directory prior to unpacking the sources. This option is used when more than
  one source archive is to be unpacked into the build directory, normally with
  the ``-b`` or ``-a`` options.

``-T``:
   The ``-T`` option is used to direct %setup to not perform the default
   unpacking of the source archive specified by the first ``Source:`` macro. It
   is used with the ``-a`` or ``-b`` options.

``-b <n>``:
  The ``-b`` option is used to direct ``%setup`` to unpack the source archive
  specified on the nth ``Source:`` macro line before changing directory into
  the build directory.

%patch
~~~~~~

The ``%patch`` macro has the same 3 command as the ``%source`` command however
the ``set`` commands is not really that useful with the ``%patch`` command. You
add patches with the ``add`` command and ``setup`` applies the patches. Patch
options can be added to each patch by placing them before the patch URL. If no
patch option is provided the default options passed to the ``setup`` command
are used. An option starts with a ``-``. The ``setup`` command must reside
inside the ``%prep`` section.

Patches are grouped in a similar way to the ``%source`` macro so you can
control applying a group of patches to a specific source tree.

The ``__patchdir`` path is searched.

To add a patch:

.. code-block:: spec

    %patch add gcc  gcc-4.7.2-rtems4.11-20121026.diff
    %patch add gcc -p0  gcc-4.7.2-rtems4.11-20121101.diff

.. topic:: Items:

  1. The patch group is ``gcc``.

  2. Option ``-p0`` is this specific to this patch.

Placing ``%patch setup`` in the ``%prep`` section will apply the groups
patches::

.. code-block:: spec

    %patch setup gcc  -p1

  1. The patch group is ``gcc``.

  2. The default option used to apply the patch is ``-p1``.

%hash
~~~~~

The ``%hash`` macro requires 3 arguments and defines a checksum for a specific
file. The checksum is not applied until the file is checked before downloading
and once downloaded. A patch or source file that does not have a hash defined
generates a warning.

A file to be checksummed must be unique in the source and patch directories.
The basename of the file is used as the key for the hash.

The hash algorthim can be ``md5``, ``sha1``, ``sha224``, ``sha256``,
``sha384``, and ``sha512`` and we typically use ``md5``.

To add a hash:

.. code-block:: spec

    %hash md5 <1> net-snmp-%{net_snmp_version}.tar.gz <2> 7db683faba037249837b226f64d566d4 <3>

.. topic:: Items:

  1. The type of checksum.

  2. The file to checksum. It can contain macros that are expanded for you.

  3. The MD5 hash for the Net-SNMP file ``net-snmp-5.7.2.1.tar.gz``.

Do not include a path with the file name. Only the basename is required. Files
can be searched for from a number of places and having a path conponent would
create confusion. This does mean files with hashes must be unique.

Downloading off repositories such as git and cvs cannot be checksummed. It is
assumed those protocols and tools manage the state of the files.

%echo
~~~~~

The ``%echo`` macro outputs the following string to stdout. This can also be used
as ``%{echo: message}``.

%warning
~~~~~~~~

The ``%warning`` macro outputs the following string as a warning. This can also
be used as ``%{warning: message}``.

%error
~~~~~~

The ``%error`` macro outputs the follow string as an error and exits the RTEMS
Source Builder. This can also be used as ``%{error: message}``.

%select
~~~~~~~

The ``%select`` macro selects the map specified. If there is no map no error or
warning is generated. Macro maps provide a simple way for a user to override
the settings in a configuration file without having to edit it. The changes are
recorded in the build report so they can be traced.

Configurations use different maps so macro overrides can target a specific
package.

The default map is ``global``:

.. code-block:: spec

    %select gcc-4.8-snapshot <1>
    %define one_plus_one 2 <2>

.. topic:: Items:

  1. The map switches to ``gcc-4.8-snapshot``. Any overrides in this map will
     be used.

  2. Defining macros only updates the ``global`` map and not the selected map.

%define
~~~~~~~

The ``%define`` macro defines a new macro or updates an existing one. If no
value is given it is assumed to be ``1``:

.. code-block:: spec

    %define foo bar
    %define one_plus_one 2
    %define one <1>

.. topic:: Items:

  1. The macro _one_ is set to 1.

%undefine
~~~~~~~~~

The ``%undefine`` macro removes a macro if it exists. Any further references to
it will result in an undefine macro error.

%if
~~~

The ``%if`` macro starts a conditional logic block that can optionally have a
*else* section. A test follows this macro and can have the following operators:

.. list-table::

  * - **%{}**
    - Check the macro is set or *true*, ie non-zero:

      .. code-block:: spec

         %if ${foo}
          %warning The test passes, must not be empty or is non-zero
         %else
          %error The test fails, must be empty or zero
         %endif

  * - **\!**
    - The *not* operator inverts the test of the macro:

      .. code-block:: spec

         %if ! ${foo}
          %warning The test passes, must be empty or zero
         %else
          %error The test fails, must not be empty or is non-zero
         %endif

  * - **==**
    - The left hand size must equal the right hand side. For example:

      .. code-block:: spec

         %define one 1
         %if ${one} == 1
          %warning The test passes
         %else
          %error The test fails
         %endif

      You can also check to see if a macro is empty:

      .. code-block:: spec

         %if ${nothing} == %{nil}
          %warning The test passes
         %else
          %error The test fails

  * - **!=**
    - The left hand size does not equal the right hand side. For example:

      .. code-block:: spec

         #
         # Check a value not being equal.
         #
         %define one 1
         %if ${one} != 2
          %warning The test passes
         %else
          %error The test fails
         %endif
         #
         # Check if a macro is set.
         #
         %if ${something} != %{nil}
           %warning The test passes
         %else
          %error The test fails
         %endif

  * - **>**
    - The left hand side is numerically greater than the right hand side.

  * - **>**
    - The left hand side is numerically greater than or equal to the
      right hand side.

  * - **<**
    - The left hand side is numerically less than the right hand side.

  * - **<=**
    - The left hand side is numerically less than or equal to the
      right hand side.

%ifn
~~~~

The ``%ifn`` macro inverts the normal ``%if`` logic. It avoids needing to provide
empty *if* blocks followed by *else* blocks. It is useful when checking if a
macro is defined:

.. code-block:: spec

    %ifn %{defined foo}
     %define foo bar
    %endif

%ifarch
~~~~~~~

The ``%ifarch`` is a short cut for ``%if %{_arch} == i386``. Currently not used.

%ifnarch
~~~~~~~~

The ``%ifnarch`` is a short cut for ``%if %{_arch} != i386``. Currently not
used.

%ifos
~~~~~

The ``%ifos`` is a short cut for ``%if %{_os} != mingw32``. It allows
conditional support for various operating system differences when building
packages.

%else
~~~~~

The ``%else`` macro starts the conditional *else* block.

%endfi
~~~~~~

The ``%endif`` macro ends a conditional logic block.

%bconf_with
~~~~~~~~~~~

The ``%bconf_with`` macro provides a way to test if the user has passed a
specific option on the command line with the ``--with-<label>`` option. This
option is only available with the ``sb-builder`` command.

%bconf_without
~~~~~~~~~~~~~~

The ``%bconf_without`` macro provides a way to test if the user has passed a
specific option on the command line with the ``--without-<label>`` option. This
option is only available with the ``sb-builder`` command.
