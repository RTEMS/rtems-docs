.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

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

.. Generated from spec:/acfg/if/group-eventrecord

Event Recording Configuration
=============================

This section describes configuration options related to the event recording.

.. Generated from spec:/acfg/if/record-extensions-enabled

.. index:: CONFIGURE_RECORD_EXTENSIONS_ENABLED

.. _CONFIGURE_RECORD_EXTENSIONS_ENABLED:

CONFIGURE_RECORD_EXTENSIONS_ENABLED
-----------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_EXTENSIONS_ENABLED``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case

    * this configuration option is defined

    * and :ref:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,

    then the event record extensions are enabled.

NOTES:
    The record extensions capture thread create, start, restart, delete, switch,
    begin, exitted and terminate events.

.. Generated from spec:/acfg/if/record-fatal-dump-base64

.. index:: CONFIGURE_RECORD_FATAL_DUMP_BASE64

.. _CONFIGURE_RECORD_FATAL_DUMP_BASE64:

CONFIGURE_RECORD_FATAL_DUMP_BASE64
----------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_FATAL_DUMP_BASE64``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case

    * this configuration option is defined

    * and :ref:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,

    * and :ref:`CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB` is undefined,

    then the event records are dumped in Base64 encoding in a fatal error
    extension (see :ref:`Terminate`).

NOTES:
    This extension can be used to produce crash dumps.

.. Generated from spec:/acfg/if/record-fatal-dump-base64-zlib

.. index:: CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB

.. _CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB:

CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB
---------------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case

    * this configuration option is defined

    * and :ref:`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,

    then the event records are compressed by zlib and dumped in Base64 encoding
    in a fatal error extension (see :ref:`Terminate`).

NOTES:
    The zlib compression needs about 512KiB of RAM.  This extension can be used
    to produce crash dumps.

.. Generated from spec:/acfg/if/record-per-processor-items

.. index:: CONFIGURE_RECORD_PER_PROCESSOR_ITEMS

.. _CONFIGURE_RECORD_PER_PROCESSOR_ITEMS:

CONFIGURE_RECORD_PER_PROCESSOR_ITEMS
------------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_PER_PROCESSOR_ITEMS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 16.

    * It shall be less than or equal to `SIZE_MAX <https://en.cppreference.com/w/c/types/limits>`_.

    * It shall be a power of two.

    * It shall be less than or equal to a
      BSP-specific and application-specific value which depends on the size of the
      memory available to the application.

DESCRIPTION:
    The value of this configuration option defines the event record item count
    per processor.

NOTES:
    The event record buffers are statically allocated for each configured
    processor (:ref:`CONFIGURE_MAXIMUM_PROCESSORS`).  If the value of this
    configuration option is zero, then nothing is allocated.
