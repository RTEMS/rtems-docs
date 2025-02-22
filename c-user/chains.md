% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2014 Gedare Bloom

```{index} chains
```

# Chains

## Introduction

The Chains API is an interface to the Super Core (score) chain
implementation. The Super Core uses chains for all list type functions. This
includes wait queues and task queues. The Chains API provided by RTEMS is:

- [rtems_chain_initialize] - initialize the chain with nodes
- [rtems_chain_initialize_empty] - initialize the chain as empty
- [rtems_chain_is_null_node] - Is the node NULL ?
- [rtems_chain_head] - Return the chain's head
- [rtems_chain_tail] - Return the chain's tail
- [rtems_chain_are_nodes_equal] - Are the node's equal ?
- [rtems_chain_is_empty] - Is the chain empty ?
- [rtems_chain_is_first] - Is the Node the first in the chain ?
- [rtems_chain_is_last] - Is the Node the last in the chain ?
- [rtems_chain_has_only_one_node] - Does the node have one node ?
- [rtems_chain_node_count_unprotected] - Returns the node count of the chain (unprotected)
- [rtems_chain_is_head] - Is the node the head ?
- [rtems_chain_is_tail] - Is the node the tail ?
- [rtems_chain_extract] - Extract the node from the chain
- [rtems_chain_extract_unprotected] - Extract the node from the chain (unprotected)
- [rtems_chain_get] - Return the first node on the chain
- [rtems_chain_get_unprotected] - Return the first node on the chain (unprotected)
- [rtems_chain_insert] - Insert the node into the chain
- [rtems_chain_insert_unprotected] - Insert the node into the chain (unprotected)
- [rtems_chain_append] - Append the node to chain
- [rtems_chain_append_unprotected] - Append the node to chain (unprotected)
- [rtems_chain_prepend] - Prepend the node to the end of the chain
- [rtems_chain_prepend_unprotected] - Prepend the node to chain (unprotected)

## Background

The Chains API maps to the Super Core Chains API. Chains are implemented as a
double linked list of nodes anchored to a control node. The list starts at the
control node and is terminated at the control node. A node has previous and
next pointers. Being a double linked list nodes can be inserted and removed
without the need to travse the chain.

Chains have a small memory footprint and can be used in interrupt service
routines and are thread safe in a multi-threaded environment. The directives
list which operations disable interrupts.

Chains are very useful in Board Support packages and applications.

### Nodes

A chain is made up from nodes that orginate from a chain control object. A node
is of type `rtems_chain_node`. The node is designed to be part of a user data
structure and a cast is used to move from the node address to the user data
structure address. For example:

```c
typedef struct foo
{
    rtems_chain_node node;
    int              bar;
} foo;
```

creates a type `foo` that can be placed on a chain. To get the foo structure
from the list you perform the following:

```c
foo* get_foo(rtems_chain_control* control)
{
    return (foo*) rtems_chain_get(control);
}
```

The node is placed at the start of the user's structure to allow the node
address on the chain to be easly cast to the user's structure address.

### Controls

A chain is anchored with a control object. Chain control provide the user with
access to the nodes on the chain. The control is head of the node.

```c
[Control]
first ------------------------>
permanent_null <--------------- [NODE]
last ------------------------->
```

The implementation does not require special checks for manipulating the first
and last nodes on the chain. To accomplish this the `rtems_chain_control`
structure is treated as two overlapping `rtems_chain_node` structures. The
permanent head of the chain overlays a node structure on the first and
`permanent_null` fields. The `permanent_tail` of the chain overlays a node
structure on the `permanent_null` and `last` elements of the structure.

## Operations

### Multi-threading

Chains are designed to be used in a multi-threading environment. The directives
list which operations mask interrupts. Chains supports tasks and interrupt
service routines appending and extracting nodes with out the need for extra
locks. Chains how-ever cannot insure the integrity of a chain for all
operations. This is the responsibility of the user. For example an interrupt
service routine extracting nodes while a task is iterating over the chain can
have unpredictable results.

### Creating a Chain

To create a chain you need to declare a chain control then add nodes
to the control. Consider a user structure and chain control:

```c
typedef struct foo
{
    rtems_chain_node node;
    char*            data;
} foo;
rtems_chain_control chain;
```

Add nodes with the following code:

