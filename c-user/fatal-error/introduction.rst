.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Introduction
============

The fatal error manager processes all fatal or irrecoverable errors and other
sources of system termination (for example after :c:func:`exit()`).  Fatal
errors are identified by the (fatal source, error code) pair.  The directives
provided by the fatal error manager are:

- :ref:`rtems_fatal`

- :ref:`rtems_panic`

- :ref:`rtems_shutdown_executive`

- :ref:`rtems_exception_frame_print`

- :ref:`rtems_fatal_source_text`

- :ref:`rtems_internal_error_text`

- :ref:`rtems_fatal_error_occurred`
