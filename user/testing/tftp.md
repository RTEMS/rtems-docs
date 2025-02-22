% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

(tftp-and-uboot)=

# TFTP and U-Boot

```{index} TFTP, U-Boot, Testing
```

TFTP and U-Boot provides a simple way to test RTEMS on a network capable
target. The RTEMS Tester starts a TFTP server session for each test and the
target's boot monitor, in this case U-Boot request a file, any file, which the
TFTP server supplies. U-Boot loads the executable and boots it using a
standard U-Boot script.

The RTEMS Tester contains a TFTP server so no external TFTP server or
configuration is required. If you have an external TFTP server and wish to use
that resource the {ref}`tester-config-wait` directive can be used.

(fig-tester-tftp-u-boot)=

```{figure} ../../images/user/test-tftp.png
:alt: RTEMS Tester using TFTP and U-Boot
:figclass: align-center
:width: 35%

RTEMS Tester using TFTP and U-Boot.
```

The Figure {ref}`fig-tester-tftp-u-boot` figure shows the structure and
control flow of the RTEMS Tester using TFTP and U-boot. The executables are
built and the `rtems-test` command is run from the top of the build
directory.

This test mode can only support a single test job running at once. You cannot
add more test target hardware and run the tests in parallel.

## Target Hardware

The RTEMS Tester TFTP and U-Boot method of testing requires:

1. A target with network interface.
2. U-Boot, iPXE or similar boot loader with network driver support for your
   target hardware and support for the TFTP protocol.
3. Network power of IO switch.
4. Network DHCP server.
5. Console interface cable that matches your target's console UART interface.
6. Telnet terminal server. See {ref}`TesterConsoles`.

The network power or IO switch is a device that can control power or an IO pin
over a network connection using a script-able protocol such as Telnet or
curl. This device can be used with the target control commands.

### U-Boot Set Up

Obtain a working image of the U-Boot boot loader for your target. We suggest
you follow the instructions for you target.

Configure U-Boot to network boot using the TFTP protocol. This is U-Boot script
for a Zedboard:

```none
loadaddr=0x02000000
uenvcmd=echo Booting RTEMS Zed from net; set autoload no; dhcp; set serverip 10.10.5.2; tftpboot zed/rtems.img; bootm; reset;
```

The load address variable `loadaddr` is specific to the Zedboard and can be
found in the various examples scripts on the internet. The script then sets
U-Boot environment variable `autoload` to `no` causing DHCP to only request
a DHCP lease from the DHCP server. The script sets the `serverip` to the host
that will be running the RTEMS Tester then issues a TFTP request. The file name
can be anything because the RTEMS Tester ignores it sending the executable
image under test. Finally the script boots the download executable and if that
fails the catch all `reset` resets the board and starts the boot process
over.

Test the target boots and U-Boot runs and obtains a valid DHCP lease. Manually
connect the console's telnet port.

## BSP Configuration

The BSP's configuration file must contain the standard fields:

- `bsp`
- `arch`
- `jobs` - Must be set to `1`.
- `tester` - Set to `%{_rtscripts}/tftp.cfg`

For example the Zedboard's configuration is:

```ini
[xilinx_zynq_zedboard]
bsp    = xilinx_zynq_zedboard
arch   = arm
jobs   = 1
tester = %{_rtscripts}/tftp.cfg
```

The TFTP configuration supports the following field's:

`bsp_tty_dev`

: The target's tty console. For telnet this is a host and port pair written in
  the standard networking format, for example `serserver:12345`.

`test_restarts`

: The number of restarts before the test is considered `invalid`.

`target_reset_regex`

