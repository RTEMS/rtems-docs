.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

Eighty Character Line Limit
***************************

.. COMMENT: TBD - Convert the following to Rest and insert into this file
.. COMMENT: TBD - https://devel.rtems.org/wiki/Developer/Coding/80_characters_per_line

 Code should look good for everyone under some standard width assumptions.
 Where a line wraps should be the same for anyone reading the code. For
 historical reasons, RTEMS uses 80 characters as the maximum width for each
 line of code.

If you find yourself with code longer than 80 characters, first ask yourself
whether the nesting level is too deep, names too long, compound expressions too
complicated, or if some other guideline for improving readability can help to
shrink the line length. Refactoring nested blocks into functions can help to
alleviate code width problems while improving code readability. Making names
descriptive yet terse can also improve readability. If absolutely necessary
to have a long line, follow the rules on this page to break the line up to adhere
to the 80 characters per line rule.

Breaking long lines
-------------------

``if``, ``while``, and ``for`` loops have their condition expressions aligned
and broken on separate lines. When the conditions have to be broken, none go on
the first line with the ``if``, ``while``, or ``for`` statement, and none go on
the last line with the closing parenthesis and (optional) curly brace. Long
statements are broken up and indented at operators, with an operator always
being the last token on a line. No blank spaces should be left at the end of
any line. Here is an example with a ``for`` loop.

.. code-block:: c

  for ( initialization = statement; a + really + long + statement + that + evaluates + to < a + boolean; another + statement++ ) {
    z = a + really + long + statement + that + needs + two + lines + gets + indented + four + more + spaces + on + the + second + and + subsequent + lines + and + broken + up + at + operators;
  }

Should be replaced with

.. code-block:: c

  for (
    initialization = statement;
    a + really + long + statement + that + evaluates + to <
    a + boolean;
    another + statement++
  ) {
    z = a + really + long + statement + that + needs +
        two + lines + gets + indented + four + more +
        spaces + on + the + second + and + subsequent +
        lines + and + broken + up + at + operators;
  }

Note that indentations should add 2 nesting levels (4 space characters, not tabs).

Similarly,

.. code-block:: c

  if ( this + that < those && this + these < that && this + those < these && this < those && those < that ) {

should be broken up like

.. code-block:: c

  if (
    this + that < those &&
    this + these < that &&
    this + those < these &&
    this < those &&
    those < that
  ) {

Note that each expression that resolves to a boolean goes on its own line.
Where you place the boolean operator is a matter of choice.

When a line is long because of a comment at the end, move the comment to
just before the line, for example

.. code-block:: c

  #define A_LONG_MACRO_NAME (AND + EXPANSION) /* Plus + a + really + long + comment */

can be replaced with

.. code-block:: c

  /* Plus + a + really + long + comment */
  #define A_LONG_MACRO_NAME (AND + EXPANSION)

C Preprocessor macros need to be broken up with some care, because the
preprocessor does not understand that it should eat newline characters. So

.. code-block:: c

  #define A_LONG_MACRO_NAME (AND + EXCESSIVELY + LONG + EXPANSION + WITH + LOTS + OF + EXTRA + STUFF + DEFINED)

would become

.. code-block:: c

  #define A_LONG_MACRO_NAME ( \
    AND + EXCESSIVELY + LONG + EXPANSION + WITH + LOTS + OF + EXTRA + STUFF + \
    DEFINED \
  )

Notice that each line is terminated by a backslash then the carriage return.
The backslash tells the preprocessor to eat the newline. Of course, if you have
such a long macro, you should consider not using a macro.

Function declarations can be broken up at each argument, for example

.. code-block:: c

  int this_is_a_function( int arg1, int arg2, int arg3, int arg4, int arg5, int arg6, int arg7, int arg8, int arg9 );

would be broken up as

.. code-block:: c

  int this_is_a_function(
    int arg1,
    int arg2,
    int arg3,
    int arg4,
    int arg5,
    int arg6,
    int arg7,
    int arg8,
    int arg9
  );

Excessively long comments should be broken up at a word boundary or somewhere
that makes sense, for example

.. code-block:: c

  /* Excessively long comments should be broken up at a word boundary or somewhere that makes sense, for example */

would be

.. code-block:: c

  /* Excessively long comments should be broken up at a word boundary or
   * somewhere that makes sense, for example */

Note that multiline comments have a single asterisk aligned with the asterisk
in the opening ``/*``. The closing ``*/`` should go at the end of the last
line.
