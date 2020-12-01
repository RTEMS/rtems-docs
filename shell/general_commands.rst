.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

General Commands
****************

Introduction
============

The RTEMS shell has the following general commands:

- help_ - Print command help

- alias_ - Add alias for an existing command

- cmdls_ - List commands

- cmdchown_ - Change user or owner of commands

- cmdchmod_ - Change mode of commands

- date_ - Print or set current date and time

- echo_ - Produce message in a shell script

- sleep_ - Delay for a specified amount of time

- id_ - show uid gid euid and egid

- tty_ - show ttyname

- whoami_ - print effective user id

- getenv_ - print environment variable

- setenv_ - set environment variable

- unsetenv_ - unset environment variable

- time_ - time command execution

- logoff_ - logoff from the system

- rtc_ - RTC driver configuration

- i2cdetect_ - detect I2C devices

- i2cget_ - get data from an EEPROM like I2C device

- i2cset_ - write data to an EEPROM like I2C device

- spi_ - read and write simple data to an SPI bus

- exit_ - alias for logoff command

Commands
========

This section details the General Commands available.  A subsection is dedicated
to each of the commands and describes the behavior and configuration of that
command as well as providing an example usage.

.. raw:: latex

   \clearpage

.. _help:

help - Print command help
-------------------------
.. index:: help

SYNOPSYS:
    .. code-block:: shell

        help misc

DESCRIPTION:
    This command prints the command help. Help without arguments prints a list
    of topics and help with a topic prints the help for that topic.

EXIT STATUS:
    This command returns 0.

NOTES:
    The help print will break the output up based on the environment variable
    SHELL_LINES. If this environment variable is not set the default is 16
    lines. If set the number of lines is set to that the value. If the shell
    lines is set 0 there will be no break.

EXAMPLES:
    The following is an example of how to use ``alias``:

    .. code-block:: shell

        SHLL [/] $ help
        help: ('r' repeat last cmd - 'e' edit last cmd)
        TOPIC? The topics are
        mem, misc, files, help, rtems, network, monitor
        SHLL [/] $ help misc
        help: list for the topic 'misc'
        alias        - alias old new
        time         - time command [arguments...]
        joel         - joel [args] SCRIPT
        date         - date [YYYY-MM-DD HH:MM:SS]
        echo         - echo [args]
        sleep        - sleep seconds [nanoseconds]
        id           - show uid, gid, euid, and egid
        tty          - show ttyname
        whoami       - show current user
        logoff       - logoff from the system
        setenv       - setenv [var] [string]
        getenv       - getenv [var]
        unsetenv     - unsetenv [var]
        umask        - umask [new_umask]
        Press any key to continue...
        rtc          - real time clock read and set
        SHLL [/] $ setenv SHELL_ENV 0
        SHLL [/] $ help misc
        help: list for the topic 'misc'
        alias        - alias old new
        time         - time command [arguments...]
        joel         - joel [args] SCRIPT
        date         - date [YYYY-MM-DD HH:MM:SS]
        echo         - echo [args]
        sleep        - sleep seconds [nanoseconds]
        id           - show uid, gid, euid, and egid
        tty          - show ttyname
        whoami       - show current user
        logoff       - logoff from the system
        setenv       - setenv [var] [string]
        getenv       - getenv [var]
        unsetenv     - unsetenv [var]
        umask        - umask [new_umask]
        rtc          - real time clock read and set

CONFIGURATION:
    This command has no configuration.

.. raw:: latex

   \clearpage

.. _alias:

alias - add alias for an existing command
-----------------------------------------
.. index:: alias

SYNOPSYS:
    .. code-block:: shell

        alias oldCommand newCommand

DESCRIPTION:
    This command adds an alternate name for an existing command to the command
    set.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    None.

EXAMPLES:
    The following is an example of how to use ``alias``:

    .. code-block:: shell

        SHLL [/] $ me
        shell:me command not found
        SHLL [/] $ alias whoami me
        SHLL [/] $ me
        rtems
        SHLL [/] $ whoami
        rtems

