.. COMMENT: COPYRIGHT (c) 1988-2008.
.. COMMENT: On-Line Applications Research Corporation (OAR).
.. COMMENT: All rights reserved.

RTEMS Data Types
################

Introduction
============

This chapter contains a complete list of the RTEMS primitive data types in
alphabetical order.  This is intended to be an overview and the user is
encouraged to look at the appropriate chapters in the manual for more
information about the usage of the various data types.

List of Data Types
==================

The following is a complete list of the RTEMS primitive data types in
alphabetical order:

.. index:: rtems_address

``rtems_address``
  The data type used to manage addresses.  It is equivalent to a ``void *``
  pointer.

.. index:: rtems_asr

``rtems_asr``
  The return type for an RTEMS ASR.

.. index:: rtems_asr_entry

``rtems_asr_entry``
  The address of the entry point to an RTEMS ASR.

 .. index:: rtems_attribute

``rtems_attribute``
  The data type used to manage the attributes for RTEMS objects.  It is
  primarily used as an argument to object create routines to specify
  characteristics of the new object.

.. index:: rtems_boolean

``rtems_boolean``
  May only take on the values of ``TRUE`` and ``FALSE``.  This type is
  deprecated. Use ``bool`` instead.

.. index:: rtems_context

``rtems_context``
  The CPU dependent data structure used to manage the integer and system
  register portion of each task's context.

.. index:: rtems_context_fp

``rtems_context_fp``
  The CPU dependent data structure used to manage the floating point portion of
  each task's context.

.. index:: rtems_device_driver

``rtems_device_driver``
  The return type for a RTEMS device driver routine.

.. index:: rtems_device_driver_entry

``rtems_device_driver_entry``
  The entry point to a RTEMS device driver routine.

.. index:: rtems_device_major_number

``rtems_device_major_number``
  The data type used to manage device major numbers.

.. index:: rtems_device_minor_number

``rtems_device_minor_number``
  The data type used to manage device minor numbers.

.. index:: rtems_double

``rtems_double``
  The RTEMS data type that corresponds to double precision floating point on
  the target hardware.  This type is deprecated. Use ``double`` instead.

.. index:: rtems_event_set

``rtems_event_set``
  The data type used to manage and manipulate RTEMS event sets with the Event
  Manager.

.. index:: rtems_extension

``rtems_extension``
  The return type for RTEMS user extension routines.

.. index:: rtems_fatal_extension

``rtems_fatal_extension``

  The entry point for a fatal error user extension handler routine.

.. index:: rtems_id

``rtems_id``
  The data type used to manage and manipulate RTEMS object IDs.

.. index:: rtems_interrupt_frame

``rtems_interrupt_frame``
  The data structure that defines the format of the interrupt stack frame as it
  appears to a user ISR.  This data structure may not be defined on all ports.

.. index:: rtems_interrupt_level

``rtems_interrupt_level``

  The data structure used with the ``rtems_interrupt_disable``,
  ``rtems_interrupt_enable``, and ``rtems_interrupt_flash`` routines.  This
  data type is CPU dependent and usually corresponds to the contents of the
  processor register containing the interrupt mask level.

.. index:: rtems_interval

``rtems_interval``
  The data type used to manage and manipulate time intervals.  Intervals are
  non-negative integers used to measure the length of time in clock ticks.

.. index:: rtems_isr

``rtems_isr``
  The return type of a function implementing an RTEMS ISR.

.. index:: rtems_isr_entry

``rtems_isr_entry``
  The address of the entry point to an RTEMS ISR.  It is equivalent to the
  entry point of the function implementing the ISR.

.. index:: rtems_mp_packet_classes

``rtems_mp_packet_classes``
  The enumerated type which specifies the categories of multiprocessing
  messages.  For example, one of the classes is for messages that must be
  processed by the Task Manager.

.. index:: rtems_mode

``rtems_mode``
  The data type used to manage and dynamically manipulate the execution mode of
  an RTEMS task.

.. index:: rtems_mpci_entry

``rtems_mpci_entry``
  The return type of an RTEMS MPCI routine.

.. index:: rtems_mpci_get_packet_entry

``rtems_mpci_get_packet_entry``
  The address of the entry point to the get packet routine for an MPCI
  implementation.

.. index:: rtems_mpci_initialization_entry

``rtems_mpci_initialization_entry``
  The address of the entry point to the initialization routine for an MPCI
  implementation.

.. index:: rtems_mpci_receive_packet_entry

``rtems_mpci_receive_packet_entry``
  The address of the entry point to the receive packet routine for an MPCI
  implementation.

.. index:: rtems_mpci_return_packet_entry

``rtems_mpci_return_packet_entry``
  The address of the entry point to the return packet routine for an MPCI
  implementation.

.. index:: rtems_mpci_send_packet_entry

``rtems_mpci_send_packet_entry``
  The address of the entry point to the send packet routine for an MPCI
  implementation.

.. index:: rtems_mpci_table

