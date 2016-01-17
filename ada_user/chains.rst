Chains
######

.. index:: chains

Introduction
============

The Chains API is an interface to the Super Core (score) chain
implementation. The Super Core uses chains for all list type
functions. This includes wait queues and task queues. The Chains API
provided by RTEMS is:

- build_id

- ``rtems.chain_node`` - Chain node used in user objects

- ``rtems.chain_control`` - Chain control node

- ``rtems.chain_initialize`` - initialize the chain with nodes

- ``rtems.chain_initialize_empty`` - initialize the chain as empty

- ``rtems.chain_is_null_node`` - Is the node NULL ?

- ``rtems.chain_head`` - Return the chain’s head

- ``rtems.chain_tail`` - Return the chain’s tail

- ``rtems.chain_are_nodes_equal`` - Are the node’s equal ?

- ``rtems.chain_is_empty`` - Is the chain empty ?

- ``rtems.chain_is_first`` - Is the Node the first in the chain ?

- ``rtems.chain_is_last`` - Is the Node the last in the chain ?

- ``rtems.chain_has_only_one_node`` - Does the node have one node ?

- ``rtems.chain_node_count_unprotected`` - Returns the node count of the chain (unprotected)

- ``rtems.chain_is_head`` - Is the node the head ?

- ``rtems.chain_is_tail`` - Is the node the tail ?

- ``rtems.chain_extract`` - Extract the node from the chain

- ``rtems.chain_extract_unprotected`` - Extract the node from the chain (unprotected)

- ``rtems.chain_get`` - Return the first node on the chain

- ``rtems.chain_get_unprotected`` - Return the first node on the chain (unprotected)

- ``rtems.chain_get_first_unprotected`` - Get the first node on the chain (unprotected)

- ``rtems.chain_insert`` - Insert the node into the chain

- ``rtems.chain_insert_unprotected`` - Insert the node into the chain (unprotected)

- ``rtems.chain_append`` - Append the node to chain

- ``rtems.chain_append_unprotected`` - Append the node to chain (unprotected)

- ``rtems.chain_prepend`` - Prepend the node to the end of the chain

- ``rtems.chain_prepend_unprotected`` - Prepend the node to chain (unprotected)

Background
==========

The Chains API maps to the Super Core Chains API. Chains are
implemented as a double linked list of nodes anchored to a control
node. The list starts at the control node and is terminated at the
control node. A node has previous and next pointers. Being a double
linked list nodes can be inserted and removed without the need to
travse the chain.

Chains have a small memory footprint and can be used in interrupt
service routines and are thread safe in a multi-threaded
environment. The directives list which operations disable interrupts.

Chains are very useful in Board Support packages and applications.

Nodes
-----

A chain is made up from nodes that orginate from a chain control
object. A node is of type ``rtems.chain_node``. The node
is designed to be part of a user data structure and a cast is used to
move from the node address to the user data structure address. For
example:
.. code:: c

    typedef struct foo
    {
    rtems.chain_node node;
    int              bar;
    } foo;

creates a type ``foo`` that can be placed on a chain. To get the
foo structure from the list you perform the following:
.. code:: c

    foo* get_foo(rtems.chain_control* control)
    {
    return (foo*) rtems.chain_get(control);
    }

The node is placed at the start of the user’s structure to allow the
node address on the chain to be easly cast to the user’s structure
address.

Controls
--------

A chain is anchored with a control object. Chain control provide the
user with access to the nodes on the chain. The control is head of the
node.

.. code:: c

    Control
    first ------------------------>
    permanent_null <--------------- NODE
    last ------------------------->

The implementation does not require special checks for manipulating
the first and last nodes on the chain. To accomplish this the``rtems.chain_control`` structure is treated as two
overlapping ``rtems.chain_node`` structures.  The
permanent head of the chain overlays a node structure on the first and``permanent_null`` fields.  The ``permanent_tail`` of the chain
overlays a node structure on the ``permanent_null`` and ``last``
elements of the structure.

Operations
==========

Multi-threading
---------------

