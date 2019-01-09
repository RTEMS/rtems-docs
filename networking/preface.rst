.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: Written by Eric Norum
.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Preface
#######

This document describes the RTEMS specific parts of the FreeBSD TCP/IP stack.
Much of this documentation was written by Eric Norum (eric@skatter.usask.ca) of
the Saskatchewan Accelerator Laboratory who also ported the FreeBSD TCP/IP
stack to RTEMS.

The following is a list of resources which should be useful in trying to
understand Ethernet:

- *Charles Spurgeon's Ethernet Web Site*
  "This site provides extensive information about Ethernet (IEEE 802.3) local
  area network (LAN) technology. Including the original 10 Megabit per second
  (Mbps) system, the 100 Mbps Fast Ethernet system (802.3u), and the Gigabit
  Ethernet system (802.3z)."  The URL is:
  (http://www.ethermanage.com/ethernet/ethernet.html)

- *TCP/IP Illustrated, Volume 1 : The Protocols*
  by W. Richard Stevens (ISBN: 0201633469)
  This book provides detailed introduction to TCP/IP and includes diagnostic
  programs which are publicly available.

- *TCP/IP Illustrated, Volume 2 : The Implementation*
  by W. Richard Stevens and Gary Wright (ISBN: 020163354X)
  This book focuses on implementation issues regarding TCP/IP.  The
  treat for RTEMS users is that the implementation covered is the BSD
  stack with most of the source code described in detail.

- *UNIX Network Programming, Volume 1 : 2nd Edition*
  by W. Richard Stevens (ISBN: 0-13-490012-X)
  This book describes how to write basic TCP/IP applications, again with primary
  focus on the BSD stack.
