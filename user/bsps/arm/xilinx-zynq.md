% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2015, 2020 Chris Johns (chrisj@rtems.org)

# xilinx-zynq

This BSP supports the Xilinx Zynq range of devices. This family of
devices contain the same ARM hard IP and the different parts have
different sizes of programable logic.

The BSP defaults may need to be adjusted using `configure` BSP
options to match the size of memory your board may have.

## Bootloader

The bootloader initialises the Zynq device. The Xilinx tool provide an
interface to configure the hardware. This is includes the buses,
clocks, memory and UART board rate. The output of this is called
`ps7_init` and it a C file. The Xilinx SDK builds a first stage boot
loader (FSBL) using this file.

The U-Boot boot loader has it's own FSBL called `MLO` to initialise
the hardware.

## Clocks

An application can provide a function called:

```none
uint32_t a9mpcore_clock_periphclk(void);
```

to return the peripheral clock. Normally this is half the CPU
clock. This function is declared `weak` so you can override the
default behaviour by providing it in your application.

## Console

The console driver for the UARTs will always be initialized to a
baud rate of 115200 with 8 bit characters, 1 stop bit and no parity
bits during start up.
Previous configurations programmed into the hardware by the Xilinx
tools or a bootloader will be overwritten.

The settings for the console driver can be changed by the user
application through the termios API afterwards.

## Network

The Cadence network interface driver of LibBSD works on the Xilinx Zynq
platform. The hardware checksum support works on real hardware but does not
seem to be supported on Qemu therefore the default state is to disable
`IFCAP_TXCSUM` and `IFCAP_RXCSUM` and this can be enabled from the shell
with:

```none
ifconfig cgem0 rxcsum txcsum
```

or with an `ioctl()` call to the network interface driver with `SIOCSIFCAP`
and the mask `IFCAP_TXCSUM` and `IFCAP_RXCSUM` set.

## Debugging with xilinx_zynq_a9_qemu

To debug an application add the QEMU options `-s`. If you need to
debug an initialisation issue also add `-S`. For example to debug a
networking application you could use:

```none
qemu-system-arm -M xilinx-zynq-a9 -m 256M -no-reboot -serial \
    null -serial mon:stdio -nographic \
    -net nic,model=cadence_gem -net vde,id=vde0,sock=/tmp/vde1 \
    -kernel myapp.exe \
    -s -S
```

Start GDB with the same executable QEMU is running and connect to the
QEMU GDB server:

```none
(gdb) target remote :1234
```

If your application is crashing set a breakpoint on the fatal error
handler:

```none
(gdb) b bsp_fatal_extension
```

Enter continue to run the application. Running QEMU loads the
executable and initialises the CPU. If the `-S` option is provided
the CPU is held in reset. Without the option the CPU runs starting
RTEMS. Either way you are connecting to set up target and all you need
to do is continue:

```none
(gdb) c
```

If you have a crash and the breakpoint on `bsp_fatal_extension` is
hit, load the following a GDB script:

```none
 define arm-crash
  set $code = $arg0
  set $r0 = ((const rtems_exception_frame *) $code)->register_r0
  set $r1 = ((const rtems_exception_frame *) $code)->register_r1
  set $r2 = ((const rtems_exception_frame *) $code)->register_r2
  set $r3 = ((const rtems_exception_frame *) $code)->register_r3
  set $r4 = ((const rtems_exception_frame *) $code)->register_r4
  set $r5 = ((const rtems_exception_frame *) $code)->register_r5
  set $r6 = ((const rtems_exception_frame *) $code)->register_r6
  set $r7 = ((const rtems_exception_frame *) $code)->register_r7
  set $r8 = ((const rtems_exception_frame *) $code)->register_r8
  set $r9 = ((const rtems_exception_frame *) $code)->register_r9
  set $r10 = ((const rtems_exception_frame *) $code)->register_r10
  set $r11 = ((const rtems_exception_frame *) $code)->register_r11
  set $r12 = ((const rtems_exception_frame *) $code)->register_r12
  set $sp = ((const rtems_exception_frame *) $code)->register_sp
  set $lr = ((const rtems_exception_frame *) $code)->register_lr
  set $pc = ((const rtems_exception_frame *) $code)->register_pc
  set $cpsr = ((const rtems_exception_frame *) $code)->register_cpsr
end
```

Enter the command:

```none
(gdb) arm-crash code
```

Enter `bt` to see the stack back trace.

The script moves the context back to the crash location. You should be
able to view variables and inspect the stack.

The fatal error handler runs inside an exception context that is not
the one than generated the exception.
