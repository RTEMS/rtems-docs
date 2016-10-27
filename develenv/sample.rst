.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Sample Applications
###################

Introduction
============

The RTEMS source distribution includes a set of sample applications that are
located in the ``${RTEMS_ROOT}/testsuites/samples/`` directory.  These
applications are intended to illustrate the basic format of RTEMS single and
multiple processor applications and the use of some features.  In addition,
these relatively simple applications can be used to test locally developed
board support packages and device drivers as they exercise a critical subset of
RTEMS functionality that is often broken in new BSPs.

Some of the following sample applications will be covered in more detail in
subsequent sections:

*Hello World*
    The RTEMS Hello World test is provided in the subdirectory
    ``${RTEMS_ROOT}/testsuites/samples/hello/``.  This test is helpful when
    testing new RTEMS development environment.

*Clock Tick*
    The ``${RTEMS_ROOT}/testsuites/samples/ticker/`` subdirectory provides a
    test for verification of clock chip device drivers of BSPs.

*Base Single Processor*
    A simple single processor test similar to those in the single processor
    test suite is provided in ``${RTEMS_ROOT}/testsuites/samples/base_sp/``.

*Base Multiple Processor*
    A simple two node multiprocessor test capable of testing an newly developed
    MPCI layer is provided in ``${RTEMS_ROOT}/testsuites/samples/base_mp/``.

*Capture*
    The RTEMS Capture test is provided in the subdirectory
    ``${RTEMS_ROOT}/testsuites/samples/capture/``.  This is an interactive test
    which demonstrates the capabilities of the RTEMS Capture Engine.  It
    includes a few test threads which generate interesting execution patterns.
    Look at the file ``${RTEMS_ROOT}/testsuites/samples/capture/capture.scn``
    for a sample session.

*Constructor/Destructor C++ Test*
    The ``${RTEMS_ROOT}/testsuites/samples/cdtest/`` subdirectory provides a
    simple C++ application using constructors and destructors.  It is only
    built when C++ is enabled and its primary purpose is to demonstrate that
    global constructors and destructors work.  Since this requires that the
    linker script for your BSP be correct, this is an important test.

*File IO*
    The RTEMS File IO test is provided in the subdirectory
    ``${RTEMS_ROOT}/testsuites/samples/fileio/``.  This is an interactive test
    which allows the user to interact with an ATA/IDE device.  It will read the
    partition table and allow the user to dynamically mount one of the FAT32
    partitions it finds.  Commands are also provided to write and read files on
    the disk.

*IO Stream*
    The RTEMS IO Stream test is provided in the subdirectory
    ``${RTEMS_ROOT}/testsuites/samples/iostream/``.  This test is a simple C++
    application which demonstrates that C++ iostreams are functional. This
    requires that the RTEMS C++ run-time support is functioning properly.  This
    test is only build when C++ is enabled.

*Network Loopback Test*
    The ``${RTEMS_ROOT}/testsuites/samples/loopback/`` directory contains a
    sample test that demonstrates the use of sockets and the loopback network
    device.  It does not require the presence of network hardware in order to
    run.  It is only built if RTEMS was configured with networking enabled.

*Minimum Size Test*
    The directory ``${RTEMS_ROOT}/testsuites/samples/minimum/`` contains a
    simple RTEMS program that results in a non-functional executable.  It is
    intended to show the size of a minimum footprint application based upon the
    current RTEMS configuration.

*Nanoseconds*
    The RTEMS Nanoseconds test is provided in the subdirectory
    ``${RTEMS_ROOT}/testsuites/samples/nsecs/``.  This test demonstrates that
    the BSP has support for nanosecond timestamp granularity.  It prints the
    time of day and uptime multiple times as quickly as possible.  It should be
    possible from the output to determine if your BSP has nanosecond accurate
    clock support and it is functional.

*Paranoia Floating Point Test*
    The directory ``${RTEMS_ROOT}/testsuites/samples/paranoia/`` contains the
    public domain floating point and math library test.

*Point-to-Point Protocol Daemon*
    The RTEMS Point-to-Point Protocol Daemon test is provided in the
    subdirectory ``${RTEMS_ROOT}/testsuites/samples/pppd/``.  This test
    primarily serves as the baseline for a user application using the PPP
    protocol.

*Unlimited Object Allocation*
    The ``${RTEMS_ROOT}/testsuites/samples/unlimited/`` directory contains a
    sample test that demonstrates the use of the*unlimited* object allocation
    configuration option to RTEMS.

The sample tests are written using the Classic API so the reader should be
familiar with the terms used and material presented in the *RTEMS Applications
Users Guide*.

Hello World
===========

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/hello/

It provides a rudimentary test of the BSP start up code and the console output
routine.  The C version of this sample application uses the printf function
from the RTEMS Standard C Library to output messages.  The Ada version of this
sample uses the TEXT_IO package to output the hello messages.  The following
messages are printed:

