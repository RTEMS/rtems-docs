.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017 Chris Johns <chrisj@rtems.org>

RTEMS Symbols
=============

.. index:: Tools, rtems-syms

The RTEMS Symbols (:program:`rtems-syms`) command is an RTEMS tool to generate
symbol tables used by the RTEMS Runtime Loader (RTL). The symbol table contains
the exported base kernel symbols user code dynamically loaded can reference.

The RTEMS Runtime Loader supports two methods of loading a symbol table,
embedded and runtime loading. Embedding the table requires linking the symbol
table with the base image and runtime loading loads the table using the dynamic
loader when RTEMS is running.

.. sidebar:: *Filtering Symbols*

   Currently there is no filtering of symbols in the symbol table. This means
   all base kernel image symbols are present in the symbol table when only a
   sub-set of the symbols are referenced.

Embedding the symbol table creates self contained images. A target may not have
any external media, for example RTEMS tests, or there is a requirement to avoid
the management need to match the symbol table with the kernel base
image. Embedding the symbol table requires a 2-pass link process making the
application's build system more complicated.

A dynamically loadable symbol table is simpler to create however the symbol
table and the kernel base image must match or the behaviour is undefined. There
is currently no mechnanisum to ensure the symbol table and the kernel image
match The :program:`rtems-syms` command is run against the base kernel image
and the generated symbol table is installed on to the target hardware and
loaded before any other modules.

Symbol Table
------------

The symbol table is an ELF object file in the target's ELF format and is built
using the target's RTEMS C compiler. The :program:`rtems-syms` command searches
for the C compller under the prefix this command is installed under or the
system path. If the target's C compiler is not located in either of these paths
use the option ``-c`` or ``--cc`` to specify the path to the compiler.

The :program:`rtems-syms` command loads the base kernel image's ELF file and
reads the global or public symbols, creates a temporary C file and then
compiles it using the target's RTEMS C compiler. The command automatically
detects the architecture from the base kernel image's ELF file and uses it to
create the C compiler's name. The option ``-E`` or ``--exec-prefix`` can be
used to override the executable prefix used.

It is important to supply suitable C compiler flags (``cflags``) that match the
kernel image's so the symbol table can be linked or loaded.

2-Pass Linking
--------------

2-Pass linking is used to embed a symbol table in a base kernel image. The
first link pass is a normal RTEMS kernel link process. The link output is
passed to the :program:`rtems-syms` command and the ``-e`` or ``--embed``
option is used. The symbol table object file created by :program:`rtems-syms`
is added to the linker command used in the first pass to create the second
pass. The address map will change between the first pass and second pass
without causing a problem, the symbol table embedded in the second link pass
will adjust the symbol addresses to match.

Command
-------

:program:`rtems-syms` [options] kernel

.. option:: -V, --version

   Display the version information and then exit.

.. option:: -v, --verbose

   Increase the verbose level by 1. The option can be used more than once to
   get more detailed trace and debug information.

.. option:: -w, --warn

   Enable build warnings. This is useful when debugging symbol table
   generation.

.. option:: -k, --keep

   Do not delete temporary files on exit, keep them.

.. option:: -e, --embed

   Create a symbol table that can be embedded in the base kernel image using a
   2-pass link process.

.. option:: -S, --symc

   Specify the symbol's C source file. The defautl is to use a temporary file
   name.

.. option:: -o, --output

   Specify the ELF output file name.

.. option:: -m, --map

   Create a map file using the provided file name.

.. option:: -C, --cc

   Specify the C compile executable file name. The file can be absolute and no
   path is search or relative and the environment's path is searched.

.. option:: -E, --exec-prefix

   Specify the RTEMS tool prefix. For example for RTEMS 5 and the SPARC
   architecture the prefix is ``sparc-rtems5``.

.. option:: -c, --cflags

   Specify the C compiler flags used to build the symbol table with. These
   should be the same or compatible with the flags used to build the RTEMS
   kernel.

.. option:: -?, -h

   Reort the usage help.

Examples
--------

Create a dynamlically loaded symbol table for the ``minimum.exe`` sample
program for the ``i386/pc686`` BSP:

.. code-block:: shell

  $ rtems-syms -o ms.o i386-rtems5/c/pc686/testsuites/samples/minimum/minimum.exe
  $ file ms.o
  ms.o: ELF 32-bit LSB relocatable, Intel 80386, version 1 (SYSV), not stripped

Run the same command, this time create a map file:

.. code-block:: shell

  $ rtems-syms -o ms.o -m ms.map i386-rtems5/c/pc686/testsuites/samples/minimum/minimum.exe
  $ head -10 ms.map
  RTEMS Kernel Symbols Map
   kernel: i386-rtems5/c/pc686/testsuites/samples/minimum/minimum.exe

  Globals:
   No.  Index Scope      Type        SHNDX  Address    Size    Name
      0   931 STB_GLOBAL STT_OBJECT      11 0x0012df08       4 BSPBaseBaud   (minimum.exe)
      1  1124 STB_GLOBAL STT_OBJECT      11 0x0012d894       4 BSPPrintkPort   (minimum.exe)
      2   836 STB_GLOBAL STT_FUNC         1 0x00104b00     302 BSP_dispatch_isr   (minimum.exe)
      3  1156 STB_GLOBAL STT_FUNC         1 0x001082d0      92 BSP_install_rtems_shared_irq_handler   (minimum.exe)
      4   876 STB_GLOBAL STT_FUNC         1 0x00106500     138 BSP_outch   (minimum.exe)

Run the same command with a raise verbose level to observe the stages the
command performs:

.. code-block:: shell

  $ rtems-syms -vvv -o ms.o i386-rtems5/c/pc686/testsuites/samples/minimum/minimum.exe
  RTEMS Kernel Symbols 5.a72a462adc18
  kernel: i386-rtems5/c/pc686/testsuites/samples/minimum/minimum.exe
  cache:load-sym: object files: 1
  cache:load-sym: symbols: 1043
  symbol C file: /tmp/rld--X7paaa.c
  symbol O file: ms.o
  execute: i386-rtems5-gcc -O2 -c -o ms.o /tmp/rld--X7paaa.c
  execute: status: 0
