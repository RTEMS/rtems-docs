% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Filesystem Implementation Requirements

This chapter details the behavioral requirements that all filesystem
implementations must adhere to.

## General

The RTEMS filesystem framework was intended to be compliant with the POSIX
Files and Directories interface standard. The following filesystem
characteristics resulted in a functional switching layer.

```shell
Figure of the Filesystem Functional Layering goes here.
This figure includes networking and disk caching layering.
```

# Application programs are presented with a standard set of POSIX compliant

: functions that allow them to interface with the files, devices and
  directories in the filesystem. The interfaces to these routines do not
  reflect the type of subordinate filesystem implementation in which the file
  will be found.

# The filesystem framework developed under RTEMS allows for mounting filesystem

: of different types under the base filesystem.

# The mechanics of locating file information may be quite different between

: filesystem types.

\# The process of locating a file may require crossing filesystem boundaries.

# The transitions between filesystem and the processing required to access

: information in different filesystem is not visible at the level of the POSIX
  function call.

# The POSIX interface standard provides file access by character pathname to

: the file in some functions and through an integer file descriptor in other
  functions.

# The nature of the integer file descriptor and its associated processing is

: operating system and filesystem specific.

# Directory and device information must be processed with some of the same

: routines that apply to files.

# The form and content of directory and device information differs greatly from

: that of a regular file.

# Files, directories and devices represent elements (nodes) of a tree

: hierarchy.

# The rules for processing each of the node types that exist under the

: filesystem are node specific but are still not reflected in the POSIX
  interface routines.

```shell
Figure of the Filesystem Functional Layering goes here.
This figure focuses on the Base Filesystem and IMFS.
```

```shell
Figure of the IMFS Memfile control blocks
```

(file-and-directory-removal-constraints)=

## File and Directory Removal Constraints

The following POSIX constraints must be honored by all filesystems.

- If a node is a directory with children it cannot be removed.
- The root node of any filesystem, whether the base filesystem or a mounted
  filesystem, cannot be removed.
- A node that is a directory that is acting as the mount point of a file system
  cannot be removed.
- On filesystems supporting hard links, a link count is maintained. Prior to
  node removal, the node's link count is decremented by one. The link count
  must be less than one to allow for removal of the node.

## API Layering

### Mapping of Generic System Calls to Filesystem Specific Functions

The list of generic system calls includes the routines open(), read(), write(),
close(), etc..

The Files and Directories section of the POSIX Application Programs Interface
specifies a set of functions with calling arguments that are used to gain
access to the information in a filesystem. To the application program, these
functions allow access to information in any mounted filesystem without
explicit knowledge of the filesystem type or the filesystem mount
configuration. The following are functions that are provided to the
application:

01. access()
02. chdir()
03. chmod()
04. chown()
05. close()
06. closedir()
07. fchmod()
08. fcntl()
09. fdatasync()
10. fpathconf()
11. fstat()
12. fsync()
13. ftruncate()
14. link()
15. lseek()
16. mkdir()
17. mknod()
18. mount()
19. open()
20. opendir()
21. pathconf()
22. read()
23. readdir()
24. rewinddir()
25. rmdir()
26. rmnod()
27. scandir()
28. seekdir()
29. stat()
30. telldir()
31. umask()
32. unlink()
33. unmount()
34. utime()
35. write()

The filesystem's type as well as the node type within the filesystem determine
the nature of the processing that must be performed for each of the functions
above. The RTEMS filesystem provides a framework that allows new filesystem to
be developed and integrated without alteration to the basic framework.

To provide the functional switching that is required, each of the POSIX file
and directory functions have been implemented as a shell function. The shell
function adheres to the POSIX interface standard. Within this functional shell,
filesystem and node type information is accessed which is then used to invoke
the appropriate filesystem and node type specific routine to process the POSIX
function call.

### File/Device/Directory function access via file control block - rtems_libio_t structure

The POSIX open() function returns an integer file descriptor that is used as a
reference to file control block information for a specific file. The file
control block contains information that is used to locate node, file system,
mount table and functional handler information. The diagram in Figure 8 depicts
the relationship between and among the following components.

File Descriptor Table:

: This is an internal RTEMS structure that tracks all currently defined file
  descriptors in the system. The index that is returned by the file open()
  operation references a slot in this table. The slot contains a pointer to the
  file descriptor table entry for this file. The rtems_libio_t structure
  represents the file control block.

