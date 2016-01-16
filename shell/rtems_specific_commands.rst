RTEMS Specific Commands
#######################

Introduction
============

The RTEMS shell has the following rtems commands:

- ``shutdown`` - Shutdown the system

- ``cpuuse`` - print or reset per thread cpu usage

- ``stackuse`` - print per thread stack usage

- ``perioduse`` - print or reset per period usage

- ``profreport`` - print a profiling report

- ``wkspace`` - Display information on Executive Workspace

- ``config`` - Show the system configuration.

- ``itask`` - List init tasks for the system

- ``extension`` - Display information about extensions

- ``task`` - Display information about tasks

- ``queue`` - Display information about message queues

- ``sema`` - display information about semaphores

- ``region`` - display information about regions

- ``part`` - display information about partitions

- ``object`` - Display information about RTEMS objects

- ``driver`` - Display the RTEMS device driver table

- ``dname`` - Displays information about named drivers

- ``pthread`` - Displays information about POSIX threads

Commands
========

This section details the RTEMS Specific Commands available.  A
subsection is dedicated to each of the commands and
describes the behavior and configuration of that
command as well as providing an example usage.

shutdown - Shutdown the system
------------------------------
.. index:: shutdown

**SYNOPSYS:**

.. code:: c

    shutdown

**DESCRIPTION:**

This command is used to shutdown the RTEMS application.

**EXIT STATUS:**

This command does not return.

**NOTES:**

**EXAMPLES:**

The following is an example of how to use ``shutdown``:
.. code:: c

    SHLL \[/] $ shutdown
    System shutting down at user request

The user will not see another prompt and the system will
shutdown.

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_SHUTDOWN
.. index:: CONFIGURE_SHELL_COMMAND_SHUTDOWN

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_SHUTDOWN`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_SHUTDOWN`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

The configuration structure for the ``shutdown`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_SHUTDOWN_Command;

cpuuse - print or reset per thread cpu usage
--------------------------------------------
.. index:: cpuuse

**SYNOPSYS:**

.. code:: c

    cpuuse \[-r]

**DESCRIPTION:**

This command may be used to print a report on the per thread
cpu usage or to reset the per thread CPU usage statistics. When
invoked with the ``-r`` option, the CPU usage statistics
are reset.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

The granularity of the timing information reported is dependent
upon the BSP and the manner in which RTEMS was built.  In the
default RTEMS configuration, if the BSP supports nanosecond
granularity timestamps, then the information reported will be
highly accurate. Otherwise, the accuracy of the information
reported is limited by the clock tick quantum.

**EXAMPLES:**

The following is an example of how to use ``cpuuse``:
.. code:: c

    SHLL \[/] $ cpuuse
    CPU Usage by thread
    ID            NAME         SECONDS   PERCENT
    0x09010001   IDLE            49.745393   98.953
    0x0a010001   UI1              0.000000    0.000
    0x0a010002   SHLL             0.525928    1.046
    Time since last CPU Usage reset 50.271321 seconds
    SHLL \[/] $ cpuuse -r
    Resetting CPU Usage information
    SHLL \[/] $ cpuuse
    CPU Usage by thread
    ID            NAME         SECONDS   PERCENT
    0x09010001   IDLE             0.000000    0.000
    0x0a010001   UI1              0.000000    0.000
    0x0a010002   SHLL             0.003092  100.000
    Time since last CPU Usage reset 0.003092 seconds

In the above example, the system had set idle for nearly
a minute when the first report was generated.  The``cpuuse -r`` and ``cpuuse`` commands were pasted
from another window so were executed with no gap between.
In the second report, only the ``shell`` thread has
run since the CPU Usage was reset.  It has consumed
approximately 3.092 milliseconds of CPU time processing
the two commands and generating the output.

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_CPUUSE
.. index:: CONFIGURE_SHELL_COMMAND_CPUUSE

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_CPUUSE`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_CPUUSE`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_cpuuse

The ``cpuuse`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_cpuuse(
    int    argc,
    char \**argv
    );

