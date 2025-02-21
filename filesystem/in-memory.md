.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

In-Memory Filesystem
********************

This chapter describes the In-Memory FileSystem (IMFS).  The IMFS is a full
featured POSIX filesystem that keeps all information in memory.

IMFS Per Node Data Structure
============================

Each regular file, device, hard link, and directory is represented by a data
structure called a ``jnode``. The ``jnode`` is formally represented by the
structure:

.. code-block:: c

    struct IMFS_jnode_tt {
        Chain_Node          Node;             /* for chaining them together */
        IMFS_jnode_t       *Parent;           /* Parent node */
        char                name[NAME_MAX+1]; /* "basename" */
        mode_t              st_mode;          /* File mode */
        nlink_t             st_nlink;         /* Link count */
        ino_t               st_ino;           /* inode */
        uid_t               st_uid;           /* User ID of owner */
        gid_t               st_gid;           /* Group ID of owner */
        time_t              st_atime;         /* Time of last access */
        time_t              st_mtime;         /* Time of last modification */
        time_t              st_ctime;         /* Time of last status change */
        IMFS_jnode_types_t  type;             /* Type of this entry */
        IMFS_typs_union     info;
    };

The key elements of this structure are listed below together with a brief
explanation of their role in the filesystem.

*Node*
    exists to allow the entire ``jnode`` structure to be included in a chain.

*Parent*
    is a pointer to another ``jnode`` structure that is the logical parent of
    the node in which it appears.  This field may be NULL if the file
    associated with this node is deleted but there are open file descriptors on
    this file or there are still hard links to this node.

*name*
    is the name of this node within the filesystem hierarchical tree. Example:
    If the fully qualified pathname to the ``jnode`` was ``/a/b/c``, the
    ``jnode`` name field would contain the null terminated string ``"c"``.

*st_mode*
    is the standard Unix access permissions for the file or directory.

*st_nlink*
    is the number of hard links to this file. When a ``jnode`` is first created
    its link count is set to 1. A ``jnode`` and its associated resources cannot
    be deleted unless its link count is less than 1.

*st_ino*
    is a unique node identification number

*st_uid*
    is the user ID of the file's owner

*st_gid*
    is the group ID of the file's owner

*st_atime*
    is the time of the last access to this file

*st_mtime*
    is the time of the last modification of this file

*st_ctime*
    is the time of the last status change to the file

*type*
    is the indication of node type must be one of the following states:
      - IMFS_DIRECTORY
      - IMFS_MEMORY_FILE
      - IMFS_HARD_LINK
      - IMFS_SYM_LINK
      - IMFS_DEVICE

*info*
    is this contains a structure that is unique to file type (See
    IMFS_typs_union in imfs.h).

    - IMFS_DIRECTORY

      An IMFS directory contains a dynamic chain structure that records all
      files and directories that are subordinate to the directory node.

    - IMFS_MEMORY_FILE

      Under the in memory filesystem regular files hold data. Data is
      dynamically allocated to the file in 128 byte chunks of memory.  The
      individual chunks of memory are tracked by arrays of pointers that record
      the address of the allocated chunk of memory. Single, double, and triple
      indirection pointers are used to record the locations of all segments of
      the file.  The memory organization of an IMFS file are discussed
      elsewhere in this manual.

    - IMFS_HARD_LINK

      The IMFS filesystem supports the concept of hard links to other nodes in
      the IMFS filesystem.  These hard links are actual pointers to other nodes
      in the same filesystem. This type of link cannot cross-filesystem
      boundaries.

    - IMFS_SYM_LINK

      The IMFS filesystem supports the concept of symbolic links to other nodes
      in any filesystem. A symbolic link consists of a pointer to a character
      string that represents the pathname to the target node. This type of link
      can cross-filesystem boundaries.  Just as with most versions of UNIX
      supporting symbolic links, a symbolic link can point to a non-existent
      file.

    - IMFS_DEVICE

      All RTEMS devices now appear as files under the in memory filesystem. On
      system initialization, all devices are registered as nodes under the file
      system.

Miscellaneous IMFS Information
==============================

