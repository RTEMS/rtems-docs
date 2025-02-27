% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2018.

% COMMENT: RTEMS Foundation, The RTEMS Documentation Project

(NamingRules)=

# Naming Rules

## General Rules

- Avoid abbreviations.

  - Exception: When the abbreviation is more common than the full word.
  - Exception: For well-known acronyms.

- Use descriptive language.

- File names should be lower-case alphabet letters only, plus the extension.
  Avoid symbols in file names.

  - Exception: Use a single underscore `_` or hyphen `-` to separate words in
    file names.

- Prefer to use underscores (Snake_Case) to separate words, rather than
  CamelCase or TitleCase.

- Local-scope variable names are all lower case with underscores between words.

- CPP macros are all capital letters with underscores between words.

- Enumerated (enum) values are all capital letters with underscores between
  words, but the type name follows the regular rules of other type names.

- Constant (const) variables follow the same rules as other variables. An
  exception is that a const that replaces a CPP macro might be all capital
  letters for backward compatibility.

- Type names, function names, and global scope names have different rules
  depending on whether they are part of the public API or are internal to
  RTEMS, see below.

## User-facing API

The public API routines follow a standard API like POSIX or BSD or start with
`rtems_`. If a name starts with `rtems_`, then it should be assumed to be
available for use by the application and be documented in the User's Guide.

The POSIX API follows the rules of POSIX.

## RTEMS internal interfaces

The SuperCore (`cpukit/score`) or "score" is organized in an object-oriented
fashion. Each score Manager is a Package (or Module), and each Module contains
type definitions, functions, etc. The following summarizes our conventions for
using names within SuperCore Modules:

- Use `Module_name_Particular_type_name` for type names.

- Use `_Module_name_Particular_function_name` for function names.

- Use `_Module_name_Global_or_file_scope_variable_name` for global or file
  scope variable names.

- Within a structure:

  - Use `Name` for struct aggregate members.

  - Use `name` for reference members.

  - Use `name` for primitive type members.

  - Example:

    > ```C
    > typedef struct {
    >   Other_module_Struct_type    Aggregate_member_name;
    >   Other_module_Struct_type   *reference_member_name;
    >   Other_module_Primitive_type primitive_member_name;
    > } The_module_Type_name;
    > ```
