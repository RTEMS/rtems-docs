.. comment SPDX-License-Identifier: CC-BY-SA-4.0

Message Passing
###############

Data Definitions for Message Queues
===================================

Data Structures
---------------

NOTE: Semaphores are implemented but only unnamed semaphores
are currently tested.
.. code:: c

    mqd_t, Type, Implemented
    struct mq_attr, Type, Implemented

Message Passing Functions
=========================

Open a Message Queue
--------------------

.. code:: c

    mq_open(), Function, Implemented

Close a Message Queue
---------------------

.. code:: c

    mq_close(), Function, Implemented

Remove a Message Queue
----------------------

.. code:: c

    mq_unlink(), Function, Implemented

Send a Message to a Message Queue
---------------------------------

.. code:: c

    mq_send(), Function, Implemented

Receive a Message From a Message Queue
--------------------------------------

.. code:: c

    mq_receive(), Function, Implemented

Notify Process That a Message is Available on a Queue
-----------------------------------------------------

.. code:: c

    mq_notify(), Function, Implemented

Set Message Queue Attributes
----------------------------

.. code:: c

    mq_setattr(), Function, Implemented

Get Message Queue Attributes
----------------------------

.. code:: c

    mq_getattr(), Function, Implemented

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

