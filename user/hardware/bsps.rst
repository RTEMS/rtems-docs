.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. _bsps:

Board Support Packages (BSP)
============================
.. index:: Board Support Package
.. index:: BSP

A Board Suport Package is a historical term for a package of code, and
supporting documentation for a target. The sparation is still important today
for users with custom hardware.

RTEMS includes 173 board support packages in it's source tree and this is a
small number of actual targets running because it does not take into account
the custom targets.

You can see the BSP list in RTEMS by asking RTEMS with:

.. code-block:: shell

  $ ./rtems-bsps
