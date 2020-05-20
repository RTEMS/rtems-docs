.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. _ReqEngTrace:

Traceability of Specification Items
===================================

The standard ECSS-E-ST-10-06C demands that requirements shall be under
configuration management, backwards-traceable and forward-traceable
:cite:`ECSS_E_ST_10_06C`.  Requirements are a specialization of specification
items in RTEMS.

.. _ReqEngTraceHistory:

History of Specification Items
------------------------------

The RTEMS specification items should placed in the RTEMS sources using Git for
version control.  The history of specification items can be traced with Git.
Special commit procedures for changes in specification item files should be
established.  For example, it should be allowed to change only one
specification item per commit.  A dedicated Git commit message format may be
used as well, e.g. use of ``Approved-by:`` or ``Reviewed-by:`` lines which
indicate an agreed statement (similar to the
`Linux kernel patch submission guidelines <https://www.kernel.org/doc/html/latest//process/submitting-patches.html#using-reported-by-tested-by-reviewed-by-suggested-by-and-fixes>`_).
Git commit procedures may be ensured through a server-side pre-receive hook.
The history of requirements may be also added to the specification items
directly in a *revision* attribute.  This would make it possible to generate
the history information for documents without having the Git repository
available, e.g. from an RTEMS source release archive.

.. _ReqEngTraceBackward:

Backward Traceability of Specification Items
--------------------------------------------

Providing backward traceability of specification items means that we must be
able to find the corresponding higher level specification item for each refined
specification item.  A custom tool needs to verify this.

.. _ReqEngTraceForward:

Forward Traceability of Specification Items
-------------------------------------------

Providing forward traceability of specification items means that we must be
able to find all the refined specification items for each higher level
specification item.  A custom tool needs to verify this.  The links from
parent to child specification items are implicitly defined by links from a
child item to a parent item.

.. _ReqEngTraceReqArchDesign:

Traceability between Software Requirements, Architecture and Design
-------------------------------------------------------------------

The software requirements are implemented in custom YAML files, see
:ref:`ReqEngSpecItems`.  The software architecture and design is written in
Doxygen markup.  Doxygen markup is used throughout all header and source files.
A Doxygen filter program may be provided to place Doxygen markup in assembler
files.  The software architecture is documented via Doxygen groups.  Each
Doxygen group name should have a project-specific name and the name should be
unique within the project, e.g.  RTEMSTopLevel\ MidLevel\ LowLevel.  The link
from a Doxygen group to its parent group is realized through the ``@ingroup``
special command.  The link from a Doxygen group or :term:`software component`
to the corresponding requirement is realized through a ``@satisfy{req}``
`custom command <http://www.doxygen.nl/manual/custcmd.html>`_ which needs the
identifier of the requirement as its one and only parameter.  Only links to
parents are explicitly given in the Doxygen markup.  The links from a parent to
its children are only implicitly specified via the link from a child to its
parent.  So, a tool must process all files to get the complete hierarchy of
software requirements, architecture and design. Links from a software component
to another software component are realized through automatic Doxygen references
or the ``@ref`` and ``@see`` special commands.
