% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Aaron Nyholm

```{index} IO Device
```

```{index} iodev
```
# Directives

## API

API functions for creating and destroying a `rtems_iodev`.

### rtems_iodev_alloc_and_init

Allocates and initialises an `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
rtems_iodev *rtems_iodev_alloc_and_init(
    size_t size
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`size`
: This parameter is the size allocated. Must be equal or larger then the size of `rtems_iodev`.


```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns pointer to allocated and initialised `rtems_iodev`.

### rtems_iodev_init

Initialises an `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int rtems_iodev_init(
    rtems_iodev *iodev
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev` to be initialised.


```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

A successfully registered `rtems_iodev` can only be destroyed by unregistering it
using `rtems_iodev_unregister`.

### rtems_iodev_register

Registers an `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int rtems_iodev_register(
    rtems_iodev *iodev,
    const char *iodev_path
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev` to be registers.

`iodev_path`
: This parameter is a pointer to a string containing the path to create the device node at.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

A successfully registered `rtems_iodev` can only be destroyed by unregistering it
using `rtems_iodev_unregister`.

### rtems_iodev_unregister_and_destroy

Unregisters and destroys an `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int rtems_iodev_unregister(
    const char *iodev_path
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev_path`
: This parameter is a pointer to a string containing the path to `rtems_iodev` to unregister.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### rtems_iodev_destroy_unregistered

Destroys an unregistered `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_iodev_destroy_unregistered(
    rtems_iodev *iodev,
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev` to be destroyed.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

Can only be called on a non-registered `rtems_iodev`.

## iodev Device Driver Functions

IO device driver functions. These need to be set by the device driver after initalisation
but before registration.

### get_device_info

Returns device information via a void pointer.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int get_device_info(
    rtems_iodev *iodev,
    void *info
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

`info`
: This parameter is a pointer to a device driver specific struct containing device information.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### get_event_count

Returns number of events for a given `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int get_event_count(
    rtems_iodev *iodev,
    size_t *event_count
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

`event_count`
: This parameter is a pointer to a `size_t` where the number of events will be placed.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### get_event_info

Returns event information for requested event in a given `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int get_event_info(
    rtems_iodev *iodev,
    rtems_iodev_event_info *event_info
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

`event_info`
: This parameter is a pointer to a `rtems_iodev_event_info` with the index of the
requested event and fields for returned information.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### event_wait

Waits for the requested event for a given `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int get_event_info(
    rtems_iodev *iodev,
    rtems_iodev_event_args *event_args
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

`event_args`
: This parameter is a pointer to a `rtems_iodev_event_args` with the index of the
requested event and other arguments.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### get_regions

Gets the array of `rtems_iodev_regions` for a given `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int get_event_info(
    rtems_iodev *iodev,
    rtems_iodev_regions **regions
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

`regions`
: This parameter is a pointer to an array of `rtems_iodev_regions` returned by the call.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### get_region_count

Gets the number of regions for a given `rtems_iodev`.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
int get_event_info(
    rtems_iodev *iodev,
    size_t *region_count
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

`region_count`
: This parameter is a pointer a `size_t` set by the call containing the number of regions.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

Returns 0 on success and non-zero value on error.

### priv_destroy

Destroys private data held by the device driver as the `rtems_iodev` is destroyed.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void priv_destroy(
    rtems_iodev *iodev,
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`iodev`
: This parameter is a pointer to the `rtems_iodev`.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

None.