TBD

Memory associated with the IMFS
===============================

A memory based filesystem draws its resources for files and directories from
the memory resources of the system. When it is time to un-mount the filesystem,
the memory resources that supported filesystem are set free.  In order to free
these resources, a recursive walk of the filesystems tree structure will be
performed. As the leaf nodes under the filesystem are encountered their
resources are freed. When directories are made empty by this process, their
resources are freed.

Node removal constraints for the IMFS
-------------------------------------

The IMFS conforms to the general filesystem requirements for node removal.  See
:ref:`file-and-directory-removal-constraints`.

IMFS General Housekeeping Notes
-------------------------------

The following is a list of odd housekeeping notes for the IMFS.

- If the global variable rtems_filesystem_current refers to the node that we
  are trying to remove, the node_access element of this structure must be set
  to NULL to invalidate it.

- If the node was of IMFS_MEMORY_FILE type, free the memory associated with the
  memory file before freeing the node. Use the IMFS_memfile_remove() function.

IMFS Operation Tables
=====================

IMFS Filesystem Handler Table Functions
---------------------------------------

OPS table functions are defined in a rtems_filesystem_operations_table
structure.  It defines functions that are specific to a given filesystem.  One
table exists for each filesystem that is supported in the RTEMS
configuration. The structure definition appears below and is followed by
general developmental information on each of the functions contained in this
function management structure.

.. code-block:: c

    rtems_filesystem_operations_table  IMFS_ops = {
        IMFS_eval_path,
        IMFS_evaluate_for_make,
        IMFS_link,
        IMFS_unlink,
        IMFS_node_type,
        IMFS_mknod,
        IMFS_rmnod,
        IMFS_chown,
        IMFS_freenodinfo,
        IMFS_mount,
        IMFS_initialize,
        IMFS_unmount,
        IMFS_fsunmount,
        IMFS_utime,
        IMFS_evaluate_link,
        IMFS_symlink,
        IMFS_readlink
    };

.. COMMENT: @page

IMFS_evalpath()
^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_evalformake()
^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_link()
^^^^^^^^^^^

Corresponding Structure Element:
    ``link``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t    *to_loc,      /* IN */
        rtems_filesystem_location_info_t    *parent_loc,  /* IN */
        const char                          *token        /* IN */

File:
    ``imfs_link.c``

Description:

    This routine is used in the IMFS filesystem to create a hard-link.

    It will first examine the st_nlink count of the node that we are trying to.
    If the link count exceeds LINK_MAX an error will be returned.

    The name of the link will be normalized to remove extraneous separators
    from the end of the name.

    IMFS_create_node will be used to create a filesystem node that will have
    the following characteristics:

    - parent that was determined in the link() function in file link.c

    - Type will be set to IMFS_HARD_LINK

    - name will be set to the normalized name

    - mode of the hard-link will be set to the mode of the target node

    If there was trouble allocating memory for the new node an error will be
    returned.

    The st_nlink count of the target node will be incremented to reflect the
    new link.

    The time fields of the link will be set to reflect the creation time of the
    hard-link.

IMFS_unlink()
^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_node_type()
^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_node_type()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t    *pathloc        /* IN */

File:
    ``imfs_ntype.c``

Description:
    This routine will locate the IMFS_jnode_t structure that holds ownership
    information for the selected node in the filesystem.

    This structure is pointed to by pathloc->node_access.

    The IMFS_jnode_t type element indicates one of the node types listed below:

    - RTEMS_FILESYSTEM_DIRECTORY

    - RTEMS_FILESYSTEM_DEVICE

    - RTEMS_FILESYSTEM_HARD_LINK

    - RTEMS_FILESYSTEM_MEMORY_FILE

.. COMMENT: @page

IMFS_mknod()
^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_mknod()``

Arguments:
    .. code-block:: c

        const char                          *token,        /* IN */
        mode_t                               mode,         /* IN */
        dev_t                                dev,          /* IN */
        rtems_filesystem_location_info_t    *pathloc       /* IN/OUT */

File:
    ``imfs_mknod.c``

