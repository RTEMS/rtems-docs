.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017 Chris Johns <chrisj@rtems.org>

.. _rtems-tester-command:

RTEMS Tester and Run
====================

.. index:: Tools, rtems-test, rtems-run

The RTEMS Tester is a test tool that provides a command line interface to run
test executables on supported targets. The tool provides back end support for
common simulators, debuggers and boot loaders. Board support package (BSP)
configurations for RTEMS are provided and can be used to run all the tests in
the RTEMS test suite. The tool and its framework is not specific to RTEMS and
can be configured to run any suitable application.

RTEMS is an embedded operating system and is cross-compiled on a range of host
machines. The executables run on hardware which can vary widely from open
source simulators, commercial simulators, debuggers with simulators, debuggers
with hardware specific pods and devices, and targets with boot loaders.
Testing RTEMS requires that the cross-compiled test executable is transferred
to the target hardware, executed, the output captured and returned to the test
host where it is analyzed to determine the test result.

Running the RTEMS tests on your target is very important. It provides you with
a traceable record showing that your RTEMS version and its tools are working at
the level the RTEMS development team expect when releasing RTEMS. Being able to
easily run the tests and verify the results is critical in maintaining high
standards.

Available BSP testers
---------------------

You can list the available BSP testers with:

.. code-block:: none

    $ rtems-test --list-bsps
    arm920
    beagleboardxm
    beagleboneblack
    jmr3904-run
    jmr3904
    mcf5235
    pc
    psim-run
    psim
    realview_pbx_a9_qemu
    sis-run
    sis
    xilinx_zynq_a9_qemu
    xilinx_zynq_a9_qemu_smp
    xilinx_zynq_zc706
    xilinx_zynq_zc706_qemu
    xilinx_zynq_zedboard

.. note:: The list is growing all the time and if your BSP is not supported we
          encourage you to add it and submit the configuration back to the
          project.

Some of the BSPs may appear more than once in the list. These are aliased BSP
configurations that may use a different back end. An example is the erc32 BSP.
There is the erc32 tester which uses the GDB back end and the ``erc32-run``
tester which uses the ``run`` command for erc32. We will show how to use
:program:`rtems-test` command with the erc32 BSP because it is easy to build
and use.

.. _BuildingRTEMSTests:

Building RTEMS Tests
--------------------

Build the RTEMS Kernel (See :ref:`rtems-kernel`) by cloning the repository,
running the ``bootstrap`` procedure, building and finally installing the
kernel. Be sure to enable tests by using ``--enable-tests`` option with
configure after running ``bootstrap``.

.. code-block:: none

    $ ../../rtems.git/configure --target=sparc-rtems5 \
                        --enable-tests --enable-rtemsbsp=erc32
    $ make

Add the `-j` option to the make command with the number of parallel jobs to run a
parallel build (e.g. `-j 8`).

Building all the tests takes time and it uses more disk so be patient. When
make finishes, all the tests will have been built.

.. note:: Some BSPs may require a post-build process to be run on the RTEMS ELF
          executable to create an image suitable for execution. This can be built
          into the configuration script and the tester will perform a pre-test
          command to convert the executable to a suitable format for your target.

Before running all the tests it is a good idea to run the ``hello`` test. The
``hello`` test is an RTEMS version of the classic "Hello World" example and
running it shows you have a working toolchain and build of RTEMS ready to run
the tests. Using the run with the ERC32 BSP the command is:

.. code-block:: none

    $ sparc-rtems5-run sparc-rtems5/c/erc32/testsuites/samples/hello/hello.exe

    *** BEGIN OF TEST HELLO WORLD ***
    Hello World
    *** END OF TEST HELLO WORLD ***

The run command is the GDB simulator without the GDB part.

Running the example using SIS:

.. code-block:: none

    $ sparc-rtems5-sis sparc-rtems5/c/erc32/testsuites/samples/hello/hello.exe
    SIS - SPARC/RISCV instruction simulator 2.20,  copyright Jiri Gaisler 2019
    Bug-reports to jiri@gaisler.se
    ERC32 emulation enabled

    Loaded sparc-rtems5/c/erc32/testsuites/samples/hello.exe, entry 0x02000000

    sis> run


    *** BEGIN OF TEST HELLO WORLD ***
    *** TEST VERSION: 5.0.0.c6d8589bb00a9d2a5a094c68c90290df1dc44807
    *** TEST STATE: EXPECTED-PASS
    *** TEST BUILD: RTEMS_POSIX_API
    *** TEST TOOLS: 7.5.0 20191114 (RTEMS 5, RSB 83fa79314dd87c0a8c78fd642b2cea3138be8dd6, Newlib 3e24fbf6f)
    Hello World

    *** END OF TEST HELLO WORLD ***


    *** FATAL ***
    fatal source: 0 (INTERNAL_ERROR_CORE)
    fatal code: 5 (INTERNAL_ERROR_THREAD_EXITTED)
    RTEMS version: 5.0.0.c6d8589bb00a9d2a5a094c68c90290df1dc44807
    RTEMS tools: 7.5.0 20191114 (RTEMS 5, RSB 83fa79314dd87c0a8c78fd642b2cea3138be8dd6, Newlib 3e24fbf6f)
    executing thread ID: 0x08a010001
    executing thread name: UI1
    cpu 0 in error mode (tt = 0x101)
        116401  02009ae0:  91d02000   ta  0x0

    sis> q

The examples can also be run using GDB with SIS as the back end. SIS can be connected to
gdb through a network socket using the gdb remote interface.

Either start SIS with ``-gdb``, or issue the ``gdb`` command inside SIS, and connect
gdb with ``target remote:1234``. The default port is ``1234``, the port can be changed
using the ``-port`` option.

Open a terminal and issue the following command:

.. code-block:: none

    $ sparc-rtems5-sis -gdb
    SIS - SPARC/RISCV instruction simulator 2.20,  copyright Jiri Gaisler 2019
    Bug-reports to jiri@gaisler.se
    ERC32 emulation enabled

    gdb: listening on port 1234

Now open another terminal and issue the following command:

.. code-block:: none

    $ sparc-rtems5-gdb sparc-rtems5/c/erc32/testsuites/samples/hello/hello.exe
    GNU gdb (GDB) 8.3
    Copyright (C) 2019 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    Type "show copying" and "show warranty" for details.
    This GDB was configured as "--host=x86_64-linux-gnu --target=sparc-rtems5".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
        <http://www.gnu.org/software/gdb/documentation/>.

    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    Reading symbols from sparc-rtems5/c/erc32/testsuites/samples/hello.exe...
    (gdb) target remote:1234

The ``target remote:1234`` will tell gdb to connect to the sis simulator. After this
command the output of the first terminal will change to:

.. code-block:: none

    $ sparc-rtems5-sis -gdb
    SIS - SPARC/RISCV instruction simulator 2.20,  copyright Jiri Gaisler 2019
    Bug-reports to jiri@gaisler.se
    ERC32 emulation enabled

    gdb: listening on port 1234 connected

Before running the executable, it must be loaded, this is done using the
``load`` command in gdb, and to run it, issue the ``continue`` command.

.. code-block:: none

    $ sparc-rtems5-gdb sparc-rtems5/c/erc32/testsuites/samples/hello/hello.exe
    GNU gdb (GDB) 8.3
    Copyright (C) 2019 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    Type "show copying" and "show warranty" for details.
    This GDB was configured as "--host=x86_64-linux-gnu --target=sparc-rtems5".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
        <http://www.gnu.org/software/gdb/documentation/>.

    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    Reading symbols from sparc-rtems5/c/erc32/testsuites/samples/hello.exe...
    (gdb) target remote:1234
    Remote debugging using :1234
    0x00000000 in ?? ()
    (gdb) load
    Loading section .text, size 0x17170 lma 0x2000000
    Loading section .rtemsroset, size 0x40 lma 0x2017170
    Loading section .data, size 0x600 lma 0x20181c0
    Start address 0x2000000, load size 96176
    Transfer rate: 4696 KB/sec, 270 bytes/write.
    (gdb) continue
    Continuing.

You can see your executable running in the first terminal.

