.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

Appendix: RTEMS Formal Model Guide
**********************************

Here we describe the various formal models of RTEMS that are currently in
existence. The following were delivered as part of the ESA-sponsored activity,
and will be included as the initial set when the directory ``formal`` is added
to ``rtems-central``:

Chains API (ESA-sponsored Activity)
    Models the unprotected chain append and get API calls in the Classic
    Chains API Guide. This was an early model to develop the basic methodology.

Events Manager (ESA-sponsored Activity, M.Sc. Dissertation :cite:`Jennings:2021:FV` )
    Models the behaviour of all the API calls in the Classic Events Manager API
    Guide. This had to tackle real concurrency and deal with multiple CPUs and priority
    issues.

Thread-Queues (ESA-sponsored Activity)
    Models related to the SMP versions of the scheduler thread queues. These are
    a work in progress and no test generation is currently available.

A number of other Classic RTEMS Managers have been modelled and have had tests
generated, as M.Sc. Dissertation topics. This need some final validation and
will be added later. They will be used to assess the proposed mechanism for
upgrade and maintenance (:numref:`FormalMaint`):


Barrier Manager (M.Sc. Dissertation :cite:`Jaskuc:2022:TESTGEN` )
    Models the Classic Barrier Manager API.

Message Manager (M.Sc. Dissertation :cite:`Lynch:2022:TESTGEN` )
    Models the Classic Message Manager API.

.. _TestGenOverview:

Test Generation Overview
------------------------

Given an RTEMS feature we want to test, we first define a rootname
``feature-model`` that identifies the feature, and indicates that we are basing
our tests on a model.

We develop a Promela model of the feature as file ``feature-model.pml``. We
ensure this model captures the correct behaviour and verify it correctness.
We also add annotation ``printf()`` statements and a way to negate the
relevant properties.

We then use SPIN to generate the test scenarios and replay them so we have the
annotation output available. This results in a number of text files named
``feature-model-N.spn`` , where ``N`` ranges from 0 upwards.

For each value of ``N`` we use a refinement mapping defined in
``feature-model-rfn.yml`` to generate segments of C test code, one for each
Promela process. We then generate the corresponding test code in file
``tr-feature-model-N.c`` by concatenating the following pieces:

1. ``feature-model-pre.h``  (The Preamble)
2. The segments of C test code produced by the refinement mapping
3. ``feature-model-post.h``  (The Postamble)
4. The contents of ``feature-model-run.h`` (The Runner) where the value of
   ``N`` has been substituted in at key locations.

The Runner defines a test case for this scenario. It is a file that contains
substitution markers for use with Pythons ``format()`` substitution,
and whose contents will generally look like this:

.. code-block:: c

   void RtemsFeatureModel_Run{0}()
   {{
     Context ctx;
     memset( &ctx, 0, sizeof( ctx ) );
     T_set_verbosity( T_NORMAL );
     TestSegment0( &ctx );
   }}
   T_TEST_CASE( RtemsFeatureModel{0} )
   {{
     RtemsFeatureModel_Run{0}( );
   }}

All the ``{0}`` above will be replaced by ``N``, and the double braces by
single ones, so for ``N`` equal to 42 (say), we get:

.. code-block:: c

   void RtemsFeatureModel_Run42()
   {{
     Context ctx;
     memset( &ctx, 0, sizeof( ctx ) );
     T_set_verbosity( T_NORMAL );
     TestSegment0( &ctx );
   }}
   T_TEST_CASE( RtemsFeatureModel42 )
   {{
     RtemsFeatureModel_Run42( );
   }}

All the generated ``tr-feature-model-N.c`` sources are copied to the location
for the testsuite sources.  Also so copied are the following files:
``tr-feature-model.h``, ``tr-feature-model.c``, and ``tc-feature-model.c``
(if present). The latter file is not required for simple test setups like the
Chains API, but is needed for more complex cases like the Event Manager.

Testing Chains
--------------

The Chains API provides a doubly-linked list data-structure, optimised for fast
operations in an SMP setting. We used it a proof of concept exercise.

See https://docs.rtems.org/branches/master/c-user/chains.html

Model Directory: ``formal/promela/models/chains``

Model
^^^^^

