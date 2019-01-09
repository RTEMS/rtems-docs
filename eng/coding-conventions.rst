.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

.. COMMENT:TBD  - Convert the following to Rest and insert into this file
.. COMMENT:TBD  - https://devel.rtems.org/wiki/Developer/Coding/Conventions

Coding Conventions
******************

The style of RTEMS is generally consistent in the core areas.
This page attempts to capture generally accepted practices.
When in doubt, consult the code around you or look in cpukit/rtems.
See the sister page `Doxygen Recommendations <https://devel.rtems.org/wiki/Developer/Coding/Doxygen>`_.
for examples that illustrate style rules and Doxygen usage.

Source Documentation
--------------------

* Use Doxygen according to our `Doxygen Recommendations <https://devel.rtems.org/wiki/Developer/Coding/Doxygen>`_..
* Start each file with a brief description followed by a license.
  See `Boilerplate File Header <https://devel.rtems.org/wiki/Developer/Coding/Boilerplate_File_Header>`_..
* Use /* */ comments.
* Use comments wisely within function bodies, to explain
  or draw attention without being verbose.
* Use English prose and strive for good grammar,
  spelling, and punctuation.
* Use TODO: with a comment to indicate code that needs improvement.
  Make it clear what there is to do.
* Use XXX or FIXME to indicate an error/bug/broken code.

Licenses
--------

* The RTEMS `License <https://devel.rtems.org/wiki/TBR/Website/License>`_. is the typical
  and preferred license.
  * 2- and 3-clause BSD, MIT, and other OSI-approved non-copyleft licenses
    that permit statically linking with the code of different licenses
    are acceptable.
  * GPL licensed code is NOT acceptable, neither is LGPL.
    See `this blog post explanation <http://gedare-csphd.blogspot.com/2013/05/software-licenses-with-rtems.html>`_.
    for more information.
  * Advertising obligations are NOT acceptable, but restrictions are permissible.

Language and Compiler
---------------------

* Use C99.
* Treat warnings as errors: eliminate them.
* Favor C, but when assembly language is required use inline
  assembly if possible.
* Do not use compiler extensions.
* Use the RTEMS_macros defined in score/basedefs.h for abstracting
  compiler-specific features.
* Use NULL for the null pointer, and prefer to use explicit
  checks against NULL, e.g.,

  .. code-block:: c

      if ( ptr != NULL )
  instead of

  .. code-block:: c

      if ( !ptr )
* Use explicit checks for bits in variables.
   * Example 1: Use
      .. code-block:: c

           if ( XBITS == (var & XBITS) )
     to check for a set of defined bits.
   * Example 2: Use
      .. code-block:: c

          if ( (var & X_FLAGS) != 0) )
     instead of
      .. code-block:: c

          if ( !!(var & X_FLAGS) )
     to check for at least 1 defined bit in a set.
* Use '(void) unused;' to mark unused parameters and set-but-unused
  variables immediately after being set.
* Do not put function prototypes in C source files, any global functions
  should have a prototype in a header file and any private function
  should be declared static.
* Declare global variables in exactly one header file.
  Define global variables in at most one source file.
  Include the header file declaring the global variable as
  the first include file if possible to make sure that the
  compiler checks the declaration and definition and that
  the header file is self-contained.
* Do not cast arguments to any printf() or printk() variant.
  Use <inttypes.h> PRI constants for the types supported there.
  Use <rtems/inttypes.h> for the other POSIX and RTEMS types that
  have PRI constants defined there. This increases the portability
  of the printf() format.
* Do not use the register keyword. It is deprecated since C++14.

Formatting
-----------

* Use spaces instead of tabs.
* Use two spaces for indentation, four spaces for
  hanging indentation.
* Adhere to a limit of `80 characters per line <https://devel.rtems.org/wiki/Developer/Coding/80_characters_per_line>`_..
* Put function return types and names on one line if they fit.
* Put function calls on one line if they fit.
* No space between a function name or function-like macro and
  the opening parens.
* Put braces on the same line as and one space after the
  conditional expression ends.
* Put the opening brace of a function definition one line after
  the closing parenthesis of its prototype.
* Put a single space inside and outside of each parenthesis
  of a conditional expression.
  * Exception: never put a space before a closing semi-colon.
* Put a single space before and after ternary operators.
* Put a single space before and after binary operators.
* Put no space between unary operators (e.g. *, &, !, ~, ++, --)
  and their operands.
* No spaces around dereferencing operators (-> and .).
* Do not use more than one blank line in a row.
* Do not use trailing whitespace at the end of a line.

Readability
------------

* Understand and follow the `naming rules <https://devel.rtems.org/wiki/Developer/Coding/NamingRules>`_..
* Use typedef to remove 'struct', but do not use typedef
  to hide pointers or arrays.
  * Exception: typedef can be used to simplify function pointer types.

