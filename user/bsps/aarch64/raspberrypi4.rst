.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Mohd Noor Aman

.. _BSP_aarch64_Raspberrypi_4:

Raspberry Pi 4B
===============

The 'raspberrypi4b' BSP currently supports only the LP64 ABI. ILP32 is not
supported. Raspberry pi 4B all variants and Raspberry Pi 400  are supported. The
default bootloader which is used by the Raspbian OS or other OS can be used to
boot RTEMS. SMP is currently not supported.

Raspberry Pi 4B has 2 types of interrupt controller, GIC-400 (GICv2) and ARM
legacy generic controller. Both are supported. By default, raspberrypi 4B uses
ARM legacy generic controller. Set ``enable_gic=1`` in the ``config.txt`` file
to enable GIC.

Clock Driver
------------

The clock driver uses the `ARM Generic Timer`.

Console Driver
--------------

Raspberry pi 4B has 2 types of UARTs, ARM PL011 and Mini-uart. The PL011 is a
capable, broadly 16550-compatible UART, while the mini UART has a reduced
feature set. The console driver supports the default Qemu emulated ARM PL011
PrimeCell UART as well as the physical ARM PL011 PrimeCell UART in the
raspberrypi hardware. Mini-uart is not supported.

GPIO Driver
-----------

The GPIO of Raspberry pi 4B can be controlled by the following functions:
``raspberrypi_gpio_set_function()``
``raspberrypi_gpio_set_pin()``
``raspberrypi_gpio_clear_pin()``
``raspberrypi_gpio_set_pull()``

.. code-block:: none
  #include <bsp/rpi-gpio.h>

  void gpio(void)
  {
    /* Define the operation of the general-purpose I/O pins. Each of the 58
     * GPIO pins has at least two alternative functions as defined.
     * The optional functions are GPIO_INPUT, GPIO_OUTPUT, GPIO_AF5, GPIO_AF4,
     * GPIO_AF0, GPIO_AF1, GPIO_AF2, GPIO_AF3
     */
    raspberrypi_gpio_set_function(8, GPIO_AF0);

    /* Control the actuation of the internal pull-up/down resistors. 
     * The optional value are GPIO_PULL_NONE, GPIO_PULL_UP, GPIO_PULL_DOWN
     */
    raspberrypi_gpio_set_pull(8, GPIO_PULL_NONE);

    /* Clear a GPIO pin. */
    raspberrypi_gpio_clear_pin(8);
    
    /* Set a GPIO pin. */
    raspberrypi_gpio_set_pin(8);
  }

Preparing to boot
------------------

Raspberry Pi uses a different mechanism to boot when compared with any ARM SoC.
First the GPU initializes, loads the bootloader (Raspberry pi firmware) and then
looks for the kernel img. This whole process is done by the GPU (VideoCore IV)
till the kernel is loaded. More information can be found on the `Raspberry pi
documentation page
<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#boot-sequence>`_.
By default the arm64 mode looks for the ``kernel8.img``. Any other kernel can be
loaded by adding ``kernel=<img_name>`` to the ``config.txt`` file.

The Firmware files are required in order to boot RTEMS. The latest firmware can
be downloaded from the `Raspberry Pi Firmware Repository
<https://github.com/raspberrypi/firmware/>`_. USB boot is supported. All the
files (Firmwares and kernel) must be place in the FAT32 partition only. Add
``arm_64bit=1`` in the ``config.txt`` file in order to boot the BSP in 64bit
kernel mode.


UART Setup
^^^^^^^^^^

Connect your serial device to the GPIO15 and GPIO14. Add the following to the
``config.txt`` file in order to use the PL011 UART0 and thus disabling the
default Mini-uart.

.. code-block:: none

  # if user wants to enable GIC, uncomment the next line
  # enable_gic=1
  arm_64bit=1
  dtoverlay = disable-bt
  enable_uart=1

.. note::
  The Raspberry Pi 4B and 400 have an additional four PL011 UARTs. They are not
  supported.

Generating kernel image
^^^^^^^^^^^^^^^^^^^^^^^

The following steps show how to run ``hello.exe`` on the BSP. Other executables
can be processed in a similar way.

To create the kernel image:

.. code-block:: shell

  $ aarch64-rtems@rtems-ver-major@-objcopy -Obinary hello.exe kernel8.img

Copy the kernel image to the SD card.

JTAG Setup
----------

The Raspberry Pi 4 doesn't have dedicated JTAG pins. Instead, you must configure
the GPIO pins (GPIO22-GPIO27) to activate the JTAG functionality. The RPi 4
documentation refers to this as Alt4 functions of those pins. Alt5 does exist
too, which goes from GPIO4, 5, 6, 12 and 13. you can check this out from
`pinout.xyz <https://pinout.xyz/pinout/jtag#>`_ or `eLinux
<https://elinux.org/RPi_BCM2835_GPIOs>`_

One more thing to note on JTAG with Raspberry pi 4B is that, by default, All the
GPIO pins are pulled down, according to the `BCM2711 documentation
<https://datasheets.raspberrypi.com/bcm2711/bcm2711-peripherals.pdf>`_. This
wasn't the case in the earlier models. So in order to let the data flow freely,
we will have to disable them.

.. code-block:: none

  # Disable pull downs
  gpio=22-27=np

  # Enable jtag pins (i.e. GPIO22-GPIO27)
  enable_jtag_gpio=1
