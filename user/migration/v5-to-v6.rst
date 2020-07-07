.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. _Migration_5_to_6:

RTEMS 5 to RTEMS 6
==================

This section provides helpful information when migrating from RTEMS 5 to
RTEMS 6.

Update to GCC 10
----------------

The tool suite for RTEMS 6 uses GCC 10.  GCC 10 enables ``-fno-common`` by
default.  Code bases which never used this option before may observe now
multiple definition linker errors.  For example, if global variables are
declared and defined in header files (usually a missing ``extern`` in the header
file).
