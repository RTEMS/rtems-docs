.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin


Modelling Thread Queues
-----------------------

**This material has been removed for now from the SWEng manual as it is work in progress.
It will revised and added back into the modelling guide when it is deemed fit for deployment**

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
