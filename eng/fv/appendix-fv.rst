.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

Appendix: RTEMS Formal Model Guide
**********************************

This appendix covers the various formal models of RTEMS that are currently in
existence. It serves two purposes:
one is to provide detailed documentation of each model,
while the other is provide a guide into how to go about developing and deploying such models.

The general approach followed here is to start by looking at the API documentation and identifying the key data-structures and function prototypes.
These are then modelled appropriately in Promela.
Then, general behavior patterns of interest are identified,
and the Promela model is extended to provide those patterns.
A key aspect here is exploiting the fact that Promela allows non-deterministic choices to be specified, which gives the effect of producing arbitrary orderings of model behavior.
All of this leads to a situation were the SPIN model-checker can effectively generate scenarios for all possible interleavings.
The final stage is mapping those scenarios to RTEMS C test code,
which has two parts: generating machine-readable output from SPIN, and developing the refinement mapping from that output to C test code.

Some familiarity is assumed here with the Software Test Framework section in this document.

The following models are included in the directory ``formal/promela/models/``
at the top-level in ``rtems-central``:

Chains API (``chains/``)
    Models the unprotected chain append and get API calls in the Classic
    Chains API Guide. This was an early model to develop the basic methodology.

Events Manager (``events/``)
    Models the behaviour of all the API calls in the Classic Events Manager API
    Guide. This had to tackle real concurrency and deal with multiple CPUs and priority
    issues.

Barrier Manager (``barriers/``)
    Models the behaviour of all the API calls in then Classic Barrier Manager API.

Message Manager (``messages/``)
    Models the create, send and receive API calls in the Classic Message Manager API.

At the end of this guide is a section that discusses various issues that should be tackled in future work.

Testing Chains
--------------

Documentation:  Chains section in the RTEMS Classic API Guide.

Model Directory: ``formal/promela/models/chains``.

Model Name: ``chains-api-model``.

The Chains API provides a doubly-linked list data-structure, optimised for fast
operations in an SMP setting. It was used as proof of concept exercise,
and focussed on just two API calls: ``rtems-chain-append-unprotected``
and ``rtems-chain-get-unprotected`` (hereinafter just ``append`` and ``get``).


API Model
^^^^^^^^^

File: ``chains-api-model.pml``

While smart code optimization techniques are very important for RTEMS code,
the focus when constructing formal models is on functional correctness,
not performance. What is required is the simplest, most obviously correct model.

The ``append`` operation adds new nodes on the end of the list,
while ``get`` removes and returns the node at the start of the list.
The Chains API has many other operations that can add/remove nodes at either end, or somewhere in the middle, but these are considered out of scope.

Data Structures
~~~~~~~~~~~~~~~

There are no pointers in Promela, so we have to use arrays,
with array indices modelling pointers.
With just ``append`` and ``get``, an array can be used to implement a collection
of nodes in memory.
A ``Node`` type is defined that has next and previous indices,
plus an item payload.
Access to the node list is via a special control node with head and tail pointers.
In the model, an explicit size value is added to this control node,
to allow the writing of properties about chain length,
and to prevent array out-of-bound errors in the model itself.
We assume a single ``chain``,
with list node storage statically allocated in ``memory``.

.. code:: c

  #define PTR_SIZE 3
  #define MEM_SIZE 8

  typedef Node {
    unsigned nxt  : PTR_SIZE
  ; unsigned prv  : PTR_SIZE
  ; byte     itm
  }
  Node memory[MEM_SIZE] ;

  typedef Control {
    unsigned head : PTR_SIZE;
    unsigned tail : PTR_SIZE;
    unsigned size : PTR_SIZE
  }
  Control chain ;

While there are 8 memory elements, element 0 is inaccessible,
as the index 0 is treated like a ``NULL`` pointer.

Function Calls
~~~~~~~~~~~~~~

The RTEMS prototype for ``append`` is:

.. code:: c

  void rtems_chain_append_unprotected(
      rtems_chain_control *the_chain,
      rtems_chain_node    *the_node
  );

Its implementation starts by checking that the node to be appended is "off
chain", before performing the append.
The model is designed to satisfy this property so the check is not modelled.
Also, the Chains documentation is not clear about certain error cases.
As this is a proof of concept exercise, these details are not modelled.

A Promela inline definition ``append`` models the desired behavior,
simulating C pointers with array addresses. Here ``ch`` is the chain argument,
while ``np`` is a node index.
The model starts by checking that the node pointer is not ``NULL``,
and that there is room in ``memory`` for another node.
These are to ensure that the model does not have any runtime errors.
Doing a standard model-check of this model finds no errors,
which indicates that those assertions are never false.

.. code:: c

  inline append(ch,np) {
    assert(np!=0); assert(ch.size < (MEM_SIZE-1));
    if
    :: (ch.head == 0) -> ch.head = np; ch.tail = np; ch.size = 1;
                         memory[np].nxt = 0; memory[np].prv = 0;
    :: (ch.head != 0) -> memory[ch.tail].nxt = np; memory[np].prv = ch.tail;
                         ch.tail = np; ch.size = ch.size + 1;
    fi
  }

The RTEMS prototype for ``get`` is:

.. code:: c

  rtems_chain_node *rtems_chain_get_unprotected(
    rtems_chain_control *the_chain
  );

It returns a pointer to the node, with ``NULL`` returned if the chain is empty.

Promela inlines involve textual substitution,
so the concept of returning a value makes no sense.
For ``get``,  the model is that of a statement that assigns the return value to
a variable. Both the function argument and return variable name are passed as parameters:

.. code:: c

  /* np = get(ch); */
  inline get(ch,np) {
    np = ch.head ;
    if
      :: (np != 0) ->
          ch.head = memory[np].nxt;
          ch.size = ch.size - 1;
          // memory[np].nxt = 0
      :: (np == 0) -> skip
    fi
    if
      :: (ch.head == 0) -> ch.tail = 0
      :: (ch.head != 0) -> skip
    fi
  }

Behavior patterns
^^^^^^^^^^^^^^^^^

File: ``chains-api-model.pml``

A key feature of using a modelling language like Promela is that it has both
explicit and implicit non-determinism. This can be exploited so that SPIN will
find all possible interleavings of behavior.

The Chains API model consists of six processes, three which perform ``append``,
and three that perform ``get``, waiting if the chain is empty. This model relies
on implicit non-determinism, in that the SPIN scheduler can choose and switch
between any unblocked process at any point. There is no explicit non-determinism
in this model.

Promela process ``doAppend`` takes node index ``addr`` and a value ``val`` as
parameters. It puts ``val`` into the node indexed by ``addr``,
then calls ``append``, and terminates.
It is all made atomic to avoid unnecessary internal interleaving of operations because unprotected versions of API calls should only be used when interrupts
are disabled.

.. code:: c

  proctype doAppend(int addr; int val) {
    atomic{ memory[addr].itm = val;
            append(chain,addr); } ;
  }

