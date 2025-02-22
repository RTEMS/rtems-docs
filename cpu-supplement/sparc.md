% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2021 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# SPARC Specific Information

The Real Time Executive for Multiprocessor Systems (RTEMS) is designed to be
portable across multiple processor architectures. However, the nature of
real-time systems makes it essential that the application designer understand
certain processor dependent implementation details. These processor
dependencies include calling convention, board support package issues,
interrupt processing, exact RTEMS memory requirements, performance data, header
files, and the assembly language interface to the executive.

This document discusses the SPARC architecture dependencies in this port of
RTEMS. This architectural port is for SPARC Version 7 and
8\.

It is highly recommended that the SPARC RTEMS application developer obtain and
become familiar with the documentation for the processor being used as well as
the specification for the revision of the SPARC architecture which corresponds
to that processor.

**SPARC Architecture Documents**

For information on the SPARC architecture, refer to the following documents
available from SPARC International, Inc. ([https://sparc.org/](https://sparc.org/)):

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
error-detection. The core is designed to work at 25MHz, but using space
qualified memories limits the system frequency to around 15 MHz, resulting in a
performance of 10 MIPS and 2 MFLOPS.

The ERC32 is available from Atmel as the TSC695F.

The RTEMS configuration of GDB enables the SPARC Instruction Simulator (SIS)
which can simulate the ERC32 as well as the follow up LEON2 and LEON3
microprocessors.

## CPU Model Dependent Features

Microprocessors are generally classified into families with a variety of CPU
models or implementations within that family. Within a processor family, there
is a high level of binary compatibility. This family may be based on either an
architectural specification or on maintaining compatibility with a popular
processor. Recent microprocessor families such as the SPARC or PowerPC are
based on an architectural specification which is independent or any particular
CPU model or implementation. Older families such as the M68xxx and the iX86
evolved as the manufacturer strived to produce higher performance processor
models which maintained binary compatibility with older models.

RTEMS takes advantage of the similarity of the various models within a CPU
family. Although the models do vary in significant ways, the high level of
compatibility makes it possible to share the bulk of the CPU dependent
executive code across the entire family.

### CPU Model Feature Flags

Each processor family supported by RTEMS has a list of features which vary
between CPU models within a family. For example, the most common model
dependent feature regardless of CPU family is the presence or absence of a
floating point unit or coprocessor. When defining the list of features present
on a particular CPU model, one simply notes that floating point hardware is or
is not present and defines a single constant appropriately. Conditional
compilation is utilized to include the appropriate source code for this CPU
model's feature set. It is important to note that this means that RTEMS is
thus compiled using the appropriate feature set and compilation flags optimal
for this CPU model used. The alternative would be to generate a binary which
would execute on all family members using only the features which were always
present.

This section presents the set of features which vary across SPARC
implementations and are of importance to RTEMS. The set of CPU model feature
macros are defined in the file cpukit/score/cpu/sparc/sparc.h based upon the
particular CPU model defined on the compilation command line.

#### CPU Model Name

The macro CPU_MODEL_NAME is a string which designates the name of this CPU
model. For example, for the European Space Agency's ERC32 SPARC model, this
macro is set to the string "erc32".

#### Floating Point Unit

The macro SPARC_HAS_FPU is set to 1 to indicate that this CPU model has a
hardware floating point unit and 0 otherwise.

#### Bitscan Instruction

The macro SPARC_HAS_BITSCAN is set to 1 to indicate that this CPU model has the
bitscan instruction. For example, this instruction is supported by the Fujitsu
SPARClite family.

#### Number of Register Windows

The macro SPARC_NUMBER_OF_REGISTER_WINDOWS is set to indicate the number of
register window sets implemented by this CPU model. The SPARC architecture
allows a for a maximum of thirty-two register window sets although most
implementations only include eight.

#### Low Power Mode

The macro SPARC_HAS_LOW_POWER_MODE is set to one to indicate that this CPU
model has a low power mode. If low power is enabled, then there must be CPU
model specific implementation of the IDLE task in cpukit/score/cpu/sparc/cpu.c.
The low power mode IDLE task should be of the form:

```c
while ( TRUE ) {
    enter low power mode
}
```

The code required to enter low power mode is CPU model specific.

### CPU Model Implementation Notes

The ERC32 is a custom SPARC V7 implementation based on the Cypress 601/602
chipset. This CPU has a number of on-board peripherals and was developed by
the European Space Agency to target space applications. RTEMS currently
provides support for the following peripherals:

- UART Channels A and B
- General Purpose Timer
- Real Time Clock
- Watchdog Timer (so it can be disabled)
- Control Register (so powerdown mode can be enabled)
- Memory Control Register
- Interrupt Control

The General Purpose Timer and Real Time Clock Timer provided with the ERC32
share the Timer Control Register. Because the Timer Control Register is write
only, we must mirror it in software and insure that writes to one timer do not
alter the current settings and status of the other timer. Routines are
provided in erc32.h which promote the view that the two timers are completely
independent. By exclusively using these routines to access the Timer Control
Register, the application can view the system as having a General Purpose Timer
Control Register and a Real Time Clock Timer Control Register rather than the
single shared value.

The RTEMS Idle thread take advantage of the low power mode provided by the
ERC32. Low power mode is entered during idle loops and is enabled at
initialization time.

## Calling Conventions

Each high-level language compiler generates subroutine entry and exit code
based upon a set of rules known as the application binary interface (ABI)
calling convention. These rules address the following issues:

- register preservation and usage
- parameter passing
- call and return mechanism

An ABI calling convention is of importance when interfacing to subroutines
written in another language either assembly or high-level. It determines also
the set of registers to be saved or restored during a context switch and
interrupt processing.

The ABI relevant for RTEMS on SPARC is defined by SYSTEM V APPLICATION BINARY
INTERFACE, SPARC Processor Supplement, Third Edition.

### Programming Model

This section discusses the programming model for the SPARC architecture.

#### Non-Floating Point Registers

The SPARC architecture defines thirty-two non-floating point registers directly
visible to the programmer. These are divided into four sets:

- input registers
- local registers
- output registers
- global registers

Each register is referred to by either two or three names in the SPARC
reference manuals. First, the registers are referred to as r0 through r31 or
with the alternate notation r[0] through r[31]. Second, each register is a
member of one of the four sets listed above. Finally, some registers have an
architecturally defined role in the programming model which provides an
alternate name. The following table describes the mapping between the 32
registers and the register sets:

| Register Number | Register Names | Description      |
| --------------- | -------------- | ---------------- |
| 0 - 7           | g0 - g7        | Global Registers |
| 8 - 15          | o0 - o7        | Output Registers |
| 16 - 23         | l0 - l7        | Local Registers  |
| 24 - 31         | i0 - i7        | Input Registers  |

As mentioned above, some of the registers serve defined roles in the
programming model. The following table describes the role of each of these
registers:

| Register Name | Alternate Name | Description                        |
| ------------- | -------------- | ---------------------------------- |
| g0            | na             | reads return 0, writes are ignored |
| o6            | sp             | stack pointer                      |
| i6            | fp             | frame pointer                      |
| i7            | na             | return address                     |

The registers g2 through g4 are reserved for applications. GCC uses them as
volatile registers by default. So they are treated like volatile registers in
RTEMS as well.

The register g6 is reserved for the operating system and contains the address
of the per-CPU control block of the current processor. This register is
initialized during system start and then remains unchanged. It is not
saved/restored by the context switch or interrupt processing code.

The register g7 is reserved for the operating system and contains the thread
pointer used for thread-local storage (TLS) as mandated by the SPARC ABI.

#### Floating Point Registers

The SPARC V7 architecture includes thirty-two, thirty-two bit registers. These
registers may be viewed as follows:

- 32 single precision floating point or integer registers (f0, f1, ... f31)
- 16 double precision floating point registers (f0, f2, f4, ... f30)
- 8 extended precision floating point registers (f0, f4, f8, ... f28)

The floating point status register (FSR) specifies the behavior of the floating
point unit for rounding, contains its condition codes, version specification,
and trap information.

According to the ABI all floating point registers and the floating point status
register (FSR) are volatile. Thus the floating point context of a thread is
the empty set. The rounding direction is a system global state and must not be
modified by threads.

A queue of the floating point instructions which have started execution but not
yet completed is maintained. This queue is needed to support the multiple
cycle nature of floating point operations and to aid floating point exception
trap handlers. Once a floating point exception has been encountered, the queue
is frozen until it is emptied by the trap handler. The floating point queue is
loaded by launching instructions. It is emptied normally when the floating
point completes all outstanding instructions and by floating point exception
handlers with the store double floating point queue (stdfq) instruction.

#### Special Registers

The SPARC architecture includes two special registers which are critical to the
programming model: the Processor State Register (`PSR`) and the Window Invalid
Mask (`WIM`). The `PSR` contains the condition codes, processor interrupt level,
trap enable bit, supervisor mode and previous supervisor mode bits, version
information, floating point unit and coprocessor enable bits, and the current
window pointer (`CWP`). The `CWP` field of the `PSR` and `WIM` register are used to
manage the register windows in the SPARC architecture. The register windows
are discussed in more detail below.

### Register Windows

The SPARC architecture includes the concept of register windows. An overly
simplistic way to think of these windows is to imagine them as being an
infinite supply of "fresh" register sets available for each subroutine to use.
In reality, they are much more complicated.

The save instruction is used to obtain a new register window. This instruction
decrements the current window pointer, thus providing a new set of registers
for use. This register set includes eight fresh local registers for use
exclusively by this subroutine. When done with a register set, the restore
instruction increments the current window pointer and the previous register set
is once again available.

The two primary issues complicating the use of register windows are that (1)
the set of register windows is finite, and (2) some registers are shared
between adjacent registers windows.

Because the set of register windows is finite, it is possible to execute enough
save instructions without corresponding restore's to consume all of the
register windows. This is easily accomplished in a high level language because
each subroutine typically performs a save instruction upon entry. Thus having
a subroutine call depth greater than the number of register windows will result
in a window overflow condition. The window overflow condition generates a trap
which must be handled in software. The window overflow trap handler is
responsible for saving the contents of the oldest register window on the
program stack.

Similarly, the subroutines will eventually complete and begin to perform
restore's. If the restore results in the need for a register window which has
previously been written to memory as part of an overflow, then a window
underflow condition results. Just like the window overflow, the window
underflow condition must be handled in software by a trap handler. The window
underflow trap handler is responsible for reloading the contents of the
register window requested by the restore instruction from the program stack.

The Window Invalid Mask (`WIM`) and the Current Window Pointer (`CWP`) field in the
`PSR` are used in conjunction to manage the finite set of register windows and
detect the window overflow and underflow conditions. The `CWP` contains the
index of the register window currently in use. The save instruction decrements
the `CWP` modulo the number of register windows. Similarly, the restore
instruction increments the `CWP` modulo the number of register windows. Each bit
in the `WIM` represents represents whether a register window contains valid
information. The value of 0 indicates the register window is valid and 1
indicates it is invalid. When a save instruction causes the `CWP` to point to a
register window which is marked as invalid, a window overflow condition
results. Conversely, the restore instruction may result in a window underflow
condition.

Other than the assumption that a register window is always available for trap
(i.e. interrupt) handlers, the SPARC architecture places no limits on the
number of register windows simultaneously marked as invalid (i.e. number of
bits set in the `WIM`). However, RTEMS assumes that only one register window is
marked invalid at a time (i.e. only one bit set in the `WIM`). This makes the
maximum possible number of register windows available to the user while still
meeting the requirement that window overflow and underflow conditions can be
detected.

The window overflow and window underflow trap handlers are a critical part of
the run-time environment for a SPARC application. The SPARC architectural
specification allows for the number of register windows to be any power of two
less than or equal to 32. The most common choice for SPARC implementations
appears to be 8 register windows. This results in the `CWP` ranging in value
from 0 to 7 on most implementations.

The second complicating factor is the sharing of registers between adjacent
register windows. While each register window has its own set of local
registers, the input and output registers are shared between adjacent windows.
The output registers for register window N are the same as the input registers
for register window ((N - 1) modulo RW) where RW is the number of register
windows. An alternative way to think of this is to remember how parameters are
passed to a subroutine on the SPARC. The caller loads values into what are its
output registers. Then after the callee executes a save instruction, those
parameters are available in its input registers. This is a very efficient way
to pass parameters as no data is actually moved by the save or restore
instructions.

### Call and Return Mechanism

The SPARC architecture supports a simple yet effective call and return
mechanism. A subroutine is invoked via the call (call) instruction. This
instruction places the return address in the caller's output register 7 (o7).
After the callee executes a save instruction, this value is available in input
register 7 (i7) until the corresponding restore instruction is executed.

The callee returns to the caller via a jmp to the return address. There is a
delay slot following this instruction which is commonly used to execute a
restore instruction - if a register window was allocated by this subroutine.

It is important to note that the SPARC subroutine call and return mechanism
does not automatically save and restore any registers. This is accomplished
via the save and restore instructions which manage the set of registers
windows.

In case a floating-point unit is supported, then floating-point return values
appear in the floating-point registers. Single-precision values occupy %f0;
double-precision values occupy %f0 and %f1. Otherwise, these are scratch
registers. Due to this the hardware and software floating-point ABIs are
incompatible.

### Calling Mechanism

All RTEMS directives are invoked using the regular SPARC calling convention via
the call instruction.

### Register Usage

As discussed above, the call instruction does not automatically save any
registers. The save and restore instructions are used to allocate and
deallocate register windows. When a register window is allocated, the new set
of local registers are available for the exclusive use of the subroutine which
allocated this register set.

### Parameter Passing

RTEMS assumes that arguments are placed in the caller's output registers with
the first argument in output register 0 (o0), the second argument in output
register 1 (o1), and so forth. Until the callee executes a save instruction,
the parameters are still visible in the output registers. After the callee
executes a save instruction, the parameters are visible in the corresponding
input registers. The following pseudo-code illustrates the typical sequence
used to call a RTEMS directive with three (3) arguments:

```c
load third argument into o2
load second argument into o1
load first argument into o0
invoke directive
```

### User-Provided Routines

All user-provided routines invoked by RTEMS, such as user extensions, device
drivers, and MPCI routines, must also adhere to these calling conventions.

______________________________________________________________________

```{sidebar} *Origin*
This SPARC Annul Slot section was originally an email from Jiri Gaisler
to Joel Sherrill that explained why sometimes, a single instruction
will not be executed, due to the Annul Slot feature.
```

In SPARC, the default behaviour is to execute instructions after a branch.
As with the behaviour of most RISC (Reduced Instruction Set Computer)
machines, SPARC uses a branch delay slot. This is because completing
an instruction every clock cycle introduces the problem that a branch
may not be resolved until the instruction has passed through the
pipeline. By inserting stalls, this is prevented. In each cycle, if a
stall is inserted, it is considered one branch delay slot.

For example, a regular branch instruction might look like so:

```assembly
cmp %o4, %g4    /* if %o4 is equals to %g4 */
be 200fd06      /* then branch */
mov [%g4], %o4  /* instructions after the branch, this is a */
                /* branch delay slot it is executed regardless */
                /* of whether %o4 is equals to %g4 */
```

However, if marked with "`,a`", the instructions after the branch will
only be executed if the branch is taken. In other words, only if the
condition before is true, then it would be executed. Otherwise if would be
"annulled".

```assembly
cmp %o4, %g4    /* if %o4 is equals to %g4 */
be,a 200fd06    /* then branch */
mov [%g4], %o4  /* instruction after the branch */
```

The `mov` instruction is in a branch delay slot and is only executed
if the branch is taken (e.g. if %o4 is equals to %g4).

This shows up in analysis of coverage reports when a single instruction
is marked unexecuted when the instruction above and below it are executed.

## Memory Model

A processor may support any combination of memory models ranging from pure
physical addressing to complex demand paged virtual memory systems. RTEMS
supports a flat memory model which ranges contiguously over the processor's
allowable address space. RTEMS does not support segmentation or virtual memory
of any kind. The appropriate memory model for RTEMS provided by the targeted
processor and related characteristics of that model are described in this
chapter.

### Flat Memory Model

The SPARC architecture supports a flat 32-bit address space with addresses
ranging from 0x00000000 to 0xFFFFFFFF (4 gigabytes). Each address is
represented by a 32-bit value and is byte addressable. The address may be used
to reference a single byte, half-word (2-bytes), word (4 bytes), or doubleword
(8 bytes). Memory accesses within this address space are performed in big
endian fashion by the SPARC. Memory accesses which are not properly aligned
generate a "memory address not aligned" trap (type number 7). The following
table lists the alignment requirements for a variety of data accesses:

| Data Type  | Alignment Requirement |
| ---------- | --------------------- |
| byte       | 1                     |
| half-word  | 2                     |
| word       | 4                     |
| doubleword | 8                     |

Doubleword load and store operations must use a pair of registers as their
source or destination. This pair of registers must be an adjacent pair of
registers with the first of the pair being even numbered. For example, a valid
destination for a doubleword load might be input registers 0 and 1 (i0 and i1).
The pair i1 and i2 would be invalid. [NOTE: Some assemblers for the SPARC do
not generate an error if an odd numbered register is specified as the beginning
register of the pair. In this case, the assembler assumes that what the
programmer meant was to use the even-odd pair which ends at the specified
register. This may or may not have been a correct assumption.]

RTEMS does not support any SPARC Memory Management Units, therefore, virtual
memory or segmentation systems involving the SPARC are not supported.

## Interrupt Processing

Different types of processors respond to the occurrence of an interrupt in its
own unique fashion. In addition, each processor type provides a control
mechanism to allow for the proper handling of an interrupt. The processor
dependent response to the interrupt modifies the current execution state and
results in a change in the execution stream. Most processors require that an
interrupt handler utilize some special control mechanisms to return to the
normal processing stream. Although RTEMS hides many of the processor dependent
details of interrupt processing, it is important to understand how the RTEMS
interrupt manager is mapped onto the processor's unique architecture. Discussed
in this chapter are the SPARC's interrupt response and control mechanisms as
they pertain to RTEMS.

RTEMS and associated documentation uses the terms interrupt and vector. In the
SPARC architecture, these terms correspond to traps and trap type,
respectively. The terms will be used interchangeably in this manual.

### Synchronous Versus Asynchronous Traps

The SPARC architecture includes two classes of traps: synchronous and
asynchronous. Asynchronous traps occur when an external event interrupts the
processor. These traps are not associated with any instruction executed by the
processor and logically occur between instructions. The instruction currently
in the execute stage of the processor is allowed to complete although
subsequent instructions are annulled. The return address reported by the
processor for asynchronous traps is the pair of instructions following the
current instruction.

Synchronous traps are caused by the actions of an instruction. The trap
stimulus in this case either occurs internally to the processor or is from an
external signal that was provoked by the instruction. These traps are taken
immediately and the instruction that caused the trap is aborted before any
state changes occur in the processor itself. The return address reported by
the processor for synchronous traps is the instruction which caused the trap
and the following instruction.

### Trap Table

A SPARC processor uses a trap table to execute the trap handler associated with
a trap. The trap table location is defined by the Trap Base Register
(`TBR`). The trap table has 256 entries. Each entry has space for four
instructions (16 bytes). RTEMS uses a statically initialized trap table. The
start address of the trap table is associated with the `trap_table` global
symbol. The first action of the system initialization (entry points `_start`
and `hard_reset`) is to set the `TBR` to `trap_table`. The interrupt
traps (trap numbers 16 to 31) are connected with the RTEMS interrupt handling.
Some traps are connected to standard services defined by the SPARC
architecture, for example the window overflow, underflow, and flush handling.
Most traps are connected to a fatal error handler. The fatal error trap
handler saves the processor context to an exception frame and starts the system
termination procedure.

### Vectoring of Interrupt Handler

Upon receipt of an interrupt a SPARC processor automatically performs the
following actions:

- disables traps (sets the `PSR.ET` bit to 0 in the `PSR`),
- the `PSR.S` bit is copied into the Previous Supervisor Mode (`PSR.PS`)
  bit in the `PSR`,
- the `CWP` is decremented by one (modulo the number of register windows) to
  activate a trap window,
- the PC and nPC are loaded into local register 1 and 2 (`%l0` and `%l1`),
- the trap type (`tt`) field of the Trap Base Register (`TBR`) is set to
  the appropriate value, and
- if the trap is not a reset, then the PC is written with the contents of the
  `TBR` and the nPC is written with `TBR` + 4. If the trap is a reset,
  then the PC is set to zero and the nPC is set to 4.

Trap processing on the SPARC has two features which are noticeably different
than interrupt processing on other architectures. First, the value of `PSR`
register in effect immediately before the trap occurred is not explicitly
saved. Instead only reversible alterations are made to it. Second, the
Processor Interrupt Level (`PSR.PIL`) is not set to correspond to that of the
interrupt being processed. When a trap occurs, **all** subsequent traps are
disabled. In order to safely invoke a subroutine during trap handling, traps
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

Asynchronous interrupts are ignored while traps are disabled. Synchronous
traps which occur while traps are disabled result in the CPU being forced into
an error mode.

A nested interrupt is processed similarly with the exception that the current
stack need not be switched to the interrupt stack.

### Traps and Register Windows

One of the register windows must be reserved at all times for trap processing.
This is critical to the proper operation of the trap mechanism in the SPARC
architecture. It is the responsibility of the trap handler to insure that
there is a register window available for a subsequent trap before re-enabling
traps. It is likely that any high level language routines invoked by the trap
handler (such as a user-provided RTEMS interrupt handler) will allocate a new
register window. The save operation could result in a window overflow trap.
This trap cannot be correctly processed unless (1) traps are enabled and (2) a
register window is reserved for traps. Thus, the RTEMS interrupt handler
insures that a register window is available for subsequent traps before
enabling traps and invoking the user's interrupt handler.

### Interrupt Levels

Sixteen levels (0-15) of interrupt priorities are supported by the SPARC
architecture with level fifteen (15) being the highest priority. Level
zero (0) indicates that interrupts are fully enabled. Interrupt requests for
interrupts with priorities less than or equal to the current interrupt mask
level are ignored. Level fifteen (15) is a non-maskable interrupt (NMI), which
makes it unsuitable for standard usage since it can affect the real-time
behaviour by interrupting critical sections and spinlocks. Disabling traps
stops also the NMI interrupt from happening. It can however be used for
power-down or other critical events.

Although RTEMS supports 256 interrupt levels, the SPARC only supports sixteen.
RTEMS interrupt levels 0 through 15 directly correspond to SPARC processor
interrupt levels. All other RTEMS interrupt levels are undefined and their
behavior is unpredictable.

Many LEON SPARC v7/v8 systems features an extended interrupt controller which
adds an extra step of interrupt decoding to allow handling of interrupt
16-31. When such an extended interrupt is generated the CPU traps into a
specific interrupt trap level 1-14 and software reads out from the interrupt
controller which extended interrupt source actually caused the interrupt.

### Disabling of Interrupts by RTEMS

During the execution of directive calls, critical sections of code may be
executed. When these sections are encountered, RTEMS disables interrupts to
level fifteen (15) before the execution of the section and restores them to the
previous level upon completion of the section. RTEMS has been optimized to
ensure that interrupts are disabled for less than RTEMS_MAXIMUM_DISABLE_PERIOD
microseconds on a RTEMS_MAXIMUM_DISABLE_PERIOD_MHZ Mhz ERC32 with zero wait
states. These numbers will vary based the number of wait states and processor
speed present on the target board. [NOTE: The maximum period with interrupts
disabled is hand calculated. This calculation was last performed for Release
RTEMS_RELEASE_FOR_MAXIMUM_DISABLE_PERIOD.]

[NOTE: It is thought that the length of time at which the processor interrupt
level is elevated to fifteen by RTEMS is not anywhere near as long as the
length of time ALL traps are disabled as part of the "flush all register
windows" operation.]

Non-maskable interrupts (NMI) cannot be disabled, and ISRs which execute at
this level MUST NEVER issue RTEMS system calls. If a directive is invoked,
unpredictable results may occur due to the inability of RTEMS to protect its
critical sections. However, ISRs that make no system calls may safely execute
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

### Interrupt Stack

The SPARC architecture does not provide for a dedicated interrupt stack. Thus
by default, trap handlers would execute on the stack of the RTEMS task which
they interrupted. This artificially inflates the stack requirements for each
task since **every** task stack would have to include enough space to account
for the worst case interrupt stack requirements in addition to it's own worst
case usage. RTEMS addresses this problem on the SPARC by providing a dedicated
interrupt stack managed by software.

The interrupt stack is statically allocated by RTEMS. There is one interrupt
stack for each configured processor. The interrupt stack is used to initialize
the system. The amount of memory allocated for the interrupt stack is
determined by the `CONFIGURE_INTERRUPT_STACK_SIZE` application configuration
option. As part of processing a non-nested interrupt, RTEMS will switch to the
interrupt stack before invoking the installed handler.

## Symmetric Multiprocessing

SMP is supported. Available platforms are the Cobham Gaisler GR712RC and
GR740.

## Thread-Local Storage

Thread-local storage is supported.

## Board Support Packages

An RTEMS Board Support Package (BSP) must be designed to support a particular
processor and target board combination. This chapter presents a discussion of
SPARC specific BSP issues. For more information on developing a BSP, refer to
the chapter titled Board Support Packages in the RTEMS Applications User's
Guide.

### System Reset

An RTEMS based application is initiated or re-initiated when the SPARC
processor is reset. When the SPARC is reset, the processor performs the
following actions:

- the enable trap (ET) of the `PSR` is set to 0 to disable traps,
- the supervisor bit (S) of the `PSR` is set to 1 to enter supervisor mode, and
- the PC is set 0 and the nPC is set to 4.

The processor then begins to execute the code at location 0. It is important
to note that all fields in the `PSR` are not explicitly set by the above steps
and all other registers retain their value from the previous execution mode.
This is true even of the Trap Base Register (`TBR`) whose contents reflect the
last trap which occurred before the reset.

### Processor Initialization

It is the responsibility of the application's initialization code to initialize
the `TBR` and install trap handlers for at least the register window overflow and
register window underflow conditions. Traps should be enabled before invoking
any subroutines to allow for register window management. However, interrupts
should be disabled by setting the Processor Interrupt Level (pil) field of the
`PSR` to 15. RTEMS installs it's own Trap Table as part of initialization which
is initialized with the contents of the Trap Table in place when the
`rtems_initialize_executive` directive was invoked. Upon completion of
executive initialization, interrupts are enabled.

If this SPARC implementation supports on-chip caching and this is to be
utilized, then it should be enabled during the reset application initialization
code.

In addition to the requirements described in the Board Support Packages chapter
of the C Applications Users Manual for the reset code which is executed before
the call to\`\`rtems_initialize_executive\`\`, the SPARC version has the following
specific requirements:

- Must leave the S bit of the status register set so that the SPARC remains in
  the supervisor state.
- Must set stack pointer (sp) such that a minimum stack size of
  MINIMUM_STACK_SIZE bytes is provided for the\`\`rtems_initialize_executive\`\`
  directive.
- Must disable all external interrupts (i.e. set the pil to 15).
- Must enable traps so window overflow and underflow conditions can be properly
  handled.
- Must initialize the SPARC's initial trap table with at least trap handlers
  for register window overflow and register window underflow.

% COMMENT: Include SPARC v8 Register Windows Explanation

% COMMENT: Keep separate until completely formatted, maybe forever

```{eval-rst}
.. include:: sparc_v8_stacks_regwin.rst
```
