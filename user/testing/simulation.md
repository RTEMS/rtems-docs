% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

# Simulation

```{index} Simulation, Testing
```

Simulation is a important regression and development tool for RTEMS. Developers
use simulation to work on core parts of RTEMS as it provides excellent
debugging supporting. Simulation run via the RTEMS Tester allows a test to run
on each core of your testing host machine lower the time to run all tests.

(fig-tester-simulation)=

```{figure} ../../images/user/test-simulation.png
:alt: RTEMS Tester Simulation
:figclass: align-center
:width: 30%

RTEMS Tester Simulation
```

The {ref}`fig-tester-simulation` figure shows the structure of RTEMS Testing
using simulation. The executables are built and the `rtems-test` command is
run from the top of the build directory. The RTEMS Tester executes the
BSP specific simulator for each test capturing the output
