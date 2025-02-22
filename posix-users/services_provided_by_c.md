% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

# Services Provided by C Library (libc)

## Introduction

This section lists the routines that provided by the Newlib C Library.

## Standard Utility Functions (stdlib.h)

- `abort` - Abnormal termination of a program
- `abs` - Integer absolute value (magnitude)
- `assert` - Macro for Debugging Diagnostics
- `atexit` - Request execution of functions at program exit
- `atof` - String to double or float
- `atoi` - String to integer
- `bsearch` - Binary search
- `calloc` - Allocate space for arrays
- `div` - Divide two integers
- `ecvtbuf` - Double or float to string of digits
- `ecvt` - Double or float to string of digits (malloc result)
- `__env_lock` - Lock environment list for getenv and setenv
- `gvcvt` - Format double or float as string
- `exit` - End program execution
- `getenv` - Look up environment variable
- `labs` - Long integer absolute value (magnitude)
- `ldiv` - Divide two long integers
- `malloc` - Allocate memory
- `realloc` - Reallocate memory
- `free` - Free previously allocated memory
- `mallinfo` - Get information about allocated memory
- `__malloc_lock` - Lock memory pool for malloc and free
- `mbstowcs` - Minimal multibyte string to wide string converter
- `mblen` - Minimal multibyte length
- `mbtowc` - Minimal multibyte to wide character converter
- `qsort` - Sort an array
- `rand` - Pseudo-random numbers
- `strtod` - String to double or float
- `strtol` - String to long
- `strtoul` - String to unsigned long
- `system` - Execute command string
- `wcstombs` - Minimal wide string to multibyte string converter
- `wctomb` - Minimal wide character to multibyte converter

## Character Type Macros and Functions (ctype.h)

- `isalnum` - Alphanumeric character predicate
- `isalpha` - Alphabetic character predicate
- `isascii` - ASCII character predicate
- `iscntrl` - Control character predicate
- `isdigit` - Decimal digit predicate
- `islower` - Lower-case character predicate
- `isprint` - Printable character predicates (isprint, isgraph)
- `ispunct` - Punctuation character predicate
- `isspace` - Whitespace character predicate
- `isupper` - Uppercase character predicate
- `isxdigit` - Hexadecimal digit predicate
- `toascii` - Force integers to ASCII range
- `tolower` - Translate characters to lower case
- `toupper` - Translate characters to upper case

## Input and Output (stdio.h)

- `clearerr` - Clear file or stream error indicator
- `fclose` - Close a file
- `feof` - Test for end of file
- `ferror` - Test whether read/write error has occurred
- `fflush` - Flush buffered file output
- `fgetc` - Get a character from a file or stream
- `fgetpos` - Record position in a stream or file
- `fgets` - Get character string from a file or stream
- `fiprintf` - Write formatted output to file (integer only)
- `fopen` - Open a file
- `fdopen` - Turn an open file into a stream
- `fputc` - Write a character on a stream or file
- `fputs` - Write a character string in a file or stream
- `fread` - Read array elements from a file
- `freopen` - Open a file using an existing file descriptor
- `fseek` - Set file position
- `fsetpos` - Restore position of a stream or file
- `ftell` - Return position in a stream or file
- `fwrite` - Write array elements from memory to a file or stream
- `getc` - Get a character from a file or stream (macro)
- `getchar` - Get a character from standard input (macro)
- `gets` - Get character string from standard input (obsolete)
- `iprintf` - Write formatted output (integer only)
- `mktemp` - Generate unused file name
- `perror` - Print an error message on standard error
- `putc` - Write a character on a stream or file (macro)
- `putchar` - Write a character on standard output (macro)
- `puts` - Write a character string on standard output
- `remove` - Delete a file's name
- `rename` - Rename a file
- `rewind` - Reinitialize a file or stream
- `setbuf` - Specify full buffering for a file or stream
- `setvbuf` - Specify buffering for a file or stream
- `siprintf` - Write formatted output (integer only)
- `printf` - Write formatted output
- `scanf` - Scan and format input
- `tmpfile` - Create a temporary file
- `tmpnam` - Generate name for a temporary file
- `vprintf` - Format variable argument list

## Strings and Memory (string.h)

- `bcmp` - Compare two memory areas
- `bcopy` - Copy memory regions
- `bzero` - Initialize memory to zero
- `index` - Search for character in string
- `memchr` - Find character in memory
- `memcmp` - Compare two memory areas
- `memcpy` - Copy memory regions
- `memmove` - Move possibly overlapping memory
- `memset` - Set an area of memory
- `rindex` - Reverse search for character in string
- `strcasecmp` - Compare strings ignoring case
- `strcat` - Concatenate strings
- `strchr` - Search for character in string
- `strcmp` - Character string compare
- `strcoll` - Locale specific character string compare
- `strcpy` - Copy string
- `strcspn` - Count chars not in string
- `strerror` - Convert error number to string
- `strlen` - Character string length
- `strlwr` - Convert string to lower case
- `strncasecmp` - Compare strings ignoring case
- `strncat` - Concatenate strings
- `strncmp` - Character string compare
- `strncpy` - Counted copy string
- `strpbrk` - Find chars in string
- `strrchr` - Reverse search for character in string
- `strspn` - Find initial match
- `strstr` - Find string segment
- `strtok` - Get next token from a string
- `strupr` - Convert string to upper case
- `strxfrm` - Transform string

