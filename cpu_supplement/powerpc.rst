PowerPC Specific Information
############################

This chapter discusses the PowerPC architecture dependencies
in this port of RTEMS.  The PowerPC family has a wide variety
of implementations by a range of vendors.  Consequently,
there are many, many CPU models within it.

It is highly recommended that the PowerPC RTEMS
application developer obtain and become familiar with the
documentation for the processor being used as well as the
specification for the revision of the PowerPC architecture which
corresponds to that processor.

**PowerPC Architecture Documents**

For information on the PowerPC architecture, refer to
the following documents available from Motorola and IBM:

- *PowerPC Microprocessor Family: The Programming Environment*
  (Motorola Document MPRPPCFPE-01).

- *IBM PPC403GB Embedded Controller User’s Manual*.

- *PoweRisControl MPC500 Family RCPU RISC Central Processing
  Unit Reference Manual* (Motorola Document RCPUURM/AD).

- *PowerPC 601 RISC Microprocessor User’s Manual*
  (Motorola Document MPR601UM/AD).

- *PowerPC 603 RISC Microprocessor User’s Manual*
  (Motorola Document MPR603UM/AD).

- *PowerPC 603e RISC Microprocessor User’s Manual*
  (Motorola Document MPR603EUM/AD).

- *PowerPC 604 RISC Microprocessor User’s Manual*
  (Motorola Document MPR604UM/AD).

- *PowerPC MPC821 Portable Systems Microprocessor User’s Manual*
  (Motorola Document MPC821UM/AD).

- *PowerQUICC MPC860 User’s Manual* (Motorola Document MPC860UM/AD).

Motorola maintains an on-line electronic library for the PowerPC
at the following URL:

-  http://www.mot.com/powerpc/library/library.html

This site has a a wealth of information and examples.  Many of the
manuals are available from that site in electronic format.

**PowerPC Processor Simulator Information**

PSIM is a program which emulates the Instruction Set Architecture
of the PowerPC microprocessor family.  It is reely available in source
code form under the terms of the GNU General Public License (version
2 or later).  PSIM can be integrated with the GNU Debugger (gdb) to
execute and debug PowerPC executables on non-PowerPC hosts.  PSIM
supports the addition of user provided device models which can be
used to allow one to develop and debug embedded applications using
the simulator.

The latest version of PSIM is included in GDB and enabled on pre-built
binaries provided by the RTEMS Project.

CPU Model Dependent Features
============================

This section presents the set of features which vary
across PowerPC implementations and are of importance to RTEMS.
The set of CPU model feature macros are defined in the file``cpukit/score/cpu/powerpc/powerpc.h`` based upon the particular CPU
model specified on the compilation command line.

Alignment
---------

The macro PPC_ALIGNMENT is set to the PowerPC model’s worst case alignment
requirement for data types on a byte boundary.  This value is used
to derive the alignment restrictions for memory allocated from
regions and partitions.

Cache Alignment
---------------

The macro PPC_CACHE_ALIGNMENT is set to the line size of the cache.  It is
used to align the entry point of critical routines so that as much code
as possible can be retrieved with the initial read into cache.  This
is done for the interrupt handler as well as the context switch routines.

In addition, the "shortcut" data structure used by the PowerPC implementation
to ease access to data elements frequently accessed by RTEMS routines
implemented in assembly language is aligned using this value.

Maximum Interrupts
------------------

The macro PPC_INTERRUPT_MAX is set to the number of exception sources
supported by this PowerPC model.

Has Double Precision Floating Point
-----------------------------------

The macro PPC_HAS_DOUBLE is set to 1 to indicate that the PowerPC model
has support for double precision floating point numbers.  This is
important because the floating point registers need only be four bytes
wide (not eight) if double precision is not supported.

Critical Interrupts
-------------------

The macro PPC_HAS_RFCI is set to 1 to indicate that the PowerPC model
has the Critical Interrupt capability as defined by the IBM 403 models.

