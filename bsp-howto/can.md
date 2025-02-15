.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024 Michal Lenc <michallenc@seznam.cz>

CAN Driver
**********

RTEMS provides fully featured CAN/CAN FD stack. The API to the driver is
provided in the form of the POSIX character driver with each CAN controller
(chip) registered as node into "/dev" namespace by name (i.e. "can0", "can1",
... ). The stack utilizes FIFO queues (also called edges) organized into
oriented edges between controller side and application side. Edges,
responsible for message transfers from an application to controller and vice
versa, can have different priorities and function as priority classes. The
naming of the edges and functions using these edges is taken from the FIFO's
point of view. Therefore, outgoing edge is the edge that passes the frames
to the FIFO and incoming edge retrieves the frames from FIFO. Note that these
can be used both from application and device driver point of view as both
sides may use the same FIFO related functions.

Controller takes frames from FIFOs according their priority class and transmits
them to the network. Successfully sent frames are echoed through queues back
to open file instances except the sending one (that filtering is configurable).
Received frames a filtered to all queues to applications ends of the queues
which filter matches the CAN identifier and frame type.

The stack provides run time configuration options to create new queues with
desired priority, direction and filter, making it suitable for various
applications requirements. There is also a possibility to configure controller's
characteristics (bit rate, mode, chip specific ioctl calls).

The device can be opened in both blocking and nonblocking mode and one device
can be opened from multiple applications. Read and write operations wait
on binary semaphore indefinitely if blocking mode is used and frame can not be
passed to the framework immediately (full FIFO queue for example) or there
is no received message to process.

Include Headers
===============

To use the infrastructure, an application, BSP initiator or controller device
driver has to include few header files that provides related structures,
definitions and function declarations.

Application
-----------

.. code-block:: c

    #include <dev/can/can.h>

The only required include for standard application using the structure
through POSIX character device API is :c:type:`<dev/can/can.h>`. This
provides all defines, ioctl calls, and structures required to operate with
the infrastructure from application layer. These are in detail described
in RTEMS CAN API section.

The mentioned header also includes several other headers. These are still
strictly API interface, but separated to multiple headers for clearer
code organization. This contains the header defining CAN frame structure,
header introducing CAN bit timing structures, filters for FIFO queues
or CAN RX/TX statistics tracking. The application does not have to bother
include all of these headers as they are already included
through :c:type:`<dev/can/can.h>`.

BSP Registration
----------------

.. code-block:: c

    #include <dev/can/can-bus.h>
    #include <dev/can/controller-dependent.h>

It is expected the controller will be initialized and registered from board
support package during board initialization, but this includes will work
anywhere else (even from an application if required by the user). The header
:c:type:`<dev/can/can-bus.h>` provides definition of :c:type:`rtems_can_bus`
structure and declarations of :c:func:`rtems_can_bus_register()` that
registers the controller to standard /dev namespace. The usage of these
functions is described in Registering CAN Bus section.

The source code will most likely have to include a controller dependent
header that declares the initialization function for the specific controller.

Device Driver
-------------

.. code-block:: c

    #include <dev/can/can.h>
    #include <dev/can/can-devcommon.h>

The device driver (i.e. the file that implements the controller) has to
include :c:type:`<dev/can/can.h>` because of CAN frame definition and other
defines/structures with which it has to interact. Functions and structures
providing the interface with the infrastructure (obtaining frames from FIFO,
pushing frames to FIFO, slot abort and so on) are included through
:c:type:`<dev/can/can-devcommon.h>` header. The usage of these functions
is described in Driver Interface section.

It is expected :c:type:`<dev/can/can-devcommon.h>` will be used primarily
from a controller device driver (i.e. from RTEMS kernel code), but there
is a possibility to include this header even from an application if the
user has a special needs surpassing the API.

RTEMS CAN API
=============

.. code-block:: c

    #include <dev/can/can.h>

It is necessary to include the header above to operate with CAN infrastructure
through the described application interface.

Application Interface is provided with standard POSIX calls :c:func:`open()`,
:c:func:`write()`, :c:func:`read()`. :c:func:`close()` and :c:func:`ioctl()`.
Functions :c:func:`write()` and :c:func:`read()` are used with
:c:type:`can_frame` structure representing one CAN frame (message).

Opening Device and Configuration
--------------------------------

