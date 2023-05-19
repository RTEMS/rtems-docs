.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. Generated from spec:/acfg/if/group-filesystem

Filesystem Configuration
========================

This section describes configuration options related to filesytems.
By default, the In-Memory Filesystem (IMFS) is used as the base filesystem (also
known as root filesystem).  In order to save some memory for your application,
you can disable the filesystem support with the
:ref:`CONFIGURE_APPLICATION_DISABLE_FILESYSTEM` configuration option.
Alternatively, you can strip down the features of the base filesystem with the
:ref:`CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM` and
:ref:`CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM` configuration options.  These
three configuration options are mutually exclusive.  They are intended for an
advanced application configuration.

Features of the IMFS can be disabled and enabled with the following
configuration options:

* :ref:`CONFIGURE_IMFS_DISABLE_CHMOD`

* :ref:`CONFIGURE_IMFS_DISABLE_CHOWN`

* :ref:`CONFIGURE_IMFS_DISABLE_LINK`

* :ref:`CONFIGURE_IMFS_DISABLE_MKNOD`

* :ref:`CONFIGURE_IMFS_DISABLE_MKNOD_FILE`

* :ref:`CONFIGURE_IMFS_DISABLE_MOUNT`

* :ref:`CONFIGURE_IMFS_DISABLE_READDIR`

* :ref:`CONFIGURE_IMFS_DISABLE_READLINK`

* :ref:`CONFIGURE_IMFS_DISABLE_RENAME`

* :ref:`CONFIGURE_IMFS_DISABLE_RMNOD`

* :ref:`CONFIGURE_IMFS_DISABLE_SYMLINK`

* :ref:`CONFIGURE_IMFS_DISABLE_UNMOUNT`

* :ref:`CONFIGURE_IMFS_DISABLE_UTIME`

* :ref:`CONFIGURE_IMFS_ENABLE_MKFIFO`

.. Generated from spec:/acfg/if/appl-disable-filesystem

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_APPLICATION_DISABLE_FILESYSTEM

.. _CONFIGURE_APPLICATION_DISABLE_FILESYSTEM:

CONFIGURE_APPLICATION_DISABLE_FILESYSTEM
----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_APPLICATION_DISABLE_FILESYSTEM``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then a base filesystem and the
configured filesystems are initialized during system initialization.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then **no base filesystem** is
initialized during system initialization and **no filesystems** are
configured.

.. rubric:: NOTES:

Filesystems shall be initialized to support file descriptor based device
drivers and basic input/output functions such as :c:func:`printf`.
Filesystems can be disabled to reduce the memory footprint of an application.

.. Generated from spec:/acfg/if/filesystem-all

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_ALL

.. _CONFIGURE_FILESYSTEM_ALL:

CONFIGURE_FILESYSTEM_ALL
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_ALL``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the following
configuration options will be defined as well

* :ref:`CONFIGURE_FILESYSTEM_DOSFS`,

* :ref:`CONFIGURE_FILESYSTEM_FTPFS`,

* :ref:`CONFIGURE_FILESYSTEM_IMFS`,

* :ref:`CONFIGURE_FILESYSTEM_JFFS2`,

* :ref:`CONFIGURE_FILESYSTEM_NFS`,

* :ref:`CONFIGURE_FILESYSTEM_RFS`, and

* :ref:`CONFIGURE_FILESYSTEM_TFTPFS`.

.. Generated from spec:/acfg/if/filesystem-dosfs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_DOSFS

.. _CONFIGURE_FILESYSTEM_DOSFS:

CONFIGURE_FILESYSTEM_DOSFS
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_DOSFS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the DOS (FAT) filesystem
is registered, so that instances of this filesystem can be mounted by the
application.

.. rubric:: NOTES:

This filesystem requires a Block Device Cache configuration, see
:ref:`CONFIGURE_APPLICATION_NEEDS_LIBBLOCK`.

