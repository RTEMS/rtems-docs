.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
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

.. Generated from spec:/acfg/if/group-mpci

Multiprocessing Configuration
=============================

This section describes multiprocessing related configuration options.  The
options are only used if RTEMS was built with the ``--enable-multiprocessing``
build configuration option.  Additionally, this class of configuration options
are only applicable if the configuration option :ref:`CONFIGURE_MP_APPLICATION`
is defined.  The multiprocessing (MPCI) support must not be confused with the
SMP support.

.. Generated from spec:/acfg/if/mp-extra-server-stack

.. index:: CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK

.. _CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK:

CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK
-----------------------------------------

CONSTANT:
    ``CONFIGURE_EXTRA_MPCI_RECEIVE_SERVER_STACK``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 0.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to 0.

    * It shall be less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

    * It shall be small enough so that the
      MPCI receive server stack area calculation carried out by
      ``<rtems/confdefs.h>`` does not overflow an integer of type
      `size_t <https://en.cppreference.com/w/c/types/size_t>`_.

DESCRIPTION:
    The value of this configuration option defines the number of bytes the
    applications wishes to add to the MPCI task stack on top of
    :ref:`CONFIGURE_MINIMUM_TASK_STACK_SIZE`.

NOTES:
    This configuration option is only evaluated if
    :ref:`CONFIGURE_MP_APPLICATION` is defined.

.. Generated from spec:/acfg/if/mp-appl

.. index:: CONFIGURE_MP_APPLICATION

.. _CONFIGURE_MP_APPLICATION:

CONFIGURE_MP_APPLICATION
------------------------

CONSTANT:
    ``CONFIGURE_MP_APPLICATION``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the multiprocessing services
    are not initialized.

DESCRIPTION:
    This configuration option is defined to indicate that the application intends
    to be part of a multiprocessing configuration.  Additional configuration
    options are assumed to be provided.

NOTES:
    This configuration option shall be undefined if the multiprocessing support
    is not enabled (e.g. RTEMS was built without the ``--enable-multiprocessing``
    build configuration option).  Otherwise a compile time error in the
    configuration file will occur.

.. Generated from spec:/acfg/if/mp-max-global-objects

.. index:: CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS

.. _CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS:

CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS
-----------------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 32.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the maximum number of
    concurrently active global objects in a multiprocessor system.

NOTES:
    This value corresponds to the total number of objects which can be created
    with the :c:macro:`RTEMS_GLOBAL` attribute.

    This configuration option is only evaluated if
    :ref:`CONFIGURE_MP_APPLICATION` is defined.

.. Generated from spec:/acfg/if/mp-max-nodes

.. index:: CONFIGURE_MP_MAXIMUM_NODES

.. _CONFIGURE_MP_MAXIMUM_NODES:

CONFIGURE_MP_MAXIMUM_NODES
--------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_NODES``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 2.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the maximum number of nodes in
    a multiprocessor system.

NOTES:
    This configuration option is only evaluated if
    :ref:`CONFIGURE_MP_APPLICATION` is defined.

.. Generated from spec:/acfg/if/mp-max-proxies

.. index:: CONFIGURE_MP_MAXIMUM_PROXIES

.. _CONFIGURE_MP_MAXIMUM_PROXIES:

CONFIGURE_MP_MAXIMUM_PROXIES
----------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_PROXIES``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 32.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the maximum number of
    concurrently active thread/task proxies on this node in a multiprocessor
    system.

NOTES:
    Since a proxy is used to represent a remote task/thread which is blocking
    on this node. This configuration parameter reflects the maximum number of
    remote tasks/threads which can be blocked on objects on this node, see
    :ref:`MPCIProxies`.

    This configuration option is only evaluated if
    :ref:`CONFIGURE_MP_APPLICATION` is defined.

.. Generated from spec:/acfg/if/mp-mpci-table-pointer

.. index:: CONFIGURE_MP_MPCI_TABLE_POINTER

.. _CONFIGURE_MP_MPCI_TABLE_POINTER:

CONFIGURE_MP_MPCI_TABLE_POINTER
-------------------------------

CONSTANT:
    ``CONFIGURE_MP_MPCI_TABLE_POINTER``

OPTION TYPE:
    This configuration option is an initializer define.

DEFAULT VALUE:
    The default value is ``&MPCI_table``.

VALUE CONSTRAINTS:
    The value of this configuration option shall be a pointer to
    :c:type:`rtems_mpci_table`.

DESCRIPTION:
    The value of this configuration option initializes the MPCI Configuration
    Table.

NOTES:
    RTEMS provides a Shared Memory MPCI Device Driver which can be used on any
    Multiprocessor System assuming the BSP provides the proper set of
    supporting methods.

    This configuration option is only evaluated if
    :ref:`CONFIGURE_MP_APPLICATION` is defined.

.. Generated from spec:/acfg/if/mp-node-number

.. index:: CONFIGURE_MP_NODE_NUMBER

.. _CONFIGURE_MP_NODE_NUMBER:

CONFIGURE_MP_NODE_NUMBER
------------------------

CONSTANT:
    ``CONFIGURE_MP_NODE_NUMBER``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is ``NODE_NUMBER``.

VALUE CONSTRAINTS:
    The value of this configuration option shall be greater than or equal to 0
    and less than or equal to `UINT32_MAX <https://en.cppreference.com/w/c/types/integer>`_.

DESCRIPTION:
    The value of this configuration option defines the node number of this node
    in a multiprocessor system.

NOTES:
    In the RTEMS Multiprocessing Test Suite, the node number is derived from
    the Makefile variable ``NODE_NUMBER``. The same code is compiled with the
    ``NODE_NUMBER`` set to different values. The test programs behave
    differently based upon their node number.

    This configuration option is only evaluated if
    :ref:`CONFIGURE_MP_APPLICATION` is defined.