The ``doNonNullGet`` process waits for the chain to be non-empty before attempting to ``get`` an element. The first statement inside the atomic
construct is an expression, as a statements, that blocks while it evaluates to
zero. That only happens if ``head`` is in fact zero. The model also has an
assertion that checks that a non-null node is returned.

.. code:: c

  proctype doNonNullGet() {
    atomic{
      chain.head != 0;
      get(chain,nptr);
      assert(nptr != 0);
    } ;
  }

All processes terminate after they have performed their (sole) action.

The top-level of a Promela model is an initial process declared by the ``init`` construct. This initializes the chain as empty and then runs all six processes concurrently. It then uses the special ``_nr_pr`` variable to wait for all six
processes to terminate. A final assertion checks that the chain is empty.

.. code:: c

  init {
    pid nr;
    chain.head = 0; chain.tail = 0; chain.size = 0 ;
    nr = _nr_pr;  // assignment, sets `nr` to current number of procs
    run doAppend(6,21);
    run doAppend(3,22);
    run doAppend(4,23);
    run doNonNullGet();
    run doNonNullGet();
    run doNonNullGet();
    nr == _nr_pr; // expression, waits until number of procs equals `nr`
    assert (chain.size == 0);
  }

Simulation of this model will show some execution sequence in which the appends
happen in a random order, and the gets also occur in a random order, whenever
the chain is not empty. All assertions are always satisfied, including the last
one above. Model checking this model explores all possible interleavings and reports no errors of any kind. In particular, when the model reaches the last
assert statement, the chain size is always zero.

SPIN uses the C pre-processor, and generates the model as a C program. This
model has a simple flow of control: basically execute each process once in an
almost arbitrary order, assert that the chain is empty, and terminate. Test
generation here just requires the negation of the final assertion to get all
possible interleavings. The special C pre-processor definition ``TEST_GEN`` is
used to switch between the two uses of the model. The last line above is
replaced by:

.. code:: c

  #ifdef TEST_GEN
    assert (chain.size != 0);
  #else
    assert (chain.size == 0);
  #endif

A test generation run can then be invoked by passing in ``-DTEST_GEN`` as a
command-line argument.

Annotations
^^^^^^^^^^^

File: ``chains-api-model.pml``

The model needs to have ``printf`` statements added to generation the
annotations used to perform the test generation.

This model wraps each of six API calls in its own process, so that model
checking can generate all feasible interleavings. However, the plan for the test code is that it will be just one RTEMS Task, that executes all the API
calls in the order determined by the scenario under consideration. All the
annotations in this model specify ``0`` as the Promela process identifier.

Data Structures
~~~~~~~~~~~~~~~

Annotations have to be provided for any variable or datastructure declarations
that will need to have corresponding code in the test program.
These have to be printed out as the model starts to run.
For this model, the ``MAX_SIZE`` parameter is important,
as are the variables ``memory``, ``nptr``, and ``chain``:

.. code:: c

  printf("@@@ 0 NAME Chain_AutoGen\n")
  printf("@@@ 0 DEF MAX_SIZE 8\n");
  printf("@@@ 0 DCLARRAY Node memory MAX_SIZE\n");
  printf("@@@ 0 DECL unsigned nptr NULL\n")
  printf("@@@ 0 DECL Control chain\n");

At this point, a parameter-free initialization annotation is issued. This should
be refined to C code that initializes the above variables.

.. code:: c

  printf("@@@INIT\n");

Function Calls
~~~~~~~~~~~~~~

For ``append``, two forms of annotation are produced. One uses the ``CALL``
format to report the function being called along with its arguments. The other
form reports the resulting contents of the chain.

.. code:: c

   proctype doAppend(int addr; int val) {
     atomic{ memory[addr].itm = val; append(chain,addr);
             printf("@@@ 0 CALL append %d %d\n",val,addr);
             show_chain();
           } ;
   }

The statement ``show_chain()`` is an inline function that prints the
contents of the chain after append returns.
The resulting output is multi-line,
starting with ``@@@ 0 SEQ chain``,
ending with ``@@@ 0 END chain``,
and with entries in between of the form ``@@@ 0 SCALAR _ val``
displaying chain elements, line by line.

Something similar is done for ``get``, with the addition of a third annotation
``show_node()`` that shows the node that was got:

.. code:: c

  proctype doNonNullGet() {
    atomic{
      chain.head != 0;
      get(chain,nptr);
      printf("@@@ 0 CALL getNonNull %d\n",nptr);
      show_chain();
      assert(nptr != 0);
      show_node();
    } ;
  }

The statement ``show_node()`` is defined as follows:

.. code:: c

  inline show_node (){
    atomic{
      printf("@@@ 0 PTR nptr %d\n",nptr);
      if
      :: nptr -> printf("@@@ 0 STRUCT nptr\n");
                 printf("@@@ 0 SCALAR itm %d\n", memory[nptr].itm);
                 printf("@@@ 0 END nptr\n")
      :: else -> skip
      fi
    }
  }

It prints out the value of ``nptr``, which is an array index. If it is not zero,
it prints out some details of the indexed node structure.

Annotations are also added to the ``init`` process to show the chain and node.

.. code:: c

  chain.head = 0; chain.tail = 0; chain.size = 0;
  show_chain();
  show_node();

Refinement
^^^^^^^^^^

Files:

  ``chains-api-model-rfn.yml``

  ``chains-api-model-pre.h``

  ``tr-chains-api-model.c``

Model annotations are converted to C test code using a YAML file that maps
single names to test code snippets into which parameters can be substituted.
Parameters are numbered from zero, and the ``n`` th parameter will be substituted
wherever ``{n}`` occurs in the snippet.

Refinement is more than just the above mapping from annotations to code. Some of
this code will refer to C variables, structures, and functions that are needed
to support the test. Some of these are declared ``chains-api-model-pre.h`` and implemented in ``tr-chains-api-model.c``.

Data Structures
~~~~~~~~~~~~~~~

The initialization generates one each of ``NAME``, ``DEF``, ``DCLARRAY``, and
``INIT`` annotations, and two ``DECL`` annotations.

The ``DEF`` entry is currently not looked up as it is automatically converted to a ``#define``.

The ``NAME`` annotation is used to declare the test case name, which is
stored in the global variable ``rtems_test_name``. The current
refinement entry is:

.. code:: python

   NAME: |
     const char rtems_test_name[] = "Model_Chain_API";

In this case, the name is fixed and ignores what is declared in the model.

The ``DCLARRAY Node memory MAX_SIZE`` annotation looks up ``memory_DCL`` in the
refinement file, passing in ``memory`` and ``MAX_SIZE`` as arguments. The entry in the refinement file is:

.. code:: python

  memory_DCL: item {0}[{1}];

Here ``item`` is the type of the chains nodes used in the test code. It is
declared in ``chains-api-model.pre.h`` as:

.. code:: c

  typedef struct item
  {
      rtems_chain_node node;
      int               val;
  } item;

Substituting the arguments gives:

.. code:: c

  item memory[MAX_SIZE];