.. index:: CONFIGURE_SHELL_NO_COMMAND_ALIAS
.. index:: CONFIGURE_SHELL_COMMAND_ALIAS

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_ALIAS`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_ALIAS`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_alias

PROGRAMMING INFORMATION:
    The ``alias`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_alias(
            int    argc,
            char **argv
        );

    The configuration structure for the ``alias`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_ALIAS_Command;

.. raw:: latex

   \clearpage

.. _cmdls:

cmdls - List commands
---------------------
.. index:: cmdls

SYNOPSYS:
    .. code-block:: shell

        cmdls COMMAND...

DESCRIPTION:
    This command lists the visible commands of the command set.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The current user must have read permission to list a command.

EXAMPLES:
    The following is an example of how to use ``cmdls``:

    .. code-block:: shell

        SHLL [/] # cmdls help shutdown
        r-xr-xr-x     0     0 help
        r-x------     0     0 shutdown

.. index:: CONFIGURE_SHELL_NO_COMMAND_CMDLS
.. index:: CONFIGURE_SHELL_COMMAND_CMDLS

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_CMDLS`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_CMDLS`` when all shell commands have been
    configured.

PROGRAMMING INFORMATION:
    The configuration structure for the ``cmdls`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_CMDLS_Command;

.. raw:: latex

   \clearpage

.. _cmdchown:

cmdchown - Change user or owner of commands
-------------------------------------------
.. index:: cmdchown

SYNOPSYS:
    .. code-block:: shell

        cmdchown [OWNER][:[GROUP]] COMMAND...

DESCRIPTION:
    This command changes the user or owner of a command.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The current user must have an UID of zero or be the command owner to change
    the owner or group.

EXAMPLES:
    The following is an example of how to use ``cmdchown``:

    .. code-block:: shell

        [/] # cmdls help
        r-xr-xr-x     0     0 help
        [/] # cmdchown 1:1 help
        [/] # cmdls help
        r--r--r--     1     1 help

.. index:: CONFIGURE_SHELL_NO_COMMAND_CMDCHOWN
.. index:: CONFIGURE_SHELL_COMMAND_CMDCHOWN

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_CMDCHOWN`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_CMDCHOWN`` when all shell commands have been
    configured.

PROGRAMMING INFORMATION:
    The configuration structure for the ``cmdchown`` has the following
    prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_CMDCHOWN_Command;

.. raw:: latex

   \clearpage

.. _cmdchmod:

cmdchmod - Change mode of commands
----------------------------------
.. index:: cmdchmod

SYNOPSYS:
    .. code-block:: shell

        cmdchmod OCTAL-MODE COMMAND...

DESCRIPTION:
    This command changes the mode of a command.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The current user must have an UID of zero or be the command owner to change
    the mode.

EXAMPLES:
    The following is an example of how to use ``cmdchmod``:

    .. code-block:: shell

        [/] # cmdls help
        r-xr-xr-x     0     0 help
        [/] # cmdchmod 544 help
        [/] # cmdls help
        r-xr--r--     0     0 help

.. index:: CONFIGURE_SHELL_NO_COMMAND_CMDCHMOD
.. index:: CONFIGURE_SHELL_COMMAND_CMDCHMOD

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_CMDCHMOD`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_CMDCHMOD`` when all shell commands have been
    configured.

PROGRAMMING INFORMATION:
    The configuration structure for the ``cmdchmod`` has the following
    prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_CMDCHMOD_Command;

.. raw:: latex

   \clearpage

.. _date:

date - print or set current date and time
-----------------------------------------
.. index:: date

SYNOPSYS:
    .. code-block:: shell

        date
        date DATE TIME

DESCRIPTION:
    This command operates one of two modes.  When invoked with no arguments, it
    prints the current date and time.  When invoked with both ``date`` and
    ``time`` arguments, it sets the current time.

    The ``date`` is specified in ``YYYY-MM-DD`` format.
    The ``time`` is specified in ``HH:MM:SS`` format.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    None.

