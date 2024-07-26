.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

.. _FormalToolSetup:

Formal Tools Setup
==================

The required formal tools consist of
the model checking software (Promela/SPIN),
and the test generation software (spin2test/testbuilder).

Installing Tools
----------------

Installing Promela/SPIN
^^^^^^^^^^^^^^^^^^^^^^^

Follow the installation instructions for Promela/Spin
at https://spinroot.com/spin/Man/README.html.

There are references there to the Spin Distribution which is now on
Github (https://github.com/nimble-code/Spin).

Installing Test Generation Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The test generation tools are found in ``formal/promela/src``, written in
Python3, and installed using a virtual environment.
To build the tools, enter ``formal/promela/src`` and issue the
commands:

.. code:: shell

  make env
  . env/bin/activate
  make py

The test generation tools need to be used from within this Python virtual
environment. Use the ``deactivate`` command to exit from it.

Test generation is managed at the top level by the script ``testbuilder.py``
located in the top-level of ``formal/promela/src``.
To avoid using (long) absolute pathnames,
it helps to define an suitable alias
*(e.g.)*:

.. code-block:: shell

  alias tbuild='python3 /..../formal/promela/src/testbuilder.py'

This alias is used subsequently in this documentation.

To check for a successful tool build, invoke the command without any
arguments, which should result in an extended help message being displayed:

.. code-block:: shell

  (env) prompt % tbuild
  USAGE:
  help - more details about usage and commands below
  all modelname - runs clean, spin, gentests, copy, compile and run
  clean modelname - remove spin, test files
  archive modelname - archives spin, test files
  zero  - remove all tesfiles from RTEMS
  spin modelname - generate spin files
  gentests modelname - generate test files
  copy modelname - copy test files and configuration to RTEMS
  compile - compiles RTEMS tests
  run - runs RTEMS tests

The tool is not yet ready for use, as it needs to be configured.

Tool Configuration
------------------

Tool configuration involves setting up a new testsuite in RTEMS, and providing
information to ``tbuild`` that tells it where to find key locations, and some
command-line arguments for some of the tools.
A template file ``testbuilder-template.yml`` is included,
and contains the following entries:

.. code-block:: python

  # This should be specialised for your setup, as testbuilder.yml,
  # located in the same directory as testbuilder.py
  # All pathnames should be absolute

  spin2test: <spin2test_directory>/spin2test.py
  rtems: <path-to-main-rtems-directory>  # rtems.git, or ..../modules/rtems/
  rsb: <rsb-build_directory>/rtems/6/bin/
  simulator: <path-to>/sparc-rtems6-sis
  testyamldir: <rtems>/spec/build/testsuites/validation/ # directory containing <modelname>.yml
  testcode: <rtems>/testsuites/validation/
  testexedir:  <rtems>/build/.../testsuites/validation/ # directory containing ts-<modelname>.exe
  testsuite: model-0
  simulatorargs: -leon3 -r s -m 2  # run command executes "<simulator> <simargs> <testexedir>/ts-<testsuite>.exe"
  spinallscenarios: -DTEST_GEN -run -E -c0 -e # trail generation "spin <spinallscenarios> <model>.pml"

This template should be copied/renamed to ``testbuilder.yml``
and each entry updated as follows:

* spin2test:
    This should be the absolute path to ``spin2test.py``
    in the Promela sources directory.

    ``/.../formal/promela/src/spin2test.py``

* rtems:
    This should be the absolute path to your RTEMS source directory,
    with the terminating ``/``.
    From ``rtems-central`` this would be:

    ``/.../rtems-central/modules/rtems/``

    For a separate ``rtems`` installation
    it would be where ``rtems.git`` was cloned.

    We refer to this path below as ``<rtems>``.

* rsb:
    This should be the absolute path
    to your RTEMS source-builder binaries directory,
    with the terminating ``/``.
    From ``rtems-central`` this would be (assuming RTEMS 6):

    ``/.../rtems-central/modules/rsb/6/bin/``

* simulator:
    This should be the absolute path to the RTEMS Tester
    (See Host Tools in the RTEMS User Manual)

    It defaults at present to the ``sis`` simulator

    ``/.../rtems-central/modules/rsb/6/bin/sparc-rtems6-sis``

* testsuite:
    This is the name for the testsuite :

    Default value: ``model-0``

* testyamldir:
    This should be the absolute path to where validation tests are *specified*:

    ``<rtems>/spec/build/testsuites/validation/``

* testcode:
    This should be the absolute path to where validation test sources
    are found:

    ``<rtems>/testsuites/validation/``

* testexedir:
    This should be the absolute path to where
    the model-based validation test executable
    will be found:

    ``<rtems>/build/.../testsuites/validation/``

    This will contain ``ts-<testsuite>.exe`` (e.g. ``ts-model-0.exe``)

* simulatorargs:
    These are the command line arguments for the RTEMS Tester.
    It defaults at present to those for the ``sis`` simulator.

    ``-<bsp> -r s -m <cpus>``

    The first argument should be the BSP used when building RTEMS sources.
    BSPs ``leon3``, ``gr712rc`` and ``gr740`` have been used.
    The argument to the ``-m`` flag is the number of cores.
    Possible values are: 1, 2 and 4 (BSP dependent)

    Default: ``-leon3 -r s -m 2``

* spinallscenarios:
    These are command line arguments for SPIN,
    that ensure that all counter-examples are generated.

    Default: ``-DTEST_GEN -run -E -c0 -e`` (recommended)

Testsuite Setup
^^^^^^^^^^^^^^^

The C test code generated by these tools is installed into the main ``rtems``
repository  at ``testsuites/validation`` in the exact same way as other RTEMS
test code.
This means that whenever ``waf`` is used at the top level to build and/or run
tests, that the formally generated code is automatically included.
This requires adding and modifying some *Specification Items*
(See Software Requirements Engineering section in this document).

To create a testsuite called ``model-0`` (say), do the following, in the
``spec/build/testsuites/validation`` directory:

* Edit ``grp.yml`` and add the following two lines into the `links` entry:

  .. code-block:: YAML

    - role: build-dependency
      uid: model-0

* Copy ``validation-0.yml`` (say) to ``model-0.yml``, and change the following
  entries as shown:

  .. code-block:: YAML

    enabled-by: RTEMS_SMP
    source:
    - testsuites/validation/ts-model-0.c
    target: testsuites/validation/ts-model-0.exe

Then, go to the ``testsuites/validation`` directory, and copy
``ts-validation-0.c`` to ``ts-model-0.c``, and edit as follows:

  * Change all occurrences of ``Validation0`` in comments to ``Model0``.

  * Change ``rtems_test_name`` to ``Model0``.

Running Test Generation
-----------------------

The testbuilder takes a command as its first command-line argument. Some of
these commands require the model-name as a second argument:

  Usage:   ``tbuild <command> [<modelname>]``

The commands provided are:

``clean <model>``
  Removes generated files.

``spin <model>``
  Runs SPIN to find all scenarios. The scenarios are found in numbered files
  called ``<model>N.spn``.

``gentests <model>``
  Convert SPIN scenarios to test sources. Each ``<model>N.spn`` produces a numbered
  test source file.

``copy <model>``
  Copies the generated test files to the relevant test source directory, and
  updates the relevant test configuration files.

``archive <model>``
  Copies generated spn, trail, source, and test log files to an archive
  sub-directory of the model directory.

``compile``
  Rebuilds the test executable.

``run``
  Runs tests in a simulator.

``all <model>``
  Does clean, spin, gentests, copy, compile, and run.

``zero``
  Removes all generated test filenames from the test configuration files, but
  does NOT remove the test sources from the test source directory.

In order to generate test files the following input files are required:
    ``<model>.pml``,
    ``<model>-rfn.yml``,
    ``<model>-pre.h``,
    ``<model>-post.h``, and
    ``<model>-run.h``.
In addition there may be other files
whose names have <model> embedded in them. These are included in what is
transfered to the test source directory by the copy command.

The simplest way to check test generation is setup properly is to visit one of
the models, found under ``formal/promela/models`` and execute the following
command:

.. code-block:: shell

   tbuild all mymodel

This should end by generating a file `model-0-test.log`. The output is
identical to that generated by the regular RTEMS tests, using the
*Software Test Framework* described elsewhere in this document.

Output for the Event Manager model, highly redacted:

.. code-block::

  SIS - SPARC/RISCV instruction simulator 2.29,  copyright Jiri Gaisler 2020
  Bug-reports to jiri@gaisler.se

  GR740/LEON4 emulation enabled, 4 cpus online, delta 50 clocks

  Loaded ts-model-0.exe, entry 0x00000000

  *** BEGIN OF TEST Model0 ***
  *** TEST VERSION: 6.0.0.03337dab21e961585d323a9974c8eea6106c803d
  *** TEST STATE: EXPECTED_PASS
  *** TEST BUILD: RTEMS_SMP
  *** TEST TOOLS: 10.3.1 20210409 (RTEMS 6, RSB 889cf95db0122bd1a6b21598569620c40ff2069d, Newlib eb03ac1)
  A:Model0
  S:Platform:RTEMS
  ...
  B:RtemsModelSystemEventsMgr8
  ...
  L:@@@ 3 CALL event_send 1 2 10 sendrc
  L:Calling Send(167837697,10)
  L:Returned 0x0 from Send
  ...
  E:RtemsModelEventsMgr0:N:21:F:0:D:0.005648
  Z:Model0:C:18:N:430:F:0:D:0.130464
  Y:ReportHash:SHA256:5EeLdWsRd25IE-ZsS6pduLDsrD_qzB59dMU-Mg2-BDA=

  *** END OF TEST Model0 ***

  cpu 0 in error mode (tt = 0x80)
    6927700  0000d580:  91d02000   ta  0x0