Chains are designed to be used in a multi-threading environment. The
directives list which operations mask interrupts. Chains supports
tasks and interrupt service routines appending and extracting nodes
with out the need for extra locks. Chains how-ever cannot insure the
integrity of a chain for all operations. This is the responsibility of
the user. For example an interrupt service routine extracting nodes
while a task is iterating over the chain can have unpredictable
results.

Creating a Chain
----------------

To create a chain you need to declare a chain control then add nodes
to the control. Consider a user structure and chain control:
.. code:: c

    typedef struct foo
    {
    rtems.chain_node node;
    uint8_t char*    data;
    } foo;
    rtems.chain_control chain;

Add nodes with the following code:
.. code:: c

    rtems.chain_initialize_empty (&chain);
    for (i = 0; i < count; i++)
    {
    foo* bar = malloc (sizeof (foo));
    if (!bar)
    return -1;
    bar->data = malloc (size);
    rtems.chain_append (&chain, &bar->node);
    }

The chain is initialized and the nodes allocated and appended to the
chain. This is an example of a pool of buffers.

Iterating a Chain
-----------------
.. index:: chain iterate

Iterating a chain is a common function. The example shows how to
iterate the buffer pool chain created in the last section to find
buffers starting with a specific string. If the buffer is located it is
extracted from the chain and placed on another chain:
.. code:: c

    void foobar (const char*          match,
    rtems.chain_control* chain,
    rtems.chain_control* out)
    {
    rtems.chain_node* node;
    foo*              bar;
    rtems.chain_initialize_empty (out);
    node = chain->first;
    while (!rtems.chain_is_tail (chain, node))
    {
    bar = (foo*) node;
    rtems_chain_node* next_node = node->next;
    if (strcmp (match, bar->data) == 0)
    {
    rtems.chain_extract (node);
    rtems.chain_append (out, node);
    }
    node = next_node;
    }
    }

Directives
==========

The section details the Chains directives.

.. COMMENT: Initialize this Chain With Nodes

Initialize Chain With Nodes
---------------------------
.. index:: chain initialize

**CALLING SEQUENCE:**

**RETURNS**

Returns nothing.

**DESCRIPTION:**

This function take in a pointer to a chain control and initializes it
to contain a set of chain nodes.  The chain will contain ``number_nodes``
chain nodes from the memory pointed to by ``start_address``.  Each node
is assumed to be ``node_size`` bytes.

**NOTES:**

This call will discard any nodes on the chain.

This call does NOT inititialize any user data on each node.

.. COMMENT: Initialize this Chain as Empty

Initialize Empty
----------------
.. index:: chain initialize empty

**CALLING SEQUENCE:**

**RETURNS**

Returns nothing.

**DESCRIPTION:**

This function take in a pointer to a chain control and initializes it
to empty.

**NOTES:**

This call will discard any nodes on the chain.

Is Null Node ?
--------------
.. index:: chain is node null

**CALLING SEQUENCE:**

**RETURNS**

Returns ``true`` is the node point is NULL and ``false`` if the node is not
NULL.

**DESCRIPTION:**

Tests the node to see if it is a NULL returning ``true`` if a null.

Head
----
.. index:: chain get head

**CALLING SEQUENCE:**

**RETURNS**

Returns the permanent head node of the chain.

**DESCRIPTION:**

This function returns a pointer to the first node on the chain.

Tail
----
.. index:: chain get tail

**CALLING SEQUENCE:**

**RETURNS**

Returns the permanent tail node of the chain.

**DESCRIPTION:**

This function returns a pointer to the last node on the chain.

Are Two Nodes Equal ?
---------------------
.. index:: chare are nodes equal

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if the left node and the right node are
equal, and ``false`` otherwise.

**DESCRIPTION:**

This function returns ``true`` if the left node and the right node are
equal, and ``false`` otherwise.

Is the Chain Empty
------------------
.. index:: chain is chain empty

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if there a no nodes on the chain and ``false``
otherwise.

**DESCRIPTION:**

This function returns ``true`` if there a no nodes on the chain and ``false``
otherwise.

Is this the First Node on the Chain ?
-------------------------------------
.. index:: chain is node the first

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if the node is the first node on a chain
and ``false`` otherwise.

