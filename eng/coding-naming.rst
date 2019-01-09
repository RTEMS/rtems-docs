.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

Naming Rules
************

.. COMMENT:TBD  - Convert the following to Rest and insert into this file
.. COMMENT:TBD  - https://devel.rtems.org/wiki/Developer/Coding/NamingRules

General Rules
-------------

 *  Avoid abbreviations.

    *  Exception: when the abbreviation is more common than the full word.
    *  Exception: For well-known acronyms.

 *  Use descriptive language.
 *  File names should be lower-case alphabet letters only, plus the extension.
    Avoid symbols in file names.
 *  Prefer to use underscores to separate words, rather than
    `CamelCase <https://devel.rtems.org/wiki/CamelCase>`_.or !TitleCase.
 *  Local-scope variable names are all lower case with underscores between words.
 *  CPP macros are all capital letters with underscores between words.
 *  Enumerated (enum) values are all capital letters with underscores between
    words, but the type name follows the regular rules of other type names.
 *  Constant (const) variables follow the same rules as other variables.
    An exception is that a const that replaces a CPP macro might be all
    capital letters for backward compatibility.
 *  Type names, function names, and global scope names have different rules
    depending on whether they are part of the public API or are internal
    to RTEMS, see below.

**User-Facing APIs**

The public API routines follow a standard API like POSIX or BSD or start
with *rtems_*. If a name starts with *rtems_*, then it should be assumed to be
available for use by the application and be documented in the User's Guide.

If the method is intended to be private, then make it static to a file or
start the name with a leading _.

**Classic API**

* Public facing APIs start with *rtems_* followed by a word or phrase to
  indicate the Manager or functional category the method or data type
  belongs to.

* Non-public APIs should be static or begin with a leading _. The required
  form is the use of a leading underscore, functional area with leading
  capital letter, an underscore, and the method with a leading capital letter.

**POSIX API**

 *  Follow the rules of POSIX.

**RTEMS Internal Interfaces**

**Super Core**

The `Super Core <https://docs.rtems.org/doxygen/cpukit/html/>`_. is organized in an
Object-Oriented fashion. Each score Handler is a Package, or Module,
and each Module contains type definitions, functions, etc.
The following summarizes our conventions for using names within
`SuperCore <https://docs.rtems.org/doxygen/cpukit/html/>`_. Modules.

 *  Use "Module_name_Particular_type_name" for type names.
 *  Use "_Module_name_Particular_function_name" for functions names.
 *  Use "_Module_name_Global_or_file_scope_variable_name" for global or
    file scope variable names.

Within a structure:

 *  Use "Name" for struct aggregate members.
 *  Use "name" for reference members.
 *  Use "name" for primitive type members.

As shown in the following example:

   .. code-block:: c

       typedef struct {
           Other_module_Struct_type    Aggregate_member_name;
           Other_module_Struct_type   *reference_member_name;
           Other_module_Primitive_type primitive_member_name;
         } The_module_Type_name;


**BSP**

 * TODO.
