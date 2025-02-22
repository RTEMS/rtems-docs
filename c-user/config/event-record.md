% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019, 2022 embedded brains GmbH & Co. KG

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

% Generated from spec:/acfg/if/group-eventrecord

# Event Recording Configuration

This section describes configuration options related to the event recording.

% Generated from spec:/acfg/if/record-extensions-enabled

```{raw} latex
\clearpage
```

```{index} CONFIGURE_RECORD_EXTENSIONS_ENABLED
```

(configure-record-extensions-enabled)=

## CONFIGURE_RECORD_EXTENSIONS_ENABLED

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_RECORD_EXTENSIONS_ENABLED`

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

In case

- this configuration option is defined
- and {ref}`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,

then the event record extensions are enabled.

```{eval-rst}
.. rubric:: NOTES:
```

The record extensions capture thread create, start, restart, delete, switch,
begin, exitted and terminate events.

% Generated from spec:/acfg/if/record-fatal-dump-base64

```{raw} latex
\clearpage
```

```{index} CONFIGURE_RECORD_FATAL_DUMP_BASE64
```

(configure-record-fatal-dump-base64)=

## CONFIGURE_RECORD_FATAL_DUMP_BASE64

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_RECORD_FATAL_DUMP_BASE64`

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

In case

- this configuration option is defined
- and {ref}`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,
- and {ref}`CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB` is undefined,

then the event records are dumped in Base64 encoding in a fatal error
extension (see {ref}`Terminate`).

```{eval-rst}
.. rubric:: NOTES:
```

This extension can be used to produce crash dumps.

% Generated from spec:/acfg/if/record-fatal-dump-base64-zlib

```{raw} latex
\clearpage
```

```{index} CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB
```

(configure-record-fatal-dump-base64-zlib)=

## CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_RECORD_FATAL_DUMP_BASE64_ZLIB`

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

In case

- this configuration option is defined
- and {ref}`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,

then the event records are compressed by zlib and dumped in Base64 encoding
in a fatal error extension (see {ref}`Terminate`).

```{eval-rst}
.. rubric:: NOTES:
```

The zlib compression needs about 512KiB of RAM. This extension can be used
to produce crash dumps.

% Generated from spec:/acfg/if/record-interrupts-enabled

```{raw} latex
\clearpage
```

```{index} CONFIGURE_RECORD_INTERRUPTS_ENABLED
```

(configure-record-interrupts-enabled)=

## CONFIGURE_RECORD_INTERRUPTS_ENABLED

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_RECORD_INTERRUPTS_ENABLED`

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

In case

- this configuration option is defined
- and {ref}`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS` is properly defined,

then the interrupt event recording is enabled.

```{eval-rst}
.. rubric:: NOTES:
```

The interrupt event recording generates interrupt entry and exit events when
interrupt entries are dispatched.

% Generated from spec:/acfg/if/record-per-processor-items

```{raw} latex
\clearpage
```

```{index} CONFIGURE_RECORD_PER_PROCESSOR_ITEMS
```

(configure-record-per-processor-items)=

## CONFIGURE_RECORD_PER_PROCESSOR_ITEMS

```{eval-rst}
.. rubric:: CONSTANT:
```

`CONFIGURE_RECORD_PER_PROCESSOR_ITEMS`

```{eval-rst}
.. rubric:: OPTION TYPE:
```

This configuration option is an integer define.

```{eval-rst}
.. rubric:: DEFAULT VALUE:
```

The default value is 0.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The value of this configuration option defines the event record item count
per processor.

```{eval-rst}
.. rubric:: NOTES:
```

The event record buffers are statically allocated for each configured
processor ({ref}`CONFIGURE_MAXIMUM_PROCESSORS`). If the value of this
configuration option is zero, then nothing is allocated.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this configuration option:

- The value of the configuration option shall be greater than or equal to 16.
- The value of the configuration option shall be less than or equal to
  [SIZE_MAX](https://en.cppreference.com/w/c/types/limits).
- The value of the configuration option shall be a power of two.
- The value of the configuration option shall be less than or equal to a
  BSP-specific and application-specific value which depends on the size of the
  memory available to the application.