Description:
    This routine will examine the mode argument to determine is we are trying
    to create a directory, regular file and a device node. The creation of
    other node types is not permitted and will cause an assert.

    Memory space will be allocated for a ``jnode`` and the node will be set up
    according to the nodal type that was specified. The IMFS_create_node()
    function performs the allocation and setup of the node.

    The only problem that is currently reported is the lack of memory when we
    attempt to allocate space for the ``jnode`` (ENOMEN).

IMFS_rmnod()
^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_chown()
^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_chown()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t    *pathloc        /* IN */
        uid_t                                owner          /* IN */
        gid_t                                group          /* IN */

File:
    ``imfs_chown.c``

Description:
    This routine will locate the IMFS_jnode_t structure that holds ownership
    information for the selected node in the filesystem.

    This structure is pointed to by pathloc->node_access.

    The st_uid and st_gid fields of the node are then modified. Since this is a
    memory based filesystem, no further action is required to alter the
    ownership of the IMFS_jnode_t structure.

IMFS_freenod()
^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_freenod()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t      *pathloc       /* IN */

File:
    ``imfs_free.c``

Description:
    This method is a private function to the IMFS.  It is called by IMFS
    routines to free nodes that have been allocated.  Examples of where this
    routine may be called from are unlink and rmnod.

    Note: This routine should not be confused with the filesystem callback
    freenod.  The IMFS allocates memory until the node no longer exists.

IMFS_freenodinfo()
^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_freenodinfo()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t      *pathloc       /* IN */

File:
    ``imfs_free.c``

Description:
    The In-Memory File System does not need to allocate memory during the
    evaluate routines. Therefore, this routine simply routines PASS.

IMFS_mount()
^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_mount()``

Arguments:
    .. code-block:: c

        rtems_filesystem_mount_table_entry_t   *mt_entry

File:
    ``imfs_mount.c``

Description:
    This routine provides the filesystem specific processing required to mount
    a filesystem for the system that contains the mount point. It will
    determine if the point that we are trying to mount onto is a node of
    IMFS_DIRECTORY type.

    If it is the node's info element is altered so that the
    info.directory.mt_fs element points to the mount table chain entry that is
    associated with the mounted filesystem at this point. The
    info.directory.mt_fs element can be examined to determine if a filesystem
    is mounted at a directory. If it is NULL, the directory does not serve as a
    mount point. A non-NULL entry indicates that the directory does serve as a
    mount point and the value of info.directory.mt_fs can be used to locate the
    mount table chain entry that describes the filesystem mounted at this
    point.

IMFS_fsmount_me()
^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_initialize()``

Arguments:
    .. code-block:: c

        rtems_filesystem_mount_table_entry_t   *mt_entry

File:
    ``imfs_init.c``