Device is registered as a node into "/dev" namespace and can be opened with
POSIX :c:func:`open()` call. A single chip can be opened multiple times
with each instance creating its own queues between the controller and
application. The frames received by the controller are filtered to all
connected queues if they match the filter set by the user. Therefore,
the applications do not race for the received frames.

CALLING SEQUENCE:
    .. code-block:: c

        int open( const char* pathname, int flags );

DESCRIPTION:
    Opens CAN device at path :c:type:`pathname` with mode defined in
    :c:type:`flags` argument. Modes are defined according to POSIX standard.

.. raw:: latex

    \clearpage

Both infrastructure resources and controller itself can be configured once
the device is opened. The configuration is provided via ioctl calls. Some
of these configuration are available only if the controller is stopped.

Managing Queues
~~~~~~~~~~~~~~~

One RX and one TX queue is created by default during :c:func:`open()`
operation. These queues have the lowest priority and default filter and
size settings. If needed, more queues can be created with
:c:type:`RTEMS_CAN_CREATE_QUEUE` call.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_CREATE_QUEUE, &queue );

DESCRIPTION:
    Creates new queue with characteristics defined in "queue" field provided
    as :c:type:`rtems_can_queue_param` structure.

    .. code-block:: c

      struct rtems_can_queue_param {
        uint8_t direction;
        uint8_t priority;
        uint8_t dlen_max;
        uint8_t buffer_size;
        struct rtems_can_filter filter;
      };

    Field :c:type:`dlen_max` set maximum CAN frame data length that can be
    sent through the queue. This allows the user to limit the size of allocated
    memory if only shorter frames are sent to the network. If set to zero,
    default value (64 bytes for CAN FD capable controllers, 8 bytes otherwise)
    is used. It is not possible to set an invalid value (less than zero or
    greater than 64). Field :c:type:`buffer_size` configures number of
    slots (frames) that fits in the FIFO.

    .. code-block:: c

      struct rtems_can_filter {
        uint32_t id;
        uint32_t id_mask;
        uint32_t flags;
        uint32_t flags_mask;
      };

    Structure :c:type:`rtems_can_filter` is used to set queue's filter. It
    holds the CAN frame identifier and flag filters, ensuring only frames
    matching this filter are passed to the queue's ends. Fields :c:type:`id`
    and :c:type:`flags` hold identifier bits and frames' flags, respectively,
    required to be present in a CAN frame to assign it to the corresponding
    FIFO queue. In other words, it specifies that only specific identifiers
    and/or flags shall be assigned to the queue. Members with :c:type:`_mask`
    postfix are used to mask out identifiers or flags that are forbidden for
    a given FIFO queue. Refer to CAN frame description for possible flags.

    The filter can be used to create queues that process only defined subset
    of CAN frames. This may be used to create priority classes based on
    frame identifier range or special queues for certain type of
    frames (echo, error etc.). Setting all fields of :c:type:`rtems_can_filter`
    to zero means all frames are passed through the queue.

    Default queues created during :c:func:`open()` operation allows all
    identifiers and filters out error and echo frames.

.. raw:: latex

    \clearpage

Queues can be removed (discarded) with :c:type:`RTEMS_CAN_DISCARD_QUEUES` command.
It is not possible to discard one specific queue, just all RX or/and all TX
queues for given opened instance (file descriptor) at once. Direction can be
defined by :c:type:`RTEMS_CAN_QUEUE_TX` and :c:type:`RTEMS_CAN_QUEUE_RX` defines.
Terms TX and RX are used from the application's point of view: TX meaning
queues transferring messages from an application to a controller, RX from a
controller to an application.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_DISCARD_QUEUES, type );

DESCRIPTION:
    Discard TX and/or RX queues based on integer "type" argument. Defines
    :c:type:`RTEMS_CAN_QUEUE_TX` and :c:type:`RTEMS_CAN_QUEUE_RX` can be used
    to specify queues for deletion.

.. raw:: latex

    \clearpage

Queues can also be flushed with :c:type:`RTEMS_CAN_FLUSH_QUEUES` command.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_FLUSH_QUEUES, type );

DESCRIPTION:
    Flushes TX and/or RX queues based on integer "type" argument. Defines
    :c:type:`RTEMS_CAN_QUEUE_TX` and :c:type:`RTEMS_CAN_QUEUE_RX` can be used
    to specify queues for deletion. The operation flushes all RX or/and all
    TX queues even if multiple queues are used.

.. raw:: latex

    \clearpage

Setting Bit Timing
~~~~~~~~~~~~~~~~~~

