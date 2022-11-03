.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH

.. Copyright (C) 2022 Karel Gardas <karel@functional.vision>

stm32h7
=======

This BSP supports the
`STM32H7 Series <https://www.st.com/en/microcontrollers-microprocessors/stm32h7-series.html>`_.

The BSP is known to run on these boards on specified core with using specified BSP variant.

.. table::

  +----------------------------------------------------------------------------------+-----------+------------------------+
  | Board name                                                                       | Core name |  BSP variant name      |
  +==================================================================================+===========+========================+
  |`STM32H743I-EVAL 2 <https://www.st.com/en/evaluation-tools/stm32h743i-eval.html>`_| M7        | arm/stm32h7            |
  +----------------------------------------------------------------------------------+-----------+------------------------+
  |`STM32H743ZI-Nucleo <https://www.st.com/en/evaluation-tools/nucleo-h743zi.html>`_ | M7        | arm/nucleo-h743zi      |
  +----------------------------------------------------------------------------------+-----------+------------------------+
  |`STM32H7B3I-DK <https://www.st.com/en/evaluation-tools/stm32h7b3i-dk.html>`_      | M7        | arm/stm32h7b3i-dk      |
  +----------------------------------------------------------------------------------+-----------+------------------------+
  |`STM32H757I-EVAL <https://www.st.com/en/evaluation-tools/stm32h757i-eval.html>`_  | M7        | arm/stm32h757i-eval    |
  |                                                                                  +-----------+------------------------+
  |                                                                                  | M4        | arm/stm32h757i-eval-m4 |
  +----------------------------------------------------------------------------------+-----------+------------------------+
  |`STM32H747I-DISCO <https://www.st.com/en/evaluation-tools/stm32h747i-disco.html>`_| M7        | arm/stm32h747i-disco   |
  |                                                                                  +-----------+------------------------+
  |                                                                                  | M4        | arm/stm32h747i-disco-m4|
  +----------------------------------------------------------------------------------+-----------+------------------------+


Clock Driver
------------

The clock driver uses the `ARMv7-M Systick` module. The HSE (external
oscillator) value can also be different for different evaluation or custom
boards, so it is recommended to check the default values of the BSP.

Console Driver
--------------

The console driver supports the on-chip UART and USART modules. Even
the MCU supports about 10 U(S)ARTs, only those supported by the chosen
board are enabled by default configuration. The board needs to support
some kind of connector-based connection to the U(S)ART in order for the
feature to be considered supported here.
..
.. Leaving previous notes here as a comment. They may still be useful
.. and incorporated into the later version of the document.
..
.. Different board variations use different GPIO pins and blocks for the default
.. communication UART and it is recommended to check whether the default
.. configuration provided is valid in the BSP.

.. To specify that the BSP should be built for the STM32H743ZI-Nucleo board,
.. users can supply ``STM32H743ZI_NUCLEO = True`` to ``config.ini`` when
.. building the BSP.

.. Alternatively, users can supply the configuration structs defined in ``hal.h``
.. in the application for other boards. For the console driver, the
.. ``stm32h7_usartX_config`` structs are used to configure the GPIO pins and other
.. parameters. The default implementations can be found in
.. ``bsps/arm/stm32ht/console`` in the RTEMS sources.

Network Interface Driver
------------------------

The network interface driver ``if_stmac`` is provided by the ``libbsd``.

USB Host Driver
---------------

The USB host driver ``dwc_otg`` is provided by the ``libbsd``.

SD/MMC Driver
-------------

The SDMMC driver ``st_sdmmc`` is provided by the ``libbsd``.

The default initialization is done for the STM32H743I-EVAL 2 board.

To use different pins, you can create a ``HAL_SD_MspInit()`` function in your
application that overwrites the default one defined in ``RTEMS``. If you don't
have direction lines like on the evaluation board, you can just skip
initializing these pins.

