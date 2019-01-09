.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017 Chris Johns <chrisj@rtems.org>

RTEMS Executable Infomation
===========================

.. index:: Tools, rtems-exeinfo

The RTEMS Executable Information (:program:`rtems-exeinfo`) command is an RTEMS
tool to display some important parts of an RTEMS executable. RTEMS uses ELF as
the final linker output and this tool displays useful RTEMS specific
information held in the ELF executable. The tool does not replace tools like
`readelf`, rather it focuses on reporting specific information RTEMS builds
into the executable.

System Initialisation
---------------------

Linker based system initialisation automatically lets RTEMS only link into the
executable the system initialisation code referenced by the user's application
or indirectly by RTEMS. The technique is a varation of the system
initialisation process used in the FreeBSD kernel. It is also similar to the
process used by the C++ language to run static constructors before entering
`main` and destructors after `exit` is called.

Linker based system initialisation collects the address of referenced system
initialisation functions in specially named sections. The system initialisation
function's address is placed in a variable and the section attribute of the
variable is set to a special section name. The linker is instructed via a
special linker command file to collect these variables together to create a
table. The start-up code in RTRMS loops over the table of addresses and calling
each address or system initialisation function. Special section names given to
the variables sorts the table placing the functions in a specific order.

A user places a call to an API function in their application and the linker
pulls the API code from the RTEMS kernel library adding it to the
executing. The API code the linker loads references the variable containing the
address of the that API's system initialisation function. The linker loads the
API system initialisation code into the executable to resolve the external
refernece created by the variable. If the user does not reference the API the
variables is loaded into the executable and no reference to the API system
initialisation code is made so it is not linked into the executable.

The design automatically creates a unique system intialisation table for each
executable and the code in RTEMS does not change, there is no special build
system tricks, or stub libraries.

The RTEMS Execuable Information reports the tables created and you can use this
information to debug any initialisation issues.

Command
-------

The :program:`rtems-exeinfo` tool reports RTEMS specific information about the
executable. The ``init`` and ``fini`` tables print the symbol referenced for
each table entry and if the symbol is from the C++ language it is demangled.

:program:`rtems-exeinfo`

.. option:: -V

   Display the version information and then exit.

.. option:: -v

   Increase the verbose level by 1. The option can be used more than once to
   get more detailed trace and debug information.

.. option:: -a

   Report all types of output data.

.. option:: -I

   Report the ``init`` or initialisation table.

.. option:: -F

   Report the ``fini`` or finialisation table.

.. option:: -S

   Report the sections.

.. option:: -?, -h

   Reort the usage help.

Examples
--------

Prints all reports for the ``hello.exe`` for the ``i386/pc686`` BSP:

.. code-block:: shell

  $ rtems-exeinfo -a i386-rtems5/c/pc686/testsuites/samples/hello/hello.exe
  RTEMS Executable Info 5.6f5cfada964c
   rtems-exeinfo -a i386-rtems5/c/pc686/testsuites/samples/hello/hello.exe
  exe: i386-rtems5/c/pc686/testsuites/samples/hello/hello.exe
  Sections: 22
                   -------------- addr: 0x00000000 0x00000000 size:          0 align:   0 relocs:      0
    .bss           WA------------ addr: 0x00135760 0x0013b300 size:      23456 align:  32 relocs:      0
    .comment       ---MS--------- addr: 0x00000000 0x00000083 size:        131 align:   1 relocs:      0
    .ctors         WA------------ addr: 0x0013322c 0x00133234 size:          8 align:   4 relocs:      0
    .data          WA------------ addr: 0x00133240 0x0013574c size:       9484 align:  32 relocs:      0
    .debug_abbrev  -------------- addr: 0x00000000 0x0003c5ce size:     247246 align:   1 relocs:      0
    .debug_aranges -------------- addr: 0x00000000 0x00003a18 size:      14872 align:   8 relocs:      0
    .debug_info    -------------- addr: 0x00000000 0x0032496d size:    3295597 align:   1 relocs:      0
    .debug_line    -------------- addr: 0x00000000 0x0006606b size:     417899 align:   1 relocs:      0
    .debug_loc     -------------- addr: 0x00000000 0x0003b704 size:     243460 align:   1 relocs:      0
    .debug_ranges  -------------- addr: 0x00000000 0x00008128 size:      33064 align:   1 relocs:      0
    .debug_str     ---MS--------- addr: 0x00000000 0x0001a9d7 size:     109015 align:   1 relocs:      0
    .dtors         WA------------ addr: 0x00133234 0x0013323c size:          8 align:   4 relocs:      0
    .eh_frame      -A------------ addr: 0x0012b884 0x0013222c size:      27048 align:   4 relocs:      0
    .fini          -AE----------- addr: 0x00127fdd 0x00127fe5 size:          8 align:   1 relocs:      0
    .init          -AE----------- addr: 0x00127fd0 0x00127fdd size:         13 align:   1 relocs:      0
    .rodata        -A------------ addr: 0x00128000 0x0012b884 size:      14468 align:  32 relocs:      0
    .rtemsroset    WA------------ addr: 0x00127f94 0x00127fd0 size:         60 align:   4 relocs:      0
    .shstrtab      -------------- addr: 0x00000000 0x000000c6 size:        198 align:   1 relocs:      0
    .strtab        -------------- addr: 0x00000000 0x000068ca size:      26826 align:   1 relocs:      0
    .symtab        -------------- addr: 0x00000000 0x00006290 size:      25232 align:   4 relocs:      0
    .text          WAE----------- addr: 0x00100000 0x00127f91 size:     163729 align:  16 relocs:      0

  Init sections: 3
   .ctors
    0xffffffff RamSize
    0x00000000 REG_EFLAGS
   .init
    0xfd81ebe8 no symbol
    0xff86e8ff no symbol
    0x00c2ffff no symbol
   .rtemsroset
    0x00100310 bsp_work_area_initialize
    0x00100440 bsp_start_default
    0x001160e0 _User_extensions_Handler_initialization
    0x0010fe60 rtems_initialize_data_structures
    0x0010fcf0 _RTEMS_tasks_Manager_initialization
    0x0010f310 _Semaphore_Manager_initialization
    0x0010ed90 _POSIX_Keys_Manager_initialization
    0x00113af0 _Thread_Create_idle
    0x0010c100 rtems_libio_init
    0x0010bec0 rtems_filesystem_initialize
    0x00100420 bsp_predriver_hook
    0x0010bfb0 _Console_simple_Initialize
    0x0010ff30 _IO_Initialize_all_drivers
    0x0010fc10 _RTEMS_tasks_Initialize_user_tasks_body
    0x0010ccb0 rtems_libio_post_driver

  Fini sections: 2
   .dtors
    0xffffffff RamSize
    0x00000000 REG_EFLAGS
   .fini
    0xfd815ee8 no symbol
    0x0000c2ff no symbol

The Init section ``.rtemsroset`` shows the initialisation call order for the
``hello.exe`` sample application. The order is initialise the BSP work area,
call the BSP start up, initialise the User extensions, initialise the RTEMS
data structures, then call the various Classic API managers that have been
linked into the application. Next any POSIX managers are initialisations, in
this case the POSIX Keys manager which is used by the thread local storage
(TLS) support. Finally the IO and file system is initialise followed by the
drivers.

Print the ``Init`` section data for the ``cdtest.exe`` for the ``i386/pc686`` BSP:

.. code-block:: shell

  $ rtems-exeinfo -I i386-rtems5/c/pc686/testsuites/samples/cdtest/cdtest.exe
  RTEMS Executable Info 5.6f5cfada964c
   rtems-exeinfo -I i386-rtems5/c/pc686/testsuites/samples/cdtest/cdtest.exe
  exe: i386-rtems5/c/pc686/testsuites/samples/cdtest/cdtest.exe
  Init sections: 3
   .ctors
    0xffffffff RamSize
    0x00100ea0 _GLOBAL__sub_I_rtems_test_name
    0x001015d0 __gnu_cxx::__freeres()
    0x00101df0 __cxxabiv1::__terminate(void (*)())
    0x00102ac0 _GLOBAL__sub_I___cxa_get_globals_fast
    0x00103260 std::nothrow
    0x00000000 REG_EFLAGS
   .init
    0xfcb3dbe8 no symbol
    0xff86e8ff no symbol
    0x00c2ffff no symbol
   .rtemsroset
    0x001112c0 bsp_work_area_initialize
    0x001113f0 bsp_start_default
    0x001276c0 _User_extensions_Handler_initialization
    0x00121260 rtems_initialize_data_structures
    0x001210f0 _RTEMS_tasks_Manager_initialization
    0x00120710 _Semaphore_Manager_initialization
    0x0011ff70 _POSIX_Keys_Manager_initialization
    0x001250d0 _Thread_Create_idle
    0x0011d220 rtems_libio_init
    0x0011cfe0 rtems_filesystem_initialize
    0x001113d0 bsp_predriver_hook
    0x0011d0d0 _Console_simple_Initialize
    0x00121310 _IO_Initialize_all_drivers
    0x00121010 _RTEMS_tasks_Initialize_user_tasks_body
    0x0011ddd0 rtems_libio_post_driver

The C++ constructor section ``.ctors`` shows you the C++ static objects the
RTEMS kernel will construct before calling ``main``.
