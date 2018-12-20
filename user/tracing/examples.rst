.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2018 Vidushi Vashishth <vidushivashishth96@gmail.com>
.. comment: All rights reserved.

.. _examples:

Tracing Examples
****************

The following example executes RTEMS trace using trace buffering for the
`fileio` sample testcase.

Features
--------

Tracing using trace buffering consists of the following sets of features:

- Individual entry and exit records.
- Task details such as CPU, current priority, real priority, task state and
  interrupt state.
- Nano-second timestamp.
- Interrupt safe buffer management.
- Function argument capture.
- Return value capture.
- Shell command support to report to the console, save a buffer, assess status
  of tracing, or view buffers between specified index ranges.

Prerequisites
-------------

1. Setup RTEMS for the `sparc/erc32` architecture-bsp pair to run the
   following example.
2. Download the fileio `configuration file <https://devel.rtems.org/attachment
   /wiki/Developer/Tracing/Trace_Buffering/fileio-trace.ini>`_ and store it on
   the top of the installed BSP's directory.
3. Change the value of the keys: `rtems-path` and `prefix` according to your
   rtems installation. The `rtems-path` is the path to the bsp installation
   and `prefix` is the path to the tools used to build rtems. Also set the
   value of the `rtems-bsp` key to `sparc/erc32`.

Demonstration
-------------

Inside the RTEMS build directory (the directory where the fileio configuration
has been stored) run the following commands to generate traces:

BSP is configured with the following command -

.. code:: shell

  ../rtems/configure --target=sparc-rtems5 --prefix=/development/rtems/5 \
  --enable-networking --enable-tests --enable-rtemsbsp=erc32 --enable-cxx

The next two commands are used to link the fileio executable.The `-B` option
signifies the use of the complete path to the required directory or file. Write
the full path instead of the path file: `sparc-rtems5/erc32/lib/` in the
following commands according to your installation. Also confirm the path of the
fileio's executable and object files in the last line of the command according
to your installation.

.. code:: shell

  sparc-rtems5-gcc -Bsparc-rtems5/erc32/lib/ \
  -specs bsp_specs -qrtems -mcpu=cypress -O2 -g -ffunction-sections \
  -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration \
  -Wstrict-prototypes -Wnested-externs -Wl,--gc-sections -mcpu=cypress \
  -o sparc-rtems5/c/erc32/testsuites/samples/fileio.exe sparc-rtems5/c/erc32/\
  testsuites/samples/fileio/fileio-init.o

This is the trace linker command to generate and compile the wrapper c file for
the application. The link command follows the escape sequence "--". "-C" option
denotes the name of the user configuration file and "-W" specifies the name of
the wrapper c file.

.. code:: shell

  rtems-tld -C fileio-trace.ini -W fileio-wrapper -- -Bsparc-rtems5/erc32/lib/ \
  -specs bsp_specs -qrtems -mcpu=cypress -O2 -g -ffunction-sections \
  -fdata-sections -Wall -Wmissing-prototypes -Wimplicit-function-declaration \
  -Wstrict-prototypes -Wnested-externs -Wl,--gc-sections -mcpu=cypress \
  -o sparc-rtems5/c/erc32/testsuites/samples/fileio.exe sparc-rtems5/c/erc32/\
  testsuites/samples/fileio/fileio-init.o

The following command is used to run the application. Hit enter key quickly and
type "s" and "root" and "pwd" to run the rtems shell. Use the `rtrace status`,
`rtrace trace` and `rtrace save` commands to know the status of the tracing,
display the contents of the trace buffer and save the buffer to disk in the form
of binary files. Use `rtrace -l` to list the availalble options for commands
with `rtrace`.

.. code:: shell

  sparc-rtems5-run sparc-rtems5/c/erc32/testsuites/samples/fileio.exe

The output from the above commands will be as follows:

.. code:: shell

  *** BEGIN OF TEST FILE I/O ***
  *** TEST VERSION: 5.0.0.de9b7d712bf5da6593386fd4fbca0d5f8b8431d8
  *** TEST STATE: USER_INPUT
  *** TEST BUILD: RTEMS_NETWORKING RTEMS_POSIX_API
  *** TEST TOOLS: 7.3.0 20180125 (RTEMS 5, RSB a3a6c34c150a357e57769a26a460c475e188438f, Newlib 3.0.0)
  Press any key to start file I/O sample (20s remaining)
  Press any key to start file I/O sample (19s remaining)
  Press any key to start file I/O sample (18s remaining)
  Press any key to start file I/O sample (17s remaining)
  Press any key to start file I/O sample (16s remaining)
  Press any key to start file I/O sample (15s remaining)
  Press any key to start file I/O sample (14s remaining)
   =========================
   RTEMS FILE I/O Test Menu
   =========================
     p -> part_table_initialize
     f -> mount all disks in fs_table
     l -> list  file
     r -> read  file
     w -> write file
     s -> start shell
     Enter your selection ==>s
  Creating /etc/passwd and group with four useable accounts:
    root/pwd
    test/pwd
    rtems/NO PASSWORD
    chroot/NO PASSWORD
  Only the root user has access to all available commands.
   =========================
     starting shell
   =========================

  Welcome to rtems-5.0.0 (SPARC/w/FPU/erc32)
  COPYRIGHT (c) 1989-2008.
  On-Line Applications Research Corporation (OAR).

  Login into RTEMS
  /dev/foobar login: root
  Password:

  RTEMS Shell on /dev/foobar. Use 'help' to list commands.
  SHLL [/] # rtrace status
  RTEMS Trace Bufferring: status
     Running:  yes
   Triggered:  yes
       Level:   0%
      Traces:   25
  SHLL [/] # rtrace stop
  RTEMS Trace Bufferring: stop
  SHLL [/] # rtrace trace
  RTEMS Trace Bufferring: trace
   Trace buffer: 0x20921d8
   Words traced: 1487
         Traces: 25
    0:00:40.983197010  2081910  0a010002 [  2/  2] > malloc((size_t) 00000130)
    0:00:40.983333119   136109  0a010002 [  2/  2] < malloc => (void*) 0x219bb88
    0:00:40.983471669   138550  0a010002 [  2/  2] > malloc((size_t) 00000006)
    0:00:40.983606557   134888  0a010002 [  2/  2] < malloc => (void*) 0x219bcc0
    0:00:40.983684682    78125  0a010002 [  2/  2] > malloc((size_t) 00000007)
    0:00:40.983819569   134887  0a010002 [  2/  2] < malloc => (void*) 0x219bcd0
    0:00:40.983909901    90332  0a010002 [  2/  2] > malloc((size_t) 000003fc)
    0:00:40.984046620   136719  0a010002 [  2/  2] < malloc => (void*) 0x219bce0
    0:00:40.986624137  2577517  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.986767569   143432  0a010003 [200/200] < malloc => (void*) 0x219bce0
    0:00:40.987531119   763550  0a010003 [200/200] > calloc((size_t) 00000001, (size_t) 0000005d)
    0:00:40.987603751    72632  0a010003 [200/200] > malloc((size_t) 0000005d)
    0:00:40.987744743   140992  0a010003 [200/200] < malloc => (void*) 0x219bce0
    0:00:40.987824699    79956  0a010003 [200/200] < calloc => (void*) 0x219bce0
    0:00:40.988302604   477905  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.988446647   144043  0a010003 [200/200] < malloc => (void*) 0x219bd48
    0:00:40.988667595   220948  0a010003 [200/200] > calloc((size_t) 00000001, (size_t) 00000080)
    0:00:40.988740837    73242  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.988884880   144043  0a010003 [200/200] < malloc => (void*) 0x219bdd0
    0:00:40.988964836    79956  0a010003 [200/200] < calloc => (void*) 0x219bdd0
    0:00:40.989042961    78125  0a010003 [200/200] > calloc((size_t) 00000001, (size_t) 00000080)
    0:00:40.989110100    67139  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.989254143   144043  0a010003 [200/200] < malloc => (void*) 0x219be58
    0:00:40.989334099    79956  0a010003 [200/200] < calloc => (void*) 0x219be58
    0:00:40.990118401   784302  0a010003 [200/200] > calloc((size_t) 00000001, (size_t) 00000061)
    0:00:40.990176995    58594  0a010003 [200/200] > malloc((size_t) 00000061)
    0:00:40.990309441   132446  0a010003 [200/200] < malloc => (void*) 0x219bd48
    0:00:40.990384515    75074  0a010003 [200/200] < calloc => (void*) 0x219bd48
    0:00:40.990870355   485840  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.991011346   140991  0a010003 [200/200] < malloc => (void*) 0x219bee0
    0:00:40.991227411   216065  0a010003 [200/200] > calloc((size_t) 00000001, (size_t) 00000080)
    0:00:40.991296380    68969  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.991438593   142213  0a010003 [200/200] < malloc => (void*) 0x219bf68
    0:00:40.991514276    75683  0a010003 [200/200] < calloc => (void*) 0x219bf68
    0:00:40.991589349    75073  0a010003 [200/200] > calloc((size_t) 00000001, (size_t) 00000080)
    0:00:40.991653437    64088  0a010003 [200/200] > malloc((size_t) 00000080)
    0:00:40.991794428   140991  0a010003 [200/200] < malloc => (void*) 0x219bff0
    0:00:40.991871332    76904  0a010003 [200/200] < calloc => (void*) 0x219bff0
    0:00:40.992283320   411988  0a010003 [200/200] > malloc((size_t) 00000008)
  SHLL [/] # rtrace save fileio-trace.bin
  RTEMS Trace Bufferring: trace
     Trace File: fileio-trace.bin
     Trace buffer: 0x20921d8
     Words traced: 1487
         Traces: 25
  SHLL [/] #
