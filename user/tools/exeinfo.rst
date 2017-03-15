.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2017 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

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
table. The start-up code in RTEMS loops over the table of addresses and calls
each address or system initialisation function. Th especial section names given
to the variables sort the table placing the initialisation calls in a specific
and controlled order.

A user places a call to an API function in their application and the linker
pulls the API code from the RTEMS kernel library adding it to the
executable. The API code the linker loads references the variable containing
the address of that API's system initialisation function. The linker loads the
API system initialisation code into the executable to resolve the external
reference created by the variable. If the user does not reference the API the
variable is not referenced and so not loaded into the executable resling in no
API initialisation.

The design automatically creates a unique system intialisation table for each
executable and the code in RTEMS does not change. There are no special build
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

  $ rtems-exeinfo -a i386-rtems4.12/c/pc686/testsuites/samples/hello/hello.exe
  RTEMS Executable Info 4.12.a72a462adc18
   rtems-exeinfo -a i386-rtems4.12/c/pc686/testsuites/samples/hello/hello.exe
  exe: i386-rtems4.12/c/pc686/testsuites/samples/hello/hello.exe
  Sections: 23
                    -------------- address: 0x00000000 0x00000000 size:       0 align:   0 relocs:    0
    .bss            WA------------ address: 0x0013f340 0x00144d9c size:   23132 align:  32 relocs:    0
    .comment        ---MS--------- address: 0x00000000 0x0000008f size:     143 align:   1 relocs:    0
    .ctors          WA------------ address: 0x0013cc9c 0x0013cca4 size:       8 align:   4 relocs:    0
    .data           WA------------ address: 0x0013ccc0 0x0013f32c size:    9836 align:  32 relocs:    0
    .debug_abbrev   -------------- address: 0x00000000 0x0003ef4c size:  257868 align:   1 relocs:    0
    .debug_aranges  -------------- address: 0x00000000 0x00003da8 size:   15784 align:   8 relocs:    0
    .debug_info     -------------- address: 0x00000000 0x0036dd9e size: 3595678 align:   1 relocs:    0
    .debug_line     -------------- address: 0x00000000 0x00072dca size:  470474 align:   1 relocs:    0
    .debug_loc      -------------- address: 0x00000000 0x0003fd2c size:  261420 align:   1 relocs:    0
    .debug_ranges   -------------- address: 0x00000000 0x00009738 size:   38712 align:   1 relocs:    0
    .debug_str      ---MS--------- address: 0x00000000 0x0001bf78 size:  114552 align:   1 relocs:    0
    .dtors          WA------------ address: 0x0013cca4 0x0013ccac size:       8 align:   4 relocs:    0
    .eh_frame       -A------------ address: 0x00134340 0x0013bc9c size:   31068 align:   4 relocs:    0
    .fini           -AE----------- address: 0x0012d8a9 0x0012d8b1 size:       8 align:   1 relocs:    0
    .init           -AE----------- address: 0x0012d89c 0x0012d8a9 size:      13 align:   1 relocs:    0
    .jcr            WA------------ address: 0x0013ccac 0x0013ccb0 size:       4 align:   4 relocs:    0
    .rodata         -A------------ address: 0x0012d8c0 0x0013433d size:   27261 align:  32 relocs:    0
    .rtemsroset     WA------------ address: 0x0012d860 0x0012d89c size:      60 align:   4 relocs:    0
    .shstrtab       -------------- address: 0x00000000 0x000000cb size:     203 align:   1 relocs:    0
    .strtab         -------------- address: 0x00000000 0x0000772a size:   30506 align:   1 relocs:    0
    .symtab         -------------- address: 0x00000000 0x00007120 size:   28960 align:   4 relocs:    0
    .text           WAE----------- address: 0x00100000 0x0012d860 size:  186464 align:  16 relocs:    0

  Init sections: 2
   .ctors
    0xffffffff RamSize
    0x00000000 _TLS_Data_size
   .rtemsroset
    0x00100280 bsp_work_area_initialize
    0x001003b0 bsp_start_default
    0x0011ace0 _User_extensions_Handler_initialization
    0x00113040 rtems_initialize_data_structures
    0x00112ec0 _RTEMS_tasks_Manager_initialization
    0x0011df30 _Message_queue_Manager_initialization
    0x0011cfa0 _Semaphore_Manager_initialization
    0x0011ce70 _POSIX_Keys_Manager_initialization
    0x00117360 _Thread_Create_idle
    0x0010c8d0 rtems_libio_init
    0x0010c7c0 rtems_filesystem_initialize
    0x00100390 bsp_predriver_hook
    0x001130f0 _IO_Initialize_all_drivers
    0x00112d90 _RTEMS_tasks_Initialize_user_tasks_body
    0x0010d520 rtems_libio_post_driver

  Fini sections: 1
   .dtors
    0xffffffff RamSize
    0x00000000 _TLS_Data_size

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

  $ rtems-exeinfo -I i386-rtems4.12/c/pc686/testsuites/samples/cdtest/cdtest.exe
  RTEMS Executable Info 4.12.a72a462adc18
   rtems-exeinfo -I i386-rtems4.12/c/pc686/testsuites/samples/cdtest/cdtest.exe
  exe: i386-rtems4.12/c/pc686/testsuites/samples/cdtest/cdtest.exe
  Init sections: 2
   .ctors
    0xffffffff RamSize
    0x00100e90 rtems_test_name
    0x001014b0 __gnu_cxx::__freeres()
    0x001017c0 __cxa_get_globals_fast
    0x001024e0 __cxxabiv1::__terminate(void (*)())
    0x001030a0 std::_V2::error_category::~error_category()
    0x0010cfa0 std::ctype_byname<char>::ctype_byname(std::string const&, unsigned long)
    0x0010d070 std::ctype_byname<wchar_t>::ctype_byname(std::string const&, unsigned long)
    0x0010d210 std::nothrow
    0x0010d230 std::ctype_byname<char>::ctype_byname(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long)
    0x0010d2c0 std::ctype_byname<wchar_t>::ctype_byname(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long)
    0x00000000 _TLS_Data_size
   .rtemsroset
    0x00111210 bsp_work_area_initialize
    0x00111340 bsp_start_default
    0x0012c560 _User_extensions_Handler_initialization
    0x001244d0 rtems_initialize_data_structures
    0x00124350 _RTEMS_tasks_Manager_initialization
    0x0012f790 _Message_queue_Manager_initialization
    0x0012e7c0 _Semaphore_Manager_initialization
    0x0013ccc0 _POSIX_signals_Manager_Initialization
    0x0012e650 _POSIX_Keys_Manager_initialization
    0x00128be0 _Thread_Create_idle
    0x0011d9d0 rtems_libio_init
    0x0011d8c0 rtems_filesystem_initialize
    0x00111320 bsp_predriver_hook
    0x00124580 _IO_Initialize_all_drivers
    0x00124220 _RTEMS_tasks_Initialize_user_tasks_body
    0x0011e620 rtems_libio_post_driver

The C++ constructor section ``.ctors`` shows you the C++ static objects the
RTEMS kernel will construct before calling ``main``.