There are two ways to set CAN bit timing. Either the user can pass desired
bit rate value and let the infrastructure calculate bit timing, or precomputed
bit timing values can be passed directly. ioctl call :c:type:`RTEMS_CAN_SET_BITRATE`
is used for this purpose.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_SET_BITRATE, &set_bittiming );

DESCRIPTION:
    Sets bit timing based on "set_bittiming" parameter passed as a pointer to
    :c:type:`can_set_bittiming` structure.

    .. code-block:: c

        struct rtems_can_bittiming {
          uint32_t bitrate;
          uint32_t sample_point;
          uint32_t tq;
          uint32_t prop_seg;
          uint32_t phase_seg1;
          uint32_t phase_seg2;
          uint32_t sjw;
          uint32_t brp;
        };

        struct rtems_can_set_bittiming {
          uint16_t type;
          uint16_t from;
          struct rtems_can_bittiming bittiming;
        };

    Field :c:type:`type` determines the bit timing type to be set
    (:c:type:`CAN_BITTIME_TYPE_NOMINAL` or :c:type:`CAN_BITTIME_TYPE_DATA`),
    field :c:type:`from` determines the source of the bit timing values
    (:c:type:`CAN_BITTIME_FROM_BITRATE` or :c:type:`CAN_BITTIME_FROM_PRECOMPUTED`).

.. raw:: latex

    \clearpage

Actual bit timing values and controller's bit timing constants can
be retrieved with :c:type:`RTEMS_CAN_GET_BITTIMING`.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_GET_BITTIMING, &get_bittiming );

DESCRIPTION:
    Retrieves currently set bit timing values and controller's bit timing
    constants.

    .. code-block:: c

        struct rtems_can_bittiming_const {
          char name[32];
          uint32_t tseg1_min;
          uint32_t tseg1_max;
          uint32_t tseg2_min;
          uint32_t tseg2_max;
          uint32_t sjw_max;
          uint32_t brp_min;
          uint32_t brp_max;
          uint32_t brp_inc;
        };

        struct rtems_can_get_bittiming {
          uint16_t type;
          struct rtems_can_bittiming bittiming;
          struct rtems_can_bittiming_const bittiming_const;
        };

    Field :c:type:`type` determines bit timing to be set
    (:c:type:`CAN_BITTIME_TYPE_NOMINAL` or :c:type:`CAN_BITTIME_TYPE_DATA`).

.. raw:: latex

    \clearpage


Setting Mode
~~~~~~~~~~~~

Different modes of the chip can be enabled/disabled. ioctl call
:c:type:`RTEMS_CAN_CHIP_SET_MODE` is used to set the mode as a 32-bit large
unsigned integer mask.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_CHIP_SET_MODE, mode );

DESCRIPTION:
    Argument :c:type:`mode` is a 32-bit large unsigned integer with modes to
    be set. Available modes are

    * :c:type:`CAN_CTRLMODE_LOOPBACK`,

    * :c:type:`CAN_CTRLMODE_LISTENONLY`,

    * :c:type:`CAN_CTRLMODE_3_SAMPLES`,

    * :c:type:`CAN_CTRLMODE_ONE_SHOT`,

    * :c:type:`CAN_CTRLMODE_BERR_REPORTING`,

    * :c:type:`CAN_CTRLMODE_FD`,

    * :c:type:`CAN_CTRLMODE_PRESUME_ACK`,

    * :c:type:`CAN_CTRLMODE_FD_NON_ISO`,

    * :c:type:`CAN_CTRLMODE_CC_LEN8_DLC`,

    * :c:type:`CAN_CTRLMODE_TDC_AUTO`, and

    * :c:type:`CAN_CTRLMODE_TDC_MANUAL`.

    The modes are implemented to be compatible with GNU/Linux's SocketCAN
    stack and possibly with other operating systems as well. It is possible to
    set multiple modes during one ioctl call. The controller should be
    implemented in such a way that not setting particular mode in this ioctl
    call disables this mode. Therefore, the same ioctl call may be used for
    both enable and disable operation.

    Every controller should know its supported mode. An attempt to set a mode
    not supported by the controller leads to the ioctl call returning an error.
    It is also possible to change controller's modes only if the controller is
    stopped, otherwise error is returned.

Starting Chip
~~~~~~~~~~~~~

Opening the device does not automatically start the chip, this operation has
to be handled by specific ioctl call :c:type:`RTEMS_CAN_CHIP_START`.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_CHIP_START );

