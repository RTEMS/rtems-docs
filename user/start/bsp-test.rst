.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber

.. _QuickStartBSPTest:

Test a Board Support Package (BSP)
==================================

You built a BSP with tests in the previous section.  We built the ``erc32`` BSP
in :file:`$HOME/quick-start/build/b-erc32`.

You should run the RTEMS test suite on your target hardware.  The RTEMS Project
provides some support to do this, see the :ref:`Testing <Testing>` chapter for
the details.

On the ``erc32`` BSP we selected for this quick start chapter this is easy.
Just run this command:

.. code-block:: none

    cd $HOME/quick-start/build/b-erc32
    rtems-test --rtems-bsp=erc32 --rtems-tools=$HOME/quick-start/rtems/5 .

This command should output something like this (omitted lines are denoted by
...).  In this output the base directory :file:`$HOME/quick-start` was replaced
by ``$BASE``.

.. code-block:: none

    RTEMS Testing - Tester, 5.0.not_released
     Command Line: $BASE/rtems/5/bin/rtems-test --rtems-bsp=erc32 --rtems-tools=$BASE/rtems/5 .
     Python: 2.7.15 (default, Jan 10 2019, 01:14:47) [GCC 4.2.1 Compatible FreeBSD Clang 6.0.1 (tags/RELEASE_601/final 335540)]
    Host: FreeBSD-12.0-RELEASE-p2-amd64-64bit-ELF (FreeBSD Build_FreeBSD12 12.0-RELEASE-p2 FreeBSD 12.0-RELEASE-p2 GENERIC amd64 amd64)
    [  1/589] p:0   f:0   u:0   e:0   I:0   B:0   t:0   i:0   W:0   | sparc/erc32: dhrystone.exe
    ...
    [589/589] p:574 f:0   u:5   e:0   I:0   B:3   t:0   i:0   W:0   | sparc/erc32: tmtimer01.exe

    Passed:        580
    Failed:          0
    User Input:      5
    Expected Fail:   0
    Indeterminate:   0
    Benchmark:       3
    Timeout:         1
    Invalid:         0
    Wrong Version:   0
    Wrong Build:     0
    Wrong Tools:     0
    ------------------
    Total:         589
    User Input:
     monitor.exe
     termios.exe
     top.exe
     fileio.exe
     capture.exe
    Benchmark:
     whetstone.exe
     linpack.exe
     dhrystone.exe
    Timeouts:
     pppd.exe
    Average test time: 0:00:00.437773
    Testing time     : 0:04:17.848557