The configuration structure for the ``cpuuse`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_CPUUSE_Command;

stackuse - print per thread stack usage
---------------------------------------
.. index:: stackuse

**SYNOPSYS:**

.. code:: c

    stackuse

**DESCRIPTION:**

This command prints a Stack Usage Report for all of the tasks
and threads in the system.  On systems which support it, the
usage of the interrupt stack is also included in the report.

**EXIT STATUS:**

This command always succeeds and returns 0.

**NOTES:**

The ``CONFIGURE_STACK_CHECKER_ENABLED`` ``confdefs.h`` constant
must be defined when the application is configured for this
command to have any information to report.

**EXAMPLES:**

The following is an example of how to use ``stackuse``:
.. code:: c

    SHLL \[/] $ stackuse
    Stack usage by thread
    ID      NAME    LOW          HIGH     CURRENT     AVAILABLE     USED
    0x09010001  IDLE 0x023d89a0 - 0x023d99af 0x023d9760      4096        608
    0x0a010001  UI1  0x023d9f30 - 0x023daf3f 0x023dad18      4096       1804
    0x0a010002  SHLL 0x023db4c0 - 0x023df4cf 0x023de9d0     16384       5116
    0xffffffff  INTR 0x023d2760 - 0x023d375f 0x00000000      4080        316

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_STACKUSE
.. index:: CONFIGURE_SHELL_COMMAND_STACKUSE

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_STACKUSE`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_STACKUSE`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_stackuse

The ``stackuse`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_stackuse(
    int    argc,
    char \**argv
    );

The configuration structure for the ``stackuse`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_STACKUSE_Command;

perioduse - print or reset per period usage
-------------------------------------------
.. index:: perioduse

**SYNOPSYS:**

.. code:: c

    perioduse \[-r]

**DESCRIPTION:**

This command may be used to print a statistics report on the rate
monotonic periods in the application or to reset the rate monotonic
period usage statistics. When invoked with the ``-r`` option, the
usage statistics are reset.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

The granularity of the timing information reported is dependent
upon the BSP and the manner in which RTEMS was built.  In the
default RTEMS configuration, if the BSP supports nanosecond
granularity timestamps, then the information reported will be
highly accurate. Otherwise, the accuracy of the information
reported is limited by the clock tick quantum.

**EXAMPLES:**

The following is an example of how to use ``perioduse``:
.. code:: c

    SHLL \[/] $ perioduse
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
    SHLL \[/] $ perioduse -r
    Resetting Period Usage information
    SHLL \[/] $ perioduse
    --- CPU times are in seconds ---
    --- Wall times are in seconds ---
    ID     OWNER COUNT MISSED          CPU TIME                  WALL TIME
    MIN/MAX/AVG                MIN/MAX/AVG
    0x42010001 TA1      0      0
    0x42010002 TA2      0      0
    0x42010003 TA3      0      0
    0x42010004 TA4      0      0
    0x42010005 TA5      0      0

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_PERIODUSE
.. index:: CONFIGURE_SHELL_COMMAND_PERIODUSE

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_PERIODUSE`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_PERIODUSE`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_perioduse

The ``perioduse`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_perioduse(
    int    argc,
    char \**argv
    );

The configuration structure for the ``perioduse`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_PERIODUSE_Command;

profreport - print a profiling report
-------------------------------------
.. index:: profreport

**SYNOPSYS:**

.. code:: c

    profreport

**DESCRIPTION:**

This command may be used to print a profiling report.

**EXIT STATUS:**

This command returns 0.

**NOTES:**

Profiling must be enabled at build configuration time to get profiling
information.

**EXAMPLES:**

The following is an example of how to use ``profreport``:
.. code:: c

    SHLL \[/] $ profreport
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

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_PROFREPORT
.. index:: CONFIGURE_SHELL_COMMAND_PROFREPORT

When building a custom command set, define``CONFIGURE_SHELL_COMMAND_PROFREPORT`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_PROFREPORT`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

The configuration structure for the ``profreport`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_PROFREPORT_Command;

wkspace - display information on executive workspace
----------------------------------------------------
.. index:: wkspace

**SYNOPSYS:**

.. code:: c

    wkspace

**DESCRIPTION:**

