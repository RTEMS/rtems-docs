.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH (http://www.embedded-brains.de)

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
