.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH & Co. KG

Requirement Management
======================

Change Control Board
--------------------

Working with requirements usually involves a Change Control Board
(:term:`CCB`).  The CCB of the RTEMS Project is the
`RTEMS developer mailing list <https://lists.rtems.org/mailman/listinfo/devel>`_.

There are the following actors involved:

* *RTEMS users*: Everyone using the RTEMS real-time operating system to design,
  develop and build an application on top of it.

* *RTEMS developers*: The persons developing and maintaining RTEMS.  They write
  patches to add or modify code, requirements, tests and documentation.

Adding and changing requirements follows the normal patch review process.  The
normal patch review process is described in the
`RTEMS User Manual <https://docs.rtems.org/docs/main/user/support/contrib.html#patch-review-process>`_.
Reviews and comments may be submitted by anyone, but a maintainer review is
required to approve *significant* changes.  In addition for significant
changes, there should be at least one reviewer with a sufficient independence
from the author which proposes a new requirement or a change of an existing
requirement.  Working in another company on different projects is sufficiently
independent.  RTEMS maintainers do not know all the details, so they trust in
general people with experience on a certain platform.  Sometimes no review
comments may appear in a reasonable time frame, then an implicit agreement to
the proposed changes is assumed.  Patches can be sent at anytime, so
controlling changes in RTEMS requires a permanent involvement on the RTEMS
developer mailing list.

For a qualification of RTEMS according to certain standards, the requirements
may be approved by an RTEMS user.  The approval by RTEMS users is not the
concern of the RTEMS Project, however, the RTEMS Project should enable RTEMS
users to manage the approval of requirements easily.  This information may be
also used by a independent authority which comes into play with an Independent
Software Verification and Validation (:term:`ISVV`).  It could be used to
select a subset of requirements, e.g. look only at the ones approved by a
certain user.  RTEMS users should be able to reference the determinative
content of requirements, test procedures, test cases and justification reports
in their own documentation.  Changes in the determinative content should
invalidate all references to previous versions.

Add a Requirement
-----------------

.. image:: ../../images/eng/req-add.*
    :scale: 70
    :align: center

.. _ReqEngModifyRequirement:

Modify a Requirement
--------------------

.. image:: ../../images/eng/req-modify.*
    :scale: 70
    :align: center

Mark a Requirement as Obsolete
------------------------------

Requirements shall be never removed.  They shall be marked as obsolete.  This
ensures that requirement identifiers are not reused.  The procedure to obsolete
a requirement is the same as the one to :ref:`modify a requirement
<ReqEngModifyRequirement>`.
