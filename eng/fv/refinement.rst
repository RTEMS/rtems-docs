.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

Promela to C Refinement
=======================

Promela models are more abstract than concrete C code. We need to establish a
rigourous link, known as a :term:`refinement`, from Promela to C. This is composed of
two parts: manual annotations in the Promela model to make its behaviour easy
to identify and parse; and a refinement defined as a YAML file that maps from
annotations to corresponding C code.

**GB: In section "9.4 Promela to C Refinement" what is the name of the YAML
file? Is there more than one, or is it unique.**

Model Annotations
-----------------

We use ``printf`` statements in the Promela models to output information that
is used by ``spin2test`` to generate test code. This information is used to
lookup keys in a YAML file that defines the mapping to C code. It uses a simple
format that makes it easy to parse and process, and is also designed to be
easily understood by a human reader. This is important because any V&V process
will require this information to be carefully assessed.

Annotation Syntax
^^^^^^^^^^^^^^^^^

Format, where :math:`N \geq 0`:

  ``@@@ <pid> <KEYWORD> <parameter1> ... <parameterN>``

The leading ``@@@`` is a marker that makes it easy to filter out this
information from other SPIN output.

Parameters take the following forms:

  ``<pid>``  Promela Process Id of ``proctype`` generating annotation

  ``<word>`` chunk of text containing no white space

  ``<name>`` Promela variable/structure/constant identifier

  ``<type>`` Promela type identifier

  ``<tid>``  OS Task/Thread/Process Id

  ``_``  unused argument (within containers)

Each ``<KEYWORD>`` is associated with specific forms of parameters:

.. code-block:: none

  LOG <word1> ... <wordN>
  NAME <name>
  INIT
  DEF <name> <value>
  DECL <type> <name> [<value>]
  DCLARRAY <type> <name> <value>
  TASK <name>
  SIGNAL <name> <value>
  WAIT   <name> <value>
  STATE tid <name>
  SCALAR (<name>|_) [<index>] <value>
  PTR <name> <value>
  STRUCT <name>
  SEQ <name>
  END <name>
  CALL <name> <value1> ... <valueN>


Annotation Lookup
-----------------

The way that code is generated depends on the keyword in the annotation.
In particular, the keyword determines how, or if,
the YAML refinement file is looked up.

  Direct Output - no lookup
  (``LOG``, ``DEF``)

  Keyword Refinement - lookup the ``<KEYWORD>``
  (``NAME``, ``INIT``, ``SIGNAL``, ``WAIT``)

  Name Refinement - lookup first parameter (considered as text)
  (``TASK``, ``DECL``, ``DCLARRAY``, ``PTR``, ``CALL``, ``SCALAR``)

The same name may appear in different contexts,
and so we can extend the name with a suffix of the form
``_XXX`` to lookup less frequent uses:

  ``_DCL`` - A variable declaration

  ``_PTR`` - The pointer value itself

  ``_FSCALAR`` - A scalar that is a struct field

  ``_FPTR`` - A pointer that is a struct field

Generally, the keyword, or name is used to lookup ``mymodel-rfn.yml`` to get a
string result. This string typically has substitution placeholders, as used by
the Python ``format()`` method for strings. The other parameters in the
annotation are then textually substituted in, to produce a segment of test code.

This is all implemented in the source file
``formal/promela/src/src/refine_command.coco``.


Lookup Example
^^^^^^^^^^^^^^

Consider the following annotation, from the Events Manager model:

  ``@@@ 1 CALL event_send 1 2 10 sendrc``

This uses Name refinement so we lookup ``send``
and get back the following text:

.. code-block:: python3

  T_log( T_NORMAL, "Calling Send(%d,%d)", mapid( ctx, {1}), {2} );
  {3} = ( *ctx->send )( mapid( ctx, {1} ), {2} );
  T_log( T_NORMAL, "Returned 0x%x from Send", {3} );

We then substitute in arguments ``1``, ``2``, ``10``, and ``sendrc``
to get the code:

.. code-block:: c

  T_log( T_NORMAL, "Calling Send(%d,%d)", mapid( ctx, 2), 10 );
  sendrc = ( *ctx->send )( mapid( ctx, 2 ), 10 );
  T_log( T_NORMAL, "Returned 0x%x from Send", sendrc );

Given a Promela process id of ``1``, this code is put into a code segment
for the corresponding RTEMS task.




Specifying Refinement
---------------------

Using the terminology of the RTEMS Test Framework (Section
:numref:`RTEMSTestFramework`) we convert each Promela model into a set of
Test Cases, one for each complete scenario produced by test generation. We have
a number of template files, tailored for each model, that are used to assemble
the test code sources, along with code segments for each Promela process, based
on the annotations output for any given scenario.


The refinement mapping from annotations to code is defined in a YAML file that
describes a Python dictionary that maps a name to some C code, with placeholders
that are used to allow for substituting in actual test values.

The YAML file has entries of the following form:

.. code:: yaml

    entity: |
      C code line1{0}
      ...
      C code lineM{2}

The entity is a reference to an annotation concept, which can refer to key
declarations, values, variables, types, API calls or model events. There can be
zero or more arguments in the annotations, and any occurrence of braces
enclosing a number in the C code means that the corresponding annotation
argument string is substituted in (using the python string object `format()`
method).

The general pattern is that we work through all the annotations in order. The
code we obtain by looking up the YAML file is collated into different
code-segments, on for each Promela process id (``<pid>``).

In addition to the explicit annotations generated by the Promela models, there
are two implicit annotations produced by the python refinement code. These
occur when the ``<pid>`` part of a given explicit annotation is different to the
one belonging to the immediately preceding annotation. This indicates a point in
a test generation scenario where one task is suspended and another resumes. This
generates internal annotations with keywords ``SUSPEND`` and ``WAKEUP`` which
should have entries in the refinement file to provide code to ensure that the
corresponding RTEMS tasks in the test behave accordingly.