This command prints information on the current state of
the RTEMS Executive Workspace reported.  This includes the
following information:

- Number of free blocks

- Largest free block

- Total bytes free

- Number of used blocks

- Largest used block

- Total bytes used

**EXIT STATUS:**

This command always succeeds and returns 0.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of how to use ``wkspace``:
.. code:: c

    SHLL \[/] $ wkspace
    Number of free blocks: 1
    Largest free block:    132336
    Total bytes free:      132336
    Number of used blocks: 36
    Largest used block:    16408
    Total bytes used:      55344

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_WKSPACE
.. index:: CONFIGURE_SHELL_COMMAND_WKSPACE

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_WKSPACE`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_WKSPACE`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_wkspace

The ``wkspace`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_wkspace(
    int    argc,
    char \**argv
    );

The configuration structure for the ``wkspace`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_WKSPACE_Command;

config - show the system configuration.
---------------------------------------
.. index:: config

**SYNOPSYS:**

.. code:: c

    config

**DESCRIPTION:**

This command display information about the RTEMS Configuration.

**EXIT STATUS:**

This command always succeeds and returns 0.

**NOTES:**

At this time, it does not report every configuration parameter.
This is an area in which user submissions or sponsorship of
a developer would be appreciated.

**EXAMPLES:**

The following is an example of how to use ``config``:
.. code:: c

    INITIAL (startup) Configuration Info

    WORKSPACE      start: 0x23d22e0;  size: 0x2dd20
    TIME           usec/tick: 10000;  tick/timeslice: 50;  tick/sec: 100
    MAXIMUMS       tasks: 20;  timers: 0;  sems: 50;  que's: 20;  ext's: 1
    partitions: 0;  regions: 0;  ports: 0;  periods: 0

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_CONFIG
.. index:: CONFIGURE_SHELL_COMMAND_CONFIG

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_CONFIG`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_CONFIG`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_config

The ``config`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_config(
    int    argc,
    char \**argv
    );

The configuration structure for the ``config`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_CONFIG_Command;

itask - list init tasks for the system
--------------------------------------
.. index:: itask

**SYNOPSYS:**

.. code:: c

    itask

**DESCRIPTION:**

This command prints a report on the set of initialization
tasks and threads in the system.

**EXIT STATUS:**

This command always succeeds and returns 0.

**NOTES:**

At this time, it includes only Classic API Initialization Tasks.
This is an area in which user submissions or sponsorship of
a developer would be appreciated.

**EXAMPLES:**

The following is an example of how to use ``itask``:
.. code:: c

    SHLL \[/] $ itask
    #    NAME   ENTRY        ARGUMENT    PRIO   MODES  ATTRIBUTES   STACK SIZE
    ------------------------------------------------------------------------------
    0   UI1    \[0x2002258] 0 \[0x0]        1    nP      DEFAULT     4096 \[0x1000]

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_ITASK
.. index:: CONFIGURE_SHELL_COMMAND_ITASK

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_ITASK`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_ITASK`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_itask

The ``itask`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_itask(
    int    argc,
    char \**argv
    );

The configuration structure for the ``itask`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_ITASK_Command;

extension - display information about extensions
------------------------------------------------
.. index:: extension

**SYNOPSYS:**

