.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

Test Generation Methodology
===========================

The general approach to using any model-checking technology for test generation
has three major steps:

Model desired behavior
----------------------

Construct a model that describes the desired properties (`P1`, ..., `PN`)
and use the model-checker to verify those properties.

Promela can specify properties using the ``assert()`` statement, to be
true at the point where it gets executed, and can use Linear Temporal Logic
(LTL) to specify more complex properties over execution sequences. SPIN will
also check generic correctness properties such as deadlock and
livelock freedom.

Make claims about undesired behavior
------------------------------------

Given a fully verified model, systematically negate each specified property.
Given that each property was verified as true, 
then these negated properties will fail model-checking, 
and counter-examples will be
generated. These counter-examples will in fact be scenarios describing correct
behavior of the system, demonstrating the truth of each property.

.. warning::

  It is very important that the negations only apply to stated properties,
  and do not alter the possible behaviors of the model in any way.

With Promela, there are a number of different ways to do systematic
negation. The precise approach adopted depends the nature of the models, and
more details can be found 
in the RTEMS Formal Models Guide Appendix in this document.

Map good behavior scenarios to tests
--------------------------------------

Define a mapping from counter-example output to test code, 
and use this in the process of constructing a test program.

A YAML file is used to define a mapping from SPIN output to
relevant fragments of RTEMS C test code, using the Test Framework section
in this document. 
The process is automated by a python script called ``testbuilder``.

