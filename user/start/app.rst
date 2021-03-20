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
     RTEMS Version                            : 5
     Architectures                            : sparc-rtems5
     Board Support Package (BSP)              : sparc-rtems5-erc32
     Show commands                            : no
     Long commands                            : no
     Checking for program 'sparc-rtems5-gcc'  : $BASE/rtems/5/bin/sparc-rtems5-gcc
     Checking for program 'sparc-rtems5-g++'  : $BASE/rtems/5/bin/sparc-rtems5-g++
     Checking for program 'sparc-rtems5-gcc'  : $BASE/rtems/5/bin/sparc-rtems5-gcc
     Checking for program 'sparc-rtems5-ld'   : $BASE/rtems/5/bin/sparc-rtems5-ld
     Checking for program 'sparc-rtems5-ar'   : $BASE/rtems/5/bin/sparc-rtems5-ar
     Checking for program 'sparc-rtems5-nm'   : $BASE/rtems/5/bin/sparc-rtems5-nm
     Checking for program 'sparc-rtems5-objdump' : $BASE/rtems/5/bin/sparc-rtems5-objdump
     Checking for program 'sparc-rtems5-objcopy' : $BASE/rtems/5/bin/sparc-rtems5-objcopy
     Checking for program 'sparc-rtems5-readelf' : $BASE/rtems/5/bin/sparc-rtems5-readelf
     Checking for program 'sparc-rtems5-strip'   : $BASE/rtems/5/bin/sparc-rtems5-strip
     Checking for program 'sparc-rtems5-ranlib'  : $BASE/rtems/5/bin/sparc-rtems5-ranlib
     Checking for program 'rtems-ld'             : $BASE/rtems/5/bin/rtems-ld
     Checking for program 'rtems-tld'            : $BASE/rtems/5/bin/rtems-tld
     Checking for program 'rtems-syms'           : $BASE/rtems/5/bin/rtems-syms
     Checking for program 'rtems-bin2c'          : $BASE/rtems/5/bin/rtems-bin2c
     Checking for program 'tar'                  : /usr/bin/tar
     Checking for program 'gcc, cc'              : $BASE/rtems/5/bin/sparc-rtems5-gcc
     Checking for program 'ar'                   : $BASE/rtems/5/bin/sparc-rtems5-ar
     Checking for program 'g++, c++'             : $BASE/rtems/5/bin/sparc-rtems5-g++
     Checking for program 'ar'                   : $BASE/rtems/5/bin/sparc-rtems5-ar
     Checking for program 'gas, gcc'             : $BASE/rtems/5/bin/sparc-rtems5-gcc
     Checking for program 'ar'                   : $BASE/rtems/5/bin/sparc-rtems5-ar
     Checking for c flags '-MMD'                 : yes
     Checking for cxx flags '-MMD'               : yes
     Compiler version (sparc-rtems5-gcc)         : 7.5.0 20191114 (RTEMS 5, RSB 5.1.0, Newlib fbaa096)
     Checking for a valid RTEMS BSP installation : yes
     Checking for RTEMS_DEBUG                    : no
     Checking for RTEMS_MULTIPROCESSING          : no
     Checking for RTEMS_NEWLIB                   : yes
     Checking for RTEMS_POSIX_API                : yes
     Checking for RTEMS_SMP                      : no
     Checking for RTEMS_NETWORKING               : no
     'configure' finished successfully (0.686s)

Build the application:

.. code-block:: none

    ./waf

The output will be something close to:

.. code-block:: none

    Waf: Entering directory `$BASE/app/hello/build/sparc-rtems5-erc32'
    [1/3] Compiling init.c
    [2/3] Compiling hello.c
    [3/3] Linking build/sparc-rtems5-erc32/hello.exe
    Waf: Leaving directory `$BASE/app/hello/build/sparc-rtems5-erc32'
    'build-sparc-rtems5-erc32' finished successfully (0.183s)

Run the executable:

.. code-block:: none

    $HOME/quick-start/rtems/6/bin/rtems-run --rtems-bsps=erc32-sis build/sparc-rtems6-erc32/hello.exe

The output will be something close to:

.. code-block:: none

    RTEMS Testing - Run, 5.1.0
     Command Line: $BASE/rtems/5/bin/rtems-run --rtems-bsps=erc32-sis build/sparc-rtems5-erc32/hello.exe
     Host: FreeBSD hihi 12.1-RELEASE-p2 FreeBSD 12.1-RELEASE-p2 GENERIC amd64
     Python: 3.7.6 (default, Jan 30 2020, 01:18:54) [Clang 6.0.1 (tags/RELEASE_601/final 335540)]
    Host: FreeBSD-12.1-RELEASE-p2-amd64-64bit-ELF (FreeBSD hihi 12.1-RELEASE-p2 FreeBSD 12.1-RELEASE-p2 GENERIC amd64 amd64)

     SIS - SPARC/RISCV instruction simulator 2.21,  copyright Jiri Gaisler 2019
     Bug-reports to jiri@gaisler.se

     ERC32 emulation enabled

     Loaded build/sparc-rtems5-erc32/hello.exe, entry 0x02000000

    Hello World

    *** FATAL ***
    fatal source: 5 (RTEMS_FATAL_SOURCE_EXIT)
    fatal code: 0 (0x00000000)
    RTEMS version: 5.1.0
    RTEMS tools: 7.5.0 20191114 (RTEMS 5, RSB 5.1.0, Newlib fbaa096)
    executing thread ID: 0x08a010001
    executing thread name: UI1
    cpu 0 in error mode (tt = 0x101)
       107883  0200b6c0:  91d02000   ta  0x0
    Run time     : 0:00:01.011474

Commit the application to the repository:

.. code-block:: none

    git add init.c hello.c wscript
    git commit -m "My first RTEMS application."
