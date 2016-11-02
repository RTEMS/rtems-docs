.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment COPYRIGHT (c) 2012 - 2016.
.. comment Chris Johns <chrisj@rtems.org>

Quick Start
###########

The quick start will show you how to build a set of RTEMS tools for a supported
architecture. The tools are installed into a build *prefix*. The *prefix* is the
top of a group of directories containing all the files needed to develop RTEMS
applications. Building an RTEMS build set will build all that you need. This
includes autoconf, automake, assemblers, linkers, compilers, debuggers,
standard libraries and RTEMS itself.

There is no need to become root or the administrator and we recommend you
avoid doing this. You can build and install the tools anywhere on the
host's file system you, as a standard user, have read and write access
too. I recommend you use your home directory and work under the directory
``~/development/rtems``. The examples shown here will do this.

You can use the build *prefix* to install and maintain different versions of
the tools. Doing this lets you try a new set of tools while not touching your
proven working production set of tools. Once you have proven the new tools are
working rebuild with the *production* prefix switching your development to them.

We recommend you keep your environment to the bare minimum, particularly the
path variable. Using environment variables has been proven over the years to be
difficult to manage in production systems.

.. warning::

    The RSB assumes your host is set up and the needed packages are installed
    and configured to work. If your host has not been set up please refer to
    :ref:`Hosts` and your host's section for packages you need to install.

.. topic:: Path to use when building applications:

    Do not forget to set the path before you use the tools, for example to
    build the RTEMS kernel.

    The RSB by default will install (copy) the executables to a directory tree
    under the *prefix* you supply. To use the tools once finished just set your
    path to the ``bin`` directory under the *prefix* you use. In the examples
    that follow the *prefix* is ``$HOME/development/rtems/4.11`` and is set
    using the ``--prefix`` option so the path you need to configure to build
    applications can be set with the following in a BASH shell:

    .. code-block:: shell

      $ export PATH=$HOME/development/rtems/4.11/bin:$PATH

    Make sure you place the RTEMS tool path at the front of your path so they
    are searched first. RTEMS can provide newer versions of some tools your
    operating system provides and placing the RTEMS tools path at the front
    means it is searched first and the RTEMS needed versions of the tools are
    used.

.. note::

    RSB and RTEMS have a matching *git branch* for each version of RTEMS. For
    example, if you want to build a toolchain for 4.11, then you should
    checkout the 4.11 branch of the RSB:

    .. code-block:: shell

      $ git checkout -t origin/4.11

    Branches are available for the 4.9, 4.10, and 4.11 versions of RTEMS.

Setup
~~~~~

Setup a development work space::

    $ cd
    $ mkdir -p development/rtems/src
    $ cd development/rtems/src

The RTEMS Source Builder is distributed as source. It is Python code so all you
need to do is download the release's RSB tarball or clone the code directly
from the RTEMS GIT repository::

    $ git clone git://git.rtems.org/rtems-source-builder.git
    $ cd rtems-source-builder

.. topic:: Workspaces

   The examples in the *Quick Start Guide* build and install tools in your
   *home* directory. Please refer to the RTEMS User Manual for more detail
   about *Sandboxing* and the *prefix*.

Checking
~~~~~~~~

The next step is to check if your host is set up correctly. The RTEMS Source
Builder provides a tool to help::

    $ source-builder/sb-check
    warning: exe: absolute exe found in path: (__objcopy) /usr/local/bin/objcopy <1>
    warning: exe: absolute exe found in path: (__objdump) /usr/local/bin/objdump
    error: exe: not found: (_xz) /usr/local/bin/xz    <2>
    RTEMS Source Builder environment is not correctly set up
    $ source-builder/sb-check
    RTEMS Source Builder environment is ok   <3>

.. topic:: Items:

  1. A tool is in the environment path but it does not match the expected path.

  2. The executable ``xz`` is not found.

  3. The host's environment is set up correct.

The checking tool will output a list of executable files not found if problems
are detected. Locate those executable files and install them. You may also be
given a list of warnings about executable files not in the expected location
however the executable was located somewhere in your environment's path. You
will need to check each tool to determine if this is an issue. An executable
not in the standard location may indicate it is not the host operating system's
standard tool. It maybe ok or it could be buggy, only you can determine this.

The :ref:`Hosts` section lists packages you should install for common host
operating systems. It maybe worth checking if you have those installed.

