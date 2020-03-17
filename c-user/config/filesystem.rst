.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Filesystem Configuration
========================

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

.. index:: CONFIGURE_APPLICATION_DISABLE_FILESYSTEM

.. _CONFIGURE_APPLICATION_DISABLE_FILESYSTEM:

CONFIGURE_APPLICATION_DISABLE_FILESYSTEM
----------------------------------------

CONSTANT:
    ``CONFIGURE_APPLICATION_DISABLE_FILESYSTEM``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default. If no other root file system configuration
    parameters are specified, the IMFS will be used as the root file system.

DESCRIPTION:
    This configuration parameter is defined if the application dose not intend
    to use any kind of filesystem support. This include the device
    infrastructure necessary to support ``printf()``.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_CHMOD

.. _CONFIGURE_IMFS_DISABLE_CHMOD:

CONFIGURE_IMFS_DISABLE_CHMOD
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_CHMOD``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to change
    the mode is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_CHOWN

.. _CONFIGURE_IMFS_DISABLE_CHOWN:

CONFIGURE_IMFS_DISABLE_CHOWN
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_CHOWN``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to change
    the owner is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_LINK

.. _CONFIGURE_IMFS_DISABLE_LINK:

CONFIGURE_IMFS_DISABLE_LINK
---------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_LINK``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to create
    hard links is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD

.. _CONFIGURE_IMFS_DISABLE_MKNOD:

CONFIGURE_IMFS_DISABLE_MKNOD
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MKNOD``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to make
    directories, devices, regular files and FIFOs is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_MKNOD_FILE

.. _CONFIGURE_IMFS_DISABLE_MKNOD_FILE:

CONFIGURE_IMFS_DISABLE_MKNOD_FILE
---------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MKNOD_FILE``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to make
    regular files is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_MOUNT

.. _CONFIGURE_IMFS_DISABLE_MOUNT:

CONFIGURE_IMFS_DISABLE_MOUNT
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_MOUNT``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to mount
    other file systems is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_READDIR

.. _CONFIGURE_IMFS_DISABLE_READDIR:

CONFIGURE_IMFS_DISABLE_READDIR
------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_READDIR``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to read a
    directory is disabled in the root IMFS.  It is still possible to open nodes
    in a directory.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_READLINK

.. _CONFIGURE_IMFS_DISABLE_READLINK:

CONFIGURE_IMFS_DISABLE_READLINK
-------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_READLINK``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to read
    symbolic links is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_RENAME

.. _CONFIGURE_IMFS_DISABLE_RENAME:

CONFIGURE_IMFS_DISABLE_RENAME
-----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_RENAME``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to rename
    nodes is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_RMNOD

.. _CONFIGURE_IMFS_DISABLE_RMNOD:

CONFIGURE_IMFS_DISABLE_RMNOD
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_RMNOD``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to remove
    nodes is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_SYMLINK

.. _CONFIGURE_IMFS_DISABLE_SYMLINK:

CONFIGURE_IMFS_DISABLE_SYMLINK
------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_SYMLINK``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to create
    symbolic links is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_UNMOUNT

.. _CONFIGURE_IMFS_DISABLE_UNMOUNT:

CONFIGURE_IMFS_DISABLE_UNMOUNT
------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_UNMOUNT``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to unmount
    file systems is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_DISABLE_UTIME

.. _CONFIGURE_IMFS_DISABLE_UTIME:

CONFIGURE_IMFS_DISABLE_UTIME
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_DISABLE_UTIME``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to change
    times is disabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_ENABLE_MKFIFO

.. _CONFIGURE_IMFS_ENABLE_MKFIFO:

CONFIGURE_IMFS_ENABLE_MKFIFO
----------------------------

CONSTANT:
    ``CONFIGURE_IMFS_ENABLE_MKFIFO``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the support to make FIFOs
    is enabled in the root IMFS.

NOTES:
    None.

.. index:: CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK

.. _CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK:

CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK
--------------------------------------

CONSTANT:
    ``CONFIGURE_IMFS_MEMFILE_BYTES_PER_BLOCK``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Valid values for this configuration parameter are a power of two (2)
    between 16 and 512 inclusive.  In other words, valid values are 16, 32, 64,
    128, 256,and 512.

DEFAULT VALUE:
    The default IMFS block size is 128 bytes.

DESCRIPTION:
    This configuration parameter specifies the block size for in-memory files
    managed by the IMFS. The configured block size has two impacts. The first
    is the average amount of unused memory in the last block of each file. For
    example, when the block size is 512, on average one-half of the last block
    of each file will remain unused and the memory is wasted. In contrast, when
    the block size is 16, the average unused memory per file is only 8
    bytes. However, it requires more allocations for the same size file and
    thus more overhead per block for the dynamic memory management.

    Second, the block size has an impact on the maximum size file that can be
    stored in the IMFS. With smaller block size, the maximum file size is
    correspondingly smaller. The following shows the maximum file size possible
    based on the configured block size:

    - when the block size is 16 bytes, the maximum file size is 1,328 bytes.

    - when the block size is 32 bytes, the maximum file size is 18,656 bytes.

    - when the block size is 64 bytes, the maximum file size is 279,488 bytes.

    - when the block size is 128 bytes, the maximum file size is 4,329,344 bytes.

    - when the block size is 256 bytes, the maximum file size is 68,173,568 bytes.

    - when the block size is 512 bytes, the maximum file size is 1,082,195,456
      bytes.

NOTES:
    None.

.. index:: CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM

.. _CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM:

CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM
--------------------------------------

CONSTANT:
    ``CONFIGURE_USE_DEVFS_AS_BASE_FILESYSTEM``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default. If no other root file system configuration
    parameters are specified, the IMFS will be used as the root file system.

DESCRIPTION:
    This configuration parameter is defined if the application wishes to use
    the device-only filesytem as the root file system.

NOTES:
    The device-only filesystem supports only device nodes and is smaller in
    executable code size than the full IMFS and miniIMFS.

    The devFS is comparable in functionality to the pseudo-filesystem name
    space provided before RTEMS release 4.5.0.

.. index:: CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM

.. _CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM:

CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM
-----------------------------------------

CONSTANT:
    ``CONFIGURE_USE_MINIIMFS_AS_BASE_FILESYSTEM``

DATA TYPE:
    Boolean feature macro.

RANGE:
    Defined or undefined.

DEFAULT VALUE:
    This is not defined by default.

DESCRIPTION:
    In case this configuration option is defined, then the following
    configuration options will be defined as well

    - ``CONFIGURE_IMFS_DISABLE_CHMOD``,

    - ``CONFIGURE_IMFS_DISABLE_CHOWN``,

    - ``CONFIGURE_IMFS_DISABLE_UTIME``,

    - ``CONFIGURE_IMFS_DISABLE_LINK``,

    - ``CONFIGURE_IMFS_DISABLE_SYMLINK``,

    - ``CONFIGURE_IMFS_DISABLE_READLINK``,

    - ``CONFIGURE_IMFS_DISABLE_RENAME``, and

    - ``CONFIGURE_IMFS_DISABLE_UNMOUNT``.

NOTES:
    None.