The two ``DECL`` annotations have two or three parameters. The first is the
type, the second is the variable name, and the optional third is an initial
value. The lookup key is the variable name with ``_DCL`` added on.
In the refinement file, the entry only provides the C type, and the other parts of the declaration are added in.
The entries are:

.. code:: python

  nptr_DCL: item *
  chain_DCL: rtems_chain_control

Annotation ``DECL unsigned nptr NULL`` results in:

.. code:: c

  item * nptr = NULL ;

Annotation ``DECL Control chain`` results in:

.. code:: c

  rtems_chain_control chain ;

The ``INIT`` annotation is looked up as ``INIT`` itself. It should be mapped to
code that does all necessary initialization. The refinement entry for chains is:

.. code:: python

  INIT: rtems_chain_initialize_empty( &chain );

In addition to all the above dealing with declarations and initialization,
there are the annotations,  already described above, that are used to display
composite values, such as structure contents, and chain contents.

In the model, all accesses to individual chain nodes are via index ``nptr``,
which occurs in two types of annotations, ``PTR`` and ``STRUCT``. The ``PTR``
annotation is refined by looking up ``nptr_PTR`` with the value of ``nptr`` as the sole argument. The refinement entry is:

.. code:: python

  nptr_PTR: |
    T_eq_ptr( nptr, NULL );
    T_eq_ptr( nptr, &memory[{0}] );

The first line is used if the value of ``nptr`` is zero, otherwise the second
line is used.

The use of ``STRUCT`` requires three annotation lines in a row, *e.g.*:

.. code:: c

  @@@ 0 STRUCT nptr
  @@@ 0 SCALAR itm 21
  @@@ 0 END nptr

The ``STRUCT`` and ``END`` annotations do not generate any code, but open and
close a scope in which ``nptr`` is noted as the "name" of the struct. The
``SCALAR`` annotation is used to observe simple values such as numbers or booleans. However, within a ``STRUCT`` it belongs to a C ``struct``, so the
relevant field needs to be used to access the value.
Within this scope, the scalar variable ``itm`` is looked up as a field name,
by searching for ``itm_FSCALAR`` with arguments``nptr`` and ``21``, which returns the entry:

.. code:: python

  itm_FSCALAR:   T_eq_int( {0}->val, {1} );

This gets turned into the following test:

.. code:: c

  T_eq_int( nptr->val, 21 );

A similar idea is used to test the contents of a chain. The annotations produced
start with a ``SEQ`` annotation, followed by a ``SCALAR`` annotation for each
item in the chain, and then ending with an ``END`` annotation. Again, there is
a scope defined where the ``SEQ`` argument is the "name" of the sequence.
The ``SCALAR`` entries have no name here (indicated by ``_``), and their values
are accumulated in a string, separated by spaces. Test code generation is
triggered this time by the ``END`` annotation, that looks up the "name" with ``_SEQ`` appended, and the accumulated string as an argument. The corresponding entry for chain sequences is:

.. code:: python

  chain_SEQ: |
    show_chain( &chain, ctx->buffer );
    T_eq_str( ctx->buffer, "{0} 0" );

So, the following chain annotation sequence:

.. code:: c

  @@@ 0 SEQ chain
  @@@ 0 SCALAR _ 21
  @@@ 0 SCALAR _ 22
  @@@ 0 END chain

becomes the following C code:

.. code:: C

  show_chain( &chain, ctx->buffer );
  T_eq_str( ctx->buffer, " 21 22 0" );

C function ``show_chain()`` is defined in ``tr-chains-api-model.c`` and
generates a string with exactly the same format as that produced above. These
are then compared for equality.

.. note::

  The Promela/SPIN model checker's prime focus is modelling and verifying
  concurrency related properties. It is not intended for verifying sequential
  code or data transformations. This is why some of the ``STRUCT``/``SEQ``
  material here is so clumsy. It plays virtually no role in the other models.

Function Calls
~~~~~~~~~~~~~~

For ``@@@ 0 CALL append 22 3`` lookup ``append`` to get

.. code-block:: c

     memory[{1}].val = {0};
     rtems_chain_append_unprotected( &chain, (rtems_chain_node*)&memory[{1}] );

Substitute ``22`` and ``3`` in to produce

.. code-block:: c

     memory[3].val = 22;
     rtems_chain_append_unprotected( &chain, (rtems_chain_node*)&memory[3] );

For ``@@@ 0 CALL getNonNull 3`` lookup ``getNonNull`` to obtain

.. code:: c

  nptr = get_item( &chain );
  T_eq_ptr( nptr, &memory[{0}] );

Function ``get_item()`` is defined in ``tc-chains-api-model.c`` and calls ``rtems_chain_get_unprotected()``. Substitute  ``3`` to produce:

.. code:: c

  nptr = get_item( &chain );
  T_eq_ptr( nptr, &memory[3] );

Testing Concurrent Managers
---------------------------

All the other models are of Managers that provide some form of communication
between multiple RTEMS Tasks. This introduces a number of issues regarding
the timing and control of tasks, particularly when developing *reproducible*
tests, where the sequencing of behavior is the same every time the test runs.
The tests are generated by following the schemes already in use for regular
RTEMS handwritten tests.
In particular the pre-existing tests for Send and Receive in the Event Manager
where used as a guide.

Testing Strategy
^^^^^^^^^^^^^^^^

The tests are organized as follows:

1. A designated Task, the Runner, is responsible for initializing,
   coordinating and tearing down a test run.
   Coordination involves starting other Worker Tasks that perform tests,
   and waiting for them to complete.
   It may also run some tests itself.

1. One or more Worker Tasks are used to perform test actions.

1. Each RTEMS Task (Runner/Worker) is modelled by one Promela process.

1. Simple Binary Semaphores
   are used to coordinate all the tasks to ensure
   that the interleaving is always the same
   (See Semaphore Manager section in Classic API Manual).

1. Two other Promela processes are required:
   One, called ``Clock()`` is used to model timing and timeouts;
   The other, called ``System()`` models relevant behavior of the RTEMS scheduler.

Model Structure
^^^^^^^^^^^^^^^