EXAMPLES:
    The following is an example of how to use ``date``:

    .. code-block:: shell

        SHLL [/] $ date
        Fri Jan  1 00:00:09 1988
        SHLL [/] $ date 2008-02-29 06:45:32
        SHLL [/] $ date
        Fri Feb 29 06:45:35 2008

.. index:: CONFIGURE_SHELL_NO_COMMAND_DATE
.. index:: CONFIGURE_SHELL_COMMAND_DATE

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_DATE`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_DATE`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_date

PROGRAMMING INFORMATION:
    The ``date`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_date(
            int    argc,
            char **argv
        );

    The configuration structure for the ``date`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_DATE_Command;

.. raw:: latex

   \clearpage

.. _echo:

echo - produce message in a shell script
----------------------------------------
.. index:: echo

SYNOPSYS:
    .. code-block:: shell

        echo [-n | -e] args ...

DESCRIPTION:
    Echo prints its arguments on the standard output, separated by spaces.
    Unless the *-n* option is present, a newline is output following the
    arguments.  The *-e* option causes echo to treat the escape sequences
    specially, as described in the following paragraph.  The *-e* option is the
    default, and is provided solely for compatibility with other systems.  Only
    one of the options *-n* and *-e* may be given.

    If any of the following sequences of characters is encountered during
    output, the sequence is not output.  Instead, the specified action is
    performed:

    *\b*
        A backspace character is output.

    *\c*
        Subsequent output is suppressed.  This is normally used at the end of
        the last argument to suppress the trailing newline that echo would
        otherwise output.

    *\f*
        Output a form feed.

    *\n*
        Output a newline character.

    *\r*
        Output a carriage return.

    *\t*
        Output a (horizontal) tab character.

    *\v*
        Output a vertical tab.

    *\0digits*
        Output the character whose value is given by zero to three digits.  If
        there are zero digits, a nul character is output.

    *\\*
        Output a backslash.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    The octal character escape mechanism (\0digits) differs from the C language
    mechanism.

    There is no way to force ``echo`` to treat its arguments literally, rather
    than interpreting them as options and escape sequences.

EXAMPLES:
    The following is an example of how to use ``echo``:

    .. code-block:: shell

        SHLL [/] $ echo a b c
        a b c
        SHLL [/] $ echo

.. index:: CONFIGURE_SHELL_NO_COMMAND_ECHO
.. index:: CONFIGURE_SHELL_COMMAND_ECHO

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_ECHO`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_ECHO`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_echo

PROGRAMMING INFORMATION:
    The ``echo`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_echo(
            int    argc,
            char **argv
        );

    The configuration structure for the ``echo`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_ECHO_Command;

ORIGIN:
    The implementation and portions of the documentation for this command are
    from NetBSD 4.0.

.. raw:: latex

   \clearpage

.. _sleep:

sleep - delay for a specified amount of time
--------------------------------------------
.. index:: sleep

SYNOPSYS:
    .. code-block:: shell

        sleep seconds
        sleep seconds nanoseconds

DESCRIPTION:
    This command causes the task executing the shell to block for the specified
    number of ``seconds`` and ``nanoseconds``.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    This command is implemented using the ``nanosleep()`` method.

    The command line interface is similar to the ``sleep`` command found on
    POSIX systems but the addition of the ``nanoseconds`` parameter allows fine
    grained delays in shell scripts without adding another command such as
    ``usleep``.

EXAMPLES:
    The following is an example of how to use ``sleep``:

    .. code-block:: shell

        SHLL [/] $ sleep 10
        SHLL [/] $ sleep 0 5000000

    It is not clear from the above but there is a ten second pause after
    executing the first command before the prompt is printed.  The second
    command completes very quickly from a human perspective and there is no
    noticeable delay in the prompt being printed.

.. index:: CONFIGURE_SHELL_NO_COMMAND_SLEEP
.. index:: CONFIGURE_SHELL_COMMAND_SLEEP

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_SLEEP`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_SLEEP`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_sleep