: The target reset regular expression. This is a [Python regular expression](https://docs.python.org/2/library/re.html#regular-expression-syntax) used
  to filter the console input. If a match is made something has happened during
  the boot process that requires a reset. The `target_reset_command`
  is issued to perform the reset. This field is typically looks for boot loader
  error messages that indicate the boot process as failed.

`target_start_regex`

: The target start regular expression. This also a Python regular expression to
  filter the console input to detect if a target has reset. If a board crashes
  running a test or at any point in time and reset this filter detects this as
  happened and end the test with a suitable result.

`target_on_command`

: The target on command is a host shell command that is called before the first
  test. This command powers on a target. Targets should be left powered off
  when not running tests or the target may request TFTP downloads that are for
  another target interfering with those test results. We recommend you
  implement this command as a target off command, a pause, then a target on
  command.

`target_off_command`

: The target off command is a host shell command that is called after the last
  test powering off the target.

`target_reset_command`

: The target reset command is a host shell command that is called when the
  target needs to be reset. This command can power cycle the target or toggle a
  reset signal connected to the target. If you are power cycling a target make
  sure you have a suitable pause to let the target completely power down.

`target_pretest_command`

: The target pretest command is a host shell comment that is called before the
  test is run

The commands in the listed fields can include parameters that are
substituted. The parameters are:

`@ARCH@`

: The BSP architecture

`@BSP@`

: The BSP's name

`@EXE@`

: The executable name.

`@FEXE@`

: The

. The

: `@ARCH` is the

substituted

Some of these field are normally provided by a user's configuration. To do this
use:

```ini
requires = bsp_tty_dev, target_on_command, target_off_command, target_reset_command
```

The `requires` value requires the user provide these settings in their
configuration file.

The Zedboard's configuration file is:

```ini
[xilinx_zynq_zedboard]
bsp                = xilinx_zynq_zedboard
arch               = arm
jobs               = 1
tester             = %{_rtscripts}/tftp.cfg
test_restarts      = 3
target_reset_regex = ^No ethernet found.*|^BOOTP broadcast 6.*|^.+complete\.+ TIMEOUT.*
target_start_regex = ^U-Boot SPL .*
requires           = target_on_command, target_off_command, target_reset_command, bsp_tty_dev
```

The `target_start_regex` searches for U-Boot's first console message. This
indicate the board can restarted.

The `target_reset_regex` checks if no ethernet interface is found. This can
happen if U-Boot cannot detect the PHY device. It also checks if too many DHCP
requests happen and finally a check is made for any timeouts reported by
U-Boot.

An example of a user configuration for the Zedboard is:

```ini
[xilinx_zynq_zedboard]
bsp_tty_dev            = selserver:12345
target_pretest_command = zynq-mkimg @EXE@
target_exe_filter      = /\.exe/.exe.img/
target_on_command      = power-ctl toggle-on 1 4
target_off_command     = power-ctl off 1
target_reset_command   = power-ctl toggle-on 1 3
```

## TFTP Sequences

Running a large number of tests on real hardware exposes a range of issues and
RTEMS Tester is designed to be tolerant of failures in booting or loading that
can happen, for example a hardware design. These sequence diagrams document
some of the sequences that can occur when errors happen.

The simplest sequence is running a test. The target is powered on, the test is
loaded and executed and a pass or fail is determined:

(fig-tester-tftp-seq-1)=

```{figure} ../../images/user/test-tftp-seq-1.png
:alt: Test Pass and Fail Sequence
:figclass: align-center
:width: 90%

Test Pass and Fail Sequences
```

The target start filter triggers if a start condition is detected. This can
happen if the board crashes or resets with no output. If this happens
repeatedly the test result is invalid:

(fig-tester-tftp-seq-2)=

```{figure} ../../images/user/test-tftp-seq-2.png
:alt: Target Start Filter Trigger
:figclass: align-center
:width: 80%

Target Start Filter Trigger
```

The reset filter triggers if an error condition is found such as the bootloader
not being able to load the test executable. If the filter triggers the
`target_reset_command` is run:

(fig-tester-tftp-seq-3)=

```{figure} ../../images/user/test-tftp-seq-3.png
:alt: Target Reset Filter Trigger
:figclass: align-center
:width: 50%

Target Reset Filter Trigger
```

If the RTEMS Tester does not detect a test has started it can restart the test
by resetting the target. The reset command can toggle an IO pin connected to
reset, request a JTAG pod issue a reset or turn the power off and on:

(fig-tester-tftp-seq-4)=

```{figure} ../../images/user/test-tftp-seq-4.png
:alt: Target Timeout
:figclass: align-center
:width: 60%

Target Timeout
```