If you want to use a different number of data lines, another polarity for the
data direction pins, a different voltage or similar, you have to redefine
``st_sdmmc_get_config()`` (normally provided by ``libbsd``) in your application.

Known limitations:

* Currently 1.8V signaling is not implemented. Therefore higher speeds like used
  for UHS cards are not available. All cards fall back to High Speed transfers.
* The driver uses the IDMA only. MDMA is currently not implemented. For SDMMC1
  that means that the memory buffers can only come from AXI SRAM, QSPI memory,
  Flash or the FMC (SDRAM, ...). The internal SRAM1, SRAM2, SRAM3 and SRAM4 are
  not supported. SDMMC2 should not have that limitation. See ST AN5200 "Getting
  started with STM32H7 Series SDMMC host controller" for more details.


How to run RTEMS on the board
-----------------------------
Following few paragraphs save a purpose of simple HOWTO or a quick
starting guide for the users not versed in STM32 toolchain and their
boards workflow.

Board hardware setup
^^^^^^^^^^^^^^^^^^^^
Connect board with the host computer using micro-USB cable connected
to micro-USB connector on the board marked with 'ST-LINK V3E' in case of evaluation
and discovery boards or with 'USB PWR' in case of Nucleo board.

STM32CubeIDE installation
^^^^^^^^^^^^^^^^^^^^^^^^^
Download and install STM32CubeIDE from
https://www.st.com/en/development-tools/stm32cubeide.html. Install the
software into the user directory. On Linux install with 'sudo' command
to install as a root since as part of the installation USB permissions
rules for ST-Link GDB server are also installed. The reason for
installing into the user directory is that the IDE is based on
Eclipse, which provides
its own update method and this will not work well in case of read-only
access to the installation directory. In case of any troubles consult
installation manual provided by ST here https://www.st.com/resource/en/user_manual/um2563-stm32cubeide-installation-guide-stmicroelectronics.pdf.
Although we will not used full fledged IDE here, the package provides ST-Link GDB Server which will be used for uploading RTEMS binaries to the board
memory.

STM32CubeProgrammer installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Download and install STM32CubeProgrammer from
https://www.st.com/en/development-tools/stm32cubeprog.html. We will
use this software for board setup required for RTEMS and later when
something goes wrong to delete content of the MCU flash memory. The
software is also internally used by the ST-Link GDB Server from
STM32CubeIDE so it is crucial to have it installed.

Board ST-Link firmware upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Download ST-Link board firmware upgrade package from
https://www.st.com/en/development-tools/stsw-link007.html. The
software is distributed in a form of Java jar file for Linux and Mac
OSX and in a form of Windows binary for MS Windows. Unpack it
somewhere and run it with

.. code-block:: shell

  $ unzip en.stsw-link007-v3-9-3_v3.9.3.zip
  $ cd stsw-link007/AllPlatforms
  $ java -jar STLinkUpgrade.jar

Click on *Open in update mode* button and then if *Version* and *Update
to Firmware* version information are different in shown version number/code, click on *Upgrade*
button and wait till upgrade finishes.

.. note: On Linux you will need to have libusb library installed in
   order to make upgrade process working. On Ubuntu 20.04 LTS you can do
   that with following command.

.. code-block:: shell

   $ sudo apt install libusb-1.0-0


Dual core board setup for RTEMS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Current RTEMS BSP supports
running MCU in a single-core mode only on either M7 core or M4
core. That means that to not leave other core interfering with the
system we either need to upload short infinite loop code to it or we
may switch off the core completely. The second option is what is
described here. The board by default switches on and starts both
cores. Based on chosen BSP variant you may like to switch off other
core with using STMCubeProgrammer tool.
Go to the directory where you have installed STMCubeProgrammer
software and run it with

.. code-block:: shell

                $ cd bin
                $ ./STM32CubeProgrammer


