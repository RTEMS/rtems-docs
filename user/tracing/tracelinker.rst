.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _TraceLinker:

Trace Linker
************

RTEMS trace linker is a post link tool central to the RTEMS trace framework. It
is installed as a part of the RTEMS Tool Project. The RTEMS Trace Linker is a
post link tool that performs a re-link of your application to produce a trace
executable. A trace executable has been instrumented by the RTEMS Trace Linker
with additional code that implements software tracing. A key requirement of the
trace process in RTEMS is to take existing code in a compiled format (ELF) and
instrument it without rebuilding that code from source and without annotating
that source with trace code.

Command Line
============

A typical command to invoke the trace linker consists of two parts separated by
``--``.  The first part controls the trace linker and provides the various
options it needs and the second part is a standard linker command line you would
use to link an RTEMS application. The current command line for trace linker
consists of:

.. code-block:: none

  $ rtems-tld -h
  rtems-trace-ld [options] objects
  Options and arguments:
   -h          : help (also --help)
   -V          : print linker version number and exit (also --version)
   -v          : verbose (trace import parts), can supply multiple times
                 to increase verbosity (also --verbose)
   -w          : generate warnings (also --warn)
   -k          : keep temporary files (also --keep)
   -c compiler : target compiler is not standard (also --compiler)
   -l linker   : target linker is not standard (also --linker)
   -E prefix   : the RTEMS tool prefix (also --exec-prefix)
   -f cflags   : C compiler flags (also --cflags)
   -r path     : RTEMS path (also --rtems)
   -B bsp      : RTEMS arch/bsp (also --rtems-bsp)
   -W wrapper  : wrapper file name without ext (also --wrapper)
   -C ini      : user configuration INI file (also --config)
   -P path     : user configuration INI file search path (also --path)

The trace linker generates code that needs to be compiled and linked to the
application executable so it needs to know the target compiler and `CFLAGS`.
There are a couple of ways to do this. The simplest is to provide the path to
RTEMS using the `-r` option and the architecture and BSP name in the standard
RTEMS format of arch/bsp. The trace linker will extract the compiler and flags
used to build RTEMS and will use them. If you require specific options you can
use the `-f`, `-c`, `-l`, and `-E` options to provide them. If the functions you
are tracing use types from your code then add the include path to the `CFLAGS`.

The trace linker requires you to provide a user configuration file using the
`-C` or ``--config`` option. This is an INI format file detailed in the
Configuration section. You can also provide an INI file search path using the
`-P` option.

If you are working with new configuration files and you want to view the files
the trace linker generates, add the `-k` option to keep the temporary files, and
`-W` to specify an explicit wrapper C file name. If you set the
``dump-on-error`` option in the configuration options section you will get a
dump of the configuration on an error.

Configuration (INI) files
=========================

The Trace Linker is controlled using configuration files. Configuration files
are categorized into 3 types:

- User Configuration: These are specific to the user application to be traced.
  This file initializes the values of the trace generator, triggers, enables,
  and traces.

- Tracer Configuration: These are like a library of common or base trace
  functions that can be referenced by an application. These files tend to hold
  the details needed to wrap a specific set of functions. Examples provided with
  the RTEMS Linker are the RTEMS API and Libc.

- Generator Configuration: This is used to encapsulate a specific method of
  tracing. RTEMS currently provides generators for trace buffering, printk, and
  printf.

The configuration files are in the *INI file format* which is composed of
`sections`. Each section has a section name and set of *keys* which consist of
*names* and *values*. A typical key is of the form ``name=value``. Keys can be
used to include other INI files using the include key name. This is shown in the
following example where the values indicate rtems and rtld-base configuration
files:

.. code-block:: ini

  include = rtems.ini, rtld-base.ini

The trace linker also uses values in keys to specify other sections. In this
example the functions name lists `test-trace-funcs` and that section contains a
headers key that further references a section called `test-headers`:

.. code-block:: ini

  functions = test-trace-funcs, rtems-api

  [test-trace-funcs]
  ; Parsed via the 'function-set', not parse as a 'trace'.
  headers = test-headers

  [test-headers]
  header = '#include "test-trace-1.h"'

The format of a configuration file is explained next. Snippets of the file:
`test-trace.ini` have been used for explicit understanding. This file can
be found in the rtems-tools directory of the rtems installation.

Tracer Section
--------------

