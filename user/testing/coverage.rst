.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 Vijay Kumar Banerjee <vijaykumar9597@gmail.com>

Coverage Analysis
=================

RTEMS is used in many critical systems. It is important that the RTEMS Project
ensure that the RTEMS product is tested as thoroughly as possible. With this
goal in mind, the RTEMS test suite was expanded with the goal that 100% of the
RTEMS executive is tested.

RTEMS-TESTER takes the following arguments to produce coverage reports:

`--coverage :`
    When the coverage option is enabled the tester produces coverage reports for
    all the symbols in cpukit. To generate a coverage report for a specific
    symbol-set ( e.g.: score) the symbol-set is passed as an argument to the
    option, e.g.: --coverage=score.

`--no-clean :`
    Tells the script not to delete the .cov trace files generated while running
    the coverage. These trace files are used for debugging purposes and will not
    be needed for a normal user.

For example: To generate a coverage report of hello.exe for leon3 on SIS, the
following command is used:

.. code-block:: none

    rtems-test \
    --rtems-tools=$HOME/development/rtems/6 \
    --log=coverage_analysis.log \
    --no-clean \
    --coverage \
    --rtems-bsp=leon3-sis-cov \
    $HOME/development/rtems/kernel/leon3/sparc-rtems6/c/leon3/testsuites/samples/hello.exe

The command will create the coverage report in the following tree structure:

.. code-block:: none

    ├── coverage_analysis.log
    ├── leon3-sis-coverage
    │   └── score
    │       ├── annotated.html
    │       ├── annotated.txt
    │       ├── branch.html
    │       ├── branch.txt
    │       ├── covoar.css
    │       ├── ExplanationsNotFound.txt
    │       ├── index.html
    │       ├── no_range_uncovered.html
    │       ├── no_range_uncovered.txt
    │       ├── NotReferenced.html
    │       ├── sizes.html
    │       ├── sizes.txt
    │       ├── summary.txt
    │       ├── symbolSummary.html
    │       ├── symbolSummary.txt
    │       ├── table.js
    │       ├── uncovered.html
    │       └── uncovered.txt
    └── leon3-sis-report.html

The html on top of the directory, i.e., leon3-sis-report.html is the top level
navigation for the coverage analysis report and will let the user browse through
all the generated reports from different subsystems.
