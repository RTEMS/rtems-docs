% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 embedded brains GmbH & Co. KG

% Copyright (C) 2024 Gedare Bloom

(Migration_5_to_6)=

# RTEMS 5 to RTEMS 6

This section provides helpful information when migrating from RTEMS 5 to
RTEMS 6.

## Update Development Sites to GitLab

The source code repos and ticket tracking systems have been migrated from the
previous sites at git.rtems.org and devel.rtems.org to a new {r:url}`devel`
built with GitLab. GitLab lets you have repositories structured as projects.
We have a top level namespace called RTEMS and our repositories reside under
this namespace. We have updated the RTEMS Documentation to reflect the new
worfklow and use of this GitLab service. If you have cloned repositories from
RTEMS you may need to correct the remote or re-clone those repositories.
Additional help can be found in `#gitlab-support` on our {r:url}`discord`.

## Update to GCC 10 and Later

The tool suite for RTEMS 6 uses at least GCC 10. GCC 10 and later enable
`-fno-common` by default. Code bases which never used this option before may
observe now multiple definition linker errors. For example, if global
variables are declared and defined in header files (usually a missing
`extern` in the header file).

## No -specs bsp_specs GCC Option

The `-spec bsp_specs` GCC Option is no longer needed to build RTEMS
applications and there is no {file}`bsp_specs` file installed. If you use this
option, then you get an error like this:

```none
sparc-rtems6-gcc: fatal error: cannot read spec file 'bsp_specs': No such file or directory
```

You can remove this GCC option from your build to fix this error.
Alternatively, you can add an empty {file}`bsp_specs` file.

## Replacements for Removed APIs

Please refer to the release notes.
