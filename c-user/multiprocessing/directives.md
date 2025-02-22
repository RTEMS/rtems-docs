% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2021 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

(multiprocessingmanagerdirectives)=

# Directives

This section details the directives of the Multiprocessing Manager. A
subsection is dedicated to each of this manager's directives and lists the
calling sequence, parameters, description, return values, and notes of the
directive.

% Generated from spec:/rtems/mp/if/announce

```{raw} latex
\clearpage
```

```{index} rtems_multiprocessing_announce()
```

(interfacertemsmultiprocessingannounce)=

## rtems_multiprocessing_announce()

Announces the arrival of a packet.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_multiprocessing_announce( void );
```

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive informs RTEMS that a multiprocessing communications packet has
arrived from another node. This directive is called by the user-provided MPCI,
and is only used in multiprocessing configurations.

```{eval-rst}
.. rubric:: NOTES:
```

This directive is typically called from an {term}`ISR`.

This directive does not generate activity on remote nodes.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within interrupt context.
- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may unblock a task. This may cause the calling task to be
  preempted.
