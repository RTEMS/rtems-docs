.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

.. _Testing:

Testing
*******

RTEMS developers run test executables when adding new features or testing a bug
fix. All tests are run to make sure changes do not introduce regressions. Users
can run the RTEMS tests to be certain the build of the kernel they have is
functioning.

The section describes using and configuring the RTEMS Tester and RTEMS Run
tools, the types of laboratory set ups supported and how to add your BSP to the
framework. The tools command line interfaces are detailed in
:ref:`rtems-tester-command`.

An RTEMS Test is an RTEMS executable where the application code is a
test. Tests in RTEMS print banners to the console to indicate the configuration
of the test and if it has start and finished.

The RTEMS Tools Project provides the RTEMS Tester and RTEMS Run tools. The
RTEMS Tester command is ``rtems-test`` and the RTEMS Run command is
``rtems-run``. These commands manage the complexity of running embedded
executables. The commands provide a consistent command line interface to a
testing framework that supports the various run time and testing scenarios we
encounter such as simulators, GDB and executing directly on target hardware.

The RTEMS kernel code contains an extensive set of tests to exercise and test
the RTEMS kernel. The tests check functionality, provide coverage testing and
make sure the kernel is operating as intended on your target system. The
testsuite has support to make creating a test simple and uniform.

The tests are built by adding ``--enable-tests`` to the RTEMS build
configuration command line. There are over 600 tests and building them does
extend the RTEMS kernel's build time and use more disk space but it worth
building and running them. The RTEMS test executables have the ``.exe`` file
extension.

.. toctree::

   tests
   configuration
   coverage
   consoles
   simulation
   gdb-jtag
   tftp
