.. comment SPDX-License-Identifier: CC-BY-SA-4.0

.. COMMENT: COPYRIGHT (c) 2018.
.. COMMENT: RTEMS Foundation, The RTEMS Documentation Project

General Doxygen Recommentations
-------------------------------

TBD - Convert the following to Rest and insert into this file
TBD - https://devel.rtems.org/wiki/Developer/Coding/Doxygen

Doxygen Best Practices
----------------------

* Do not use @a. Instead use @param to document function parameters.
* Do not use @return. Instead use @retval to document return status codes.
* Do not write documentation for trivial functions.
* Do not repeat documentation, use @see for example.
* Do not use @note.
* Use groups and arrange them in a hierarchy. Put every file into at least one group.
* Use dot comments for state diagrams.
* Use one whitespace character after an asterisk.

Special Notes for Google Code In Students
-----------------------------------------

* Follow the directions given by the `Google Code In <https://devel.rtems.org/wiki/GCI>`_ task and this should take care of itself if in doubt ask a mentor and/or tell a mentor the decision you made.

Header File Example
-------------------

​`thread.h <https://git.rtems.org/rtems/tree/cpukit/score/include/rtems/score/thread.h>`_ and `​threadimpl.h <https://git.rtems.org/rtems/tree/cpukit/score/include/rtems/score/threadimpl.h>`_ should be a good example of how a header file should be written. The following gives details in bits and pieces.

Header blocks
-------------

Header files should contain the similar comment blocks as other source files, described at `Boilerplate File Header <https://devel.rtems.org/wiki/Developer/Coding/Boilerplate_File_Header>`_.

	.. code-block:: c

		/**
		 * @file
		 *
		 * @ingroup FlipFlop
		 *
		 * @brief Flip-Flop API
		 */

		/*
		 * Copyright (c) YYYY Author.
		 *
		 * The license and distribution terms for this file may be
		 * found in the file LICENSE in this distribution or at
		 * http://www.rtems.com/license/LICENSE.
		 */

Header guard
------------

After the comment blocks, use a header guard that assembles at least the include path of the file. For example, if flipflop.h is in <rtems/lib/flipflop.h> then

	.. code-block:: c

		#ifndef RTEMS_LIB_FLIP_FLOP_H
		#define RTEMS_LIB_FLIP_FLOP_H

Includes
--------

