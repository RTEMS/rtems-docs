Status of Implementation
########################

This chapter provides an overview of the status of the implementation
of the POSIX API for RTEMS.  The *POSIX 1003.1b Compliance Guide*
provides more detailed information regarding the implementation of
each of the numerous functions, constants, and macros specified by
the POSIX 1003.1b standard.

RTEMS supports many of the process and user/group oriented services
in a "single user/single process" manner.  This means that although
these services may be of limited usefulness or functionality, they
are provided and do work in a coherent manner.  This is significant
when porting existing code from UNIX to RTEMS.

- Implementation

  - The current implementation of ``dup()`` is insufficient.
  - FIFOs ``mkfifo()`` are not currently implemented.
  - Asynchronous IO is not implemented.
  - The ``flockfile()`` family is not implemented
  - getc/putc unlocked family is not implemented
  - Shared Memory is not implemented
  - Mapped Memory is not implemented
  - NOTES:

    - For Shared Memory and Mapped Memory services, it is unclear what
      level of support is appropriate and possible for RTEMS.

- Functional Testing

  - Tests for unimplemented services

- Performance Testing

  - There are no POSIX Performance Tests.

- Documentation

  - Many of the service description pages are not complete in this
    manual.  These need to be completed and information added to the
    background and operations sections.

  - Example programs (not just tests) would be very nice.
