.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>
.. comment: All rights reserved.

.. _rtems-development:

RTEMS Development
*****************

RTEMS can be developed using Eclipse. The RTEMS kernel is an `autotools` or
`autoconf` and `automake` based package. You can create a project in Eclipse
that lets you configure and build a BSP for an architecture. We assume you have
already build and installed your tools using the RTEMS Source Builder.

Kernel Source
-------------

Download or clone the RTEMS Kernel source code. We will clone the source code:

.. code-block:: shell

  $ git clone git://git.rtems.org/rtems.git rtems.master
  Cloning into 'rtems'...
  remote: Counting objects: 483342, done.
  remote: Compressing objects: 100% (88974/88974), done.
  remote: Total 483342 (delta 390053), reused 475669 (delta 383809)
  Receiving objects: 100% (483342/483342), 69.88 MiB | 1.37 MiB/s, done.
  Resolving deltas: 100% (390053/390053), done.
  Checking connectivity... done.

We need to `bootstrap` the kernel source code. A `botostrap` invokes the
various `autotools` commands need to generate build system files. First we need
to the path to our tools:

.. code-block:: shell

  $ export PATH=/opt/rtems/5/bin:$PATH

Now run the `bootstrap` command:

.. code-block:: shell

  $ cd rtems.master
  $ ./bootstrap

Sit back, this can take a while. The Getting Started Guide talks about using
the RSB's `sb-bootstrap` to run the bootstrap process in parallel on all
available cores. The output of the bootstrap has not been copied into this
documentment.

The source code is now ready.

Eclipse SDK Software
--------------------

We need the following Eclipse SDK Software packages installed:

 - C/C++ Autotools support
 - C/C++ Development Tools
 - C/C++ GCC Cross Compiler Support

Start Eclipse and check to see if you have the them installed via the **Help,
Installation Details** menu item:

.. figure:: ../images/eclipse/eclipse-help-installation.png
  :width: 50%
  :align: center
  :alt: Help, Installation Details

The dialog box shows the installed software packages and you can see the
**C/C++ Autotools support** and the **C/C++ Development Tools** are installed:

.. figure:: ../images/eclipse/eclipse-sdk-details.png
  :align: center
  :alt: SDK Installation Details

You can see some other software packages are installed in the figure. You can ignore those.

If you do not have the listed software packages install select **Help, Install
New Software** and in the **Work with:** list box select
**http://download.eclipse.org/releases/mars**.

.. figure:: ../images/eclipse/eclipse-install-new-software.png
  :width: 80%
  :align: center
  :alt: Help, Install New Software

Afer a small period of time a list of available packages will populate and you
can select the ones we are interested in. Enter ``autotools`` in the search
box and select the package:

.. figure:: ../images/eclipse/eclipse-autotools.png
  :width: 80%
  :align: center
  :alt: C/C++ Autotools support

Clear the search line and enter ``development tools`` in the search box and
then scroll down to find **C/C++ Development Tools**:

.. figure:: ../images/eclipse/eclipse-cdt.png
  :width: 80%
  :align: center
  :alt: C/C++ Development Tools

Again clear the search line and enter ``gcc cross`` in the search box and
select the package:

.. figure:: ../images/eclipse/eclipse-gcc-cross.png
  :width: 80%
  :align: center
  :alt: C/C++ GCC Cross Compiler Support

Click **Next** and once the **Install Details** have determined what is needed
select **Finish** to install the packages.

Kernel Build Project
--------------------

We create a project in Eclipse that can configure and build RTEMS for the
``pc686`` BSP. This BSP is based on the ``pc386`` BSP and is under the ``i386``
architecture.

We assume you have built and installed the ``i386`` RTEMS Tools, obtained the
RTEMS kernel code and ``bootstrapped`` it if a git clone, and installed the
required Eclipse Software packages.

The paths used in this project are:

:file:`/opt/work/rtems/4.11`
   The RTEMS Tools prefix the tools are install under.

:file:`/opt/work/chris/rtems/kernel/rtems.master`
   The RTEMS Kernel source code.

:file:`/opt/work/chris/rtems/kernel/5`
   The RTEMS Kernel prefix.

:file:`/opt/work/chris/rtems/kernel/bsp/pc`
   The RTEMS Kernel BSP build directory.

The menus shown here may vary from those you have as Eclipse changes them based
on what you do.

Select **File, New, Project** :

.. figure:: ../images/eclipse/eclipse-new-project.png
  :width: 100%
  :align: center
  :alt: File, New, Project...

Click on **C/C++** and select **Makefile Project with Existing Code** then
select **Next** :

.. figure:: ../images/eclipse/eclipse-project-makefile-existing-code.png
  :width: 75%
  :align: center
  :alt: Makefile Project with Existing Code

Enter the project name ``rtems-git`` into the **Project Name** field and select
the **Browse...** button and the path to the RTEMS Kernel source code then
click **Finish** :

.. figure:: ../images/eclipse/eclipse-project-import-existing-code.png
  :width: 75%
  :align: center
  :alt: Import Existing Code

Eclipse will show the RTEMS Kernel source code in the **Project Explorer** panel:

.. figure:: ../images/eclipse/eclipse-rtems-git-files.png
  :width: 100%
  :align: center
  :alt: RTEMS GIT Project showing files

We now convert the project to an Autotools project. Select **File, New,
Convert to a C/C++ Autotools Project** :

