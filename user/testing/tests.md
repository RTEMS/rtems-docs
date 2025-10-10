% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018 Chris Johns <chrisj@rtems.org>

# Test Banners

All test output banners or strings are embedded in each test and the test
outputs the banners to the BSP's console as it executes. The RTEMS Tester
captures the BSP's console and uses this information to manage the state of
the executing test. The banner strings are:

(test-banner-begin)=

```{index} test begin, TEST BEGIN
```

`*** BEGIN TEST <name> ***`
: The test has loaded, RTEMS has initialized and the test specific code is
  about to start executing. The `<name>` field is the name of the test. The
  test name is internal to the test and may not match the name of the
  executable. The test name is informative and not used by the RTEMS Tester.

(test-banner-end)=

```{index} test end, TEST END
```

`*** END TEST <name> ***`
: The test has finished without error and has passed. The `<name>` field is
  the name of the test. See the {ref}`Test Begin Banner <test-banner-begin>`
  for details about the name.

```{index} test banner version, TEST VERSION
```

`*** TEST VERSION: <version>`
: The test prints the RTEMS version return by the RTEMS Version API as
  `<version>`. All tests must match the first test's version or the Wrong
  Version error count is incremented.

(test-banner-state)=

```{index} test state, TEST STATE
```

`*** TEST STATE: <state>`
: The test is tagged in the RTEMS sources with a special `<state>` for this
  BSP. See {ref}`Test States <test-states>` for the list of possible
  states. The state banner lets the RTEMS Tester categorize and manage the
  test. For example a user input test typically needing user interaction may
  never complete producing an *invalid* test result. A user input test is
  terminated to avoid extended delays in a long test run.

(test-banner-build)=

```{index} test build, TEST BUILD
```

`*** TEST BUILD: <build>`
: The test prints the RTEMS build as a space separated series of labels as
  `<build>`. The build labels are created from the configuration settings in
  the Super Score header file `rtems/score/cputops.h`. All tests must match
  the first test's build or the Wrong Build error count is incremented.

(test-banner-tools)=

```{index} test tools, TEST TOOLS
```

`*** TEST TOOLS: <version>`
: The test prints the RTEMS tools version returned the GGC internal macro
  `_VERSION_` as `<version>`. All tests must match the first test's tools
  version string or the Wrong Tools error count is incremented.

(test-states)=

```{index} Test states
```

# Test Controls

The tests in the RTEMS kernel testsuite can be configured for each BSP. The
expected state of the test can be set as well as any configuration parameters
a test needs to run on a BSP.

The test states are:

```{index} test state passed
```

`passed`
: The test start and end banners have been sent to the console.

```{index} test state failure
```

`failure`
: The test start banner has been sent to the console and no end banner has been
  seen when a target restart is detected.

```{index} test state expected-fail
```

`excepted-fail`
: The test is tagged as `expected-fail` in the RTEMS sources for this BSP and
  outputs the banner `*** TEST STATE: EXPECTED_FAIL`. The test is known not
  to pass on this BSP. The RTEMS Tester will let the test run as far as it
  can and if the test passes it is recorded as a pass in the test results
  otherwise it is recorded as *expected-fail*.

```{index} test state indeterminate
```

`indeterminate`
: The test is tagged as `indeterminate` in the RTEMS sources for this BSP and
  outputs the banner `*** TEST STATE: INDETERMINATE`. The test may or may not
  pass so the result is not able to be determined. The RTEMS Tester will let
  the test run as far as it can and record the result as indeterminate.

```{index} test state user-input
```

`user-input`
: The test is tagged as `user-input` in the RTEMS sources and outputs the
  banner `*** TEST STATE: USER_INPUT`. The RTEMS Tester will reset the target
  if the target's configuration provides a target reset command.

```{index} test state benchmark
```

`benchmark`
: The test is tagged as `benchmark` in the RTEMS sources and outputs the
  banner `*** TEST STATE: BENCHMARK`. Benchmarks can take a while to run and
  performance is not regression tested in RTEMS. The RTEMS Tester will reset
  the target if the target's configuration provides a target reset command.

