.. comment SPDX-License-Identifier: CC-BY-SA-4.0


.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Miscellaneous Support Files
###########################

GCC Compiler Specifications File
================================

The file ``bsp_specs`` defines the start files and libraries that are always
used with this BSP.  The format of this file is admittedly cryptic and this
document will make no attempt to explain it completely.  Below is the
``bsp_specs`` file from the PowerPC psim BSP:

.. code-block:: c

    %rename endfile old_endfile
    %rename startfile old_startfile
    %rename link old_link
    *startfile:
    %{!qrtems: %(old_startfile)} \
    %{!nostdlib: %{qrtems: ecrti%O%s rtems_crti%O%s crtbegin.o%s start.o%s}}
    *link:
    %{!qrtems: %(old_link)} %{qrtems: -Qy -dp -Bstatic -e _start -u __vectors}
    *endfile:
    %{!qrtems: %(old_endfile)} %{qrtems: crtend.o%s ecrtn.o%s}

The first section of this file renames the built-in definition of some
specification variables so they can be augmented without embedded their
original definition.  The subsequent sections specify what behavior is expected
when the ``-qrtems`` option is specified.

The ``*startfile`` section specifies that the BSP specific file ``start.o``
will be used instead of ``crt0.o``.  In addition, various EABI support files
(``ecrti.o`` etc.) will be linked in with the executable.

The ``*link`` section adds some arguments to the linker when it is invoked by
GCC to link an application for this BSP.

The format of this file is specific to the GNU Compiler Suite.  The argument
used to override and extend the compiler built-in specifications is available
in all recent GCC versions.  The ``-specs`` option is present in all ``egcs``
distributions and ``gcc`` distributions starting with version 2.8.0.

README Files
============

Most BSPs provide one or more ``README`` files.  Generally, there is a
``README`` file at the top of the BSP source.  This file describes the board
and its hardware configuration, provides vendor information, local
configuration information, information on downloading code to the board,
debugging, etc..  The intent of this file is to help someone begin to use the
BSP faster.

A ``README`` file in a BSP subdirectory typically explains something about the
contents of that subdirectory in greater detail.  For example, it may list the
documentation available for a particular peripheral controller and how to
obtain that documentation.  It may also explain some particularly cryptic part
of the software in that directory or provide rationale on the implementation.

times
=====

This file contains the results of the RTEMS Timing Test Suite.  It is in a
standard format so that results from one BSP can be easily compared with those
of another target board.

If a BSP supports multiple variants, then there may be multiple ``times``
files.  Usually these are named ``times.VARIANTn``.

Tools Subdirectory
==================

Some BSPs provide additional tools that aid in using the target board.  These
tools run on the development host and are built as part of building the BSP.
Most common is a script to automate running the RTEMS Test Suites on the BSP.
Examples of this include:

- ``powerpc/psim`` includes scripts to ease use of the simulator

- ``m68k/mvme162`` includes a utility to download across the VMEbus into target
  memory if the host is a VMEbus board in the same chasis.

bsp.h Include File
==================

The file ``include/bsp.h`` contains prototypes and definitions specific to this
board.  Every BSP is required to provide a ``bsp.h``.  The best approach to
writing a ``bsp.h`` is copying an existing one as a starting point.

Many ``bsp.h`` files provide prototypes of variables defined in the linker
script (``linkcmds``).

tm27.h Include File
===================

The ``tm27`` test from the RTEMS Timing Test Suite is designed to measure the
length of time required to vector to and return from an interrupt handler. This
test requires some help from the BSP to know how to cause and manipulate the
interrupt source used for this measurement.  The following is a list of these:

- ``MUST_WAIT_FOR_INTERRUPT`` - modifies behavior of ``tm27``.

- ``Install_tm27_vector`` - installs the interrupt service routine for the
  Interrupt Benchmark Test (``tm27``).

- ``Cause_tm27_intr`` - generates the interrupt source used in the Interrupt
  Benchmark Test (``tm27``).

- ``Clear_tm27_intr`` - clears the interrupt source used in the Interrupt
  Benchmark Test (``tm27``).

- ``Lower_tm27_intr`` - lowers the interrupt mask so the interrupt source used
  in the Interrupt Benchmark Test (``tm27``) can generate a nested interrupt.

All members of the Timing Test Suite are designed to run *WITHOUT* the Clock
Device Driver installed.  This increases the predictability of the tests'
execution as well as avoids occassionally including the overhead of a clock
tick interrupt in the time reported.  Because of this it is sometimes possible
to use the clock tick interrupt source as the source of this test interrupt.
On other architectures, it is possible to directly force an interrupt to occur.

Calling Overhead File
=====================

