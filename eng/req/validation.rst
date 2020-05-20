.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. _ReqEngValidation:

Requirement Validation
======================

The validation of each requirement shall be accomplished by one or more of
the following methods and nothing else:

* *By test*: A :ref:`ReqEngTestCase` specification item is provided to
  demonstrate that the requirement is satisfied when the software product is
  executed on the target platform.

* *By analysis*: A statement is provided how the requirement is met, by
  analysing static properties of the software product.

* *By inspection*: A statement is provided how the requirement is met, by
  inspection of the :term:`source code`.

* *By review of design*: A rationale is provided to demonstrate how the
  qualification requirement is satisfied implicitly by the software design.

Validation by test is strongly recommended.  The choice of any other validation
method shall be strongly justified.  The requirements author is obligated to
provide the means to validate the requirement with detailed instructions.

For a specification item in a parent directory it could be checked that at
least one item in a subdirectory has a link to it.  For example a subdirectory
could contain validation items.  With this feature you could check that all
requirements are covered by at least one validation item.

The requirement validation by analysis, by inspection, and by design
specification items shall have the following attribute specializations:

type
    The type attribute value shall be *validation-by-analysis*,
    *validation-by-inspection*, or *validation-by-review-of-design*.

link
    There shall be exactly one link to the validated requirement.

text
    The statement or rational of the requirement validation.