```c
rtems_chain_initialize_empty (&chain);

for (i = 0; i < count; i++)
{
    foo* bar = malloc (sizeof (foo));
    if (!bar)
        return -1;
    bar->data = malloc (size);
    rtems_chain_append (&chain, &bar->node);
}
```

The chain is initialized and the nodes allocated and appended to the
chain. This is an example of a pool of buffers.

```{index} chain iterate
```

### Iterating a Chain

Iterating a chain is a common function. The example shows how to iterate the
buffer pool chain created in the last section to find buffers starting with a
specific string. If the buffer is located it is extracted from the chain and
placed on another chain:

```c
void foobar (const char*          match,
             rtems_chain_control* chain,
             rtems_chain_control* out)
{
    rtems_chain_node* node;
    foo*              bar;

    rtems_chain_initialize_empty (out);

    node = rtems_chain_first (chain);

    while (!rtems_chain_is_tail (chain, node))
    {
        bar = (foo*) node;
        rtems_chain_node* next_node = rtems_chain_next(node);
        if (strcmp (match, bar->data) == 0)
        {
            rtems_chain_extract (node);
            rtems_chain_append (out, node);
        }
        node = next_node;
    }
}
```

## Directives

The section details the Chains directives.

% COMMENT: Initialize this Chain With Nodes

```{raw} latex
\clearpage
```

(rtems-chain-initialize)=

```{index} chain initialize
```

```{index} rtems_chain_initialize()
```

### Initialize Chain With Nodes

CALLING SEQUENCE:
: ```c
  void rtems_chain_initialize(
      rtems_chain_control *the_chain,
      void                *starting_address,
      size_t               number_nodes,
      size_t               node_size
  )
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This function take in a pointer to a chain control and initializes it to
  contain a set of chain nodes. The chain will contain `number_nodes`
  chain nodes from the memory pointed to by `start_address`. Each node is
  assumed to be `node_size` bytes.

NOTES:

: This call will discard any nodes on the chain.

  This call does NOT inititialize any user data on each node.

% COMMENT: Initialize this Chain as Empty

```{raw} latex
\clearpage
```

(rtems-chain-initialize-empty)=

```{index} chain initialize empty
```

```{index} rtems_chain_initialize_empty()
```

### Initialize Empty

CALLING SEQUENCE:
: ```c
  void rtems_chain_initialize_empty(
      rtems_chain_control *the_chain
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This function take in a pointer to a chain control and initializes it to
  empty.

NOTES:

: This call will discard any nodes on the chain.

```{raw} latex
\clearpage
```

(rtems-chain-is-null-node)=

```{index} chain is node null
```

```{index} rtems_chain_is_null_node()
```

### Is Null Node ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_is_null_node(
      const rtems_chain_node *the_node
  );
  ```

RETURNS:

: Returns `true` is the node point is NULL and `false` if the node is not
  NULL.

DESCRIPTION:

: Tests the node to see if it is a NULL returning `true` if a null.

```{raw} latex
\clearpage
```

(rtems-chain-head)=

```{index} chain get head
```

```{index} rtems_chain_head()
```

### Head

CALLING SEQUENCE:
: ```c
  rtems_chain_node *rtems_chain_head(
      rtems_chain_control *the_chain
  )
  ```

RETURNS:

: Returns the permanent head node of the chain.

DESCRIPTION:

: This function returns a pointer to the first node on the chain.

```{raw} latex
\clearpage
```

(rtems-chain-tail)=

```{index} chain get tail
```

```{index} rtems_chain_tail()
```

### Tail

CALLING SEQUENCE:
: ```c
  rtems_chain_node *rtems_chain_tail(
      rtems_chain_control *the_chain
  );
  ```

RETURNS:

: Returns the permanent tail node of the chain.

DESCRIPTION:

: This function returns a pointer to the last node on the chain.

```{raw} latex
\clearpage
```

(rtems-chain-are-nodes-equal)=

```{index} chare are nodes equal
```

```{index} rtems_chain_are_nodes_equal()
```

### Are Two Nodes Equal ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_are_nodes_equal(
      const rtems_chain_node *left,
      const rtems_chain_node *right
  );
  ```

RETURNS:

: This function returns `true` if the left node and the right node are
  equal, and `false` otherwise.

DESCRIPTION:

