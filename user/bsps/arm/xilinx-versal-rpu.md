% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2026 Airbus Defence and Space

(BSP_arm_versal_rpu_lock_step)=

(BSP_arm_versal_rpu_split_0)=

(BSP_arm_versal_rpu_split_1)=

# Xilinx Versal RPU

This BSP supports the Real-time Processing Unit (RPU) on Xilinx Versal
Adaptive SoCs. The RPU has two Cortex-R5 cores which can operate in lock-step
or split mode. Basic hardware initialization is performed by the Cortex-R5
BSP. This BSP supports the GICv2 interrupt controller available to the RPU
subsystem. Since the RPU subsystem only varies in speed, this BSP should be
functional across all chip variants as well as on Xilinx's QEMU branch.
There are three BSP variants available for customization:

- `versal_rpu_lock_step`
- `versal_rpu_split_0`
- `versal_rpu_split_1`

The `versal_rpu_lock_step` BSP variant is intended to be used for the RPU in
lock-step mode. In this case, Tightly-Coupled Memories (ATCM and BTCM) could be
used as a combined memory area for code and data. The `versal_rpu_split_0` and
`versal_rpu_split_1` BSP variants are intended to be used for the RPU in
split mode for core 0 and 1 respectively. The core 0 variant initializes the
GIC distributor. The core 1 variants waits for the GIC distributor
initialization done by core 0 during the system initialization. The DDR RAM is
a shared resource and should be used according to applications-specific
requirements. The default BSP settings for the DDR RAM usage aimed at testing
the BSP variants via `remoteproc`.

## Clock Driver

The clock driver uses the Triple Timer Counter 3 (TTC3) as the timer interrupt
source.

## Console Driver

The console driver supports the default Qemu emulated ARM PL011 PrimeCell UART
as well as the physical ARM PL011 PrimeCell UART in the Versal hardware.

## Boot on Versal Hardware

On the Versal RPU, RTEMS can be started by:

- Platform Loader and Manager (PLM) firmware, when directly in the `BOOT.BIN`.
- Cortex-A72 linux, with `remoteproc` driver.
- Cortex-R5 U-Boot.
- Cortex-A72 U-Boot.
- JTAG.

For quick turnaround during testing, it is recommended to use Cortex-A72 linux
via `remoteproc` driver to avoid repeated `BOOT.bin` generation.

Example with `hello.exe` application:
```shell
$ cp hello.exe /lib/firmware/
$ echo hello.exe > /sys/class/remoteproc/remoteproc0/firmware
$ echo start > /sys/class/remoteproc/remoteproc0/state
 remoteproc remoteproc0: powering up ff9a0000.rf5ss:r5f_0
 remoteproc remoteproc0: Booting fw image hello.exe, size 1861792
 remoteproc remoteproc0: no resource table found.
 remoteproc remoteproc0: remote processor ff9a0000.rf5ss:r5f_0 is now up

*** BEGIN OF TEST HELLO WORLD ***
*** TEST VERSION: 7.0.0.98e76a5a3bfecafc4b07bbcdb84a1aabb14fea21-modified
*** TEST STATE: EXPECTED_PASS
*** TEST BUILD:
*** TEST TOOLS: 15.2.0 20250808 (RTEMS 7, RSB 3546aa1e5662aa475bc0521ad2d1c66c3
9fe47ec, Newlib 038afec1)
Hello World

*** END OF TEST HELLO WORLD ***

[ RTEMS shutdown ]
RTEMS version: 7.0.0.98e76a5a3bfecafc4b07bbcdb84a1aabb14fea21-modified
RTEMS tools: 15.2.0 20250808 (RTEMS 7, RSB 3546aa1e5662aa475bc0521ad2d1c66c39fe
47ec, Newlib 038afec1)
executing thread ID: 0x0a010001
executing thread name: UI1

$ echo stop > /sys/class/remoteproc/remoteproc0/state
```

## Linux device tree