All the models developed so far are based on this framework.
The structure of these models takes the following form:

  Constant Declarations
     Mainly ``#define``\ s that define important constants.

  Datastructure Definitions
    Promela ``typedef``\ s that describe key forms of data.
    In particular there is a type ``Task`` that models RTEMS Tasks.
    The Simple Binary Semaphores are modelled as boolean variables.

  Global Variable Declarations
    Typically these are arrays of data-structures,
    representing objects such as tasks or semaphores.

  Supporting Models
    These are ``inline`` definitions that capture common behavior.
    In all models this includes ``Obtain()`` and ``Release()`` to model semaphores,
    and ``waitUntilReady()`` that models a blocked task waiting to be unblocked.
    Included here are other definitions specific to the particular Manager being
    modelled.

  API Models
    These are ``inline`` definitions that model the behavior of each API call.
    All behavior must be modelled, including bad calls that (should) result in
    an error code being returned.
    The parameter lists used in the Promela models will differ from those
    of the actual API calls.
    Consider a hypothetical RTEMS API call:

    .. code:: c

      rc = rtems_some_api(arg1,arg2,...,argN);

    One reason, common to all calls, is that the ``inline`` construct has
    no concept of returning a value,
    so a variable parameter has to be added to represent it,
    and it has to be ensured the appropriate return code is assigned to it.

    .. code:: promela

      inline some_api(arg1,arg2,...,argN,rc) {
        ...
        rc = RC_some_code
      }

    Another reason is that some RTEMS types encode a number of different
    concepts in a single machine word.
    The most notable of these is the ``rtems_options`` type,
    that specifies various options, usually for calls that may block.
    In some models, some options are modelled individually, for clarity.
    So the API model may have two or more parameters where the RTEMS call has one.

    .. code:: promela

      inline some_api(arg1,arg2feat1,arg2feat2,...,argN,rc) {
        ...
        rc = RC_some_code
      }

    The refinement of this will pass the multiple feature arguments to
    a C function that will assemble the single RTEMS argument.

    A third reason is that sometimes it is important to also provide
    the process id of the *calling* task. This can be important where
    priority and preemption are involved.

  Scenario Generation
    A Testsuite that exercises *all* the API code is highly desirable.
    This requires running tests that explore a wide range of scenarios,
    normally devised by hand when writing a testsuite.
    With Promela/SPIN, the model-checker can generate all of these simplify
    as a result of its exhaustive search of the model.
    In practice, scenarios fall into a number of high-level categories,
    so the first step is make a random choice of such a category.
    Within a category there may be further choices to be done.
    A collection of global scenario variables are used to records the choices made.
    This is all managed by inline ``chooseScenario()``.

  RTEMS Test Task Modelling
    This is a series of Promela ``proctype``\ s, one for the Runner Task,
    and one for each of the Worker Tasks.
    Their behavior is controlled by the global scenario variables.

  System Modelling
    These are Promela processes that model relevant underlying RTEMS behavior,
    such as the scheduler (``System()``) and timers (``Clock()``).

  Model Main Process
    Called ``init``, this initialises variables, invokes ``chooseScenario()``,
    runs all the processes, waits for them to terminate,
    and then terminates itself.

The Promela models developed so far for these Managers always terminate.
The last few lines of each are of the form:

.. code:: promela

  #ifdef TEST_GEN
    assert(false);
  #endif

If these models are run in the usual way (simulation or verification),
then a correct verified model is observed.
If ``-DTEST_GEN`` is provided as the first command-line argument,
in verification mode configured to find *all* counterexamples,
then all the possible (correct) behaviours of the system will be generated.

Transforming Model Behavior to C Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As described earlier, ``printf`` statements are used
to produce easy to parse output that makes
model events and outcomes easy to identify and process.
The YAML file used to define the refinement from model to code
provides a way of looking up an observation with arguments,
and then obtaining a C template that can be populated with those arguments.

This refinement is a bridge between two distinct worlds:

  Model World:
    where the key focus is on correctness and clarity.

  Code World:
    where clarity is often sacrificed for efficiency.

This means that the model-to-code relationship
need not be a simple one-to-one mapping.
This has already been alluded to above when the need for extra parameters
in API call models was discussed.
It can also be helpful when the model is better treating various attributes
separately, while the code handles those attributes packed into machine words.

It is always reasonable to add test support code to the C test sources,
and this can include C functions that map distinct attribute values
down into some compact merged representation.


Testing the Event Manager
-------------------------

Documentation:  Event Manager section in the RTEMS Classic API Guide.

Model Directory: ``formal/promela/models/events``.

Model Name: ``event-mgr-model``.

The Event Manager allows tasks to send events to,
and receive events from, other tasks.
From the perspective of the Event Manager,
events are just uninterpreted numbers in the range 0..31,
encoded as a 32-bit bitset.

``rtems_event_send(id,event_in)``
  allows a task to send a bitset to a designated task

``rtems_event_receive(event_in,option_set,ticks,event_out)``
  allows a task to specify a desired bitset
  with options on what to do if it is not present.

Most of the requirements are pretty straightforward,
but two were a little more complex,
and drove the more complex parts of the modelling.

1. If a task was blocked waiting to receive events,
   and a lower priority task then sent the events that would wake that
   blocked task,
   then the sending task would be immediately preempted by the receiver task.

2. There was a requirement that explicitly discussed the situation
   where the two tasks involved were running on different processors.

A preliminary incomplete model of the Event Manager was originally developed
by the consortium early in the project. The model was then completed during
the rest of the activity by a Masters student: :cite:`Jennings:2021:FV`.
They also developed the first iteration of the ``testbuilder`` program.

API Model
^^^^^^^^^

File: ``event-mgr-model.pml``

The RTEMS Event set contains 32 values, but in the model limits this to
just four, which is enough for test purposes.
Some inline definitions are provided to encode (``events``), display
(``printevents``), and subtract (``setminus``) events.

The ``rtems_option_set`` is simplifiedto just two relevant bits: the timeout
setting (``Wait``, ``NoWait``), and how much of the desired event set will
satisfy the receiver (``All``, ``Any``).
These are passed in as two separate arguments to the model of the receive call.

Event Send
~~~~~~~~~~

An RTEMS call ``rc = rtems_event_send(tid,evts)`` is modelled by an inline of
the form:

.. code-block:: c

   event_send(self,tid,evts,rc)

The four arguments are:
 | ``self`` : id of process modelling the task/IDR making call.
 | ``tid``  : id of process modelling the target task of the call.
 | ``evts`` : event set being sent.
 | ``rc``   : updated with the return code when the send completes.

The main complication in the otherwise straightforward model is the requirement
to preempt under certain circumstances.

.. code-block:: c

   inline event_send(self,tid,evts,rc) {
     atomic{
       if
       ::  tid >= BAD_ID -> rc = RC_InvId
       ::  tid < BAD_ID ->
           tasks[tid].pending = tasks[tid].pending | evts
           // at this point, have we woken the target task?
           unsigned got : NO_OF_EVENTS;
           bool sat;
           satisfied(tasks[tid],got,sat);
           if
           ::  sat ->
               tasks[tid].state = Ready;
               printf("@@@ %d STATE %d Ready\n",_pid,tid)
               preemptIfRequired(self,tid) ;
               // tasks[self].state may now be OtherWait !
               waitUntilReady(self);
           ::  else -> skip
           fi
           rc = RC_OK;
       fi
     }
   }

Three inline abstractions are used:

``satisfied(task,out,sat)``
    updates ``out`` with the wanted events received so far, and then checks if a receive has been satisfied. It
    updates its ``sat`` argument to reflect the check outcome.

``preemptIfRequired(self,tid)``
   forces the sending process to enter the ``OtherWait``,
   if circumstances require it.

``waitUntilReady(self)``
   basically waits for the process state to become ``Ready``.

Event Receive
~~~~~~~~~~~~~

