<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- Copyright (C) 2026 Wayne Michael Thornton (wmthornton-dev@outlook.com) -->

# Intel/AMD x86_64 Specific Information

This chapter discusses the Intel and AMD x86_64 (AMD64 / Intel 64) architecture dependencies in this port of RTEMS. This 64-bit architecture extends the traditional 32-bit i386/i686 family, providing a significantly enlarged 64-bit general-purpose register set, a 64-bit virtual address space, and mandatory floating-point and SIMD (SSE2) support as part of the baseline hardware specification.

For detailed information on the x86_64 processor architecture, refer to the following documents:

- AMD64 Architecture Programmer's Manual Volume 1: Application Programming, Advanced Micro Devices.
- AMD64 Architecture Programmer's Manual Volume 2: System Programming, Advanced Micro Devices.
- AMD64 Architecture Programmer's Manual Volume 3: General-Purpose and System Instructions, Advanced Micro Devices.
- Intel 64 and IA-32 Architectures Software Developer's Manual Volume 1: Basic Architecture, Intel.
- Intel 64 and IA-32 Architectures Software Developer's Manual Volume 3: System Programming Guide, Intel.
- System V Application Binary Interface AMD64 Architecture Processor Supplement.

## CPU Model Dependent Features

This section presents the set of features which vary across x86_64 implementations and are of importance to RTEMS. The set of CPU model feature macros are defined in {file}`cpukit/score/cpu/x86_64/include/rtems/score/x86_64.h` based upon the particular CPU model and flags specified on the compilation command line.

### Hardware Floating Point and SIMD

Unlike the legacy i386 architecture where an x87 FPU or co-processor was optional, all x86_64 processors implement the x87 floating-point unit as well as MMX, SSE, and SSE2 instructions as a mandatory baseline. RTEMS utilizes SSE/SSE2 registers for floating-point math by default, aligning with the standard AMD64 ABI.

## Calling Conventions

### Processor Background

The x86_64 architecture supports a modernized call and return mechanism that heavily leverages the expanded register set to reduce stack traffic. A subroutine is invoked via the `callq` instruction, which pushes the 64-bit return address onto the stack. The return instruction (`retq`) pops the return address off the stack and transfers control to that instruction.

RTEMS on x86_64 adheres strictly to the System V AMD64 ABI. This calling convention dictates clear rules for register preservation, argument passing, and stack alignment.

### Calling Mechanism

All RTEMS directives are invoked using a `callq` instruction and return to the user application via the `retq` instruction.

### Register Usage

The x86_64 architecture provides sixteen 64-bit general-purpose registers: RAX, RBX, RCX, RDX, RSI, RDI, RBP, RSP, and R8 through R15. Under the System V ABI:

**Callee-saved registers:** RBX, RSP, RBP, R12, R13, R14, and R15 must be preserved across function calls. A directive or subroutine that utilizes these registers must back them up upon entry and restore them before returning.

**Caller-saved (scratch) registers:** RAX, RCX, RDX, RSI, RDI, R8, R9, R10, and R11 are not preserved by RTEMS directives. The contents of these registers should not be assumed to remain intact upon return from any directive.

### Parameter Passing

The System V AMD64 ABI passes the first six integer or pointer arguments in registers, making directive invocation significantly faster than legacy stack-pushed conventions:

| Argument | Register |
|----------|----------|
| First    | RDI      |
| Second   | RSI      |
| Third    | RDX      |
| Fourth   | RCX      |
| Fifth    | R8       |
| Sixth    | R9       |

Floating-point arguments are passed in XMM registers (XMM0 through XMM7).

If a directive or function requires more than six integer/pointer arguments, the additional arguments are pushed onto the stack from right to left (in reverse order) before executing the `callq` instruction.

Additionally, the calling convention mandates that the stack pointer (RSP) must be 16-byte aligned immediately before the `callq` instruction is executed. The `callq` instruction pushes an 8-byte return address, meaning that upon entry to the called function, RSP will be congruent to 8 modulo 16.

## Memory Model

### Flat Memory Model with Paging

Unlike the 32-bit i386 port where RTEMS runs in protected mode with paging disabled, the x86_64 architecture requires long mode, which architecturally mandates that hardware paging be enabled.

RTEMS supports the x86_64 long mode flat memory model. In this mode, segmentation is largely disabled by hardware; the base addresses for all code and data segment descriptors in the Global Descriptor Table (GDT) are forced to `0x0000000000000000` by the processor (with the exception of the FS and GS segments used for thread-local storage).

To implement a flat physical memory model while fulfilling the architectural requirement for paging, the RTEMS Board Support Package (BSP) initializes a 4-level (or 5-level) page table structure during startup. This page table typically performs an identity mapping (virtual address equals physical address) of the available system RAM and memory-mapped I/O devices, utilizing large pages (2MB or 1GB) to minimize Translation Lookaside Buffer (TLB) misses and reduce page table overhead.

