% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2024 Suraj Kumar

(prettyprinting)=

# Pretty Printing and GDB

```{index} Pretty printing and GDB
```

Pretty-printing in GDB refers to the customisation of the output format for
complex data structures during debugging sessions. By default, GDB may display
raw data that can be difficult to interpret, especially for intricate
structures. Pretty-printers are user-defined scripts that transform this raw
data into a more human-readable and informative format, making it easier for
developers to understand the current state of their application.

For instance, instead of showing the internal memory representation of a linked
list or a C++ STL Vector, a pretty-printer can display a user-friendly view of
the list's elements and structure. This enhanced visualization aids in quickly
identifying issues and comprehending the program's state without manually
parsing the data.

## Enabling Pretty-printing in RTEMS

Pretty-printing support in RTEMS has been made possible through a combination of
custom sections in the executable and Python scripts that register the necessary
pretty-printers. An overview of the setup is as follows:

1. *Custom section in executable*
   : To ensure that the pretty-printers are automatically loaded when debugging,
     a custom section named `.debug_gdb_scripts` is added to each executable
     being linked in RTEMS. This section contains a small assembly code snippet
     that, when the executable is loaded into GDB, automatically imports a Python
     script responsible for setting up the pretty-printers. You can dump the code
     present with the following command:

     ```shell
     arm-rtems@rtems-ver-major@-objdump -s -j .debug_gdb_scripts build/arm-rtems@rtems-ver-major@-xilinx_zynq_a9_qemu/iostream.exe
     ```
2. *Python script for Pretty-printer Registration*
   : The `pprinter.py` script, located in the `rtems` directory within the
     GDB Python directory, is imported and executed when the executable (and
     thereby, the custom section) is loaded. This script is responsible for
     registering all the pretty-printers defined for various RTEMS kernel
     structures, as well as `libstdcxx` printers (which are shipped and
     maintained by GCC).
