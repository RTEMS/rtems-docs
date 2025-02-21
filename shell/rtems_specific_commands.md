.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

RTEMS Specific Commands
***********************

Introduction
============

The RTEMS shell has the following RTEMS specific commands:

- rtems_ - Display RTEMS specific detail

- shutdown_ - Shutdown the system

- cpuinfo_ - print per-processor information

- cpuuse_ - print or reset per thread cpu usage

- stackuse_ - print per thread stack usage

- perioduse_ - print or reset per period usage

- profreport_ - print a profiling report

- wkspace_ - Display information on Executive Workspace

- config_ - Show the system configuration.

- itask_ - List init tasks for the system

- extension_ - Display information about extensions

- task_ - Display information about tasks

- queue_ - Display information about message queues

- sema_ - display information about semaphores

- region_ - display information about regions

- part_ - display information about partitions

- object_ - Display information about RTEMS objects

- driver_ - Display the RTEMS device driver table

- dname_ - Displays information about named drivers

- pthread_ - Displays information about POSIX threads

Commands
========

This section details the RTEMS Specific Commands available.  A subsection is
dedicated to each of the commands and describes the behavior and configuration
of that command as well as providing an example usage.

.. raw:: latex

   \clearpage

.. _rtems:

rtems - RTEMS Details
---------------------
.. index:: rtems

SYNOPSYS:
    .. code-block:: shell

        rtems

DESCRIPTION:
    This command reports various RTEMS specific details such as a the
    version, CPU and CPU module, BSP name, version of tools and the
    build options.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The following commands are supported:

    - ``ver``:
      Version of RTEMS running

    - ``cpu``:
      CPU name and model

    - ``bsp``:
      Name of the BSP

    - ``tools``:
      Version of the tools used to build RTEMS

    - ``opts``:
      RTEMS build options

    - ``all``:
      All of the available commands


EXAMPLES:
    The following is an example of how to use ``rtems``:

    .. code-block:: shell

        SHLL [/] # rtems
        RTEMS: 6.0.0 (071640d310b432d15350188c2ebf086653a0d578)

    The version of RTEMS running is displayed. To see the CPU name and
    moduel enter:

    .. code-block:: shell

        SHLL [/] # rtems cpu
        CPU: SPARC (w/FPU)

    The ``help`` command will list all available commands. The ``all``
    command will display all avalable output:

    .. code-block:: shell

        SHLL [/] # rtems all
        RTEMS: 6.0.0 (071640d310b432d15350188c2ebf086653a0d578)
        CPU: SPARC (w/FPU)
        BSP: erc32
        Tools: 12.1.1 20220622 (RTEMS 6, RSB f4f5d43a98051f7562103aaa2ec7723c628c6947, Newlib ea99f21)
        Options: DEBUG POSIX

.. index:: CONFIGURE_SHELL_NO_COMMAND_RTEMS
.. index:: CONFIGURE_SHELL_COMMAND_RTEMS

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_RTEMS`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_RTEMS`` when all shell commands have been
    configured.

PROGRAMMING INFORMATION:
    The configuration structure for the ``rtems`` has the following
    prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_RTEMS_Command;

.. raw:: latex

   \clearpage

.. _shutdown:

shutdown - Shutdown the system
------------------------------
.. index:: shutdown

SYNOPSYS:
    .. code-block:: shell

        shutdown

DESCRIPTION:
    This command is used to shutdown the RTEMS application.

EXIT STATUS:
    This command does not return.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``shutdown``:

    .. code-block:: shell

        SHLL [/] $ shutdown
        System shutting down at user request

    The user will not see another prompt and the system will shutdown.

.. index:: CONFIGURE_SHELL_NO_COMMAND_SHUTDOWN
.. index:: CONFIGURE_SHELL_COMMAND_SHUTDOWN

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_SHUTDOWN`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_SHUTDOWN`` when all shell commands have been
    configured.

PROGRAMMING INFORMATION:
    The configuration structure for the ``shutdown`` has the following
    prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_SHUTDOWN_Command;

.. raw:: latex

   \clearpage

.. _cpuinfo:

cpuinfo - print per-processor information
--------------------------------------------
.. index:: cpuinfo

SYNOPSYS:
    .. code-block:: shell

        cpuinfo

DESCRIPTION:
    This command may be used to print per-processor information.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

