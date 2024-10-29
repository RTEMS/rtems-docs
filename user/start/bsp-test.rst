.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH & Co. KG
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBSPTest:

Test a Board Support Package (BSP)
==================================

You built a BSP with tests in the previous section.  We built the
``sparc/erc32`` BSP in :file:`$HOME/quick-start/src/rtems`.

You should run the RTEMS test suite on your target hardware.  The RTEMS Project
provides some support to do this, see the :ref:`Testing <Testing>` chapter for
the details.

On the ``sparc/erc32`` BSP we selected for this quick start chapter this is
easy.  Just run this command:

.. code-block:: none

    cd $HOME/quick-start/src/rtems
    rtems-test --rtems-bsp=erc32-sis build/sparc/erc32

This command should output something like this (omitted lines are denoted by
...).  In this output the base directory :file:`$HOME/quick-start` was replaced
by ``$BASE``.

.. code-block:: none

    RTEMS Testing - Tester, @rtems-ver-major@.@rtems-ver-minor@.not_released
     Command Line: $BASE/rtems/@rtems-ver-major@/bin/rtems-test --rtems-bsp=erc32-sis build/sparc/erc32
     Host: Linux 5.8.0-44-generic #50~20.04.1-Ubuntu SMP Wed Feb 10 21:07:30 UTC 2021 x86_64
    Python: 3.8.5 (default, Jan 27 2021, 15:41:15) [GCC 9.3.0]
    Host: Linux-5.8.0-44-generic-x86_64-with-glibc2.29 (Linux 5.8.0-44-generic #50~20.04.1-Ubuntu SMP Wed Feb 10 21:07:30 UTC 2021 x86_64 x86_64)
    [  1/570] p:0   f:0   u:0   e:0   I:0   B:0   t:0   L:0   i:0   W:0   | sparc/erc32: dhrystone.exe
    ...
    [570/570] p:554 f:2   u:6   e:1   I:0   B:3   t:0   L:0   i:0   W:0   | sparc/erc32: ts-validation-1.exe

    Passed:        558
    Failed:          2
    User Input:      6
    Expected Fail:   1
    Indeterminate:   0
    Benchmark:       3
    Timeout:         0
    Test too long:   0
    Invalid:         0
    Wrong Version:   0
    Wrong Build:     0
    Wrong Tools:     0
    ------------------
    Total:         570
    Failures:
    dl06.exe
    minimum.exe
    User Input:
    dl10.exe
    monitor.exe
    termios.exe
    top.exe
    capture.exe
    fileio.exe
    Expected Fail:
    psxfenv01.exe
    Benchmark:
    dhrystone.exe
    linpack.exe
    whetstone.exe
    Average test time: 0:00:00.371256
    Testing time     : 0:03:31.616055
