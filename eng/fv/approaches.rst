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


Frama-C
^^^^^^^

Frama-C (frama-c.com) is a platform supporting a range of tools for analysing C
code, including static analysers, support for functional specifications (ANSI-C
Specification Language – ACSL), and links to theorem provers. Some of its
analyses require code annotations, while other can extract useful information
from un-annotated code. It has a plug-in architecture, which makes it easy to
extend.

Frama-C, and its plugins, are implemented in OCaml,
and it is installed using the ``opam`` package manager.

A tele-conference call was held on 18th September with two members
of the Frama-C team, Florent Kirchner and Loic Sorrenson.
Notes of what was discussed are in
Appendix :numref:`%s <subsection_CEATelecon>`.
A follow-up email interchange asked about the use of the WP plug-in
by Airbus as part of their CI flow.
We shall refer to some of what was said below,
citing the "Frama-C team".

Automation
~~~~~~~~~~
Frama-C has a very comprehensive command-line interface,
and it has clearly been designed to fit
into an automated test/verification environment.
It also has a GUI which is not only a wrapper around the command-line program,
but also takes any proof you build through the GUI
and outputs it in a form that allows it to be replayed
via the command-line.

In :cite:`Brahmi:2018:FM` there is a discussion of how Frama-C is used
as part of the Airbus development process.
Airbus have spent a decade now at a project to formalise most if not all
of their software development process, by describing all engineering
artifacts using notations with formal semantics, and building interoperable
tools that use these notations.
In particular, they can perform verification of any system with a mix
of testing and proof, an approach they call "hybrid verification".
In particular they have a design language DCSL that can automatically
produce ACSL annotations for C programs, which themselves are produced
from templates generated by their toolset.
The WP plugin is used to prove the correctness of the code,
typically handling 95% of the proofs automatically.
Proof engineers supply loop invariants and use
tactics to prove the remaining 5% of proofs.
These tactics become part of the automated proof checking.
As far as test design is concerned, a lot of automation handles
the test boilerplate, leaving the test developer to focus on test scenarios.

An extended version of this paper can be found at
http://www.di.ens.fr/~delmas/erts18/.

There is an issue about integrating tools like
Frama-C into the current systems used by ``rtems.org``
for CI, see Section :numref:`%s <subsubsection_FutureCI>`.

Test Generation
~~~~~~~~~~~~~~~

There is a Frama-C plugin called ``pathcrawler`` that does test generation,
but is only available by email request for research/evaluation purposes.
An online demo version of it is available at

    http://pathcrawler-online.com:8080

When asked, the Frama-C team replied that
they don't make it available as, in their opinion at least,
using higher-level design artefacts (e.g. an ACSL specification)
to automatically derive tests for a lower level design artifact
(e.g., C code) is forbidden by DO178C.
Hence, they have not released it formally,
nor has much work gone into maintaining it.
There is an analysis of other standards, including DO178C,
in deliverable QT-109 :cite:`RQT_R1`
but the issue of automatic *test* generation does not seem to be discussed.


A recent study looked at how to add model-checking to Frama-C
based on counterexample guided-refinement (CEGAR) :cite:`Shankar:2016:MC`.
It developed a Frama-C plugin called `cegarmc`, which takes C annotated
with ACSL and converts it to a form that can be passed to CEGAR tools (e.g. SATAB, Blast). All are freely available.
However it is not clear how to get to tests from there.

Code Handling
~~~~~~~~~~~~~

Frama-C is designed to handle C99 from the very beginning.
However, the RTEMS sources also use C11, and so there may be
issues with certain parts of the code.

For example,
having run the following:

.. code-block:: c

    > sparc-rtems5-gcc -E -C -Iinclude -Iscore/cpu/sparc/include score/src/threadqenqueue.c

to obtain `threadqenqueue.i` to pass to Frama-C, we get a syntax error:

.. code-block:: c

    > frama-c threadqenqueue.i

    [kernel] Parsing threadqenqueue.i (no preprocessing)
    [kernel] /users/staff/butrfeld/rtemsSMP/rtems/5/lib/gcc/sparc-rtems5/7.4.1/include/stdatomic.h:40:
      syntax error:
      Location: line 40, between columns 8 and 16, before or at token: _Bool
      38
      39
      40    typedef _Atomic _Bool atomic_bool;
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      41    typedef _Atomic char atomic_char;
      42    typedef _Atomic signed char atomic_schar;
    [kernel] Frama-C aborted: invalid user input.

Again, this is an issue where we may need consider if we can make this code
more C99 compliant.
This was discussed with the Frama-C team,
and they said that the syntax issues are easy to fix,
but the real challenge is how to use ACSL to model atomic behaviour
and the underlying semantics that will drive the WP logic.


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



Automation
~~~~~~~~~~

Proof development in Isabelle/HOL is best done using their IDE.
However, all proofs can be replayed from the command-line.

