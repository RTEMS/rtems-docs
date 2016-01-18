Red-Black Trees
###############

.. index:: rbtrees

Introduction
============

The Red-Black Tree API is an interface to the SuperCore (score) rbtree
implementation. Within RTEMS, red-black trees are used when a binary search
tree is needed, including dynamic priority thread queues and non-contiguous
heap memory. The Red-Black Tree API provided by RTEMS is:

- build_id

- ``rtems_rtems_rbtree_node`` - Red-Black Tree node embedded in another struct

- ``rtems_rtems_rbtree_control`` - Red-Black Tree control node for an entire tree

- ``rtems_rtems_rbtree_initialize`` - initialize the red-black tree with nodes

- ``rtems_rtems_rbtree_initialize_empty`` - initialize the red-black tree as empty

- ``rtems_rtems_rbtree_set_off_tree`` - Clear a node’s links

- ``rtems_rtems_rbtree_root`` - Return the red-black tree’s root node

- ``rtems_rtems_rbtree_min`` - Return the red-black tree’s minimum node

- ``rtems_rtems_rbtree_max`` - Return the red-black tree’s maximum node

- ``rtems_rtems_rbtree_left`` - Return a node’s left child node

- ``rtems_rtems_rbtree_right`` - Return a node’s right child node

- ``rtems_rtems_rbtree_parent`` - Return a node’s parent node

- ``rtems_rtems_rbtree_are_nodes_equal`` - Are the node’s equal ?

- ``rtems_rtems_rbtree_is_empty`` - Is the red-black tree empty ?

- ``rtems_rtems_rbtree_is_min`` - Is the Node the minimum in the red-black tree ?

- ``rtems_rtems_rbtree_is_max`` - Is the Node the maximum in the red-black tree ?

- ``rtems_rtems_rbtree_is_root`` - Is the Node the root of the red-black tree ?

- ``rtems_rtems_rbtree_find`` - Find the node with a matching key in the red-black tree

- ``rtems_rtems_rbtree_predecessor`` - Return the in-order predecessor of a node.

- ``rtems_rtems_rbtree_successor`` - Return the in-order successor of a node.

- ``rtems_rtems_rbtree_extract`` - Remove the node from the red-black tree

- ``rtems_rtems_rbtree_get_min`` - Remove the minimum node from the red-black tree

- ``rtems_rtems_rbtree_get_max`` - Remove the maximum node from the red-black tree

- ``rtems_rtems_rbtree_peek_min`` - Returns the minimum node from the red-black tree

- ``rtems_rtems_rbtree_peek_max`` - Returns the maximum node from the red-black tree

- ``rtems_rtems_rbtree_insert`` - Add the node to the red-black tree

Background
==========

The Red-Black Trees API is a thin layer above the SuperCore Red-Black Trees
implementation. A Red-Black Tree is defined by a control node with pointers to
the root, minimum, and maximum nodes in the tree. Each node in the tree
consists of a parent pointer, two children pointers, and a color attribute.  A
tree is parameterized as either unique, meaning identical keys are rejected, or
not, in which case duplicate keys are allowed.

Users must provide a comparison functor that gets passed to functions that need
to compare nodes. In addition, no internal synchronization is offered within
the red-black tree implementation, thus users must ensure at most one thread
accesses a red-black tree instance at a time.

Nodes
-----

A red-black tree is made up from nodes that orginate from a red-black tree control
object. A node is of type ``rtems_rtems_rbtree_node``. The node
is designed to be part of a user data structure. To obtain the encapsulating
structure users can use the ``RTEMS_CONTAINER_OF`` macro.
The node can be placed anywhere within the user’s structure and the macro will
calculate the structure’s address from the node’s address.

Controls
--------

A red-black tree is rooted with a control object. Red-Black Tree control
provide the user with access to the nodes on the red-black tree.  The
implementation does not require special checks for manipulating the root of the
red-black tree. To accomplish this the``rtems_rtems_rbtree_control`` structure is treated as a``rtems_rtems_rbtree_node`` structure with a ``NULL`` parent
and left child pointing to the root.

Operations
==========

Examples for using the red-black trees
can be found in the testsuites/sptests/sprbtree01/init.c file.

Directives
==========

Documentation for the Red-Black Tree Directives
-----------------------------------------------
.. index:: rbtree doc

Source documentation for the Red-Black Tree API can be found in the
generated Doxygen output for cpukit/sapi.

.. COMMENT: COPYRIGHT (c) 1988-2012.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

