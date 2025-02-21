.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1989, 2011 On-Line Applications Research Corporation (OAR)

Example Application
*******************

.. code-block:: c
    :linenos:

    /*
    *  This file contains an example of a simple RTEMS
    *  application.  It instantiates the RTEMS Configuration
    *  Information using confdef.h and contains two tasks:
    *  a user initialization task and a simple task.
    */

    #include <rtems.h>

    rtems_task user_application(rtems_task_argument argument);

    rtems_task init_task(
        rtems_task_argument ignored
    )
    {
        rtems_id          tid;
        rtems_status_code status;
        rtems_name        name;

        name = rtems_build_name( 'A', 'P', 'P', '1' )

        status = rtems_task_create(
            name, 1, RTEMS_MINIMUM_STACK_SIZE,
            RTEMS_NO_PREEMPT, RTEMS_FLOATING_POINT, &tid
        );
        if ( status != RTEMS_SUCCESSFUL ) {
            printf( "rtems_task_create failed with status of %d.\n", status );
            exit( 1 );
        }

        status = rtems_task_start( tid, user_application, 0 );
        if ( status != RTEMS_SUCCESSFUL ) {
            printf( "rtems_task_start failed with status of %d.\n", status );
            exit( 1 );
        }

        status = rtems_task_delete( SELF );    /* should not return */

        printf( "rtems_task_delete returned with status of %d.\n", status );
        exit( 1 );
    }

    rtems_task user_application(rtems_task_argument argument)
    {
        /* application specific initialization goes here */
        while ( 1 )  {              /* infinite loop */
            /*  APPLICATION CODE GOES HERE
             *
             *  This code will typically include at least one
             *  directive which causes the calling task to
             *  give up the processor.
             */
        }
    }

    /* The Console Driver supplies Standard I/O. */
    #define CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER
    /* The Clock Driver supplies the clock tick. */
    #define CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
    #define CONFIGURE_MAXIMUM_TASKS 2
    #define CONFIGURE_INIT_TASK_NAME rtems_build_name( 'E', 'X', 'A', 'M' )
    #define CONFIGURE_RTEMS_INIT_TASKS_TABLE
    #define CONFIGURE_INIT
    #include <rtems/confdefs.h>