The topmost level section is the ``tracer`` section. It can contains the
following keys:

- ``name``: The name of trace being linked.

- ``options``: A list of option sections.

- ``defines``: A list of sections containing defines or define record.

- ``define``: A list of define string that are single or double quoted.

- ``enables``: The list of sections containing enabled functions to trace.

- ``triggers``: The list of sections containing enabled functions to trigger
  trace on.

- ``traces``: The list of sections containing function lists to trace.

- ``functions``: The list of sections containing function details.

- ``include``: The list of files to include.

The tracer section of the file:`test-trace.ini` is shown below with explanatory
comments.

.. code-block:: ini

  ;
  ; RTEMS Trace Linker Test Configuration.
  ;
  ; We must provide a top level trace section.
  ;
  [tracer]
  ;
  ; Name of the trace.
  ;
  name = RTEMS Trace Linker Test
  ;
  ; The BSP.
  ;
  bsp = sparc/sis
  ;
  ; Functions to trace.
  ;
  traces = test-trace, test-trace-funcs, rtems-api-task
  ;
  ; Specify the options.
  ;
  options = test-options
  ;
  ; Define the function sets. These are the function's that can be
  ; added to the trace lists.
  ;
  functions = test-trace-funcs, rtems-api
  ;
  ; Include RTEMS Trace support.
  ;
  include = rtems.ini, rtld-base.ini

Options section
---------------

The options section in the fileio-trace.ini is called the `fileio-options`. A
general options section can contain following sets of keys:

- ``dump-on-error``: Dump the parsed configuration data on error. The value can
  be true or false.

- ``verbose``: Set the verbose level. The value can be true or a number value.

- ``prefix``: The prefix for the tools and an install RTEMS if rtems-path is not
  set.

- ``cc``: The compiler used to compile the generated wrapper code. Overrides the
  BSP configuration value if a BSP is specified.

- ``ld``: The linker used to link the application. The default is the cc value
  as read from the BSP configuration if specified. If your application contains
  C++ code use this setting to the change the linker to g++.

- ``cflags``: Set the CFLAGS used to compiler the wrapper. These flags are
  pre-pended to the BSP read flags if a BSP is specified. This option is used
  to provide extra include paths to header files in your application that
  contain types referenced by functions being traced.

- ``rtems-path``: The path to an install RTEMS if not installed under the
  prefix.

- ``rtems-bsp``: The BSP we are building the trace executable for. The is an
  arch and bsp pair. For example sparc/erc32.

The options section of the file: `test-trace.ini` uses two of the aforementioned
keys as shown below:

.. code-block:: ini

  ;
  ; Options can be defined here or on the command line.
  ;
  [test-options]
  prefix = /development/rtems/5
  verbose = true

Trace Section
-------------

A trace section defines how trace wrapper functions are built. To build a trace
function that wraps an existing function in an ELF object file or library
archive we need to have the function's signature. A signature is the function's
declaration with any types used. The signature has specific types and we need
access to those types which means the wrapper code needs to include header files
that define those types. There may also be specific defines needed to access
those types. A trace section can contain the following keys:

- ``generator``: The generator defines the type of tracing being used.

- ``headers``: List of sections that contain header file's keys.

- ``header``: A header key. Typically the include code.

- ``defines``: List of sections that contain defines.

- ``define``: A define key. Typically the define code.

- ``signatures``: List of function signature sections.

- ``trace``: Functions that are instrumented with trace code.

The trace section of the file: `test-trace.ini` is shown below. A trace section
can reference other trace sections of a specific type. This allows a trace
sections to build on other trace sections.

.. code-block:: ini

  ; User application trace example.
  ;
  [test-trace]
  generator = printf-generator
  ; Just here for testing.
  trace = test_trace_3

  [test-trace-funcs]
  ; Parsed via the 'function-set', not parse as a 'trace'.
  headers = test-headers
  header = '#include "test-trace-2.h"'
  defines = test-defines
  define = "#define TEST_TRACE_2 2"
  signatures = test-signatures
  ; Parsed via the 'trace', not parsed as a function-set
  trace = test_trace_1, test_trace_2

  [test-headers]
  header = '#include "test-trace-1.h"'

  [test-defines]
  define = "#define TEST_TRACE_1 1"

  [test-signatures]
  test_trace_1 = void, int
  test_trace_2 = test_type_2, test_type_1
  test_trace_3 = float, float*

