.. SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: Text Written by Jake Janovetz
.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Testing the Driver
##################

Preliminary Setup
=================

The network used to test the driver should include at least:

- The hardware on which the driver is to run.  It makes testing much easier if
  you can run a debugger to control the operation of the target machine.

- An Ethernet network analyzer or a workstation with an 'Ethernet snoop'
  program such as ``ethersnoop`` or ``tcpdump``.

- A workstation.

During early debug, you should consider putting the target, workstation, and
snooper on a small network by themselves.  This offers a few advantages:

- There is less traffic to look at on the snooper and for the target to process
  while bringing the driver up.

- Any serious errors will impact only your small network not a building or
  campus network.  You want to avoid causing any unnecessary problems.

- Test traffic is easier to repeatably generate.

- Performance measurements are not impacted by other systems on the network.

Debug Output
============

There are a number of sources of debug output that can be enabled to aid in
tracing the behavior of the network stack.  The following is a list of them:

- mbuf activity
  There are commented out calls to ``printf`` in the file ``sys/mbuf.h`` in the
  network stack code.  Uncommenting these lines results in output when mbuf's
  are allocated and freed.  This is very useful for finding memory leaks.

- TX and RX queuing
  There are commented out calls to ``printf`` in the file ``net/if.h`` in the
  network stack code.  Uncommenting these lines results in output when packets
  are placed on or removed from one of the transmit or receive packet queues.
  These queues can be viewed as the boundary line between a device driver and
  the network stack.  If the network stack is enqueuing packets to be
  transmitted that the device driver is not dequeuing, then that is indicative
  of a problem in the transmit side of the device driver.  Conversely, if the
  device driver is enqueueing packets as it receives them (via a call to
  ``ether_input``) and they are not being dequeued by the network stack, then
  there is a problem.  This situation would likely indicate that the network
  server task is not running.

- TCP state transitions

  In the unlikely event that one would actually want to see TCP state
  transitions, the ``TCPDEBUG`` macro can be defined in the file
  ``opt_tcpdebug.h``.  This results in the routine ``tcp_trace()`` being called
  by the network stack and the state transitions logged into the ``tcp_debug``
  data structure.  If the variable ``tcpconsdebug`` in the file
  ``netinet/tcp_debug.c`` is set to ``1``, then the state transitions will also
  be printed to the console.

Monitor Commands
================

There are a number of command available in the shell / monitor to aid in
tracing the behavior of the network stack.  The following is a list of them:

- ``inet``
  This command shows the current routing information for the TCP/IP
  stack. Following is an example showing the output of this command.

  .. code-block:: shell

      Destination     Gateway/Mask/Hw    Flags     Refs     Use Expire Interface
      10.0.0.0        255.0.0.0          U           0        0     17 smc1
      127.0.0.1       127.0.0.1          UH          0        0      0 lo0

  In this example, there is only one network interface with an IP address of
  10.8.1.1.  This link is currently not up.  Two routes that are shown are the
  default routes for the Ethernet interface (10.0.0.0) and the loopback
  interface (127.0.0.1).  Since the stack comes from BSD, this command is very
  similar to the netstat command.  For more details on the network routing
  please look the following URL:
  (http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/network-routing.html)
  For a quick reference to the flags, see the table below:

  '``U``'
      Up: The route is active.

  '``H``'
      Host: The route destination is a single host.

  '``G``'
      Gateway: Send anything for this destination on to this remote system,
      which will figure out from there where to send it.

  '``S``'
      Static: This route was configured manually, not automatically generated
      by the system.

  '``C``'
      Clone: Generates a new route based upon this route for machines we
      connect to. This type of route is normally used for local networks.

  '``W``'
      WasCloned: Indicated a route that was auto-configured based upon a local
      area network (Clone) route.

  '``L``'
      Link: Route involves references to Ethernet hardware.

- ``mbuf``
  This command shows the current MBUF statistics.  An example of the command is
  shown below:

  .. code-block:: shell

      ************ MBUF STATISTICS ************
      mbufs:4096    clusters: 256    free: 241
      drops:   0       waits:   0  drains:   0
      free:4080          data:16          header:0           socket:0
      pcb:0             rtable:0          htable:0           atable:0
      soname:0          soopts:0          ftable:0           rights:0
      ifaddr:0         control:0         oobdata:0

- ``if``
  This command shows the current statistics for your Ethernet driver as long as
  the ioctl hook ``SIO_RTEMS_SHOW_STATS`` has been implemented.  Below is an
  example:

  .. code-block:: shell

      ************ INTERFACE STATISTICS ************
      ***** smc1 *****
      Ethernet Address: 00:12:76:43:34:25
      Address:10.8.1.1        Broadcast Address:10.255.255.255  Net mask:255.0.0.0
      Flags: Up Broadcast Running Simplex
      Send queue limit:50   length:0    Dropped:0
      SMC91C111 RTEMS driver A0.01 11/03/2002 Ian Caddy (ianc@microsol.iinet.net.au)
      Rx Interrupts:0              Not First:0               Not Last:0
      Giant:0                           Runt:0              Non-octet:0
      Bad CRC:0                      Overrun:0              Collision:0
      Tx Interrupts:2               Deferred:0        Missed Hearbeat:0
      No Carrier:0          Retransmit Limit:0         Late Collision:0
      Underrun:0             Raw output wait:0              Coalesced:0
      Coalesce failed:0                Retries:0
      ***** lo0 *****
      Address:127.0.0.1       Net mask:255.0.0.0
      Flags: Up Loopback Running Multicast
      Send queue limit:50   length:0    Dropped:0

