% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2012, 2016 Chris Johns <chrisj@rtems.org>

# History

The RTEMS Source Builder is a stand alone tool based on another tool called the
*SpecBuilder* written by Chris Johns. The *SpecBuilder* was written around 2010
for the RTEMS project to provide Chris with a way to build tools on hosts that
did not support RPMs. At the time the RTEMS tools maintainer only supported
*spec* files and these files held all the vital configuration data needed to
create suitable tool sets. The available SRPM and *spec* files by themselves
where of little use because a suitable `rpm` tool was needed to use them. At
the time the available versions of `rpm` for a number of non-RPM hosts were
broken and randomly maintained. The solution Chris settled on was to use the
*spec* files and to write a Python based tool that parsed the *spec* file
format creating a shell script that could be run to build the package. The
approach proved successful and Chris was able to track the RPM version of the
RTEMS tools on a non-RPM host for a number of years.

The *SpecBuilder* tool did not build tools or packages unrelated to the RTEMS
Project where no suitable *spec* file was available so another tool was
needed. Rather than start again Chris decided to take the parsing code for the
*spec* file format and build a new tool called the RTEMS Source Builder.