Function Section
----------------

Function sections define functions that can be traced. Defining a function so it
can be traced does not mean it is traced. The function must be added to a trace
list to be traced. Function sections provide any required defines, header files,
and the function signatures.

A function signature is the function's declaration. It is the name of the
function, the return value, and the arguments. Tracing using function wrappers
requires that we have accurate function signatures and ideally we would like to
determine the function signature from the data held in ELF files. ELF files can
contain DWARF data, the ELF debugging data format. In time the trace project
would like to support libdwarf so the DWARF data can be accessed and used to
determine a function's signature. This work is planned but not scheduled to be
done and so in the meantime we explicitly define the function signatures in the
configuration files.

A function section can consist of the following keys:

- ``headers``: A list of sections containing headers or header records.
- ``header``: A list of include string that are single or double quoted.
- ``defines``: A list of sections containing defines or define record.
- ``defines``: A list of define string that are single or double quoted.
- ``signatures``: A list of section names of function signatures.
- ``includes``: A list of files to include.

Function signatures are specified with the function name being the key's name
and the key's value being the return value and a list of function arguments. You
need to provide void if the function uses void. Variable argument list are
currently not supported. There is no way to determine statically a variable
argument list. The function section in the file: `test-trace.ini` has been
labeled as `test-trace-funcs`. This can be seen in the file snippet of the
previous section.

Generators
----------

The trace linker's major role is to wrap functions in the existing executable
with trace code. The directions on how to wrap application functions is provided
by the generator configuration. The wrapping function uses a GNU linker option
called --wrap=symbol. The GNU Ld manual states:

"Use a wrapper function for symbol. Any undefined reference to symbol will be
resolved to __wrap_symbol. Any undefined reference to __real_symbol will be
resolved to symbol."

Generator sections specify how to generate trace wrapping code. The trace
linker and generator section must match to work. The trace linker expects a some
things to be present when wrapping functions. The section's name specifies the
generator and can be listed in a generator key in a tracer or trace section. If
the generator is not interested in a specific phase it does not need to define
it. Nothing will be generated in regard to this phase. For example code to
profile specific functions may only provide the entry-trace and exit-trace code
where a nano-second time stamp is taken.

The generate code will create an entry and exit call and the generator code
block can be used to allocate buffer space for each with the lock held. The
entry call and argument copy is performed with the lock released. The buffer
space having been allocated will cause the trace events to be in order. The same
goes for the exit call. Space is allocated in separate buffer allocate calls so
the blocking calls will have the exit event appear in the correct location in
the buffer.

The following keys can be a part of the generator configuration:

- ``headers``: A list of sections containing headers or header records.
- ``header``: A list of include string that are single or double quoted.
- ``defines``: A list of sections containing defines or define record.
- ``define``: A list of define string that are single or double quoted.
- ``entry-trace``: The wrapper call made on a function's entry. Returns bool
  where true is the function is being traced. This call is made without the lock
  being held if a lock is defined.
- ``arg-trace``: The wrapper call made for each argument to the trace function
  if the function is being traced. This call is made without the lock being held
  if a lock is defined.
- ``exit-trace``: The wrapper call made after a function's exit. Returns bool
  where true is the function is being traced. This call is made without the lock
  being held if a lock is defined.
- ``ret-trace``: The wrapper call made to log the return value if the function
  is being traced. This call is made without the lock being held if a lock is
  defined.
- ``lock-local``: The wrapper code to declare a local lock variable.
- ``lock-acquire``: The wrapper code to acquire the lock.
- ``lock-release``: The wrapper code to release the lock.
- ``buffer-local``: The wrapper code to declare a buffer index local variable.
- ``buffer-alloc``: The wrapper call made with a lock held if defined to
  allocate buffer space to hold the trace data. A suitable 32bit buffer index is
  returned. If there is no space an invalid index is returned. The generator
  must handle any overhead space needed. The generator needs to make sure the
  space is available before making the alloc all.
- ``code-blocks``: A list of code block section names.
- ``code``: A code block in <<CODE --- CODE (without the single quote).
- ``includes``: A list of files to include.

The following macros can be used in wrapper calls:

- ``@FUNC_NAME@``: The trace function name as a quote C string.
- ``@FUNC_INDEX@``: The trace function index as a held in the sorted list of
  trace functions by the trace linker. It can be used to index the names,
  enables, and triggers data.