Allocation of entry in the File Descriptor Table:

: Access to the file descriptor table is controlled through a semaphore that is
  implemented using the rtems_libio_allocate() function. This routine will grab
  a semaphore and then scan the file control blocks to determine which slot is
  free for use. The first free slot is marked as used and the index to this
  slot is returned as the file descriptor for the open() request. After the
  alterations have been made to the file control block table, the semaphore is
  released to allow further operations on the table.

  Maximum number of entries in the file descriptor table is configurable
  through the src/exec/sapi/headers/confdefs.h file. If the
  `CONFIGURE_LIBIO_MAXIMUM_FILE_DESCRIPTORS` constant is defined its value
  will represent the maximum number of file descriptors that are allowed. If
  `CONFIGURE_LIBIO_MAXIMUM_FILE_DESCRIPTORS` is not specified a default value
  of 20 will be used as the maximum number of file descriptors allowed.

File control block - rtems_libio_t structure:

: ```c
  struct rtems_libio_tt {
      rtems_driver_name_t              *driver;
      off_t                             size;
      off_t                             offset;
      unsigned32                        flags;
      rtems_filesystem_location_info_t  pathinfo;
      Objects_Id                        sem;
      unsigned32                        data0;
      void                              data1;
      void                              file_info;
      rtems_filesystem_file_handlers_r  handlers;
  };
  ```

  A file control block can exist for regular files, devices and directories.
  The following fields are important for regular file and directory access:

  - Size - For a file this represents the number of bytes currently stored in a
    file. For a directory this field is not filled in.
  - Offset - For a file this is the byte file position index relative to the
    start of the file. For a directory this is the byte offset into a sequence
    of dirent structures.
  - Pathinfo - This is a structure that provides a pointer to node information,
    OPS table functions, Handler functions and the mount table entry associated
    with this node.
  - file_info - A pointer to node information that is used by Handler functions
  - handlers - A pointer to a table of handler functions that operate on a
    file, device or directory through a file descriptor index

### File/Directory function access via rtems_filesystem_location_info_t structure

The `rtems_filesystem_location_info_tt` structure below provides sufficient
information to process nodes under a mounted filesystem.

```c
struct rtems_filesystem_location_info_tt {
    void                                     *node_access;
    rtems_filesystem_file_handlers_r         *handlers;
    rtems_filesystem_operations_table        *ops;
    rtems_filesystem_mount_table_entry_t     *mt_entry;
};
```

It contains a void pointer to filesystem specific nodal structure, pointers to
the OPS table for the filesystem that contains the node, the node type specific
handlers for the node and a reference pointer to the mount table entry
associated with the filesystem containing the node

## Operation Tables

Filesystem specific operations are invoked indirectly. The set of routines
that implement the filesystem are configured into two tables. The Filesystem
Handler Table has routines that are specific to a filesystem but remain
constant regardless of the actual file type. The File Handler Table has
routines that are both filesystem and file type specific.

### Filesystem Handler Table Functions

OPS table functions are defined in a `rtems_filesystem_operations_table`
structure. It defines functions that are specific to a given filesystem. One
table exists for each filesystem that is supported in the RTEMS
configuration. The structure definition appears below and is followed by
general developmental information on each of the functions contained in this
function management structure.

```c
typedef struct {
    rtems_filesystem_evalpath_t        evalpath;
    rtems_filesystem_evalmake_t        evalformake;
    rtems_filesystem_link_t            link;
    rtems_filesystem_unlink_t          unlink;
    rtems_filesystem_node_type_t       node_type;
    rtems_filesystem_mknod_t           mknod;
    rtems_filesystem_rmnod_t           rmnod;
    rtems_filesystem_chown_t           chown;
    rtems_filesystem_freenode_t        freenod;
    rtems_filesystem_mount_t           mount;
    rtems_filesystem_fsmount_me_t      fsmount_me;
    rtems_filesystem_unmount_t         unmount;
    rtems_filesystem_fsunmount_me_t    fsunmount_me;
    rtems_filesystem_utime_t           utime;
    rtems_filesystem_evaluate_link_t   eval_link;
    rtems_filesystem_symlink_t         symlink;
} rtems_filesystem_operations_table;
```

#### evalpath Handler

Corresponding Structure Element:

: `evalpath`

Arguments:
: ```c
  const char                        *pathname,      /* IN     */
  int                                flags,         /* IN     */
  rtems_filesystem_location_info_t  *pathloc        /* IN/OUT */
  ```