: This function returns `true` if the left node and the right node are
  equal, and `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-is-empty)=

```{index} chain is chain empty
```

```{index} rtems_chain_is_empty()
```

### Is the Chain Empty

CALLING SEQUENCE:
: ```c
  bool rtems_chain_is_empty(
      rtems_chain_control *the_chain
  );
  ```

RETURNS:

: This function returns `true` if there a no nodes on the chain and
  `false` otherwise.

DESCRIPTION:

: This function returns `true` if there a no nodes on the chain and
  `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-is-first)=

```{index} chain is node the first
```

```{index} rtems_chain_is_first()
```

### Is this the First Node on the Chain ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_is_first(
      const rtems_chain_node *the_node
  );
  ```

RETURNS:

: This function returns `true` if the node is the first node on a chain and
  `false` otherwise.

DESCRIPTION:

: This function returns `true` if the node is the first node on a chain and
  `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-is-last)=

```{index} chain is node the last
```

```{index} rtems_chain_is_last()
```

### Is this the Last Node on the Chain ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_is_last(
      const rtems_chain_node *the_node
  );
  ```

RETURNS:

: This function returns `true` if the node is the last node on a chain and
  `false` otherwise.

DESCRIPTION:

: This function returns `true` if the node is the last node on a chain and
  `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-has-only-one-node)=

```{index} chain only one node
```

```{index} rtems_chain_has_only_one_node()
```

### Does this Chain have only One Node ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_has_only_one_node(
      const rtems_chain_control *the_chain
  );
  ```

RETURNS:

: This function returns `true` if there is only one node on the chain and
  `false` otherwise.

DESCRIPTION:

: This function returns `true` if there is only one node on the chain and
  `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-node-count-unprotected)=

```{index} chain only one node
```

```{index} rtems_chain_node_count_unprotected()
```

### Returns the node count of the chain (unprotected)

CALLING SEQUENCE:
: ```c
  size_t rtems_chain_node_count_unprotected(
      const rtems_chain_control *the_chain
  );
  ```

RETURNS:

: This function returns the node count of the chain.

DESCRIPTION:

: This function returns the node count of the chain.

```{raw} latex
\clearpage
```

(rtems-chain-is-head)=

```{index} chain is node the head
```

```{index} rtems_chain_is_head()
```

### Is this Node the Chain Head ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_is_head(
      rtems_chain_control    *the_chain,
      rtems_const chain_node *the_node
  );
  ```

RETURNS:

: This function returns `true` if the node is the head of the chain and
  `false` otherwise.

DESCRIPTION:

: This function returns `true` if the node is the head of the chain and
  `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-is-tail)=

```{index} chain is node the tail
```

```{index} rtems_chain_is_tail()
```

### Is this Node the Chain Tail ?

CALLING SEQUENCE:
: ```c
  bool rtems_chain_is_tail(
      rtems_chain_control    *the_chain,
      const rtems_chain_node *the_node
  )
  ```

RETURNS:

: This function returns `true` if the node is the tail of the chain and
  `false` otherwise.

DESCRIPTION:

: This function returns `true` if the node is the tail of the chain and
  `false` otherwise.

```{raw} latex
\clearpage
```

(rtems-chain-extract)=

```{index} chain extract a node
```

```{index} rtems_chain_extract()
```

### Extract a Node