DESCRIPTION:
    Starts the chip (enables write/read). Repeated calls on already started
    chip do not have any effect.

It is also possible to start the chip with a function call
:c:func:`rtems_can_chip_start`. This way the controller may be started even
before the first open, for example from board support package right after
its initialization.

CALLING SEQUENCE:
    .. code-block:: c

       #include <dev/can/can-devcommon.h>

       int rtems_can_chip_start( struct rtems_can_chip *chip )

DESCRIPTION:
    Starts the chip (enables write/read). Repeated calls on already started
    chip do not have any effect.

Stopping Chip
~~~~~~~~~~~~~

Similarly to the chip start operation, chip stop is performed with
:c:type:`RTEMS_CAN_CHIP_STOP` ioctl call.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_CHIP_STOP, &timeout );

DESCRIPTION:
    Stops the chip (disables write/read). Repeated calls on already stopped
    chip do not have any effect. The call is nonblocking if :c:type:`timeout`
    parameter is set to :c:type:`NULL`, otherwise the calling thread is
    blocked for a timeout specified as a relative timeout with
    :c:type:`timespec` structure.

    This gives the controller the time to abort the frames already present
    in its buffers and to return these frames and the frames from FIFO
    queues back to the applications that opened it as TX error frames. This
    way the applications can get the information their frames were not
    transmitted because the controller was stopped. If timed out before
    all frames are returned as error frames, the queues are flushed and
    the frames are lost. In any way, it is ensured the queues are empty
    when/if the chip is started again. Therefore, the minimal implementation
    should always at least flush the FIFO queues from the application to the
    controller.

NOTES.
    It is important to check the number of users (applications) using the chip
    before turning it off as there can be more than one user per chip. The
    infrastructure allows turning off the controller even if there are other
    users using it. Read and write calls from other applications return error
    in that case.

Controller Related Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An ioctl call :c:type:`RTEMS_CAN_CHIP_GET_INFO` can be used to obtain some
information about the device driver (controller).

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_CHIP_GET_INFO, info_type );

DESCRIPTION:
    Obtains information about the chip. The information to be obtained is
    defined as integer argument info_type. Following parameters can be
    obtained.

    .. code-block:: c

        RTEMS_CAN_CHIP_BITRATE,
        RTEMS_CAN_CHIP_DBITRATE,
        RTEMS_CAN_CHIP_NUSERS,
        RTEMS_CAN_CHIP_FLAGS,
        RTEMS_CAN_CHIP_MODE, and
        RTEMS_CAN_CHIP_MODE_SUPPORTED.

    The defines listed above may be used to obtain information from the
    controller. It is possible to obtain only one information for one ioctl
    call. :c:type:`RTEMS_CAN_CHIP_MODE` and :c:type:`RTEMS_CAN_CHIP_MODE_SUPPORTED`
    are used to obtain currently set controller modes and all modes supported
    by the controller, respectively. Stop command described previously may
    benefit from :c:type:`RTEMS_CAN_CHIP_NUSERS` providing number of users
    currently using the controller. Controller's flags obtained by
    :c:type:`RTEMS_CAN_CHIP_FLAGS` provide various information including FD
    capability of the controller, status of the chip (configured, running),
    and so on. Refer to source code documentation for possible chip's status
    defines.

Controller Statistics
~~~~~~~~~~~~~~~~~~~~~

The controller can keep track of its statistics as number of received/transmitted
frames, number of received/transmitted bytes, number of errors and so on. These
statistics are represented in :c:type:`can_stats` structure and can be
obtained with :c:type:`RTEMS_CAN_CHIP_STATISTICS` ioctl call.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_CHIP_STATISTICS, &statistics );

DESCRIPTION:
    Obtains controller's statistics provided in with argument
    :c:type:`statistics` as a pointer to the :c:type:`rtems_can_stats`
    structure.

    .. code-block:: c

        enum can_state {
          CAN_STATE_ERROR_ACTIVE = 0,
          CAN_STATE_ERROR_WARNING,
          CAN_STATE_ERROR_PASSIVE,
          CAN_STATE_BUS_OFF,
          CAN_STATE_STOPPED,
          CAN_STATE_SLEEPING,
          CAN_STATE_STOPPING,
          CAN_STATE_MAX
        };

        struct rtems_can_stats {
          unsigned long tx_done;
          unsigned long rx_done;
          unsigned long tx_bytes;
          unsigned long rx_bytes;
          unsigned long tx_error;
          unsigned long rx_error;
          unsigned long rx_overflows;
          int chip_state;
        };