Description:
    This function is provided with a filesystem to take care of the internal
    filesystem management details associated with mounting that filesystem
    under the RTEMS environment.

    It is not responsible for the mounting details associated the filesystem
    containing the mount point.

    The rtems_filesystem_mount_table_entry_t structure contains the key
    elements below:

    .. code-block:: c

        rtems_filesystem_location_info_t         *mt_point_node,

    This structure contains information about the mount point. This allows us
    to find the ops-table and the handling functions associated with the
    filesystem containing the mount point.

    .. code-block:: c

        rtems_filesystem_location_info_t         *fs_root_node,

    This structure contains information about the root node in the file system
    to be mounted. It allows us to find the ops-table and the handling
    functions associated with the filesystem to be mounted.

    .. code-block:: c

        rtems_filesystem_options_t                 options,

    Read only or read/write access

    .. code-block:: c

        void                                         *fs_info,

    This points to an allocated block of memory the will be used to hold any
    filesystem specific information of a global nature. This allocated region
    if important because it allows us to mount the same filesystem type more
    than once under the RTEMS system.  Each instance of the mounted filesystem
    has its own set of global management information that is separate from the
    global management information associated with the other instances of the
    mounted filesystem type.

    .. code-block:: c

        rtems_filesystem_limits_and_options_t    pathconf_info,

    The table contains the following set of values associated with the mounted
    filesystem:

    - link_max

    - max_canon

    - max_input

    - name_max

    - path_max

    - pipe_buf

    - posix_async_io

    - posix_chown_restrictions

    - posix_no_trunc

    - posix_prio_io

    - posix_sync_io

    - posix_vdisable

    These values are accessed with the pathconf() and the fpathconf ()
    functions.

    .. code-block:: c

        const char                                   *dev

    The is intended to contain a string that identifies the device that
    contains the filesystem information. The filesystems that are currently
    implemented are memory based and don't require a device specification.

    If the mt_point_node.node_access is NULL then we are mounting the base file
    system.

    The routine will create a directory node for the root of the IMFS file
    system.

    The node will have read, write and execute permissions for owner, group and
    others.

    The node's name will be a null string.

    A filesystem information structure(fs_info) will be allocated and
    initialized for the IMFS filesystem. The fs_info pointer in the mount table
    entry will be set to point the filesystem information structure.

    The pathconf_info element of the mount table will be set to the appropriate
    table of path configuration constants ( IMFS_LIMITS_AND_OPTIONS ).

    The fs_root_node structure will be filled in with the following:

    - pointer to the allocated root node of the filesystem

    - directory handlers for a directory node under the IMFS filesystem

    - OPS table functions for the IMFS

    A 0 will be returned to the calling routine if the process succeeded,
    otherwise a 1 will be returned.

IMFS_unmount()
^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_unmount()``

Arguments:
    .. code-block:: c

        rtems_filesystem_mount_table_entry_t   *mt_entry

File:
    ``imfs_unmount.c``

Description:
    This routine allows the IMFS to unmount a filesystem that has been mounted
    onto a IMFS directory.

    The mount entry mount point node access is verified to be a mounted
    directory.  It's mt_fs is set to NULL.  This identifies to future calles
    into the IMFS that this directory node is no longer a mount point.
    Additionally, it will allow any directories that were hidden by the mounted
    system to again become visible.

IMFS_fsunmount()
^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``imfs_fsunmount()``

Arguments:
    .. code-block:: c

        rtems_filesystem_mount_table_entry_t   *mt_entry

File:
    ``imfs_init.c``

Description:
    This method unmounts this instance of the IMFS file system.  It is the
    counterpart to the IMFS_initialize routine.  It is called by the generic
    code under the fsunmount_me callback.

    All method loops finding the first encountered node with no children and
    removing the node from the tree, thus returning allocated resources.  This
    is done until all allocated nodes are returned.

IMFS_utime()
^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_eval_link()
^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

Regular File Handler Table Functions
------------------------------------

Handler table functions are defined in a rtems_filesystem_file_handlers_r
structure. It defines functions that are specific to a node type in a given
filesystem. One table exists for each of the filesystem's node types. The
structure definition appears below. It is followed by general developmental
information on each of the functions associated with regular files contained in
this function management structure.

.. code-block:: c

    rtems_filesystem_file_handlers_r IMFS_memfile_handlers = {
        memfile_open,
        memfile_close,
        memfile_read,
        memfile_write,
        memfile_ioctl,
        memfile_lseek,
        IMFS_stat,
        IMFS_fchmod,
        memfile_ftruncate,
        NULL,                /* fpathconf */
        NULL,                /* fsync */
        IMFS_fdatasync,
        IMFS_fcntl
    };

memfile_open() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``memfile_open()``

Arguments:
    .. code-block:: c

        rtems_libio_t   *iop,
        const char      *pathname,
        unsigned32       flag,
        unsigned32       mode

File:
    ``memfile.c``

Description:
    Currently this function is a shell. No meaningful processing is performed
    and a success code is always returned.

memfile_close() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``memfile_close()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop

File:
    ``memfile.c``

Description:
    This routine is a dummy for regular files under the base filesystem. It
    performs a capture of the IMFS_jnode_t pointer from the file control block
    and then immediately returns a success status.

memfile_read() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``memfile_read()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop,
        void              *buffer,
        unsigned32         count

File:
    ``memfile.c``

