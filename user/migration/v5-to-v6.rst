.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. _Migration_5_to_6:

RTEMS 5 to RTEMS 6
==================

This section provides helpful information when migrating from RTEMS 5 to
RTEMS 6.

Update to GCC 10 and Later
--------------------------

The tool suite for RTEMS 6 uses at least GCC 10.  GCC 10 and later enable
``-fno-common`` by default.  Code bases which never used this option before may
observe now multiple definition linker errors.  For example, if global
variables are declared and defined in header files (usually a missing
``extern`` in the header file).

No -specs bsp_specs GCC Option
------------------------------

The ``-spec bsp_specs`` GCC Option is no longer needed to build RTEMS
applications and there is no :file:`bsp_specs` file installed.  If you use this
option, then you get an error like this:

.. code-block:: none

    sparc-rtems6-gcc: fatal error: cannot read spec file 'bsp_specs': No such file or directory

You can remove this GCC option from your build to fix this error.
Alternatively, you can add an empty :file:`bsp_specs` file.

Replacements for Removed APIs
-----------------------------

* The ``rtems_iterate_over_all_threads()`` directive was removed. Use
  ``rtems_task_iterate()`` instead.

* The ``rtems_get_current_processor()`` directive was removed. Use
  ``rtems_scheduler_get_processor()`` instead.

* The ``rtems_get_processor_count()`` directive was removed. Use
  ``rtems_scheduler_get_processor_maximum()`` instead.

* The ``boolean`` type was removed. Use ``bool`` instead.

* The ``single_precision`` type was removed. Use ``float`` instead.

* The ``double_precision`` type was removed. Use ``double`` instead.

* The ``proc_ptr`` type was removed. Use a proper function pointer type.

* The ``rtems_context`` type was removed.  If you need this type in your
  applications, please ask on the :r:list:`devel`.

* The ``rtems_context_fp`` type was removed.  If you need this type in your
  applications, please ask on the :r:list:`devel`.

* The ``rtems_extension`` type was removed.  Use ``void`` instead.

* The ``rtems_io_lookup_name()`` directive was removed. Use ``stat()`` instead.

* The ``region_information_block`` type was removed. Use
  ``Heap_Information_block`` instead.

* The ``rtems_thread_cpu_usage_t`` type was removed. Use ``struct timespec``
  instead.

* The ``rtems_rate_monotonic_period_time_t`` type was removed. Use ``struct
  timespec`` instead.

* The ``_Copyright_Notice`` constant was removed from the API. Use
  ``rtems_get_copyright_notice()`` instead.

* The ``_RTEMS_version`` constant was removed from the API. Use
  ``rtems_get_version_string()`` instead.

* The ``RTEMS_MAXIMUM_NAME_LENGTH`` define was removed. Use
  ``sizeof( rtems_name )`` instead.

* The ``<rtems/system.h>`` header file was removed. Include ``<rtems.h>``
  instead.
