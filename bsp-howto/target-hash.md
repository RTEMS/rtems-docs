% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2021 embedded brains GmbH & Co. KG

# Target Hash

Each BSP must provide an implementation of the {c:func}`rtems_get_target_hash`
directive. The
[default implementation](https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/bsps/shared/start/gettargethash-default.c)
is based on the CPU counter frequency. A BSP-specific implementation may be
provided which covers also for example the device tree, settings of the memory
controller, processor and bus frequencies, a serial number of a chip, etc. For
a BSP-specific implementation start with the default implementation and add
more values to the target hash using the functions {c:func}`_Hash_Add_data` and
{c:func}`_Hash_Add_string`. The target hash can be used to distinguish test
suite results obtained from different target systems.
