% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Port Specific Information

This chaper provides a general description of the type of architecture specific
information which is in each of the architecture specific chapters that follow.
The outline of this chapter is identical to that of the architecture specific
chapters.

In each of the architecture specific chapters, this introductory section will
provide an overview of the architecture:

**Architecture Documents**

In each of the architecture specific chapters, this section will provide
pointers on where to obtain documentation.

## CPU Model Dependent Features

Microprocessors are generally classified into families with a variety of CPU
models or implementations within that family. Within a processor family, there
is a high level of binary compatibility. This family may be based on either an
architectural specification or on maintaining compatibility with a popular
processor. Recent microprocessor families such as the SPARC or PowerPC are
based on an architectural specification which is independent or any particular
CPU model or implementation. Older families such as the Motorola 68000 and the
Intel x86 evolved as the manufacturer strived to produce higher performance
processor models which maintained binary compatibility with older models.

RTEMS takes advantage of the similarity of the various models within a CPU
family. Although the models do vary in significant ways, the high level of
compatibility makes it possible to share the bulk of the CPU dependent
executive code across the entire family. Each processor family supported by
RTEMS has a list of features which vary between CPU models within a family.
For example, the most common model dependent feature regardless of CPU family
is the presence or absence of a floating point unit or coprocessor. When
defining the list of features present on a particular CPU model, one simply
notes that floating point hardware is or is not present and defines a single
constant appropriately. Conditional compilation is utilized to include the
appropriate source code for this CPU model's feature set. It is important to
note that this means that RTEMS is thus compiled using the appropriate feature
set and compilation flags optimal for this CPU model used. The alternative
would be to generate a binary which would execute on all family members using
only the features which were always present.

The set of CPU model feature macros are defined in the
{file}`cpukit/score/cpu/CPU/rtems/score/cpu.h` based upon the GNU tools
multilib variant that is appropriate for the particular CPU model defined on
the compilation command line.

In each of the architecture specific chapters, this section presents the set of
features which vary across various implementations of the architecture that may
be of importance to RTEMS application developers.

The subsections will vary amongst the target architecture chapters as the
specific features may vary. However, each port will include a few common
features such as the CPU Model Name and presence of a hardware Floating Point
Unit. The common features are described here.

### CPU Model Name

The macro `CPU_MODEL_NAME` is a string which designates the name of this CPU
model. For example, for the MC68020 processor model from the m68k
architecture, this macro is set to the string "mc68020".

### Floating Point Unit

In most architectures, the presence of a floating point unit is an option. It
does not matter whether the hardware floating point support is incorporated
on-chip or is an external coprocessor as long as it appears an FPU per the ISA.
However, if a hardware FPU is not present, it is possible that the floating
point emulation library for this CPU is not reentrant and thus context switched
by RTEMS.

RTEMS provides two feature macros to indicate the FPU configuration:

- CPU_HARDWARE_FP
  is set to TRUE to indicate that a hardware FPU is present.
- CPU_SOFTWARE_FP
  is set to TRUE to indicate that a hardware FPU is not present and that the FP
  software emulation will be context switched.

## Multilibs

Newlib and GCC provide several target libraries like the {file}`libc.a`,
{file}`libm.a` and {file}`libgcc.a`. These libraries are artifacts of the GCC
build process. Newlib is built together with GCC. To provide optimal support
for various chip derivatives and instruction set revisions multiple variants of
these libraries are available for each architecture. For example one set may
use software floating point support and another set may use hardware floating
point instructions. These sets of libraries are called *multilibs*. Each
library set corresponds to an application binary interface (ABI) and
instruction set.

A multilib variant can be usually detected via built-in compiler defines at
compile-time. This mechanism is used by RTEMS to select for example the
context switch support for a particular BSP. The built-in compiler defines
corresponding to multilibs are the only architecture specific defines allowed
in the `cpukit` area of the RTEMS sources.