- ``ip``
  This command show the IP statistics for the currently configured interfaces.

- ``icmp``
  This command show the ICMP statistics for the currently configured interfaces.

- ``tcp``
  This command show the TCP statistics for the currently configured interfaces.

- ``udp``
  This command show the UDP statistics for the currently configured interfaces.

Driver basic operation
======================

The network demonstration program ``netdemo`` may be used for these tests.

- Edit ``networkconfig.h`` to reflect the values for your network.

- Start with ``RTEMS_USE_BOOTP`` not defined.

- Edit ``networkconfig.h`` to configure the driver with an explicit Ethernet
  and Internet address and with reception of broadcast packets disabled: Verify
  that the program continues to run once the driver has been attached.

- Issue a '``u``' command to send UDP packets to the 'discard' port.  Verify
  that the packets appear on the network.

- Issue a '``s``' command to print the network and driver statistics.

- On a workstation, add a static route to the target system.

- On that same workstation try to 'ping' the target system.
  Verify that the ICMP echo request and reply packets appear on the net.

- Remove the static route to the target system.  Modify ``networkconfig.h`` to
  attach the driver with reception of broadcast packets enabled.  Try to 'ping'
  the target system again.  Verify that ARP request/reply and ICMP echo
  request/reply packets appear on the net.

- Issue a '``t``' command to send TCP packets to the 'discard' port.  Verify
  that the packets appear on the network.

- Issue a '``s``' command to print the network and driver statistics.

- Verify that you can telnet to ports 24742 and 24743 on the target system from
  one or more workstations on your network.

BOOTP/DHCP operation
====================

Set up a BOOTP/DHCP server on the network.  Set define ``RTEMS USE_BOOT`` in
``networkconfig.h``.  Run the ``netdemo`` test program.  Verify that the target
system configures itself from the BOOTP/DHCP server and that all the above
tests succeed.

Stress Tests
============

Once the driver passes the tests described in the previous section it should be
subjected to conditions which exercise it more thoroughly and which test its
error handling routines.

Giant packets
-------------

- Recompile the driver with ``MAXIMUM_FRAME_SIZE`` set to a smaller value,
  say 514.

- 'Ping' the driver from another workstation and verify that frames larger than
  514 bytes are correctly rejected.

- Recompile the driver with ``MAXIMUM_FRAME_SIZE`` restored  to 1518.

Resource Exhaustion
-------------------

- Edit ``networkconfig.h`` so that the driver is configured with just two
  receive and transmit descriptors.

- Compile and run the ``netdemo`` program.

- Verify that the program operates properly and that you can still telnet to
  both the ports.

- Display the driver statistics (Console '``s``' command or telnet 'control-G'
  character) and verify that:

  #. The number of transmit interrupts is non-zero.  This indicates that all
     transmit descriptors have been in use at some time.

  #. The number of missed packets is non-zero.  This indicates that all receive
     descriptors have been in use at some time.

Cable Faults
------------

- Run the ``netdemo`` program.

- Issue a '``u``' console command to make the target machine transmit a bunch
  of UDP packets.

- While the packets are being transmitted, disconnect and reconnect the network
  cable.

- Display the network statistics and verify that the driver has detected the
  loss of carrier.

- Verify that you can still telnet to both ports on the target machine.

Throughput
----------

Run the ``ttcp`` network benchmark program.  Transfer large amounts of data
(100's of megabytes) to and from the target system.

The procedure for testing throughput from a host to an RTEMS target is as
follows:

 #. Download and start the ttcp program on the Target.

 #. In response to the ``ttcp`` prompt, enter ``-s -r``.  The meaning of these
    flags is described in the ``ttcp.1`` manual page found in the ``ttcp_orig``
    subdirectory.

 #. On the host run ``ttcp -s -t <<insert the hostname or IP address of  the Target here>>``

The procedure for testing throughput from an RTEMS target to a Host is as
follows:

 #. On the host run ``ttcp -s -r``.

 #. Download and start the ttcp program on the Target.

 #. In response to the ``ttcp`` prompt, enter ``-s -t <<insert the hostname or
    IP address of the Target here>>``.  You need to type the IP address of the
    host unless your Target is talking to your Domain Name Server.

To change the number of buffers, the buffer size, etc. you just add the extra
flags to the ``-t`` machine as specified in the ``ttcp.1`` manual page found in
the ``ttcp_orig`` subdirectory.