There is an issue about integrating tools like
Isabell/HOL into the current systems used by ``rtems.org``
for CI, see Section :numref:`%s <subsubsection_FutureCI>`.


Test Generation
~~~~~~~~~~~~~~~

Currently not aware of work in this space.

Code Handling
~~~~~~~~~~~~~

There are encodings of the semantics of C in Isabelle/HOL,
most notably that developed by NICTA/Data61 for their verification of
the sel4 kernel :cite:`Klein:2009:FVOS`.
However, that semantics is highly tailored towards their kernel code,
and both were developed in tandem to ensure interoperability.

.. (Andrew Butterfield) **Stop Press**

    One of the candidates for the Research Fellow position with TCD
    has a lot of Isabelle/HOL experience and recent work has looked
    developing Isabelle/C, which captures C semantics in Isabelle.

Handling Assembler
------------------

One issue that has been raised is that of using formal methods
to assist in determining test coverage for assembly language.
The idea is we can take an assembler test-suite,
and produce a tool,
driven by a formal instruction-set architecture (ISA) model
that computes code coverage.
Magnus Myreen :cite:`Myreen:2012:Decompilation`
and Anthony Fox :cite:`Fox:2015:Decompilation`
have developed ISA models that cover a wide range of
processor designs, such as x86 and ARM.
They describe a process called "decompilation" that
converts machine-code into Hoare triples over the hardware state,
expressed in HOL4.
Fox also introduced the L3 domain specific language
to specify ISAs.
However the one architecture they don't treat is that of SPARC processors.
A treatment of the SPARCv8 architecture has been done in Isabelle/HOL
by Zhe Hou and colleagues :cite:`Hou:2016:ExeFM-of-LEON3`
which uses the LEON3 architecture as a concrete example.
This provides an executable formalisation of the integer unit
along with the register windowing,
and various aspects of memory access,
along with simple caching and trap models.
Not covered are hardware signals and interrupts,
or the modelling of concurrent behaviours at the ISA level.
They can export to OCaml for execution,
but the non-determinism induced by concurrency
makes it difficult to write HOL models (functions)
that satisfy the limitations on code generation.
The resulting work has also been submitted to
the Archive of Formal Proofs (AFP) :cite:`Hou:2016:FM-SPARCv8`.

All of the above artefacts are freely available.

If we were to look at assembler coverage in Task 3.2,
then the Isabelle/HOL SPARCv8 model would be a starting point.
This would not be cheap in terms of effort,
and raises the question:
would it not be easier to get coverage data from a SPARCv8/LEON4
simulator?

.. (Andrew Butterfield) **Stop Press**

    The candidate for the Research Fellow position with TCD
    who has a lot of Isabelle/HOL experience
    also spent time with David Sanan and others in Singapore,
    where the Isabelle/HOL models of SPARCv8 were developed.

More detailed description of what we actually explored.

A good survey of formal techniques and testing
is found in a 2009 ACM survey paper :cite:`Hierons:2009:FMT`.
They idea is that a formal specification of some form
may be able to support testing in a varie

 discussion of the automated reasoning tools
indicates that these can indeed support testing.
Model checkers produce counterexample witnesses,
and these can be converted into tests.
Temporal logics describe properties
that can again be converted into test sequences.
In :cite:`Hierons:2009:FMT` they clearly state:

  "The most important role for formal verification in testing
  is in the automated generation of test cases.
  In this context,
  model checking is the formal verification technology of choice;
  this is due to the ability of model checkers
  to produce counterexamples
  in case a temporal property does not hold for a system model."



Formal Method actually used
---------------------------

The current use of formal methods in RTEMS is based on using Promela to model
key RTEMS features, in such a way that we can generate tests using SPIN.
The delivered tests do not use the more advanced techniques we explored.

Promela/SPIN
^^^^^^^^^^^^

A technique mentioned based on the SPIN model checker, with its
modelling language called Promela (spinroot.com). Promela is quite a low-level
modelling language that makes it easy to get close to code level, and is
specifically targeted to modelling software. It is one of the most widely used
model-checkers, both in industry and education. It also has a tool called modex
that will automatically generate a Promela model from C code. It uses
linear-time temporal logic (LTL) to express properties of interest.

It is open-source, and very easy to install, needing only cc and lex/yacc.

Automation
~~~~~~~~~~

The ``spin`` program is command-line driven,
so it can be easily automated.
It's output is plain text reporting
with some structure.
We would need to decide how these get transformed
into a form suitable for the datapack.

It has a GUI interface as well which may assist in developing
Promela models.
These can always be subsequently exercised from the command-line.

Test Generation
~~~~~~~~~~~~~~~

