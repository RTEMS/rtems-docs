% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2016 Pavel Pisa
% Copyright (C) 2014, 2024 embedded brains GmbH & Co. KG
% Copyright (C) 2000, 2008 On-Line Applications Research Corporation (OAR)

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

(CacheManagerDirectives)=

# Directives

This section details the directives of the Cache Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

% Generated from spec:/rtems/cache/if/flush-multiple-data-lines

```{raw} latex
\clearpage
```

```{index} rtems_cache_flush_multiple_data_lines()
```

(InterfaceRtemsCacheFlushMultipleDataLines)=

## rtems_cache_flush_multiple_data_lines()

Flushes the data cache lines covering the memory area.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_flush_multiple_data_lines( const void *begin, size_t size );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`begin`
: This parameter is the begin address of the memory area to flush.

`size`
: This parameter is the size in bytes of the memory area to flush.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

Dirty data cache lines covering the area are transfered to memory. Depending on
the cache implementation this may mark the lines as invalid.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/invalidate-multiple-data-lines

```{raw} latex
\clearpage
```

```{index} rtems_cache_invalidate_multiple_data_lines()
```

(InterfaceRtemsCacheInvalidateMultipleDataLines)=

## rtems_cache_invalidate_multiple_data_lines()

Invalidates the data cache lines covering the memory area.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_invalidate_multiple_data_lines(
  const void *begin,
  size_t      size
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`begin`
: This parameter is the begin address of the memory area to invalidate.

`size`
: This parameter is the size in bytes of the memory area to invalidate.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The cache lines covering the area are marked as invalid. A later read access in
the area will load the data from memory.

```{eval-rst}
.. rubric:: NOTES:
```

In case the area is not aligned on cache line boundaries, then this operation
may destroy unrelated data.

On some systems, the cache lines may be flushed before they are invalidated.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/invalidate-multiple-instruction-lines

```{raw} latex
\clearpage
```

```{index} rtems_cache_invalidate_multiple_instruction_lines()
```

(InterfaceRtemsCacheInvalidateMultipleInstructionLines)=

## rtems_cache_invalidate_multiple_instruction_lines()

Invalidates the instruction cache lines covering the memory area.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_invalidate_multiple_instruction_lines(
  const void *begin,
  size_t      size
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`begin`
: This parameter is the begin address of the memory area to invalidate.

`size`
: This parameter is the size in bytes of the memory area to invalidate.

```{eval-rst}
.. rubric:: DESCRIPTION:
```

The cache lines covering the area are marked as invalid. A later instruction
fetch from the area will result in a load from memory.

```{eval-rst}
.. rubric:: NOTES:
```

In SMP configurations, on processors without instruction cache snooping, this
operation will invalidate the instruction cache lines on all processors.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/instruction-sync-after-code-change

```{raw} latex
\clearpage
```

```{index} rtems_cache_instruction_sync_after_code_change()
```

(InterfaceRtemsCacheInstructionSyncAfterCodeChange)=

## rtems_cache_instruction_sync_after_code_change()

Ensures necessary synchronization required after code changes.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_instruction_sync_after_code_change(
  const void *begin,
  size_t      size
);
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`begin`
: This parameter is the begin address of the code area to synchronize.

`size`
: This parameter is the size in bytes of the code area to synchronize.

```{eval-rst}
.. rubric:: NOTES:
```

When code is loaded or modified, then most systems require synchronization
instructions to update the instruction caches so that the loaded or modified
code is fetched. For example, systems with separate data and instruction caches
or systems without instruction cache snooping. The directives should be used by
run time loader for example.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/get-maximal-line-size

```{raw} latex
\clearpage
```

```{index} rtems_cache_get_maximal_line_size()
```

(InterfaceRtemsCacheGetMaximalLineSize)=

## rtems_cache_get_maximal_line_size()

Gets the maximal cache line size in bytes of all caches (data, instruction, or
unified).

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
size_t rtems_cache_get_maximal_line_size( void );
```

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`0`
: There is no cache present.

Returns the maximal cache line size in bytes of all caches (data, instruction,
or unified).

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/get-data-line-size

```{raw} latex
\clearpage
```

```{index} rtems_cache_get_data_line_size()
```

(InterfaceRtemsCacheGetDataLineSize)=

## rtems_cache_get_data_line_size()

Gets the data cache line size in bytes.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
size_t rtems_cache_get_data_line_size( void );
```

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`0`
: There is no data cache present.

Returns the data cache line size in bytes. For multi-level caches this is the
maximum of the cache line sizes of all levels.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/get-instruction-line-size

```{raw} latex
\clearpage
```

```{index} rtems_cache_get_instruction_line_size()
```

(InterfaceRtemsCacheGetInstructionLineSize)=

## rtems_cache_get_instruction_line_size()

Gets the instruction cache line size in bytes.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
size_t rtems_cache_get_instruction_line_size( void );
```

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`0`
: There is no instruction cache present.

Returns the instruction cache line size in bytes. For multi-level caches this
is the maximum of the cache line sizes of all levels.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/get-data-size

```{raw} latex
\clearpage
```

```{index} rtems_cache_get_data_cache_size()
```

(InterfaceRtemsCacheGetDataCacheSize)=

## rtems_cache_get_data_cache_size()

Gets the data cache size in bytes for the cache level.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
size_t rtems_cache_get_data_cache_size( uint32_t level );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`level`
: This parameter is the requested data cache level. The cache level zero
  specifies the entire data cache.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`0`
: There is no data cache present at the requested cache level.

Returns the data cache size in bytes of the requested cache level.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/get-instruction-size

```{raw} latex
\clearpage
```

```{index} rtems_cache_get_instruction_cache_size()
```

(InterfaceRtemsCacheGetInstructionCacheSize)=

## rtems_cache_get_instruction_cache_size()

Gets the instruction cache size in bytes for the cache level.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
size_t rtems_cache_get_instruction_cache_size( uint32_t level );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`level`
: This parameter is the requested instruction cache level. The cache level zero
  specifies the entire instruction cache.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

`0`
: There is no instruction cache present at the requested cache level.

Returns the instruction cache size in bytes of the requested cache level.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/flush-entire-data

```{raw} latex
\clearpage
```

```{index} rtems_cache_flush_entire_data()
```

(InterfaceRtemsCacheFlushEntireData)=

## rtems_cache_flush_entire_data()

Flushes the entire data cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_flush_entire_data( void );
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/invalidate-entire-data

```{raw} latex
\clearpage
```

```{index} rtems_cache_invalidate_entire_data()
```

(InterfaceRtemsCacheInvalidateEntireData)=

## rtems_cache_invalidate_entire_data()

Invalidates the entire data cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_invalidate_entire_data( void );
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/invalidate-entire-instruction

```{raw} latex
\clearpage
```

```{index} rtems_cache_invalidate_entire_instruction()
```

(InterfaceRtemsCacheInvalidateEntireInstruction)=

## rtems_cache_invalidate_entire_instruction()

Invalidates the entire instruction cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_invalidate_entire_instruction( void );
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/enable-data

```{raw} latex
\clearpage
```

```{index} rtems_cache_enable_data()
```

(InterfaceRtemsCacheEnableData)=

## rtems_cache_enable_data()

Enables the data cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_enable_data( void );
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/disable-data

```{raw} latex
\clearpage
```

```{index} rtems_cache_disable_data()
```

(InterfaceRtemsCacheDisableData)=

## rtems_cache_disable_data()

Disables the data cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_disable_data( void );
```

```{eval-rst}
.. rubric:: NOTES:
```

On some {term}`targets <target>` or configurations, calling this directive may
cause a fatal error with a fatal source of
{ref}`INTERNAL_ERROR_CORE <FatalErrorSources>` and fatal code of
{ref}`INTERNAL_ERROR_CANNOT_DISABLE_DATA_CACHE <internal_errors>`. The data
cache may be necessary to provide {term}`atomic operations`. In SMP
configurations, the data cache may be required to ensure data coherency. See
the BSP documentation in the *RTEMS User Manual* for more information.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/enable-instruction

```{raw} latex
\clearpage
```

```{index} rtems_cache_enable_instruction()
```

(InterfaceRtemsCacheEnableInstruction)=

## rtems_cache_enable_instruction()

Enables the instruction cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_enable_instruction( void );
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/disable-instruction

```{raw} latex
\clearpage
```

```{index} rtems_cache_disable_instruction()
```

(InterfaceRtemsCacheDisableInstruction)=

## rtems_cache_disable_instruction()

Disables the instruction cache.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void rtems_cache_disable_instruction( void );
```

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within any runtime context.

- The directive will not cause the calling task to be preempted.

% Generated from spec:/rtems/cache/if/aligned-malloc

```{raw} latex
\clearpage
```

```{index} rtems_cache_aligned_malloc()
```

(InterfaceRtemsCacheAlignedMalloc)=

## rtems_cache_aligned_malloc()

Allocates memory from the C Program Heap which begins at a cache line boundary.

```{eval-rst}
.. rubric:: CALLING SEQUENCE:
```

```{code-block} c
void *rtems_cache_aligned_malloc( size_t size );
```

```{eval-rst}
.. rubric:: PARAMETERS:
```

`size`
: This parameter is the size in bytes of the memory area to allocate.

```{eval-rst}
.. rubric:: RETURN VALUES:
```

[NULL](https://en.cppreference.com/w/c/types/NULL)
: There is not enough memory available to satisfy the allocation request.

Returns the begin address of the allocated memory. The begin address is on a
cache line boundary.

```{eval-rst}
.. rubric:: CONSTRAINTS:
```

The following constraints apply to this directive:

- The directive may be called from within device driver initialization context.

- The directive may be called from within task context.

- The directive may obtain and release the object allocator mutex. This may
  cause the calling task to be preempted.
