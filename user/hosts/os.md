% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

(host-os)=

# Host Operating Systems

```{sidebar} *GDB and Python*
RTEMS uses Python in GDB to aid debugging which means GDB needs to be built
with Python development libraries. Please check the RSB documentation and
install the packages specified for your host. Make sure a python development
package is included.
```

A wide range of host operating systems and hardware can be used. The host
operating systems supported are:

- Linux
- FreeBSD
- NetBSD
- Apple OS X
- Windows
- Solaris

The functionality on a POSIX operating such as Linux and FreeBSD is similar and
most features on Windows are supported but you are best to ask on the
{r:list}`users` if you have a specific question.

We recommend you maintain your operating system by installing any updates.

We also recommend you keep your environment to the bare minimum,
particularly the PATH variable. Using environment variables has been
proven over the years to be difficult to manage in production systems.

```{warning}
The RSB assumes your host is set up and the needed packages are installed
and configured to work. If your host has not been set up please refer to
section that covers your host's packages you need to install.
```

````{topic} Path to use when building applications:
Do not forget to set the path before you use the tools, for example to
build the RTEMS kernel.

The RSB by default will install (copy) the executables to a directory tree
under the *prefix* you supply. To use the tools once finished just set your
path to the `bin` directory under the *prefix* you use. In the examples
that follow the *prefix* is `$HOME/development/rtems/@rtems-ver-major@.@rtems-ver-minor@` and is set
using the `--prefix` option so the path you need to configure to build
applications can be set with the following in a BASH shell:

```none
$ export PATH=$HOME/development/rtems/@rtems-ver-major@.@rtems-ver-minor@/bin:$PATH
```

Make sure you place the RTEMS tool path at the front of your path so they
are searched first. RTEMS can provide newer versions of some tools your
operating system provides and placing the RTEMS tools path at the front
means it is searched first and the RTEMS needed versions of the tools are
used.
````

```{warning}
Do not put spaces or special characters in the directories you use to build
RTEMS. Many of the packages built by the RSB use GNU *make*, which cannot
handle spaces in pathnames. If there is a space in the pathname the build
will fail. Special characters are also likely to confuse build systems.
```

````{note}
RSB and RTEMS have a matching *git branch* for each version of RTEMS. For
example, if you want to build a toolchain for 4.11, then you should
checkout the 4.11 branch of the RSB:

```none
$ git checkout -t origin/@rtems-ver-major@.@rtems-ver-minor@
```

Branches are available for the 4.9, 4.10, 4.11 and 5 versions of RTEMS.
````
