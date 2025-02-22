% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2022 Trinity College Dublin

(promelamodelling)=

# Modelling with Promela

Promela is a large language with many features,
but only a subset is used here for test generation.
This is a short overview of that subset.
The definitive documentation can be found at
<https://spinroot.com/spin/Man/promela.html>.

## Promela Execution

Promela is a *modelling* language, not a programming language. It is designed
to describe the kind of runtime behaviors that make reasoning about low-level
concurrency so difficult: namely shared mutable state and effectively
non-deterministic interleaving of concurrent threads. This means that there are
control constructs that specify non-deterministic outcomes,
and an execution model that allows the specification of when threads should
block.

The execution model is based on the following concepts:

Interleaving Concurrency
: A running Promela system consists of one or more concurrent processes. Each
  process is described by a segment of code that defines a sequence of
  atomic steps. The scheduler looks at all the available next-steps and makes
  a **non-deterministic choice** of which one will run. The scheduler is
  invoked after every atomic step.

Executability
: At any point in time, a Promela process is either able to perform a step,
  and is considered executable, or is unable to do so, and is considered
  blocked. Whether a statement is executable or blocked may depend on the
  global state of the model. The scheduler will only select from among the
  executable processes.

The Promela language is based loosely on C, and the SPIN model-checking tool
converts a Promela model into a C program that has the specific model
hard-coded and optimized for whatever analysis has been invoked. It also
supports the use of the C pre-processor.

### Simulation vs. Verification

SPIN can run a model in several distinct modes:

Simulation

: SPIN simply makes random choices for the scheduler to produce a possible
  execution sequence (a.k.a. scenario) allowed by the model. A readable
  transcript is written to `stdout` as the simulation runs.

  The simplest SPIN invocation does simulation by default:

  ```shell
  spin model.pml
  ```

Verification

: SPIN does an analysis of the whole model by exploring all the possible
  choices that the scheduler can make. This will continue until either all
  possible choices have been covered, or some form of error is uncovered.
  If verification ends successfully, then this is simply reported as ok.
  If an error occurs, verification stops, and the sequence of steps that led
  to that failure are output to a so-called trail file.

  The simplest way to run a verification is to give the `-run` option:

  ```shell
  spin -run model.pml
  ```

Replaying

: A trail file is an uninformative list of number-triples, but can be replayed
  in simulation mode to produce human-readable output.

  ```shell
  spin -t model.pml
  ```

## Promela Datatypes

Promela supports a subset of C scalar types (`short`, `int`), but also
adds some of its own (`bit`, `bool`, `byte`, `unsigned`).
It has support for one-dimensional arrays,
and its own variation of the C struct concept
(confusingly called a `typedef`!).
It has a single enumeration type called `mtype`.
There are no pointers in Promela, which means that modelling pointer
usage requires the use of arrays with their indices acting as proxies for
pointers.

## Promela Declarations

Variables and one-dimensional arrays can be declared in Promela in much the
same way as they are done in C:

```C
int x, y[3] ;
```

All global variables and arrays are initialized to zero.

The identifier `unsigned` is the name of a type, rather than a modifier.
It is used to declare an unsigned number variable with a given bit-width:

```C
unsigned mask : 4 ;
```

Structure-like datatypes in Promela are defined using the `typedef` keyword
that associates a name with what is basically a C `struct`:

```C
typedef CBuffer {
  short count;
  byte buffer[8]
}

CBuffers cbuf[6];
```

Note that we can have arrays of `typedef`s that themselves contain arrays.
This is the only way to get multi-dimensional arrays in Promela.

There is only one enumeration type, which can be defined incrementally.
Consider the following sequence of four declarations that defines the values in
`mtype` and declares two variables of that type:

```C
mtype = { up, down } ;
mtype dir1;
mtype = { left, right} ;
mtype dir2;
```

This gives the same outcome with the following two declarations:

```C
mtype = { left, right, up, down } ;
mtype dir1, dir2;
```

### Special Identifiers

The are a number of variable identifiers that have a special meaning in Promela.
These all start with an underscore. We use the following:

Process Id
: `_pid` holds the process id of the currently active process

Process Count
: `_nr_pr` gives the number of currently active processes.

## Promela Atomic Statements

Assignment

: `x = e` where `x` is a variable and `e` is an expression.

  Expression `e` must have no side-effects. An assignment is always
  executable. Its effect is to update the value of `x` with the current
  value of `e`.

Condition Statement

: `e` where `e` is an expression

  Expression `e`, used standalone as a statement, is executable if its
  value in the current state is non-zero. If its current value is zero,
  then it is blocked. It behaves like a NO-OP when executed.

Skip

: `skip`, a keyword

  `skip` is always executable, and behaves like a NO-OP when executed.

