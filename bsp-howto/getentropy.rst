.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2017 embedded brains GmbH & Co. KG

Entropy Source
**************

Each BSP must provide an implementation of the :c:func:`getentropy` system
call.  This system call was introduced by
`OpenBSD <https://man.openbsd.org/getentropy.2>`_
and is also available in
`glibc since version 2.25 <http://man7.org/linux/man-pages/man3/getentropy.3.html>`_.
This system call is used by the Newlib provided
`ARC4RANDOM(3) <https://man.openbsd.org/arc4random.3>`_ functions, which in
turn are used by various cryptographic functions.

.. warning::
    A good entropy source is critical for (nearly) all cryptographic
    applications. The default implementation based on the CPU counter is not
    suitable for such applications.

The :c:func:`getentropy` implementation must fill the specified memory region
of the given size with random numbers and return 0 on success.  A non-zero
return may cause the :c:macro:`INTERNAL_ERROR_ARC4RANDOM_GETENTROPY_FAIL`
internal error by one of the
`ARC4RANDOM(3) <https://man.openbsd.org/arc4random.3>`_ functions.

In general, for embedded systems it is not easy to get some real entropy. Normally,
that can only be reached with some extra hardware support. Some microcontrollers
integrate a true random number generator or something similar for cryptographic
applications. That is the preferred source of entropy for most BSPs. For example
the
`atsam BSP uses the TRNG for its entropy source <https://git.rtems.org/rtems/tree/bsps/arm/atsam/start/getentropy-trng.c>`_.

There is also a quite limited
`default implementation based on the CPU counter <https://git.rtems.org/rtems/tree/bsps/shared/dev/getentropy/getentropy-cpucounter.c>`_.
Due to the fact that it is a time based source, the values provided by
:c:func:`getentropy` are quite predictable. This implementation is not
appropriate for any cryptographic applications but it is good enough for some
basic tasks. Use it only if you do not have any strong requirements on the
entropy and if there is no better source.
