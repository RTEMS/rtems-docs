% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

# GDB and JTAG

```{index} GDB, JTAG, Testing
```

GDB with JTAG provides a low level way to runs tests on hardware with limited
resources. The RTEMS Tester runs and controls an instance of GDB per test and
GDB connects via the GDB remote protocol to a GDB server that interfaces to the
JTAG port of a target.

(fig-tester-gdb-jtag)=

```{figure} ../../images/user/test-gdb-jtag.png
---
alt: RTEMS Tester using GDB and  JTAG
figclass: align-center
width: 35%
---
RTEMS Tester using GDB and JTAG
```

The Figure {ref}`fig-tester-gdb-jtag` shows the structure of RTEMS Testing
using GDB and JTAG. The executables are built and the `rtems-test` command is
run from the top of the build directory. The RTEMS Tester executes the BSP
architecture's GDB and expects the user to provide a `gdb-script` to connect
t the JTAG GDB server.