Given a Promela model that checks successfully,
we can generated tests for a property P by asking
Spin to check its negation.
There are ways to get Spin to generate multiple counterexamples,
as well as getting it to find the shortest.
A tool called TorX was developed by the University of Twente
to produce tests :cite:`deVries:2000:FMT`, released under the Apache License,
but no longer seems to be downloadable.
Another system, *ScenTest* uses Promela to model and analyse test *scenarios*
which are then translated into tests for a Java implementation :cite:`Ulrich:2010:FMT`.
The tool requires Sparx Enterprise Architect, which is commercial.
Promela/SPIN along with LTL has been used to model/test a multi-core RTOS
called AUTOSAR :cite:`Fang:2012:FMT`. Key there is keeping the Promela
models close to the actual run-time environment.

.. (Manuel Coutinho) type -> implementation. Consider running a spellchecker (there are more errors).
.. (Andrew Butterfield) fixed - the editor I use, Atom,
  has a bad habit of autocompleting typos.
  Will check the document carefully.


Code Handling
~~~~~~~~~~~~~

There is a program called ``modex`` that extracts Promela models
from C code.
It assumes that the programmer is using a well-known thread library
such as pthreads,
so may not suit our needs.
Modex will take ``assert()`` statements in C code and bring those
into the Promela model, making it possible to have code annotations
that are available for interpretation by Spin.

However in a test using ``rtems/cpukit/score/src/chain.c``
we observe the following:

.. code-block:: c

    > verify chain.c

    	Extract Model:
    	--------------
    modex chain.c
    MODEX Version 2.11 - 3 November 2017
    chain.c:27: Error (syntax error, unexpected STAR, expecting RPAREN or COMMA) before '*'
      Chain_Control *the_chain,
                    ^
    1 errors
    modex: cannot happen fct decl1

Some of the tools like modex above, and Frama-C later,
report syntax errors on RTEMS code.
This may be due to differences in the syntax allowed between C99 and C11.
Whether or not RTEMS code should be, or can be,
modified to use a conservative coding style that satisfies both C99, C11,
where possible, is something that should be discussed.
This is related to the view in the SoW that we should adopt
the NASA/JPL approach to code that fails static analysis, even
if shown to be a false positive.
This is because these indicate some form of "code smell"
and the code should be re-written so that the tool no longer reports an error.

.. (Manuel Coutinho) I don't think it is feasible to change the RTEMS code in order to fit a tool
.. (Andrew Butterfield) Part of the SoW talks about adopting the
   NASA/JPL approach to code that fails static analysis, even
   if shown to be a false positive:namely that these indicate
   some form of "code smell" and the code should be re-written
   so that the tool no longer reports an error.
   This needs to be discussed.
   "rewrite" might be a better term to use here than "refactor".




Our chosen formal modelling is Promela/SPIN  (``spinroot.com``).
Promela is the modelling language, while SPIN is the model checking tool.

The modelling language is used to describe concurrent processes
executing with global shared state, as well as messaging mechanisms.
A key feature of the models is that they embody the non-determinism
found in concurrent systems.
The language also provides a variety of ways to specify desired properties,
ranging from special statement labels, the ``assert(...)`` statement,
up to temporal properties expressed in linear temporal logic.

SPIN runs in two modes.
The first, *simulation*, runs the model from the start, making random
choices whenever non-determinism occurs, and halting if the model terminates,
or a certain class of errors occur (deadlock, failed ``assert()``,...).
The second, "*verification*", explores all possible paths through the model.
If no errors are uncovered, SPIN reports success.
If an error is discovered, the sequence of events leading to that failure
(a *counterexample*) is issued in a so-called *trail* file.
SPIN can be set to halt when one error is encountered,
but can also be asked to search for all error paths.
Each trail file can be re-played by SPIN
to show the details of the erroneous scenario.

Scenario Notation
-----------------

While SPIN produces plenty of output to allow a user see what is happening,
it is not easy to parse.
Promela has a ``printf`` statement that can be used by a user to produce
tailored output.
These ``printf`` statements are executed during a simulation run,
or when a trail file is replayed.
They are not output during verification.

We use this facility to output all behaviour of interest
in a easy to parse format.
All of these lines are flagged by a prefix marker ("@@@")
that makes it easy for the test generation tools to filter them out
from the regular SPIN output.
We refer to these lines as model, feature or scenario *annotations*.


Test Generation
----------------

The key idea for test generation using model-checkers is the following:

  Phase 1: develop a correct model by using the model-checker as normally intended

  Phase 2: Pick a property
  (known be true when Phase 1 is completed),
  negate it, and run a verification.
  The model checker will establish its false and generate a counterexample.
  This is in fact a scenario showing correct model behaviour
  associated with that property.

With this process, we can obtain trail files that represent correct
(i.e. predicted) behaviours of the modelled systems.
We replay these with SPIN to obtain the resulting scenario annotations.

The test generation software takes these annotations
and uses them to lookup a YAML dictionary that maps annotations
to RTEMS test code.
These test code fragments are stitched together with some boilerplate code
to produce valid RTEMS test programs.

There are a number of configurations under which these tests can be run.
We can use simulators provided as part of the RTEMS tools (e.g. ``sis``),
and we also had access to real Leon processor hardware.
Tests can also be performed in settings where SMP is disable or enabled.
