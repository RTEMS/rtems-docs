.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2015, 2020 embedded brains GmbH & Co. KG
.. Copyright (C) 2015, 2020 Sebastian Huber

.. index:: linkersets

.. _linker_sets:

Linker Sets
***********

Introduction
============

Linker sets are a flexible means to create arrays of items out of a set of
object files at link-time.  For example it is possible to define an item *I* of
type *T* in object file *A* and an item *J* of type *T* in object file *B* to
be a member of a linker set *S*.  The linker will then collect these two items
*I* and *J* and place them in consecutive memory locations, so that they can be
accessed like a normal array defined in one object file.  The size of a linker
set is defined by its begin and end markers.  A linker set may be empty.  It
should only contain items of the same type.

The following macros are provided to create, populate and use linker sets.

- RTEMS_LINKER_SET_BEGIN_ - Designator of the linker set begin marker

- RTEMS_LINKER_SET_END_ - Designator of the linker set end marker

- RTEMS_LINKER_SET_SIZE_ - The linker set size in characters

- RTEMS_LINKER_SET_ITEM_COUNT_ - The linker set item count

- RTEMS_LINKER_SET_IS_EMPTY_ - Is the linker set empty?

- RTEMS_LINKER_SET_FOREACH_ - Iterate through the linker set items

- RTEMS_LINKER_ROSET_DECLARE_ - Declares a read-only linker set

- RTEMS_LINKER_ROSET_ - Defines a read-only linker set

- RTEMS_LINKER_ROSET_ITEM_DECLARE_ - Declares a read-only linker set item

- RTEMS_LINKER_ROSET_ITEM_ORDERED_DECLARE_ - Declares an ordered read-only linker set item

- RTEMS_LINKER_ROSET_ITEM_REFERENCE_ - References a read-only linker set item

- RTEMS_LINKER_ROSET_ITEM_ - Defines a read-only linker set item

- RTEMS_LINKER_ROSET_ITEM_ORDERED_ - Defines an ordered read-only linker set item

- RTEMS_LINKER_ROSET_CONTENT_ - Marks a declaration as a read-only linker set content

- RTEMS_LINKER_RWSET_DECLARE_ - Declares a read-write linker set

- RTEMS_LINKER_RWSET_ - Defines a read-write linker set

- RTEMS_LINKER_RWSET_ITEM_DECLARE_ - Declares a read-write linker set item

- RTEMS_LINKER_RWSET_ITEM_ORDERED_DECLARE_ - Declares an ordered read-write linker set item

- RTEMS_LINKER_RWSET_ITEM_REFERENCE_ - References a read-write linker set item

- RTEMS_LINKER_RWSET_ITEM_ - Defines a read-write linker set item

- RTEMS_LINKER_RWSET_ITEM_ORDERED_ - Defines an ordered read-write linker set item

- RTEMS_LINKER_RWSET_CONTENT_ - Marks a declaration as a read-write linker set content

Background
==========

Linker sets are used not only in RTEMS, but also for example in Linux, in
FreeBSD, for the GNU C constructor extension and for global C++ constructors.
They provide a space efficient and flexible means to initialize modules.  A
linker set consists of

- dedicated input sections for the linker (e.g. ``.ctors`` and ``.ctors.*`` in
  the case of global constructors),

