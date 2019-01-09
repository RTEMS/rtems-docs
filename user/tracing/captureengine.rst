.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018 Vidushi Vashishth <vidushivashishth96@gmail.com>

.. _capturengine:

Capture Engine
**************

Capture Engine is a trace tool built inside the RTEMS operating system. Capture
Engine is designed to cause the lowest load on the system when operating. Hence
it does not effect RTEMS when operating or when disabled. It binds to RTEMS at
runtime and does not require RTEMS or your application to be rebuilt in order
to use it.

The Capture Engine's sample testcase for the `sparc/erc32` is available in
build directory created when building RTEMS in the path
file: `sparc-rtems5/c/erc32/testsuites/samples`. In order to access the capture
testcase perform the following set of operations inside the RTEMS build
directory.

.. code-block:: shell

  $ cd /sparc-rtems5/c/erc32/testsuites/samples
  $ sparc-rtems5-run ./capture.exe


  *** BEGIN OF TEST CAPTURE ENGINE ***
  *** TEST VERSION: 5.0.0.de9b7d712bf5da6593386fd4fbca0d5f8b8431d8
  *** TEST STATE: USER_INPUT
  *** TEST BUILD: RTEMS_NETWORKING RTEMS_POSIX_API
  *** TEST TOOLS: 7.3.0 20180125 (RTEMS 5, RSB a3a6c34c150a357e57769a26a460c475e188438f, Newlib 3.0.0)
  Press any key to start capture engine (20s remaining)
  Press any key to start capture engine (19s remaining)
  Press any key to start capture engine (18s remaining)

  Monitor ready, press enter to login.

  1-rtems $

Capture Engine comes with a set of commands to perform various actions.

Capture Engine Commands
-----------------------

1) ``copen <buffer-size>``: Used to initialize the Capture Engine with the
   trace buffer size in bytes. By default the Capture Engine is not initialized
   and not running.

2) ``cwceil <priority-value>``: Capture Engine filter used to put an upper
   limit on the event priority to be captured.

3) ``cwfloor <priority-value>``: Capture Engine filter used to put a lower
   limit on the event priority to be captured.

4) ``cwglob <on/off>``: Enable or disable the global watch.

5) ``cenable``: Enables the Capture Engine. Capture Engine is by default
   disabled after being opened.

6) ``cdisable``: Disables the Capture Engine.

7) ``ctlist``: Lists the watch and trigger configurations.

8) ``ctrace``: Dumps the recorded traces. By default this command displays 24
   trace records. Repeated use of this command will display all the recorded
   traces.

9) ``cwadd <task-name>``: Add watch on a particular task.

10) ``cwtctl <task-name> <on/off>``: Enable or disable watch on a particular
    task.

11) ``ctset``: Used to set a trigger. The general form of the command is:

``ctset [-?] type [to name/id] [from] [from name/id]``

`type` in the above command refers to the type of trigger needed. The types of
triggers that currently exist are:

- switch  : a context switch from one task to another task
- create  : the executing task creates a task
- start   : the executing task starts a task
- restart : the executing task restarts a task
- delete  : the executing task deletes a task
- begin   : a task is beginning
- exitted : a task is exitting

Example
-------

The following is a sample run of the capture testsuite. The `test1` command on
the Capture Engine Command Line Interface (CLI) makes the `RMON` task invoke a
call to the `capture_test_1()` command. This function (in the `test1.c` source
code) creates and starts three tasks : `CT1a`, `CT1b` and `CT1c`. These tasks
are passed the object id of a semaphore as a task argument. This run through
traces the context switches between these tasks. ``cwceil`` and ``cwfloor`` are
set to a narrow range of task priorities to avoid creating noise from a large
number of context switches between tasks we are not interested in.