.. figure:: ../images/eclipse/eclipse-rtems-git-convert-autotools.png
  :width: 100%
  :align: center
  :alt: Convert the project to Autotools

Select **C Project** then **Finish** :

.. figure:: ../images/eclipse/eclipse-rtems-git-convert-autotools-dialog.png
  :width: 85%
  :align: center
  :alt: Convert the project to Autotools

We now configure the project's properties by right clicking on the
``rtems-git`` project title and then **Properties** :

.. figure:: ../images/eclipse/eclipse-rtems-git-properties-menu.png
  :width: 100%
  :align: center
  :alt:

Click on the **Autotools** item then **Configure Settings** and **Platform
specifiers** and set the **Target platform** field with ``i386-rtems5``:

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-at-target.png
  :width: 100%
  :align: center
  :alt: Enter the Autotool target

Select **Platform directories** and enter the **Arch-independent install
directory (--prefix)** to the RTEMS Kernel prefix of
:file:`/opt/work/chris/rtems/kernel/5`:

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-at-prefix.png
  :width: 100%
  :align: center
  :alt: Enter the Autotool target

We disable networking to use the external LibBSD package and set the BSP to
``pc686``. Select the **Advanced** and in the **Additional command-line
options** enter ``--disable-networking`` and ``--enable-rtemsbsps=pc686``. You
can add extra options you may need:

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-at-add-opts.png
  :width: 100%
  :align: center
  :alt: Enter the Autotool additional options

Select **C/C++ Build** and **Environment**. Uncheck or clear the **Use default
build command** and add ``-j N`` where ``N`` is the number of cores you have in
your machine. The figure has told `make` to run 8 jobs, one per core for an 8
core machine. Click on the **File system...** button and navigate to the BSP
build directory. This is the location Eclipse builds the BSP. RTEMS requires
you build outside the source tree and in this example we are forcing the build
directory to something specific. Finish by pressing **Apply** :

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-build.png
  :width: 100%
  :align: center
  :alt: C/C++ Build Properties

Select **Environment** under **C/C++ Build** as we need to set the path to the
RTEMS Tools. In this example we set the path in the Eclipse project so each
project can have a specific set of tools. Press the **Add...** button:

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-env.png
  :width: 100%
  :align: center
  :alt: C/C++ Build Environment

Enter the path to the tools, in our case it is
:file:`/opt/work/rtems/5/bin`, then press **Variables** :

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-env-var.png
  :width: 85%
  :align: center
  :alt: C/C++ Build Environment

Scroll down and select **PATH** and then press **OK** :

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-env-var-path.png
  :width: 60%
  :align: center
  :alt: C/C++ Build Environment

You will now see the path in the **Value:** field. Make sure you have a path
separator between the end of the tools path and the path variable we have just
added. In this case is a Unix host and the separator is `:`. Windows use
`;`. Press **OK** when you have a valid path:

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-env-var-path-add.png
  :width: 85%
  :align: center
  :alt: C/C++ Build Environment

The **Environment** panel will now show the added `PATH` variable. Click
**Replace native environment with specified one** as shown and then press
**Apply** :

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-env-replace.png
  :width: 100%
  :align: center
  :alt: C/C++ Build Environment

Select **Settings** under **C/C++ Build** and check **Elf Parser** and **GNU
Elf Parser** and then press **OK** :

.. figure:: ../images/eclipse/eclipse-rtems-git-prop-cdt-settings.png
  :width: 100%
  :align: center
  :alt: C/C++ Build Settings

We are now ready to run configure using Eclipse. Right click on the project
name ``rtems-git`` and then **Reconfigure Project** :

.. figure:: ../images/eclipse/eclipse-rtems-git-reconfigure.png
  :width: 100%
  :align: center
  :alt: Reconfigure the RTEMS Project

Select the **Console** tab in the output panel to view the configure process
output. You will notice the end of the configure process shows the names of the
BSPs we have asked to build. In our case this is the ``pc686`` BSP:

.. figure:: ../images/eclipse/eclipse-rtems-git-reconfigure-console.png
  :width: 100%
  :align: center
  :alt: Reconfigure console output

We can now build RTEMS using Eclipse. Right click on the project name
``rtems-git`` and then select **Build Project** :

.. figure:: ../images/eclipse/eclipse-rtems-git-build-project.png
  :width: 100%
  :align: center
  :alt: Reconfigure the RTEMS Project

A **Build Project** message box will appear showing the progress:

.. figure:: ../images/eclipse/eclipse-rtems-git-build-project-building.png
  :width: 75%
  :align: center
  :alt: Reconfigure the RTEMS Project

When finished click on the **Problems** output tab to view any errors or warnings:

.. figure:: ../images/eclipse/eclipse-rtems-git-built.png
  :width: 100%
  :align: center
  :alt: Reconfigure the RTEMS Project

If you get errors during the configure phase or building you will need to
determine reason why. The main source of errors will be the path to the
tools. Check the top of the ``config.log`` file ``configure`` generates. This
file can be found in the top directory of you BSP build tree. The file will
list the path components near the top and you should see the path to your tools
listed first. While looking make sure the configure command matches what you
expect and matches the documentation for configuring RTEMS.

If the contents of ``config.log`` look fine check the build log. The project's
**Properties** dialog under **C/C++ Build**, **Logging** has a path to a build
log. Open the build log and search for the error. If you cannot figure out the
source of the error please ask on the :r:list:`users` for help.
