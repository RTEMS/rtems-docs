% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2019 embedded brains GmbH & Co. KG

% Copyright (C) 2019 Sebastian Huber

% Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

(QuickStartPrefixes)=

# Choose an Installation Prefix

```{index} prefix
```

You will see the term {ref:term}`prefix` referred to throughout this
documentation and in a wide number of software packages you can download from
the internet. It is also used in the
[GNU Coding Standard](https://www.gnu.org/prep/standards/html_node/Directory-Variables.html).
A *prefix* is the path on your host computer a software package is installed
under. Packages that have a prefix will place all parts under the prefix
path. Packages for your host computer typically use a default prefix of
{file}`/usr/local` on FreeBSD and Linux.

You have to select a prefix for your installation. You will build and install
the RTEMS tool suite, an RTEMS kernel for a BSP, and you may build and install
third party libraries. You can build all the parts as a stack with a single
prefix or you can separate various parts by providing different prefixes to
each part as it is built. Using separate prefixes is for experienced RTEMS
users.

Do not select a prefix that is under the top of any of the source trees. The
prefix collects the install output of the various build steps you take in this
guide and need to be kept separate from the sources used.

The RTEMS tool suite consists of a cross tool chain (Binutils, GCC, GDB,
Newlib, etc.) for your target architecture and {ref}`RTEMS tools <HostTools>`
provided by the RTEMS Project. The RTEMS Tools are a toolkit that help create
the RTEMS ecosystem and help support the building of embedded real-time
applications and systems.
The RTEMS tool chain changes less often than the RTEMS kernel. One method of
working with development releases is to have a separate `prefix` for the RTEMS
tools and a different one for the RTEMS kernel. You can then update each
without interacting with the other. You can also have a number of RTEMS
versions available to test with.

You build and install the tool suite with the {ref}`RTEMS Source Builder (RSB) <RSB>`. By default, the RSB will start the prefix path with a host operating
system specific path plus {file}`rtems`, and the RTEMS version, e.g.
{file}`/opt/rtems/@rtems-ver-major@` on Linux, and {file}`/usr/local/rtems/@rtems-ver-major@` on FreeBSD and
macOS. Placing the RTEMS version number in the path lets you manage and
migrate RTEMS versions as they are released. It is best to
have a `prefix` for each different version of RTEMS you are using. If you are
using RTEMS in production it is **not** a good idea to install a development
version of over the top by using the same `prefix`. A separate `prefix` for each
version avoids this.

It is strongly recommended to run the RSB as a *normal user* and not with
*root* privileges (also known as *super user* or *Administrator*). You have to
make sure that your normal user has sufficient privileges to create files and
directories under the prefix. For example, you can create a directory
{file}`/opt/rtems` and give it to a developer group with read, write, and
execute permissions. Alternatively, you can choose a prefix in your home
directory, e.g. {file}`$HOME/rtems/@rtems-ver-major@` or with a project-specific component
{file}`$HOME/project-x/rtems/@rtems-ver-major@`. For more ideas, see the {ref}`project sandboxing <ProjectSandboxing>` section. In this quick start chapter, we will
choose {file}`$HOME/quick-start/rtems/@rtems-ver-major@` for the RTEMS tool suite prefix.

```{warning}
The prefix must not contain space characters.
```