EXAMPLES:
    The following is an example of how to use ``cpuinfo``:

    .. code-block:: shell

        SHLL [/] $ cpuinfo
        -------------------------------------------------------------------------------
                                    PER PROCESSOR INFORMATION
        -------+--------+--------------+-----------------------------------------------
         INDEX | ONLINE | SCHEDULER ID | SCHEDULER NAME
        -------+--------+--------------+-----------------------------------------------
             0 |      1 |   0x0f010001 | UPD

    In the above example, the system has only one processor.  This processor
    has the index zero and is online.  It is owned by the scheduler with the
    identifier ``0x0f010001`` and name ``UPD``.

.. index:: CONFIGURE_SHELL_NO_COMMAND_CPUINFO
.. index:: CONFIGURE_SHELL_COMMAND_CPUINFO

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_CPUINFO`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_CPUINFO`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_cpuinfo

PROGRAMMING INFORMATION:
    The ``cpuinfo`` is implemented by a C language function which has the following
    prototype:

    .. code-block:: c

        int rtems_cpu_info_report(
            const rtems_printer *printer
        );

    The configuration structure for the ``cpuinfo`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_CPUINFO_Command;

.. raw:: latex

   \clearpage

.. _cpuuse:

cpuuse - print or reset per thread cpu usage
--------------------------------------------
.. index:: cpuuse

SYNOPSYS:
    .. code-block:: shell

        cpuuse [-r]

DESCRIPTION:
    This command may be used to print a report on the per thread cpu usage or
    to reset the per thread CPU usage statistics. When invoked with the ``-r``
    option, the CPU usage statistics are reset.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The granularity of the timing information reported is dependent upon the
    BSP and the manner in which RTEMS was built.  In the default RTEMS
    configuration, if the BSP supports nanosecond granularity timestamps, then
    the information reported will be highly accurate. Otherwise, the accuracy
    of the information reported is limited by the clock tick quantum.

EXAMPLES:
    The following is an example of how to use ``cpuuse``:

    .. code-block:: shell

        [/] cpuuse
        -------------------------------------------------------------------------------
                                      CPU USAGE BY THREAD
        ------------+----------------------------------------+---------------+---------
         ID         | NAME                                   | SECONDS       | PERCENT
        ------------+----------------------------------------+---------------+---------
         0x09010001 | IDLE                                   |     11.444381 |  73.938
         0x0a010001 | UI1                                    |      0.206754 |   1.335
         0x0a010002 | BSWP                                   |      0.008277 |   0.053
         0x0a010003 | BRDA                                   |      0.000952 |   0.006
         0x0a010004 | MDIA                                   |      0.000334 |   0.002
         0x0a010005 | TIME                                   |      0.912809 |   5.895
         0x0a010006 | IRQS                                   |      0.004810 |   0.031
         0x0a010007 | swi1: netisr 0                         |      0.002593 |   0.016
         0x0a010008 | kqueue_ctx task                        |      0.000663 |   0.004
         0x0a010009 | swi5: fast task                        |      0.000059 |   0.000
         0x0a01000a | thread taskq                           |      0.000057 |   0.000
         0x0a01000b | swi6: task queu                        |      0.003063 |   0.019
         0x0a01000c | DHCP                                   |      1.391745 |   8.986
         0x0a01000d | FTPa                                   |      0.002203 |   0.014
         0x0a01000e | FTPb                                   |      0.000233 |   0.001
         0x0a01000f | FTPc                                   |      0.000226 |   0.001
         0x0a010010 | FTPd                                   |      0.000228 |   0.001
         0x0a010011 | FTPD                                   |      0.002959 |   0.019
         0x0a010012 | TNTD                                   |      0.001111 |   0.007
         0x0a010013 | SHLL                                   |      1.508445 |   9.736
        ------------+----------------------------------------+---------------+---------
         TIME SINCE LAST CPU USAGE RESET IN SECONDS:                         15.492171
        -------------------------------------------------------------------------------
        [/] # cpuuse -r
        Resetting CPU Usage information
        [/] # cpuuse
        -------------------------------------------------------------------------------
                                      CPU USAGE BY THREAD
        ------------+----------------------------------------+---------------+---------
         ID         | NAME                                   | SECONDS       | PERCENT
        ------------+----------------------------------------+---------------+---------
         0x09010001 | IDLE                                   |      0.000000 |   0.000
         0x0a010001 | UI1                                    |      0.000000 |   0.000
         0x0a010002 | BSWP                                   |      0.000000 |   0.000
         0x0a010003 | BRDA                                   |      0.000000 |   0.000
         0x0a010004 | MDIA                                   |      0.000000 |   0.000
         0x0a010005 | TIME                                   |      0.000000 |   0.000
         0x0a010006 | IRQS                                   |      0.000000 |   0.000
         0x0a010007 | swi1: netisr 0                         |      0.000000 |   0.000
         0x0a010008 | kqueue_ctx task                        |      0.000000 |   0.000
         0x0a010009 | swi5: fast task                        |      0.000000 |   0.000
         0x0a01000a | thread taskq                           |      0.000000 |   0.000
         0x0a01000b | swi6: task queu                        |      0.000000 |   0.000
         0x0a01000c | DHCP                                   |      0.000000 |   0.000
         0x0a01000d | FTPa                                   |      0.000000 |   0.000
         0x0a01000e | FTPb                                   |      0.000000 |   0.000
         0x0a01000f | FTPc                                   |      0.000000 |   0.000
         0x0a010010 | FTPd                                   |      0.000000 |   0.000
         0x0a010011 | FTPD                                   |      0.000000 |   0.000
         0x0a010012 | TNTD                                   |      0.000000 |   0.000
         0x0a010013 | SHLL                                   |      0.016503 |  99.962
        ------------+----------------------------------------+---------------+---------
         TIME SINCE LAST CPU USAGE RESET IN SECONDS:                          0.016509
        -------------------------------------------------------------------------------

    In the above example, the system did something for roughly 15 seconds when the
    first report was generated.  The ``cpuuse -r`` and ``cpuuse`` commands were
    pasted from another window so were executed with no gap between.  In the
    second report, only the ``SHLL`` thread has run since the CPU Usage was
    reset.  It has consumed approximately 16.509 milliseconds of CPU time
    processing the two commands and generating the output.

.. index:: CONFIGURE_SHELL_NO_COMMAND_CPUUSE
.. index:: CONFIGURE_SHELL_COMMAND_CPUUSE

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_CPUUSE`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_CPUUSE`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_cpuuse

PROGRAMMING INFORMATION:
    The ``cpuuse`` is implemented by a C language function which has the following
    prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_cpuuse(
           int    argc,
           char **argv
        );

    The configuration structure for the ``cpuuse`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_CPUUSE_Command;

