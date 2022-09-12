.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _rtems-kernel:

RTEMS Kernel
============

RTEMS is an open source real-time operating system. As a user you have access
to all the source code. The ``RTEMS Kernel`` section will show you how you
build the RTEMS kernel on your host.

Development Sources
-------------------

Create a new location to build the RTEMS kernel:

.. code-block:: none

  $ cd $HOME/development/rtems
  $ mkdir src
  $ cd src

Clone the RTEMS respository:

.. code-block:: none

  $ git clone git://git.rtems.org/rtems.git rtems
  Cloning into 'rtems'...
  remote: Counting objects: 483342, done.
  remote: Compressing objects: 100% (88974/88974), done.
  remote: Total 483342 (delta 390053), reused 475669 (delta 383809)
  Receiving objects: 100% (483342/483342), 69.88 MiB | 1.37 MiB/s, done.
  Resolving deltas: 100% (390053/390053), done.
  Checking connectivity... done.

Building a BSP
--------------

We build RTEMS in a directory within the source tree we have just cloned.  For
the details, see the :ref:`BSPBuildSystem`.  We will build for the ``erc32``
BSP with POSIX enabled.  Firstly, create the file :file:`config.ini` in the
source tree root directory with the BSP build configuration, for example:

.. code-block:: ini

  [sparc/erc32]
  RTEMS_POSIX_API = True

Configure RTEMS using the ``waf configure`` command:

.. code-block:: none

  $ cd $HOME/development/rtems/src/rtems
  $ ./waf configure --prefix=$HOME/development/rtems/6
  Setting top to                           : $HOME/development/rtems/src/rtems
  Setting out to                           : $HOME/development/rtems/src/rtems/build
  Regenerate build specification cache (needs a couple of seconds)...
  Configure board support package (BSP)    : sparc/erc32
  Checking for program 'sparc-rtems6-gcc'  : $HOME/development/rtems/6/bin/sparc-rtems6-gcc
  Checking for program 'sparc-rtems6-g++'  : $HOME/development/rtems/6/bin/sparc-rtems6-g++
  Checking for program 'sparc-rtems6-ar'   : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'sparc-rtems6-ld'   : $HOME/development/rtems/6/bin/sparc-rtems6-ld
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'g++, c++'          : $HOME/development/rtems/6/bin/sparc-rtems6-g++
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'gas, gcc'          : $HOME/development/rtems/6/bin/sparc-rtems6-gcc
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for program 'gcc, cc'           : $HOME/development/rtems/6/bin/sparc-rtems6-gcc
  Checking for program 'ar'                : $HOME/development/rtems/6/bin/sparc-rtems6-ar
  Checking for asm flags '-MMD'            : yes
  Checking for c flags '-MMD'              : yes
  Checking for cxx flags '-MMD'            : yes
  Checking for program 'rtems-bin2c'       : $HOME/development/rtems/6/bin/rtems-bin2c
  Checking for program 'gzip'              : /usr/bin/gzip
  Checking for program 'xz'                : /usr/bin/xz
  Checking for program 'rtems-ld'          : $HOME/development/rtems/6/bin/rtems-ld
  Checking for program 'rtems-syms'        : $HOME/development/rtems/6/bin/rtems-syms
  Checking for program 'rtems-bin2c'       : $HOME/development/rtems/6/bin/rtems-bin2c
  Checking for program 'gzip'              : /usr/bin/gzip
  Checking for program 'xz'                : /usr/bin/xz
  'configure' finished successfully (7.996s)

Build RTEMS:

.. code-block:: none

  $ ./waf
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build'
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build'
  'build' finished successfully (0.051s)
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  [   1/1524] Compiling bsps/shared/dev/serial/mc68681_reg2.c
  [   2/1524] Compiling bsps/shared/dev/rtc/mc146818a_ioreg.c
  [   3/1524] Compiling bsps/shared/dev/flash/am29lv160.c
  ...
  [1521/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/libz.a
  [1522/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/librtemscxx.a
  [1523/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/testsuites/samples/paranoia.exe
  [1524/1524] Linking $HOME/development/rtems/src/rtems/build/sparc/erc32/libmghttpd.a
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  'build_sparc/erc32' finished successfully (4.894s)

Installing A BSP
----------------

All that remains to be done is to install the kernel. Installing RTEMS copies
the API headers and architecture specific libraries to a locaiton under the
`prefix` you provide. You can install any number of BSPs under the same
`prefix`. We recommend you have a separate `prefix` for different versions of
RTEMS. Do not mix versions of RTEMS under the same `prefix`. Make installs
RTEMS with the following command:

.. code-block:: none

  $ ./waf install
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build'
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build'
  'install' finished successfully (0.074s)
  Waf: Entering directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/libchip/am29lv160.h (from bsps/include/libchip/am29lv160.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/libchip/mc146818a.h (from bsps/include/libchip/mc146818a.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/libchip/mc68681.h (from bsps/include/libchip/mc68681.h)
  ...
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/rtems/version.h (from cpukit/include/rtems/version.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/rtems/vmeintr.h (from cpukit/include/rtems/vmeintr.h)
  + install $HOME/development/rtems/6/sparc-rtems6/erc32/lib/include/rtems/watchdogdrv.h (from cpukit/include/rtems/watchdogdrv.h)
  Waf: Leaving directory `$HOME/development/rtems/src/rtems/build/sparc/erc32'
  'install_sparc/erc32' finished successfully (0.637s)

Contributing Patches
--------------------

RTEMS welcomes fixes to bugs and new features. The RTEMS Project likes to have
bugs fixed against a ticket created on our :r:url:`devel`. Please raise a
ticket if you have a bug. Any changes that are made can be tracked against the
ticket. If you want to add a new a feature please post a message to
:r:list:`devel` describing what you would like to implement. The RTEMS
maintainer will help decide if the feature is in the best interest of the
project. Not everything is and the maintainers need to evalulate how much
effort it is to maintain the feature. Once accepted into the source tree it
becomes the responsibility of the maintainers to keep the feature updated and
working.

Changes to the source tree are tracked using git. If you have not made changes
and enter the source tree and enter a git status command you will see nothing
has changed:

.. code-block:: none

  $ cd $HOME/development/rtems/src/rtems
  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  nothing to commit, working directory clean

We will make a change to the source code. In this example I change the help
message to the RTEMS shell's ``halt`` command. Running the same git status
command reports:

.. code-block:: none

  $ git status
  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

          modified:   cpukit/libmisc/shell/main_halt.c

  no changes added to commit (use "git add" and/or "git commit -a")

As an example I have a ticket open and the ticket number is 9876. I commit the
change with the follow git command:

.. code-block:: none

  $ git commit cpukit/libmisc/shell/main_halt.c

An editor is opened and I enter my commit message. The first line is a title
and the following lines form a body. My message is:

.. code-block:: none

  shell: Add more help detail to the halt command.

  Closes #9876.

  # Please enter the commit message for your changes. Lines starting
  # with '#' will be ignored, and an empty message aborts the commit.
  # Explicit paths specified without -i or -o; assuming --only paths...
  #
  # Committer: Chris Johns <chrisj@rtems.org>
  #
  # On branch master
  # Your branch is up-to-date with 'origin/master'.
  #
  # Changes to be committed:
  #       modified:   cpukit/libmisc/shell/main_halt.c

When you save and exit the editor git will report the commit's status:

.. code-block:: none

  $ git commit cpukit/libmisc/shell/main_halt.c
  [master 9f44dc9] shell: Add more help detail to the halt command.
   1 file changed, 1 insertion(+), 1 deletion(-)

You can either email the patch to :r:list:`devel` with the following git
command, and it is `minus one` on the command line:

.. code-block:: none

  $ git send-email --to=devel@rtems.org -1
   <add output here>

Or you can ask git to create a patch file using:

.. code-block:: none

  $ git format-patch -1
  0001-shell-Add-more-help-detail-to-the-halt-command.patch

This patch can be attached to a ticket.
