% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2024 embedded brains GmbH & Co. KG

(RustBareMetal)=

# Bare Metal Rust with RTEMS

To develop with Rust and RTEMS together, you must find a Rust bare metal
target which matches an RTEMS BSP. The instructions in this section
are for a SPARC and a Risc-V *hello world* program. These examples use
the combinations shown in the table below:

| RTEMS Architecture | RTEMS BSP        | Rust Target                | Rust CPU     |
| ------------------ | ---------------- | -------------------------- | ------------ |
| rtems-sparc        | sparc/leon3      | sparc-unknown-none-elf     | leon3        |
| rtems-riscv        | riscv/rv64imafdc | riscv64gc-unknown-none-elf | generic-rv64 |

The following sources may be helpful to find a matching BSP and target:

- `./waf bsplist` -- executed in an RTEMS git clone
- `source-builder/sb-set-builder --list-bsets` -- executed in an
  RTEMS source builder git clone
- `./rtems-bsps` -- executed in an RTEMS git clone
- `rustc --print target-list`
- `rustc --target=riscv64gc-unknown-none-elf --print target-features`
- `rustc --target=riscv64gc-unknown-none-elf  --print target-cpus`
- [Rust Platform Support](https://doc.rust-lang.org/nightly/rustc/platform-support.html)

The sample instructions which follow build two executables using the
same source code for the RTEMS configuration `init.c` and the Rust
hello-world application `lib.rs`. Only the configuration as well as
the compile and link commands differ for SPARC Leon3 and RISC-V
64 bit. The Rust application uses `printk()` from RTEMS to print
text to the console.

After building the RTEMS BSP and installing Rust, the basic steps are:

1. Compile the RTEMS configuration in `init.c` into an object
   file using the GNU C compiler from the RTEMS tool chain.
2. Compile the Rust code containing `main()` into a
   static library using the Rust compiler.
3. Link the static library with the Rust code,
   the RTEMS configuration and the RTEMS OS libraries
   together into one single executable.
4. Finally run the executable on a simulator.

You can build the examples in a container. This is optional. If you
prefer to follow these instructions directly on your machine simply
skip the section *Build a Container*. Just make sure that you machine
meets all prerequisites to build the RTEMS tools and install the Rust
tools.

(RustBareMetal_Container)=

## Build a Container

The container must be able to execute the RTEMS source builder and to
install and run the Rust tools. In an empty directory of your choice
create the following `Dockerfile`.

```shell
cat >Dockerfile <<"EOF"
# Dockerfile to build a container image to use Rust on top of RTEMS
FROM ubuntu:24.04
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
        bison \
        build-essential \
        curl \
        flex \
        g++ \
        gdb \
        git \
        libncurses5-dev \
        ninja-build \
        pax \
        pkg-config \
        python3-dev \
        python-is-python3 \
        qemu-system-misc \
        texinfo \
        unzip \
        zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -c "Rust Developer" -g "users" \
            -d "/home/ferris" --create-home "ferris" && \
    mkdir -p /opt/rtems && \
    chown ferris:users /opt/rtems && \
    runuser -u ferris echo \
            'export PATH=/opt/rtems/@rtems-ver-major@/bin:${PATH}' \
            >>/home/ferris/.bashrc
USER ferris
WORKDIR /home/ferris
CMD ["/bin/bash"]
EOF
```

Podman is used in the shell commands below. If you prefer Docker
simply replace `podman` through `docker`.

Build the container image `rtems_rust`, create and start a container
with these commands:

```shell
podman build -t rtems_rust .
podman run -it --name=rusty_rtems rtems_rust bash
```

To follow the step-by-step instructions of the next sub-sections,
simply execute them as user `ferris` in the container. Note that
this container will not automatically be deleted on `exit`.
The building of the RTEMS tools takes a while and you probably want
to keep the container for further experiments.

(RustBareMetal_RTEMSTools)=

## Build the RTEMS Tools

In an empty directory of your choice, clone the RTEMS source builder
git repository:

```shell
git clone https://gitlab.rtems.org/rtems/tools/rtems-source-builder.git rsb
```

Next build the RTEMS tools. In this example, you need tools for
*SPARC* and *RISC-V* architectures. The source builder installs them
in the prefix directory `/opt/rtems/@rtems-ver-major@`. The
directory `/opt/rtems` must exist and the user must have read and
write access.

```shell
cd rsb/rtems
../source-builder/sb-set-builder --prefix /opt/rtems/@rtems-ver-major@ \
    @rtems-ver-major@/rtems-sparc \
    @rtems-ver-major@/rtems-riscv
cd ../..
```

The tools will end up in `/opt/rtems/@rtems-ver-major@/bin` and that
directory should be part of the `$PATH` environment variable of the
user. For example:

```shell
export PATH=/opt/rtems/@rtems-ver-major@/bin:${PATH}
```

The following commands should work:

```shell
sparc-rtems@rtems-ver-major@-gcc --version
riscv-rtems@rtems-ver-major@-gcc --version
```

(RustBareMetal_RTEMSBSP)=

## Build and Install the RTEMS BSPs

Clone the RTEMS git repository:

```shell
git clone https://gitlab.rtems.org/rtems/rtos/rtems.git
```

Create a `config.ini` file for the two BSPs for which your are going
to build RTEMS:

```shell
cd rtems

cat >config.ini <<"EOF"
[sparc/leon3]
RTEMS_SMP = True
[riscv/rv64imafdc]
EOF
```

Build and install RTEMS:

```shell
./waf configure --prefix=/opt/rtems/@rtems-ver-major@
./waf
./waf install
```

Run some RTEMS tests to make sure the installation and the emulators
are working:

```shell
sparc-rtems@rtems-ver-major@-sis -leon3 -nouartrx -r m 4 \
    build/sparc/leon3/testsuites/samples/hello.exe
sparc-rtems@rtems-ver-major@-sis -leon3 -nouartrx -r m 4 \
    build/sparc/leon3/testsuites/samples/ticker.exe
qemu-system-riscv64 -M virt -nographic -bios \
    build/riscv/rv64imafdc/testsuites/samples/hello.exe
qemu-system-riscv64 -M virt -nographic -bios \
    build/riscv/rv64imafdc/testsuites/samples/ticker.exe
```

Finally, leave the git working tree:

```shell
cd ..
```

(RustBareMetal_InstallRust)=

## Install and Setup Rust Tools

Install Rust from the web-page with this command:

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

At this point you must setup the environment variables:

```shell
source "$HOME/.cargo/env"
```

Check that rust is correctly setup:

```shell
rustup update
cargo --version
```

(RustBareMetal_Sources)=

## Setup a Rust Project and Create Sources

Write a simple RTEMS `init.c` to configure RTEMS in a new directory:

```shell
mkdir example-rust
cd example-rust

cat >init.c <<"EOF"
/*
 * Simple RTEMS configuration
 */

#define CONFIGURE_APPLICATION_NEEDS_CLOCK_DRIVER
#define CONFIGURE_APPLICATION_NEEDS_CONSOLE_DRIVER

#define CONFIGURE_UNLIMITED_OBJECTS
#define CONFIGURE_UNIFIED_WORK_AREAS

#define CONFIGURE_RTEMS_INIT_TASKS_TABLE

#define CONFIGURE_INIT

#include <rtems/confdefs.h>
EOF
```

Create a new Rust project which produces a static linked library:

```shell
cargo new --lib --vcs=none hello-rtems
cat >>hello-rtems/Cargo.toml <<"EOF"

[lib]
crate-type = ["staticlib"]
EOF
```

Store the Rust application code:

```rust
cat >hello-rtems/src/lib.rs <<"EOF"
#![no_std]
#![no_main]

use core::fmt::Write;
use core::ffi::c_char;

extern "C" {
    fn printk(fmt: *const core::ffi::c_char, ...) -> core::ffi::c_int;
    fn rtems_panic(fmt: *const core::ffi::c_char, ...) -> !;
    fn rtems_shutdown_executive(fatal_code: u32);
}

/// Write text to the console using RTEMS `printk()` function
struct Console;

impl core::fmt::Write for Console {
    fn write_str(&mut self, message: &str) -> core::fmt::Result {
        const FORMAT_STR: &core::ffi::CStr = {
            let Ok(s) = core::ffi::CStr::from_bytes_with_nul(b"%.*s\0") else {
                panic!()
            };
            s
        };
        if message.len() != 0 {
            unsafe {
                printk(FORMAT_STR.as_ptr(), message.len() as core::ffi::c_int, message.as_ptr());
            }
        }
        Ok(())
    }
}

/// Our `Init()` calls `rust_main()` and handles errors
#[no_mangle]
pub extern "C" fn Init() {
    if let Err(e) = rust_main() {
        panic!("Main returned {:?}", e);
    }
    unsafe {
        rtems_shutdown_executive( 0 );
    }
}

/// This is the main function of this program
fn rust_main() -> Result<(), core::fmt::Error> {
    let mut console = Console;
    writeln!(console, "Hello from Rust")?;
    Ok(())
}

/// Handle panic by forwarding it to the `rtems_panic()` handler
#[panic_handler]
fn panic(panic: &core::panic::PanicInfo) -> ! {
    // The panic message can only be reached from libcore in unstable
    // (i.e. nightly builds). Print at least the location raising the panic.
    // See https://www.ralfj.de/blog/2019/11/25/how-to-panic-in-rust.html
    if let Some(location) = panic.location() {
        const FORMAT_STR: *const c_char = {
            const BYTES: &[u8] = b"Panic occurred at %.*s:%d:%d\n\0";
            BYTES.as_ptr().cast()
        };
        if location.file().len() != 0 {
            unsafe {
                rtems_panic(FORMAT_STR,
                    location.file().len() as core::ffi::c_int,
                    location.file().as_ptr(),
                    location.line() as core::ffi::c_int,
                    location.column() as core::ffi::c_int,
                );
            }
        }
    }

    // If there is no location, fall back to the basic.
    let message = "Panic occured!";
    const FORMAT_PTR: *const c_char = {
        const BYTES: &[u8] = b"%.*s\n\0";
        BYTES.as_ptr().cast()
    };
    unsafe {
       rtems_panic(FORMAT_PTR,
           message.len() as core::ffi::c_int,
           message.as_ptr());
    }
}
EOF
```

Create a configuration file for Cargo:

```shell
mkdir hello-rtems/.cargo

cat >hello-rtems/.cargo/config.toml <<"EOF"
[target.riscv64gc-unknown-none-elf]
# Either kind should work as a linker
linker = "riscv-rtems@rtems-ver-major@-gcc"
# linker = "riscv-rtems@rtems-ver-major@-clang"
rustflags = [
    # See `rustc --target=riscv64gc-unknown-none-elf  --print target-cpus`
    "-Ctarget-cpu=generic-rv64",
    # The linker is a gcc compatible C Compiler
    "-Clinker-flavor=gcc",
    # Pass these options to the linker
    "-Clink-arg=-march=rv64imafdc",
    "-Clink-arg=-mabi=lp64d",
    "-Clink-arg=-mcmodel=medany",
    # Rust needs libatomic.a to satisfy Rust's compiler-builtin library
    "-Clink-arg=-latomic",
]
runner = "qemu-system-riscv64 -M virt -nographic -bios"

# Target available in rust nightly from 2023-07-18
[target.sparc-unknown-none-elf]
# Either kind should work as a linker
linker = "sparc-rtems@rtems-ver-major@-gcc"
# linker = "sparc-rtems@rtems-ver-major@-clang"
rustflags = [
    # The target is LEON3
    "-Ctarget-cpu=leon3",
    # The linker is a gcc compatible C Compiler
    "-Clinker-flavor=gcc",
    # Pass these options to the linker
    "-Clink-arg=-mcpu=leon3",
    # Rust needs libatomic.a to satisfy Rust's compiler-builtin library
    "-Clink-arg=-latomic",
]
runner = "sparc-rtems@rtems-ver-major@-sis -leon3 -nouartrx -r m 4"

[build]
target = ["riscv64gc-unknown-none-elf", "sparc-unknown-none-elf"]

[unstable]
build-std = ["core"]
EOF
```

(RustBareMetal_BuildRiscV)=

## Build and Run on RISC-V

First, download some additional files needed for this target:

```shell
rustup target add riscv64gc-unknown-none-elf
```

Compile the Rust source file into a static library:

```shell
cd hello-rtems
cargo build --target=riscv64gc-unknown-none-elf
cd ..
```

This should create
`hello-rtems/target/riscv64gc-unknown-none-elf/debug/libhello_rtems. a`. Note that the project directory (`hello-rtems`) is written with
a minus "`-`" while the library (`libhello_rtems.a`) is written
with an underscore "`_`".

Compile the RTEMS `init.c` file and link everything
together into a single executable:

```shell
export PKG_CONFIG_RISCV=/opt/rtems/@rtems-ver-major@/lib/pkgconfig/riscv-rtems@rtems-ver-major@-rv64imafdc.pc

riscv-rtems@rtems-ver-major@-gcc -Wall -Wextra -O2 -g \
    -fdata-sections -ffunction-sections \
    $(pkg-config --cflags ${PKG_CONFIG_RISCV}) init.c -c -o init_riscv.o

riscv-rtems@rtems-ver-major@-gcc init_riscv.o \
  -Lhello-rtems/target/riscv64gc-unknown-none-elf/debug \
  -lhello_rtems \
  -ohello_rtems_riscv.exe \
  $(pkg-config --variable=ABI_FLAGS ${PKG_CONFIG_RISCV}) \
  $(pkg-config --libs ${PKG_CONFIG_RISCV})
```

This should produce the executable file `hello_rtems_riscv.exe`. Finally,
run the executable on an emulator (`qemu`):

```shell
rtems-run --rtems-bsp=rv64imafdc hello_rtems_riscv.exe
```

The emulator run should produce the following output:

```none
RTEMS Testing - Run, @rtems-ver-major@.0.not_released
 Command Line: /opt/rtems/@rtems-ver-major@/bin/rtems-run --rtems-bsp=rv64imafdc hello_rtems_riscv.exe
 Host: Linux 0fa931a464ca 5.14.21-150500.55.62-default #1 SMP PREEMPT_DYNAMIC Tue May 7 11:55:30 UTC 2024 (66dfe0d) x86_64
 Python: 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0]
Host: Linux-5.14.21-150500.55.62-default-x86_64-with-glibc2.39 (Linux 0fa931a464ca 5.14.21-150500.55.62-default #1 SMP PREEMPT_DYNAMIC Tue May 7 11:55:30 UTC 2024 (66dfe0d) x86_64 x86_64)
Hello from Rust

[ RTEMS shutdown ]
RTEMS version: @rtems-ver-major@.0.0.e74cea4172ee8564bef5f8500c5dd07512257d99
RTEMS tools: 13.2.1 20240502 (RTEMS @rtems-ver-major@, RSB 484c7a4095fe8cebba0320b58bf9477f2f40b1b6, Newlib 730703b)
executing thread ID: 0x0a010001
executing thread name: UI1
Run time     : 0:00:00.254684
```

Version numbers may be different in your output.

(RustBareMetal_BuildSparc)=

## Build and Run on SPARC

You need to use the Rust nightly build because the support for
Gaisler LEON3/4/5 was added in July 2023 and is not yet available
in stable Rust:

```shell
rustup toolchain add nightly
rustup component add rust-src --toolchain=nightly
```

Compile the Rust source file into a static library:

```shell
cd hello-rtems
cargo +nightly build --target=sparc-unknown-none-elf
cd ..
```

It should create
`hello-rtems/target/sparc-unknown-none-elf/debug/libhello_rtems.a`.

Compile the RTEMS `init.c` file and link everything
together into an executable:

```shell
export PKG_CONFIG_SPARC=/opt/rtems/@rtems-ver-major@/lib/pkgconfig/sparc-rtems@rtems-ver-major@-leon3.pc

sparc-rtems@rtems-ver-major@-gcc -Wall -Wextra -O2 -g \
    -fdata-sections -ffunction-sections \
    $(pkg-config --cflags ${PKG_CONFIG_SPARC}) init.c -c -o init_sparc.o

sparc-rtems@rtems-ver-major@-gcc init_sparc.o \
    -qnolinkcmds -T linkcmds.leon3 \
    -Lhello-rtems/target/sparc-unknown-none-elf/debug \
    -lhello_rtems \
    -ohello_rtems_sparc.exe \
    $(pkg-config --libs ${PKG_CONFIG_SPARC})
```

This should produce the executable file `hello_rtems_sparc.exe`. Finally,
run the executable on an emulator (`sis`):

```shell
rtems-run --rtems-bsp=leon3-sis hello_rtems_sparc.exe
```

The emulator run should produce the following output:

```none
RTEMS Testing - Run, @rtems-ver-major@.0.not_released
 Command Line: /opt/rtems/@rtems-ver-major@/bin/rtems-run --rtems-bsp=leon3-sis hello_rtems_sparc.exe
 Host: Linux 0fa931a464ca 5.14.21-150500.55.62-default #1 SMP PREEMPT_DYNAMIC Tue May 7 11:55:30 UTC 2024 (66dfe0d) x86_64
 Python: 3.12.3 (main, Apr 10 2024, 05:33:47) [GCC 13.2.0]
Host: Linux-5.14.21-150500.55.62-default-x86_64-with-glibc2.39 (Linux 0fa931a464ca 5.14.21-150500.55.62-default #1 SMP PREEMPT_DYNAMIC Tue May 7 11:55:30 UTC 2024 (66dfe0d) x86_64 x86_64)

 SIS - SPARC/RISCV instruction simulator 2.30,  copyright Jiri Gaisler 2020
 Bug-reports to jiri@gaisler.se

 LEON3 emulation enabled, 4 cpus online, delta 50 clocks

 Loaded hello_rtems_sparc.exe, entry 0x40000000
Hello from Rust
cpu 0 in error mode (tt = 0x80)
   217550  40018f60:  91d02000   ta  0x0
Run time     : 0:00:00.253700
```

Version numbers may be different in your output.
