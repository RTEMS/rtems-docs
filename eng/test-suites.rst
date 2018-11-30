.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

Test Suites
***********

.. COMMENT:TBD  - Convert the following to Rest and insert into this file
.. COMMENT:TBD  from https://devel.rtems.org/wiki/Developer/Testing/TestSuites

.. COMMENT:TBD also update list of tests based on rtems/testsuites

All RTEMS source distributions include the complete RTEMS test suites. These
tests must be compiled and linked for a specific BSP. Some BSPs are for freely
available simulators and thus anyone may test RTEMS on a simulator. Most of
the BSPs which can execute on a simulator include scripts to help automate
running them.

The RTEMS Project welcomes additions to the various test suites and sample
application collections.

The following functional test suites are included with RTEMS.

* Classic API Single Processor Test Suite
* POSIX API Test Suite
* ITRON API Test Suite
* Support Library Test Suite (libtests)
* Multiprocessing Test Suite
* Classic API Ada95 Binding Test Suite

The following timing test suites are included with RTEMS.

* Classic API Timing Test Suite
* ITRON API Timing Test Suite
* The RTEMS source distribution includes three collections of sample applications.

Sample Applications (built as RTEMS tests)

* Example Applications (built as RTEMS user applications)
* Network Demonstration Applications
