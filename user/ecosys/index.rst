.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. comment: Copyright (c) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _ecosystem:

RTEMS Ecosystem
***************
.. index:: Ecosystem

The RTEMS Ecosystem is the collection of tools, packages, code, documentation
and online content provided by the RTEMS Project. The ecosystem provides a way
to develop, maintain, and use RTEMS. It's parts interact with the user, the
host environment, and each other to make RTEMS accessable, useable and
predicable.

The ecosystem is for users, developers and maintainers and it is an on going
effort that needs your help and support. The RTEMS project is always improving
the way it delivers the kernel to you and your feedback is important so please
join the mailing lists and contribute back comments, success stories, bugs and
patches.

What the RTEMS project describes here to develop, maintain and use RTEMS does
not dictate what you need to use in your project. You can and should select the
work-flow that best suites the demands of your project and what you are
delivering.

Rational
========

RTEMS is complex and the focus of the RTEMS Ecosystem is to simplify the
complexity for users by providing a stable documented way to build, configure
and run RTEMS. RTEMS is more than a kernel running real-time applications on
target hardware, it is part of a project's and therefore team's workflow and
every project and team is different.

RTEMS's ecosystem does not mandate a way to work. It is a series of parts,
components, and items that are used to create a suitable development
environment to work with. The processes explained in this manual are the same
things an RTEMS maintainer does to maintain the kernel or an experienced user
does to build their production system. It is important to keep this in mind
when working through this manual. We encourage users to explore what can be
done and to discover ways to make it fit their needs. The ecosystem provided by
the RTEMS Project will not install in a single click of a mouse because we want
users to learn the parts they will come to depend on as their project's
development matures.

The RTEMS Ecosystem provides a standard interface that is the same on all
supported host systems. Standardizing how a user interacts with RTEMS is
important and making that experience portable is also important. As a result
the ecosystem is documented at the command line level and we leave GUI and IDE
integration for users and integrators.

Standardizing the parts and how to use them lets users create processes and
procedures that are stable over releases. The RTEMS Ecosystem generates data
that can be used to audit the build process so their configuration can be
documented.

The ecosystem is based around the source code used in the various parts,
compontents and items of the RTEMS development environment. A user can create
an archive of the complete build process including all the source code for long
term storage. This is important for projects with a long life cycle.

Open Source
===========

RTEMS is an open source operating system and an open source project and this
extends to the ecosystem. We encourage users to integrate the processes to
build tools, the kernel and any 3rd party libraries into their project's
configuration management processes.

All the parts that make up the ecosystem are open source. The ecosystem uses a
package's source code to create an executable on a host so when an example
RTEMS executable is created and run for the first time the user will have built
every tool as well as the executable from source. The RTEMS Project believes
the freedom this gives a user is as important as the freedom of having access
to the source code for a package.

Deployment
==========

The RTEMS Project provides the ecosystem as source code that users can download
to create personalised development environments. The RTEMS Project does not
provide packaging and deployment for a specific host environment, target
architecture or BSP. The RTEMS Project encourages users and organizations to
fill this role for the community.