Description:

: This routine is responsible for evaluating the pathname passed in based
  upon the flags and the valid `rthems_filesystem_location_info_t`.
  Additionally, it must make any changes to pathloc necessary to identify the
  pathname node. This should include calling the evalpath for a mounted
  filesystem, if the given filesystem supports the mount command.

  This routine returns a 0 if the evaluation was successful. Otherwise, it
  returns a -1 and sets errno to the correct error.

  This routine is required and should NOT be set to NULL.

#### evalformake Handler

Corresponding Structure Element:

: `evalformake`

Arguments:
: ```c
  const char                       *path,       /* IN */
  rtems_filesystem_location_info_t *pathloc,    /* IN/OUT */
  const char                      **name        /* OUT */
  ```

Description:

: This method is given a path to evaluate and a valid start location. It is
  responsible for finding the parent node for a requested make command,
  setting pathloc information to identify the parent node, and setting the
  name pointer to the first character of the name of the new node.
  Additionally, if the filesystem supports the mount command, this method
  should call the evalformake routine for the mounted filesystem.

  This routine returns a 0 if the evaluation was successful. Otherwise, it
  returns a -1 and sets errno to the correct error.

  This routine is required and should NOT be set to NULL. However, if the
  filesystem does not support user creation of a new node, it may set errno
  to ENOSYS and return -1.

#### link Handler

Corresponding Structure Element:

: `link`

Arguments:
: ```c
  rtems_filesystem_location_info_t    *to_loc,      /* IN */
  rtems_filesystem_location_info_t    *parent_loc,  /* IN */
  const char                          *token        /* IN */
  ```

Description:

: This routine is used to create a hard-link.

  It will first examine the st_nlink count of the node that we are trying to.
  If the link count exceeds LINK_MAX an error will be returned.

  The name of the link will be normalized to remove extraneous separators
  from the end of the name.

  This routine is not required and may be set to NULL.

#### unlink Handler

Corresponding Structure Element:

: `unlink`

Arguments:

: XXX

Description:

: XXX

#### node_type Handler

Corresponding Structure Element:

: `node_type()`

Arguments:
: ```c
  rtems_filesystem_location_info_t    *pathloc        /* IN */
  ```

Description:

: XXX

#### mknod Handler

Corresponding Structure Element:

: `mknod()`

Arguments:
: ```c
  const char                          *token,        /* IN */
  mode_t                               mode,         /* IN */
  dev_t                                dev,          /* IN */
  rtems_filesystem_location_info_t    *pathloc       /* IN/OUT */
  ```

Description:

: XXX

#### rmnod Handler

Corresponding Structure Element:

: `rmnod()`

Arguments:

: XXX

Description:

: XXX

#### chown Handler

Corresponding Structure Element:

: `chown()`

Arguments:
: ```c
  rtems_filesystem_location_info_t    *pathloc        /* IN */
  uid_t                                owner          /* IN */
  gid_t                                group          /* IN */
  ```

Description:

: XXX

#### freenod Handler

Corresponding Structure Element:

: `freenod()`

Arguments:
: ```c
  rtems_filesystem_location_info_t      *pathloc       /* IN */
  ```

Description:

: This routine is used by the generic code to allow memory to be allocated
  during the evaluate routines, and set free when the generic code is
  finished accessing a node. If the evaluate routines allocate memory to
  identify a node this routine should be utilized to free that memory.

  This routine is not required and may be set to NULL.

#### mount Handler

Corresponding Structure Element:

: `mount()`

Arguments:
: ```c
  rtems_filesystem_mount_table_entry_t   *mt_entry
  ```

Description:

: XXX

#### fsmount_me Handler

Corresponding Structure Element:

: `imfs_fsmount_me`

Arguments:
: ```c
  rtems_filesystem_mount_table_entry_t   *mt_entry
  ```

Description:

: This function is provided with a filesystem to take care of the internal
  filesystem management details associated with mounting that filesystem
  under the RTEMS environment.

  It is not responsible for the mounting details associated the filesystem
  containing the mount point.

  The rtems_filesystem_mount_table_entry_t structure contains the key
  elements below:

  ```c
  rtems_filesystem_location_info_t         *mt_point_node,
  ```

  This structure contains information about the mount point. This allows us
  to find the ops-table and the handling functions associated with the
  filesystem containing the mount point.

  ```c
  rtems_filesystem_location_info_t         *fs_root_node,
  ```

  This structure contains information about the root node in the file system
  to be mounted. It allows us to find the ops-table and the handling
  functions associated with the filesystem to be mounted.

  ```c

  ```

  rtems_filesystem_options_t options,

  Read only or read/write access

  ```c
  void                                         *fs_info,
  ```

  This points to an allocated block of memory the will be used to hold any
  filesystem specific information of a global nature. This allocated region
  if important because it allows us to mount the same filesystem type more
  than once under the RTEMS system. Each instance of the mounted filesystem
  has its own set of global management information that is separate from the
  global management information associated with the other instances of the
  mounted filesystem type.

  ```c
  rtems_filesystem_limits_and_options_t    pathconf_info,
  ```

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

  These values are accessed with the pathconf() and the fpathconf () functions.

  ```c
  const char                                   *dev
  ```

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
  table of path configuration constants (LIMITS_AND_OPTIONS).

  The fs_root_node structure will be filled in with the following:

  - pointer to the allocated root node of the filesystem
  - directory handlers for a directory node under the IMFS filesystem
  - OPS table functions for the IMFS

  A 0 will be returned to the calling routine if the process succeeded,
  otherwise a 1 will be returned.

#### unmount Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

#### fsunmount_me Handler

Corresponding Structure Element:

: `imfs_fsunmount_me()`

Arguments:
: ```c
  rtems_filesystem_mount_table_entry_t   *mt_entry
  ```

Description:

: XXX

#### utime Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

#### eval_link Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

#### symlink Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

### File Handler Table Functions

Handler table functions are defined in a `rtems_filesystem_file_handlers_r`
structure. It defines functions that are specific to a node type in a given
filesystem. One table exists for each of the filesystem's node types. The
structure definition appears below. It is followed by general developmental
information on each of the functions associated with regular files contained in
this function management structure.

```c
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
    rtems_filesystem_fcntl_t          fcntl;
} rtems_filesystem_file_handlers_r;
```

#### open Handler

Corresponding Structure Element:

: `open()`

Arguments:
: ```c
  rtems_libio_t   *iop,
  const char      *pathname,
  unsigned32       flag,
  unsigned32       mode
  ```

Description:

: XXX

##### close Handler

Corresponding Structure Element:

: `close()`

Arguments:
: ```c
  rtems_libio_t     *iop
  ```

Description:

: XXX

NOTES:

: XXX

##### read Handler

Corresponding Structure Element:

: `read()`

Arguments:
: ```c
  rtems_libio_t     *iop,
  void              *buffer,
  unsigned32         count
  ```

Description:

: XXX

NOTES:

: XXX

##### write Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

NOTES:

: XXX

##### ioctl Handler

Corresponding Structure Element:

: XXX

Arguments:
: ```c
  rtems_libio_t     *iop,
  unsigned32       command,
  void              *buffer
  ```

Description:

: XXX

NOTES:

: XXX

##### lseek Handler

Corresponding Structure Element:

: `lseek()`

Arguments:
: ```c
  rtems_libio_t     *iop,
  off_t              offset,
  int                whence
  ```

Description:

: XXX

NOTES:

: XXX

##### fstat Handler

Corresponding Structure Element:

: `fstat()`

Arguments:
: ```c
  rtems_filesystem_location_info_t   *loc,
  struct stat                        *buf
  ```

Description:

: The following information is extracted from the filesystem specific node
  and placed in the `stat` structure:

  - st_mode
  - st_nlink
  - st_ino
  - st_uid
  - st_gid
  - st_atime
  - st_mtime
  - st_ctime

NOTES:

: Both the `stat()` and `lstat()` services are implemented directly using
  the `fstat()` handler. The difference in behavior is determined by how
  the path is evaluated prior to this handler being called on a particular
  file entity.

  The `fstat()` system call is implemented directly on top of this
  filesystem handler.

##### fchmod Handler

Corresponding Structure Element:

: `fchmod()`

Arguments:
: ```c
  rtems_libio_t     *iop
  mode_t             mode
  ```

Description:

: XXX

NOTES:

: XXX

##### ftruncate Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

NOTES:

: XXX

##### fpathconf Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

NOTES:

: XXX

##### fsync Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

NOTES:

: XXX

##### fdatasync Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

NOTES:

: XXX

##### fcntl Handler

Corresponding Structure Element:

: XXX

Arguments:

: XXX

Description:

: XXX

NOTES:

: XXX
