Object Services
###############

.. index:: object manipulation

Introduction
============

RTEMS provides a collection of services to assist in the
management and usage of the objects created and utilized
via other managers.  These services assist in the
manipulation of RTEMS objects independent of the API used
to create them.  The object related services provided by
RTEMS are:

- build_id

- ``rtems_build_name`` - build object name from characters

- ``rtems_object_get_classic_name`` - lookup name from Id

- ``rtems_object_get_name`` - obtain object name as string

- ``rtems_object_set_name`` - set object name

- ``rtems_object_id_get_api`` - obtain API from Id

- ``rtems_object_id_get_class`` - obtain class from Id

- ``rtems_object_id_get_node`` - obtain node from Id

- ``rtems_object_id_get_index`` - obtain index from Id

- ``rtems_build_id`` - build object id from components

- ``rtems_object_id_api_minimum`` - obtain minimum API value

- ``rtems_object_id_api_maximum`` - obtain maximum API value

- ``rtems_object_id_api_minimum_class`` - obtain minimum class value

- ``rtems_object_id_api_maximum_class`` - obtain maximum class value

- ``rtems_object_get_api_name`` - obtain API name

- ``rtems_object_get_api_class_name`` - obtain class name

- ``rtems_object_get_class_information`` - obtain class information

Background
==========

APIs
----

RTEMS implements multiple APIs including an Internal API,
the Classic API, and the POSIX API.  These
APIs share the common foundation of SuperCore objects and
thus share object management code. This includes a common
scheme for object Ids and for managing object names whether
those names be in the thirty-two bit form used by the Classic
API or C strings.

The object Id contains a field indicating the API that
an object instance is associated with.  This field
holds a numerically small non-zero integer.

Object Classes
--------------

Each API consists of a collection of managers.  Each manager
is responsible for instances of a particular object class.
Classic API Tasks and POSIX Mutexes example classes.

The object Id contains a field indicating the class that
an object instance is associated with.  This field
holds a numerically small non-zero integer.  In all APIs,
a class value of one is reserved for tasks or threads.

Object Names
------------

Every RTEMS object which has an Id may also have a
name associated with it.  Depending on the API, names
may be either thirty-two bit integers as in the Classic
API or strings as in the POSIX API.

Some objects have Ids but do not have a defined way to associate
a name with them.  For example, POSIX threads have
Ids but per POSIX do not have names. In RTEMS, objects
not defined to have thirty-two bit names may have string
names assigned to them via the ``rtems_object_set_name``
service.  The original impetus in providing this service
was so the normally anonymous POSIX threads could have
a user defined name in CPU Usage Reports.

Operations
==========

Decomposing and Recomposing an Object Id
----------------------------------------

Services are provided to decompose an object Id into its
subordinate components. The following services are used
to do this:

- ``rtems_object_id_get_api``

- ``rtems_object_id_get_class``

- ``rtems_object_id_get_node``

- ``rtems_object_id_get_index``

The following C language example illustrates the
decomposition of an Id and printing the values.
.. code:: c

    void printObjectId(rtems_id id)
    {
    printf(
    "API=%d Class=%d Node=%d Index=%d\\n",
    rtems_object_id_get_api(id),
    rtems_object_id_get_class(id),
    rtems_object_id_get_node(id),
    rtems_object_id_get_index(id)
    );
    }

This prints the components of the Ids as integers.

It is also possible to construct an arbitrary Id using
the ``rtems_build_id`` service.  The following
C language example illustrates how to construct the
"next Id."
.. code:: c

    rtems_id nextObjectId(rtems_id id)
    {
    return rtems_build_id(
    rtems_object_id_get_api(id),
    rtems_object_id_get_class(id),
    rtems_object_id_get_node(id),
    rtems_object_id_get_index(id) + 1
    );
    }

Note that this Id may not be valid in this
system or associated with an allocated object.

Printing an Object Id
---------------------

RTEMS also provides services to associate the API and Class
portions of an Object Id with strings.  This allows the
application developer to provide more information about
an object in diagnostic messages.

In the following C language example, an Id is decomposed into
its constituent parts and "pretty-printed."
.. code:: c

    void prettyPrintObjectId(rtems_id id)
    {
    int tmpAPI, tmpClass;
    tmpAPI   = rtems_object_id_get_api(id),
    tmpClass = rtems_object_id_get_class(id),
    printf(
    "API=%s Class=%s Node=%d Index=%d\\n",
    rtems_object_get_api_name(tmpAPI),
    rtems_object_get_api_class_name(tmpAPI, tmpClass),
    rtems_object_id_get_node(id),
    rtems_object_id_get_index(id)
    );
    }

Directives
==========

BUILD_NAME - Build object name from characters
----------------------------------------------
.. index:: build object name

**CALLING SEQUENCE:**

.. index:: rtems_build_name

.. code:: c

    rtems_name rtems_build_name(
    uint8_t c1,
    uint8_t c2,
    uint8_t c3,
    uint8_t c4
    );

