.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project


.. COMMENT:TBD  - Convert the following to Rest and insert into this file
.. COMMENT:TBD - https://devel.rtems.org/wiki/Developer/Coding/Doxygen_for_BSPs


Doxygen Recommendations for BSPs
================================

RTEMS contains well over a hundred `Board Support Packages (BSPs)
<wiki:TBR/Website/Board_Support_Packages>`_. , across over 20 different
`CPU Architectures <wiki:TBR/UserManual/SupportedCPUs>`_. . What this
means is that there is a lot of hardware dependent code that gets
written, and that adding Doxygen to properly document it all can be a
very complicated task.

The goal of this document is to attempt to simplify this process a bit,
and to get you started on adding Doxygen to the bsps/ directory in a way
that is logical and has structure. Before we move on to detailing the
process of actually adding Doxygen to BSPs, you will be greatly served by
having at least a basic understanding of the purpose of a Board Support
Package (it always helps to know a bit about what you're documenting),
as well as of the existing structure of the bsps/ directory.

Feel free to skip around and skim parts of this.

BSP Basics
----------

Embedded development is hard. Different CPUs have different instructions
for doing the same thing, and different boards will have all sorts of
different hardware that require unique drivers and interfaces. RTEMS
handles this by having discrete packages, BSPs, to encapsulate
code to accommodate for unique hardware. BSPs seek to implement the
Hardware-Software interface. This, in a nutshell, is one of the `core
purposes <wiki:Mission_Statement>`_. of RTEMS: To abstract (as much as
is possible) away from the physical hardware and provide a standards
compliant real-time environment for the embedded developer. If you think
about it, the operating system on your normal computer serves a very
similar purpose.

Common Features Found In BSPs
-----------------------------

Although the actual implementation code will differ between BSPs, all
BSPs will share some degree of common functionality. This is because
that no matter what exact hardware you have, you need some basic features
implemented in order to have a real time system you can develop on. Some
of the most common shared features across most boards include:

 *  **console**: is technically the serial driver for the BSP rather than
 just a console driver, it deals with the board UART (i.e. serial devices)
 *  **clock**: support for the clock tick - a regular time basis for the kernel
 *  **timer**: support of timer devices, used for timing tests
 *  **rtc** or **tod**: support for the hardware real time clock
 *  **network**: the Ethernet driver
 *  **shmsupp**: support of shared memory driver MPCI layer in a
 multiprocessor system
 *  **gnatsupp**: BSP specific support for the GNU Ada run-time
 *  **irq**: support for how the processor handles interrupts (probably
 the most common module shared by all boards)
 *  **tm27**: specific routines for the tm27 timing test
 *  **start** and **startup**: C and assembly used to initialize the
 board during startups/resets/reboots

These are just some of the things you should be looking for when adding
Doxygen to a BSP.

Note that there is no guarantee a particular BSP will implement all of
these features, or even some of them. These are just the most common
ones to look for. RTEMS follows a standardized naming convention for
the BSP sub directories, so you should be able to tell in most cases
what has been implemented on the BSP level and what has not.

Shared Features
---------------

Some of the RTEMS executive is hardware independent and can be abstracted
so that the same piece of code can be shared across multiple CPU
architectures, or across multiple boards on the same architecture. This
is done so that chunks of software can be reused, as well as aiding
in reducing the development and debugging time for implementing new
BSPs. This greatly aids the developer, but as someone seeking to document
this code, this can make your life a little bit harder. It is hard to
tell by looking at the directory of a BSP which features have simply been
left out and which features are being implemented by using shared code
from either from the architecture (../shared) or the base bsps/ shared
directory (../../shared). You may be looking at the BSP headers and notice
that you have an irq.h, but no irq.c implementing it, or you might even be
missing both. You know that the processor has interrupt support somehow,
but where is it? The easiest way to figure this out is by looking at
the Makefile.am for a BSP. We'll detail this process more in a bit.

Rationale
---------

As someone adding documentation and not doing actual development
work, you might think it is not necessary to know some of the in and
outs of BSPs. In actuality, this information will prove to be very
useful. Doxygen documentation works by grouping things and their
components (i.e. functions and other definitions), and by having
brief descriptions of what each group does. You can't know what to
look for or know how to group it or know how to describe it without
some basic knowledge of what a BSP is. For more information on any
of the above or BSPs in general, check out the `BSP Development Guide
<http://rtems.org/onlinedocs/doc-current/share/rtems/html/bsp_howto/index.html>`_.
.

The Structure of the bsps/ directory
------------------------------------

All BSPs are found within the bsps/ directory, which is itself very
well ordered. At the first level, we find a directory for each CPU
architecture RTEMS supports, as well as a directory for code shared by
all implementations.

    .. code-block:: shell

        $ cd bsps
        $ ls
        arm   bsp.am  lm32  m68k             mips   no_cpu         README  sparc
        avr   h8300   m32c  Makefile.am      moxie  powerpc        sh      sparc64
        bfin  i386    m32r  MERGE.PROCEDURE  nios2  preinstall.am  shared  v850


If we cd into a specific architecture, we see that a similar structure is
employed. bsps/arm/ contains directories for each Board Support Package
for boards with an ARM cpu, along with a folder for files and .h's shared
by all BSPs of that architecture.

    .. code-block:: shell

        $ cd arm
        $ ls
        acinclude.m4  edb7312    gumstix   Makefile.am    realview-pbx-a9  stm32f4
        configure.ac  gba        lm3s69xx  nds            rtl22xx          xilinx-zynq
        csb336        lpc24xx   preinstall.am  shared     csb337           gp32
        lpc32xx   raspberrypi    smdk2410

Finally, if we cd into a specific BSP, we see the files and .h's that
compose the package for that particular board. You may recognize the
directory names as some of the [common features] we outlined above,
like '''irq''', '''clock''', '''console''', and '''startup'''. These
directories contain implementations of these features.

    .. code-block:: shell

        $ cd raspberrypi
        $ ls
        bsp_specs  configure.ac  include  make         misc           README
        clock      console       irq      Makefile.am  preinstall.am  startup

Another way to get an idea of the structure of bsps/ is to navigate
to a directory and execute the "tree -f" command. This outputs a nice
graphic that conveys some of the hierarchical properties of a particular
directory.

    .. code-block:: shell

        $ pwd
        ~/rtems/bsps/arm/raspberrypi
        $ tree -f
                .
                |-- ./bsp_specs
        |-- ./clock
        |   `-- ./clock/clockdrv.c
        |-- ./configure.ac
        |-- ./console
        |   |-- ./console/console-config.c
                |   `-- ./console/usart.c
        |-- ./include
        |   |-- ./include/bsp.h
        |   |-- ./include/irq.h
        |   |-- ./include/mmu.h
        |   |-- ./include/raspberrypi.h
        |   `-- ./include/usart.h
        |-- ./irq
        |   `-- ./irq/irq.c
        |-- ./make
        |   `-- ./make/custom
        |       `-- ./make/custom/raspberrypi.cfg
        |-- ./Makefile.am
        |-- ./misc
        |   `-- ./misc/timer.c
        |-- ./preinstall.am
        |-- ./README
        `-- ./startup
            |-- ./startup/bspreset.c
            |-- ./startup/bspstart.c
            |-- ./startup/bspstarthooks.c
            |-- ./startup/linkcmds
            `-- ./startup/mm_config_table.c


In short, BSPs will use the following directories:

 *  bsps/**shared**                        <- code used that is shared by all BSPs
 *  bsps/**CPU**/**shared**          <- code used shared by all BSPs of a particular CPU architecture
 *  bsps/**CPU**/**BSP**             <- code unique to this BSP

As you can see, the bsps/ directory has a very logical and easy to
understand structure to it. The documentation generated by Doxygen
should attempt to match this structure as closely as possible. We want
an overarching parent group to serve the same purpose as the bsps/
directory. In it, we want groups for each CPU architecture and a group
for the shared files. We then want groups for each BSP. Breaking our
documentation up into discrete groups like this will greatly simplify
the process and make the documentation much easier to go through. By
learning about the existing structure of the bsps/ directory, we get an
idea of how we should structure the Doxygen groups we create. More on
this in the next section.

Doxygen
-------

Now that we have covered some of the preliminaries, we can move on to
what you are actually reading this wiki page for: adding Doxygen to the
bsps/ directory. Let's start with some Doxygen basics. Skip this if you
are already comfortable with Doxygen.

In addition to this, check out the page on `Doxygen Recommendations
<wiki:Developer/Coding/Doxygen >`_. , which also contains a fair amount
of information that will not be covered here.

Doxygen Basics
--------------

Doxygen is a documentation generator. It allows for documentation to be
written right by the source code, greatly easing the pains of keeping
documentation relevant and up to date. Doxygen has many commands,
used for things like annotating functions with descriptions, parameter
information, or return value information. You can reference other files
or even other documentation.

The core component of Doxygen (that we care about right now at least) is
what's called a **group**, or **module**. These are used to add structure
and associate groups of files that serve a similar purpose or implement
the same thing.

Doxygen Headers
---------------
Doxygen is always found in a special Doxygen comment block, known as a
**Doxygen header**. In RTEMS, this block comes in the form of a multiline
comment with some included Doxygen commands, which are preceded by the '@'
tag. Take a look at this Doxygen header that declares the arm_raspberrypi
module, which houses the documentation in the BSP for the Raspberry Pi.

    .. code-block:: c

        bsps/arm/raspberrypi/include/bsp.h:

        /**
         * @defgroup arm_raspberrypi Raspberry Pi Support
         *
         * @ingroup bsp_arm
         *
         * @brief Raspberry Pi support package
         *
         */

You see a few commands here that we'll cover in the following
sections. Briefly, the @defgroup command declares a new group, the
@ingroup command nests this group as a submodule of some other group (in
this case bsp_arm), and the @brief command provides a brief description
of what this group is.

The @defgroup Command
---------------------

The @defgroup command is used to declare new groups or modules. Think
"define group". The syntax of this command is as follows:

    .. code-block:: c

        @defgroup <group name> <group description>


The group name is the name used by Doxygen elsewhere to reference this
group. The group description is what is displayed when the end user
navigates to this module in the resulting documentation. The group
description is a couple words formatted as how it would be in a table
of contents. This part is what actually shows up in the documentation,
when the user navigates to this group's module, this description will
be the modules name.

Groups should only be declared (@defgroup) in .h files. This is
because Doxygen is used primarily to document interfaces, which are
only found in .h files. Placing @defgroups in .h files is the only real
restriction. Which .h file you place the group declaration in surprisingly
doesn't matter. There is no information in the resulting documentation
that indicates where the group was declared. You will see that we do
have some rules for where you should place these declarations, but we
also use this fact that it doesn't matter to our advantage, in order to
standardize things.

The @defgroup command is used only to define ''structure''. No actual
documentation is generated as a result of its use. We must @ingroup things
to the group we declare in order to create documentation. Even though it
does not generate visible documentation, the @defgroup command is still
very important. We use it in a way that seeks to emulate the structure
of the bsps/ directory itself. We do this by creating a hierarchy of
groups for each CPU architecture and each BSP.

The @ingroup Command
--------------------

The @ingroup command is used to add 'things' to already declared
groups or modules. These 'things' can either be other groups, or files
themselves. The syntax of the @ingroup command is as follows:

    .. code-block:: shell

        @ingroup <group name>


The group name is the actual name, not description, of the group you
want to add yourself to. Remember that group name was the second argument
passed to the @defgroup command.

Using the @ingroup command is how we add ''meaning'' to the ''structure''
created by using @defgroup. @ingroup associates the file it is found in
and all other Doxygen found within (function annotations, prototypes, etc)
with the group we declared with the @defgroup command. We add related
files and headers to the same groups to create a logical and cohesive
body of documentation. If the end user wanted to read documentation
about how the raspberry pi handles interrupts, all they would have to
do would be to navigate to the raspberry pi's interrupt support module
(which we created with a @defgroup command), and read the documentation
contained within (which we added with @ingroup commands).

@ingroup is found within all Doxygen headers, along with an @brief
statement. There are two types of Doxygen headers, which we will go over
after we see a description of the @brief command.

The @brief Command
------------------

The @brief command is used to give either a)  a brief description
in the form of an entry as you would see it in a table of contents
(i.e. Capitalized, only a couple of words) or b) a brief topic sentence
giving a basic idea of what the group does. The reason you have two uses
for the brief command is that it is used differently in the two types of
Doxygen headers, as we will see shortly. The syntax of the brief command
is self evident, but included for the sake of completion:

    .. code-block:: shell

        @brief <Table of Contents entry '''or''' Topic Sentence>


The Two Types of Doxygen Headers
--------------------------------

There are two types of Doxygen Headers. The first type is found at the
beginning of a file, and contains an @file command. This type of header
is used when @ingroup-ing the file into another doxygen group. The form
of the @brief command in this case is a topic sentence, often very close
to the file name or one of it's major functions. An example of this type
of header, found in bsps/arm/raspberrypi/include/bsp.h is as follows:

    .. code-block:: c

        Header type 1: used to add files to groups, always found at the beginning of a file
        /**
         * @file
         *
         * @ingroup raspberrypi
         *
         * @brief Global BSP definitions.
         */

        /*
         *  Copyright (c) YYYY NAME
         *
         *   <LICENSE TERMS>
         */


Notice the form and placement of this type of header. It is always found
at the beginning of a file, and is in its own multiline comment block,
separated by one line white space from the copyright. If you look at the
header itself, you see a @file, @ingroup, and @brief command. Consider
the @file and the @ingroup together, what this says is that we are
adding this file to the raspberrypi group. There is actually a single
argument to the @file command, but Doxygen can infer it, so we leave
it out. Any other Doxygen, function annotations, function prototypes,
#defines, and other code included in the file will now be visible and
documented when the end user navigates to the group you added it to in
the resulting documentation.

Now let's consider the second type of header. This type is syntactically
very similar, but is used not to add files to groups, but to add groups
to other groups. We use this type of header to define new groups
and nest them within old groups. This is how we create hierarchy
and structure within Doxygen. The following is found, again, in
bsps/arm/raspberrypi/include/bsp.h:

    .. code-block:: c

        Header type 2: Used to nest groups, found anywhere within a file
        /**
         * @defgroup arm_raspberrypi Raspberry Pi Support
         *
         * @ingroup bsp_arm
         *
         * @brief Raspberry Pi Support Package
         */

It looks very similar to the first type of header, but notice that the
@file command is replaced with the @defgroup command. You can think
about it in the same way though. Here we are creating a new group, the
arm_raspberry pi group, and nesting it within the bsp_arm group. The
@brief in this case should be in the form of how you would see it in a
table of contents. Words should be capitalized and there should be no
period. This type of header can be found anywhere in a file, but it is
typically found either in the middle before the file's main function,
or at the tail end of a file. Recall that as we are using the @defgroup
command and creating a new group in this header, the actual .h we place
this in does not matter.

The second type of header is the **structure** header, it's how we
create new groups and implement hierarchy. The first type of header
was the **meaning** header, it's how we added information to the groups
we created.

For more examples of Doxygen structure and syntax, refer to BSPs found
within the arm architecture, the lpc32xx and raspberrypi BSPs are
particularly well documented. A good way to quickly learn more is by
tweaking some Doxygen in a file, then regenerating the html, and seeing
what has changed.

Generating Documentation
------------------------

Doxygen is a documentation generator, and as such, we must
generate the actual html documentation to see the results
of our work. This is a very good way to check your work, and
see if the resulting structure and organization was what you had
intended. The best way to do this is to simply run the `do_doxygen script
<https://github.com/joelsherrill/gci_tasks/blob/master/2015/doxygen_c_header_tasks/validate/do_doxygen>`_.  To use the script:

Make sure Doxygen is installed. Also, the environment needs to have the
root directory of RTEMS set in the variable `r` so that `$r` prints the
path to RTEMS, and the script takes as argument a relative directory
from there to generate the doxygen, for example to generate the doxygen
for all of bsps/ you would do:

    .. code-block:: shell

        export r=~/rtems
        ./do_doxygen bsps

Doxygen in bsps/
----------------

Now that we've covered the basics of Doxygen, the basics of BSPs and the
structure of the bsps/ directory, actually adding new Doxygen to bsps/
will be much easier than it was before. We will cover a set of rules and
conventions that you should follow when adding Doxygen to this directory,
and include some tips and tricks.

Group Naming Conventions
------------------------

This is an easy one. These are in place in order for you to quickly
identify some of the structure of the Doxygen groups and nested groups,
without actually generating and looking at the documentation. The basic
idea is this: when defining a new group (@defgroup), the form of the name
should be the super group, or the name of the group you are nesting this
group within, followed by an underscore, followed by the intended name
of this new group. In command form:

    .. code-block:: c

          <----- This is your group name -------> <--usual description -->
        @defgroup <super-group name>_<name of this group> <group description>


Some examples of this:

*  **bsp_arm**: This is the group for the arm architecture. It is a
member of the all inclusive bsp-kit group (more on this in structure
conventions), so we prefix it with the "**bsp**" super group name. This
is the group for the arm architecture, so the rest is just "'''arm'''"

*  **arm_raspberrypi**: This is the group for the Raspberry Pi BSP. It
is is an arm board, and as such, is nested within the bsp_arm group. We
prefix the group name with an "**arm**" (notice we drop the bsp prefix
of the arm group - we only care about the immediate super group),
and the rest is a simple "'''raspberrypi'''", indicating this is the
raspberrypi group, which is nested within the bsp_arm group.

*  **raspberrypi_interrupt** This is the group for code handling
interrupts on the Raspberry Pi platform. Because this code and the group
that envelops it is Raspberry Pi dependent, we prefix our name with a
"**raspberrypi**", indicating this group is nested within the raspberrypi
group.= Structure Conventions =

This covers where, when, and why you should place the second type of
Doxygen header. Remember that our goal is to have the structure of
the documentation to match the organization of the bsps/ directory as
closely as possible. We accomplish this by creating groups for each
cpu architecture, each BSP, and each shared directory. These groups are
nested as appropriate in order to achieve a hierarchy similar to that
of bsps/. The arm_raspberrypi group would be nested within the bsp_arm
group, for example.

Where to place @defgroup
------------------------

Remember how I said it really doesn't matter where you place the
@defgroup? Well, it does and it doesn't. It would be chaotic to place
these anywhere, and almost impossible to tell when you have a @defgroup
and when you don't, so we do have some rules in place to guide where
you should place these.

@defgroups for CPU Architectures and Shared Directories
-------------------------------------------------------

The standardized place for these is within a special doxygen.h file
placed within the particular architectures shared directory. This
doxygen.h file exists solely for this purpose, to provide a standard
place to house the group definitions for CPU architectures and the
shared directory for that architecture. This is done because there is
no single file that all architectures share, so it would be impossible
to declare a standardized location for architecture declarations without
the creation of a new file. This also allows others to quickly determine
if the group for a particular architecture has already been defined or
not. Lets look at the doxygen.h for the arm architecture as an example,
found at arm/shared/doxygen.h:

    .. code-block:: c

         /**
          *  @defgroup bsp_arm ARM
          *
          *  @ingroup bsp_kit
          *
          *  @brief ARM Board Support Packages
          */

         /**
          *  @defgroup arm_shared ARM Shared Modules
          *
          *  @ingroup bsp_arm
          *
          *  @brief ARM Shared Modules
          */


The doxygen.h contains only 2 Doxygen headers, both of which are of
the second type. One header is used to create the groups for the arm
architecture **bsp_arm**, nesting it as part of the bsp_kit group,
and the other creates an **arm_shared** group to house the code that is
shared across all BSPs of this architecture. Because these are the second
type of Doxygen header, where we place them does not matter. This allows
us to place them in a standard doxygen.h file, and the end user is non
the wiser. Note that this .h file should never be included by a .c file,
and that the only group declarations that should be placed here are the
declarations for the CPU Architecture group and the shared group.

There is also a doxygen.h file that exists at the root bsps/shared
directory, to @defgroup the the parent **bsp_kit** group (the only
group to not be nested within any other groups) and to @defgroup
the **bsp_shared** group, to serve as the holder for the bsps/shared
directory.

If the architecture in which the BSP you are tasked with does not have
one of these files already, you will need to copy the format of the file
here, replacing the **arm** with whatever the CPU Architecture you are
working with is. Name this file doxygen.h, and place it in the shared
directory for that architecture.

The only groups you should ever add to this CPU group would be groups
for specific BSPs and a group for the shared directory.

@defgroups for BSPs
-------------------

These are much easier than placing @defgroups for CPU Architectures. The
overwhelming majority of the time, the @defgroup for a BSP is found within
the bsp.h file found at '''''bsp'''''/include/bsp.h. It is usually placed
midway through or towards the end of the file. In the event that your
board lacks a bsp.h file, include this group declaration within the most
standard or commonly included header for that BSP.

The group for a BSP should **always** be nested within the group for
the CPU architecture it uses. This means that the Doxygen header for
defining a BSP group should always look something like this:

    .. code-block:: c

        /**
          *  @defgroup *architecture*_*BSP* *name*
          *
          *  @ingroup bsp_*architecture*
          *
          *  @brief *BSP* Support Package
          */


@defgroups for Everything Else
------------------------------

Never be afraid to add more structure! Once the basic CPU and BSP group
hierarchy is established, what we're left with is all the sub directories
and implementation code. Whether working within a shared directory for
a CPU architecture, or within a BSP directory, you should always be
looking for associations you can make to group files together by. Your
goal should be to avoid @ingroup-ing files directly to the cpu_shared
group and the cpu_bsp group as much as possible, you want to find more
groups you can nest within these groups, and then @ingroup files to
those groups. Here are some things to look for:

Look Common Features Implemented
--------------------------------

Remember that list of common features outlined in the BSP Basics
section? Find the .h's that are responsible for providing the interface
for these features, and @defgroup a group to @ingroup the files
responsible for implementing this feature.

RTEMS has a naming convention for its BSP sub directories, so it should
be a really quick and easy process to determine what features are there
and what is missing.

Examples of this are found within the **arm_raspberrypi** group, which
contains nested subgroups like **raspberry_interrupt** to group files
responsible for handling interrupts, **raspberrypi_usart** to group files
responsible for implementing USART support, and many other subgroups.

Check out the Makefile
----------------------

When working within a BSP, take a look at the Makefile.am. Often times,
you will find that the original developer of the code has outlined the
groups nicely for you already, with comments and titles before including
source files to be built. Also, this is often the only way to tell which
features a BSP simply does not implement, and which features a BSP borrows
from either the architecture's shared group, or the bsps/ shared group.

Start with a .h, and look for files that include it
---------------------------------------------------

You should end up with a @defgroup for ''most'' .h files. Some .h files
are related and will not have independent groups, but most provide
interfaces for different features and should have their own group
defined. Declare a group for the header, then use cscope to find the files
that include this header, and try to determine where the implementation
code for prototypes are found. These are the files you should @ingroup.

Files with similar names
------------------------

If you see that a few files have similar names, like they are all prefixed
with the same characters, then these files should most likely be part
of the same group.

Remember, your goal is to @defgroup as much as you can. The only files
you should be @ingroup-ing directly to the BSP group or the shared group
are files that don't cleanly fit into any other group.

Where to place @ingroup
-----------------------

The @ingroups you add should make sense.

* If you are working within an architecture's shared directory, @ingroup should be adding things either to the *architecture*_shared group, or some sub group of it.

* If you are working within a BSP directory, @ingroup should be adding things to either the *architecture_*bsp* group, or some sub group of it.

@ingroup in the first type of Doxygen Header
--------------------------------------------

Remember that in the first type of Doxygen header, we are adding files
to groups. This type of header should always be at the top of the
file. You should be adding files that are associated in some way to
the same groups. That is to say, if three different .h files provide an
interface allowing interrupt support, they should be a part of the same
group. Some good ways to associate files were outlined above.

@ingroup in the second type of Doxygen Header
---------------------------------------------

Here we are using the @ingroup command to add groups to other groups,
creating a hierarchy. The goal for bsps/ is to have one single group that
holds all other groups. This root group is the **bsp_kit** group. All
groups should be added either directly to this group (if you are creating
an architecture group) or added to one of its sub groups.

When nesting groups, try to match the structure of bsps/ as closely as
possible. For example, if a group is defined to associate all files that
provide for a real time clock for the raspberrypi, nest it within the
arm_raspberrypi group.

@ingroup for shared code
------------------------

This is tricky. You may end up in a situation where your BSP uses code
found in either the architecture shared directory, or the bsps/shared
directory. Even though this code is logically associated with the BSP,
as stated above: all files in the shared directory should be added to
either the *architecture*_shared group, or some subgroup of it ''not''
the BSP group. You could make a note under the @brief line in the header
(which shows up in the resulting documentation) that a particular BSP
uses this code.

When working with shared code, you should be careful and add notes to
@brief to indicate that it is a shared code or interface. Prefixing things
with "Generic" is a good idea here. You will still be able to form groups
and associate things when working on the shared level, but sometimes you
will find that you have the interface (.h) to @defgroup, but not many
files to add to the group as it may be hardware dependent. This is okay.
