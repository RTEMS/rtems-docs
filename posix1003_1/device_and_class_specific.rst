Device- and Class-Specific Functions
####################################

General Terminal Interface
==========================

Interface Characteristics
-------------------------

Opening a Terminal Device File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Process Groups (TTY)
~~~~~~~~~~~~~~~~~~~~

The Controlling Terminal
~~~~~~~~~~~~~~~~~~~~~~~~

Terminal Access Control
~~~~~~~~~~~~~~~~~~~~~~~

Input Processing and Reading Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Canonical Mode Input Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Noncanonical Mode Input Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Case A - MIN > 0 and TIME > 0

- Case B - MIN > 0 and TIME = 0

- Case C - MIN = 0 and TIME > 0

- Case D - MIN = 0 and TIME = 0

Writing Data and Output Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Special Characters
~~~~~~~~~~~~~~~~~~

.. code:: c

    INTR, Constant, Implemented
    QUIT, Constant, Implemented
    ERASE, Constant, Implemented
    KILL, Constant, Implemented
    EOF, Constant, Implemented
    NL, Constant, Implemented
    EOL, Constant, Implemented
    SUSP, Constant, Implemented
    STOP, Constant, Implemented
    START, Constant, Implemented
    CR, Constant, Implemented

Modem Disconnect
~~~~~~~~~~~~~~~~

Closing a Terminal Device File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameters That Can Be Set
--------------------------

termios Structure
~~~~~~~~~~~~~~~~~

.. code:: c

    tcflag_t, Type, Implemented
    cc_t, Type, Implemented
    struct termios, Type, Implemented

Input Modes
~~~~~~~~~~~

.. code:: c

    BRKINT, Constant, Implemented
    ICRNL, Constant, Implemented
    IGNBREAK, Constant, Unimplemented
    IGNCR, Constant, Implemented
    IGNPAR, Constant, Implemented
    INLCR, Constant, Implemented
    INPCK, Constant, Implemented
    ISTRIP, Constant, Implemented
    IXOFF, Constant, Implemented
    IXON, Constant, Implemented
    PARMRK, Constant, Implemented

Output Modes
~~~~~~~~~~~~

.. code:: c

    OPOST, Constant, Implemented

Control Modes
~~~~~~~~~~~~~

.. code:: c

    CLOCAL, Constant, Implemented
    CREAD, Constant, Implemented
    CSIZE, Constant, Implemented
    CS5, Constant, Implemented
    CS6, Constant, Implemented
    CS7, Constant, Implemented
    CS8, Constant, Implemented
    CSTOPB, Constant, Implemented
    HUPCL, Constant, Implemented
    PARENB, Constant, Implemented
    PARODD, Constant, Implemented

Local Modes
~~~~~~~~~~~

.. code:: c

    ECHO, Constant, Implemented
    ECHOE, Constant, Implemented
    ECHOK, Constant, Implemented
    ECHONL, Constant, Implemented
    ICANON, Constant, Implemented
    IEXTEN, Constant, Implemented
    ISIG, Constant, Implemented
    NOFLSH, Constant, Implemented
    TOSTOP, Constant, Implemented

Special Control Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: c

    VEOF, Constant, Implemented
    VEOL, Constant, Implemented
    VERASE, Constant, Implemented
    VINTR, Constant, Implemented
    VKILL, Constant, Implemented
    VQUIT, Constant, Implemented
    VSUSP, Constant, Implemented
    VSTART, Constant, Implemented
    VSTOP, Constant, Implemented
    VMIN, Constant, Implemented
    VTIME, Constant, Implemented

Baud Rate Values
----------------

.. code:: c

    B0, Constant, Implemented
    B50, Constant, Implemented
    B75, Constant, Implemented
    B110, Constant, Implemented
    B134, Constant, Implemented
    B150, Constant, Implemented
    B200, Constant, Implemented
    B300, Constant, Implemented
    B600, Constant, Implemented
    B1200, Constant, Implemented
    B1800, Constant, Implemented
    B2400, Constant, Implemented
    B4800, Constant, Implemented
    B9600, Constant, Implemented
    B19200, Constant, Implemented
    B38400, Constant, Implemented

Baud Rate Functions
~~~~~~~~~~~~~~~~~~~

.. code:: c

    cfgetospeed(), Function, Implemented
    cfsetospeed(), Function, Implemented
    cfgetispeed(), Function, Implemented
    cfsetispeed(), Function, Implemented
    TCIFLUSH, Constant, Implemented
    TCOFLUSH, Constant, Implemented
    TCIOFLUSH, Constant, Implemented
    TCOOFF, Constant, Implemented
    TCOON, Constant, Implemented
    TCIOOFF, Constant, Implemented
    TCIOON, Constant, Implemented

General Terminal Interface Control Functions
============================================

Get and Set State
-----------------

.. code:: c

    tcgetattr(), Function, Implemented
    tcsetattr(), Function, Implemented

Line Control Functions
----------------------

.. code:: c

    tcsendbreak(), Function, Dummy Implementation
    tcdrain(), Function, Implemented
    tcflush(), Function, Dummy Implementation
    tcflow(), Function, Dummy Implementation

Get Foreground Process Group ID
-------------------------------

.. code:: c

    tcgetprgrp(), Function, Implemented, SUSP

Set Foreground Process Group ID
-------------------------------

.. code:: c

    tcsetprgrp(), Function, Dummy Implementation

.. COMMENT: COPYRIGHT (c) 1988-2002.

.. COMMENT: On-Line Applications Research Corporation (OAR).

.. COMMENT: All rights reserved.