CAN Frame Representation
------------------------

The represenation of one CAN frame is defined statically with a header
separated in its own structure :c:type:`can_frame_header`. It has an 8
bytes long timestamp, 4 bytes long CAN identifier, 2 bytes long flag field
and 2 bytes long field with information about data length. Data field itself
is a 64 byte long array with byte access.

Only first 11 bits of the identifier are valid (29 if extended identifier
format is used). Having any of the upper three bits set to one indicates an
invalid CAN frame format. If these are set, the user should check frame's
flags to get information if this is not an error frame generated by the
controller.

.. code-block:: c

    struct can_frame_header {
      uint64_t timestamp;
      uint32_t can_id;
      uint16_t flags;
      uint16_t len;
    };

    struct can_frame {
        struct can_frame_header header;
        uint8_t data[CAN_FRAME_MAX_DLEN];
    };

Flags are used to distinguish frame formats (extended identifier, CAN FD
format, remote request and so on). Following defines can be used.

* :c:type:`CAN_FRAME_IDE`,

* :c:type:`CAN_FRAME_RTR`,

* :c:type:`CAN_FRAME_ECHO`,

* :c:type:`CAN_FRAME_LOCAL`,

* :c:type:`CAN_FRAME_TXERR`,

* :c:type:`CAN_FRAME_ERR`.

* :c:type:`CAN_FRAME_FIFO_OVERFLOW`.

* :c:type:`CAN_FRAME_FDF`,

* :c:type:`CAN_FRAME_BRS`, and

* :c:type:`CAN_FRAME_ESI`.

Extended frame format (:c:type:`CAN_FRAME_IDE`) is forced automatically if
identifier exceeds 11 bits. Flags :c:type:`CAN_FRAME_FDF` and
:c:type:`CAN_FRAME_BRS` (if bit rate switch between arbitration and data phase
is intended) should be set for CAN FD frame transmission.

Some of these flags are automatically masked for the first queues created
during the instance open operation. These include :c:type:`CAN_FRAME_ECHO`
and both error flags :c:type:`CAN_FRAME_TXERR` and :c:type:`CAN_FRAME_ERR`.
Flag :c:type:`CAN_FRAME_FIFO_OVERFLOW` is set automatically by the stack for
RX frames and can not be filtered out. It indicates FIFO overflow occurred,
and some frames on the receiver side have been discarded. More specifically,
it informs the user there are discarded frames between the frame with
:c:type:`CAN_FRAME_FIFO_OVERFLOW` flag and a previous correctly received
frame.

Frame Transmission
------------------

Frame is transmitted to the CAN framework by calling :c:func:`write()`
function.

CALLING SEQUENCE:
    .. code-block:: c

        ssize_t write( int fd, struct can_frame *frame, size_t count );

DESCRIPTION:
    Passes CAN frame represented by :c:type:`can_frame` structure to the
    network. Return values comply with POSIX standard. Write size :c:type:`count`
    can be calculated with :c:func:`can_framesize()` function. It is possible
    to write just one frame with a single call. Passing incorrect frame length
    (less than the header size or larger than maximum CAN frame size) results
    in write error.

.. raw:: latex

    \clearpage

User can check whether the messages were transferred from RTEMS framework
to the physical network by calling ioctl :c:type:`RTEMS_CAN_WAIT_TX_DONE`.

CALLING SEQUENCE:
    .. code-block:: c

        ssize_t ioctl( fd, RTEMS_CAN_WAIT_TX_DONE, &timeout );

DESCRIPTION:
    Waits with timeout until all frames are transferred to the network. The
    timeout is defined as a pointer to :c:type:`timespec` structure. The
    timeout is specified as a relative timeout. Returns 0 on success
    and :c:type:`ETIME` on timeout.

    This call applies to TX FIFO queues at once for a given file descriptor.

.. raw:: latex

    \clearpage

Polling in nonblocking mode can be done with :c:type:`RTEMS_CAN_POLL_TX_READY`
ioctl call.

CALLING SEQUENCE:
    .. code-block:: c

       ssize_t ioctl( fd, RTEMS_CAN_POLL_TX_READY, &timeout );

DESCRIPTION:
  Implements polling function on outgoing edges. Timeout is defined with
  :c:type:`timespec` structure. The timeout is specified as a relative
  timeout. It waits until there is an available frame in any of the input
  FIFOs or until timeout.

