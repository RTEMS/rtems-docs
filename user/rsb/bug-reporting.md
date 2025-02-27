% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

(bugs-crashes-and-build-failures)=

# Bugs, Crashes, and Build Failures

The RTEMS Source Builder is a Python program and every care is taken to test
the code however bugs, crashes, and build failures can and do happen. If you
find a bug please report it via the {r:url}`devel` or email on the RTEMS Users
list.

Please include the generated RSB report. If you see the following a report has
been generated:

```none
...
...
Build FAILED   <1>
  See error report: rsb-report-@rtems-ver-major@.@rtems-ver-minor@-rtems-sparc.txt   <2>
```

```{topic} Items:
1. The build has failed.
2. The report's file name.
```

The generated report contains the command line, version of the RSB, your host's
`uname` details, the version of Python and the last 200 lines of the log.

If for some reason there is no report please send please report the following:

- Command line,
- The git hash,
- Host details with the output of the `uname -a` command,
- If you have made any modifications.

If there is a Python crash please cut and paste the Python backtrace into the
bug report. If the tools fail to build please locate the first error in the log
file. This can be difficult to find on hosts with many cores so it sometimes
pays to re-run the command with the `--jobs=none` option to get a log that is
correctly sequenced. If searching the log file seach for `error:` and the
error should be just above it.

(Contributing)=

## Contributing

We welcome all users adding, fixing, updating and upgrading packages and their
configurations. The RSB is open source and open to contributions. These can be
bug fixes, new features or new configurations. Please break patches down into
changes to the core Python code, configuration changes or new configurations.

Please email patches generated using git so your commit messages and you are
acknowledged as the contributor.