The memory model supports a 64-bit virtual address space, though current hardware typically implements a 48-bit canonical addressing scheme, providing an addressable range of 256 terabytes.

## Interrupt Processing

Although RTEMS hides many of the processor-dependent details of interrupt processing, it is important to understand how the RTEMS interrupt manager is mapped onto the processor's unique architecture.

### Vectoring of Interrupt Handler

RTEMS and all user software execute at privilege level 0 (Ring 0). When an interrupt occurs, the x86_64 processor automatically performs the following actions in long mode:

1. Aligns the stack pointer (RSP) to a 16-byte boundary if an interrupt stack switch occurs.
2. Pushes the old Stack Segment (SS).
3. Pushes the old Stack Pointer (RSP).
4. Pushes the 64-bit RFLAGS register.
5. Pushes the old Code Segment (CS).
6. Pushes the 64-bit Instruction Pointer (RIP).
7. If the interrupt exception generates an error code, the hardware pushes the error code onto the stack last.
8. Vectors to the Interrupt Service Routine (ISR) via the 64-bit Interrupt Descriptor Table (IDT).

### Interrupt Stack Frame

The structure of the Interrupt Stack Frame for the x86_64 placed on the stack by the processor in response to an interrupt is as follows:

```
+----------------------+--------+
|        Old SS        | RSP+32 |
+----------------------+--------+
|       Old RSP        | RSP+24 |
+----------------------+--------+
|      Old RFLAGS      | RSP+16 |
+----------------------+--------+
|        Old CS        | RSP+8  |
+----------------------+--------+
|       Old RIP        | RSP    |
+----------------------+--------+
```

**Note:** If the hardware pushes an error code, all offsets above increase by 8 bytes, and the Error Code resides at RSP.

### Interrupt Levels

The x86_64 architecture supports two primary interrupt states: enabled and disabled. Interrupts are enabled when the Interrupt Enable Flag (IF) bit in the RFLAGS register is set. Conversely, interrupt processing is inhibited when the IF bit is cleared.

RTEMS maps interrupt levels 0 and 1 such that level zero (0) indicates that maskable interrupts are fully enabled (RFLAGS.IF = 1), and level one (1) indicates that maskable interrupts are disabled (RFLAGS.IF = 0). All other RTEMS interrupt levels are undefined. During a Non-Maskable Interrupt (NMI), all other interrupts are inhibited by hardware until the execution of the `iretq` instruction.

### Interrupt Stack and IST

The x86_64 architecture introduces an Interrupt Stack Table (IST) within the 64-bit Task State Segment (TSS). The IST provides up to seven dedicated hardware stack pointers.

RTEMS utilizes the IST to guarantee clean, non-nested interrupt handling without risking stack overflow on individual thread stacks. When an interrupt vector is configured in the IDT, it can be assigned to an IST index. Upon receiving the interrupt, the hardware automatically switches RSP to the clean interrupt stack defined in the IST before pushing the interrupt frame. When a non-nested interrupt returns via `iretq`, hardware automatically restores the interrupted thread's RSP.

## Symmetric Multiprocessing

RTEMS provides full Symmetric Multiprocessing (SMP) support for multiprocessor x86_64 systems. The architecture leverages the Advanced Programmable Interrupt Controller (APIC), consisting of Local APICs (LAPIC) integrated into each processor core and I/O APICs for routing external hardware interrupts.

### Bootstrapping Application Processors

In an SMP configuration, the system boots on a single processor known as the Bootstrap Processor (BSP). During initialization, the BSP enumerates the available CPU cores using ACPI tables (MADT) or Multiprocessor (MP) configuration tables.

To start the secondary cores—termed Application Processors (APs)—the BSP issues an INIT-SIPI-SIPI sequence via the Local APIC:

1. An INIT Inter-Processor Interrupt (IPI) resets the target AP.
2. A Startup IPI (SIPI) pointing to a physical memory address (below 1MB) containing real-mode 16-bit trampoline code is sent.
3. A second SIPI is sent to ensure reliable startup across varying hardware implementations.

The AP executes the trampoline code, transitions through protected mode into 64-bit long mode, sets up its local GDT, IDT, and TSS, and calls into the RTEMS SMP initialization framework to join the scheduler.

### Inter-Processor Interrupts (IPIs)

RTEMS uses APIC-generated IPIs to coordinate state across CPU cores. IPIs are essential for:

- Triggering thread preemption on remote cores when a higher-priority task becomes ready.
- Synchronizing Translation Lookaside Buffer (TLB) shootdowns across cores when memory mappings change.
- Initiating system-wide halt or fatal error states.

### SMP Synchronization and `_CPU_Spin_wait()`

In an SMP environment, the RTEMS executive relies on fine-grained spinlocks to protect system critical sections, task queues, and scheduler data structures. When a processor attempts to acquire a spinlock that is currently held by another core, it must enter a busy-waiting loop until the lock is released.