Description:
    This routine will determine the ``jnode`` that is associated with this
    file.

    It will then call IMFS_memfile_read() with the ``jnode``, file position
    index, buffer and transfer count as arguments.

    IMFS_memfile_read() will do the following:

    - Verify that the ``jnode`` is associated with a memory file

    - Verify that the destination of the read is valid

    - Adjust the length of the read if it is too long

    - Acquire data from the memory blocks associated with the file

    - Update the access time for the data in the file

memfile_write() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

memfile_ioctl() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    .. code-block:: c

        rtems_libio_t   *iop,
        unsigned32       command,
        void            *buffer

File:
    ``memfile.c``

Description:
    The current code is a placeholder for future development. The routine
    returns a successful completion status.

memfile_lseek() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``Memfile_lseek()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop,
        off_t              offset,
        int                whence

File:
    ``memfile.c``

Description:
    This routine make sure that the memory based file is sufficiently large to
    allow for the new file position index.

    The IMFS_memfile_extend() function is used to evaluate the current size of
    the memory file and allocate additional memory blocks if required by the
    new file position index. A success code is always returned from this
    routine.

IMFS_stat() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_stat()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t   *loc,
        struct stat                        *buf

File:
    ``imfs_stat.c``

Description:
    This routine actually performs status processing for both devices and
    regular files.

    The IMFS_jnode_t structure is referenced to determine the type of node
    under the filesystem.

    If the node is associated with a device, node information is extracted and
    transformed to set the st_dev element of the stat structure.

    If the node is a regular file, the size of the regular file is extracted
    from the node.

    This routine rejects other node types.

    The following information is extracted from the node and placed in the stat
    structure:

    - st_mode

    - st_nlink

    - st_ino

    - st_uid

    - st_gid

    - st_atime

    - st_mtime

    - st_ctime

IMFS_fchmod() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_fchmod()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop
        mode_t             mode

File:
    ``imfs_fchmod.c``

Description:
    This routine will obtain the pointer to the IMFS_jnode_t structure from the
    information currently in the file control block.

    Based on configuration the routine will acquire the user ID from a call to
    getuid() or from the IMFS_jnode_t structure.

    It then checks to see if we have the ownership rights to alter the mode of
    the file.  If the caller does not, an error code is returned.

    An additional test is performed to verify that the caller is not trying to
    alter the nature of the node. If the caller is attempting to alter more
    than the permissions associated with user group and other, an error is
    returned.

    If all the preconditions are met, the user, group and other fields are set
    based on the mode calling parameter.

memfile_ftruncate() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

No pathconf() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``NULL``

Arguments:
    Not Implemented

File:
    Not Implemented

Description:
    Not Implemented

No fsync() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_fdatasync() for Regular Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

Directory Handler Table Functions
---------------------------------

Handler table functions are defined in a rtems_filesystem_file_handlers_r
structure. It defines functions that are specific to a node type in a given
filesystem. One table exists for each of the filesystem's node types. The
structure definition appears below. It is followed by general developmental
information on each of the functions associated with directories contained in
this function management structure.

.. code:: c

    rtems_filesystem_file_handlers_r IMFS_directory_handlers = {
        IMFS_dir_open,
        IMFS_dir_close,
        IMFS_dir_read,
        NULL,             /* write */
        NULL,             /* ioctl */
        IMFS_dir_lseek,
        IMFS_dir_fstat,
        IMFS_fchmod,
        NULL,             /* ftruncate */
        NULL,             /* fpathconf */
        NULL,             /* fsync */
        IMFS_fdatasync,
        IMFS_fcntl
    };

IMFS_dir_open() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``imfs_dir_open()``

Arguments:
    .. code-block:: c

        rtems_libio_t  *iop,
        const char     *pathname,
        unsigned32      flag,
        unsigned32      mode

File:
    ``imfs_directory.c``

Description:
    This routine will look into the file control block to find the ``jnode``
    that is associated with the directory.

    The routine will verify that the node is a directory. If its not a
    directory an error code will be returned.

    If it is a directory, the offset in the file control block will be set
    to 0.  This allows us to start reading at the beginning of the directory.