File: ``chains-api-model.pml``

We focussed on just two API calls: ``rtems-chain-append-unprotected``
and ``rtems-chain-get-unprotected`` (hereinafter just ``append`` and ``get``).

The model produced is one in which we have 6 processes, 3 of which perform a
single ``append``, and 3 of which do a single ``get`` when the chain is not
empty. All processes terminate after they have performed their action.
We initialize an empty chain and then run all six processes concurrently,
and at the end, we assert that the chain is empty. We use the special
``_nr_pr`` variable to ensure we wait for all six processes to terminate
before checking the final condition.
SPIN uses the C pre-processor, and the model-checker code can accept
Environment Variables, so we use ``TEST_GEN`` as a way to distinguish normal
model-checker operation from the test generation mode. For test generation,
SPIN is invoked at the command-line with ``-DTEST_GEN``.

.. code:: c

  init {
    pid nr;
    atomic{ chain.head = 0; chain.tail = 0; chain.size = 0 } ;
    nr = _nr_pr;
    run doAppend(6,21);
    run doAppend(3,22);
    run doAppend(4,23);
    run doNonNullGet();
    run doNonNullGet();
    run doNonNullGet();
    nr == _nr_pr;
  #ifdef TEST_GEN
    assert (chain.size != 0);
  #else
    assert (chain.size == 0);
  #endif
  }

As Promela does not have pointers, we re-coded the append algorithm using arrays
with pointers being array indices. We treat array index 0 as the equivalent of a
NULL pointer, so the first array element is never used.

.. code:: c

  typedef Node { unsigned nxt : PTR_SIZE; unsigned prv : PTR_SIZE; byte itm}
  Node memory[MEM_SIZE] ;
  typedef Control {
    unsigned head : PTR_SIZE; unsigned tail : PTR_SIZE; unsigned size : PTR_SIZE
  }
  Control chain ;

The chains implementation is a doubly-linked list of nodes that
are accessed from a special control structure, using some subtle union
overlays to ensure that node access can be done uniformly
(no NULL pointer in any node).
We abstract considerably from these details for now.
In particular,
we added an explicit ``size`` component
to the Promela *model* we are developing,
to allow us to easily write properties about chain length,
and to prevent array out-of-bound errors in the model itself.

Here is our model array version of the ``append`` code. We check that the
node-pointer ``np`` is not null, and that we have space for the entry being
added.

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

We then create a Promela process `doAppend` that puts the new chain value into
the addressed node and then calls ``append``, and terminates. We make it all
atomic because we don't want the chain operations to interleave internally. Such
extra interleaving is unnecessary and would only make the model larger and
produce more redundant tests.

.. code:: c

  proctype doAppend(int addr; int val) {
    atomic{ memory[addr].itm = val; append(chain,addr); } ;
  }

We implement the ``get`` operation similarly. The ``doNonNullGet`` process
waits for the chain to be non-empty before attempting to extract an element.

Annotations
^^^^^^^^^^^

However, this pure model of ``append`` and ``get`` is not, of itself, useful
for test generation. We need to add in ``printf()`` statements to generate
annotations. We do this for ``append`` by adding in two statements to the
``doAppend`` process

.. code:: c

   proctype doAppend(int addr; int val) {
     atomic{ memory[addr].itm = val; append(chain,addr);
             printf("@@@ 0 CALL append %d %d\n",val,addr); show_chain(); } ;
   }

The ``printf`` statement output indicates a call (``CALL``) to the
``append`` API with the actual values supplied for parameters ``addr`` and
``val``. The statement ``show_chain()`` is an inline function that prints the
contents of the chain after append returns.
The resulting output is multi-line,
starting with ``@@@ 0 SEQ chain``,
ending with ``@@@ 0 END chain``,
and with entries in between of the form ``@@@ 0 SCALAR _ val``
displaying chain elements, line by line.

We need more than just API calls annotated in this way.
We also have to provide annotations for various declarations.
These have to appear in the Promela main program (called ``init``)
as they have to be printed out as the model starts to run.
The atomic initialiser becomes somewhat larger:

.. code:: c

      atomic{
        printf("\n\n Chain Model running.\n");
        printf("@@@ 0 NAME Chain_AutoGen\n")
        printf("@@@ 0 DEF MAX_SIZE 8\n");
        printf("@@@ 0 DCLARRAY Node memory MAX_SIZE\n");
        printf("@@@ 0 DECL unsigned nptr NULL\n")
        printf("@@@ 0 DECL Control chain\n");

        printf("\nInitialising...\n")
        printf("@@@INIT\n");
        chain.head = 0; chain.tail = 0; chain.size = 0;
        show_chain();
      } ;

The problem is that a ``#define``, or a type or variable declaration,
is a compile-time feature of the Promela language,
so it won't output useful information at runtime.
Here we are adding ``printf`` statements to the ``init`` block
in Promela model to output this information.

Note that we show the initialised (empty) chain at the end.

We can now run the Promela model using SPIN in verification mode,
to generate a counter-example.
This is done in two steps:
the first writes the counter-example to a trail file;
while the second replays this trail file to run the counter-example.
We can get SPIN to find all possible counterexamples at once with this model.
This generates 21 scenarios.

Part of one possible result of running SPIN to get counter-example output
is shown below, from ``chains-api-model-8.spn`` . When we filter it to keep just
the lines starting with ``@@@`` we get:

.. code:: none

    @@@ 0 NAME Chain_AutoGen
    @@@ 0 DEF MAX_SIZE 8
    @@@ 0 DCLARRAY Node memory MAX_SIZE
    @@@ 0 DECL unsigned nptr NULL
    @@@ 0 DECL Control chain
    @@@ 0 INIT
    @@@ 0 SEQ chain
    @@@ 0 END chain
    @@@ 0 PTR nptr 0
    @@@ 0 CALL append 22 3
    @@@ 0 SEQ chain
    @@@ 0 SCALAR _ 22
    @@@ 0 END chain
    ...

Refinement
^^^^^^^^^^

Files:
 | ``chains-api-model-N.spn`` where ``N`` ranges from 0 to 20.
 | ``chains-api-model-rfn.yml``

The ``spin2test`` script takes these annotations, along with the YAML
refinement file defined for the model, and proceeds to generate testcode. All
of these annotations have the same ``<pid>``, namely 0, so one test segment of
code is produced. We show some examples of how this works below.

Given ``@@@ 0 NAME Chain_AutoGen`` we lookup `NAME` in the refinement file,
and get the following (which ignores the ``<name>`` parameter in this case):

.. code-block:: c

     const char rtems_test_name[] = "Model_Chain_API";

For ``@@@ 0 DEF MAX_SIZE 8`` we directly output

.. code-block:: c

   #define MAX_SIZE 8

For ``@@@ 0 DCLARRAY Node memory MAX_SIZE`` we lookup ``memory_DCL`` and get
``item {0}[{1}];``. We substitute ``memory`` and ``MAX_SIZE`` to get

.. code-block:: c

   item memory[MAX_SIZE];

For ``INIT`` we lookup ``INIT`` to get

.. code-block:: c

   rtems_chain_initialize_empty( &chain );

The first ``SEQ`` ... ``END`` pair is intended to display the initial chain,
which should be empty. The second shows the result of an ``append`` with one
value in the chain. In both cases, the name ``chain`` is recorded, and for
each ``SCALAR _ val``, the value of ``val`` is printed to a string with a
leading space. When ``@@@ 0 END chain`` is encountered we lookup ``chain_SEQ``
to obtain:

.. code-block:: c

     show_chain( &chain, ctx->buffer );
     T_eq_str( ctx->buffer, "{0} 0" );

Function ``show_chain`` is defined in the preamble C file used in test
generation and is designed to display the chain contents in a string that
matches the one generated here by the processing of ``SEQ`` ... ``SCALAR`` ...
``END``. We substitute the accumulated string in for ``{0}``, which will be
either empty, or just " 23". In the latter case we get the following code:

.. code-block:: c

     show_chain( &chain, ctx->buffer );
     T_eq_str( ctx->buffer, "23 0" );


For ``@@@ 0 CALL append 22 3`` we lookup ``append`` to get

.. code-block:: c

     memory[{1}].val = {0};
     rtems_chain_append_unprotected( &chain, (rtems_chain_node*)&memory[{1}] );

