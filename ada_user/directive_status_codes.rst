Directive Status Codes
######################

Introduction
============

*``RTEMS.SUCCESSFUL`` - successful completion*

*``RTEMS.TASK_EXITTED`` - returned from a task*

*``RTEMS.MP_NOT_CONFIGURED`` - multiprocessing not configured*

*``RTEMS.INVALID_NAME`` - invalid object name*

*``RTEMS.INVALID_ID`` - invalid object id*

*``RTEMS.TOO_MANY`` - too many*

*``RTEMS.TIMEOUT`` - timed out waiting*

*``RTEMS.OBJECT_WAS_DELETED`` - object was deleted while waiting*

*``RTEMS.INVALID_SIZE`` - invalid specified size*

*``RTEMS.INVALID_ADDRESS`` - invalid address specified*

*``RTEMS.INVALID_NUMBER`` - number was invalid*

*``RTEMS.NOT_DEFINED`` - item not initialized*

*``RTEMS.RESOURCE_IN_USE`` - resources outstanding*

*``RTEMS.UNSATISFIED`` - request not satisfied*

*``RTEMS.INCORRECT_STATE`` - task is in wrong state*

*``RTEMS.ALREADY_SUSPENDED`` - task already in state*

*``RTEMS.ILLEGAL_ON_SELF`` - illegal for calling task*

*``RTEMS.ILLEGAL_ON_REMOTE_OBJECT`` - illegal for remote object*

*``RTEMS.CALLED_FROM_ISR`` - invalid environment*

*``RTEMS.INVALID_PRIORITY`` - invalid task priority*

*``RTEMS.INVALID_CLOCK`` - invalid time buffer*

*``RTEMS.INVALID_NODE`` - invalid node id*

*``RTEMS.NOT_CONFIGURED`` - directive not configured*

*``RTEMS.NOT_OWNER_OF_RESOURCE`` - not owner of resource*

*``RTEMS.NOT_IMPLEMENTED`` - directive not implemented*

*``RTEMS.INTERNAL_ERROR`` - RTEMS inconsistency detected*

*``RTEMS.NO_MEMORY`` - could not get enough memory*

Directives
==========

STATUS_TEXT - Returns the enumeration name for a status code
------------------------------------------------------------

**CALLING SEQUENCE:**

**DIRECTIVE STATUS CODES**

The status code enumeration name or "?" in case the status code is invalid.

**DESCRIPTION:**

Returns the enumeration name for the specified status code.

.. COMMENT: Copyright 2015 embedded brains GmbH

.. COMMENT: All rights reserved.


