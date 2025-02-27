% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2015, 2021 embedded brains GmbH & Co. KG

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

(FatalErrorManagerDirectives)=

# Directives

This section details the directives of the Fatal Error Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/fatal/if/fatal

```{raw} latex
\clearpage
```

```{index} rtems_fatal()
```

```{index} announce fatal error
```

```{index} fatal error, announce
```

(InterfaceRtemsFatal)=

## rtems_fatal()

Invokes the fatal error handler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_fatal(
  rtems_fatal_source fatal_source,
  rtems_fatal_code   fatal_code
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`fatal_source`
: This parameter is the fatal source.

`fatal_code`
: This parameter is the fatal code.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive processes fatal errors. The fatal source is set to the value of
the `fatal_source` parameter. The fatal code is set to the value of the
`fatal_code` parameter.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not return to the caller.
- The directive invokes the fatal error extensions in {term}`extension forward order`.
- The directive does not invoke handlers registered by {c:func}`atexit` or
  {c:func}`on_exit`.
- The directive may terminate the system.

% Generated from spec:/rtems/fatal/if/panic

```{raw} latex
\clearpage
```

```{index} rtems_panic()
```

```{index} panic
```

(InterfaceRtemsPanic)=

## rtems_panic()

Prints the message and invokes the fatal error handler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_panic( const char *fmt, ... );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`fmt`
: This parameter is the message format.

`...`
: This parameter is a list of optional parameters required by the message
  format.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive prints a message via {ref}`InterfacePrintk` specified by the
`fmt` parameter and optional parameters and then invokes the fatal error
handler. The fatal source is set to {c:macro}`RTEMS_FATAL_SOURCE_PANIC`. The
fatal code is set to the value of the `fmt` parameter value.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not return to the caller.
- The directive invokes the fatal error extensions in {term}`extension forward order`.
- The directive does not invoke handlers registered by {c:func}`atexit` or
  {c:func}`on_exit`.
- The directive may terminate the system.

% Generated from spec:/rtems/fatal/if/shutdown-executive

```{raw} latex
\clearpage
```

```{index} rtems_shutdown_executive()
```

```{index} shutdown RTEMS
```

(InterfaceRtemsShutdownExecutive)=

## rtems_shutdown_executive()

Invokes the fatal error handler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_shutdown_executive( uint32_t fatal_code );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`fatal_code`
: This parameter is the fatal code.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive processes fatal errors. The fatal source is set to
{c:macro}`RTEMS_FATAL_SOURCE_EXIT`. The fatal code is set to the value of the
`fatal_code` parameter.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not return to the caller.
- The directive invokes the fatal error extensions in {term}`extension forward order`.
- The directive does not invoke handlers registered by {c:func}`atexit` or
  {c:func}`on_exit`.
- The directive may terminate the system.

% Generated from spec:/rtems/fatal/if/exception-frame-print

```{raw} latex
\clearpage
```

```{index} rtems_exception_frame_print()
```

```{index} exception frame
```

(InterfaceRtemsExceptionFramePrint)=

## rtems_exception_frame_print()

Prints the exception frame.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_exception_frame_print( const rtems_exception_frame *frame );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`frame`
: This parameter is the reference to the exception frame to print.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The exception frame is printed in an architecture-dependent format using
{ref}`InterfacePrintk`.

% Generated from spec:/rtems/fatal/if/source-text

```{raw} latex
\clearpage
```

```{index} rtems_fatal_source_text()
```

```{index} fatal error
```

(InterfaceRtemsFatalSourceText)=

## rtems_fatal_source_text()

Returns a descriptive text for the fatal source.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
const char *rtems_fatal_source_text( rtems_fatal_source fatal_source );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`fatal_source`
: This parameter is the fatal source.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

"?"
: The `fatal_source` parameter value was not a fatal source.

Returns a descriptive text for the fatal source. The text for the fatal source
is the enumerator constant name.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

% Generated from spec:/rtems/fatal/if/internal-error-text

```{raw} latex
\clearpage
```

```{index} rtems_internal_error_text()
```

```{index} fatal error
```

(InterfaceRtemsInternalErrorText)=

## rtems_internal_error_text()

Returns a descriptive text for the internal error code.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
const char *rtems_internal_error_text( rtems_fatal_code internal_error_code );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`internal_error_code`
: This parameter is the internal error code.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

"?"
: The `internal_error_code` parameter value was not an internal error code.

Returns a descriptive text for the internal error code. The text for the
internal error code is the enumerator constant name.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

% Generated from spec:/rtems/fatal/if/error-occurred

```{raw} latex
\clearpage
```

```{index} rtems_fatal_error_occurred()
```

(InterfaceRtemsFatalErrorOccurred)=

## rtems_fatal_error_occurred()

Invokes the fatal error handler.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
void rtems_fatal_error_occurred( uint32_t fatal_code );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`fatal_code`
: This parameter is the fatal code.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive processes fatal errors. The fatal source is set to
{c:macro}`INTERNAL_ERROR_RTEMS_API`. The fatal code is set to the value of the
`fatal_code` parameter.

```{eval-rst}
.. rubric:: NOTES:
```

This directive is deprecated and should not be used in new code. It is
recommended to not use this directive since error locations cannot be uniquely
identified. A recommended alternative directive is {ref}`InterfaceRtemsFatal`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not return to the caller.
- The directive invokes the fatal error extensions in {term}`extension forward order`.
- The directive does not invoke handlers registered by {c:func}`atexit` or
  {c:func}`on_exit`.
- The directive may terminate the system.