We substitute ``22`` and ``3`` in to get

.. code-block:: c

     memory[3].val = 22;
     rtems_chain_append_unprotected( &chain, (rtems_chain_node*)&memory[3] );


The following is the corresponding excerpt from the generated test-segment:

.. code-block:: c

  // @@@ 0 NAME Chain_AutoGen
  // @@@ 0 DEF MAX_SIZE 8
  #define MAX_SIZE 8
  // @@@ 0 DCLARRAY Node memory MAX_SIZE
  static item memory[MAX_SIZE];
  // @@@ 0 DECL unsigned nptr NULL
  static item * nptr = NULL;
  // @@@ 0 DECL Control chain
  static rtems_chain_control chain;

  //  ===== TEST CODE SEGMENT 0 =====

  static void TestSegment0( Context* ctx ) {
    const char rtems_test_name[] = "Model_Chain_API";

    T_log(T_NORMAL,"@@@ 0 INIT");
    rtems_chain_initialize_empty( &chain );
    T_log(T_NORMAL,"@@@ 0 SEQ chain");
    T_log(T_NORMAL,"@@@ 0 END chain");
    show_chain( &chain, ctx->buffer );
    T_eq_str( ctx->buffer, " 0" );

    T_log(T_NORMAL,"@@@ 0 PTR nptr 0");
    T_eq_ptr( nptr, NULL );
    T_log(T_NORMAL,"@@@ 0 CALL append 22 3");
    memory[3].val = 22;
    rtems_chain_append_unprotected( &chain, (rtems_chain_node*)&memory[3] );

    T_log(T_NORMAL,"@@@ 0 SEQ chain");
    T_log(T_NORMAL,"@@@ 0 SCALAR _ 22");
    T_log(T_NORMAL,"@@@ 0 END chain");
    show_chain( &chain, ctx->buffer );
    T_eq_str( ctx->buffer, " 22 0" );
    ...
  }

Note the extensive use of ``T_log()``, and emitted comments showing the
annotations when producing declarations. These help when debugging models,
refinement files, and the resulting test code. There are plans to provide a
mechanism that can be used to control the level of verbosity involved.


Assembly
^^^^^^^^

Files:
 | ``chains-api-model-pre.h`` (Preamble)
 | ``chains-api-model-post.h`` (Postamble)
 | ``chains-api-model-run.h`` (Runner)

The ``spin2test`` script then generates the required C test code from the
test segment generated using the refinement file, and the above-mentioned files,
as described in the :ref:`TestGenOverview` sub-section. For the Chain model,
the Preamble #includes ``<rtems.h>``, ``<rtems/test.h>``, ``<rtems/chain.h>``,
and ``tr-chains-api-model.h``. The Postamble is empty.

Deployment
^^^^^^^^^^

Files:
 | ``tr-chains-api-model.h``
 | ``tr-chains-api-model.c``
 | ``tr-chains-api-model-N.c`` where ``N`` ranges from zero upwards.

All the above files are copied to ``testsuites/validation`` in the ``rtems``
repository, where they should be built and run using ``waf`` as normal.

Testing Events
--------------

The Event Manager is a central piece of code in RTEMS SMP, being at the basis
of task communication and synchronization. It is used for instance in the
implementation of semaphores or various essential high-level data-structures,
and used in the Scheduling process. At the same time, its implementation is
making use of concurrent features of C11, and contains many unprotected
interactions with the Threads API. Having a Promela model faithfully modelling
the Event Manager code of RTEMS represent thus a real challenge, especially
with respect to formal testing. This application constitutes as well a way to
measure the completeness of our manual and automatic test generation tools
previously developed.

he RTEMS Event Manager was chosen as the second case-study because
it involved concurrency and communication, had a small number of API calls
(just two),
but also had somewhat complex requirements related to task priorities.

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


Annotated Model
^^^^^^^^^^^^^^^

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

``Sender``
    A Promela process used to model the RTEMS sender task.

``Receiver``
    A Promela process used to model the RTEMS receiver task.

Model State
~~~~~~~~~~~

