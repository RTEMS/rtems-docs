% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 embedded brains GmbH & Co. KG

(DoxygenGuidelines)=

# Doxygen Guidelines

## Group Names

Doxygen group names shall use
[CamelCase](https://en.wikipedia.org/wiki/Camel_case).
In the RTEMS source code, CamelCase is rarely used, so this makes it easier to
search and replace Doxygen groups. It avoids ambiguous references to
functions, types, defines, macros, and groups. All groups shall have an
`RTEMS` prefix. This makes it possible to include the RTEMS files with
Doxygen comments in a larger project without name conflicts. The group name
shall use [Title Case](https://en.wikipedia.org/wiki/Letter_case#Title_Case).

```c
/**
 * @defgroup RTEMSScoreThread Thread Handler
 *
 * @ingroup RTEMSScore
 *
 * ...
 */
```

## Use Groups

Every file, function declaration, type definition, typedef, define, macro and
global variable declaration shall belong to at least one Doxygen group. Use
`@defgroup` and `@addtogroup` with `@{` and `@}` brackets to add
members to a group. A group shall be defined at most once. Each group shall
be documented with an `@brief` description and an optional detailed
description. Use grammatically correct sentences for the `@brief` and
detailed descriptions.

For the `@brief` description use phrases like this:

- This group contains ... and so on.
- The XYZ Handler provides ... and so on.
- The ABC Component contains ... and so on.

```c
/**
 * @defgroup RTEMSScoreThread Thread Handler
 *
 * @ingroup RTEMSScore
 *
 * @brief The Thread Handler provides functionality related to the
 *   management of threads.
 *
 * This includes the creation, deletion, and scheduling of threads.
 *
 * ...
 *
 * @{
 */

 ... declarations, defines ...

 /** @} */
```

```c
/**
 * @addtogroup RTEMSScoreThread
 *
 * @{
 */

 ... declarations, defines ...

 /** @} */
```

## Files

Each header and source file shall have an `@file` block at the top of the
file after the SPDX License Identifier. The `@file` block shall precede the
license header separated by one blank line, see {ref}`CCXXHeaderFileTemplate`
and {ref}`CCXXASMSourceFileTemplate`. The `@file` block shall be put into a
group with `@ingroup GroupName`. The `@file` block shall have an
`@brief` description and an optional detailed description. The detailed
description could give an explanation why a certain set of functions or data
structures is grouped in one file. Use grammatically correct sentences for the
`@brief` and detailed descriptions.

For the `@brief` description of header files use phrases like this:

- This header file provides ... and so on.
- This header file provides the API of the ABC Manager.
- This header file provides interfaces and functions used to implement the XYZ
  Handler.

For the `@brief` description of source files use phrases like this:

- This source file contains the implementation of some_function().
- This source file contains the definition of some_data_element.
- This source file contains the implementation of XZY Hander functions related
  to ABC processing.

```c
/**
 * @file
 *
 * @ingroup RTEMSScoreThread
 *
 * @brief This source file contains the implementation of
 *   _Thread_Initialize().
 */
```

## Type Definitions

Each type (`typedef`, `struct`, `enum`) defined in a header file shall be
documented with an `@brief` description and an optional detailed description.
Use grammatically correct sentences for the `@brief` and detailed
descriptions.

For the `@brief` description of types use phrases like this:

- This type represents ... and so on.
- This structure represents ... and so on.
- This structure provides ... and so on.
- This enumeration represents ... and so on.
- The XYZ represents ... and so on.

Each type member shall be documented with an `@brief` description and an
optional detailed description. Use grammatically correct sentences for the
`@brief` and detailed descriptions.

For the `@brief` description of types members use phrases like this:

- This member represents ... and so on.
- This member contains ... and so on.
- This member references ... and so on.
- The XYZ lock protects ... and so on.

For the `@brief` description of boolean type members use a phrase like this:
"This member is true, if some condition is satisfied, otherwise it is false.".

```c
/**
 * @brief The object information structure maintains the objects of an
 *   object class.
 *
 * If objects for the object class are configured, then an instance of this
 * structure is statically allocated and pre-initialized by
 * OBJECTS_INFORMATION_DEFINE() through <rtems/confdefs.h>.  The RTEMS
 * library contains a statically allocated and pre-initialized instance for
 * each object class providing zero objects, see
 * OBJECTS_INFORMATION_DEFINE_ZERO().
 */
typedef struct {
  /**
   * @brief This member contains the object identifier maximum of this
   *   object class.
   *
   * It is statically initialized.  The object identifier maximum provides
   * also the object API, class, and multiprocessing node information.
   *
   * It is used by _Objects_Get() to validate an object identifier.
   */
  Objects_Id maximum_id;

  ... more members ...
} Objects_Information;
```

## Function Declarations

Each function declaration or function-like macro in a header file shall be
documented with an `@brief` description and an optional detailed description.
Use grammatically correct sentences for the `@brief` and detailed
descriptions. Use the descriptive-style for `@brief` descriptions, for
example `"Creates a task."`, `"Sends the events to the task."`, or
`"Obtains the semaphore."`. Use "the" to refer to parameters of the
function. Do not use descriptions like `"Returns this and that."`. Describe
the function return in `@retval` and `@return` paragraphs.

Each parameter shall be documented with an `@param` entry. List the
`@param` entries in the order of the function parameters. For *non-const
pointer* parameters

- use `@param[out]`, if the function writes under some conditions to memory
  locations referenced directly or indirectly by the non-`const` pointer
  parameter, or
- use `@param[in, out]`, if the function reads under some conditions from
  memory locations referenced directly or indirectly by the non-`const`
  pointer parameter and the function writes under some conditions to memory
  locations referenced directly or indirectly by the non-`const` pointer
  parameter.

If the function only reads from memory locations referenced directly or
indirectly by a non-`const` pointer parameter, then the pointer parameter
should be made `const`.

For other parameters (e.g. *const pointer* and *scalar* parameters) do not use
the `[in]`, `[out]` or `[in, out]` parameter specifiers.

For the `@param` descriptions use phrases like this:

- is the ABC.
- indicates what should be done.
- defines the something.
- references the object to deal with.

The phrase shall form a grammatically correct sentence if "This parameter"
precedes the phrase, for example "This parameter is the size of the message in
bytes to send.".

Distinctive return values shall be documented with an `@retval` entry.
Document the most common return value first. Use `@return` to describe the
return of non-distinctive values. Use grammatically correct sentences for the
descriptions. Use sentences in simple past tense to describe conditions which
resulted in the return of a status value. Place `@retval` descriptions
before the `@return` description. For functions returning a boolean value,
use `@return` and a phrase like this: "Returns true, if some condition is
satisfied, otherwise false.".

```c
/**
 * @brief Sends a message to the message queue.
 *
 * This directive sends the message buffer to the message queue indicated by
 * ID.  If one or more tasks is blocked waiting to receive a message from this
 * message queue, then one will receive the message.  The task selected to
 * receive the message is based on the task queue discipline algorithm in use
 * by this particular message queue.  If no tasks are waiting, then the message
 * buffer will be placed at the rear of the chain of pending messages for this
 * message queue.
 *
 * @param id The message queue ID.
 * @param buffer The message content buffer.
 * @param size The size of the message.
 *
 * @retval RTEMS_SUCCESSFUL Successful operation.
 * @retval RTEMS_INVALID_ID Invalid message queue ID.
 * @retval RTEMS_INVALID_ADDRESS The message buffer pointer is @c NULL.
 * @retval RTEMS_INVALID_SIZE The message size is larger than the maximum
 *   message size of the message queue.
 * @retval RTEMS_TOO_MANY The new message would exceed the message queue limit
 *   for pending messages.
 */
rtems_status_code rtems_message_queue_send(
  rtems_id    id,
  const void *buffer,
  size_t      size
);
```

```c
/**
 * @brief Receives a message from the message queue
 *
 * This directive is invoked when the calling task wishes to receive a message
 * from the message queue indicated by ID. The received message is to be placed
 * in the buffer. If no messages are outstanding and the option set indicates
 * that the task is willing to block, then the task will be blocked until a
 * message arrives or until, optionally, timeout clock ticks have passed.
 *
 * @param id The message queue ID.
 * @param[out] buffer The buffer for the message content.  The buffer must be
 *   large enough to store maximum size messages of this message queue.
 * @param[out] size The size of the message.
 * @param option_set The option set, e.g. RTEMS_NO_WAIT or RTEMS_WAIT.
 * @param timeout The number of ticks to wait if the RTEMS_WAIT is set.  Use
 *   RTEMS_NO_TIMEOUT to wait indefinitely.
 *
 * @retval RTEMS_SUCCESSFUL Successful operation.
 * @retval RTEMS_INVALID_ID Invalid message queue ID.
 * @retval RTEMS_INVALID_ADDRESS The message buffer pointer or the message size
 *   pointer is @c NULL.
 * @retval RTEMS_TIMEOUT A timeout occurred and no message was received.
 */
rtems_status_code rtems_message_queue_receive(
  rtems_id        id,
  void           *buffer,
  size_t         *size,
  rtems_option    option_set,
  rtems_interval  timeout
);
```

```c
/**
 * @brief Allocates a memory block of the specified size from the workspace.
 *
 * @param size is the size in bytes of the memory block.
 *
 * @retval NULL No memory block with the requested size was available in the
 *   workspace.
 *
 * @return Returns the pointer to the allocated memory block, if enough
 *   memory to satisfy the allocation request was available.  The pointer is at
 *   least aligned by #CPU_HEAP_ALIGNMENT.
 */
void *_Workspace_Allocate( size_t size );
```

```c
/**
 * @brief Rebalances the red-black tree after insertion of the node.
 *
 * @param[in, out] the_rbtree references the red-black tree.
 * @param[in, out] the_node references the most recently inserted node.
 */
void _RBTree_Insert_color(
  RBTree_Control *the_rbtree,
  RBTree_Node    *the_node
);
```

```c
/**
 * @brief Builds an object ID from its components.
 *
 * @param the_api is the object API.
 * @param the_class is the object class.
 * @param node is the object node.
 * @param index is the object index.
 *
 * @return Returns the object ID built from the specified components.
 */
#define _Objects_Build_id( the_api, the_class, node, index )
```

## Header File Examples

The
[\<rtems/score/thread.h>](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/rtems/score/thread.h)
and
[\<rtems/score/threadimpl.h>](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/include/rtems/score/threadimpl.h)
header files are a good example of how header files should be documented.