An RTEMS call ``rc = rtems_event_receive(evts,opts,interval,out)`` is modelled
by an inline of
the form:

.. code-block:: c

   event_receive(self,evts,wait,wantall,interval,out,rc)

The seven arguments are:
 | ``self`` : id of process modelling the task making call
 | ``evts`` : input event set
 | ``wait`` : true if receive should wait
 | ``what`` : all, or some?
 | ``interval`` : wait interval (0 waits forever)
 | ``out`` : pointer to location for satisfying events when the receive
     completes.
 | ``rc`` : updated with the return code when the receive completes.


There is a small complication, in that there are distinct variables in the model
for receiver options that are combined into a single RTEMS option set. The
actual calling sequence in C test code will be:

.. code-block:: c

   opts = mergeopts(wait,wantall);
   rc = rtems_event_receive(evts,opts,interval,out);

Here ``mergeopts`` is a C function defined in the C Preamble.

.. code-block:: c

   inline event_receive(self,evts,wait,wantall,interval,out,rc){
     atomic{
       printf("@@@ %d LOG pending[%d] = ",_pid,self);
       printevents(tasks[self].pending); nl();
       tasks[self].wanted = evts;
       tasks[self].all = wantall
       if
       ::  out == 0 ->
           printf("@@@ %d LOG Receive NULL out.\n",_pid);
           rc = RC_InvAddr ;
       ::  evts == EVTS_PENDING ->
           printf("@@@ %d LOG Receive Pending.\n",_pid);
           recout[out] = tasks[self].pending;
           rc = RC_OK
       ::  else ->
           bool sat;
           retry:  satisfied(tasks[self],recout[out],sat);
           if
           ::  sat ->
               printf("@@@ %d LOG Receive Satisfied!\n",_pid);
               setminus(tasks[self].pending,tasks[self].pending,recout[out]);
               printf("@@@ %d LOG pending'[%d] = ",_pid,self);
               printevents(tasks[self].pending); nl();
               rc = RC_OK;
           ::  !sat && !wait ->
               printf("@@@ %d LOG Receive Not Satisfied (no wait)\n",_pid);
               rc = RC_Unsat;
           ::  !sat && wait && interval > 0 ->
               printf("@@@ %d LOG Receive Not Satisfied (timeout %d)\n",_pid,interval);
               tasks[self].ticks = interval;
               tasks[self].tout = false;
               tasks[self].state = TimeWait;
               printf("@@@ %d STATE %d TimeWait %d\n",_pid,self,interval)
               waitUntilReady(self);
               if
               ::  tasks[self].tout  ->  rc = RC_Timeout
               ::  else              ->  goto retry
               fi
           ::  else -> // !sat && wait && interval <= 0
               printf("@@@ %d LOG Receive Not Satisfied (wait).\n",_pid);
               tasks[self].state = EventWait;
               printf("@@@ %d STATE %d EventWait\n",_pid,self)
               if
               :: sendTwice && !sentFirst -> Released(sendSema);
               :: else
               fi
               waitUntilReady(self);
               goto retry
           fi
       fi
       printf("@@@ %d LOG pending'[%d] = ",_pid,self);
       printevents(tasks[self].pending); nl();
     }
   }

Here ``satisfied()`` and ``waitUntilReady()`` are also used.

Behaviour Patterns
^^^^^^^^^^^^^^^^^^

File: ``event-mgr-model.pml``

The Event Manager model consists of
five Promela processes:

``init``
    The first top-level Promela process that performs initialisation,
    starts the other processes, waits for them to terminate, and finishes.

``System``
    A Promela process that models the behaviour of the operating system,
    in particular that of the scheduler.

``Clock``
    A Promela process used to facilitate modelling timeouts.

``Receiver``
    The Promela process modelling the test Runner,
    that also invokes the receive API call.

``Sender``
    A Promela process modelling a singe test Worker
    that invokes the send API call.


Two simple binary semaphores are used to synchronise the tasks.

The Task model only looks at an abstracted version of RTEMS Task states:

``Zombie``
    used to model a task that has just terminated. It can only be deleted.

``Ready``
    same as the RTEMS notion of ``Ready``.

``EventWait``
    is ``Blocked`` inside a call of ``event_receive()`` with no timeout.

``TimeWait``
    is ``Blocked`` inside a call of ``event_receive()`` with a timeout.

``OtherWait``
    is ``Blocked`` for some other reason, which arises in this model when a
    sender gets pre-empted by a higher priority receiver it has just satisfied.


Tasks are represented using a datastructure array.
As array indices are proxies here for C pointers,
the zeroth array entry is always unused,
as index value 0 is used to model a NULL C pointer.

.. code-block:: c

   typedef Task {
     byte nodeid; // So we can spot remote calls
     byte pmlid; // Promela process id
     mtype state ; // {Ready,EventWait,TickWait,OtherWait}
     bool preemptable ;
     byte prio ; // lower number is higher priority
     int ticks; //
     bool tout; // true if woken by a timeout
     unsigned wanted  : NO_OF_EVENTS ; // EvtSet, those expected by receiver
     unsigned pending : NO_OF_EVENTS ; // EvtSet, those already received
     bool all; // Do we want All?
   };
   Task tasks[TASK_MAX]; // tasks[0] models a NULL dereference

.. code-block:: c

   byte sendrc;            // Sender global variable
   byte recrc;             // Receiver global variable
   byte recout[TASK_MAX] ; // models receive 'out' location.

Task Scheduling
~~~~~~~~~~~~~~~

In order to produce a model that captures real RTEMS Task behaviour,
there need to be mechanisms that mimic the behaviour of the scheduler and other
activities that can modify the execution state of these Tasks. Given a scenario
generated by such a model, synchronisation needs to be added to the generated C
code to ensure test has the same execution patterns.

Relevant scheduling behavior is modelled by two inlines that have already
been mentioned: ``waitUntilReady()`` and ``preemptIfRequired()``.

For synchronisation, simple boolean semaphores are used, where True means
available, and False means the semaphore has been acquired.

.. code-block:: c

   bool semaphore[SEMA_MAX]; // Semaphore

The synchronisation mechanisms are:


``Obtain(sem_id)``
   call that waits to obtain semaphore ``sem_id``.

``Release(sem_id)``
    call that releases semaphore ``sem_id``

``Released(sem_id)``
    simulates ecosystem behaviour that releases ``sem_id``.

The difference between ``Release`` and ``Released`` is that the first issues
a ``SIGNAL`` annotation, while the second does not.


Scenarios
~~~~~~~~~

A number of different scenario schemes were defined
that cover various aspects of
Event Manager behaviour. Some schemes involve only one task, and are usually
used to test error-handling or abnormal situations. Other schemes involve two
tasks, with some mixture of event sending and receiving, with varying task
priorities.

For example, an event send operation can involve a target identifier that
is invalid (``BAD_ID``), correctly identifies a receiver task (``RCV_ID``), or
is sending events to itself (``SEND_ID``).