``rtems_mpci_table``
  The data structure containing the configuration information for an MPCI.

.. index:: rtems_name

``rtems_name``
  The data type used to contain the name of a Classic API object.  It is an
  unsigned thirty-two bit integer which can be treated as a numeric value or
  initialized using ``rtems_build_name`` to contain four ASCII characters.

.. index:: rtems_option

``rtems_option``
  The data type used to specify which behavioral options the caller desires.
  It is commonly used with potentially blocking directives to specify whether
  the caller is willing to block or return immediately with an error indicating
  that the resource was not available.

.. index:: rtems_packet_prefix

``rtems_packet_prefix``
  The data structure that defines the first bytes in every packet sent between
  nodes in an RTEMS multiprocessor system.  It contains routing information
  that is expected to be used by the MPCI layer.

.. index:: rtems_signal_set

``rtems_signal_set``
  The data type used to manage and manipulate RTEMS signal sets with the Signal
  Manager.

.. index:: int8_t

``int8_t``
  The C99 data type that corresponds to signed eight bit integers.  This data
  type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: int16_t

``int16_t``
  The C99 data type that corresponds to signed sixteen bit integers.  This data
  type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: int32_t

``int32_t``
  The C99 data type that corresponds to signed thirty-two bit integers.  This
  data type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: int64_t

``int64_t``
  The C99 data type that corresponds to signed sixty-four bit integers.  This
  data type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: rtems_single

``rtems_single``
  The RTEMS data type that corresponds to single precision floating point on
  the target hardware.  This type is deprecated. Use ``float`` instead.

.. index:: rtems_status_codes

``rtems_status_codes``
  The return type for most RTEMS services.  This is an enumerated type of
  approximately twenty-five values.  In general, when a service returns a
  particular status code, it indicates that a very specific error condition has
  occurred.

.. index:: rtems_task

``rtems_task``
  The return type for an RTEMS Task.

.. index:: rtems_task_argument

``rtems_task_argument``
  The data type for the argument passed to each RTEMS task. In RTEMS 4.7 and
  older, this is an unsigned thirty-two bit integer.  In RTEMS 4.8 and newer,
  this is based upon the C99 type ``uintptr_t`` which is guaranteed to be an
  integer large enough to hold a pointer on the target architecture.

.. index:: rtems_task_begin_extension

``rtems_task_begin_extension``
  The entry point for a task beginning execution user extension handler
  routine.

.. index:: rtems_task_create_extension

``rtems_task_create_extension``
  The entry point for a task creation execution user extension handler routine.

.. index:: rtems_task_delete_extension

``rtems_task_delete_extension``
  The entry point for a task deletion user extension handler routine.

.. index:: rtems_task_entry

``rtems_task_entry``
  The address of the entry point to an RTEMS ASR.  It is equivalent to the
  entry point of the function implementing the ASR.

.. index:: rtems_task_exitted_extension

``rtems_task_exitted_extension``
  The entry point for a task exitted user extension handler routine.

.. index:: rtems_task_priority

``rtems_task_priority``
  The data type used to manage and manipulate task priorities.

.. index:: rtems_task_restart_extension

``rtems_task_restart_extension``
  The entry point for a task restart user extension handler routine.

.. index:: rtems_task_start_extension

``rtems_task_start_extension``
  The entry point for a task start user extension handler routine.

.. index:: rtems_task_switch_extension

``rtems_task_switch_extension``
  The entry point for a task context switch user extension handler routine.

.. index:: rtems_tcb

``rtems_tcb``
  The data structure associated with each task in an RTEMS system.

.. index:: rtems_time_of_day

``rtems_time_of_day``
  The data structure used to manage and manipulate calendar time in RTEMS.

.. index:: rtems_timer_service_routine

``rtems_timer_service_routine``
  The return type for an RTEMS Timer Service Routine.

.. index:: rtems_timer_service_routine_entry

``rtems_timer_service_routine_entry``
  The address of the entry point to an RTEMS TSR.  It is equivalent to the
  entry point of the function implementing the TSR.

.. index:: rtems_vector_number

``rtems_vector_number``
  The data type used to manage and manipulate interrupt vector numbers.

.. index:: uint8_t

``uint8_t``
  The C99 data type that corresponds to unsigned eight bit integers.  This data
  type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: uint16_t

``uint16_t``
  The C99 data type that corresponds to unsigned sixteen bit integers.  This
  data type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: uint32_t

``uint32_t``
  The C99 data type that corresponds to unsigned thirty-two bit integers.  This
  data type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: uint64_t

``uint64_t``
  The C99 data type that corresponds to unsigned sixty-four bit integers.  This
  data type is defined by RTEMS in a manner that ensures it is portable across
  different target processors.

.. index:: uintptr_t

``uintptr_t``
  The C99 data type that corresponds to the unsigned integer type that is of
  sufficient size to represent addresses as unsigned integers.  This data type
  is defined by RTEMS in a manner that ensures it is portable across different
  target processors.
