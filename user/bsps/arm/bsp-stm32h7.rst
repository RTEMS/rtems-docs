.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH

stm32h7
=======

This BSP supports the
`STM32H7 Series <https://www.st.com/en/microcontrollers-microprocessors/stm32h7-series.html>`_.
The BSP is known to run on these boards:

* `STM32H743I-EVAL 2 <https://www.st.com/en/evaluation-tools/stm32h743i-eval.html>`_

Clock Driver
------------

The clock driver uses the `ARMv7-M Systick` module.

Console Driver
--------------

The console driver supports the on-chip UART and USART modules.

Network Interface Driver
------------------------

The network interface driver ``if_stmac`` is provided by the ``libbsd``.

USB Host Driver
---------------

The USB host driver ``dwc_otg`` is provided by the ``libbsd``.
