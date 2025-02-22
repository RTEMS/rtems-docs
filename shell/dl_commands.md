% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 Chris Johns <chrisj@rtems.org>

# Dynamic Loader

## Introduction

The RTEMS shell has the following dynamic loader commands:

- [rtl] - Manage the Run-Time Loader (RTL)

## Commands

This section details the Dynamic Loader Commands available. A subsection is
dedicated to each of the commands and describes the behavior and configuration
of that command as well as providing an example usage.

```{raw} latex
\clearpage
```

(rtl)=

### rtl - Manager the RTL

```{index} rtl
```

SYNOPSYS:
: ```none
  rtl [-l] -[h] command [...]
  ```

DESCRIPTION:

: This command manages the Run-time Loader (RTL) using a series of
  sub-commands. The sub-command selected determines what is displayed or the
  action taken. Sub-commands can have options that modified the behaviour of
  the specific command.

  The `-l` option lists the available commands and `-h` displays
  a simple help message.

  The commands are:

  > - [list][rtl-list] : Listings
  > - [sym][rtl-sym] : Symbols
  > - [obj][rtl-obj] : Object files
  > - [ar][rtl-ar] : Archive files
  > - [call][rtl-call] : Call symbols
  > - [trace][rtl-trace] : Link-editor trace debugging

  ```{index} rtl list
  ```

  (rtl-list)=

  `list`:

  : List the loaded object files. The executable object file's full path is
    displayed. If the executable object file is loaded from an archive the
    archive is include in the path. If no options are provided only a list of
    the object file names is displayed.

    The command is:

    ```none
    rtl list [-nlmsdb] [name]
    ```

    The options are:

    `-n`

    : Display all the name fields.

    `-l`

    : Long display the RTL's fields:

      - `unresolved` - number of unresolved symbols
      - `users` - number of users, ie times loaded
      - `references` - number of referencs to symbols
      - `symbols` - number of symbols
      - `symbol memory` - amount of symbol memory

    `-m`

    : Display the memory map. The sections listed are:

      - `exec` - total memory allocated
      - `text` - size of the executable code resident
      - `const` - size of the constants or read-only memory
      - `data` - size of the initialised data memory
      - `bss` - size of the uninitialised data memory

    `-s`

    : Display the local symbols present in the listed object file's symbol
      table. List the symbol's value.

    `-d`

    : Display the loaded object files that depend on symbols provided by this
      object file. The object file cannot be unloaded while there are
      references.

    `-b`

    : Include the base kernel image in the list of object modules. It is not
      included by default. If this option is included the base kernel module
      name of `rtems-kernel` can be used as a `name`.

    `name`

    : The optional `name` argument is a regular expression filter for the
      object files to list. The match is partial. If no name argument is
      provided all object modules are listed.

  ```{index} rtl sym
  ```

  (rtl-sym)=

  `sym`:

  : List symbols in the symbol table with their value. Symbols are grouped by
    the object file they reside in.

    The command is:

    ```none
    rtl sym [-bu] [-o name] [symbol]
    ```

    The options are:

    `-u`

    : List the system wide unresolved externals. Symbols are not displayed
      when displaying unresolved externals.

    `-o name`

    : Display the symbols for the matching object files. The name is a
      regular expression and it is a partial match.

    `-b`

    : Include the base kernel image in the list of object modules. It is not
      included by default. If this option is included the base kernel module
      name of `rtems-kernel` can be used as a `name`.

    `symbol`

    : The optional `symbol` argument is a regular expression filter for the
      symbols. The match is partial. If no symbol argument is provided all
      symbols and their values are displayed.

  ```{index} rtl obj
  ```

  (rtl-obj)=

  `obj`:

  : Manage object files. The sub-commands control the operation this command
    performs.

    The command is:

    ```none
    rtl obj [command] [...]
    ```

    `load <file>`

    : Load the executable object file specificed by the `<file>`
      argument. The `file` argument can be a file or it can be resided in
      archive file. The format is `archive:file`. The `archive` is file
      name of the archive and `file` is the file in the archive.

      If the `<file>` references symbols in known archive dependent object
      files in the available archives they are loaded.

    `unload <file>`

    : Unload the executable object file specificed by the `<file>`
      argument. The `<file>` argument can be the object files' name or it
      can be a complete name including the archive.

  ```{index} rtl ar
  ```

  (rtl-ar)=

  `ar`:

  : Display details about archives known to the link editor.

    The command is:

    ```none
    rtl ar [-lsd] [name]
    ```

    The options are:

    `-l`

    : Long display the RTL's archive fields:

      - `size` - size of the archive in the file system
      - `symbols` - number of symbols in the archive's symbol search table
      - `refs` - number of referencs to object files in the archive
      - `flags` - RTL specific flags

    `-s`

    : Display the symbols in the archive symbol tables

    `-d`

    : Display any duplicate symbols in any archives with the archive the
      instance of the symbol.

    `name`

    : The optional `name` argument is a regular expression filter for the
      archive files to list. The match is partial. If no name argument is
      provided all archives known to the link editor are listed.

  ```{index} rtl call
  ```

  (rtl-call)=

  `call`:

  : Call a symbol that resides in a code (`text`) section of an object
    file. Arguments can be passed and there is no return value support.

    There are no checks made on the signature of a symbol being called. The
    argument signature used needs to match the symbol being called or
    unpredictable behaviour may result.

    The reference count of the object file containing the symbol is
    increased while the call is active. The `-l` option locks the object
    by not lowering the reference count once the call completes. This is
    useful if the call starts a thread in the object file. The reference
    count cannot be lowered by the shell and the object file remains locked
    in memory.

    The call occurs on the stack of the shell so it is important to make
    sure there is sufficient space available to meet the needs of the call
    when configuring your shell.

    The call blocks the shell while it is active. There is no ability to
    background the call.

    If no arguments are provided the call signature is:

    ```none
    void call (void);
    ```

    If no options to specify a format are provided and there are arguments
    the call signature is the standard `argc/argv` call signature:

    ```none
    void call (int argc, const char* argv[]);
    ```

    The command is:

    ```none
    rtl call [-lsui] name [args]
    ```

    The options are:

    `-l`

    : Leave the object file the symbol resides in locked after the call
      returns.

    `-s`

    : Concatenate the `[args]` into a single string and pass as a single
      `const char*` argument. Quoted arguments are stripped or quotes and
      merged into the single string. The call signature is:

      ```none
      void call (const char* str);
      ```

    `-u`

    : Pass up to four unsigned integer `[args]` arguments. The symbol's
      call signature can have fewer than four arguments, the unreferenced
      arguments are ignored. The call signature is:

      ```none
      void call (unsigned int u1,
                 unsigned int u2,
                 unsigned int u3,
                 unsigned int u4);
      ```

    `-i`

    : Pass up to four integer `[args]` arguments. The symbol's call
      signature can have fewer than four arguments, the unreferenced
      arguments are ignored. The call signature is:

      ```none
      void call (int i1, int i2, int i3, int i4);
      ```

    `name`

    : The `name` argument is symbol name to find and call.

  ```{index} rtl trace
  ```

  (rtl-trace)=

  `trace`:

  : Clear or set trace flags. The trace flags provide details trace
    information from the link editor and can aid debugging. Note, some
    options can produce a large volume or output.

    The command is:

    ```none
    rtl trace [-l] [-h] [set/clear] flags...
    ```

    The options are:

    `-l`

    : List the available flags that can be cleared or set.

    `-?`

    : A `trace` command specific help

    The flags are:

    - `all`
    - `detail`
    - `warning`
    - `load`
    - `unload`
    - `section`
    - `symbol`
    - `reloc`
    - `global-sym`
    - `load-sect`
    - `allocator`
    - `unresolved`
    - `cache`
    - `archives`
    - `archive-syms`
    - `dependency`
    - `bit-alloc`

