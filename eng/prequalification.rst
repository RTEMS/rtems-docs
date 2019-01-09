.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016, 2018 RTEMS Foundation, The RTEMS Documentation Project
.. Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

Introduction to Pre-Qualification
*********************************

RTEMS has a long history of being used to support critical
applications. In some of these application domains, there are standards
(e.g., DO-178C, NPR 7150.2) which define the expectations for the
processes used to develop software and the associated artifacts. These
standards typically do not specify software functionality but address
topics like requirements definition, traceability, having a documented
change process, coding style, testing requirements, and a user's
manual. During system test, these standards call for a review - usually
by an independent entity - that the standard has been adhered too. These
reviews cover a broad variety of topics and activities, but the process
is generally referred to as qualification, verification, or auditing
against the specific standard in use. The RTEMS Project will use the
term "qualification" independent of the standard.

The goal of the RTEMS Qualification Project is to make RTEMS easier
to review regardless of the standard chosen. Quite specifically,
the RTEMS Qualification effort will NOT produce a directly qualified
product or artifacts in the format dictated by a specific organization
or standard. The goal is to make RTEMS itself, documentation, testing
infrastructure, etc. more closely align with the information requirements
of these high integrity qualification standards. In addition to improving
the items that a mature, high quality open source project will have,
there are additional artifacts needed for a qualification effort that
no known open source project possesses. Specifically, requirements and
the associated traceability to source code, tests, and documentation
are needed.

The RTEMS Qualification Project is technically
"pre-qualification." True qualification must be performed on the
project's target hardware in a system context. The FAA has provided
guidance for Reusable Software Components (FAA-AC20-148) and this
effort should follow that guidance. The open RTEMS Project, with the
assistance of domain experts, will possess and maintain the master
technical information needed in a qualification effort. Consultants
will provide the services required to tailor the master information,
perform testing on specific system hardware, and to guide end users in
using the master technical data in the context of a particular standard.

The RTEMS Qualification Project will broadly address two areas. The
first area is suggesting areas of improvement for automated project
infrastructure and the master technical data that has traditionally been
provided by the RTEMS Project. For example, the RTEMS Qualification could
suggest specific improvements to code coverage reports. The teams focused
on qualification should be able to provide resources for improving the
automated project infrastructure and master technical data for RTEMS. The
term "resources" is often used by open source projects to refer to
volunteer code contributions or funding. Although code contributions in
this area are important and always welcome, funding is also important. At
a minimum, ongoing funding is needed for maintenance and upgrades of
the RTEMS Project server infrastructure, addition of services to those
servers, and core contributors to review submissions

The second area is the creation and maintenance of master technical
data that has traditionally not been owned or maintained by the RTEMS
Project. The most obvious example of this is a requirements set with
proper infrastructure for tracing requirements through code to test
and documentation. It is expected that these will be maintained by the
RTEMS Qualification Project. They will be evaluated for adoption by
the main RTEMS Project but the additional maintenance burden imposed
will be a strong factor in this consideration. It behooves the RTEMS
Qualification Project to limit dependence on manual checks and ensure
that automation and ongoing support for that automation is contributed
to the RTEMS Project.

It is expected that the RTEMS Qualification Project will create and
maintain maps from the RTEMS master technical data to the various
qualification standards. It will maintain "scorecards" which
identify how the RTEMS Project is currently doing when reviewed per each
standard. These will be maintained in the open as community resources
which will guide the community in improving its infrastructure.
