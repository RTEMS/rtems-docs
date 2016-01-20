CPU Initialization
##################

This section describes the general CPU and system initialization sequence
as it pertains to the CPU dependent code.

Introduction
============

XXX general startup sequence description rewritten to make it more
applicable to CPU depdent code in executive

Initializing the CPU
====================

The _CPU_Initialize routine performs processor dependent initialization.
.. code:: c

    void _CPU_Initialize(
    void            (\*thread_dispatch)  /* may be ignored \*/
    )

The thread_dispatch argument is the address of the entry point for the
routine called at the end of an ISR once it has been decided a context
switch is necessary.  On some compilation systems it is difficult to call
a high-level language routine from assembly.  Providing the address of the
_Thread_ISR_Dispatch routine allows the porter an easy way to obtain this
critical address and thus provides an easy way to work around this
limitation on these systems.

If you encounter this problem save the entry point in a CPU dependent
variable as shown below:
.. code:: c

    _CPU_Thread_dispatch_pointer = thread_dispatch;

During the initialization of the context for tasks with floating point,
the CPU dependent code is responsible for initializing the floating point
context.  If there is not an easy way to initialize the FP context during
Context_Initialize, then it is usually easier to save an "uninitialized"
FP context here and copy it to the task's during Context_Initialize.  If
this technique is used to initialize the FP contexts, then it is important
to ensure that the state of the floating point unit is in a coherent,
initialized state.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.
