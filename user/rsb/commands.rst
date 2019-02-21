.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

Commands
--------

Checker (sb-check)
^^^^^^^^^^^^^^^^^^

This commands checks your system is set up correctly. Most options are ignored:

.. code-block:: shell

    $ ../source-builder/sb-check --help
    sb-check: [options] [args]
    RTEMS Source Builder, an RTEMS Tools Project (c) 2012-2013 Chris Johns
    Options and arguments:
    --force                : Force the build to proceed
    --quiet                : Quiet output (not used)
    --trace                : Trace the execution
    --dry-run              : Do everything but actually run the build
    --warn-all             : Generate warnings
    --no-clean             : Do not clean up the build tree
    --always-clean         : Always clean the build tree, even with an error
    --jobs                 : Run with specified number of jobs, default: num CPUs.
    --host                 : Set the host triplet
    --build                : Set the build triplet
    --target               : Set the target triplet
    --prefix path          : Tools build prefix, ie where they are installed
    --topdir path          : Top of the build tree, default is $PWD
    --configdir path       : Path to the configuration directory, default: ./config
    --builddir path        : Path to the build directory, default: ./build
    --sourcedir path       : Path to the source directory, default: ./source
    --patchdir path        : Path to the patches directory, default: ./patches
    --tmppath path         : Path to the temp directory, default: ./tmp
    --macros file[,[file]  : Macro format files to load after the defaults
    --log file             : Log file where all build out is written too
    --url url[,url]        : URL to look for source
    --no-download          : Disable the source downloader
    --targetcflags flags   : List of C flags for the target code
    --targetcxxflags flags : List of C++ flags for the target code
    --libstdcxxflags flags : List of C++ flags to build the target libstdc++ code
    --with-<label>         : Add the --with-<label> to the build
    --without-<label>      : Add the --without-<label> to the build
    --regression           : Set --no-install, --keep-going and --always-clean
    $ ../source-builder/sb-check
    RTEMS Source Builder - Check, v0.2.0
    Environment is ok

Defaults (sb-defaults)
^^^^^^^^^^^^^^^^^^^^^^

This commands outputs and the default macros for your when given no
arguments. Most options are ignored:

.. code-block:: shell

    $ ../source-builder/sb-defaults --help
    sb-defaults: [options] [args]
    RTEMS Source Builder, an RTEMS Tools Project (c) 2012-2013 Chris Johns
    Options and arguments:
    --force                : Force the build to proceed
    --quiet                : Quiet output (not used)
    --trace                : Trace the execution
    --dry-run              : Do everything but actually run the build
    --warn-all             : Generate warnings
    --no-clean             : Do not clean up the build tree
    --always-clean         : Always clean the build tree, even with an error
    --jobs                 : Run with specified number of jobs, default: num CPUs.
    --host                 : Set the host triplet
    --build                : Set the build triplet
    --target               : Set the target triplet
    --prefix path          : Tools build prefix, ie where they are installed
    --topdir path          : Top of the build tree, default is $PWD
    --configdir path       : Path to the configuration directory, default: ./config
    --builddir path        : Path to the build directory, default: ./build
    --sourcedir path       : Path to the source directory, default: ./source
    --patchdir path        : Path to the patches directory, default: ./patches
    --tmppath path         : Path to the temp directory, default: ./tmp
    --macros file[,[file]  : Macro format files to load after the defaults
    --log file             : Log file where all build out is written too
    --url url[,url]        : URL to look for source
    --no-download          : Disable the source downloader
    --targetcflags flags   : List of C flags for the target code
    --targetcxxflags flags : List of C++ flags for the target code
    --libstdcxxflags flags : List of C++ flags to build the target libstdc++ code
    --with-<label>         : Add the --with-<label> to the build
    --without-<label>      : Add the --without-<label> to the build
    --regression           : Set --no-install, --keep-going and --always-clean

Set Builder (sb-set-builder)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command builds a set:

.. code-block:: shell

    $ ../source-builder/sb-set-builder --help
    RTEMS Source Builder, an RTEMS Tools Project (c) 2012-2013 Chris Johns
    Options and arguments:
    --force                : Force the build to proceed
    --quiet                : Quiet output (not used)
    --trace                : Trace the execution
    --dry-run              : Do everything but actually run the build
    --warn-all             : Generate warnings
    --no-clean             : Do not clean up the build tree
    --always-clean         : Always clean the build tree, even with an error
    --regression           : Set --no-install, --keep-going and --always-clean
    ---jobs                 : Run with specified number of jobs, default: num CPUs.
    --host                 : Set the host triplet
    --build                : Set the build triplet
    --target               : Set the target triplet
    --prefix path          : Tools build prefix, ie where they are installed
    --topdir path          : Top of the build tree, default is $PWD
    --configdir path       : Path to the configuration directory, default: ./config
    --builddir path        : Path to the build directory, default: ./build
    --sourcedir path       : Path to the source directory, default: ./source
    --patchdir path        : Path to the patches directory, default: ./patches
    --tmppath path         : Path to the temp directory, default: ./tmp
    --macros file[,[file]  : Macro format files to load after the defaults
    --log file             : Log file where all build out is written too
    --url url[,url]        : URL to look for source
    --no-download          : Disable the source downloader
    --no-install           : Do not install the packages to the prefix
    --targetcflags flags   : List of C flags for the target code
    --targetcxxflags flags : List of C++ flags for the target code
    --libstdcxxflags flags : List of C++ flags to build the target libstdc++ code
    --with-<label>         : Add the --with-<label> to the build
    --without-<label>      : Add the --without-<label> to the build
    --mail-from            : Email address the report is from.
    --mail-to              : Email address to send the email too.
    --mail                 : Send email report or results.
    --smtp-host            : SMTP host to send via.
    --no-report            : Do not create a package report.
    --report-format        : The report format (text, html, asciidoc).
    --bset-tar-file        : Create a build set tar file
    --pkg-tar-files        : Create package tar files
    --list-bsets           : List available build sets
    --list-configs         : List available configurations
    --list-deps            : List the dependent files.

The ``arguments`` are a list of build sets to build.

**Options**:

``--force``:
  Force the build to proceed even if the host check fails. Typically this
  happens if executable files are found in the path at a different location to
  the host defaults.

``--trace``:
  Trace enable printing of debug information to stdout. It is really only of
  use to RTEMS Source Builder's developers.

``--dry-run``:
  Do everything but actually run the build commands. This is useful when
  checking a new configuration parses cleanly.

``--warn-all``:
  Generate warnings.

``--no-clean``:
  Do not clean up the build tree during the cleaning phase of the build. This
  leaves the source and the build output on disk so you can make changes, or
  amend or generate new patches. It also allows you to review configure type
  output such as ``config.log``.

``--always-clean``:
  Clean away the results of a build even if the build fails. This is normally
  used with ``--keep-going`` when regression testing to see which build sets
  fail to build. It keeps the disk usage down.

``--jobs``:
  Control the number of jobs make is given. The jobs can be ``none`` for only 1
  job, ``half`` so the number of jobs is half the number of detected cores, a
  fraction such as ``0.25`` so the number of jobs is a quarter of the number of
  detected cores and a number such as ``25`` which forces the number of jobs to
  that number.

``--host``:
  Set the host triplet value. Be careful with this option.

``--build``:
  Set the build triplet. Be careful with this option.

``--target``:
  Set the target triplet. Be careful with this option. This is useful if you
  have a generic configuration script that can work for a range of
  architectures.

``--prefix path``:
  Tools build prefix, ie where they are installed.

``--topdir path``:
  Top of the build tree, that is the current directory you are in.

``--configdir path``:
  Path to the configuration directory. This overrides the built in defaults.

``--builddir path``:
  Path to the build directory. This overrides the default of +build+.

``--sourcedir path``:
  Path to the source directory. This overrides the default of +source+.

``--patchdir path``:
  Path to the patches directory. This overrides the default of +patches+.

``--tmppath path``:
  Path to the temporary directory. This overrides the default of +tmp+.

``--macros files``:
  Macro files to load. The configuration directory path is searched.

``--log file``:
  Log all the output from the build process. The output is directed to +stdout+
  if no log file is provided.

``--url url``:
  URL to look for source when downloading. This is can be comma separate list.

``--no-download``:
  Disable downloading of source and patches. If the source is not found an
  error is raised.

``--targetcflags flags``:
  List of C flags for the target code. This allows for specific local
  customisation when testing new variations.

``--targetcxxflags flags``:
  List of C++ flags for the target code. This allows for specific local
  customisation when testing new variations.

``--libstdcxxflags flags``:
  List of C++ flags to build the target libstdc++ code. This allows for
  specific local customisation when testing new variations.

``--with-<label>``:
  Add the ``--with-<label>`` to the build. This can be tested for in a script
  with the ``%bconf_with`` macro.

``--without-<label>``:
  Add the ``--without-<label>`` to the build. This can be tested for in a
  script with the ``%bconf_without`` macro.

``--mail-from``:
  Set the from mail address if report mailing is enabled.

``--mail-to``:
  Set the to mail address if report mailing is enabled. The report is mailed to
  this address.

``--mail``:
  Mail the build report to the mail to address.

``--smtp-host``:
  The SMTP host to use to send the email. The default is ``localhost``.

``--no-report``:
  Do not create a report format.

``--report-format format``:
  The report format can be ``text`` or ``html``. The default is ``html``.

``--keep-going``:
  Do not stop on error. This is useful if your build sets performs a large
  number of testing related builds and there are errors.

``--always-clean``:
  Always clean the build tree even with a failure.

``--no-install``:
  Do not install the packages to the prefix. Use this if you are only after the
  tar files.

``--regression``:
  A convenience option which is the same as ``--no-install``, ``--keep-going``
  and ``--always-clean``.

``--bset-tar-file``:
  Create a build set tar file. This is a single tar file of all the packages in
  the build set.

``--pkg-tar-files``:
  Create package tar files. A tar file will be created for each package built
  in a build set.

``--list-bsets``:
  List available build sets.

``--list-configs``:
  List available configurations.

``--list-deps``:
  Print a list of dependent files used by a build set. Dependent files have a
  ``dep[?]` prefix where ``?`` is a number. The files are listed alphabetically.

Set Builder (sb-builder)
^^^^^^^^^^^^^^^^^^^^^^^^

This command builds a configuration as described in a configuration
file. Configuration files have the extension of ``.cfg``:

.. code-block:: shell

    $ ./source-builder/sb-builder --help
    sb-builder: [options] [args]
    RTEMS Source Builder, an RTEMS Tools Project (c) 2012 Chris Johns
    Options and arguments:
    --force                : Force the build to proceed
    --quiet                : Quiet output (not used)
    --trace                : Trace the execution
    --dry-run              : Do everything but actually run the build
    --warn-all             : Generate warnings
    --no-clean             : Do not clean up the build tree
    --always-clean         : Always clean the build tree, even with an error
    --jobs                 : Run with specified number of jobs, default: num CPUs.
    --host                 : Set the host triplet
    --build                : Set the build triplet
    --target               : Set the target triplet
    --prefix path          : Tools build prefix, ie where they are installed
    --topdir path          : Top of the build tree, default is $PWD
    --configdir path       : Path to the configuration directory, default: ./config
    --builddir path        : Path to the build directory, default: ./build
    --sourcedir path       : Path to the source directory, default: ./source
    --patchdir path        : Path to the patches directory, default: ./patches
    --tmppath path         : Path to the temp directory, default: ./tmp
    --macros file[,[file]  : Macro format files to load after the defaults
    --log file             : Log file where all build out is written too
    --url url[,url]        : URL to look for source
    --targetcflags flags   : List of C flags for the target code
    --targetcxxflags flags : List of C++ flags for the target code
    --libstdcxxflags flags : List of C++ flags to build the target libstdc++ code
    --with-<label>         : Add the --with-<label> to the build
    --without-<label>      : Add the --without-<label> to the build
    --list-configs         : List available configurations
