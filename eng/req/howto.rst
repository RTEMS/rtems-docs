.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)

How-To
======

Interface Specification
-----------------------

.. _ReqEngAddAPIHeaderFile:

Specify an API Header File
^^^^^^^^^^^^^^^^^^^^^^^^^^

The RTEMS :term:`API` header files are specified under ``spec:/if/rtems/*``.
Create a subdirectory with a corresponding name for the API, for example in
:file:`spec/if/rtems/foo` for the `foo` API.  In this new subdirectory place an
:ref:`SpecTypeInterfaceHeaderFileItemType` item named :file:`header.yml`
(:file:`spec/if/rtems/foo/header.yml`) and populate it with the required
attributes.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    interface-type: header-file
    links:
    - role: interface-placement
      uid: /if/domains/api
    path: rtems/rtems/foo.h
    prefix: cpukit/include
    type: interface

Specify an API Element
^^^^^^^^^^^^^^^^^^^^^^

Figure out the corresponding header file item.  If it does not exist, see
:ref:`ReqEngAddAPIHeaderFile`.  Place a specialization of an
:ref:`SpecTypeInterfaceItemType` item into the directory of the header file
item, for example :file:`spec/if/rtems/foo/bar.yml` for the :c:func:`bar`
function.  Add the required attributes for the new interface item.  Do not hard
code interface names which are used to define the new interface.  Use
``${uid-of-interface-item:/name}`` instead.  If the referenced interface is
specified in the same directory, then use a relative UID.  Using interface
references creates implicit dependencies and helps the header file generator to
resolve the interface dependencies and header file includes for you.  Use
:ref:`SpecTypeInterfaceUnspecifiedItemType` items for interface dependencies to
other domains such as the C language, the compiler, the implementation, or
user-provided defines.  To avoid cyclic dependencies between types you may use
an :ref:`SpecTypeInterfaceForwardDeclarationItemType` item.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    brief: Tries to create a magic object and returns it.
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    definition:
      default:
        body: null
        params:
        - ${magic-wand:/name} ${.:/params[0]/name}
        return: ${magic-type:/name} *
      variants: []
    description: |
      The magic object is created out of nothing with the help of a magic wand.
    enabled-by: true
    interface-type: function
    links:
    - role: interface-placement
      uid: header
    - role: interface-ingroup
      uid: /groups/api/classic/foo
    name: bar
    notes: null
    params:
    - description: is the magic wand.
      dir: null
      name: magic_wand
    return:
      return: Otherwise, the magic object is returned.
      return-values:
      - description: The caller did not have enough magic power.
        value: ${/if/c/null}
    type: interface
