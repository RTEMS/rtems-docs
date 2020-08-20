.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)
.. Copyright (C) 2017 Kuan-Hsun Chen.

Introduction
============

The rate monotonic manager provides facilities to implement tasks which execute
in a periodic fashion.  Critically, it also gathers information about the
execution of those periods and can provide important statistics to the user
which can be used to analyze and tune the application.  The directives provided
by the rate monotonic manager are:

- :ref:`rtems_rate_monotonic_create`

- :ref:`rtems_rate_monotonic_ident`

- :ref:`rtems_rate_monotonic_cancel`

- :ref:`rtems_rate_monotonic_delete`

- :ref:`rtems_rate_monotonic_period`

- :ref:`rtems_rate_monotonic_get_status`

- :ref:`rtems_rate_monotonic_get_statistics`

- :ref:`rtems_rate_monotonic_reset_statistics`

- :ref:`rtems_rate_monotonic_reset_all_statistics`

- :ref:`rtems_rate_monotonic_report_statistics`
