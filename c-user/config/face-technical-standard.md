% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2022 On-Line Applications Research Corporation (OAR)

% This file is part of the RTEMS quality process and was automatically
% generated.  If you find something that needs to be fixed or
% worded better please post a report or patch to an RTEMS mailing list
% or raise a bug report:
%
% https://www.rtems.org/bugs.html
%
% For information on updating and regenerating please refer to the How-To
% section in the Software Requirements Engineering chapter of the
% RTEMS Software Engineering manual.  The manual is provided as a part of
% a release.  For development sources please refer to the online
% documentation at:
%
% https://docs.rtems.org

% Generated from spec:/acfg/if/group-face

# FACE Technical Standard Related Configuration

This section describes configuration options related to adapting RTEMS behavior
to be aligned with the FACE Technical Standard. The FACE Technical Standard is
a product of the FACE Consortium which operates under the Open Group. The FACE
Consortium was founded by avionics organizations to improve the portability of
cockpit software across various platforms. It addresses technical and business
concerns.

Most important from an RTEMS perspective, the FACE Technical Standard defines
four POSIX profiles: Security, Safety Base, Safety Extended, and the General
Purpose Profile. Each has an increasingly larger subset of POSIX APIs. In the
Security and Safety profiles, ARINC 653 is required. It is optional in the
General Purpose Profile.

The RTEMS Project has been tracking alignment with the FACE POSIX profiles and
they are included in the "RTEMS POSIX 1003.1 Compliance Guide."

% Generated from spec:/acfg/if/posix-timer-face-behavior

```{raw} latex
\clearpage
```

```{index} CONFIGURE_POSIX_TIMERS_FACE_BEHAVIOR
```

(CONFIGURE_POSIX_TIMERS_FACE_BEHAVIOR)=

## CONFIGURE_POSIX_TIMERS_FACE_BEHAVIOR

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_POSIX_TIMERS_FACE_BEHAVIOR`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is a boolean feature define.

```{eval-rst}
.. rubric:: DEFAULT CONFIGURATION:
```

If this configuration option is undefined, then the described feature is not
enabled.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

If this configuration option is defined, then POSIX timers may not be created
to use the {term}`CLOCK_REALTIME`. Per POSIX, this is allowed behavior but per
the FACE Technical Standard, it is not. Using POSIX timers based on
CLOCK_REALTIME (e.g., time of day) is unsafe for real-time safety systems as
setting CLOCK_REALTIME will perturb any active timers.

If this option is not defined, POSIX timers may be created to use the
CLOCK_REALTIME in compliance with the POSIX specification.
