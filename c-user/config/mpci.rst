.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH (http://www.embedded-brains.de)
.. Copyright (C) 1988, 2022 On-Line Applications Research Corporation (OAR)

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

.. Generated from spec:/acfg/if/group-mpci

Multiprocessing Configuration
=============================

This section describes multiprocessing related configuration options.
The options are only used if RTEMS was built when the multiprocessing
build configuration option is enabled. The multiprocessing configuration
is distinct from the SMP configuration.  Additionally, this class of
configuration options are only applicable if the configuration option
:ref:`CONFIGURE_MP_APPLICATION` is defined.  The multiprocessing (MPCI)
support must not be confused with the SMP support.

.. Generated from spec:/acfg/if/mp-extra-server-stack

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK

.. _CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK:

CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK
-----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 0.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the number of bytes the
applications wishes to add to the MPCI task stack on top of
:ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

.. rubric:: NOTES:

This configuration option is only evaluated if
:ref:`CONFIGURE_MP_APPLICATION` is defined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

* The value of the configuration option shall be small enough so that the MPCI
  receive server stack area calculation carried out by ``<rtems/confdefs.h>``
  does not overflow an integer of type `size_t
  <https://en.cppreference.com/w/c/types/size_t>`_.

.. Generated from spec:/acfg/if/mp-appl

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MP_APPLICATION

.. _CONFIGURE_MP_APPLICATION:

CONFIGURE_MP_APPLICATION
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MP_APPLICATION``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the multiprocessing services
are not initialized.

.. rubric:: DESCRIPTION:

This configuration option is defined to indicate that the application intends
to be part of a multiprocessing configuration.  Additional configuration
options are assumed to be provided.

.. rubric:: NOTES:

This configuration option shall be undefined if the multiprocessing support
is not enabled (e.g. RTEMS was built without the multiprocessing build
configuration option enabled).  Otherwise a compile time error in the
configuration file will occur.

.. Generated from spec:/acfg/if/mp-max-global-objects

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS

.. _CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS:

CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS
-----------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 32.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of
concurrently active global objects in a multiprocessor system.

.. rubric:: NOTES:

This value corresponds to the total number of objects which can be created
with the :c:macro:`RTEMS_GLOBAL` attribute.

This configuration option is only evaluated if
:ref:`CONFIGURE_MP_APPLICATION` is defined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/mp-max-nodes

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MP_MAXIMUM_NODES

.. _CONFIGURE_MP_MAXIMUM_NODES:

CONFIGURE_MP_MAXIMUM_NODES
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MP_MAXIMUM_NODES``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 2.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of nodes in
a multiprocessor system.

.. rubric:: NOTES:

This configuration option is only evaluated if
:ref:`CONFIGURE_MP_APPLICATION` is defined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/mp-max-proxies

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MP_MAXIMUM_PROXIES

.. _CONFIGURE_MP_MAXIMUM_PROXIES:

CONFIGURE_MP_MAXIMUM_PROXIES
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MP_MAXIMUM_PROXIES``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 32.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the maximum number of
concurrently active thread/task proxies on this node in a multiprocessor
system.

.. rubric:: NOTES:

Since a proxy is used to represent a remote task/thread which is blocking
on this node. This configuration parameter reflects the maximum number of
remote tasks/threads which can be blocked on objects on this node, see
:ref:`MPCIProxies`.

This configuration option is only evaluated if
:ref:`CONFIGURE_MP_APPLICATION` is defined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

.. Generated from spec:/acfg/if/mp-mpci-table-pointer

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MP_MPCI_TABLE_POINTER

.. _CONFIGURE_MP_MPCI_TABLE_POINTER:

CONFIGURE_MP_MPCI_TABLE_POINTER
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MP_MPCI_TABLE_POINTER``

.. rubric:: OPTION TYPE:

This configuration option is an initializer define.

.. rubric:: DEFAULT VALUE:

The default value is ``&MPCI_table``.

.. rubric:: DESCRIPTION:

The value of this configuration option initializes the MPCI Configuration
Table.

.. rubric:: NOTES:

RTEMS provides a Shared Memory MPCI Device Driver which can be used on any
Multiprocessor System assuming the BSP provides the proper set of
supporting methods.

This configuration option is only evaluated if
:ref:`CONFIGURE_MP_APPLICATION` is defined.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be a pointer to
:c:type:`rtems_mpci_table`.

.. Generated from spec:/acfg/if/mp-node-number

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_MP_NODE_NUMBER

.. _CONFIGURE_MP_NODE_NUMBER:

CONFIGURE_MP_NODE_NUMBER
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_MP_NODE_NUMBER``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is ``NODE_NUMBER``.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the node number of this node
in a multiprocessor system.

.. rubric:: NOTES:

In the RTEMS Multiprocessing Test Suite, the node number is derived from
the Makefile variable ``NODE_NUMBER``. The same code is compiled with the
``NODE_NUMBER`` set to different values. The test programs behave
differently based upon their node number.

This configuration option is only evaluated if
:ref:`CONFIGURE_MP_APPLICATION` is defined.

.. rubric:: CONSTRAINTS:

The following constraints apply to this configuration option:

* The value of the configuration option shall be greater than or equal to zero.

* The value of the configuration option shall be less than or equal to
  `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.