Assertion

: `assert(e)` where `e` is an expression

  An assertion is always executable. When executed, it evaluates its
  expression. If the value is non-zero, then it behaves like a NO-OP. If the
  value is zero, then it generates an assertion error and aborts further
  simulation/verification of the model.

Printing

: `printf(string,args)` where `string` is a format-string and `args`
  are values and expressions.

  A `printf` statement is completely ignored in verification mode.
  In simulation mode, it is always executable,
  and generates output to `stdout` in much the same way as in C.
  This is is used in a structured way to assist with test generation.

Goto

: `goto lbl` where `lbl` is a statement label.

  Promela supports labels for statements, in the same manner as C.
  The `goto` statement is always executable.
  When executed, flow of control goes to the statement labelled by `lbl:`.

Break

: `break`, a keyword

  Can only occur within a loop (`do ... od`, see below). It is always
  executable, and when executed performs a `goto` to the statement just
  after the end of the innermost enclosing loop.

## Promela Composite Statements

Sequencing

: `{ <stmt> ; <stmt> ; ... ; <stmt> }` where each `<stmt>` can be any
  kind of statement, atomic or composite. The sub-statements execute in
  sequence in the usual way.

Selection

: > ```none
  > if
  > :: <stmt>
  > :: <stmt>
  > ...
  > :: <stmt>
  > fi
  > ```

  A selection construct is blocked if all the `<stmt>` are blocked. It is
  executable if at least one `<stmt>` is executable. The scheduler will make
  a non-deterministic choice from all of those `<stmt>` that are executable.
  The construct terminates when/if the chosen `<stmt>` does.

  Typically, a selection statement will be a sequence of the form
  `g ; s1 ; ... ; sN` where `g` is an expression acting as a guard,
  and the rest of the statements are intended to run if `g` is non-zero.
  The symbol `->` plays the same syntactic role as `;`, so this allows
  for a more intuitive look and feel; `g -> s1 ; ... ; sN`.

  If the last `<stmt>` has the form `else -> ...`, then the `else` is
  executable only when all the other selection statements are blocked.

Repetition

: ```none
  do
  :: <stmt>
  :: <stmt>
  ...
  :: <stmt>
  od
  ```

  The executability rules here are the same as for Selection above. The key
  difference is that when/if a chosen `<stmt>` terminates, then the whole
  construct is re-executed, making it basically an infinite loop. The only
  way to exit this loop is for an active `<stmt>` to execute a `break`
  or `goto` statement.

  A `break` statement only makes sense inside a Repetition, is always
  executable, and its effect is to jump to the next statement after the
  next `od` keyword in text order.

The selection and repetition syntax and semantics are based on Edsger
Djikstra's Guarded Command Language {cite}`Djikstra:1975:GCL` .

Atomic Composite

: `atomic{stmt}` where `stmt` is usually a (sequential) composite.

  Wrapping the `atomic` keyword around a statement makes its entire
  execution proceed without any interference from the scheduler. Once it is
  executable, if the scheduler chooses it to run, then it runs to completion.

  There is one very important exception: if it should block internally because
  some sub-statement is blocked, then the atomicity gets broken, and the
  scheduler is free to find some other executable process to run. When/if the
  sub-statement eventually becomes executable, once it gets chosen to run by
  the scheduler then it continues to run atomically.

Processes

: `proctype name (args) { sequence }` where `args` is a list of zero
  or more typed parameter declarations,
  and `sequence` is a list of local declarations and statements.

  This defines a process type called `name` which takes parameters defined
  by `args` and has the behavior defined by `sequence`. When invoked, it
  runs as a distinct concurrent process. Processes can be invoked explicitly
  by an existing process using the `run` statement,
  or can be setup to start automatically.

Run

: `run name (exprs)` where `exprs` is a list of expressions that match
  the arguments defined the `proctype` declaration for `name`.

  This is executable as long as the maximum process limit has not been reached,
  and immediately starts the process running.
  It is an atomic statement.

Inlining

: `inline name (names) { sequence }` where `names` is a list of zero or
  more identifiers, and `sequence` is a list of declarations and statements.

  Inlining does textual substitution, and does not represent some kind of
  function call. An invocation `name(texts)` gets replaced by
  `{ sequence }` where each occurrence of an identifier in `names` is
  replaced by the corresponding text in `texts`. Such an invocation can
  only appear in a context where a Promela statement can appear.

## Promela Top-Level

At the top-level, a Promela model is a list of declarations, much like a C
program. The Promela equivalent of `main` is a process called `init` that
has no arguments. There must be at least one Promela process setup to be running
at the start. This can be `init`, or one or more `proctype`s declared as
`active`.