**DIRECTIVE STATUS CODES**

Returns a name constructed from the four characters.

**DESCRIPTION:**

This service takes the four characters provided as arguments
and constructs a thirty-two bit object name with ``c1``
in the most significant byte and ``c4`` in the least
significant byte.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_GET_CLASSIC_NAME - Lookup name from id
---------------------------------------------
.. index:: get name from id
.. index:: obtain name from id

**CALLING SEQUENCE:**

.. index:: rtems_build_name

.. code:: c

    rtems_status_code rtems_object_get_classic_name(
    rtems_id      id,
    rtems_name   \*name
    );

**DIRECTIVE STATUS CODES**

``RTEMS_SUCCESSFUL`` - name looked up successfully
``RTEMS_INVALID_ADDRESS`` - invalid name pointer
``RTEMS_INVALID_ID`` - invalid object id

**DESCRIPTION:**

This service looks up the name for the object ``id`` specified
and, if found, places the result in ``*name``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_GET_NAME - Obtain object name as string
----------------------------------------------
.. index:: get object name as string
.. index:: obtain object name as string

**CALLING SEQUENCE:**

.. index:: rtems_object_get_name

.. code:: c

    char \*rtems_object_get_name(
    rtems_id       id,
    size_t         length,
    char          \*name
    );

**DIRECTIVE STATUS CODES**

Returns a pointer to the name if successful or ``NULL``
otherwise.

**DESCRIPTION:**

This service looks up the name of the object specified by``id`` and places it in the memory pointed to by ``name``.
Every attempt is made to return name as a printable string even
if the object has the Classic API thirty-two bit style name.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_SET_NAME - Set object name
---------------------------------
.. index:: set object name

**CALLING SEQUENCE:**

.. index:: rtems_object_set_name

.. code:: c

    rtems_status_code rtems_object_set_name(
    rtems_id       id,
    const char    \*name
    );

**DIRECTIVE STATUS CODES**

``RTEMS_SUCCESSFUL`` - name looked up successfully
``RTEMS_INVALID_ADDRESS`` - invalid name pointer
``RTEMS_INVALID_ID`` - invalid object id

**DESCRIPTION:**

This service sets the name of ``id`` to that specified
by the string located at ``name``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

If the object specified by ``id`` is of a class that
has a string name, this method will free the existing
name to the RTEMS Workspace and allocate enough memory
from the RTEMS Workspace to make a copy of the string
located at ``name``.

If the object specified by ``id`` is of a class that
has a thirty-two bit integer style name, then the first
four characters in ``*name`` will be used to construct
the name.
name to the RTEMS Workspace and allocate enough memory
from the RTEMS Workspace to make a copy of the string

OBJECT_ID_GET_API - Obtain API from Id
--------------------------------------
.. index:: obtain API from id

**CALLING SEQUENCE:**

.. index:: rtems_object_id_get_api

.. code:: c

    int rtems_object_id_get_api(
    rtems_id id
    );

**DIRECTIVE STATUS CODES**

Returns the API portion of the object Id.

**DESCRIPTION:**

This directive returns the API portion of the provided object ``id``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

This directive does NOT validate the ``id`` provided.

OBJECT_ID_GET_CLASS - Obtain Class from Id
------------------------------------------
.. index:: obtain class from object id

**CALLING SEQUENCE:**

.. index:: rtems_object_id_get_class

.. code:: c

    int rtems_object_id_get_class(
    rtems_id id
    );

**DIRECTIVE STATUS CODES**

Returns the class portion of the object Id.

**DESCRIPTION:**

This directive returns the class portion of the provided object ``id``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

This directive does NOT validate the ``id`` provided.

OBJECT_ID_GET_NODE - Obtain Node from Id
----------------------------------------
.. index:: obtain node from object id

**CALLING SEQUENCE:**

.. index:: rtems_object_id_get_node

.. code:: c

    int rtems_object_id_get_node(
    rtems_id id
    );

**DIRECTIVE STATUS CODES**

Returns the node portion of the object Id.

**DESCRIPTION:**

This directive returns the node portion of the provided object ``id``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

This directive does NOT validate the ``id`` provided.

OBJECT_ID_GET_INDEX - Obtain Index from Id
------------------------------------------
.. index:: obtain index from object id

**CALLING SEQUENCE:**

.. index:: rtems_object_id_get_index

.. code:: c

    int rtems_object_id_get_index(
    rtems_id id
    );

**DIRECTIVE STATUS CODES**

Returns the index portion of the object Id.

**DESCRIPTION:**

This directive returns the index portion of the provided object ``id``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

This directive does NOT validate the ``id`` provided.

BUILD_ID - Build Object Id From Components
------------------------------------------
.. index:: build object id from components

**CALLING SEQUENCE:**

.. index:: rtems_build_id

.. code:: c

    rtems_id rtems_build_id(
    int the_api,
    int the_class,
    int the_node,
    int the_index
    );

**DIRECTIVE STATUS CODES**

Returns an object Id constructed from the provided arguments.

