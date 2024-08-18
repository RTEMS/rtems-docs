.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 Suraj Kumar 

.. _Debugging:

Debugging
***********
.. index:: Debugging
.. index:: Embedded executable

Debugging is a critical process in software development that involves
identifying and resolving bugs or defects in a program. A debugger is a tool
that allows developers to inspect the internal state of a program while it runs
or after it crashes (like with a core dump), providing insights into the
program's execution flow and state.

A debugger allows us to:

#. Set breakpoints to pause execution at specific points
#. Step through code line-by-line or instruction by instruction 
#. Inspect/modify variables and memory 
#. Monitor a program's call stack and thread states


Debugging an RTEMS executable involves loading its code, data and read-only data
into the target system while a debugger on a host computer connects to it. The
debugger reads the ELF (Executable and Linkable Format) file to accesses the
embedded debug information.

To enable effective debugging, the executable must be build with compiler and
linker options that include debug information (the ``-g`` tag in GCC, for
example). Although this debug information increases the size of the ELF file, it
does not impact the binary footprint (loadable memory size) of the executable on
the target system. Target bootloaders and file conversion tools extract the
necessary binary code, data, and read-only data to create the file for the
target.

An ELF file with debug information contains DWARF (Debugging With Attributed
Record Formats) data. This detailed information allows the debugger to:

- Locate functions
- Find and inspect variables
- Understand the type and structure of different data
- Determine the entry code for every function call

With DWARF information, the debugger can set breakpoints, step through functions
or individual instructions, view data, and perform many other tasks critical for
debugging.

It is highly recommended to always enable compiler and linker debug options. An
ELF file with debug information is invaluable for post-mortem, such as
investigating a crash report from a production system, provided the production
ELF image is archived. The RTEMS toolchain includes utilities that can translate
an address from a crash dump into the corresponding source line and instruction.
The extra size of debug information is negligible on the host compared to the
significant benefits it provides for debugging.

Remote debugging is essential for embedded systems where the target hardware
might not be directly accessible from the host system. In this setup, an
additional component called a debug agent facilitates communication between the
debugger on the host and the target system. The following diagram illustrates
this setup:

.. _fig-exe-debug:

.. figure:: ../../images/user/exe-debug.png
   :width: 80%
   :alt: Embedded Executable Debugging
   :figclass: align-center

   Embedded Executable Debugging

A desktop or server operating system's kernel hosts the executable being
debugged, handling the interaction with the executable and the debugger. The
debugger knows how to communicate with the kernel to obtain the necessary
information. However, debugging an embedded executable requires an extra piece,
an agent, to connect the target to the debugger. The agent provides a standard
remote interface to the debugger and an agent-specific connection to the target.

The RTEMS tool chain provides the GNU debugger (GDB). GDB has a remote protocol
that can run over networks using TCP and UDP protocols. The GDB remote protocol
is available in a number of open-source and commercial debugging solutions.
Network debugging using the remote protocol helps set up an environment where
the targets can be remote from the developer's desktop, allowing for better
control of the target hardware while avoiding the need to plug devices into an
expensive desktop or server machine.

.. toctree::

   gdb 
   pretty-printing