Build Sets
~~~~~~~~~~

The RTEMS tools can be built within the RTEMS Source Builder's source tree. We
recommend you do this so lets change into the RTEMS directory in the RTEMS
Source Builder package::

    $ cd rtems

If you are unsure how to specify the build set for the architecture you wish to
build ask the tool::

    $ ../source-builder/sb-set-builder --list-bsets   <1>
    RTEMS Source Builder - Set Builder, v4.11.0
    Examining: config
    Examining: ../source-builder/config    <2>
        4.10/rtems-all.bset      <3>
        4.10/rtems-arm.bset      <4>
        4.10/rtems-autotools.bset
        4.10/rtems-avr.bset
        4.10/rtems-bfin.bset
        4.10/rtems-h8300.bset
        4.10/rtems-i386.bset
        4.10/rtems-lm32.bset
        4.10/rtems-m32c.bset
        4.10/rtems-m32r.bset
        4.10/rtems-m68k.bset
        4.10/rtems-mips.bset
        4.10/rtems-nios2.bset
        4.10/rtems-powerpc.bset
        4.10/rtems-sh.bset
        4.10/rtems-sparc.bset
        4.11/rtems-all.bset
        4.11/rtems-arm.bset
        4.11/rtems-autotools.bset
        4.11/rtems-avr.bset
        4.11/rtems-bfin.bset
        4.11/rtems-h8300.bset
        4.11/rtems-i386.bset
        4.11/rtems-lm32.bset
        4.11/rtems-m32c.bset
        4.11/rtems-m32r.bset
        4.11/rtems-m68k.bset
        4.11/rtems-microblaze.bset
        4.11/rtems-mips.bset
        4.11/rtems-moxie.bset
        4.11/rtems-nios2.bset
        4.11/rtems-powerpc.bset
        4.11/rtems-sh.bset
        4.11/rtems-sparc.bset
        4.11/rtems-sparc64.bset
        4.11/rtems-v850.bset
        4.9/rtems-all.bset
        4.9/rtems-arm.bset
        4.9/rtems-autotools.bset
        4.9/rtems-i386.bset
        4.9/rtems-m68k.bset
        4.9/rtems-mips.bset
        4.9/rtems-powerpc.bset
        4.9/rtems-sparc.bset
        gnu-tools-4.6.bset
        rtems-4.10-base.bset    <5>
        rtems-4.11-base.bset
        rtems-4.9-base.bset
        rtems-base.bset         <5>

.. topic:: Items:

  1. Only option required is ``--list-bsets``

  2. The paths inspected. See :ref:`Configuration`.

  3. A build set to build all RTEMS 4.10 supported architectures.

  4. The build set for the ARM architecture on RTEMS 4.10.

  5. Support build set file with common functionality included by other build
     set files.

Building
~~~~~~~~

The quick start builds a SPARC tool set::

    $ ../source-builder/sb-set-builder --log=l-sparc.txt \   <1>
          --prefix=$HOME/development/rtems/4.11 \       <2>
          4.11/rtems-sparc           <3>
    Source Builder - Set Builder, v0.2.0
    Build Set: 4.11/rtems-sparc
    config: expat-2.1.0-1.cfg        <4>
    package: expat-2.1.0-x86_64-freebsd9.1-1
    building: expat-2.1.0-x86_64-freebsd9.1-1
    config: tools/rtems-binutils-2.22-1.cfg        <5>
    package: sparc-rtems4.11-binutils-2.22-1
    building: sparc-rtems4.11-binutils-2.22-1
    config: tools/rtems-gcc-4.7.2-newlib-1.20.0-1.cfg   <6>
    package: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    building: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    config: tools/rtems-gdb-7.5.1-1.cfg      <7>
    package: sparc-rtems4.11-gdb-7.5.1-1
    building: sparc-rtems4.11-gdb-7.5.1-1
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11 <8>
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11
    cleaning: expat-2.1.0-x86_64-freebsd9.1-1     <9>
    cleaning: sparc-rtems4.11-binutils-2.22-1
    cleaning: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    cleaning: sparc-rtems4.11-gdb-7.5.1-1
    Build Set: Time 0:13:43.616383        <10>

