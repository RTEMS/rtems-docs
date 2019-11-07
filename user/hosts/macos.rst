.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _MacOS:

Apple macOS
===========

Apple's macOS is fully supported. You need to download and install a recent
version of the Apple developer application Xcode. Xocde is available in the App
Store. Make sure you install the Command Line Tools add on available for
download within Xcode and once installed open a Terminal shell and enter the
command ``cc`` and accept the license agreement.

The normal prefix when working on macOS as a user is under your home directory.
Prefixes of :file:`$HOME/development/rtems` or :file:`$HOME/rtems` are
suitable.

:ref:`QuickStartPrefixes` details using Prefixes to manage the installation.

Catalina
~~~~~~~~

In the
`macOS Catalina 10.15 Release Notes <https://developer.apple.com/documentation/macos_release_notes/macos_catalina_10_15_release_notes>`_
Apple deprecated several scripting language runtimes such as Python 2.7.  See
also
`Xcode 11 Release Notes <https://developer.apple.com/documentation/xcode_release_notes/xcode_11_release_notes>`_.
Due to the deprecated Python 2.7 support, we recommend to install and use the
`latest Python 3 release from python.org <https://www.python.org/downloads/mac-osx/>`_.

Sierra
~~~~~~

The RSB works on Sierra with the latest Xcode.

.. _Mavericks:

Mavericks
~~~~~~~~~

The RSB works on Mavericks and the GNU tools can be built for RTEMS using the
Mavericks clang LLVM tool chain. You will need to build and install a couple of
packages to make the RSB pass the ``sb-check``. These are CVS and XZ. You can get
these tools from a packaging tool for macOS such as *MacPorts* or *HomeBrew*.

I do not use third-party packaging on macOS and prefer to build the packages from
source using a prefix of ``/usr/local``. There are good third-party packages around
however they sometimes bring in extra dependence and that complicates my build
environment and I want to know the minimal requirements when building
tools. The following are required:

. The XZ package's home page is http://tukaani.org/xz/ and I use version
  5.0.5. XZ builds and installs cleanly.