The file ``include/coverhd.h`` contains the overhead associated with invoking
each directive.  This overhead consists of the execution time required to
package the parameters as well as to execute the "jump to subroutine" and
"return from subroutine" sequence.  The intent of this file is to help separate
the calling overhead from the actual execution time of a directive.  This file
is only used by the tests in the RTEMS Timing Test Suite.

The numbers in this file are obtained by running the "Timer
Overhead"``tmoverhd`` test.  The numbers in this file may be 0 and no overhead
is subtracted from the directive execution times reported by the Timing Suite.

There is a shared implementation of ``coverhd.h`` which sets all of the
overhead constants to 0.  On faster processors, this is usually the best
alternative for the BSP as the calling overhead is extremely small.  This file
is located at:

.. code-block:: c

    c/src/lib/libbsp/shared/include/coverhd.h

sbrk() Implementation
=====================

Although nearly all BSPs give all possible memory to the C Program Heap at
initialization, it is possible for a BSP to configure the initial size of the
heap small and let it grow on demand.  If the BSP wants to dynamically extend
the heap used by the C Library memory allocation routines (i.e. ``malloc``
family), then the``sbrk`` routine must be functional.  The following is the
prototype for this routine:

.. code-block:: c

    void * sbrk(size_t increment)

The ``increment`` amount is based upon the ``sbrk_amount`` parameter passed to
the ``bsp_libc_init`` during system initialization.

.. index:: CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK

If your BSP does not want to support dynamic heap extension, then you do not
have to do anything special.  However, if you want to support ``sbrk``, you
must provide an implementation of this method and define
``CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK`` in ``bsp.h``.  This informs
``rtems/confdefs.h`` to configure the Malloc Family Extensions which support
``sbrk``.

bsp_fatal_extension() - Cleanup the Hardware
============================================

The ``bsp_fatal_extension()`` is an optional BSP specific initial extension
invoked once a fatal system state is reached.  Most of the BSPs use the same
shared version of ``bsp_fatal_extension()`` that does nothing or performs a
system reset.  This implementation is located in the following file:

.. code-block:: c

    c/src/lib/libbsp/shared/bspclean.c

The ``bsp_fatal_extension()`` routine can be used to return to a ROM monitor,
insure that interrupt sources are disabled, etc..  This routine is the last
place to ensure a clean shutdown of the hardware.  The fatal source, internal
error indicator, and the fatal code arguments are available to evaluate the
fatal condition.  All of the non-fatal shutdown sequences ultimately pass their
exit status to ``rtems_shutdown_executive`` and this is what is passed to this
routine in case the fatal source is ``RTEMS_FATAL_SOURCE_EXIT``.

On some BSPs, it prints a message indicating that the application completed
execution and waits for the user to press a key before resetting the board.
The PowerPC/gen83xx and PowerPC/gen5200 BSPs do this when they are built to
support the FreeScale evaluation boards.  This is convenient when using the
boards in a development environment and may be disabled for production use.

Configuration Macros
====================

Each BSP can define macros in bsp.h which alter some of the the default
configuration parameters in ``rtems/confdefs.h``.  This section describes those
macros:

.. index:: CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK

- ``CONFIGURE_MALLOC_BSP_SUPPORTS_SBRK`` must be defined if the BSP has proper
  support for ``sbrk``.  This is discussed in more detail in the previous
  section.

.. index:: BSP_IDLE_TASK_BODY

- ``BSP_IDLE_TASK_BODY`` may be defined to the entry point of a BSP specific
  IDLE thread implementation.  This may be overridden if the application
  provides its own IDLE task implementation.

.. index:: BSP_IDLE_TASK_STACK_SIZE

- ``BSP_IDLE_TASK_STACK_SIZE`` may be defined to the desired default stack size
  for the IDLE task as recommended when using this BSP.

.. index:: BSP_INTERRUPT_STACK_SIZE

- ``BSP_INTERRUPT_STACK_SIZE`` may be defined to the desired default interrupt
  stack size as recommended when using this BSP.  This is sometimes required
  when the BSP developer has knowledge of stack intensive interrupt handlers.

.. index:: BSP_ZERO_WORKSPACE_AUTOMATICALLY

- ``BSP_ZERO_WORKSPACE_AUTOMATICALLY`` is defined when the BSP requires that
  RTEMS zero out the RTEMS C Program Heap at initialization.  If the memory is
  already zeroed out by a test sequence or boot ROM, then the boot time can be
  reduced by not zeroing memory twice.

.. index:: BSP_DEFAULT_UNIFIED_WORK_AREAS

- ``BSP_DEFAULT_UNIFIED_WORK_AREAS`` is defined when the BSP recommends that
  the unified work areas configuration should always be used.  This is
  desirable when the BSP is known to always have very little RAM and thus
  saving memory by any means is desirable.

set_vector() - Install an Interrupt Vector
==========================================

