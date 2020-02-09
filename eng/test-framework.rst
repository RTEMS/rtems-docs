.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018, 2019 embedded brains GmbH
.. Copyright (C) 2018, 2019 Sebastian Huber

Software Test Framework
***********************

.. _RTEMSTestFramework:

The RTEMS Test Framework
========================

The `RTEMS Test Framework` helps you to write test suites.  It has the following
features:

* Implemented in standard C11

* Runs on at least FreeBSD, MSYS2, Linux and RTEMS

* Test runner and test case code can be in separate translation units

* Test cases are automatically registered at link-time

* Test cases may have a test fixture

* Test checks for various standard types

* Supports test case planning

* Test case scoped dynamic memory

* Test case destructors

* Test case resource accounting to show that no resources are leaked
  during the test case execution

* Supports early test case exit, e.g. in case a malloc() fails

* Individual test case and overall test suite duration is reported

* Procedures for code runtime measurements in RTEMS

* Easy to parse test report to generate for example human readable test reports

* Low overhead time measurement of short time sequences (using cycle counter
  hardware if a available)

* Configurable time service provider for a monotonic clock

* Low global memory overhead for test cases and test checks

* Supports multi-threaded execution and interrupts in test cases

* A simple (polled) put character function is sufficient to produce the test report

* Only text, global data and a stack pointer must be set up to run a test suite

* No dynamic memory is used by the framework itself

* No memory is aggregated throughout the test case execution

Nomenclature
------------

A `test suite` is a collection of test cases.  A `test case` consists of
individual test actions and checks.  A `test check` determines if the outcome
of a test action meets its expectation.  A `test action` is a program sequence
with an observable outcome, for example a function invocation with a return
status.  If the test action outcome is all right, then the test check passes,
otherwise the test check fails.  The test check failures of a test case are
summed up.  A test case passes, if the failure count of this test case is zero,
otherwise the test case fails.  The test suite passes if all test cases pass,
otherwise it fails.

Test Cases
----------

You can write a test case with the `T_TEST_CASE()` macro followed by a function
body:

.. code-block:: c

   T_TEST_CASE(name)
   {
      /* Your test case code */
   }

The test case `name` must be a valid C designator.  The test case names must be
unique within the test suite.  Just link modules with test cases to the test
runner to form a test suite.  The test cases are automatically registered via
static constructors.

.. code-block:: c
    :caption: Test Case Example

    #include <t.h>

    static int add(int a, int b)
    {
        return a + b;
    }

    T_TEST_CASE(a_test_case)
    {
        int actual_value;

        actual_value = add(1, 1);
        T_eq_int(actual_value, 2);
        T_true(false, "a test failure message");
    }

.. code-block:: none
    :caption: Test Case Report

    B:a_test_case
    P:0:8:UI1:test-simple.c:13
    F:1:8:UI1:test-simple.c:14:a test failure message
    E:a_test_case:N:2:F:1:D:0.001657

The `B` line indicates the begin of test case `a_test_case`.  The `P` line
shows that the test check in file `test-simple.c` at line 13 executed by task
`UI1` on processor 0 as the test step 0 passed.  The invocation of `add()` in
line 12 is the test action of test step 0.  The `F` lines shows that the test
check in file `test-simple.c` at line 14 executed by task `UI1` on processor 0
as the test step 1 failed with a message of `"a test failure message"`.  The
`E` line indicates the end of test case `a_test_case` resulting in a total of
two test steps (`N`) and one test failure (`F`).  The test case execution
duration (`D`) was 0.001657 seconds.  For test report details see:
:ref:`Test Reporting <RTEMSTestFrameworkTestReporting>`.

Test Fixture
------------

You can write a test case with a test fixture with the `T_TEST_CASE_FIXTURE()`
macro followed by a function body:

.. code-block:: c

   T_TEST_CASE_FIXTURE(name, fixture)
   {
      /* Your test case code */
   }

The test case `name` must be a valid C designator.  The test case names must be
unique within the test suite.  The `fixture` must point to a statically
initialized read-only object of type `T_fixture`.  The test fixture
provides methods to setup, stop and tear down a test case.  A context is passed
to the methods.  The initial context is defined by the read-only fixture
object.  The context can be obtained by the `T_fixture_context()`
function.  It can be set within the scope of one test case by the
`T_set_fixture_context()` function.  This can be used for example to
dynamically allocate a test environment in the setup method.

.. code-block:: c
    :caption: Test Fixture Example

    #include <t.h>

    static int initial_value = 3;

    static int counter;

    static void
    setup(void *ctx)
    {
        int *c;

        T_log(T_QUIET, "setup begin");
        T_eq_ptr(ctx, &initial_value);
        T_eq_ptr(ctx, T_fixture_context());
        c = ctx;
        counter = *c;
        T_set_fixture_context(&counter);
        T_eq_ptr(&counter, T_fixture_context());
        T_log(T_QUIET, "setup end");
    }

    static void
    stop(void *ctx)
    {
        int *c;

        T_log(T_QUIET, "stop begin");
        T_eq_ptr(ctx, &counter);
        c = ctx;
        ++(*c);
        T_log(T_QUIET, "stop end");
    }

    static void
    teardown(void *ctx)
    {
        int *c;

        T_log(T_QUIET, "teardown begin");
        T_eq_ptr(ctx, &counter);
        c = ctx;
        T_eq_int(*c, 4);
        T_log(T_QUIET, "teardown end");
    }

    static const T_fixture fixture = {
        .setup = setup,
        .stop = stop,
        .teardown = teardown,
        .initial_context = &initial_value
    };

    T_TEST_CASE_FIXTURE(fixture, &fixture)
    {
        T_assert_true(true, "all right");
        T_assert_true(false, "test fails and we stop the test case");
        T_log(T_QUIET, "not reached");
    }

.. code-block:: none
    :caption: Test Fixture Report

    B:fixture
    L:setup begin
    P:0:0:UI1:test-fixture.c:13
    P:1:0:UI1:test-fixture.c:14
    P:2:0:UI1:test-fixture.c:18
    L:setup end
    P:3:0:UI1:test-fixture.c:55
    F:4:0:UI1:test-fixture.c:56:test fails and we stop the test case
    L:stop begin
    P:5:0:UI1:test-fixture.c:28
    L:stop end
    L:teardown begin
    P:6:0:UI1:test-fixture.c:40
    P:7:0:UI1:test-fixture.c:42
    L:teardown end
    E:fixture:N:8:F:1

Test Case Planning
------------------

Each non-quiet test check fetches and increments the test step counter
atomically.  For each test case execution the planned steps can be specified
with the `T_plan()` function.

.. code-block:: c

    void T_plan(unsigned int planned_steps);

This function must be invoked at most once in each test case execution.  If the
planned test steps are set with this function, then the final test steps after
the test case execution must be equal to the planned steps, otherwise the test
case fails.

Use the `T_step_*(step, ...)` test check variants to ensure that the test case
execution follows exactly the planned steps.

.. code-block:: c
    :caption: Test Planning Example

    #include <t.h>

    T_TEST_CASE(wrong_step)
    {
        T_plan(2);
        T_step_true(0, true, "all right");
        T_step_true(2, true, "wrong step");
    }

    T_TEST_CASE(plan_ok)
    {
        T_plan(1);
        T_step_true(0, true, "all right");
    }

    T_TEST_CASE(plan_failed)
    {
        T_plan(2);
        T_step_true(0, true, "not enough steps");
        T_quiet_true(true, "quiet test do not count");
    }

    T_TEST_CASE(double_plan)
    {
        T_plan(99);
        T_plan(2);
    }

    T_TEST_CASE(steps)
    {
        T_step(0, "a");
        T_plan(3);
        T_step(1, "b");
        T_step(2, "c");
    }

.. code-block:: none
    :caption: Test Planning Report

    B:wrong_step
    P:0:0:UI1:test-plan.c:6
    F:1:0:UI1:test-plan.c:7:planned step (2)
    E:wrong_step:N:2:F:1
    B:plan_ok
    P:0:0:UI1:test-plan.c:13
    E:plan_ok:N:1:F:0
    B:plan_failed
    P:0:0:UI1:test-plan.c:19
    F:*:0:UI1:*:*:actual steps (1), planned steps (2)
    E:plan_failed:N:1:F:1
    B:double_plan
    F:*:0:UI1:*:*:planned steps (99) already set
    E:double_plan:N:0:F:1
    B:steps
    P:0:0:UI1:test-plan.c:31
    P:1:0:UI1:test-plan.c:33
    P:2:0:UI1:test-plan.c:34
    E:steps:N:3:F:0