* Do not mix variable declarations and code.
* Declare variables at the start of a block.
* Only use primitive initialization of variables at their declarations.
  Avoid complex initializations or function calls in variable declarations.
* Do not put unrelated functions or data in a single file.
* Do not declare functions inside functions.
* Avoid deep nesting by using early exits e.g. return, break, continue.
  * Parameter checking should be done first with early error returns.
  * Avoid allocation and critical sections until error checking is done.
  * For error checks that require locking, do the checks early after acquiring locks.
  * Use of 'goto' requires good reason and justification.

* Test and action should stay close together.
* Avoid complex logic in conditional and loop statements.
* Put conditional and loop statements on the line after the expression.
* Favor inline functions to hide
  `compile-time feature-conditioned compilation <https://devel.rtems.org/wiki/Developer/Coding/Compile-time_feature-conditioned_compilation>`_..
* Define non-inline functions in a .c source file.
* Declare all global (non-static) functions in a .h header file.
* Declare and define inline functions in one place. Usually, this
  is a *impl.h header file.
* Declare and define static functions in one place. Usually, this is
  toward the start of a .c file. Minimize forward declarations of
  static functions.
* Function declarations should include variable names.
* Avoid excess parentheses. Learn the
  `operator precedence <https://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B#Operator_precedence>`_. rules.
* Always use parentheses with sizeof. This is an exception to the rule
  about excess parentheses.

Robustness
-----------

* Check all return statuses.
* Validate input parameters.
* Use debug assertions (assert).
* Use const when appropriate for read-only function parameters
  and compile-time constant values.
* Do not hard code limits such as maximum instances into your code.
* Prefer to use sizeof(variable) instead of sizeof(type).
* Favor C automatic variables over global or static variables.
* Use global variables only when necessary and ensure
  atomicity of operations.
* Do not shadow variables.
* Avoid declaring large buffers or structures on the stack.
* Avoid using zero (0) as a valid value. Memory often
  defaults to being zero.
* Favor mutual exclusion primitives over disabling preemption.
* Avoid unnecessary dependencies, such as by not calling
  ''printf()'' on error paths.
* Avoid inline functions and macros with complicated logic
  and decision points.
* Prefer inline functions, enum, and const variables instead of CPP macros.
* CPP macros should use a leading underscore for parameter
  names and `avoid macro pitfalls <https://gcc.gnu.org/onlinedocs/cpp/Macro-Pitfalls.html#Macro-Pitfalls>`_..

Portability
-----------

* Think portable! RTEMS supports a lot of target hardware.
* For integer primitives, prefer to use precise-width integer
  types from C99 stdint.h.
* Write code that is 16-bit, 32-bit, and 64-bit friendly.

Maintainability
---------------

* Minimize modifications to `third-party code <https://devel.rtems.org/wiki/Developer/Coding/ThirdPartyCode>`_..
* Keep it simple! Simple code is easier to debug and easier to read than clever code.
* Share code with other architectures, CPUs, and BSPs where possible.
* Do not duplicate standard OS or C Library routines.

Performance
-----------

* Prefer algorithms with the `lowest order of time and space <https://devel.rtems.org/wiki/FAQ/AlgorithmicComplexity>`_.
  for fast, deterministic execution times with small memory footprints.
* Understand the constraints of `real-time programming <https://devel.rtems.org/wiki/TBR/Review/Real-Time_Resources>`_..
  Limit execution times in interrupt contexts and critical sections,
  such as Interrupt and Timer Service Routines (TSRs).
* Functions used only through function pointers should be declared
  'static inline' (RTEMS_INLINE_ROUTINE)
* Prefer to ++preincrement instead of postincrement++.
* Avoid using floating point except where absolutely necessary.

Miscellaneous
-------------

* If you need to temporarily change the execution mode of a
  task/thread, restore it.
* If adding code to ''cpukit'' be sure the filename is unique since
  all files under that directory get merged into a single library.

Layering
--------

* TBD: add something about the dependencies and header file layering.
* Understand the `RTEMS Software Architecture <https://devel.rtems.org/wiki/TBR/UserManual/RTEMS_Software_Architecture>'_.

Exceptions to the Rules
-----------------------

* Minimize reformatting existing code in RTEMS unless the file undergoes
  substantial non-style changes.
* `Third-party code <https://devel.rtems.org/wiki/Developer/Coding/ThirdPartyCode>`_.
  should not be reformatted to fit RTEMS style.
  Exception: unmaintained third-party code adopted and
  maintained by RTEMS may be reformatted, subject to the
  above rules.

Tools
-----

Some of the above can be assisted by tool support. Feel free to add
more tools, configurations, etc here.

* `Uncrustify <http://uncrustify.sourceforge.net/>`_.
  Configuration for RTEMS:
  `rtems.uncrustify <https://devel.rtems.org/attachment/wiki/Developer/Coding/Conventions/rtems.uncrustify>`_.
