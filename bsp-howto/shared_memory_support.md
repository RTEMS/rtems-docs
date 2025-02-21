.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 1988, 2009 On-Line Applications Research Corporation (OAR)

Shared Memory Support Driver
****************************

The Shared Memory Support Driver is responsible for providing glue routines and
configuration information required by the Shared Memory Multiprocessor
Communications Interface (MPCI).  The Shared Memory Support Driver tailors the
portable Shared Memory Driver to a particular target platform.

This driver is only required in shared memory multiprocessing systems that use
the RTEMS mulitprocessing support.  For more information on RTEMS
multiprocessing capabilities and the MPCI, refer to the *Multiprocessing
Manager* chapter of the *RTEMS Application C User's Guide*.

Shared Memory Configuration Table
=================================

The Shared Memory Configuration Table is defined in the following structure:

.. code-block:: c

    typedef volatile uint32_t vol_u32;

    typedef struct {
      vol_u32 *address;        /* write here for interrupt    */
      vol_u32  value;          /* this value causes interrupt */
      vol_u32  length;         /* for this length (0,1,2,4)   */
    } Shm_Interrupt_information;

    struct shm_config_info {
      vol_u32           *base;                     /* base address of SHM         */
      vol_u32            length;                   /* length (in bytes) of SHM    */
      vol_u32            format;                   /* SHM is big or little endian */
      vol_u32          (*convert)();               /* neutral conversion routine  */
      vol_u32            poll_intr;                /* POLLED or INTR driven mode  */
      void             (*cause_intr)( uint32_t );
      Shm_Interrupt_information Intr;              /* cause intr information      */
    };

    typedef struct shm_config_info shm_config_table;

where the fields are defined as follows:

``base``
    is the base address of the shared memory buffer used to pass messages
    between the nodes in the system.

``length``
    is the length (in bytes) of the shared memory buffer used to pass messages
    between the nodes in the system.

``format``
    is either ``SHM_BIG`` or ``SHM_LITTLE`` to indicate that the neutral format
    of the shared memory area is big or little endian.  The format of the
    memory should be chosen to match most of the inter-node traffic.

``convert``
    is the address of a routine which converts from native format to neutral
    format.  Ideally, the neutral format is the same as the native format so
    this routine is quite simple.

``poll_intr``, ``cause_intr``
    is either ``INTR_MODE`` or ``POLLED_MODE`` to indicate how the node will be
    informed of incoming messages.

``Intr``
    is the information required to cause an interrupt on a node.  This
    structure contains the following fields:

    ``address``
        is the address to write at to cause an interrupt on that node.  For a
        polled node, this should be NULL.

    ``value``
        is the value to write to cause an interrupt.

    ``length``
        is the length of the entity to write on the node to cause an interrupt.
        This can be 0 to indicate polled operation, 1 to write a byte, 2 to
        write a sixteen-bit entity, and 4 to write a thirty-two bit entity.

Primitives
==========

Convert Address
---------------

The ``Shm_Convert_address`` is responsible for converting an address of an
entity in the shared memory area into the address that should be used from this
node.  Most targets will simply return the address passed to this routine.
However, some target boards will have a special window onto the shared memory.
For example, some VMEbus boards have special address windows to access
addresses that are normally reserved in the CPU's address space.

.. code-block:: c

    void *Shm_Convert_address( void *address )
    {
      return the local address version of this bus address
    }

Get Configuration
-----------------

The ``Shm_Get_configuration`` routine is responsible for filling in the Shared
Memory Configuration Table passed to it.

.. code-block:: c

    void Shm_Get_configuration(
      uint32_t           localnode,
      shm_config_table **shmcfg
    )
    {
      fill in the Shared Memory Configuration Table
    }

Locking Primitives
------------------

This is a collection of routines that are invoked by the portable part of the
Shared Memory Driver to manage locks in the shared memory buffer area.
Accesses to the shared memory must be atomic.  Two nodes in a multiprocessor
system must not be manipulating the shared data structures simultaneously.  The
locking primitives are used to insure this.

To avoid deadlock, local processor interrupts should be disabled the entire
time the locked queue is locked.

The locking primitives operate on the lock ``field`` of the
``Shm_Locked_queue_Control`` data structure.  This structure is defined as
follows:

.. code-block:: c

    typedef struct {
      vol_u32 lock;  /* lock field for this queue    */
      vol_u32 front; /* first envelope on queue      */
      vol_u32 rear;  /* last envelope on queue       */
      vol_u32 owner; /* receiving (i.e. owning) node */
    } Shm_Locked_queue_Control;

where each field is defined as follows:

``lock``
    is the lock field.  Every node in the system must agree on how this field
    will be used.  Many processor families provide an atomic "test and set"
    instruction that is used to manage this field.

``front``
    is the index of the first message on this locked queue.

``rear``
    is the index of the last message on this locked queue.

``owner``
    is the node number of the node that currently has this structure locked.

Initializing a Shared Lock
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Shm_Initialize_lock`` routine is responsible for initializing the lock
field.  This routines usually is implemented as follows:

.. code-block:: c

    void Shm_Initialize_lock(
      Shm_Locked_queue_Control *lq_cb
    )
    {
      lq_cb->lock = LQ_UNLOCKED;
    }

Acquiring a Shared Lock
~~~~~~~~~~~~~~~~~~~~~~~

The ``Shm_Lock`` routine is responsible for acquiring the lock field.
Interrupts should be disabled while that lock is acquired.  If the lock is
currently unavailble, then the locking routine should delay a few microseconds
to allow the other node to release the lock.  Doing this reduces bus contention
for the lock.  This routines usually is implemented as follows:

.. code-block:: c

    void Shm_Lock(
      Shm_Locked_queue_Control *lq_cb
    )
    {
      disable processor interrupts
        set Shm_isrstat to previous interrupt disable level

      while ( TRUE ) {
        atomically attempt to acquire the lock
        if the lock was acquired
          return
        delay some small period of time
      }
    }

Releasing a Shared Lock
~~~~~~~~~~~~~~~~~~~~~~~

The ``Shm_Unlock`` routine is responsible for releasing the lock field and
reenabling processor interrupts.  This routines usually is implemented as
follows:

.. code-block:: c

    void Shm_Unlock(
      Shm_Locked_queue_Control *lq_cb
    )
    {
      set the lock to the unlocked value
      reenable processor interrupts to their level prior
        to the lock being acquired.  This value was saved
        in the global variable Shm_isrstat
    }

Installing the MPCI ISR
=======================

The ``Shm_setvec`` is invoked by the portable portion of the shared memory to
install the interrupt service routine that is invoked when an incoming message
is announced.  Some target boards support an interprocessor interrupt or
mailbox scheme and this is where the ISR for that interrupt would be installed.

On an interrupt driven node, this routine would be implemented
as follows:

.. code-block:: c

    void Shm_setvec( void )
    {
      install the interprocessor communications ISR
    }

On a polled node, this routine would be empty.