To optimize performance and prevent hardware degradation during these busy-wait cycles, RTEMS allows the developer to utilize the `_CPU_Spin_wait()` directive. On the x86_64 architecture, `_CPU_Spin_wait()` is implemented using the machine-level `pause` instruction (equivalent to `rep nop`).

```c
static inline void _CPU_Spin_wait( void )
{
  __asm__ volatile ( "pause" : : : "memory" );
}
```

The inclusion of `_CPU_Spin_wait()` inside spinlock wait loops provides three vital architectural benefits:

**Pipeline Optimization:** The `pause` instruction serves as an explicit hint to the processor that the executing code is in a spin-wait loop. Without this hint, the CPU continuously speculates and reorders instructions inside the tight loop. When the lock is finally released by the remote core, the memory order violation causes a severe pipeline flush, incurring a massive performance penalty.

**Power and Thermal Reduction:** By temporarily stalling the instruction pipeline for a few clock cycles, `_CPU_Spin_wait()` significantly reduces processor power consumption and heat generation during high-contention lock wait times.

**Memory Bus Contention Relief:** Throttling the execution rate of the read-compare loop reduces the frequency of cache line eviction and memory bus queries, leaving interconnect bandwidth available for the core currently holding the lock to finish its critical section faster.

## Thread-Local Storage

Thread-Local Storage (TLS) is supported. The x86_64 architecture utilizes the segmentation architecture's FS or GS segment base registers to point to the thread-local storage area.

In the RTEMS x86_64 port, the FS segment base address is dedicated to TLS. When a context switch occurs between threads, RTEMS updates the TLS base address for the incoming thread by writing the new pointer to the `MSR_FS_BASE` Model Specific Register (MSR) via the `wrmsr` instruction, or by using the faster unprivileged `wrfsbase` instruction if supported by the processor's feature set.

## Board Support Packages

### System Reset

An RTEMS-based application is initiated when the x86_64 processor is reset or booted via a bootloader (such as GRUB or Multiboot2). Upon hardware reset, the processor begins execution in 16-bit real mode with paging disabled:

- The EAX register contains the result of the processor's power-up self-test (BIST). A value of zero indicates a successful self-test.
- Control Register Zero (CR0) is set to real mode with paging disabled (CR0.PG = 0, CR0.PE = 0).
- The Extended Flags register (RFLAGS) is cleared, inhibiting all maskable interrupts.
- The Interrupt Descriptor Table Register (IDTR) is set to base address zero with a limit of `0xFFFF`.
- The Instruction Pointer (RIP) is set to `0xFFFFFFF0` (the reset vector), where an intersegment jump directs execution to the system BIOS or UEFI firmware initialization routines.

When booting via a Multiboot-compliant bootloader, the BSP typically enters the RTEMS application startup code in 32-bit protected mode with paging disabled, holding a pointer to the Multiboot information structure in the EBX/RBX register.

### Processor Initialization

The RTEMS initialization code is responsible for transitioning the processor from 32-bit protected mode into 64-bit long mode before invoking the executive initialization sequence. This transition requires a precise sequence of architectural operations:

1. **Page Table Setup:** The BSP allocates and initializes a hierarchical 4-level page table (PML4, Page Directory Pointer Table, Page Directory, and Page Table) mapping the kernel code, data segments, and physical memory.
2. **Physical Address Extension (PAE):** PAE must be enabled by setting bit 5 (CR4.PAE) in Control Register Four.
3. **Long Mode Enable (LME):** Bit 8 (LME) in the Extended Feature Enable Register (IA32_EFER) MSR is set using the `wrmsr` instruction.
4. **Paging Activation:** Paging and Protection are enabled simultaneously by setting the PG and PE bits in Control Register Zero (CR0). At this instant, the processor enters compatibility mode.
5. **GDT Initialization:** A 64-bit Global Descriptor Table is loaded using the `lgdt` instruction. A far jump (`jmp far`) is executed to reload the Code Segment (CS) register with a 64-bit code selector (where the L bit is set and the D bit is cleared), transitioning the CPU into full 64-bit Long Mode.
6. **IDT and TSS Setup:** The Interrupt Descriptor Table Register (IDTR) is loaded via `lidt` with a pointer to a 64-bit IDT containing 16-byte interrupt gate descriptors. A 64-bit Task State Segment is structured with valid Interrupt Stack Table pointers, and its selector is loaded into the Task Register (TR) via the `ltr` instruction.
7. **APIC Initialization:** The Local APIC is mapped and enabled, timer frequencies are calibrated, and spurious interrupt vectors are established.

Once the processor is executing in long mode with a valid 64-bit stack, paging active, and interrupts mapped, the startup code invokes the `boot_card()` or `initialize_executive` directive to begin RTEMS multitasking.

For more detailed information regarding x86_64 machine-specific data structures, memory mapping tables, and system instructions, refer to the AMD64 and Intel 64 System Programming Guides.