.. code:: shell

  *** BEGIN OF TEST CAPTURE ENGINE ***
  *** TEST VERSION: 5.0.0.de9b7d712bf5da6593386fd4fbca0d5f8b8431d8
  *** TEST STATE: USER_INPUT
  *** TEST BUILD: RTEMS_NETWORKING RTEMS_POSIX_API
  *** TEST TOOLS: 7.3.0 20180125 (RTEMS 5, RSB a3a6c34c150a357e57769a26a460c475e188438f, Newlib 3.0.0)
  Press any key to start capture engine (20s remaining)
  Press any key to start capture engine (19s remaining)
  Press any key to start capture engine (18s remaining)
  Press any key to start capture engine (17s remaining)

  Monitor ready, press enter to login.

  1-rtems $ copen 50000
  capture engine opened.
  1-rtems $ cwceil 100
  watch ceiling is 100.
  1-rtems $ cwfloor 102
  watch floor is 102.
  1-rtems $ cwglob on
  global watch enabled.
  1-rtems $ ctset RMON
  trigger set.
  1-rtems $ cenable
  capture engine enabled.
  1-rtems $ test1
  1-rtems $ cdisable
  capture engine disabled.
  1-rtems $ ctrace
  0 0:18:17.462314124           0a010003 CT1a 102 102 102   4096  TASK_RECORD
  0 0:18:17.462398963         0 0a010003 CT1a 102 102             CREATED
  0 0:18:17.462647987    249024 0a010003 CT1a 102 102             STARTED
  0 0:18:17.462904334    256347 0a010003 CT1a 102 102             SWITCHED_IN
  0 0:18:17.463069129    164795 0a010003 CT1a 102 102             BEGIN
  0 0:18:17.463335853    266724 0a010003 CT1a 102 102             SWITCHED_OUT
  0 0:18:18.461348547           0a010004 CT1b 101 101 101   4096  TASK_RECORD
  0 0:18:18.461433997 998098144 0a010004 CT1b 101 101             CREATED
  0 0:18:18.461683631    249634 0a010004 CT1b 101 101             STARTED
  0 0:18:18.461934485    250854 0a010004 CT1b 101 101             SWITCHED_IN
  0 0:18:18.462099891    165406 0a010004 CT1b 101 101             BEGIN
  0 0:18:19.460935339 998835448 0a010004 CT1b 101 101             SWITCHED_OUT
  0 0:18:19.461431555           0a010005 CT1c 100 100 100   4096  TASK_RECORD
  0 0:18:19.461516394    581055 0a010005 CT1c 100 100             CREATED
  0 0:18:19.461765418    249024 0a010005 CT1c 100 100             STARTED
  0 0:18:19.462019324    253906 0a010005 CT1c 100 100             SWITCHED_IN
  0 0:18:19.462184119    164795 0a010005 CT1c 100 100             BEGIN
  0 0:18:19.462475257    291138 0a010005 CT1c 100 100             SWITCHED_OUT
  0 0:18:19.462551551     76294 0a010004 CT1b 101 101             SWITCHED_IN
  0 0:18:19.960935645 498384094 0a010004 CT1b 101 101             SWITCHED_OUT
  0 0:18:19.961012549     76904 0a010003 CT1a 102 100             SWITCHED_IN
  0 0:18:19.961341528    328979 0a010003 CT1a 102 102             SWITCHED_OUT
  1-rtems $ ctrace
  0 0:18:19.961418433         0 0a010005 CT1c 100 100             SWITCHED_IN
  0 0:18:19.961672339    253906 0a010005 CT1c 100 100             SWITCHED_OUT
  0 0:18:19.961749854     77515 0a010004 CT1b 101 101             SWITCHED_IN
  0 0:18:20.460967077 499217223 0a010004 CT1b 101 101             SWITCHED_OUT
  0 0:18:20.461219763    252686 0a010005 CT1c 100 100             SWITCHED_IN
  0 0:18:20.461424231    204468 0a010005 CT1c 100 100             TERMINATED
  0 0:18:20.461747107    322876 0a010005 CT1c 100 100             SWITCHED_OUT
  0 0:18:20.461824011     76904 0a010004 CT1b 101 101             SWITCHED_IN
  0 0:18:20.462015052    191041 0a010004 CT1b 101 101             TERMINATED
  0 0:18:20.462336707    321655 0a010004 CT1b 101 101             SWITCHED_OUT
  0 0:18:20.462414222     77515 0a010003 CT1a 102 102             SWITCHED_IN
  0 0:18:20.462608924    194702 0a010003 CT1a 102 102             TERMINATED
  0 0:18:20.462933021    324097 0a010003 CT1a 102 102             SWITCHED_OUT
  1-rtems $ ctrace
  1-rtems $
