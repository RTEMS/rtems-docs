.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)

How-To
======

Getting Started
---------------

The RTEMS specification items and qualification tools are work in progress.  The
first step to work with the RTEMS specification and the corresponding tools is a
clone of the following repository:

.. code-block:: none

    git clone git://git.rtems.org/rtems-central.git
    git submodule init
    git submodule update

The tools need a virtual Python 3 environment. To set it up use:

.. code-block:: none

    cd rtems-central
    make env

Each time you want to use one of the tools, you have to activate the
environment in your shell:

.. code-block:: none

    cd rtems-central
    . env/bin/activate

Glossary Specification
----------------------

The glossary of terms for the RTEMS Project is defined by
:ref:`SpecTypeGlossaryTermItemType` items in the :file:`spec/glossary`
directory.  For a new glossary term add a glossary item to this directory.  As
the file name use the term in lower case with all white space and special
characters removed or replaced by alphanumeric characters, for example
:file:`spec/glossary/magicpower.yml` for the term `magic power`.

Use ``${uid:/attribute}`` substitutions to reference other parts of the
specification.

.. code-block:: yaml

    SPDX-License-Identifier: CC-BY-SA-4.0 OR BSD-2-Clause
    copyrights:
    - Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
    enabled-by: true
    glossary-type: term
    links:
    - role: glossary-member
      uid: ../glossary-general
    term: magic power
    text: |
      Magic power enables a caller to create magic objects using a
      ${magicwand:/term}.
    type: glossary

Define acronyms with the phrase `This term is an acronym for *.` in the
``text`` attribute:

.. code-block:: yaml

    ...
    term: MP
    ...
    text: |
      This term is an acronym for Magic Power.
    ...

Once you are done with the glossary items, run the script :file:`spec2doc.py`
to generate the derived documentation content.  Send patches for the generated
documentation and the specification to the :r:list:`devel` and follow the
normal patch review process.

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