Test Case Resource Accounting
-----------------------------

The framework can check if various resources are leaked during a test case
execution.  The resource checkers are specified by the test run configuration.
On RTEMS, checks for the following resources are available

* workspace and heap memory,
* file descriptors,
* POSIX keys and key value pairs,
* RTEMS barriers,
* RTEMS user extensions,
* RTEMS message queues,
* RTEMS partitions,
* RTEMS periods,
* RTEMS regions,
* RTEMS semaphores,
* RTEMS tasks, and
* RTEMS timers.

.. code-block:: c
    :caption: Resource Accounting Example

    #include <t.h>

    #include <stdlib.h>

    #include <rtems.h>

    T_TEST_CASE(missing_sema_delete)
    {
        rtems_status_code sc;
        rtems_id id;

        sc = rtems_semaphore_create(rtems_build_name('S', 'E', 'M', 'A'), 0,
            RTEMS_COUNTING_SEMAPHORE, 0, &id);
        T_rsc_success(sc);
    }

    T_TEST_CASE(missing_free)
    {
        void *p;

        p = malloc(1);
        T_not_null(p);
    }

.. code-block:: none
    :caption: Resource Accounting Report

    B:missing_sema_delete
    P:0:0:UI1:test-leak.c:14
    F:*:0:UI1:*:*:RTEMS semaphore leak (1)
    E:missing_sema_delete:N:1:F:1:D:0.004013
    B:missing_free
    P:0:0:UI1:test-leak.c:22
    F:*:0:UI1:*:*:memory leak in workspace or heap
    E:missing_free:N:1:F:1:D:0.003944

Test Case Scoped Dynamic Memory
-------------------------------

You can allocate dynamic memory which is automatically freed after the current
test case execution.  You can provide an optional destroy function to
`T_zalloc()` which is called right before the memory is freed.  The
`T_zalloc()` function initializes the memory to zero.

.. code-block:: c

   void *T_malloc(size_t size);

   void *T_calloc(size_t nelem, size_t elsize);

   void *T_zalloc(size_t size, void (*destroy)(void *));

   void T_free(void *ptr);

.. code-block:: c
    :caption: Test Case Scoped Dynamic Memory Example

    #include <t.h>

    T_TEST_CASE(malloc_free)
    {
        void *p;

        p = T_malloc(1);
        T_assert_not_null(p);
        T_free(p);
    }

    T_TEST_CASE(malloc_auto)
    {
        void *p;

        p = T_malloc(1);
        T_assert_not_null(p);
    }

    static void
    destroy(void *p)
    {
        int *i;

        i = p;
        T_step_eq_int(2, *i, 1);
    }

    T_TEST_CASE(zalloc_auto)
    {
        int *i;

        T_plan(3);
        i = T_zalloc(sizeof(*i), destroy);
        T_step_assert_not_null(0, i);
        T_step_eq_int(1, *i, 0);
        *i = 1;
    }

.. code-block:: none
    :caption: Test Case Scoped Dynamic Memory Report

    B:malloc_free
    P:0:0:UI1:test-malloc.c:8
    E:malloc_free:N:1:F:0:D:0.005200
    B:malloc_auto
    P:0:0:UI1:test-malloc.c:17
    E:malloc_auto:N:1:F:0:D:0.004790
    B:zalloc_auto
    P:0:0:UI1:test-malloc.c:35
    P:1:0:UI1:test-malloc.c:36
    P:2:0:UI1:test-malloc.c:26
    E:zalloc_auto:N:3:F:0:D:0.006583

Test Case Destructors
---------------------

You can add test case destructors with `T_add_destructor()`.  They are called
automatically at the test case end before the resource accounting takes place.
Optionally, a registered destructor can be removed before the test case end
with `T_remove_destructor()`.  The `T_destructor` structure of a destructor
must exist after the return from the test case body.  Do not use stack memory
or dynamic memory obtained via `T_malloc()`, `T_calloc()` or `T_zalloc()` for
the `T_destructor` structure.

.. code-block:: c

    void T_add_destructor(T_destructor *destructor,
       void (*destroy)(T_destructor *));

    void T_remove_destructor(T_destructor *destructor);

.. code-block:: c
    :caption: Test Case Destructor Example

    #include <t.h>

    static void
    destroy(T_destructor *dtor)
    {
        (void)dtor;
        T_step(0, "destroy");
    }

    T_TEST_CASE(destructor)
    {
        static T_destructor dtor;

        T_plan(1);
        T_add_destructor(&dtor, destroy);
    }

.. code-block:: none
    :caption: Test Case Destructor Report

    B:destructor
    P:0:0:UI1:test-destructor.c:7
    E:destructor:N:1:F:0:D:0.003714

Test Checks
-----------

A `test check` determines if the actual value presented to the test check meets
its expectation.  The actual value should represent the outcome of a test
action.  If the actual value is all right, then the test check passes,
otherwise the test check fails.  A failed test check does not stop the test
case execution immediately unless the `T_assert_*()` test variant is used.
Each test check increments the test step counter unless the `T_quiet_*()` test
variant is used.  The test step counter is initialized to zero before the test
case begins to execute.  The `T_step_*(step, ...)` test check variants verify
that the test step counter is equal to the planned test step value, otherwise
the test check fails.

Test Check Parameter Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following names for test check parameters are used throughout the test
checks:

step
    The planned test step for this test check.

a
    The actual value to check against an expected value.  It is usually the
    first parameter in all test checks, except in the `T_step_*(step, ...)`
    test check variants, here it is the second parameter.

e
    The expected value of a test check.  This parameter is optional.  Some test
    checks have an implicit expected value.  If present, then this parameter is
    directly after the actual value parameter of the test check.

fmt
    A printf()-like format string.  Floating-point and exotic formats may be
    not supported.

Test Check Condition Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following names for test check conditions are used:

eq
    The actual value must equal the expected value.

ne
    The actual value must not equal the value of the second parameter.

ge
    The actual value must be greater than or equal to the expected value.

gt
    The actual value must be greater than the expected value.

le
    The actual value must be less than or equal to the expected value.

lt
    The actual value must be less than the expected value.

If the actual value satisfies the test check condition, then the test check
passes, otherwise it fails.

Test Check Variant Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `T_quiet_*()` test check variants do not increment the test step counter
and only print a message if the test check fails.  This is helpful in case a
test check appears in a tight loop.

The `T_step_*(step, ...)` test check variants check in addition that the test
step counter is equal to the specified test step value, otherwise the test
check fails.

The `T_assert_*()` and `T_step_assert_*(step, ...)` test check variants stop
the current test case execution if the test check fails.

The following names for test check type variants are used:

ptr
    The test value must be a pointer (`void *`).

mem
    The test value must be a memory area with a specified length.

str
    The test value must be a null byte terminated string.

nstr
    The length of the test value string is limited to a specified maximum.

char
    The test value must be a character (`char`).

schar
    The test value must be a signed character (`signed char`).

uchar
    The test value must be an unsigned character (`unsigned char`).

short
    The test value must be a short integer (`short`).

ushort
    The test value must be an unsigned short integer (`unsigned short`).

int
    The test value must be an integer (`int`).

uint
    The test value must be an unsigned integer (`unsigned int`).

long
    The test value must be a long integer (`long`).

ulong
    The test value must be an unsigned long integer (`unsigned long`).

ll
    The test value must be a long long integer (`long long`).

ull
    The test value must be an unsigned long long integer (`unsigned long long`).

i8
    The test value must be a signed 8-bit integer (`int8_t`).

u8
    The test value must be an unsigned 8-bit integer (`uint8_t`).

i16
    The test value must be a signed 16-bit integer (`int16_t`).

u16
    The test value must be an unsigned 16-bit integer (`uint16_t`).

i32
    The test value must be a signed 32-bit integer (`int32_t`).

u32
    The test value must be an unsigned 32-bit integer (`uint32_t`).

i64
    The test value must be a signed 64-bit integer (`int64_t`).

u64
    The test value must be an unsigned 64-bit integer (`uint64_t`).

iptr
    The test value must be of type `intptr_t`.

uptr
    The test value must be of type `uintptr_t`.

ssz
    The test value must be of type `ssize_t`.

sz
    The test value must be of type `size_t`.

Boolean Expressions
~~~~~~~~~~~~~~~~~~~

The following test checks for boolean expressions are available:

.. code-block:: c

    void T_true(bool a, const char *fmt, ...);
    void T_assert_true(bool a, const char *fmt, ...);
    void T_quiet_true(bool a, const char *fmt, ...);
    void T_step_true(unsigned int step, bool a, const char *fmt, ...);
    void T_step_assert_true(unsigned int step, bool a, const char *fmt, ...);

    void T_false(bool a, const char *fmt, ...);
    void T_assert_false(bool a, const char *fmt, ...);
    void T_quiet_true(bool a, const char *fmt, ...);
    void T_step_true(unsigned int step, bool a, const char *fmt, ...);
    void T_step_assert_true(unsigned int step, bool a, const char *fmt, ...);

The message is only printed in case the test check fails.  The format parameter
is mandatory.

.. code-block:: c
    :caption: Boolean Test Checks Example

    #include <t.h>

    T_TEST_CASE(example)
    {
        T_true(true, "test passes, no message output");
        T_true(false, "test fails");
        T_quiet_true(true, "quiet test passes, no output at all");
        T_quiet_true(false, "quiet test fails");
        T_step_true(2, true, "step test passes, no message output");
        T_step_true(3, false, "step test fails");
        T_assert_false(true, "this is a format %s", "string");
    }

.. code-block:: none
    :caption: Boolean Test Checks Report

    B:example
    P:0:0:UI1:test-example.c:5
    F:1:0:UI1:test-example.c:6:test fails
    F:*:0:UI1:test-example.c:8:quiet test fails
    P:2:0:UI1:test-example.c:9
    F:3:0:UI1:test-example.c:10:step test fails
    F:4:0:UI1:test-example.c:11:this is a format string
    E:example:N:5:F:4

Generic Types
~~~~~~~~~~~~~

The following test checks for data types with an equality (`==`) or inequality
(`!=`) operator are available:

.. code-block:: c

    void T_eq(T a, T e, const char *fmt, ...);
    void T_assert_eq(T a, T e, const char *fmt, ...);
    void T_quiet_eq(T a, T e, const char *fmt, ...);
    void T_step_eq(unsigned int step, T a, T e, const char *fmt, ...);
    void T_step_assert_eq(unsigned int step, T a, T e, const char *fmt, ...);

    void T_ne(T a, T e, const char *fmt, ...);
    void T_assert_ne(T a, T e, const char *fmt, ...);
    void T_quiet_ne(T a, T e, const char *fmt, ...);
    void T_step_ne(unsigned int step, T a, T e, const char *fmt, ...);
    void T_step_assert_ne(unsigned int step, T a, T e, const char *fmt, ...);

The type name `T` specifies an arbitrary type which must support the
corresponding operator.  The message is only printed in case the test check
fails.  The format parameter is mandatory.

Pointers
~~~~~~~~

The following test checks for pointers are available:

.. code-block:: c

    void T_eq_ptr(const void *a, const void *e);
    void T_assert_eq_ptr(const void *a, const void *e);
    void T_quiet_eq_ptr(const void *a, const void *e);
    void T_step_eq_ptr(unsigned int step, const void *a, const void *e);
    void T_step_assert_eq_ptr(unsigned int step, const void *a, const void *e);

    void T_ne_ptr(const void *a, const void *e);
    void T_assert_ne_ptr(const void *a, const void *e);
    void T_quiet_ne_ptr(const void *a, const void *e);
    void T_step_ne_ptr(unsigned int step, const void *a, const void *e);
    void T_step_assert_ne_ptr(unsigned int step, const void *a, const void *e);

    void T_null(const void *a);
    void T_assert_null(const void *a);
    void T_quiet_null(const void *a);
    void T_step_null(unsigned int step, const void *a);
    void T_step_assert_null(unsigned int step, const void *a);

    void T_not_null(const void *a);
    void T_assert_not_null(const void *a);
    void T_quiet_not_null(const void *a);
    void T_step_not_null(unsigned int step, const void *a);
    void T_step_assert_not_null(unsigned int step, const void *a);

An automatically generated message is printed in case the test check fails.

Memory Areas
~~~~~~~~~~~~

The following test checks for memory areas are available:

.. code-block:: c

    void T_eq_mem(const void *a, const void *e, size_t n);
    void T_assert_eq_mem(const void *a, const void *e, size_t n);
    void T_quiet_eq_mem(const void *a, const void *e, size_t n);
    void T_step_eq_mem(unsigned int step, const void *a, const void *e, size_t n);
    void T_step_assert_eq_mem(unsigned int step, const void *a, const void *e, size_t n);

    void T_ne_mem(const void *a, const void *e, size_t n);
    void T_assert_ne_mem(const void *a, const void *e, size_t n);
    void T_quiet_ne_mem(const void *a, const void *e, size_t n);
    void T_step_ne_mem(unsigned int step, const void *a, const void *e, size_t n);
    void T_step_assert_ne_mem(unsigned int step, const void *a, const void *e, size_t n);

The `memcmp()` function is used to compare the memory areas.  An automatically
generated message is printed in case the test check fails.

Strings
~~~~~~~

The following test checks for strings are available:

.. code-block:: c

    void T_eq_str(const char *a, const char *e);
    void T_assert_eq_str(const char *a, const char *e);
    void T_quiet_eq_str(const char *a, const char *e);
    void T_step_eq_str(unsigned int step, const char *a, const char *e);
    void T_step_assert_eq_str(unsigned int step, const char *a, const char *e);

    void T_ne_str(const char *a, const char *e);
    void T_assert_ne_str(const char *a, const char *e);
    void T_quiet_ne_str(const char *a, const char *e);
    void T_step_ne_str(unsigned int step, const char *a, const char *e);
    void T_step_assert_ne_str(unsigned int step, const char *a, const char *e);

    void T_eq_nstr(const char *a, const char *e, size_t n);
    void T_assert_eq_nstr(const char *a, const char *e, size_t n);
    void T_quiet_eq_nstr(const char *a, const char *e, size_t n);
    void T_step_eq_nstr(unsigned int step, const char *a, const char *e, size_t n);
    void T_step_assert_eq_nstr(unsigned int step, const char *a, const char *e, size_t n);

    void T_ne_nstr(const char *a, const char *e, size_t n);
    void T_assert_ne_nstr(const char *a, const char *e, size_t n);
    void T_quiet_ne_nstr(const char *a, const char *e, size_t n);
    void T_step_ne_nstr(unsigned int step, const char *a, const char *e, size_t n);
    void T_step_assert_ne_nstr(unsigned int step, const char *a, const char *e, size_t n);

The `strcmp()` and `strncmp()` functions are used to compare the strings.  An
automatically generated message is printed in case the test check fails.

Characters
~~~~~~~~~~

The following test checks for characters (`char`) are available:

.. code-block:: c

    void T_eq_char(char a, char e);
    void T_assert_eq_char(char a, char e);
    void T_quiet_eq_char(char a, char e);
    void T_step_eq_char(unsigned int step, char a, char e);
    void T_step_assert_eq_char(unsigned int step, char a, char e);

    void T_ne_char(char a, char e);
    void T_assert_ne_char(char a, char e);
    void T_quiet_ne_char(char a, char e);
    void T_step_ne_char(unsigned int step, char a, char e);
    void T_step_assert_ne_char(unsigned int step, char a, char e);

An automatically generated message is printed in case the test check fails.

Integers
~~~~~~~~

The following test checks for integers are available:

.. code-block:: c

    void T_eq_xyz(I a, I e);
    void T_assert_eq_xyz(I a, I e);
    void T_quiet_eq_xyz(I a, I e);
    void T_step_eq_xyz(unsigned int step, I a, I e);
    void T_step_assert_eq_xyz(unsigned int step, I a, I e);

    void T_ne_xyz(I a, I e);
    void T_assert_ne_xyz(I a, I e);
    void T_quiet_ne_xyz(I a, I e);
    void T_step_ne_xyz(unsigned int step, I a, I e);
    void T_step_assert_ne_xyz(unsigned int step, I a, I e);

    void T_ge_xyz(I a, I e);
    void T_assert_ge_xyz(I a, I e);
    void T_quiet_ge_xyz(I a, I e);
    void T_step_ge_xyz(unsigned int step, I a, I e);
    void T_step_assert_ge_xyz(unsigned int step, I a, I e);

    void T_gt_xyz(I a, I e);
    void T_assert_gt_xyz(I a, I e);
    void T_quiet_gt_xyz(I a, I e);
    void T_step_gt_xyz(unsigned int step, I a, I e);
    void T_step_assert_gt_xyz(unsigned int step, I a, I e);

    void T_le_xyz(I a, I e);
    void T_assert_le_xyz(I a, I e);
    void T_quiet_le_xyz(I a, I e);
    void T_step_le_xyz(unsigned int step, I a, I e);
    void T_step_assert_le_xyz(unsigned int step, I a, I e);

    void T_lt_xyz(I a, I e);
    void T_assert_lt_xyz(I a, I e);
    void T_quiet_lt_xyz(I a, I e);
    void T_step_lt_xyz(unsigned int step, I a, I e);
    void T_step_assert_lt_xyz(unsigned int step, I a, I e);