The RTEMS Event set contains 32 values, but in our model we limit ourselves to
just four, which is enough for test purposes. We envisage two RTEMS tasks
involved, at most. We use two simple binary semaphores to synchronise the tasks.
We provide some inline definitions to encode (``events``), display
(``printevents``), and subtract (``setminus``) events.

Our Task model only looks at an abstracted version of RTEMS Task states:

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

We simplify the ``rtems_option_set`` to just two relevant bits: the timeout
setting (``Wait``, ``NoWait``), and how much of the desired event set will
satisfy the receiver (``All``, ``Any``).

We represent tasks using a datastructure array. As array indices are proxies
here for C pointers, the zeroth array entry is always unused, as we use index
value 0 to model a NULL C pointer.

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

There is no notion of returning values from Promela ``proctype`` or ``inline``
constructs, so we need to have global variables to model return values. Also,
C pointers used to designate where to return a result need to be modelled
by indices into global array variables.

.. code-block:: c

   byte sendrc;            // Sender global variable
   byte recrc;             // Receiver global variable
   byte recout[TASK_MAX] ; // models receive 'out' location.

Task Scheduling
~~~~~~~~~~~~~~~

In order to produce a model that captures real RTEMS Task behaviour, we need
to have mechanisms that mimic the behaviour of the scheduler and other
activities that can modify the execution state of these Tasks. Given a scenario
generated by such a model, we need to add synchronisation to the generated C
code to ensure test has the same execution patterns.

For scheduling we use:

``waitUntilReady``
    ``waitUntilReady(id)`` logs that ``task[id]`` is waiting, and then attempts
    to execute a statement that blocks, until some other process changes
    ``task[id]``\ 's state to ``Ready``. It relies on the fact that if a
    statement blocks inside an atomic block, the block loses its atomic
    behaviour and yields to other Promela processes It is used to model a task
    that has been suspended for any reason.

``preemptIfRequired``
    ``preemptIfRequired(sendid,rcvid)`` is executed, when ``task[rcvid]`` has had its receive request satisfied
    by a send from ``task[sendid]``. It is invoked by the send operation in this
    model. It checks if ``task[sendid]`` should be preempted, and makes it so.
    This is achieved here by setting the task state to ``OtherWait``.

For synchronisation we use simple boolean semaphores, where True means
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


Event Send
~~~~~~~~~~

We start with the notion of when a event receive call is statisfied. The
requirements for both send and receive depend on such satisfaction.

``satisfied(task,out,sat)``
    ``satisfied(task,out,sat)`` checks if a receive has been satisfied. It
    updates its ``sat`` argument to reflect the check outcome.

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


There is a small complication, in that we have distinct variables in our model
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

Scenarios
~~~~~~~~~

We define a number of different scenario schemes that cover various aspects of
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

We have a range of global variables that define scenarios for both send and
receive. We then have a two-step process for choosing a scenario.
The first step is to select a scenario scheme. The poissible schemes are
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

We define default values for all the global scenario variables so that the
above code focusses on what differs. The default scenario is a receiver waiting
for a sender of the same priority which sends exactly what was requested.

Sender Process
~~~~~~~~~~~~~~


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

Receiver Process
~~~~~~~~~~~~~~~~

The receiver process  uses the scenario configuration to determine its
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

 We need a process that periodically wakes up blocked processes. This is
 modelling background behaviour of the system, such as ISRs and scheduling. We
 visit all tasks in round-robin order (to prevent starvation) and make them
 ready if waiting on other things. Tasks waiting for events or timeouts are
 not touched. This terminates when all tasks are zombies.

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

We need a process that handles a clock tick, by decrementing the tick count for
tasks waiting on a timeout. Such a task whose ticks become zero is then made
Ready, and its timer status is flagged as a timeout. This terminates when all
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


Refinement
^^^^^^^^^^

Files:
 | ``event-mgr-model-N.spn`` where ``N`` ranges from 0 to 8.
 | ``event-mgr-model-rfn.yml``

The test-code we generate here is based on the test-code generated from the
specification items used to describe the Event Manager in the main (non-formal)
part of the new qualification material.

The relevant specification item is ``spec/rtems/event/req/send-receive.yml``
found in ``rtems-central``. The corresponding C test code is
``tr-event-send-receive.c`` found in ``rtems`` at ``testsuites/validation``.
That automatically generated C code is a single file that uses a set of deeply
nested loops to iterate through the scenarios it generates.

