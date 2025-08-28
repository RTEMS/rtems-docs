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

% Generated from spec:/rtems/dpmem/if/group

(DualPortedMemoryManagerIntroduction)=

# Introduction

% The following list was generated from:
% spec:/rtems/dpmem/if/create
% spec:/rtems/dpmem/if/ident
% spec:/rtems/dpmem/if/delete
% spec:/rtems/dpmem/if/external-to-internal
% spec:/rtems/dpmem/if/internal-to-external

The Dual-Ported Memory Manager provides a mechanism for converting addresses
between internal and external representations for multiple dual-ported memory
areas (DPMA). The directives provided by the Dual-Ported Memory Manager are:

- {ref}`InterfaceRtemsPortCreate` - Creates a port.

- {ref}`InterfaceRtemsPortIdent` - Identifies a port by the object name.

- {ref}`InterfaceRtemsPortDelete` - Deletes the port.

- {ref}`InterfaceRtemsPortExternalToInternal` - Converts the external address
  to the internal address.

- {ref}`InterfaceRtemsPortInternalToExternal` - Converts the internal address
  to the external address.
