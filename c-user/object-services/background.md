% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

# Background

## APIs

RTEMS implements multiple APIs including an Internal API, the Classic API, and
the POSIX API. These APIs share the common foundation of SuperCore objects and
thus share object management code. This includes a common scheme for object Ids
and for managing object names whether those names be in the thirty-two bit form
used by the Classic API or C strings.

The object Id contains a field indicating the API that an object instance is
associated with. This field holds a numerically small non-zero integer.

## Object Classes

Each API consists of a collection of managers. Each manager is responsible for
instances of a particular object class. Classic API Tasks and POSIX Mutexes
example classes.

The object Id contains a field indicating the class that an object instance is
associated with. This field holds a numerically small non-zero integer. In
all APIs, a class value of one is reserved for tasks or threads.

## Object Names

Every RTEMS object which has an Id may also have a name associated with it.
Depending on the API, names may be either thirty-two bit integers as in the
Classic API or strings as in the POSIX API.

Some objects have Ids but do not have a defined way to associate a name with
them. For example, POSIX threads have Ids but per POSIX do not have names. In
RTEMS, objects not defined to have thirty-two bit names may have string names
assigned to them via the `rtems_object_set_name` service. The original
impetus in providing this service was so the normally anonymous POSIX threads
could have a user defined name in CPU Usage Reports.
