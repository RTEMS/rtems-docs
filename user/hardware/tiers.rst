.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _tiers:

Tiers
=====
.. index Tiers

RTEMS has a tiered structure for architecture and BSPs. It provides:

#. A way to determine the state of a BSP in RTEMS.

#. A quaility measure for changes entering the RTEMS source code.

The tier structure in RTEMS is support by the Buildbot continuous integration
server. Changes to RTEMS are automatically built and tested and the results
indicate if a BSP currently meets it's tier status.

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
   current tier level.

#. Changes to RTEMS may result in a BSP not meeting it's tier are acceptable if
   the change is accompanied by an announcement and a plan on how this is to be
   resolved.

#. Test results are set on a per BSP basis by the RTEMS Project team. Changes
   to the test result values requires agreement. The test results are defined
   as:

     #. Passes

     #. Expected Failures

   Expected failures must be explicitly listed. A BSP is required to have a
   valid test result entry to reach tier 1.
