.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH & Co. KG

Tooling
=======

Tool Requirements
-----------------

To manage requirements some tool support is helpful.  Here is a list of
requirements for the tool:

* The tool shall be open source.

* The tool should be actively maintained during the initial phase of the RTEMS
  requirements specification.

* The tool shall use plain text storage (no binary formats, no database).

* The tool shall support version control via Git.

* The tool should export the requirements in a human readable form using the
  Sphinx documentation framework.

* The tool shall support traceability of requirements to items external to the
  tool.

* The tool shall support traceability between requirements.

* The tool shall support custom requirement attributes.

* The tool should ensure that there are no cyclic dependencies between
  requirements.

* The tool should provide an export to :term:`ReqIF`.

Tool Evaluation
---------------

During an evaluation phase the following tools were considered:

* `aNimble <https://sourceforge.net/projects/nimble/>`_
* :term:`Doorstop`
* `OSRMT <https://github.com/osrmt/osrmt>`_
* `Papyrus <https://www.eclipse.org/papyrus/>`_
* `ProR <https://www.eclipse.org/rmf/pror/>`_
* `ReqIF Studio <https://formalmind.com/tools/studio/>`_
* `Requirement Heap <https://sourceforge.net/projects/reqheap/>`_
* `rmToo <http://rmtoo.florath.net/>`_

The tools aNimble, OSRMT and Requirement Heap were not selected since they use
a database.  The tools Papyrus, ProR and ReqIF are Eclipse based and use
complex XML files for data storage.  They were difficult to use and lack good
documentation/tutorials.  The tools rmToo and Doorstop turned out to be the
best candidates to manage requirements in the RTEMS Project.  The Doorstop tool
was selected as the first candidate mainly due a recommendation by an RTEMS
user.

.. _ReqEngDoorstop:

Best Available Tool - Doorstop
------------------------------

:term:`Doorstop` is a requirements management tool.  It has a modern,
object-oriented and well-structured implementation in Python 3.6 under the
LGPLv3 license.  It uses a continuous integration build with style checkers,
static analysis, documentation checks, code coverage, unit test and integration
tests.  In 2019, the project was actively maintained.  Pull requests for minor
improvements and new features were reviewed and integrated within days.  Each
requirement is contained in a single file in :term:`YAML` format.  Requirements
are organized in documents and can be linked to each other
:cite:`Browning:2014:RequirementsManagement`.

Doorstop consists of three main parts

* a stateless command line tool `doorstop`,

* a file format with a pre-defined set of attributes (YAML), and

* a primitive GUI tool (not intended to be used).

For RTEMS, its scope could be extended to manage specifications in general.
The primary reason for a close consideration of Doorstop as the requirements
management tool for the RTEMS Project was its data format which allows a high
degree of customization.  Doorstop uses a directed, acyclic graph (DAG) of
items.  The items are files in YAML format.  Each item has a set of
`standard attributes <https://doorstop.readthedocs.io/en/latest/reference/item/>`_
(key-value pairs).

The use case for the standard attributes is requirements management.  However,
Doorstop is capable to manage custom attributes as well.  We will heavily use
custom attributes for the specification items.  Enabling Doorstop to effectively
use custom attributes was done specifically for the RTEMS Project in several
patch sets which in the end turned out to be not enough to use Doorstop for the
RTEMS Project.

A key feature of Doorstop is the `fingerprint of items
<https://doorstop.readthedocs.io/en/latest/reference/item/#reviewed>`_.
For the RTEMS Project, the fingerprint hash algorithm was changed from MD5 to
SHA256.  In 2019, it can be considered cryptographically secure.  The
fingerprint should cover the normative values of an item, e.g. comments etc. are
not included.  The fingerprint would help RTEMS users to track the significant
changes in the requirements (in contrast to all the changes visible in Git).
As an example use case, a user may want to assign a project-specific status to
specification items.  This can be done with a table which contains columns for 

1. the UID of the item,

2. the fingerprint, and

3. the project-specific status.

Given the source code of RTEMS (which includes the specification items) and this
table, it can be determined which items are unchanged and which have another
status (e.g. unknown, changed, etc.).

After some initial work with Doorstop some issues surfaced
(`#471 <https://github.com/doorstop-dev/doorstop/issues/471>`_).
It turned out that Doorstop is not designed as a library and contains too much
policy. This results in a lack of flexibility required for the RTEMS Project.

1. Its primary use case is requirements management. So, it has some standard
   attributes useful in this domain, like derived, header, level, normative,
   ref, reviewed, and text. However, we want to use it more generally for
   specification items and these attributes make not always sense.  Having them
   in every item is just overhead and may cause confusion.

2. The links cannot have custom attributes, e.g. role, enabled-by. With
   link-specific attributes you could have multiple DAGs formed up by the same
   set of items.

3. Inside a document (directory) items are supposed to have a common type (set
   of attributes). We would like to store at a hierarchy level also distinct
   specializations.

4. The verification of the items is quite limited.  We need verification with
   type-based rules.

5. The UIDs in combination with the document hierarchy lead to duplication,
   e.g. a/b/c/a-b-c-d.yml. You have the path (a/b/c) also in the file name
   (a-b-c). You cannot have relative UIDs in links (e.g. ../parent-req) . The
   specification items may contain multiple requirements, e.g. min/max
   attributes.  There is no way to identify them.

6. The links are ordered by Doorstop alphabetically by UID. For some
   applications, it would be better to use the order specified by the user. For
   example, we want to use specification items for a new build system. Here it
   is handy if you can express things like this: A is composed of B and C.
   Build B before C.

.. _ReqEngManagementTool:

Custom Requirements Management Tool
-----------------------------------

No requirements management tool was available that fits the need of the RTEMS
Qualification Project.  The decision was to develop a custom requirements
management tool written in Python 3.6 or later.  The design for it is heavily
inspired by Doorstop.