.. raw:: latex

    \clearpage

Frame Reception
---------------

Frame is received from the CAN framework by calling :c:func:`read()`
function.

CALLING SEQUENCE:
    .. code-block:: c

        ssize_t read( int fd, struct can_frame *frame, size_t count );

DESCRIPTION:
    Reads CAN frame represented by :c:type:`can_frame` from the network.
    Return values comply with POSIX standard. The call returns error if
    read size specified by :c:type:`count` is less than the length
    of the frame header. It is possible to read only a single frame with one
    read call.

.. raw:: latex

    \clearpage

Polling in nonblocking mode can be done with :c:type:`RTEMS_CAN_POLL_RX_AVAIL`
ioctl call.

CALLING SEQUENCE:
    .. code-block:: c

        ssize_t ioctl( fd, RTEMS_CAN_POLL_RX_AVAIL, &timeout );

DESCRIPTION:
  Implements polling function on incoming edges. Timeout is defined with
  :c:type:`timespec` structure. It waits until there is an available
  frame in any of the input FIFOs or until timeout.

.. raw:: latex

    \clearpage

Error Reporting
---------------

There are two flags for error reporting: :c:type:`CAN_FRAME_TXERR`
and :c:type:`CAN_FRAME_ERR`. First flag is used to report frame transmission
error. In this case, the controller should send the frame that caused the
error back to its opened instance with added :c:type:`CAN_FRAME_TXERR` flag.
The message should not be changed in any other way.

It is possible to receive various CAN bus related error through error messages
sent from the controller to the application. Flag :c:type:`CAN_FRAME_ERR`
is used for that. If this flag is set, received frame has a special format
and shall be looked up as an error frame.

For generated error frame, identifier field is used to store the information
about error type. Following types are supported.

* :c:type:`CAN_ERR_ID_TXTIMEOUT`,

* :c:type:`CAN_ERR_ID_LOSTARB`,

* :c:type:`CAN_ERR_ID_CRTL`,

* :c:type:`CAN_ERR_ID_PROT`,

* :c:type:`CAN_ERR_ID_TRX`,

* :c:type:`CAN_ERR_ID_ACK`.

* :c:type:`CAN_ERR_ID_BUSOFF`.

* :c:type:`CAN_ERR_ID_BUSERROR`,

* :c:type:`CAN_ERR_ID_RESTARTED`,

* :c:type:`CAN_ERR_ID_CNT`, and

* :c:type:`CAN_ERR_ID_INTERNAL`.

Additionally, 31st bit of CAN identifier is set to logical one. This is another
check that indicates it is not a regular frame but error one. Having error
types located in CAN frame identifier brings the possibility to create new
RX queues with identifier mask set in such way that only some of these errors
are propagated to the application.

The additional information providing deeper description of raised error are
also available in data fields for some error types. Only a standard frame with
8 bytes long data field is used.

The first byte (8 bits) of the data field keeps the detailed information
regarding lost arbitration error (:c:type:`CAN_ERR_ID_LOSTARB`). This basically just
informs in that bit the arbitration was lost. Another field stores controller
related problems (:c:type:`CAN_ERR_ID_CRTL`). This includes RX or TX overflows
and the controller changing its error state (error active, warning, passive).

Protocol related violations (:c:type:`CAN_ERR_ID_PROT`) are stored in the third
and the fourth data field. The first informs what kind of violation is
present. This may be incorrect bit stuffing, controller incapability to
generate dominant or recessive bit or bus overload for example. The latter
field provides a location of this violation.

Transceiver status (:c:type:`CAN_ERR_ID_TRX`) is located in the fifth data field.
This is used to report hardware layer issues as missing wire or wire being
short-circuited to ground or supply voltage. The sixth data field is reserved and
not used. The infrastructure also reports number of the current values of TX
and RX error counter (:c:type:`CAN_ERR_ID_CNT`). These data are passed through
seventh and eight data fields for transmission and reception, respectively.

Driver Interface
================

.. code-block:: c

    #include <dev/can/can.h>
    #include <dev/can/can-devcommon.h>

The includes listed above are required to use the functions described in this
section.

The infrastructure provides several functions ensuring an interface between
FIFO queue side of the stack and the controller's specific implementation.
Controller's driver should use these functions to access the FIFOs.

