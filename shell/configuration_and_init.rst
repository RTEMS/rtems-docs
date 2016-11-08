.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Configuration and Initialization
################################

Introduction
============

This chapter provides information on how the application configures and
initializes the RTEMS shell.

Configuration
=============

The command set available to the application is user configurable.  It is
configured using a mechanism similar to the ``confdefs.h`` mechanism used to
specify application configuration.

In the simplest case, if the user wishes to configure a command set with all
commands available that are neither filesystem management (e.g. mounting,
formating, etc.) or network related, then the following is all that is
required:

.. code-block:: c

    #define CONFIGURE_SHELL_COMMANDS_INIT
    #define CONFIGURE_SHELL_COMMANDS_ALL
    #include <rtems/shellconfig.h>

In a slightly more complex example, if the user wishes to include all
networking commands as well as support for mounting MS-DOS and NFS filesystems,
then the following is all that is required:

.. code-block:: c

    #define CONFIGURE_SHELL_COMMANDS_INIT
    #define CONFIGURE_SHELL_COMMANDS_ALL
    #define CONFIGURE_SHELL_MOUNT_MSDOS
    #define CONFIGURE_SHELL_MOUNT_NFS
    #include <rtems/shellconfig.h>

Customizing the Command Set
---------------------------

The user can configure specific command sets by either building up the set from
individual commands or starting with a complete set and disabling individual
commands.  Each command has two configuration macros associated with it.

*CONFIGURE_SHELL_COMMAND_XXX*
    Each command has a constant of this form which is defined when
    building a command set by individually enabling specific
    commands.

*CONFIGURE_SHELL_NO_COMMAND_XXX*
    In contrast, each command has a similar command which is
    defined when the application is configuring a command set
    by disabling specific commands in the set.

Adding Custom Commands
----------------------

One of the design goals of the RTEMS Shell was to make it easy for a user to
add custom commands specific to their application.  We believe this design goal
was accomplished.  In order to add a custom command, the user is required to do
the following:

- Provide a *main-style* function which implements the command.  If that
  command function uses a ``getopt`` related function to parse arguments, it
  *MUST* use the reentrant form.

- Provide a command definition structure of type ``rtems_shell_cmd_t``.

- Configure that command using the ``CONFIGURE_SHELL_USER_COMMANDS`` macro.

Custom aliases are configured similarly but the user only provides an alias
definition structure of type ``rtems_shell_alias_t`` and configures the alias
via the ``CONFIGURE_SHELL_USER_ALIASES`` macro.

In the following example, we have implemented a custom command named
``usercmd`` which simply prints the arguments it was passed. We have also
provided an alias for ``usercmd`` named ``userecho``.

.. code-block:: c

    #include <rtems/shell.h>
    int main_usercmd(int argc, char **argv)
    {
        int i;
        printf( "UserCommand: argc=%d\n", argc );
        for (i=0 ; i<argc ; i++ )
            printf( "argv[%d]= %s\n", i, argv[i] );
        return 0;
    }
    rtems_shell_cmd_t Shell_USERCMD_Command = {
        "usercmd",                   /* name */
        "usercmd n1 \[n2 \[n3...]]", /* usage */
        "user",                      /* topic */
        main_usercmd,                /* command */
        NULL,                        /* alias */
        NULL                         /* next */
    };
    rtems_shell_alias_t Shell_USERECHO_Alias = {
        "usercmd",                   /* command */
        "userecho"                   /* alias */
    };
    #define CONFIGURE_SHELL_USER_COMMANDS &Shell_USERCMD_Command
    #define CONFIGURE_SHELL_USER_ALIASES &Shell_USERECHO_Alias
    #define CONFIGURE_SHELL_COMMANDS_INIT
    #define CONFIGURE_SHELL_COMMANDS_ALL
    #define CONFIGURE_SHELL_MOUNT_MSDOS
    #include <rtems/shellconfig.h>

Notice in the above example, that the user wrote the *main* for their command
(e.g. ``main_usercmd``) which looks much like any other ``main()``.  They then
defined a ``rtems_shell_cmd_t`` structure named ``Shell_USERCMD_Command`` which
describes that command.  This command definition structure is registered into
the static command set by defining ``CONFIGURE_SHELL_USER_COMMANDS``
to ``&Shell_USERCMD_Command``.

Similarly, to add the ``userecho`` alias, the user provides the alias
definition structure named ``Shell_USERECHO_Alias`` and defines
``CONFIGURE_SHELL_USER_ALIASES`` to configure the alias.

The user can configure any number of commands and aliases in this manner.

Initialization
==============

The shell may be easily attached to a serial port or to the ``telnetd`` server.
This section describes how that is accomplished.

Attached to a Serial Port
-------------------------

Starting the shell attached to the console or a serial port is very simple. The
user invokes ``rtems_shell_init`` with parameters to indicate the
characteristics of the task that will be executing the shell including name,
stack size, and priority.  The user also specifies the device that the shell is
to be attached to.

This example is taken from the ``fileio`` sample test.  This shell portion of
this test can be run on any target which provides a console with input and
output capabilities.  It does not include any commands which cannot be
supported on all BSPs.  The source code for this test is in
``testsuites/samples/fileio`` with the shell configuration in the ``init.c``
file.

