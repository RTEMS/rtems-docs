% SPDX-License-Identifier: CC-BY-SA-4.0

(legacy_network_stack)=

# RTEMS Legacy Network Stack

```{index} RTEMS Legacy Network Stack
```

```{index} Legacy Network Stack
```

This document describes the RTEMS specific parts of the legacy FreeBSD TCP/IP
stack. The stack is based on a old version of the FreeBSD network stack. A lot
of RTEMS specific changes have been added and there is no realistic chance to
ever update it to a newer FreeBSD version. There will be no further development
of this stack. If you start with a new target, please select one of the other
network stacks that support RTEMS.

```{toctree}
preface
quick_start
network_task_structure
networking_driver
using_networking_rtems_app
testing_the_driver
network_servers
dec_21140
command
```