EXIT STATUS:

: This command returns 0 to indicate success else it returns 1.

NOTES:
: - Using this command may initialise the RTL manager if has not been used
    and initialised before now.
  - A base kernel image symbol file has to be present for base kernel symbols
    to be viewed and searched.

EXAMPLES:

: The following examples can be used with the testsuite's `dl10` test.

  Attempt to load an object file that not exist then load an object file that
  exists:

  ```none
  SHLL [/] # rtl obj load /foo.o
  error: load: /foo.o: file not found
  SHLL [/] $ rtl obj load /dl10-o1.o
  ```

  List the object files:

  ```none
  SHLL [/] # rtl list
   /dl10-o1.o
   /libdl10_1.a:dl10-o2.o
   /libdl10_2.a:dl10-o5.o
   /libdl10_2.a:dl10-o3.o
   /libdl10_1.a:dl10-o4.o
  ```

  The list shows the referenced archive object files that have been
  loaded. Show the details for the library object file `dl10-o2.o`:

  ```none
  SHLL [/] # rtl list -l dl10-o4.o
   /libdl10_1.a:dl10-o4.o
    unresolved    : 0
    users         : 0
    references    : 1
    symbols       : 7
    symbol memory : 250
  ```

  The object file has one reference, 7 symbols and uses 250 bytes of
  memory. List the symbols:

  ```none
  SHLL [/] # rtl list -s dl10-o4.o
   /libdl10_1.a:dl10-o4.o
     rtems_main_o4   = 0x20de818
     dl04_unresolv_1 = 0x20dead0
     dl04_unresolv_2 = 0x20dead4
     dl04_unresolv_3 = 0x20dead8
     dl04_unresolv_4 = 0x20deadc
     dl04_unresolv_5 = 0x20deaa0
     dl04_unresolv_6 = 0x20deac0
  ```

  The dependents of a group of object files can be listed using a regular
  expression:

  ```none
  SHLL [/] # rtl list -d dl10-o[234].o
   /libdl10_1.a:dl10-o2.o
    dependencies  : dl10-o3.o
   /libdl10_2.a:dl10-o3.o
    dependencies  : dl10-o4.o
                  : dl10-o5.o
   /libdl10_1.a:dl10-o4.o
    dependencies  : dl10-o5.o
  ```

  A number of flags can be selected at once:

  ```none
  SHLL [/] # rtl list -lmsd dl10-o1.o
   /dl10-o1.o
    exec size     : 1086
    text base     : 0x20dbec0 (352)
    const base    : 0x20dc028 (452)
    data base     : 0x20dc208 (12)
    bss base      : 0x20dc220 (266)
    unresolved    : 0
    users         : 1
    references    : 0
    symbols       : 9
    symbol memory : 281
      dl01_func1    = 0x20dbec0
      rtems_main_o1 = 0x20dbec8
      dl01_bss1     = 0x20dc220
      dl01_bss2     = 0x20dc224
      dl01_bss3     = 0x20dc2a0
      dl01_data1    = 0x20dc20c
      dl01_data2    = 0x20dc208
      dl01_const1   = 0x20dc1e8
      dl01_const2   = 0x20dc1e4
    dependencies  : dl10-o2.o
  ```

  List all symbols that contain `main`:

  ```none
  SHLL [/] # rtl sym main
   /dl10-o1.o
      rtems_main_o1 = 0x20dbec8
   /libdl10_1.a:dl10-o2.o
      rtems_main_o2 = 0x20dd1a0
   /libdl10_2.a:dl10-o5.o
      rtems_main_o5 = 0x20df280
   /libdl10_2.a:dl10-o3.o
      rtems_main_o3 = 0x20ddc40
   /libdl10_1.a:dl10-o4.o
      rtems_main_o4 = 0x20de818
  ```

  Include the base kernel image in the search:

  ```none
  SHLL [/] # rtl sym -b main
   rtems-kernel
      rtems_shell_main_cp      = 0x2015e9c
      rtems_shell_main_loop    = 0x201c2bc
      rtems_shell_main_monitor = 0x203f070
      rtems_shell_main_mv      = 0x201a11c
      rtems_shell_main_rm      = 0x201ad38
   /dl10-o1.o
      rtems_main_o1 = 0x20dbec8
   /libdl10_1.a:dl10-o2.o
      rtems_main_o2 = 0x20dd1a0
   /libdl10_2.a:dl10-o5.o
      rtems_main_o5 = 0x20df280
   /libdl10_2.a:dl10-o3.o
      rtems_main_o3 = 0x20ddc40
   /libdl10_1.a:dl10-o4.o
      rtems_main_o4 = 0x20de818
  ```

  The filter is a regular expression:

  ```none
  SHLL [/] # rtl sym -b ^rtems_task
   rtems-kernel
      rtems_task_create       = 0x2008934
      rtems_task_delete       = 0x20386b8
      rtems_task_exit         = 0x2008a98
      rtems_task_ident        = 0x2038738
      rtems_task_iterate      = 0x2038798
      rtems_task_self         = 0x20387b8
      rtems_task_set_priority = 0x20387c4
      rtems_task_start        = 0x2008b7c
      rtems_task_wake_after   = 0x2008bd0
  ```

  The search can be limited to a selection of object files:

  ```none
  SHLL [/] # rtl sym -o dl10-o[12].o dl01_b
   /dl10-o1.o
      dl01_bss1 = 0x20dc220
      dl01_bss2 = 0x20dc224
      dl01_bss3 = 0x20dc2a0
  SHLL [/] # rtl sym -o dl10-o[12].o dl0[12]_b
   /dl10-o1.o
      dl01_bss1 = 0x20dc220
      dl01_bss2 = 0x20dc224
      dl01_bss3 = 0x20dc2a0
   /libdl10_1.a:dl10-o2.o
      dl02_bss1 = 0x20dd400
      dl02_bss2 = 0x20dd404
      dl02_bss3 = 0x20dd420
  ```

  List the archives known to the link editor:

  ```none
  SHLL [/] # rtl ar
  /libdl10_1.a
  /libdl10_2.a
  ```

  A long listing of the archives provides the link editor details:

  ```none
  SHLL [/] # rtl ar -l
  /libdl10_1.a:
    size    : 37132
    symbols : 13
    refs    : 0
    flags   : 0
  /libdl10_2.a:
    size    : 53050
    symbols : 8
    refs    : 0
    flags   : 0
  ```

  ```{index} list archive symbols
  ```

  List the symbols an archive provides using the `-s` option:

  ```none
  SHLL [/] # rtl ar -s libdl10_1.a
  /libdl10_1.a:
    symbols : dl02_bss1
         dl02_bss2
         dl02_bss3
         dl02_data1
         dl02_data2
         dl04_unresolv_1
         dl04_unresolv_2
         dl04_unresolv_3
         dl04_unresolv_4
         dl04_unresolv_5
         dl04_unresolv_6
         rtems_main_o2
         rtems_main_o4
  ```

  ```{index} duplicate symbols
  ```

  List the duplicate symbols in the archives using the `-d` option:

  ```none
  SHLL [/] # rtl ar -d
  /libdl10_1.a:
    dups    :
  /libdl10_2.a:
    dups    : rtems_main_o5 (/libdl10_2.a)
  ```

  The link editor will list the first archive if finds that has the duplicate
  symbol.

  Call the symbol `rtems_main_o4` with no options:

  ```none
  SHLL [/] # rtl call rtems_main_o4
  dlo4: module: testsuites/libtests/dl10/dl-o4.c
  dlo4:   dl04_unresolv_1:    4: 0x20dee68: 0
  dlo4:   dl04_unresolv_2:    4: 0x20dee6c: %f
  dlo4:   dl04_unresolv_3:    1: 0x20dee70: 00
  dlo4:   dl04_unresolv_4:    4: 0x20dee74: 0
  dlo4:   dl04_unresolv_5:    4: 0x20dee38: 4
  dlo4:   dl04_unresolv_6:    4: 0x20dee58: dl-O4
  dlo5: module: testsuites/libtests/dl10/dl-o5.c
  dlo5:   dl05_unresolv_1:    8: 0x20df860: 0
  dlo5:   dl05_unresolv_2:    2: 0x20df868: 0
  dlo5:   dl05_unresolv_3:    4: 0x20df86c: 0
  dlo5:   dl05_unresolv_4:    1: 0x20df870: 0
  dlo5:   dl05_unresolv_5:    8: 0x20df878: 0
  ```

  Call a symbol in a data section of an object file:

  ```none
  SHLL [/] # rtl call dl04_unresolv_3
  error: symbol not in obj text: dl04_unresolv_3
  ```

  Call the symbol `rtems_main_o5` with a single string:

  ```none
  SHLL [/] # rtl call -s rtems_main_o5 arg1 arg2 "arg3 and still arg3" arg4
  dlo5: module: testsuites/libtests/dl10/dl-o5.c
  dlo5:   dl05_unresolv_1:    8: 0x20df860: 0
  dlo5:   dl05_unresolv_2:    2: 0x20df868: 0
  dlo5:   dl05_unresolv_3:    4: 0x20df86c: 0
  dlo5:   dl05_unresolv_4:    1: 0x20df870: 0
  dlo5:   dl05_unresolv_5:    8: 0x20df878: 0
  ```

  Note, the call does not have any argument and the strin passed is
  ignored.

  Call the symbol `rtems_main_o5` with three integer arguments:

  ```none
  SHLL [/] # rtl call -i rtems_main_o5 1 22 333
  dlo5: module: testsuites/libtests/dl10/dl-o5.c
  dlo5:   dl05_unresolv_1:    8: 0x20df860: 0
  dlo5:   dl05_unresolv_2:    2: 0x20df868: 0
  dlo5:   dl05_unresolv_3:    4: 0x20df86c: 0
  dlo5:   dl05_unresolv_4:    1: 0x20df870: 0
  dlo5:   dl05_unresolv_5:    8: 0x20df878: 0
  ```