```{index} test state timeout
```

`timeout`
: The test start banner has been sent to the console and no end banner is seen
  within the *timeout* period and the target has not restart. A default
  *timeout* can be set in a target configuration, a user configuration or
  provide on the RTEMS Tester's command line using the `--timeout` option.

```{index} test state invalid
```

`invalid`
: The test did not output a start banner and the RTEMS Tester has detected the
  target has restarted. This means the executable did not load correctly, the
  RTEMS kernel did not initialize or the RTEMS kernel configuration failed for
  this BSP.

## Expected Test States

A test's expected state is set in the RTEMS kernel's testsuite. The default for
a tested is to `pass`. If a test is known to fail it can have it's state set
to `expected-fail`. Setting tests that are known to fail to `expected-fail`
lets everyone know a failure is not to be countered and consider a regression.

Expected test states are listed in test configuration files

## Test Configuration

Tests can be configured for each BSP using test configuration files. These
files exist under the `spec` directory and have the form `tst*.yml`. Global
default test states exist as part of the tests themselves and are applied to
all BSPs. BSPs can provide a test configuration that applies to just that BSP
and these files can include subsets of test configurations.

The configuration supports:

1. Including test configuration files to allow sharing of common
   configurations.
2. Excluding tests from being built that do not build for a BSP.
3. Setting the test state if it is not `passed`.
4. Specifing a BSP specific build configuration for a test.

The test configuration file format is described in the engineering manual.
Expected test state is configured using `set-test-state` action blocks in
build type YAML configuration files. These `set-test-state` action blocks
contain one or more sub blocks that each describe a `reason`, an expected
`state`, and a list of `tests` to which the `state` and `reason` apply.

The `reason` is a text description of why the expected test state is being
changed from the default and will typically include a ticket number that further
documents the status of the listed tests.

The `state` is one of:

`include`
: The test list is the name of a test configuration file to include

`exclude`
: The tests listed are not build. This can happen if a BSP cannot support a
  test. For example it does not have enough memory.

`expected-fail`
: The tests listed are set to expected fail. The test will fail on the BSP
  being built.

`user-input`
: The tests listed require user input to run and are not supported by automatic
  testers.

`indeterminate`
: The tests listed may pass or may not, the result is not reliable.

`benchmark`
: The tests listed are benchmarks. Benchmarks are flagged and not left to
  run to completion because they may take too long.

By default all tests are included, specific excluded tests using the
`exclude` state are excluded and cannot be included again.

# Test Builds

The test reports the build of RTEMS being tested. The build are:

```{index} build default
```

`default`
: The build is the default. No RTEMS configure options have been used.

```{index} build posix
```

`posix`
: The build includes the POSIX API. The RTEMS configure option
  `RTEMS_POSIX_API` has been set to True. The `cpuopts.h` define
  `RTEMS_POSIX` has defined and it true.

```{index} build smp
```

`smp`
: The build is an SMP kernel. The RTEMS configure option `RTEMS_SMP` has
  been set to True. The `cpuopts.h` define `RTEMS_SMP` has defined and it true.

```{index} build mp
```

`mp`
: The build is an MP kernel. The RTEMS configure option
  `RTEMS_MULTIPROCESSING`has been set to True. The `cpuopts.h` define
  `RTEMS_MULTIPROCESSING` has defined and it true.

```{index} build paravirt
```

`paravirt`
: The build is a paravirtualization kernel. The `cpuopts.h` define
  `RTEMS_PARAVIRT` has defined and it true.

```{index} build debug
```

`debug`
: The build includes kernel debugging support. The RTEMS configure option
  `RTEMS_DEBUG` has been set to True. The `cpuopts.h` define `RTEMS_DEBUG`
  has defined and it true.

```{index} build profiling
```

`profiling`
: The build include profiling support. The RTEMS configure option
  `RTEMS_PROFILING` has been set to True. The `cpuopts.h` define
  `RTEMS_PROFILING` has defined and it true.
