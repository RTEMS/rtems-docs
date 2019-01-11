.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _RSBDeployment:

Building and Deploying Tool Binaries
====================================

If you wish to create and distribute your build or you want to archive a build
you can create a tar file. We term this deploying a build. This is a more
advanced method for binary packaging and installing of tools.

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
directory to the root (``/``) and untar the file because the ``/home`` is root
access only. To install a tar file you have downloaded into your new machine's
``Downloads`` directory in your home directoty you would enter:

.. code-block:: shell

    $ cd /somewhere
    $ tar --strip-components=3 -xjf \
          $HOME/Downloads/rtems-4.11-sparc-rtems4.11-1.tar.bz2

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
