.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2011,2015 Aeroflex Gaisler AB

.. index:: PCI
.. index:: libpci

PCI Library
***********

Introduction
============

The Peripheral Component Interconnect (PCI) bus is a very common computer bus
architecture that is found in almost every PC today. The PCI bus is normally
located at the motherboard where some PCI devices are soldered directly onto
the PCB and expansion slots allows the user to add custom devices easily. There
is a wide range of PCI hardware available implementing all sorts of interfaces
and functions.

This section describes the PCI Library available in RTEMS used to access the
PCI bus in a portable way across computer architectures supported by RTEMS.

The PCI Library aims to be compatible with PCI 2.3 with a couple of
limitations, for example there is no support for hot-plugging, 64-bit memory
space and cardbus bridges.

In order to support different architectures and with small foot-print embedded
systems in mind the PCI Library offers four different configuration options
listed below. It is selected during compile time by defining the appropriate
macros in confdefs.h. It is also possible to enable PCI_LIB_NONE (No
Configuration) which can be used for debuging PCI access functions.

- Auto Configuration (Plug & Play)

- Read Configuration (read BIOS or boot loader configuration)

- Static Configuration (write user defined configuration)

- Peripheral Configuration (no access to cfg-space)

Background
==========

The PCI bus is constructed in a way where on-board devices and devices in
expansion slots can be automatically found (probed) and configured using Plug &
Play completely implemented in software. The bus is set up once during boot
up. The Plug & Play information can be read and written from PCI configuration
space. A PCI device is identified in configuration space by a unique bus, slot
and function number. Each PCI slot can have up to 8 functions and interface to
another PCI sub-bus by implementing a PCI-to-PCI bridge according to the PCI
Bridge Architecture specification.

Using the unique \[bus:slot:func] any device can be configured regardless of
how PCI is currently set up as long as all PCI buses are enumerated
correctly. The enumeration is done during probing, all bridges are given a bus
number in order for the bridges to respond to accesses from both
directions. The PCI library can assign address ranges to which a PCI device
should respond using Plug & Play technique or a static user defined
configuration. After the configuration has been performed the PCI device
drivers can find devices by the read-only PCI Class type, Vendor ID and Device
ID information found in configuration space for each device.

In some systems there is a boot loader or BIOS which have already configured
all PCI devices, but on embedded targets it is quite common that there is no
BIOS or boot loader, thus RTEMS must configure the PCI bus. Only the PCI host
may do configuration space access, the host driver or BSP is responsible to
translate the \[bus:slot:func] into a valid PCI configuration space access.

If the target is not a host, but a peripheral, configuration space can not be
accessed, the peripheral is set up by the host during start up. In complex
embedded PCI systems the peripheral may need to access other PCI boards than
the host. In such systems a custom (static) configuration of both the host and
peripheral may be a convenient solution.

The PCI bus defines four interrupt signals INTA#..INTD#. The interrupt signals
must be mapped into a system interrupt/vector, it is up to the BSP or host
driver to know the mapping, however the BIOS or boot loader may use the 8-bit
read/write "Interrupt Line" register to pass the knowledge along to the OS.

The PCI standard defines and recommends that the backplane route the interupt
lines in a systematic way, however in standard there is no such requirement.
The PCI Auto Configuration Library implements the recommended way of routing
which is very common but it is also supported to some extent to override the
interrupt routing from the BSP or Host Bridge driver using the configuration
structure.

Software Components
-------------------

The PCI library is located in cpukit/libpci, it consists of different parts:

- PCI Host bridge driver interface

- Configuration routines

- Access (Configuration, I/O and Memory space) routines

- Interrupt routines (implemented by BSP)

- Print routines

- Static/peripheral configuration creation

- PCI shell command

PCI Configuration
-----------------

During start up the PCI bus must be configured in order for host and
peripherals to access one another using Memory or I/O accesses and that
interrupts are properly handled. Three different spaces are defined and mapped
separately:

#. I/O space (IO)

#. non-prefetchable Memory space (MEMIO)

#. prefetchable Memory space (MEM)

