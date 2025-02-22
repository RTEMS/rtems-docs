% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# File and Directory Commands

## Introduction

The RTEMS shell has the following file and directory commands:

- [blksync] - sync the block driver
- [cat] - display file contents
- [cd] - alias for chdir
- [chdir] - change the current directory
- [chmod] - change permissions of a file
- [chroot] - change the root directory
- [cp] - copy files
- [dd] - convert and copy a file
- [debugrfs] - debug RFS file system
- [df] - display file system disk space usage
- [dir] - alias for [ls]
- [fdisk] - format disks
- [hexdump] - format disks
- [ln] - make links
- [ls] - list files in the directory
- [md5] - display file system disk space usage
- [mkdir] - create a directory
- [mkdos] - DOSFS disk format
- [mknod] - make device special file
- [mkrfs] - format RFS file system
- [mount] - mount disk
- [mv] - move files
- [pwd] - print work directory
- [rmdir] - remove empty directories
- [rm] - remove files
- [umask] - Set file mode creation mask
- [unmount] - unmount disk

## Commands

This section details the File and Directory Commands available. A subsection
is dedicated to each of the commands and describes the behavior and
configuration of that command as well as providing an example usage.

```{raw} latex
\clearpage
```

(blksync)=

### blksync - sync the block driver

```{index} blksync
```

SYNOPSYS:
: ```shell
  blksync driver
  ```

DESCRIPTION:

: This command issues a block driver sync call to the driver. The driver is a
  path to a device node. The sync call will flush all pending writes in the
  cache to the media and block until the writes have completed.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `blksync`:

  ```shell
  blksync /dev/hda1
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_BLKSYNC
```

```{index} CONFIGURE_SHELL_COMMAND_BLKSYNC
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_BLKSYNC` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_BLKSYNC` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_blksync
```

PROGRAMMING INFORMATION:

