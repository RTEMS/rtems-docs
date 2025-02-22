% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 2009 On-Line Applications Research Corporation (OAR)

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

(objectservicesdirectives)=

# Directives

This section details the directives of the Object Services. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/object/if/build-id

```{raw} latex
\clearpage
```

```{index} rtems_build_id()
```

(interfacertemsbuildid)=

## rtems_build_id()

Builds the object identifier from the API, class, MPCI node, and index
components.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_id rtems_build_id(
  uint32_t api,
  uint32_t the_class,
  uint32_t node,
  uint32_t index
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`api`
: This parameter is the API of the object identifier to build.

`the_class`
: This parameter is the class of the object identifier to build.

`node`
: This parameter is the MPCI node of the object identifier to build.

`index`
: This parameter is the index of the object identifier to build.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the object identifier built from the API, class, MPCI node, and index
components.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/build-name

```{raw} latex
\clearpage
```

```{index} rtems_build_name()
```

(interfacertemsbuildname)=

## rtems_build_name()

Builds the object name composed of the four characters.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_name rtems_build_name( char c1, char c2, char c3, char c4 );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`c1`
: This parameter is the first character of the name.

`c2`
: This parameter is the second character of the name.

`c3`
: This parameter is the third character of the name.

`c4`
: This parameter is the fourth character of the name.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive takes the four characters provided as arguments and composes a
32-bit object name with `c1` in the most significant 8-bits and `c4` in the
least significant 8-bits.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the object name composed of the four characters.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/get-classic-name

```{raw} latex
\clearpage
```

```{index} rtems_object_get_classic_name()
```

(interfacertemsobjectgetclassicname)=

## rtems_object_get_classic_name()

Gets the object name associated with the object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_object_get_classic_name(
  rtems_id    id,
  rtems_name *name
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier to get the name.

`name`
: This parameter is the pointer to an {ref}`InterfaceRtemsName` object. When
  the directive call is successful, the object name associated with the
  object identifier will be stored in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `name` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`
: There was no object information available for the object identifier.

{c:macro}`RTEMS_INVALID_ID`
: The object name associated with the object identifier was a string.

{c:macro}`RTEMS_INVALID_ID`
: There was no object associated with the object identifier.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/get-name

```{raw} latex
\clearpage
```

```{index} rtems_object_get_name()
```

(interfacertemsobjectgetname)=

## rtems_object_get_name()

Gets the object name associated with the object identifier as a string.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
char *rtems_object_get_name( rtems_id id, size_t length, char *name );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier to get the name.

`length`
: This parameter is the buffer length in bytes.

`name`
: This parameter is the pointer to a buffer of the specified length.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The object name is stored in the name buffer. If the name buffer length is
greater than zero, then the stored object name will be `NUL` terminated. The
stored object name may be truncated to fit the length. There is no indication
if a truncation occurred. Every attempt is made to return name as a printable
string even if the object has the Classic API 32-bit integer style name.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

[NULL](https://en.cppreference.com/w/c/types/NULL)
: The `length` parameter was 0.

[NULL](https://en.cppreference.com/w/c/types/NULL)
: The `name` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

[NULL](https://en.cppreference.com/w/c/types/NULL)
: There was no object information available for the object identifier.

[NULL](https://en.cppreference.com/w/c/types/NULL)
: There was no object associated with the object identifier.

Returns the `name` parameter value, if there is an object name associated
with the object identifier.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/set-name

```{raw} latex
\clearpage
```

```{index} rtems_object_set_name()
```

(interfacertemsobjectsetname)=

## rtems_object_set_name()

Sets the object name of the object associated with the object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_object_set_name( rtems_id id, const char *name );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier of the object to set the name.

`name`
: This parameter is the object name to set.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

This directive will set the object name based upon the user string.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `name` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_ID`
: There was no object information available for the object identifier.

{c:macro}`RTEMS_INVALID_ID`
: There was no object associated with the object identifier.

{c:macro}`RTEMS_NO_MEMORY`
: There was no memory available to duplicate the name.

```{eval-rst}
.. rubric:: NOTES:
```

This directive can be used to set the name of objects which do not have a
naming scheme per their API.

If the object specified by `id` is of a class that has a string name, this
directive will free the existing name to the RTEMS Workspace and allocate
enough memory from the RTEMS Workspace to make a copy of the string located at
`name`.

If the object specified by `id` is of a class that has a 32-bit integer style
name, then the first four characters in `name` will be used to construct the
name.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.
- The directive may be called from within task context.
- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-get-api

```{raw} latex
\clearpage
```

```{index} rtems_object_id_get_api()
```

(interfacertemsobjectidgetapi)=

## rtems_object_id_get_api()

Gets the API component of the object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_id_get_api( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier with the API component to get.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the API component of the object identifier.

```{eval-rst}
.. rubric:: NOTES:
```

This directive does not validate the object identifier provided in `id`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-get-class

```{raw} latex
\clearpage
```

```{index} rtems_object_id_get_class()
```

(interfacertemsobjectidgetclass)=

## rtems_object_id_get_class()

Gets the class component of the object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_id_get_class( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier with the class component to get.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the class component of the object identifier.

```{eval-rst}
.. rubric:: NOTES:
```

This directive does not validate the object identifier provided in `id`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-get-node

```{raw} latex
\clearpage
```

```{index} rtems_object_id_get_node()
```

(interfacertemsobjectidgetnode)=

## rtems_object_id_get_node()

Gets the MPCI node component of the object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_id_get_node( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier with the MPCI node component to
  get.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the MPCI node component of the object identifier.

```{eval-rst}
.. rubric:: NOTES:
```

This directive does not validate the object identifier provided in `id`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-get-index

```{raw} latex
\clearpage
```

```{index} rtems_object_id_get_index()
```

(interfacertemsobjectidgetindex)=

## rtems_object_id_get_index()

Gets the index component of the object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_id_get_index( rtems_id id );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`id`
: This parameter is the object identifier with the index component to get.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the index component of the object identifier.

```{eval-rst}
.. rubric:: NOTES:
```

This directive does not validate the object identifier provided in `id`.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-api-minimum

```{raw} latex
\clearpage
```

```{index} rtems_object_id_api_minimum()
```

(interfacertemsobjectidapiminimum)=

## rtems_object_id_api_minimum()

Gets the lowest valid value for the API component of an object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_id_api_minimum( void );
```

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the lowest valid value for the API component of an object identifier.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-api-maximum

```{raw} latex
\clearpage
```

```{index} rtems_object_id_api_maximum()
```

(interfacertemsobjectidapimaximum)=

## rtems_object_id_api_maximum()

Gets the highest valid value for the API component of an object identifier.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_id_api_maximum( void );
```

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the highest valid value for the API component of an object identifier.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive is implemented by a macro and may be called from within C/C++
  constant expressions. In addition, a function implementation of the
  directive exists for bindings to other programming languages.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/api-minimum-class

```{raw} latex
\clearpage
```

```{index} rtems_object_api_minimum_class()
```

(interfacertemsobjectapiminimumclass)=

## rtems_object_api_minimum_class()

Gets the lowest valid class value of the object API.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_api_minimum_class( int api );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`api`
: This parameter is the object API to get the lowest valid class value.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`-1`
: The object API was invalid.

Returns the lowest valid class value of the object API.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/api-maximum-class

```{raw} latex
\clearpage
```

```{index} rtems_object_api_maximum_class()
```

(interfacertemsobjectapimaximumclass)=

## rtems_object_api_maximum_class()

Gets the highest valid class value of the object API.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
int rtems_object_api_maximum_class( int api );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`api`
: This parameter is the object API to get the highest valid class value.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`0`
: The object API was invalid.

Returns the highest valid class value of the object API.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/get-api-name

```{raw} latex
\clearpage
```

```{index} rtems_object_get_api_name()
```

(interfacertemsobjectgetapiname)=

## rtems_object_get_api_name()

Gets a descriptive name of the object API.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
const char *rtems_object_get_api_name( int api );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`api`
: This parameter is the object API to get the name.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

"BAD API"
: The API was invalid.

Returns a descriptive name of the API, if the API was valid.

```{eval-rst}
.. rubric:: NOTES:
```

The string returned is from constant space. Do not modify or free it.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/get-api-class-name

```{raw} latex
\clearpage
```

```{index} rtems_object_get_api_class_name()
```

(interfacertemsobjectgetapiclassname)=

## rtems_object_get_api_class_name()

Gets a descriptive name of the object class of the object API.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
const char *rtems_object_get_api_class_name( int the_api, int the_class );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`the_api`
: This parameter is the object API of the object class.

`the_class`
: This parameter is the object class of the object API to get the name.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

"BAD API"
: The API was invalid.

"BAD CLASS"
: The class of the API was invalid.

Returns a descriptive name of the class of the API, if the class of the API and
the API were valid.

```{eval-rst}
.. rubric:: NOTES:
```

The string returned is from constant space. Do not modify or free it.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/get-class-information

```{raw} latex
\clearpage
```

```{index} rtems_object_get_class_information()
```

(interfacertemsobjectgetclassinformation)=

## rtems_object_get_class_information()

Gets the object class information of the object class of the object API.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_status_code rtems_object_get_class_information(
  int                                 the_api,
  int                                 the_class,
  rtems_object_api_class_information *info
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`the_api`
: This parameter is the object API of the object class.

`the_class`
: This parameter is the object class of the object API to get the class
  information.

`info`
: This parameter is the pointer to an
  {ref}`InterfaceRtemsObjectApiClassInformation` object. When the directive
  call is successful, the object class information of the class of the API
  will be stored in this object.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

{c:macro}`RTEMS_SUCCESSFUL`
: The requested operation was successful.

{c:macro}`RTEMS_INVALID_ADDRESS`
: The `info` parameter was [NULL](https://en.cppreference.com/w/c/types/NULL).

{c:macro}`RTEMS_INVALID_NUMBER`
: The class of the API or the API was invalid.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/get-local-node

```{raw} latex
\clearpage
```

```{index} rtems_object_get_local_node()
```

(interfacertemsobjectgetlocalnode)=

## rtems_object_get_local_node()

Gets the local MPCI node number.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
uint16_t rtems_object_get_local_node( void );
```

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the local MPCI node number.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/object/if/id-initial

```{raw} latex
\clearpage
```

```{index} RTEMS_OBJECT_ID_INITIAL()
```

(interfacertemsobjectidinitial)=

## RTEMS_OBJECT_ID_INITIAL()

Builds the object identifier with the lowest index from the API, class, and
MPCI node components.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```c
rtems_id RTEMS_OBJECT_ID_INITIAL(
  uint32_t api,
  uint32_t class,
  uint32_t node
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`api`
: This parameter is the API of the object identifier to build.

`class`
: This parameter is the class of the object identifier to build.

`node`
: This parameter is the MPCI node of the object identifier to build.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns the object identifier with the lowest index built from the API, class,
and MPCI node components.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.
- The directive will not cause the calling task to be preempted.