.. raw:: latex

   \clearpage

.. _stackuse:

stackuse - print per thread stack usage
---------------------------------------
.. index:: stackuse

SYNOPSYS:
    .. code-block:: shell

        stackuse

DESCRIPTION:
    This command prints a Stack Usage Report for all of the tasks and threads
    in the system.  On systems which support it, the usage of the interrupt
    stack is also included in the report.

EXIT STATUS:
    This command always succeeds and returns 0.

NOTES:
    The ``CONFIGURE_STACK_CHECKER_ENABLED`` ``confdefs.h`` constant must be
    defined when the application is configured for this command to have any
    information to report.

EXAMPLES:
    The following is an example of how to use ``stackuse``:

    .. code-block:: shell

        [/] # stackuse
                                     STACK USAGE BY THREAD
        ID         NAME                  LOW        HIGH       CURRENT    AVAIL  USED
        0x09010001 IDLE                  0x03559960 0x03564055 0x03563728   4080    584
        0x0a010001 UI1                   0x03564664 0x03597431 0x03596976  32752   4168
        0x0a010002 BSWP                  0x03714576 0x03718671 0x03718408   4080    564
        0x0a010003 BRDA                  0x03718680 0x03722775 0x03722480   4080    596
        0x0a010004 MDIA                  0x03722808 0x03755575 0x03755288  32752    588
        0x0a010005 TIME                  0x03755664 0x03788431 0x03788168  32752   1448
        0x0a010006 IRQS                  0x03788440 0x03821207 0x03820952  32752    608
        0x0a010007 swi1: netisr 0        0x03896880 0x03929647 0x03929376  32752    820
        0x0a010008 kqueue_ctx task       0x03929872 0x03962639 0x03962392  32752    580
        0x0a010009 swi5: fast task       0x03963088 0x03995855 0x03995584  32752    572
        0x0a01000a thread taskq          0x03996080 0x04028847 0x04028600  32752    548
        0x0a01000b swi6: task queu       0x04029296 0x04062063 0x04061792  32752   1364
        0x0a01000c DHCP                  0x04250192 0x04258383 0x04257288   8176   2764
        0x0a01000d FTPa                  0x04258792 0x04266983 0x04265792   8176   1548
        0x0a01000e FTPb                  0x04267120 0x04275311 0x04274120   8176   1496
        0x0a01000f FTPc                  0x04275448 0x04283639 0x04282448   8176   1496
        0x0a010010 FTPd                  0x04283776 0x04291967 0x04290776   8176   1496
        0x0a010011 FTPD                  0x04292104 0x04296199 0x04295784   4080    772
        0x0a010012 TNTD                  0x04297088 0x04329855 0x04329368  32752    804
        0x0a010013 SHLL                  0x04329976 0x04346359 0x04344576  16368   3616

