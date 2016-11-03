.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 1988-2002.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

Real-Time Clock Driver
######################

Introduction
============

The Real-Time Clock (*RTC*) driver is responsible for providing an interface to
an *RTC* device.  The capabilities provided by this driver are:

- Set the RTC TOD to RTEMS TOD

- Set the RTEMS TOD to the RTC TOD

- Get the RTC TOD

- Set the RTC TOD to the Specified TOD

- Get the Difference Between the RTEMS and RTC TOD

.. note::

  In this chapter, the abbreviation `TOD` is used for *Time of Day*.

The reference implementation for a real-time clock driver can be found in
``c/src/lib/libbsp/shared/tod.c``.  This driver is based on the libchip concept
and can be easily configured to work with any of the RTC chips supported by the
RTC chip drivers in the directory ``c/src/lib/lib/libchip/rtc``.  There is a
README file in this directory for each supported RTC chip.  Each of these
README explains how to configure the shared libchip implementation of the RTC
driver for that particular RTC chip.

The DY-4 DMV177 BSP used the shared libchip implementation of the RTC driver.
There were no DMV177 specific configuration routines.  A BSP could use
configuration routines to dynamically determine what type of real-time clock is
on a particular board.  This would be useful for a BSP supporting multiple
board models.  The relevant ports of the DMV177's ``RTC_Table`` configuration
table is below:

.. code-block:: c

    #include <bsp.h>
    #include <libchip/rtc.h>
    #include <libchip/icm7170.h>

    bool dmv177_icm7170_probe(int minor);

    rtc_tbl RTC_Table[] = {
      { "/dev/rtc0",                 /* sDeviceName */
         RTC_ICM7170,                /* deviceType */
         &icm7170_fns,               /* pDeviceFns */
         dmv177_icm7170_probe,       /* deviceProbe */
         (void *) ICM7170_AT_1_MHZ,  /* pDeviceParams */
         DMV170_RTC_ADDRESS,         /* ulCtrlPort1 */
         0,                          /* ulDataPort */
         icm7170_get_register_8,     /* getRegister */
         icm7170_set_register_8,     /* setRegister */
      }
    };
    unsigned long RTC_Count = (sizeof(RTC_Table)/sizeof(rtc_tbl));
    rtems_device_minor_number RTC_Minor;

    bool dmv177_icm7170_probe(int minor)
    {
      volatile unsigned16 *card_resource_reg;
      card_resource_reg = (volatile unsigned16 *) DMV170_CARD_RESORCE_REG;
      if ( (*card_resource_reg & DMV170_RTC_INST_MASK) == DMV170_RTC_INSTALLED )
        return TRUE;
      return FALSE;
    }

Initialization
==============

The ``rtc_initialize`` routine is responsible for initializing the RTC chip so
it can be used.  The shared libchip implementation of this driver supports
multiple RTCs and bases its initialization order on the order the chips are
defined in the ``RTC_Table``.  Each chip defined in the table may or may not be
present on this particular board.  It is the responsibility of the
``deviceProbe`` to indicate the presence of a particular RTC chip.  The first
RTC found to be present is considered the preferred RTC.

In the shared libchip based implementation of the driver, the following actions
are performed:

.. code-block:: c

    rtems_device_driver rtc_initialize(
      rtems_device_major_number  major,
      rtems_device_minor_number  minor_arg,
      void                      *arg
    )
    {
      for each RTC configured in RTC_Table
        if the deviceProbe for this RTC indicates it is present
          set RTC_Minor to this device
          set RTC_Present to TRUE
          break out of this loop

        if RTC_Present is not TRUE
          return RTEMS_INVALID_NUMBER to indicate that no RTC is present

        register this minor number as the "/dev/rtc"

        perform the deviceInitialize routine for the preferred RTC chip

        for RTCs past this one in the RTC_Table
          if the deviceProbe for this RTC indicates it is present
            perform the deviceInitialize routine for this RTC chip
            register the configured name for this RTC
    }

The ``deviceProbe`` routine returns TRUE if the device configured by this entry
in the ``RTC_Table`` is present.  This configuration scheme allows one to
support multiple versions of the same board with a single BSP.  For example, if
the first generation of a board had Vendor A's RTC chip and the second
generation had Vendor B's RTC chip, RTC_Table could contain information for
both.  The ``deviceProbe`` configured for Vendor A's RTC chip would need to
return TRUE if the board was a first generation one.  The ``deviceProbe``
routines are very board dependent and must be provided by the BSP.

setRealTimeToRTEMS
==================

The ``setRealTimeToRTEMS`` routine sets the current RTEMS TOD to that
of the preferred RTC.

.. code-block:: c

    void setRealTimeToRTEMS(void)
    {
      if no RTCs are present
        return

      invoke the deviceGetTime routine for the preferred RTC
      set the RTEMS TOD using rtems_clock_set
    }

setRealTimeFromRTEMS
====================

The ``setRealTimeFromRTEMS`` routine sets the preferred RTC TOD to the
current RTEMS TOD.

.. code-block:: c

    void setRealTimeFromRTEMS(void)
    {
      if no RTCs are present
        return

      obtain the RTEMS TOD using rtems_clock_get
      invoke the deviceSetTime routine for the preferred RTC
    }

getRealTime
===========

The ``getRealTime`` returns the preferred RTC TOD to the caller.

.. code-block:: c

    void getRealTime( rtems_time_of_day *tod )
    {
      if no RTCs are present
      return

      invoke the deviceGetTime routine for the preferred RTC
    }

setRealTime
===========

The ``setRealTime`` routine sets the preferred RTC TOD to the TOD specified by
the caller.

.. code-block:: c

    void setRealTime( rtems_time_of_day *tod )
    {
      if no RTCs are present
        return

      invoke the deviceSetTime routine for the preferred RTC
    }

checkRealTime
=============

The ``checkRealTime`` routine returns the number of seconds difference between
the RTC TOD and the current RTEMS TOD.

.. code-block:: c

    int checkRealTime( void )
    {
      if no RTCs are present
        return -1

      obtain the RTEMS TOD using rtems_clock_get
      get the TOD from the preferred RTC using the deviceGetTime routine
      convert the RTEMS TOD to seconds
      convert the RTC TOD to seconds

      return the RTEMS TOD in seconds - RTC TOD in seconds
    }
