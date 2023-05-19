.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 embedded brains GmbH & Co. KG

fvp (Fixed Virtual Platform)
============================

The BSP for the
`Arm Fixed Virtual Platforms <https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms>`_
offers one variant.  You need a license from Arm to run the simulator.  The
`fvp_cortex_r52` variant supports a simulation of the Cortex-R52 processor.
The BSP supports the SMP configuration.

Run an Executable
-----------------

To run an executable on a single Cortex-R52 processor use:

.. code-block:: none

    FVP_BaseR_Cortex-R52x1 -C bp.vis.disable_visualisation=1 -a build/arm/fvp_cortex_r52/testsuites/samples/ticker.exe

To run an executable on a four Cortex-R52 processors use:

.. code-block:: none

    FVP_BaseR_Cortex-R52x4 -C bp.vis.disable_visualisation=1 -a build/arm/fvp_cortex_r52/testsuites/samples/ticker.exe

Clock Driver
------------

The clock driver uses the `ARMv7-AR Generic Timer`.

Console Driver
--------------

The console driver uses the
`semihosting <https://developer.arm.com/documentation/dui0471/g/Semihosting/Semihosting-operations?lang=en>`_
``SYS_READC`` and ``SYS_WRITEC`` system calls.