```{index} rtems_rtl_shell_command
```

CONFIGURATION:

: This command is not included in the default shell command set. The command
  needs to be added with the shell's `rtems_shell_add_cmd`.

  ```c
  #include <rtems/rtl/rtl-shell.h>
  #include <rtems/shell.h>

  rtems_shell_init_environment ();

  if (rtems_shell_add_cmd ("rtl",
                           "rtl",
                           "rtl -?",
                           rtems_rtl_shell_command) == NULL)
    printf("error: command add failed\n");
  ```

PROGRAMMING INFORMATION:

: The `rtl` commanf is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_rtl_shell_command(
      int    argc,
      char **argv
  );
  ```

  The sub-command parts of the `rtl` command can be called directly. These
  calls all use the RTEMS Printer interface and as a result can be redirected
  and captured.

  ```{index} rtems_rtl_shell_list
  ```

  `list`

  : The RTL list command.

    ```c
    #include <rtems/rtl/rtl-shell.h>

    int rtems_rtl_shell_list (
        const rtems_printer* printer,
        int                  argc,
        char*                argv[]
    );
    ```

  ```{index} rtems_rtl_shell_object
  ```

  `sym`

  : The RTL symbol command.

    ```c
    #include <rtems/rtl/rtl-shell.h>

    int rtems_rtl_shell_sym (
        const rtems_printer* printer,
        int                  argc,
        char*                argv[]
    );
    ```

  ```{index} rtems_rtl_shell_object
  ```

  `sym`

  : The RTL object command.

    ```c
    #include <rtems/rtl/rtl-shell.h>

    int rtems_rtl_shell_object (
        const rtems_printer* printer,
        int                  argc,
        char*                argv[]
    );
    ```

  ```{index} rtems_rtl_shell_archive
  ```

  `ar`

  : The RTL object command.

    ```c
    #include <rtems/rtl/rtl-archive.h>

    int rtems_rtl_shell_archive (
        const rtems_printer* printer,
        int                  argc,
        char*                argv[]
    );
    ```

  ```{index} rtems_rtl_shell_call
  ```

  `call`

  : The RTL object command.

    ```c
    #include <rtems/rtl/rtl-archive.h>

    int rtems_rtl_shell_call (
        const rtems_printer* printer,
        int                  argc,
        char*                argv[]
    );
    ```