On targets with Simple Vectored Interrupts, the BSP must provide an
implementation of the ``set_vector`` routine.  This routine is responsible for
installing an interrupt vector.  It invokes the support routines necessary to
install an interrupt handler as either a "raw" or an RTEMS interrupt handler.
Raw handlers bypass the RTEMS interrupt structure and are responsible for
saving and restoring all their own registers.  Raw handlers are useful for
handling traps, debug vectors, etc.

The ``set_vector`` routine is a central place to perform interrupt controller
manipulation and encapsulate that information.  It is usually implemented as
follows:

.. code-block:: c

    rtems_isr_entry set_vector(                 /* returns old vector */
      rtems_isr_entry handler,                  /* isr routine        */
      rtems_vector_number vector,               /* vector number      */
      int                 type                  /* RTEMS or RAW intr  */
    )
    {
      if the type is RAW
        install the raw vector
      else
        use rtems_interrupt_catch to install the vector
      perform any interrupt controller necessary to unmask the interrupt source
      return the previous handler
    }

.. note::

    The i386, PowerPC and ARM ports use a Programmable Interrupt Controller
    model which does not require the BSP to implement ``set_vector``.  BSPs for
    these architectures must provide a different set of support routines.

Interrupt Delay Profiling
=========================

The RTEMS profiling needs support by the BSP for the interrupt delay times.  In
case profiling is enabled via the RTEMS build configuration option
``--enable-profiling`` (in this case the pre-processor symbol
``RTEMS_PROFILING`` is defined) a BSP may provide data for the interrupt delay
times.  The BSP can feed interrupt delay times with the
``_Profiling_Update_max_interrupt_delay()`` function (``#include
<rtems/score/profiling.h>``).  For an example please have a look at
``c/src/lib/libbsp/sparc/leon3/clock/ckinit.c``.

Programmable Interrupt Controller API
=====================================

A BSP can use the PIC API to install Interrupt Service Routines through a set
of generic methods. In order to do so, the header files
libbsp/shared/include/irq-generic.h and ``libbsp/shared/include/irq-info.h``
must be included by the bsp specific irq.h file present in the include/
directory. The irq.h acts as a BSP interrupt support configuration file which
is used to define some important MACROS. It contains the declarations for any
required global functions like bsp_interrupt_dispatch(). Thus later on, every
call to the PIC interface requires including ``<bsp/irq.h>``

The generic interrupt handler table is intitalized by invoking the
``bsp_interrupt_initialize()`` method from bsp_start() in the bspstart.c file
which sets up this table to store the ISR addresses, whose size is based on the
definition of macros, ``BSP_INTERRUPT_VECTOR_MIN`` and
``BSP_INTERRUPT_VECTOR_MAX`` in include/bsp.h

For the generic handler table to properly function, some bsp specific code is
required, that should be present in ``irq/irq.c``. The bsp-specific functions
required to be writen by the BSP developer are :

.. index:: bsp_interrupt_facility_initialize()

- ``bsp_interrupt_facility_initialize()`` contains bsp specific interrupt
  initialization code(Clear Pending interrupts by modifying registers, etc.).
  This method is called from ``bsp_interrupt_initialize()`` internally while
  setting up the table.

.. index:: bsp_interrupt_handler_default()

- ``bsp_interrupt_handler_default()`` acts as a fallback handler when no ISR
  address has been provided corresponding to a vector in the table.

.. index:: bsp_interrupt_dispatch()

- ``bsp_interrupt_dispatch()`` service the ISR by handling any bsp specific
  code & calling the generic method ``bsp_interrupt_handler_dispatch()`` which
  in turn services the interrupt by running the ISR after looking it up in the
  table. It acts as an entry to the interrupt switchboard, since the bsp
  branches to this function at the time of occurrence of an interrupt.

.. index:: bsp_interrupt_vector_enable()

- ``bsp_interrupt_vector_enable()`` enables interrupts and is called in
  irq-generic.c while setting up the table.

.. index:: bsp_interrupt_vector_disable()

- ``bsp_interrupt_vector_disable()`` disables interrupts and is called in
  irq-generic.c while setting up the table & during other important parts.

An interrupt handler is installed or removed with the help of the following functions :

.. code-block:: c

    rtems_status_code rtems_interrupt_handler_install(   /* returns status code */
      rtems_vector_number     vector,                    /* interrupt vector */
      const char             *info,                      /* custom identification text */
      rtems_option            options,                   /* Type of Interrupt */
      rtems_interrupt_handler handler,                   /* interrupt handler */
      void                   *arg                        /* parameter to be passed
                                                            to handler at the time of
                                                            invocation */
    )
    rtems_status_code rtems_interrupt_handler_remove(   /* returns status code */
      rtems_vector_number     vector,                   /* interrupt vector */
      rtems_interrupt_handler handler,                  /* interrupt handler */
      void                   *arg                       /* parameter to be passed to handler */
    )
