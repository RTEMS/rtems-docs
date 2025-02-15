.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020, 2021 embedded brains GmbH & Co. KG
.. Copyright (C) 2015 On-Line Applications Research Corporation (OAR)

.. This file is part of the RTEMS quality process and was automatically
.. generated.  If you find something that needs to be fixed or
.. worded better please post a report or patch to an RTEMS mailing list
.. or raise a bug report:
..
.. https://www.rtems.org/bugs.html
..
.. For information on updating and regenerating please refer to the How-To
.. section in the Software Requirements Engineering chapter of the
.. RTEMS Software Engineering manual.  The manual is provided as a part of
.. a release.  For development sources please refer to the online
.. documentation at:
..
.. https://docs.rtems.org

.. _KernelCharacterIOSupportDirectives:

Directives
==========

This section details the directives of the Kernel Character I/O Support. A
subsection is dedicated to each of this manager's directives and lists the
calling sequence, parameters, description, return values, and notes of the
directive.

.. Generated from spec:/rtems/io/if/putc

.. raw:: latex

    \clearpage

.. index:: rtems_putc()

.. _InterfaceRtemsPutc:

rtems_putc()
------------

Outputs the character to the kernel character output device.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_putc( char c );

.. rubric:: PARAMETERS:

``c``
    This parameter is the character to output.

.. rubric:: DESCRIPTION:

The directive outputs the character specified by ``c`` to the kernel character
output device using the polled character output implementation provided by
BSP_output_char.  The directive performs a character translation from ``NL`` to
``CR`` followed by ``NR``.

If the kernel character output device is concurrently accessed, then
interleaved output may occur.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/io/if/put-char

.. raw:: latex

    \clearpage

.. index:: rtems_put_char()

.. _InterfaceRtemsPutChar:

rtems_put_char()
----------------

Puts the character using :ref:`InterfaceRtemsPutc`

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    void rtems_put_char( int c, void *unused );

.. rubric:: PARAMETERS:

``c``
    This parameter is the character to output.

``unused``
    This parameter is an unused argument.

.. rubric:: NOTES:

The directive is provided to support the RTEMS Testing Framework.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/io/if/putk

.. raw:: latex

    \clearpage

.. index:: putk()

.. _InterfacePutk:

putk()
------

Outputs the characters of the string and a newline character to the kernel
character output device.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    int putk( const char *s );

.. rubric:: PARAMETERS:

``s``
    This parameter is the string to output.

.. rubric:: RETURN VALUES:

Returns the number of characters output to the kernel character output device.

.. rubric:: NOTES:

The directive may be used to print debug and test information.  It uses
:ref:`InterfaceRtemsPutc` to output the characters.  This directive performs a
character translation from ``NL`` to ``CR`` followed by ``NR``.

If the kernel character output device is concurrently accessed, then
interleaved output may occur.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

.. Generated from spec:/rtems/io/if/printk

.. raw:: latex

    \clearpage

.. index:: printk()

.. _InterfacePrintk:

printk()
--------

Outputs the characters defined by the format string and the arguments to the
kernel character output device.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    int printk( const char *fmt, ... );

.. rubric:: PARAMETERS:

``fmt``
    This parameter is a printf()-style format string.

``...``
    This parameter is a list of optional parameters required by the format
    string.

.. rubric:: RETURN VALUES:

Returns the number of characters output to the kernel character output device.

.. rubric:: NOTES:

The directive may be used to print debug and test information.  It uses
:ref:`InterfaceRtemsPutc` to output the characters.  This directive performs a
character translation from ``NL`` to ``CR`` followed by ``NR``.

If the kernel character output device is concurrently accessed, then
interleaved output may occur.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* Formatting of floating point numbers is not supported.

.. Generated from spec:/rtems/io/if/vprintk

.. raw:: latex

    \clearpage

.. index:: vprintk()

.. _InterfaceVprintk:

vprintk()
---------

Outputs the characters defined by the format string and the variable argument
list to the kernel character output device.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    int vprintk( const char *fmt, va_list ap );

.. rubric:: PARAMETERS:

``fmt``
    This parameter is a printf()-style format string.

``ap``
    This parameter is the variable argument list required by the format string.

.. rubric:: RETURN VALUES:

Returns the number of characters output to the kernel character output device.

.. rubric:: NOTES:

The directive may be used to print debug and test information.  It uses
:ref:`InterfaceRtemsPutc` to output the characters.  This directive performs a
character translation from ``NL`` to ``CR`` followed by ``NR``.

If the kernel character output device is concurrently accessed, then
interleaved output may occur.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* Formatting of floating point numbers is not supported.

.. Generated from spec:/rtems/io/if/printk-printer

.. raw:: latex

    \clearpage

.. index:: rtems_printk_printer()

.. _InterfaceRtemsPrintkPrinter:

rtems_printk_printer()
----------------------

Outputs the characters defined by the format string and the variable argument
list to the kernel character output device.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    int rtems_printk_printer( void *unused, const char *fmt, va_list ap );

.. rubric:: PARAMETERS:

``unused``
    This parameter is an unused argument.

``fmt``
    This parameter is a printf()-style format string.

``ap``
    This parameter is the variable argument list required by the format string.

.. rubric:: RETURN VALUES:

Returns the number of characters output to the kernel character output device.

.. rubric:: NOTES:

The directive may be used to print debug and test information.  It uses
:ref:`InterfaceRtemsPutc` to output the characters.  This directive performs a
character translation from ``NL`` to ``CR`` followed by ``NR``.

If the kernel character output device is concurrently accessed, then
interleaved output may occur.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.

* Formatting of floating point numbers is not supported.

.. Generated from spec:/rtems/io/if/getchark

.. raw:: latex

    \clearpage

.. index:: getchark()

.. _InterfaceGetchark:

getchark()
----------

Tries to dequeue a character from the kernel character input device.

.. rubric:: CALLING SEQUENCE:

.. code-block:: c

    int getchark( void );

.. rubric:: DESCRIPTION:

The directive tries to dequeue a character from the kernel character input
device using the polled character input implementation referenced by
BSP_poll_char if it is available.

.. rubric:: RETURN VALUES:

``-1``
    The BSP_poll_char pointer was equal to `NULL
    <https://en.cppreference.com/w/c/types/NULL>`_.

``-1``
    There was no character enqueued on the kernel character input device.

Returns the character least recently enqueued on the kernel character input
device as an unsigned character value.

.. rubric:: CONSTRAINTS:

The following constraints apply to this directive:

* The directive may be called from within any runtime context.

* The directive will not cause the calling task to be preempted.
