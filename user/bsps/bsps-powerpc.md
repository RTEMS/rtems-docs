% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 embedded brains GmbH & Co. KG

# powerpc (PowerPC)

## beatnik
The ``beatnik`` BSP supports the ``MVME5500`` and the ``MVME6100`` boards.

## gen5200

TODO.

## gen83xx

TODO.

## haleakala

TODO.

## motorola_powerpc

### Boot Image Generation

The application executable file (ELF file) must be converted to a boot
image. Use the following commands:

```none
powerpc-rtems@rtems-ver-major@-objcopy -O binary -R .comment -S ticker.exe rtems
gzip -9 -f rtems
powerpc-rtems@rtems-ver-major@-ld -o ticker.boot bootloader.o --just-symbols=ticker.exe -b binary rtems.gz -T ppcboot.lds -no-warn-mismatch
powerpc-rtems@rtems-ver-major@-objcopy -O binary ticker.boot ticker.bin
```

## mpc55xxevb

TODO.

## mpc8260ads

TODO.

## mvme3100

TODO.

## psim

TODO.

## qemuppc

TODO.

## qoriq (QorIQ)

The BSP for the [QorIQ](https://en.wikipedia.org/wiki/QorIQ) chip family
offers three variants. The `qoriq_e500` variant supports the P-series chips
such as P1020, P2010 and P2020. The `qoriq_e6500_32` (32-bit ISA) and
`qoriq_e6500_64` (64-bit ISA) variants support the T-series chips such as T2080
and T4240. The basic hardware initialization is not performed by the BSP. A
boot loader with device tree support must be used to start the BSP, e.g.
U-Boot.

The BSP is known to run on these boards:

- NXP P1020RDB
- MicroSys miriac MPX2020 (System on Module)
- Artesyn MVME2500 (VME64x SBC)
- NXP T2080RDB
- NXP T4240RDB
- MEN G52A (CompactPCI Serial)

The `qoriq_core_0` and `qoriq_core_1` variants should be used with care. They
are inteded for a `RTEMS_MULTIPROCESSING` configuration on the P1020.

### Boot via U-Boot

The application executable file (ELF file) must be converted to an U-Boot
image. Use the following commands:

```none
powerpc-rtems@rtems-ver-major@-objcopy -O binary app.exe app.bin
gzip -9 -f -c app.bin > app.bin.gz
mkimage -A ppc -O linux -T kernel -a 0x4000 -e 0x4000 -n RTEMS -d app.bin.gz app.img
```

Use the following U-Boot commands to boot an application via TFTP download:

```none
tftpboot ${loadaddr} app.img && run loadfdt && bootm ${loadaddr} - ${fdt_addr} ; reset
```

### Clock Driver

The clock driver uses two MPIC global timer (`QORIQ_CLOCK_TIMER` and
`QORIQ_CLOCK_TIMECOUNTER`). In case `QORIQ_IS_HYPERVISOR_GUEST` is
defined, then the PowerPC decrementer is used.

### Console Driver

The console driver supports the on-chip NS16550 compatible UARTs. In case
`QORIQ_IS_HYPERVISOR_GUEST` is defined, then the EPAPR byte channel is used
for the console device.

### Network Interface Driver

The network interface driver is provided by the `libbsd`. The DPAA is
supported including 10Gbit/s Ethernet.

### Topaz Hypervisor Guest

For a Topaz hypervisor guest configuration use:

```
../configure --enable-rtemsbsp=qoriq_e6500_32 \
    QORIQ_IS_HYPERVISOR_GUEST=1 \
    QORIQ_UART_0_ENABLE=0 \
    QORIQ_UART_1_ENABLE=0 \
    QORIQ_TLB1_ENTRY_COUNT=16
```

You may have to adjust the linker command file according to your partition
configuration.

## ss555

TODO.

## t32mppc

TODO.

## tqm8xx

TODO.

## virtex

TODO.

## virtex4

TODO.

## virtex5

TODO.
