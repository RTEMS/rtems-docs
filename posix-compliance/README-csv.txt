7 April 2021

The .cvs file is exported from a spreadsheet used to track the status
of RTEMS versus various POSIX related standards. The spreadsheet
is maintained and managed outside the RTEMS Documentation. The
spreadsheet is versioned but that is not reflected in the name
"RTEMS-Standards-Compliance.csv". The version of the spreadsheet included
currently is:

v15 - 1 June 2021

This is the information in each column:

  Methods
  Header File
  IEEE Std 1003.1-2017
  IEEE Std 1003.1-2008
  IEEE Std 1003.1-2003
  PSE51
  PSE52
  PSE53
  PSE54
  C99
  C11
  FACE 2.1 Security
  FACE 2.1 Safety Base
  FACE 2.1 Safety Extended
  FACE 2.1 General Purpose
  FACE 3.0 Security
  FACE 3.0 Safety Base
  FACE 3.0 Safety Extended
  FACE 3.0 General Purpose
  FACE 3.1 Security
  FACE 3.1 Safety Base
  FACE 3.1 Safety Extended
  FACE 3.1 General Purpose
  SCA 2.2.2 AEP
  SCA 4.1 Ultra Lightweight AEP
  SCA 4.1 Lightweight AEP
  SCA 4.1 [Full] AEP
  RTEMS w/o Networking
  RTEMS w/ Networking
  Deos RTEMS Safety Base
  Deos RTEMS Safety Ext
  Deos RTEMS Gen Purp
  RTEMS Impl Note
  POSIX Functionality Categories

NOTE: "RTEMS w/Networking" uses the rtems-libbsd network stack.

Information on each standard is included in the chapter "Standards"
which can be found in standards.rst.

For the standards columns, the cells are blank to indicate not
required or "INCL" to indicate required.

For the RTEMS columns, the following values are used:

CTS-YES  - FACE Conformance Test Suite reports present
CTS-NO   - FACE Conformance Test Suite reports not present
RT-YES   - RTEMS specific probe test reports present
RT-NO    - RTEMS specific probe test reports not present
HAND-YES - Override by hand to indicate RTEMS supports this

The "RTEMS Impl Notes" column has the following values:

+ ENOSYS to indicate the method is a stub that sets errno to ENOSYS and
  returns -1
+ SUSP to indicate the method is limited due to the Single Use,
  Single Process nature of RTEMS.