PROGRAMMING INFORMATION:
    The ``sleep`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_sleep(
            int    argc,
            char **argv
        );

    The configuration structure for the ``sleep`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_SLEEP_Command;

.. raw:: latex

   \clearpage

.. _id:

id - show uid gid euid and egid
-------------------------------
.. index:: id

SYNOPSYS:
    .. code-block:: shell

        id

DESCRIPTION:
    This command prints the user identity.  This includes the user id (uid),
    group id (gid), effective user id (euid), and effective group id (egid).

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    Remember there is only one POSIX process in a single processor RTEMS
    application. Each thread may have its own user identity and that identity
    is used by the filesystem to enforce permissions.

EXAMPLES:
    The first example of the ``id`` command is from a session logged
    in as the normal user ``rtems``:

    .. code-block:: shell

        SHLL [/] # id
        uid=1(rtems),gid=1(rtems),euid=1(rtems),egid=1(rtems)

    The second example of the ``id`` command is from a session logged in as the
    ``root`` user:

    .. code-block:: shell

        SHLL [/] # id
        uid=0(root),gid=0(root),euid=0(root),egid=0(root)

.. index:: CONFIGURE_SHELL_NO_COMMAND_ID
.. index:: CONFIGURE_SHELL_COMMAND_ID

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_ID`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_ID`` when all shell commands have been configured.

.. index:: rtems_shell_rtems_main_id

PROGRAMMING INFORMATION:
    The ``id`` is implemented by a C language function which has the following
    prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_id(
            int    argc,
            char **argv
        );

    The configuration structure for the ``id`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_ID_Command;

.. raw:: latex

   \clearpage

.. _tty:

tty - show ttyname
------------------
.. index:: tty

SYNOPSYS:
    .. code-block:: shell

        tty

DESCRIPTION:
    This command prints the file name of the device connected to standard
    input.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    NONE

EXAMPLES:
    The following is an example of how to use ``tty``:

    .. code-block:: shell

        SHLL [/] $ tty
        /dev/console

.. index:: CONFIGURE_SHELL_NO_COMMAND_TTY
.. index:: CONFIGURE_SHELL_COMMAND_TTY

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_TTY`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_TTY`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_tty