.. code-block:: none

    SIS - SPARC/RISCV instruction simulator 2.20,  copyright Jiri Gaisler 2019
    Bug-reports to jiri@gaisler.se

    ERC32 emulation enabled

    gdb: listening on port 1235 connected
    X2000000,0:#40


    *** BEGIN OF TEST HELLO WORLD ***
    *** TEST VERSION: 5.0.0.c6d8589bb00a9d2a5a094c68c90290df1dc44807
    *** TEST STATE: EXPECTED-PASS
    *** TEST BUILD: RTEMS_POSIX_API
    *** TEST TOOLS: 7.5.0 20191114 (RTEMS 5, RSB 83fa79314dd87c0a8c78fd642b2cea3138be8dd6, Newlib 3e24fbf6f)
    Hello World

    *** END OF TEST HELLO WORLD ***

    ^Csis> q


For more information on the sis simulator refer to this doc: https://gaisler.se/sis/sis.pdf

There are currently close to 500 separate tests and you can run them all with a
single RTEMS Tester command.

Running the Tests
-----------------

The :program:`rtems-test` command line accepts a range of options. These are
discussed later in the manual. Command line arguments without a `--` prefix are
test executables or paths to directories. When using a path to a directory,
the directories under that path are searched for any file with a ``.exe`` extension.
This is the default extension for RTEMS executables built within RTEMS. You can
pass more than one executable on the command line.

To run the erc32 tests enter the following command from the top of the erc32
BSP build tree:

.. code-block:: none

    $ ~/development/rtems/test/rtems-tools.git/tester/rtems-test \
             --log=log_erc32_run \
             --rtems-bsp=erc32-run \
             --rtems-tools=$HOME/development/rtems/5 \
                 sparc-rtems5/c/erc32/testsuites/samples
    RTEMS Testing - Tester, 5.not_released
    [ 1/13] p:0  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: base_sp.exe
    [ 2/13] p:0  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: capture.exe
    [ 3/13] p:0  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: cdtest.exe
    [ 4/13] p:0  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: fileio.exe
    [ 5/13] p:2  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: hello.exe
    [ 6/13] p:2  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: cxx_iostream.exe
    [ 8/13] p:2  f:0  u:0  e:0  I:0  B:0  t:2  i:0  | sparc/erc32: minimum.exe
    [ 7/13] p:2  f:0  u:0  e:0  I:0  B:0  t:2  i:0  | sparc/erc32: loopback.exe
    [ 9/13] p:3  f:0  u:0  e:0  I:0  B:0  t:3  i:0  | sparc/erc32: nsecs.exe
    [10/13] p:3  f:0  u:0  e:0  I:0  B:0  t:3  i:0  | sparc/erc32: paranoia.exe
    [11/13] p:4  f:0  u:0  e:0  I:0  B:0  t:3  i:0  | sparc/erc32: pppd.exe
    [12/13] p:6  f:0  u:0  e:0  I:0  B:0  t:3  i:0  | sparc/erc32: ticker.exe
    [13/13] p:6  f:0  u:0  e:0  I:0  B:0  t:3  i:0  | sparc/erc32: unlimited.exe
    Passed:         7
    Failed:         0
    User Input:     0
    Expected Fail:  0
    Indeterminate:  0
    Benchmark:      0
    Timeout:        5
    Invalid:        1
    Total:         13
    Average test time: 0:00:27.963000
    Testing time     : 0:06:03.519012

The output has been shortened so it fits nicely here. Following the order of
appearance above, we have the following:

* The RTEMS Tester's test command. In this example we are using an absolute
  path.
* The ``--log`` option sends the output to a log file. By default only failed
  tests log the complete output.
* The ``--rtems-bsp`` option selects the erc32 BSP.
* The path to the RTEMS tools so GDB can be found.
* The path to the erc32 BSP tests to run. If you add subdirectories
  to the path specific tests can be run.
* The test results so far. See details below.
* Overall results of the run. In this run, 13 tests passed, 5 tests timed out
  and 1 is invalid. The timeouts are probably due to the tests not having enough
  time to complete. The default timeout is 180 seconds and some of the interrupt
  tests need more time. The amount of time each test takes depends on the
  performance of your host CPU when running the simulations.
* The average time per test and the total time taken to run all the tests.

.. note:: If the path to the testsuites was set to
  ``sparc-rtems5/c/erc32/testsuites`` instead of
  ``sparc-rtems5/c/erc32/testsuites/samples`` then all the executables
  would have been tested and not just those in samples.

This BSP requires the ``--rtems-tools`` option because the SPARC GDB is the
``sparc-rtems4.11-gdb`` command that is part of the RTEMS tools. Not every BSP
will require this option so you will need to check the specifics of the BSP
configuration you are using in order to determine if it is needed.