**DESCRIPTION:**

This function returns ``true`` if the node is the first node on a chain
and ``false`` otherwise.

Is this the Last Node on the Chain ?
------------------------------------
.. index:: chain is node the last

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if the node is the last node on a chain and``false`` otherwise.

**DESCRIPTION:**

This function returns ``true`` if the node is the last node on a chain and``false`` otherwise.

Does this Chain have only One Node ?
------------------------------------
.. index:: chain only one node

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if there is only one node on the chain and``false`` otherwise.

**DESCRIPTION:**

This function returns ``true`` if there is only one node on the chain and``false`` otherwise.

Returns the node count of the chain (unprotected)
-------------------------------------------------
.. index:: chain only one node

**CALLING SEQUENCE:**

**RETURNS**

This function returns the node count of the chain.

**DESCRIPTION:**

This function returns the node count of the chain.

Is this Node the Chain Head ?
-----------------------------
.. index:: chain is node the head

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if the node is the head of the chain and``false`` otherwise.

**DESCRIPTION:**

This function returns ``true`` if the node is the head of the chain and``false`` otherwise.

Is this Node the Chain Tail ?
-----------------------------
.. index:: chain is node the tail

**CALLING SEQUENCE:**

**RETURNS**

This function returns ``true`` if the node is the tail of the chain and``false`` otherwise.

**DESCRIPTION:**

This function returns ``true`` if the node is the tail of the chain and``false`` otherwise.

Extract a Node
--------------
.. index:: chain extract a node

**CALLING SEQUENCE:**

**RETURNS**

Returns nothing.

**DESCRIPTION:**

This routine extracts the node from the chain on which it resides.

**NOTES:**

Interrupts are disabled while extracting the node to ensure the
atomicity of the operation.

Use ``rtems.chain_extract_unprotected()`` to avoid disabling of
interrupts.

Get the First Node
------------------
.. index:: chain get first node

**CALLING SEQUENCE:**

**RETURNS**

Returns a pointer a node. If a node was removed, then a pointer to
that node is returned. If the chain was empty, then NULL is
returned.

**DESCRIPTION:**

This function removes the first node from the chain and returns a
pointer to that node.  If the chain is empty, then NULL is returned.

**NOTES:**

Interrupts are disabled while obtaining the node to ensure the
atomicity of the operation.

Use ``rtems.chain_get_unprotected()`` to avoid disabling of
interrupts.

Get the First Node (unprotected)
--------------------------------
.. index:: chain get first node

**CALLING SEQUENCE:**

**RETURNS:**

A pointer to the former first node is returned.

**DESCRIPTION:**

Removes the first node from the chain and returns a pointer to it.  In case the
chain was empty, then the results are unpredictable.

**NOTES:**

The function does nothing to ensure the atomicity of the operation.

Insert a Node
-------------
.. index:: chain insert a node

**CALLING SEQUENCE:**

**RETURNS**

Returns nothing.

**DESCRIPTION:**

This routine inserts a node on a chain immediately following the
specified node.

**NOTES:**

Interrupts are disabled during the insert to ensure the atomicity of
the operation.

Use ``rtems.chain_insert_unprotected()`` to avoid disabling of
interrupts.

Append a Node
-------------
.. index:: chain append a node

**CALLING SEQUENCE:**

**RETURNS**

Returns nothing.

**DESCRIPTION:**

This routine appends a node to the end of a chain.

**NOTES:**

Interrupts are disabled during the append to ensure the atomicity of
the operation.

Use ``rtems.chain_append_unprotected()`` to avoid disabling of
interrupts.

Prepend a Node
--------------
.. index:: prepend node

**CALLING SEQUENCE:**

**RETURNS**

Returns nothing.

**DESCRIPTION:**

This routine prepends a node to the front of the chain.

**NOTES:**

Interrupts are disabled during the prepend to ensure the atomicity of
the operation.

Use ``rtems.chain_prepend_unprotected()`` to avoid disabling of
interrupts.

.. COMMENT: Copyright 2014 Gedare Bloom.

.. COMMENT: All rights reserved.