.. code-block:: shell

    *** HELLO WORLD TEST ***
    Hello World
    *** END OF HELLO WORLD TEST ***

These messages are printed from the application's single initialization task.
If the above messages are not printed correctly, then either the BSP start up
code or the console output routine is not operating properly.

Clock Tick
==========

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/ticker/

This application is designed as a simple test of the clock tick device driver.
In addition, this application also tests the printf function from the RTEMS
Standard C Library by using it to output the following messages:

.. code-block:: shell

    *** CLOCK TICK TEST ***
    TA1 - tm_get - 09:00:00   12/31/1988
    TA2 - tm_get - 09:00:00   12/31/1988
    TA3 - tm_get - 09:00:00   12/31/1988
    TA1 - tm_get - 09:00:05   12/31/1988
    TA1 - tm_get - 09:00:10   12/31/1988
    TA2 - tm_get - 09:00:10   12/31/1988
    TA1 - tm_get - 09:00:15   12/31/1988
    TA3 - tm_get - 09:00:15   12/31/1988
    TA1 - tm_get - 09:00:20   12/31/1988
    TA2 - tm_get - 09:00:20   12/31/1988
    TA1 - tm_get - 09:00:25   12/31/1988
    TA1 - tm_get - 09:00:30   12/31/1988
    TA2 - tm_get - 09:00:30   12/31/1988
    TA3 - tm_get - 09:00:30   12/31/1988
    *** END OF CLOCK TICK TEST ***

The clock tick sample application utilizes a single initialization task and
three copies of the single application task.  The initialization task prints
the test herald, sets the time and date, and creates and starts the three
application tasks before deleting itself.  The three application tasks generate
the rest of the output.  Every five seconds, one or more of the tasks will
print the current time obtained via the tm_get directive.  The first task, TA1,
executes every five seconds, the second task, TA2, every ten seconds, and the
third task, TA3, every fifteen seconds. If the time printed does not match the
above output, then the clock device driver is not operating properly.

Base Single Processor Application
=================================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/base_sp/

It provides a framework from which a single processor RTEMS application can be
developed. The use of the task argument is illustrated.  This sample
application uses the printf function from the RTEMS Standard C Library or
TEXT_IO functions when using the Ada version to output the following messages:

.. code-block:: shell

    *** SAMPLE SINGLE PROCESSOR APPLICATION ***
    Creating and starting an application task
    Application task was invoked with argument (0) and has id of 0x10002
    *** END OF SAMPLE SINGLE PROCESSOR APPLICATION ***

The first two messages are printed from the application's single initialization
task.  The final messages are printed from the single application task.

Base Multiple Processor Application
===================================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/base_mp/

It provides a framework from which a multiprocessor RTEMS application can be
developed. This directory has a subdirectory for each node in the
multiprocessor system.  The task argument is used to distinguish the node on
which the application task is executed.  The first node will print the
following messages:

.. code-block:: shell

    *** SAMPLE MULTIPROCESSOR APPLICATION ***
    Creating and starting an application task
    This task was invoked with the node argument (1)
    This task has the id of 0x10002
    *** END OF SAMPLE MULTIPROCESSOR APPLICATION ***

The second node will print the following messages:

.. code-block:: shell

    *** SAMPLE MULTIPROCESSOR APPLICATION ***
    Creating and starting an application task
    This task was invoked with the node argument (2)
    This task has the id of 0x20002
    *** END OF SAMPLE MULTIPROCESSOR APPLICATION ***

The herald is printed from the application's single initialization task on each
node.  The final messages are printed from the single application task on each
node.

In this sample application, all source code is shared between the nodes except
for the node dependent configuration files.  These files contains the
definition of the node number used in the initialization of the RTEMS
Multiprocessor Configuration Table. This file is not shared because the node
number field in the RTEMS Multiprocessor Configuration Table must be unique on
each node.

Constructor/Destructor C++ Application
======================================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/cdtest/

This sample application demonstrates that RTEMS is compatible with C++
applications.  It uses constructors, destructor, and I/O stream output in
testing these various capabilities.  The board support package responsible for
this application must support a C++ environment.

This sample application uses the printf function from the RTEMS Standard C
Library to output the following messages:

.. code-block:: shell

    Hey I'M in base class constructor number 1 for 0x400010cc.
    Hey I'M in base class constructor number 2 for 0x400010d4.
    Hey I'M in derived class constructor number 3 for 0x400010d4.
    *** CONSTRUCTOR/DESTRUCTOR TEST ***
    Hey I'M in base class constructor number 4 for 0x4009ee08.
    Hey I'M in base class constructor number 5 for 0x4009ee10.
    Hey I'M in base class constructor number 6 for 0x4009ee18.
    Hey I'M in base class constructor number 7 for 0x4009ee20.
    Hey I'M in derived class constructor number 8 for 0x4009ee20.
    Testing a C++ I/O stream
    Hey I'M in derived class constructor number 8 for 0x4009ee20.
    Derived class - Instantiation order 8
    Hey I'M in base class constructor number 7 for 0x4009ee20.
    Instantiation order 8
    Hey I'M in base class constructor number 6 for 0x4009ee18.
    Instantiation order 6
    Hey I'M in base class constructor number 5 for 0x4009ee10.
    Instantiation order 5
    Hey I'M in base class constructor number 4 for 0x4009ee08.
    Instantiation order 5
    *** END OF CONSTRUCTOR/DESTRUCTOR TEST ***
    Hey I'M in base class constructor number 3 for 0x400010d4.
    Hey I'M in base class constructor number 2 for 0x400010d4.
    Hey I'M in base class constructor number 1 for 0x400010cc.

Minimum Size Test
=================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/minimum/

This sample application is designed to produce the minimum code space required
for any RTEMS application based upon the current RTEMS configuration and BSP.
In many situations, the bulk of this executable consists of hardware and RTEMS
initialization, basic infrastructure such as malloc(), and RTEMS and hardware
shutdown support.

Nanosecond Granularity Application
==================================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/nsecs/

This sample application exercises the Clock Driver for this BSP and
demonstrates its ability to generate accurate timestamps.  This application
does this by exercising the time subsystem in three ways:

- Obtain Time of Day Twice Back to Back

- Obtain System Up Time Twice Back to Back

- Use System Up Time to Measure Loops

The following is an example of what the output of this test may appear like:

.. code-block:: shell

    *** NANOSECOND CLOCK TEST ***
    10 iterations of getting TOD
    Start: Sat Mar 24 11:15:00 2007:540000
    Stop : Sat Mar 24 11:15:00 2007:549000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:3974000
    Stop : Sat Mar 24 11:15:00 2007:3983000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:7510000
    Stop : Sat Mar 24 11:15:00 2007:7519000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:11054000
    Stop : Sat Mar 24 11:15:00 2007:11063000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:14638000
    Stop : Sat Mar 24 11:15:00 2007:14647000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:18301000
    Stop : Sat Mar 24 11:15:00 2007:18310000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:21901000
    Stop : Sat Mar 24 11:15:00 2007:21910000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:25526000
    Stop : Sat Mar 24 11:15:00 2007:25535000 --> 0:9000
    Start: Sat Mar 24 11:15:00 2007:29196000
    Stop : Sat Mar 24 11:15:00 2007:29206000 --> 0:10000
    Start: Sat Mar 24 11:15:00 2007:32826000
    Stop : Sat Mar 24 11:15:00 2007:32835000 --> 0:9000
    10 iterations of getting Uptime
    0:38977000 0:38986000 --> 0:9000
    0:40324000 0:40332000 --> 0:8000
    0:41636000 0:41645000 --> 0:9000
    0:42949000 0:42958000 --> 0:9000
    0:44295000 0:44304000 --> 0:9000
    0:45608000 0:45617000 --> 0:9000
    0:46921000 0:46930000 --> 0:9000
    0:48282000 0:48291000 --> 0:9000
    0:49595000 0:49603000 --> 0:8000
    0:50908000 0:50917000 --> 0:9000
    10 iterations of getting Uptime with different loop values
    loop of 10000 0:119488000 0:119704000 --> 0:216000
    loop of 20000 0:124028000 0:124463000 --> 0:435000
    loop of 30000 0:128567000 0:129220000 --> 0:653000
    loop of 40000 0:133097000 0:133964000 --> 0:867000
    loop of 50000 0:137643000 0:138728000 --> 0:1085000
    loop of 60000 0:142265000 0:143572000 --> 0:1307000
    loop of 70000 0:146894000 0:148416000 --> 0:1522000
    loop of 80000 0:151519000 0:153260000 --> 0:1741000
    loop of 90000 0:156145000 0:158099000 --> 0:1954000
    loop of 100000 0:160770000 0:162942000 --> 0:2172000
    *** END OF NANOSECOND CLOCK TEST ***

Paranoia Floating Point Application
===================================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/paranoia/

This sample application uses a public domain floating point and math library
test to verify these capabilities of the RTEMS executive.  Deviations between
actual and expected results are reported to the screen.  This is a very
extensive test which tests all mathematical and number conversion functions.
Paranoia is also very large and requires a long period of time to run.
Problems which commonly prevent this test from executing to completion include
stack overflow and FPU exception handlers not installed.

Network Loopback Test
=====================

This sample application is in the following directory:

.. code-block:: shell

    ${RTEMS_ROOT}/testsuites/samples/loopback/

This sample application uses the network loopback device to demonstrate the use
of the RTEMS TCP/IP stack.  This sample test illustrates the basic
configuration and initialization of the TCP/IP stack as well as simple socket
usage.
