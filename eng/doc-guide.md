% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 embedded brains GmbH & Co. KG

(docguide)=

# Documentation Guidelines

## Application Configuration Options

Add at least an index entry and a label for the configuration option. Use a
pattern of `CONFIGURE_[A-Z0-9_]+` for the option name. Use the following
template for application configuration feature options:

```rst
.. index:: CONFIGURE_FEATURE

.. _CONFIGURE_FEATURE:

CONFIGURE_FEATURE
-----------------

CONSTANT:
    ``CONFIGURE_FEATURE``

OPTION TYPE:
    This configuration option is a boolean feature define.

DEFAULT CONFIGURATION:
    If this configuration option is undefined, then the described feature is not
    enabled.

DESCRIPTION:
    In case this configuration option is defined, then feature happens.

NOTES:
    Keep the description short.  Add all special cases, usage notes, error
    conditions, configuration dependencies, references, etc. here to the notes.
```

Use the following template for application configuration integer and
initializer options:

```rst
.. index:: CONFIGURE_VALUE

.. _CONFIGURE_VALUE:

CONFIGURE_VALUE
-----------------

CONSTANT:
    ``CONFIGURE_VALUE``

OPTION TYPE:
    This configuration option is an integer (or initializer) define.

DEFAULT VALUE:
    The default value is X.

VALUE CONSTRAINTS:
    The value of this configuration option shall satisfy all of the following
    constraints:

    * It shall be greater than or equal to A.

    * It shall be less than or equal to B.

    * It shall meet C.

DESCRIPTION:
    The value of this configuration option defines the Y of Z in W.

NOTES:
    Keep the description short.  Add all special cases, usage notes, error
    conditions, configuration dependencies, references, etc. here to the notes.
```
