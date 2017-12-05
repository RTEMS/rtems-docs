.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: Copyright 2015 embedded brains GmbH
.. COMMENT: All rights reserved.

.. index:: Status Codes

Directive Status Codes
**********************

Introduction
============

The directive status code directives are:

- rtems_status_text_ - Return the name for the status code

Directives
==========

The directives are:

.. index:: rtems_status_code

.. list-table::
 :class: rtems-table

 * - ``RTEMS_SUCCESSFUL``
   - successful completion
 * - ``RTEMS_TASK_EXITTED``
   - returned from a task
 * - ``RTEMS_MP_NOT_CONFIGURED``
   - multiprocessing not configured
 * - ``RTEMS_INVALID_NAME``
   - invalid object name
 * - ``RTEMS_INVALID_ID``
   - invalid object id
 * - ``RTEMS_TOO_MANY``
   - too many
 * - ``RTEMS_TIMEOUT``
   - timed out waiting
 * - ``RTEMS_OBJECT_WAS_DELETED``
   - object was deleted while waiting
 * - ``RTEMS_INVALID_SIZE``
   - invalid specified size
 * - ``RTEMS_INVALID_ADDRESS``
   - invalid address specified
 * - ``RTEMS_INVALID_NUMBER``
   - number was invalid
 * - ``RTEMS_NOT_DEFINED``
   - item not initialized
 * - ``RTEMS_RESOURCE_IN_USE``
   - resources outstanding
 * - ``RTEMS_UNSATISFIED``
   - request not satisfied
 * - ``RTEMS_INCORRECT_STATE``
   - task is in wrong state
 * - ``RTEMS_ALREADY_SUSPENDED``
   - task already in state
 * - ``RTEMS_ILLEGAL_ON_SELF``
   - illegal for calling task
 * - ``RTEMS_ILLEGAL_ON_REMOTE_OBJECT``
   - illegal for remote object
 * - ``RTEMS_CALLED_FROM_ISR``
   - invalid environment
 * - ``RTEMS_INVALID_PRIORITY``
   - invalid task priority
 * - ``RTEMS_INVALID_CLOCK``
   - invalid time buffer
 * - ``RTEMS_INVALID_NODE``
   - invalid node id
 * - ``RTEMS_NOT_CONFIGURED``
   - directive not configured
 * - ``RTEMS_NOT_OWNER_OF_RESOURCE``
   - not owner of resource
 * - ``RTEMS_NOT_IMPLEMENTED``
   - directive not implemented or feature not available in configuration
 * - ``RTEMS_INTERNAL_ERROR``
   - RTEMS inconsistency detected
 * - ``RTEMS_NO_MEMORY``
   - could not get enough memory

.. raw:: latex

   \clearpage

.. index:: rtems_status_text

.. _rtems_status_text:

STATUS_TEXT - Returns the enumeration name for a status code
------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        const char *rtems_status_text(
            rtems_status_code code
        );

DIRECTIVE STATUS CODES
    The status code enumeration name or "?" in case the status code is invalid.

DESCRIPTION:
    Returns the enumeration name for the specified status code.
