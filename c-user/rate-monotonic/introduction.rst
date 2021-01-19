.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 2017 Kuan-Hsun Chen
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. Generated from spec:/rtems/ratemon/if/group

.. _RateMonotonicManagerIntroduction:

Introduction
============

.. The following list was generated from:
.. spec:/rtems/ratemon/if/create
.. spec:/rtems/ratemon/if/ident
.. spec:/rtems/ratemon/if/cancel
.. spec:/rtems/ratemon/if/delete
.. spec:/rtems/ratemon/if/period
.. spec:/rtems/ratemon/if/get-status
.. spec:/rtems/ratemon/if/get-statistics
.. spec:/rtems/ratemon/if/reset-statistics
.. spec:/rtems/ratemon/if/reset-all-statistics
.. spec:/rtems/ratemon/if/report-statistics
.. spec:/rtems/ratemon/if/report-statistics-with-plugin

The Rate-Monotonic Manager provides facilities to implement tasks which execute
in a periodic fashion.  Critically, it also gathers information about the
execution of those periods and can provide important statistics to the user
which can be used to analyze and tune the application. The directives provided
by the Rate-Monotonic Manager are:

* :ref:`InterfaceRtemsRateMonotonicCreate` - Creates a period.

* :ref:`InterfaceRtemsRateMonotonicIdent` - Identifies a period by the object
  name.

* :ref:`InterfaceRtemsRateMonotonicCancel` - Cancels the period.

* :ref:`InterfaceRtemsRateMonotonicDelete` - Deletes the period.

* :ref:`InterfaceRtemsRateMonotonicPeriod` - Concludes the current period and
  start the next period, or gets the period status.

* :ref:`InterfaceRtemsRateMonotonicGetStatus` - Gets the detailed status of the
  period.

* :ref:`InterfaceRtemsRateMonotonicGetStatistics` - Gets the statistics of the
  period.

* :ref:`InterfaceRtemsRateMonotonicResetStatistics` - Resets the statistics of
  the period.

* :ref:`InterfaceRtemsRateMonotonicResetAllStatistics` - Resets the statistics
  of all periods.

* :ref:`InterfaceRtemsRateMonotonicReportStatistics` - Reports the period
  statistics using the :c:func:`printk` printer.

* :ref:`InterfaceRtemsRateMonotonicReportStatisticsWithPlugin` - Reports the
  period statistics using the printer plugin.