Then add your include files before protecting C declarations from C++.


	.. code-block:: c

		#include <rtems.h>

		#ifdef __cplusplus
		extern "C" {
		#endif /* __cplusplus */

Using @defgroup for group definitions
-------------------------------------

Add any group definitions surrounding the function declarations that belong in that group. Rarely, a header may define more than one group. Here we use a dot diagram.


	.. code-block:: c

		/**
		 * @defgroup FlipFlop Flip-Flop
		 *
		 * @brief Simple Flip-Flop state machine.
		 *
		 * @dot
		 *   digraph {
		 *     start [label="START"];
		 *     flip [label="FLIP"];
		 *     flop [label="FLOP"];
		 *     flip -> flop [label="flop()", URL="\ref flop"];
		 *     flop -> flip [label="flip()", URL="\ref flip"];
		 *     start -> flip
		 *       [label="flip_flop_initialize(FLIP)", URL="\ref flip_flop_initialize"];
		 *     start -> flop
		 *       [label="flip_flop_initialize(FLOP)", URL="\ref flip_flop_initialize"];
		 *     flip -> start
		 *       [label="flip_flop_restart()", URL="\ref flip_flop_restart"];
		 *   }
		 * @enddot
		 *
		 * @{
		 */

enum and struct
---------------

Provide documentation for declarations of enumerated types and structs. Use typedefs for structs, and do not use _t as a typename suffix.


	.. code-block:: c

		/**
		 * @brief The set of possible flip-flop states.
		 *
		 * Enumerated type to define the set of states for a flip-flop.
		 */
		typedef enum {
		  START = 0,
		  FLIP,
		  FLOP
		} flip_flop_state;

		/**
		 * @brief Object containing multiple flip-flops.
		 *
		 * Encapsulates multiple flip-flops.
		 */
		typedef struct {
		  /**
		   * @brief Primary flip-flop.
		   */
		  flip_flop_state primary;
		  /**
		   * @brief Secondary flip-flop.
		   */
		  flip_flop_state secondary;
		} flip_flop_multiple;


Using @name for organization
----------------------------

Complicated groups can be given additional organization by using @name, or by declaring additional groups within the hierarchy of the header file's top-level group.

	.. code-block:: c

		/**
		 * @name Flip-Flop Maintenance
		 *
		 * @{
		 */

Declaring functions
-------------------

Function declarations should have an @brief that states what the function does in a single topic sentence starting with a descriptive verb in the present tense.


	.. code-block:: c
		/**
		 * @brief Initializes the flip-flop state.
		 *
		 * @param[in] state The initial state to set the flip-flop.
		 *
		 * @retval RTEMS_SUCCESSFUL Successfully initialized.
		 * @retval RTEMS_INCORRECT_STATE Flip-flop state is not valid.
		 */
		rtems_status_code flip_flop_initialize(flip_flop_state state);

		/**
		 * @brief Restarts the flip-flop.
		 *
		 * @retval RTEMS_SUCCESSFUL Successfully restarted.
		 * @retval RTEMS_INCORRECT_STATE Flip-flop not in flip state.
		 */
		rtems_status_code flip_flop_restart(void);

Do not document trivial functions, such as getter/setter methods.

	.. code-block:: c
		flip_flop_state flip_flop_current_state(void);

Close the documentation name definition and open a new name definition.

	.. code-block:: c
		/** @} */

		/**
		 * @name Flip-Flop Usage
		 *
		 * @{
		 */

		/**
		 * @brief Flip operation.
		 *
		 * @retval RTEMS_SUCCESSFUL Flipped successfully.
		 * @retval RTEMS_INCORRECT_STATE Incorrect state for flip operation.
		 */
		rtems_status_code flip( void );

		/**
		 * @brief Flop operation.
		 *
		 * @retval RTEMS_SUCCESSFUL Flopped successfully.
		 * @retval RTEMS_INCORRECT_STATE Incorrect state for flop operation.
		 */
		rtems_status_code flop( void );

		/** @} */

Ending the file
---------------

Close the documentation group definition, then the extern C declarations, then the header guard.

	.. code-block:: c
		/** @} */

		#ifdef __cplusplus
		}
		#endif /* __cplusplus */

		#endif /* RTEMS_LIB_FLIP_FLOP_H */

No newline at the end of the file.

Source File Example
-------------------

	.. code-block:: c

		/**
		 * @file
		 *
		 * @ingroup FlipFlop
		 *
		 * @brief Flip-Flop implementation.
		 */

		/*
		 * Copyright (c) YYYY Author.
		 *
		 * The license and distribution terms for this file may be
		 * found in the file LICENSE in this distribution or at
		 * http://www.rtems.com/license/LICENSE.
		 */

		#include <rtems/lib/flipflop.h>

		static flip_flop_state current_state;

		rtems_status_code flip_flop_initialize(flip_flop_state state)
		{
		  if (current_state == START) {
		    current_state = state;

		    return RTEMS_SUCCESSFUL;
		  } else {
		    return RTEMS_INCORRECT_STATE;
		  }
		}

		rtems_status_code flip_flop_restart(void)
		{
		  if (current_state == FLIP) {
		    current_state = START;

		    return RTEMS_SUCCESSFUL;
		  } else {
		    return RTEMS_INCORRECT_STATE;
		  }
		}

		flip_flop_state flip_flop_current_state(void)
		{
		  return current_state;
		}

		rtems_status_code flip(void)
		{
		  if (current_state == FLOP) {
		    current_state = FLIP;

		    return RTEMS_SUCCESSFUL;
		  } else {
		    return RTEMS_INCORRECT_STATE;
		  }
		}

		rtems_status_code flop(void)
		{
		  if (current_state == FLIP) {
		    current_state = FLOP;

		    return RTEMS_SUCCESSFUL;
		  } else {
		    return RTEMS_INCORRECT_STATE;
		  }
		}

Files
-----

Document files with the @file directive omitting the optional filename argument. Doxygen will infer the filename from the actual name of the file. Within one Doxygen run all files are unique and specified by the current Doxyfile. We can define how the generated output of path and filenames looks like in the Doxyfile via the FULL_PATH_NAMES, STRIP_FROM_PATH and STRIP_FROM_INC_PATH options.

Functions
---------

