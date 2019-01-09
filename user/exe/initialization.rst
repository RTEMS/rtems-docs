.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

BSP Initialization
==================
.. index:: BSP Initialization

The bootloader jumps or calls the RTEMS executable's entry point, normally a
fixed address. The BSP entry point or start up code performs:

#. Low level processor specific initialization that such as setting control
   registers so the processor is operating in a mode RTEMS is built for

#. Cache flushing, clearing and invalidation

#. Memory management unit (MMU) set up if required

#. Clear the uninitialized data section

#. Process a command line if supported by the bootloader

#. Call ``bootcard`` which disabled interrupts, saves away a command line if
   the BSP supports it then call the RTEMS kernel early initialize entry point
   ``rtems_initialize_executive``. This call never returns.

Further BSP initialization happens as part of RTEMS kernel's System
Initialization process. The following handlers are declared and if provided are
placed at the beginning of the initialization handler list. The BSP can
provides:

``bsp_work_area_initialize``
  This function determines the amount of memory that can be given to RTEMS for
  the workspace and the C library heap which ``malloc`` uses. The call
  typically uses the ``bsp_work_area_initialize_default`` to perform actually
  perform the initialization.

``bsp_start``
  This function is specialized for each architecture and even for some BSPs. It
  performs the low level initialization RTEMS needs so it can run on the
  architecture and BSP.

``bsp_predriver_hook``
  This function can be used to initialize hardware drivers depend on such as
  configuring an interrupt controller. The default version is empty and does
  nothing.

BSPs all perform similar operations with common functionality and the RTEMS
kernel provides common code that can be shared between BSPs. The use of the
common code is encouraged for all new BSPs.

RTEMS Initialization
====================
.. index:: RTEMS Initialization

The RTEMS kernel initialization is:

#. Invoke the registered system initialization handlers

#. Set the system state to **up**

#. If the kernel supports SMP request multitasking start. All online cores are
   transferred to the **ready to start multitasking** state.

#. Start threaded multitasking. RTEMS starts multitasking by getting the first
   thread to run and dispatching it.

C++ static object constructors are called in the context of the first running
thread before the thread body is entered.

System Initialization Handlers
------------------------------

RTEMS supports the automatic registration of services used in
applications. This method of initialization automatically configures RTEMS with
only the services used in an application. There is no manual configuration of
services used and no updating of initialization function tables.

RTEMS uses specialized sections in the ELF executable to perform this task. The
system is based on the `FreeBSD SYSINT Framework
<https://www.freebsd.org/doc/en/books/arch-handbook/sysinit.html>`_. Ordered
initialization is performed before multitasking is started.

The RTEMS Tool ``rtems-exeinfo`` can provide some detail about the registered
handlers. The following shows the initialization handlers for the *hello world*
sample application in the RTEMS kernel's testsuite::

 $ rtems-exeinfo --init arm-rtems5/c/xilinx_zynq_zedboard/testsuites/samples/hello.exe
 RTEMS Executable Info 5.5416cfa39dd6
  rtems-exeinfo --init arm-rtems5/c/xilinx_zynq_zedboard/testsuites/samples/hello.exe
 exe: arm-rtems5/c/xilinx_zynq_zedboard/testsuites/samples/hello.exe

 Compilation:
  Producers: 2
   |  GNU AS 2.31.1: 14 objects
   |  GNU C11 7.3.0 20180125 (RTEMS 5, RSB e55769c64cf1a201588565a5662deafe3f1ccdcc, Newlib 103b055035fea328f8bc7826801760fb1c055683): 284 objects
  Common flags: 4
   | -march=armv7-a -mthumb -mfpu=neon -mfloat-abi=hard

 Init sections: 2
  .init_array
   0x001047c1 frame_dummy
  .rtemsroset
   0x00104c05 bsp_work_area_initialize
   0x00104c41 bsp_start
   0x0010eb45 zynq_debug_console_init
   0x0010ec19 rtems_counter_sysinit
   0x0010b779 _User_extensions_Handler_initialization
   0x0010c66d rtems_initialize_data_structures
   0x00107751 _RTEMS_tasks_Manager_initialization
   0x0010d4f5 _POSIX_Keys_Manager_initialization
   0x0010dd09 _Thread_Create_idle
   0x0010cf01 rtems_libio_init
   0x001053a5 rtems_filesystem_initialize
   0x0010546d _Console_simple_Initialize
   0x0010c715 _IO_Initialize_all_drivers
   0x001076d5 _RTEMS_tasks_Initialize_user_tasks_body
   0x0010cfa9 rtems_libio_post_driver

The section ``.rtemsroset`` lists the handlers called in order. The handlers
can be split into the BSP initialization handlers that start the BSP:

- ``bsp_work_area_initialize``
- ``bsp_start``
- ``zynq_debug_console_init``
- ``rtems_counter_sysinit``

And the remainder are handlers for services used by the application. The list
varies based on the services the application uses.