We can also emit the annotation as a comment into the generated test-code, so
it is easy to check that parameters are correct, and the generated code is
correct.

If a lookup fails, we output a C comment line stating the lookup failed. We
don't abort the translation but continue the translation.


Annotation Refinement Guide
---------------------------


LOG
^^^

``LOG <word1> ... <wordN>`` (Direct Output)
    We generate a call to ``T_log()`` with a message formed from the ``<word..>``
    parameters.

NAME
^^^^

``NAME <name>`` (Keyword Refinement)
    We lookup ``NAME`` (currently ignoring ``<name>``) and returns the resulting
    text as is as part of the code. This code should define the name of the
    testcase, if needed.

INIT
^^^^

``INIT`` (Keyword Refinement)
    Lookup ``INIT`` and expect to obtain test initialisation code.

TASK
^^^^

``TASK <name>`` (Name Refinement)
    Lookup ``<name>`` and return corresponding C code.

SIGNAL
^^^^^^

``SIGNAL <value>`` (Keyword Refinement)
    Lookup `SIGNAL` and return code with `<value>` substituted in.

WAIT
^^^^

``WAIT <value>`` (Keyword Refinement)
    Lookup `WAIT` and return code with `<value>` substituted in.

DEF
^^^

``DEF <name> <value>`` (Direct Output)
    Output ``#define <name> <value>``.

DECL
^^^^

``DECL <type> <name> [<value>]`` (Name Refinement)
    Lookup ``<name>_DCL`` and substitute ``<name>`` in. If ``<value>`` is
    present, append ``=<value>``. Add a final semicolon. If the `<pid>` value
    is zero, prepend ``static``.

DCLARRAY
^^^^^^^^

``DCLARRAY <type> <name> <value>`` (Name Refinement)
    Lookup ``<name>_DCL`` and substitute ``<name>`` and ``<value>`` in. If the
    `<pid>` value is zero, prepend ``static``.

CALL
^^^^

``CALL <name> <value0> .. <valueN>`` (Name refinement, ``N`` < 6)
    Lookup ``<name>`` and substitute all ``<value..>`` in.

STATE
^^^^^

``STATE <tid> <name>`` (Name Refinement)
    Lookup ``<name>`` and substitute in ``<tid>``.

STRUCT
^^^^^^

``STRUCT <name>``
    Declares that are we going to output the contents of variable ``<name>``
    that is itself a structure. The ``<name>`` is noted, as is the fact we are
    processing a structured value. We should not already be processing a
    structure or a sequence.

SEQ
^^^

``SEQ <name>``
    Declares that are we going to output the contents of variable ``<name>``
    that is itself a sequence/array. The ``<name>`` is noted, as is the fact we
    are processing a structured value. We will accumulate values in a string
    that is now initialsed to empty. We should not already be processing a
    structure or a sequence.

PTR
^^^

``PTR <name> <value>`` (Name Refinement)
    If not inside a ``STRUCT``, lookup ``<name>_PTR``. Two lines of code should
    be returned. If the ``<value>`` is zero, use the first line, otherwise use
    the second with ``<value>`` substituted in. This is required to handle NULL
    pointers.

    If inside a ``STRUCT``, lookup ``<name>_FPTR``. Two lines of code should
    be returned. If the ``<value>`` is zero, use the first line, otherwise use
    the second with ``<value>`` substituted in. This is required to handle NULL
    pointers.

SCALAR
^^^^^^

We have quite a few variations here.

``SCALAR _ <value>``
    Should only be used inside a ``SEQ``. A space and ``<value>`` is appended
    to the string being accumulated by this ``SEQ``.

``SCALAR <name> <value>`` (Name Refinement)
    If not inside a ``STRUCT``, lookup ``<name>``, and substitute ``<value>``
    into the resulting code.

    If inside a ``STRUCT``, lookup ``<name>_FSCALAR`` and substitute the saved
    ``STRUCT`` name and ``<value>`` into the resulting code.

    This should not be used inside a ``SEQ``.

``SCALAR <name> <index> <value>`` (Name Refinement)
    If not inside a ``STRUCT``, lookup ``<name>``, and substitute ``<index>``
    and ``<value>`` into the resulting code.

    If inside a ``STRUCT``, lookup ``<name>_FSCALAR`` and substitute the saved
    ``STRUCT`` name and ``<value>`` into the resulting code.

    This should not be used inside a ``SEQ``.

END
^^^

``END <name>``
    If inside a ``STRUCT``, indicate that we are no longer processing a
    structured variable.

    If inside a ``SEQ``, lookup ``<name>_SEQ``. For each line of code obtained,
    substitute in the saved sequence string. Indicate that we are no longer
    processing a sequence/array variable.

    This should not be encountered outside of a ``STRUCT`` or ``SEQ``.

SUSPEND and WAKEUP
^^^^^^^^^^^^^^^^^^

We have found a change of Promela process id from ``oldid`` to ``newid``. We
have incremented a counter that tracks the number of such changes.

``SUSPEND``  (Keyword Refinement)

    Lookup ``SUSPEND`` and substitute in the counter value, ``oldid`` and
    ``newid``.

``WAKEUP``  (Keyword Refinement)

    Lookup ``WAKEUP`` and substitute in the counter value, ``newid`` and
    ``oldid``.

Annotation Ordering
-------------------

While most annotations occur in an order determined by any given test scenario,
there are some annotations that need to be issued first. These are, in order:
``NAME``, ``DEF``, ``DECL`` and ``DCLARRAY``, and finally, ``INIT``.