.. index:: CONFIGURE_SHELL_NO_COMMAND_STACKUSE
.. index:: CONFIGURE_SHELL_COMMAND_STACKUSE

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_STACKUSE`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_STACKUSE`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_stackuse

PROGRAMMING INFORMATION:
    The ``stackuse`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_stackuse(
            int    argc,
            char **argv
        );

    The configuration structure for the ``stackuse`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_STACKUSE_Command;

.. raw:: latex

   \clearpage

.. _perioduse:

perioduse - print or reset per period usage
-------------------------------------------
.. index:: perioduse

SYNOPSYS:
    .. code-block:: shell

        perioduse [-r]

DESCRIPTION:
    This command may be used to print a statistics report on the rate monotonic
    periods in the application or to reset the rate monotonic period usage
    statistics. When invoked with the ``-r`` option, the usage statistics are
    reset.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The granularity of the timing information reported is dependent upon the
    BSP and the manner in which RTEMS was built.  In the default RTEMS
    configuration, if the BSP supports nanosecond granularity timestamps, then
    the information reported will be highly accurate. Otherwise, the accuracy
    of the information reported is limited by the clock tick quantum.

EXAMPLES:
    The following is an example of how to use ``perioduse``:

    .. code-block:: shell

        SHLL [/] $ perioduse
        Period information by period
        --- CPU times are in seconds ---
        --- Wall times are in seconds ---
        ID     OWNER COUNT MISSED          CPU TIME                  WALL TIME
        MIN/MAX/AVG                MIN/MAX/AVG
        0x42010001 TA1    502      0 0:000039/0:042650/0:004158 0:000039/0:020118/0:002848
        0x42010002 TA2    502      0 0:000041/0:042657/0:004309 0:000041/0:020116/0:002848
        0x42010003 TA3    501      0 0:000041/0:041564/0:003653 0:000041/0:020003/0:002814
        0x42010004 TA4    501      0 0:000043/0:044075/0:004911 0:000043/0:020004/0:002814
        0x42010005 TA5     10      0 0:000065/0:005413/0:002739 0:000065/1:000457/0:041058
        MIN/MAX/AVG                MIN/MAX/AVG
        SHLL [/] $ perioduse -r
        Resetting Period Usage information
        SHLL [/] $ perioduse
        --- CPU times are in seconds ---
        --- Wall times are in seconds ---
        ID     OWNER COUNT MISSED          CPU TIME                  WALL TIME
        MIN/MAX/AVG                MIN/MAX/AVG
        0x42010001 TA1      0      0
        0x42010002 TA2      0      0
        0x42010003 TA3      0      0
        0x42010004 TA4      0      0
        0x42010005 TA5      0      0

.. index:: CONFIGURE_SHELL_NO_COMMAND_PERIODUSE
.. index:: CONFIGURE_SHELL_COMMAND_PERIODUSE

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_PERIODUSE`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_PERIODUSE`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_perioduse

PROGRAMMING INFORMATION:
    The ``perioduse`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_perioduse(
            int    argc,
            char **argv
        );

    The configuration structure for the ``perioduse`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_PERIODUSE_Command;

.. raw:: latex

   \clearpage

.. _profreport:

profreport - print a profiling report
-------------------------------------
.. index:: profreport

SYNOPSYS:
    .. code-block:: shell

        profreport

DESCRIPTION:
    This command may be used to print a profiling report if profiling is built
    into the RTEMS kernel.

EXIT STATUS:
    This command returns 0.

NOTES:
    Profiling must be enabled at build configuration time to get profiling
    information.