The type variant `xyz` must be `schar`, `uchar`, `short`, `ushort`, `int`,
`uint`, `long`, `ulong`, `ll`, `ull`, `i8`, `u8`, `i16`, `u16`, `i32`, `u32`,
`i64`, `u64`, `iptr`, `uptr`, `ssz`, or `sz`.

The type name `I` must be compatible to the type variant.

An automatically generated message is printed in case the test check fails.

RTEMS Status Codes
~~~~~~~~~~~~~~~~~~

The following test checks for RTEMS status codes are available:

.. code-block:: c

    void T_rsc(rtems_status_code a, rtems_status_code e);
    void T_assert_rsc(rtems_status_code a, rtems_status_code e);
    void T_quiet_rsc(rtems_status_code a, rtems_status_code e);
    void T_step_rsc(unsigned int step, rtems_status_code a, rtems_status_code e);
    void T_step_assert_rsc(unsigned int step, rtems_status_code a, rtems_status_code e);

    void T_rsc_success(rtems_status_code a);
    void T_assert_rsc_success(rtems_status_code a);
    void T_quiet_rsc_success(rtems_status_code a);
    void T_step_rsc_success(unsigned int step, rtems_status_code a);
    void T_step_assert_rsc_success(unsigned int step, rtems_status_code a);

An automatically generated message is printed in case the test check fails.

POSIX Error Numbers
~~~~~~~~~~~~~~~~~~~

The following test checks for POSIX error numbers are available:

.. code-block:: c

    void T_eno(int a, int e);
    void T_assert_eno(int a, int e);
    void T_quiet_eno(int a, int e);
    void T_step_eno(unsigned int step, int a, int e);
    void T_step_assert_eno(unsigned int step, int a, int e);

    void T_eno_success(int a);
    void T_assert_eno_success(int a);
    void T_quiet_eno_success(int a);
    void T_step_eno_success(unsigned int step, int a);
    void T_step_assert_eno_success(unsigned int step, int a);

The actual and expected value must be a POSIX error number, e.g. EINVAL,
ENOMEM, etc.  An automatically generated message is printed in case the test
check fails.

POSIX Status Codes
~~~~~~~~~~~~~~~~~~

The following test checks for POSIX status codes are available:

.. code-block:: c

    void T_psx_error(int a, int eno);
    void T_assert_psx_error(int a, int eno);
    void T_quiet_psx_error(int a, int eno);
    void T_step_psx_error(unsigned int step, int a, int eno);
    void T_step_assert_psx_error(unsigned int step, int a, int eno);

    void T_psx_success(int a);
    void T_assert_psx_success(int a);
    void T_quiet_psx_success(int a);
    void T_step_psx_success(unsigned int step, int a);
    void T_step_assert_psx_success(unsigned int step, int a);

The `eno` value must be a POSIX error number, e.g. EINVAL, ENOMEM, etc.  An
actual value of zero indicates success.  An actual value of minus one indicates
an error.  An automatically generated message is printed in case the test check
fails.

.. code-block:: c
    :caption: POSIX Status Code Example

    #include <t.h>

    #include <sys/stat.h>
    #include <errno.h>

    T_TEST_CASE(stat)
    {
        struct stat st;
        int status;

        errno = 0;
        status = stat("foobar", &st);
        T_psx_error(status, ENOENT);
    }

.. code-block:: none
    :caption: POSIX Status Code Report

    B:stat
    P:0:0:UI1:test-psx.c:13
    E:stat:N:1:F:0

Log Messages and Formatted Output
---------------------------------

You can print log messages with the `T_log()` function:

.. code-block:: c

    void T_log(T_verbosity verbosity, char const *fmt, ...);

A newline is automatically added to terminate the log message line.

.. code-block:: c
    :caption: Log Message Example

    #include <t.h>

    T_TEST_CASE(log)
    {
        T_log(T_NORMAL, "a log message %i, %i, %i", 1, 2, 3);
        T_set_verbosity(T_QUIET);
        T_log(T_NORMAL, "not verbose enough");
    }

.. code-block:: none
    :caption: Log Message Report

    B:log
    L:a log message 1, 2, 3
    E:log:N:0:F:0

You can use the following functions to print formatted output:

.. code-block:: c

    int T_printf(char const *, ...);

    int T_vprintf(char const *, va_list);

    int T_snprintf(char *, size_t, const char *, ...);

In contrast to the corresponding standard C library functions, floating-point
and exotic formats may be not supported.  On some architectures supported by
RTEMS, floating-point operations are only supported in special tasks and may be
forbidden in interrupt context.  The formatted output functions provided by the
test framework work in every context.

Time Services
-------------

The test framework provides two unsigned integer types for time values.  The
`T_ticks` unsigned integer type is used by the `T_tick()` function which
measures time using the highest frequency counter available on the platform.
It should only be used to measure small time intervals.  The `T_time` unsigned
integer type is used by the `T_now()` function which returns the current
monotonic clock value of the platform, e.g. `CLOCK_MONOTONIC`.

.. code-block:: c

   T_ticks T_tick(void);

   T_time T_now(void);

The reference time point for these two clocks is unspecified.  You can obtain
the test case begin time with the `T_case_begin_time()` function.

.. code-block:: c

   T_time T_case_begin_time(void);

You can convert time into ticks with the `T_time_to_ticks()` function and vice
versa with the `T_ticks_to_time()` function.

.. code-block:: c

    T_time T_ticks_to_time(T_ticks ticks);

    T_ticks T_time_to_ticks(T_time time);

You can convert seconds and nanoseconds values into a combined time value with
the `T_seconds_and_nanoseconds_to_time()` function.  You can convert a time
value into separate seconds and nanoseconds values with the
`T_time_to_seconds_and_nanoseconds()` function.

.. code-block:: c

    T_time T_seconds_and_nanoseconds_to_time(uint32_t s, uint32_t ns);

    void T_time_to_seconds_and_nanoseconds(T_time time, uint32_t *s, uint32_t *ns);

You can convert a time value into a string represention.  The time unit of the
string representation is seconds.  The precision of the string represention may
be nanoseconds, microseconds, milliseconds, or seconds.  You have to provide a
buffer for the string (`T_time_string`).

.. code-block:: c

    const char *T_time_to_string_ns(T_time time, T_time_string buffer);

    const char *T_time_to_string_us(T_time time, T_time_string buffer);

    const char *T_time_to_string_ms(T_time time, T_time_string buffer);

    const char *T_time_to_string_s(T_time time, T_time_string buffer);

.. code-block:: c
    :caption: Time String Example

    #include <t.h>

    T_TEST_CASE(time_to_string)
    {
        T_time_string ts;
        T_time t;
        uint32_t s;
        uint32_t ns;

        t = T_seconds_and_nanoseconds_to_time(0, 123456789);
        T_eq_str(T_time_to_string_ns(t, ts), "0.123456789");
        T_eq_str(T_time_to_string_us(t, ts), "0.123456");
        T_eq_str(T_time_to_string_ms(t, ts), "0.123");
        T_eq_str(T_time_to_string_s(t, ts), "0");

        T_time_to_seconds_and_nanoseconds(t, &s, &ns);
        T_eq_u32(s, 0);
        T_eq_u32(ns, 123456789);
    }

.. code-block:: none
    :caption: Time String Report

    B:time_to_string
    P:0:0:UI1:test-time.c:11
    P:1:0:UI1:test-time.c:12
    P:2:0:UI1:test-time.c:13
    P:3:0:UI1:test-time.c:14
    P:4:0:UI1:test-time.c:17
    P:5:0:UI1:test-time.c:18
    E:time_to_string:N:6:F:0:D:0.005250

You can convert a tick value into a string represention.  The time unit of the
string representation is seconds.  The precision of the string represention may
be nanoseconds, microseconds, milliseconds, or seconds.  You have to provide a
buffer for the string (`T_time_string`).

.. code-block:: c

    const char *T_ticks_to_string_ns(T_ticks ticks, T_time_string buffer);

    const char *T_ticks_to_string_us(T_ticks ticks, T_time_string buffer);

    const char *T_ticks_to_string_ms(T_ticks ticks, T_time_string buffer);

    const char *T_ticks_to_string_s(T_ticks ticks, T_time_string buffer);

Code Runtime Measurements
-------------------------

