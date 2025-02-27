% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2011.

% COMMENT: On-Line Applications Research Corporation (OAR).

```{index} TImespec Helpers
```

# Timespec Helpers

## Introduction

The Timespec helpers manager provides directives to assist in manipulating
instances of the POSIX `struct timespec` structure.

The directives provided by the timespec helpers manager are:

- [rtems_timespec_set] - Set timespec's value
- [rtems_timespec_zero] - Zero timespec's value
- [rtems_timespec_is_valid] - Check if timespec is valid
- [rtems_timespec_add_to] - Add two timespecs
- [rtems_timespec_subtract] - Subtract two timespecs
- [rtems_timespec_divide] - Divide two timespecs
- [rtems_timespec_divide_by_integer] - Divide timespec by integer
- [rtems_timespec_less_than] - Less than operator
- [rtems_timespec_greater_than] - Greater than operator
- [rtems_timespec_equal_to] - Check if two timespecs are equal
- [rtems_timespec_get_seconds] - Obtain seconds portion of timespec
- [rtems_timespec_get_nanoseconds] - Obtain nanoseconds portion of timespec
- [rtems_timespec_to_ticks] - Convert timespec to number of ticks
- [rtems_timespec_from_ticks] - Convert ticks to timespec

## Background

### Time Storage Conventions

Time can be stored in many ways. One of them is the `struct timespec` format
which is a structure that consists of the fields `tv_sec` to represent
seconds and `tv_nsec` to represent nanoseconds. The\`\`struct timeval\`\`
structure is simular and consists of seconds (stored in `tv_sec`) and
microseconds (stored in `tv_usec`). Either\`\`struct timespec\`\` or `struct timeval` can be used to represent elapsed time, time of executing some
operations, or time of day.

## Operations

### Set and Obtain Timespec Value

A user may write a specific time by passing the desired seconds and nanoseconds
values and the destination `struct timespec` using the `rtems_timespec_set`
directive.

The `rtems_timespec_zero` directive is used to zero the seconds
and nanoseconds portions of a `struct timespec` instance.

Users may obtain the seconds or nanoseconds portions of a `struct timespec`
instance with the `rtems_timespec_get_seconds` or
`rtems_timespec_get_nanoseconds` methods, respectively.

### Timespec Math

A user can perform multiple operations on `struct timespec` instances. The
helpers in this manager assist in adding, subtracting, and performing divison
on `struct timespec` instances.

- Adding two `struct timespec` can be done using the
  `rtems_timespec_add_to` directive. This directive is used mainly to
  calculate total amount of time consumed by multiple operations.
- The `rtems_timespec_subtract` is used to subtract two `struct timespecs`
  instances and determine the elapsed time between those two points in time.
- The `rtems_timespec_divide` is used to use to divide one `struct timespec` instance by another. This calculates the percentage with a
  precision to three decimal points.
- The `rtems_timespec_divide_by_integer` is used to divide a `struct timespec` instance by an integer. It is commonly used in benchmark
  calculations to dividing duration by the number of iterations performed.

### Comparing struct timespec Instances

A user can compare two `struct timespec` instances using the
`rtems_timespec_less_than`, `rtems_timespec_greater_than` or
`rtems_timespec_equal_to` routines.

### Conversions and Validity Check

Conversion to and from clock ticks may be performed by using the
`rtems_timespec_to_ticks` and `rtems_timespec_from_ticks` directives.

User can also check validity of timespec with `rtems_timespec_is_valid`
routine.

## Directives

This section details the Timespec Helpers manager's directives. A subsection
is dedicated to each of this manager's directives and describes the calling
sequence, related constants, usage, and status codes.

```{raw} latex
\clearpage
```

```{index} set struct timespec instance
```

```{index} rtems_timespec_set()
```

(rtems_timespec_set)=

### TIMESPEC_SET - Set struct timespec Instance

CALLING SEQUENCE:
: ```c
  void rtems_timespec_set(
      struct timespec *time,
      time_t           seconds,
      uint32_t         nanoseconds
  );
  ```

DIRECTIVE STATUS CODES:
: NONE

DESCRIPTION:
: This directive sets the `struct timespec` *time* to the desired
  `seconds` and `nanoseconds` values.

NOTES:
: This method does NOT check if `nanoseconds` is less than the maximum
  number of nanoseconds in a second.

```{raw} latex
\clearpage
```

```{index} rtems_timespec_zero()
```

(rtems_timespec_zero)=

### TIMESPEC_ZERO - Zero struct timespec Instance

CALLING SEQUENCE:
: ```c
  void rtems_timespec_zero(
      struct timespec *time
  );
  ```

DIRECTIVE STATUS CODES:
: NONE

DESCRIPTION:
: This routine sets the contents of the `struct timespec` instance `time` to
  zero.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_is_valid()
```