An output line is printed for each test that is executed. The :program:`rtems-test`
command by default runs multiple tests in parallel so you will see a number
of tests starting quickly and then new tests start as others finish. For example,
the output shown above is from an 8-core processor. Thus, the first 8 tests
started in parallel and the status shows the order in which they actually started,
which is not necessarily sequential, as it happens in the example above where
test 8 started before test 7.

Each output line shows information about the current status of the tests.
The status reported in each line is the status when the test starts and not the
result of that particular test. Thus, a fail, timeout or invalid count changing
means a test running before this test failed. The overall status in the end
shows that 7 tests passed, no failures, 5 timeouts and 1 invalid test.

Concerning the output of each line, we have the following:

.. code-block:: none

    [ 5/13] p:2  f:0  u:0  e:0  I:0  B:0  t:0  i:0  | sparc/erc32: hello.exe

* [ 5/13] indicates the test number, in this case test 5 out of 13 tests.
* ``p`` is the passed test count (2 in this case).
* ``f`` is the failed test count (0 in this case).
* ``u`` is the count for test marked as "user-input" (tests that expect input
    from the user).
* ``e`` is the expected-fail count (tests that are expected to fail).
* ``I`` is the count for tests the results of which are indeterminate.
* ``B`` is the count for benchmarked tests.
* ``t`` is the timeout test count.
* ``i`` is the invalid test count.
* ``sparc/erc32`` is the architecture and BSP names.
* ``hello.exe`` is the executable name.

The test log records all the tests and results. The logging mode by default
only provides the output history if a test fails, times out, or is invalid. The
time taken by each test is also recorded.

The tests must complete in a specified period of time or the test is marked as
timed out. The default timeout is 3 minutes and can be globally changed using the
``--timeout`` command line option. The time required to complete a test can
vary. When simulators are run in parallel, the time taken depends on the resources
available on the host machine being used. A test per core is the most stable
method even though more tests can be run than available cores. If your machine
needs longer or you are using a VM you may need to lengthen the timeout.

Test Status
-----------

Tests can be marked with one of the following:

* Pass
* Fail
* User-input
* Expected-fail
* Indeterminate
* Benchmark
* Timeout
* Invalid

The RTEMS console or ``stdout`` output from the test is needed to determine the
result of the test.

Pass
^^^^
A test passes if the start and end markers are seen in the test output. The
start marker is ``***`` and the end mark is ``*** END OF TEST``. All tests in
the RTEMS test suite have these markers.

Fail
^^^^
A test fails if the start marker is seen and there is no end marker.

User-input
^^^^^^^^^^
A test marked as "user-input" as it expects input from user.

Expected-fail
^^^^^^^^^^^^^
A test that is expected to fail.

Indeterminate
^^^^^^^^^^^^^
A test the results of which are indeterminate.

Benchmark
^^^^^^^^^
A benchmarked test.

Timeout
^^^^^^^
If the test does not complete within the timeout setting the test is marked as
having timed out.

Invalid
^^^^^^^
If no start marker is seen the test is marked as invalid. If you are testing on
real target hardware things can sometimes go wrong and the target may not
initialize or respond to the debugger in an expected way.

Logging
-------

The following modes of logging are available:

* All (``all``)
* Failures (``failures``)
* None (``none``)

This mode is controlled using the command line option ``--log-mode`` using
the values listed above.

All
^^^
The output of all tests is written to the log.

Failures
^^^^^^^^
The output of the all tests that do not pass is written to the log.

None
^^^^
No output is written to the log.

The output is tagged so you can determine where it comes from. The following is
the complete output for the In Memory File System test ``imfs_fslink.exe``
running on a Coldfire MCF5235 using GDB and a BDM pod:

.. code-block:: none

    [ 11/472] p:9   f:0   t:0   i:1   | m68k/mcf5235: imfs_fslink.exe
    > gdb: ..../bin/m68k-rtems4.11-gdb -i=mi --nx --quiet ..../imfs_fslink.exe
    > Reading symbols from ..../fstests/imfs_fslink/imfs_fslink.exe...
    > done.
    > target remote | m68k-bdm-gdbserver pipe 003-005
    > Remote debugging using | m68k-bdm-gdbserver pipe 003-005
    > m68k-bdm: debug module version 0
    > m68k-bdm: detected MCF5235
    > m68k-bdm: architecture CF5235 connected to 003-005
    > m68k-bdm: Coldfire debug module version is 0 (5206(e)/5235/5272/5282)
    > Process 003-005 created; pid = 0
    > 0x00006200 in ?? ()
    > thb *0xffe254c0
    > Hardware assisted breakpoint 1 at 0xffe254c0
    > continue
    > Continuing.
    ]
    ]
    ] External Reset
    ]
    ] ColdFire MCF5235 on the BCC
    ] Firmware v3b.1a.1a (Built on Jul 21 2004 17:31:28)
    ] Copyright 1995-2004 Freescale Semiconductor, Inc.  All Rights Reserved.
    ]
    ] Enter 'help' for help.
    ]
    > Temporary breakpoint
    > 1, 0xffe254c0 in ?? ()
    > load
    > Loading section .text, size 0x147e0 lma 0x40000
    > Loading section .data, size 0x5d0 lma 0x547e0
    > Start address 0x40414, load size 85424
    > Transfer rate: 10 KB/sec, 1898 bytes/write.
    > b bsp_reset
    > Breakpoint 2 at 0x41274: file ..../shared/bspreset_loop.c, line 14.
    > continue
    > Continuing.
    ] dBUG>
    ]
    ] *** FILE SYSTEM TEST ( IMFS ) ***
    ] Initializing filesystem IMFS
    ]
    ]
    ] *** LINK TEST ***
    ] link creates hardlinks
    ] test if the stat is the same
    ] chmod and chown
    ] unlink then stat the file
    ] *** END OF LINK TEST ***
    ]
    ]
    ] Shutting down filesystem IMFS
    ] *** END OF FILE SYSTEM TEST ( IMFS ) ***
    > Breakpoint
    > 2, bsp_reset () at ..../m68k/mcf5235/../../shared/bspreset_loop.c:14
    > 14    {
    Result: passed     Time: 0:00:10.045447

* GDB command line (Note: paths with \'....' have been shortened)
* Lines starting with ``>`` are from GDB's console.
* Line starting with ``]`` are from the target's console.
* The result with the test time.

Reporting
---------

The RTEMS Tester supports output in a machine parsable format. This can be
enabled using the options ``--report-path`` and ``--report-format``. Currently,
JSON output is supported using these options like so:
``--report-path="report" --report-format=json``

This will produce a file ``report.json`` that contains output equivalent to the
``failure`` logging mode.

Running Tests in Parallel
-------------------------

The RTEMS Tester supports parallel execution of tests by default. This only
makes sense if the test back end can run in parallel without resulting in
resource contention. Simulators are an example of back ends that can run in
parallel. A hardware debug tool like a BDM or JTAG pod can manage only a
single test at once so the tests need to be run one at a time.

The test framework manages the test jobs and orders the output in the log
in test order. Output is held for completed tests until the next test to be
reported has finished.

Command Line Help
-----------------

The :program:`rtems-test` command line accepts a range of options. You can
review the available options by using the ``--help`` option:

.. code-block:: none

    RTEMS Tools Project (c) 2012-2014 Chris Johns
    Options and arguments:
    --always-clean               : Always clean the build tree, even with an error
    --debug-trace                : Debug trace based on specific flags
    --dry-run                    : Do everything but actually run the build
    --force                      : Force the build to proceed
    --jobs=[0..n,none,half,full] : Run with specified number of jobs, default: num CPUs.
    --keep-going                 : Do not stop on an error.
    --list-bsps                  : List the supported BSPs
    --log file                   : Log file where all build output is written to
    --macros file[,file]         : Macro format files to load after the defaults
    --no-clean                   : Do not clean up the build tree
    --quiet                      : Quiet output (not used)
    --report-path                : Report output base path (file extension will be added)
    --report-format              : Formats in which to report test results: json
    --log-mode                   : Log modes, failures (default),all,none
    --rtems-bsp                  : The RTEMS BSP to run the test on
    --rtems-tools                : The path to the RTEMS tools
    --target                     : Set the target triplet
    --timeout                    : Set the test timeout in seconds (default 180 seconds)
    --trace                      : Trace the execution
    --warn-all                   : Generate warnings

.. note:: The list of options may be different for each release. For more
          information, please see the available options for the release
          you are using.