.. code:: c

    extension \[id \[id ...] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of User Extensions currently active in the system.

If invoked with a set of ids as arguments, then just
those objects are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of using the ``extension`` command
on a system with no user extensions.
.. code:: c

    SHLL \[/] $ extension
    ID       NAME
    ------------------------------------------------------------------------------

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_EXTENSION
.. index:: CONFIGURE_SHELL_COMMAND_EXTENSION

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_EXTENSION`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_EXTENSION`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_extension

The ``extension`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_extension(
    int    argc,
    char \**argv
    );

The configuration structure for the ``extension`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_EXTENSION_Command;

task - display information about tasks
--------------------------------------
.. index:: task

**SYNOPSYS:**

.. code:: c

    task \[id \[id ...] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of Classic API Tasks currently active in the system.

If invoked with a set of ids as arguments, then just
those objects are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of how to use the ``task`` on an
application with just two Classic API tasks:
.. code:: c

    SHLL \[/] $ task
    ID       NAME   PRIO   STAT   MODES  EVENTS   WAITID  WAITARG  NOTES
    ------------------------------------------------------------------------------
    0a010001   UI1      1   SUSP   P:T:nA  NONE
    0a010002   SHLL   100   READY  P:T:nA  NONE

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_TASK
.. index:: CONFIGURE_SHELL_COMMAND_TASK

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_TASK`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_TASK`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_task

The ``task`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_task(
    int    argc,
    char \**argv
    );

The configuration structure for the ``task`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_TASK_Command;

queue - display information about message queues
------------------------------------------------
.. index:: queue

**SYNOPSYS:**

.. code:: c

    queue \[id \[id ... ] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of Classic API Message Queues currently active in the system.

If invoked with a set of ids as arguments, then just
those objects are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of using the ``queue`` command
on a system with no Classic API Message Queues.
.. code:: c

    SHLL \[/] $ queue
    ID       NAME   ATTRIBUTES   PEND   MAXPEND  MAXSIZE
    ------------------------------------------------------------------------------

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_QUEUE
.. index:: CONFIGURE_SHELL_COMMAND_QUEUE

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_QUEUE`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_QUEUE`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_queue

The ``queue`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_queue(
    int    argc,
    char \**argv
    );

The configuration structure for the ``queue`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_QUEUE_Command;

sema - display information about semaphores
-------------------------------------------
.. index:: sema

**SYNOPSYS:**

.. code:: c

    sema \[id \[id ... ] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of Classic API Semaphores currently active in the system.

If invoked with a set of objects ids as arguments, then just
those objects are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of how to use ``sema``:
.. code:: c

    SHLL \[/] $ sema
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

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_SEMA
.. index:: CONFIGURE_SHELL_COMMAND_SEMA

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_SEMA`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_SEMA`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_sema

The ``sema`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_sema(
    int    argc,
    char \**argv
    );

The configuration structure for the ``sema`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_SEMA_Command;

region - display information about regions
------------------------------------------
.. index:: region

**SYNOPSYS:**

.. code:: c

    region \[id \[id ... ] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of Classic API Regions currently active in the system.

If invoked with a set of object ids as arguments, then just
those object are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of using the ``region`` command
on a system with no user extensions.
.. code:: c

    SHLL \[/] $ region
    ID       NAME   ATTR        STARTADDR LENGTH    PAGE_SIZE USED_BLOCKS
    ------------------------------------------------------------------------------

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_REGION
.. index:: CONFIGURE_SHELL_COMMAND_REGION

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_REGION`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_REGION`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_region

The ``region`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_region(
    int    argc,
    char \**argv
    );

The configuration structure for the ``region`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_REGION_Command;

part - display information about partitions
-------------------------------------------
.. index:: part

**SYNOPSYS:**

.. code:: c

    part \[id \[id ... ] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of Classic API Partitions currently active in the system.

If invoked with a set of object ids as arguments, then just
those objects are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of using the ``part`` command
on a system with no user extensions.
.. code:: c

    SHLL \[/] $ part
    ID       NAME   ATTR        STARTADDR LENGTH    BUF_SIZE  USED_BLOCKS
    ------------------------------------------------------------------------------

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_PART
.. index:: CONFIGURE_SHELL_COMMAND_PART

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_PART`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_PART`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_part

The ``part`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_part(
    int    argc,
    char \**argv
    );

The configuration structure for the ``part`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_PART_Command;

object - display information about rtems objects
------------------------------------------------
.. index:: object

**SYNOPSYS:**

.. code:: c

    object \[id \[id ...] ]

**DESCRIPTION:**

When invoked with a set of object ids as arguments, then
a report on those objects is printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of how to use ``object``:
.. code:: c

    SHLL \[/] $ object 0a010001 1a010002
    ID       NAME   PRIO   STAT   MODES  EVENTS   WAITID  WAITARG  NOTES
    ------------------------------------------------------------------------------
    0a010001   UI1      1   SUSP   P:T:nA  NONE
    ID       NAME   ATTR        PRICEIL CURR_CNT HOLDID
    ------------------------------------------------------------------------------
    1a010002   TRmi   PR:BI:IN      0        1     00000000

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_OBJECT
.. index:: CONFIGURE_SHELL_COMMAND_OBJECT

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_OBJECT`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_OBJECT`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_object

The ``object`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_object(
    int    argc,
    char \**argv
    );

The configuration structure for the ``object`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_OBJECT_Command;

driver - display the rtems device driver table
----------------------------------------------
.. index:: driver

**SYNOPSYS:**

.. code:: c

    driver [ major [ major ... ] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of Device Drivers currently active in the system.

If invoked with a set of major numbers as arguments, then just
those Device Drivers are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of how to use ``driver``:
.. code:: c

    SHLL \[/] $ driver
    Major      Entry points
    ------------------------------------------------------------------------------
    0          init: \[0x200256c];  control: \[0x20024c8]
    open: \[0x2002518];  close: \[0x2002504]
    read: \[0x20024f0];  write: \[0x20024dc]
    1          init: \[0x20023fc];  control: \[0x2002448]
    open: \[0x0];  close: \[0x0]
    read: \[0x0];  write: \[0x0]
    SHLL \[/] $

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_DRIVER
.. index:: CONFIGURE_SHELL_COMMAND_DRIVER

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_DRIVER`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_DRIVER`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_driver

The ``driver`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_driver(
    int    argc,
    char \**argv
    );

The configuration structure for the ``driver`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_DRIVER_Command;

dname - displays information about named drivers
------------------------------------------------
.. index:: dname

**SYNOPSYS:**

.. code:: c

    dname

**DESCRIPTION:**

This command XXX

WARNING! XXX This command does not appear to work as of 27 February 2008.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

NONE

**EXAMPLES:**

The following is an example of how to use ``dname``:
.. code:: c

    EXAMPLE_TBD

**CONFIGURATION:**

.. index:: CONFIGURE_SHELL_NO_COMMAND_DNAME
.. index:: CONFIGURE_SHELL_COMMAND_DNAME

This command is included in the default shell command set.
When building a custom command set, define``CONFIGURE_SHELL_COMMAND_DNAME`` to have this
command included.

This command can be excluded from the shell command set by
defining ``CONFIGURE_SHELL_NO_COMMAND_DNAME`` when all
shell commands have been configured.

**PROGRAMMING INFORMATION:**

.. index:: rtems_shell_rtems_main_dname

The ``dname`` is implemented by a C language function
which has the following prototype:
.. code:: c

    int rtems_shell_rtems_main_dname(
    int    argc,
    char \**argv
    );

The configuration structure for the ``dname`` has the
following prototype:
.. code:: c

    extern rtems_shell_cmd_t rtems_shell_DNAME_Command;

pthread - display information about POSIX threads
-------------------------------------------------
.. index:: pthread

**SYNOPSYS:**

.. code:: c

    pthread \[id \[id ...] ]

**DESCRIPTION:**

When invoked with no arguments, this command prints information on
the set of POSIX API threads currently active in the system.

If invoked with a set of ids as arguments, then just
those objects are included in the information printed.

**EXIT STATUS:**

This command returns 0 on success and non-zero if an error is encountered.

**NOTES:**

This command is only available when the POSIX API is configured.

**EXAMPLES:**

The following is an example of how to use the ``task`` on an
application with four POSIX threads:
.. code:: c

    SHLL \[/] $ pthread
    ID       NAME           PRI  STATE MODES   EVENTS    WAITID  WAITARG  NOTES
    ------------------------------------------------------------------------------
    0b010002   Main           133 READY  P:T:nA    NONE   43010001 0x7b1148
    0b010003   ISR            133 Wcvar  P:T:nA    NONE   43010003 0x7b1148
    0b01000c                  133 READY  P:T:nA    NONE   33010002 0x7b1148
    0b01000d                  133 Wmutex P:T:nA    NONE   33010002 0x7b1148

**CONFIGURATION:**

This command is part of the monitor commands which are always
available in the shell.

**PROGRAMMING INFORMATION:**

This command is not directly available for invocation.

.. COMMENT: COPYRIGHT (c) 1988-2008.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

