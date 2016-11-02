.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment COPYRIGHT (c) 2012 - 2016.
.. comment Chris Johns <chrisj@rtems.org>

History
#######

The RTEMS Source Builder is a stand alone tool based on another tool called the
'SpecBuilder'. The SpecBuilder was written for the RTEMS project to give me a
way to build tools on hosts that did not support RPMs. At the time the RTEMS
tools maintainer only used spec files to create various packages. This meant I
had either spec files, RPM files or SRPM files. The RPM and SPRM files where
useless because you needed an 'rpm' type tool to extract and manage them. There
are versions of 'rpm' for a number of non-RPM hosts however these proved to be
in various broken states and randomly maintained. The solution I settled on was
to use spec files so I wrote a Python based tool that parsed the spec file
format and allowed me to create a shell script I could run to build the
package. This approach proved successful and I was able to track the RPM
version of the RTEMS tools on a non-RPM host over a number of years. however
the SpecBuilder tool did not help me build tools or other packages not related
to the RTEMS project where there was no spec file I could use so I needed
another tool. Rather than start again I decided to take the parsing code for
the spec file format and build a new tool called the RTEMS Source Builder.