.. code-block:: c

   typedef SendInputs {
     byte target_id ;
     unsigned send_evts : NO_OF_EVENTS ;
   } ;
   SendInputs  send_in[MAX_STEPS];

An event receive operation will be determined by values for desired events,
and the relevant to bits of the option-set parameter.

.. code-block:: c

   typedef ReceiveInputs {
     unsigned receive_evts : NO_OF_EVENTS ;
     bool will_wait;
     bool everything;
     byte wait_length;
   };
   ReceiveInputs receive_in[MAX_STEPS];

There is a range of global variables that define scenarios for both send and
receive. This defines a two-step process for choosing a scenario.
The first step is to select a scenario scheme. The possible schemes are
defined by the following ``mtype``:

.. code-block:: c

   mtype = {Send,Receive,SndRcv,RcvSnd,SndRcvSnd,SndPre,MultiCore};
   mtype scenario;

One of these is chosen by using a conditional where all alternatives are
executable, so behaving as a non-deterministic choice of one of them.

.. code-block:: c

   if
   ::  scenario = Send;
   ::  scenario = Receive;
   ::  scenario = SndRcv;
   ::  scenario = SndPre;
   ::  scenario = SndRcvSnd;
   ::  scenario = MultiCore;
   fi


Once the value of ``scenario`` is chosen, it is used in another conditional
to select a non-deterministic choice of the finer details of that scenario.

.. code-block:: c

    if
    ::  scenario == Send ->
          doReceive = false;
          sendTarget = BAD_ID;
    ::  scenario == Receive ->
          doSend = false
          if
          :: rcvWait = false
          :: rcvWait = true; rcvInterval = 4
          :: rcvOut = 0;
          fi
          printf( "@@@ %d LOG sub-senario wait:%d interval:%d, out:%d\n",
                  _pid, rcvWait, rcvInterval, rcvOut )
    ::  scenario == SndRcv ->
          if
          ::  sendEvents = 14; // {1,1,1,0}
          ::  sendEvents = 11; // {1,0,1,1}
          fi
          printf( "@@@ %d LOG sub-senario send-receive events:%d\n",
                  _pid, sendEvents )
    ::  scenario == SndPre ->
          sendPrio = 3;
          sendPreempt = true;
          startSema = rcvSema;
          printf( "@@@ %d LOG sub-senario send-preemptable events:%d\n",
                  _pid, sendEvents )
    ::  scenario == SndRcvSnd ->
          sendEvents1 = 2; // {0,0,1,0}
          sendEvents2 = 8; // {1,0,0,0}
          sendEvents = sendEvents1;
          sendTwice = true;
          printf( "@@@ %d LOG sub-senario send-receive-send events:%d\n",
                  _pid, sendEvents )
    ::  scenario == MultiCore ->
          multicore = true;
          sendCore = 1;
          printf( "@@@ %d LOG sub-senario multicore send-receive events:%d\n",
                  _pid, sendEvents )
    ::  else // go with defaults
    fi

Ddefault values are defined for all the global scenario variables so that the
above code focusses on what differs. The default scenario is a receiver waiting
for a sender of the same priority which sends exactly what was requested.

Sender Process (Worker Task)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sender process then uses the scenario configuration to determine its
behaviour. A key feature is the way it acquires its semaphore before doing a
send, and releases the receiver semaphore when it has just finished sending.
Both these semaphores are initialised in the unavailable state.

.. code-block:: c

   proctype Sender (byte nid, taskid) {

     tasks[taskid].nodeid = nid;
     tasks[taskid].pmlid = _pid;
     tasks[taskid].prio = sendPrio;
     tasks[taskid].preemptable = sendPreempt;
     tasks[taskid].state = Ready;
     printf("@@@ %d TASK Worker\n",_pid);
     if
     :: multicore ->
          // printf("@@@ %d CALL OtherScheduler %d\n", _pid, sendCore);
          printf("@@@ %d CALL SetProcessor %d\n", _pid, sendCore);
     :: else
     fi
     if
     :: sendPrio > rcvPrio -> printf("@@@ %d CALL LowerPriority\n", _pid);
     :: sendPrio == rcvPrio -> printf("@@@ %d CALL EqualPriority\n", _pid);
     :: sendPrio < rcvPrio -> printf("@@@ %d CALL HigherPriority\n", _pid);
     :: else
     fi
   repeat:
     Obtain(sendSema);
     if
     :: doSend ->
       if
       :: !sentFirst -> printf("@@@ %d CALL StartLog\n",_pid);
       :: else
       fi
       printf("@@@ %d CALL event_send %d %d %d sendrc\n",_pid,taskid,sendTarget,sendEvents);
       if
       :: sendPreempt && !sentFirst -> printf("@@@ %d CALL CheckPreemption\n",_pid);
       :: !sendPreempt && !sentFirst -> printf("@@@ %d CALL CheckNoPreemption\n",_pid);
       :: else
       fi
       event_send(taskid,sendTarget,sendEvents,sendrc);
       printf("@@@ %d SCALAR sendrc %d\n",_pid,sendrc);
     :: else
     fi
     Release(rcvSema);
     if
     :: sendTwice && !sentFirst ->
        sentFirst = true;
        sendEvents = sendEvents2;
        goto repeat;
     :: else
     fi
     printf("@@@ %d LOG Sender %d finished\n",_pid,taskid);
     tasks[taskid].state = Zombie;
     printf("@@@ %d STATE %d Zombie\n",_pid,taskid)
   }

Receiver Process (Runner Task)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The receiver process uses the scenario configuration to determine its
behaviour. It has the responsibility to trigger the start semaphore to allow
either itself or the sender to start. The start semaphore corresponds to either
the send or receive semaphore, depending on the scenario. The receiver acquires
the receive semaphore before proceeding, and releases the send sempahore when
done.

.. code-block:: c

   proctype Receiver (byte nid, taskid) {

     tasks[taskid].nodeid = nid;
     tasks[taskid].pmlid = _pid;
     tasks[taskid].prio = rcvPrio;
     tasks[taskid].preemptable = false;
     tasks[taskid].state = Ready;
     printf("@@@ %d TASK Runner\n",_pid,taskid);
     if
     :: multicore ->
          printf("@@@ %d CALL SetProcessor %d\n", _pid, rcvCore);
     :: else
     fi
     Release(startSema); // make sure stuff starts */
     /* printf("@@@ %d LOG Receiver Task %d running on Node %d\n",_pid,taskid,nid); */
     Obtain(rcvSema);

     // If the receiver is higher priority then it will be running
     // The sender is either blocked waiting for its semaphore
     // or because it is lower priority.
     // A high priority receiver needs to release the sender now, before it
     // gets blocked on its own event receive.
     if
     :: rcvPrio < sendPrio -> Release(sendSema);  // Release send semaphore for preemption
     :: else
     fi
     if
     :: doReceive ->
       printf("@@@ %d SCALAR pending %d %d\n",_pid,taskid,tasks[taskid].pending);
       if
       :: sendTwice && !sentFirst -> Release(sendSema)
       :: else
       fi
       printf("@@@ %d CALL event_receive %d %d %d %d %d recrc\n",
              _pid,rcvEvents,rcvWait,rcvAll,rcvInterval,rcvOut);
                 /* (self,  evts,     when,   what,  ticks,      out,   rc) */
       event_receive(taskid,rcvEvents,rcvWait,rcvAll,rcvInterval,rcvOut,recrc);
       printf("@@@ %d SCALAR recrc %d\n",_pid,recrc);
       if
       :: rcvOut > 0 ->
         printf("@@@ %d SCALAR recout %d %d\n",_pid,rcvOut,recout[rcvOut]);
       :: else
       fi
       printf("@@@ %d SCALAR pending %d %d\n",_pid,taskid,tasks[taskid].pending);
     :: else
     fi
     Release(sendSema);
     printf("@@@ %d LOG Receiver %d finished\n",_pid,taskid);
     tasks[taskid].state = Zombie;
     printf("@@@ %d STATE %d Zombie\n",_pid,taskid)
   }

