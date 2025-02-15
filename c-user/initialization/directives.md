.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2015, 2021 embedded brains GmbH & Co. KG
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

.. _InitializationManagerDirectives:

Directives
==========

This section details the directives of the Initialization Manager. A subsection
is dedicated to each of this manager's directives and lists the calling
sequence, parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/init/if/initialize-executive

.. raw:: latex

    \clearpage

.. index:: rtems_initialize_executive()
.. index:: initialize RTEMS
.. index:: start multitasking

.. _InterfaceRtemsInitializeExecutive:

rtems_initialize_executive()
----------------------------

Initializes the system and starts multitasking.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_initialize_executive( void );

.. rubric:: DESCRIPTION:

Iterates through the system initialization linker set and invokes the
registered handlers.  The final step is to start multitasking.

.. rubric:: NOTES:

Errors in the initialization sequence are usually fatal and lead to a system
termination.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive should be called by :c:func:`boot_card` only.

* The directive will not return to the caller.
