
The .cvs file is exported from a spreadsheet used to track the
status of RTEMS versus various POSIX related standards. 

This is the information in each column:

1 - Master List of Methods
2 - Header File
3 - IEEE Std 1003.1-2008 API
4 - PSE51
5 - PSE52
6 - PSE53
7 - PSE54
8 - C99
9 - FACE 2.1  Security
10 - FACE 2.1 Safety Base
11 - FACE 2.1 Safety Extended
12 - FACE 2.1 General-Purpose
13 - RTEMS w/o Networking
14 - RTEMS w/ Networking
15 - Deos RTEMS Safety Base
16 - Deos RTEMS Safety Ext
17 - Deos RTEMS Gen Purp
18 - RTEMS Impl Note
19 - POSIX Functionality Categories
20 - misc 

NOTE: Column 13 uses the rtems-libbsd network stack.

For the standards columns, the cells are blank to indicate not
required or "INCL" to indicate required.

For the RTEMS colums, the following values are used:

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