: The `blksync` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_blksync(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `blksync` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_BLKSYNC_Command;
  ```

```{raw} latex
\clearpage
```

(cat)=

### cat - display file contents

```{index} cat
```

SYNOPSYS:
: ```shell
  cat file1 [file2 .. fileN]
  ```

DESCRIPTION:

: This command displays the contents of the specified files.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: It is possible to read the input from a device file using `cat`.

EXAMPLES:

: The following is an example of how to use `cat`:

  ```shell
  SHLL [/] # cat /etc/passwd
  root:*:0:0:root::/:/bin/sh
  rtems:*:1:1:RTEMS Application::/:/bin/sh
  tty:!:2:2:tty owner::/:/bin/false
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_CAT
```

```{index} CONFIGURE_SHELL_COMMAND_CAT
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_CAT` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_CAT` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_cat
```

PROGRAMMING INFORMATION:

: The `cat` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_rtems_main_cat(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `cat` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_CAT_Command;
  ```

```{raw} latex
\clearpage
```

(cd)=

### cd - alias for chdir

```{index} cd
```

SYNOPSYS:
: ```shell
  cd directory
  ```

DESCRIPTION:

: This command is an alias or alternate name for the `chdir`. See `ls -
  list files in the directory` for more information.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `cd`:

  ```shell
  SHLL [/] $ cd etc
  SHLL [/etc] $ cd /
  SHLL [/] $ cd /etc
  SHLL [/etc] $ pwd
  /etc
  SHLL [/etc] $ cd /
  SHLL [/] $ pwd
  /
  SHLL [/] $ cd etc
  SHLL [/etc] $ cd ..
  SHLL [/] $ pwd
  /
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_CD
```

```{index} CONFIGURE_SHELL_COMMAND_CD
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_CD` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_CD` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_cd
```

PROGRAMMING INFORMATION:

: The `cd` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_rtems_main_cd(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `cd` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_CD_Command;
  ```

```{raw} latex
\clearpage
```

(chdir)=

### chdir - change the current directory

```{index} chdir
```

SYNOPSYS:
: ```shell
  chdir [dir]
  ```

DESCRIPTION:

: This command is used to change the current working directory to the
  specified directory. If no arguments are given, the current working
  directory will be changed to `/`.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `chdir`:

  ```shell
  SHLL [/] $ pwd
  /
  SHLL [/] $ chdir etc
  SHLL [/etc] $ pwd
  /etc
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_CHDIR
```

```{index} CONFIGURE_SHELL_COMMAND_CHDIR
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_CHDIR` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_CHDIR` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_chdir
```

PROGRAMMING INFORMATION:

: The `chdir` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_chdir(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `chdir` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_CHDIR_Command;
  ```

```{raw} latex
\clearpage
```

(chmod)=

### chmod - change permissions of a file

```{index} chmod
```

SYNOPSYS:
: ```shell
  chmod permissions file1 [file2...]
  ```

DESCRIPTION:

: This command changes the permissions on the files specified to the
  indicated `permissions`. The permission values are POSIX based with
  owner, group, and world having individual read, write, and executive
  permission bits.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: The `chmod` command only takes numeric representations of the
  permissions.

EXAMPLES:

: The following is an example of how to use `chmod`:

  ```shell
  SHLL [/] # cd etc
  SHLL [/etc] # ls
  -rw-r--r--   1   root   root         102 Jan 01 00:00 passwd
  -rw-r--r--   1   root   root          42 Jan 01 00:00 group
  -rw-r--r--   1   root   root          30 Jan 01 00:00 issue
  -rw-r--r--   1   root   root          28 Jan 01 00:00 issue.net
  4 files 202 bytes occupied
  SHLL [/etc] # chmod 0777 passwd
  SHLL [/etc] # ls
  -rwxrwxrwx   1   root   root         102 Jan 01 00:00 passwd
  -rw-r--r--   1   root   root          42 Jan 01 00:00 group
  -rw-r--r--   1   root   root          30 Jan 01 00:00 issue
  -rw-r--r--   1   root   root          28 Jan 01 00:00 issue.net
  4 files 202 bytes occupied
  SHLL [/etc] # chmod 0322 passwd
  SHLL [/etc] # ls
  --wx-w--w-   1 nouser   root         102 Jan 01 00:00 passwd
  -rw-r--r--   1 nouser   root          42 Jan 01 00:00 group
  -rw-r--r--   1 nouser   root          30 Jan 01 00:00 issue
  -rw-r--r--   1 nouser   root          28 Jan 01 00:00 issue.net
  4 files 202 bytes occupied
  SHLL [/etc] # chmod 0644 passwd
  SHLL [/etc] # ls
  -rw-r--r--   1   root   root         102 Jan 01 00:00 passwd
  -rw-r--r--   1   root   root          42 Jan 01 00:00 group
  -rw-r--r--   1   root   root          30 Jan 01 00:00 issue
  -rw-r--r--   1   root   root          28 Jan 01 00:00 issue.net
  4 files 202 bytes occupied
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_CHMOD
```

```{index} CONFIGURE_SHELL_COMMAND_CHMOD
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_CHMOD` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_CHMOD` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_chmod
```

PROGRAMMING INFORMATION:

: The `chmod` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_chmod(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `chmod` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_CHMOD_Command;
  ```

```{raw} latex
\clearpage
```

(chroot)=

### chroot - change the root directory

```{index} chroot
```

SYNOPSYS:
: ```shell
  chroot [dir]
  ```

DESCRIPTION:

: This command changes the root directory to `dir` for subsequent commands.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

  The destination directory `dir` must exist.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `chroot` and the impact it has
  on the environment for subsequent command invocations:

  ```shell
  SHLL [/] $ cat passwd
  cat: passwd: No such file or directory
  SHLL [/] $ chroot etc
  SHLL [/] $ cat passwd
  root:*:0:0:root::/:/bin/sh
  rtems:*:1:1:RTEMS Application::/:/bin/sh
  tty:!:2:2:tty owner::/:/bin/false
  SHLL [/] $ cat /etc/passwd
  cat: /etc/passwd: No such file or directory
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_CHROOT
```

```{index} CONFIGURE_SHELL_COMMAND_CHROOT
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_CHROOT` to have this
  command included. Additional to that you have to add one POSIX key value
  pair for each thread where you want to use the command.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_CHROOT` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_chroot
```

PROGRAMMING INFORMATION:

: The `chroot` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_chroot(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `chroot` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_CHROOT_Command;
  ```

```{raw} latex
\clearpage
```

(cp)=

### cp - copy files

```{index} cp
```

SYNOPSYS:
: ```shell
  cp [-R [-H | -L | -P]] [-f | -i] [-pv] src target
  cp [-R [-H | -L] ] [-f | -i] [-NpPv] source_file ... target_directory
  ```

DESCRIPTION:

: In the first synopsis form, the cp utility copies the contents of the
  source_file to the target_file. In the second synopsis form, the contents
  of each named source_file is copied to the destination
  target_directory. The names of the files themselves are not changed. If cp
  detects an attempt to copy a file to itself, the copy will fail.

  The following options are available:

  *-f*

  : For each existing destination pathname, attempt to overwrite it. If
    permissions do not allow copy to succeed, remove it and create a new
    file, without prompting for confirmation. (The -i option is ignored if
    the -f option is specified.)

  *-H*

  : If the -R option is specified, symbolic links on the command line are
    followed. (Symbolic links encountered in the tree traversal are not
    followed.)

  *-i*

  : Causes cp to write a prompt to the standard error output before copying
    a file that would overwrite an existing file. If the response from the
    standard input begins with the character 'y', the file copy is
    attempted.

  *-L*

  : If the -R option is specified, all symbolic links are followed.

  *-N*

  : When used with -p, do not copy file flags.

  *-P*

  : No symbolic links are followed.

  *-p*

  : Causes cp to preserve in the copy as many of the modification time,
    access time, file flags, file mode, user ID, and group ID as allowed by
    permissions. If the user ID and group ID cannot be preserved, no error
    message is displayed and the exit value is not altered. If the source
    file has its set user ID bit on and the user ID cannot be preserved,
    the set user ID bit is not preserved in the copy's permissions. If the
    source file has its set group ID bit on and the group ID cannot be
    preserved, the set group ID bit is not preserved in the copy's
    permissions. If the source file has both its set user ID and set group
    ID bits on, and either the user ID or group ID cannot be preserved,
    neither the set user ID or set group ID bits are preserved in the
    copy's permissions.

  *-R*

  : If source_file designates a directory, cp copies the directory and the
    entire subtree connected at that point. This option also causes
    symbolic links to be copied, rather than indirected through, and for cp
    to create special files rather than copying them as normal
    files. Created directories have the same mode as the corresponding
    source directory, unmodified by the process's umask.

  *-v*

  : Cause cp to be verbose, showing files as they are copied.

  For each destination file that already exists, its contents are overwritten
  if permissions allow, but its mode, user ID, and group ID are unchanged.

  In the second synopsis form, target_directory must exist unless there is
  only one named source_file which is a directory and the -R flag is
  specified.

  If the destination file does not exist, the mode of the source file is used
  as modified by the file mode creation mask (umask, see csh(1)). If the
  source file has its set user ID bit on, that bit is removed unless both the
  source file and the destination file are owned by the same user. If the
  source file has its set group ID bit on, that bit is removed unless both
  the source file and the destination file are in the same group and the user
  is a member of that group. If both the set user ID and set group ID bits
  are set, all of the above conditions must be fulfilled or both bits are
  removed.

  Appropriate permissions are required for file creation or overwriting.

  Symbolic links are always followed unless the -R flag is set, in which case
  symbolic links are not followed, by default. The -H or -L flags (in
  conjunction with the -R flag), as well as the -P flag cause symbolic links
  to be followed as described above. The -H and -L options are ignored unless
  the -R option is specified. In addition, these options override
  eachsubhedading other and the command's actions are determined by the last
  one specified.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: NONE

EXAMPLES:

: The following is an example of how to use `cp` to copy a file to a new
  name in the current directory:

  ```shell
  SHLL [/] # cat joel
  cat: joel: No such file or directory
  SHLL [/] # cp etc/passwd joel
  SHLL [/] # cat joel
  root:*:0:0:root::/:/bin/sh
  rtems:*:1:1:RTEMS Application::/:/bin/sh
  tty:!:2:2:tty owner::/:/bin/false
  SHLL [/] # ls
  drwxr-xr-x   1   root   root         536 Jan 01 00:00 dev/
  drwxr-xr-x   1   root   root        1072 Jan 01 00:00 etc/
  -rw-r--r--   1   root   root         102 Jan 01 00:00 joel
  3 files 1710 bytes occupied
  ```

  The following is an example of how to use `cp` to copy one or more files
  to a destination directory and use the same `basename` in the destination
  directory:

  ```shell
  SHLL [/] # mkdir tmp
  SHLL [/] # ls tmp
  0 files 0 bytes occupied
  SHLL [/] # cp /etc/passwd tmp
  SHLL [/] # ls /tmp
  -rw-r--r--   1   root   root         102 Jan 01 00:01 passwd
  1 files 102 bytes occupied
  SHLL [/] # cp /etc/passwd /etc/group /tmp
  SHLL [/] # ls /tmp
  -rw-r--r--   1   root   root         102 Jan 01 00:01 passwd
  -rw-r--r--   1   root   root          42 Jan 01 00:01 group
  2 files 144 bytes occupied
  SHLL [/] #
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_CP
```

```{index} CONFIGURE_SHELL_COMMAND_CP
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define\`\`CONFIGURE_SHELL_COMMAND_CP\`\` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_CP` when all shell commands have been
  configured.

```{index} rtems_shell_main_cp
```

PROGRAMMING INFORMATION:

: The `cp` command is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_main_cp(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `cp` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_CP_Command;
  ```

ORIGIN:

: The implementation and portions of the documentation for this command are
  from NetBSD 4.0.

```{raw} latex
\clearpage
```

(dd)=

### dd - convert and copy a file

```{index} dd
```

SYNOPSYS:
: ```shell
  dd [operands ...]
  ```

DESCRIPTION:

: The dd utility copies the standard input to the standard output. Input
  data is read and written in 512-byte blocks. If input reads are short,
  input from multiple reads are aggregated to form the output block. When
  finished, dd displays the number of complete and partial input and output
  blocks and truncated input records to the standard error output.

  The following operands are available:

  *bs=n*

  : Set both input and output block size, superseding the ibs and obs
    operands. If no conversion values other than noerror, notrunc or sync
    are specified, then each input block is copied to the output as a
    single block without any aggregation of short blocks.

  *cbs=n*

  : Set the conversion record size to n bytes. The conversion record size
    is required by the record oriented conversion values.

  *count=n*

  : Copy only n input blocks.

  *files=n*

  : Copy n input files before terminating. This operand is only applicable
    when the input device is a tape.

  *ibs=n*

  : Set the input block size to n bytes instead of the default 512.

  *if=file*

  : Read input from file instead of the standard input.

  *obs=n*

  : Set the output block size to n bytes instead of the default 512.

  *of=file*

  : Write output to file instead of the standard output. Any regular
    output file is truncated unless the notrunc conversion value is
    specified. If an initial portion of the output file is skipped (see
    the seek operand) the output file is truncated at that point.

  *seek=n*

  : Seek n blocks from the beginning of the output before copying. On
    non-tape devices, a *lseek* operation is used. Otherwise, existing
    blocks are read and the data discarded. If the seek operation is past
    the end of file, space from the current end of file to the specified
    offset is filled with blocks of NUL bytes.

  *skip=n*

  : Skip n blocks from the beginning of the input before copying. On input
    which supports seeks, a *lseek* operation is used. Otherwise, input
    data is read and discarded. For pipes, the correct number of bytes is
    read. For all other devices, the correct number of blocks is read
    without distinguishing between a partial or complete block being read.

  *progress=n*

  : Switch on display of progress if n is set to any non-zero value. This
    will cause a "." to be printed (to the standard error output) for every
    n full or partial blocks written to the output file.

  *conv=value[,value...]*

  : Where value is one of the symbols from the following list.

    *ascii, oldascii*

    : The same as the unblock value except that characters are translated
      from EBCDIC to ASCII before the records are converted. (These
      values imply unblock if the operand cbs is also specified.) There
      are two conversion maps for ASCII. The value ascii specifies the
      recom- mended one which is compatible with AT&T System V UNIX. The
      value oldascii specifies the one used in historic AT&T and pre
      4.3BSD-Reno systems.

    *block*

    : Treats the input as a sequence of newline or end-of-file terminated
      variable length records independent of input and output block
      boundaries. Any trailing newline character is discarded. Each
      input record is converted to a fixed length output record where the
      length is specified by the cbs operand. Input records shorter than
      the conversion record size are padded with spaces. Input records
      longer than the conversion record size are truncated. The number
      of truncated input records, if any, are reported to the standard
      error output at the completion of the copy.

    *ebcdic, ibm, oldebcdic, oldibm*

    : The same as the block value except that characters are translated
      from ASCII to EBCDIC after the records are converted. (These
      values imply block if the operand cbs is also specified.) There
      are four conversion maps for EBCDIC. The value ebcdic specifies
      the recommended one which is compatible with AT&T System V UNIX.
      The value ibm is a slightly different mapping, which is compatible
      with the AT&T System V UNIX ibm value. The values oldebcdic and
      oldibm are maps used in historic AT&T and pre 4.3BSD-Reno systems.

    *lcase*

    : Transform uppercase characters into lowercase characters.

    *noerror*

    : Do not stop processing on an input error. When an input error
      occurs, a diagnostic message followed by the current input and
      output block counts will be written to the standard error output in
      the same format as the standard completion message. If the sync
      conversion is also specified, any missing input data will be
      replaced with NUL bytes (or with spaces if a block oriented
      conversion value was specified) and processed as a normal input
      buffer. If the sync conversion is not specified, the input block
      is omitted from the output. On input files which are not tapes or
      pipes, the file offset will be positioned past the block in which
      the error occurred using lseek(2).

    *notrunc*

    : Do not truncate the output file. This will preserve any blocks in
      the output file not explicitly written by dd. The notrunc value is
      not supported for tapes.

    *osync*

    : Pad the final output block to the full output block size. If the
      input file is not a multiple of the output block size after
      conversion, this conversion forces the final output block to be the
      same size as preceding blocks for use on devices that require
      regularly sized blocks to be written. This option is incompatible
      with use of the bs=n block size specification.

    *sparse*

    : If one or more non-final output blocks would consist solely of NUL
      bytes, try to seek the output file by the required space instead of
      filling them with NULs. This results in a sparse file on some file
      systems.

    *swab*

    : Swap every pair of input bytes. If an input buffer has an odd
      number of bytes, the last byte will be ignored during swapping.

    *sync*

    : Pad every input block to the input buffer size. Spaces are used
      for pad bytes if a block oriented conversion value is specified,
      otherwise NUL bytes are used.

    *ucase*

    : Transform lowercase characters into uppercase characters.

    *unblock*

    : Treats the input as a sequence of fixed length records independent
      of input and output block boundaries. The length of the input
      records is specified by the cbs operand. Any trailing space
      characters are discarded and a newline character is appended.

  Where sizes are specified, a decimal number of bytes is expected. Two or
  more numbers may be separated by an "x" to indicate a product. Each number
  may have one of the following optional suffixes:

  *b*

  : Block; multiply by 512

  *k*

  : Kibi; multiply by 1024 (1 KiB)

  *m*

  : Mebi; multiply by 1048576 (1 MiB)

  *g*

  : Gibi; multiply by 1073741824 (1 GiB)

  *t*

  : Tebi; multiply by 1099511627776 (1 TiB)

  *w*

  : Word; multiply by the number of bytes in an integer

  When finished, dd displays the number of complete and partial input and
  output blocks, truncated input records and odd-length byte-swapping ritten.
  Partial output blocks to tape devices are considered fatal errors.
  Otherwise, the rest of the block will be written. Partial output blocks to
  character devices will produce a warning message. A truncated input block
  is one where a variable length record oriented conversion value was
  specified and the input line was too long to fit in the conversion record
  or was not newline terminated.

  Normally, data resulting from input or conversion or both are aggregated
  into output blocks of the specified size. After the end of input is
  reached, any remaining output is written as a block. This means that the
  final output block may be shorter than the output block size.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: NONE

EXAMPLES:

: The following is an example of how to use `dd`:

  ```shell
  SHLL [/] $ dd if=/nfs/boot-image of=/dev/hda1
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_DD
```

```{index} CONFIGURE_SHELL_COMMAND_DD
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_DD` to have this
  command included.

  This command can be excluded from the shell command set by
  defining\`\`CONFIGURE_SHELL_NO_COMMAND_DD\`\` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_dd
```

PROGRAMMING INFORMATION:

: The `dd` command is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_dd(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `dd` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_DD_Command;
  ```

```{raw} latex
\clearpage
```

(debugrfs)=

### debugrfs - debug RFS file system

```{index} debugrfs
```

SYNOPSYS:
: ```shell
  debugrfs [-hl] path command [options]
  ```

DESCRIPTION:

: The command provides debugging information for the RFS file system.

  The options are:

  *-h*

  : Print a help message.

  *-l*

  : List the commands.

  *path*

  : Path to the mounted RFS file system. The file system has to be mounted
    to view to use this command.

  The commands are:

  *block start [end]*

  : Display the contents of the blocks from start to end.

  *data*

  : Display the file system data and configuration.

  *dir bno*

  : Process the block as a directory displaying the entries.

  *group start [end]*

  : Display the group data from the start group to the end group.

  *inode [-aef] [start] [end]*

  : Display the inodes between start and end. If no start and end is
    provides all inodes are displayed.

    *-a*

    : Display all inodes. That is allocated and unallocated inodes.

    *-e*

    : Search and display on inodes that have an error.

    *-f*

    : Force display of inodes, even when in error.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: NONE

EXAMPLES:

: The following is an example of how to use `debugrfs`:

  ```shell
  SHLL [/] $ debugrfs /c data
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_DEBUGRFS
```

```{index} CONFIGURE_SHELL_COMMAND_DEBUGRFS
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_DEBUGRFS` to have
  this command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_DEBUGRFS` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_debugrfs
```

PROGRAMMING INFORMATION:

: The `debugrfs` command is implemented by a C language function which has
  the following prototype:

  ```c
  int rtems_shell_rtems_main_debugrfs(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for `debugrfs` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_DEBUGRFS_Command;
  ```

```{raw} latex
\clearpage
```

(df)=

### df - display file system disk space usage

```{index} df
```

SYNOPSYS:
: ```shell
  df [-h] [-B block_size]
  ```

DESCRIPTION:

: This command print disk space usage for mounted file systems.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: NONE

EXAMPLES:

: The following is an example of how to use `df`:

  ```shell
  SHLL [/] $ df -B 4K
  Filesystem     4K-blocks        Used   Available       Use%     Mounted on
  /dev/rda               124         1         124         0%   /mnt/ramdisk
  SHLL [/] $ df
  Filesystem     1K-blocks        Used   Available       Use%     Mounted on
  /dev/rda               495         1         494         0%   /mnt/ramdisk
  SHLL [/] $ df -h
  Filesystem     Size             Used   Available       Use%     Mounted on
  /dev/rda              495K        1K        494K         0%   /mnt/ramdisk
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_DF
```

```{index} CONFIGURE_SHELL_COMMAND_DF
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_DF` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_DF` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_df
```

PROGRAMMING INFORMATION:

: The `df` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_main_df(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `df` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_DF_Command;
  ```

```{raw} latex
\clearpage
```

(dir)=

### dir - alias for ls

```{index} dir
```

SYNOPSYS:
: ```shell
  dir [dir]
  ```

DESCRIPTION:

: This command is an alias or alternate name for the `ls`. See `ls - list
  files in the directory` for more information.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: NONE

EXAMPLES:

: The following is an example of how to use `dir`:

  ```shell
  SHLL [/] $ dir
  drwxr-xr-x   1   root   root         536 Jan 01 00:00 dev/
  drwxr-xr-x   1   root   root        1072 Jan 01 00:00 etc/
  2 files 1608 bytes occupied
  SHLL [/] $ dir etc
  -rw-r--r--   1   root   root         102 Jan 01 00:00 passwd
  -rw-r--r--   1   root   root          42 Jan 01 00:00 group
  -rw-r--r--   1   root   root          30 Jan 01 00:00 issue
  -rw-r--r--   1   root   root          28 Jan 01 00:00 issue.net
  4 files 202 bytes occupied
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_DIR
```

```{index} CONFIGURE_SHELL_COMMAND_DIR
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define\`\`CONFIGURE_SHELL_COMMAND_DIR\`\` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_DIR` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_dir
```

PROGRAMMING INFORMATION:

: The `dir` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_rtems_main_dir(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `dir` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_DIR_Command;
  ```

```{raw} latex
\clearpage
```

(fdisk)=

### fdisk - format disk

```{index} fdisk
```

SYNOPSYS:
: ```shell
  fdisk
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_FDISK
```

```{index} CONFIGURE_SHELL_COMMAND_FDISK
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_FDISK` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_FDISK` when all shell commands have been
  configured.

```{raw} latex
\clearpage
```

(hexdump)=

### hexdump - ascii/dec/hex/octal dump

```{index} hexdump
```

SYNOPSYS:
: ```shell
  hexdump [-bcCdovx] [-e format_string] [-f format_file] [-n length] [-s skip] file ...
  ```

DESCRIPTION:

: The hexdump utility is a filter which displays the specified files, or the
  standard input, if no files are specified, in a user specified format.

  The options are as follows:

  *-b*

  : One-byte octal display. Display the input offset in hexadecimal,
    followed by sixteen space-separated, three column, zero-filled, bytes
    of input data, in octal, per line.

  *-c*

  : One-byte character display. Display the input offset in hexadecimal,
    followed by sixteen space-separated, three column, space-filled,
    characters of input data per line.

  *-C*

  : Canonical hex+ASCII display. Display the input offset in hexadecimal,
    followed by sixteen space-separated, two column, hexadecimal bytes,
    followed by the same sixteen bytes in %\_p format enclosed in "|"
    characters.

  *-d*

  : Two-byte decimal display. Display the input offset in hexadecimal,
    followed by eight space-separated, five column, zero-filled, two-byte
    units of input data, in unsigned decimal, per line.

  *-e format_string*

  : Specify a format string to be used for displaying data.

  *-f format_file*

  : Specify a file that contains one or more newline separated format
    strings. Empty lines and lines whose first non-blank character is a
    hash mark (#) are ignored.

  *-n length*

  : Interpret only length bytes of input.

  *-o*

  : Two-byte octal display. Display the input offset in hexadecimal,
    followed by eight space-separated, six column, zerofilled, two byte
    quantities of input data, in octal, per line.

  *-s offset*

  : Skip offset bytes from the beginning of the input. By default, offset
    is interpreted as a decimal number. With a leading 0x or 0X, offset is
    interpreted as a hexadecimal number, otherwise, with a leading 0,
    offset is interpreted as an octal number. Appending the character b,
    k, or m to offset causes it to be interpreted as a multiple of 512,
    1024, or 1048576, respectively.

  *-v*

  : The -v option causes hexdump to display all input data. Without the -v
    option, any number of groups of output lines, which would be identical
    to the immediately preceding group of output lines (except for the
    input offsets), are replaced with a line containing a single asterisk.

  *-x*

  : Two-byte hexadecimal display. Display the input offset in hexadecimal,
    followed by eight, space separated, four column, zero-filled, two-byte
    quantities of input data, in hexadecimal, per line.

  For each input file, hexdump sequentially copies the input to standard
  output, transforming the data according to the format strings specified by
  the -e and -f options, in the order that they were specified.

  *Formats*

  A format string contains any number of format units, separated by
  whitespace. A format unit contains up to three items: an iteration count,
  a byte count, and a format.

  The iteration count is an optional positive integer, which defaults to one.
  Each format is applied iteration count times.

  The byte count is an optional positive integer. If specified it defines
  the number of bytes to be interpreted by each iteration of the format.

  If an iteration count and/or a byte count is specified, a single slash must
  be placed after the iteration count and/or before the byte count to
  disambiguate them. Any whitespace before or after the slash is ignored.

  The format is required and must be surrounded by double quote (" ") marks.
  It is interpreted as a fprintf-style format string (see\*fprintf\*), with the
  following exceptions:

  - An asterisk (\*) may not be used as a field width or precision.

  - A byte count or field precision is required for each "s" con- version
    character (unlike the fprintf(3) default which prints the entire string
    if the precision is unspecified).

  - The conversion characters "h", "l", "n", "p" and "q" are not supported.

  - The single character escape sequences described in the C standard are
    supported:

    > NUL 0
    > \<alert character> a
    > \<backspace> b
    > \<form-feed> f
    > \<newline> n
    > \<carriage return> r
    > \<tab> t
    > \<vertical tab> v

  Hexdump also supports the following additional conversion strings:

  *\_a[dox]*

  : Display the input offset, cumulative across input files, of the next
    byte to be displayed. The appended characters d, o, and x specify the
    display base as decimal, octal or hexadecimal respectively.

  *\_A[dox]*

  : Identical to the \_a conversion string except that it is only performed
    once, when all of the input data has been processed.

  *\_c*

  : Output characters in the default character set. Nonprinting characters
    are displayed in three character, zero-padded octal, except for those
    representable by standard escape notation (see above), which are
    displayed as two character strings.

  *\_p*

  : Output characters in the default character set. Nonprinting characters
    are displayed as a single ".".

  *\_u*

  : Output US ASCII characters, with the exception that control characters
    are displayed using the following, lower-case, names. Characters
    greater than 0xff, hexadecimal, are displayed as hexadecimal strings.

    ```{eval-rst}
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |``000`` nul|``001`` soh|``002`` stx|``003`` etx|``004`` eot|``005`` enq|
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |``006`` ack|``007`` bel|``008`` bs |``009`` ht |``00A`` lf |``00B`` vt |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |``00C`` ff |``00D`` cr |``00E`` so |``00F`` si |``010`` dle|``011`` dc1|
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |``012`` dc2|``013`` dc3|``014`` dc4|``015`` nak|``016`` syn|``017`` etb|
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |``018`` can|``019`` em |``01A`` sub|``01B`` esc|``01C`` fs |``01D`` gs |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |``01E`` rs |``01F`` us |``07F`` del|           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    ```

  The default and supported byte counts for the conversion characters are as
  follows:

  > ```{eval-rst}
  > +----------------------+---------------------------------+
  > |%_c, %_p, %_u, %c     |One byte counts only.            |
  > +----------------------+---------------------------------+
  > |%d, %i, %o, %u, %X, %x|Four byte default, one, two, four|
  > |                      |and eight byte counts supported. |
  > +----------------------+---------------------------------+
  > |%E, %e, %f, %G, %g    |Eight byte default, four byte    |
  > |                      |counts supported.                |
  > +----------------------+---------------------------------+
  > ```

  The amount of data interpreted by each format string is the sum of the data
  required by each format unit, which is the iteration count times the byte
  count, or the iteration count times the number of bytes required by the
  format if the byte count is not specified.

  The input is manipulated in "blocks", where a block is defined as the
  largest amount of data specified by any format string. Format strings
  interpreting less than an input block's worth of data, whose last format
  unit both interprets some number of bytes and does not have a specified
  iteration count, have the iteration count incremented until the entire
  input block has been processed or there is not enough data remaining in the
  block to satisfy the format string.

  If, either as a result of user specification or hexdump modifying the
  iteration count as described above, an iteration count is greater than one,
  no trailing whitespace characters are output during the last iteration.

  It is an error to specify a byte count as well as multiple conversion
  characters or strings unless all but one of the conversion characters or
  strings is \_a or \_A.

  If, as a result of the specification of the -n option or end-of-file being
  reached, input data only partially satisfies a format string, the input
  block is zero-padded sufficiently to display all available data (i.e. any
  format units overlapping the end of data will display some num- ber of the
  zero bytes).

  Further output by such format strings is replaced by an equivalent number
  of spaces. An equivalent number of spaces is defined as the number of
  spaces output by an s conversion character with the same field width and
  precision as the original conversion character or conversion string but
  with any "+", " ", "#" conversion flag characters removed, and ref-
  erencing a NULL string.

  If no format strings are specified, the default display is equivalent to
  specifying the -x option.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: NONE

EXAMPLES:

: The following is an example of how to use `hexdump`:

  ```shell
  SHLL [/] $ hexdump -C -n 512 /dev/hda1
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_HEXDUMP
```

```{index} CONFIGURE_SHELL_COMMAND_HEXDUMP
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_HEXDUMP` to have this
  command included.

  This command can be excluded from the shell command set by
  defining\`\`CONFIGURE_SHELL_NO_COMMAND_HEXDUMP\`\` when all shell commands have
  been configured.

```{index} rtems_shell_rtems_main_hexdump
```

PROGRAMMING INFORMATION:

: The `hexdump` command is implemented by a C language function which has
  the following prototype:

  ```c
  int rtems_shell_rtems_main_hexdump(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `hexdump` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_HEXDUMP_Command;
  ```

```{raw} latex
\clearpage
```

(ln)=

### ln - make links

```{index} ln
```

SYNOPSYS:
: ```shell
  ln [-fhinsv] source_file [target_file]
  ln [-fhinsv] source_file ... target_dir
  ```

DESCRIPTION:

: The ln utility creates a new directory entry (linked file) which has the
  same modes as the original file. It is useful for maintaining multiple
  copies of a file in many places at once without using up storage for the
  "copies"; instead, a link "points" to the original copy. There are two
  types of links; hard links and symbolic links. How a link "points" to a
  file is one of the differences between a hard or symbolic link.

  The options are as follows:

  *-f*

  : Unlink any already existing file, permitting the link to occur.

  *-h*

  : If the target_file or target_dir is a symbolic link, do not follow it.
    This is most useful with the -f option, to replace a symlink which may
    point to a directory.

  *-i*

  : Cause ln to write a prompt to standard error if the target file exists.
    If the response from the standard input begins with the character 'y'
    or 'Y', then unlink the target file so that the link may occur.
    Otherwise, do not attempt the link. (The -i option overrides any
    previous -f options.)

  *-n*

  : Same as -h, for compatibility with other ln implementations.

  *-s*

  : Create a symbolic link.

  *-v*

  : Cause ln to be verbose, showing files as they are processed.

  By default ln makes hard links. A hard link to a file is indistinguishable
  from the original directory entry; any changes to a file are effective
  independent of the name used to reference the file. Hard links may not
  normally refer to directories and may not span file systems.

  A symbolic link contains the name of the file to which it is linked. The
  referenced file is used when an *open* operation is performed on the link.
  A *stat* on a symbolic link will return the linked-to file; an *lstat* must
  be done to obtain information about the link. The *readlink* call may be
  used to read the contents of a symbolic link. Symbolic links may span file
  systems and may refer to directories.

  Given one or two arguments, ln creates a link to an existing file
  source_file. If target_file is given, the link has that name; target_file
  may also be a directory in which to place the link; otherwise it is placed
  in the current directory. If only the directory is specified, the link
  will be made to the last component of source_file.

  Given more than two arguments, ln makes links in target_dir to all the
  named source files. The links made will have the same name as the files
  being linked to.

EXIT STATUS:

: The `ln` utility exits 0 on success, and >0 if an error occurs.

NOTES:

: None.

EXAMPLES:
: ```shell
  SHLL [/] ln -s /dev/console /dev/con1
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_LN
```

```{index} CONFIGURE_SHELL_COMMAND_LN
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_LN` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_LN` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_ln
```

PROGRAMMING INFORMATION:

: The `ln` command is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_ln(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `ln` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_LN_Command;
  ```

ORIGIN:

: The implementation and portions of the documentation for this command are
  from NetBSD 4.0.

```{raw} latex
\clearpage
```

(ls)=

### ls - list files in the directory

```{index} ls
```

SYNOPSYS:
: ```shell
  ls [dir]
  ```

DESCRIPTION:

: This command displays the contents of the specified directory. If no
  arguments are given, then it displays the contents of the current working
  directory.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: This command currently does not display information on a set of files like
  the POSIX ls(1). It only displays the contents of entire directories.

EXAMPLES:

: The following is an example of how to use `ls`:

  ```shell
  SHLL [/] $ ls
  drwxr-xr-x   1   root   root         536 Jan 01 00:00 dev/
  drwxr-xr-x   1   root   root        1072 Jan 01 00:00 etc/
  2 files 1608 bytes occupied
  SHLL [/] $ ls etc
  -rw-r--r--   1   root   root         102 Jan 01 00:00 passwd
  -rw-r--r--   1   root   root          42 Jan 01 00:00 group
  -rw-r--r--   1   root   root          30 Jan 01 00:00 issue
  -rw-r--r--   1   root   root          28 Jan 01 00:00 issue.net
  4 files 202 bytes occupied
  SHLL [/] $ ls dev etc
  -rwxr-xr-x   1  rtems   root           0 Jan 01 00:00 console
  -rwxr-xr-x   1   root   root           0 Jan 01 00:00 console_b
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_LS
```

```{index} CONFIGURE_SHELL_COMMAND_LS
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_LS` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_LS` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_ls
```

PROGRAMMING INFORMATION:

: The `ls` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_rtems_main_ls(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `ls` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_LS_Command;
  ```

```{raw} latex
\clearpage
```

(md5)=

### md5 - compute the Md5 hash of a file or list of files

```{index} md5
```

SYNOPSYS:
: ```shell
  md5 <files>
  ```

DESCRIPTION:

: This command prints the MD5 of a file. You can provide one or more files on
  the command line and a hash for each file is printed in a single line of
  output.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `md5`:

  ```shell
  SHLL [/] $ md5 shell-init
  MD5 (shell-init) = 43b4d2e71b47db79eae679a2efeacf31
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_MD5
```

```{index} CONFIGURE_SHELL_COMMAND_MD5
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define\`\`CONFIGURE_SHELL_COMMAND_MD5\`\` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MD5` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_md5
```

PROGRAMMING INFORMATION:

: The `md5` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_main_md5(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `md5` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MD5_Command;
  ```

```{raw} latex
\clearpage
```

(mkdir)=

### mkdir - create a directory

```{index} mkdir
```

SYNOPSYS:
: ```shell
  mkdir  dir [dir1 .. dirN]
  ```

DESCRIPTION:

: This command creates the set of directories in the order they are specified
  on the command line. If an error is encountered making one of the
  directories, the command will continue to attempt to create the remaining
  directories on the command line.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: If this command is invoked with no arguments, nothing occurs.

  The user must have sufficient permissions to create the directory. For the
  `fileio` test provided with RTEMS, this means the user must login as
  `root` not `rtems`.

EXAMPLES:

: The following is an example of how to use `mkdir`:

  ```shell
  SHLL [/] # ls
  drwxr-xr-x   1   root   root         536 Jan 01 00:00 dev/
  drwxr-xr-x   1   root   root        1072 Jan 01 00:00 etc/
  2 files 1608 bytes occupied
  SHLL [/] # mkdir joel
  SHLL [/] # ls joel
  0 files 0 bytes occupied
  SHLL [/] # cp etc/passwd joel
  SHLL [/] # ls joel
  -rw-r--r--   1   root   root         102 Jan 01 00:02 passwd
  1 files 102 bytes occupied
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_MKDIR
```

```{index} CONFIGURE_SHELL_COMMAND_MKDIR
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_MKDIR` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MKDIR` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_mkdir
```

PROGRAMMING INFORMATION:

: The `mkdir` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_mkdir(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `mkdir` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MKDIR_Command;
  ```

```{raw} latex
\clearpage
```

(mkdos)=

### mkdos - DOSFS file system format

```{index} mkdos
```

SYNOPSYS:
: ```shell
  mkdos [-V label] [-s sectors/cluster] [-r size] [-v] path
  ```

DESCRIPTION:

: This command formats a block device entry with the DOSFS file system.

  *-V label*

  : Specify the volume label.

  *-s sectors/cluster*

  : Specify the number of sectors per cluster.

  *-r size*

  : Specify the number of entries in the root directory.

  *-v*

  : Enable verbose output mode.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `mkdos`:

  ```shell
  SHLL [/] $ mkdos /dev/rda1
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_MKDOS
```

```{index} CONFIGURE_SHELL_COMMAND_MKDOS
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_MKDOS` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MKDOS` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_mkdos
```

PROGRAMMING INFORMATION:

: The `mkdos` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_mkdos(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `mkdos` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MKDOS_Command;
  ```

```{raw} latex
\clearpage
```

(mknod)=

### mknod - make device special file

```{index} mknod
```

SYNOPSYS:
: ```shell
  mknod [-rR] [-F fmt] [-g gid] [-m mode] [-u uid] name [c | b] [driver | major] minor
  mknod [-rR] [-F fmt] [-g gid] [-m mode] [-u uid] name [c | b] major unit subunit
  mknod [-rR] [-g gid] [-m mode] [-u uid] name [c | b] number
  mknod [-rR] [-g gid] [-m mode] [-u uid] name p
  ```

DESCRIPTION:

: The mknod command creates device special files, or fifos. Normally the
  shell script /dev/MAKEDEV is used to create special files for commonly
  known devices; it executes mknod with the appropriate arguments and can
  make all the files required for the device.

  To make nodes manually, the arguments are:

  *-r*

  : Replace an existing file if its type is incorrect.

  *-R*

  : Replace an existing file if its type is incorrect. Correct the mode,
    user and group.

  *-g gid*

  : Specify the group for the device node. The gid operand may be a
    numeric group ID or a group name. If a group name is also a numeric
    group ID, the operand is used as a group name. Precede a numeric group
    ID with a # to stop it being treated as a name.

  *-m mode*

  : Specify the mode for the device node. The mode may be absolute or
    symbolic, see *chmod*.

  *-u uid*

  : Specify the user for the device node. The uid operand may be a numeric
    user ID or a user name. If a user name is also a numeric user ID, the
    operand is used as a user name. Precede a numeric user ID with a # to
    stop it being treated as a name.

  *name*

  : Device name, for example "tty" for a termios serial device or "hd" for
    a disk.

  *b | c | p*

  : Type of device. If the device is a block type device such as a tape or
    disk drive which needs both cooked and raw special files, the type
    is b. All other devices are character type devices, such as terminal
    and pseudo devices, and are type c. Specifying p creates fifo files.

  *driver | major*

  : The major device number is an integer number which tells the kernel
    which device driver entry point to use. If the device driver is
    configured into the current kernel it may be specified by driver name
    or major number.

  *minor*

  : The minor device number tells the kernel which one of several similar
    devices the node corresponds to; for example, it may be a specific
    serial port or pty.

  *unit and subunit*

  : The unit and subunit numbers select a subset of a device; for example,
    the unit may specify a particular disk, and the subunit a partition on
    that disk. (Currently this form of specification is only supported by
    the bsdos format, for compatibility with the BSD/OS mknod).

  *number*

  : A single opaque device number. Useful for netbooted computers which
    require device numbers packed in a format that isn't supported by -F.

EXIT STATUS:

: The `mknod` utility exits 0 on success, and >0 if an error occurs.

NOTES:

: None.

EXAMPLES:
: ```shell
  SHLL [/] mknod c 3 0 /dev/ttyS10
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_MKNOD
```

```{index} CONFIGURE_SHELL_COMMAND_MKNOD
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_MKNOD` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MKNOD` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_mknod
```

PROGRAMMING INFORMATION:

: The `mknod` command is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_mknod(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `mknod` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MKNOD_Command;
  ```

ORIGIN:

: The implementation and portions of the documentation for this command are
  from NetBSD 4.0.

```{raw} latex
\clearpage
```

(mkrfs)=

### mkrfs - format RFS file system

```{index} mkrfs
```

SYNOPSYS:
: ```shell
  mkrfs [-vsbiIo] device
  ```

DESCRIPTION:

: Format the block device with the RTEMS File System (RFS). The default
  configuration with not parameters selects a suitable block size based on
  the size of the media being formatted.

  The media is broken up into groups of blocks. The number of blocks in a
  group is based on the number of bits a block contains. The large a block
  the more blocks a group contains and the fewer groups in the file system.

  The following options are provided:

  *-v*

  : Display configuration and progress of the format.

  *-s*

  : Set the block size in bytes.

  *-b*

  : The number of blocks in a group. The block count must be equal or less
    than the number of bits in a block.

  *-i*

  : Number of inodes in a group. The inode count must be equal or less than
    the number of bits in a block.

  *-I*

  : Initialise the inodes. The default is not to initialise the inodes and
    to rely on the inode being initialised when allocated. Initialising the
    inode table helps recovery if a problem appears.

  *-o*

  : Integer percentage of the media used by inodes. The default is 1%.

  *device*

  : Path of the device to format.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `mkrfs`:

  ```shell
  SHLL [/] $ mkrfs /dev/fdda
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_MKRFS
```

```{index} CONFIGURE_SHELL_COMMAND_MKRFS
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_MKRFS` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MKRFS` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_mkrfs
```

PROGRAMMING INFORMATION:

: The `mkrfs` command is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_mkrfs(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for `mkrfs` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MKRFS_Command;
  ```

```{raw} latex
\clearpage
```

(mount)=

### mount - mount disk

```{index} mount
```

SYNOPSYS:
: ```shell
  mount [-t fstype] [-r] [-L] device path
  ```

DESCRIPTION:

: The `mount` command will mount a block device to a mount point using the
  specified file system. The files systems are:

  - msdos - MSDOS File System
  - tftp - TFTP Network File System
  - ftp - FTP Network File System
  - nfs - Network File System
  - rfs - RTEMS File System

  When the file system type is 'msdos' or 'rfs' the driver is a "block device
  driver" node present in the file system. The driver is ignored with the
  'tftp' and 'ftp' file systems. For the 'nfs' file system the driver is the
  'host:/path' string that described NFS host and the exported file system
  path.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: The mount point must exist.

  The services offered by each file-system vary. For example you cannot list
  the directory of a TFTP file-system as this server is not provided in the
  TFTP protocol. You need to check each file-system's documentation for the
  services provided.

EXAMPLES:

: Mount the Flash Disk driver to the '/fd' mount point:

  ```shell
  SHLL [/] $ mount -t msdos /dev/flashdisk0 /fd
  ```

  Mount the NFS file system exported path 'bar' by host 'foo':

  ```shell
  $ mount -t nfs foo:/bar /nfs
  ```

  Mount the TFTP file system on '/tftp':

  ```shell
  $ mount -t tftp /tftp
  ```

  To access the TFTP files on server '10.10.10.10':
  .. code-block:: shell

  > \$ cat /tftp/10.10.10.10/test.txt

```{index} CONFIGURE_SHELL_NO_COMMAND_MOUNT
```

```{index} CONFIGURE_SHELL_COMMAND_MOUNT
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_MOUNT` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MOUNT` when all shell commands have been
  configured.

  The mount command includes references to file-system code. If you do not
  wish to include file-system that you do not use do not define the mount
  command support for that file-system. The file-system mount command defines
  are:

  - msdos - CONFIGURE_SHELL_MOUNT_MSDOS
  - tftp - CONFIGURE_SHELL_MOUNT_TFTP
  - ftp - CONFIGURE_SHELL_MOUNT_FTP
  - nfs - CONFIGURE_SHELL_MOUNT_NFS
  - rfs - CONFIGURE_SHELL_MOUNT_RFS

  An example configuration is:

  ```c
  #define CONFIGURE_SHELL_MOUNT_MSDOS
  #ifdef RTEMS_NETWORKING
  #define CONFIGURE_SHELL_MOUNT_TFTP
  #define CONFIGURE_SHELL_MOUNT_FTP
  #define CONFIGURE_SHELL_MOUNT_NFS
  #define CONFIGURE_SHELL_MOUNT_RFS
  #endif
  ```

```{index} rtems_shell_rtems_main_mount
```

PROGRAMMING INFORMATION:

: The `mount` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_mount(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `mount` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MOUNT_Command;
  ```

```{raw} latex
\clearpage
```

(mv)=

### mv - move files

```{index} mv
```

SYNOPSYS:
: ```shell
  mv [-fiv] source_file target_file
  mv [-fiv] source_file... target_file
  ```

DESCRIPTION:

: In its first form, the mv utility renames the file named by the source
  operand to the destination path named by the target operand. This form is
  assumed when the last operand does not name an already existing directory.

  In its second form, mv moves each file named by a source operand to a
  destination file in the existing directory named by the directory operand.
  The destination path for each operand is the pathname produced by the
  concatenation of the last operand, a slash, and the final pathname
  component of the named file.

  The following options are available:

  *-f*

  : Do not prompt for confirmation before overwriting the destination path.

  *-i*

  : Causes mv to write a prompt to standard error before moving a file that
    would overwrite an existing file. If the response from the standard
    input begins with the character 'y', the move is attempted.

  *-v*

  : Cause mv to be verbose, showing files as they are processed.

  The last of any -f or -i options is the one which affects mv's behavior.

  It is an error for any of the source operands to specify a nonexistent file
  or directory.

  It is an error for the source operand to specify a directory if the target
  exists and is not a directory.

  If the destination path does not have a mode which permits writing, mv
  prompts the user for confirmation as specified for the -i option.

  Should the *rename* call fail because source and target are on different
  file systems, `mv` will remove the destination file, copy the source file
  to the destination, and then remove the source. The effect is roughly
  equivalent to:

  ```shell
  rm -f destination_path && \
  cp -PRp source_file destination_path && \
  rm -rf source_file
  ```

EXIT STATUS:

: The `mv` utility exits 0 on success, and >0 if an error occurs.

NOTES:

: None.

EXAMPLES:
: ```shell
  SHLL [/] mv /dev/console /dev/con1
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_MV
```

```{index} CONFIGURE_SHELL_COMMAND_MV
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_MV` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_MV` when all shell commands have been
  configured.

```{index} rtems_shell_main_mv
```

PROGRAMMING INFORMATION:

: The `mv` command is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_main_mv(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `mv` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_MV_Command;
  ```

ORIGIN:

: The implementation and portions of the documentation for this command are
  from NetBSD 4.0.

```{raw} latex
\clearpage
```

(pwd)=

### pwd - print work directory

```{index} pwd
```

SYNOPSYS:
: ```shell
  pwd
  ```

DESCRIPTION:

: This command prints the fully qualified filename of the current working
  directory.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `pwd`:

  ```shell
  SHLL [/] $ pwd
  /
  SHLL [/] $ cd dev
  SHLL [/dev] $ pwd
  /dev
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_PWD
```

```{index} CONFIGURE_SHELL_COMMAND_PWD
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_PWD` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_PWD` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_pwd
```

PROGRAMMING INFORMATION:

: The `pwd` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_rtems_main_pwd(
      int    argc,
      char argv
  );
  ```

  The configuration structure for the `pwd` has the following prototype:

  ```c

  ```

  extern rtems_shell_cmd_t rtems_shell_PWD_Command;

```{raw} latex
\clearpage
```

(rmdir)=

### rmdir - remove empty directories

```{index} rmdir
```

SYNOPSYS:
: ```shell
  rmdir  [dir1 .. dirN]
  ```

DESCRIPTION:

: This command removes the specified set of directories. If no directories
  are provided on the command line, no actions are taken.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: This command is a implemented using the `rmdir(2)` system call and all
  reasons that call may fail apply to this command.

EXAMPLES:

: The following is an example of how to use `rmdir`:

  ```shell
  SHLL [/] # mkdir joeldir
  SHLL [/] # rmdir joeldir
  SHLL [/] # ls joeldir
  joeldir: No such file or directory.
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_RMDIR
```

```{index} CONFIGURE_SHELL_COMMAND_RMDIR
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_RMDIR` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_RMDIR` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_rmdir
```

PROGRAMMING INFORMATION:

: The `rmdir` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_rmdir(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `rmdir` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_RMDIR_Command;
  ```

```{raw} latex
\clearpage
```

(rm)=

### rm - remove files

```{index} rm
```

SYNOPSYS:
: ```shell
  rm file1 [file2 ... fileN]
  ```

DESCRIPTION:

: This command deletes a name from the filesystem. If the specified file
  name was the last link to a file and there are no `open` file descriptor
  references to that file, then it is deleted and the associated space in the
  file system is made available for subsequent use.

  If the filename specified was the last link to a file but there are open
  file descriptor references to it, then the file will remain in existence
  until the last file descriptor referencing it is closed.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: None.

EXAMPLES:

: The following is an example of how to use `rm`:

  ```shell
  SHLL [/] # cp /etc/passwd tmpfile
  SHLL [/] # cat tmpfile
  root:*:0:0:root::/:/bin/sh
  rtems:*:1:1:RTEMS Application::/:/bin/sh
  tty:!:2:2:tty owner::/:/bin/false
  SHLL [/] # rm tmpfile
  SHLL [/] # cat tmpfile
  cat: tmpfile: No such file or directory
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_RM
```

```{index} CONFIGURE_SHELL_COMMAND_RM
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_RM` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_RM` when all shell commands have been
  configured.

```{index} rtems_shell_main_rm
```

PROGRAMMING INFORMATION:

: The `rm` is implemented by a C language function which has the following
  prototype:

  ```c
  int rtems_shell_main_rm(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `rm` has the
  following prototype:
  .. code-block:: c

  > extern rtems_shell_cmd_t rtems_shell_RM_Command;

```{raw} latex
\clearpage
```

(umask)=

### umask - set file mode creation mask

```{index} umask
```

SYNOPSYS:
: ```shell
  umask [new_umask]
  ```

DESCRIPTION:

: This command sets the user file creation mask to `new_umask`. The
  argument `new_umask` may be octal, hexadecimal, or decimal.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: This command does not currently support symbolic mode masks.

EXAMPLES:

: The following is an example of how to use `umask`:

  ```shell
  SHLL [/] $ umask
  022
  SHLL [/] $ umask 0666
  0666
  SHLL [/] $ umask
  0666
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_UMASK
```

```{index} CONFIGURE_SHELL_COMMAND_UMASK
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_UMASK` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_UMASK` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_umask
```

PROGRAMMING INFORMATION:

: The `umask` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_umask(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `umask` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_UMASK_Command;
  ```

```{raw} latex
\clearpage
```

(unmount)=

### unmount - unmount disk

```{index} unmount
```

SYNOPSYS:
: ```shell
  unmount path
  ```

DESCRIPTION:

: This command unmounts the device at the specified `path`.

EXIT STATUS:

: This command returns 0 on success and non-zero if an error is encountered.

NOTES:

: TBD - Surely there must be some warnings to go here.

EXAMPLES:

: The following is an example of how to use `unmount`:

  ```shell
  # unmount /mnt
  ```

```{index} CONFIGURE_SHELL_NO_COMMAND_UNMOUNT
```

```{index} CONFIGURE_SHELL_COMMAND_UNMOUNT
```

CONFIGURATION:

: This command is included in the default shell command set. When building a
  custom command set, define `CONFIGURE_SHELL_COMMAND_UNMOUNT` to have this
  command included.

  This command can be excluded from the shell command set by defining
  `CONFIGURE_SHELL_NO_COMMAND_UNMOUNT` when all shell commands have been
  configured.

```{index} rtems_shell_rtems_main_unmount
```

PROGRAMMING INFORMATION:

: The `unmount` is implemented by a C language function which has the
  following prototype:

  ```c
  int rtems_shell_rtems_main_unmount(
      int    argc,
      char **argv
  );
  ```

  The configuration structure for the `unmount` has the following prototype:

  ```c
  extern rtems_shell_cmd_t rtems_shell_UNMOUNT_Command;
  ```
