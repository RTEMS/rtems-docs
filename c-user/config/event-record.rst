.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

Event Recording Configuration
=============================

This section describes configuration options related to the event recording.

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

.. index:: CONFIGURE_RECORD_PER_PROCESSOR_ITEMS

.. _CONFIGURE_RECORD_PER_PROCESSOR_ITEMS:

CONFIGURE_RECORD_PER_PROCESSOR_ITEMS
------------------------------------

CONSTANT:
    ``CONFIGURE_RECORD_PER_PROCESSOR_ITEMS``

DATA TYPE:
    Unsigned integer (``unsigned int``).

RANGE:
    A power of two greater than or equal to 16.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    If defined, then a record item buffer of the specified item count is
    statically allocated for each configured processor
    (:ref:`CONFIGURE_MAXIMUM_PROCESSORS <CONFIGURE_MAXIMUM_PROCESSORS>`).

NOTES:
    None.
