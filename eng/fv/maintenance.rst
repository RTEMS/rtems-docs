.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2022 Trinity College Dublin

.. _FormalMaint:

Test Generation Maintenance
===========================

The standard RTEMS technique of emailing a patch-set for review shall be used.
the basic principle is that any file modified as a result of changes, *including
generated C test code* will be included in the patch-sets. A complication is
that most model changes will apply to ``rtems-central``, while the resulting
test code changes will take place in the ``rtems`` sub-module. Changes to the
overall configuration (new testsuites mainly) may affect both respositories.
**GB: In Section "9.6 Test Generation Maintenance" please refer to Section
"Software Development Management" instead of hard-coding the patch
submission process.**

Key pathnames, as viewed from ``rtems-central``:

Formal Models
    ``formal/promela/models/``

    Every distinct model has a name (``mymodel`` say), and the relevant model
    files shall live in ``formal/promela/models/mymodel``

Configuration
    ``spec/testsuites/model-0.yml`` whose main role is provide meta-data about
    the testsuite. The key parts of these are as follows:

    .. code-block:: yaml

      enabled-by: RTEMS_SMP
      test-suite-name: Model0
      test-target: testsuites/validation/ts-model-0.c

    ``modules/rtems/spec/build/testsuites/validation/model-0.yml`` contains a
    listing of all the C test code that is deployed to this testsuite.

Generated Test Code
    ``modules/rtems/testsuites/validation/`` will contain ``ts-model-0.c`` plus
    any other supporting source files.

Changing an existing model
--------------------------

Having made the required changes to model and generation files (``.pml``,
``-rfn.yml``, ``.c``, ``.h``), run the test generation process and deploy the
generated test code to ``testsuites/validation/``.

Adding a new model into an existing testsuite
---------------------------------------------

Assume the new model is called ``newmodel``. The new model and generation files
(``.pml``, ``-rfn.yml``, ``.c``, ``.h``) are added into
``formal/promela/models/newmodel``. The test generation process is then run,
and then the generated C can be deployed. Before building the tests, however,
it is necessary to update the overall configuration. The names of all the files
to be deployed need to be added to
``modules/rtems/spec/build/testsuites/validation/model-0.yml``. Once this is
done the tests can be built and run.


Adding a new testsuite
----------------------

At present there is only one testsuite for formal methods tests, ``model-0``.
There is no immediate plan to add another, but if this was required, then it
would require adding two ``another-model.yml`` files, one in
``spec/testsuites/``, the other in
``modules/rtems/spec/build/testsuites/validation/``, following the same pattern
as the two ``model-0.yml`` files.
