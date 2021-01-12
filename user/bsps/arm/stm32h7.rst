.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH

stm32h7
=======

This BSP supports the
`STM32H7 Series <https://www.st.com/en/microcontrollers-microprocessors/stm32h7-series.html>`_.

The BSP is known to run on these boards:

* `STM32H743I-EVAL 2 <https://www.st.com/en/evaluation-tools/stm32h743i-eval.html>`_
* `STM32H743ZI-Nucleo <https://www.st.com/en/evaluation-tools/nucleo-h743zi.html>`_

Clock Driver
------------

The clock driver uses the `ARMv7-M Systick` module. The HSE (external
oscillator) value can also be different for different evaluation or custom
boards, so it is recommended to check the default values of the BSP.

Console Driver
--------------

The console driver supports the on-chip UART and USART modules.
Different board variations use different GPIO pins and blocks for the default
communication UART and it is recommended to check whether the default
configuration provided is valid in the BSP.

To specify that the BSP should be built for the STM32H743ZI-Nucleo board,
users can supply ``STM32H743ZI_NUCLEO = True`` to ``config.ini`` when
building the BSP.

Alternatively, users can supply the configuration structs defined in ``hal.h``
in the application for other boards. For the console driver, the
``stm32h7_usartX_config`` structs are used to configure the GPIO pins and other
parameters. The default implementations can be found in
``bsps/arm/stm32ht/console`` in the RTEMS sources.

Network Interface Driver
------------------------

The network interface driver ``if_stmac`` is provided by the ``libbsd``.

USB Host Driver
---------------

The USB host driver ``dwc_otg`` is provided by the ``libbsd``.