System Process
~~~~~~~~~~~~~~

 A process is needed that periodically wakes up blocked processes.
 This is modelling background behaviour of the system,
 such as ISRs and scheduling.
 All tasks are visited in round-robin order (to prevent starvation)
 and are made ready if waiting on other things. Tasks waiting for events or timeouts are not touched. This terminates when all tasks are zombies.

.. code-block:: c

   proctype System () {
     byte taskid ;
     bool liveSeen;
     printf("@@@ %d LOG System running...\n",_pid);
     loop:
     taskid = 1;
     liveSeen = false;
     printf("@@@ %d LOG Loop through tasks...\n",_pid);
     atomic {
       printf("@@@ %d LOG Scenario is ",_pid);
       printm(scenario); nl();
     }
     do   // while taskid < TASK_MAX ....
     ::  taskid == TASK_MAX -> break;
     ::  else ->
         atomic {
           printf("@@@ %d LOG Task %d state is ",_pid,taskid);
           printm(tasks[taskid].state); nl()
         }
         if
         :: tasks[taskid].state == Zombie -> taskid++
         :: else ->
            if
            ::  tasks[taskid].state == OtherWait
                -> tasks[taskid].state = Ready
                   printf("@@@ %d STATE %d Ready\n",_pid,taskid)
            ::  else -> skip
            fi
            liveSeen = true;
            taskid++
         fi
     od
     printf("@@@ %d LOG ...all visited, live:%d\n",_pid,liveSeen);
     if
     ::  liveSeen -> goto loop
     ::  else
     fi
     printf("@@@ %d LOG All are Zombies, game over.\n",_pid);
     stopclock = true;
   }

Clock Process
~~~~~~~~~~~~~

A process is needed that handles a clock tick,
by decrementing the tick count for tasks waiting on a timeout.
Such a task whose ticks become zero is then made ``Ready``,
and its timer status is flagged as a timeout. This terminates when all
tasks are zombies (as signalled by ``System()`` via ``stopclock``).

.. code-block:: c

   proctype Clock () {
     int tid, tix;
     printf("@@@ %d LOG Clock Started\n",_pid)
     do
     ::  stopclock  -> goto stopped
     ::  !stopclock ->
         printf(" (tick) \n");
         tid = 1;
         do
         ::  tid == TASK_MAX -> break
         ::  else ->
             atomic{
               printf("Clock: tid=%d, state=",tid);
               printm(tasks[tid].state); nl()
             };
             if
             ::  tasks[tid].state == TimeWait ->
                 tix = tasks[tid].ticks - 1;
                 if
                 ::  tix == 0
                     tasks[tid].tout = true
                     tasks[tid].state = Ready
                     printf("@@@ %d STATE %d Ready\n",_pid,tid)
                 ::  else
                     tasks[tid].ticks = tix
                 fi
             ::  else // state != TimeWait
             fi
             tid = tid + 1
         od
     od
   stopped:
     printf("@@@ %d LOG Clock Stopped\n",_pid);
   }


init Process
~~~~~~~~~~~~

The initial process outputs annotations for defines and declarations,
generates a scenario non-deterministically and then starts the system, clock
and send and receive processes running. It then waits for those to complete,
and them, if test generation is underway, asserts ``false`` to trigger a
seach for counterexamples:

.. code-block:: c

   init {
     pid nr;
     printf("@@@ %d NAME Event_Manager_TestGen\n",_pid)
     outputDefines();
     outputDeclarations();
     printf("@@@ %d INIT\n",_pid);
     chooseScenario();
     run System();
     run Clock();
     run Sender(THIS_NODE,SEND_ID);
     run Receiver(THIS_NODE,RCV_ID);
     _nr_pr == 1;
   #ifdef TEST_GEN
     assert(false);
   #endif
   }

The information regarding when tasks should wait and/or restart
can be obtained by tracking the process identifiers,
and noting when they change.
The ``spin2test`` program does this,
and also produces separate test code segments for each Promela process.

Annotations
^^^^^^^^^^^

File: ``event-mgr-model.pml``

Nothing more to say here.

Refinement
^^^^^^^^^^

File: ``event-mgr-model-rfn.yml``


The test-code generated here is based on the test-code generated from the
specification items used to describe the Event Manager in the main (non-formal)
part of the new qualification material.

The relevant specification item is ``spec/rtems/event/req/send-receive.yml``
found in ``rtems-central``. The corresponding C test code is
``tr-event-send-receive.c`` found in ``rtems`` at ``testsuites/validation``.
That automatically generated C code is a single file that uses a set of deeply
nested loops to iterate through the scenarios it generates.

The approach here is to generate a stand-alone C code file for each scenario
(``tr-event-mgr-model-N.c`` for ``N`` in range 0..8.)


The ``TASK`` annotations issued by the ``Sender`` and ``Receiver`` processes
lookup the following refinement entries, to get code that tests that the C
code Task does correspond to what is being defined in the model.

.. code-block:: yaml

   Runner: |
     checkTaskIs( ctx->runner_id );

   Worker: |
     checkTaskIs( ctx->worker_id );

The ``WAIT`` and ``SIGNAL`` annotations produced by ``Obtain()`` and
``Release()`` respectively, are mapped to the corresponding operations on
RTEMS semaphores in the test code.

.. code-block:: yaml

   code content
   SIGNAL: |
     Wakeup( semaphore[{}] );

   WAIT: |
     Wait( semaphore[{}] );

Some of the ``CALL`` annotations are used to do more complex test setup
involving priorities, or other processors and schedulers. For example:

.. code-block:: yaml

   HigherPriority: |
     SetSelfPriority( PRIO_HIGH );
     rtems_task_priority prio;
     rtems_status_code sc;
     sc = rtems_task_set_priority( RTEMS_SELF, RTEMS_CURRENT_PRIORITY, &prio );
     T_rsc_success( sc );
     T_eq_u32( prio, PRIO_HIGH );

   SetProcessor: |
     T_ge_u32( rtems_scheduler_get_processor_maximum(), 2 );
     uint32_t processor = {};
     cpu_set_t cpuset;
     CPU_ZERO(&cpuset);
     CPU_SET(processor, &cpuset);