For documentation of function arguments there are basically to ways: The first one uses @param:

	.. code-block::
		/**
		 * @brief Copies from a source to a destination memory area.
		 *
		 * The source and destination areas may not overlap.
		 *
		 * @param[out] dest The destination memory area to copy to.
		 * @param[in] src The source memory area to copy from.
		 * @param[in] n The number of bytes to copy.
		 */
		The second is to use @a param in descriptive text, for example:

		/**
		 * Copies @a n bytes from a source memory area @a src to a destination memory
		 * area @a dest, where both areas may not overlap.
		 */

The @a indicates that the next word is a function argument and deserves some kind of highlighting. However, we feel that @a buries the usage of function arguments within description text. In RTEMS sources, we prefer to use @param instead of @a.

Doxyfile Hints
--------------

Header Files
------------

It is an RTEMS build feature that header files need to be installed in order to be useful. One workaround to generate documentation which allows automatic link generation is to use the installed header files as documentation input. Assume that we have the RTEMS sources in the rtems directory and the build of our BSP in build/powerpc-rtems5/mybsp relative to a common top-level directory. Then you can configure Doxygen like:


	.. code-block::
		INPUT           = rtems/bsps/powerpc/mybsp \
				  rtems/c/src/lib/libcpu/powerpc/mycpu \
				  rtems/make/custom/mybsp.cfg \
				  build/powerpc-rtems5/mybsp/lib/include/myincludes

		RECURSIVE       = YES

		EXCLUDE         = rtems/bsps/powerpc/mybsp/include \
				  rtems/c/src/lib/libcpu/powerpc/mycpu/include

		FULL_PATH_NAMES = YES

		STRIP_FROM_PATH = build/powerpc-rtems5/mybsp/lib/include \
				  rtems

Script and Assembly Files
-------------------------

Doxygen cannot cope with script (= files with #-like comments) or assembly files. But you can add filter programs for them (TODO: Add source code for filter programs somewhere):

	.. code-block::
		FILTER_PATTERNS = *.S=c-comments-only \
				  *.s=c-comments-only \
				  *.cfg=script-comments-only \
				  *.am=script-comments-only \
				  *.ac=script-comments-only

Assembly Example
----------------

	.. code-block::
		/**
		 * @fn void mpc55xx_fmpll_reset_config()
		 *
		 * @brief Configure FMPLL after reset.
		 *
		 * Sets the system clock from 12 MHz in two steps up to 128 MHz.
		 */
		GLOBAL_FUNCTION mpc55xx_fmpll_reset_config
		    /* Save link register */
		    mflr r3

		    LA r4, FMPLL_SYNCR

You have to put a declaration of this function somewhere in a header file.

Script Example
--------------

	.. code-block::
		##
		#
		# @file
		#
		# @ingroup mpc55xx_config
		#
		# @brief Configure script of LibBSP for the MPC55xx evaluation boards.
		#

		AC_PREREQ(2.60)
		AC_INIT([rtems-c-src-lib-libbsp-powerpc-mpc55xxevb],[_RTEMS_VERSION],[http://www.rtems.org/bugzilla])

GCC Attributes
--------------

The Doxygen C/C++ parser cannot cope with the GCC attribute((something)) stuff. But you can discard such features with pre-defined preprocessor macros:

	.. code-block::
		ENABLE_PREPROCESSING = YES
		MACRO_EXPANSION      = YES
		EXPAND_ONLY_PREDEF   = YES
		PREDEFINED           = __attribute__(x)=

History
-------

RTEMS is much older than ​`Doxygen <http://www.doxygen.org/>`_ and the documentation in the .h and .inl files was obviously not written with ​`Doxygen markup <http://www.stack.nl/~dimitri/doxygen/manual.html>`_. In 2007, `JoelSherrill <https://devel.rtems.org/wiki/TBR/User/JoelSherrill>`_ undertook to convert the documentation in the .h and .inl files in the RTEMS SuperCore? to Doxygen format. As a result of this effort, the Doxygen for the development version of the RTEMSSuperCore is now built automatically multiple times per day and made available on the RTEMS Website. In April 2008, `JoelSherrill <https://devel.rtems.org/wiki/TBR/User/JoelSherrill>`_ began to update the Classic API (e.g. cpukit/rtems) .h and .inl files to include `​Doxygen markup <http://www.stack.nl/~dimitri/doxygen/manual.html>`_.
