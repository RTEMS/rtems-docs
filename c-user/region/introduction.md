% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG
% Copyright (C) 1988, 2008 On-Line Applications Research Corporation (OAR)

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

% Generated from spec:/rtems/region/if/group

(RegionManagerIntroduction)=

# Introduction

% The following list was generated from:
% spec:/rtems/region/if/create
% spec:/rtems/region/if/ident
% spec:/rtems/region/if/delete
% spec:/rtems/region/if/extend
% spec:/rtems/region/if/get-segment
% spec:/rtems/region/if/return-segment
% spec:/rtems/region/if/resize-segment
% spec:/rtems/region/if/get-information
% spec:/rtems/region/if/get-free-information
% spec:/rtems/region/if/get-segment-size

The Region Manager provides facilities to dynamically allocate memory in
variable sized units. The directives provided by the Region Manager are:

- {ref}`InterfaceRtemsRegionCreate` - Creates a region.

- {ref}`InterfaceRtemsRegionIdent` - Identifies a region by the object name.

- {ref}`InterfaceRtemsRegionDelete` - Deletes the region.

- {ref}`InterfaceRtemsRegionExtend` - Extends the region.

- {ref}`InterfaceRtemsRegionGetSegment` - Gets a segment from the region.

- {ref}`InterfaceRtemsRegionReturnSegment` - Returns the segment to the region.

- {ref}`InterfaceRtemsRegionResizeSegment` - Changes the size of the segment.

- {ref}`InterfaceRtemsRegionGetInformation` - Gets the region information.

- {ref}`InterfaceRtemsRegionGetFreeInformation` - Gets the region free
  information.

- {ref}`InterfaceRtemsRegionGetSegmentSize` - Gets the size of the region
  segment.