DDR RAM used by RTEMS application should be specified in a `reserved-memory`
node and nodes related to `remoteproc` driver should be declared.

Device tree for Versal RPU in lockstep mode:
```
&{/} {
	reserved-memory {
		#address-cells = <2>;
		#size-cells = <2>;
		ranges;

		rproc_0_reserved: rproc@3e000000 {
			no-map;
			reg = <0x0 0x3e000000 0x0 0x1000000>;
		};

		rpu0vdev0vring0: rpu0vdev0vring0@3d000000 {
			no-map;
			reg = <0x0 0x3d000000 0x0 0x4000>;
		};
		rpu0vdev0vring1: rpu0vdev0vring1@3d004000 {
			no-map;
			reg = <0x0 0x3d004000 0x0 0x4000>;
		};
		rpu0vdev0buffer: rpu0vdev0buffer@3d008000 {
			no-map;
			reg = <0x0 0x3d008000 0x0 0x100000>;
		};
	};

	tcm_0a: tcm_0a@ffe00000 {
		no-map;
		reg = <0x0 0xffe00000 0x0 0x10000>;
		status = "okay";
		compatible = "mmio-sram";
		power-domain = <&versal_firmware 0x1831800b>;
	};

	tcm_0b: tcm_0b@ffe20000 {
		no-map;
		reg = <0x0 0xffe20000 0x0 0x10000>;
		status = "okay";
		compatible = "mmio-sram";
		power-domain = <&versal_firmware 0x1831800c>;
	};

	rf5ss@ff9a0000 {
		compatible = "xlnx,zynqmp-r5-remoteproc";
		#address-cells = <0x2>;
		#size-cells = <0x2>;
		ranges;
		xlnx,cluster-mode = <0>; /* lockstep (0), split (1) */
		reg = <0x0 0xff9a0000 0x0 0x10000>;

		r5f_0 {
			compatible = "xilinx,r5f";
			#address-cells = <0x2>;
			#size-cells = <0x2>;
			ranges;
			sram = <&tcm_0a>, <&tcm_0b>;
			memory-region = <&rproc_0_reserved>, <&rpu0vdev0buffer>,
					<&rpu0vdev0vring0>, <&rpu0vdev0vring1>;
			power-domain = <&versal_firmware 0x18110005>;
		};
	};
};
```

