% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2020 Chris Johns <chrisj@rtems.org>

(host-os)=

# Python

RTEMS uses Python in a range of host tools for users and
developer. RTEMS supports:

1. Python3 and Python2 for user tools,
2. Python3 for developer tools.

Python2 is now **end of life** however the RTEMS Project will continue to
provide support for its user commands. We do this to support older host
operating systems some users may be forced to use. At some point the
project will drop support for Python2 so we recommend users look at ways to
transition to Python3 if it is not easily available.

Developers of RTEMS are required to have Python3 available. RTEMS tools used
by developers for the development and maintenance of RTEMS are Python3 only.

All RTEMS Tools that can be invoked from the command line start with the
following line:

```
#! /usr/bin/env python
```

The `env` command is available on all POSIX host operating systems and it
searches the `$PATH` environment variable for the `python` command invoking
it with the script as the first argument. This means you need to have a
suitable `python` command on your host to run the RTEMS user tools. Not all
hosts provide a `python` command. If your host does not you need to find a
way to provide one. The following are some examples you can use to solve this
problem.

Python2 by default always provides a `python` command.

## Virtual Environment

Python3 provides virtual environment support. This is a great way to manage
Python on a single host. You can have a number of virtual environments with a
different mix of installed Python packages with different versions that do not
clash.

Virtual environment always provide a `python` command. This makes it ideal
if your host only provides Python3 and there is no default `python` command.

A virtual environment is created once and when you need to use it you activate
it and when finished you deactivate it.

The following shows how to create a virtual environment using different
methods. You can select the method that best suites you.

To create a virtual environment using the Python3 `venv` module:

```none
python3 -m venv rtems-py
```

To create a virtual environment for a specific version of Python3 you
can enter the command:

```none
python3.7 -m venv rtems-py
```

You can also install the `virtualenv` package on your host if it is
avaliable then enter the following create command:

```none
virtualenv rtems-py
```

To activate the virtual environment:

```none
. rtems-py/bin/activate
```

You will see your prompt change to reflect the virtual environment you
have active. To check if you now have a `python` command enter:

```none
type python
```

The output will be something similar to the following:

```none
(rtems-py) $ type python
python is /home/chris/development/rtems-py/bin/python
```

## Symbolic Link

If your host does not provide the `python` command you can add a symbolic
link to it.

```{note}
We recommend you do not add the symbolic link in any of your operating
system controlled directories as it is changing your operating system.
```

We suggest you add the symbolic link to a directory under your home directory
adding that directory to your environment's `PATH` variable. The following
commands show how to do this:

```none
cd
mkdir bin
cd bin
ln -s `command -v python3` python
export PATH=$HOME/bin:$PATH
```

```{note}
You will need to modify your shell's initialization scripts to make the
`PATH` change permanent.
```

## Directly Invoking Python

It is valid to specifically invoke any python script directly. To do this
simply prepend the specific version of python you wish to use. For example to
run the `waf` build system command with Python3 use:

```none
python3 ./waf
```