Some handle more complicated test outcomes, such as observing context-switches:

.. code-block:: yaml

   CheckPreemption: |
     log = &ctx->thread_switch_log;
     T_eq_sz( log->header.recorded, 2 );
     T_eq_u32( log->events[ 0 ].heir, ctx->runner_id );
     T_eq_u32( log->events[ 1 ].heir, ctx->worker_id );

Most of the other refinement entries are similar to those described above for
the Chains API.

Testing the Barrier Mananger
----------------------------

Documentation:  Barrier Manager section in the RTEMS Classic API Guide.

Model Directory: ``formal/promela/models/barriers``.

Model Name: ``barrier-mgr-model``.

The Barrier Manager is used to arrange for a number of tasks to wait on a
designated barrier object, until either another task releases them, or a
given number of tasks are waiting, at which point they are all released.

All five directives were modelled:

* ``rtems_barrier_create()``

* ``rtems_barrier_ident()``

* ``rtems_barrier_delete()``

* ``rtems_barrier_wait()``

* ``rtems_barrier_release()``

Barriers can be manual (released only by a call to ``..release()``),
or automatic (released by the call to ``..wait()`` that results in a wait count limit being reached.)
There is no notion of queuing in this manager,
only waiting for a barrier to be released.

This model was developed by a Masters student :cite:`Jaskuc:2022:TESTGEN`,
using the Event Manager as a model. It was added into the QDP produced by
the follow-on IV&V activity.

API Model
^^^^^^^^^

File: ``barrier-mgr-model.pml``

Modelling waiting is much easier than modelling queueing.
All that is required is an array of booleans (``waiters``), indexed by process id:

.. code:: promela

  typedef Barrier {
    byte b_name; // barrier name
    bool isAutomatic; // true for automatic, false for manual barrier
    int maxWaiters; // maximum count of waiters for automatic barrier
    int waiterCount; // current amount of tasks waiting on the barrier
    bool waiters[TASK_MAX]; // waiters on the barrier
    bool isInitialised; // indicated whenever this barrier was created
  }

The name ``satisfied`` is currently used here for an inline that checks when
a barrier can be released.
Other helper inlines include ``waitAtBarrier()`` and ``barrierRelease()``.

Behaviour Patterns
^^^^^^^^^^^^^^^^^^

File: ``barrier-mgr-model.pml``

The overall architecture in terms of Promela processes has processes ``init``, ``System``, ``Clock``, ``Runner``,
and two workers: ``Worker1`` and ``Worker2``.
The runner and workers each may perform one or more API calls,
in the following order: create, ident, wait, release, delete.
Scenarios mix and match which task does what.

There are three top-level scenarios:

.. code:: promela

  mtype = {ManAcqRel,AutoAcq,AutoToutDel};

In scenario ``ManAcqRel``, the runner will do create, release and delete,
with sub-scenarios to check error cases as well as good behaviour,
for manual barriers.
Good behaviour involves one or more workers doing a wait.
The ``AutoAcq`` and ``AutoToutDel``
scenarios look at good and bad uses of automatic barriers.

Annotations
^^^^^^^^^^^

File: ``barrier-mgr-model.pml``

Similiar to those used in the Event Manager.

Refinement
^^^^^^^^^^

File: ``barrier-mgr-model-rfn.yml``

Similiar to those used in the Event Manager.

Testing the Message Manager
---------------------------

Documentation:  Message Manager section in the RTEMS Classic API Guide.

Model Directory: ``formal/promela/models/messages``.

Model Name: ``msg-mgr-model``.

The Message Manager provides objects that act as message queues. Tasks can
interact with these by enqueuing and/or dequeuing message objects.

There are 11 directives in total, but only the following were modelled:

  * ``rtems_message_queue_create()``

  * ``rtems_message_queue_send()``

  * ``rtems_message_queue_receive()``

The manager supports two queuing protocols, FIFO and priority-based.
Only the FIFO queueing was modelled.

This model was developed by a Masters student :cite:`Lynch:2022:TESTGEN`,
using the Event Manager as a model. It was added into the QDP produced by
the follow-on IV&V activity.

Below we focus on aspects of this model that differ from the Event Manager.

API Model
^^^^^^^^^

File: ``msg-mgr-model.pml``

A key feature of this manager is that not only are messages in a queue,
but so are the tasks waiting for those messages.
Both task and message queues are modelled as circular buffers,
with inline definitions of enqueuing and dequeuing operations.

While the Message Manager allows many queues to be created,
the model only uses one.


Behaviour Patterns
^^^^^^^^^^^^^^^^^^

File: ``msg-mgr-model.pml``

The overall architecture in terms of Promela processes has processes ``init``, ``System``, ``Clock``, ``Sender``, and two receivers:
``Receiver1`` and ``Receiver2``.
The ``Sender`` is the test runner, which performs the queue creation,
releases the start semaphore and then performs a send operation if needed.
The receivers are worker processes.

There are four top level scenarios:

.. code:: promela

  mtype = {Send,Receive,SndRcv, RcvSnd};

Scenarios ``Send`` and ``Receive`` are used for testing erroneous calls.
The ``SndRcv`` scenario fills up queues before the receivers run,
while the ``RcvSnd`` has the receivers waiting before messages are sent.

Annotations
^^^^^^^^^^^

File: ``msg-mgr-model.pml``

Similiar to those used in the Event Manager.

Refinement
^^^^^^^^^^

File: ``msg-mgr-model-rfn.yml``

Similiar to those used in the Event Manager.

Current State of Play
---------------------

The models developed here are the result of
an ad-hoc incremental development process
and have a lot of overlapping material.

Model State
^^^^^^^^^^^

The models were developed by first focusing on simple behavior
such as error handling, and then adding in simpler behaviors,
until sufficient coverage was acheived.
The basic philosophy at the time was not to fix anything not broken.

This has led to the models being somewhat over-engineered,
particularly when it comes to scenario generation.
There is some conditional looping behaviour,
implemented using labels and ``goto``,
that should really be linearised, using conditionals to skip parts.
It is harder than it should be to understand what each scenario does.

Also the API call models have perhaps a bit too much code devoted
to system behaviour.

Model Refactoring
^^^^^^^^^^^^^^^^^

There is a case to be made to perform some model refactoring.
Some of this would address the model state issues above.
Other refactoring would extract the common model material out,
to be put into files that could be included.
This includes the binary semaphore models,
and the parts modelling preemption and waiting while blocked.


Test Code Refactoring
^^^^^^^^^^^^^^^^^^^^^

During the qualification activity,
a new file ``tx-support.c`` was added to the RTEMS validation testsuite codebase.
This gathers C test support functions used by most of the tests.
The contents of the ``tr-<modelname>.h`` and ``tr-<modelname>.c``
files in particular should be brought in line with ``tx-support.c``.

Suitable Promela models should also be produced
of relevant functions in ``tx-support.c``.