(rtems_timespec_is_valid)=

### TIMESPEC_IS_VALID - Check validity of a struct timespec instance

CALLING SEQUENCE:
: ```c
  bool rtems_timespec_is_valid(
      const struct timespec *time
  );
  ```

DIRECTIVE STATUS CODES:
: This method returns `true` if the instance is valid, and `false`
  otherwise.

DESCRIPTION:
: This routine check validity of a `struct timespec` instance. It checks if
  the nanoseconds portion of the `struct timespec` instanceis in allowed
  range (less than the maximum number of nanoseconds per second).

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_add_to()
```

(rtems_timespec_add_to)=

### TIMESPEC_ADD_TO - Add Two struct timespec Instances

CALLING SEQUENCE:
: ```c
  uint32_t rtems_timespec_add_to(
      struct timespec       *time,
      const struct timespec *add
  );
  ```

DIRECTIVE STATUS CODES:
: The method returns the number of seconds `time` increased by.

DESCRIPTION:
: This routine adds two `struct timespec` instances. The second argument is
  added to the first. The parameter `time` is the base time to which the
  `add` parameter is added.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_subtract()
```

(rtems_timespec_subtract)=

### TIMESPEC_SUBTRACT - Subtract Two struct timespec Instances

CALLING SEQUENCE:
: ```c
  void rtems_timespec_subtract(
      const struct timespec *start,
      const struct timespec *end,
      struct timespec       *result
  );
  ```

DIRECTIVE STATUS CODES:
: NONE

DESCRIPTION:
: This routine subtracts `start` from `end` saves the difference in
  `result`. The primary use of this directive is to calculate elapsed time.

NOTES:
: It is possible to subtract when `end` is less than `start` and it
  produce negative `result`. When doing this you should be careful and
  remember that only the seconds portion of a `struct timespec` instance is
  signed, which means that nanoseconds portion is always increasing. Due to
  that when your timespec has seconds = -1 and nanoseconds = 500,000,000 it
  means that result is -0.5 second, NOT the expected -1.5!

```{raw} latex
\clearpage
```

```{index} rtems_timespec_divide()
```

(rtems_timespec_divide)=

### TIMESPEC_DIVIDE - Divide Two struct timespec Instances

CALLING SEQUENCE:
: ```c
  void rtems_timespec_divide(
      const struct timespec *lhs,
      const struct timespec *rhs,
      uint32_t              *ival_percentage,
      uint32_t              *fval_percentage
  );
  ```

DIRECTIVE STATUS CODES:

: NONE

DESCRIPTION:

: This routine divides the `struct timespec` instance `lhs` by the
  `struct timespec` instance `rhs`. The result is returned in the
  `ival_percentage` and `fval_percentage`, representing the integer and
  fractional results of the division respectively.

  The `ival_percentage` is integer value of calculated percentage and
  `fval_percentage` is fractional part of calculated percentage.

NOTES:

: The intended use is calculating percentges to three decimal points.

  When dividing by zero, this routine return both `ival_percentage` and
  `fval_percentage` equal zero.

  The division is performed using exclusively integer operations.

```{raw} latex
\clearpage
```

```{index} rtems_timespec_divide_by_integer()
```

(rtems_timespec_divide_by_integer)=

### TIMESPEC_DIVIDE_BY_INTEGER - Divide a struct timespec Instance by an Integer

CALLING SEQUENCE:
: ```c
  int rtems_timespec_divide_by_integer(
      const struct timespec *time,
      uint32_t               iterations,
      struct timespec       *result
  );
  ```

