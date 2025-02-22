% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Introduction

This document describes how to create or modify a Board Support Package (BSP)
for RTEMS, i.e. how to port RTEMS on a new microcontroller, system on chip
(SoC) or board. It is strongly recommended to notify the
[RTEMS development mailing](https://lists.rtems.org/mailman/listinfo/devel)
about any activity in this area and maybe also
[open an issue at](https://gitlab.rtems.org/rtems/rtos/rtems)
for specific work packages.

A basic BSP consists of the following components:

- Low-level initialization
- Console driver
- Clock driver