Regions of the same type (I/O or Memory) may not overlap which is guaranteed by
the software. MEM regions may be mapped into MEMIO regions, but MEMIO regions
can not be mapped into MEM, for that could lead to prefetching of
registers. The interrupt pin which a board is driving can be read out from PCI
configuration space, however it is up to software to know how interrupt signals
are routed between PCI-to-PCI bridges and how PCI INT[A..D]# pins are mapped to
system IRQ. In systems where previous software (boot loader or BIOS) has
already set up this the configuration is overwritten or simply read out.

In order to support different configuration methods the following configuration
libraries are selectable by the user:

- Auto Configuration (run Plug & Play software)

- Read Configuration (relies on a boot loader or BIOS)

- Static Configuration (write user defined setup, no Plug & Play)

- Peripheral Configuration (user defined setup, no access to
  configuration space)

A host driver can be made to support all three configuration methods, or any
combination. It may be defined by the BSP which approach is used.

The configuration software is called from the PCI driver
(``pci_config_init()``).

Regardless of configuration method a PCI device tree is created in RAM during
initialization, the tree can be accessed to find devices and resources without
accessing configuration space later on. The user is responsible to create the
device tree at compile time when using the static/peripheral method.

RTEMS Configuration selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The active configuration method can be selected at compile time in the same way
as other project parameters by including rtems/confdefs.h and setting

- ``CONFIGURE_INIT``

- ``RTEMS_PCI_CONFIG_LIB``

- ``CONFIGURE_PCI_LIB`` = PCI_LIB_(AUTO,STATIC,READ,PERIPHERAL)

See the RTEMS configuration section how to setup the PCI library.

Auto Configuration
~~~~~~~~~~~~~~~~~~

The auto configuration software enumerates PCI buses and initializes all PCI
devices found using Plug & Play. The auto configuration software requires that
a configuration setup has been registered by the driver or BSP in order to
setup the I/O and Memory regions at the correct address ranges. PCI interrupt
pins can optionally be routed over PCI-to-PCI bridges and mapped to a system
interrupt number. BAR resources are sorted by size and required alignment,
unused "dead" space may be created when PCI bridges are present due to the PCI
bridge window size does not equal the alignment. To cope with that resources
are reordered to fit smaller BARs into the dead space to minimize the PCI space
required. If a BAR or ROM register can not be allocated a PCI address region
(due to too few resources available) the register will be given the value of
pci_invalid_address which defaults to 0.

The auto configuration routines support:

- PCI 2.3

- Little and big endian PCI bus

- one I/O 16 or 32-bit range (IO)

- memory space (MEMIO)

- prefetchable memory space (MEM), if not present MEM will be mapped into MEMIO

- multiple PCI buses - PCI-to-PCI bridges

- standard BARs, PCI-to-PCI bridge BARs, ROM BARs

- Interrupt routing over bridges

- Interrupt pin to system interrupt mapping

Not supported:

- hot-pluggable devices

- Cardbus bridges

- 64-bit memory space

- 16-bit and 32-bit I/O address ranges at the same time

In PCI 2.3 there may exist I/O BARs that must be located at the low 64kBytes
address range, in order to support this the host driver or BSP must make sure
that I/O addresses region is within this region.

Read Configuration
~~~~~~~~~~~~~~~~~~

When a BIOS or boot loader already has setup the PCI bus the configuration can
be read directly from the PCI resource registers and buses are already
enumerated, this is a much simpler approach than configuring PCI ourselves. The
PCI device tree is automatically created based on the current configuration and
devices present. After initialization is done there is no difference between
the auto or read configuration approaches.

Static Configuration
~~~~~~~~~~~~~~~~~~~~

To support custom configurations and small-footprint PCI systems, the user may
provide the PCI device tree which contains the current configuration. The PCI
buses are enumerated and all resources are written to PCI devices during
initialization. When this approach is selected PCI boards must be located at
the same slots every time and devices can not be removed or added, Plug & Play
is not performed. Boards of the same type may of course be exchanged.

