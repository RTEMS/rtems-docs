.. SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: RTEMS Remote Debugger Server Specifications
.. COMMENT: Written by: Emmanuel Raguet <raguet@crf.canon.fr>

Network Servers
###############

RTEMS FTP Daemon
================

The RTEMS FTPD is a complete file transfer protocol (FTP) daemon which can
store, retrieve, and manipulate files on the local filesystem.  In addition,
the RTEMS FTPD provides "hooks" which are actions performed on received data.
Hooks are useful in situations where a destination file is not necessarily
appropriate or in cases when a formal device driver has not yet been
implemented.

This server was implemented and documented by Jake Janovetz
(janovetz@tempest.ece.uiuc.edu).

Configuration Parameters
------------------------

The configuration structure for FTPD is as follows:

.. code-block:: c

    struct rtems_ftpd_configuration
    {
        rtems_task_priority     priority;           /* FTPD task priority  */
        unsigned long           max_hook_filesize;  /* Maximum buffersize  */
        /*    for hooks        */
        int                     port;               /* Well-known port     */
        struct rtems_ftpd_hook  *hooks;             /* List of hooks       */
    };

The FTPD task priority is specified with ``priority``.  Because hooks are not
saved as files, the received data is placed in an allocated buffer.
``max_hook_filesize`` specifies the maximum size of this buffer.  Finally,
``hooks`` is a pointer to the configured hooks structure.

Initializing FTPD (Starting the daemon)
---------------------------------------

Starting FTPD is done with a call to ``rtems_initialize_ftpd()``.  The
configuration structure must be provided in the application source code.
Example hooks structure and configuration structure follow.

.. code-block:: c

    struct rtems_ftpd_hook ftp_hooks[] =
    {
        {"untar", Untar_FromMemory},
        {NULL, NULL}
    };

    struct rtems_ftpd_configuration rtems_ftpd_configuration =
    {
        40,                     /* FTPD task priority */
        512*1024,               /* Maximum hook 'file' size */
        0,                      /* Use default port */
        ftp_hooks,              /* Local ftp hooks */
        0,                      /* Use / as root */
        1,                      /* Max. connections */
        0,                      /* Infinite idle timeout */
        0,                      /* Read-write access */
        0,                      /* Ignore login check */
        true                    /* Say hello */
    };

Specifying 0 for the well-known port causes FTPD to use the UNIX standard FTPD
port (21).

Using Hooks
-----------

In the example above, one hook was installed.  The hook causes FTPD to call the
function ``Untar_FromMemory`` when the user sends data to the file ``untar``.
The prototype for the ``untar`` hook (and hooks, in general) is:

.. code-block:: c

    int Untar_FromMemory(void *tar_buf, size_t size);

An example FTP transcript which exercises this hook is:

.. code-block:: shell

    220 RTEMS FTP server (Version 1.0-JWJ) ready.
    Name (dcomm0:janovetz): John Galt
    230 User logged in.
    Remote system type is RTEMS.
    ftp> bin
    200 Type set to I.
    ftp> dir
    200 PORT command successful.
    150 ASCII data connection for LIST.
    drwxrwx--x      0     0         268  dev
    drwxrwx--x      0     0           0  TFTP
    226 Transfer complete.
    ftp> put html.tar untar
    local: html.tar remote: untar
    200 PORT command successful.
    150 BINARY data connection.
    210 File transferred successfully.
    471040 bytes sent in 0.48 secs (9.6e+02 Kbytes/sec)
    ftp> dir
    200 PORT command successful.
    150 ASCII data connection for LIST.
    drwxrwx--x      0     0         268  dev
    drwxrwx--x      0     0           0  TFTP
    drwxrwx--x      0     0        3484  public_html
    226 Transfer complete.
    ftp> quit
    221 Goodbye.
