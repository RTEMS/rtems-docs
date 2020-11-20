.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Operations
==========

Decomposing and Recomposing an Object Id
----------------------------------------

Services are provided to decompose an object Id into its subordinate
components. The following services are used to do this:

- ``rtems_object_id_get_api``

- ``rtems_object_id_get_class``

- ``rtems_object_id_get_node``

- ``rtems_object_id_get_index``

The following C language example illustrates the decomposition of an Id and
printing the values.

.. code-block:: c

    void printObjectId(rtems_id id)
    {
        printf(
            "API=%d Class=%" PRIu32 " Node=%" PRIu32 " Index=%" PRIu16 "\n",
            rtems_object_id_get_api(id),
            rtems_object_id_get_class(id),
            rtems_object_id_get_node(id),
            rtems_object_id_get_index(id)
        );
    }

This prints the components of the Ids as integers.

It is also possible to construct an arbitrary Id using the ``rtems_build_id``
service.  The following C language example illustrates how to construct the
"next Id."

.. code-block:: c

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

RTEMS also provides services to associate the API and Class portions of an
Object Id with strings.  This allows the application developer to provide more
information about an object in diagnostic messages.

In the following C language example, an Id is decomposed into its constituent
parts and "pretty-printed."

.. code-block:: c

    void prettyPrintObjectId(rtems_id id)
    {
        int tmpAPI;
        uint32_t tmpClass;

        tmpAPI   = rtems_object_id_get_api(id),
        tmpClass = rtems_object_id_get_class(id),

        printf(
            "API=%s Class=%s Node=%" PRIu32 " Index=%" PRIu16 "\n",
            rtems_object_get_api_name(tmpAPI),
            rtems_object_get_api_class_name(tmpAPI, tmpClass),
            rtems_object_id_get_node(id),
            rtems_object_id_get_index(id)
        );
    }