Use Multiword Load/Store Instructions
-------------------------------------

The macro PPC_USE_MULTIPLE is set to 1 to indicate that multiword load and
store instructions should be used to perform context switch operations.
The relative efficiency of multiword load and store instructions versus
an equivalent set of single word load and store instructions varies based
upon the PowerPC model.

Instruction Cache Size
----------------------

The macro PPC_I_CACHE is set to the size in bytes of the instruction cache.

Data Cache Size
---------------

The macro PPC_D_CACHE is set to the size in bytes of the data cache.

Debug Model
-----------

The macro PPC_DEBUG_MODEL is set to indicate the debug support features
present in this CPU model.  The following debug support feature sets
are currently supported:

*``PPC_DEBUG_MODEL_STANDARD``*
    indicates that the single-step trace enable (SE) and branch trace
    enable (BE) bits in the MSR are supported by this CPU model.

*``PPC_DEBUG_MODEL_SINGLE_STEP_ONLY``*
    indicates that only the single-step trace enable (SE) bit in the MSR
    is supported by this CPU model.

*``PPC_DEBUG_MODEL_IBM4xx``*
    indicates that the debug exception enable (DE) bit in the MSR is supported
    by this CPU model.  At this time, this particular debug feature set
    has only been seen in the IBM 4xx series.

Low Power Model
~~~~~~~~~~~~~~~

The macro PPC_LOW_POWER_MODE is set to indicate the low power model
supported by this CPU model.  The following low power modes are currently
supported.

*``PPC_LOW_POWER_MODE_NONE``*
    indicates that this CPU model has no low power mode support.

*``PPC_LOW_POWER_MODE_STANDARD``*
    indicates that this CPU model follows the low power model defined for
    the PPC603e.

Multilibs
=========

The following multilibs are available:

# ``.``: 32-bit PowerPC with FPU

# ``nof``: 32-bit PowerPC with software floating point support

# ``m403``: Instruction set for PPC403 with FPU

# ``m505``: Instruction set for MPC505 with FPU

# ``m603e``: Instruction set for MPC603e with FPU

# ``m603e/nof``: Instruction set for MPC603e with software floating
  point support

# ``m604``: Instruction set for MPC604 with FPU

# ``m604/nof``: Instruction set for MPC604 with software floating point
  support

# ``m860``: Instruction set for MPC860 with FPU

# ``m7400``: Instruction set for MPC7500 with FPU

# ``m7400/nof``: Instruction set for MPC7500 with software floating
  point support

# ``m8540``: Instruction set for e200, e500 and e500v2 cores with
  single-precision FPU and SPE

# ``m8540/gprsdouble``: Instruction set for e200, e500 and e500v2 cores
  with double-precision FPU and SPE

# ``m8540/nof/nospe``: Instruction set for e200, e500 and e500v2 cores
  with software floating point support and no SPE

# ``me6500/m32``: 32-bit instruction set for e6500 core with FPU and
  AltiVec

# ``me6500/m32/nof/noaltivec``: 32-bit instruction set for e6500 core
  with software floating point support and no AltiVec

Calling Conventions
===================

RTEMS supports the Embedded Application Binary Interface (EABI)
calling convention.  Documentation for EABI is available by sending
a message with a subject line of "EABI" to eabi@goth.sis.mot.com.

Programming Model
-----------------

This section discusses the programming model for the
PowerPC architecture.

Non-Floating Point Registers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PowerPC architecture defines thirty-two non-floating point registers
directly visible to the programmer.  In thirty-two bit implementations, each
register is thirty-two bits wide.  In sixty-four bit implementations, each
register is sixty-four bits wide.

These registers are referred to as ``gpr0`` to ``gpr31``.

