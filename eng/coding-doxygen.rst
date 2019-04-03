.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH

Doxygen Guidelines
==================

Group Names
-----------

Doxygen group names shall use
`CamelCase <https://en.wikipedia.org/wiki/Camel_case>`_.
In the RTEMS source code, CamelCase is rarely used, so this makes it easier to
search and replace Doxygen groups.  It avoids ambiguous references to
functions, types, defines, macros, and groups.  All groups shall have an
``RTEMS`` prefix.  This makes it possible to include the RTEMS files with
Doxygen comments in a larger project without name conflicts.

.. code:: c

    /**
     * @defgroup RTEMSScoreThread
     *
     * @ingrop RTEMSScore
     *
     * ...
     */

Use Groups
----------

Every file, function declaration, type definition, typedef, define, macro and
global variable declaration shall belong to at least one Doxygen group.  Use
``@defgroup`` and ``@addtogroup`` with ``@{`` and ``@}`` brackets to add
members to a group.  A group shall be defined at most once.  Each group shall
be documented with an ``@brief`` description and an optional detailed
description.  The ``@brief`` description shall use
`Title Case <https://en.wikipedia.org/wiki/Letter_case#Title_Case>`_.
Use grammatically correct sentences for the detailed descriptions.

.. code:: c

    /**
     * @defgroup RTEMSScoreThread
     *
     * @ingrop RTEMSScore
     *
     * @brief Thread Handler
     *
     * ...
     *
     * @{
     */

     ... declarations, defines ...

     /** @} */

.. code:: c

    /**
     * @addtogroup RTEMSScoreThread
     *
     * @{
     */

     ... declarations, defines ...

     /** @} */

Files
-----

Each source or header file shall have an ``@file`` block at the top of the
file.  The ``@file`` block should precede the license header separated by one
blank line.  This placement reduces the chance of merge conflicts in imported
third-party code.  The ``@file`` block shall be put into a group with
``@ingroup GroupName``.  The ``@file`` block should have an ``@brief``
description and a detailed description if it is considered helpful.  Use
``@brief @copybrief GroupName`` as a default to copy the ``@brief`` description
from the corresponding group and omit the detailed description.

.. code:: c

    /**
     * @file
     *
     * @ingroup RTEMSScoreThread
     *
     * @brief @copybrief RTEMSScoreThread
     */

.. code:: c

    /**
     * @file
     *
     * @ingroup RTEMSScoreThread
     *
     * @brief Some helpful brief description.
     *
     * Some helpful detailed description.
     */

Type Definitions
----------------

Each type defined in a header file shall be documented with an ``@brief``
description and an optional detailed description.  Each type member shall be
documented with an ``@brief`` description and an optional detailed description.
Use grammatically correct sentences for the detailed descriptions.

.. code:: c

    /**
     * @brief The information structure used to manage each API class of objects.
     *
     * If objects for the API class are configured, an instance of this structure
     * is statically allocated and pre-initialized by OBJECTS_INFORMATION_DEFINE()
     * through <rtems/confdefs.h>.  The RTEMS library contains a statically
     * allocated and pre-initialized instance for each API class providing zero
     * objects, see OBJECTS_INFORMATION_DEFINE_ZERO().
     */
    typedef struct {
      /**
       * @brief This is the maximum valid ID of this object API class.
       *
       * This member is statically initialized and provides also the object API,
       * class and multiprocessing node information.
       *
       * It is used by _Objects_Get() to validate an object ID.
       */
      Objects_Id maximum_id;

      ... more members ...
    } Objects_Information;

Function Declarations
---------------------

Each function declaration or function-like macros in a header file shall be
documented with an ``@brief`` description and an optional detailed description.
Use grammatically correct sentences for the brief and detailed descriptions.
Each parameter shall be documented with an ``@param`` entry.  List the
``@param`` entries in the order of the function parameters.  For *non-const
pointer* parameters

* use ``@param[out]``, if the referenced object is modified by the function, or

* use ``@param[in, out]``, if the referenced object is read and modified by the
  function.

For other parameters (e.g. *const pointer* and *scalar* parameters) do not use
the ``[in]``, ``[out]`` or ``[in, out]`` parameter specifiers.  Each return
value or return value range shall be documented with an ``@retval`` entry.
Document the most common return value first.  Use a placeholder name for value
ranges, e.g. ``pointer`` in the ``_Workspace_Allocate()`` example below.  In
case the function returns only one value, then use ``@return``, e.g. use
``@retval`` only if there are at least two return values or return value
ranges.  Use grammatically correct sentences for the parameter and return value
descriptions.

.. code:: c

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

.. code:: c

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

.. code:: c

    /**
     * @brief Allocates a memory block of the specified size from the workspace.
     *
     * @param size The size of the memory block.
     *
     * @retval pointer The pointer to the memory block.  The pointer is at least
     *   aligned by CPU_HEAP_ALIGNMENT.
     * @retval NULL No memory block with the requested size is available in the
     *   workspace.
     */
    void *_Workspace_Allocate( size_t size );

.. code:: c

    /**
     * @brief Rebalances the red-black tree after insertion of the node.
     *
     * @param[in, out] the_rbtree The red-black tree control.
     * @param[in, out] the_node The most recently inserted node.
     */
    void _RBTree_Insert_color(
      RBTree_Control *the_rbtree,
      RBTree_Node    *the_node
    );

.. code:: c

    /**
     * @brief Builds an object ID from its components.
     *
     * @param the_api The object API.
     * @param the_class The object API class.
     * @param node The object node.
     * @param index The object index.
     *
     * @return Returns the object ID constructed from the arguments.
     */
    #define _Objects_Build_id( the_api, the_class, node, index )

Header File Examples
--------------------

The
`<rtems/score/thread.h> <https://git.rtems.org/rtems/tree/cpukit/include/rtems/score/thread.h>`_
and
`<rtems/score/threadimpl.h> <https://git.rtems.org/rtems/tree/cpukit/include/rtems/score/threadimpl.h>`_
header files are a good example of how header files should be documented.
