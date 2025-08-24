% SPDX-License-Identifier: CC-BY-SA-4.0

(network_services)=

# Network Services

```{index} RTEMS Network Services
```

```{index} Net Services
```

RTEMS Network Services (RNS) is a set of libraries and test applications that
can be used on top of any of the available network stacks that are compatible
with RTEMS. RNS is usable with any BSP that has network support and has no
configuration in that regard.

RNS provides the following libraries:

- NTP - A port of the ntp.org library used to synchronize time across the
  network
- TTCP - Test Transmission Control Protocol, used to perform network throughput
  tests

RNS provides test applications for NTP, TTCP, and telnetd. The telnetd library
currently resides in the RTEMS repository.

Basic installation and usage instructions can be found in README.md in the
package repository:

<https://gitlab.rtems.org/rtems/pkg/rtems-network-services>
