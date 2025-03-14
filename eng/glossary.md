% SPDX-License-Identifier: CC-BY-SA-4.0

% Copyright (C) 2022, 2023 Trinity College Dublin

% Copyright (C) 2017, 2019 embedded brains GmbH & Co. KG

% Copyright (C) 1988, 1998 On-Line Applications Research Corporation (OAR)

# Glossary

```{glossary}
---
sorted: true
---
API

: This term is an acronym for Application Programming Interface.

assembler language

: The assembler language is a programming language which can be translated very
  easily into machine code and data. For this project assembler languages are
  restricted to languages accepted by the {term}`GNU` assembler
  program for the target architectures.

C language

: The C language for this project is defined in terms of
  {term}`C11`.

C11

: The standard ISO/IEC 9899:2011.

CCB

: This term is an acronym for Change Control Board.

Doorstop

: [Doorstop](https://github.com/doorstop-dev/doorstop) is a
  requirements management tool.

EARS

: This term is an acronym for Easy Approach to Requirements Syntax.

ELF

: This term is an acronym for
  [Executable and Linkable Format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format).

formal model

: A model of a computing component (hardware or software) that has a
  mathematically based {term}`semantics`.

GCC

: This term is an acronym for [GNU Compiler Collection](https://gcc.gnu.org/).

GNAT

: *GNAT* is the {term}`GNU` compiler for Ada, integrated into the
  {term}`GCC`.

GNU

: This term is an acronym for [GNU's Not Unix](https://www.gnu.org/).

interrupt service

: An *interrupt service* consists of an
  {term}`Interrupt Service Routine` which is called with a user
  provided argument upon reception of an interrupt service request. The
  routine is invoked in interrupt context. Interrupt service requests may have
  a priority and an affinity to a set of processors. An *interrupt service* is
  a {term}`software component`.

Interrupt Service Routine

: An ISR is invoked by the CPU to process a pending interrupt.

ISVV

: This term is an acronym for Independent Software Verification and Validation.

Linear Temporal Logic

: This is a logic that states properties about (possibly infinite) sequences of
  states.

LTL

: This term is an acronym for {term}`Linear Temporal Logic`.

refinement

: A *refinement* is a relationship between a specification and its
  implementation as code.

reification

: Another term used to denote {term}`refinement`.

ReqIF

: This term is an acronym for
  [Requirements Interchange Format](https://www.omg.org/spec/ReqIF/About-ReqIF/).

RTEMS

: This term is an acronym for Real-Time Executive for Multiprocessor Systems.

scenario

: In the context of formal verification, in a setting that involves many
  concurrent tasks that interleave in arbitrary ways, a scenario describes a
  single specific possible interleaving. One interpretation of the behaviour
  of a concurrent system is the set of all its scenarios.

semantics

: This term refers to the meaning of text or utterances in some language. In a
  software engineering context these will be programming, modelling or
  specification languages.

software component

: This term is defined by ECSS-E-ST-40C 3.2.28 as a "part of a software
  system". For this project a *software component* shall be any of the
  following items and nothing else:

  - {term}`software unit`
  - explicitly defined {term}`ELF` symbol in a
    {term}`source code` file
  - {term}`assembler language` data in a source code file
  - {term}`C language` object with static storage duration
  - C language object with thread-local storage duration
  - {term}`thread`
  - {term}`interrupt service`
  - collection of *software components* (this is a software architecture
    element)

  Please note that explicitly defined ELF symbols and assembler language
  data are considered a software component only if they are defined in a
  {term}`source code` file. For example, this rules out symbols
  and data generated as side-effects by the toolchain (compiler, assembler,
  linker) such as jump tables, linker trampolines, exception frame information,
  etc.

software product

: The *software product* is the {term}`RTEMS` real-time operating system.

software unit

: This term is defined by ECSS-E-ST-40C 3.2.24 as a "separately compilable
  piece of source code". For this project a *software unit* shall be any of
  the following items and nothing else:

  - {term}`assembler language` function in a
    {term}`source code` file
  - {term}`C language` function (external and internal linkage)

  A *software unit* is a {term}`software component`.

source code

: This project uses the *source code* definition of the
  [Linux Information Project](http://www.linfo.org/source_code.html):
  "Source code (also referred to as source or code) is the version of
  software as it is originally written (i.e., typed into a computer) by a
  human in plain text (i.e., human readable alphanumeric characters)."

target

: The system on which the application will ultimately execute.

task

: This project uses the
  [thread definition of Wikipedia](<https://en.wikipedia.org/wiki/Thread_(computing)>):
  "a thread of execution is the smallest sequence of programmed
  instructions that can be managed independently by a scheduler, which is
  typically a part of the operating system."

  It consists normally of a set of registers and a stack. The scheduler
  assigns processors to a subset of the ready tasks. The terms task and
  {term}`thread` are synonym in RTEMS. The term task is used
  throughout the Classic API, however, internally in the operating system
  implementation and the POSIX API the term thread is used.

  A *task* is a {term}`software component`.

thread

: This term has the same meaning as {term}`task`.

YAML

: This term is an acronym for [YAML Ain't Markup Language](https://yaml.org/).
```