You can measure the runtime of code fragments in several execution environment
variants with the `T_measure_runtime()` function.  This function needs a
context which must be created with the `T_measure_runtime_create()` function.
The context is automatically destroyed after the test case execution.

.. code-block:: c

    typedef struct {
        size_t sample_count;
    } T_measure_runtime_config;

    typedef struct {
        const char *name;
        int flags;
        void (*setup)(void *arg);
        void (*body)(void *arg);
        bool (*teardown)(void *arg, T_ticks *delta, uint32_t tic, uint32_t toc,
            unsigned int retry);
        void *arg;
    } T_measure_runtime_request;

    T_measure_runtime_context *T_measure_runtime_create(
        const T_measure_runtime_config *config);

    void T_measure_runtime(T_measure_runtime_context *ctx,
        const T_measure_runtime_request *request);

The runtime measurement is performed for the `body` request handler of the
measurement request (`T_measure_runtime_request`).  The optional `setup`
request handler is called before each invocation of the `body` request handler.
The optional `teardown` request handler is called after each invocation of the
`body` request handler.  It has several parameters and a return status.  If it
returns true, then this measurement sample value is recorded, otherwise the
measurement is retried.  The `delta` parameter is the current measurement
sample value.  It can be altered by the `teardown` request handler.  The `tic`
and `toc` parameters are the system tick values before and after the request
body invocation.  The `retry` parameter is the current retry counter.  The
runtime of the operational `setup` and `teardown` request handlers is not
measured.

You can control some aspects of the measurement through the request flags (use
zero for the default):

T_MEASURE_RUNTIME_ALLOW_CLOCK_ISR
    Allow clock interrupts during the measurement.  By default, measurements
    during which a clock interrupt happened are discarded unless it happens two
    times in a row.

T_MEASURE_RUNTIME_REPORT_SAMPLES
    Report all measurement samples.

T_MEASURE_RUNTIME_DISABLE_VALID_CACHE
    Disable the `ValidCache` execution environment variant.

T_MEASURE_RUNTIME_DISABLE_HOT_CACHE
    Disable the `HotCache` execution environment variant.

T_MEASURE_RUNTIME_DISABLE_DIRTY_CACHE
    Disable the `DirtyCache` execution environment variant.

T_MEASURE_RUNTIME_DISABLE_MINOR_LOAD
    Disable the `Load` execution environment variants with a load worker count
    less than the processor count.

T_MEASURE_RUNTIME_DISABLE_MAX_LOAD
    Disable the `Load` execution environment variant with a load worker count
    equal to the processor count.

The execution environment variants (`M:V`) are:

ValidCache
    Before the `body` request handler is invoked a memory area with twice the
    size of the outer-most data cache is completely read.  This fills the data
    cache with valid cache lines which are unrelated to the `body` request
    handler.

    You can disable this variant with the
    `T_MEASURE_RUNTIME_DISABLE_VALID_CACHE` request flag.

HotCache
    Before the `body` request handler is invoked the `body` request handler is
    called without measuring the runtime.  The aim is to load all data used by
    the `body` request handler to the cache.

    You can disable this variant with the
    `T_MEASURE_RUNTIME_DISABLE_HOT_CACHE` request flag.

DirtyCache
    Before the `body` request handler is invoked a memory area with twice the
    size of the outer-most data cache is completely written with new data.
    This should produce a data cache with dirty cache lines which are unrelated
    to the `body` request handler.  In addition, the entire instruction cache
    is invalidated.

    You can disable this variant with the
    `T_MEASURE_RUNTIME_DISABLE_DIRTY_CACHE` request flag.

Load
    This variant tries to get close to worst-case conditions.  The cache is set
    up according to the `DirtyCache` variant.  In addition, other processors
    try to fully load the memory system.  The load is produced through writes
    to a memory area with twice the size of the outer-most data cache.  The
    load variant is performed multiple times with a different set of active
    load worker threads (`M:L`).  The active workers range from one up to the
    processor count.

    You can disable these variants with the
    `T_MEASURE_RUNTIME_DISABLE_MINOR_LOAD` and
    `T_MEASURE_RUNTIME_DISABLE_MAX_LOAD` request flags.

    On SPARC, the `body` request handler is called with a register window
    setting so that window overflow traps will occur in the next level function
    call.

Each execution in an environment variant produces a sample set of `body`
request handler runtime measurements.  The minimum (`M:MI`), first quartile
(`M:Q1`), median (`M:Q2`), third quartile (`M:Q3`), maximum (`M:MX`), median
absolute deviation (`M:MAD`), and the sum of the sample values (`M:D`) is
reported.

.. code-block:: c
    :caption: Code Runtime Measurement Example

    #include <t.h>

    static void
    empty(void *arg)
    {
        (void)arg;
    }

    T_TEST_CASE(measure_empty)
    {
        static const T_measure_runtime_config config = {
            .sample_count = 1024
        };
        T_measure_runtime_context *ctx;
        T_measure_runtime_request req;

        ctx = T_measure_runtime_create(&config);
        T_assert_not_null(ctx);

        memset(&req, 0, sizeof(req));
        req.name = "Empty";
        req.body = empty;
        T_measure_runtime(ctx, &req);
    }

.. code-block:: none
    :caption: Code Runtime Measurement Report

    B:measure_empty
    P:0:0:UI1:test-rtems-measure.c:18
    M:B:Empty
    M:V:ValidCache
    M:N:1024
    M:MI:0.000000000
    M:Q1:0.000000000
    M:Q2:0.000000000
    M:Q3:0.000000000
    M:MX:0.000000009
    M:MAD:0.000000000
    M:D:0.000000485
    M:E:Empty:D:0.208984183
    M:B:Empty
    M:V:HotCache
    M:N:1024
    M:MI:0.000000003
    M:Q1:0.000000003
    M:Q2:0.000000003
    M:Q3:0.000000003
    M:MX:0.000000006
    M:MAD:0.000000000
    M:D:0.000002626
    M:E:Empty:D:0.000017046
    M:B:Empty
    M:V:DirtyCache
    M:N:1024
    M:MI:0.000000007
    M:Q1:0.000000007
    M:Q2:0.000000007
    M:Q3:0.000000008
    M:MX:0.000000559
    M:MAD:0.000000000
    M:D:0.000033244
    M:E:Empty:D:1.887834875
    M:B:Empty
    M:V:Load
    M:L:1
    M:N:1024
    M:MI:0.000000000
    M:Q1:0.000000002
    M:Q2:0.000000002
    M:Q3:0.000000003
    M:MX:0.000000288
    M:MAD:0.000000000
    M:D:0.000002421
    M:E:Empty:D:0.001798809
    [... 22 more load variants ...]
    M:E:Empty:D:0.021252583
    M:B:Empty
    M:V:Load
    M:L:24
    M:N:1024
    M:MI:0.000000001
    M:Q1:0.000000002
    M:Q2:0.000000002
    M:Q3:0.000000003
    M:MX:0.000001183
    M:MAD:0.000000000
    M:D:0.000003406
    M:E:Empty:D:0.015188063
    E:measure_empty:N:1:F:0:D:14.284869


Test Runner
-----------

You can call the `T_main()` function to run all registered test cases.

.. code-block:: c

    int T_main(const T_config *config);

The `T_main()` function returns 0 if all test cases passed, otherwise it
returns 1.  Concurrent execution of the `T_main()` function is undefined
behaviour.

You can ask if you execute within the context of the test runner with the
`T_is_runner()` function:

.. code-block:: c

    bool T_is_runner(void);

It returns `true` if you execute within the context of the test runner (the
context which executes for example `T_main()`).  Otherwise it returns `false`,
for example if you execute in another task, in interrupt context, nobody
executes `T_main()`, or during system initialization on another processor.

On RTEMS, you have to register the test cases with the `T_register()` function
before you call `T_main()`.  This makes it possible to run low level tests, for
example without the operating system directly in `boot_card()` or during device
driver initialization.  On other platforms, the `T_register()` is a no
operation.

.. code-block:: c

    void T_register(void);

You can run test cases also individually.  Use `T_run_initialize()` to
initialize the test runner.  Call `T_run_all()` to run all or `T_run_by_name()`
to run specific registered test cases.  Call `T_case_begin()` to begin a
freestanding test case and call `T_case_end()` to finish it.  Finally,
call `T_run_finalize()`.

.. code-block:: c

    void T_run_initialize(const T_config *config);

    void T_run_all(void);

    void T_run_by_name(const char *name);

    void T_case_begin(const char *name, const T_fixture *fixture);

    void T_case_end(void);

    bool T_run_finalize(void);

