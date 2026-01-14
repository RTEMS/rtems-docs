% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 TBD

# stm32f4

## How to Run an RTEMS Application on the Board

By following these simple steps, you can deploy your RTEMS application on
the board.
These steps include:

- Building your RTEMS Application,
  already discussed in the {ref}`Build Your Application <QuickStartAPP>`.
- [Flashing Application](#flashing-the-application) onto your board .
- Viewing the
  [Serial Monitor Output using OpenOCD](#serial-monitor-output-using-openocd).

### Flashing The Application

Open a shell or terminal on your host computer.
Make sure that your board is connected to your host computer.
It does not matter if any application is already running on your board.

For starting a GDB Server, we will use *OpenOCD*.
Download and install OpenOCD for your host operating system.

- Start OpenOCD using the configuration file for your board
  (this example uses the Nucleo-F4)

```shell
openocd -f board/st_nucleo_f4.cfg
```

Upon a successful connection, you will see output similar to this.

```none
$ openocd -f board/st_nucleo_f4.cfg
Open On-Chip Debugger 0.12.0
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
Info : The selected transport took over low-level target control. The results might differ compared to plain JTAG/SWD
srst_only separate srst_nogate srst_open_drain connect_deassert_srst

Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
Info : clock speed 2000 kHz
Info : STLINK V2J33M25 (API v2) VID:PID 0483:374B
Info : Target voltage: 3.249012
Info : [stm32f4x.cpu] Cortex-M4 r0p1 processor detected
Info : [stm32f4x.cpu] target has 6 breakpoints, 4 watchpoints
Info : starting gdb server for stm32f4x.cpu on 3333
Info : Listening on port 3333 for gdb connections

```

- You can see the port number in the output (in this case, 3333).
  The GDB server is listening on this port. This may be different in your case.
  Remember this port, as we are going use it connect to the GDB Server.

Open another shell or terminal. In this terminal we are going to launch
the RTEMS GDB and load our application on the board.

- We will launch the RTEMS GDB and
  pass our compiled application path along with it.

```shell
arm-rtems7-gdb path/to/your/compiled/application 
```

you will see the output as follows,

```none
$ arm-rtems7-gdb build/arm-rtems7-stm32f4/hello.exe
GNU gdb (GDB) 16.2
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "--host=x86_64-linux-gnu --target=arm-rtems7".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from build/arm-rtems7-stm32f4/hello.exe...
warning: File "/home/dell/quick-start/app/hello/build/arm-rtems7-stm32f4/hello.exe" auto-loading has been declined by your `auto-load safe-path' set to "$debugdir:$datadir/auto-load".
To enable execution of this file add
	add-auto-load-safe-path /home/dell/quick-start/app/hello/build/arm-rtems7-stm32f4/hello.exe
line to your configuration file "/home/dell/.config/gdb/gdbinit".
To completely disable this security protection add
	set auto-load safe-path /
line to your configuration file "/home/dell/.config/gdb/gdbinit".
For more information about this security protection see the
"Auto-loading safe path" section in the GDB manual.  E.g., run from the shell:
	info "(gdb)Auto-loading safe path"
(gdb) 
```

- Now, we will connect our RTEMS GDB to the OpenOCD GDB server.

```shell
target remote :<Your-PORT>
```

Example output.

```shell
(gdb) target remote :3333
Remote debugging using :3333
```

If you get the above output,
it means your RTEMS GDB is connected the OpenOCD server.

- Now, we are going to load our application on the board.

```shell
(gdb) load
```

This will load the application on your board.

Example output.

```none
(gdb) load
Loading section .start, size 0x28c lma 0x8000000
Loading section .text, size 0xe0f4 lma 0x80002c0
Loading section .init, size 0xc lma 0x800e3b4
Loading section .fini, size 0xc lma 0x800e3c0
Loading section .rodata, size 0x20f8 lma 0x800e3d0
Loading section .ARM.exidx, size 0x8 lma 0x80104c8
Loading section .eh_frame, size 0x4 lma 0x80104d0
Loading section .tdata, size 0xc lma 0x80104d4
Loading section .init_array, size 0x4 lma 0x80104e0
Loading section .fini_array, size 0x4 lma 0x80104e4
Loading section .rtemsroset, size 0x6c lma 0x80104e8
Loading section .data, size 0x4dc lma 0x8010554
Start address 0x08000188, load size 68088
Transfer rate: 20 KB/sec, 4005 bytes/write.
```

- since our application is loaded on the board, we may execute it.
  Enter the following command.

```shell
(gdb) cont
```

Example output.

```none
(gdb) cont
Continuing.
```

### Serial Monitor Output using OpenOCD

```{important}
Make sure the proper USART is enabled for the board.
```

To view any serial output, we need a Serial Monitor.
You can use whichever you want and available to you.
This guide uses minicom as an example.

Make sure your board is connected to the host computer and
that minicom is installed.

- We will configure the minicom first. Enter the command to open configure menu.

```shell
$ sudo minicom -s
```

This opens the miniconm configuration menu.

- Go into the
  *Serial port setup* and hit *a* key to select *Serial Device*
  setup.
- Change */dev/modem* from there into */dev/ttyACM0* and hit
  *Enter* key.
- Hit *f* key to change hardware flow control from *Yes* to
  *No*.
- When you are done with it, you can hit *Enter* key to finish
  this part of configuration and then scrolls in menu to *Exit* and hit
  *Enter* key on it.

Minicom will now switch to terminal mode with the new configuration.

Now, you can view your Serial output from your application on the minicom,
you can press the reset button on your board to re-run your application,
and observe its output on the Serial monitor.

Example output.

```none

Welcome to minicom 2.9

OPTIONS: I18n 
Port /dev/ttyACM0, 23:57:40

Press CTRL-A Z for help on special keys
                                                                                                    
                                                                                                    
Hello World                                                                                         
                                                                                                    
[ RTEMS shutdown ]                                                                                  
RTEMS version: 7.0.0.e96fd2398b63bc6975094c648a9981e10731de5c-modified
RTEMS tools: 15.2.0 20250808 (RTEMS 7, RSB 08d2e69f30b61de6bf0f5dbf06946d12d074d60e, Newlib 038afec1)
executing thread ID: 0x0a010001
executing thread name: UI1 
```