IMFS_dir_close() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``imfs_dir_close()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop

File:
    ``imfs_directory.c``

Description:
    This routine is a dummy for directories under the base filesystem. It
    immediately returns a success status.

IMFS_dir_read() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``imfs_dir_read``

Arguments:
    .. code-block:: c

        rtems_libio_t  *iop,
        void           *buffer,
        unsigned32      count

File:
    ``imfs_directory.c``

Description:
    This routine will read a fixed number of directory entries from the current
    directory offset. The number of directory bytes read will be returned from
    this routine.

No write() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

No ioctl() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``ioctl``

Arguments:
    Not supported

File:
    Not supported

Description:
    XXX

IMFS_dir_lseek() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``imfs_dir_lseek()``

Arguments:
    .. code-block:: c

        rtems_libio_t      *iop,
        off_t               offset,
        int                 whence

File:
    ``imfs_directory.c``

Description:
    This routine alters the offset in the file control block.

    No test is performed on the number of children under the current open
    directory.  The imfs_dir_read() function protects against reads beyond the
    current size to the directory by returning a 0 bytes transfered to the
    calling programs whenever the file position index exceeds the last entry in
    the open directory.

IMFS_dir_fstat() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``imfs_dir_fstat()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t   *loc,
        struct stat                        *buf

File:
    ``imfs_directory.c``

Description:
    The node access information in the rtems_filesystem_location_info_t
    structure is used to locate the appropriate IMFS_jnode_t structure. The
    following information is taken from the IMFS_jnode_t structure and placed
    in the stat structure:

    - st_ino

    - st_mode

    - st_nlink

    - st_uid

    - st_gid

    - st_atime

    - st_mtime

    - st_ctime

    The st_size field is obtained by running through the chain of directory
    entries and summing the sizes of the dirent structures associated with each
    of the children of the directory.

IMFS_fchmod() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_fchmod()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop
        mode_t             mode

File:
    ``imfs_fchmod.c``

Description:
    This routine will obtain the pointer to the IMFS_jnode_t structure from the
    information currently in the file control block.

    Based on configuration the routine will acquire the user ID from a call to
    getuid() or from the IMFS_jnode_t structure.

    It then checks to see if we have the ownership rights to alter the mode of
    the file.  If the caller does not, an error code is returned.

    An additional test is performed to verify that the caller is not trying to
    alter the nature of the node. If the caller is attempting to alter more
    than the permissions associated with user group and other, an error is
    returned.

    If all the preconditions are met, the user, group and other fields are set
    based on the mode calling parameter.

No ftruncate() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

No fpathconf() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``fpathconf``

Arguments:
    Not Implemented

File:
    Not Implemented

Description:
    Not Implemented

No fsync() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

IMFS_fdatasync() for Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

Device Handler Table Functions
------------------------------

Handler table functions are defined in a rtems_filesystem_file_handlers_r
structure. It defines functions that are specific to a node type in a given
filesystem. One table exists for each of the filesystem's node types. The
structure definition appears below. It is followed by general developmental
information on each of the functions associated with devices contained in this
function management structure.

.. code-block:: c

    typedef struct {
        rtems_filesystem_open_t           open;
        rtems_filesystem_close_t          close;
        rtems_filesystem_read_t           read;
        rtems_filesystem_write_t          write;
        rtems_filesystem_ioctl_t          ioctl;
        rtems_filesystem_lseek_t          lseek;
        rtems_filesystem_fstat_t          fstat;
        rtems_filesystem_fchmod_t         fchmod;
        rtems_filesystem_ftruncate_t      ftruncate;
        rtems_filesystem_fpathconf_t      fpathconf;
        rtems_filesystem_fsync_t          fsync;
        rtems_filesystem_fdatasync_t      fdatasync;
    } rtems_filesystem_file_handlers_r;

device_open() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``device_open()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop,
        const char        *pathname,
        unsigned32         flag,
        unsigned32         mode

File:
    ``deviceio.c``

