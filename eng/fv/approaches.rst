.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

Formal Verification Approaches
==============================

We present here an overview of a range of formal methods and tools
that look feasible for use with RTEMS.

A key criterion for any proposed tool is the ability to deploy it
in a highly automated manner.
This amounts to the tool having a command-line interface that covers
all the features we require.
One such feature is that the tool generates output that can be
easily transformed into the formats
used as part of the qualification datapack reports.
Tools with GUI interfaces can be very helpful while developing
and deploying formal models, as long as the models/tests/proofs
can be re-run automatically via the command-line.

Other important criteria concern the support available
for for test generation support,
and how close we can connect the formalism to actual C code.

The final key criteria is whatever techniques we propose should fit in 
with the RTEMS Project Mission Statement (Section 2 in this document).
This requires, among other things, 
that any tool we add to the tool-chain needs to be open-source.

A more detailed report regarding the decisions we took can be found in
:cite:`Butterfield:2021:FV1-200`.


We start with a general overview of formal methods and testing,
and discuss a number of formalisms and tools against the criteria above.

Formal Methods Overview
-----------------------

We can divide formal specification languages into the following groups:

  Model-based:  e.g., Z, VDM, B

    These have a language that describes a system in terms of having an abstract
    state and how it is modified by operations. Reasoning is typically based 
    around the notions of pre- and post-conditions and state invariants.
    The usual method of reasoning is by using theorem-proving. The resulting
    models often have an unbounded number of possible states, and are capable
    of describing unbounded numbers of operation steps.

  Finite State-based: e.g., finite-state machines (FSMs), SDL, Statecharts

    These a variant of model-based specification, with the added constraint
    that the number of states are bounded. Desired model properties are often
    expressed using some form of temporal logic. The languages used to describe
    these are often more constrained than in more general model-based
    approaches. The finiteness allows reasoning by searching the model,
    including doing exhaustive searches, a.k.a. model-checking.

  Process Algebras: e.g., CSP, CCS, pi-calculus, LOTOS

    The model systems in terms of the sequence of externally observable
    events that they perform. There is no explicit definition of the abstract
    states, but their underlying semantics is given as a state machine,
    where the states are deduced from the overall behaviour of the system,
    and events denote transitions between these state. In general both the
    number of such states and length of observed event sequences are unbounded.
    While temporal logics can be used to express properties, many process 
    algebras use their own notation to express desired properties by simpler
    systems. A technique called bisimulation is used reason about the 
    relationships between these.

  Most of the methods above start with formal specifications/models. Also 
  needed is a way to bridge the gap to actual code. The relationship between
  specification and code is often referred to as a refinement 
  (some prefer the term reification). Most model-based methods have refinement,
  with the concept baked in as a key part of the methodology.

  Theorem Provers: e.g., CoQ, HOL4, PVS, Isabelle/HOL

    Many modern theorem provers are not only useful to help reason about the
    formalisms mentioned above, but are often powerful enough to be used to 
    describe formal models in their own terms and then apply their proof
    systems directly to those.

  Model Checkers: SPIN, FDR

    Model checkers are tools that do exhaustive searches over models with a 
    finite number of states. These are most commonly used with the finite-state
    methods, as well as the process algebras were some bound is put on the
    state-space. As model-checking is basically exhaustive testing, these are
    often the easiest way to get test generation from formal techniques.

  Formal Development frameworks: e.g. TLA+, Frama-C, Key

    There are also a number of frameworks that support a close connection
    between a programming language, a formalism to specify desired behaviour
    for programs in that language, as well as tools to support the reasoning 
    (proof, simulation, test).

  
Formal Methods actively considered
----------------------------------

Given the emphasis on verifying RTEMS C code,
we rapidly focussed in on freely available tools that could easily connect to C.
These included: Frama-C, TLA+/PlusCal, Isabelle/HOL, and Promela/SPIN.
Further investigation ruled out TLA+/PlusCal because it is Java-based,
and requires installing a Java Runtime Environment.

Frama-C, Isabelle/HOL, and Promela/SPIN were all explored in more detail,
and used in initial experiments to assess their suitability.
A key decision was also made early in the project to start looking at how to use
formal techniques to do test generation.


Frama-C
^^^^^^^

Frama-C (frama-c.com) is a platform supporting a range of tools for analysing C
code, including static analysers, support for functional specifications (ANSI-C
Specification Language – ACSL), and links to theorem provers. Some of its
analyses require code annotations, while other can extract useful information
from un-annotated code. It has a plug-in architecture, which makes it easy to
extend. It is used extensively by Airbus.

Frama-C, and its plugins, are implemented in OCaml,
and it is installed using the ``opam`` package manager.
An issue here was that Frama-C has many quite large dependencies.
There was support for test generation, but it was not freely available.
Another issue was that Frama-C only supported C99, and not C11
(the issue is how to handle C11 Atomics in terms of their semantics).


Isabelle/HOL
^^^^^^^^^^^^

Isabelle/HOL is a wide-spectrum theorem-prover, implemented as an embedding of
Higher-Order Logic (HOL) into the Isabelle generic proof assistant
(isabelle.in.tum.de). It has a high degree of automation, including an ability
to link to third-party verification tools, and a very large library of verified
mathematical theorems, covering number and set theory, algebra, analysis. It is
based on the idea of a small trusted code kernel that defines an encapsulated
datatype representing a theorem, which can only be constructed using methods in
the kernel for that datatype, but which also scales effectively regardless of
how many  theorems are proven.
It is implemented using `polyml`, with the IDE implemented using Scala,
is open-source, and is easy to install.
However, like Frama-C, it is also a very large software suite.




Formal Method actually used
---------------------------

A good survey of formal techniques and testing
is found in a 2009 ACM survey paper :cite:`Hierons:2009:FMT`.
Here they clearly state:

  "The most important role for formal verification in testing
  is in the automated generation of test cases.
  In this context,
  model checking is the formal verification technology of choice;
  this is due to the ability of model checkers
  to produce counterexamples
  in case a temporal property does not hold for a system model."


Promela/SPIN
^^^^^^^^^^^^

The current use of formal methods in RTEMS is based on using the Promela
language to model key RTEMS features,
in such a way that we can generate tests using the SPIN model checker
(spinroot.com).
Promela is quite a low-level modelling language that makes it easy to get close
to code level, and is specifically targeted to modelling software. It is one of
the most widely used model-checkers, both in industry and education. It uses
assertions, and linear-time temporal logic (LTL) to express properties of
interest.

It is open-source, and very easy to install, needing only cc and lex/yacc.

Given a Promela model that checks key properties successfully,
we can generated tests for a property P by asking
Spin to check the negations of those properties.
There are ways to get Spin to generate multiple/all possible counterexamples,
as well as getting it to find the shortest.