.. topic:: Items

  1. Providing a log file redirects the build output into a file. Logging the
     build output provides a simple way to report problems.

  2. The prefix is the location on your file system the tools are installed
     into. Provide a prefix to a location you have read and write access. You
     can use the prefix to install different versions or builds of tools. Just
     use the path to the tools you want to use when building RTEMS.

  3. The build set. This is the SPARC build set. First a specifically
     referenced file is checked for and if not found the ``%{_configdir}`` path
     is searched. The set builder will first look for files with a ``.bset``
     extension and then for a configuration file with a ``.cfg`` extension.

  4. The SPARC build set first builds the expat library as it is used in GDB.
     This is the expat configuration used.

  5. The binutils build configuration.

  6. The GCC and Newlib build configuration.

  7. The GDB build configuration.

  8. Installing the built packages to the install prefix.

  9. All the packages built are cleaned at the end. If the build fails all the
     needed files are present. You may have to clean up by deleting the build
     directory if the build fails.

  10. The time to build the package. This lets you see how different host
      hardware or configurations perform.

Your SPARC RTEMS 4.11 tool set will be installed and ready to build RTEMS and
RTEMS applications. When the build runs you will notice the tool fetch the
source code from the internet. These files are cached in directies called
``source`` and ``patches``. If you run the build again the cached files are
used. This is what happened in the shown example. Archiving these directories
archives the source you need to recreate the build.

.. topic:: RTEMS Releases

  The RSB found in a release will automatically build and install RTEMS. If you
  do not want a released version of the RSB to build RTEMS add
  ``--without-rtems`` to the command line. The development version requires
  adding ``--with-rtems`` to build RTEMS. Use this option to create a single
  command to build the tools and RTEMS.

  The source used in release builds is downloaded from the RTEMS FTP
  server. This ensures the source is always available for a release.

The installed tools::

    $ ls $HOME/development/rtems/4.11
    bin         include     lib         libexec     share       sparc-rtems4.11
    $ ls $HOME/development/rtems/4.11/bin
    sparc-rtems4.11-addr2line       sparc-rtems4.11-cpp
    sparc-rtems4.11-gcc-ar          sparc-rtems4.11-gprof
    sparc-rtems4.11-objdump         sparc-rtems4.11-size
    sparc-rtems4.11-ar              sparc-rtems4.11-elfedit
    sparc-rtems4.11-gcc-nm          sparc-rtems4.11-ld
    sparc-rtems4.11-ranlib          sparc-rtems4.11-strings
    sparc-rtems4.11-as              sparc-rtems4.11-g++
    sparc-rtems4.11-gcc-ranlib      sparc-rtems4.11-ld.bfd
    sparc-rtems4.11-readelf         sparc-rtems4.11-strip
    sparc-rtems4.11-c++             sparc-rtems4.11-gcc
    sparc-rtems4.11-gcov            sparc-rtems4.11-nm
    sparc-rtems4.11-run             xmlwf
    sparc-rtems4.11-c++filt         sparc-rtems4.11-gcc-4.7.2
    sparc-rtems4.11-gdb             sparc-rtems4.11-objcopy
    sparc-rtems4.11-sis
    $ $HOME/development/rtems/4.11/bin/sparc-rtems4.11-gcc -v
    Using built-in specs.
    COLLECT_GCC=/home/chris/development/rtems/4.11/bin/sparc-rtems4.11-gcc
    COLLECT_LTO_WRAPPER=/usr/home/chris/development/rtems/4.11/bin/../ \
    libexec/gcc/sparc-rtems4.11/4.7.2/lto-wrapper
    Target: sparc-rtems4.11                         <1>
    Configured with: ../gcc-4.7.2/configure         <2>
    --prefix=/home/chris/development/rtems/4.11
    --bindir=/home/chris/development/rtems/4.11/bin
    --exec_prefix=/home/chris/development/rtems/4.11
    --includedir=/home/chris/development/rtems/4.11/include
    --libdir=/home/chris/development/rtems/4.11/lib
    --libexecdir=/home/chris/development/rtems/4.11/libexec
    --mandir=/home/chris/development/rtems/4.11/share/man
    --infodir=/home/chris/development/rtems/4.11/share/info
    --datadir=/home/chris/development/rtems/4.11/share
    --build=x86_64-freebsd9.1 --host=x86_64-freebsd9.1 --target=sparc-rtems4.11
    --disable-libstdcxx-pch --with-gnu-as --with-gnu-ld --verbose --with-newlib
    --with-system-zlib --disable-nls --without-included-gettext
    --disable-win32-registry --enable-version-specific-runtime-libs --disable-lto
    --enable-threads --enable-plugin --enable-newlib-io-c99-formats
    --enable-newlib-iconv --enable-languages=c,c++
    Thread model: rtems             <3>
    gcc version 4.7.2 20120920      <4>
     (RTEMS 4.11 RSB cb12e4875c203f794a5cd4b3de36101ff9a88403)-1 newlib 2.0.0) (GCC)