Description:
    This routine will use the file control block to locate the node structure
    for the device.

    It will extract the major and minor device numbers from the ``jnode``.

    The major and minor device numbers will be used to make a rtems_io_open()
    function call to open the device driver. An argument list is sent to the
    driver that contains the file control block, flags and mode information.

device_close() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``device_close()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop

File:
    ``deviceio.c``

Description:
    This routine extracts the major and minor device driver numbers from the
    IMFS_jnode_t that is referenced in the file control block.

    It also forms an argument list that contains the file control block.

    A rtems_io_close() function call is made to close the device specified by
    the major and minor device numbers.

device_read() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``device_read()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop,
        void              *buffer,
        unsigned32         count

File:
    ``deviceio.c``

Description:
    This routine will extract the major and minor numbers for the device from
    the - jnode- associated with the file descriptor.

    A rtems_io_read() call will be made to the device driver associated with
    the file descriptor. The major and minor device number will be sent as
    arguments as well as an argument list consisting of:

    - file control block

    - file position index

    - buffer pointer where the data read is to be placed

    - count indicating the number of bytes that the program wishes to read from
      the device

    - flags from the file control block

    On return from the rtems_io_read() the number of bytes that were actually
    read will be returned to the calling program.

device_write() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

device_ioctl() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``ioctl``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop,
        unsigned32         command,
        void              *buffer

File:
    ``deviceio.c``

Description:
    This handler will obtain status information about a device.

    The form of status is device dependent.

    The rtems_io_control() function uses the major and minor number of the
    device to obtain the status information.

    rtems_io_control() requires an rtems_libio_ioctl_args_t argument list which
    contains the file control block, device specific command and a buffer
    pointer to return the device status information.

    The device specific command should indicate the nature of the information
    that is desired from the device.

    After the rtems_io_control() is processed, the buffer should contain the
    requested device information.

    If the device information is not obtained properly a -1 will be returned to
    the calling program, otherwise the ioctl_return value is returned.

device_lseek() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``device_lseek()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop,
        off_t              offset,
        int                whence

File:
    ``deviceio.c``

Description:
    At the present time this is a placeholder function. It always returns a
    successful status.

IMFS_stat() for Devices
^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_stat()``

Arguments:
    .. code-block:: c

        rtems_filesystem_location_info_t   *loc,
        struct stat                        *buf

File:
    ``imfs_stat.c``

Description:
    This routine actually performs status processing for both devices and
    regular files.

    The IMFS_jnode_t structure is referenced to determine the type of node
    under the filesystem.

    If the node is associated with a device, node information is extracted and
    transformed to set the st_dev element of the stat structure.

    If the node is a regular file, the size of the regular file is extracted
    from the node.

    This routine rejects other node types.

    The following information is extracted from the node and placed in the stat
    structure:

    - st_mode

    - st_nlink

    - st_ino

    - st_uid

    - st_gid

    - st_atime

    - st_mtime

    - st_ctime

IMFS_fchmod() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``IMFS_fchmod()``

Arguments:
    .. code-block:: c

        rtems_libio_t     *iop
        mode_t             mode

File:
    ``imfs_fchmod.c``

Description:
    This routine will obtain the pointer to the IMFS_jnode_t structure from the
    information currently in the file control block.

    Based on configuration the routine will acquire the user ID from a call to
    getuid() or from the IMFS_jnode_t structure.

    It then checks to see if we have the ownership rights to alter the mode of
    the file.  If the caller does not, an error code is returned.

    An additional test is performed to verify that the caller is not trying to
    alter the nature of the node. If the caller is attempting to alter more
    than the permissions associated with user group and other, an error is
    returned.

    If all the preconditions are met, the user, group and other fields are set
    based on the mode calling parameter.

No ftruncate() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

No fpathconf() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    ``fpathconf``

Arguments:
    Not Implemented

File:
    Not Implemented

Description:
    Not Implemented

No fsync() for Devices
^^^^^^^^^^^^^^^^^^^^^^

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX

No fdatasync() for Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^

Not Implemented

Corresponding Structure Element:
    XXX

Arguments:
    XXX

File:
    XXX

Description:
    XXX