CALLING SEQUENCE:
: ```c
  void rtems_chain_extract(
      rtems_chain_node *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine extracts the node from the chain on which it resides.

NOTES:

: Interrupts are disabled while extracting the node to ensure the atomicity
  of the operation.

  Use `rtems_chain_extract_unprotected` to avoid disabling of interrupts.

```{raw} latex
\clearpage
```

(rtems-chain-extract-unprotected)=

```{index} chain extract a node unprotected
```

```{index} rtems_chain_extract_unprotected()
```

### Extract a Node (unprotected)

CALLING SEQUENCE:
: ```c
  void rtems_chain_extract_unprotected(
      rtems_chain_node *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine extracts the node from the chain on which it resides.

NOTES:

: The function does nothing to ensure the atomicity of the operation.

```{raw} latex
\clearpage
```

(rtems-chain-get)=

```{index} chain get first node
```

```{index} rtems_chain_get()
```

### Get the First Node

CALLING SEQUENCE:
: ```c
  rtems_chain_node *rtems_chain_get(
      rtems_chain_control *the_chain
  );
  ```

RETURNS:

: Returns a pointer a node. If a node was removed, then a pointer to that
  node is returned. If the chain was empty, then `NULL` is returned.

DESCRIPTION:

: This function removes the first node from the chain and returns a pointer
  to that node. If the chain is empty, then `NULL` is returned.

NOTES:

: Interrupts are disabled while obtaining the node to ensure the atomicity of
  the operation.

  Use `rtems_chain_get_unprotected()` to avoid disabling of interrupts.

```{raw} latex
\clearpage
```

(rtems-chain-get-unprotected)=

```{index} chain get first node
```

```{index} rtems_chain_get_unprotected()
```

### Get the First Node (unprotected)

CALLING SEQUENCE:
: ```c
  rtems_chain_node *rtems_chain_get_unprotected(
      rtems_chain_control *the_chain
  );
  ```

RETURNS:

: A pointer to the former first node is returned.

DESCRIPTION:

: Removes the first node from the chain and returns a pointer to it. In case
  the chain was empty, then the results are unpredictable.

NOTES:

: The function does nothing to ensure the atomicity of the operation.

```{raw} latex
\clearpage
```

(rtems-chain-insert)=

```{index} chain insert a node
```

```{index} rtems_chain_insert()
```

### Insert a Node

CALLING SEQUENCE:
: ```c
  void rtems_chain_insert(
      rtems_chain_node *after_node,
      rtems_chain_node *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine inserts a node on a chain immediately following the specified
  node.

NOTES:

: Interrupts are disabled during the insert to ensure the atomicity of the
  operation.

  Use `rtems_chain_insert_unprotected()` to avoid disabling of interrupts.

```{raw} latex
\clearpage
```

(rtems-chain-insert-unprotected)=

```{index} chain insert a node unprotected
```

```{index} rtems_chain_insert_unprotected()
```

### Insert a Node (unprotected)

CALLING SEQUENCE:
: ```c
  void rtems_chain_insert_unprotected(
      rtems_chain_node *after_node,
      rtems_chain_node *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine inserts a node on a chain immediately following the specified
  node.

NOTES:

: The function does nothing to ensure the atomicity of the operation.

```{raw} latex
\clearpage
```

(rtems-chain-append)=

```{index} chain append a node
```

```{index} rtems_chain_append()
```

### Append a Node

CALLING SEQUENCE:
: ```c
  void rtems_chain_append(
      rtems_chain_control *the_chain,
      rtems_chain_node    *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine appends a node to the end of a chain.

NOTES:

: Interrupts are disabled during the append to ensure the atomicity of the
  operation.

  Use `rtems_chain_append_unprotected` to avoid disabling of interrupts.

```{raw} latex
\clearpage
```

(rtems-chain-append-unprotected)=

```{index} chain append a node unprotected
```

```{index} rtems_chain_append_unprotected()
```

### Append a Node (unprotected)

CALLING SEQUENCE:
: ```c
  void rtems_chain_append_unprotected(
      rtems_chain_control *the_chain,
      rtems_chain_node    *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine appends a node to the end of a chain.

NOTES:

: The function does nothing to ensure the atomicity of the operation.

```{raw} latex
\clearpage
```

(rtems-chain-prepend)=

```{index} prepend node
```

```{index} rtems_chain_prepend()
```

### Prepend a Node

CALLING SEQUENCE:
: ```c
  void rtems_chain_prepend(
      rtems_chain_control *the_chain,
      rtems_chain_node    *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine prepends a node to the front of the chain.

NOTES:

: Interrupts are disabled during the prepend to ensure the atomicity of the
  operation.

  Use `rtems_chain_prepend_unprotected` to avoid disabling of interrupts.

```{raw} latex
\clearpage
```

(rtems-chain-prepend-unprotected)=

```{index} prepend node unprotected
```

```{index} rtems_chain_prepend_unprotected()
```

### Prepend a Node (unprotected)

CALLING SEQUENCE:
: ```c
  void rtems_chain_prepend_unprotected(
      rtems_chain_control *the_chain,
      rtems_chain_node    *the_node
  );
  ```

RETURNS:

: Returns nothing.

DESCRIPTION:

: This routine prepends a node to the front of the chain.

NOTES:

: The function does nothing to ensure the atomicity of the operation.
