Preface
#######

This document describes the implementation of the RTEMS filesystem
infrastructure.  This infrastructure supports the following
capabilities:

- Mountable file systems

- Hierarchical file system directory structure

- POSIX compliant set of routines for the manipulation of files and directories

- Individual file and directory support for the following:
  # Permissions for read, write and execute
  # User ID
  # Group ID
  # Access time
  # Modification time
  # Creation time

- Hard links to files and directories

- Symbolic links to files and directories

This has been implemented to provide the framework for a UNIX-like
file system support. POSIX file and directory functions have been
implemented that allow a standard method of accessing file, device and
directory information within file systems. The file system concept that
has been implemented allows for expansion and adaptation of the file
system to a variety of existing and future data storage devices. To this
end, file system mount and unmount capabilities have been included in this
RTEMS framework.

This framework slightly alters the manner in which devices are handled
under RTEMS from that of public release 4.0.0 and earlier.  Devices that
are defined under a given RTEMS configuration will now be registered as
files in a mounted file system.  Access to these device drivers and their
associated devices may now be performed through the traditional file system
open(), read(), write(), lseek(), fstat() and ioctl() functions in addition
to the interface provided by the IO Manager in the RTEMS Classic API.

An In-Memory File System (IMFS) is included which provides full POSIX
filesystem functionality yet is RAM based.  The IMFS maintains a
node structure for each file, device, and directory in each mounted
instantiation of its file system. The node structure is used to
manage ownership, access rights, access time, modification time,
and creation time.  A union of structures within the IMFS nodal
structure provide for manipulation of file data, device selection,
or directory content as required by the nodal type. Manipulation of
these properties is accomplished through the POSIX set of file and
directory functions.  In addition to being useful in its own right,
the IMFS serves as a full featured example filesystem.

The intended audience for this document is those persons implementing
their own filesystem.  Users of the filesystem may find information
on the implementation useful.  But the user interface to the filesystem
is through the ISO/ANSI C Library and POSIX 1003.1b file and directory
APIs.

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

