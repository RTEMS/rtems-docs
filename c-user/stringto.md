% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Prashant Rahul

```{index} stringto
```

```{index} libmisc
```

# Stringto utility

## Introduction

The stringto library is a set of wrapper functions around the standard string
to numeric conversion functions `strto*()`. Their goal is to provide a more
consistent and safe interface to work with.

## Background

The standard `strto*()` functions are quite inconsistent in how they handle
and return errors. For example, passing a NULL as an input string causes
`strto*()` functions to cause a segmentation violation in glibc. Whereas
RTEMS `rtems_stringto_*` functions return an error code indicating what went
wrong. RTEMS's stringto library tries to handle these cases.

## Operations

stringto functions can be used in the following patterns:

### Converting to integers

Converting to integers is very similar to how they are in standard `strto*`
functions. They take an input string, a pointer to the output value, an
optional ending pointer, and the base of the number.

```c
#include <rtems/stringto.h>
#include <rtems/status.h>

rtems_status_code status;

int outi;
status = rtems_string_to_int( "67", &outi, NULL, 10 );
assert( status == RTEMS_SUCCESSFUL );
assert( outi == 67 );

unsigned long outul;
status = rtems_string_to_unsigned_long( "0xA", &outul, NULL, 16 );
assert( status == RTEMS_SUCCESSFUL );
assert( outul == 10 );
```

### Converting to floats

Converting to floats is also very similar to how they are in standard `strto*`
functions. They take an input string, a pointer to the output value, an
optional ending pointer.

```c
#include <rtems/stringto.h>
#include <rtems/status.h>

rtems_status_code status;

double outd;
status = rtems_string_to_double( "141.23", &outd, NULL );
assert( status == RTEMS_SUCCESSFUL );
assert( outd == 141.23 );

float outf;
status = rtems_string_to_float( "56.57", &outf, NULL );
assert( status == RTEMS_SUCCESSFUL );
assert( outf == 56.57f );
```

### Handling errors

The stringto functions provide meaningful information with their return value.

```c
#include <rtems/stringto.h>
#include <rtems/status.h>

rtems_status_code status;

/* overflow and underflow */
int outi;
status = rtems_string_to_int( "987654321123456789123456789", &outi, NULL, 10 );
assert( status == RTEMS_INVALID_NUMBER );

status = rtems_string_to_int( "-987654321123456789123456789", &outi, NULL, 10 );
assert( status == RTEMS_INVALID_NUMBER );

/* bad value */
double outd;
status = rtems_string_to_double( "zzz", &outd, NULL );
assert( status == RTEMS_NOT_DEFINED );

/* empty string */
status = rtems_string_to_double( "", &outd, NULL );
assert( status == RTEMS_NOT_DEFINED );

/* NULL for input string or return value  */
status = rtems_string_to_double( NULL, &outd, NULL );
assert( status == RTEMS_INVALID_ADDRESS );

status = rtems_string_to_double( "23.5", NULL, NULL );
assert( status == RTEMS_INVALID_ADDRESS );
```

## Functions

The stringto library provides the following functions:

```c
rtems_status_code rtems_string_to_pointer(const char *s, void **n, char **endptr);
rtems_status_code rtems_string_to_unsigned_char(const char *s, unsigned char *n, char **endptr, int base);
rtems_status_code rtems_string_to_int(const char *s, int *n, char **endptr, int base);
rtems_status_code rtems_string_to_unsigned_int(const char *s, unsigned int *n, char **endptr, int base);
rtems_status_code rtems_string_to_long(const char *s, long *n, char **endptr, int base);
rtems_status_code rtems_string_to_unsigned_long(const char *s, unsigned long *n, char **endptr, int base);
rtems_status_code rtems_string_to_long_long(const char *s, long long *n, char **endptr, int base);
rtems_status_code rtems_string_to_unsigned_long_long(const char *s, unsigned long long *n, char **endptr, int base);
rtems_status_code rtems_string_to_float(const char *s, float *n, char **endptr);
rtems_status_code rtems_string_to_double(const char *s, double *n, char **endptr);
rtems_status_code rtems_string_to_long_double(const char *s, long double *n, char **endptr);
```

Each allowing conversion from string to different types.
