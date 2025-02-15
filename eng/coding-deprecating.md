.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2024.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

Deprectating Interfaces
***********************

Use the deprecate attribute
===========================

Add the `RTEMS_COMPILER_DEPRECATED_ATTRIBUTE`, which for gcc wraps the 
`deprecated attribute 
<https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html#index-deprecated-function-attribute>`_,
to functions, structures, and global symbols exported by the deprecated 
interface. Update the doxygen for each of these with the @deprecated command, 
for example:

.. code-block:: c

    /**
     * @brief RTEMS Feature
     *
     * @deprecated Feature is deprecated and will be removed.
     */


Add a warning
=============

Add a warning for configured features in confdefs.h

For features that are enabled or configured through confdefs.h, the feature 
should be disabled by default and a compile-time warning message should be 
printed, something along the lines of:

.. code-block:: c

    #warning "CONFIGURE_FEATURE_XXX\n\t\t\t**** Deprecated and will be removed. ****"


Update documentation
====================

Find references to the deprecated feature in the user manuals (doc) and wiki, 
and make a note that the features are deprecated and may be removed.


Update support code
===================

Update support code  using deprecated feature

If there is support code using the feature, you will need to modify that support 
code to not use that feature. If the code cannot be immediately modified, file a 
ticket on the issue and disable the deprecated warning. The code will need to be 
addressed before the feature can be removed.

If the code in question is such that the feature's use can benignly be removed 
when the feature is removed, then simply disable the deprecated warning as shown 
below.

It is possible that a test may need to be split into two or more tests, so the 
code that is exercising the deprecated feature can be easily removed when the 
feature is removed.


Disable deprecated warnings
===========================

After adding the deprecated attribute, the files which implement the method(s), 
any tests for them, and any support code using that feature that will remain 
until the feature is removed will need the deprecate warning disabled. If it is 
for an entire file, then using this:

.. code-block:: c

    /*
    * We know this is deprecated and don't want a warning on every BSP built.
    */
    #pragma GCC diagnostic ignored "-Wdeprecated-declarat

If it is for a section of code, then this is the appropriate code to surround 
the section with:

.. code-block:: c

    /*
    * We know this is deprecated and don't want a warning on every BSP built.
    */
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wdeprecated-declarations"

    /**** Code using deprecated feature ****/
    #pragma GCC diagnostic pop


Add a release note
==================
Add the feature to a list of deprecated interfaces in the release notes.
