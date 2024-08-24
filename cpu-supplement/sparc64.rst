.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2010 Gedare Bloom
.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

SPARC-64 Specific Information
*****************************

This document discusses the SPARC Version 9 (aka SPARC-64, SPARC64 or SPARC V9)
architecture dependencies in this port of RTEMS.

The SPARC V9 architecture leaves a lot of undefined implemenation dependencies
which are defined by the processor models. Consult the specific CPU model
section in this document for additional documents covering the implementation
dependent architectural features.

**sun4u Specific Information**

sun4u is the subset of the SPARC V9 implementations comprising the UltraSPARC I
through UltraSPARC IV processors.

The following documents were used in developing the SPARC-64 sun4u port:

- UltraSPARC  User's Manual
  (http://www.sun.com/microelectronics/manuals/ultrasparc/802-7220-02.pdf)

- UltraSPARC IIIi Processor (http://datasheets.chipdb.org/Sun/UltraSparc-IIIi.pdf)

**sun4v Specific Information**

sun4v is the subset of the SPARC V9 implementations comprising the UltraSPARC
T1 or T2 processors.

The following documents were used in developing the SPARC-64 sun4v port:

- UltraSPARC Architecture 2005 Specification
  (http://opensparc-t1.sunsource.net/specs/UA2005-current-draft-P-EXT.pdf)

- UltraSPARC T1 supplement to UltraSPARC Architecture 2005 Specification
  (http://opensparc-t1.sunsource.net/specs/UST1-UASuppl-current-draft-P-EXT.pdf)

The defining feature that separates the sun4v architecture from its predecessor
is the existence of a super-privileged hypervisor that is responsible for
providing virtualized execution environments.  The impact of the hypervisor on
the real-time guarantees available with sun4v has not yet been determined.

CPU Model Dependent Features
============================

CPU Model Feature Flags
-----------------------

This section presents the set of features which vary across SPARC-64
implementations and are of importance to RTEMS. The set of CPU model feature
macros are defined in the file cpukit/score/cpu/sparc64/sparc64.h based upon
the particular CPU model defined on the compilation command line.

CPU Model Name
~~~~~~~~~~~~~~

The macro CPU MODEL NAME is a string which designates the name of this CPU
model.  For example, for the UltraSPARC T1 SPARC V9 model, this macro is set to
the string "sun4v".

Floating Point Unit
~~~~~~~~~~~~~~~~~~~

The macro SPARC_HAS_FPU is set to 1 to indicate that this CPU model has a
hardware floating point unit and 0 otherwise.

Number of Register Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~

The macro SPARC_NUMBER_OF_REGISTER_WINDOWS is set to indicate the number of
register window sets implemented by this CPU model.  The SPARC architecture
allows for a maximum of thirty-two register window sets although most
implementations only include eight.

CPU Model Implementation Notes
------------------------------

This section describes the implemenation dependencies of the CPU Models sun4u
and sun4v of the SPARC V9 architecture.

sun4u Notes
~~~~~~~~~~~

XXX

sun4v Notes
-----------

XXX

Calling Conventions
===================

Each high-level language compiler generates subroutine entry and exit code
based upon a set of rules known as the compiler's calling convention.  These
rules address the following issues:

- register preservation and usage

- parameter passing

- call and return mechanism

A compiler's calling convention is of importance when
interfacing to subroutines written in another language either
assembly or high-level.  Even when the high-level language and
target processor are the same, different compilers may use
different calling conventions.  As a result, calling conventions
are both processor and compiler dependent.

The following document also provides some conventions on the global register
usage in SPARC V9: http://developers.sun.com/solaris/articles/sparcv9abi.html

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

Floating Point Registers
~~~~~~~~~~~~~~~~~~~~~~~~

The SPARC V9 architecture includes sixty-four, thirty-two bit registers.  These
registers may be viewed as follows:

- 32 32-bit single precision floating point or integer registers (f0, f1,
  ... f31)

- 32 64-bit double precision floating point registers (f0, f2, f4, ... f62)

- 16 128-bit extended precision floating point registers (f0, f4, f8, ... f60)

The floating point state register (fsr) specifies the behavior of the floating
point unit for rounding, contains its condition codes, version specification,
and trap information.

Special Registers
~~~~~~~~~~~~~~~~~

The SPARC architecture includes a number of special registers:

*``Ancillary State Registers (ASRs)``*
    The ancillary state registers (ASRs) are optional state registers that may
    be privileged or nonprivileged. ASRs 16-31 are implementation-
    dependent. The SPARC V9 ASRs include: y, ccr, asi, tick, pc, fprs.  The
    sun4u ASRs include: pcr, pic, dcr, gsr, softint set, softint clr, softint,
    and tick cmpr. The sun4v ASRs include: pcr, pic, gsr, soft- int set,
    softint clr, softint, tick cmpr, stick, and stick cmpr.

*``Processor State Register (pstate)``*
    The privileged pstate register contains control fields for the proces-
    sor's current state. Its flag fields include the interrupt enable, privi-
    leged mode, and enable FPU.

*``Processor Interrupt Level (pil)``*
    The PIL specifies the interrupt level above which interrupts will be
    accepted.

*``Trap Registers``*
    The trap handling mechanism of the SPARC V9 includes a number of registers,
    including: trap program counter (tpc), trap next pc (tnpc), trap state
    (tstate), trap type (tt), trap base address (tba), and trap level (tl).

*``Alternate Globals``*
    The AG bit of the pstate register provides access to an alternate set of
    global registers. On sun4v, the AG bit is replaced by the global level (gl)
    register, providing access to at least two and at most eight alternate sets
    of globals.

*``Register Window registers``*
    A number of registers assist in register window management.  These include
    the current window pointer (cwp), savable windows (cansave), restorable
    windows (canrestore), clean windows (clean- win), other windows (otherwin),
    and window state (wstate).

Register Windows
----------------

The SPARC architecture includes the concept of register windows.  An overly
simplistic way to think of these windows is to imagine them as being an
infinite supply of "fresh" register sets available for each subroutine to use.
In reality, they are much more complicated.

The save instruction is used to obtain a new register window.  This instruction
increments the current window pointer, thus providing a new set of registers
for use. This register set includes eight fresh local registers for use
exclusively by this subroutine. When done with a register set, the restore
instruction decrements the current window pointer and the previous register set
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

The cansave, canrestore, otherwin, and cwp are used in conjunction to manage
the finite set of register windows and detect the window overflow and underflow
conditions. The first three of these registers must satisfy the invariant
cansave + canrestore + otherwin = nwindow - 2, where nwindow is the number of
register windows.  The cwp contains the index of the register window currently
in use.  RTEMS does not use the cleanwin and otherwin registers.

The save instruction increments the cwp modulo the number of register windows,
and if cansave is 0 then it also generates a window overflow. Similarly, the
restore instruction decrements the cwp modulo the number of register windows,
and if canrestore is 0 then it also generates a window underflow.

Unlike with the SPARC model, the SPARC-64 port does not assume that a register
window is available for a trap. The window overflow and underflow conditions
are not detected without hardware generating the trap. (These conditions can be
detected by reading the register window registers and doing some simple
arithmetic.)

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
for register window ((N + 1) modulo RW) where RW is the number of register
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
windows.  This allows for the compiler to generate leaf-optimized functions
that utilize the caller's output registers without using save and restore.

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

The SPARC-64 architecture supports a flat 64-bit address space with addresses
ranging from 0x0000000000000000 to 0xFFFFFFFFFFFFFFFF.  Each address is
represented by a 64-bit value (and an 8-bit address space identifider or ASI)
and is byte addressable. The address may be used to reference a single byte,
half-word (2-bytes), word (4 bytes), doubleword (8 bytes), or quad-word (16
bytes).  Memory accesses within this address space are performed in big endian
fashion by the SPARC. Memory accesses which are not properly aligned generate a
"memory address not aligned" trap (type number 0x34). The following table lists
the alignment requirements for a variety of data accesses:

==============  ======================
Data Type       Alignment Requirement
==============  ======================
byte            1
half-word       2
word            4
doubleword      8
quadword        16
==============  ======================

RTEMS currently does not support any SPARC Memory Management Units, therefore,
virtual memory or segmentation systems involving the SPARC are not supported.

Interrupt Processing
====================

RTEMS and associated documentation uses the terms interrupt and vector.  In the
SPARC architecture, these terms correspond to traps and trap type,
respectively.  The terms will be used interchangeably in this manual. Note that
in the SPARC manuals, interrupts are a subset of the traps that are delivered
to software interrupt handlers.

Synchronous Versus Asynchronous Traps
-------------------------------------

The SPARC architecture includes two classes of traps: synchronous (precise) and
asynchronous (deferred).  Asynchronous traps occur when an external event
interrupts the processor.  These traps are not associated with any instruction
executed by the processor and logically occur between instructions.  The
instruction currently in the execute stage of the processor is allowed to
complete although subsequent instructions are annulled.  The return address
reported by the processor for asynchronous traps is the pair of instructions
following the current instruction.

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

- The trap level is set. This provides access to a fresh set of privileged
  trap-state registers used to save the current state, in effect, pushing a
  frame on the trap stack.  TL <- TL + 1

- Existing state is preserved
  - TSTATE[TL].CCR <- CCR
  - TSTATE[TL].ASI <- ASI
  - TSTATE[TL].PSTATE <- PSTATE
  - TSTATE[TL].CWP <- CWP
  - TPC[TL] <- PC
  - TNPC[TL] <- nPC

- The trap type is preserved. TT[TL] <- the trap type

- The PSTATE register is updated to a predefined state
  - PSTATE.MM is unchanged
  - PSTATE.RED <- 0
  - PSTATE.PEF <- 1 if FPU is present, 0 otherwise
  - PSTATE.AM <- 0 (address masking is turned off)
  - PSTATE.PRIV <- 1 (the processor enters privileged mode)
  - PSTATE.IE <- 0 (interrupts are disabled)
  - PSTATE.AG <- 1 (global regs are replaced with alternate globals)
  - PSTATE.CLE <- PSTATE.TLE (set endian mode for traps)

- For a register-window trap only, CWP is set to point to the register
  window that must be accessed by the trap-handler software, that is:

  - If TT[TL] = 0x24 (a clean window trap), then CWP <- CWP + 1.
  - If (0x80 <= TT[TL] <= 0xBF) (window spill trap), then CWP <- CWP +
    CANSAVE + 2.
  - If (0xC0 <= TT[TL] <= 0xFF) (window fill trap), then CWP <- CWP1.
  - For non-register-window traps, CWP is not changed.

- Control is transferred into the trap table:

  - PC <- TBA<63:15> (TL>0) TT[TL] 0 0000
  - nPC <- TBA<63:15> (TL>0) TT[TL] 0 0100
  - where (TL>0) is 0 if TL = 0, and 1 if TL > 0.

In order to safely invoke a subroutine during trap handling, traps must be
enabled to allow for the possibility of register window overflow and underflow
traps.

If the interrupt handler was installed as an RTEMS interrupt handler, then upon
receipt of the interrupt, the processor passes control to the RTEMS interrupt
handler which performs the following actions:

- saves the state of the interrupted task on it's stack,

- switches the processor to trap level 0,

- if this is the outermost (i.e. non-nested) interrupt, then the RTEMS
  interrupt handler switches from the current stack to the interrupt stack,

- enables traps,

- invokes the vectors to a user interrupt service routine (ISR).

Asynchronous interrupts are ignored while traps are disabled.  Synchronous
traps which occur while traps are disabled may result in the CPU being forced
into an error mode.

A nested interrupt is processed similarly with the exception that the current
stack need not be switched to the interrupt stack.

Traps and Register Windows
--------------------------

XXX

Interrupt Levels
----------------

Sixteen levels (0-15) of interrupt priorities are supported by the SPARC
architecture with level fifteen (15) being the highest priority.  Level
zero (0) indicates that interrupts are fully enabled.  Interrupt requests for
interrupts with priorities less than or equal to the current interrupt mask
level are ignored.

Although RTEMS supports 256 interrupt levels, the SPARC only supports sixteen.
RTEMS interrupt levels 0 through 15 directly correspond to SPARC processor
interrupt levels.  All other RTEMS interrupt levels are undefined and their
behavior is unpredictable.

Disabling of Interrupts by RTEMS
--------------------------------

XXX

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

Symmetric Multiprocessing
=========================

SMP is not supported.

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

HelenOS and Open Firmware
-------------------------

The provided BSPs make use of some bootstrap and low-level hardware code of the
HelenOS operating system. These files can be found in the shared/helenos
directory of the sparc64 bsp directory.  Consult the sources for more detailed
information.

The shared BSP code also uses the Open Firmware interface to re-use firmware
code, primarily for console support and default trap handlers.