Some of the registers serve defined roles in the EABI programming model.
The following table describes the role of each of these registers:
.. code:: c

    +---------------+----------------+------------------------------+
    | Register Name | Alternate Name |         Description          |
    +---------------+----------------+------------------------------+
    |      r1       |      sp        |         stack pointer        |
    +---------------+----------------+------------------------------+
    |               |                |  global pointer to the Small |
    |      r2       |      na        |     Constant Area (SDA2)     |
    +---------------+----------------+------------------------------+
    |    r3 - r12   |      na        | parameter and result passing |
    +---------------+----------------+------------------------------+
    |               |                |  global pointer to the Small |
    |      r13      |      na        |         Data Area (SDA)      |
    +---------------+----------------+------------------------------+

Floating Point Registers
~~~~~~~~~~~~~~~~~~~~~~~~

The PowerPC architecture includes thirty-two, sixty-four bit
floating point registers.  All PowerPC floating point instructions
interpret these registers as 32 double precision floating point registers,
regardless of whether the processor has 64-bit or 32-bit implementation.

The floating point status and control register (fpscr) records exceptions
and the type of result generated by floating-point operations.
Additionally, it controls the rounding mode of operations and allows the
reporting of floating exceptions to be enabled or disabled.

Special Registers
~~~~~~~~~~~~~~~~~

The PowerPC architecture includes a number of special registers
which are critical to the programming model:

*Machine State Register*
    The MSR contains the processor mode, power management mode, endian mode,
    exception information, privilege level, floating point available and
    floating point excepiton mode, address translation information and
    the exception prefix.

*Link Register*
    The LR contains the return address after a function call.  This register
    must be saved before a subsequent subroutine call can be made.  The
    use of this register is discussed further in the *Call and Return
    Mechanism* section below.

*Count Register*
    The CTR contains the iteration variable for some loops.  It may also be used
    for indirect function calls and jumps.

Call and Return Mechanism
-------------------------

The PowerPC architecture supports a simple yet effective call
and return mechanism.  A subroutine is invoked
via the "branch and link" (``bl``) and
"brank and link absolute" (``bla``)
instructions.  This instructions place the return address
in the Link Register (LR).  The callee returns to the caller by
executing a "branch unconditional to the link register" (``blr``)
instruction.  Thus the callee returns to the caller via a jump
to the return address which is stored in the LR.

The previous contents of the LR are not automatically saved
by either the ``bl`` or ``bla``.  It is the responsibility
of the callee to save the contents of the LR before invoking
another subroutine.  If the callee invokes another subroutine,
it must restore the LR before executing the ``blr`` instruction
to return to the caller.

It is important to note that the PowerPC subroutine
call and return mechanism does not automatically save and
restore any registers.

The LR may be accessed as special purpose register 8 (``SPR8``) using the
"move from special register" (``mfspr``) and
"move to special register" (``mtspr``) instructions.

Calling Mechanism
-----------------

All RTEMS directives are invoked using the regular
PowerPC EABI calling convention via the ``bl`` or``bla`` instructions.

Register Usage
--------------

As discussed above, the call instruction does not
automatically save any registers.  It is the responsibility
of the callee to save and restore any registers which must be preserved
across subroutine calls.  The callee is responsible for saving
callee-preserved registers to the program stack and restoring them
before returning to the caller.

Parameter Passing
-----------------

RTEMS assumes that arguments are placed in the
general purpose registers with the first argument in
register 3 (``r3``), the second argument in general purpose
register 4 (``r4``), and so forth until the seventh
argument is in general purpose register 10 (``r10``).
If there are more than seven arguments, then subsequent arguments
are placed on the program stack.  The following pseudo-code
illustrates the typical sequence used to call a RTEMS directive
with three (3) arguments:
.. code:: c

    load third argument into r5
    load second argument into r4
    load first argument into r3
    invoke directive

Memory Model
============

Flat Memory Model
-----------------

The PowerPC architecture supports a variety of memory models.
RTEMS supports the PowerPC using a flat memory model with
paging disabled.  In this mode, the PowerPC automatically
converts every address from a logical to a physical address
each time it is used.  The PowerPC uses information provided
in the Block Address Translation (BAT) to convert these addresses.