EXAMPLES:
    The following is an example of how to use ``profreport``:

    .. code-block:: shell

        SHLL [/] $ profreport
        <ProfilingReport name="Shell">
        <PerCPUProfilingReport processorIndex="0">
        <MaxThreadDispatchDisabledTime unit="ns">10447</MaxThreadDispatchDisabledTime>
        <MeanThreadDispatchDisabledTime unit="ns">2</MeanThreadDispatchDisabledTime>
        <TotalThreadDispatchDisabledTime unit="ns">195926627</TotalThreadDispatchDisabledTime>
        <ThreadDispatchDisabledCount>77908688</ThreadDispatchDisabledCount>
        <MaxInterruptDelay unit="ns">0</MaxInterruptDelay>
        <MaxInterruptTime unit="ns">688</MaxInterruptTime>
        <MeanInterruptTime unit="ns">127</MeanInterruptTime>
        <TotalInterruptTime unit="ns">282651157</TotalInterruptTime>
        <InterruptCount>2215855</InterruptCount>
        </PerCPUProfilingReport>
        <PerCPUProfilingReport processorIndex="1">
        <MaxThreadDispatchDisabledTime unit="ns">9053</MaxThreadDispatchDisabledTime>
        <MeanThreadDispatchDisabledTime unit="ns">41</MeanThreadDispatchDisabledTime>
        <TotalThreadDispatchDisabledTime unit="ns">3053830335</TotalThreadDispatchDisabledTime>
        <ThreadDispatchDisabledCount>73334202</ThreadDispatchDisabledCount>
        <MaxInterruptDelay unit="ns">0</MaxInterruptDelay>
        <MaxInterruptTime unit="ns">57</MaxInterruptTime>
        <MeanInterruptTime unit="ns">35</MeanInterruptTime>
        <TotalInterruptTime unit="ns">76980203</TotalInterruptTime>
        <InterruptCount>2141179</InterruptCount>
        </PerCPUProfilingReport>
        <SMPLockProfilingReport name="SMP lock stats">
        <MaxAcquireTime unit="ns">608</MaxAcquireTime>
        <MaxSectionTime unit="ns">1387</MaxSectionTime>
        <MeanAcquireTime unit="ns">112</MeanAcquireTime>
        <MeanSectionTime unit="ns">338</MeanSectionTime>
        <TotalAcquireTime unit="ns">119031</TotalAcquireTime>
        <TotalSectionTime unit="ns">357222</TotalSectionTime>
        <UsageCount>1055</UsageCount>
        <ContentionCount initialQueueLength="0">1055</ContentionCount>
        <ContentionCount initialQueueLength="1">0</ContentionCount>
        <ContentionCount initialQueueLength="2">0</ContentionCount>
        <ContentionCount initialQueueLength="3">0</ContentionCount>
        </SMPLockProfilingReport>
        <SMPLockProfilingReport name="Giant">
        <MaxAcquireTime unit="ns">4186</MaxAcquireTime>
        <MaxSectionTime unit="ns">7575</MaxSectionTime>
        <MeanAcquireTime unit="ns">160</MeanAcquireTime>
        <MeanSectionTime unit="ns">183</MeanSectionTime>
        <TotalAcquireTime unit="ns">1772793111</TotalAcquireTime>
        <TotalSectionTime unit="ns">2029733879</TotalSectionTime>
        <UsageCount>11039140</UsageCount>
        <ContentionCount initialQueueLength="0">11037655</ContentionCount>
        <ContentionCount initialQueueLength="1">1485</ContentionCount>
        <ContentionCount initialQueueLength="2">0</ContentionCount>
        <ContentionCount initialQueueLength="3">0</ContentionCount>
        </SMPLockProfilingReport>
        </ProfilingReport>

.. index:: CONFIGURE_SHELL_NO_COMMAND_PROFREPORT
.. index:: CONFIGURE_SHELL_COMMAND_PROFREPORT

CONFIGURATION:
    When building a custom command set, define
    ``CONFIGURE_SHELL_COMMAND_PROFREPORT`` to have this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_PROFREPORT`` when all shell commands have been
    configured.

PROGRAMMING INFORMATION:
    The configuration structure for the ``profreport`` has the following
    prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_PROFREPORT_Command;

.. raw:: latex

   \clearpage

.. _wkspace:

wkspace - display information on executive workspace
----------------------------------------------------
.. index:: wkspace

SYNOPSYS:
    .. code-block:: shell

        wkspace

DESCRIPTION:
    This command prints information on the current state of the RTEMS Executive
    Workspace reported.  This includes the following information:

    - Number of free blocks

    - Largest free block

    - Total bytes free

    - Number of used blocks

    - Largest used block

    - Total bytes used

EXIT STATUS:
    This command always succeeds and returns 0.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``wkspace``:

    .. code-block:: shell

        SHLL [/] $ wkspace
        Number of free blocks: 1
        Largest free block:    132336
        Total bytes free:      132336
        Number of used blocks: 36
        Largest used block:    16408
        Total bytes used:      55344

.. index:: CONFIGURE_SHELL_NO_COMMAND_WKSPACE
.. index:: CONFIGURE_SHELL_COMMAND_WKSPACE

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_WKSPACE`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_WKSPACE`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_wkspace

