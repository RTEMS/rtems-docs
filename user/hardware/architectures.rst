.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH & Co. KG
.. Copyright (C) 2019 Sebastian Huber
.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _TargetArchitectures:

Architectures
=============

.. index:: Architectures

An RTEMS architecture is a class or family of a processor architecture that
RTEMS supports.  The RTEMS architecture model follows the architecture model of
GCC. An architecture in GCC results in a specific RTEMS GCC compiler. This
compiler may support a range of processors in the family that may have
differences in instructions sets, floating point support or other aspects.
RTEMS configures GCC to create separate runtime libraries for each supported
instruction set, floating point unit, vector unit, word size (e.g. 32-bit and
64-bit), endianess, code model, :ref:term:`ABI`, processor errata workarounds,
and so on in the architecture. This is termed *multilib*. Multilibs are chosen
automatically by GCC via selecting a specific set of machine options.

You can query the multilibs of a specific RTEMS GCC compiler via the
``-print-multi-lib`` option:

.. code-block:: none

    $ sparc-rtems5-gcc -print-multi-lib
    .;
    soft;@msoft-float
    v8;@mcpu=v8
    leon3;@mcpu=leon3
    leon3v7;@mcpu=leon3v7
    leon;@mcpu=leon
    leon3/gr712rc;@mcpu=leon3@mfix-gr712rc
    leon3v7/gr712rc;@mcpu=leon3v7@mfix-gr712rc
    leon/ut699;@mcpu=leon@mfix-ut699
    leon/at697f;@mcpu=leon@mfix-at697f
    soft/v8;@msoft-float@mcpu=v8
    soft/leon3;@msoft-float@mcpu=leon3
    soft/leon3v7;@msoft-float@mcpu=leon3v7
    soft/leon;@msoft-float@mcpu=leon
    soft/leon3/gr712rc;@msoft-float@mcpu=leon3@mfix-gr712rc
    soft/leon3v7/gr712rc;@msoft-float@mcpu=leon3v7@mfix-gr712rc
    soft/leon/ut699;@msoft-float@mcpu=leon@mfix-ut699
    soft/leon/at697f;@msoft-float@mcpu=leon@mfix-at697f

Each printed line represents a multilib.  The ``.`` corresponds to the default
multilib.  It is used if a set of machine options does not match to a
specialized multilib.  The string before the ``;`` describes the directory in
the GCC installation used for the particular multilib.  After the ``;`` the set
of machine options for this multilib follows separated by ``@`` characters.

You can figure out the multilib selected by GCC for a set of machine options
with the ``-print-multi-directory`` option:

.. code-block:: none

    $ sparc-rtems5-gcc -print-multi-directory -mcpu=leon3
    leon3

It is crucial that the RTEMS BSP, support libraries and the application code
are compiled consistently with a compatible set of machine options.  Otherwise,
in the best case errors during linking will occur or you may end up silently
with undefined behaviour which results in sporadic run-time crashes.  A wrong
set of machine options may result in a running application, however, with
degraded performance, e.g. hardware floating point unit is not used by the
mathematical library.

For a list of architectures supported by RTEMS please have a look at the
sections of the :ref:`Board Support Packages <BSPs>` chapter.

:ref:`RTEMS executables <Executables>` are statically linked for a specific
target therefore a precise and exact match can be made for the hardware that
extracts the best possible performance. The compiler supports the variants to
the instruction set and RTEMS extends the specialization to specific processors
in an architecture. This specialization gives RTEMS a finer resolution of
features and capabilities a specific device may offer allowing the kernel,
drivers and application to make the most of those resources. The trade off is
portability however this is not important because the executable are statically
linked for a single target.

.. note::

   RTEMS support dynamically load code through the ``dlopen``
   interface. Loading code via this interface results in an executable image
   that is equivalent to statically linked executable of the same code. Dynamic
   loading is a system level tool for system architects.
