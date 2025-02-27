% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2017 On-Line Applications Research Corporation (OAR)

# Device Control

## Introduction

The POSIX Device Control API is defined by POSIX 1003.26 and attempts
to provides a portable alternative to the ioctl() service which is
not standardized across POSIX implementations. Support for this
standard is required by the Open Group's FACE Technical Standard
\:cits:"FACE:2012:FTS". Unfortunately, this part of the POSIX standard
is not widely implemented.

The services provided by the timer manager are:

- [posix_devctl] - Control a Device

## Background

## Operations

## System Calls

This section details the POSIX device control's services. A subsection
is dedicated to each of this manager's services and describes the calling
sequence, related constants, usage, and status codes.

% COMMENT: posix_devctl

(posix_devctl)=

% _posix_devctl

### posix_devctl - Control a Device

**CALLING SEQUENCE:**

```c

```

\: #include \<devctl.h>
int posix_devctl(

> int fd,
> int dcmd,
> void restrict dev_data_ptr,
> size_t nbyte,
> int restrict dev_info_ptr

);

\`
**STATUS CODES:**

The status codes returned reflect those returned by the `ioctl()` service
and the underlying device drivers.

**DESCRIPTION:**

This method is intended to be a portable alternative to the `ioctl()`
method. The RTEMS implementation follows what is referred to as a library
implementation which is a simple wrapper for the `ioctl()` method.
The fd, fcmd, dev_data_ptr, and nbyte parameters are passed unmodified
to the `ioctl()` method.

If the dev_info_ptr parameter is not NULL, then the location pointed
to by dev_info_ptr is set to 0.

**NOTES:**

NONE
