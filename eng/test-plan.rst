.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project


Software Test Plan Assurance and Procedures
********************************************

Testing and Coverage
====================

Testing to verify that requirements are implemented is a critical part of
the high integrity processes. Similarly, measuring and reporting source
and decision path coverage of source code is critical.

Needed improvements to the RTEMS testing infrastructure should be done
as part of the open project. Similarly, improvements in RTEMS coverage
reporting should be done as part of the open project. Both of these
capabilities are part of the RTEMS Tester toolset.

Assuming that a requirements focused test suite is added to the open
RTEMS, tools will be needed to assist in verifying that requirements are
“fully tested.” A fully tested requirement is one which is implemented
and tested with associated logical tracing. Tools automating this analysis
and generating reporting and alerts will be a critical part of ensuring
the master technical data does not bit rot.

Must use tools from:

TBD - Change URL to git.rtems.org and list support tools
RTEMS Tools Project: https://github.com/RTEMS/rtems-tools


Scope, Procedures, Methodologies, Tools
TBD - Write content

.. COMMENT: Subsections
.. toctree::

    test-suites
    tester