The user can create a configuration by calling pci_cfg_print() on a running
system that has had PCI setup by the auto or read configuration routines, it
can be called from the PCI shell command. The user must provide the PCI device
tree named pci_hb.

Peripheral Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

On systems where a peripheral PCI device needs to access other PCI devices than
the host the peripheral configuration approach may be handy. Most PCI devices
answers on the PCI host's requests and start DMA accesses into the Hosts
memory, however in some complex systems PCI devices may want to access other
devices on the same bus or at another PCI bus.

A PCI peripheral is not allowed to do PCI configuration cycles, which means
that it must either rely on the host to give it the addresses it needs, or that
the addresses are predefined.

This configuration approach is very similar to the static option, however the
configuration is never written to PCI bus, instead it is only used for drivers
to find PCI devices and resources using the same PCI API as for the host

PCI Access
----------

The PCI access routines are low-level routines provided for drivers,
configuration software, etc. in order to access different regions in a way not
dependent upon the host driver, BSP or platform.

- PCI configuration space

- PCI I/O space

- Registers over PCI memory space

- Translate PCI address into CPU accessible address and vice versa

By using the access routines drivers can be made portable over different
architectures. The access routines take the architecture endianness into
consideration and let the host driver or BSP implement I/O space and
configuration space access.

Some non-standard hardware may also define the PCI bus big-endian, for example
the LEON2 AT697 PCI host bridge and some LEON3 systems may be configured that
way. It is up to the BSP to set the appropriate PCI endianness on compile time
(``BSP_PCI_BIG_ENDIAN``) in order for inline macros to be correctly defined.
Another possibility is to use the function pointers defined by the access layer
to implement drivers that support "run-time endianness detection".

Configuration space
~~~~~~~~~~~~~~~~~~~

Configuration space is accessed using the routines listed below. The pci_dev_t
type is used to specify a specific PCI bus, device and function. It is up to
the host driver or BSP to create a valid access to the requested PCI
slot. Requests made to slots that are not supported by hardware should result
in ``PCISTS_MSTABRT`` and/or data must be ignored (writes) or ``0xFFFFFFFF`` is
always returned (reads).

.. code-block:: c

    /* Configuration Space Access Read Routines */
    extern int pci_cfg_r8(pci_dev_t dev, int ofs, uint8_t *data);
    extern int pci_cfg_r16(pci_dev_t dev, int ofs, uint16_t *data);
    extern int pci_cfg_r32(pci_dev_t dev, int ofs, uint32_t *data);

    /* Configuration Space Access Write Routines */
    extern int pci_cfg_w8(pci_dev_t dev, int ofs, uint8_t data);
    extern int pci_cfg_w16(pci_dev_t dev, int ofs, uint16_t data);
    extern int pci_cfg_w32(pci_dev_t dev, int ofs, uint32_t data);

I/O space
~~~~~~~~~

The BSP or driver provide special routines in order to access I/O space. Some
architectures have a special instruction accessing I/O space, others have it
mapped into a "PCI I/O window" in the standard address space accessed by the
CPU. The window size may vary and must be taken into consideration by the host
driver. The below routines must be used to access I/O space. The address given
to the functions is not the PCI I/O addresses, the caller must have translated
PCI I/O addresses (available in the PCI BARs) into a BSP or host driver custom
address, see `Access functions`_ for how addresses are translated.

.. code-block:: c

    /* Read a register over PCI I/O Space */
    extern uint8_t pci_io_r8(uint32_t adr);
    extern uint16_t pci_io_r16(uint32_t adr);
    extern uint32_t pci_io_r32(uint32_t adr);

    /* Write a register over PCI I/O Space */
    extern void pci_io_w8(uint32_t adr, uint8_t data);
    extern void pci_io_w16(uint32_t adr, uint16_t data);
    extern void pci_io_w32(uint32_t adr, uint32_t data);

Registers over Memory space
~~~~~~~~~~~~~~~~~~~~~~~~~~~