.. Generated from spec:/acfg/if/filesystem-ftpfs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_FTPFS

.. _CONFIGURE_FILESYSTEM_FTPFS:

CONFIGURE_FILESYSTEM_FTPFS
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_FTPFS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the FTP filesystem (FTP
client) is registered, so that instances of this filesystem
can be mounted by the application.

.. Generated from spec:/acfg/if/filesystem-imfs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_IMFS

.. _CONFIGURE_FILESYSTEM_IMFS:

CONFIGURE_FILESYSTEM_IMFS
-------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_IMFS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the In-Memory Filesystem
(IMFS) is registered, so that instances of this filesystem can be mounted by
the application.

.. rubric:: NOTES:

Applications will rarely need this configuration option.  This configuration
option is intended for test programs.  You do not need to define this
configuration option for the base filesystem (also known as root filesystem).

.. Generated from spec:/acfg/if/filesystem-jffs2

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_JFFS2

.. _CONFIGURE_FILESYSTEM_JFFS2:

CONFIGURE_FILESYSTEM_JFFS2
--------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_JFFS2``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the JFFS2 filesystem
is registered, so that instances of this filesystem can be mounted by the
application.

.. Generated from spec:/acfg/if/filesystem-nfs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_NFS

.. _CONFIGURE_FILESYSTEM_NFS:

CONFIGURE_FILESYSTEM_NFS
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_NFS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the Network Filesystem
(NFS) client is registered, so that instances of this filesystem can be
mounted by the application.

.. Generated from spec:/acfg/if/filesystem-rfs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_RFS

.. _CONFIGURE_FILESYSTEM_RFS:

CONFIGURE_FILESYSTEM_RFS
------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_RFS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the RTEMS Filesystem (RFS)
is registered, so that instances of this filesystem can be mounted by the
application.

.. rubric:: NOTES:

This filesystem requires a Block Device Cache configuration, see
:ref:`CONFIGURE_APPLICATION_NEEDS_LIBBLOCK`.

.. Generated from spec:/acfg/if/filesystem-tftpfs

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_FILESYSTEM_TFTPFS

.. _CONFIGURE_FILESYSTEM_TFTPFS:

CONFIGURE_FILESYSTEM_TFTPFS
---------------------------

.. rubric:: CONSTANT:

``CONFIGURE_FILESYSTEM_TFTPFS``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the TFTP filesystem (TFTP
client) is registered, so that instances of this filesystem can be mounted by
the application.

.. Generated from spec:/acfg/if/imfs-disable-chmod

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_CHMOD

.. _CONFIGURE_IMFS_DISABLE_CHMOD:

CONFIGURE_IMFS_DISABLE_CHMOD
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_CHMOD``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
changing the mode of files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support changing the mode of files (no support for :c:func:`chmod`).

.. Generated from spec:/acfg/if/imfs-disable-chown

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_CHOWN

.. _CONFIGURE_IMFS_DISABLE_CHOWN:

CONFIGURE_IMFS_DISABLE_CHOWN
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_CHOWN``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
changing the ownership of files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support changing the ownership of files (no support for :c:func:`chown`).

.. Generated from spec:/acfg/if/imfs-disable-link

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_LINK

.. _CONFIGURE_IMFS_DISABLE_LINK:

CONFIGURE_IMFS_DISABLE_LINK
---------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_LINK``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports hard
links.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support hard links (no support for :c:func:`link`).

.. Generated from spec:/acfg/if/imfs-disable-mknod

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD

.. _CONFIGURE_IMFS_DISABLE_MKNOD:

CONFIGURE_IMFS_DISABLE_MKNOD
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_MKNOD``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports making
files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support making files (no support for :c:func:`mknod`).

.. Generated from spec:/acfg/if/imfs-disable-mknod-device

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE

.. _CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE:

CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE
-----------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports making
device files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support making device files.

.. Generated from spec:/acfg/if/imfs-disable-mknod-file

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD_FILE