- ``@FUNC_LABEL@``: The trace function name as a C label that can be referenced.
  You can take the address of the label.
- ``@FUNC_DATA_SIZE@``: The size of the data in bytes.
- ``@FUNC_DATA_ENTRY_SIZE@``: The size of the entry data in bytes.
- ``@FUNC_DATA_RET_SIZE@``: The size of the return data in bytes.
- ``@ARG_NUM@``: The argument number to the trace function.
- ``@ARG_TYPE@``: The type of the argument as a C string.
- ``@ARG_SIZE@``: The size of the type of the argument in bytes.
- ``@ARG_LABEL@``: The argument as a C label that can be referenced.
- ``@RET_TYPE@``: The type of the return value as a C string.
- ``@RET_SIZE@``: The size of the type of the return value in bytes.
- ``@RET_LABEL@``: The return value as a C label that can be referenced.

The `buffer-alloc`, `entry-trace`, and `exit-trace` can be transformed using the
following macros:

- ``@FUNC_NAME@``
- ``@FUNC_INDEX@``
- ``@FUNC_LABEL@``
- ``@FUNC_DATA_SZIE@``
- ``@FUNC_DATA_ENTRY_SZIE@``
- ``@FUNC_DATA_EXIT_SZIE@``

The `arg-trace` can be transformed using the following macros:

- ``@ARG_NUM@``
- ``@ARG_TYPE@``
- ``@ARG_SIZE@``
- ``@ARG_LABEL@``

The `ret-trace` can be transformed using the following macros:

- ``@RET_TYPE@``
- ``@RET_SIZE@``
- ``@RET_LABEL@``

The file: `test-trace.ini` specifies ``printf-generator`` as its generator. This
section can be found in the file: `rtld-print.ini` in the rtems-tools directory
and is shown below:

.. code:: ini

  ;
  ; A printf generator prints to stdout the trace functions.
  ;
  [printf-generator]
  headers = printf-generator-headers
  entry-trace = "rtld_pg_printf_entry(@FUNC_NAME@, (void*) &@FUNC_LABEL@);"
  arg-trace = "rtld_pg_printf_arg(@ARG_NUM@, @ARG_TYPE@, @ARG_SIZE@, (void*) &@ARG_LABEL@);"
  exit-trace = "rtld_pg_printf_exit(@FUNC_NAME@, (void*) &@FUNC_LABEL@);"
  ret-trace = "rtld_pg_printf_ret(@RET_TYPE@, @RET_SIZE@, (void*) &@RET_LABEL@);"
  code = <<<CODE
  static inline void rtld_pg_printf_entry(const char* func_name,
                                          void*       func_addr)
  {
    printf (">>> %s (0x%08x)\n", func_name, func_addr);
  }
  static inline void rtld_pg_printf_arg(int         arg_num,
                                        const char* arg_type,
                                        int         arg_size,
                                        void*       arg)
  {
    const unsigned char* p = arg;
    int   i;
    printf (" %2d] %s(%d) = ", arg_num, arg_type, arg_size);
    for (i = 0; i < arg_size; ++i, ++p) printf ("%02x", (unsigned int) *p);
    printf ("\n");
  }
  static inline void rtld_pg_printf_exit(const char* func_name,
                                         void*       func_addr)
  {
    printf ("<<< %s (0x%08x)\n", func_name, func_addr);
  }
  static inline void rtld_pg_printf_ret(const char* ret_type,
                                        int         ret_size,
                                        void*       ret)
  {
    const unsigned char* p = ret;
    int   i;
    printf (" rt] %s(%d) = ", ret_type, ret_size);
    for (i = 0; i < ret_size; ++i, ++p) printf ("%02x", (unsigned int) *p);
    printf ("\n");
  }
  CODE

  [printf-generator-headers]
  header = "#include <stdio.h>"

The trace linker generates C code with a wrapper for each function to be
instrumented. The trace code generated is driven by the configuration INI files.

Development
===========

The Trace Linker is part of the RTEMS tools git repository available at :
https://git.rtems.org/rtems-tools
The RTEMS tools project utilizes the waf build system. Use the following
commands in the topmost build directory to build the tools project:

First we configure using:

.. code-block:: none

  $./waf configure --prefix=$HOME/development/rtems/5

Then we build and install using:

.. code-block:: none

  $./waf build install
