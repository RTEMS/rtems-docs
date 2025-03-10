% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

(MacOS)=

# Apple macOS

Apple's macOS is supported. You need to download and install a recent
version of the Apple developer application Xcode. Xcode is available
in the App Store. Make sure you install the Command Line Tools add on
available for download within Xcode and once installed open a Terminal
shell and enter the command `cc` and accept the license agreement.

The normal prefix when working on macOS as a user is under your home
directory. Prefixes of {file}`$HOME/development/rtems` or
{file}`$HOME/rtems` are suitable.

{ref}`QuickStartPrefixes` details using Prefixes to manage the installation.

Homebrew and Macports should work but are not tested by the project as
they are rolling releases making it difficult to reproduce any
problems there may be. We recommend reaching out to those projects for
support.

Intel and Apple silicon is supported.

## Python

Building GDB requires the installation of Python's development
libraries. Building GDB includes the Python runtime header
`Python.h` and linking to the Python runtime libraries. The RSB
detects a valid header and libraries before starting a GDB
build.

It is recommended you run the RSB in a Python virtual environment. A
virtual environment manages paths for you, provides a `python`
executable mapped to the version the virtual environment is built with
and a command to find the appropiate runtime header and library files
GDB needs. Virtual environments make it easier to update Python to a
newer version if this is needed.

Apple has removed support for Python's development libraries from
recent versions of MacOS as users can manage Python using the
installer packages provided by the Python project.

To install:

1. Download a Python installer for MacOS from <https://www.python.org/>.

2. Run the installer and install Python.

3. Open a terminal and update your shell profile using the command
   Python provides. For Python 3.12 the command is:

   ```shell
   /Applications/Python\ 3.12/Update\ Shell\ Profile.command
   ```

   Check with:

   ```shell
   % type python3.12
   python3.12 is /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12
   ```

4. Create a virtual environment:

   ```shell
   mkdir $HOME/development/rtems
   cd $HOME/development/rtems
   python3.12 -m venv py3.12
   ```

   Activate the virtual environment:

   ```shell
   . $HOME/development/rtems/py3.12/bin/activate
   ```

   You are now ready to the build the tools within the virtual
   environment.

(Sonoma)=

## Sonoma

The RSB is supported on Sonoma and Apple silicon.

(Ventura)=

## Ventura

The RSB is supported on Ventura and Intel silicon.

(Monterey)=

## Monterey

The RSB is supported on Ventura and Intel silicon.

(Catalina)=

## Catalina

In the
[macOS Catalina 10.15 Release Notes](https://developer.apple.com/documentation/macos_release_notes/macos_catalina_10_15_release_notes)
Apple deprecated several scripting language runtimes such as Python 2.7. See
also
[Xcode 11 Release Notes](https://developer.apple.com/documentation/xcode_release_notes/xcode_11_release_notes).
Due to the deprecated Python 2.7 support, we recommend to install and use the
[latest Python 3 release from python.org](https://www.python.org/downloads/mac-osx/).

(Sierra)=

## Sierra

The RSB works on Sierra with the latest Xcode.

(Mavericks)=

## Mavericks

The RSB works on Mavericks and the GNU tools can be built for RTEMS using the
Mavericks clang LLVM tool chain. You will need to build and install a couple of
packages to make the RSB pass the `sb-check`. These are CVS and XZ. You can get
these tools from a packaging tool for macOS such as *MacPorts* or *HomeBrew*.

I do not use third-party packaging on macOS and prefer to build the packages from
source using a prefix of `/usr/local`. There are good third-party packages around
however they sometimes bring in extra dependence and that complicates my build
environment and I want to know the minimal requirements when building
tools. The following are required:

. The XZ package's home page is <http://tukaani.org/xz/> and I use version
: 5.0.5. XZ builds and installs cleanly.