Our approach is to generate a stand-alone C code file for each scenario
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


Most of the other refinement  entries are similar to those described above for
the Chains API.

Assembly
^^^^^^^^

Files:
 | ``tr-event-mgr-model.h``
 | ``tr-event-mgr-model.c``
 | ``event-mgr-model-pre.h`` (Preamble)
 | ``event-mgr-model-post.h`` (Postamble)
 | ``event-mgr-model-run.h`` (Runner)


The assembly process is the same as described for Chains.

Deployment
^^^^^^^^^^

Files:
 | ``tc-event-mgr-model.c``
 | ``tr-event-mgr-model.h``
 | ``tr-event-mgr-model.c``
 | ``tr-event-mgr-model-N.c`` where ``N`` ranges from 0 to 8.

All the above files are copied to ``testsuites/validation`` in the ``rtems``
repository, where they should be built and run using ``waf`` as normal.


Modelling Thread Queues
-----------------------

Below,
we summarise the current state of the thread queue verification effort.
All this verification material can be found at
``formal/promela/models/threadq``, which contains the following directories:

``MrsP-Code``
    Contains Promela models of the MrsP semaphore implementation, based on a
    reading of the actual code, assuming ``RTEMS_SMP`` is defined (among other
    settings). It is intended to check for desirable properties, and the
    absence of undesirable ones. It is not suitable for test generation. The
    main module is found in ``MAIN.pml``.

``MrsP-Tests``
    Contains Promela models of the MrsP semaphore behaviour, at a high level of
    abstraction. These are intended for test generation, which is not currently
    completed. The main module is ``mrsp-threadq-model.pml``, which currently
    generates 1092 scenarios. We go into more detail about this in sub-section
    :ref:`TestingThreadQueues`.

``Weak-Memory``
    Contains models of various aspects of weak memory. Parts of these may find
    their way into the MrsP models.

``docs``
    Contains LaTeX sources for early working documents. Currently out of scope.



Weak Memory Models
^^^^^^^^^^^^^^^^^^

Files in ``Weak-Memory/``:
 | ``memory_model.pml``
 | ``RAM.pml``
 | ``SPARC-TSO.pml``
 | ``wmemory.pml``

A model of generic weak memory is found in ``memory_model.pml`` (which includes
``RAM.pml`` and ``wmemory.pml``). This replaces an ideal atomic load or store
by one that has two phases, a move from register or RAM into some transport
medium (aether), follwed by a subsequent move into RAM or register. The model
has two threads that try to increment a memory location. At the end it asserts
that the location has value 2. This can be simulated using:

.. code-block:: shell

  spin memory_model.pml

This will sometimes succeed, and sometimes fail, as expected. If we run the
following commands:

.. code-block:: shell

  spin -run memory_model.pml
  spin -t -v memory_model.pml

then the first command reports an assertion violation error, while the second
replays the generated counter-example.

The file ``SPARC-TSO.pml`` is a standalone model of the Sparc architectures
Total Store Order (TSO) memory model. It is low-level, modelling individual
memory access instructions.

Modelling Thread Code
^^^^^^^^^^^^^^^^^^^^^

Files in ``MrsP-Code/`` :
 | ``MAIN.pml``
 | ``Chains.pml``
 | ``Concurrency.pml``
 | ``Heaps.pml``
 | ``Init.pml``
 | ``Locks.pml``
 | ``Priority.pml``
 | ``RBTrees.pml``
 | ``Scenarios.pml``
 | ``Semaphores.pml``
 | ``Sizing.pml``
 | ``State.pml``
 | ``Structs.pml``
 | ``Values.pml``

Scoping
~~~~~~~



Scoping is complete, and at first glance seems reasonable in size.
We are looking at scenarios involving a number of processors and schedulers
running a number of tasks of varying priorities that simply create,
obtain,
and release MrsP semaphores.
In practise, this touches a large part of the RTEMS code base.
We need to handle a wide variety of queues, implemented using both chains
and red-black trees, as well as different locking protocols.
The datastructures that represent processors, schedulers and threads,
are complex, with many linkages in between them. The MrsP protocols require
task to migrate from one processor to another under certain circumstances.