DIRECTIVE STATUS CODES:
: NONE

DESCRIPTION:
: This routine divides the `struct timespec` instance `time` by the
  integer value `iterations`. The result is saved in `result`.

NOTES:
: The expected use is to assist in benchmark calculations where you typically
  divide a duration (`time`) by a number of iterations what gives average
  time.

```{raw} latex
\clearpage
```

```{index} rtems_timespec_less_than()
```

(rtems_timespec_less_than)=

### TIMESPEC_LESS_THAN - Less than operator

CALLING SEQUENCE:
: ```c
  bool rtems_timespec_less_than(
      const struct timespec *lhs,
      const struct timespec *rhs
  );
  ```

DIRECTIVE STATUS CODES:
: This method returns `struct true` if `lhs` is less than `rhs` and
  `struct false` otherwise.

DESCRIPTION:
: This method is the less than operator for `struct timespec`
  instances. The first parameter is the left hand side and the second is the
  right hand side of the comparison.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_greater_than()
```

(rtems_timespec_greater_than)=

### TIMESPEC_GREATER_THAN - Greater than operator

CALLING SEQUENCE:
: ```c
  bool rtems_timespec_greater_than(
      const struct timespec *_lhs,
      const struct timespec *_rhs
  );
  ```

DIRECTIVE STATUS CODES:
: This method returns `struct true` if `lhs` is greater than `rhs` and
  `struct false` otherwise.

DESCRIPTION:
: This method is greater than operator for `struct timespec` instances.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_equal_to()
```

(rtems_timespec_equal_to)=

### TIMESPEC_EQUAL_TO - Check equality of timespecs

CALLING SEQUENCE:
: ```c
  bool rtems_timespec_equal_to(
      const struct timespec *lhs,
      const struct timespec *rhs
  );
  ```

DIRECTIVE STATUS CODES:
: This method returns `struct true` if `lhs` is equal to `rhs` and
  `struct false` otherwise.

DESCRIPTION:
: This method is equality operator for `struct timespec` instances.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_get_seconds()
```

(rtems_timespec_get_seconds)=

### TIMESPEC_GET_SECONDS - Get Seconds Portion of struct timespec Instance

CALLING SEQUENCE:
: ```c
  time_t rtems_timespec_get_seconds(
      struct timespec *time
  );
  ```

DIRECTIVE STATUS CODES:
: This method returns the seconds portion of the specified `struct timespec` instance.

DESCRIPTION:
: This method returns the seconds portion of the specified `struct timespec` instance `time`.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_get_nanoseconds()
```

(rtems_timespec_get_nanoseconds)=

### TIMESPEC_GET_NANOSECONDS - Get Nanoseconds Portion of the struct timespec Instance

CALLING SEQUENCE:
: ```c
  uint32_t rtems_timespec_get_nanoseconds(
      struct timespec *_time
  );
  ```

DIRECTIVE STATUS CODES:
: This method returns the nanoseconds portion of the specified `struct timespec` instance.

DESCRIPTION:
: This method returns the nanoseconds portion of the specified timespec which
  is pointed by `_time`.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_to_ticks()
```

(rtems_timespec_to_ticks)=

### TIMESPEC_TO_TICKS - Convert struct timespec Instance to Ticks

CALLING SEQUENCE:
: ```c
  uint32_t rtems_timespec_to_ticks(
      const struct timespec *time
  );
  ```

DIRECTIVE STATUS CODES:
: This directive returns the number of ticks computed.

DESCRIPTION:
: This directive converts the `time` timespec to the corresponding number
  of clock ticks.

NOTES:
: NONE

```{raw} latex
\clearpage
```

```{index} rtems_timespec_from_ticks()
```

(rtems_timespec_from_ticks)=

### TIMESPEC_FROM_TICKS - Convert Ticks to struct timespec Representation

CALLING SEQUENCE:
: ```c
  void rtems_timespec_from_ticks(
      uint32_t         ticks,
      struct timespec *time
  );
  ```

DIRECTIVE STATUS CODES:
: NONE

DESCRIPTION:
: This routine converts the `ticks` to the corresponding `struct timespec` representation and stores it in `time`.

NOTES:
: NONE
