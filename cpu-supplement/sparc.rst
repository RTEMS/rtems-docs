.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

SPARC Specific Information
**************************

The Real Time Executive for Multiprocessor Systems (RTEMS) is designed to be
portable across multiple processor architectures.  However, the nature of
real-time systems makes it essential that the application designer understand
certain processor dependent implementation details.  These processor
dependencies include calling convention, board support package issues,
interrupt processing, exact RTEMS memory requirements, performance data, header
files, and the assembly language interface to the executive.

This document discusses the SPARC architecture dependencies in this port of
RTEMS.  This architectural port is for SPARC Version 7 and
8. Implementations for SPARC V9 are in the sparc64 target.

It is highly recommended that the SPARC RTEMS application developer obtain and
become familiar with the documentation for the processor being used as well as
the specification for the revision of the SPARC architecture which corresponds
to that processor.

**SPARC Architecture Documents**

For information on the SPARC architecture, refer to the following documents
available from SPARC International, Inc.  (http://www.sparc.com):

- SPARC Standard Version 7.

- SPARC Standard Version 8.

**ERC32 Specific Information**

The European Space Agency's ERC32 is a microprocessor implementing a
SPARC V7 processor and associated support circuitry for embedded space
applications. The integer and floating-point units (90C601E & 90C602E) are
based on the Cypress 7C601 and 7C602, with additional error-detection and
recovery functions. The memory controller (MEC) implements system support
functions such as address decoding, memory interface, DMA interface, UARTs,
timers, interrupt control, write-protection, memory reconfiguration and
error-detection.  The core is designed to work at 25MHz, but using space
qualified memories limits the system frequency to around 15 MHz, resulting in a
performance of 10 MIPS and 2 MFLOPS.

The ERC32 is available from Atmel as the TSC695F.

The RTEMS configuration of GDB enables the SPARC Instruction Simulator (SIS) 
which can simulate the ERC32 as well as the follow up LEON2 and LEON3
microprocessors.

CPU Model Dependent Features
============================

Microprocessors are generally classified into families with a variety of CPU
models or implementations within that family.  Within a processor family, there
is a high level of binary compatibility.  This family may be based on either an
architectural specification or on maintaining compatibility with a popular
processor.  Recent microprocessor families such as the SPARC or PowerPC are
based on an architectural specification which is independent or any particular
CPU model or implementation.  Older families such as the M68xxx and the iX86
evolved as the manufacturer strived to produce higher performance processor
models which maintained binary compatibility with older models.

RTEMS takes advantage of the similarity of the various models within a CPU
family.  Although the models do vary in significant ways, the high level of
compatibility makes it possible to share the bulk of the CPU dependent
executive code across the entire family.

CPU Model Feature Flags
-----------------------

Each processor family supported by RTEMS has a list of features which vary
between CPU models within a family.  For example, the most common model
dependent feature regardless of CPU family is the presence or absence of a
floating point unit or coprocessor.  When defining the list of features present
on a particular CPU model, one simply notes that floating point hardware is or
is not present and defines a single constant appropriately.  Conditional
compilation is utilized to include the appropriate source code for this CPU
model's feature set.  It is important to note that this means that RTEMS is
thus compiled using the appropriate feature set and compilation flags optimal
for this CPU model used.  The alternative would be to generate a binary which
would execute on all family members using only the features which were always
present.

This section presents the set of features which vary across SPARC
implementations and are of importance to RTEMS.  The set of CPU model feature
macros are defined in the file cpukit/score/cpu/sparc/sparc.h based upon the
particular CPU model defined on the compilation command line.

CPU Model Name
~~~~~~~~~~~~~~

The macro CPU_MODEL_NAME is a string which designates the name of this CPU
model.  For example, for the European Space Agency's ERC32 SPARC model, this
macro is set to the string "erc32".

Floating Point Unit
~~~~~~~~~~~~~~~~~~~

The macro SPARC_HAS_FPU is set to 1 to indicate that this CPU model has a
hardware floating point unit and 0 otherwise.

Bitscan Instruction
~~~~~~~~~~~~~~~~~~~

The macro SPARC_HAS_BITSCAN is set to 1 to indicate that this CPU model has the
bitscan instruction.  For example, this instruction is supported by the Fujitsu
SPARClite family.

Number of Register Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~

The macro SPARC_NUMBER_OF_REGISTER_WINDOWS is set to indicate the number of
register window sets implemented by this CPU model.  The SPARC architecture
allows a for a maximum of thirty-two register window sets although most
implementations only include eight.

Low Power Mode
~~~~~~~~~~~~~~

The macro SPARC_HAS_LOW_POWER_MODE is set to one to indicate that this CPU
model has a low power mode.  If low power is enabled, then there must be CPU
model specific implementation of the IDLE task in cpukit/score/cpu/sparc/cpu.c.
The low power mode IDLE task should be of the form:

.. code-block:: c

    while ( TRUE ) {
        enter low power mode
    }

The code required to enter low power mode is CPU model specific.

CPU Model Implementation Notes
------------------------------

The ERC32 is a custom SPARC V7 implementation based on the Cypress 601/602
chipset.  This CPU has a number of on-board peripherals and was developed by
the European Space Agency to target space applications.  RTEMS currently
provides support for the following peripherals:

- UART Channels A and B

- General Purpose Timer

- Real Time Clock

- Watchdog Timer (so it can be disabled)

- Control Register (so powerdown mode can be enabled)

- Memory Control Register

- Interrupt Control

The General Purpose Timer and Real Time Clock Timer provided with the ERC32
share the Timer Control Register.  Because the Timer Control Register is write
only, we must mirror it in software and insure that writes to one timer do not
alter the current settings and status of the other timer.  Routines are
provided in erc32.h which promote the view that the two timers are completely
independent.  By exclusively using these routines to access the Timer Control
Register, the application can view the system as having a General Purpose Timer
Control Register and a Real Time Clock Timer Control Register rather than the
single shared value.

The RTEMS Idle thread take advantage of the low power mode provided by the
ERC32.  Low power mode is entered during idle loops and is enabled at
initialization time.

Calling Conventions
===================

Each high-level language compiler generates subroutine entry and exit code
based upon a set of rules known as the application binary interface (ABI)
calling convention.  These rules address the following issues:

- register preservation and usage

- parameter passing

- call and return mechanism

An ABI calling convention is of importance when interfacing to subroutines
written in another language either assembly or high-level.  It determines also
the set of registers to be saved or restored during a context switch and
interrupt processing.

The ABI relevant for RTEMS on SPARC is defined by SYSTEM V APPLICATION BINARY
INTERFACE, SPARC Processor Supplement, Third Edition.

Programming Model
-----------------

This section discusses the programming model for the SPARC architecture.

Non-Floating Point Registers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SPARC architecture defines thirty-two non-floating point registers directly
visible to the programmer.  These are divided into four sets:

- input registers

- local registers

- output registers

- global registers

Each register is referred to by either two or three names in the SPARC
reference manuals.  First, the registers are referred to as r0 through r31 or
with the alternate notation r[0] through r[31].  Second, each register is a
member of one of the four sets listed above.  Finally, some registers have an
architecturally defined role in the programming model which provides an
alternate name.  The following table describes the mapping between the 32
registers and the register sets:

================ ================ ===================
Register Number  Register Names   Description
================ ================ ===================
0 - 7            g0 - g7          Global Registers
8 - 15           o0 - o7          Output Registers
16 - 23          l0 - l7          Local Registers
24 - 31          i0 - i7          Input Registers
================ ================ ===================

As mentioned above, some of the registers serve defined roles in the
programming model.  The following table describes the role of each of these
registers:

============== ================ ==================================
Register Name  Alternate Name   Description
============== ================ ==================================
g0             na               reads return 0, writes are ignored
o6             sp               stack pointer
i6             fp               frame pointer
i7             na               return address
============== ================ ==================================

The registers g2 through g4 are reserved for applications.  GCC uses them as
volatile registers by default.  So they are treated like volatile registers in
RTEMS as well.

The register g6 is reserved for the operating system and contains the address
of the per-CPU control block of the current processor.  This register is
initialized during system start and then remains unchanged.  It is not
saved/restored by the context switch or interrupt processing code.

The register g7 is reserved for the operating system and contains the thread
pointer used for thread-local storage (TLS) as mandated by the SPARC ABI.

Floating Point Registers
~~~~~~~~~~~~~~~~~~~~~~~~

The SPARC V7 architecture includes thirty-two, thirty-two bit registers.  These
registers may be viewed as follows:

- 32 single precision floating point or integer registers (f0, f1, ... f31)

- 16 double precision floating point registers (f0, f2, f4, ... f30)

- 8 extended precision floating point registers (f0, f4, f8, ... f28)

The floating point status register (FSR) specifies the behavior of the floating
point unit for rounding, contains its condition codes, version specification,
and trap information.

According to the ABI all floating point registers and the floating point status
register (FSR) are volatile.  Thus the floating point context of a thread is
the empty set.  The rounding direction is a system global state and must not be
modified by threads.

A queue of the floating point instructions which have started execution but not
yet completed is maintained.  This queue is needed to support the multiple
cycle nature of floating point operations and to aid floating point exception
trap handlers.  Once a floating point exception has been encountered, the queue
is frozen until it is emptied by the trap handler.  The floating point queue is
loaded by launching instructions.  It is emptied normally when the floating
point completes all outstanding instructions and by floating point exception
handlers with the store double floating point queue (stdfq) instruction.

Special Registers
~~~~~~~~~~~~~~~~~

The SPARC architecture includes two special registers which are critical to the
programming model: the Processor State Register (psr) and the Window Invalid
Mask (wim).  The psr contains the condition codes, processor interrupt level,
trap enable bit, supervisor mode and previous supervisor mode bits, version
information, floating point unit and coprocessor enable bits, and the current
window pointer (cwp).  The cwp field of the psr and wim register are used to
manage the register windows in the SPARC architecture.  The register windows
are discussed in more detail below.

Register Windows
----------------

The SPARC architecture includes the concept of register windows.  An overly
simplistic way to think of these windows is to imagine them as being an
infinite supply of "fresh" register sets available for each subroutine to use.
In reality, they are much more complicated.

The save instruction is used to obtain a new register window.  This instruction
decrements the current window pointer, thus providing a new set of registers
for use.  This register set includes eight fresh local registers for use
exclusively by this subroutine.  When done with a register set, the restore
instruction increments the current window pointer and the previous register set
is once again available.

The two primary issues complicating the use of register windows are that (1)
the set of register windows is finite, and (2) some registers are shared
between adjacent registers windows.

Because the set of register windows is finite, it is possible to execute enough
save instructions without corresponding restore's to consume all of the
register windows.  This is easily accomplished in a high level language because
each subroutine typically performs a save instruction upon entry.  Thus having
a subroutine call depth greater than the number of register windows will result
in a window overflow condition.  The window overflow condition generates a trap
which must be handled in software.  The window overflow trap handler is
responsible for saving the contents of the oldest register window on the
program stack.

Similarly, the subroutines will eventually complete and begin to perform
restore's.  If the restore results in the need for a register window which has
previously been written to memory as part of an overflow, then a window
underflow condition results.  Just like the window overflow, the window
underflow condition must be handled in software by a trap handler.  The window
underflow trap handler is responsible for reloading the contents of the
register window requested by the restore instruction from the program stack.

The Window Invalid Mask (wim) and the Current Window Pointer (cwp) field in the
psr are used in conjunction to manage the finite set of register windows and
detect the window overflow and underflow conditions.  The cwp contains the
index of the register window currently in use.  The save instruction decrements
the cwp modulo the number of register windows.  Similarly, the restore
instruction increments the cwp modulo the number of register windows.  Each bit
in the wim represents represents whether a register window contains valid
information.  The value of 0 indicates the register window is valid and 1
indicates it is invalid.  When a save instruction causes the cwp to point to a
register window which is marked as invalid, a window overflow condition
results.  Conversely, the restore instruction may result in a window underflow
condition.

Other than the assumption that a register window is always available for trap
(i.e. interrupt) handlers, the SPARC architecture places no limits on the
number of register windows simultaneously marked as invalid (i.e. number of
bits set in the wim).  However, RTEMS assumes that only one register window is
marked invalid at a time (i.e. only one bit set in the wim).  This makes the
maximum possible number of register windows available to the user while still
meeting the requirement that window overflow and underflow conditions can be
detected.

The window overflow and window underflow trap handlers are a critical part of
the run-time environment for a SPARC application.  The SPARC architectural
specification allows for the number of register windows to be any power of two
less than or equal to 32.  The most common choice for SPARC implementations
appears to be 8 register windows.  This results in the cwp ranging in value
from 0 to 7 on most implementations.

The second complicating factor is the sharing of registers between adjacent
register windows.  While each register window has its own set of local
registers, the input and output registers are shared between adjacent windows.
The output registers for register window N are the same as the input registers
for register window ((N - 1) modulo RW) where RW is the number of register
windows.  An alternative way to think of this is to remember how parameters are
passed to a subroutine on the SPARC.  The caller loads values into what are its
output registers.  Then after the callee executes a save instruction, those
parameters are available in its input registers.  This is a very efficient way
to pass parameters as no data is actually moved by the save or restore
instructions.

Call and Return Mechanism
-------------------------

The SPARC architecture supports a simple yet effective call and return
mechanism.  A subroutine is invoked via the call (call) instruction.  This
instruction places the return address in the caller's output register 7 (o7).
After the callee executes a save instruction, this value is available in input
register 7 (i7) until the corresponding restore instruction is executed.

The callee returns to the caller via a jmp to the return address.  There is a
delay slot following this instruction which is commonly used to execute a
restore instruction - if a register window was allocated by this subroutine.

It is important to note that the SPARC subroutine call and return mechanism
does not automatically save and restore any registers.  This is accomplished
via the save and restore instructions which manage the set of registers
windows.

In case a floating-point unit is supported, then floating-point return values
appear in the floating-point registers.  Single-precision values occupy %f0;
double-precision values occupy %f0 and %f1.  Otherwise, these are scratch
registers.  Due to this the hardware and software floating-point ABIs are
incompatible.

Calling Mechanism
-----------------

All RTEMS directives are invoked using the regular SPARC calling convention via
the call instruction.

Register Usage
--------------

As discussed above, the call instruction does not automatically save any
registers.  The save and restore instructions are used to allocate and
deallocate register windows.  When a register window is allocated, the new set
of local registers are available for the exclusive use of the subroutine which
allocated this register set.

Parameter Passing
-----------------

RTEMS assumes that arguments are placed in the caller's output registers with
the first argument in output register 0 (o0), the second argument in output
register 1 (o1), and so forth.  Until the callee executes a save instruction,
the parameters are still visible in the output registers.  After the callee
executes a save instruction, the parameters are visible in the corresponding
input registers.  The following pseudo-code illustrates the typical sequence
used to call a RTEMS directive with three (3) arguments:

.. code-block:: c

    load third argument into o2
    load second argument into o1
    load first argument into o0
    invoke directive

User-Provided Routines
----------------------

All user-provided routines invoked by RTEMS, such as user extensions, device
drivers, and MPCI routines, must also adhere to these calling conventions.

Memory Model
============

A processor may support any combination of memory models ranging from pure
physical addressing to complex demand paged virtual memory systems.  RTEMS
supports a flat memory model which ranges contiguously over the processor's
allowable address space.  RTEMS does not support segmentation or virtual memory
of any kind.  The appropriate memory model for RTEMS provided by the targeted
processor and related characteristics of that model are described in this
chapter.

Flat Memory Model
-----------------

The SPARC architecture supports a flat 32-bit address space with addresses
ranging from 0x00000000 to 0xFFFFFFFF (4 gigabytes).  Each address is
represented by a 32-bit value and is byte addressable.  The address may be used
to reference a single byte, half-word (2-bytes), word (4 bytes), or doubleword
(8 bytes).  Memory accesses within this address space are performed in big
endian fashion by the SPARC.  Memory accesses which are not properly aligned
generate a "memory address not aligned" trap (type number 7).  The following
table lists the alignment requirements for a variety of data accesses:

==============  ======================
Data Type       Alignment Requirement
==============  ======================
byte            1
half-word       2
word            4
doubleword      8
==============  ======================

Doubleword load and store operations must use a pair of registers as their
source or destination.  This pair of registers must be an adjacent pair of
registers with the first of the pair being even numbered.  For example, a valid
destination for a doubleword load might be input registers 0 and 1 (i0 and i1).
The pair i1 and i2 would be invalid.  \[NOTE: Some assemblers for the SPARC do
not generate an error if an odd numbered register is specified as the beginning
register of the pair.  In this case, the assembler assumes that what the
programmer meant was to use the even-odd pair which ends at the specified
register.  This may or may not have been a correct assumption.]

RTEMS does not support any SPARC Memory Management Units, therefore, virtual
memory or segmentation systems involving the SPARC are not supported.

Interrupt Processing
====================

Different types of processors respond to the occurrence of an interrupt in its
own unique fashion. In addition, each processor type provides a control
mechanism to allow for the proper handling of an interrupt.  The processor
dependent response to the interrupt modifies the current execution state and
results in a change in the execution stream.  Most processors require that an
interrupt handler utilize some special control mechanisms to return to the
normal processing stream.  Although RTEMS hides many of the processor dependent
details of interrupt processing, it is important to understand how the RTEMS
interrupt manager is mapped onto the processor's unique architecture. Discussed
in this chapter are the SPARC's interrupt response and control mechanisms as
they pertain to RTEMS.

RTEMS and associated documentation uses the terms interrupt and vector.  In the
SPARC architecture, these terms correspond to traps and trap type,
respectively.  The terms will be used interchangeably in this manual.

Synchronous Versus Asynchronous Traps
-------------------------------------

The SPARC architecture includes two classes of traps: synchronous and
asynchronous.  Asynchronous traps occur when an external event interrupts the
processor.  These traps are not associated with any instruction executed by the
processor and logically occur between instructions.  The instruction currently
in the execute stage of the processor is allowed to complete although
subsequent instructions are annulled.  The return address reported by the
processor for asynchronous traps is the pair of instructions following the
current instruction.

Synchronous traps are caused by the actions of an instruction.  The trap
stimulus in this case either occurs internally to the processor or is from an
external signal that was provoked by the instruction.  These traps are taken
immediately and the instruction that caused the trap is aborted before any
state changes occur in the processor itself.  The return address reported by
the processor for synchronous traps is the instruction which caused the trap
and the following instruction.

Vectoring of Interrupt Handler
------------------------------

Upon receipt of an interrupt the SPARC automatically performs the following
actions:

- disables traps (sets the ET bit of the psr to 0),

- the S bit of the psr is copied into the Previous Supervisor Mode (PS) bit of
  the psr,

- the cwp is decremented by one (modulo the number of register windows) to
  activate a trap window,

- the PC and nPC are loaded into local register 1 and 2 (l0 and l1),

- the trap type (tt) field of the Trap Base Register (TBR) is set to the
  appropriate value, and

- if the trap is not a reset, then the PC is written with the contents of the
  TBR and the nPC is written with TBR + 4.  If the trap is a reset, then the PC
  is set to zero and the nPC is set to 4.

Trap processing on the SPARC has two features which are noticeably different
than interrupt processing on other architectures.  First, the value of psr
register in effect immediately before the trap occurred is not explicitly
saved.  Instead only reversible alterations are made to it.  Second, the
Processor Interrupt Level (pil) is not set to correspond to that of the
interrupt being processed.  When a trap occurs, ALL subsequent traps are
disabled.  In order to safely invoke a subroutine during trap handling, traps
must be enabled to allow for the possibility of register window overflow and
underflow traps.

If the interrupt handler was installed as an RTEMS interrupt handler, then upon
receipt of the interrupt, the processor passes control to the RTEMS interrupt
handler which performs the following actions:

- saves the state of the interrupted task on it's stack,

- insures that a register window is available for subsequent traps,

- if this is the outermost (i.e. non-nested) interrupt, then the RTEMS
  interrupt handler switches from the current stack to the interrupt stack,

- enables traps,

- invokes the vectors to a user interrupt service routine (ISR).

Asynchronous interrupts are ignored while traps are disabled.  Synchronous
traps which occur while traps are disabled result in the CPU being forced into
an error mode.

A nested interrupt is processed similarly with the exception that the current
stack need not be switched to the interrupt stack.

Traps and Register Windows
--------------------------

One of the register windows must be reserved at all times for trap processing.
This is critical to the proper operation of the trap mechanism in the SPARC
architecture.  It is the responsibility of the trap handler to insure that
there is a register window available for a subsequent trap before re-enabling
traps.  It is likely that any high level language routines invoked by the trap
handler (such as a user-provided RTEMS interrupt handler) will allocate a new
register window.  The save operation could result in a window overflow trap.
This trap cannot be correctly processed unless (1) traps are enabled and (2) a
register window is reserved for traps.  Thus, the RTEMS interrupt handler
insures that a register window is available for subsequent traps before
enabling traps and invoking the user's interrupt handler.

Interrupt Levels
----------------

Sixteen levels (0-15) of interrupt priorities are supported by the SPARC
architecture with level fifteen (15) being the highest priority.  Level
zero (0) indicates that interrupts are fully enabled.  Interrupt requests for
interrupts with priorities less than or equal to the current interrupt mask
level are ignored. Level fifteen (15) is a non-maskable interrupt (NMI), which
makes it unsuitable for standard usage since it can affect the real-time
behaviour by interrupting critical sections and spinlocks. Disabling traps
stops also the NMI interrupt from happening. It can however be used for
power-down or other critical events.

Although RTEMS supports 256 interrupt levels, the SPARC only supports sixteen.
RTEMS interrupt levels 0 through 15 directly correspond to SPARC processor
interrupt levels.  All other RTEMS interrupt levels are undefined and their
behavior is unpredictable.

Many LEON SPARC v7/v8 systems features an extended interrupt controller which
adds an extra step of interrupt decoding to allow handling of interrupt
16-31. When such an extended interrupt is generated the CPU traps into a
specific interrupt trap level 1-14 and software reads out from the interrupt
controller which extended interrupt source actually caused the interrupt.

Disabling of Interrupts by RTEMS
--------------------------------

During the execution of directive calls, critical sections of code may be
executed.  When these sections are encountered, RTEMS disables interrupts to
level fifteen (15) before the execution of the section and restores them to the
previous level upon completion of the section.  RTEMS has been optimized to
ensure that interrupts are disabled for less than RTEMS_MAXIMUM_DISABLE_PERIOD
microseconds on a RTEMS_MAXIMUM_DISABLE_PERIOD_MHZ Mhz ERC32 with zero wait
states.  These numbers will vary based the number of wait states and processor
speed present on the target board.  [NOTE: The maximum period with interrupts
disabled is hand calculated.  This calculation was last performed for Release
RTEMS_RELEASE_FOR_MAXIMUM_DISABLE_PERIOD.]

[NOTE: It is thought that the length of time at which the processor interrupt
level is elevated to fifteen by RTEMS is not anywhere near as long as the
length of time ALL traps are disabled as part of the "flush all register
windows" operation.]

Non-maskable interrupts (NMI) cannot be disabled, and ISRs which execute at
this level MUST NEVER issue RTEMS system calls.  If a directive is invoked,
unpredictable results may occur due to the inability of RTEMS to protect its
critical sections.  However, ISRs that make no system calls may safely execute
as non-maskable interrupts.

Interrupts are disabled or enabled by performing a system call to the Operating
System reserved software traps 9 (SPARC_SWTRAP_IRQDIS) or 10
(SPARC_SWTRAP_IRQEN). The trap is generated by the software trap (Ticc)
instruction or indirectly by calling sparc_disable_interrupts() or
sparc_enable_interrupts() functions. Disabling interrupts return the previous
interrupt level (on trap entry) in register G1 and sets PSR.PIL to 15 to
disable all maskable interrupts. The interrupt level can be restored by
trapping into the enable interrupt handler with G1 containing the new interrupt
level.

Interrupt Stack
---------------

The SPARC architecture does not provide for a dedicated interrupt stack.  Thus
by default, trap handlers would execute on the stack of the RTEMS task which
they interrupted.  This artificially inflates the stack requirements for each
task since EVERY task stack would have to include enough space to account for
the worst case interrupt stack requirements in addition to it's own worst case
usage.  RTEMS addresses this problem on the SPARC by providing a dedicated
interrupt stack managed by software.

During system initialization, RTEMS allocates the interrupt stack from the
Workspace Area.  The amount of memory allocated for the interrupt stack is
determined by the interrupt_stack_size field in the CPU Configuration Table.
As part of processing a non-nested interrupt, RTEMS will switch to the
interrupt stack before invoking the installed handler.

Default Fatal Error Processing
==============================

Upon detection of a fatal error by either the application or RTEMS the fatal
error manager is invoked.  The fatal error manager will invoke the
user-supplied fatal error handlers.  If no user-supplied handlers are
configured, the RTEMS provided default fatal error handler is invoked.  If the
user-supplied fatal error handlers return to the executive the default fatal
error handler is then invoked.  This chapter describes the precise operations
of the default fatal error handler.

Default Fatal Error Handler Operations
--------------------------------------

The default fatal error handler which is invoked by the fatal_error_occurred
directive when there is no user handler configured or the user handler returns
control to RTEMS.

If the BSP has been configured with ``BSP_POWER_DOWN_AT_FATAL_HALT`` set to
true, the default handler will disable interrupts and enter power down mode. If
power down mode is not available, it goes into an infinite loop to simulate a
halt processor instruction.

If ``BSP_POWER_DOWN_AT_FATAL_HALT`` is set to false, the default handler will
place the value ``1`` in register ``g1``, the error source in register ``g2``,
and the error code in register``g3``. It will then generate a system error
which will hand over control to the debugger, simulator, etc.

Symmetric Multiprocessing
=========================

SMP is supported.  Available platforms are the Cobham Gaisler GR712RC and
GR740.

Thread-Local Storage
====================

Thread-local storage is supported.

Board Support Packages
======================

An RTEMS Board Support Package (BSP) must be designed to support a particular
processor and target board combination.  This chapter presents a discussion of
SPARC specific BSP issues.  For more information on developing a BSP, refer to
the chapter titled Board Support Packages in the RTEMS Applications User's
Guide.

System Reset
------------

An RTEMS based application is initiated or re-initiated when the SPARC
processor is reset.  When the SPARC is reset, the processor performs the
following actions:

- the enable trap (ET) of the psr is set to 0 to disable traps,

- the supervisor bit (S) of the psr is set to 1 to enter supervisor mode, and

- the PC is set 0 and the nPC is set to 4.

The processor then begins to execute the code at location 0.  It is important
to note that all fields in the psr are not explicitly set by the above steps
and all other registers retain their value from the previous execution mode.
This is true even of the Trap Base Register (TBR) whose contents reflect the
last trap which occurred before the reset.

Processor Initialization
------------------------

It is the responsibility of the application's initialization code to initialize
the TBR and install trap handlers for at least the register window overflow and
register window underflow conditions.  Traps should be enabled before invoking
any subroutines to allow for register window management.  However, interrupts
should be disabled by setting the Processor Interrupt Level (pil) field of the
psr to 15.  RTEMS installs it's own Trap Table as part of initialization which
is initialized with the contents of the Trap Table in place when the
``rtems_initialize_executive`` directive was invoked.  Upon completion of
executive initialization, interrupts are enabled.

If this SPARC implementation supports on-chip caching and this is to be
utilized, then it should be enabled during the reset application initialization
code.

In addition to the requirements described in the Board Support Packages chapter
of the C Applications Users Manual for the reset code which is executed before
the call to``rtems_initialize_executive``, the SPARC version has the following
specific requirements:

- Must leave the S bit of the status register set so that the SPARC remains in
  the supervisor state.

- Must set stack pointer (sp) such that a minimum stack size of
  MINIMUM_STACK_SIZE bytes is provided for the``rtems_initialize_executive``
  directive.

- Must disable all external interrupts (i.e. set the pil to 15).

- Must enable traps so window overflow and underflow conditions can be properly
  handled.

- Must initialize the SPARC's initial trap table with at least trap handlers
  for register window overflow and register window underflow.

....................................
.... 

Understanding stacks and registers in the SPARC architecture(s)
===============================================================

The content in this section originally appeared at
https://www.sics.se/~psm/sparcstack.html. It appears here with the
gracious permission of the author Peter Magnusson.


The SPARC architecture from Sun Microsystems has some "interesting"
characteristics. After having to deal with both compiler, interpreter, OS
emulator, and OS porting issues for the SPARC, I decided to gather notes
and documentation in one place. If there are any issues you don't find
addressed by this page, or if you know of any similar Net resources, let
me know. This document is limited to the V8 version of the architecture.

General Structure
-----------------

SPARC has 32 general purpose integer registers visible to the program
at any given time. Of these, 8 registers are global registers and 24
registers are in a register window. A window consists of three groups
of 8 registers, the out, local, and in registers. See table 1. A SPARC
implementation can have from 2 to 32 windows, thus varying the number
of registers from 40 to 520. Most implentations have 7 or 8 windows. The
variable number of registers is the principal reason for the SPARC being
"scalable".

At any given time, only one window is visible, as determined by the
current window pointer (CWP) which is part of the processor status
register (PSR). This is a five bit value that can be decremented or
incremented by the SAVE and RESTORE instructions, respectively. These
instructions are generally executed on procedure call and return
(respectively). The idea is that the in registers contain incoming
parameters, the local register constitute scratch registers, the out
registers contain outgoing parameters, and the global registers contain
values that vary little between executions. The register windows overlap
partially, thus the out registers become renamed by SAVE to become the in
registers of the called procedure. Thus, the memory traffic is reduced
when going up and down the procedure call. Since this is a frequent
operation, performance is improved.

(That was the idea, anyway. The drawback is that upon interactions
with the system the registers need to be flushed to the stack,
necessitating a long sequence of writes to memory of data that is
often mostly garbage. Register windows was a bad idea that was caused
by simulation studies that considered only programs in isolation, as
opposed to multitasking workloads, and by considering compilers with
poor optimization. It also caused considerable problems in implementing
high-end SPARC processors such as the SuperSPARC, although more recent
implementations have dealt effectively with the obstacles. Register
windows is now part of the compatibility legacy and not easily removed
from the architecture.)

================ ======== ================
Register  Group  Mnemonic Register Address
================ ======== ================
global           %g0-%g7  r[0]-r[7]
out              %o0-%o7  r[8]-r[15]
local            %l0-%l7  r[16]-r[23]
in               %i0-%i7  r[24]-r[31]
================ ======== ================

.. Table 1 - Visible Registers

The overlap of the registers is illustrated in figure 1. The figure
shows an implementation with 8 windows, numbered 0 to 7 (labeled w0 to
w7 in the figure).. Each window corresponds to 24 registers, 16 of which
are shared with "neighboring" windows. The windows are arranged in a
wrap-around manner, thus window number 0 borders window number 7. The
common cause of changing the current window, as pointed to by CWP, is
the RESTORE and SAVE instuctions, shown in the middle. Less common is
the supervisor RETT instruction (return from trap) and the trap event
(interrupt, exception, or TRAP instruction).


.. image:: sparcwin.gif

Figure 1 - Windowed Registers

The "WIM" register is also indicated in the top left of figure 1. The
window invalid mask is a bit map of valid windows. It is generally used
as a pointer, i.e. exactly one bit is set in the WIM register indicating
which window is invalid (in the figure it's window 7). Register windows
are generally used to support procedure calls, so they can be viewed
as a cache of the stack contents. The WIM "pointer" indicates how
many procedure calls in a row can be taken without writing out data to
memory. In the figure, the capacity of the register windows is fully
utilized. An additional call will thus exceed capacity, triggering a
window overflow trap. At the other end, a window underflow trap occurs
when the register window "cache" if empty and more data needs to be
fetched from memory.

Register Semantics
------------------

phe SPARC Architecture includes recommended software semantics. These are
described in the architecture manual, the SPARC ABI (application binary
interface) standard, and, unfortunately, in various other locations as
well (including header files and compiler documentation).

Figure 2 shows a summary of register contents at any given time.

.. code-block:: asm

                 %g0  (r00)       always zero
                 %g1  (r01)  [1]  temporary value
                 %g2  (r02)  [2]  global 2
     global      %g3  (r03)  [2]  global 3
                 %g4  (r04)  [2]  global 4
                 %g5  (r05)       reserved for SPARC ABI
                 %g6  (r06)       reserved for SPARC ABI
                 %g7  (r07)       reserved for SPARC ABI

                 %o0  (r08)  [3]  outgoing parameter 0 / return value from callee   
                 %o1  (r09)  [1]  outgoing parameter 1
                 %o2  (r10)  [1]  outgoing parameter 2
     out         %o3  (r11)  [1]  outgoing parameter 3
                 %o4  (r12)  [1]  outgoing parameter 4
                 %o5  (r13)  [1]  outgoing parameter 5
            %sp, %o6  (r14)  [1]  stack pointer
                 %o7  (r15)  [1]  temporary value / address of CALL instruction

                 %l0  (r16)  [3]  local 0
                 %l1  (r17)  [3]  local 1
                 %l2  (r18)  [3]  local 2
     local       %l3  (r19)  [3]  local 3
                 %l4  (r20)  [3]  local 4
                 %l5  (r21)  [3]  local 5
                 %l6  (r22)  [3]  local 6
                 %l7  (r23)  [3]  local 7

                 %i0  (r24)  [3]  incoming parameter 0 / return value to caller
                 %i1  (r25)  [3]  incoming parameter 1
                 %i2  (r26)  [3]  incoming parameter 2
     in          %i3  (r27)  [3]  incoming parameter 3
                 %i4  (r28)  [3]  incoming parameter 4
                 %i5  (r29)  [3]  incoming parameter 5
            %fp, %i6  (r30)  [3]  frame pointer
                 %i7  (r31)  [3]  return address - 8

Notes:

# assumed by caller to be destroyed (volatile) across a procedure call

# should not be used by SPARC ABI library code

# assumed by caller to be preserved across a procedure call

.. Above was Figure 2 - SPARC register semantics

Particular compilers are likely to vary slightly.

Note that globals %g2-%g4 are reserved for the "application", which
includes libraries and compiler. Thus, for example, libraries may
overwrite these registers unless they've been compiled with suitable
flags. Also, the "reserved" registers are presumed to be allocated
(in the future) bottom-up, i.e. %g7 is currently the "safest" to use.

Optimizing linkers and interpreters are exmples that use global registers.

Register Windows and the Stack
------------------------------

The SPARC register windows are, naturally, intimately related to the
stack. In particular, the stack pointer (%sp or %o6) must always point
to a free block of 64 bytes. This area is used by the operating system
(Solaris, SunOS, and Linux at least) to save the current local and in
registers upon a system interupt, exception, or trap instruction. (Note
that this can occur at any time.)

Other aspects of register relations with memory are programming
convention. The typical, and recommended, layout of the stack is shown
in figure 3. The figure shows a stack frame.

.. code-block:: asm
                    low addresses
               +-------------------------+         
     %sp  -->  | 16 words for storing    |
               | LOCAL and IN registers  |
               +-------------------------+
               |  one-word pointer to    |
               | aggregate return value  |
               +-------------------------+
               |   6 words for callee    |
               |   to store register     |
               |       arguments         |
               +-------------------------+
               |  outgoing parameters    |
               |  past the 6th, if any   |
               +-------------------------+
               |  space, if needed, for  |
               |  compiler temporaries   |
               |   and saved floating-   |
               |    point registers      |
               +-------------------------+
                    .................
               +-------------------------+
               |    space dynamically    |
               |    allocated via the    |
               |  alloca() library call  |
               +-------------------------+
               |  space, if needed, for  |
               |    automatic arrays,    |
               |    aggregates, and      |
               |   addressable scalar    |
               |       automatics        |
               +-------------------------+
    %fp  -->
                     high addresses

.. Figure 3 - Stack frame contents

Note that the top boxes of figure 3 are addressed via the stack pointer
(%sp), as positive offsets (including zero), and the bottom boxes are
accessed over the frame pointer using negative offsets (excluding zero),
and that the frame pointer is the old stack pointer. This scheme allows
the separation of information known at compile time (number and size
of local parameters, etc) from run-time information (size of blocks
allocated by alloca()).

"addressable scalar automatics" is a fancy name for local variables.

The clever nature of the stack and frame pointers are that they are always
16 registers apart in the register windows. Thus, a SAVE instruction will
make the current stack pointer into the frame pointer and, since the SAVE
instruction also doubles as an ADD, create a new stack pointer. Figure 4
illustrates what the top of a stack might look like during execution. (The
listing is from the "pwin" command in the SimICS simulator.)

.. code-block:: asm

                  REGISTER WINDOWS
                 +--+---+----------+
                 |g0|r00|0x00000000| global
                 |g1|r01|0x00000006| registers
                 |g2|r02|0x00091278|
      g0-g7      |g3|r03|0x0008ebd0|
                 |g4|r04|0x00000000|        (note: 'save' and 'trap' decrements CWP,
                 |g5|r05|0x00000000|        i.e. moves it up on this diagram. 'restore'
                 |g6|r06|0x00000000|        and 'rett' increments CWP, i.e. down)
                 |g7|r07|0x00000000|
                 +--+---+----------+
 CWP (2)         |o0|r08|0x00000002|
                 |o1|r09|0x00000000|                            MEMORY
                 |o2|r10|0x00000001|
      o0-o7      |o3|r11|0x00000001|             stack growth
                 |o4|r12|0x000943d0|
                 |o5|r13|0x0008b400|                  ^
                 |sp|r14|0xdffff9a0| ----\           /|\
                 |o7|r15|0x00062abc|     |            |                     addresses
                 +--+---+----------+     |     +--+----------+         virtual     physical
                 |l0|r16|0x00087c00|     \---> |l0|0x00000000|        0xdffff9a0  0x000039a0  top of frame 0   
                 |l1|r17|0x00027fd4|           |l1|0x00000000|        0xdffff9a4  0x000039a4
                 |l2|r18|0x00000000|           |l2|0x0009df80|        0xdffff9a8  0x000039a8
      l0-l7      |l3|r19|0x00000000|           |l3|0x00097660|        0xdffff9ac  0x000039ac
                 |l4|r20|0x00000000|           |l4|0x00000014|        0xdffff9b0  0x000039b0
                 |l5|r21|0x00097678|           |l5|0x00000001|        0xdffff9b4  0x000039b4
                 |l6|r22|0x0008b400|           |l6|0x00000004|        0xdffff9b8  0x000039b8
                 |l7|r23|0x0008b800|           |l7|0x0008dd60|        0xdffff9bc  0x000039bc
              +--+--+---+----------+           +--+----------+
 CWP+1 (3)    |o0|i0|r24|0x00000002|           |i0|0x00091048|        0xdffff9c0  0x000039c0
              |o1|i1|r25|0x00000000|           |i1|0x00000011|        0xdffff9c4  0x000039c4
              |o2|i2|r26|0x0008b7c0|           |i2|0x00091158|        0xdffff9c8  0x000039c8
      i0-i7   |o3|i3|r27|0x00000019|           |i3|0x0008d370|        0xdffff9cc  0x000039cc
              |o4|i4|r28|0x0000006c|           |i4|0x0008eac4|        0xdffff9d0  0x000039d0
              |o5|i5|r29|0x00000000|           |i5|0x00000000|        0xdffff9d4  0x000039d4
              |o6|fp|r30|0xdffffa00| ----\     |fp|0x00097660|        0xdffff9d8  0x000039d8
              |o7|i7|r31|0x00040468|     |     |i7|0x00000000|        0xdffff9dc  0x000039dc
              +--+--+---+----------+     |     +--+----------+
                                         |        |0x00000001|        0xdffff9e0  0x000039e0  parameters
                                         |        |0x00000002|        0xdffff9e4  0x000039e4
                                         |        |0x00000040|        0xdffff9e8  0x000039e8
                                         |        |0x00097671|        0xdffff9ec  0x000039ec
                                         |        |0xdffffa68|        0xdffff9f0  0x000039f0
                                         |        |0x00024078|        0xdffff9f4  0x000039f4
                                         |        |0x00000004|        0xdffff9f8  0x000039f8
                                         |        |0x0008dd60|        0xdffff9fc  0x000039fc
              +--+------+----------+     |     +--+----------+
              |l0|      |0x00087c00|     \---> |l0|0x00091048|        0xdffffa00  0x00003a00  top of frame 1
              |l1|      |0x000c8d48|           |l1|0x0000000b|        0xdffffa04  0x00003a04
              |l2|      |0x000007ff|           |l2|0x00091158|        0xdffffa08  0x00003a08
              |l3|      |0x00000400|           |l3|0x000c6f10|        0xdffffa0c  0x00003a0c
              |l4|      |0x00000000|           |l4|0x0008eac4|        0xdffffa10  0x00003a10
              |l5|      |0x00088000|           |l5|0x00000000|        0xdffffa14  0x00003a14
              |l6|      |0x0008d5e0|           |l6|0x000c6f10|        0xdffffa18  0x00003a18
              |l7|      |0x00088000|           |l7|0x0008cd00|        0xdffffa1c  0x00003a1c
              +--+--+---+----------+           +--+----------+
 CWP+2 (4)    |i0|o0|   |0x00000002|           |i0|0x0008cb00|        0xdffffa20  0x00003a20
              |i1|o1|   |0x00000011|           |i1|0x00000003|        0xdffffa24  0x00003a24
              |i2|o2|   |0xffffffff|           |i2|0x00000040|        0xdffffa28  0x00003a28
              |i3|o3|   |0x00000000|           |i3|0x0009766b|        0xdffffa2c  0x00003a2c
              |i4|o4|   |0x00000000|           |i4|0xdffffa68|        0xdffffa30  0x00003a30
              |i5|o5|   |0x00064c00|           |i5|0x000253d8|        0xdffffa34  0x00003a34
              |i6|o6|   |0xdffffa70| ----\     |i6|0xffffffff|        0xdffffa38  0x00003a38
              |i7|o7|   |0x000340e8|     |     |i7|0x00000000|        0xdffffa3c  0x00003a3c
              +--+--+---+----------+     |     +--+----------+
                                         |        |0x00000001|        0xdffffa40  0x00003a40  parameters
                                         |        |0x00000000|        0xdffffa44  0x00003a44
                                         |        |0x00000000|        0xdffffa48  0x00003a48
                                         |        |0x00000000|        0xdffffa4c  0x00003a4c
                                         |        |0x00000000|        0xdffffa50  0x00003a50
                                         |        |0x00000000|        0xdffffa54  0x00003a54
                                         |        |0x00000002|        0xdffffa58  0x00003a58
                                         |        |0x00000002|        0xdffffa5c  0x00003a5c
                                         |        |    .     |
                                         |        |    .     |        .. etc (another 16 bytes)
                                         |        |    .     |

.. Figure 4 - Sample stack contents

Note how the stack contents are not necessarily synchronized with the
registers. Various events can cause the register windows to be "flushed"
to memory, including most system calls. A programmer can force this
update by using ST_FLUSH_WINDOWS trap, which also reduces the number of
valid windows to the minimum of 1.

Writing a library for multithreaded execution is an example that requires
explicit flushing, as is longjmp().

Procedure epilogue and prologue
-------------------------------

The stack frame described in the previous section leads to the standard
entry/exit mechanisms listed in figure 5.

.. code-block:: asm

  function:
    save  %sp, -C, %sp

               ; perform function, leave return value,   
               ; if any, in register %i0 upon exit

    ret        ; jmpl %i7+8, %g0
    restore    ; restore %g0,%g0,%g0

.. Figure 5 - Epilogue/prologue in procedures
The SAVE instruction decrements the CWP, as discussed earlier, and also
performs an addition. The constant "C" that is used in the figure to
indicate the amount of space to make on the stack, and thus corresponds
to the frame contents in Figure 3. The minimum is therefore the 16 words
for the LOCAL and IN registers, i.e. (hex) 0x40 bytes.

A confusing element of the SAVE instruction is that the source operands
(the first two parameters) are read from the old register window, and
the destination operand (the rightmost parameter) is written to the new
window. Thus, allthough "%sp" is indicated as both source and destination,
the result is actually written into the stack pointer of the new window
(the source stack pointer becomes renamed and is now the frame pointer).

The return instructions are also a bit particular. ret is a synthetic
instruction, corresponding to jmpl (jump linked). This instruction
jumps to the address resulting from adding 8 to the %i7 register. The
source instruction address (the address of the ret instruction itself)
is written to the %g0 register, i.e. it is discarded.

The restore instruction is similarly a synthetic instruction, and is
just a short form for a restore that choses not to perform an addition.

The calling instruction, in turn, typically looks as follows:

.. code-block:: asm

    call <function>    ; jmpl <address>, %o7
    mov 0, %o0

Again, the call instruction is synthetic, and is actually the same
instruction that performs the return. This time, however, it is interested
in saving the return address, into register %o7. Note that the delay
slot is often filled with an instruction related to the parameters,
in this example it sets the first parameter to zero.
Note also that the return value is also generally passed in %o0.

Leaf procedures are different. A leaf procedure is an optimization that
reduces unnecessary work by taking advantage of the knowledge that no
call instructions exist in many procedures. Thus, the save/restore couple
can be eliminated. The downside is that such a procedure may only use
the out registers (since the in and local registers actually belong to
the caller). See Figure 6.

.. code-block:: asm

  function:
               ; no save instruction needed upon entry

               ; perform function, leave return value,   
               ; if any, in register %o0 upon exit

    retl       ; jmpl %o7+8, %g0
    nop        ; the delay slot can be used for something else   

.. Figure 6 - Epilogue/prologue in leaf procedures

Note in the figure that there is only one instruction overhead, namely the
retl instruction. retl is also synthetic (return from leaf subroutine), is
again a variant of the jmpl instruction, this time with %o7+8 as target.

Yet another variation of epilogue is caused by tail call elimination,
an optimization supported by some compilers (including Sun's C compiler
but not GCC). If the compiler detects that a called function will return
to the calling function, it can replace its place on the stack with the
called function. Figure 7 contains an example.

.. code-block:: asm

       int
        foo(int n)
      {
        if (n == 0)
          return 0;
        else
          return bar(n);
      }
         cmp     %o0,0
        bne     .L1
        or      %g0,%o7,%g1
        retl
        or      %g0,0,%o0
  .L1:  call    bar
        or      %g0,%g1,%o7

.. Figure 7 - Example of tail call elimination

Note that the call instruction overwrites register %o7 with the program
counter. Therefore the above code saves the old value of %o7, and restores
it in the delay slot of the call instruction. If the function call is
register indirect, this twiddling with %o7 can be avoided, but of course
that form of call is slower on modern processors.

The benefit of tail call elimination is to remove an indirection upon
return. It is also needed to reduce register window usage, since otherwise
the foo() function in Figure 7 would need to allocate a stack frame to
save the program counter.

A special form of tail call elimination is tail recursion elimination,
which detects functions calling themselves, and replaces it with a simple
branch. Figure 8 contains an example.

.. code-block:: asm

         int
          foo(int n)
        {
          if (n == 0)
            return 1;
          else
            return (foo(n - 1));
        }
         cmp     %o0,0
        be      .L1
        or      %g0,%o0,%g1
        subcc   %g1,1,%g1
  .L2:  bne     .L2
        subcc   %g1,1,%g1
  .L1:  retl
        or      %g0,1,%o0

.. comment Figure 8 - Example of tail recursion elimination

Needless to say, these optimizations produce code that is difficult to debug.

Procedures, stacks, and debuggers
----------------------------------

When debugging an application, your debugger will be parsing the binary
and consulting the symbol table to determine procedure entry points. It
will also travel the stack frames "upward" to determine the current
call chain.

When compiling for debugging, compilers will generate additional code
as well as avoid some optimizations in order to allow reconstructing
situations during execution. For example, GCC/GDB makes sure original
parameter values are kept intact somewhere for future parsing of
the procedure call stack. The live in registers other than %i0 are
not touched. %i0 itself is copied into a free local register, and its
location is noted in the symbol file. (You can find out where variables
reside by using the "info address" command in GDB.)

Given that much of the semantics relating to stack handling and procedure
call entry/exit code is only recommended, debuggers will sometimes
be fooled. For example, the decision as to wether or not the current
procedure is a leaf one or not can be incorrect. In this case a spurious
procedure will be inserted between the current procedure and it's "real"
parent. Another example is when the application maintains its own implicit
call hierarchy, such as jumping to function pointers. In this case the
debugger can easily become totally confused.

The window overflow and underflow traps
---------------------------------------

When the SAVE instruction decrements the current window pointer (CWP)
so that it coincides with the invalid window in the window invalid mask
(WIM), a window overflow trap occurs. Conversely, when the RESTORE or
RETT instructions increment the CWP to coincide with the invalid window,
a window underflow trap occurs.

Either trap is handled by the operating system. Generally, data is
written out to memory and/or read from memory, and the WIM register
suitably altered.

The code in Figure 9 and Figure 10 below are bare-bones handlers for
the two traps. The text is directly from the source code, and sort of
works. (As far as I know, these are minimalistic handlers for SPARC
V8). Note that there is no way to directly access window registers
other than the current one, hence the code does additional save/restore
instructions. It's pretty tricky to understand the code, but figure 1
should be of help.

.. code-block:: asm

        /* a SAVE instruction caused a trap */
window_overflow:
        /* rotate WIM on bit right, we have 8 windows */
        mov %wim,%l3
        sll %l3,7,%l4
        srl %l3,1,%l3
        or  %l3,%l4,%l3
        and %l3,0xff,%l3

        /* disable WIM traps */
        mov %g0,%wim
        nop; nop; nop

        /* point to correct window */
        save

        /* dump registers to stack */
        std %l0, [%sp +  0]
        std %l2, [%sp +  8]
        std %l4, [%sp + 16]
        std %l6, [%sp + 24]
        std %i0, [%sp + 32]
        std %i2, [%sp + 40]
        std %i4, [%sp + 48]
        std %i6, [%sp + 56]

        /* back to where we should be */
        restore

        /* set new value of window */
        mov %l3,%wim
        nop; nop; nop

        /* go home */
        jmp %l1
        rett %l2
Figure 9 - window_underflow trap handler
        /* a RESTORE instruction caused a trap */
window_underflow:
        
        /* rotate WIM on bit LEFT, we have 8 windows */ 
        mov %wim,%l3
        srl %l3,7,%l4
        sll %l3,1,%l3
        or  %l3,%l4,%l3
        and %l3,0xff,%l3

        /* disable WIM traps */
        mov %g0,%wim
        nop; nop; nop

        /* point to correct window */
        restore
        restore

        /* dump registers to stack */
        ldd [%sp +  0], %l0
        ldd [%sp +  8], %l2
        ldd [%sp + 16], %l4
        ldd [%sp + 24], %l6
        ldd [%sp + 32], %i0
        ldd [%sp + 40], %i2
        ldd [%sp + 48], %i4
        ldd [%sp + 56], %i6

        /* back to where we should be */
        save
        save

        /* set new value of window */
        mov %l3,%wim
        nop; nop; nop

        /* go home */
        jmp %l1
        rett %l2

.. comment Figure 10 - window_underflow trap handler

