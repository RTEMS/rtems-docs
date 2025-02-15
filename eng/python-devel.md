.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2020 embedded brains GmbH & Co. KG

.. _PythonDevelGuide:

Python Development Guidelines
*****************************

Python is the preferred programming language for the RTEMS Tools.  The RTEMS
Tools run on the host computer of an RTEMS user or maintainer.  These
guidelines cover the Python language version, the source code formatting, use
of static analysis tools, type annotations, testing, code coverage, and
documentation.  There are exceptions for existing code and third-party code.
It is recommended to read the
`PEP 8 - Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_
and the
`Google Python Style Guide <http://google.github.io/styleguide/pyguide.html>`_.

Python Language Versions
========================

Although the official end-of-life of Python 2.7 was on January 1, 2020, the
RTEMS Project still cares about Python 2.7 compatibility for some tools.  Every
tool provided by the RTEMS Project which an RTEMS user may use to develop
applications with RTEMS should be Python 2.7 compatible.  Examples are the
build system, the RTEMS Source Builder, and the RTEMS Tester.  The rationale is
that there are still some maintained Linux distributions in the wild which ship
only Python 2.7 by default.  An example is CentOS 7 which gets maintenance
updates until June 2024.  Everything an RTEMS maintainer uses should be written
in Python 3.6.

Python Code Formatting
======================

Good looking code is important.  Unfortunately, what looks good is a bit
subjective and varies from developer to developer.  Arguing about the code
format is not productive.  Code reviews should focus on more important topics,
for example functionality, testability, and performance.  Fortunately, for
Python there are some good automatic code formatters available.  All new code
specifically developed for the RTEMS Tools should be piped through the
`yapf <https://github.com/google/yapf>`_ Python code formatter before it is
committed or sent for review.  Use the default settings of the tool
(`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ coding style).

You can disable the automatic formatting by the tool in a region starting with
the ``#yapf: disable`` comment until the next ``# yapf: enable`` comment, for
example

.. code-block:: python

    # yapf: disable
    FOO = {
        # ... some very large, complex data literal.
    }

    BAR = [
        # ... another large data literal.
    ]
    # yapf: enable

For a single literal, you can disable the formatting like this:

.. code-block:: python

    BAZ = {
        (1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
    }  # yapf: disable

Static Analysis Tools
=====================

Use the ``flake8`` and ``pylint`` static analysis tools for Python.  Do not
commit your code or send it for review if the tools find some rule
violations.  Run the tools with the default configuration.  If you have
problems to silence the tools, then please ask for help on the :r:list:`devel`.
Consult the tool documentation to silence false positives.

Type Annotations
================

For Python 3.6 or later code use type annotations.  All public functions of
your modules should have `PEP 484 <https://www.python.org/dev/peps/pep-0484/>`_
type annotations.  Check for type issues with the
`mypy <http://mypy-lang.org/>`_ static type checker.

Testing
=======

Write tests for your code with the
`pytest <https://docs.pytest.org/en/latest/contents.html>`_ framework.  Use the
`monkeypatch <https://docs.pytest.org/en/latest/monkeypatch.html>`_ mocking
module.  Do not use the standard Python ``unittest`` and ``unittest.mock``
modules.  Use ``coverage run -m pytest`` to run the tests with code coverage
support.  If you modify existing code or contribute new code to a subproject
which uses tests and the code coverage metric, then do not make the code
coverage worse.

Test Organization
-----------------

Do not use test classes to group tests.  Use separate files instead.  Avoid
deep test directory hierarchies.  For example, place tests for
:file:`mymodule.py` in :file:`tests/test_mymodule.py`.  For class-specific
tests use:

* ``mymodule.py:class First`` :math:`\rightarrow`
  :file:`tests/test_mymodule_first.py`

* ``mymodule.py:class Second`` :math:`\rightarrow`
  :file:`tests/test_mymodule_second.py`

* ``mymodule.py:class Third`` :math:`\rightarrow`
  :file:`tests/test_mymodule_third.py`

You can also group tests in other ways, for example:

* :file:`mymodule.py` :math:`\rightarrow` :file:`tests/test_mymodule_input.py`

* :file:`mymodule.py` :math:`\rightarrow` :file:`tests/test_mymodule_output.py`

Documentation
=============

Document your code using the
`PEP 257 - Docstring Conventions <https://www.python.org/dev/peps/pep-0257/>`_.
Contrary to PEP 257, use the descriptive-style
(``"""Fetches rows from a Bigtable."""``) instead of imperative-style
(``"""Fetch rows from a Bigtable."""``) as recommended by
`Comments and Docstrings - Functions and Methods <http://google.github.io/styleguide/pyguide.html#383-functions-and-methods>`_.
Use the
`Sphinx <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_
format.  The
`sphinx-autodoc-typehints <https://pypi.org/project/sphinx-autodoc-typehints/>`_
helps to reuse the type annotations for the documentation.  Test code does not
need docstrings in general.

Existing Code
=============

Existing code in the RTEMS Tools may not follow the preceding guidelines.  The
RTEMS Project welcomes contributions which bring existing code in line with the
guidelines.  Firstly, run the ``yapf`` code formatter through the existing code
of interest.  Add ``# yapf: disable`` comments to avoid reformatting in some
areas if it makes sense.  If the existing code has no unit tests, then add unit
tests before you modify existing code by hand.  With the new unit tests aim at
a good code coverage especially in the areas you intend to modify.  While you
review the code add docstrings.  Run the static analysers and fix the rule
violations.  Please keep in mind that also trivial modifications can break
working code.  Make sure you have some unit tests.  Add type annotations unless
the code should be Python 2.7 compatible.  Concentrate on the public
interfaces.

Third-Party Code
================

Try to not modify imported third-party code.  In case there are issues with
third-party code, then at least write a bug report or otherwise contact the
upstream project.  Reimport the third-party code after the issue is fixed in
the upstream project.  Only temporarily modify imported third-party code until
a solution integrated in the upstream is available.