PROGRAMMING INFORMATION:
    The ``wkspace`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_wkspace(
            int    argc,
            char **argv
        );

    The configuration structure for the ``wkspace`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_WKSPACE_Command;

.. raw:: latex

   \clearpage

.. _config:

config - show the system configuration.
---------------------------------------
.. index:: config

SYNOPSYS:
    .. code-block:: shell

        config

DESCRIPTION:
    This command display information about the RTEMS Configuration.

EXIT STATUS:
    This command always succeeds and returns 0.

NOTES:
    At this time, it does not report every configuration parameter.  This is an
    area in which user submissions or sponsorship of a developer would be
    appreciated.

EXAMPLES:
    The following is an example of how to use ``config``:

    .. code-block:: shell

        SHLL [/] $ config
        INITIAL (startup) Configuration Info

        WORKSPACE      start: 0x23d22e0;  size: 0x2dd20
        TIME           usec/tick: 10000;  tick/timeslice: 50;  tick/sec: 100
        MAXIMUMS       tasks: 20;  timers: 0;  sems: 50;  que's: 20;  ext's: 1
        partitions: 0;  regions: 0;  ports: 0;  periods: 0

.. index:: CONFIGURE_SHELL_NO_COMMAND_CONFIG
.. index:: CONFIGURE_SHELL_COMMAND_CONFIG

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_CONFIG`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_CONFIG`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_config

PROGRAMMING INFORMATION:
    The ``config`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_config(
            int    argc,
            char **argv
        );

    The configuration structure for the ``config`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_CONFIG_Command;

.. raw:: latex

   \clearpage

.. _itask:

itask - list init tasks for the system
--------------------------------------
.. index:: itask

SYNOPSYS:
    .. code-block:: shell

        itask

DESCRIPTION:
    This command prints a report on the set of initialization tasks and threads
    in the system.

EXIT STATUS:
    This command always succeeds and returns 0.

NOTES:
    At this time, it includes only Classic API Initialization Tasks.  This is an
    area in which user submissions or sponsorship of a developer would be
    appreciated.

EXAMPLES:
    The following is an example of how to use ``itask``:

    .. code-block:: shell

        SHLL [/] $ itask
        #    NAME   ENTRY        ARGUMENT    PRIO   MODES  ATTRIBUTES   STACK SIZE
        ------------------------------------------------------------------------------
        0   UI1    [0x2002258] 0 [0x0]        1    nP      DEFAULT     4096 [0x1000]

.. index:: CONFIGURE_SHELL_NO_COMMAND_ITASK
.. index:: CONFIGURE_SHELL_COMMAND_ITASK

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_ITASK`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_ITASK`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_itask

PROGRAMMING INFORMATION:
    The ``itask`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_itask(
            int    argc,
            char **argv
        );

    The configuration structure for the ``itask`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_ITASK_Command;

.. raw:: latex

   \clearpage

.. _extension:

extension - display information about extensions
------------------------------------------------
.. index:: extension