PROGRAMMING INFORMATION:
    The ``tty`` is implemented by a C language function which has the following
    prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_tty(
            int    argc,
            char **argv
        );

    The configuration structure for the ``tty`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_TTY_Command;

.. raw:: latex

   \clearpage

.. _whoami:

whoami - print effective user id
--------------------------------
.. index:: whoami

SYNOPSYS:
    .. code-block:: shell

        whoami

DESCRIPTION:
    This command displays the user name associated with the current effective
    user
    id.

EXIT STATUS:
    This command always succeeds.

NOTES:
    None.

EXAMPLES:
    The following is an example of how to use ``whoami``:

    .. code-block:: shell

        SHLL [/] $ whoami
        rtems

.. index:: CONFIGURE_SHELL_NO_COMMAND_WHOAMI
.. index:: CONFIGURE_SHELL_COMMAND_WHOAMI

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_WHOAMI`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_WHOAMI`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_whoami

PROGRAMMING INFORMATION:
    The ``whoami`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_whoami(
            int    argc,
            char **argv
        );

    The configuration structure for the ``whoami`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_WHOAMI_Command;

.. raw:: latex

   \clearpage

.. _getenv:

getenv - print environment variable
-----------------------------------
.. index:: getenv

SYNOPSYS:
    .. code-block:: shell

        getenv variable

DESCRIPTION:
    This command is used to display the value of a ``variable`` in the set of
    environment variables.

EXIT STATUS:
    This command will return 1 and print a diagnostic message if a failure
    occurs.

NOTES:
    The entire RTEMS application shares a single set of environment variables.

EXAMPLES:
    The following is an example of how to use ``getenv``:

    .. code-block:: shell

        SHLL [/] $ getenv BASEPATH
        /mnt/hda1

.. index:: CONFIGURE_SHELL_NO_COMMAND_GETENV
.. index:: CONFIGURE_SHELL_COMMAND_GETENV

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_GETENV`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_GETENV`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_getenv

PROGRAMMING INFORMATION:
    The ``getenv`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_getenv(
            int    argc,
            char **argv
        );

    The configuration structure for the ``getenv`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_GETENV_Command;

.. raw:: latex

   \clearpage

.. _setenv:

setenv - set environment variable
---------------------------------
.. index:: setenv

SYNOPSYS:
    .. code-block:: shell

        setenv variable [value]

DESCRIPTION:
    This command is used to add a new ``variable`` to the set of environment
    variables or to modify the variable of an already existing ``variable``.
    If the ``value`` is not provided, the ``variable`` will be set to the empty
    string.

EXIT STATUS:
    This command will return 1 and print a diagnostic message if a failure
    occurs.

NOTES:
    The entire RTEMS application shares a single set of environment variables.

EXAMPLES:
    The following is an example of how to use ``setenv``:

    .. code-block:: shell

        SHLL [/] $ setenv BASEPATH /mnt/hda1

.. index:: CONFIGURE_SHELL_NO_COMMAND_SETENV
.. index:: CONFIGURE_SHELL_COMMAND_SETENV

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_SETENV`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_SETENV`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_setenv

PROGRAMMING INFORMATION:
    The ``setenv`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_setenv(
            int    argc,
            char **argv
        );

    The configuration structure for the ``setenv`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_SETENV_Command;

.. raw:: latex

   \clearpage

.. _unsetenv:

unsetenv - unset environment variable
-------------------------------------
.. index:: unsetenv

SYNOPSYS:
    .. code-block:: shell

        unsetenv variable

DESCRIPTION:
    This command is remove to a ``variable`` from the set of environment
    variables.

EXIT STATUS:
    This command will return 1 and print a diagnostic message if a failure
    occurs.

NOTES:
    The entire RTEMS application shares a single set of environment variables.

EXAMPLES:
    The following is an example of how to use ``unsetenv``:

    .. code-block:: shell

        SHLL [/] $ unsetenv BASEPATH

.. index:: CONFIGURE_SHELL_NO_COMMAND_UNSETENV
.. index:: CONFIGURE_SHELL_COMMAND_UNSETENV

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_UNSETENV`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_UNSETENV`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_unsetenv

PROGRAMMING INFORMATION:
    The ``unsetenv`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_unsetenv(
            int    argc,
            char **argv
        );

    The configuration structure for the ``unsetenv`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_UNSETENV_Command;

.. raw:: latex

   \clearpage

.. _time:

time - time command execution
-----------------------------
.. index:: time

SYNOPSYS:
    .. code-block:: shell

        time command [argument ...]

DESCRIPTION:
    The time command executes and times a command.  After the command finishes,
    time writes the total time elapsed.  Times are reported in seconds.

EXIT STATUS:
    This command returns 0 on success and non-zero if an error is encountered.

NOTES:
    None.

EXAMPLES:
    The following is an example of how to use ``time``:

    .. code-block:: shell

        SHLL [/] $ time cp -r /nfs/directory /c

.. index:: CONFIGURE_SHELL_NO_COMMAND_TIME
.. index:: CONFIGURE_SHELL_COMMAND_TIME

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_TIME`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_TIME`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_time

PROGRAMMING INFORMATION:
    The ``time`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_time(
            int    argc,
            char **argv
        );

    The configuration structure for the ``time`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_TIME_Command;

.. raw:: latex

   \clearpage

.. _logoff:

logoff - logoff from the system
-------------------------------
.. index:: logoff

SYNOPSYS:
    .. code-block:: shell

        logoff

DESCRIPTION:
    This command logs the user out of the shell.

EXIT STATUS:
    This command does not return.

NOTES:
    The system behavior when the shell is exited depends upon how the shell was
    initiated.  The typical behavior is that a login prompt will be displayed
    for the next login attempt or that the connection will be dropped by the
    RTEMS system.

EXAMPLES:
    The following is an example of how to use ``logoff``:

    .. code-block:: shell

        SHLL [/] $ logoff
        logoff from the system...

.. index:: CONFIGURE_SHELL_NO_COMMAND_LOGOFF
.. index:: CONFIGURE_SHELL_COMMAND_LOGOFF

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_LOGOFF`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_LOGOFF`` when all shell commands have been
    configured.

