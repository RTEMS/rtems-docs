.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019, 2020 embedded brains GmbH (http://www.embedded-brains.de)

.. |E40| replace:: ECSS-E-ST-40C

.. _ReqEng:

Software Requirements Engineering
*********************************

Software engineering standards for critical software such as |E40| demand that
software requirements for a software product are collected in a software
requirements specification (technical specification in |E40| terms).  They are
usually derived from system requirements (requirements baseline in |E40|
terms).  RTEMS is designed as a reusable software product which can be utilized
by application designers to ease the development of their applications.  The
requirements of the end system (system requirements) using RTEMS are only known
to the application designer.  RTEMS itself is developed by the RTEMS
maintainers and they do not know the requirements of a particular end system in
general.  RTEMS is designed as a real-time operating system to meet typical
system requirements for a wide range of applications.  Its suitability for a
particular application must be determined by the application designer based on
the technical specification provided by RTEMS accompanied with performance data
for a particular target platform.

Currently, no technical specification of RTEMS exists in the form of a
dedicated document.  Since the beginning of the RTEMS evolution in the late
1980s it was developed iteratively.  It was never developed in a waterfall
model.  During initial development the RTEID :cite:`Motorola:1988:RTEID` and
later the ORKID :cite:`VITA:1990:ORKID` draft specifications were used as
requirements.  These were evolving during the development and an iterative
approach was followed often using simple algorithms and coming back to
optimise.  In 1993 and 1994 a subset of pthreads sufficient to support
:term:`GNAT` was added as requirements.  At this time the Ada tasking was
defined, however, not implemented in GNAT, so this involved guessing during the
development. Later some adjustments were made when Ada tasking was actually
implemented.  So, it was consciously iterative with the specifications evolving
and feedback from performance analysis.  Benchmarks published from other real
time operating systems were used for comparison.  Optimizations were carried
out until the results were comparable.  Development was done with distinct
contractual phases and tasks for development, optimization, and the addition of
priority inheritance and rate monotonic scheduling.  The pthreads requirement
has grown to be as much POSIX as possible.

Portability from FreeBSD to use its network stack, USB stack, SD/MMC card stack
and device drivers resulted in another set of requirements.  The addition of
support for symmetric multiprocessing (SMP) was a huge driver for change.  It
was developed step by step and sponsored by several independent users with
completely different applications and target platforms in mind.  The high
performance OpenMP support introduced the Futex as a new synchronization
primitive.

.. topic:: Guidance

    A key success element of RTEMS is the ability to accept changes driven by
    user needs and still keep the operating system stable enough for production
    systems.  Procedures that place a high burden on changes are doomed to be
    discarded by the RTEMS Project.  We have to keep this in mind when we
    introduce a requirements management work flow which should be followed by
    RTEMS community members and new contributors.

We have to put in some effort first into the reconstruction of software
requirements through reverse engineering using the RTEMS documentation, test
cases, sources, standard references, mailing list archives, etc. as input.
Writing a technical specification for the complete RTEMS code base is probably
a job of several person-years.  We have to get started with a moderate feature
set (e.g. subset of the Classic API) and extend it based on user demands step
by step.

The development of the technical specification will take place in two phases.
The first phase tries to establish an initial technical specification for an
initial feature set.  This technical specification will be integrated into
RTEMS as a big chunk.  In the second phase the technical specification is
modified through arranged procedures.  There will be procedures

* to modify existing requirements,

* add new requirements, and

* mark requirements as obsolete.

All procedures should be based on a peer review principles.

.. toctree::

    req-for-req
    items
    traceability
    management
    tooling