.. important:: It is absolutely necessary you will do that from inside the bin
   directory where STM32CubeProgrammer binary resides. If you don't, then
   programmer UI will crash on attempt to connect to the board. Probable
   reason is a bug in the programmer which is not able to correctly locate
   its C dynamic library responsible for connecting to the ST-Link board
   interface. Version 2.9.0 of the programmer is described here. Other
   versions may behave a bit differently.

When you start the programmer application, the UI window of the programmer will
appear.
Click on green *Connect* button in the right upper corner of
the UI. This will connect programmer to the board.
Then click on *OB*
icon in the left upper corner. Actually this is hidden menu item which you
can un-hide by clicking on menu icon (three horizontal stripes) in the
upper left corner.
When you click on *OB* or *Option bytes* in un-hidden state, then
click on *User Configuration* in the options list and when the user
configuration list opens
unselect preselected *BCM4* item inside it to switch off M4 core or
unselect preselected *BCM7* item to switch off M7 core from
starting up. The action needs to be saved by clicking on *Apply* button
below the option table.

.. warning:: Be careful! Wrong setup in STM32H7 configuration may result in
             *bricked* board.

Do not forget to disconnect the programmer application from the board by clicking on green *Disconnect* button
in the upper right corner and then close the programmer UI.

.. important:: If you keep programmer connected then you will not be able
   to connect ST-Link GDB server to the board and upload RTEMS binary to
   it.


STM32CubeIDE ST-Link GDB Server setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to use STM provided ST-Link GDB server externally, that is
not from inside the IDE, we need to configure it. Please go to the
directory where you have installed STM32CubeIDE software. Look for
file containing *ST-LINK* string inside its name. Following shell
command sequence shows example about how to find it.

.. code-block:: shell

                $ cd $HOME/sfw/stm32cubeide_1.8.0
                $ find . -name 'ST-LINK*'
                ./plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.200.202202231230/tools/bin/ST-LINK_gdbserver.sh
                ./plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.200.202202231230/tools/bin/ST-LINK_gdbserver
                ./plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.100.202109301221/tools/bin/ST-LINK_gdbserver.sh
                ./plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.100.202109301221/tools/bin/ST-LINK_gdbserver

Notice that in this particular installation case we already have two
versions of GDB server installed. This is due to fact that version
1.8.0 of the IDE was later upgraded to 1.9.0 version. Anyway, we will choose
to use the latest one, or if there is only one, then the only one
installed. Please go to its *bin* directory. E.g.

.. code-block:: shell

                $ cd plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.200.202202231230/tools/bin

Now, you will need to edit provided *config.txt* file inside the
directory. Use your favorite editor. Open the file and scrolls
down to its end. You will see following comment:

.. code-block:: none

                ###############################################################
                #  -cp <path>         : Path to STM32CubeProgrammer
                #                       Modify to correct path
                #                       for STM32_Programmer_CLI executable
                ###############################################################
                -cp

and here you will need to place path where your STM32CubeProgrammer is
installed directly behind the *-cp* parameter. E.g.

.. code-block:: none

                ###############################################################
                #  -cp <path>         : Path to STM32CubeProgrammer
                #                       Modify to correct path
                #                       for STM32_Programmer_CLI executable
                ###############################################################
                -cp /home/karel/sfw/stm32cubeide_1.8.0/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_2.0.200.202202231230/tools/bin

Once you are done with it, you can save the file and close the
editor. Let's verify that GDB server is configured and running well by starting
it inside the shell. Please go inside the directory where
ST-LINK_gdbserver.sh is located and run it by:

.. code-block:: shell

                $ ./ST-LINK_gdbserver.sh

If everything is all right and if you have board still connected to
the host computer then you should see output like following:

.. code-block:: shell

                $ ./ST-LINK_gdbserver.sh

                STMicroelectronics ST-LINK GDB server. Version 6.1.0
                Copyright (c) 2022, STMicroelectronics. All rights reserved.

                Starting server with the following options:
                Persistent Mode            : Enabled
                LogFile Name               : debug.log
                Logging Level              : 31
                Listen Port Number         : 61234
                Status Refresh Delay       : 15s
                Verbose Mode               : Disabled
                SWD Debug                  : Enabled

                COM frequency = 24000 kHz
                Target connection mode: Default
                Reading ROM table for AP 0 @0xe00fefd0
                Hardware watchpoint supported by the target
                ST-LINK Firmware version : V3J9M3
                Device ID: 0x450
                PC: 0x8028fa4
                ST-LINK device status: HALT_MODE
                ST-LINK detects target voltage = 3.28 V
                ST-LINK device status: HALT_MODE
                ST-LINK device initialization OK
                Stm32Device, pollAndNotify running...
                SwvSrv state change: 0 -> 1
                Waiting for connection on port 61235...
                Waiting for debugger connection...
                Waiting for connection on port 61234...

In output above you can see ST-Link GDB server waiting for debugger
connection. If this is the case in your case, then you can finish GDB server by hitting
*Ctrl-C* key combination.

RTEMS BSP samples build and run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We will use STM32H747I-DISCO board as an example hereafter. If you use
different board please adjust configuration steps in BSP configuration
accordingly. You should use BSP variant name specified for your
particular board in the table above.

Generate default configuration for the board:

.. code-block:: shell

                $ ./waf bspdefaults --rtems-bsps=arm/stm32h747i-disco > stm32h747i-disco.ini
                Regenerate build specification cache (needs a couple of seconds)...

To run basic hello world or ticker samples you do not need to modify
default BSP configuration here as the compilation of basic RTEMS demo samples is
enabled by default. Let's continue with configuration of
the RTEMS source by running following command. Please change the RTEMS
tools installation prefix to suite your installation.

.. code-block:: shell

                $ ./waf configure --rtems-bsps=arm/stm32h747i-disco --rtems-config=./stm32h747i-disco.ini --rtems-tools=$HOME/workspace/rtems-tools
                Setting top to                           : /home/rtems/workspace/rtems
                Setting out to                           : /home/rtems/workspace/rtems/build
                Configure board support package (BSP)    : arm/stm32h747i-disco
                Checking for program 'arm-rtems6-gcc'    : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-gcc
                Checking for program 'arm-rtems6-g++'    : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-g++
                Checking for program 'arm-rtems6-ar'     : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-ar
                Checking for program 'arm-rtems6-ld'     : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-ld
                Checking for program 'ar'                : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-ar
                Checking for program 'g++, c++'          : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-g++
                Checking for program 'ar'                : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-ar
                Checking for program 'gas, gcc'          : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-gcc
                Checking for program 'ar'                : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-ar
                Checking for program 'gcc, cc'           : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-gcc
                Checking for program 'ar'                : /home/rtems/workspace/rtems-tools/bin/arm-rtems6-ar
                Checking for asm flags '-MMD'            : yes
                Checking for c flags '-MMD'              : yes
                Checking for cxx flags '-MMD'            : yes
                'configure' finished successfully (0.454s)

Build the BSP including samples using *build* command:

.. code-block:: shell

                $ ./waf build

the command outputs a lot of information about files being compiled
and ends with output like:

.. code-block:: shell

                Waf: Leaving directory `/home/rtems/workspace/rtems/build/arm/stm32h747i-disco'
                'build_arm/stm32h747i-disco' finished successfully (12.086s)

As your RTEMS BSP including samples is compiled, we will proceed with
running the hello world sample on the board now.
Open 3 shell windows for the test on the host computer. Also make sure
board is connected to the computer and is running. It does not matter
if manufacturer's demo is running there or if you navigated to some
demo part and left it there. ST-Link GDB server always takes over the
board when connected to it.

Start GDB server in the first window by switching to GDB server
directory and running the shell script. This is from testing machine
installation, the path to GDB server will probably look different in your
installation case.

.. code-block:: shell

                $ cd sfw/stm32cubeide_1.8.0/plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.200.202202231230/tools/bin
                $ ./ST-LINK_gdbserver.sh

                STMicroelectronics ST-LINK GDB server. Version 6.1.0
                Copyright (c) 2022, STMicroelectronics. All rights reserved.

                Starting server with the following options:
                Persistent Mode            : Enabled
                LogFile Name               : debug.log
                Logging Level              : 31
                Listen Port Number         : 61234
                Status Refresh Delay       : 15s
                Verbose Mode               : Disabled
                SWD Debug                  : Enabled

                COM frequency = 24000 kHz
                Target connection mode: Default
                Reading ROM table for AP 0 @0xe00fefd0
                Hardware watchpoint supported by the target
                ST-LINK Firmware version : V3J9M3
                Device ID: 0x450
                PC: 0x8028fa4
                ST-LINK device status: HALT_MODE
                ST-LINK detects target voltage = 3.28 V
                ST-LINK device status: HALT_MODE
                ST-LINK device initialization OK
                Stm32Device, pollAndNotify running...
                SwvSrv state change: 0 -> 1
                Waiting for connection on port 61235...
                Waiting for debugger connection...
                Waiting for connection on port 61234...

In second shell window you will need to run your terminal program and
connect to the board virtual serial port. Following steps describes
how to do that on the Ubuntu 20.04. The recommended way here is to use minicom. Let's install it
first by:

.. code-block:: shell

                $ sudo apt install minicom

And run it with root privileges to be able to reach USB serial port
provided by board:

.. code-block:: shell

                $ sudo minicom -s

The minicom is invoked with configuration menu open. Go into the
*Serial port setup* and hit *a* key to select *Serial Device*
setup. Change */dev/modem* from there into */dev/ttyACM0* and hit
*Enter* key. Hit *f* key to change hardware flow control from *Yes* to
*No*. When you are done with it, you can hit *Enter* key to finish
this part of configuration and then scrolls in menu to *Exit* and hit
*Enter* key on it. The minicom will switch to terminal mode with just
provided configuration.

In the third shell window navigate into the BSP build directory and start
RTEMS GDB with the hello.exe sample.

.. code-block:: shell

                $ arm-rtems6-gdb build/arm/stm32h747i-disco/testsuites/samples/hello.exe
                GNU gdb (GDB) 10.1.90.20210409-git
                Copyright (C) 2021 Free Software Foundation, Inc.
                License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
                This is free software: you are free to change and redistribute it.
                There is NO WARRANTY, to the extent permitted by law.
                Type "show copying" and "show warranty" for details.
                This GDB was configured as "--host=x86_64-linux-gnu --target=arm-rtems6".
                Type "show configuration" for configuration details.
                For bug reporting instructions, please see:
                <https://www.gnu.org/software/gdb/bugs/>.
                Find the GDB manual and other documentation resources online at:
                <http://www.gnu.org/software/gdb/documentation/>.

                For help, type "help".
                Type "apropos word" to search for commands related to "word"...
                Reading symbols from build/arm/stm32h747i-disco/testsuites/samples/hello.exe...
                (gdb)

Now, you need to connect GDB with the ST's GDB server by:

.. code-block:: shell

                (gdb) target extended-remote :61234
                Remote debugging using :61234
                0x08028fa4 in ?? ()
                (gdb)

and finally you will need to load hello.exe binary into the board
memory by:

.. code-block:: shell

                (gdb) load
                Loading section .start, size 0x458 lma 0x24000000
                Loading section .text, size 0xfca8 lma 0x24000480
                Loading section .init, size 0xc lma 0x24010128
                Loading section .fini, size 0xfecc lma 0x24010134
                Loading section .rodata, size 0x1aab lma 0x24020000
                Loading section .ARM.exidx, size 0x8 lma 0x24021aac
                Loading section .eh_frame, size 0x4 lma 0x24021ab4
                Loading section .init_array, size 0x4 lma 0x24021ab8
                Loading section .fini_array, size 0x4 lma 0x24021abc
                Loading section .rtemsroset, size 0x540 lma 0x24021ac0
                Loading section .data, size 0x6a4 lma 0x24022000
                Start address 0x24000400, load size 140923
                Transfer rate: 684 KB/sec, 2562 bytes/write.
                (gdb)

If everything went fine, then you can run the RTEMS binary by using
*cont* GDB command.

.. note:: Memory address values in the load output in the gdb shows
          that we have loaded our application into the AXI
          SRAM. Memory addresses will be different when loading into
          different part of MCU memory.

.. code-block:: shell

                (gdb) cont
                Continuing.

Note that this command should never finish. To see the actual output
from RTEMS switch to
the second shell window with minicom (or other terminal emulation
program) running and you should see hello output
there:

.. code-block:: none

                *** BEGIN OF TEST HELLO WORLD ***
                *** TEST VERSION: 6.0.0.50ce036cfbd9807a54af47eb60eadb6a33a9e82d
                *** TEST STATE: EXPECTED_PASS
                *** TEST BUILD:
                *** TEST TOOLS: 10.3.1 20220224 (RTEMS 6, RSB 49e3dac17765fa82ce2f754da839638ee352f95c, Newlib 64b2081)
                Hello World

                *** END OF TEST HELLO WORLD ***


                [ RTEMS shutdown ]
                RTEMS version: 6.0.0.50ce036cfbd9807a54af47eb60eadb6a33a9e82d
                RTEMS tools: 10.3.1 20220224 (RTEMS 6, RSB 49e3dac17765fa82ce2f754da839638ee352f95c, Newlib 64b2081)
                executing thread ID: 0x08a010001

Since default RTEMS BSP configuration resets the board after run
immediately you can also see output from the immediately started ST
demo:

.. code-block:: none

                STM32H747I-DISCO_MB1248: Out Of the Box Demonstration V1.0.1 (Build Aug 22 2019 at 11:56:22)
                STM32H747I-DISCO_MB1248: ST Menu Launcher V1.1.0
                CPU running at 400MHz, Peripherals at 100MHz/100Mz

which is not a problem here at all. Later we can reconfigure BSP to
not reset board to prevent demo output here.

How to load binary file into the QSPI NOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Connect the board to your host computer using micro-USB
cable. Start STM32CubeProgrammer and connect it to the board by
clicking on *Connect* button which is located in the right upper
corner of the programmer application UI. For accessing QSPI connected
memory you will need to configure programmer's external loader which
needs to match your target board. Click on *EL* icon (or *External
loaders*) in the left sidebar menu. Either go thorough the list of
external loaders or just search for your board by typing board
name (or part of the name) into the search bar located on top of the table view. When
you find your board, select it by selecting rectangle in the *Select*
table column. That's what is needed to make programmer ready to
program your board memory.
For uploading file to the board, you need to continue with clicking on
*Erase & programming* menu item in the left sidebar menu. It's second item
from the top. Now, let's select
your file to upload by clicking on *Browse* button and selecting the
file name from your host computer filesystem. The most important thing here is
to specify start address of flashing process. You need to do that by
typing start address into the *Start address* field.

.. note:: Usually external memory connected to QSPI has 0x90000000 starting
          address.

When all is set you can click on *Start Programming* button.

.. important:: Cube programmer is very picky about files it shows in the file list. The only recognized suffixes are: elf, bin, hex and
               similar. Also do not try to fool programmer by renaming let's say text
               file to bin file. It'll detect file type as ascii text and will not
               show it in the list of files to flash. So bin file type is really for
               media types like avi, jpeg, mpeg or for binary dumps from elf
               files. If you need to save text file, convert it to hex file first.
