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

% Generated from spec:/rtems/cache/if/group

(CacheManagerIntroduction)=

# Introduction

% The following list was generated from:
% spec:/rtems/cache/if/flush-multiple-data-lines
% spec:/rtems/cache/if/invalidate-multiple-data-lines
% spec:/rtems/cache/if/invalidate-multiple-instruction-lines
% spec:/rtems/cache/if/instruction-sync-after-code-change
% spec:/rtems/cache/if/get-maximal-line-size
% spec:/rtems/cache/if/get-data-line-size
% spec:/rtems/cache/if/get-instruction-line-size
% spec:/rtems/cache/if/get-data-size
% spec:/rtems/cache/if/get-instruction-size
% spec:/rtems/cache/if/flush-entire-data
% spec:/rtems/cache/if/invalidate-entire-data
% spec:/rtems/cache/if/invalidate-entire-instruction
% spec:/rtems/cache/if/enable-data
% spec:/rtems/cache/if/disable-data
% spec:/rtems/cache/if/enable-instruction
% spec:/rtems/cache/if/disable-instruction
% spec:/rtems/cache/if/aligned-malloc

The Cache Manager provides functions to perform maintenance operations for data
and instruction caches.

The actual actions of the Cache Manager operations depend on the hardware and
the implementation provided by the CPU architecture port or a board support
package. Cache implementations tend to be highly hardware dependent. The
directives provided by the Cache Manager are:

- {ref}`InterfaceRtemsCacheFlushMultipleDataLines` - Flushes the data cache
  lines covering the memory area.

- {ref}`InterfaceRtemsCacheInvalidateMultipleDataLines` - Invalidates the data
  cache lines covering the memory area.

- {ref}`InterfaceRtemsCacheInvalidateMultipleInstructionLines` - Invalidates
  the instruction cache lines covering the memory area.

- {ref}`InterfaceRtemsCacheInstructionSyncAfterCodeChange` - Ensures necessary
  synchronization required after code changes.

- {ref}`InterfaceRtemsCacheGetMaximalLineSize` - Gets the maximal cache line
  size in bytes of all caches (data, instruction, or unified).

- {ref}`InterfaceRtemsCacheGetDataLineSize` - Gets the data cache line size in
  bytes.

- {ref}`InterfaceRtemsCacheGetInstructionLineSize` - Gets the instruction cache
  line size in bytes.

- {ref}`InterfaceRtemsCacheGetDataCacheSize` - Gets the data cache size in
  bytes for the cache level.

- {ref}`InterfaceRtemsCacheGetInstructionCacheSize` - Gets the instruction
  cache size in bytes for the cache level.

- {ref}`InterfaceRtemsCacheFlushEntireData` - Flushes the entire data cache.

- {ref}`InterfaceRtemsCacheInvalidateEntireData` - Invalidates the entire data
  cache.

- {ref}`InterfaceRtemsCacheInvalidateEntireInstruction` - Invalidates the
  entire instruction cache.

- {ref}`InterfaceRtemsCacheEnableData` - Enables the data cache.

- {ref}`InterfaceRtemsCacheDisableData` - Disables the data cache.

- {ref}`InterfaceRtemsCacheEnableInstruction` - Enables the instruction cache.

- {ref}`InterfaceRtemsCacheDisableInstruction` - Disables the instruction
  cache.

- {ref}`InterfaceRtemsCacheAlignedMalloc` - Allocates memory from the C Program
  Heap which begins at a cache line boundary.