Invoking the GCC with the `-print-multi-lib` option lists the available
multilibs. Each line of the output describes one multilib variant. The
default variant is denoted by `.` which is selected when no or contradicting
GCC machine options are selected. The multilib selection for a target is
specified by target makefile fragments (see file {file}`t-rtems` in the GCC
sources and section *The Target Makefile Fragment*
(<https://gcc.gnu.org/onlinedocs/gccint/Target-Fragment.html#Target-Fragment>)
in the *GCC Internals Manual* (<https://gcc.gnu.org/onlinedocs/gccint/>).

## Calling Conventions

Each high-level language compiler generates subroutine entry and exit code
based upon a set of rules known as the compiler's calling convention. These
rules address the following issues:

- register preservation and usage
- parameter passing
- call and return mechanism

A compiler's calling convention is of importance when interfacing to
subroutines written in another language either assembly or high-level. Even
when the high-level language and target processor are the same, different
compilers may use different calling conventions. As a result, calling
conventions are both processor and compiler dependent.

### Calling Mechanism

In each of the architecture specific chapters, this subsection will describe
the instruction(s) used to perform a *normal* subroutine invocation. All RTEMS
directives are invoked as *normal* C language functions so it is important to
the user application to understand the call and return mechanism.

### Register Usage

In each of the architecture specific chapters, this subsection will detail the
set of registers which are *NOT* preserved across subroutine invocations. The
registers which are not preserved are assumed to be available for use as
scratch registers. Therefore, the contents of these registers should not be
assumed upon return from any RTEMS directive.

In some architectures, there may be a set of registers made available
automatically as a side-effect of the subroutine invocation mechanism.

### Parameter Passing

In each of the architecture specific chapters, this subsection will describe
the mechanism by which the parameters or arguments are passed by the caller to
a subroutine. In some architectures, all parameters are passed on the stack
while in others some are passed in registers.

### User-Provided Routines

All user-provided routines invoked by RTEMS, such as user extensions, device
drivers, and MPCI routines, must also adhere to these calling conventions.

## Memory Model

A processor may support any combination of memory models ranging from pure
physical addressing to complex demand paged virtual memory systems. RTEMS
supports a flat memory model which ranges contiguously over the processor's
allowable address space. RTEMS does not support segmentation or virtual memory
of any kind. The appropriate memory model for RTEMS provided by the targeted
processor and related characteristics of that model are described in this
chapter.

### Flat Memory Model

Most RTEMS target processors can be initialized to support a flat address
space. Although the size of addresses varies between architectures, on most
RTEMS targets, an address is 32-bits wide which defines addresses ranging from
0x00000000 to 0xFFFFFFFF (4 gigabytes). Each address is represented by a
32-bit value and is byte addressable. The address may be used to reference a
single byte, word (2-bytes), or long word (4 bytes). Memory accesses within
this address space may be performed in little or big endian fashion.

On smaller CPU architectures supported by RTEMS, the address space may only be
20 or 24 bits wide.

If the CPU model has support for virtual memory or segmentation, it is the
responsibility of the Board Support Package (BSP) to initialize the MMU
hardware to perform address translations which correspond to flat memory model.

In each of the architecture specific chapters, this subsection will describe
any architecture characteristics that differ from this general description.

## Interrupt Processing

Different types of processors respond to the occurrence of an interrupt in its
own unique fashion. In addition, each processor type provides a control
mechanism to allow for the proper handling of an interrupt. The processor
dependent response to the interrupt modifies the current execution state and
results in a change in the execution stream. Most processors require that an
interrupt handler utilize some special control mechanisms to return to the
normal processing stream. Although RTEMS hides many of the processor dependent
details of interrupt processing, it is important to understand how the RTEMS
interrupt manager is mapped onto the processor's unique architecture.

RTEMS supports a dedicated interrupt stack for all architectures. On
architectures with hardware support for a dedicated interrupt stack, it will be
initialized such that when an interrupt occurs, the processor automatically
switches to this dedicated stack. On architectures without hardware support
for a dedicated interrupt stack which is separate from those of the tasks,
RTEMS will support switching to a dedicated stack for interrupt processing.

Without a dedicated interrupt stack, every task in the system must have enough
stack space to accommodate the worst case stack usage of that particular task
and the interrupt service routines combined. By supporting a dedicated
interrupt stack, RTEMS significantly lowers the stack requirements for each
task.

A nested interrupt is processed similarly with the exception that since the CPU
is already executing on the interrupt stack, there is no need to switch to the
interrupt stack.

The interrupt stacks (one for each configured processor) are statically
allocated by the application configuration via `<rtems/confdefs.h>` in the
special section `.rtemsstack`. This enables an optimal placement of the
interrupt stacks by the Board Support Package (BSP), e.g. a fast on-chip
memory. The amount of memory allocated for each interrupt stack is user
configured and based upon the `<rtems/confdefs.h>` parameter
`CONFIGURE_INTERRUPT_STACK_SIZE`. This parameter is described in detail in
the Configuring a System chapter of the User's Guide. Since interrupts are
disabled during the sequential system initialization and the
`_Thread_Start_multitasking()` function does not return to the caller each
interrupt stack may be used for the initialization stack on the corresponding
processor.

In each of the architecture specific chapters, this section discusses the
interrupt response and control mechanisms of the architecture as they pertain
to RTEMS.

### Vectoring of an Interrupt Handler

In each of the architecture specific chapters, this subsection will describe
the architecture specific details of the interrupt vectoring process. In
particular, it should include a description of the Interrupt Stack Frame (ISF).

### Interrupt Levels

In each of the architecture specific chapters, this subsection will describe
how the interrupt levels available on this particular architecture are mapped
onto the 255 reserved in the task mode. The interrupt level value of zero (0)
should always mean that interrupts are enabled.

Any use of an interrupt level that is is not undefined on a particular
architecture may result in behavior that is unpredictable.

### Disabling of Interrupts by RTEMS

During the execution of directive calls, critical sections of code may be
executed. When these sections are encountered, RTEMS disables all external
interrupts before the execution of this section and restores them to the
previous level upon completion of the section. RTEMS has been optimized to
ensure that interrupts are disabled for the shortest number of instructions
possible. Since the precise number of instructions and their execution time
varies based upon target CPU family, CPU model, board memory speed, compiler
version, and optimization level, it is not practical to provide the precise
number for all possible RTEMS configurations.

Historically, the measurements were made by hand analyzing and counting the
execution time of instruction sequences during interrupt disable critical
sections. For reference purposes, on a 16 Mhz Motorola MC68020, the maximum
interrupt disable period was typically approximately ten (10) to thirteen (13)
microseconds. This architecture was memory bound and had a slow bit scan
instruction. In contrast, during the same period a 14 Mhz SPARC would have a
worst case disable time of approximately two (2) to three (3) microseconds
because it had a single cycle bit scan instruction and used fewer cycles for
memory accesses.

If you are interested in knowing the worst case execution time for a particular
version of RTEMS, please contact OAR Corporation and we will be happy to
product the results as a consulting service.

Non-maskable interrupts (NMI) cannot be disabled, and ISRs which execute at
this level MUST NEVER issue RTEMS system calls. If a directive is invoked,
unpredictable results may occur due to the inability of RTEMS to protect its
critical sections. However, ISRs that make no system calls may safely execute
as non-maskable interrupts.

## Symmetric Multiprocessing

This section contains information about the Symmetric Multiprocessing (SMP)
status of a particular architecture.

## Thread-Local Storage

In order to support thread-local storage (TLS) the CPU port must implement the
facilities mandated by the application binary interface (ABI) of the CPU
architecture. The CPU port must initialize the TLS area in the
`_CPU_Context_Initialize()` function. There are support functions available
via `#include <rtems/score/tls.h>` which implement Variants I and II
according to {cite}`Drepper:2013:TLS`.

`_TLS_TCB_at_area_begin_initialize()`
: Uses Variant I, TLS offsets emitted by linker takes the TCB into account.
  For a reference implementation see {file}`cpukit/score/cpu/arm/cpu.c`.

`_TLS_TCB_before_TLS_block_initialize()`
: Uses Variant I, TLS offsets emitted by linker neglects the TCB. For a
  reference implementation see
  {file}`c/src/lib/libcpu/powerpc/new-exceptions/cpu.c`.

`_TLS_TCB_after_TLS_block_initialize()`
: Uses Variant II. For a reference implementation see
  {file}`cpukit/score/cpu/sparc/cpu.c`.

The board support package (BSP) must provide the following sections and symbols
in its linker command file:

```c
.tdata : {
  _TLS_Data_begin = .;
  *(.tdata .tdata.* .gnu.linkonce.td.*)
  _TLS_Data_end = .;
}
.tbss : {
  _TLS_BSS_begin = .;
  *(.tbss .tbss.* .gnu.linkonce.tb.*) *(.tcommon)
  _TLS_BSS_end = .;
}
_TLS_Data_size = _TLS_Data_end - _TLS_Data_begin;
_TLS_Data_begin = _TLS_Data_size != 0 ? _TLS_Data_begin : _TLS_BSS_begin;
_TLS_Data_end = _TLS_Data_size != 0 ? _TLS_Data_end : _TLS_BSS_begin;
_TLS_BSS_size = _TLS_BSS_end - _TLS_BSS_begin;
_TLS_Size = _TLS_BSS_end - _TLS_Data_begin;
_TLS_Alignment = MAX (ALIGNOF (.tdata), ALIGNOF (.tbss));
```

## CPU counter

The CPU support must implement the CPU counter interface. A CPU counter is
some free-running counter. It ticks usually with a frequency close to the CPU
or system bus clock. On some architectures the actual implementation is board
support package dependent. The CPU counter is used for profiling of low-level
functions. It is also used to implement two busy wait functions
`rtems_counter_delay_ticks()` and `rtems_counter_delay_nanoseconds()` which
may be used in device drivers. It may be also used as an entropy source for
random number generators.

The CPU counter interface uses a CPU port specific unsigned integer type
`CPU_Counter_ticks` to represent CPU counter values. The CPU port must
provide the following two functions

- `_CPU_Counter_read()` to read the current CPU counter value, and
- `_CPU_Counter_difference()` to get the difference between two CPU
  counter values.

## Interrupt Profiling

The RTEMS profiling needs support by the CPU port for the interrupt entry and
exit times. In case profiling is enabled via the RTEMS build configuration
option `RTEMS_PROFILING` set to True. The CPU port may provide
data for the interrupt entry and exit times of the outer-most
interrupt. The CPU port can feed interrupt entry and exit times with the
`_Profiling_Outer_most_interrupt_entry_and_exit()` function (`#include
<rtems/score/profiling.h>`). For an example please have a look at
{file}`cpukit/score/cpu/arm/arm_exc_interrupt.S`.

## Board Support Packages

An RTEMS Board Support Package (BSP) must be designed to support a particular
processor model and target board combination.

In each of the architecture specific chapters, this section will present a
discussion of architecture specific BSP issues. For more information on
developing a BSP, refer to *RTEMS BSP and Driver Guide* chapter titled
`Board Support Packages` in the *RTEMS Classic API Guide*.

### System Reset

An RTEMS based application is initiated or re-initiated when the processor is
reset or transfer is passed to it from a boot monitor or ROM monitor.

In each of the architecture specific chapters, this subsection describes the
actions that the BSP must take assuming the application gets control
when the microprocessor is reset.