.. index:: rtems_shell_rtems_main_logoff

PROGRAMMING INFORMATION:
    The ``logoff`` is implemented by a C language function which has the
    following prototype:

    .. code-block:: c

        int rtems_shell_rtems_main_logoff(
            int    argc,
            char **argv
        );

    The configuration structure for the ``logoff`` has the following prototype:

    .. code-block:: c

        extern rtems_shell_cmd_t rtems_shell_LOGOFF_Command;

.. raw:: latex

   \clearpage

.. _rtc:

rtc - RTC driver configuration
------------------------------
.. index:: rtc

SYNOPSYS:
    .. code-block:: shell

        rtc

.. index:: CONFIGURE_SHELL_NO_COMMAND_RTC
.. index:: CONFIGURE_SHELL_COMMAND_RTC

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_RTC`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_RTC`` when all shell commands have been
    configured.

.. raw:: latex

   \clearpage

.. _i2cdetect:

i2cdetect - detect I2C devices
------------------------------
.. index:: i2cdetect

SYNOPSYS:
    .. code-block:: shell

        i2cdetect <I2C_BUS>

.. index:: CONFIGURE_SHELL_NO_COMMAND_I2CDETECT
.. index:: CONFIGURE_SHELL_COMMAND_I2CDETECT

DESCRIPTION:
    Tries to detect I2C devices connected to the I2C bus. To do that, write
    requests with the length of 0 are used.

    WARNING: This might confuse some I2C devices, so please use it only if you
    know what you are doing.

    The command supports a ``-h`` option to get usage details.

    The command works only with I2C bus drivers that use the Linux-Style API.

EXAMPLES:
    The following is an example where two I2C devices are detected. One on 0x1a
    and one on 0x1f:

    .. code-block:: shell

        SHLL [/] # i2cdetect /dev/i2c1
            x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 xA xB xC xD xE xF
        0x     -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        1x  -- -- -- -- -- -- -- -- -- -- 1a -- -- -- -- 1f
        2x  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        3x  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        4x  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        5x  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        6x  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        7x  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        SHLL [/] #

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_I2CDETECT`` to have
    this command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_I2CDETECT`` when all shell commands have been
    configured.

.. raw:: latex

   \clearpage

.. _i2cget:

i2cget - get data from an EEPROM like I2C device
------------------------------------------------
.. index:: i2cget

SYNOPSYS:
    .. code-block:: shell

        i2cget <I2C_BUS> <CHIP-ADDRESS> <DATA-ADDRESS> [<NR-BYTES>]

.. index:: CONFIGURE_SHELL_NO_COMMAND_I2CGET
.. index:: CONFIGURE_SHELL_COMMAND_I2CGET

DESCRIPTION:
    Get one or multiple bytes from an EEPROM like I2C device. If <NR-BYTES> is
    not given the command defaults to reading one byte. If you read multiple
    bytes (<NR-BYTES> given and bigger then 1) the read will be done in one
    single request. An auto incrementing register pointer is assumed.

    The command supports a ``-h`` option to get usage details.

    All numbers can be entered in decimal form (normal digits; e.g. 16),
    hexadecimal form (with 0x prefix; e.g. 0x10) or octal form (with a leading
    zero; e.g. 020).

    The command works only with I2C bus drivers that use the Linux-Style API.

EXAMPLES:
    The following is an example how to read a one byte register at 0xd from the
    I2C device at 0x1f:

    .. code-block:: shell

        SHLL [/] # i2cget /dev/i2c1 0x1f 0x0d
        0xc7 
        SHLL [/] #

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_I2CGET`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_I2CGET`` when all shell commands have been
    configured.