The `T_run_finalize()` function returns `true` if all test cases passed,
otherwise it returns `false`.  Concurrent execution of the runner functions
(including `T_main()`) is undefined behaviour.  The test suite configuration
must be persistent throughout the test run.

.. code-block:: c

    typedef enum {
        T_EVENT_RUN_INITIALIZE,
        T_EVENT_CASE_EARLY,
        T_EVENT_CASE_BEGIN,
        T_EVENT_CASE_END,
        T_EVENT_CASE_LATE,
        T_EVENT_RUN_FINALIZE
    } T_event;

    typedef void (*T_action)(T_event, const char *);

    typedef void (*T_putchar)(int, void *);

    typedef struct {
        const char *name;
        T_putchar putchar;
        void *putchar_arg;
        T_verbosity verbosity;
        T_time (*now)(void);
        size_t action_count;
        const T_action *actions;
    } T_config;

With the test suite configuration you can specifiy the test suite name, the put
character handler used the output the test report, the initial verbosity, the
monotonic time provider and an optional set of test suite actions.  The test
suite actions are called with the test suite name for test suite run events
(`T_EVENT_RUN_INITIALIZE` and `T_EVENT_RUN_FINALIZE`) and the test case name
for the test case events (`T_EVENT_CASE_EARLY`, `T_EVENT_CASE_BEGIN`,
`T_EVENT_CASE_END` and `T_EVENT_CASE_LATE`).

Test Verbosity
--------------

Three test verbosity levels are defined:

T_QUIET
    Only the test suite begin, system, test case end, and test suite end lines
    are printed.

T_NORMAL
    Prints everything except passed test lines.

T_VERBOSE
    Prints everything.

The test verbosity level can be set within the scope of one test case with the
`T_set_verbosity()` function:

.. code-block:: c

    T_verbosity T_set_verbosity(T_verbosity new_verbosity);

The function returns the previous verbosity.  After the test case, the
configured verbosity is automatically restored.

An example with `T_QUIET` verbosity:

    .. code-block:: none

        A:xyz
        S:Platform:RTEMS
        [...]
        E:a:N:2:F:1
        E:b:N:0:F:1
        E:c:N:1:F:1
        E:d:N:6:F:0
        Z:xyz:C:4:N:9:F:3

The same example with `T_NORMAL` verbosity:

    .. code-block:: none

        A:xyz
        S:Platform:RTEMS
        [...]
        B:a
        F:1:0:UI1:test-verbosity.c:6:test fails
        E:a:N:2:F:1
        B:b
        F:*:0:UI1:test-verbosity.c:12:quiet test fails
        E:b:N:0:F:1
        B:c
        F:0:0:UI1:test-verbosity.c:17:this is a format string
        E:c:N:1:F:1
        B:d
        E:d:N:6:F:0
        Z:xyz:C:4:N:9:F:3

The same example with `T_VERBOSE` verbosity:

    .. code-block:: none

        A:xyz
        S:Platform:RTEMS
        [...]
        B:a
        P:0:0:UI1:test-verbosity.c:5
        F:1:0:UI1:test-verbosity.c:6:test fails
        E:a:N:2:F:1
        B:b
        F:*:0:UI1:test-verbosity.c:12:quiet test fails
        E:b:N:0:F:1
        B:c
        F:0:0:UI1:test-verbosity.c:17:this is a format string
        E:c:N:1:F:1
        B:d
        P:0:0:UI1:test-verbosity.c:22
        P:1:0:UI1:test-verbosity.c:23
        P:2:0:UI1:test-verbosity.c:24
        P:3:0:UI1:test-verbosity.c:25
        P:4:0:UI1:test-verbosity.c:26
        P:5:0:UI1:test-verbosity.c:27
        E:d:N:6:F:0
        Z:xyz:C:4:N:9:F:3

.. _RTEMSTestFrameworkTestReporting:

Test Reporting
--------------

The test reporting is line based which should be easy to parse with a simple
state machine. Each line consists of a set of fields separated by colon
characters (`:`).  The first character of the line determines the line format:

A
    A test suite begin line.  It has the format:

    **A:<TestSuite>**

    A description of the field follows:

    <TestSuite>
        The test suite name.  Must not contain colon characters (`:`).

S
    A test suite system line.  It has the format:

    **S:<Key>:<Value>**

    A description of the fields follows:

    <Key>
        A key string.  Must not contain colon characters (`:`).

    <Value>
        An arbitrary key value string.  May contain colon characters (`:`).

B
    A test case begin line.  It has the format:

    **B:<TestCase>**

    A description of the field follows:

    <TestCase>
        A test case name.  Must not contain colon characters (`:`).

P
    A test pass line.  It has the format:

    **P:<Step>:<Processor>:<Task>:<File>:<Line>**

    A description of the fields follows:

    <Step>
        Each non-quiet test has a unique test step counter value in each test case
        execution.  The test step counter is set to zero before the test case
        executes.  For quiet test checks, there is no associated test step and the
        character `*` instead of an integer is used to indicate this.

    <Processor>
        The processor index of the processor which executed at least one
        instruction of the corresponding test.

    <Task>
        The name of the task which executed the corresponding test if the test
        executed in task context.  The name `ISR` indicates that the test executed
        in interrupt context.  The name `?` indicates that the test executed in an
        arbitrary context with no valid executing task.

    <File>
        The name of the source file which contains the corresponding test.  A
        source file of `*` indicates that no test source file is associated
        with the test, e.g. it was produced by the test framework itself.

    <Line>
        The line of the test statement in the source file which contains the
        corresponding test.  A line number of `*` indicates that no test source
        file is associated with the test, e.g. it was produced by the test
        framework itself.

F
    A test failure line.  It has the format:

    **F:<Step>:<Processor>:<Task>:<File>:<Line>:<Message>**

    A description of the fields follows:

    <Step> <Processor> <Task> <File> <Line>
        See above **P** line.

    <Message>
        An arbitrary message string.  May contain colon characters (`:`).

L
    A log message line.  It has the format:

    **L:<Message>**

    A description of the field follows:

    <Message>
        An arbitrary message string.  May contain colon characters (`:`).

E
    A test case end line.  It has the format:

    **E:<TestCase>:N:<Steps>:F:<Failures>:D:<Duration>**

    A description of the fields follows:

    <TestCase>
        A test case name.  Must not contain colon characters (`:`).

    <Steps>
        The final test step counter of a test case.  Quiet test checks produce
        no test steps.

    <Failures>
        The count of failed test checks of a test case.

    <Duration>
        The test case duration in seconds.

Z
    A test suite end line. It has the format:

    **Z:<TestSuite>:C:<TestCases>:N:<OverallSteps>:F:<OverallFailures>:D:<Duration>**

    A description of the fields follows:

    <TestSuite>
        The test suite name.  Must not contain colon characters (`:`).

    <TestCases>
        The count of test cases in the test suite.

    <OverallSteps>
        The overall count of test steps in the test suite.

    <OverallFailures>
        The overall count of failed test cases in the test suite.

    <Duration>
        The test suite duration in seconds.

Y
    Auxiliary information line.  Issued after the test suite end. It has the format:

    **Y:ReportHash:SHA256:<Hash>**

    A description of the fields follows:

    <Hash>
        The SHA256 hash value of the test suite report from the begin to the
        end of the test suite.

M
    A code runtime measurement line.  It has the formats:

    **M:B:<Name>**

    **M:V:<Variant>**

    **M:L:<Load>**

    **M:N:<SampleCount>**

    **M:S:<Count>:<Value>**

    **M:MI:<Minimum>**

    **M:Q1:<FirstQuartile>**

    **M:Q2:<Median>**

    **M:Q3:<ThirdQuartile>**

    **M:MX:<Maximum>**

    **M:MAD:<MedianAbsoluteDeviation>**

    **M:D:<SumOfSampleValues>**

    **M:E:<Name>:D:<Duration>**

    A description of the fields follows:

    <Name>
        A code runtime measurement name.  Must not contain colon characters
        (`:`).

    <Variant>
        The execution variant which is one of **ValidCache**, **HotCache**,
        **DirtyCache**, or **Load**.

    <Load>
        The active load workers count which ranges from one to the processor
        count.

    <SampleCount>
        The sample count as defined by the runtime measurement configuration.

    <Count>
        The count of samples with the same value.

    <Value>
        A sample value in seconds.

    <Minimum>
        The minimum of the sample set in seconds.

    <FirstQuartile>
        The first quartile of the sample set in seconds.

    <Median>
        The median of the sample set in seconds.

    <ThirdQuartile>
        The third quartile of the sample set in seconds.

    <Maximum>
        The maximum of the sample set in seconds.

    <MedianAbsoluteDeviation>
        The median absolute deviation of the sample set in seconds.

    <SumOfSampleValues>
        The sum of all sample values of the sample set in seconds.

    <Duration>
        The runtime measurement duration in seconds.  It includes time to set
        up the execution environment variant.