- a begin marker (e.g. provided by ``crtbegin.o``, and

- an end marker (e.g. provided by ``crtend.o``).

A module may place a certain data item into the dedicated input section.  The
linker will collect all such data items in this section and create a begin and
end marker.  The initialization code can then use the begin and end markers to
find all the collected data items (e.g. pointers to initialization functions).

In the linker command file of the GNU linker we need the following output
section descriptions.

.. code-block:: c

    /* To be placed in a read-only memory region */
    .rtemsroset : {
      KEEP (*(SORT(.rtemsroset.*)))
    }
    /* To be placed in a read-write memory region */
    .rtemsrwset : {
      KEEP (*(SORT(.rtemsrwset.*)))
    }

The ``KEEP()`` ensures that a garbage collection by the linker will not discard
the content of this section.  This would normally be the case since the linker
set items are not referenced directly.  The ``SORT()`` directive sorts the
input sections lexicographically.  Please note the lexicographical order of the
``.begin``, ``.content`` and ``.end`` section name parts in the RTEMS linker
sets macros which ensures that the position of the begin and end markers are
right.

So, what is the benefit of using linker sets to initialize modules?  They can be
used to initialize and include only those RTEMS managers and other components
which are used by the application.  For example, in case an application uses
message queues, it must call ``rtems_message_queue_create()``.  In the module
implementing this function, we can place a linker set item and register the
message queue handler constructor.  Otherwise, in case the application does not
use message queues, there will be no reference to the
``rtems_message_queue_create()`` function and the constructor is not
registered, thus nothing of the message queue handler will be in the final
executable.

For an example see test program :file:`sptests/splinkersets01`.

Directives
==========

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_SET_BEGIN

.. _RTEMS_LINKER_SET_BEGIN:

RTEMS_LINKER_SET_BEGIN - Designator of the linker set begin marker
------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        type *begin = RTEMS_LINKER_SET_BEGIN( set );

DESCRIPTION:
    This macro generates the designator of the begin marker of the linker set
    identified by ``set``.  The item at the begin marker address is the first
    member of the linker set if it exists, e.g. the linker set is not empty.  A
    linker set is empty, if and only if the begin and end markers have the same
    address.

    The ``set`` parameter itself must be a valid C designator on which no macro
    expansion is performed.  It uniquely identifies the linker set.

NOTE:
    The compiler may try to be smart.  In general it will not work to assign linker
    set begin and end addresses to pointer variables and treat them like
    ordinary pointers.  The compiler may exploit the fact that actually two
    distinct objects are involved and use this to optimize.  To avoid trouble
    use :ref:`RTEMS_LINKER_SET_SIZE`, :ref:`RTEMS_LINKER_SET_ITEM_COUNT`,
    :ref:`RTEMS_LINKER_SET_IS_EMPTY` and :ref:`RTEMS_LINKER_SET_FOREACH`.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_SET_END

.. _RTEMS_LINKER_SET_END:

RTEMS_LINKER_SET_END - Designator of the linker set end marker
--------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        type *end = RTEMS_LINKER_SET_END( set );

DESCRIPTION:
    This macro generates the designator of the end marker of the linker set
    identified by ``set``.  The item at the end marker address is not a member
    of the linker set.  The ``set`` parameter itself must be a valid C
    designator on which no macro expansion is performed.  It uniquely
    identifies the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_SET_SIZE

.. _RTEMS_LINKER_SET_SIZE:

RTEMS_LINKER_SET_SIZE - The linker set size in characters
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        size_t size = RTEMS_LINKER_SET_SIZE( set );

DESCRIPTION:
    This macro returns the size of the linker set identified by ``set`` in
    characters.  The ``set`` parameter itself must be a valid C designator on
    which no macro expansion is performed.  It uniquely identifies the linker
    set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_SET_ITEM_COUNT

.. _RTEMS_LINKER_SET_ITEM_COUNT:

RTEMS_LINKER_SET_ITEM_COUNT - The linker set item count
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        size_t item_count = RTEMS_LINKER_SET_ITEM_COUNT( set );

DESCRIPTION:
    This macro returns the item count of the linker set identified by ``set``.
    The ``set`` parameter itself must be a valid C designator on which no macro
    expansion is performed.  It uniquely identifies the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_SET_IS_EMPTY

.. _RTEMS_LINKER_SET_IS_EMPTY:

RTEMS_LINKER_SET_IS_EMPTY - Is the linker set empty?
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        bool is_empty = RTEMS_LINKER_SET_IS_EMPTY( set );

DESCRIPTION:
    This macro returns true if the linker set identified by ``set`` is empty,
    otherwise returns false.  The ``set`` parameter itself must be a valid C
    designator on which no macro expansion is performed.  It uniquely
    identifies the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_SET_FOREACH

.. _RTEMS_LINKER_SET_FOREACH:

RTEMS_LINKER_SET_FOREACH - Iterate through the linker set items
---------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET( myset, int );

        int count( void )
        {
          int *item;
          int n;

          n = 0;
          RTEMS_LINKER_SET_FOREACH( myset, item ) {
            n += *item;
          }

          return n;
        }

DESCRIPTION:
    This macro generates a for loop statement which iterates through each item
    of a linker set identified by ``set``.  The ``set`` parameter itself must
    be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set.  The ``item`` parameter must be a
    pointer to an item of the linker set.  It iterates through all items of the
    linker set from begin to end.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_DECLARE

.. _RTEMS_LINKER_ROSET_DECLARE:

RTEMS_LINKER_ROSET_DECLARE - Declares a read-only linker set
------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_DECLARE( set, type );

DESCRIPTION:
    This macro generates declarations for the begin and end markers of a
    read-only linker set identified by ``set``.  The ``set`` parameter itself
    must be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set. The ``type`` parameter defines the type
    of the linker set items.  The type must be the same for all macro
    invocations of a particular linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET

.. _RTEMS_LINKER_ROSET:

RTEMS_LINKER_ROSET - Defines a read-only linker set
---------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET( set, type );

DESCRIPTION:
    This macro generates definitions for the begin and end markers of a
    read-only linker set identified by ``set``.  The ``set`` parameter itself
    must be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set. The ``type`` parameter defines the type
    of the linker set items.  The type must be the same for all macro
    invocations of a particular linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_ITEM_DECLARE

.. _RTEMS_LINKER_ROSET_ITEM_DECLARE:

RTEMS_LINKER_ROSET_ITEM_DECLARE - Declares a read-only linker set item
----------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_ITEM_DECLARE( set, type, item );

DESCRIPTION:
    This macro generates a declaration of an item contained in the read-only
    linker set identified by ``set``.  For a description of the ``set``,
    ``type``, and ``item`` parameters see :ref:`RTEMS_LINKER_ROSET_ITEM`.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_ITEM_ORDERED_DECLARE

.. _RTEMS_LINKER_ROSET_ITEM_ORDERED_DECLARE:

RTEMS_LINKER_ROSET_ITEM_ORDERED_DECLARE - Declares an ordered read-only linker set item
---------------------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_ITEM_ORDERED_DECLARE( set, type, item, order );

DESCRIPTION:
    This macro generates a declaration of an ordered item contained in the
    read-only linker set identified by ``set``.  For a description of the
    ``set``, ``type``, ``item``, and ``order`` parameters see
    :ref:`RTEMS_LINKER_ROSET_ITEM_ORDERED`.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_ITEM_REFERENCE

.. _RTEMS_LINKER_ROSET_ITEM_REFERENCE:

RTEMS_LINKER_ROSET_ITEM_REFERENCE - References a read-only linker set item
--------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_ITEM_REFERENCE( set, type, item );

DESCRIPTION:
    This macro generates a reference to an item contained in the read-only
    linker set identified by ``set``.  The ``set`` parameter itself must be a
    valid C designator on which no macro expansion is performed.  It uniquely
    identifies the linker set. The ``type`` parameter defines the type of the
    linker set items.  The type must be the same for all macro invocations of a
    particular linker set. The ``item`` parameter itself must be a valid C
    designator on which no macro expansion is performed.  It uniquely
    identifies an item in the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_ITEM

.. _RTEMS_LINKER_ROSET_ITEM:

RTEMS_LINKER_ROSET_ITEM - Defines a read-only linker set item
-------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_ITEM( set, type, item );

DESCRIPTION:
    This macro generates a definition of an item contained in the read-only
    linker set identified by ``set``.  The ``set`` parameter itself must be a
    valid C designator on which no macro expansion is performed.  It uniquely
    identifies the linker set. The ``type`` parameter defines the type of the
    linker set items.  The type must be the same for all macro invocations of a
    particular linker set. The ``item`` parameter itself must be a valid C
    designator on which no macro expansion is performed.  It uniquely
    identifies an item in the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_ITEM_ORDERED

.. _RTEMS_LINKER_ROSET_ITEM_ORDERED:

RTEMS_LINKER_ROSET_ITEM_ORDERED - Defines an ordered read-only linker set item
------------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_ITEM_ORDERED( set, type, item, order );

DESCRIPTION:
    This macro generates a definition of an ordered item contained in the
    read-only linker set identified by ``set``.  The ``set`` parameter itself
    must be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set. The ``type`` parameter defines the type
    of the linker set items.  The type must be the same for all macro
    invocations of a particular linker set.  The ``item`` parameter itself must
    be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies an item in the linker set. The ``order`` parameter must
    be a valid linker input section name part on which macro expansion is
    performed.  The items are lexicographically ordered according to the
    ``order`` parameter within a linker set.  Ordered items are placed before
    unordered items in the linker set.

NOTES:
    To be resilient to typos in the order parameter, it is recommended to use
    the following construct in macros defining items for a particular linker
    set (see enum in ``XYZ_ITEM()``).

    .. code-block:: c

        #include <rtems/linkersets.h>

        typedef struct {
          int foo;
        } xyz_item;

        /* The XYZ-order defines */
        #define XYZ_ORDER_FIRST 0x00001000
        #define XYZ_ORDER_AND_SO_ON 0x00002000

        /* Defines an ordered XYZ-item */
        #define XYZ_ITEM( item, order ) \
          enum { xyz_##item = order }; \
          RTEMS_LINKER_ROSET_ITEM_ORDERED( \
            xyz, const xyz_item *, item, order \
          ) = { &item }

        /* Example item */
        static const xyz_item some_item = { 123 };
        XYZ_ITEM( some_item, XYZ_ORDER_FIRST );

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_ROSET_CONTENT

.. _RTEMS_LINKER_ROSET_CONTENT:

RTEMS_LINKER_ROSET_CONTENT - Marks a declaration as a read-only linker set content
----------------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_ROSET_CONTENT( set, decl );

DESCRIPTION:
    This macro marks a declaration as a read-only linker set content.  The
    linker set is identified by ``set``.  The ``set`` parameter itself must be
    a valid C designator on which no macro expansion is performed.  It uniquely
    identifies the linker set. The ``decl`` parameter must be an arbitrary
    variable declaration.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_DECLARE

.. _RTEMS_LINKER_RWSET_DECLARE:

RTEMS_LINKER_RWSET_DECLARE - Declares a read-write linker set
-------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_DECLARE( set, type );

DESCRIPTION:
    This macro generates declarations for the begin and end markers of a
    read-write linker set identified by ``set``.  The ``set`` parameter itself
    must be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set. The ``type`` parameter defines the type
    of the linker set items.  The type must be the same for all macro
    invocations of a particular linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET

.. _RTEMS_LINKER_RWSET:

RTEMS_LINKER_RWSET - Defines a read-write linker set
----------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET( set, type );

DESCRIPTION:
    This macro generates definitions for the begin and end markers of a
    read-write linker set identified by ``set``.  The ``set`` parameter itself
    must be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set. The ``type`` parameter defines the type
    of the linker set items.  The type must be the same for all macro
    invocations of a particular linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_ITEM_DECLARE

.. _RTEMS_LINKER_RWSET_ITEM_DECLARE:

RTEMS_LINKER_RWSET_ITEM_DECLARE - Declares a read-write linker set item
-----------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_ITEM_DECLARE( set, type, item );

DESCRIPTION:
    This macro generates a declaration of an item contained in the read-write
    linker set identified by ``set``.  For a description of the ``set``,
    ``type``, and ``item`` parameters see :ref:`RTEMS_LINKER_RWSET_ITEM`.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_ITEM_ORDERED_DECLARE

.. _RTEMS_LINKER_RWSET_ITEM_ORDERED_DECLARE:

RTEMS_LINKER_RWSET_ITEM_ORDERED_DECLARE - Declares an ordered read-write linker set item
----------------------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_ITEM_ORDERED_DECLARE( set, type, item, order );

DESCRIPTION:
    This macro generates a declaration of an ordered item contained in the
    read-write linker set identified by ``set``.  For a description of the
    ``set``, ``type``, ``item``, and ``order`` parameters see
    :ref:`RTEMS_LINKER_RWSET_ITEM_ORDERED`.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_ITEM_REFERENCE

.. _RTEMS_LINKER_RWSET_ITEM_REFERENCE:

RTEMS_LINKER_RWSET_ITEM_REFERENCE - References a read-write linker set item
---------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_ITEM_REFERENCE( set, type, item );

DESCRIPTION:
    This macro generates a reference to an item contained in the read-write
    linker set identified by ``set``.  The ``set`` parameter itself must be a
    valid C designator on which no macro expansion is performed.  It uniquely
    identifies the linker set. The ``type`` parameter defines the type of the
    linker set items.  The type must be the same for all macro invocations of a
    particular linker set. The ``item`` parameter itself must be a valid C
    designator on which no macro expansion is performed.  It uniquely
    identifies an item in the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_ITEM

.. _RTEMS_LINKER_RWSET_ITEM:

RTEMS_LINKER_RWSET_ITEM - Defines a read-write linker set item
--------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_ITEM( set, type, item );

DESCRIPTION:
    This macro generates a definition of an item contained in the read-write
    linker set identified by ``set``.  The ``set`` parameter itself must be a
    valid C designator on which no macro expansion is performed.  It uniquely
    identifies the linker set. The ``type`` parameter defines the type of the
    linker set items.  The type must be the same for all macro invocations of a
    particular linker set. The ``item`` parameter itself must be a valid C
    designator on which no macro expansion is performed.  It uniquely
    identifies an item in the linker set.

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_ITEM_ORDERED

.. _RTEMS_LINKER_RWSET_ITEM_ORDERED:

RTEMS_LINKER_RWSET_ITEM_ORDERED - Defines an ordered read-write linker set item
-------------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_ITEM_ORDERED( set, type, item, order );

DESCRIPTION:
    This macro generates a definition of an ordered item contained in the
    read-write linker set identified by ``set``.  The ``set`` parameter itself
    must be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies the linker set. The ``type`` parameter defines the type
    of the linker set items.  The type must be the same for all macro
    invocations of a particular linker set.  The ``item`` parameter itself must
    be a valid C designator on which no macro expansion is performed.  It
    uniquely identifies an item in the linker set. The ``order`` parameter must
    be a valid linker input section name part on which macro expansion is
    performed.  The items are lexicographically ordered according to the
    ``order`` parameter within a linker set.  Ordered items are placed before
    unordered items in the linker set.

NOTES:
    To be resilient to typos in the order parameter, it is recommended to use
    the following construct in macros defining items for a particular linker
    set (see enum in ``XYZ_ITEM()``).

    .. code-block:: c

        #include <rtems/linkersets.h>

        typedef struct {
          int foo;
        } xyz_item;

        /* The XYZ-order defines */
        #define XYZ_ORDER_FIRST 0x00001000
        #define XYZ_ORDER_AND_SO_ON 0x00002000

        /* Defines an ordered XYZ-item */
        #define XYZ_ITEM( item, order ) \
          enum { xyz_##item = order }; \
          RTEMS_LINKER_RWSET_ITEM_ORDERED( \
            xyz, const xyz_item *, item, order \
          ) = { &item }

        /* Example item */
        static const xyz_item some_item = { 123 };
        XYZ_ITEM( some_item, XYZ_ORDER_FIRST );

.. raw:: latex

   \clearpage

.. index:: RTEMS_LINKER_RWSET_CONTENT

.. _RTEMS_LINKER_RWSET_CONTENT:

RTEMS_LINKER_RWSET_CONTENT - Marks a declaration as a read-write linker set content
-----------------------------------------------------------------------------------

CALLING SEQUENCE:
    .. code-block:: c

        RTEMS_LINKER_RWSET_CONTENT( set, decl );

DESCRIPTION:
    This macro marks a declaration as a read-write linker set content.  The
    linker set is identified by ``set``.  The ``set`` parameter itself must be
    a valid C designator on which no macro expansion is performed.  It uniquely
    identifies the linker set. The ``decl`` parameter must be an arbitrary
    variable declaration.
