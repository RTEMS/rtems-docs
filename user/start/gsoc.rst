.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 Niteesh Babu <niteesh.gs@gmail.com>

.. _QuickStartGSoC:

GSoC Getting Started
====================

The goal of this page is to help new users, especially students get RTEMS
compiled and running so they can start with the real work.

Please join the :r:list:`users` and :r:list:`devel` and ask
questions. Help correct any deficiencies in the code or documentation you spot,
including those on the wiki. The ultimate goal of GSoC is to help you become
part of the open source community.

This section will help you to quickly setup a development environment without
delving into the details. For more information you can go through the other
subsections under :ref:`Quick Start <QuickStart>` chapter or ask on the
:r:list:`devel`.

We recommend new student developers use the current development (unreleased)
version. The :ref:`Quick Start Preparation <QuickStartPreparation>` should be
consulted for guidance. The examples shown here use the released version 5,
which may not be recommended for your purposes. If you are unsure, feel free to
inquire on the :r:list:`devel`.

You will be best served by using a GNU/Linux environment, which could be in a
virtual machine, for example that uses `Virtualbox <https://www.virtualbox.org/>`_
and should run on most modern desktop systems. You should also be able to work
with a MacOS or Windows system, but might encounter more difficulty than a *nix
environment.

Setting up a development environment consists of the following steps.

1) Installing dependencies for your host operating system.
2) Choosing an installation prefix.
3) Downloading the source code.
4) Installing the tool suite.
5) Building the Board Support Package (BSP).
6) Testing the Board Support Package (BSP).

Installing Dependencies
-----------------------

You need tools for your host’s operating system to build the RTEMS tool suite
from source. Please have a look at the :ref:`host-computer` chapter for the
instructions to install the tools for your OS.

Choosing an installation prefix
-------------------------------

The term ``prefix`` refers to the path on your computer where the software is to
be installed.
You can refer to the :ref:`Prefix <QuickStartPrefixes>` section for details on
choosing an installation prefix.

Downloading the Sources
-----------------------

We will be using Git to clone the sources for RTEMS and RSB. This is the
preferred way if you are planning to make contributions to the RTEMS project.

Please refer to the :ref:`QuickStartSources_Git` section for instructions on
obtaining sources using Git.

Installing the Tool Suite
-------------------------

The Tools suite is the collection of tools required to build the BSP. This
includes the compiler, debugger, assembler and other tools. These tools are
architecture-specific. We will be installing the SPARC tool suite since we are
building a SPARC based BSP.

Please refer to the :ref:`QuickStartTools` section for instructions on
building and installing the tool suite.

Building the Board Support Package
----------------------------------

There are two ways of building a BSP. We could either ask RSB to build the BSP
or manually build it. In this section will we be building it manually.
Please refer the :ref:`QuickStartBSPBuild_Manual` section for the
instructions.

Testing the Board Support Package
---------------------------------

Testing is an essential part of RTEMS development process. The main reason for
choosing the SPARC erc32 BSP is that, it has very good simulator support. This
will allow you to test your changes without the need for SPARC hardware.

Please refer to :ref:`QuickStartBSPTest` for instructions on testing the BSP.

Prove You Can Work On RTEMS
---------------------------

This section is only for students interested in Google Summer of Code.

You have to finish the following task to prove that you can work on RTEMS.

Modify the hello world example to include a new different print statement.
Something like "Hello from The Dark Side!". Then send us enough to prove to us
that you did this. We want to know you can work with RTEMS.

Create a patch of your changes and send it to :r:list:`devel` along with the
screenshot of the output.

If you followed this guide, this hello world modification will likely need to be
made in ``$HOME/quick-start/src/rtems/testsuites/samples/hello/init.c``.
To test your changes, you have to build the BSP again. This could be done by
running `make` in the BSP build directory.

.. code-block:: none

  cd $HOME/quick-start/src/rtems
  ./waf

If you are happy with your changes you can commit the changes and send the patch
to :r:list:`devel`.

Creating and Sending Patches
----------------------------

Before sending patches, make sure that the changes you have made conforms to
RTEMS coding standards.
You can refer to :ref:`Contributing` section for instruction on creating and
sending patches.

Here are a few pointers to keep in mind while creating the patches.

* Make sure not to commit changes in the master branch. This is to avoid merge
  conflicts when you are pulling the latest changes from the remote branch.
* Avoid trailing whitespace errors.
* The author name of the patch is your full name.
* The author email of the patch is your valid email address.
* Ensure that your patches build before sending them for review.