The driver is forbidden to access the CAN framework from an interrupt
handler. Instead, it should utilize a worker thread waiting on a semaphore
and triggered when there are interrupts to be processed (received frame, send
done, error and so on) or where there are frames to be transmitted (this
information is triggered from the CAN framework, see the next section for
the detailed description).

For examples of CAN controller's driver see:

* `CAN virtual driver <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/dev/can/can-virtual.c>`_
* `CTU CAN FD driver <https://gitlab.rtems.org/rtems/rtos/rtems/-/blob/main/cpukit/dev/can/ctucanfd/ctucanfd.c>`_

Chip Initialization
-------------------

The chip initialization function should allocate a :c:type:`rtems_can_chip`
structure. This structure holds the controller's ends of FIFO queues as well
as the chip's private structure. This structure is chip specific, and it is
used to store the chip specific data. The controller has to allocate and
initialize its side of the FIFO queues. The structure to be allocated is
:c:type:`rtems_can_queue_ends_dev` located on a :c:type:`qends_dev` field
of :c:type:`rtems_can_chip` structure and initialization is done with a
:c:func:`rtems_can_queue_ends_init_chip()` function call.

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_queue_ends_init_chip (
          struct rtems_can_chip *chip,
          const char *name
        );

DESCRIPTION:
    Initializes controller's side of ends defined in :c:type:`chip` structure
    and connects them to the FIFO queues. It also creates a worker binary
    semaphore :c:type:`worker_sem` named :c:type:`name` and used by the
    framework to inform the controller's side about new frame to be
    transmitted. The controller may also use this semaphore to trigger its
    worker thread in case of an interrupt (received frame for example).

Driver should also register several functions used by ioctl calls (start chip,
stop chip, set bit rate for example). These functions are assigned through
:c:type:`rtems_can_chip_ops` structure.

Frame Transmission
------------------

The controller retrieves the slots (frames) from FIFO queues (edges) and
sends them to the network. The naming of the functions utilizes :c:type:`_outslot`
suffix, because the controller's side takes the frames from the FIFO's outputs.