.. code-block:: none
    :caption: Example Test Report

    A:xyz
    S:Platform:RTEMS
    S:Compiler:7.4.0 20181206 (RTEMS 5, RSB e0aec65182449a4e22b820e773087636edaf5b32, Newlib 1d35a003f)
    S:Version:5.0.0.820977c5af17c1ca2f79800d64bd87ce70a24c68
    S:BSP:erc32
    S:RTEMS_DEBUG:1
    S:RTEMS_MULTIPROCESSING:0
    S:RTEMS_POSIX_API:1
    S:RTEMS_PROFILING:0
    S:RTEMS_SMP:1
    B:timer
    P:0:0:UI1:test-rtems.c:26
    P:1:0:UI1:test-rtems.c:29
    P:2:0:UI1:test-rtems.c:33
    P:3:0:ISR:test-rtems.c:14
    P:4:0:ISR:test-rtems.c:15
    P:5:0:UI1:test-rtems.c:38
    P:6:0:UI1:test-rtems.c:39
    P:7:0:UI1:test-rtems.c:42
    E:timer:N:8:F:0:D:0.019373
    B:rsc_success
    P:0:0:UI1:test-rtems.c:59
    F:1:0:UI1:test-rtems.c:60:RTEMS_INVALID_NUMBER == RTEMS_SUCCESSFUL
    F:*:0:UI1:test-rtems.c:62:RTEMS_INVALID_NUMBER == RTEMS_SUCCESSFUL
    P:2:0:UI1:test-rtems.c:63
    F:3:0:UI1:test-rtems.c:64:RTEMS_INVALID_NUMBER == RTEMS_SUCCESSFUL
    E:rsc_success:N:4:F:3:D:0.011128
    B:rsc
    P:0:0:UI1:test-rtems.c:48
    F:1:0:UI1:test-rtems.c:49:RTEMS_INVALID_NUMBER == RTEMS_INVALID_ID
    F:*:0:UI1:test-rtems.c:51:RTEMS_INVALID_NUMBER == RTEMS_INVALID_ID
    P:2:0:UI1:test-rtems.c:52
    F:3:0:UI1:test-rtems.c:53:RTEMS_INVALID_NUMBER == RTEMS_INVALID_ID
    E:rsc:N:4:F:3:D:0.011083
    Z:xyz:C:3:N:16:F:6:D:0.047201
    Y:ReportHash:SHA256:e5857c520dd9c9b7c15d4a76d78c21ccc46619c30a869ecd11bbcd1885155e0b

Test Report Validation
----------------------

You can add the `T_report_hash_sha256()` test suite action to the test suite
configuration to generate and report the SHA256 hash value of the test suite
report.  The hash value covers everything reported by the test suite run from
the begin to the end.  This can be used to check that the report generated on
the target is identical to the report received on the report consumer side.
The hash value is reported after the end of test suite line (`Z`) as auxiliary
information in a `Y` line.  Consumers may have to reverse a `\\n` to `\\r\\n`
conversion before the hash is calculated.  Such a conversion could be performed
by a particular put character handler provided by the test suite configuration.

Supported Platforms
-------------------

The framework runs on FreeBSD, MSYS2, Linux and RTEMS.

Test Framework Requirements for RTEMS
=====================================

The requirements on a test framework suitable for RTEMS are:

License Requirements
--------------------

TF.License.Permissive
    The test framework shall have a permissive open source license such as
    BSD-2-Clause.

Portability Requirements
------------------------

TF.Portability
    The test framework shall be portable.

    TF.Portability.RTEMS
        The test framework shall run on RTEMS.

    TF.Portability.POSIX
        The test framework shall be portable to POSIX compatible operating
        systems.  This allows to run test cases of standard C/POSIX/etc. APIs
        on multiple platforms.

        TF.Portability.POSIX.Linux
            The test framework shall run on Linux.

        TF.Portability.POSIX.FreeBSD
            The test framework shall run on FreeBSD.

    TF.Portability.C11
        The test framework shall be written in C11.

    TF.Portability.Static
        Test framework shall not use dynamic memory for basic services.

    TF.Portability.Small
        The test framework shall be small enough to support low-end platforms
        (e.g. 64KiB of RAM/ROM should be sufficient to test the architecture
        port, e.g. no complex stuff such as file systems, etc.).

    TF.Portability.Small.LinkTimeConfiguration
        The test framework shall be configured at link-time.

    TF.Portability.Small.Modular
        The test framework shall be modular so that only necessary parts end up
        in the final executable.

    TF.Portability.Small.Memory
        The test framework shall not aggregate data during test case executions.

Reporting Requirements
----------------------

TF.Reporting
    Test results shall be reported.

    TF.Reporting.Verbosity
        The test report verbosity shall be configurable.  This allows different
        test run scenarios, e.g. regression test runs, full test runs with test
        report verification against the planned test output.

    TF.Reporting.Verification
        It shall be possible to use regular expressions to verify test reports
        line by line.

    TF.Reporting.Compact
        Test output shall be compact to avoid long test runs on platforms with
        a slow output device, e.g. 9600 Baud UART.

    TF.Reporting.PutChar
        A simple output one character function provided by the platform shall be
        sufficient to report the test results.

    TF.Reporting.NonBlocking
        The ouptut functions shall be non-blocking.

    TF.Reporting.Printf
        The test framework shall provide printf()-like output functions.

        TF.Reporting.Printf.WithFP
            There shall be a printf()-like output function with floating point
            support.

        TF.Reporting.Printf.WithoutFP
            There shall be a printf()-like output function without floating
            point support on RTEMS.

    TF.Reporting.Platform
        The test platform shall be reported.

        TF.Reporting.Platform.RTEMS.Git
            The RTEMS source Git commit shall be reported.

        TF.Reporting.Platform.RTEMS.Arch
            The RTEMS architecture name shall be reported.

        TF.Reporting.Platform.RTEMS.BSP
            The RTEMS BSP name shall be reported.

        TF.Reporting.Platform.RTEMS.Tools
            The RTEMS tool chain version shall be reported.

        TF.Reporting.Platform.RTEMS.Config.Debug
            The shall be reported if RTEMS_DEBUG is defined.

        TF.Reporting.Platform.RTEMS.Config.Multiprocessing
            The shall be reported if RTEMS_MULTIPROCESSING is defined.

        TF.Reporting.Platform.RTEMS.Config.POSIX
            The shall be reported if RTEMS_POSIX_API is defined.

        TF.Reporting.Platform.RTEMS.Config.Profiling
            The shall be reported if RTEMS_PROFILING is defined.

        TF.Reporting.Platform.RTEMS.Config.SMP
            The shall be reported if RTEMS_SMP is defined.

    TF.Reporting.TestCase
        The test cases shall be reported.

        TF.Reporting.TestCase.Begin
            The test case begin shall be reported.

        TF.Reporting.TestCase.End
            The test case end shall be reported.

        TF.Reporting.TestCase.Tests
            The count of test checks of the test case shall be reported.

        TF.Reporting.TestCase.Failures
            The count of failed test checks of the test case shall be reported.

        TF.Reporting.TestCase.Timing
            Test case timing shall be reported.

        TF.Reporting.TestCase.Tracing
            Automatic tracing and reporting of thread context switches and
            interrupt service routines shall be optionally performed.

Environment Requirements
------------------------

TF.Environment
    The test framework shall support all environment conditions of the platform.

    TF.Environment.SystemStart
        The test framework shall run during early stages of the system start,
        e.g. valid stack pointer, initialized data and cleared BSS, nothing
        more.

    TF.Environment.BeforeDeviceDrivers
        The test framework shall run before device drivers are initialized.

    TF.Environment.InterruptContext
        The test framework shall support test case code in interrupt context.

Usability Requirements
----------------------