.. raw:: latex

   \clearpage

.. _i2cset:

i2cset - write data to an EEPROM like I2C device
------------------------------------------------
.. index:: i2cset

SYNOPSYS:
    .. code-block:: shell

        i2cset <I2C_BUS> <CHIP-ADDRESS> <DATA-ADDRESS> <VALUE> [<VALUE> [...]]

.. index:: CONFIGURE_SHELL_NO_COMMAND_I2CSET
.. index:: CONFIGURE_SHELL_COMMAND_I2CSET

DESCRIPTION:
    Write one or multiple bytes to an EEPROM like I2C device. If you write
    multiple bytes (multiple <VALUE> given) the write will be done in one single
    request. An auto incrementing register pointer is assumed.

    The command supports a ``-h`` option to get usage details.

    All numbers can be entered in decimal form (normal digits; e.g. 16),
    hexadecimal form (with 0x prefix; e.g. 0x10) or octal form (with a leading
    zero; e.g. 020).

    The command works only with I2C bus drivers that use the Linux-Style API.

EXAMPLES:
    The following is an example how to write one byte of 0x00 to the register at
    0x11 of the I2C device at 0x1f:

    .. code-block:: shell

        SHLL [/] # i2cset /dev/i2c1 0x1f 0x11 0x00
        SHLL [/] #

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_I2CSET`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_I2CSET`` when all shell commands have been
    configured.

.. raw:: latex

   \clearpage

.. _spi:

spi - read and write simple data to an SPI bus
----------------------------------------------
.. index:: spi

SYNOPSYS:
    .. code-block:: shell

        spi [-loh] [-c <cs>] [-s <speed>] [-m <mode>] <SPI_BUS> xx [xx [..]]

.. index:: CONFIGURE_SHELL_NO_COMMAND_SPI
.. index:: CONFIGURE_SHELL_COMMAND_SPI

DESCRIPTION:
    Write data to an SPI bus and read the responses.

    The command supports a ``-h`` option to get usage details.

    The data bytes (``xx`` in the SYNOPSIS) are in hexadecimal form (e.g.
    ``0x10`` or ``10`` both have a value of decimal 16). This allows longer
    hex strings before the shell input limit is reached. All other numbers can
    be entered in decimal form (normal digits; e.g. 16), hexadecimal form (with
    0x prefix; e.g. 0x10) or octal form (with a leading zero; e.g. 020).

    The command works only with SPI bus drivers that use the Linux-Style API.

EXAMPLES:
    The following is an example how to write multiple bytes (0x4a 0x4b 0x4c) to
    the bus. The response is 0xa1 0xa2 0xa3 in this case. Chip select 1 will be
    used.

    .. code-block:: shell

        SHLL [/] # spi /dev/spi1 -c 1 4a 4b 4c
        received: a1 a2 a3
        SHLL [/] #

CONFIGURATION:
    This command is included in the default shell command set.  When building a
    custom command set, define ``CONFIGURE_SHELL_COMMAND_SPI`` to have this
    command included.

    This command can be excluded from the shell command set by defining
    ``CONFIGURE_SHELL_NO_COMMAND_SPI`` when all shell commands have been
    configured.

.. raw:: latex

   \clearpage

.. _exit:

exit - exit the shell
---------------------
.. index:: exit

SYNOPSYS:
    .. code-block:: shell

        exit

DESCRIPTION:
    This command causes the shell interpreter to ``exit``.

EXIT STATUS:
    This command does not return.

NOTES:
    In contrast to `logoff - logoff from the system`, this command is built
    into the shell interpreter loop.

EXAMPLES:
    The following is an example of how to use ``exit``:

    .. code-block:: shell

        SHLL [/] $ exit
        Shell exiting

CONFIGURATION:
    This command is always present and cannot be disabled.

PROGRAMMING INFORMATION:
    The ``exit`` is implemented directly in the shell interpreter.  There is no
    C routine associated with it.