The framework informs the driver about the new message to be transmitted by
posting a :c:type:`worker_sem` semaphore. The driver then may call the function
:c:func:`rtems_can_queue_test_outslot()` to obtain the oldest (least recently
added to the FIFO from an application) slot from the highest priority queue.
Note that this uses the priority of the queues as described in the previous
sections, not the priority of a CAN frame (i.e. the frame's identifier value).
However, these queues may have the filter set up in such a way to accept
only a certain identifier range.

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_queue_test_outslot(
          struct rtems_can_queue_ends *qends,
          struct rtems_can_queue_edge **qedgep,
          struct rtems_can_queue_slot **slotp
        );

DESCRIPTION:
    Tests and retrieves the oldest ready slot from the highest priority active
    queue (priority class).

The slot can subsequently be put into the controller's hardware buffer and sent
to the network. Function :c:func:`rtems_can_queue_test_outslot()` does not
free the slot's space in the FIFO queue. The controller should inform the
framework to free the space by calling the :c:func:`rtems_can_queue_free_outslot()`
function once the frame is successfully transmitted or the transmission results
in an error.

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_queue_free_outslot(
          struct rtems_can_queue_ends *qends,
          struct rtems_can_queue_edge *qedge,
          struct rtems_can_queue_slot *slot
        );

DESCRIPTION:
    Releases processed slot previously acquired by a function
    :c:func:`rtems_can_queue_test_outslot()` call.

The framework also provides a unique feature to push the frames back to the
correct FIFO and schedule the slot later processing. This is useful in case
the frame put into a hardware buffer is aborted. The abort might be used when
some later scheduled low-priority frame occupies the hardware TX buffer, which
is urgently demanded for a higher priority pending message from other FIFO for
example.

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_queue_push_back_outslot(
          struct rtems_can_queue_ends *qends,
          struct rtems_can_queue_edge *qedge,
          struct rtems_can_queue_slot *slot
        );

DESCRIPTION:
    Reschedules slot previously acquired with a :c:func:`rtems_can_queue_test_outslot()`
    function call for a second time processing.

Previously described function :c:func:`rtems_can_queue_test_outslot()` already
takes the slot from the FIFO when called. This is not convenient in case there
is no free space in the controller's hardware TX buffers. We would rather just
check whether there is some pending message from higher priority class
compared to the priority classes presented in buffers. This can be done
with :c:func:`rtems_can_queue_pending_outslot_prio()`.

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_queue_pending_outslot_prio(
          struct rtems_can_queue_ends *qends,
          int prio_min
        );

DESCRIPTION:
    Tests whether there is ready slot for given ends and minimum priority
    to be considered. Negative value informs this is not a case, positive
    value informs about the available slot priority class.

Frame Reception
---------------

Upon successful frame reception, the controller has to pass the frame
to FIFO edges. This is done with :c:func:`rtems_can_queue_filter_frame_to_edges()`

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_queue_filter_frame_to_edges(
          struct rtems_can_queue_ends *qends,
          struct rtems_can_queue_edge *src_edge,
          struct can_frame *frame,
          unsigned int flags2add
        );

DESCRIPTION:
    Sends a message (frame) defined with :c:type:`frame` argument to all
    outgoing edges connected to the given ends (:c:type:`qends`) with
    additional flags defined by :c:type:`flags2add` argument. Argument
    :c:type:`src_edge` defines an optional source edge for echo detection.
    This is used to correctly filter echo frames.

The controller also should use this function to send an echo frame with
additional flag :c:type:`CAN_FRAME_LOCAL` upon a successful frame transmission
or :c:type:`CAN_FRAME_TXERR` frame when transmission error occurs.

Worker Thread Example
---------------------

This is a largely simplified example of a possible worker thread for CAN
device driver. The thread is used both for interrupt processing (semaphore
trigger by the interrupt handler) and frame sender. The interrupt handler
should disable interrupts before posting the semaphore as all interrupts are
handled in the worker. The worker should enable them before waiting on the
semaphore.

.. code-block:: c

    static rtems_task worker( rtems_task_argument arg )
    {
      struct rtems_can_chip *chip = (struct rtems_can_chip *)arg;
      struct rtems_can_queue_ends *qends = &chip->qends_dev->base;

      while ( 1 ) {
        /* This should be another while loop that handles all interrupts */
        process_interrupts( chip );

        if ( buffer_has_free_space() ) {
          ret = rtems_can_queue_test_outslot( qends, &qedge, &slot );
          if ( ret >= 0 ) {
            /* Send frame located in slot->frame */
          }
        } else {
          /* Check for the possible higher priority frames with
           * rtems_can_queue_pending_outslot_prio() call.
           * This has sense only if the controller supports frame
           * abort from HW buffers.
           */
        }

        /* Enable interrupts and wait on semaphore */
        interrupts_enable( chip );
        rtems_binary_semaphore_wait( &chip->qends_dev->worker_sem );
      }
    }

Registering CAN Bus
===================

.. code-block:: c

    #include <dev/can/can-bus.h>
    #include <dev/can/controller-dependent.h>

The headers listed above have to be used ti provide the described functions.
Header :c:type:`<dev/can/controller-dependent.h>` represents the controller's
specific header. This header usually declares the controller's initialization
function.

Once initialized (:c:type:`rtems_can_chip` structure allocated and obtained
from a controller specific function), the device can be registered into
/dev namespace by :c:func:`rtems_can_bus_register()` function.

CALLING SEQUENCE:
    .. code-block:: c

        int rtems_can_bus_register(
          struct rtems_can_bus *bus,
          const char *bus_path
        );

DESCRIPTION:
    Registers CAN devices in structure :c:type:`rtems_can_bus` to /dev
    namespace with path :c:type:`bus_path`. The path may follow the standard
    /dev/canX naming, or it can be a different name selected by the user/BSP.
    Structure :c:type:`rtems_can_bus` represents one CAN device and is
    defined as:

    .. code-block:: c

        struct rtems_can_bus {
            struct rtems_can_chip *chip;
        };

    The device can be opened by :c:func:`open()` function once registered
    into /dev namespace. It is possible to open one device multiple times.

Example
-------

The entire process of initialization and registration is demonstrated on virtual
CAN controller in the code below. Note that the user has to specify the path
to which the controller is registered, and this path has to be unique. Chip
specific function :c:func:`xxx_initialize()` may also have different input
parameters for different chips or can even have a different name according to
the chip's specific implementation.

.. code-block:: c

    #include <dev/can/can-bus.h>
    #include <dev/can/can-virtual.h>

    /* Allocate can_bus structure */
    struct rtems_can_bus bus = malloc( sizeof( struct rtems_can_bus ) );

    /* Initialize virtual CAN controller */
    bus->chip = rtems_virtual_initialize();

    /* Register controller as dev/can0, returns 0 on success */
    int ret = rtems_can_bus_register( bus, "dev/can0" );