.. topic:: Items

  1. The target the compiler is built for.

  2. The configure options used to build GCC.

  3. The threading model is always RTEMS. This makes using the RTEMS tools for
     bare metal development more difficult.

  4. The version string. It contains the Git hash of the RTEMS Source Builder
     you are using. If your local clone has been modifed that state is also
     recorded in the version string. The hash allows you to track from a GCC
     executable back to the original source used to build it.

.. note::

   The RTEMS thread model enables specific hooks in GCC so applications built
   with RTEMS tools need the RTEMS runtime to operate correctly. You can use
   RTEMS tools to build bare metal component but it is more difficult than with
   a bare metal tool chain and you need to know what you are doing at a low
   level. The RTEMS Source Builder can build bare metal tool chains as
   well. Look in the top level ``bare`` directory.

Distributing and Archiving A Build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to create and distribute your build or you want to archive a build
you can create a tar file. This is a more advanced method for binary packaging
and installing of tools.

By default the RTEMS Source Builder installs the built packages directly and
optionally it can also create a *build set tar file* or a *package tar file*
per package built. The normal and default behaviour is to let the RTEMS Source
Builder install the tools. The source will be downloaded, built, installed and
cleaned up.

The tar files are created with the full build prefix present and if you follow
the examples given in this documentation the path is absolute. This can cause
problems if you are installing on a host you do not have super user or
administrator rights on because the prefix path may references part you do not
have write access too and tar will not extract the files. You can use the
``--strip-components`` option in tar if your host tar application supports it
to remove the parts you do not have write access too or you may need to unpack
the tar file somewhere and copy the file tree from the level you have write
access from. Embedding the full prefix path in the tar files lets you know what
the prefix is and is recommended. For example if
``/home/chris/development/rtems/4.11`` is the prefix used you cannot change
directory to the root (``/``) and install because the ``/home`` is root access
only. To install you would:

.. code-block:: shell

    $ cd
    $ tar --strip-components=3 -xjf rtems-4.11-sparc-rtems4.11-1.tar.bz2


A build set tar file is created by adding ``--bset-tar-file`` option to the
``sb-set-builder`` command::

    $ ../source-builder/sb-set-builder --log=l-sparc.txt \
             --prefix=$HOME/development/rtems/4.11 \
             --bset-tar-file \     <1>
             4.11/rtems-sparc
    Source Builder - Set Builder, v0.2.0
    Build Set: 4.11/rtems-sparc
    config: expat-2.1.0-1.cfg
    package: expat-2.1.0-x86_64-freebsd9.1-1
    building: expat-2.1.0-x86_64-freebsd9.1-1
    config: tools/rtems-binutils-2.22-1.cfg
    package: sparc-rtems4.11-binutils-2.22-1
    building: sparc-rtems4.11-binutils-2.22-1
    config: tools/rtems-gcc-4.7.2-newlib-1.20.0-1.cfg
    package: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    building: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    config: tools/rtems-gdb-7.5.1-1.cfg
    package: sparc-rtems4.11-gdb-7.5.1-1
    building: sparc-rtems4.11-gdb-7.5.1-1
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11 <2>
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11
    installing: rtems-4.11-sparc-rtems4.11-1 -> /home/chris/development/rtems/4.11
    tarball: tar/rtems-4.11-sparc-rtems4.11-1.tar.bz2      <3>
    cleaning: expat-2.1.0-x86_64-freebsd9.1-1
    cleaning: sparc-rtems4.11-binutils-2.22-1
    cleaning: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    cleaning: sparc-rtems4.11-gdb-7.5.1-1
    Build Set: Time 0:15:25.92873

.. topic:: Items

  1. The option to create a build set tar file.

  2. The installation still happens unless you specify ``--no-install``.

  3. Creating the build set tar file.

