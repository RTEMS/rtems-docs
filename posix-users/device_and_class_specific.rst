.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2002 On-Line Applications Research Corporation (OAR)

Device- and Class- Specific Functions Manager
#############################################

Introduction
============

The device- and class- specific functions manager is ...

The directives provided by the device- and class- specific functions manager
are:

- cfgetispeed_ - Reads terminal input baud rate

- cfgetospeed_ - Reads terminal output baud rate

- cfsetispeed_ - Sets terminal input baud rate

- cfsetospeed_ - Set terminal output baud rate

- tcgetattr_ - Gets terminal attributes

- tcsetattr_ - Set terminal attributes

- tcsendbreak_ - Sends a break to a terminal

- tcdrain_ - Waits for all output to be transmitted to the terminal

- tcflush_ - Discards terminal data

- tcflow_ - Suspends/restarts terminal output

- tcgetpgrp_ - Gets foreground process group ID

- tcsetpgrp_ - Sets foreground process group ID

Background
==========

There is currently no text in this section.

Operations
==========

There is currently no text in this section.

Directives
==========

This section details the device- and class- specific functions manager's
directives. A subsection is dedicated to each of this manager's directives
and describes the calling sequence, related constants, usage,
and status codes.

.. _cfgetispeed:

cfgetispeed - Reads terminal input baud rate
--------------------------------------------
.. index:: cfgetispeed
.. index:: reads terminal input baud rate

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    speed_t cfgetispeed(
        const struct termios *termios_p
    );

**STATUS CODES:**

The ``cfgetispeed()`` function returns a code for baud rate.

**DESCRIPTION:**

The ``cfsetispeed()`` function stores a code for the terminal speed stored in a
struct termios. The codes are defined in ``<termios.h>`` by the macros ``BO``,
``B50``, ``B75``, ``B110``, ``B134``, ``B150``, ``B200``, ``B300``, ``B600``,
``B1200``, ``B1800``, ``B2400``, ``B4800``, ``B9600``, ``B19200``, and
``B38400``.

The ``cfsetispeed()`` function does not do anything to the hardware.  It merely
stores a value for use by ``tcsetattr()``.

**NOTES:**

Baud rates are defined by symbols, such as ``B110``, ``B1200``, ``B2400``. The
actual number returned for any given speed may change from system to system.

.. _cfgetospeed:

cfgetospeed - Reads terminal output baud rate
---------------------------------------------
.. index:: cfgetospeed
.. index:: reads terminal output baud rate

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    speed_t cfgetospeed(
        const struct termios *termios_p
    );

**STATUS CODES:**

The ``cfgetospeed()`` function returns the termios code for the baud rate.

**DESCRIPTION:**

The ``cfgetospeed()`` function returns a code for the terminal speed stored in
a ``struct termios``. The codes are defined in ``<termios.h>`` by the macros
``BO``, ``B50``, ``B75``, ``B110``, ``B134``, ``B150``, ``B200``, ``B300``,
``B600``, ``B1200``, ``B1800``, ``B2400``, ``B4800``, ``B9600``, ``B19200``,
and ``B38400``.

The ``cfgetospeed()`` function does not do anything to the hardware.  It merely
returns the value stored by a previous call to ``tcgetattr()``.

**NOTES:**

Baud rates are defined by symbols, such as ``B110``, ``B1200``, ``B2400``. The
actual number returned for any given speed may change from system to system.

.. _cfsetispeed:

cfsetispeed - Sets terminal input baud rate
-------------------------------------------
.. index:: cfsetispeed
.. index:: sets terminal input baud rate

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int cfsetispeed(
        struct termios *termios_p,
        speed_t speed
    );

**STATUS CODES:**

The ``cfsetispeed()`` function returns a zero when successful and returns -1
when an error occurs.

**DESCRIPTION:**

The ``cfsetispeed()`` function stores a code for the terminal speed stored in a
struct termios. The codes are defined in ``<termios.h>`` by the macros ``BO``,
``B50``, ``B75``, ``B110``, ``B134``, ``B150``, ``B200``, ``B300``, ``B600``,
``B1200``, ``B1800``, ``B2400``, ``B4800``, ``B9600``, ``B19200``, and
``B38400``.

**NOTES:**