TF.Usability
    The test framework shall be easy to use.

    TF.Usability.TestCase
        It shall be possible to write test cases.

        TF.Usability.TestCase.Independence
            It shall be possible to write test cases in modules independent of
            the test runner.

        TF.Usability.TestCase.AutomaticRegistration
            Test cases shall be registered automatically, e.g. via constructors
            or linker sets.

        TF.Usability.TestCase.Order
            It shall be possible to sort the registered test cases (e.g. random,
            by name) before they are executed.

        TF.Usability.TestCase.Resources
            It shall be possible to use resources with a life time restricted to
            the test case.

            TF.Usability.TestCase.Resources.Memory
                It shall be possible to dynamically allocate memory which is
                automatically freed once the test case completed.

            TF.Usability.TestCase.Resources.File
                It shall be possible to create a file which is automatically
                unlinked once the test case completed.

            TF.Usability.TestCase.Resources.Directory
                It shall be possible to create a directory which is automatically
                removed once the test case completed.

            TF.Usability.TestCase.Resources.FileDescriptor
                It shall be possible to open a file descriptor which is
                automatically closed once the test case completed.

        TF.Usability.TestCase.Fixture
            It shall be possible to use a text fixture for test cases.

            TF.Usability.TestCase.Fixture.SetUp
                It shall be possible to provide a set up handler for each test case.

            TF.Usability.TestCase.Fixture.TearDown
                It shall be possible to provide a tear down handler for each test
                case.

        TF.Usability.TestCase.Context
            The test case context shall be verified a certain points.

            TF.Usability.TestCase.Context.VerifyAtEnd
                After a test case exection it shall be verified that the context
                is equal to the context at the test case begin.  This helps to
                ensure that test cases are independent of each other.

            TF.Usability.TestCase.Context.VerifyThread
                The test framework shall provide a function to ensure that the
                test case code executes in normal thread context.  This helps
                to ensure that operating system service calls return to a sane
                context.

            TF.Usability.TestCase.Context.Configurable
                The context verified in test case shall be configurable at link-time.

            TF.Usability.TestCase.Context.ThreadDispatchDisableLevel
                It shall be possible to verify the thread dispatch disable level.

            TF.Usability.TestCase.Context.ISRNestLevel
                It shall be possible to verify the ISR nest level.

            TF.Usability.TestCase.Context.InterruptLevel
                It shall be possible to verify the interrupt level (interrupts
                enabled/disabled).

            TF.Usability.TestCase.Context.Workspace
                It shall be possible to verify the workspace.

            TF.Usability.TestCase.Context.Heap
                It shall be possible to verify the heap.

            TF.Usability.TestCase.Context.OpenFileDescriptors
                It shall be possible to verify the open file descriptors.

            TF.Usability.TestCase.Context.Classic
                It shall be possible to verify Classic API objects.

                TF.Usability.TestCase.Context.Classic.Barrier
                    It shall be possible to verify Classic API Barrier objects.

                TF.Usability.TestCase.Context.Classic.Extensions
                    It shall be possible to verify Classic API User Extensions
                    objects.

                TF.Usability.TestCase.Context.Classic.MessageQueues
                    It shall be possible to verify Classic API Message Queue
                    objects.

                TF.Usability.TestCase.Context.Classic.Partitions
                    It shall be possible to verify Classic API Partition objects.

                TF.Usability.TestCase.Context.Classic.Periods
                    It shall be possible to verify Classic API Rate Monotonic
                    Period objects.

                TF.Usability.TestCase.Context.Classic.Regions
                    It shall be possible to verify Classic API Region objects.

                TF.Usability.TestCase.Context.Classic.Semaphores
                    It shall be possible to verify Classic API Semaphore
                    objects.

                TF.Usability.TestCase.Context.Classic.Tasks
                    It shall be possible to verify Classic API Task objects.

                TF.Usability.TestCase.Context.Classic.Timers
                    It shall be possible to verify Classic API Timer objects.

            TF.Usability.TestCase.Context.POSIX
                It shall be possible to verify POSIX API objects.

                TF.Usability.TestCase.Context.POSIX.Keys
                    It shall be possible to verify POSIX API Key objects.

                TF.Usability.TestCase.Context.POSIX.KeyValuePairs
                    It shall be possible to verify POSIX API Key Value Pair
                    objects.

                TF.Usability.TestCase.Context.POSIX.MessageQueues
                    It shall be possible to verify POSIX API Message Queue
                    objects.

                TF.Usability.TestCase.Context.POSIX.Semaphores
                    It shall be possible to verify POSIX API Named Semaphores
                    objects.

                TF.Usability.TestCase.Context.POSIX.Shms
                    It shall be possible to verify POSIX API Shared Memory
                    objects.

                TF.Usability.TestCase.Context.POSIX.Threads
                    It shall be possible to verify POSIX API Thread objects.

                TF.Usability.TestCase.Context.POSIX.Timers
                    It shall be possible to verify POSIX API Timer objects.

    TF.Usability.Assert
        There shall be functions to assert test objectives.

        TF.Usability.Assert.Safe
            Test assert functions shall be safe to use, e.g. assert(a == b) vs.
            assert(a = b) vs. assert_eq(a, b).

        TF.Usability.Assert.Continue
            There shall be assert functions which allow the test case to
            continue in case of an assertion failure.

        TF.Usability.Assert.Abort
            There shall be assert functions which abourt the test case in case
            of an assertion failure.

    TF.Usability.EasyToWrite
        It shall be easy to write test code, e.g. avoid long namespace prefix
        rtems_test_*.

    TF.Usability.Threads
        The test framework shall support multi-threading.

    TF.Usability.Pattern
        The test framework shall support test patterns.

        TF.Usability.Pattern.Interrupts
            The test framework shall support test cases which use interrupts,
            e.g. spintrcritical*.

        TF.Usability.Pattern.Parallel
            The test framework shall support test cases which want to run code
            in parallel on SMP machines.

        TF.Usability.Pattern.Timing
            The test framework shall support test cases which want to measure
            the timing of code sections under various platform conditions, e.g.
            dirty cache, empty cache, hot cache, with load from other
            processors, etc..

    TF.Usability.Configuration
        The test framework shall be configurable.

        TF.Usability.Configuration.Time
            The timestamp function shall be configurable, e.g. to allow test
            runs without a clock driver.

Performance Requirements
------------------------

TF.Performance.RTEMS.No64BitDivision
    The test framework shall not use 64-bit divisions on RTEMS.

Off-the-shelf Test Frameworks
=============================

There are several
`off-the-shelf test frameworks for C/C++ <https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#C>`_.
The first obstacle for test frameworks is the license requirement
(`TF.License.Permissive`).

bdd-for-c
---------

In the `bdd-for-c <https://github.com/grassator/bdd-for-c>`_ framework the
complete test suite must be contained in one file and the main function is
generated.  This violates `TF.Usability.TestCase.Independence`.

CBDD
----

The `CBDD <https://github.com/nassersala/cbdd>`_ framework uses the
`C blocks <https://clang.llvm.org/docs/BlockLanguageSpec.html>`_ extension from
clang.  This violates `TF.Portability.C11`.

Google Test
-----------

`Google Test 1.8.1 <https://git.rtems.org/sebh/rtems-gtest.git/>`_
is supported by RTEMS.  Unfortunately, it is written in C++ and is to heavy
weight for low-end platforms.  Otherwise it is a nice framework.

Unity
-----

The `Unity Test API <https://github.com/ThrowTheSwitch/Unity>`_ does not meet
our requirements.  There was a `discussion on the mailing list in 2013
<https://lists.rtems.org/pipermail/devel/2013-September/004499.html>`_.

Standard Test Report Formats
============================

JUnit XML
---------

A common test report format is `JUnit XML <http://llg.cubic.org/docs/junit/>`_.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <testsuites id="xyz" name="abc" tests="225" failures="1262" time="0.001">
      <testsuite id="def" name="ghi" tests="45" failures="17" time="0.001">
        <testcase id="jkl" name="mno" time="0.001">
          <failure message="pqr" type="stu"></failure>
          <system-out>stdout</system-out>
          <system-err>stderr</system-err>
        </testcase>
      </testsuite>
    </testsuites>

The major problem with this format is that you have to output the failure count
of all test suites and the individual test suite before the test case output.
You know the failure count only after a complete test run.  This runs contrary
to requirement `TF.Portability.Small.Memory`.  It is also a bit verbose
(`TF.Reporting.Compact`).

It is easy to convert a full test report generated by :ref:`The RTEMS Test
Framework <RTEMSTestFramework>` to the JUnit XML format.

Test Anything Protocol
----------------------

The
`Test Anything Protocol <http://testanything.org/>`_
(TAP) is easy to consume and produce.

.. code-block:: none

    1..4
    ok 1 - Input file opened
    not ok 2 - First line of the input valid
    ok 3 - Read the rest of the file
    not ok 4 - Summarized correctly # TODO Not written yet

You have to know in advance how many test statements you want to execute in a
test case.  The problem with this format is that there is no standard way to
provide auxiliary data such as test timing or a tracing report.

It is easy to convert a full test report generated by :ref:`The RTEMS Test
Framework <RTEMSTestFramework>` to the TAP format.
