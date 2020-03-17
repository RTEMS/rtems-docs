.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Multiprocessing Configuration
=============================

This section describes multiprocessing related configuration options.  The
options are only used if RTEMS was built with the ``--enable-multiprocessing``
build configuration option.  Additionally, this class of configuration options
are only applicable if the configuration option :ref:`CONFIGURE_MP_APPLICATION`
is defined.  The multiprocessing (MPCI) support must not be confused with the
SMP support.

.. index:: CONFIGURE_MP_APPLICATION

.. _CONFIGURE_MP_APPLICATION:

CONFIGURE_MP_APPLICATION
------------------------

CONSTANT:
    ``CONFIGURE_MP_APPLICATION``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    This configuration parameter must be defined to indicate that the
    application intends to be part of a multiprocessing
    configuration. Additional configuration parameters are assumed to be
    provided.

NOTES:
    This has no impact unless RTEMS was built with the
    ``--enable-multiprocessing`` build configuration option.

.. index:: CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS

.. _CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS:

CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS
-----------------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 32.

DESCRIPTION:
    ``CONFIGURE_MP_MAXIMUM_GLOBAL_OBJECTS`` is the maximum number of
    concurrently active global objects in a multiprocessor system.

NOTES:
    This value corresponds to the total number of objects which can be created
    with the ``RTEMS_GLOBAL`` attribute.

.. index:: CONFIGURE_MP_MAXIMUM_NODES

.. _CONFIGURE_MP_MAXIMUM_NODES:

CONFIGURE_MP_MAXIMUM_NODES
--------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_NODES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is 2.

DESCRIPTION:
    ``CONFIGURE_MP_MAXIMUM_NODES`` is the maximum number of nodes in a
    multiprocessor system.

NOTES:
    None.

.. index:: CONFIGURE_MP_MAXIMUM_PROXIES

.. _CONFIGURE_MP_MAXIMUM_PROXIES:

CONFIGURE_MP_MAXIMUM_PROXIES
----------------------------

CONSTANT:
    ``CONFIGURE_MP_MAXIMUM_PROXIES``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Undefined or positive.

DEFAULT VALUE:
    The default value is 32.

DESCRIPTION:
    ``CONFIGURE_MP_MAXIMUM_PROXIES`` is the maximum number of concurrently
    active thread/task proxies on this node in a multiprocessor system.

NOTES:
    Since a proxy is used to represent a remote task/thread which is blocking
    on this node. This configuration parameter reflects the maximum number of
    remote tasks/threads which can be blocked on objects on this node, see
    :ref:`MPCIProxies`.

.. index:: CONFIGURE_MP_MPCI_TABLE_POINTER

.. _CONFIGURE_MP_MPCI_TABLE_POINTER:

CONFIGURE_MP_MPCI_TABLE_POINTER
-------------------------------

CONSTANT:
    ``CONFIGURE_MP_MPCI_TABLE_POINTER``

DATA TYPE:
    pointer to ``rtems_mpci_table``

RANGE:
    undefined or valid pointer

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    ``CONFIGURE_MP_MPCI_TABLE_POINTER`` is the pointer to the MPCI
    Configuration Table.  The default value of this field is``&MPCI_table``.

NOTES:
    RTEMS provides a Shared Memory MPCI Device Driver which can be used on any
    Multiprocessor System assuming the BSP provides the proper set of
    supporting methods.

.. index:: CONFIGURE_MP_NODE_NUMBER

.. _CONFIGURE_MP_NODE_NUMBER:

CONFIGURE_MP_NODE_NUMBER
------------------------

CONSTANT:
    ``CONFIGURE_MP_NODE_NUMBER``

DATA TYPE:
    Unsigned integer (``uint32_t``).

RANGE:
    Positive.

DEFAULT VALUE:
    The default value is ``NODE_NUMBER``, which is assumed to be set by the
    compilation environment.

DESCRIPTION:
    ``CONFIGURE_MP_NODE_NUMBER`` is the node number of this node in a
    multiprocessor system.

NOTES:
    In the RTEMS Multiprocessing Test Suite, the node number is derived from
    the Makefile variable ``NODE_NUMBER``. The same code is compiled with the
    ``NODE_NUMBER`` set to different values. The test programs behave
    differently based upon their node number.