SYNOPSYS:
    .. code-block:: shell

        extension [id [id ...]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of User Extensions currently active in the system.

    If invoked with a set of ids as arguments, then just those objects are
    included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of using the ``extension`` command on a system
    with no user extensions.

    .. code-block:: shell

        SHLL [/] $ extension
        ID       NAME
        ------------------------------------------------------------------------------

.. index:: CONFIGURE_SHELL_NO_COMMAND_EXTENSION
.. index:: CONFIGURE_SHELL_COMMAND_EXTENSION

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_EXTENSION`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_EXTENSION`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_extension

PROGRAMMING INFORMATION:
    The ``extension`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_extension(
            int    argc,
            char **argv
        );

    The configuration structure for the ``extension`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_EXTENSION_Command;

.. raw:: latex

   \clearpage

.. _task:

task - display information about tasks
--------------------------------------
.. index:: task

SYNOPSYS:
    .. code-block:: shell

        task [id [id ...]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of Classic API Tasks currently active in the system.

    If invoked with a set of ids as arguments, then just those objects are
    included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use the ``task`` on an application
    with just two Classic API tasks:

    .. code-block:: shell

        SHLL [/] # task
        ID       NAME                 SHED PRI STATE  MODES    EVENTS WAITINFO
        ------------------------------------------------------------------------------
        0a010001 UI1                  UPD  254 EV     P:T:nA   NONE
        0a010002 SHLL                 UPD  100 READY  P:T:nA   NONE

.. index:: CONFIGURE_SHELL_NO_COMMAND_TASK
.. index:: CONFIGURE_SHELL_COMMAND_TASK

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_TASK`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_TASK`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_task

PROGRAMMING INFORMATION:
    The ``task`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: shell

        int rtems_shell_rtems_main_task(
            int    argc,
            char **argv
        );

    The configuration structure for the ``task`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_TASK_Command;

.. raw:: latex

   \clearpage

.. _queue:

queue - display information about message queues
------------------------------------------------
.. index:: queue

SYNOPSYS:
    .. code-block:: shell

        queue [id [id ... ]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of Classic API Message Queues currently active in the system.

    If invoked with a set of ids as arguments, then just those objects are
    included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of using the ``queue`` command on a system with
    no Classic API Message Queues.

    .. code-block:: shell

        SHLL [/] $ queue
        ID       NAME   ATTRIBUTES   PEND   MAXPEND  MAXSIZE
        ------------------------------------------------------------------------------

.. index:: CONFIGURE_SHELL_NO_COMMAND_QUEUE
.. index:: CONFIGURE_SHELL_COMMAND_QUEUE

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_QUEUE`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_QUEUE`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_queue

PROGRAMMING INFORMATION:
    The ``queue`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_queue(
            int    argc,
            char **argv
        );

    The configuration structure for the ``queue`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_QUEUE_Command;

.. raw:: latex

   \clearpage

.. _sema:

sema - display information about semaphores
-------------------------------------------
.. index:: sema

SYNOPSYS:
    .. code-block:: shell

        sema [id [id ... ]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of Classic API Semaphores currently active in the system.

    If invoked with a set of objects ids as arguments, then just those objects
    are included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``sema``:

    .. code-block:: shell

        SHLL [/] $ sema
        ID       NAME   ATTR        PRICEIL CURR_CNT HOLDID
        ------------------------------------------------------------------------------
        1a010001   LBIO   PR:BI:IN      0        1     00000000
        1a010002   TRmi   PR:BI:IN      0        1     00000000
        1a010003   LBI00  PR:BI:IN      0        1     00000000
        1a010004   TRia   PR:BI:IN      0        1     00000000
        1a010005   TRoa   PR:BI:IN      0        1     00000000
        1a010006   TRxa   <assoc.c: BAD NAME>   0    0 09010001
        1a010007   LBI01  PR:BI:IN      0        1     00000000
        1a010008   LBI02  PR:BI:IN      0        1     00000000

.. index:: CONFIGURE_SHELL_NO_COMMAND_SEMA
.. index:: CONFIGURE_SHELL_COMMAND_SEMA

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_SEMA`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_SEMA`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_sema

PROGRAMMING INFORMATION:
    The ``sema`` is implemented by a C language function which has the following
    prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_sema(
            int    argc,
            char **argv
        );

    The configuration structure for the ``sema`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_SEMA_Command;

.. raw:: latex

   \clearpage

.. _region:

region - display information about regions
------------------------------------------
.. index:: region

SYNOPSYS:
    .. code-block:: shell

        region [id [id ... ]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of Classic API Regions currently active in the system.

    If invoked with a set of object ids as arguments, then just those object
    are included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of using the ``region`` command on a system
    with no user extensions.

    .. code-block:: shell

        SHLL [/] $ region
        ID       NAME   ATTR        STARTADDR LENGTH    PAGE_SIZE USED_BLOCKS
        ------------------------------------------------------------------------------

.. index:: CONFIGURE_SHELL_NO_COMMAND_REGION
.. index:: CONFIGURE_SHELL_COMMAND_REGION

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_REGION`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_REGION`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_region

PROGRAMMING INFORMATION:
    The ``region`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_region(
            int    argc,
            char **argv
        );

    The configuration structure for the ``region`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_REGION_Command;

.. raw:: latex

   \clearpage

.. _part:

part - display information about partitions
-------------------------------------------
.. index:: part

SYNOPSYS:
    .. code-block:: shell

        part [id [id ... ]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of Classic API Partitions currently active in the system.

    If invoked with a set of object ids as arguments, then just those objects
    are included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of using the ``part`` command on a system with
    no user extensions.

    .. code-block:: shell

        SHLL [/] $ part
        ID       NAME   ATTR        STARTADDR LENGTH    BUF_SIZE  USED_BLOCKS
        ------------------------------------------------------------------------------

.. index:: CONFIGURE_SHELL_NO_COMMAND_PART
.. index:: CONFIGURE_SHELL_COMMAND_PART

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_PART`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_PART`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_part

PROGRAMMING INFORMATION:
    The ``part`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_part(
            int    argc,
            char **argv
        );

    The configuration structure for the ``part`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_PART_Command;

.. raw:: latex

   \clearpage

.. _object:

object - display information about RTEMS objects
------------------------------------------------
.. index:: object

SYNOPSYS:
    .. code-block:: shell

        object [id [id ...]]

DESCRIPTION:
    When invoked with a set of object ids as arguments, then a report on those
    objects is printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``object``:

    .. code-block:: shell

        SHLL [/] $ object 0a010001 1a010002
        ID       NAME   PRIO   STAT   MODES  EVENTS   WAITID  WAITARG  NOTES
        ------------------------------------------------------------------------------
        0a010001   UI1      1   SUSP   P:T:nA  NONE
        ID       NAME   ATTR        PRICEIL CURR_CNT HOLDID
        ------------------------------------------------------------------------------
        1a010002   TRmi   PR:BI:IN      0        1     00000000

.. index:: CONFIGURE_SHELL_NO_COMMAND_OBJECT
.. index:: CONFIGURE_SHELL_COMMAND_OBJECT

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_OBJECT`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_OBJECT`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_object

PROGRAMMING INFORMATION:
    The ``object`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_object(
            int    argc,
            char **argv
        );

    The configuration structure for the ``object`` has the
    following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_OBJECT_Command;

.. raw:: latex

   \clearpage

.. _driver:

driver - display the RTEMS device driver table
----------------------------------------------
.. index:: driver

SYNOPSYS:
    .. code-block:: shell

        driver [major [major ...]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of Device Drivers currently active in the system.

    If invoked with a set of major numbers as arguments, then just those Device
    Drivers are included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``driver``:

    .. code-block:: shell

        SHLL [/] $ driver
        Major      Entry points
        ------------------------------------------------------------------------------
        0          init: [0x200256c];  control: [0x20024c8]
        open: [0x2002518];  close: [0x2002504]
        read: [0x20024f0];  write: [0x20024dc]
        1          init: [0x20023fc];  control: [0x2002448]
        open: [0x0];  close: [0x0]
        read: [0x0];  write: [0x0]
        SHLL [/] $

.. index:: CONFIGURE_SHELL_NO_COMMAND_DRIVER
.. index:: CONFIGURE_SHELL_COMMAND_DRIVER

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_DRIVER`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_DRIVER`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_driver

PROGRAMMING INFORMATION:
    The ``driver`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_driver(
            int    argc,
            char **argv
        );

    The configuration structure for the ``driver`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_DRIVER_Command;

.. raw:: latex

   \clearpage

.. _dname:

dname - displays information about named drivers
------------------------------------------------
.. index:: dname

SYNOPSYS:
    .. code-block:: shell

        dname

DESCRIPTION:
    WARNING! This command does not appear to work as of 27 February 2008.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``dname``:

    .. code-block:: shell

        EXAMPLE_TBD

.. index:: CONFIGURE_SHELL_NO_COMMAND_DNAME
.. index:: CONFIGURE_SHELL_COMMAND_DNAME

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_DNAME`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_DNAME`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_dname

PROGRAMMING INFORMATION:
    The ``dname`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_dname(
            int    argc,
            char **argv
        );

    The configuration structure for the ``dname`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_DNAME_Command;

.. raw:: latex

   \clearpage

.. _pthread:

pthread - display information about POSIX threads
-------------------------------------------------
.. index:: pthread

SYNOPSYS:
    .. code-block:: shell

        pthread [id [id ...]]

DESCRIPTION:
    When invoked with no arguments, this command prints information on the set
    of POSIX API threads currently active in the system.

    If invoked with a set of ids as arguments, then just those objects are
    included in the information printed.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    This command is only available when the POSIX API is configured.

EXAMPLES:
    The following is an example of how to use the ``task`` on an application
    with four POSIX threads:

    .. code-block:: shell

        SHLL [/] $ pthread
        ID       NAME           PRI  STATE MODES   EVENTS    WAITID  WAITARG  NOTES
        ------------------------------------------------------------------------------
        0b010002   Main           133 READY  P:T:nA    NONE   43010001 0x7b1148
        0b010003   ISR            133 Wcvar  P:T:nA    NONE   43010003 0x7b1148
        0b01000c                  133 READY  P:T:nA    NONE   33010002 0x7b1148
        0b01000d                  133 Wmutex P:T:nA    NONE   33010002 0x7b1148

CONFIGURATION:
    This command is part of the monitor commands which are always available in
    the shell.

PROGRAMMING INFORMATION:
    This command is not directly available for invocation.