Device tree for Versal RPU in split mode:
```
&{/} {
	reserved-memory {
		#address-cells = <2>;
		#size-cells = <2>;
		ranges;

		rproc_0_reserved: rproc@3e000000 {
			no-map;
			reg = <0x0 0x3e000000 0x0 0x1000000>;
		};
		rproc_1_reserved: rproc@3f000000 {
			no-map;
			reg = <0x0 0x3f000000 0x0 0x1000000>;
		};

		rpu0vdev0vring0: rpu0vdev0vring0@3d000000 {
			no-map;
			reg = <0x0 0x3d000000 0x0 0x4000>;
		};
		rpu0vdev0vring1: rpu0vdev0vring1@3d004000 {
			no-map;
			reg = <0x0 0x3d004000 0x0 0x4000>;
		};
		rpu0vdev0buffer: rpu0vdev0buffer@3d008000 {
			no-map;
			reg = <0x0 0x3d008000 0x0 0x100000>;
		};
		rpu1vdev0vring0: rpu0vdev0vring0@3d200000 {
			no-map;
			reg = <0x0 0x3d200000 0x0 0x4000>;
		};
		rpu1vdev0vring1: rpu0vdev0vring1@3d204000 {
			no-map;
			reg = <0x0 0x3d204000 0x0 0x4000>;
		};
		rpu1vdev0buffer: rpu0vdev0buffer@3d208000 {
			no-map;
			reg = <0x0 0x3d208000 0x0 0x100000>;
		};
	};

	tcm_0a: tcm_0a@ffe00000 {
		no-map;
		reg = <0x0 0xffe00000 0x0 0x10000>;
		status = "okay";
		compatible = "mmio-sram";
		power-domain = <&versal_firmware 0x1831800b>;
	};

	tcm_0b: tcm_0b@ffe20000 {
		no-map;
		reg = <0x0 0xffe20000 0x0 0x10000>;
		status = "okay";
		compatible = "mmio-sram";
		power-domain = <&versal_firmware 0x1831800c>;
	};

	tcm_1a: tcm_1a@ffe90000 {
		no-map;
		reg = <0x0 0xffe90000 0x0 0x10000>;
		status = "okay";
		compatible = "mmio-sram";
		power-domain = <&versal_firmware 0x1831800d>;
	};

	tcm_1b: tcm_1b@ffeb0000 {
		no-map;
		reg = <0x0 0xffeb0000 0x0 0x10000>;
		status = "okay";
		compatible = "mmio-sram";
		power-domain = <&versal_firmware 0x1831800e>;
	};

	rf5ss@ff9a0000 {
		compatible = "xlnx,zynqmp-r5-remoteproc";
		#address-cells = <0x2>;
		#size-cells = <0x2>;
		ranges;
		xlnx,cluster-mode = <1>; /* lockstep (0), split (1) */
		reg = <0x0 0xff9a0000 0x0 0x10000>;

		r5f_0 {
			compatible = "xilinx,r5f";
			#address-cells = <0x2>;
			#size-cells = <0x2>;
			ranges;
			sram = <&tcm_0a>, <&tcm_0b>;
			memory-region = <&rproc_0_reserved>, <&rpu0vdev0buffer>,
					<&rpu0vdev0vring0>, <&rpu0vdev0vring1>;
			power-domain = <&versal_firmware 0x18110005>;
		};

		r5f_1 {
			compatible = "xilinx,r5f";
			#address-cells = <0x2>;
			#size-cells = <0x2>;
			ranges;
			sram = <&tcm_1a>, <&tcm_1b>;
			memory-region = <&rproc_1_reserved>, <&rpu1vdev0buffer>,
					<&rpu1vdev0vring0>, <&rpu1vdev0vring1>;
			power-domain = <&versal_firmware 0x18110006>;
		};
	};
};
```

## Hardware Boot Image Generation

RTEMS application could be added to the `BOOT.BIN` with a dedicated entry into
the Boot Image Format (BIF) file.
```
...
{ core=r5-lockstep, file=/build_dir/hello.exe }
...
```

> During Linux boot, unused peripherals are [powered down](https://docs.amd.com/r/2025.1-English/ug1304-versal-acap-ssdg/Power-Management-Using-XPm_InitFinalize), including triple timer counters (TTC).
In order to avoid an unexpected power down of the TTC used by RTEMS, there are 
several solutions:
> - Request the node in the RTEMS application (see [XPm_RequestNode](https://docs.amd.com/r/2025.1-English/ug1304-versal-acap-ssdg/Requesting-and-Releasing-a-Node)).
> - Modify PLM firmware in order to exclude triple timer counter from power down list (see `IsDevExcluded()` in [xpm_subsystem.c](https://github.com/Xilinx/embeddedsw/blob/master/lib/sw_services/xilpm/src/versal_common/server/xpm_subsystem.c#L171)).

## TTC debug

TTC configuration and status can be verified from Linux but requires first to
request the related node.
```shell
$ echo pm_request_node 0x18224027 0x7 0x64 0 > /sys/kernel/debug/zynqmp-firmware/pm
```

> `pm_request_node <node id> <capabilities> <QOS> <secure>`
>
> Parameters:
> - node id: node id of the slave (see [device nodes](https://docs.amd.com/r/2022.2-English/oslib_rm/Define-PM_DEV_TTC_3)).
> - capabilities: requested capabilities of the slave (0x07 set all capabilities).
> - QOS: quality of service (value in 0-100 range).
> - secure: unused.

Once node is requested, TTC registers can be obtained via devmem, ex:
```shell
$ devmem 0xFF11000C
0x00000021
```
