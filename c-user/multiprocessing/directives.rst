.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Directives
==========

This section details the additional directives required to support RTEMS in a
multiprocessor configuration.  A subsection is dedicated to each of this
manager's directives and describes the calling sequence, related constants,
usage, and status codes.

.. raw:: latex

   \clearpage

.. index:: announce arrival of package
.. index:: rtems_multiprocessing_announce

.. _rtems_multiprocessing_announce:

MULTIPROCESSING_ANNOUNCE - Announce the arrival of a packet
-----------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        void rtems_multiprocessing_announce( void );

DIRECTIVE STATUS CODES:
    NONE

DESCRIPTION:
    This directive informs RTEMS that a multiprocessing communications packet
    has arrived from another node.  This directive is called by the
    user-provided MPCI, and is only used in multiprocessor configurations.

NOTES:
    This directive is typically called from an ISR.

    This directive will almost certainly cause the calling task to be
    preempted.

    This directive does not generate activity on remote nodes.
