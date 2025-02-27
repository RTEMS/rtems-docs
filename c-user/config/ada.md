% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

(ConfigAda)=

# Ada Configuration

The GNU Ada runtime library (libgnarl) uses threads, mutexes, condition
variables, and signals from the pthreads API. It uses also thread-local storage
for the Ada Task Control Block (ATCB). From these resources only the threads
need to be accounted for in the configuration. You should include the Ada tasks
in your setting of the {ref}`CONFIGURE_MAXIMUM_POSIX_THREADS` configuration
option.