.. _CONFIGURE_IMFS_DISABLE_MKNOD_FILE:

CONFIGURE_IMFS_DISABLE_MKNOD_FILE
---------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_MKNOD_FILE``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports making
regular files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support making regular files.

.. Generated from spec:/acfg/if/imfs-disable-mount

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_MOUNT

.. _CONFIGURE_IMFS_DISABLE_MOUNT:

CONFIGURE_IMFS_DISABLE_MOUNT
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_MOUNT``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
mounting other filesystems.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support mounting other filesystems (no support for
:c:func:`mount`).

.. Generated from spec:/acfg/if/imfs-disable-readdir

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_READDIR

.. _CONFIGURE_IMFS_DISABLE_READDIR:

CONFIGURE_IMFS_DISABLE_READDIR
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_READDIR``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
reading directories.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support reading directories (no support for :c:func:`readdir`).  It is
still possible to open files in a directory.

.. Generated from spec:/acfg/if/imfs-disable-readlink

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_READLINK

.. _CONFIGURE_IMFS_DISABLE_READLINK:

CONFIGURE_IMFS_DISABLE_READLINK
-------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_READLINK``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
reading symbolic links.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support reading symbolic links (no support for :c:func:`readlink`).

.. Generated from spec:/acfg/if/imfs-disable-rename

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_RENAME

.. _CONFIGURE_IMFS_DISABLE_RENAME:

CONFIGURE_IMFS_DISABLE_RENAME
-----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_RENAME``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
renaming files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support renaming files (no support for :c:func:`rename`).

.. Generated from spec:/acfg/if/imfs-disable-rmnod

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_RMNOD

.. _CONFIGURE_IMFS_DISABLE_RMNOD:

CONFIGURE_IMFS_DISABLE_RMNOD
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_RMNOD``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
removing files.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support removing files (no support for :c:func:`rmnod`).

.. Generated from spec:/acfg/if/imfs-disable-symlink

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_SYMLINK

.. _CONFIGURE_IMFS_DISABLE_SYMLINK:

CONFIGURE_IMFS_DISABLE_SYMLINK
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_SYMLINK``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
creating symbolic links.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support creating symbolic links (no support for :c:func:`symlink`).

.. Generated from spec:/acfg/if/imfs-disable-unmount

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_UNMOUNT

.. _CONFIGURE_IMFS_DISABLE_UNMOUNT:

CONFIGURE_IMFS_DISABLE_UNMOUNT
------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_UNMOUNT``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
unmounting other filesystems.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support unmounting other filesystems (no support for
:c:func:`unmount`).

.. Generated from spec:/acfg/if/imfs-disable-utime

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_DISABLE_UTIME

.. _CONFIGURE_IMFS_DISABLE_UTIME:

CONFIGURE_IMFS_DISABLE_UTIME
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_DISABLE_UTIME``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS supports
changing file times.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS does not
support changing file times (no support for :c:func:`utime`).

.. Generated from spec:/acfg/if/imfs-enable-mkfifo

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_ENABLE_MKFIFO

.. _CONFIGURE_IMFS_ENABLE_MKFIFO:

CONFIGURE_IMFS_ENABLE_MKFIFO
----------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_ENABLE_MKFIFO``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the root IMFS does not
support making FIFOs (no support for :c:func:`mkfifo`).

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then the root IMFS supports
making FIFOs.

.. Generated from spec:/acfg/if/imfs-memfile-bytes-per-block

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK

.. _CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK:

CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK
--------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK``

.. rubric:: OPTION TYPE:

This configuration option is an integer define.

.. rubric:: DEFAULT VALUE:

The default value is 128.

.. rubric:: DESCRIPTION:

The value of this configuration option defines the block size for in-memory
files managed by the IMFS.

.. rubric:: NOTES:

The configured block size has two impacts. The first is the average amount of
unused memory in the last block of each file.  For example, when the block
size is 512, on average one-half of the last block of each file will remain
unused and the memory is wasted. In contrast, when the block size is 16, the
average unused memory per file is only 8 bytes. However, it requires more
allocations for the same size file and thus more overhead per block for the
dynamic memory management.

Second, the block size has an impact on the maximum size file that can be
stored in the IMFS. With smaller block size, the maximum file size is
correspondingly smaller. The following shows the maximum file size possible
based on the configured block size:

* when the block size is 16 bytes, the maximum file size is 1,328 bytes.

* when the block size is 32 bytes, the maximum file size is 18,656 bytes.

* when the block size is 64 bytes, the maximum file size is 279,488 bytes.

* when the block size is 128 bytes, the maximum file size is 4,329,344 bytes.

* when the block size is 256 bytes, the maximum file size is 68,173,568 bytes.

* when the block size is 512 bytes, the maximum file size is 1,082,195,456
  bytes.

.. rubric:: CONSTRAINTS:

The value of the configuration option shall be equal to 16, 32, 64, 128, 256,
or 512.

.. Generated from spec:/acfg/if/use-devfs-as-base-filesystem

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM

.. _CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM:

CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM
--------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then an IMFS with a reduced
feature set will be the base filesystem (also known as root filesystem).

.. rubric:: NOTES:

In case this configuration option is defined, then the following
configuration options will be defined as well

* :ref:`CONFIGURE_IMFS_DISABLE_CHMOD`,

* :ref:`CONFIGURE_IMFS_DISABLE_CHOWN`,

* :ref:`CONFIGURE_IMFS_DISABLE_LINK`,

* :ref:`CONFIGURE_IMFS_DISABLE_MKNOD_FILE`,

* :ref:`CONFIGURE_IMFS_DISABLE_MOUNT`,

* :ref:`CONFIGURE_IMFS_DISABLE_READDIR`,

* :ref:`CONFIGURE_IMFS_DISABLE_READLINK`,

* :ref:`CONFIGURE_IMFS_DISABLE_RENAME`,

* :ref:`CONFIGURE_IMFS_DISABLE_RMNOD`,

* :ref:`CONFIGURE_IMFS_DISABLE_SYMLINK`,

* :ref:`CONFIGURE_IMFS_DISABLE_UTIME`, and

* :ref:`CONFIGURE_IMFS_DISABLE_UNMOUNT`.

In addition, a simplified path evaluation is enabled.  It allows only a look
up of absolute paths.

This configuration of the IMFS is basically a device-only filesystem.  It is
comparable in functionality to the pseudo-filesystem name space provided
before RTEMS release 4.5.0.

.. Generated from spec:/acfg/if/use-miniimfs-as-base-filesystem

.. raw:: latex

    \clearpage

.. index:: CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM

.. _CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM:

CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM
-----------------------------------------

.. rubric:: CONSTANT:

``CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM``

.. rubric:: OPTION TYPE:

This configuration option is a boolean feature define.

.. rubric:: DEFAULT CONFIGURATION:

If this configuration option is undefined, then the described feature is not
enabled.

.. rubric:: DESCRIPTION:

In case this configuration option is defined, then an IMFS with a reduced
feature set will be the base filesystem (also known as root filesystem).

.. rubric:: NOTES:

In case this configuration option is defined, then the following
configuration options will be defined as well

* :ref:`CONFIGURE_IMFS_DISABLE_CHMOD`,

* :ref:`CONFIGURE_IMFS_DISABLE_CHOWN`,

* :ref:`CONFIGURE_IMFS_DISABLE_LINK`,

* :ref:`CONFIGURE_IMFS_DISABLE_READLINK`,

* :ref:`CONFIGURE_IMFS_DISABLE_RENAME`,

* :ref:`CONFIGURE_IMFS_DISABLE_SYMLINK`,

* :ref:`CONFIGURE_IMFS_DISABLE_UTIME`, and

* :ref:`CONFIGURE_IMFS_DISABLE_UNMOUNT`.
