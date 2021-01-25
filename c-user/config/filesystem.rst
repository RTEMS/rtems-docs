.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
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

.. index:: CONFIGURE_APPLICATION_DISABLE_FILESYSTEM

.. _CONFIGURE_APPLICATION_DISABLE_FILESYSTEM:

CONFIGURE_APPLICATION_DISABLE_FILESYSTEM
----------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_DISABLE_FILESYSTEM``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then a base filesystem and the
    configured filesystems are initialized during system initialization.

DESCRIPTION:
    In case this configuration option is defined, then **no base filesystem** is
    initialized during system initialization and **no filesystems** are
    configured.

NOTES:
    Filesystems shall be initialized to support file descriptor based device
    drivers and basic input/output functions such as :c:func:`printf`.
    Filesystems can be disabled to reduce the memory footprint of an application.

.. Generated from spec:/acfg/if/filesystem-all

.. index:: CONFIGURE_FILESYSTEM_ALL

.. _CONFIGURE_FILESYSTEM_ALL:

CONFIGURE_FILESYSTEM_ALL
------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_ALL``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the following
    configuration options will be defined as well

    * :ref:`CONFIGURE_FILESYSTEM_DOSFS`,

    * :ref:`CONFIGURE_FILESYSTEM_FTPFS`,

    * :ref:`CONFIGURE_FILESYSTEM_IMFS`,

    * :ref:`CONFIGURE_FILESYSTEM_JFFS2`,

    * :ref:`CONFIGURE_FILESYSTEM_NFS`,

    * :ref:`CONFIGURE_FILESYSTEM_RFS`, and

    * :ref:`CONFIGURE_FILESYSTEM_TFTPFS`.

NOTES:
    None.

.. Generated from spec:/acfg/if/filesystem-dosfs

.. index:: CONFIGURE_FILESYSTEM_DOSFS

.. _CONFIGURE_FILESYSTEM_DOSFS:

CONFIGURE_FILESYSTEM_DOSFS
--------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_DOSFS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the DOS (FAT) filesystem
    is registered, so that instances of this filesystem can be mounted by the
    application.

NOTES:
    This filesystem requires a Block Device Cache configuration, see
    :ref:`CONFIGURE_APPLICATION_NEEDS_LIBBLOCK`.

.. Generated from spec:/acfg/if/filesystem-ftpfs

.. index:: CONFIGURE_FILESYSTEM_FTPFS

.. _CONFIGURE_FILESYSTEM_FTPFS:

CONFIGURE_FILESYSTEM_FTPFS
--------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_FTPFS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the FTP filesystem (FTP
    client) is registered, so that instances of this filesystem
    can be mounted by the application.

NOTES:
    None.

.. Generated from spec:/acfg/if/filesystem-imfs

.. index:: CONFIGURE_FILESYSTEM_IMFS

.. _CONFIGURE_FILESYSTEM_IMFS:

CONFIGURE_FILESYSTEM_IMFS
-------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_IMFS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the In-Memory Filesystem
    (IMFS) is registered, so that instances of this filesystem can be mounted by
    the application.

NOTES:
    Applications will rarely need this configuration option.  This configuration
    option is intended for test programs.  You do not need to define this
    configuration option for the base filesystem (also known as root filesystem).

.. Generated from spec:/acfg/if/filesystem-jffs2

.. index:: CONFIGURE_FILESYSTEM_JFFS2

.. _CONFIGURE_FILESYSTEM_JFFS2:

CONFIGURE_FILESYSTEM_JFFS2
--------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_JFFS2``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the JFFS2 filesystem
    is registered, so that instances of this filesystem can be mounted by the
    application.

NOTES:
    None.

.. Generated from spec:/acfg/if/filesystem-nfs

.. index:: CONFIGURE_FILESYSTEM_NFS

.. _CONFIGURE_FILESYSTEM_NFS:

CONFIGURE_FILESYSTEM_NFS
------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_NFS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the Network Filesystem
    (NFS) client is registered, so that instances of this filesystem can be
    mounted by the application.

NOTES:
    None.

.. Generated from spec:/acfg/if/filesystem-rfs

.. index:: CONFIGURE_FILESYSTEM_RFS

.. _CONFIGURE_FILESYSTEM_RFS:

CONFIGURE_FILESYSTEM_RFS
------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_RFS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the RTEMS Filesystem (RFS)
    is registered, so that instances of this filesystem can be mounted by the
    application.

NOTES:
    This filesystem requires a Block Device Cache configuration, see
    :ref:`CONFIGURE_APPLICATION_NEEDS_LIBBLOCK`.

.. Generated from spec:/acfg/if/filesystem-tftpfs

.. index:: CONFIGURE_FILESYSTEM_TFTPFS

.. _CONFIGURE_FILESYSTEM_TFTPFS:

CONFIGURE_FILESYSTEM_TFTPFS
---------------------------

CONSTANT:
    ``CONFIGURE_FILESYSTEM_TFTPFS``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then the TFTP filesystem (TFTP
    client) is registered, so that instances of this filesystem can be mounted by
    the application.

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-chmod

.. index:: CONFIGURE_IMFS_DISABLE_CHMOD

.. _CONFIGURE_IMFS_DISABLE_CHMOD:

CONFIGURE_IMFS_DISABLE_CHMOD
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_CHMOD``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    changing the mode of files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support changing the mode of files (no support for :c:func:`chmod`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-chown

.. index:: CONFIGURE_IMFS_DISABLE_CHOWN

.. _CONFIGURE_IMFS_DISABLE_CHOWN:

CONFIGURE_IMFS_DISABLE_CHOWN
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_CHOWN``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    changing the ownership of files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support changing the ownership of files (no support for :c:func:`chown`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-link

.. index:: CONFIGURE_IMFS_DISABLE_LINK

.. _CONFIGURE_IMFS_DISABLE_LINK:

CONFIGURE_IMFS_DISABLE_LINK
---------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_LINK``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports hard
    links.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support hard links (no support for :c:func:`link`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-mknod

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD

.. _CONFIGURE_IMFS_DISABLE_MKNOD:

CONFIGURE_IMFS_DISABLE_MKNOD
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MKNOD``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports making
    files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support making files (no support for :c:func:`mknod`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-mknod-device

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE

.. _CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE:

CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE
-----------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MKNOD_DEVICE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports making
    device files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support making device files.

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-mknod-file

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD_FILE

.. _CONFIGURE_IMFS_DISABLE_MKNOD_FILE:

CONFIGURE_IMFS_DISABLE_MKNOD_FILE
---------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MKNOD_FILE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports making
    regular files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support making regular files.

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-mount

.. index:: CONFIGURE_IMFS_DISABLE_MOUNT

.. _CONFIGURE_IMFS_DISABLE_MOUNT:

CONFIGURE_IMFS_DISABLE_MOUNT
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MOUNT``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    mounting other filesystems.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support mounting other filesystems (no support for
    :c:func:`mount`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-readdir

.. index:: CONFIGURE_IMFS_DISABLE_READDIR

.. _CONFIGURE_IMFS_DISABLE_READDIR:

CONFIGURE_IMFS_DISABLE_READDIR
------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_READDIR``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    reading directories.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support reading directories (no support for :c:func:`readdir`).  It is
    still possible to open files in a directory.

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-readlink

.. index:: CONFIGURE_IMFS_DISABLE_READLINK

.. _CONFIGURE_IMFS_DISABLE_READLINK:

CONFIGURE_IMFS_DISABLE_READLINK
-------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_READLINK``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    reading symbolic links.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support reading symbolic links (no support for :c:func:`readlink`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-rename

.. index:: CONFIGURE_IMFS_DISABLE_RENAME

.. _CONFIGURE_IMFS_DISABLE_RENAME:

CONFIGURE_IMFS_DISABLE_RENAME
-----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_RENAME``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    renaming files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support renaming files (no support for :c:func:`rename`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-rmnod

.. index:: CONFIGURE_IMFS_DISABLE_RMNOD

.. _CONFIGURE_IMFS_DISABLE_RMNOD:

CONFIGURE_IMFS_DISABLE_RMNOD
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_RMNOD``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    removing files.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support removing files (no support for :c:func:`rmnod`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-symlink

.. index:: CONFIGURE_IMFS_DISABLE_SYMLINK

.. _CONFIGURE_IMFS_DISABLE_SYMLINK:

CONFIGURE_IMFS_DISABLE_SYMLINK
------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_SYMLINK``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    creating symbolic links.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support creating symbolic links (no support for :c:func:`symlink`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-unmount

.. index:: CONFIGURE_IMFS_DISABLE_UNMOUNT

.. _CONFIGURE_IMFS_DISABLE_UNMOUNT:

CONFIGURE_IMFS_DISABLE_UNMOUNT
------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_UNMOUNT``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    unmounting other filesystems.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support unmounting other filesystems (no support for
    :c:func:`unmount`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-disable-utime

.. index:: CONFIGURE_IMFS_DISABLE_UTIME

.. _CONFIGURE_IMFS_DISABLE_UTIME:

CONFIGURE_IMFS_DISABLE_UTIME
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_UTIME``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS supports
    changing file times.

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS does not
    support changing file times (no support for :c:func:`utime`).

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-enable-mkfifo

.. index:: CONFIGURE_IMFS_ENABLE_MKFIFO

.. _CONFIGURE_IMFS_ENABLE_MKFIFO:

CONFIGURE_IMFS_ENABLE_MKFIFO
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_ENABLE_MKFIFO``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the root IMFS does not
    support making FIFOs (no support for :c:func:`mkfifo`).

DESCRIPTION:
    In case this configuration option is defined, then the root IMFS supports
    making FIFOs.

NOTES:
    None.

.. Generated from spec:/acfg/if/imfs-memfile-bytes-per-block

.. index:: CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK

.. _CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK:

CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK
--------------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK``

OPTION TYPE:
    This configuration option is an integer define.

DEFAULT VALUE:
    The default value is 128.

VALUE CONSTRAINTS:
    The value of this configuration option shall be
    an element of {16, 32, 64, 128, 256, 512}.

DESCRIPTION:
    The value of this configuration option defines the block size for in-memory
    files managed by the IMFS.

NOTES:
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

.. Generated from spec:/acfg/if/use-devfs-as-base-filesystem

.. index:: CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM

.. _CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM:

CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM
--------------------------------------

CONSTANT:
    ``CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then an IMFS with a reduced
    feature set will be the base filesystem (also known as root filesystem).

NOTES:
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

.. index:: CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM

.. _CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM:

CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM
-----------------------------------------

CONSTANT:
    ``CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then an IMFS with a reduced
    feature set will be the base filesystem (also known as root filesystem).

NOTES:
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