**DESCRIPTION:**

This service constructs an object Id from the provided``the_api``, ``the_class``, ``the_node``, and ``the_index``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

This directive does NOT validate the arguments provided
or the Object id returned.

OBJECT_ID_API_MINIMUM - Obtain Minimum API Value
------------------------------------------------
.. index:: obtain minimum API value

**CALLING SEQUENCE:**

.. index:: rtems_object_id_api_minimum

.. code:: c

    int rtems_object_id_api_minimum(void);

**DIRECTIVE STATUS CODES**

Returns the minimum valid for the API portion of an object Id.

**DESCRIPTION:**

This service returns the minimum valid for the API portion of
an object Id.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_ID_API_MAXIMUM - Obtain Maximum API Value
------------------------------------------------
.. index:: obtain maximum API value

**CALLING SEQUENCE:**

.. index:: rtems_object_id_api_maximum

.. code:: c

    int rtems_object_id_api_maximum(void);

**DIRECTIVE STATUS CODES**

Returns the maximum valid for the API portion of an object Id.

**DESCRIPTION:**

This service returns the maximum valid for the API portion of
an object Id.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_API_MINIMUM_CLASS - Obtain Minimum Class Value
-----------------------------------------------------
.. index:: obtain minimum class value

**CALLING SEQUENCE:**

.. index:: rtems_object_api_minimum_class

.. code:: c

    int rtems_object_api_minimum_class(
    int api
    );

**DIRECTIVE STATUS CODES**

If ``api`` is not valid, -1 is returned.

If successful, this service returns the minimum valid for the class
portion of an object Id for the specified ``api``.

**DESCRIPTION:**

This service returns the minimum valid for the class portion of
an object Id for the specified ``api``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_API_MAXIMUM_CLASS - Obtain Maximum Class Value
-----------------------------------------------------
.. index:: obtain maximum class value

**CALLING SEQUENCE:**

.. index:: rtems_object_api_maximum_class

.. code:: c

    int rtems_object_api_maximum_class(
    int api
    );

**DIRECTIVE STATUS CODES**

If ``api`` is not valid, -1 is returned.

If successful, this service returns the maximum valid for the class
portion of an object Id for the specified ``api``.

**DESCRIPTION:**

This service returns the maximum valid for the class portion of
an object Id for the specified ``api``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

OBJECT_GET_API_NAME - Obtain API Name
-------------------------------------
.. index:: obtain API name

**CALLING SEQUENCE:**

.. index:: rtems_object_get_api_name

.. code:: c

    const char \*rtems_object_get_api_name(
    int api
    );

**DIRECTIVE STATUS CODES**

If ``api`` is not valid, the string ``"BAD API"`` is returned.

If successful, this service returns a pointer to a string
containing the name of the specified ``api``.

**DESCRIPTION:**

This service returns the name of the specified ``api``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

The string returned is from constant space.  Do not modify
or free it.

OBJECT_GET_API_CLASS_NAME - Obtain Class Name
---------------------------------------------
.. index:: obtain class name

**CALLING SEQUENCE:**

.. index:: rtems_object_get_api_class_name

.. code:: c

    const char \*rtems_object_get_api_class_name(
    int the_api,
    int the_class
    );

**DIRECTIVE STATUS CODES**

If ``the_api`` is not valid, the string ``"BAD API"`` is returned.

If ``the_class`` is not valid, the string ``"BAD CLASS"`` is returned.

If successful, this service returns a pointer to a string
containing the name of the specified ``the_api``/``the_class`` pair.

**DESCRIPTION:**

This service returns the name of the object class indicated by the
specified ``the_api`` and ``the_class``.

**NOTES:**

This directive is strictly local and does not impact task scheduling.

The string returned is from constant space.  Do not modify
or free it.

OBJECT_GET_CLASS_INFORMATION - Obtain Class Information
-------------------------------------------------------
.. index:: obtain class information

**CALLING SEQUENCE:**

.. index:: rtems_object_get_class_information

.. code:: c

    rtems_status_code rtems_object_get_class_information(
    int                                 the_api,
    int                                 the_class,
    rtems_object_api_class_information \*info
    );

**DIRECTIVE STATUS CODES**

``RTEMS_SUCCESSFUL`` - information obtained successfully
``RTEMS_INVALID_ADDRESS`` - ``info`` is NULL
``RTEMS_INVALID_NUMBER`` - invalid ``api`` or ``the_class``

If successful, the structure located at ``info`` will be filled
in with information about the specified ``api``/``the_class`` pairing.

**DESCRIPTION:**

This service returns information about the object class indicated by the
specified ``api`` and ``the_class``. This structure is defined as
follows:
.. code:: c

    typedef struct {
    rtems_id  minimum_id;
    rtems_id  maximum_id;
    int       maximum;
    bool      auto_extend;
    int       unallocated;
    } rtems_object_api_class_information;

**NOTES:**

This directive is strictly local and does not impact task scheduling.

.. COMMENT: COPYRIGHT (c) 1988-2008.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