This function merely stores a value in the ``termios`` structure. It does not
change the terminal speed until a ``tcsetattr()`` is done.  It does not detect
impossible terminal speeds.

.. _cfsetospeed:

cfsetospeed - Sets terminal output baud rate
--------------------------------------------
.. index:: cfsetospeed
.. index:: sets terminal output baud rate

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int cfsetospeed(
        struct termios *termios_p,
        speed_t speed
    );

**STATUS CODES:**

The ``cfsetospeed()`` function returns a zero when successful and
returns -1 when an error occurs.

**DESCRIPTION:**

The ``cfsetospeed()`` function stores a code for the terminal speed stored in a
struct ``termios``. The codes are defiined in ``<termios.h>`` by the macros
``BO``, ``B50``, ``B75``, ``B110``, ``B134``, ``B150``, ``B200``, ``B300``,
``B600``, ``B1200``, ``B1800``, ``B2400``, ``B4800``, ``B9600``, ``B19200``,
and ``B38400``.

The ``cfsetospeed()`` function does not do anything to the hardware. It merely
stores a value for use by ``tcsetattr()``.

**NOTES:**

This function merely stores a value in the ``termios`` structure.  It does not
change the terminal speed until a ``tcsetattr()`` is done.  It does not detect
impossible terminal speeds.

.. _tcgetattr:

tcgetattr - Gets terminal attributes
------------------------------------
.. index:: tcgetattr
.. index:: gets terminal attributes

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int tcgetattr(
        int fildes,
        struct termios *termios_p
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
 * - ``ENOOTY``
   - Terminal control function attempted for a file that is not a terminal.

**DESCRIPTION:**

The ``tcgetattr()`` gets the parameters associated with the terminal referred
to by ``fildes`` and stores them into the ``termios()`` structure pointed to by
``termios_p``.

**NOTES:**

NONE

.. _tcsetattr:

tcsetattr - Set terminal attributes
-----------------------------------
.. index:: tcsetattr
.. index:: set terminal attributes

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int tcsetattr(
        int fildes,
        int optional_actions,
        const struct termios *termios_p
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

.. _tcsendbreak:

tcsendbreak - Sends a break to a terminal
-----------------------------------------
.. index:: tcsendbreak
.. index:: sends a break to a terminal

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int tcsendbreak(
        int fildes,
        int duration
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be
in a future version.

.. _tcdrain:

tcdrain - Waits for all output to be transmitted to the terminal.
-----------------------------------------------------------------
.. index:: tcdrain
.. index:: waits for all output to be transmitted to the terminal.

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int tcdrain(
        int fildes
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``EBADF``
   - Invalid file descriptor
 * - ``EINTR``
   - Function was interrupted by a signal
 * - ``ENOTTY``
   - Terminal control function attempted for a file that is not a terminal.

**DESCRIPTION:**

The ``tcdrain()`` function waits until all output written to ``fildes`` has been
transmitted.

**NOTES:**

NONE

.. _tcflush:

tcflush - Discards terminal data
--------------------------------
.. index:: tcflush
.. index:: discards terminal data

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int tcflush(
        int fildes,
        int queue_selector
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be in a future
version.

.. _tcflow:

tcflow - Suspends/restarts terminal output.
-------------------------------------------
.. index:: tcflow
.. index:: suspends/restarts terminal output.

**CALLING SEQUENCE:**

.. code-block:: c

    #include <termios.h>
    int tcflow(
        int fildes,
        int action
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be in a future
version.

.. _tcgetpgrp:

tcgetpgrp - Gets foreground process group ID
--------------------------------------------
.. index:: tcgetpgrp
.. index:: gets foreground process group id

**CALLING SEQUENCE:**

.. code-block:: c

    #include <unistd.h>
    pid_t tcgetpgrp(
        int fildes
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be in a future
version.

.. _tcsetpgrp:

tcsetpgrp - Sets foreground process group ID
--------------------------------------------
.. index:: tcsetpgrp
.. index:: sets foreground process group id

**CALLING SEQUENCE:**

.. code-block:: c

    #include <unistd.h>
    int tcsetpgrp(
        int fildes,
        pid_t pgid_id
    );

**STATUS CODES:**

.. list-table::
 :class: rtems-table

 * - ``E``
   - The

**DESCRIPTION:**

**NOTES:**

This routine is not currently supported by RTEMS but could be in a future
version.