Implementations of the PowerPC architecture may be thirty-two or sixty-four bit.
The PowerPC architecture supports a flat thirty-two or sixty-four bit address
space with addresses ranging from 0x00000000 to 0xFFFFFFFF (4
gigabytes) in thirty-two bit implementations or to 0xFFFFFFFFFFFFFFFF
in sixty-four bit implementations.  Each address is represented
by either a thirty-two bit or sixty-four bit value and is byte addressable.
The address may be used to reference a single byte, half-word
(2-bytes), word (4 bytes), or in sixty-four bit implementations a
doubleword (8 bytes).  Memory accesses within the address space are
performed in big or little endian fashion by the PowerPC based
upon the current setting of the Little-endian mode enable bit (LE)
in the Machine State Register (MSR).  While the processor is in
big endian mode, memory accesses which are not properly aligned
generate an "alignment exception" (vector offset 0x00600).  In
little endian mode, the PowerPC architecture does not require
the processor to generate alignment exceptions.

The following table lists the alignment requirements for a variety
of data accesses:

.. code:: c

    +--------------+-----------------------+
    |   Data Type  | Alignment Requirement |
    +--------------+-----------------------+
    |     byte     |          1            |
    |   half-word  |          2            |
    |     word     |          4            |
    |  doubleword  |          8            |
    +--------------+-----------------------+

Doubleword load and store operations are only available in
PowerPC CPU models which are sixty-four bit implementations.

RTEMS does not directly support any PowerPC Memory Management
Units, therefore, virtual memory or segmentation systems
involving the PowerPC  are not supported.

.. COMMENT: COPYRIGHT (c) 1989-2007.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

Interrupt Processing
====================

Although RTEMS hides many of the processor dependent
details of interrupt processing, it is important to understand
how the RTEMS interrupt manager is mapped onto the processor’s
unique architecture. Discussed in this chapter are the PowerPC’s
interrupt response and control mechanisms as they pertain to
RTEMS.

RTEMS and associated documentation uses the terms interrupt and vector.
In the PowerPC architecture, these terms correspond to exception and
exception handler, respectively.  The terms will be used interchangeably
in this manual.

Synchronous Versus Asynchronous Exceptions
------------------------------------------

In the PowerPC architecture exceptions can be either precise or
imprecise and either synchronous or asynchronous.  Asynchronous
exceptions occur when an external event interrupts the processor.
Synchronous exceptions are caused by the actions of an
instruction. During an exception SRR0 is used to calculate where
instruction processing should resume.  All instructions prior to
the resume instruction will have completed execution.  SRR1 is used to
store the machine status.

There are two asynchronous nonmaskable, highest-priority exceptions
system reset and machine check.  There are two asynchrononous maskable
low-priority exceptions external interrupt and decrementer.  Nonmaskable
execptions are never delayed, therefore if two nonmaskable, asynchronous
exceptions occur in immediate succession, the state information saved by
the first exception may be overwritten when the subsequent exception occurs.

The PowerPC arcitecure defines one imprecise exception, the imprecise
floating point enabled exception.  All other synchronous exceptions are
precise.  The synchronization occuring during asynchronous precise
exceptions conforms to the requirements for context synchronization.

Vectoring of Interrupt Handler
------------------------------

Upon determining that an exception can be taken the PowerPC automatically
performs the following actions:

- an instruction address is loaded into SRR0

- bits 33-36 and 42-47 of SRR1 are loaded with information
  specific to the exception.

- bits 0-32, 37-41, and 48-63 of SRR1 are loaded with corresponding
  bits from the MSR.

- the MSR is set based upon the exception type.

- instruction fetch and execution resumes, using the new MSR value, at a location specific to the execption type.

If the interrupt handler was installed as an RTEMS
interrupt handler, then upon receipt of the interrupt, the
processor passes control to the RTEMS interrupt handler which
performs the following actions:

- saves the state of the interrupted task on it’s stack,

