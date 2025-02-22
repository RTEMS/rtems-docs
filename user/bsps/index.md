% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 embedded brains GmbH & Co. KG

(bsps)=

# Board Support Packages

```{index} Board Support Packages
```

```{index} BSP
```

A Board Support Package or BSP is the software that glues a specific target or
board or piece of hardware to RTEMS so it's services are available to
applications.

RTEMS contains a large number of BSPs for commonly available simulators and
target hardware.

You can see the current BSP list in the RTEMS sources by asking RTEMS with:

```none
$ ./rtems-bsps
```

```{toctree}
bsps-aarch64
bsps-arm
bsps-i386
bsps-m68k
bsps-microblaze
bsps-mips
bsps-moxie
bsps-nios2
bsps-or1k
bsps-powerpc
bsps-riscv
bsps-sparc
bsps-x86_64
```
