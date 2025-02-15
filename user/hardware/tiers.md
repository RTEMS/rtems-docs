.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _tiers:

Tiers
=====
.. index Tiers

RTEMS has a tiered structure for architecture and BSPs. It provides:

#. A way to determine the state of a BSP in RTEMS.

#. A quaility measure for changes entering the RTEMS source code.

The RTEMS project supports RTEMS Architecture Tiers. Each architecture
resided in one of the numbered tiers. The tiers are number 1 to 4 where
Tier 1 is the highest tier and Tier 4 is the lowest. Architectures move
between tiers based on the level of support and the level of testing that
is performed. An architecture requires continual testing and reporting
of test results to maintain a tier level. The RTEMS Project's continuous
integration testing program` continually monitors and reports the test
results.

The RTEMS Architecture Tier system provides a defined way to determine
the state of an architecture in RTEMS. Architectures age and support
for them drops off and the RTEMS Project needs a way to determine
if an architecture should stay and be supported or depreciated and
removed. The tier system also provides users with a clear understanding of
the state of an architecture in RTEMS, often useful when deciding on
a processor for a new project. It can also let a user know the RTEMS
Project needs support to maintain a specific architecture. Access to
hardware to perform testing is a large and complex undertaking and the
RTEMS Project is always looking for user support and help. If you can
help please contact someone and let us know.

The tier structure in RTEMS is support by the Buildbot continuous integration
server. Changes to RTEMS are automatically built and tested and the results
indicate if a BSP currently meets its tier status. As the RTEMS Project 
does not own hardware for every BSP, it is critical that users provide
test results on hardware of interest.

The rules for Tiers are:

#. A BSP can only be in one of the following tiers:

   +------+-----------------------------------------------------------------+
   | Tier | Description                                                     |
   +------+-----------------------------------------------------------------+
   | 1    | * The RTEMS Kernel must build without error.                    |
   |      | * Tests are run on target hardware.                             |
   +------+-----------------------------------------------------------------+
   | 2    | * The RTEMS Kernel must build without error.                    |
   |      | * Tests can be run on simulation.                               |
   +------+-----------------------------------------------------------------+
   | 3    | * The RTEMS Kernel must build without error.                    |
   |      | * There are no test results.                                    |
   +------+-----------------------------------------------------------------+
   | 4    | * The RTEMS Kernel does not build.                              |
   +------+-----------------------------------------------------------------+
   | 5    | * The BSP is to be removed after the next release.              |
   +------+-----------------------------------------------------------------+

#. An architecuture's tier is set by the highest BSP tier reached.

#. The tier level for a BSP is set by the RTEMS Project team. Movement of BSP
   between tier level requires agreement. The Buildbot results indicate the
   minimum current tier level.

#. Changes to RTEMS may result in a BSP not meeting its tier are acceptable if
   the change is accompanied by an announcement and a plan on how this is to be
   resolved. Temporary drops in tier are expected and should be brief.

#. Test results are set on a per BSP basis by the RTEMS Project team. Changes
   to the test result values requires agreement. The test results are defined
   as:

     #. Passes

     #. Expected Failures

   Expected failures must be explicitly listed. A BSP is required to have a
   valid test result entry on target hardware to reach tier 1.
