.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

Formal Verification Overview
============================

Formal Verification is a technique based on writing key design artifacts using
notations that have a well-defined mathematical :term:`semantics`. This means that
these descriptions can be rigorously analysed using logic and other mathematical
tools. We will use the term :term:`formal model` to refer to any such description.

Having a formal model of a software engineering artifact (requirements,
specification, code) allows it to be analysed to assess the behaviour it
describes. This means we can check that the model has desired properties, and
lacks undesired ones. A key feature of having a formal description is that we
can develop tools that parse the notation and can perform much, if not most,
of the analysis. An industrial-strength formalism is one that has very good
tool support.

When we have two formal models of the same software object at different levels
of abstraction (specification and code, say) then we can compare them. In
particular, we can formally analyse if a lower level artifact like code,
satisfies the properties described by a higher level, such as a specification.
This relationship is commonly referred to as a :term:`refinement`.

Often it is quite difficult to get a useful formal model of real code. Some
formal modelling approaches are capable of generating machine-readable
:term:`scenarios` that describe possible correct behaviours of the system at the
relevant level of abstraction. We can define a refinement for these by
using them to generate test code. This is the technique that is used here to
verify parts of RTEMS. We construct formal models based on requirements
documentation, and use these as a basis for test generation.
