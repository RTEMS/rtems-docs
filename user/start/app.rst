.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 Chris Johns

.. _QuickStartAPP:

Build Your Application
======================

You tested a BSP in the previous section.  We built the ``erc32`` BSP
and it is installed under :file:`$HOME/quick-start/rtems/6`.

We will now create a simple Hello World application with a Git
repository and using the `Waf <https://waf.io>`_ build system.

The application is be created in :file:`$HOME/quick-start/app/hello`.

In the output in this section the base directory :file:`$HOME/quick-start` was
replaced by ``$BASE``.

The steps in this section assume you are in the directory
:file:`$HOME/quick-start/app/hello` after the first step changes to
it.

Setup the application work space. Create a new Git repository, download
the Waf build system, and the `RTEMS Waf
<https://git.rtems.org/rtems_waf.git/tree/README>`_.

Create the application directory and change into it:

.. code-block:: none

    mkdir -p $HOME/quick-start/app/hello
    cd $HOME/quick-start/app/hello

Download the Waf build system and set it to executable:

.. code-block:: none

    curl https://waf.io/waf-2.0.19 > waf
    chmod +x waf

Initialise a new Git repository:

.. code-block:: none

    git init

Add RTEMS Waf support as a Git sub-module and initialise it:

.. code-block:: none

    git submodule add git://git.rtems.org/rtems_waf.git rtems_waf

Create the application source files. Three files are created with an
editor of your choice.

First create a C file that configures RTEMS. Using an editor create a
file called :file:`init.c` and copy the following configuration
settings:

.. code-block:: c

    /*
     * Simple RTEMS configuration
     */

    #define CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
    #define CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER

    #define CONFIGURE_UNLIMITED_OBJECTS
    #define CONFIGURE_UNIFIED_WORK_AREAS

    #define CONFIGURE_RTEMS_INIT_TASKS_TABLE

    #define CONFIGURE_INIT

    #include <rtems/confdefs.h>

Create the Hello World application source file. Using an editor
create :file:`hello.c` and copy the follow code:

.. code-block:: c

    /*
     * Hello world example
     */
    #include <rtems.h>
    #include <stdlib.h>
    #include <stdio.h>

    rtems_task Init(
      rtems_task_argument ignored
    )
    {
      printf( "\nHello World\n" );
      exit( 0 );
    }

Finally create the Waf script. Using an editor create :file:`wscript`
and copy the Waf script:

.. code-block:: python

    #
    # Hello world Waf script
    #
    from __future__ import print_function

    rtems_version = "6"

    try:
        import rtems_waf.rtems as rtems
    except:
        print('error: no rtems_waf git submodule')
        import sys
        sys.exit(1)

    def init(ctx):
        rtems.init(ctx, version = rtems_version, long_commands = True)

    def bsp_configure(conf, arch_bsp):
        # Add BSP specific configuration checks
        pass

    def options(opt):
        rtems.options(opt)

    def configure(conf):
        rtems.configure(conf, bsp_configure = bsp_configure)

    def build(bld):
        rtems.build(bld)

        bld(features = 'c cprogram',
            target = 'hello.exe',
            cflags = '-g -O2',
            source = ['hello.c',
                      'init.c'])

Configure the application using Waf's ``configure`` command:

.. code-block:: none

    ./waf configure --rtems=$HOME/quick-start/rtems/6 --rtems-bsp=sparc/erc32

The output will be something close to:

.. code-block:: none

     Setting top to                           : $BASE/app/hello 
     Setting out to                           : $BASE/app/hello/build 
     RTEMS Version                            : 6 
     Architectures                            : sparc-rtems6 
     Board Support Package (BSP)              : sparc-rtems6-erc32 
     Show commands                            : no 
     Long commands                            : no 
     Checking for program 'sparc-rtems6-gcc'  : $BASE/rtems/6/bin/sparc-rtems6-gcc 
     Checking for program 'sparc-rtems6-g++'  : $BASE/rtems/6/bin/sparc-rtems6-g++ 
     Checking for program 'sparc-rtems6-gcc'  : $BASE/rtems/6/bin/sparc-rtems6-gcc 
     Checking for program 'sparc-rtems6-ld'   : $BASE/rtems/6/bin/sparc-rtems6-ld 
     Checking for program 'sparc-rtems6-ar'   : $BASE/rtems/6/bin/sparc-rtems6-ar 
     Checking for program 'sparc-rtems6-nm'   : $BASE/rtems/6/bin/sparc-rtems6-nm 
     Checking for program 'sparc-rtems6-objdump' : $BASE/rtems/6/bin/sparc-rtems6-objdump 
     Checking for program 'sparc-rtems6-objcopy' : $BASE/rtems/6/bin/sparc-rtems6-objcopy 
     Checking for program 'sparc-rtems6-readelf' : $BASE/rtems/6/bin/sparc-rtems6-readelf 
     Checking for program 'sparc-rtems6-strip'   : $BASE/rtems/6/bin/sparc-rtems6-strip 
     Checking for program 'sparc-rtems6-ranlib'  : $BASE/rtems/6/bin/sparc-rtems6-ranlib 
     Checking for program 'rtems-ld'             : $BASE/rtems/6/bin/rtems-ld 
     Checking for program 'rtems-tld'            : $BASE/rtems/6/bin/rtems-tld 
     Checking for program 'rtems-syms'           : $BASE/rtems/6/bin/rtems-syms 
     Checking for program 'rtems-bin2c'          : $BASE/rtems/6/bin/rtems-bin2c 
     Checking for program 'tar'                  : /usr/bin/tar 
     Checking for program 'gcc, cc'              : $BASE/rtems/6/bin/sparc-rtems6-gcc 
     Checking for program 'ar'                   : $BASE/rtems/6/bin/sparc-rtems6-ar 
     Checking for program 'g++, c++'             : $BASE/rtems/6/bin/sparc-rtems6-g++ 
     Checking for program 'ar'                   : $BASE/rtems/6/bin/sparc-rtems6-ar 
     Checking for program 'gas, gcc'             : $BASE/rtems/6/bin/sparc-rtems6-gcc 
     Checking for program 'ar'                   : $BASE/rtems/6/bin/sparc-rtems6-ar 
     Checking for c flags '-MMD'                 : yes 
     Checking for cxx flags '-MMD'               : yes 
     Compiler version (sparc-rtems6-gcc)         : 10.2.1 20210309 (RTEMS 6, RSB 5e449fb5c2cb6812a238f9f9764fd339cbbf05c2, Newlib d10d0d9) 
     Checking for a valid RTEMS BSP installation : yes 
     Checking for RTEMS_DEBUG                    : no 
     Checking for RTEMS_MULTIPROCESSING          : no 
     Checking for RTEMS_NEWLIB                   : yes 
     Checking for RTEMS_POSIX_API                : no 
     Checking for RTEMS_SMP                      : no 
     Checking for RTEMS_NETWORKING               : no 
     'configure' finished successfully (1.142s)
Build the application:

.. code-block:: none

    ./waf

The output will be something close to:

.. code-block:: none

    Waf: Entering directory `$BASE/app/hello/build/sparc-rtems6-erc32'
    [1/3] Compiling init.c
    [2/3] Compiling hello.c
    [3/3] Linking build/sparc-rtems6-erc32/hello.exe
    Waf: Leaving directory `$BASE/app/hello/build/sparc-rtems6-erc32'
    'build-sparc-rtems6-erc32' finished successfully (0.183s)

Run the executable:

.. code-block:: none

    $HOME/quick-start/rtems/6/bin/rtems-run --rtems-bsps=erc32-sis build/sparc-rtems-erc32/hello.exe

The output will be something close to:

.. code-block:: none

    RTEMS Testing - Run, 6.0.not_released
    Command Line: $BASE/quick-start/rtems/6/bin/rtems-run --rtems-bsps=erc32-sis build/sparc-rtems6-erc32/hello.exe
    Host: Linux  5.8.0-44-generic #50~20.04.1-Ubuntu SMP Wed Feb 10 21:07:30 UTC 2021 x86_64
    Python: 3.8.5 (default, Jan 27 2021, 15:41:15) [GCC 9.3.0]
    Host: Linux-5.8.0-44-generic-x86_64-with-glibc2.29 (Linux 5.8.0-44-generic #50~20.04.1-Ubuntu SMP Wed Feb 10 21:07:30 UTC 2021 x86_64 x86_64)

    SIS - SPARC/RISCV instruction simulator 2.26,  copyright Jiri Gaisler 2020
    Bug-reports to jiri@gaisler.se

    ERC32 emulation enabled

    Loaded build/sparc-rtems6-erc32/hello.exe, entry 0x02000000

    Hello World

    *** FATAL ***
    fatal source: 5 (RTEMS_FATAL_SOURCE_EXIT)
    fatal code: 0 (0x00000000)
    RTEMS version: 6.0.0.586e06ec6222f1cd1f005aa8f4a34a8b33f5d862
    RTEMS tools: 10.2.1 20210309 (RTEMS 6, RSB 5e449fb5c2cb6812a238f9f9764fd339cbbf05c2, Newlib d10d0d9)
    executing thread ID: 0x08a010001
    executing thread name: UI1 
    cpu 0 in error mode (tt = 0x101)
    158479  0200d500:  91d02000   ta  0x0
    Run time     : 0:00:00.259136

Commit the application to the repository:

.. code-block:: none

    git add init.c hello.c wscript
    git commit -m "My first RTEMS application."