.. code-block:: c

    #include <rtems/shell.h>
    void start_shell(void)
    {
        printf(" =========================\n");
        printf(" starting shell\n");
        printf(" =========================\n");
        rtems_shell_init(
            "SHLL",                       /* task name */
            RTEMS_MINIMUM_STACK_SIZE * 4, /* task stack size */
            100,                          /* task priority */
            "/dev/console",               /* device name */
            false,                        /* run forever */
            true,                         /* wait for shell to terminate */
            rtems_shell_login_check       /* login check function,
            use NULL to disable a login check */
        );
    }

In the above example, the call to ``rtems_shell_init`` spawns a task to run the
RTEMS Shell attached to ``/dev/console`` and executing at priority 100.  The
caller suspends itself and lets the shell take over the console device.  When
the shell is exited by the user, then control returns to the caller.

Attached to a Socket
--------------------

TBD

Access Control
==============

Login Checks
------------

Login checks are optional for the RTEMS shell and can be configured via a login
check handler passed to ``rtems_shell_init()``.  One login check handler
is ``rtems_shell_login_check()``.

Configuration Files
-------------------

The following files are used by the login check handler
``rtems_shell_login_check()`` to validate a passphrase for a user and to set up
the user environment for the shell command execution.

:file:`/etc/passwd`
    The format for each line is

    .. code:: c

        user_name:password:UID:GID:GECOS:directory:shell

    with colon separated fields.  For more information refer to the Linux
    PASSWD(5) man page.  Use a ``password`` of ``*`` to disable the login of the
    user.  An empty password allows login without a password for this user.  In
    contrast to standard UNIX systems, this file is only readable and writeable
    for the user with an UID of zero by default.  The ``directory`` is used to
    perform a filesystem change root operation in ``rtems_shell_login_check()``
    in contrast to a normal usage as the HOME directory of the user.
    The *default* content is:

    .. code:: c

        root::0:0::::

    so there is *no password required* for the ``root`` user.

:file:`/etc/group`
    The format for each line is:

    .. code:: c

        group_name:password:GID:user_list

    with colon separated fields.  The ``user_list`` is comma separated.  For
    more information refer to the Linux GROUP(5) man page.  In contrast to
    standard UNIX systems, this file is only readable and writeable for the
    user with an UID of zero by default.  The default content is

    .. code:: c

        root::0:

Command Visibility and Execution Permission
-------------------------------------------

Each command has:

- an owner,

- a group, and

- a read permission flag for the owner, the group and all other users, and

- an execution permission flag for the owner, the group and all other
  users.

The read and write permission flags are stored in the command mode.  The read
permission flags determine the visibility of the command for the current user.
The execution permission flags determine the ability to execute a command for
the current user.  These command properties can be displayed and changed with
the:

- ``cmdls``,

- ``cmdchown``, and

- ``cmdchmod``

commands.  The access is determined by the effective UID, the effective GID and
the supplementary group IDs of the current user and follows the standard
filesystem access procedure.

Add CRYPT(3) Formats
--------------------

By default the ``crypt_r()`` function used by ``rtems_shell_login_check()``
supports only plain text passphrases.  Use ``crypt_add_format()`` to add more
formats.  The following formats are available out of the box:

- ``crypt_md5_format``,

- ``crypt_sha256_format``, and

- ``crypt_sha512_format``.

An example follows:

.. index:: crypt_add_format

.. code:: c

    #include <crypt.h>
    void add_formats( void )
    {
        crypt_add_format( &crypt_md5_format );
        crypt_add_format( &crypt_sha512_format );
    }

Functions
=========

This section describes the Shell related C functions which are publicly
available related to initialization and configuration.

.. raw:: latex

   \clearpage

rtems_shell_init - Initialize the shell
---------------------------------------
.. index:: initialization
.. index:: rtems_shell_init

CALLING SEQUENCE:
    .. code-block:: c

        rtems_status_code rtems_shell_init(
            const char          *task_name,
            size_t               task_stacksize,
            rtems_task_priority  task_priority,
            const char          *devname,
            bool                 forever,
            bool                 wait,
            rtems_login_check    login_check
        );

DIRECTIVE STATUS CODES:
    ``RTEMS_SUCCESSFUL`` - Shell task spawned successfully
    *others* - to indicate a failure condition

DESCRIPTION:
    This service creates a task with the specified characteristics to run the RTEMS
    Shell attached to the specified ``devname``.

NOTES:
    This method invokes the ``rtems_task_create`` and ``rtems_task_start``
    directives and as such may return any status code that those directives may
    return.

    There is one POSIX key necessary for all shell instances together and one
    POSIX key value pair per instance. You should make sure that your RTEMS
    configuration accounts for these resources.

.. raw:: latex

   \clearpage

rtems_shell_login_check - Default login check handler
-----------------------------------------------------
.. index:: initialization
.. index:: rtems_shell_login_check

CALLING SEQUENCE:
    .. code:: c

        bool rtems_shell_login_check(
          const char *user,
          const char *passphrase
        );

DIRECTIVE STATUS CODES:
    ``true`` - login is allowed, and
    ``false`` - otherwise.

DESCRIPTION:
    This function checks if the specified passphrase is valid for the specified
    user.

NOTES:
    As a side-effect if the specified passphrase is valid for the specified
    user, this function:

    - performs a filesystem change root operation to the directory of the
      specified user if the directory path is non-empty,

    - changes the owner of the current shell device to the UID of the specified
      user,

    - sets the real and effective UID of the current user environment to the
      UID of the specified user,

    - sets the real and effective GID of the current user environment to the
      GID of the specified user, and

    - sets the supplementary group IDs of the current user environment to the
      supplementary group IDs of the specified user.

    In case the filesystem change root operation fails, then the environment
    setup is aborted and ``false`` is returned.
