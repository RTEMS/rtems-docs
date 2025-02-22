% SPDX-License-Identifier: CC-BY-SA-4.0

# Quick Start

This legacy networking is now a standalone repository and needs to be built
separately.

The repository can be found here:
<https://gitlab.rtems.org/rtems/pkg/rtems-net-legacy>

There's an RSB recipe to build rtems-net-legacy. Here's an example of building
rtems-net-legacy using RSB for powerpc/beatnik BSP with rtems version 6:

> ```shell
> ../source-builder/sb-set-builder \
> --prefix=/path/to/rtems/prefix \
> 6/rtems-net-legacy \
> --host=powerpc-rtems6 \
> --with-rtems-bsp=beatnik
> ```

Manually building the rtems-net-legacy repo:

> ```shell
> git submodule init
> git submodule update
> ./waf configure --prefix=/path/to/rtems/prefix
> ./waf
> ./waf install
> ```

Please refer to README.waf in rtems-net-legacy repository for more details on
using waf with legacy networking.
