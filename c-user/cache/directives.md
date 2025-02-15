.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Pavel Pisa
.. Copyright (C) 2014, 2024 embedded brains GmbH & Co. KG
.. Copyright (C) 2000, 2008 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. _CacheManagerDirectives:

Directives
==========

This section details the directives of the Cache Manager. A subsection is
dedicated to each of this manager's directives and lists the calling sequence,
parameters, description, return values, and notes of the directive.

.. Generated from spec:/rtems/cache/if/flush-multiple-data-lines

.. raw:: latex

    \clearpage

.. index:: rtems_cache_flush_multiple_data_lines()

.. _InterfaceRtemsCacheFlushMultipleDataLines:

rtems_cache_flush_multiple_data_lines()
---------------------------------------

Flushes the data cache lines covering the memory area.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_flush_multiple_data_lines( const void *begin, size_t size );

.. rubric:: PARAMETERS:

``begin``
    This parameter is the begin address of the memory area to flush.

``size``
    This parameter is the size in bytes of the memory area to flush.

.. rubric:: DESCRIPTION:

Dirty data cache lines covering the area are transfered to memory.  Depending
on the cache implementation this may mark the lines as invalid.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/invalidate-multiple-data-lines

.. raw:: latex

    \clearpage

.. index:: rtems_cache_invalidate_multiple_data_lines()

.. _InterfaceRtemsCacheInvalidateMultipleDataLines:

rtems_cache_invalidate_multiple_data_lines()
--------------------------------------------

Invalidates the data cache lines covering the memory area.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_invalidate_multiple_data_lines(
      const void *begin,
      size_t      size
    );

.. rubric:: PARAMETERS:

``begin``
    This parameter is the begin address of the memory area to invalidate.

``size``
    This parameter is the size in bytes of the memory area to invalidate.

.. rubric:: DESCRIPTION:

The cache lines covering the area are marked as invalid.  A later read access
in the area will load the data from memory.

.. rubric:: NOTES:

In case the area is not aligned on cache line boundaries, then this operation
may destroy unrelated data.

On some systems, the cache lines may be flushed before they are invalidated.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/invalidate-multiple-instruction-lines

.. raw:: latex

    \clearpage

.. index:: rtems_cache_invalidate_multiple_instruction_lines()

.. _InterfaceRtemsCacheInvalidateMultipleInstructionLines:

rtems_cache_invalidate_multiple_instruction_lines()
---------------------------------------------------

Invalidates the instruction cache lines covering the memory area.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_invalidate_multiple_instruction_lines(
      const void *begin,
      size_t      size
    );

.. rubric:: PARAMETERS:

``begin``
    This parameter is the begin address of the memory area to invalidate.

``size``
    This parameter is the size in bytes of the memory area to invalidate.

.. rubric:: DESCRIPTION:

The cache lines covering the area are marked as invalid.  A later instruction
fetch from the area will result in a load from memory.

.. rubric:: NOTES:

In SMP configurations, on processors without instruction cache snooping, this
operation will invalidate the instruction cache lines on all processors.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/instruction-sync-after-code-change

.. raw:: latex

    \clearpage

.. index:: rtems_cache_instruction_sync_after_code_change()

.. _InterfaceRtemsCacheInstructionSyncAfterCodeChange:

rtems_cache_instruction_sync_after_code_change()
------------------------------------------------

Ensures necessary synchronization required after code changes.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_instruction_sync_after_code_change(
      const void *begin,
      size_t      size
    );

.. rubric:: PARAMETERS:

``begin``
    This parameter is the begin address of the code area to synchronize.

``size``
    This parameter is the size in bytes of the code area to synchronize.

.. rubric:: NOTES:

When code is loaded or modified, then most systems require synchronization
instructions to update the instruction caches so that the loaded or modified
code is fetched.  For example, systems with separate data and instruction
caches or systems without instruction cache snooping.  The directives should be
used by run time loader for example.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/get-maximal-line-size

.. raw:: latex

    \clearpage

.. index:: rtems_cache_get_maximal_line_size()

.. _InterfaceRtemsCacheGetMaximalLineSize:

rtems_cache_get_maximal_line_size()
-----------------------------------

Gets the maximal cache line size in bytes of all caches (data, instruction, or
unified).

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_cache_get_maximal_line_size( void );

.. rubric:: RETURN VALUES:

``0``
    There is no cache present.

Returns the maximal cache line size in bytes of all caches (data, instruction,
or unified).

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/get-data-line-size

.. raw:: latex

    \clearpage

.. index:: rtems_cache_get_data_line_size()

.. _InterfaceRtemsCacheGetDataLineSize:

rtems_cache_get_data_line_size()
--------------------------------

Gets the data cache line size in bytes.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_cache_get_data_line_size( void );

.. rubric:: RETURN VALUES:

``0``
    There is no data cache present.

Returns the data cache line size in bytes.  For multi-level caches this is the
maximum of the cache line sizes of all levels.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/get-instruction-line-size

.. raw:: latex

    \clearpage

.. index:: rtems_cache_get_instruction_line_size()

.. _InterfaceRtemsCacheGetInstructionLineSize:

rtems_cache_get_instruction_line_size()
---------------------------------------

Gets the instruction cache line size in bytes.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_cache_get_instruction_line_size( void );

.. rubric:: RETURN VALUES:

``0``
    There is no instruction cache present.

Returns the instruction cache line size in bytes.  For multi-level caches this
is the maximum of the cache line sizes of all levels.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/get-data-size

.. raw:: latex

    \clearpage

.. index:: rtems_cache_get_data_cache_size()

.. _InterfaceRtemsCacheGetDataCacheSize:

rtems_cache_get_data_cache_size()
---------------------------------

Gets the data cache size in bytes for the cache level.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_cache_get_data_cache_size( uint32_t level );

.. rubric:: PARAMETERS:

``level``
    This parameter is the requested data cache level.  The cache level zero
    specifies the entire data cache.

.. rubric:: RETURN VALUES:

``0``
    There is no data cache present at the requested cache level.

Returns the data cache size in bytes of the requested cache level.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/get-instruction-size

.. raw:: latex

    \clearpage

.. index:: rtems_cache_get_instruction_cache_size()

.. _InterfaceRtemsCacheGetInstructionCacheSize:

rtems_cache_get_instruction_cache_size()
----------------------------------------

Gets the instruction cache size in bytes for the cache level.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    size_t rtems_cache_get_instruction_cache_size( uint32_t level );

.. rubric:: PARAMETERS:

``level``
    This parameter is the requested instruction cache level.  The cache level
    zero specifies the entire instruction cache.

.. rubric:: RETURN VALUES:

``0``
    There is no instruction cache present at the requested cache level.

Returns the instruction cache size in bytes of the requested cache level.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/flush-entire-data

.. raw:: latex

    \clearpage

.. index:: rtems_cache_flush_entire_data()

.. _InterfaceRtemsCacheFlushEntireData:

rtems_cache_flush_entire_data()
-------------------------------

Flushes the entire data cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_flush_entire_data( void );

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/invalidate-entire-data

.. raw:: latex

    \clearpage

.. index:: rtems_cache_invalidate_entire_data()

.. _InterfaceRtemsCacheInvalidateEntireData:

rtems_cache_invalidate_entire_data()
------------------------------------

Invalidates the entire data cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_invalidate_entire_data( void );

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/invalidate-entire-instruction

.. raw:: latex

    \clearpage

.. index:: rtems_cache_invalidate_entire_instruction()

.. _InterfaceRtemsCacheInvalidateEntireInstruction:

rtems_cache_invalidate_entire_instruction()
-------------------------------------------

Invalidates the entire instruction cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_invalidate_entire_instruction( void );

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/enable-data

.. raw:: latex

    \clearpage

.. index:: rtems_cache_enable_data()

.. _InterfaceRtemsCacheEnableData:

rtems_cache_enable_data()
-------------------------

Enables the data cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_enable_data( void );

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/disable-data

.. raw:: latex

    \clearpage

.. index:: rtems_cache_disable_data()

.. _InterfaceRtemsCacheDisableData:

rtems_cache_disable_data()
--------------------------

Disables the data cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_disable_data( void );

.. rubric:: NOTES:

On some :term:`targets <target>` or configurations, calling this directive may
cause a fatal error with a fatal source of :ref:`INTERNAL_ERROR_CORE
<FatalErrorSources>` and fatal code of
:ref:`INTERNAL_ERROR_CANNOT_DISABLE_DATA_CACHE <internal_errors>`.   The data
cache may be necessary to provide :term:`atomic operations`. In SMP
configurations, the data cache may be required to ensure data coherency.  See
the BSP documentation in the *RTEMS User Manual* for more information.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/enable-instruction

.. raw:: latex

    \clearpage

.. index:: rtems_cache_enable_instruction()

.. _InterfaceRtemsCacheEnableInstruction:

rtems_cache_enable_instruction()
--------------------------------

Enables the instruction cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_enable_instruction( void );

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/disable-instruction

.. raw:: latex

    \clearpage

.. index:: rtems_cache_disable_instruction()

.. _InterfaceRtemsCacheDisableInstruction:

rtems_cache_disable_instruction()
---------------------------------

Disables the instruction cache.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_cache_disable_instruction( void );

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/cache/if/aligned-malloc

.. raw:: latex

    \clearpage

.. index:: rtems_cache_aligned_malloc()

.. _InterfaceRtemsCacheAlignedMalloc:

rtems_cache_aligned_malloc()
----------------------------

Allocates memory from the C Program Heap which begins at a cache line boundary.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void *rtems_cache_aligned_malloc( size_t size );

.. rubric:: PARAMETERS:

``size``
    This parameter is the size in bytes of the memory area to allocate.

.. rubric:: RETURN VALUES:

`NULL <https://en.cppreference.com/w/c/types/NULL>`_
    There is not enough memory available to satisfy the allocation request.

Returns the begin address of the allocated memory.  The begin address is on a
cache line boundary.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within device driver initialization context.

* The directive may be called from within task context.

* The directive may obtain and release the object allocator mutex.  This may
  cause the calling task to be preempted.
