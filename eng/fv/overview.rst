.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

.. _FormalVerifOverview:

Formal Verification Overview
============================

Formal Verification is a technique based on writing key design artifacts using
notations that have a well-defined mathematical :term:`semantics`. This means
that these descriptions can be rigorously analyzed using logic and other
mathematical tools. The term :term:`formal model` is used to refer to any such
description.

Having a formal model of a software engineering artifact (requirements,
specification, code) allows it to be analyzed to assess the behavior it
describes. This means checks can be done that the model has desired properties,
and that it lacks undesired ones. A key feature of having a formal description
is that tools can be developed that parse the notation and perform much,
if not most, of the analysis. An industrial-strength formalism is one that has
very good tool support.

Having two formal models of the same software object at different levels
of abstraction (specification and code, say) allows their comparison. In
particular, a formal analysis can establish if a lower level artifact like
code satisfies the properties described by a higher level,
such as a specification. This relationship is commonly referred to as a
:term:`refinement`.

Often it is quite difficult to get a useful formal model of real code. Some
formal modelling approaches are capable of generating machine-readable
:term:`scenarios` that describe possible correct behaviors of the system at the
relevant level of abstraction. A refinement for these can be defined by
using them to generate test code.
This is the technique that is used in :ref:`FormalVerifMethodology` to
verify parts of RTEMS. Formal models are constructed based on requirements
documentation, and are used as a basis for test generation.