- saves all registers which are not normally preserved
  by the calling sequence so the user’s interrupt service
  routine can be written in a high-level language.

- if this is the outermost (i.e. non-nested) interrupt,
  then the RTEMS interrupt handler switches from the current stack
  to the interrupt stack,

- enables exceptions,

- invokes the vectors to a user interrupt service routine (ISR).

Asynchronous interrupts are ignored while exceptions are
disabled.  Synchronous interrupts which occur while are
disabled result in the CPU being forced into an error mode.

A nested interrupt is processed similarly with the
exception that the current stack need not be switched to the
interrupt stack.

Interrupt Levels
----------------

The PowerPC architecture supports only a single external
asynchronous interrupt source.  This interrupt source
may be enabled and disabled via the External Interrupt Enable (EE)
bit in the Machine State Register (MSR).  Thus only two level (enabled
and disabled) of external device interrupt priorities are
directly supported by the PowerPC architecture.

Some PowerPC implementations include a Critical Interrupt capability
which is often used to receive interrupts from high priority external
devices.

The RTEMS interrupt level mapping scheme for the PowerPC is not
a numeric level as on most RTEMS ports.  It is a bit mapping in
which the least three significiant bits of the interrupt level
are mapped directly to the enabling of specific interrupt
sources as follows:

*Critical Interrupt*
    Setting bit 0 (the least significant bit) of the interrupt level
    enables the Critical Interrupt source, if it is available on this
    CPU model.

*Machine Check*
    Setting bit 1 of the interrupt level enables Machine Check execptions.

*External Interrupt*
    Setting bit 2 of the interrupt level enables External Interrupt execptions.

All other bits in the RTEMS task interrupt level are ignored.

Default Fatal Error Processing
==============================

The default fatal error handler for this architecture performs the
following actions:

- places the error code in r3, and

- executes a trap instruction which results in a Program Exception.

If the Program Exception returns, then the following actions are performed:

- disables all processor exceptions by loading a 0 into the MSR, and

- goes into an infinite loop to simulate a halt processor instruction.

Symmetric Multiprocessing
=========================

SMP is supported.  Available platforms are the Freescale QorIQ P series (e.g.
P1020) and T series (e.g. T2080, T4240).

Thread-Local Storage
====================

Thread-local storage is supported.

Board Support Packages
======================

System Reset
------------

An RTEMS based application is initiated or
re-initiated when the PowerPC processor is reset.  The PowerPC
architecture defines a Reset Exception, but leaves the
details of the CPU state as implementation specific.  Please
refer to the User’s Manual for the CPU model in question.

In general, at power-up the PowerPC begin execution at address
0xFFF00100 in supervisor mode with all exceptions disabled.  For
soft resets, the CPU will vector to either 0xFFF00100 or 0x00000100
depending upon the setting of the Exception Prefix bit in the MSR.
If during a soft reset, a Machine Check Exception occurs, then the
CPU may execute a hard reset.

Processor Initialization
------------------------

If this PowerPC implementation supports on-chip caching
and this is to be utilized, then it should be enabled during the
reset application initialization code.  On-chip caching has been
observed to prevent some emulators from working properly, so it
may be necessary to run with caching disabled to use these emulators.

In addition to the requirements described in the*Board Support Packages* chapter of the RTEMS C
Applications User’s Manual for the reset code
which is executed before the call to ``rtems_initialize_executive``,
the PowrePC version has the following specific requirements:

- Must leave the PR bit of the Machine State Register (MSR) set
  to 0 so the PowerPC remains in the supervisor state.

- Must set stack pointer (sp or r1) such that a minimum stack
  size of MINIMUM_STACK_SIZE bytes is provided for the RTEMS initialization
  sequence.

- Must disable all external interrupts (i.e. clear the EI (EE)
  bit of the machine state register).

- Must enable traps so window overflow and underflow
  conditions can be properly handled.

- Must initialize the PowerPC’s initial Exception Table with default
  handlers.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