PCI host bridge hardware normally swap data accesses into the endianness of the
host architecture in order to lower the load of the CPU, peripherals can do DMA
without swapping. However, the host controller can not separate a standard
memory access from a memory access to a register, registers may be mapped into
memory space. This leads to register content being swapped, which must be
swapped back. The below routines makes it possible to access registers over PCI
memory space in a portable way on different architectures, the BSP or
architecture must provide necessary functions in order to implement this.

.. code-block:: c

    static inline uint16_t pci_ld_le16(volatile uint16_t *addr);
    static inline void pci_st_le16(volatile uint16_t *addr, uint16_t val);
    static inline uint32_t pci_ld_le32(volatile uint32_t *addr);
    static inline void pci_st_le32(volatile uint32_t *addr, uint32_t val);
    static inline uint16_t pci_ld_be16(volatile uint16_t *addr);
    static inline void pci_st_be16(volatile uint16_t *addr, uint16_t val);
    static inline uint32_t pci_ld_be32(volatile uint32_t *addr);
    static inline void pci_st_be32(volatile uint32_t *addr, uint32_t val);

In order to support non-standard big-endian PCI bus the above ``pci_*``
functions is required, ``pci_ld_le16 != ld_le16`` on big endian PCI buses.

Access functions
~~~~~~~~~~~~~~~~

The PCI Access Library can provide device drivers with function pointers
executing the above Configuration, I/O and Memory space accesses. The functions
have the same arguments and return values as the above functions.

The pci_access_func() function defined below can be used to get a function
pointer of a specific access type.

.. code-block:: c

    /* Get Read/Write function for accessing a register over PCI Memory Space
     * (non-inline functions).
     *
     * Arguments
     *  wr             0(Read), 1(Write)
     *  size           1(Byte), 2(Word), 4(Double Word)
     *  func           Where function pointer will be stored
     *  endian         PCI_LITTLE_ENDIAN or PCI_BIG_ENDIAN
     *  type           1(I/O), 3(REG over MEM), 4(CFG)
     *
     * Return
     *  0              Found function
     *  others         No such function defined by host driver or BSP
    */
    int pci_access_func(int wr, int size, void **func, int endian, int type);

PCI device drivers may be written to support run-time detection of endianess,
this is mosly for debugging or for development systems. When the product is
finally deployed macros switch to using the inline functions instead which have
been configured for the correct endianness.

.. index:: PCI address translation

PCI address translation
~~~~~~~~~~~~~~~~~~~~~~~

When PCI addresses, both I/O and memory space, is not mapped 1:1 address
translation before access is needed. If drivers read the PCI resources directly
using configuration space routines or in the device tree, the addresses given
are PCI addresses. The below functions can be used to translate PCI addresses
into CPU accessible addresses or vice versa, translation may be different for
different PCI spaces/regions.

.. code-block:: c

    /* Translate PCI address into CPU accessible address */
    static inline int pci_pci2cpu(uint32_t *address, int type);

    /* Translate CPU accessible address into PCI address (for DMA) */
    static inline int pci_cpu2pci(uint32_t *address, int type);

.. index:: PCI Interrupt

PCI Interrupt
-------------

The PCI specification defines four different interrupt lines INTA#..INTD#, the
interrupts are low level sensitive which make it possible to support multiple
interrupt sources on the same interrupt line. Since the lines are level
sensitive the interrupt sources must be acknowledged before clearing the
interrupt contoller, or the interrupt controller must be masked. The BSP must
provide a routine for clearing/acknowledging the interrupt controller, it is up
to the interrupt service routine to acknowledge the interrupt source.

The PCI Library relies on the BSP for implementing shared interrupt handling
through the BSP_PCI_shared_interrupt_* functions/macros, they must be defined
when including bsp.h.

PCI device drivers may use the pci_interrupt_* routines in order to call the
BSP specific functions in a platform independent way. The PCI interrupt
interface has been made similar to the RTEMS IRQ extension so that a BSP can
use the standard RTEMS interrupt functions directly.

PCI Shell command
-----------------

The RTEMS shell has a PCI command 'pci' which makes it possible to read/write
configuration space, print the current PCI configuration and print out a
configuration C-file for the static or peripheral library.