You can also suppress installing the files using the ``--no-install``
option. This is useful if your prefix is not accessiable, for example when
building Canadian cross compiled tool sets::

    $ ../source-builder/sb-set-builder --log=l-sparc.txt \
                --prefix=$HOME/development/rtems/4.11 \
                --bset-tar-file \
                --no-install \      <1>
                4.11/rtems-sparc
    Source Builder - Set Builder, v0.2.0
    Build Set: 4.11/rtems-sparc
    config: expat-2.1.0-1.cfg
    package: expat-2.1.0-x86_64-freebsd9.1-1
    building: expat-2.1.0-x86_64-freebsd9.1-1
    config: tools/rtems-binutils-2.22-1.cfg
    package: sparc-rtems4.11-binutils-2.22-1
    building: sparc-rtems4.11-binutils-2.22-1
    config: tools/rtems-gcc-4.7.2-newlib-1.20.0-1.cfg
    package: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    building: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    config: tools/rtems-gdb-7.5.1-1.cfg
    package: sparc-rtems4.11-gdb-7.5.1-1
    building: sparc-rtems4.11-gdb-7.5.1-1
    tarball: tar/rtems-4.11-sparc-rtems4.11-1.tar.bz2    <2>
    cleaning: expat-2.1.0-x86_64-freebsd9.1-1
    cleaning: sparc-rtems4.11-binutils-2.22-1
    cleaning: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    cleaning: sparc-rtems4.11-gdb-7.5.1-1
    Build Set: Time 0:14:11.721274
    $ ls tar
    rtems-4.11-sparc-rtems4.11-1.tar.bz2

.. topic:: Items

  1. The option to supressing installing the packages.

  2. Create the build set tar.

A package tar file can be created by adding the ``--pkg-tar-files`` to the
``sb-set-builder`` command. This creates a tar file per package built in the
build set::

    $ ../source-builder/sb-set-builder --log=l-sparc.txt \
            --prefix=$HOME/development/rtems/4.11 \
            --bset-tar-file \
            --pkg-tar-files \        <1>
            --no-install 4.11/rtems-sparc
    Source Builder - Set Builder, v0.2.0
    Build Set: 4.11/rtems-sparc
    config: expat-2.1.0-1.cfg
    package: expat-2.1.0-x86_64-freebsd9.1-1
    building: expat-2.1.0-x86_64-freebsd9.1-1
    config: tools/rtems-binutils-2.22-1.cfg
    package: sparc-rtems4.11-binutils-2.22-1
    building: sparc-rtems4.11-binutils-2.22-1
    config: tools/rtems-gcc-4.7.2-newlib-1.20.0-1.cfg
    package: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    building: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    config: tools/rtems-gdb-7.5.1-1.cfg
    package: sparc-rtems4.11-gdb-7.5.1-1
    building: sparc-rtems4.11-gdb-7.5.1-1
    tarball: tar/rtems-4.11-sparc-rtems4.11-1.tar.bz2
    cleaning: expat-2.1.0-x86_64-freebsd9.1-1
    cleaning: sparc-rtems4.11-binutils-2.22-1
    cleaning: sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1
    cleaning: sparc-rtems4.11-gdb-7.5.1-1
    Build Set: Time 0:14:37.658460
    $ ls tar
    expat-2.1.0-x86_64-freebsd9.1-1.tar.bz2           sparc-rtems4.11-binutils-2.22-1.tar.bz2
    sparc-rtems4.11-gdb-7.5.1-1.tar.bz2 <2>           rtems-4.11-sparc-rtems4.11-1.tar.bz2 <3>
    sparc-rtems4.11-gcc-4.7.2-newlib-1.20.0-1.tar.bz2

.. topic:: Items

  1. The option to create packages tar files.

  2. The GDB package tar file.

  3. The build set tar file. All the others in a single tar file.

Controlling the Build
~~~~~~~~~~~~~~~~~~~~~

Build sets can be controlled via the command line to enable and disable various
features. There is no definitive list of build options that can be listed
because they are implemented with the configuration scripts. The best way to
find what is available is to grep the configuration files. for ``with`` and
``without``.

Following are currentlt available:

``--without-rtems``
  Do not build RTEMS when building an RTEMS build set.

``--without-cxx``
  Do not build a C++ compiler.

``--with-objc``
  Attempt to build a C++ compiler.

``--with-fortran``
  Attempt to build a Fortran compiler.
