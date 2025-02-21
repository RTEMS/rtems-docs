.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

IDLE Thread
###########

Does Idle Thread Have a Floating Point Context?
===============================================

The setting of the macro CPU_IDLE_TASK_IS_FP is based on the answer to the
question:  Should the IDLE task have a floating point context?

If the answer to this question is TRUE, then the IDLE task has a floating
point context associated.  This is equivalent to creating a task in the
Classic API (using rtems_task_create) as a RTEMS_FLOATING_POINT task. If
CPU_IDLE_TASK_IS_FP is set to TRUE, then a floating point context switch
occurs when the IDLE task is switched in and out.  This adds to the
execution overhead of the system but is necessary on some ports.

If FALSE, then the IDLE task does not have a floating point context.

NOTE: Setting CPU_IDLE_TASK_IS_FP to TRUE negatively impacts the time
required to preempt the IDLE task from an interrupt because the floating
point context must be saved as part of the preemption.

The following illustrates how to set this macro:

.. code-block:: c

    #define CPU_IDLE_TASK_IS_FP      FALSE

CPU Dependent Idle Thread Body
==============================

CPU_PROVIDES_IDLE_THREAD_BODY Macro Setting
-------------------------------------------

The CPU_PROVIDES_IDLE_THREAD_BODY macro setting is based upon the answer
to the question:  Does this port provide a CPU dependent IDLE task
implementation?  If the answer to this question is yes, then the
CPU_PROVIDES_IDLE_THREAD_BODY macro should be set to TRUE, and the routine
_CPU_Thread_Idle_body must be provided.  This routine overrides the
default IDLE thread body of _Thread_Idle_body.  If the
CPU_PROVIDES_IDLE_THREAD_BODY macro is set to FALSE, then the generic
_Thread_Idle_body is the default IDLE thread body for this port.
Regardless of whether or not a CPU dependent IDLE thread implementation is
provided, the BSP can still override it.

This is intended to allow for supporting processors which have a low power
or idle mode.  When the IDLE thread is executed, then the CPU can be
powered down when the processor is idle.

The order of precedence for selecting the IDLE thread body is:

#. BSP provided

#. CPU dependent (if provided)

#. generic (if no BSP and no CPU dependent)

The following illustrates setting the CPU_PROVIDES_IDLE_THREAD_BODY macro:

.. code-block:: c

    #define CPU_PROVIDES_IDLE_THREAD_BODY    TRUE

Implementation details of a CPU model specific IDLE thread body are in the
next section.

Idle Thread Body
----------------

The _CPU_Thread_Idle_body routine only needs to be provided if the porter
wishes to include a CPU dependent IDLE thread body.  If the port includes
a CPU dependent implementation of the IDLE thread body, then the
CPU_PROVIDES_IDLE_THREAD_BODY macro should be defined to TRUE.  This
routine is prototyped as follows:

.. code-block:: c

    void *_CPU_Thread_Idle_body( uintptr_t );

As mentioned above, RTEMS does not require that a CPU dependent IDLE
thread body be provided as part of the port.  If
CPU_PROVIDES_IDLE_THREAD_BODY is defined to FALSE, then the CPU
independent algorithm is used.  This algorithm consists of a "branch to
self" which is implemented in a routine as follows.

.. code-block:: c

    void *_Thread_Idle_body( uintptr_t ignored )
    {
      while( 1 ) ;
    }

If the CPU dependent IDLE thread body is implementation centers upon using
a "halt", "idle", or "shutdown" instruction, then don't forget to put it
in an infinite loop as the CPU will have to reexecute this instruction
each time the IDLE thread is dispatched.

.. code-block:: c

    void *_CPU_Thread_Idle_body( uintptr_t ignored )
    {
      for( ; ; )
        /* insert your "halt" instruction here */ ;
    }

Be warned. Some processors with onboard DMA have been known to stop the
DMA if the CPU were put in IDLE mode.  This might also be a problem with
other on-chip peripherals.  So use this hook with caution.