Modelling
~~~~~~~~~

Modelling began by looking at the key RTEMS API calls involved,
namely `rtems_semaphore_create()`, `rtems_semaphore_obtain()`,
and `rtems_semaphore_release()`.
Progress was good until an assertion from the RTEMS source failed
when transcribed into the Promela model.
This raised the need to model how the entire system is initialized,
at least those parts that can influence the MrsP protocol behaviour.
RTEMS initialization is very complex,
and an initial working model has only just been completed.

Validation
~~~~~~~~~~

In the current state of the model,
the main methods of validation are:
careful reading of the Promela code with respect to the corresponding C code;
and implementing every C code assertion in Promela using the `assert()` construct.
The C assertions capture the implementors understanding of good behaviour,
and our model should at least check they are satisfied within the model.

Verification
~~~~~~~~~~~~

We can perform simulation runs to observe behaviour,
but the model is not at the stage where we can use the model-checker to check
high-level properties, such as deadlock- or live-lock freedom.

.. _TestingThreadQueues:

Testing Thread Queues
-----------------------

The test-generation code is found in ``MrsP-Tests/``.

Model
^^^^^

Files:
 | ``Utilities.pml``
 | ``Sizing.pml``
 | ``Configure.pml``
 | ``Run.pml``
 | ``mrsp-threadq-model.pml``

``Utilities.pml``
~~~~~~~~~~~~~~~~~

Promela ``inline``\ s implementing useful calculations:

.. code-block:: c

    inline setMin( a, b, min ) { ... }
    inline chooseLowHigh( low, high, choice ) { ... }
    inline lowerRatio( n, p, lowerbound) { ... }

``Sizing.pml``
~~~~~~~~~~~~~~

This Promela code makes a non-deterministic choice of various sizes as follows:

  1. Choose number of cores, at least one
  2. Choose number of tasks, at least two, and at least one per core
  3. Choose number of resources, at least one

The maximum number of cores and resources possible is four, while up to six
tasks are possible.

``Configure.pml``
~~~~~~~~~~~~~~~~~

Given the number of cores, resources, and tasks, assign tasks to cores, and
resources to tasks, so that:

 1. Every core has at least one task.
 2. Every resource is associated with at least two tasks.

``Run.pml``
~~~~~~~~~~~

This builds a Promela model of a task that takes its nominal behaviour (a.k.a.
its business logic) and interleaves this with regular checks to see if it is
not blocked, doing its business, and then invoking a context switch.

.. code-block:: c

   WAIT_TO_RUN( tno );   // <1>
   tryObtain( tno, 3 );   // <2>
   contextSwitch( taskConfig[tno].taskCore );   // <3>

.. topic:: Items:

  1. Wait here until the scheduler makes me ``Ready``.
  2. Do my business logic (here trying to obtain a semaphore).
  3. Perform a context switch that allows the scheduler (model) to run.

``mrsp-threadq-model.pml``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Chooses a scenario, launches all the tasks, waits for them to complete, and then
asserts ``false`` if test generation is active and we are about to terminate.

Annotations
^^^^^^^^^^^

The only annotations that have been developed at this point are those in
``Sizing.pml`` that report the number of key elements in a scenario.

Refinement
^^^^^^^^^^

No refinement has been developed at this point.

Assembly
^^^^^^^^

Files:
 | ``tr-mrsp-threadq-model.h``
 | ``tr-mrsp-threadq-model.c``
 | ``mrsp-threadq-model-pre.h`` (Preamble)
 | ``mrsp-threadq-model-post.h`` (Postamble)
 | ``mrsp-threadq-model-run.h`` (Runner)


The assembly process is the same as described for Chains.

Deployment
^^^^^^^^^^

Files:
 | ``tc-mrsp-threadq-model.c``
 | ``tr-mrsp-threadq-model.h``
 | ``tr-mrsp-threadq-model.c``
 | ``tr-mrsp-threadq-model-N.c`` where ``N`` ranges from 0 to 1091.

All the above files are copied to ``testsuites/validation`` in the ``rtems``
repository, where they should be built and run using ``waf`` as normal.