## Signal Handling (signal.h)

- `raise` - Send a signal
- `signal` - Specify handler subroutine for a signal

## Time Functions (time.h)

- `asctime` - Format time as string
- `clock` - Cumulative processor time
- `ctime` - Convert time to local and format as string
- `difftime` - Subtract two times
- `gmtime` - Convert time to UTC (GMT) traditional representation
- `localtime` - Convert time to local representation
- `mktime` - Convert time to arithmetic representation
- `strftime` - Flexible calendar time formatter
- `time` - Get current calendar time (as single number)

## Locale (locale.h)

- `setlocale` - Select or query locale

## Reentrant Versions of Functions

- Equivalent for errno variable:
  \- `errno_r` - XXX

- Locale functions:

  - `localeconv_r` - XXX
  - `setlocale_r` - XXX

- Equivalents for stdio variables:

  - `stdin_r` - XXX
  - `stdout_r` - XXX
  - `stderr_r` - XXX

- Stdio functions:

  - `fdopen_r` - XXX
  - `perror_r` - XXX
  - `tempnam_r` - XXX
  - `fopen_r` - XXX
  - `putchar_r` - XXX
  - `tmpnam_r` - XXX
  - `getchar_r` - XXX
  - `puts_r` - XXX
  - `tmpfile_r` - XXX
  - `gets_r` - XXX
  - `remove_r` - XXX
  - `vfprintf_r` - XXX
  - `iprintf_r` - XXX
  - `rename_r` - XXX
  - `vsnprintf_r` - XXX
  - `mkstemp_r` - XXX
  - `snprintf_r` - XXX
  - `vsprintf_r` - XXX
  - `mktemp_t` - XXX
  - `sprintf_r` - XXX

- Signal functions:

  - `init_signal_r` - XXX
  - `signal_r` - XXX
  - `kill_r` - XXX
  - `_sigtramp_r` - XXX
  - `raise_r` - XXX

- Stdlib functions:

  - `calloc_r` - XXX
  - `mblen_r` - XXX
  - `srand_r` - XXX
  - `dtoa_r` - XXX
  - `mbstowcs_r` - XXX
  - `strtod_r` - XXX
  - `free_r` - XXX
  - `mbtowc_r` - XXX
  - `strtol_r` - XXX
  - `getenv_r` - XXX
  - `memalign_r` - XXX
  - `strtoul_r` - XXX
  - `mallinfo_r` - XXX
  - `mstats_r` - XXX
  - `system_r` - XXX
  - `malloc_r` - XXX
  - `rand_r` - XXX
  - `wcstombs_r` - XXX
  - `malloc_r` - XXX
  - `realloc_r` - XXX
  - `wctomb_r` - XXX
  - `malloc_stats_r` - XXX
  - `setenv_r` - XXX

- String functions:

  - `strtok_r` - XXX

- System functions:

  - `close_r` - XXX
  - `link_r` - XXX
  - `unlink_r` - XXX
  - `execve_r` - XXX
  - `lseek_r` - XXX
  - `wait_r` - XXX
  - `fcntl_r` - XXX
  - `open_r` - XXX
  - `write_r` - XXX
  - `fork_r` - XXX
  - `read_r` - XXX
  - `fstat_r` - XXX
  - `sbrk_r` - XXX
  - `gettimeofday_r` - XXX
  - `stat_r` - XXX
  - `getpid_r` - XXX
  - `times_r` - XXX

- Time function:

  - `asctime_r` - XXX

## Miscellaneous Macros and Functions

- `unctrl` - Return printable representation of a character

## Variable Argument Lists

- Stdarg (stdarg.h):

  - `va_start` - XXX
  - `va_arg` - XXX
  - `va_end` - XXX

- Vararg (varargs.h):

  - `va_alist` - XXX
  - `va_start-trad` - XXX
  - `va_arg-trad` - XXX
  - `va_end-trad` - XXX

## Reentrant System Calls

- `open_r` - XXX
- `close_r` - XXX
- `lseek_r` - XXX
- `read_r` - XXX
- `write_r` - XXX
- `fork_r` - XXX
- `wait_r` - XXX
- `stat_r` - XXX
- `fstat_r` - XXX
- `link_r` - XXX
- `unlink_r` - XXX
- `sbrk_r` - XXX
